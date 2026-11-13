"""Reconcile optional earlier NIVICT cleaned index and shortlist against raw rows."""
import argparse, collections, json
from pathlib import Path
from inventory import legacy, entity, dump, sha

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--repo",type=Path,required=True); ap.add_argument("--out",type=Path,required=True); a=ap.parse_args()
    d=a.repo/"04 - Инструменты/Каталог кандидатов/90 - Данные"
    raw={Path(n).stem:json.loads((d/n).read_text(encoding="utf-8")) for n in ["iirepresent.json","Радар.json"]}
    clean=json.loads((d/"NIVICT-Radar-Cleaned-2026-11-04.json").read_text(encoding="utf-8"))
    seen=[]; problems=[]; descriptions_not_repeated=0; missing_url_variants=[]
    for e in clean["entries"]:
        urls={e["url"],*e.get("alternate_urls",[])}
        for o in e["occurrences"]:
            key=(o["source"],o["row"]); seen.append(key)
            try: r=raw[key[0]][key[1]-1]
            except (KeyError,IndexError): problems.append(dict(kind="invalid_occurrence",key=key)); continue
            if legacy(r["link"],True)!=legacy(e["url"],True): problems.append(dict(kind="address_mismatch",key=key))
            if r["description"]!=e["description"]: descriptions_not_repeated+=1
            if r["link"] not in urls: missing_url_variants.append(dict(source=key[0],row=key[1]))
    expected={(s,i) for s,rs in raw.items() for i in range(1,len(rs)+1)}
    shortlist=json.loads((d/"NIVICT-Tool-Shortlist-2026-11-04.json").read_text(encoding="utf-8"))["items"]; sl=[]
    for t in shortlist:
        source=t.get("source"); row=t.get("original_row"); present=t.get("source_present")
        original=raw.get(source,[])[row-1] if isinstance(row,int) and 0<row<=len(raw.get(source,[])) else None
        sl.append(dict(name=t["name"],url=t["url"],claimed_source_present=present,source=source,row=row,raw_row_found=original is not None,exact_url_match=original["link"]==t["url"] if original else None,entity_match=entity(original["link"])==entity(t["url"]) if original else None,original_verification_claim=t.get("verification"),independent_runtime_verification="NOT_RUN"))
    result=dict(cleaned=dict(entries=len(clean["entries"]),occurrences=len(seen),original_ids_equal=set(seen)==expected,occurrence_unique=len(seen)==len(set(seen)),mapping_issues=problems,original_url_variants_missing_from_entry=missing_url_variants,raw_descriptions_not_repeated_verbatim_in_selected_entry_description=descriptions_not_repeated,interpretation="Lossy address grouping. Raw source registry remains authoritative; different query/path/description meanings not independently verified."),shortlist=sl,shortlist_count=len(sl),shortlist_source_present_claims=sum(bool(x["claimed_source_present"]) for x in sl),shortlist_source_present_mapping_failures=[x for x in sl if x["claimed_source_present"] and not x["entity_match"]],source_hashes={p.name:sha(p.read_bytes()) for p in d.glob("NIVICT-*")})
    dump(a.out/"EVIDENCE/PRIOR-RESEARCH-RECONCILIATION.json",result)
    print(json.dumps({k:v for k,v in result.items() if k not in ("shortlist","source_hashes")},ensure_ascii=False,indent=2))

if __name__=="__main__": main()
