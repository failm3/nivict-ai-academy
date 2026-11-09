#!/usr/bin/env python3
"""Create a third, locally staged AWE audit package from an existing frozen snapshot.

No runtime writes, no network, no Git operations and no automatic uploads.
Obvious secrets and personal addresses are redacted in selected first-party code
and log extracts. It still requires human review before any PUBLIC GitHub upload.
"""
from pathlib import Path
from collections import Counter
from datetime import datetime, timezone
import hashlib
import json
import re
import shutil
import sys
import zipfile

home=Path.home()
base=Path(sys.argv[1]).expanduser() if len(sys.argv)>1 else home/"awe-audit-export-20261109T144112Z"
private=base/"private-baseline-DO-NOT-PUBLISH"
candidate=base/"auditor-bundle-v2-REVIEW-BEFORE-UPLOAD"
reports=base/"reports"
target=base/"auditor-bundle-v3-REVIEW-BEFORE-UPLOAD"
required=[private,candidate,reports,reports/"v2-pending-review.json",reports/"v2-pruned-from-original.json"]
if not all(p.exists() for p in required):
    sys.exit("BLOCKED: missing prior export/v2 reports")
if target.exists():
    sys.exit("BLOCKED: v3 directory exists. Will not overwrite.")
target.mkdir(mode=0o700)
pending=json.loads((reports/"v2-pending-review.json").read_text())
pruned=json.loads((reports/"v2-pruned-from-original.json").read_text())
source_ext={".js",".mjs",".cjs",".jsx",".ts",".tsx",".py"}
log_ext={".log",".jsonl",".txt"}
EXCLUDE_PARTS={".private",".git",".ssh","node_modules"}
EXTERNAL_PARTS={"research","ai_agents_sources","t2_sources","sources"}
EMAIL=re.compile(r"(?<![A-Za-z0-9_.+\-])[A-Za-z0-9_.+\-]+@[A-Za-z0-9.\-]+\.[A-Za-z]{2,}")
TOKEN=re.compile(r"(?i)(?:sk-[A-Za-z0-9_\-]{15,}|gh[pousr]_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,}|AIza[A-Za-z0-9_\-]{25,}|AKIA[0-9A-Z]{16})")
PRIVATE_KEY=re.compile(r"-----BEGIN (?:OPENSSH |RSA |EC |DSA )?PRIVATE KEY-----")
BEARER=re.compile(r"(?i)(authorization[ \t]*:[ \t]*bearer[ \t]+)\S+")
SETTINGS=re.compile(r'(?i)((?:"|\\b)(?:api[_-]?key|access[_-]?token|refresh[_-]?token|client[_-]?secret|password|cookie|set-cookie)(?:"|\\b)\s*[:=]\s*["\x27]?)[^\s,"\x27}]{8,}')
URL_QUERY=re.compile(r"(?i)(https?://[^\s\"'<>()]+?)(?:[?&](?:token|key|secret|auth|session|code)=[^&\s\"'<>()]+)")
SMTP=re.compile(r"(?i)(smtp://|postgres(?:ql)?://)[^\s\"']+")
code_added=[]
evidence_added=[]
reject=[]
screen_paths=[]
copied=[]

def sha(p):
    h=hashlib.sha256()
    with p.open("rb") as f:
        for b in iter(lambda:f.read(1024*1024),b""):h.update(b)
    return h.hexdigest()
def valid_rel(s):
    p=Path(s)
    return bool(s) and not p.is_absolute() and ".." not in p.parts
def unsafe_path(p):
    return any(x in EXCLUDE_PARTS for x in p.parts)
def sanitized(text):
    counts={}
    for name,pattern,replacement in [
        ("emails",EMAIL,"auditor-redacted@example.invalid"),
        ("tokens",TOKEN,"[REDACTED-TOKEN]"),
        ("private_key",PRIVATE_KEY,"[REDACTED-PRIVATE-KEY-MARKER]"),
        ("bearer",BEARER,r"\1[REDACTED]"),
        ("password_or_credential",SETTINGS,r"\1[REDACTED]"),
        ("url_auth_parameters",URL_QUERY,r"\1?[REDACTED-AUTH-PARAM]"),
        ("credential_urls",SMTP,"[REDACTED-CREDENTIAL-URL]"),
    ]:
        text,n=pattern.subn(replacement,text)
        if n:counts[name]=n
    return text,counts
def add(src,rel,kind,redact=False):
    if not src.is_file() or src.is_symlink():
        reject.append({"path":rel.as_posix(),"reason":"not_regular_or_missing"});return
    if src.stat().st_size>4*1024*1024:
        reject.append({"path":rel.as_posix(),"reason":"size_over_4MB_for_text_screen"});return
    b=src.read_bytes()
    if b"\x00" in b:
        reject.append({"path":rel.as_posix(),"reason":"binary_no_auto_publish"});return
    try:
        t=b.decode("utf-8")
    except UnicodeDecodeError:
        reject.append({"path":rel.as_posix(),"reason":"non_utf8_no_auto_publish"});return
    dst=target/rel
    dst.parent.mkdir(parents=True,exist_ok=True)
    redactions={}
    if redact:
        t,redactions=sanitized(t)
    # Reject raw-looking secrets even after automated redaction; do not print values.
    if TOKEN.search(t) or PRIVATE_KEY.search(t) or BEARER.search(t) or SMTP.search(t):
        reject.append({"path":rel.as_posix(),"reason":"residual_credential_detector"});return
    # v2 files were not rescanned with this exact scanner: re-check all.
    if not redact and (EMAIL.search(t) or SETTINGS.search(t)):
        reject.append({"path":rel.as_posix(),"reason":"requires_redaction"});return
    dst.write_text(t,encoding="utf-8")
    meta={"path":rel.as_posix(),"original_sha256":sha(src),"published_sha256":sha(dst),"bytes":dst.stat().st_size,"source":kind,"redactions":redactions}
    copied.append(meta)
    if kind=="restored-code":
        code_added.append(meta)
    if kind=="sanitized-evidence":
        evidence_added.append(meta)

# Re-evaluate the 1067 v2 files; exclude hidden .private and sources scraped from third parties.
for p in sorted(candidate.rglob("*")):
    if not p.is_file():continue
    rel=p.relative_to(candidate)
    if unsafe_path(rel) or any(x in EXTERNAL_PARTS for x in rel.parts):
        reject.append({"path":rel.as_posix(),"reason":"sensitive_or_external_path"});continue
    if p.suffix.lower() in {".html",".svg",".pdf",".png",".jpg",".jpeg",".webp",".gif"}:
        # no automated upload of image/website cached contents; keep in private baseline.
        reject.append({"path":rel.as_posix(),"reason":"visual_or_html_manual_review"});continue
    add(p,rel,"v2-candidate",redact=False)

# Rescue source code that the first-pass scanner excluded on overbroad filename/email tests.
# Redaction changes these copies; original sha is retained for traceability.
for obj in pending:
    s=obj.get("path","")
    if not valid_rel(s):continue
    rel=Path(s)
    if not str(rel).startswith("AWE-RUNTIME/") or unsafe_path(rel) or rel.suffix.lower() not in source_ext:
        continue
    if any(x in EXTERNAL_PARTS for x in rel.parts):continue
    p=private/rel
    if (target/rel).is_file():continue
    add(p,rel,"restored-code",redact=True)

# Do not push raw external HTML, web crawls, body responses or provider billing snapshots.
# Create redacted copies of limited local execution logs, preserving source sha.
for obj in pruned:
    s=obj.get("path","")
    if not valid_rel(s):continue
    rel=Path(s)
    if unsafe_path(rel) or any(x in EXTERNAL_PARTS for x in rel.parts):continue
    if ("logs" not in rel.parts and "snapshots" not in rel.parts and "reports" not in rel.parts):
        continue
    if rel.suffix.lower() not in log_ext and not rel.name.startswith(("plan","final-")):
        continue
    if rel.name.startswith(("rc-","api_usage","token")):
        continue
    p=private/rel
    if not p.is_file():continue
    if (target/rel).is_file():continue
    add(p,rel,"sanitized-evidence",redact=True)

# Screenshots are NOT invented: inventory what exists in original snapshot.
for p in sorted(private.rglob("*")):
    if p.is_file() and p.suffix.lower() in {".png",".jpg",".jpeg",".webp",".gif"}:
        screen_paths.append(p.relative_to(private).as_posix())
manifest=[]
for p in sorted(target.rglob("*")):
    if p.is_file():
        manifest.append({"path":p.relative_to(target).as_posix(),"bytes":p.stat().st_size,"sha256":sha(p)})
metadata=target/"AUDIT-PACKAGE-METADATA"
metadata.mkdir()
(metadata/"COVERAGE.md").write_text(
    "# CAREER-01 · Пакет исходников и проверок\n\n"
    "Это обезличенная **кандидатная** копия, а не полный побайтовый baseline.\n"
    "Подлинные локальные файлы сохранены в private-baseline-DO-NOT-PUBLISH.\n"
    "Некоторые файлы были намеренно исключены или изменены ради конфиденциальности.\n"
    "Точные SHA-256 оригиналов содержатся в локальном отчёте v3-included-origin.json,\n"
    "а сырые логи и исходные материалы остаются доступны владельцу при отдельном\n"
    "согласовании безопасной передачи. Отсутствие файла не является доказательством\n"
    "отсутствия функциональности в реальной AWE. Запуск, тесты и публикация не проводились.\n\n"
    "Документы и история требований: https://github.com/failm3/nivict-ai-academy/tree/main/03%20-%20%D0%9F%D1%80%D0%B0%D0%BA%D1%82%D0%B8%D0%BA%D0%B0/05%20-%20AWE%20GROUP/AWE-CAREER-01-AUDIT-PACK-2026-11-09\n",
    encoding="utf-8"
)
zpath=base/"AWE-AUDIT-BUNDLE-v3-CANDIDATE.zip"
if zpath.exists(): sys.exit("BLOCKED: v3 ZIP exists. No overwrite.")
with zipfile.ZipFile(zpath,"w",compression=zipfile.ZIP_DEFLATED,compresslevel=6) as z:
    for p in sorted(target.rglob("*")):
        if p.is_file():z.write(p,p.relative_to(target))
with zipfile.ZipFile(zpath) as z:
    failed=z.testzip()
    if failed:sys.exit("ZIP verification failed")
result={
    "generated_utc":datetime.now(timezone.utc).isoformat(),
    "zip":str(zpath),"zip_bytes":zpath.stat().st_size,"zip_sha256":sha(zpath),
    "files_in_zip":len(manifest)+1,
    "restored_code":len(code_added),"sanitized_evidence":len(evidence_added),
    "still_excluded_or_review":len(reject),
    "screenshots_found_in_snapshot":len(screen_paths),
    "status":"CANDIDATE_REQUIRES_MANUAL_PRIVACY_AND_COMPLETENESS_REVIEW"
}
for name,body in [
    ("v3-summary.json",result),
    ("v3-included-origin.json",copied),
    ("v3-manifest.json",manifest),
    ("v3-exclusions.json",reject),
    ("v3-screenshots.json",screen_paths),
]:
    (reports/name).write_text(json.dumps(body,ensure_ascii=False,indent=2),encoding="utf-8")
print(json.dumps(result,ensure_ascii=False,indent=2))
print("NOTICE: No GitHub upload. Review archive and reports for secrets and omissions.")
