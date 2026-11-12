"""Validation from raw inputs and evidence, never imports or executes upstream source."""
import argparse, collections, hashlib, json
from pathlib import Path
from inventory import dump, REQUIRED

FIELDS="source_id source_file source_row source_sha original_url canonical_url entity_id duplicate_group name original_description resource_type categories capabilities architectural_needs confidence source_verification external_verification license_status maintenance_status security_flags integration_type priority evidence_refs checked_at blocking_reason".split()

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--repo",type=Path,required=True); ap.add_argument("--out",type=Path,required=True); a=ap.parse_args(); out=a.out
    data=a.repo/"04 - Инструменты/Каталог кандидатов/90 - Данные"
    rows=[json.loads(x) for x in (out/"INVENTORY-ALL.jsonl").read_text(encoding="utf-8").splitlines()]
    raw={n:json.loads((data/n).read_text(encoding="utf-8-sig")) for n in ("iirepresent.json","Радар.json")}
    raw_hashes={n:hashlib.sha256((data/n).read_bytes()).hexdigest() for n in raw}
    original={f"{Path(n).stem}-{i:04}":(n,i,r) for n,rs in raw.items() for i,r in enumerate(rs,1)}
    errors=[]
    for r in rows:
        if r["source_id"] not in original: errors.append("UNKNOWN_ID:"+r["source_id"]); continue
        n,i,orig=original[r["source_id"]]
        for ok,label in [(r["source_file"]==n,"FILE"),(r["source_row"]==i,"ROW"),(r["raw_record"]==orig,"RAW"),(r["original_url"]==orig["link"],"URL"),(r["original_description"]==orig["description"],"DESCRIPTION"),(r["source_sha"]==raw_hashes[n],"SOURCE_SHA")]:
            if not ok: errors.append(label+":"+r["source_id"])
    coverage=json.loads((out/"COVERAGE.json").read_text(encoding="utf-8")); reviews=json.loads((out/"TECHNICAL-REVIEWS.json").read_text(encoding="utf-8"))
    link=json.loads((out/"EVIDENCE/OBSIDIAN-LINK-CHECK.json").read_text(encoding="utf-8"))
    batches=[r for p in (out/"EVIDENCE").glob("ONLINE-BATCH-*.json") for r in json.loads(p.read_text(encoding="utf-8"))["rows"]]
    q=json.loads((out/"EVIDENCE/ONLINE-QUEUE.json").read_text(encoding="utf-8"))
    docs=json.loads((out/"EVIDENCE/PRIMARY-SOURCE-INDEX.json").read_text(encoding="utf-8"))
    checks=dict(original_id_set_equal=set(original)=={r["source_id"] for r in rows},unique_row_count=len(rows)==len({r["source_id"] for r in rows})==4504,original_content_equal=not errors,all_required_fields=all(all(k in r for k in FIELDS) for r in rows),external_attempt_evidence_for_every_row=all(r["external_attempted"] and (r.get("repository_observation") or r.get("url_observation")) for r in rows),metadata_queue_complete={r["entity_id"] for r in batches}=={r["entity_id"] for r in q} and len(batches)==len(q)==3256,body_never_read=all(not r.get("url_observation",{}).get("body_read",False) for r in rows),source_totals_sum=sum(s["total"] for s in coverage["by_source"].values())==4504,category_totals_sum=sum(s["total"] for s in coverage["by_category"].values())==4504,no_false_runtime_pass=all(r["runtime_verification"]=="NOT_RUN" and r["awe_admission"]=="NOT_APPROVED" for r in rows),no_approval_or_integration_counts=all(coverage["overall"][k]==0 for k in ["approved","integrated","sandbox_tested","externally_verified","license_verified"]),technical_review_count=len(reviews)==50,technical_no_false_pass=all(r["runtime"]=="NOT_RUN" and r["security_audit"]=="NOT_PERFORMED" and r["awe_acceptance"]=="NOT_PROVEN" and not r["approved"] for r in reviews),primary_blob_hashes_equal=all(r["git_blob"]==r["computed_git_blob"] for r in docs),primary_document_count=len(docs)==98,category_links_complete=link["all_original_ids_linked"] and link["record_link_count"]==4504 and link["file_count_match"],flag_reviews_linked=sum("flag_review" in r for r in rows)==12)
    result=dict(status="PASS" if all(checks.values()) else "FAIL",scope="Data/evidence assertions only; NOT runtime, security, external-family or Owner acceptance",checks=checks,errors=errors,flag_review_count=sum("flag_review" in r for r in rows),raw_counts={n:len(v) for n,v in raw.items()},external_attempted=sum(r["external_attempted"] for r in rows),independent_model_family_gate="NOT_SATISFIED")
    dump(out/"EVIDENCE/DELIVERY-VALIDATION.json",result); print(json.dumps(result,ensure_ascii=False,indent=2))
    if result["status"]!="PASS": raise SystemExit(1)

if __name__=="__main__": main()
