"""Bounded, unauthenticated HEAD requests. Never executes JS or downloads programs."""
import argparse, concurrent.futures, datetime, hashlib, ipaddress, json, socket, threading, time
from pathlib import Path
from urllib.parse import urlsplit, urlunsplit
from urllib.request import Request, build_opener, HTTPRedirectHandler
from urllib.error import HTTPError

def safe(url):
    u=urlsplit(url)
    if u.scheme not in ("http","https") or not u.hostname or u.username or u.password: raise ValueError("unsafe_scheme_or_authority")
    if u.port and u.port not in (80,443): raise ValueError("nonstandard_port_not_checked")
    ips={r[4][0] for r in socket.getaddrinfo(u.hostname,u.port or (443 if u.scheme=="https" else 80),type=socket.SOCK_STREAM)}
    if not ips or any(not ipaddress.ip_address(ip).is_global for ip in ips): raise ValueError("nonpublic_dns_not_checked")

class Redirects(HTTPRedirectHandler):
    max_redirections=4
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        safe(newurl)
        return Request(newurl,method="HEAD",headers={"User-Agent":"AWE-Catalog-Forensic-Audit/1.0 (read-only HEAD)"})

locks={}; lock=threading.Lock()
def probe(url):
    host=urlsplit(url).hostname
    with lock: sem=locks.setdefault(host,threading.Semaphore(2))
    with sem:
        result={"url":url,"checked_at":datetime.datetime.now(datetime.timezone.utc).isoformat(),"method":"HEAD","authentication":"NONE","body_read":False}
        for attempt in range(1,3):
            try:
                safe(url)
                with build_opener(Redirects()).open(Request(url,method="HEAD",headers={"User-Agent":"AWE-Catalog-Forensic-Audit/1.0 (read-only HEAD)"}),timeout=7) as r:
                    final=r.url; u=urlsplit(final)
                    # Redirect queries may contain ephemeral state: do not publish their values.
                    result.update(status="HTTP_RESPONSE_OBSERVED",http_status=r.status,final_url=urlunsplit((u.scheme,u.netloc,u.path,"","")),redirect_query_sha256=hashlib.sha256(u.query.encode()).hexdigest() if u.query else None,redirected=final!=url,content_type=r.headers.get("Content-Type"),attempts=attempt)
                    return result
            except HTTPError as e:
                result.update(status="HTTP_ERROR_OBSERVED",http_status=e.code,attempts=attempt)
                if e.code not in (429,500,502,503,504) or attempt==2: return result
            except Exception as e:
                result.update(status="NETWORK_OR_POLICY_UNKNOWN",error_type=type(e).__name__,reason=str(e)[:250],attempts=attempt)
                if isinstance(e,ValueError) or attempt==2: return result
            time.sleep(attempt)
        return result

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--out",type=Path,required=True); ap.add_argument("--limit",type=int,default=100000); ap.add_argument("--workers",type=int,default=12); args=ap.parse_args()
    records=[json.loads(x) for x in (args.out/"INVENTORY-ALL.jsonl").read_text(encoding="utf-8").splitlines()]
    urls=sorted({r["original_url"] for r in records if not r["entity_id"].startswith("github:")})
    dest=args.out/"EVIDENCE/URL-RESPONSES.jsonl"
    cached={json.loads(x)["url"] for x in dest.read_text(encoding="utf-8").splitlines()} if dest.exists() else set()
    todo=[u for u in urls if u not in cached][:args.limit]
    print(json.dumps({"total_distinct_non_github_urls":len(urls),"cached":len(cached),"to_check":len(todo)}),flush=True)
    with dest.open("a",encoding="utf-8") as f, concurrent.futures.ThreadPoolExecutor(max_workers=args.workers) as pool:
        for i,r in enumerate(pool.map(probe,todo),1):
            f.write(json.dumps(r,ensure_ascii=False)+"\n"); f.flush()
            if i%50==0: print(json.dumps({"completed_this_run":i,"total_saved":len(cached)+i}),flush=True)
    print("HEAD_BATCH_FINISHED",flush=True)

if __name__=="__main__": main()
