import argparse, collections, json, re
from pathlib import Path
from inventory import dump, sha, COMMIT

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--repo",type=Path,required=True); ap.add_argument("--out",type=Path,required=True); args=ap.parse_args()
    root=args.repo/"03 - Практика/05 - AWE GROUP"
    names=["01 - Архитектура — решения и открытые вопросы.md","AWE-GROUP-Architecture-v01.canvas","АРХИТЕКТУРА — ДИНАМИЧЕСКИЕ РЕКУРСИВНЫЕ ПОДАГЕНТЫ — 2026-11-12.md","AWE-CONSTITUTION-v01.md","04 - Блок 04 — AWE Quality Assurance System.md","Память — сквозная архитектура и правила.md","05 - Результат, состояние и продолжение.md","CHECKPOINTS/AWE-ARCHITECTURE-VS-LIVE-2026-11-12-1541-MSK.md","CHECKPOINTS/OPENCODE-TI-INTEGRATION-VERDICT-2026-11-12-1558.md","CHECKPOINTS/TOOL-INTELLIGENCE-V2-OPENCODE-SOURCE-HANDOFF-2026-11-12.md","REPORTS/MANUS-FULL-PLATFORM-COMPARISON-CAREER01-2026-11-12.md","REPORTS/MANUS-REVISED-AGENT-ZERO-ASSESSMENT-2026-11-12.md"]
    from urllib.parse import quote
    docs=[]
    for i,n in enumerate(names,1):
        p=root/n; b=p.read_bytes(); rel=p.relative_to(args.repo).as_posix()
        docs.append(dict(id=f"A{i:02}",path=rel,sha256=sha(b),bytes=len(b),commit=COMMIT,url=f"https://github.com/failm3/nivict-ai-academy/blob/{COMMIT}/{quote(rel)}"))
    canvas=json.loads((root/names[1]).read_text(encoding="utf-8")); ids=[n["id"] for n in canvas["nodes"]]
    check=dict(node_count=len(ids),edge_count=len(canvas["edges"]),node_ids_unique=len(ids)==len(set(ids)),dangling_edges=[e["id"] for e in canvas["edges"] if e["fromNode"] not in ids or e["toNode"] not in ids],scope="Structural checks only; not runtime/overlap/layout QA")
    dump(args.out/"EVIDENCE/ARCHITECTURE-SOURCE-INDEX.json",dict(documents=docs,canvas_checks=check,current_runtime=dict(repository="failm3/awe-group-runtime",remote_main_observed="d5e9d857dbdeb8f31f9a798b10b5af4af639dbda",published_current_cleanroom_head_source="NOT_FOUND_IN_OBSERVED_REMOTE_TREE",live_runtime="NOT_OBSERVED",working_12_record_membership="NO_INDEPENDENT_LIVE_SNAPSHOT",source_of_12_count="A09 pinned report only")))
    cat=args.repo/"04 - Инструменты/Каталог кандидатов/10 - Категории"
    files=[]; refs=[]
    for p in sorted(cat.glob("*.md")):
        b=p.read_bytes(); found=re.findall(r"\[\[((?:iirepresent|Радар)-\d{4})(?:\|[^\]]*)?\]\]",b.decode("utf-8"))
        files.append(dict(path=p.relative_to(args.repo).as_posix(),sha256=sha(b),record_links=len(found))); refs.extend(found)
    rows=[json.loads(x) for x in (args.out/"INVENTORY-ALL.jsonl").read_text(encoding="utf-8").splitlines()]; expected={r["source_id"] for r in rows}
    dump(args.out/"EVIDENCE/OBSIDIAN-LINK-CHECK.json",dict(category_file_count=len(files),manifest_expected=72,file_count_match=len(files)==72,record_link_count=len(refs),unique_record_links=len(set(refs)),all_original_ids_linked=set(refs)==expected,missing_ids=sorted(expected-set(refs)),unexpected_ids=sorted(set(refs)-expected),multiplicity=dict(collections.Counter(collections.Counter(refs).values())),files=files))
    print(json.dumps(dict(canvas=check,category_files=len(files),links=len(refs),all_original_ids_linked=set(refs)==expected),ensure_ascii=False))

if __name__=="__main__": main()
