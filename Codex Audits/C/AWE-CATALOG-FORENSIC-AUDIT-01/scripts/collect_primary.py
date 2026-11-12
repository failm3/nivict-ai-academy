"""Optional pinned primary-text retrieval. Stores data only, no install/import/exec."""
import argparse, hashlib, json, time
from pathlib import Path
from urllib.request import Request, urlopen
from inventory import sha, dump

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--audit",type=Path,required=True); ap.add_argument("--cache",type=Path,required=True); a=ap.parse_args()
    docs=json.loads((a.audit/"EVIDENCE/PRIMARY-SOURCE-INDEX.json").read_text(encoding="utf-8")); reviews=json.loads((a.audit/"TECHNICAL-REVIEWS.json").read_text(encoding="utf-8"))
    for r in reviews:
        if not r["repo"]: continue
        e=dict(rank=r["rank"],repo=r["repo"],canonical_repo=r["canonical_repo"],need=r["need"],head=r["head"],checked_at="2026-11-12",metadata={},resources=[])
        for d in [d for d in docs if d["repo"]==r["canonical_repo"]]:
            url=d["url"].replace("https://github.com/","https://raw.githubusercontent.com/",1).replace("/blob/","/",1)
            if not url.startswith("https://raw.githubusercontent.com/"): raise ValueError("unexpected_source_host")
            b=None
            for attempt in range(3):
                try:
                    with urlopen(Request(url,headers={"User-Agent":"AWE-Forensic-Replay/1.0"}),timeout=20) as resp: b=resp.read(2_000_001)
                    if len(b)>2_000_000: raise ValueError("primary_text_too_large")
                    break
                except Exception:
                    if attempt==2: raise
                    time.sleep(2**attempt)
            blob=hashlib.sha1(b"blob "+str(len(b)).encode()+b"\0"+b).hexdigest()
            if sha(b)!=d["sha256"] or blob!=d["git_blob"]: raise ValueError("source_hash_mismatch:"+d["url"])
            e["resources"].append(dict(kind=d["kind"],url=d["url"],data=dict(content=b.decode("utf-8"),sha=blob,display_title=d["path"])))
        dump(a.cache/f"{r['rank']}.json",e)
    print("PINNED_PRIMARY_TEXT_HASHES_MATCH")

if __name__=="__main__": main()
