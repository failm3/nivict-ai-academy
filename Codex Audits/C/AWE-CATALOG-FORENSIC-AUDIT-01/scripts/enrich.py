"""Join observed evidence without converting reachability/metadata into approval."""
import argparse, collections, json, re
from pathlib import Path
from inventory import dump, csvwrite

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--out",type=Path,required=True); args=ap.parse_args(); out=args.out; ev=out/"EVIDENCE"
    rs=[json.loads(x) for x in (out/"INVENTORY-ALL.jsonl").read_text(encoding="utf-8").splitlines()]
    batches=[json.loads(p.read_text(encoding="utf-8")) for p in sorted(ev.glob("ONLINE-BATCH-*.json"))]
    online={r["entity_id"]:dict(r,evidence_file=p.name) for p in sorted(ev.glob("ONLINE-BATCH-*.json")) for r in json.loads(p.read_text(encoding="utf-8"))["rows"]}
    for r in json.loads((ev/"ONLINE-RETRIES.json").read_text(encoding="utf-8")):
        online[r["entity_id"]]=dict(r,evidence_file="ONLINE-RETRIES.json")
    web={r["url"]:r for r in [json.loads(x) for x in (ev/"URL-RESPONSES.jsonl").read_text(encoding="utf-8").splitlines()]}
    reviews=json.loads((out/"TECHNICAL-REVIEWS.json").read_text(encoding="utf-8")); bysid={sid:r for r in reviews for sid in r["source_ids"]}
    spots=json.loads((out/"QA/PRIMARY-SOURCE-SPOTCHECKS.json").read_text(encoding="utf-8"))["results"]
    spotmap={r["id"]:r for r in spots}
    flags=json.loads((out/"QA/FLAGGED-SOURCE-REVIEW.json").read_text(encoding="utf-8"))["per_id"]
    flagmap={r.get("source_id",r.get("id")):r for r in flags}
    corrections={"Радар-0705":("Визуализация - Картография и терминал","terminal_map_renderer"),"Радар-0128":("Дизайн - Скриншоты и графика","image_design_editor"),"Радар-0694":("Безопасность - Справочные материалы","reference_collection")}
    for r in rs:
        r["verification_levels"]=["SOURCE_PRESERVED","CLASSIFIED_RULE_BASED"]
        r["external_attempted"]=False; r["external_observed"]=False
        r["repo_desk_reviewed"]=False; r["license_text_inspected"]=False
        r["original_url_check"]="NOT_CHECKED"; r["runtime_verification"]="NOT_RUN"; r["awe_admission"]="NOT_APPROVED"
        r["classification_review"]="RULE_BASED_UNVERIFIED"; r["capability_basis"]="KEYWORD_HINT_ONLY"; r["integration_decision"]="DEFER_NOT_EVALUATED"
        if r["entity_id"] in online:
            o=online[r["entity_id"]]; r["external_attempted"]=True
            r["external_verification"]=o["status"]; r["original_url_check"]="NOT_FETCHED_REPOSITORY_ENTITY_API_ONLY"
            r["external_observed"]=o["status"]=="METADATA_OBSERVED"; r["repository_observation"]=o
            r["evidence_refs"].append("EVIDENCE/"+o["evidence_file"]+"#"+r["entity_id"])
            r["license_status"]="METADATA_ONLY_NOT_LICENSE_VERIFIED" if o.get("license_metadata") else "UNKNOWN"
            r["maintenance_status"]="ARCHIVED_OBSERVED" if o.get("archived") else "PUSH_DATE_OBSERVED_NOT_SUPPORT_ASSURANCE" if o.get("pushed_at") else "UNKNOWN"
            if o.get("archived") and "ARCHIVED_REPOSITORY" not in r["security_flags"]: r["security_flags"].append("ARCHIVED_REPOSITORY")
            if r["external_observed"]: r["verification_levels"].append("REPOSITORY_METADATA_OBSERVED")
            r["blocking_reason"]="NOT_RUNTIME_OR_SECURITY_TESTED" if r["external_observed"] else o["status"]
        elif r["original_url"] in web:
            w=web[r["original_url"]]; r["external_attempted"]=True; r["external_observed"]=w["status"]!="NETWORK_OR_POLICY_UNKNOWN"
            r["url_observation"]=w; r["external_verification"]=w["status"]; r["original_url_check"]="HEAD_"+str(w.get("http_status","UNKNOWN"))
            r["evidence_refs"].append("EVIDENCE/URL-RESPONSES.jsonl#"+r["source_id"])
            if r["external_observed"]: r["verification_levels"].append("HTTP_RESPONSE_OBSERVED")
            r["blocking_reason"]="HEAD_ONLY_CONTENT_IDENTITY_LICENSE_FUNCTION_UNKNOWN" if w.get("http_status")==200 else "HTTP_OR_NETWORK_RESULT_NEEDS_REVIEW"
        if r["source_id"] in bysid:
            d=bysid[r["source_id"]]; r["repo_desk_reviewed"]=True; r["license_text_inspected"]=True
            r["technical_review_rank"]=d["rank"]; r["external_verification"]="REPOSITORY_DESK_REVIEWED_NOT_RUNTIME_TESTED"
            r["verification_levels"].extend(["REPO_INSPECTED_DESK_ONLY","LICENSE_TEXT_INSPECTED"])
            r["license_status"]="LICENSE_TEXT_INSPECTED_SCOPE_LIMITED"; r["license_scope"]=d["license_scope"]
            r["integration_type"]=d["integration_type"]; r["integration_decision"]=d["decision"]
            r["capabilities"]=[d["need"]]; r["architectural_needs"]=[d["need"]]; r["capability_basis"]="DOCUMENTATION_REVIEW_NOT_FUNCTIONAL_PROOF"
            r["priority"]="P1" if d["decision"] in ("REUSE","PILOT") else "P2"
            r["evidence_refs"].append(f"TECHNICAL-REVIEWS.json#rank={d['rank']}")
            r["confidence"]="DOCUMENTED_NOT_RUNTIME_PROVEN"
        if r["source_id"] in spotmap:
            r["classification_review"]="SEPARATE_SAME_FAMILY_AUDITOR_README_REVIEW"
            r["evidence_refs"].append("QA/PRIMARY-SOURCE-SPOTCHECKS.json#"+r["source_id"])
            if r["source_id"] in corrections:
                c,t=corrections[r["source_id"]]; r["categories"]=[c]; r["resource_type"]=t; r["capabilities"]=[]; r["architectural_needs"]=[]; r["capability_basis"]="PRIMARY_README_CORRECTION"
        if r["source_id"] in flagmap:
            r["flag_review"]=flagmap[r["source_id"]]; r["evidence_refs"].append("QA/FLAGGED-SOURCE-REVIEW.json#"+r["source_id"])
        r["evidence_refs"]=list(dict.fromkeys(r["evidence_refs"]))
    with (out/"INVENTORY-ALL.jsonl").open("w",encoding="utf-8",newline="\n") as f:
        for r in rs: f.write(json.dumps(r,ensure_ascii=False,separators=(",",":"))+"\n")
    def metrics(rows):
        return dict(total=len(rows),processed=len(rows),source_preserved=len(rows),classified_rule_based=len(rows),external_attempted=sum(r["external_attempted"] for r in rows),external_observed=sum(r["external_observed"] for r in rows),repo_inspected=sum(r["repo_desk_reviewed"] for r in rows),license_text_inspected=sum(r["license_text_inspected"] for r in rows),externally_verified=0,license_verified=0,sandbox_tested=0,approved=0,integrated=0,unresolved=len(rows))
    counts=dict(status="PARTIAL",source_commit=rs[0]["source_commit"],checked_at="2026-11-12",definitions=dict(external_attempted="Each record had a repository-entity API lookup OR original-URL HEAD attempt. Repository subpaths were not fetched by metadata lookup.",external_observed="Successful repository metadata OR any HTTP response; not content identity/function/safety proof.",repo_inspected="README/LICENSE desk review by exact project identity; not full code/security audit.",externally_verified="Reserved for completed independent verification; cross-family requirement is unsatisfied, so zero.",license_text_inspected="Root license text read at pinned SHA, scoped exceptions documented; not dependency/legal approval.",unresolved="AWE admission/function/security acceptance remains unresolved for every record."),overall=metrics(rs),by_source={s:metrics([r for r in rs if r["source_file"]==s]) for s in sorted({r["source_file"] for r in rs})},by_category={s:metrics([r for r in rs if s in r["categories"]]) for s in sorted({s for r in rs for s in r["categories"]})},by_prior_category={s:metrics([r for r in rs if s==r["prior_classification"]["category"]]) for s in sorted({r["prior_classification"]["category"] for r in rs})},field_coverage={k:dict(present=sum(k in r for r in rs),nonempty=sum(r.get(k) not in (None,"",[]) for r in rs),total=len(rs)) for k in sorted({k for r in rs for k in r})},verification_levels=dict(collections.Counter(l for r in rs for l in r["verification_levels"])),external_statuses=dict(collections.Counter(r["external_verification"] for r in rs)),security_flags=dict(collections.Counter(f for r in rs for f in r["security_flags"])),resource_types=dict(collections.Counter(r["resource_type"] for r in rs)),github_projects=dict(attempted=len(online),statuses=dict(collections.Counter(r["status"] for r in online.values())),archived=sum(bool(r.get("archived")) for r in online.values())),web_distinct_urls=dict(attempted=len(web),statuses=dict(collections.Counter(r["status"] for r in web.values())),http_statuses=dict(collections.Counter(str(r.get("http_status","UNKNOWN")) for r in web.values()))),technical_desk_reviews=len(reviews),primary_document_count=len(json.loads((ev/"PRIMARY-SOURCE-INDEX.json").read_text(encoding="utf-8"))),machine_checks=json.loads((ev/"LOCAL-RECONCILIATION.json").read_text(encoding="utf-8")))
    assert len(rs)==4504 and len({r["source_id"] for r in rs})==4504 and all(r["external_attempted"] for r in rs)
    assert len(online)==3256 and len(web)==1209
    dump(out/"COVERAGE.json",counts)
    queue=[]
    for r in rs:
        queue.append(dict(source_id=r["source_id"],priority=r["priority"],external_status=r["external_verification"],next_action="REVIEW_ENTITY_REDIRECT" if r.get("repository_observation",{}).get("status")=="REDIRECT_REQUIRES_REVIEW" else "INDEPENDENT_PILOT_REQUIRES_SEPARATE_AUTHORIZATION" if r.get("repo_desk_reviewed") else "PRIMARY_CONTENT_LICENSE_CLASSIFICATION_REVIEW",blocking_reason=r["blocking_reason"]))
    csvwrite(out/"CONTINUATION-QUEUE.csv",queue)
    print(json.dumps(dict(overall=counts["overall"],github=counts["github_projects"],web=counts["web_distinct_urls"]),ensure_ascii=False,indent=2))

if __name__=="__main__": main()
