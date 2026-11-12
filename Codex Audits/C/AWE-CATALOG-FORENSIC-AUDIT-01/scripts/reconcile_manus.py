"""Read ZIP members as data only. No database restore or upstream code execution."""
import argparse, collections, csv, hashlib, json, zipfile
from pathlib import Path
from inventory import canonical, entity, dump, csvwrite, sha

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--archive",type=Path,required=True); ap.add_argument("--out",type=Path,required=True); ap.add_argument("--work",type=Path,required=True); args=ap.parse_args()
    out=args.out; work=args.work; work.mkdir(parents=True,exist_ok=True)
    z=zipfile.ZipFile(args.archive); prefix="awe-tool-intelligence/"
    members=[]
    for i in z.infolist():
        if not i.is_dir():
            b=z.read(i); members.append(dict(member=i.filename,bytes=len(b),sha256=sha(b)))
    dump(out/"EVIDENCE/MANUS-ARCHIVE-MANIFEST.json",dict(archive_name=args.archive.name,archive_sha256=sha(args.archive.read_bytes()),archive_bytes=args.archive.stat().st_size,members=members))
    # Only a bounded, explicit allowlist is materialized; never extractall.
    keep=["exports/research_registry.jsonl","exports/research_registry.json","exports/metrics.json","exports/approved_integration_registry.json","DELIVERY_MANIFEST-v2.json","transfer/backup/manifest.json","awe-tool-intelligence.bundle","awe_ti/registry.py","awe_ti/ingest.py","awe_ti/extraction.py","awe_ti/verification.py","awe_ti/exporting.py","awe_ti/intelligence.py","scripts/build_stack_records.py","scripts/register_verified_evidence.py","scripts/export_reports.py","CONTRACT.md","CORE_STATUS.md","DELIVERY_STATUS.md","TECHNICAL_SOURCES.md","OPERATIONS.md","README.md","research/live_stack_resources.jsonl"]
    for n in keep:
        p=work/n; p.parent.mkdir(parents=True,exist_ok=True); p.write_bytes(z.read(prefix+n))
    source=z.read(prefix+"exports/research_registry.jsonl")
    rows=[json.loads(x) for x in source.splitlines() if x.strip()]
    alternate=json.loads(z.read(prefix+"exports/research_registry.json"))
    dump(out/"EVIDENCE/MANUS-METRICS-ORIGINAL.json",json.loads(z.read(prefix+"exports/metrics.json")))
    metadata=json.loads(z.read(prefix+"DELIVERY_MANIFEST-v2.json")); bm=json.loads(z.read(prefix+"transfer/backup/manifest.json"))
    expected_bundle=metadata["files"]["awe-tool-intelligence-v2.bundle"]["sha256"]
    checks=dict(registry_rows=len(rows),registry_unique_ids=len({r["id"] for r in rows}),json_export_type=type(alternate).__name__,json_export_keys=list(alternate)[:10] if isinstance(alternate,dict) else None,bundle_hash_match=sha(z.read(prefix+"awe-tool-intelligence.bundle"))==expected_bundle,backup_hashes_match={n:sha(z.read(prefix+"transfer/backup/"+n))==h for n,h in bm["files"].items()},claimed_git_commit=metadata["git_commit"],registry_sha256=sha(source))
    other=alternate.get("resources",alternate.get("records")) if isinstance(alternate,dict) else alternate
    checks["json_jsonl_equal"]=rows==other
    index=[]
    for i,r in enumerate(rows,1):
        urls=[]
        for key in ("canonical_url","repository_url","official_url","url"):
            if isinstance(r.get(key),str) and r[key]: urls.append((key,r[key]))
        # Preserve field-level claims as additional, untrusted aliases; do not silently overwrite.
        claims=[c for c in r.get("claims",[]) if c.get("field") in ("repository_url","official_url") and isinstance(c.get("value"),str)]
        for c in claims:
            if c["value"].startswith(("https://","http://")): urls.append(("claim:"+c["field"],c["value"]))
        urls=list(dict.fromkeys(urls))
        desc=r.get("description")
        if not desc: desc=next((c["value"] for c in r.get("claims",[]) if c.get("field")=="description"),None)
        index.append(dict(manus_id=r["id"],source_row=i,source_sha256=checks["registry_sha256"],name=r.get("name"),stage=r.get("stage"),description=desc,urls=[dict(field=k,url=v,canonical_url=canonical(v),entity_id=entity(v)) for k,v in urls],approved_for_export=r.get("approved_for_export"),approval_count=len(r.get("approvals",[])),verification_runs_count=len(r.get("verification_runs",[])),independent_verification="NOT_CHECKED",provenance=r.get("provenance",[]),raw_record_sha256=sha(json.dumps(r,ensure_ascii=False,sort_keys=True,separators=(",",":")).encode())))
    with (out/"MANUS-INDEX.jsonl").open("w",encoding="utf-8") as f:
        for r in index: f.write(json.dumps(r,ensure_ascii=False,separators=(",",":"))+"\n")
    checks["stages"]=dict(collections.Counter(r["stage"] for r in index)); checks["approved_for_export"]=sum(bool(r["approved_for_export"]) for r in index)
    checks["nested_rows"]={k:sum(len(r.get(k,[])) for r in rows) for k in ["claims","provenance","versions","verification_runs","live_tests","approvals","integration_specs","license_evidence"]}
    checks["missing_urls"]=sum(not r["urls"] for r in index)
    records=[json.loads(x) for x in (out/"INVENTORY-ALL.jsonl").read_text(encoding="utf-8").splitlines()]
    maps={key:collections.defaultdict(set) for key in ["exact","canonical","entity"]}
    for r in index:
        for u in r["urls"]:
            for k,v in [("exact",u["url"]),("canonical",u["canonical_url"]),("entity",u["entity_id"])]:
                if v: maps[k][v].add(r["manus_id"])
    cross=[]; matched=set(); basis_counts=collections.Counter()
    for r in records:
        levels=[("exact",r["original_url"]),("canonical",r["canonical_url"]),("entity",r["entity_id"])]
        basis="NO_STABLE_ID_MATCH"; ids=set()
        for k,v in levels:
            if v and maps[k].get(v): basis=k; ids=maps[k][v]; break
        matched.update(ids); basis_counts[basis]+=1
        related=[m for m in index if m["manus_id"] in ids]
        relation="EXACT_TEXT_SAME" if related and all(m["description"]==r["original_description"] for m in related) else "TEXT_DIFFERENT_NOT_A_CONTRADICTION_PROOF" if related else "NOT_APPLICABLE"
        fields=sorted({u["field"] for m in related for u in m["urls"] if (u["url"]==r["original_url"] if basis=="exact" else u["canonical_url"]==r["canonical_url"] if basis=="canonical" else u["entity_id"]==r["entity_id"])})
        cross.append(dict(nivict_id=r["source_id"],nivict_url=r["original_url"],entity_id=r["entity_id"],manus_ids="|".join(map(str,sorted(ids))),match_basis=basis,matched_url_fields="|".join(fields),description_relation=relation,semantic_contradiction_review="NOT_DONE",interpretation="POSSIBLE_SHARED_PROJECT" if basis=="entity" else "SHARED_URL" if ids else "NIVICT_ONLY_UNDER_MATCH_RULES",working_awe_12_membership="UNKNOWN_NO_LIVE_SNAPSHOT"))
    for m in index:
        if m["manus_id"] not in matched:
            cross.append(dict(nivict_id="",nivict_url="",entity_id="|".join(sorted({u["entity_id"] for u in m["urls"] if u["entity_id"]})),manus_ids=m["manus_id"],match_basis="MANUS_ONLY_UNDER_MATCH_RULES",matched_url_fields="",description_relation="NOT_APPLICABLE",semantic_contradiction_review="NOT_DONE",interpretation="NOT_A_NEW_UNIQUE_PROJECT_CLAIM",working_awe_12_membership="UNKNOWN_NO_LIVE_SNAPSHOT"))
    csvwrite(out/"DEDUP-RECONCILIATION.csv",cross)
    checks["overlap_nivict_rows_by_basis"]=dict(basis_counts); checks["matched_manus_rows"]=len(matched); checks["unmatched_manus_rows"]=len(index)-len(matched)
    checks["nivict_entity_keys"]=len({r["entity_id"] for r in records}); checks["manus_entity_keys"]=len(maps["entity"])
    checks["intersection_entity_keys"]=len({r["entity_id"] for r in records}&set(maps["entity"]))
    checks["description_relations_nivict_rows"]=dict(collections.Counter(x["description_relation"] for x in cross if x["nivict_id"]))
    dump(out/"EVIDENCE/MANUS-RECONCILIATION.json",checks)
    print(json.dumps(checks,ensure_ascii=False,indent=2),flush=True)
    print("first_record_fields",list(rows[0]),flush=True)

if __name__=="__main__": main()
