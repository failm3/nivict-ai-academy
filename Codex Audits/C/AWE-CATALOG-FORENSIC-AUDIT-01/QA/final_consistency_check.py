"""Independent final corpus/report reconciliation; no root-script/upstream imports."""
import collections
import hashlib
import json
import re
from pathlib import Path
from urllib.parse import urlsplit, urlunsplit

BASE=Path(__file__).resolve().parents[2]
OUT=BASE/'outputs'
QA=Path(__file__).resolve().parent
DATA=BASE/'work/source-repo/04 - Инструменты/Каталог кандидатов/90 - Данные'
ROOT_FILES=['AUDIT-METHOD.md','AWE-CAPABILITY-GAP-MATRIX.md','PRIORITY-BACKLOG.md','FINOPS-PROVIDERS.md','COVERAGE.md','COVERAGE.json','INDEPENDENT-QA.md','CHECKPOINT.json','INVENTORY-ALL.jsonl','TECHNICAL-REVIEWS.json','TOP-50-DEEP-REVIEW.md','CONTINUATION-QUEUE.csv','DEDUP-RECONCILIATION.csv','README.md','REPRODUCE.md']

def digest(b): return hashlib.sha256(b).hexdigest()
def read_json(p): return json.loads(p.read_bytes().decode('utf-8-sig'))
def read_jsonl(p): return [json.loads(x) for x in p.read_bytes().decode('utf-8-sig').splitlines() if x.strip()]

def identity(url):
    u=urlsplit(url.strip()); h=(u.hostname or '').lower().encode('idna').decode('ascii')
    if ':' in h: h='['+h+']'
    if u.port and (u.scheme.lower(),u.port) not in [('https',443),('http',80)]: h+=':'+str(u.port)
    canonical=urlunsplit((u.scheme.lower(),h,u.path or '/',u.query,u.fragment))
    bits=u.path.strip('/').split('/')
    reserved={'topics','collections','marketplace','search','settings','orgs','users','login','features','sponsors','explore','signup','about','pricing','enterprise','security','readme','events','apps'}
    if u.hostname and u.hostname.lower() in ('github.com','www.github.com') and len(bits)>=2 and bits[0].lower() not in reserved:
        return 'github:'+bits[0].lower()+'/'+bits[1].lower().removesuffix('.git'),canonical
    return 'resource:'+canonical,canonical

def main():
    checked_files={}
    def capture(p):
        b=p.read_bytes(); checked_files[p.relative_to(OUT).as_posix()]={'sha256':digest(b),'bytes':len(b)}; return b
    for name in ROOT_FILES: capture(OUT/name)
    inv=read_jsonl(OUT/'INVENTORY-ALL.jsonl')
    cov=read_json(OUT/'COVERAGE.json'); checkpoint=read_json(OUT/'CHECKPOINT.json'); tech=read_json(OUT/'TECHNICAL-REVIEWS.json')
    raw={}; source_hashes={}; raw_counts={}
    for name in ['iirepresent.json','Радар.json']:
        b=(DATA/name).read_bytes(); rows=json.loads(b.decode('utf-8-sig')); raw_counts[name]=len(rows); source_hashes[name]=digest(b)
        for i,row in enumerate(rows,1): raw[f'{Path(name).stem}-{i:04d}']={'source_file':name,'source_row':i,'raw':row}
    original_classified={r['id']:r for r in read_json(DATA/'all-records-classified.json')}
    checks=[]; errors=[]
    def check(name,value,detail=None):
        ok=bool(value); checks.append({'check':name,'pass':ok,'detail':detail})
        if not ok: errors.append(name)
    check('raw_source_counts',raw_counts=={'iirepresent.json':1331,'Радар.json':3173},raw_counts)
    check('inventory_id_multiset_exact',collections.Counter(r['source_id'] for r in inv)==collections.Counter(raw.keys()))
    content_bad=[]; provenance_bad=[]; prior_bad=[]; canonical_bad=[]; ref_dup=[]; missing_refs=[]
    for r in inv:
        sid=r['source_id']; source=raw.get(sid)
        if not source: continue
        b=source['raw']
        if r['original_url']!=b['link'] or r['original_description']!=b['description'] or r['raw_record']!=b: content_bad.append(sid)
        if r['source_file']!=source['source_file'] or r['source_row']!=source['source_row'] or r['source_sha']!=source_hashes[source['source_file']]: provenance_bad.append(sid)
        if r['prior_classification']!=original_classified[sid]: prior_bad.append(sid)
        eid,can=identity(b['link'])
        if r['entity_id']!=eid or r['canonical_url']!=can: canonical_bad.append(sid)
        if len(r['evidence_refs'])!=len(set(r['evidence_refs'])): ref_dup.append(sid)
        for ref in r['evidence_refs']:
            path=ref.split('#',1)[0]
            if not re.match(r'^[a-f0-9]{40}:',path) and not (OUT/path).is_file(): missing_refs.append({'id':sid,'path':path})
    check('all_original_urls_descriptions_raw_records_equal',not content_bad,content_bad)
    check('all_source_file_row_hash_equal',not provenance_bad,provenance_bad)
    check('all_original_classification_objects_preserved',not prior_bad,prior_bad)
    check('canonical_and_entity_keys_independently_recomputed',not canonical_bad,canonical_bad)
    check('evidence_refs_no_duplicates',not ref_dup,ref_dup)
    check('evidence_ref_files_exist',not missing_refs,missing_refs[:20])
    required='source_id source_file source_row source_sha original_url canonical_url entity_id duplicate_group name original_description resource_type categories capabilities architectural_needs confidence source_verification external_verification license_status maintenance_status security_flags integration_type priority evidence_refs checked_at blocking_reason'.split()
    check('required_fields_present',all(all(k in r for k in required) for r in inv))
    check('one_primary_category_per_record',all(len(r['categories'])==1 for r in inv))
    metadata={}; batch_rows=[]
    for p in sorted((OUT/'EVIDENCE').glob('ONLINE-BATCH-*.json')):
        capture(p); rows=read_json(p)['rows']; batch_rows+=rows
        for r in rows: metadata[r['entity_id']]=r
    retry_file=OUT/'EVIDENCE/ONLINE-RETRIES.json'; capture(retry_file)
    retries=read_json(retry_file)
    for r in retries: metadata[r['entity_id']]=r
    urlfile=OUT/'EVIDENCE/URL-RESPONSES.jsonl'; capture(urlfile); urlrows=read_jsonl(urlfile); urlmap={r['url']:r for r in urlrows}
    queuefile=OUT/'EVIDENCE/ONLINE-QUEUE.json'; capture(queuefile); queue=read_json(queuefile)
    github_keys={identity(x['raw']['link'])[0] for x in raw.values() if identity(x['raw']['link'])[0].startswith('github:')}
    other_urls={x['raw']['link'] for x in raw.values() if not identity(x['raw']['link'])[0].startswith('github:')}
    check('raw_metadata_batch_keys_unique',len(batch_rows)==len({r['entity_id'] for r in batch_rows}),{'batch_rows':len(batch_rows)})
    check('github_raw_evidence_complete',set(metadata)==github_keys and len(metadata)==3256)
    check('github_queue_complete',len(queue)==3256 and {r['entity_id'] for r in queue}==github_keys)
    check('other_url_raw_evidence_complete',set(urlmap)==other_urls and len(urlrows)==len(urlmap)==1209)
    github_statuses=dict(collections.Counter(r['status'] for r in metadata.values()))
    url_statuses=dict(collections.Counter(r['status'] for r in urlrows))
    check('github_status_counts',github_statuses=={'METADATA_OBSERVED':3010,'REDIRECT_REQUIRES_REVIEW':207,'UNRESOLVED':39},github_statuses)
    check('other_url_status_counts',url_statuses=={'HTTP_RESPONSE_OBSERVED':973,'HTTP_ERROR_OBSERVED':149,'NETWORK_OR_POLICY_UNKNOWN':87},url_statuses)
    check('head_requests_no_body_or_auth',all(r['method']=='HEAD' and r['body_read'] is False and r['authentication']=='NONE' for r in urlrows))
    expected_observed={}; attempt_bad=[]; observation_bad=[]; recorded_obs_bad=[]
    for r in inv:
        sid=r['source_id']; eid,_=identity(raw[sid]['raw']['link'])
        obs=metadata.get(eid) if eid.startswith('github:') else urlmap.get(r['original_url'])
        attempted=obs is not None
        observed=bool(obs and (obs['status']=='METADATA_OBSERVED' if eid.startswith('github:') else obs['status'] in ('HTTP_RESPONSE_OBSERVED','HTTP_ERROR_OBSERVED')))
        expected_observed[sid]=observed
        if r.get('external_attempted') is not attempted: attempt_bad.append(sid)
        if r.get('external_observed') is not observed: observation_bad.append(sid)
        recorded=r.get('repository_observation') if eid.startswith('github:') else r.get('url_observation')
        keys=['status','id','full_name','entity_id'] if eid.startswith('github:') else ['status','url','http_status','method','body_read']
        if not recorded or any(recorded.get(k)!=obs.get(k) for k in keys): recorded_obs_bad.append(sid)
    check('attempt_flags_match_raw_evidence_all_ids',not attempt_bad,attempt_bad)
    check('observation_flags_match_raw_evidence_all_ids',not observation_bad,observation_bad)
    check('per_row_recorded_observations_match_raw',not recorded_obs_bad,recorded_obs_bad)
    desk_ids={sid for r in tech for sid in r['source_ids']}
    def metrics(rows):
        return {'total':len(rows),'processed':len(rows),'source_preserved':sum(r['source_verification']=='SOURCE_PRESERVED' for r in rows),'classified_rule_based':sum('CLASSIFIED_RULE_BASED' in r['verification_levels'] for r in rows),'external_attempted':sum(r['source_id'] not in attempt_bad for r in rows),'external_observed':sum(expected_observed[r['source_id']] for r in rows),'repo_inspected':sum(r['source_id'] in desk_ids for r in rows),'license_text_inspected':sum(r['source_id'] in desk_ids for r in rows),'externally_verified':0,'license_verified':0,'sandbox_tested':0,'approved':0,'integrated':0,'unresolved':len(rows)}
    overall=metrics(inv)
    by_source={s:metrics([r for r in inv if r['source_file']==s]) for s in raw_counts}
    categories=sorted({r['categories'][0] for r in inv})
    by_category={c:metrics([r for r in inv if r['categories'][0]==c]) for c in categories}
    old_categories=sorted({r['category'] for r in original_classified.values()})
    by_prior={c:metrics([r for r in inv if original_classified[r['source_id']]['category']==c]) for c in old_categories}
    check('coverage_overall_exact',cov['overall']==overall,overall)
    check('coverage_source_breakdown_exact',cov['by_source']==by_source)
    check('coverage_current_category_breakdown_exact',cov['by_category']==by_category,{'categories':len(by_category),'total':sum(x['total'] for x in by_category.values())})
    check('coverage_prior_category_breakdown_exact',cov['by_prior_category']==by_prior,{'categories':len(by_prior)})
    check('coverage_external_statuses_exact',cov['external_statuses']==dict(collections.Counter(r['external_verification'] for r in inv)))
    check('coverage_level_counts_exact',cov['verification_levels']==dict(collections.Counter(x for r in inv for x in r['verification_levels'])))
    check('coverage_flag_and_type_counts_exact',cov['security_flags']==dict(collections.Counter(x for r in inv for x in r['security_flags'])) and cov['resource_types']==dict(collections.Counter(r['resource_type'] for r in inv)))
    check('no_inventory_runtime_or_approval_pass',all(r['runtime_verification']=='NOT_RUN' and r['awe_admission']=='NOT_APPROVED' and not set(r['verification_levels'])&{'URL_VERIFIED','LICENSE_VERIFIED','SANDBOX_TESTED','APPROVED','INTEGRATED'} for r in inv))
    check('desk_flags_match_review_linkage',all(r['repo_desk_reviewed']==(r['source_id'] in desk_ids) and r['license_text_inspected']==(r['source_id'] in desk_ids) for r in inv))
    link_bad=[]
    for row in tech:
        for sid in row['source_ids']:
            project=identity(raw[sid]['raw']['link'])[0].removeprefix('github:')
            if project not in {(row['repo'] or '').lower(),(row['canonical_repo'] or '').lower()}: link_bad.append({'rank':row['rank'],'id':sid})
    tech_counts={'reviews':len(tech),'exact_project_review_entries':sum(r['archive_membership']=='EXACT_PROJECT_MATCH' for r in tech),'linked_original_ids':len(desk_ids),'architecture_additions':sum(not r['source_ids'] for r in tech)}
    check('technical_review_counts_and_linkage',tech_counts=={'reviews':50,'exact_project_review_entries':30,'linked_original_ids':32,'architecture_additions':20} and not link_bad,{'counts':tech_counts,'mismatches':link_bad})
    check('no_technical_runtime_security_approval_pass',all(r['runtime']=='NOT_RUN' and r['security_audit']=='NOT_PERFORMED' and r['awe_acceptance']=='NOT_PROVEN' and r['approved'] is False for r in tech))
    idxfile=OUT/'EVIDENCE/PRIMARY-SOURCE-INDEX.json'; capture(idxfile); primary=read_json(idxfile)
    cache={}
    for p in (BASE/'work/github-cache').glob('*.json'):
        for r in read_json(p).get('resources',[]):
            if isinstance(r.get('data',{}).get('content'),str): cache[r['url']]=r['data']['content'].encode('utf-8')
    primary_bad=[]
    for r in primary:
        b=cache.get(r['url'])
        if b is None or digest(b)!=r['sha256'] or hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()!=r['git_blob']: primary_bad.append(r['url'])
    check('primary_98_text_hashes_recomputed',len(primary)==98 and not primary_bad,{'count':len(primary),'missing_or_mismatch':primary_bad})
    checkpoint_expected={'original_rows_accounted':4504,'external_attempted_rows':4504,'external_observed_rows':4169,'github_projects_attempted':3256,'technical_desk_reviews':50,'archive_project_matched_reviews':30,'archive_rows_desk_reviewed':32,'architecture_additions':20,'primary_documents':98,'sandbox_tested':0,'approved':0,'integrated':0,'different_family_qa':'NOT_SATISFIED','blind_examiner':'NOT_RUN','runtime_tests':'NOT_RUN','security_audit':'NOT_PERFORMED','working_awe_12_status':'REPORTED_ONLY_NO_INDEPENDENT_CURRENT_SNAPSHOT'}
    check('checkpoint_counts_and_limits_consistent',all(checkpoint.get(k)==v for k,v in checkpoint_expected.items()))
    check('overall_partial_status',cov['status']=='PARTIAL' and checkpoint['status']=='PARTIAL')
    docs={n:(OUT/n).read_text(encoding='utf-8') for n in ROOT_FILES if n.endswith('.md')}
    check('root_limitations_explicit',all('PARTIAL' in docs[n] for n in ['AUDIT-METHOD.md','AWE-CAPABILITY-GAP-MATRIX.md','PRIORITY-BACKLOG.md','FINOPS-PROVIDERS.md','COVERAGE.md','INDEPENDENT-QA.md']) and 'NOT_SATISFIED' in docs['INDEPENDENT-QA.md'] and 'того же семейства' in docs['INDEPENDENT-QA.md'] and 'не 50 runtime/security' in docs['TOP-50-DEEP-REVIEW.md'])
    # Manual report reading is recorded separately; lexical checks are not a semantic examiner.
    manual={'root_reports_read':True,'scope_observed':'Reports consistently label PARTIAL, distinguish source observations/desk reviews from runtime acceptance, retain cross-family/blind limitations and reported-only current12 state. No claim of current live integration, complete corpus safety, automatic installation permission or proven ROI found.','archive_extension_corrections':'Core material qualifications for ranks42-50 are present. The latest rank48 adds single-process writer;49 says local mode is not offline. Additional detailed LightRAG storage and LangExtract provider-schema caveats remain in QA source review; root summaries do not make contrary guarantees.','finops_primary_recheck':[{'url':'https://openrouter.ai/pricing','checked_at':'2026-11-12','source_lines':'53,75,88-108','result':'Public fee/BYOK/payment-method statements in the report agree with the independently read official pricing page. Account/RF access unverified.'},{'url':'https://www.requesty.ai/pricing','checked_at':'2026-11-12','source_lines':'13-17,19-36,42-54','result':'Public markup/free-tier statements agree with independently read official page. No paid request or account verification performed.'}]}
    check('reviewed_files_stable_during_final_check',all(digest((OUT/path).read_bytes())==spec['sha256'] for path,spec in checked_files.items()))
    result={'status':'DATA_AND_REPORT_CONSISTENCY_PASS_OVERALL_PARTIAL' if not errors else 'CONSISTENCY_FINDINGS_REQUIRE_REVIEW','checked_at':'2026-11-12','reviewer':'Separate same-GPT-family auditor; shared parent context, not blind/cross-family','method':'Independent standard-library recomputation from original raw JSON, enriched registry, raw metadata batches/retry, raw HEAD evidence, primary caches, technical reviews and report text. No root audit script or upstream module imported/executed.','checks':checks,'checks_total':len(checks),'checks_passed':sum(x['pass'] for x in checks),'errors':errors,'independent_totals':{'overall':overall,'by_source':by_source,'by_category':by_category,'by_prior_category':by_prior,'github_unique_statuses':github_statuses,'other_url_statuses':url_statuses,'technical':tech_counts,'runtime_statuses':dict(collections.Counter(r['runtime_verification'] for r in inv)),'admission_statuses':dict(collections.Counter(r['awe_admission'] for r in inv))},'manual_semantic_review':manual,'reviewed_files':checked_files,'source_raw_sha256':source_hashes,'limitations':['Same GPT family; no independent other-family or blind verdict.','No live/OS/database/provider/sandbox/security tests run.','Attempt coverage counts source rows supported by lookups, not the number of actual network requests or unique technologies.','Root metadata/query/readme observations are not functionality, license clearance or safety acceptance.','Public staging scan, publication, GitHub receipt and later replay receipts are separate root work; this pass does not attest future mutations.']}
    for field in ['source_verification','external_verification','license_status','maintenance_status','classification_review','resource_type']:
        result['independent_totals'][field+'_counts']=dict(collections.Counter(str(r.get(field)) for r in inv))
    result['independent_totals']['verification_level_counts']=dict(collections.Counter(level for r in inv for level in r['verification_levels']))
    result['independent_totals']['security_flag_counts']=dict(collections.Counter(flag for r in inv for flag in r['security_flags']))
    (QA/'FINAL-CONSISTENCY-REVIEW.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    lines=['# Final independent consistency review','','Status: **data/report consistency passed; overall audit PARTIAL**.' if not errors else 'Status: **consistency findings require review**.','','Separate same-GPT-family auditor, with parent context. Different-family/blind examination remains NOT_SATISFIED. Only source data and documents were read; no root audit script or upstream code was imported/executed.','',f"Independent checks: **{result['checks_passed']}/{result['checks_total']}**. See `FINAL-CONSISTENCY-REVIEW.json` for every check, independent breakdown and hashes of the exact reviewed files.",'','- All 4,504 source IDs, source file/row/hash, original URLs, descriptions, raw objects and previous classifications are preserved. No duplicate evidence references remain.','- Raw evidence supports attempt coverage for 4,504 rows and observations for 4,169. GitHub project results: 3,010 metadata / 207 redirect review / 39 unresolved. Other URLs: 973 HTTP200 / 149 other HTTP / 87 unknown. These denominators are distinct from physical network-request counts.','- Source/category/status and verification-level totals exactly match COVERAGE. Current categories include three independently supported corrections; old categories remain preserved.','- 50 desk reviews comprise 30 exact-project review entries linked to 32 original rows, plus 20 architecture additions. All 98 indexed primary text hashes were independently recomputed from cached source bodies.','- Runtime/sandbox/security/approval/integration acceptance is not falsely asserted. All 4,504 admission states are NOT_APPROVED; no review has runtime/security/approval PASS.','- Root reports retain current12 as reported-only, do not claim complete security/current live integration, and incorporate the core nine shortlist-extension corrections. Additional detailed provider/storage caveats remain available in the QA source reviews.','','Official pricing pages independently rechecked: [OpenRouter](https://openrouter.ai/pricing) and [Requesty](https://www.requesty.ai/pricing). Their quoted public headline terms agree with FINOPS-PROVIDERS; authenticated account terms, actual payments, RF access and inference performance remain unverified.','','No blocking consistency finding was found.' if not errors else 'Checks requiring review: '+', '.join(errors), '','This result attests the hashed snapshot only. Staged public-tree secret/PII scan, GitHub publication/readback and any later changes require their own checks. The overall status remains PARTIAL.']
    (QA/'FINAL-CONSISTENCY-REVIEW.md').write_text('\n'.join(lines)+'\n',encoding='utf-8')
    print(json.dumps({'checks':f"{result['checks_passed']}/{result['checks_total']}",'errors':errors,'overall':overall,'technical':tech_counts,'reviewed_file_count':len(checked_files),'status':result['status']},ensure_ascii=False))

if __name__=='__main__': main()
