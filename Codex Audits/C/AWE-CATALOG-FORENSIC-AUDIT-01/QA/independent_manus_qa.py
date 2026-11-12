"""Independent NIVICT/Manus overlap, using original raw files and ZIP bytes only."""
import collections
import hashlib
import json
import re
import zipfile
from pathlib import Path
from urllib.parse import urlsplit, urlunsplit

BASE=Path(__file__).resolve().parents[2]
OUT=Path(__file__).resolve().parent
ZIP=Path(r'C:\Users\1\Downloads\AWE-Tool-Intelligence-v2-all.zip')
DATA=BASE/'work/source-repo/04 - Инструменты/Каталог кандидатов/90 - Данные'
EXPECTED_ZIP_SHA='5855ce5cfdb0abda44954108bfe2cfa1bec97dbf7c51db7be822eb04541d5ec1'

def key(url, project=False):
    if not isinstance(url,str) or not url.strip(): return None
    p=urlsplit(url.strip())
    if p.scheme not in ('http','https') or not p.hostname: return None
    h=p.hostname.lower().encode('idna').decode('ascii')
    if ':' in h: h='['+h+']'
    if p.port and (p.scheme,p.port) not in [('https',443),('http',80)]: h+=':'+str(p.port)
    bits=p.path.strip('/').split('/')
    reserved={'topics','collections','marketplace','search','settings','orgs','users','login','features','sponsors','explore'}
    if project and p.hostname.lower() in ('github.com','www.github.com') and len(bits)>=2 and bits[0].lower() not in reserved:
        return 'github:'+bits[0].lower()+'/'+bits[1].lower().removesuffix('.git')
    return ('resource:' if project else '')+urlunsplit((p.scheme,h,p.path or '/',p.query,p.fragment))

def records(z,name): return [json.loads(x) for x in z.read(name).decode('utf-8-sig').splitlines() if x.strip()]

def stats(a,b):
    return {'nivict_unique_keys':len(a),'manus_unique_keys':len(b),'intersection_unique_keys':len(a.keys()&b.keys()),'nivict_only_keys':len(a.keys()-b.keys()),'manus_only_keys':len(b.keys()-a.keys()),'nivict_rows_with_match':len({sid for k in a.keys()&b.keys() for sid in a[k]}),'manus_rows_with_match':len({sid for k in a.keys()&b.keys() for sid in b[k]})}

def main():
    raw=[]
    for filename in ('iirepresent.json','Радар.json'):
        for i,r in enumerate(json.loads((DATA/filename).read_bytes().decode('utf-8-sig')),1): raw.append((f'{Path(filename).stem}-{i:04}',r['link'],r['description']))
    z=zipfile.ZipFile(ZIP)
    manifest=json.loads(z.read('awe-tool-intelligence/DELIVERY_MANIFEST-v2.json'))
    research=records(z,'awe-tool-intelligence/exports/research_registry.jsonl')
    live=records(z,'awe-tool-intelligence/research/live_stack_resources.jsonl')
    actual_sha=hashlib.sha256(ZIP.read_bytes()).hexdigest()
    checks=[]
    def check(n,v,detail=None): checks.append({'check':n,'pass':bool(v),'detail':detail})
    check('archive_sha_matches',actual_sha==EXPECTED_ZIP_SHA,actual_sha)
    check('archive_crc_all_members',z.testzip() is None)
    check('archive_names_unique',len(z.namelist())==len(set(z.namelist())))
    check('archive_paths_safe_for_reading',all(not n.startswith(('/','\\')) and '..' not in Path(n).parts for n in z.namelist()))
    check('research_count_3415',len(research)==3415)
    check('research_ids_unique',len({r['id'] for r in research})==len(research))
    check('research_identity_keys_unique',len({r['identity_key'] for r in research})==len(research))
    check('live_stack_is_three_library_records',len(live)==3,{'count':len(live),'interpretation':'This archive file is not a snapshot of the 12-row working AWE database.'})
    metrics={}
    overlap_rows=[]
    for mode in ('raw_urls','conservative_urls','project_or_resource'):
        na=collections.defaultdict(set); ma=collections.defaultdict(set)
        for sid,url,desc in raw:
            k=url if mode=='raw_urls' else key(url,mode=='project_or_resource')
            if k is not None: na[k].add(sid)
        for r in research:
            # Both primary URLs are preserved as aliases; not inferred from prose.
            for url in {r.get('official_url'),r.get('repository_url')}:
                if not url: continue
                k=url if mode=='raw_urls' else key(url,mode=='project_or_resource')
                if k is not None: ma[k].add(r['id'])
        metrics[mode]=stats(na,ma)
        for k in sorted(na.keys()|ma.keys()):
            overlap_rows.append({'mode':mode,'key':k,'nivict_ids':sorted(na.get(k,[])),'manus_ids':sorted(ma.get(k,[])),'relation':'BOTH' if k in na and k in ma else 'NIVICT_ONLY' if k in na else 'MANUS_ONLY'})
    aliases=collections.defaultdict(set)
    for r in research:
        for u in (r.get('official_url'),r.get('repository_url')):
            k=key(u,True)
            if k: aliases[k].add(r['id'])
    live_mapping=[]
    for r in live:
        ks={key(r.get('official_url'),True),key(r.get('repository_url'),True)}-{None}
        matches=set().union(*(aliases[k] for k in ks))
        live_mapping.append({'name':r['name'],'keys':sorted(ks),'research_ids':sorted(matches)})
    check('all_live_stack_rows_map_to_research',all(x['research_ids'] for x in live_mapping),live_mapping)
    # Sensitivity analysis: the producer also retains imported URL claims as aliases.
    # Independently reproduce those explicitly marked aliases without trusting claims as verified.
    fullmaps={name:collections.defaultdict(set) for name in ('exact','canonical','entity')}
    for r in research:
        urls={r.get(f) for f in ('canonical_url','repository_url','official_url','url') if isinstance(r.get(f),str) and r[f]}
        urls|={c['value'] for c in r.get('claims',[]) if c.get('field') in ('official_url','repository_url') and isinstance(c.get('value'),str) and c['value'].startswith(('https://','http://'))}
        for u in urls:
            for mode,k in [('exact',u),('canonical',key(u)),('entity',key(u,True))]:
                if k: fullmaps[mode][k].add(r['id'])
    basis=collections.Counter(); matched=set()
    for sid,u,description in raw:
        selected='NO_STABLE_ID_MATCH'
        for mode,k in [('exact',u),('canonical',key(u)),('entity',key(u,True))]:
            if k in fullmaps[mode]:
                selected=mode; matched|=fullmaps[mode][k]; break
        basis[selected]+=1
    full_claim_metrics={'nivict_rows_by_basis':dict(basis),'matched_manus_rows':len(matched),'unmatched_manus_rows':len(research)-len(matched),'manus_entity_keys':len(fullmaps['entity']),'intersection_entity_keys':len({key(u,True) for sid,u,d in raw}&set(fullmaps['entity']))}
    producer=BASE/'outputs/EVIDENCE/MANUS-RECONCILIATION.json'
    if producer.exists():
        claimed=json.loads(producer.read_text(encoding='utf-8'))
        check('producer_row_match_metrics_independently_recomputed',claimed['overlap_nivict_rows_by_basis']==full_claim_metrics['nivict_rows_by_basis'] and claimed['matched_manus_rows']==full_claim_metrics['matched_manus_rows'] and claimed['unmatched_manus_rows']==full_claim_metrics['unmatched_manus_rows'],full_claim_metrics)
    alias_files=['awe-tool-intelligence/research/posts/GitHubRadar.jsonl','awe-tool-intelligence/research/posts/githubradar.jsonl']
    check('githubradar_case_alias_files_byte_equal',z.read(alias_files[0])==z.read(alias_files[1]))
    backup=json.loads(z.read('awe-tool-intelligence/transfer/backup/manifest.json'))
    for name,expected in backup['files'].items():
        p='awe-tool-intelligence/transfer/backup/'+name
        check('backup_member_hash_'+name,hashlib.sha256(z.read(p)).hexdigest()==expected)
    # Do not claim original source/delivery archive verified when absent from outer ZIP.
    delivery_checks=[]
    for basename,spec in manifest['files'].items():
        names=[n for n in z.namelist() if n.endswith('/'+basename) or n==basename]
        if basename=='awe-tool-intelligence-v2.bundle' and not names:
            names=['awe-tool-intelligence/awe-tool-intelligence.bundle']
        if names:
            b=z.read(names[0]); delivery_checks.append({'basename':basename,'status':'HASH_MATCH' if hashlib.sha256(b).hexdigest()==spec['sha256'] and len(b)==spec['bytes'] else 'MISMATCH'})
        else: delivery_checks.append({'basename':basename,'status':'SOURCE_MISSING_IN_OUTER_ZIP'})
    output={'status':'PARTIAL','auditor':'separate agent, same GPT family; cross-family validation NOT_SATISFIED','archive_sha256':actual_sha,'archive_member_count':len(z.namelist()),'registry_member_sha256':hashlib.sha256(z.read('awe-tool-intelligence/exports/research_registry.jsonl')).hexdigest(),'checks':checks,'check_passed':sum(x['pass'] for x in checks),'check_total':len(checks),'primary_url_overlap_metrics':metrics,'primary_plus_imported_claim_alias_metrics':full_claim_metrics,'live_stack_mapping':live_mapping,'stages':dict(collections.Counter(r['stage'] for r in research)),'verification_status':dict(collections.Counter(r['verification_status'] for r in research)),'recorded_approvals':sum(bool(r['approvals']) for r in research),'recorded_approved_for_export':sum(bool(r['approved_for_export']) for r in research),'delivery_manifest_checks':delivery_checks,'limitations':['Registry observed in local delivered ZIP; no independent author signature established.','Metadata and live tests are imported claims, not rerun or accepted by this audit.','GitHub project grouping preserves resource distinctions and is not a unique technology count.','Official and repository URLs used as aliases can create multiple keys per Manus row. Unique-key counts must not be reported as unique-row counts.','The three-row live_stack_resources file is not the 12-row working AWE runtime database; no current runtime state was read.']}
    (OUT/'MANUS-INDEPENDENT-COUNTS.json').write_text(json.dumps(output,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    (OUT/'MANUS-OVERLAP-INDEPENDENT.jsonl').write_text(''.join(json.dumps(x,ensure_ascii=False)+'\n' for x in overlap_rows),encoding='utf-8')
    print(json.dumps({'checks':f"{output['check_passed']}/{output['check_total']}",'overlap':metrics,'stages':output['stages'],'verification_status':output['verification_status'],'delivery':delivery_checks,'failure':[x for x in checks if not x['pass']]},ensure_ascii=False,indent=2))

if __name__=='__main__': main()
