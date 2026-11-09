#!/usr/bin/env python3
"""Second-pass safe triage of AWE audit export. Only modifies export staging, never runtime."""
from pathlib import Path
from collections import Counter
import datetime as dt
import hashlib
import json
import re
import shutil
import sys
import zipfile

HOME = Path.home()
base_candidates=sorted(HOME.glob("awe-audit-export-*"), reverse=True)
base=Path(sys.argv[1]).expanduser() if len(sys.argv)>1 else (base_candidates[0] if base_candidates else None)
if not base or not base.is_dir():
    sys.exit("BLOCKED: prior export directory missing")
private=base/"private-baseline-DO-NOT-PUBLISH"
original=base/"auditor-bundle-REVIEW-BEFORE-UPLOAD"
reports=base/"reports"
out=base/"auditor-bundle-v2-REVIEW-BEFORE-UPLOAD"
manifest=reports/"requires-manual-review.json"
if not all(p.exists() for p in (private, original, reports, manifest)):
    sys.exit("BLOCKED: missing previously generated input in "+str(base))
if out.exists():
    sys.exit("BLOCKED: v2 output exists. No overwrite performed: "+str(out))
excluded=json.loads(manifest.read_text(encoding="utf-8"))
if not isinstance(excluded,list):
    sys.exit("BLOCKED: unexpected exclusions manifest format")
out.mkdir(mode=0o700)
CODE_EXT={".mjs",".cjs",".js",".jsx",".ts",".tsx",".py"}
DATA_EXT={".html",".htm",".json",".jsonl",".txt",".body",".log",".csv"}
EMAIL=re.compile(rb"(?<![A-Za-z0-9_.+\-])([A-Za-z0-9_.+\-]+)@([A-Za-z0-9.-]+\.[A-Za-z]{2,})(?![A-Za-z0-9.-])")
SAFE_DOMAINS={b"example.com",b"example.org",b"example.net",b"test.com",b"test.invalid",b"example.invalid",b"localhost.test",b"mail.test"}
SECRET_PATTERNS=[
 re.compile(rb"(?i)\b(?:sk-[a-z0-9_-]{15,}|gh[pousr]_[a-z0-9]{20,}|github_pat_[a-z0-9_]{20,}|AIza[a-z0-9_-]{25,}|AKIA[0-9A-Z]{16})"),
 re.compile(rb"(?i)(?:authorization\s*:\s*bearer\s+\S{12,})"),
 re.compile(rb"-----BEGIN (?:OPENSSH |RSA |EC |DSA )?PRIVATE KEY-----"),
 re.compile(rb"(?i)(?:api[_-]?key|access[_-]?token|client[_-]?secret|password)\s*[:=]\s*[\"'][^\"'\r\n]{8,}[\"']"),
]
# Never send source code or match values to ChatGPT as part of this local screening.
def classify(path, rel):
    if path.stat().st_size > 2*1024*1024: return "TOO_LARGE_FOR_SCREENING"
    b=path.read_bytes()
    if b"\x00" in b: return "BINARY"
    if any(p.search(b) for p in SECRET_PATTERNS): return "SECRET_PATTERN"
    domains={m.group(2).lower() for m in EMAIL.finditer(b)}
    if domains-SAFE_DOMAINS: return "PERSONAL_OR_EXTERNAL_EMAIL"
    # Extra gate: never publish cached web/third party data automatically.
    parts=rel.parts
    if "research" in parts or "sources" in parts or "t2_sources" in parts or "snapshots" in parts:
        return "THIRD_PARTY_OR_PROVIDER_DATA"
    return "ALLOW"
def valid_rel(raw):
    p=Path(raw)
    return bool(p.parts) and not p.is_absolute() and ".." not in p.parts
def sha(p):
    h=hashlib.sha256()
    with p.open("rb") as f:
        for b in iter(lambda:f.read(1024*1024),b""): h.update(b)
    return h.hexdigest()
# Start with existing candidate but prune raw third party downloads, logs that need separate review,
# snapshots carrying provider responses, and other likely-to-contain private network contents.
pruned=[]
for p in sorted(original.rglob("*")):
    if not p.is_file():continue
    rel=p.relative_to(original)
    s=rel.as_posix().lower()
    # Keep project source even if website HTML; drop cached research/evidence.
    is_external_cache=("/research/" in "/"+s+"/" or "/sources/" in "/"+s+"/" or "/t2_sources/" in "/"+s+"/")
    provider_data=("/snapshots/rc-" in "/"+s or "/logs/" in "/"+s or p.suffix.lower() in {".body",".jsonl"})
    if is_external_cache or provider_data:
        pruned.append({"path":str(rel),"reason":"THIRD_PARTY_OR_LOG_REVIEW"})
        continue
    dest=out/rel
    dest.parent.mkdir(parents=True,exist_ok=True)
    shutil.copy2(p,dest)
restored=[]
pending=[]
for entry in excluded:
    raw=entry.get("path","")
    reason=entry.get("reason","UNKNOWN")
    if not valid_rel(raw):
        pending.append({"path":raw,"reason":"INVALID_PATH"});continue
    rel=Path(raw)
    original_file=private/rel
    if not original_file.is_file():
        pending.append({"path":raw,"reason":"MISSING_PRIVATE_COPY"});continue
    # Only restore first-party source, never private directories or provider data.
    is_first_party_code=rel.suffix.lower() in CODE_EXT and (str(rel).startswith("AWE-RUNTIME/")) and ("research" not in rel.parts)
    # Filename classifier was overbroad for *session* or *secret* filenames, but content still reviewed.
    if is_first_party_code:
        status=classify(original_file,rel)
        if status=="ALLOW":
            dest=out/rel
            dest.parent.mkdir(parents=True,exist_ok=True)
            shutil.copy2(original_file,dest)
            restored.append(str(rel))
            continue
        pending.append({"path":raw,"reason":status,"original_reason":reason})
    else:
        pending.append({"path":raw,"reason":reason})
# Verify destination copies, make list of release candidates and relevant review reports.
inventory=[]
for p in sorted(out.rglob("*")):
    if p.is_file():
        inventory.append({"path":p.relative_to(out).as_posix(),"bytes":p.stat().st_size,"sha256":sha(p)})
(r := reports/"v2-restored-first-party-code.json").write_text(json.dumps(restored,ensure_ascii=False,indent=2))
(reports/"v2-pending-review.json").write_text(json.dumps(pending,ensure_ascii=False,indent=2))
(reports/"v2-pruned-from-original.json").write_text(json.dumps(pruned,ensure_ascii=False,indent=2))
(reports/"v2-file-manifest.json").write_text(json.dumps(inventory,ensure_ascii=False,indent=2))
zpath=base/"AWE-AUDIT-BUNDLE-v2-CANDIDATE.zip"
with zipfile.ZipFile(zpath,"w",compression=zipfile.ZIP_DEFLATED,compresslevel=6,allowZip64=True) as z:
    for p in sorted(out.rglob("*")):
        if p.is_file():z.write(p,p.relative_to(out))
with zipfile.ZipFile(zpath) as z:
    bad=z.testzip()
    if bad:sys.exit("ZIP CORRUPT at "+bad)
sha_out=sha(zpath)
(reports/"v2-ZIP-sha256.txt").write_text(sha_out+"  "+zpath.name+"\n")
screenshots=[p for p in private.rglob("*") if p.is_file() and p.suffix.lower() in {".png",".jpg",".jpeg",".webp",".gif"}]
(reports/"v2-screenshot-paths-local-review.json").write_text(json.dumps([str(p.relative_to(private)) for p in screenshots],ensure_ascii=False,indent=2))
print("V2 EXPORT:",base)
print("FILES IN V2 ZIP:",len(inventory))
print("FIRST PARTY CODE FILES RESTORED:",len(restored))
print("PENDING REVIEW:",len(pending))
print("PRUNED EXTERNAL/LOG CACHE:",len(pruned))
print("EXISTING SCREENSHOT CANDIDATES:",len(screenshots))
print("ZIP:",zpath)
print("ZIP BYTES:",zpath.stat().st_size)
print("ZIP SHA256:",sha_out)
print("STATUS: CANDIDATE ONLY. Do not upload to public GitHub until reviewed.")
