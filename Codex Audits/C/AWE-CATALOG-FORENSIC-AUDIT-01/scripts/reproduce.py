"""Offline replay with captured observations; never represents a new online check."""
import argparse, shutil, subprocess, sys
from pathlib import Path

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--audit",type=Path,required=True); ap.add_argument("--repo",type=Path,required=True); ap.add_argument("--archive",type=Path,required=True); ap.add_argument("--target",type=Path,required=True); a=ap.parse_args()
    if a.target.exists() and any(a.target.iterdir()): raise ValueError("target_must_be_new_or_empty")
    a.target.mkdir(parents=True,exist_ok=True)
    for d in ["EVIDENCE","QA"]: shutil.copytree(a.audit/d,a.target/d,dirs_exist_ok=True)
    shutil.copy2(a.audit/"TECHNICAL-REVIEWS.json",a.target/"TECHNICAL-REVIEWS.json")
    here=Path(__file__).resolve().parent
    def run(name,*args): subprocess.run([sys.executable,"-X","utf8",str(here/name),*map(str,args)],check=True)
    run("inventory.py","--repo",a.repo,"--out",a.target)
    run("reconcile_manus.py","--archive",a.archive,"--out",a.target,"--work",a.target/"scratch-manus")
    run("context_evidence.py","--repo",a.repo,"--out",a.target)
    run("enrich.py","--out",a.target)
    run("validate_delivery.py","--repo",a.repo,"--out",a.target)
    equal={n:(a.audit/n).read_bytes()==(a.target/n).read_bytes() for n in ["INVENTORY-ALL.jsonl","COVERAGE.json","DEDUP-RECONCILIATION.csv","DUPLICATE-GROUPS.csv","CONTINUATION-QUEUE.csv"]}
    print("CAPTURED_EVIDENCE_REPLAY_BYTE_EQUAL",equal)
    if not all(equal.values()): raise SystemExit(1)

if __name__=="__main__": main()
