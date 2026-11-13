"""Evidence inventory for a manual source-text desk review. No upstream imports."""
import hashlib
import json
import zipfile
from pathlib import Path

BASE=Path(__file__).resolve().parents[2]
QA=Path(__file__).resolve().parent
ARCHIVE=Path(r'C:\Users\1\Downloads\AWE-Tool-Intelligence-v2-all.zip')
FILES=['awe_ti/registry.py','awe_ti/ingest.py','awe_ti/verification.py','awe_ti/exporting.py','awe_ti/intelligence.py','CONTRACT.md','CORE_STATUS.md','DELIVERY_STATUS.md']

FINDINGS=[
 ('IMPORT_CLAIMS_DO_NOT_APPROVE','SOURCE_CONTROL_OBSERVED','awe_ti/ingest.py',20,25,'Imported facts use imported_claim by default; ingestion does not itself grant approval or operative verified status.'),
 ('RESOURCE_ALIAS_CONFLICT_GUARD','SOURCE_CONTROL_OBSERVED','awe_ti/ingest.py',85,110,'Advisory serialization and explicit conflict rejection are present in the inspected import function.'),
 ('PROVENANCE_POINTERS_NOT_AUTHENTICATION','TRUST_BOUNDARY','awe_ti/ingest.py',72,82,'Hashing source/post/message pointers is not proof of source ownership or claim truth.'),
 ('SUPPLIED_RAW_HASH_NOT_CONTENT_VALIDATED','CODE_SCOPE_GAP','awe_ti/ingest.py',33,46,'Provided raw_hash is stored without recomputing equality to raw content here; separate post-version content hashes are independently computed.'),
 ('RAW_HASH_MODEL_HAS_NO_MATCH_VALIDATOR','SUPPLEMENTAL_SOURCE_OBSERVATION','awe_ti/models.py',49,81,'PostImport does not validate supplied raw_hash against raw content in the inspected input model.'),
 ('URL_REACHABILITY_NOT_FUNCTION','SOURCE_CONTROL_OBSERVED','awe_ti/verification.py',28,45,'Reachability logs expressly distinguish HTTP outcomes from functional tests.'),
 ('GITHUB_METADATA_NOT_VENDOR_OWNERSHIP','SOURCE_CONTROL_OBSERVED','awe_ti/verification.py',46,79,'GitHub metadata/source hosting are separated from vendor ownership and functionality.'),
 ('LICENSE_METADATA_ONLY','CODE_SCOPE_LIMIT','awe_ti/verification.py',81,105,'License text is not decoded; NOASSERTION/OTHER becomes unknown SPDX. Mixed-license feature mapping is not performed.'),
 ('RECENT_RELEASES_NOT_FULL_HISTORY','CODE_SCOPE_LIMIT','awe_ti/verification.py',106,129,'At most five release metadata records; no code/assets downloaded.'),
 ('FORWARD_LIFECYCLE_GUARD','SOURCE_CONTROL_OBSERVED','awe_ti/registry.py',86,109,'Adjacent lifecycle transitions and dedicated live-test/approval/integration helpers are required.'),
 ('HUMAN_ATTESTED_LIVE_TEST','TRUST_BOUNDARY','awe_ti/registry.py',112,123,'Supplied result/evidence/hash is recorded, not independently run or retrieved/rehashed by this function.'),
 ('LIVE_TEST_SHAPE_TIME_VALIDATION','SOURCE_CONTROL_OBSERVED','awe_ti/models.py',138,161,'Input validation checks hash format, result enum and nonfuture test timestamp; truth of evidence remains an attestation.'),
 ('FINGERPRINT_HAS_LIMITED_FIELDS','CODE_SCOPE_LIMIT','awe_ti/registry.py',30,39,'URL/type/integrations/version strings/latest spec/license/price are bound; not a direct proof of deployed artifact/environment.'),
 ('APPROVAL_EXPORT_RECHECKS','SOURCE_CONTROL_OBSERVED','awe_ti/registry.py',126,164,'Latest passing test, latest explicit non-revoked approval, freshness and matching fingerprint gate approved export.'),
 ('ACTOR_NOT_INDEPENDENT_MODEL_IDENTITY','UNPROVEN_EXTERNAL_GATE','awe_ti/registry.py',143,161,'Actor/reason are accepted values; independent family or signed reviewer identity is not established in this helper. API auth not audited here.'),
 ('INTEGRATION_ACKNOWLEDGEMENT_NOT_ADAPTER','CODE_SCOPE_LIMIT','awe_ti/registry.py',167,171,'Integration acknowledgement reuses export eligibility and records a lifecycle transition; it is not an AWE adapter or readback.'),
 ('EXPORT_DISCLAIMS_RUNNER','SOURCE_CONTROL_OBSERVED','awe_ti/exporting.py',8,20,'Separate integration manifest has exclusions and explicitly disclaims an independent sandbox runner.'),
 ('RESEARCH_EXPORT_NOT_REDACTED_HERE','PUBLICATION_REVIEW_REQUIRED','awe_ti/exporting.py',23,43,'File modes/atomic replacement are implemented; full resource serialization has no content-level secret/PII redaction in this function.'),
 ('HEURISTICS_NOT_SEMANTIC_UNIQUENESS','CODE_SCOPE_LIMIT','awe_ti/intelligence.py',26,69,'Repository/package/model-root normalization and keyword capabilities do not establish function, licensing, safety or unique technologies.'),
 ('NORMALIZATION_CAN_MERGE_RESOURCE_DISTINCTIONS','CODE_SCOPE_LIMIT','awe_ti/models.py',18,35,'Fragments/trailing slashes are removed and query pairs sorted; preserve original resource distinctions in forensic crosswalks.'),
 ('SOURCE_CANDIDATES_NOT_AUTO_ENROLLED','SOURCE_CONTROL_OBSERVED','awe_ti/intelligence.py',74,96,'Discovery function returns auto_enrolled=0 and leaves unsampled quality unknown.'),
 ('RECHECK_SCHEDULER_BOUNDED','CODE_SCOPE_LIMIT','awe_ti/intelligence.py',99,113,'Maximum ten jobs/hour for selected URL patterns; code presence does not prove continuous service operation.'),
 ('HISTORICAL_LIMITS_EXPLICIT','ARCHIVED_REPORT_SCOPE','DELIVERY_STATUS.md',19,25,'Snapshot has heuristic discoveries, four bounded library smoke tests and an unresolved backlog; old 4504 was not imported.'),
 ('NO_DEPLOYMENT_PROOF','ARCHIVED_REPORT_SCOPE','DELIVERY_STATUS.md',43,47,'WSL/systemd continuous operation was explicitly unconfirmed.'),
 ('ZERO_APPROVED_NO_TR01_COMPATIBILITY','ARCHIVED_REPORT_SCOPE','DELIVERY_STATUS.md',51,55,'Report says APPROVED=0/INTEGRATED=0 and actual cleanroom/TR-01 import compatibility was untested.'),
]

def main():
    z=zipfile.ZipFile(ARCHIVE)
    sources=[]
    for path in FILES+['awe_ti/models.py']:
        member='awe-tool-intelligence/'+path
        b=z.read(member)
        materialized=BASE/'work/manus'/path
        match=materialized.read_bytes()==b if materialized.is_file() else None
        sources.append({'path':path,'archive_member':member,'sha256':hashlib.sha256(b).hexdigest(),'bytes':len(b),'line_count':len(b.decode('utf-8').splitlines()),'materialized_copy_equal':match,'read_scope':'Full file text; not executed/imported'})
    manifest=json.loads(z.read('awe-tool-intelligence/DELIVERY_MANIFEST-v2.json'))
    counts=json.loads((QA/'MANUS-INDEPENDENT-COUNTS.json').read_text(encoding='utf-8'))
    output={'status':'DESK_REVIEW_SLICE_COMPLETE_OVERALL_AUDIT_PARTIAL','checked_at':'2026-11-12','reviewer':'Separate same-GPT-family agent; different-family gate NOT_SATISFIED','archive_sha256':hashlib.sha256(ARCHIVE.read_bytes()).hexdigest(),'claimed_source_commit':manifest['git_commit'],'sources':sources,'findings':[dict(id=i,status=s,path=p,start_line=a,end_line=b,observation=o) for i,s,p,a,b,o in FINDINGS],'snapshot':{'registry_rows':3415,'stages':counts['stages'],'recorded_approvals':counts['recorded_approvals'],'recorded_approved_for_export':counts['recorded_approved_for_export'],'current_working_12_database':'NOT_READ','current_awe_integration':'NOT_PROVEN'},'runtime_tests':'NOT_RUN','network_verifier_implementation_review':'NOT_PERFORMED_NETWORK_MODULE_OUTSIDE_SLICE','api_role_auth_review':'NOT_PERFORMED_API_MODULE_OUTSIDE_SLICE','complete_security_audit':False,'tr01_implementation':'NOT_PERFORMED'}
    assert all(x['materialized_copy_equal'] is not False for x in sources)
    assert all(f['end_line']<=next(s['line_count'] for s in sources if s['path']==f['path']) for f in output['findings'])
    (QA/'MANUS-V2-SOURCE-REVIEW.json').write_text(json.dumps(output,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'files_read':len(sources),'source_copy_byte_mismatch':sum(x['materialized_copy_equal'] is False for x in sources),'findings':len(FINDINGS),'status':output['status'],'snapshot_stages':output['snapshot']['stages']},ensure_ascii=False))

if __name__=='__main__': main()
