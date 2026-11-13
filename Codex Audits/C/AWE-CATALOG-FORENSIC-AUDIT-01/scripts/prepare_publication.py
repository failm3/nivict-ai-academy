"""Copy only audit deliverables into an isolated repository path; no deletion/moving."""
import argparse, hashlib, json, shutil
from pathlib import Path

EXCLUDED={"MANUS-INDEX.jsonl","SHA256SUMS","LOCAL-SHA256SUMS","GITHUB-PUBLICATION.json","ARCHIVE-CHECKSUM.json"}
def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--out",type=Path,required=True); ap.add_argument("--repo",type=Path,required=True); a=ap.parse_args()
    src=a.out.resolve(); repo=a.repo.resolve(); dest=repo/"Codex Audits/C/AWE-CATALOG-FORENSIC-AUDIT-01"
    if not dest.resolve().is_relative_to(repo): raise ValueError("destination_outside_isolated_repo")
    if not (repo/".git").is_dir(): raise ValueError("isolated_git_clone_required")
    files=[]
    for p in sorted(src.rglob("*")):
        if not p.is_file() or p.name in EXCLUDED or p.suffix in {".zip",".pyc"} or "__pycache__" in p.parts: continue
        rel=p.relative_to(src); target=dest/rel; target.parent.mkdir(parents=True,exist_ok=True); shutil.copy2(p,target); files.append(rel.as_posix())
    scope=dict(destination="Codex Audits/C/AWE-CATALOG-FORENSIC-AUDIT-01",included_files=files,excluded=["MANUS-INDEX.jsonl (full descriptions/post/author provenance remains local)","Original Manus ZIP, backup/database dump, bundle and full source caches (not in outputs)","Binary ZIPs, __pycache__, post-publication receipt"],scope="Public audit data; original NIVICT descriptions already from the public owning repository are preserved. Manus public index omits descriptions/claims/provenance.")
    for base in [src,dest]:
        (base/"PUBLICATION-SCOPE.json").write_text(json.dumps(scope,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print(json.dumps(dict(destination=str(dest),copied_files=len(files)),ensure_ascii=False))

if __name__=="__main__": main()
