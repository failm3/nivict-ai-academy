import argparse, hashlib
from pathlib import Path

EXCLUDE={"SHA256SUMS","GITHUB-PUBLICATION.json","MANUS-INDEX.jsonl"}
def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--public",type=Path,required=True); ap.add_argument("--out",type=Path,required=True); a=ap.parse_args()
    lines=[]
    for p in sorted(a.public.rglob("*")):
        if p.is_file() and p.name not in EXCLUDE and p.suffix not in {".zip",".pyc"} and "__pycache__" not in p.parts:
            lines.append(hashlib.sha256(p.read_bytes()).hexdigest()+"  "+p.relative_to(a.public).as_posix())
    text="\n".join(lines)+"\n"
    (a.public/"SHA256SUMS").write_text(text,encoding="utf-8"); (a.out/"SHA256SUMS").write_text(text,encoding="utf-8")
    print("PUBLIC_FILES_HASHED",len(lines))

if __name__=="__main__": main()
