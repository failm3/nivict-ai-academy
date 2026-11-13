"""Offline forensic inventory. Standard library only; never imports source code."""
import argparse, collections, csv, hashlib, html, ipaddress, json, re, subprocess
from pathlib import Path
from urllib.parse import urlsplit, urlunsplit, unquote

COMMIT = "5c611773bff3ccba76b78337534ed8944e137236"
DATA = "04 - Инструменты/Каталог кандидатов/90 - Данные"
REQUIRED = ["iirepresent.json", "Радар.json", "catalog-all-4504.csv", "all-records-classified.json", "validation-report.json", "issues.csv", "duplicates.csv", "import-manifest.json"]
NEEDS = {
 "orchestration": r"\bagent\b|агент|orchestrat|multi.?agent|recursive",
 "routing_context": r"router|routing|маршрутиз|tokeniz|compaction|context.window|litellm",
 "tools_mcp": r"\bmcp\b|model.context.protocol|tool.gateway",
 "memory": r"\brag\b|memory|памят|knowledge.graph|vector.database",
 "qa": r"\bevals?\b|benchmark|quality|тест|testing|adversarial|security.audit",
 "browser_vision": r"playwright|browser|браузер|computer.use|vision|screenshot",
 "coding": r"coding|code.agent|\bide\b|разработ|codebase|code.review|coding.assistant",
 "design": r"figma|design|дизайн|visual.regression",
 "communications": r"gmail|calendar|telegram|google.drive|email|почт|календар",
 "recovery": r"checkpoint|durable|temporal|backup|recovery|восстанов",
 "security_policy": r"secret|policy|sandbox|vault|безопас|security|isolation",
 "operator_ui": r"operator|console|dashboard|webui|интерфейс|панел",
 "observability": r"observability|tracing|langfuse|telemetry|мониторинг",
}

def sha(b): return hashlib.sha256(b).hexdigest()
def dump(p, obj):
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(obj, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")
def csvwrite(p, rows, fields=None):
    rows = list(rows)
    with p.open("w", encoding="utf-8", newline="") as f:
        w=csv.DictWriter(f, fieldnames=fields or list(rows[0])); w.writeheader(); w.writerows(rows)

def canonical(url):
    """Conservative resource URL: preserve case, path/query/fragment and www."""
    try:
        if re.search(r"[\x00-\x20\x7f]",url): return None
        u=urlsplit(url.strip()); host=(u.hostname or "").lower().encode("idna").decode()
        if u.scheme.lower() not in ("http","https") or not host: return None
        port=u.port
        host_out=f"[{host}]" if ":" in host else host
        authority=host_out if not port or (u.scheme.lower(),port) in [("https",443),("http",80)] else f"{host_out}:{port}"
        if u.username or u.password: return None
        return urlunsplit((u.scheme.lower(), authority, u.path or "/", u.query, u.fragment))
    except (ValueError,UnicodeError): return None

def entity(url):
    c=canonical(url)
    if not c: return None
    u=urlsplit(c); bits=u.path.strip("/").split("/")
    reserved={"topics","collections","marketplace","search","settings","orgs","users","login","features","sponsors","explore"}
    if u.hostname in ("github.com","www.github.com") and len(bits)>=2 and bits[0].lower() not in reserved:
        return "github:"+bits[0].lower()+"/"+bits[1].removesuffix(".git").lower()
    return "resource:"+c

def legacy(url, address=False):
    u=urlsplit(url); h=(u.hostname or "").lower().removeprefix("www.")
    path=unquote(u.path).lower().rstrip("/")
    return (h,path) if address else (u.scheme.lower(),h,path,u.query,u.fragment)

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--repo",type=Path,required=True); ap.add_argument("--out",type=Path,required=True); args=ap.parse_args()
    repo=args.repo.resolve(); out=args.out.resolve(); out.mkdir(parents=True,exist_ok=True)
    root=repo/DATA; notes=root.parent; evidence=out/"EVIDENCE"; evidence.mkdir(exist_ok=True)
    source_hashes=[]; mismatches=[]
    for name in REQUIRED:
        p=root/name; b=p.read_bytes(); rel=p.relative_to(repo).as_posix()
        blob=hashlib.sha1(b"blob "+str(len(b)).encode()+b"\0"+b).hexdigest()
        expected=subprocess.check_output(["git","rev-parse",f"{COMMIT}:{rel}"],cwd=repo,text=True).strip()
        source_hashes.append(dict(file=name,path=rel,bytes=len(b),sha256=sha(b),git_blob=blob,expected_git_blob=expected,blob_match=blob==expected,commit=COMMIT))
    dump(evidence/"SOURCE-MANIFEST.json",source_hashes)
    hashes={x["file"]:x["sha256"] for x in source_hashes}
    raw={n:json.loads((root/n).read_text(encoding="utf-8-sig")) for n in ["iirepresent.json","Радар.json"]}
    classified=json.loads((root/"all-records-classified.json").read_text(encoding="utf-8-sig"))
    imported=list(csv.DictReader((root/"catalog-all-4504.csv").open(encoding="utf-8-sig",newline="")))
    report=json.loads((root/"validation-report.json").read_text(encoding="utf-8-sig")); manifest=json.loads((root/"import-manifest.json").read_text(encoding="utf-8-sig"))
    byid=collections.defaultdict(list); csvid=collections.defaultdict(list)
    for x in classified: byid[x["id"]].append(x)
    for x in imported: csvid[x["id"]].append(x)
    records=[]
    for name,rows in raw.items():
        for i,r in enumerate(rows,1):
            sid=f"{Path(name).stem}-{i:04}"; url=r.get("link",""); desc=r.get("description","")
            problems=[]; derived=byid[sid][0] if len(byid[sid])==1 else {}
            if len(byid[sid])!=1: problems.append("CLASSIFIED_ID_CARDINALITY")
            if len(csvid[sid])!=1: problems.append("CSV_ID_CARDINALITY")
            for field,value in [("source",Path(name).stem),("source_row",i),("url",url),("description",desc)]:
                if derived.get(field)!=value: problems.append("CLASSIFIED_"+field.upper()+"_MISMATCH")
            for c in csvid[sid]:
                for key,val in derived.items():
                    # Existing exporter writes bools as Python True/False and null as empty.
                    if c.get(key)!=("" if val is None else str(val)): problems.append("CSV_"+key.upper()+"_MISMATCH")
            np=notes/derived.get("note_path","__missing__")
            text=np.read_text(encoding="utf-8") if np.is_file() else ""
            if not text: problems.append("NOTE_MISSING")
            else:
                fm=re.split(r"(?m)^---\s*$",text,maxsplit=2)[1] if text.startswith("---") else ""
                for key,val in [("id",sid),("source",Path(name).stem),("original_row",i),("url",url),("category",derived.get("category"))]:
                    m=re.search(r"^"+key+r":\s*(.*)$",fm,re.M)
                    got=m.group(1).strip() if m else None
                    if got and got.startswith('"'):
                        try: got=json.loads(got)
                        except ValueError: pass
                    if str(got)!=str(val): problems.append("NOTE_"+key.upper()+"_MISMATCH")
                # Every exact original description must occur after removing Markdown quote prefixes.
                if desc not in html.unescape(re.sub(r"(?m)^> ?", "", text)): problems.append("NOTE_DESCRIPTION_MISMATCH")
            for p in sorted(set(problems)): mismatches.append(dict(source_id=sid,issue=p,note_path=derived.get("note_path")))
            can=canonical(url); eid=entity(url); host=urlsplit(can).hostname if can else ""
            hints=[key for key,pat in NEEDS.items() if re.search(pat,url+" "+desc,re.I)]
            flags=["UNTRUSTED_DESCRIPTION","NOT_SECURITY_AUDITED"]
            if not can: flags.append("INVALID_OR_UNSAFE_URL")
            if url.startswith("http:"): flags.append("CLEARTEXT_HTTP")
            if re.search(r"(?i)ignore (all |previous )?instructions|system.prompt|игнорируй.*инструк|отключи.*провер",desc): flags.append("PROMPT_INJECTION_KEYWORD_REVIEW")
            if re.search(r"(?i)crack|stealer|ransomware|phishing|keylogger|bypass|взлом|пират",url+" "+desc): flags.append("DUAL_USE_KEYWORD_REVIEW")
            if re.search(r"(?i)\.(exe|msi|bat|ps1|apk|dmg|zip)(?:[?#]|$)",url): flags.append("DIRECT_DOWNLOAD_REVIEW")
            if re.search(r"(?i)\bgh[pousr]_[A-Za-z0-9]{20,}|\bsk-[A-Za-z0-9]{20,}|-----BEGIN .*PRIVATE KEY",desc+url): flags.append("POSSIBLE_SECRET_REVIEW")
            if derived.get("multi_service_description"): flags.append("DESCRIPTION_MULTIPLE_ENTITIES")
            resource_type="github_project_url_candidate" if eid and eid.startswith("github:") else "website_or_resource_unknown"
            if host in ["t.me","youtube.com","www.youtube.com","youtu.be","x.com","twitter.com"]: resource_type="post_channel_or_media_candidate"
            if host and (host.endswith("apps.apple.com") or host=="play.google.com"): resource_type="app_store_listing"
            if eid and eid.startswith("github:") and re.search(r"(?i)awesome|reference|curated|collection|cheatsheet|roadmap",eid+" "+desc[:160]): resource_type="repository_index_or_reference_candidate"
            records.append(dict(source_id=sid,source_file=name,source_row=i,source_sha=hashes[name],source_commit=COMMIT,original_url=url,canonical_url=can,entity_id=eid,duplicate_group=None,name=derived.get("title") or host or "UNKNOWN",original_description=desc,raw_record=r,resource_type=resource_type,categories=[derived.get("category","UNKNOWN")],capabilities=hints,architectural_needs=hints,confidence="LOW_RULE_BASED_UNVERIFIED",source_verification="SOURCE_PRESERVED" if not problems else "SOURCE_PRESERVED_WITH_DERIVATIVE_MISMATCH",external_verification="NOT_CHECKED",license_status="UNKNOWN",maintenance_status="UNKNOWN",security_flags=flags,integration_type="UNKNOWN",priority="P2" if hints else "P3",evidence_refs=[f"EVIDENCE/SOURCE-MANIFEST.json#{name}",f"{COMMIT}:{DATA}/{name}#/{i-1}"],checked_at="2026-11-12",blocking_reason="EXTERNAL_PRIMARY_SOURCE_NOT_REVIEWED",prior_classification=derived,note_path=derived.get("note_path"),note_sha256=sha(np.read_bytes()) if np.is_file() else None,source_issues=sorted(set(problems))))
    expected={f"{Path(n).stem}-{i:04}" for n,rs in raw.items() for i in range(1,len(rs)+1)}
    groups={}
    for label,keyfn in [("exact_url",lambda x:x["original_url"]),("conservative_url",lambda x:x["canonical_url"]),("project_or_resource",lambda x:x["entity_id"]),("legacy_full_url",lambda x:legacy(x["original_url"])),("legacy_host_path",lambda x:legacy(x["original_url"],True))]:
        g=collections.defaultdict(list)
        for r in records: g[keyfn(r)].append(r["source_id"])
        groups[label]=g
    dup_rows=[]
    for label,g in groups.items():
        for key,ids in g.items():
            if len(ids)>1:
                gid=label+":"+sha(str(key).encode())[:16]
                dup_rows.append(dict(kind=label,group_id=gid,key=str(key),count=len(ids),source_ids="|".join(ids),interpretation="SAME_GITHUB_PROJECT_NOT_NECESSARILY_SAME_RESOURCE" if label=="project_or_resource" and str(key).startswith("github:") else "CANDIDATE_ONLY" if label.startswith("legacy") else "DUPLICATE_RESOURCE_URL"))
    for r in records:
        if len(groups["conservative_url"][r["canonical_url"]])>1: r["duplicate_group"]="conservative_url:"+sha(str(r["canonical_url"]).encode())[:16]
    prior_dups=list(csv.DictReader((root/"duplicates.csv").open(encoding="utf-8-sig",newline="")))
    prior_issues=list(csv.DictReader((root/"issues.csv").open(encoding="utf-8-sig",newline="")))
    expected_issues=collections.Counter((x["id"],flag.strip(),x["url"]) for x in classified for flag in x["flags"].split(";") if flag.strip())
    # Discover actual flag delimiter from source rather than silently accepting a mismatch.
    if sum(expected_issues.values())!=len(prior_issues): expected_issues=collections.Counter((x["id"],flag.strip(),x["url"]) for x in classified for flag in re.split(r"[,;|]",x["flags"]) if flag.strip())
    actual_issues=collections.Counter((x["id"],x["issue"],x["url"]) for x in prior_issues)
    note_paths=list((notes/"20 - Записи").rglob("*.md")); note_ids={p.stem for p in note_paths}
    tests=dict(source_counts={n:len(rs) for n,rs in raw.items()},expected_total=4504,processed_total=len(records),processed_id_set_equal=expected=={x["source_id"] for x in records},processed_id_unique=len(records)==len({x["source_id"] for x in records}),classified_ids_equal=expected==set(byid),csv_ids_equal=expected==set(csvid),note_ids_equal=expected==note_ids,note_count=len(note_ids),all_git_blob_hashes_match=all(x["blob_match"] for x in source_hashes),reported_source_sha256_match=report["source_sha256"]=={n:hashes[n] for n in raw},manifest_counts_match=manifest["record_source_counts"]=={Path(n).stem:len(rs) for n,rs in raw.items()},issue_rows_match_classification_flags=actual_issues==expected_issues,prior_issue_rows=len(prior_issues),expected_issue_rows=sum(expected_issues.values()),derivative_mismatch_count=len(mismatches),unique_counts={k:len(g) for k,g in groups.items()},duplicate_extra_rows={k:sum(len(ids)-1 for ids in g.values()) for k,g in groups.items()},raw_record_key_shapes={n:dict(collections.Counter(",".join(sorted(r)) for r in rs)) for n,rs in raw.items()},prior_duplicate_rows=len(prior_dups))
    tests["note_file_count"]=len(note_paths)
    tests["note_ids_unique"]=len(note_paths)==len(note_ids)
    tests["historical_hashes_explained_by_crlf"]=all(sha((root/n).read_bytes().replace(b"\r\n",b"\n").replace(b"\n",b"\r\n"))==report["source_sha256"][n] for n in raw)
    dump(evidence/"LOCAL-RECONCILIATION.json",tests); dump(evidence/"DERIVATIVE-MISMATCHES.json",mismatches)
    dump(evidence/"PRIOR-REPORT.json",report); dump(evidence/"IMPORT-MANIFEST.json",manifest)
    csvwrite(out/"DUPLICATE-GROUPS.csv",dup_rows)
    with (out/"INVENTORY-ALL.jsonl").open("w",encoding="utf-8",newline="\n") as f:
        for r in records: f.write(json.dumps(r,ensure_ascii=False,separators=(",",":"))+"\n")
    def metric(rs):
        return dict(total=len(rs),processed=len(rs),classified_rule_based=len(rs),externally_verified=0,repo_inspected=0,license_verified=0,sandbox_tested=0,approved=0,integrated=0,unresolved=len(rs))
    coverage=dict(status="PARTIAL",source_commit=COMMIT,checked_at="2026-11-12",overall=metric(records),by_source={n:metric([r for r in records if r["source_file"]==n]) for n in raw},by_category={c:metric([r for r in records if c in r["categories"]]) for c in sorted({r["categories"][0] for r in records})},by_prior_confidence=dict(collections.Counter(x["confidence"] for x in classified)),field_coverage={k:dict(present=sum(k in r for r in records),nonempty=sum(r.get(k) not in (None,"",[]) for r in records),total=len(records)) for k in records[0]},security_flags=dict(collections.Counter(f for r in records for f in r["security_flags"])),resource_types=dict(collections.Counter(r["resource_type"] for r in records)),machine_checks=tests)
    dump(out/"COVERAGE.json",coverage)
    print(json.dumps(tests,ensure_ascii=False,indent=2)); print("security_flags",coverage["security_flags"])

if __name__=="__main__": main()
