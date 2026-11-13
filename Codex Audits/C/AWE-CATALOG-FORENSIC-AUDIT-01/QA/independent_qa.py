"""Independent read-only source verification. Does not import production audit code.

Run from workspace root with Python 3.13+; all writes restricted to this directory.
"""
import ast
import collections
import csv
import hashlib
import html
import json
import re
import subprocess
from pathlib import Path
from urllib.parse import urlsplit, unquote, urlunsplit

BASE = Path(__file__).resolve().parents[2]
OUT = Path(__file__).resolve().parent
REPO = BASE / 'work/source-repo'
CAT = REPO / '04 - Инструменты/Каталог кандидатов'
DATA = CAT / '90 - Данные'
PIN = '5c611773bff3ccba76b78337534ed8944e137236'

def load_json(path):
    return json.loads(path.read_bytes().decode('utf-8-sig'))

def load_csv(path):
    with path.open(encoding='utf-8-sig', newline='') as f:
        return list(csv.DictReader(f))

def write_json(name, obj):
    (OUT / name).write_text(json.dumps(obj, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')

def legacy_full(u):
    p = urlsplit(u)
    return p.scheme.lower(), (p.hostname or '').lower().removeprefix('www.'), unquote(p.path).lower().rstrip('/') or '/', p.query, p.fragment

def resource_key(u):
    p = urlsplit(u.strip())
    if p.scheme.lower() not in ('http','https') or not p.hostname:
        return ('INVALID', u)
    h = p.hostname.lower().encode('idna').decode('ascii')
    if ':' in h:
        h = '['+h+']'
    if p.port and (p.scheme.lower(),p.port) not in (('https',443),('http',80)):
        h += ':'+str(p.port)
    if p.username is not None or p.password is not None:
        return ('CREDENTIAL_URL',u)
    return urlunsplit((p.scheme.lower(),h,p.path or '/',p.query,p.fragment))

def project_key(u):
    p = urlsplit(u)
    parts = p.path.strip('/').split('/')
    reserved={'topics','collections','marketplace','search','settings','orgs','users','login','features','sponsors','explore'}
    if p.hostname and p.hostname.lower() in ('github.com','www.github.com') and len(parts)>1 and parts[0].lower() not in reserved:
        return 'github:'+parts[0].lower()+'/'+parts[1].lower().removesuffix('.git')
    return 'resource:'+str(resource_key(u))

def parse_frontmatter(text):
    delimiters=list(re.finditer(r'(?m)^---\s*$',text))
    block=text[delimiters[0].end():delimiters[1].start()] if len(delimiters)>=2 and delimiters[0].start()==0 else ''
    result={}
    for line in block.splitlines():
        if ':' not in line: continue
        key,value=line.split(':',1); value=value.strip()
        if value.startswith('"'):
            try: value=json.loads(value)
            except json.JSONDecodeError: pass
        result[key]=value
    return result

def main():
    OUT.mkdir(parents=True,exist_ok=True)
    actual_head=subprocess.check_output(['git','rev-parse','HEAD'],cwd=REPO,text=True).strip()
    raw_sources={name:load_json(DATA/name) for name in ('iirepresent.json','Радар.json')}
    canonical=[]
    source_counts={}
    for name,rows in raw_sources.items():
        source=Path(name).stem; source_counts[source]=len(rows)
        for number,row in enumerate(rows,1):
            canonical.append({'id':f'{source}-{number:04d}','source':source,'source_row':number,'url':row.get('link'),'description':row.get('description'),'raw_keys':list(row)})
    classified=load_json(DATA/'all-records-classified.json')
    exported=load_csv(DATA/'catalog-all-4504.csv')
    reference=load_json(DATA/'validation-report.json')
    manifest=load_json(DATA/'import-manifest.json')
    duplicate_rows=load_csv(DATA/'duplicates.csv')
    issue_rows=load_csv(DATA/'issues.csv')
    ids=[r['id'] for r in canonical]
    derived=collections.defaultdict(list)
    csv_by_id=collections.defaultdict(list)
    for row in classified: derived[row['id']].append(row)
    for row in exported: csv_by_id[row['id']].append(row)
    notes=list((CAT/'20 - Записи').rglob('*.md'))
    note_stems=collections.Counter(p.stem for p in notes)
    checks=[]
    def check(name, result, detail=None): checks.append({'check':name,'pass':bool(result),'detail':detail})
    check('pinned_head',actual_head==PIN,actual_head)
    check('raw_counts',source_counts=={'iirepresent':1331,'Радар':3173},source_counts)
    check('raw_shapes_exact_link_description',all(set(r['raw_keys'])=={'link','description'} for r in canonical))
    check('raw_nonempty_strings',all(isinstance(r['url'],str) and r['url'] and isinstance(r['description'],str) and r['description'] for r in canonical))
    check('classified_count_and_ids',len(classified)==4504 and collections.Counter(r['id'] for r in classified)==collections.Counter(ids))
    check('csv_count_and_ids',len(exported)==4504 and collections.Counter(r['id'] for r in exported)==collections.Counter(ids))
    check('note_count_and_id_multiplicity',len(notes)==4504 and note_stems==collections.Counter(ids))
    mismatches=[]
    note_escaping=[]
    for row in canonical:
        sid=row['id']
        if len(derived[sid])!=1 or len(csv_by_id[sid])!=1:
            mismatches.append({'id':sid,'problem':'DERIVED_CARDINALITY'}); continue
        a=derived[sid][0]; b=csv_by_id[sid][0]
        for key in ('source','source_row','url','description'):
            if a.get(key)!=row[key]: mismatches.append({'id':sid,'problem':'JSON_RAW_'+key})
        if set(a)!=set(b): mismatches.append({'id':sid,'problem':'JSON_CSV_SCHEMA'})
        for key,value in a.items():
            if b.get(key)!=('' if value is None else str(value)):
                mismatches.append({'id':sid,'problem':'JSON_CSV_'+key})
        np=(CAT/a['note_path']).resolve()
        if not np.is_relative_to(CAT.resolve()):
            mismatches.append({'id':sid,'problem':'NOTE_PATH_TRAVERSAL'}); continue
        if not np.is_file():
            mismatches.append({'id':sid,'problem':'NOTE_MISSING'}); continue
        text=np.read_bytes().decode('utf-8-sig').replace('\r\n','\n')
        fm=parse_frontmatter(text)
        expected={'id':sid,'source':row['source'],'original_row':str(row['source_row']),'url':row['url'],'category':a['category'],'classification_confidence':a['confidence'],'resource_type':a['resource_type']}
        for key,value in expected.items():
            if str(fm.get(key))!=str(value): mismatches.append({'id':sid,'problem':'NOTE_FM_'+key})
        # Compare description in its dedicated section, not any other text in note.
        try:
            section=text.split('## Исходное описание\n',1)[1]
            section=section.split('\n> Источник не подтверждён независимо.',1)[0]
            decoded='\n'.join(line[2:] if line.startswith('> ') else line[1:] if line.startswith('>') else line for line in section.splitlines()).strip()
            raw_desc=row['description'].replace('\r\n','\n').strip()
            if decoded!=raw_desc:
                if html.unescape(decoded)==raw_desc:
                    note_escaping.append({'id':sid,'transformation':'HTML_ENTITY_ESCAPING','decoded_content_equal':True})
                else:
                    mismatches.append({'id':sid,'problem':'NOTE_DESCRIPTION_EXACT_SECTION'})
        except IndexError:
            mismatches.append({'id':sid,'problem':'NOTE_DESCRIPTION_SECTION_MISSING'})
    check('raw_json_csv_note_crosswalk',not mismatches,{'mismatch_count':len(mismatches)})
    source_hashes={}
    all_blobs=True
    for name in ('iirepresent.json','Радар.json','all-records-classified.json','catalog-all-4504.csv','validation-report.json','issues.csv','duplicates.csv','import-manifest.json'):
        p=DATA/name; data=p.read_bytes()
        rel=p.relative_to(REPO).as_posix()
        expected=subprocess.check_output(['git','rev-parse',PIN+':'+rel],cwd=REPO,text=True).strip()
        blob=hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()
        all_blobs=all_blobs and blob==expected
        source_hashes[name]={'sha256':hashlib.sha256(data).hexdigest(),'bytes':len(data),'git_blob':blob,'expected_blob':expected,'match':blob==expected}
    check('all_required_bytes_match_pinned_git_blobs',all_blobs)
    check('prior_raw_sha256_match',all(reference['source_sha256'].get(n)==source_hashes[n]['sha256'] for n in raw_sources))
    line_ending_reconciliation={n:{'reported':reference['source_sha256'][n],'pinned_git_lf':source_hashes[n]['sha256'],'crlf_reconstruction':hashlib.sha256((DATA/n).read_bytes().replace(b'\r\n',b'\n').replace(b'\n',b'\r\n')).hexdigest()} for n in raw_sources}
    check('prior_raw_sha256_explained_by_crlf',all(x['reported']==x['crlf_reconstruction'] for x in line_ending_reconciliation.values()),line_ending_reconciliation)
    for c in checks:
        if c['check']=='prior_raw_sha256_match' and not c['pass']:
            c['classification']='EXPLAINED_HISTORICAL_BYTE_MISMATCH' if all(x['reported']==x['crlf_reconstruction'] for x in line_ending_reconciliation.values()) else 'UNRESOLVED_BYTE_MISMATCH'
            c['content_failure']=False if c['classification']=='EXPLAINED_HISTORICAL_BYTE_MISMATCH' else None
    check('manifest_counts',manifest.get('record_count')==4504 and manifest.get('record_source_counts')==source_counts)
    cats=collections.Counter(r['category'] for r in classified)
    conf=collections.Counter(r['confidence'] for r in classified)
    check('prior_category_counts_recompute',dict(cats)==reference['categories'])
    check('prior_confidence_counts_recompute',dict(conf)==reference['classification_confidence'])
    exact=collections.defaultdict(list); normal=collections.defaultdict(list); address=collections.defaultdict(list); conservative=collections.defaultdict(list); projects=collections.defaultdict(list)
    for r in canonical:
        u=r['url']; exact[u].append(r['id']); k=legacy_full(u); normal[k].append(r['id']); address[(k[1],k[2])].append(r['id']); conservative[resource_key(u)].append(r['id']); projects[project_key(u)].append(r['id'])
    check('legacy_normalized_count',len(normal)==reference['unique_full_url_normalized'],len(normal))
    check('legacy_address_count',len(address)==reference['unique_host_path_only'],len(address))
    expected_duplicates={k:set(v) for k,v in normal.items() if len(v)>1}
    claimed_duplicates={ast.literal_eval(r['key']):set(r['refs'].split(',')) for r in duplicate_rows if r['kind']=='exact_normalized_full_url'}
    check('duplicates_csv_exact_group_ids',expected_duplicates==claimed_duplicates,{'expected_groups':len(expected_duplicates),'claimed_groups':len(claimed_duplicates)})
    collision_address={k:set(v) for k,v in address.items() if len(v)>1 and len({legacy_full(next(r['url'] for r in canonical if r['id']==sid)) for sid in v})>1}
    claimed_address={ast.literal_eval(r['key']):set(r['refs'].split(',')) for r in duplicate_rows if r['kind']=='address_only_collision_review_query'}
    check('duplicates_csv_query_collision_group_ids',collision_address==claimed_address,{'expected_groups':len(collision_address),'claimed_groups':len(claimed_address)})
    counts_ok=all(int(r['count'])==len(r['refs'].split(',')) for r in duplicate_rows)
    check('duplicates_csv_group_count_values',counts_ok)
    expected_issues=collections.Counter((r['id'],f.strip(),r['url']) for r in classified for f in r['flags'].split(';') if f.strip())
    actual_issues=collections.Counter((r['id'],r['issue'],r['url']) for r in issue_rows)
    check('issues_csv_exact_multiset',expected_issues==actual_issues,{'expected':sum(expected_issues.values()),'actual':len(issue_rows)})
    strata=collections.defaultdict(list)
    for r in classified: strata[(r['category'],r['confidence'])].append(r)
    sample=[]
    for (category,confidence),rs in sorted(strata.items()):
        # Stable hash sampling is independent from the producer's priorities.
        chosen=min(rs,key=lambda r:hashlib.sha256(('qa-stratified-v1:'+r['id']).encode()).hexdigest())
        sample.append({'id':chosen['id'],'category':category,'prior_confidence':confidence,'stratum_size':len(rs),'url':chosen['url'],'description':chosen['description'],'checks':'RAW_JSON_CSV_NOTE_CROSSWALK_ONLY','external_verification':'NOT_CHECKED','classification_validated':False})
    write_json('STRATIFIED-SAMPLE.json',sample)
    collision_examples=[]
    for key,refids in collision_address.items():
        urls=sorted({r['url'] for r in canonical if r['id'] in refids})
        collision_examples.append({'legacy_host_path':list(key),'source_ids':sorted(refids),'urls':urls,'must_not_automatically_merge':True})
    write_json('URL-COLLISION-EXAMPLES.json',collision_examples)
    negatives=[
        {'case':'path_case','a':'https://example.org/Tool','b':'https://example.org/tool','conservative_distinct':True,'legacy_merges':True},
        {'case':'query_identity','a':'https://example.org/api?model=a','b':'https://example.org/api?model=b','conservative_distinct':True,'legacy_address_merges':True},
        {'case':'path_encoded_slash','a':'https://example.org/a%2Fb','b':'https://example.org/a/b','conservative_distinct':True,'legacy_merges':True},
        {'case':'github_project_vs_file','a':'https://github.com/A/B','b':'https://github.com/a/b/blob/main/file.md','conservative_distinct':True,'same_project':True},
        {'case':'fragment_resource','a':'https://example.org/page#one','b':'https://example.org/page#two','conservative_distinct':True,'legacy_address_merges':True},
        {'case':'www_not_assumed_alias','a':'https://www.example.org','b':'https://example.org','conservative_distinct':True,'legacy_merges':True},
    ]
    for x in negatives:
        x['actual_conservative_distinct']=resource_key(x['a'])!=resource_key(x['b'])
        x['pass']=x['actual_conservative_distinct']==x['conservative_distinct']
        if 'same_project' in x: x['actual_same_project']=project_key(x['a'])==project_key(x['b'])
    check('independent_negative_url_cases',all(x['pass'] for x in negatives))
    write_json('NEGATIVE-CASES.json',negatives)
    report={
        'status':'PARTIAL','auditor':'independent child agent; same GPT family as lead auditor','different_family_requirement':'NOT_SATISFIED','audited_at':'2026-11-12','source_commit':PIN,
        'scope':'Read-only local corpus, derivative consistency, independent arithmetic and negative URL cases. No external code executed. No source/library imports from parent script.',
        'checks':checks,'checks_passed':sum(x['pass'] for x in checks),'checks_total':len(checks),'source_integrity':'PINNED_GIT_BLOBS_MATCH' if all_blobs else 'MISMATCH','source_content_status':'NO_CONTENT_MISMATCH_DETECTED' if not mismatches else 'MISMATCH','historical_hash_status':'EXPLAINED_HISTORICAL_BYTE_MISMATCH' if all(x['reported']==x['crlf_reconstruction'] for x in line_ending_reconciliation.values()) else 'UNRESOLVED','mismatches':mismatches,'note_escaping_reconciled':note_escaping,'line_ending_reconciliation':line_ending_reconciliation,'source_hashes':source_hashes,
        'counts':{'raw':len(canonical),'sources':source_counts,'classified':len(classified),'csv':len(exported),'notes':len(notes),'exact_urls':len(exact),'legacy_full_urls':len(normal),'legacy_addresses':len(address),'conservative_resource_urls':len(conservative),'project_or_resource_keys':len(projects),'prior_categories':dict(cats),'prior_confidence':dict(conf),'strata':len(strata),'sample_size':len(sample)},
        'limitations':['Same model family; external independent model review pending.','Stratified selection covers all 59 nonempty category/confidence strata but validates source consistency only; no primary-source claim validation.','GitHub project groups are candidate identity relations, not proof of unique installable technologies.','No current runtime tested; no license or security conclusions.'],
    }
    write_json('INDEPENDENT-COUNTS.json',report)
    print(json.dumps({'passed':report['checks_passed'],'checks':len(checks),'counts':report['counts'],'failures':[x for x in checks if not x['pass']],'mismatch_examples':mismatches[:10]},ensure_ascii=False,indent=2))

if __name__=='__main__': main()
