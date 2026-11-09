#!/usr/bin/env python3
"""Read-only evidence packager for AWE GROUP audit. No network, Git writes or DB access."""
import datetime as dt
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import zipfile
from pathlib import Path

HOME = Path.home()
RUNTIME = HOME / "awe-e1-live-runtime"
LEVEL2 = HOME / "awe-level2-observation"
MAX_FILE = 300 * 1024 * 1024
BLOCK_DIR = {".git", "node_modules", ".venv", "venv", "__pycache__", ".cache", ".npm", ".pnpm-store"}
SKIP_SHARE_EXT = {".db", ".sqlite", ".sqlite3", ".pem", ".p12", ".pfx", ".key", ".kdbx", ".env", ".zip", ".tar", ".gz", ".7z", ".bak"}
IMAGE_EXT = {".png", ".jpg", ".jpeg", ".webp", ".gif", ".svg", ".pdf"}
SENSITIVE_PATH = re.compile(r"(^|/)(\.env[^/]*|\.ssh|\.aws|\.config/(gh|opencode)|credentials(?:\.[^/]*)?|id_(rsa|ed25519).*|[^/]*(?:secret|token|api[-_]?key|password|cookie|session)[^/]*)($|/)", re.I)
SECRET_VALUE = [
    re.compile(rb"(?i)(?:sk-[a-z0-9_-]{15,}|gh[pousr]_[a-z0-9]{20,}|github_pat_[a-z0-9_]{20,}|AIza[a-z0-9_-]{25,}|AKIA[0-9A-Z]{16})"),
    re.compile(rb"(?i)(?:authorization[ \t]*:[ \t]*bearer[ \t]+[a-z0-9._~+/=-]{12,})"),
    re.compile(rb"(?i)(?:api[_-]?key|access[_-]?token|client[_-]?secret|password)\s*[:=]\s*[\"'][^\"'\r\n]{8,}[\"']"),
    re.compile(rb"-----BEGIN (?:OPENSSH |RSA |EC |DSA )?PRIVATE KEY-----"),
]
PRIVATE_DATA = re.compile(rb"\b[A-Za-z0-9.+_-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b")
ALLOWED_EMAIL_DOMAINS = {b"example.com", b"example.org", b"example.net", b"test.com", b"localhost"}
FILES = []
EXCLUDED = []
PRIVATE_COPIES = []
MISSING = []

def sha256(p):
    h = hashlib.sha256()
    with p.open("rb") as f:
        for b in iter(lambda: f.read(1024 * 1024), b""):
            h.update(b)
    return h.hexdigest()

def git_lines(args):
    try:
        r = subprocess.run(["git", "-C", str(RUNTIME), *args], stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, timeout=15, check=False)
        return r.stdout.decode("utf-8", "replace")
    except Exception:
        return "UNAVAILABLE\n"

def sensitive_content(path):
    # Binary files and screenshots cannot be confidently checked via text scan.
    if path.suffix.lower() in IMAGE_EXT:
        return "VISUAL_REVIEW"
    try:
        with path.open("rb") as f:
            data = f.read()
            if len(data) > 2 * 1024 * 1024:
                return "LARGE_REVIEW"
        if b"\x00" in data:
            return "BINARY_REVIEW"
        for pat in SECRET_VALUE:
            if pat.search(data):
                return "SECRET_PATTERN_REVIEW"
        # Personal email addresses can occur in fixture logs; require review.
        for m in PRIVATE_DATA.finditer(data):
            if m.group().rsplit(b"@", 1)[-1].lower() not in ALLOWED_EMAIL_DOMAINS:
                return "EMAIL_REVIEW"
        return None
    except Exception:
        return "UNREADABLE_REVIEW"

def collect(source, prefix, local_out, share_out):
    if not source.is_dir():
        MISSING.append(str(source))
        return
    for base, dirs, files in os.walk(source, topdown=True, followlinks=False):
        root = Path(base)
        dirs[:] = [d for d in sorted(dirs) if d not in BLOCK_DIR and not (root / d).is_symlink()]
        for filename in sorted(files):
            orig = root / filename
            if not orig.is_file() or orig.is_symlink():
                EXCLUDED.append({"path": str(orig), "reason": "symlink/nonregular"})
                continue
            rel = Path(prefix) / orig.relative_to(source)
            try:
                sz = orig.stat().st_size
                if sz > MAX_FILE:
                    EXCLUDED.append({"path": str(rel), "reason": "file_300MB_plus_local_only"})
                    continue
                raw_dest = local_out / rel
                raw_dest.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(orig, raw_dest)
                PRIVATE_COPIES.append({"path": str(rel), "size": sz, "sha256": sha256(raw_dest)})
                norm = "/" + rel.as_posix()
                reason = None
                if SENSITIVE_PATH.search(norm):
                    reason = "sensitive_path_review"
                elif orig.suffix.lower() in SKIP_SHARE_EXT:
                    reason = "archive_database_or_key_review"
                else:
                    reason = sensitive_content(raw_dest)
                if reason:
                    EXCLUDED.append({"path": str(rel), "reason": reason})
                else:
                    dst = share_out / rel
                    dst.parent.mkdir(parents=True, exist_ok=True)
                    shutil.copy2(raw_dest, dst)
                    FILES.append({"path": str(rel), "size": sz, "sha256": sha256(dst)})
            except Exception as e:
                EXCLUDED.append({"path": str(rel), "reason": "copy_error_" + type(e).__name__})

def main():
    if not RUNTIME.is_dir():
        print("BLOCKED: AWE runtime directory missing:", RUNTIME)
        return 2
    timestamp = dt.datetime.now(dt.timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    base = HOME / ("awe-audit-export-" + timestamp)
    base.mkdir(mode=0o700)
    local = base / "private-baseline-DO-NOT-PUBLISH"
    share = base / "auditor-bundle-REVIEW-BEFORE-UPLOAD"
    report = base / "reports"
    for d in [local, share, report]:
        d.mkdir(mode=0o700)
    (report / "git-head.txt").write_text(git_lines(["rev-parse", "HEAD"]))
    (report / "git-branch.txt").write_text(git_lines(["branch", "--show-current"]))
    (report / "git-status.txt").write_text(git_lines(["status", "--porcelain=v1", "-uall"]))
    (report / "git-diff-stat.txt").write_text(git_lines(["diff", "--stat"]))
    collect(RUNTIME, "AWE-RUNTIME", local, share)
    collect(LEVEL2, "LEVEL2-OBSERVATION", local, share)
    (report / "private-manifest.json").write_text(json.dumps(PRIVATE_COPIES, indent=2, ensure_ascii=False))
    (report / "public-candidate-manifest.json").write_text(json.dumps(FILES, indent=2, ensure_ascii=False))
    (report / "requires-manual-review.json").write_text(json.dumps(EXCLUDED, indent=2, ensure_ascii=False))
    (report / "missing-inputs.json").write_text(json.dumps(MISSING, indent=2, ensure_ascii=False))
    note = """# AWE GROUP — Auditor Bundle (local staging)
Status: CANDIDATE ONLY. Do not publish until manually reviewed.
For complete mission requirements and archive index see:
https://github.com/failm3/nivict-ai-academy/tree/main/03%20-%20%D0%9F%D1%80%D0%B0%D0%BA%D1%82%D0%B8%D0%BA%D0%B0/05%20-%20AWE%20GROUP/AWE-CAREER-01-AUDIT-PACK-2026-11-09

This package excludes sensitive paths, suspected secrets, screenshots, PDFs,
archives, databases and files requiring review. Inspect reports next to archive.
The snapshot is not guaranteed consistent if live processes modified files.
"""
    (share / "README.md").write_text(note)
    archive = base / "AWE-AUDIT-BUNDLE-CANDIDATE.zip"
    with zipfile.ZipFile(archive, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=6, allowZip64=True) as z:
        for p in sorted(share.rglob("*")):
            if p.is_file():
                z.write(p, p.relative_to(share))
    zipped = [{"name": "AWE-AUDIT-BUNDLE-CANDIDATE.zip", "bytes": archive.stat().st_size, "sha256": sha256(archive)}]
    # Segment large archives for GitHub Git <=100 MiB/file; avoid files larger than 40 MiB.
    if archive.stat().st_size > 40 * 1024 * 1024:
        partsdir = base / "GITHUB-PARTS-REVIEW-BEFORE-UPLOAD"
        partsdir.mkdir()
        with archive.open("rb") as f:
            count = 0
            while True:
                b = f.read(40 * 1024 * 1024)
                if not b:
                    break
                count += 1
                part = partsdir / f"AWE-AUDIT-BUNDLE-CANDIDATE.zip.part{count:03d}"
                part.write_bytes(b)
                zipped.append({"name": part.name, "bytes": len(b), "sha256": sha256(part)})
    (report / "archives-sha256.json").write_text(json.dumps(zipped, indent=2))
    (report / "README.md").write_text(
        f"# Local AWE audit export\n\nPrivate baseline: {local}\n\n"
        f"Share candidate: {share}\n\nArchive: {archive}\n\n"
        f"Share files: {len(FILES)}\nPrivate files: {len(PRIVATE_COPIES)}\n"
        f"Review/excluded: {len(EXCLUDED)}\nMissing inputs: {len(MISSING)}\n\n"
        "Do not upload anything before manual review of the archive, files, screenshots,\n"
        "logs and exclusions. This script never contacts GitHub, changes AWE or validates\n"
        "whether its source tree changed concurrently during the snapshot.\n"
    )
    os.chmod(archive, 0o600)
    print("EXPORT CANDIDATE:", base)
    print("PRIVATE FILES:", len(PRIVATE_COPIES), "SHARE CANDIDATES:", len(FILES))
    print("REVIEW/EXCLUDED:", len(EXCLUDED), "MISSING:", len(MISSING))
    print("ZIP SIZE:", archive.stat().st_size, "SHA256:", sha256(archive))
    print("NO GITHUB UPLOAD PERFORMED; screenshots/PDFs and secret candidates require review.")
    return 0

if __name__ == "__main__":
    sys.exit(main())
