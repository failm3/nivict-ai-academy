#!/usr/bin/env python3
"""Independent stdlib-only Nox R2 package auditor. Does not execute package code."""
import argparse, binascii, collections, csv, hashlib, io, json, re, sys, zipfile

EXPECTED_ZIP = '3f836b9bed092d819b5db54802ff6cf7f3d187a288c641b9841a1d248b0e2ad3'
EXPECTED_NESTED = 'fbd330bdf070f91246e43edaf2273579085cde335ed29f07fbb8a21276ff3348'
EXPECTED_SNAPSHOTS = {
 'iirepresent.json': ('01dc8a9f15f769f0c240fe7d64442ea279ef6461675f9f4204eb47571701ddc5',1331),
 'Радар.json': ('2f5c6806030dba7ac7b3e8e3c1cf9510054e88ac7085d46b08a941ecf9dc4221',3173),
 'catalog-all-4504.csv': ('8ad601eb0ff81cf8b8597da7276819c58bd4f156d1c269789fd4907bae9b3fa4',4504)}
EXPECTED_HISTORICAL = {'iirepresent.json':'ee54b674c057f0c67b584b77e02454a175c6853c769452e4654559f2582b1c3b',
 'Радар.json':'3a73e487a8187369753c627010bd36a22559b3b51b3ecae724265ef617c1c800'}
EXPECTED_FAMILIES = {'F01':('01-R2-EXECUTIVE-VERDICT.md','COMPLETE'),'F02':('02-NOX-LATEST-RUNTIME-FORENSIC-AUDIT.md','BLOCKED'),
 'F03':('03-COMPLETE-4504-REGISTRY.jsonl','PARTIAL'),'F04':('04-EXPANDED-TOOLS-AND-SKILLS-REGISTRY.jsonl','COMPLETE'),
 'F05':('05-READY-MADE-INTEGRATION-ATLAS.md','PARTIAL'),'F06':('06-ENTERPRISE-AGENT-COMPARATIVE-RESEARCH.md','COMPLETE'),
 'F07':('07-OPEN-WORLD-COMPETENCE-GRAPH.md','COMPLETE'),'F08':('08-CONTINUOUS-KNOWLEDGE-SYSTEM.md','COMPLETE'),
 'F09':('09-AUTONOMOUS-TOOL-ACQUISITION.md','COMPLETE'),'F10':('10-EXECUTION-STRATEGY-INTELLIGENCE.md','COMPLETE'),
 'F11':('11-LEARNING-META-INTELLIGENCE.md','COMPLETE'),'F12':('12-DOMAIN-CAPABILITY-PACKS.md','COMPLETE'),
 'F13':('13-BUILD-BUY-REUSE-MATRIX.csv','COMPLETE'),'F14':('14-R2-ACCEPTANCE-AND-BENCHMARKS.md','COMPLETE'),
 'F15':('15-OPENCODE-EXECUTION-PACK/','PARTIAL'),'F16':('16-FASTEST-SAFE-PATH-TO-R2.md','COMPLETE'),
 'F17':('17-SOURCE-AND-EVIDENCE-LEDGER.jsonl','PARTIAL'),'F18':('18-OWNER-DECISIONS-ONLY.md','COMPLETE')}
SHA = lambda b: hashlib.sha256(b).hexdigest()

def main():
 ap=argparse.ArgumentParser(); ap.add_argument('zip'); ap.add_argument('--sidecar'); ap.add_argument('--output',default='INDEPENDENT-DELIVERY-VALIDATION.json'); a=ap.parse_args()
 R={'schema_version':'independent-nox-r2-audit-v1','input_zip':a.zip,'checks':{},'defects':[],'security_observations':[]}
 def check(name, passed, detail):
  R['checks'][name]={'status':'PASS' if passed else 'FAIL','detail':detail}
  if not passed:R['defects'].append(name+': '+str(detail))
 data=open(a.zip,'rb').read(); R['outer_zip']={'bytes':len(data),'sha256':SHA(data)}
 check('outer_zip_hash',SHA(data)==EXPECTED_ZIP,{'expected':EXPECTED_ZIP,'actual':SHA(data)})
 if a.sidecar:
  line=open(a.sidecar,encoding='utf-8').read().strip(); fields=line.split()
  ok=len(fields)>=2 and fields[0]==SHA(data)
  R['outer_zip']['sidecar_text']=line; check('outer_sidecar',ok,{'expected_digest':SHA(data),'parsed':fields})
 with zipfile.ZipFile(io.BytesIO(data)) as z:
  infos=z.infolist(); files=[i for i in infos if not i.is_dir()]; names=[i.filename for i in files]; dup=[n for n,c in collections.Counter(names).items() if c>1]
  bad=[]
  for i in infos:
   try:
    b=z.read(i)
    if (binascii.crc32(b)&0xffffffff)!=i.CRC or len(b)!=i.file_size:bad.append(i.filename)
   except Exception as e:bad.append(i.filename+': '+str(e))
  nested_oc=[n for n in names if n.startswith('15-OPENCODE-EXECUTION-PACK/15-OPENCODE-EXECUTION-PACK/')]
  check('outer_crc_readback_count',not bad and len(files)==83,{'files':len(files),'crc_or_size_failures':bad,'duplicates':dup,'nested_opencode_copies':nested_oc})
  content={n:z.read(n) for n in names}; R['total_uncompressed_bytes']=sum(map(len,content.values()))
  manifest_lines={}
  malformed=[]
  for line in content['MANIFEST-SHA256.txt'].decode().splitlines():
   m=re.fullmatch(r'([0-9a-f]{64})  (.+)',line)
   if not m: malformed.append(line); continue
   if m.group(2) in manifest_lines: malformed.append('duplicate: '+line)
   manifest_lines[m.group(2)]=m.group(1)
  expected_names=set(names)-{'MANIFEST-SHA256.txt'}
  wrong=[n for n in expected_names & set(manifest_lines) if SHA(content[n])!=manifest_lines[n]]
  check('manifest_exact_coverage_hashes',not wrong and set(manifest_lines)==expected_names and not malformed and len(manifest_lines)==82,
   {'entries':len(manifest_lines),'missing':sorted(expected_names-set(manifest_lines)),'extra':sorted(set(manifest_lines)-expected_names),'wrong_hashes':wrong,'malformed_or_duplicates':malformed})
  dm=json.loads(content['DELIVERY-MANIFEST.json']); mismatches=[]
  for e in dm['artifacts']:
   p=e['path']; b=content.get(p)
   if p=='15-OPENCODE-EXECUTION-PACK':
    paths=sorted(n for n in names if n.startswith(p+'/'))
    # The manifest supplies no directory hash algorithm; test its byte total only.
    if sum(len(content[n]) for n in paths)!=e['bytes']:mismatches.append(p+' (directory byte total)')
   elif b is None or len(b)!=e['bytes'] or SHA(b)!=e['sha256']:mismatches.append(p)
  check('delivery_manifest_artifact_sizes_hashes',not mismatches,{'entries':len(dm['artifacts']),'mismatches':mismatches,'note':'F15 is a virtual directory aggregate and needs special handling; other entries should be ordinary files.'})
  nested=content['solutions-research.zip']; nested_crc=[]; nested_dup=[]
  with zipfile.ZipFile(io.BytesIO(nested)) as nz:
   ni=nz.infolist(); nf=[i for i in ni if not i.is_dir()]; nested_names=[i.filename for i in nf]
   nested_dup=[n for n,c in collections.Counter(nested_names).items() if c>1]
   for i in ni:
    try:
     b=nz.read(i)
     if (binascii.crc32(b)&0xffffffff)!=i.CRC or len(b)!=i.file_size:nested_crc.append(i.filename)
    except Exception as e:nested_crc.append(i.filename+': '+str(e))
  R['nested_solutions']={'bytes':len(nested),'sha256':SHA(nested),'file_count':len(nf),'directory_entries':len(ni)-len(nf),'duplicates':nested_dup}
  check('nested_solutions_hash_count_crc',SHA(nested)==EXPECTED_NESTED and len(nf)==246 and not nested_crc and not nested_dup,
   {'expected_sha256':EXPECTED_NESTED,'actual_sha256':SHA(nested),'files':len(nf),'crc_failures':nested_crc,'duplicates':nested_dup})
  snapshots={n:content['raw-provenance/snapshots/'+n] for n in EXPECTED_SNAPSHOTS}; snap_report={}
  for n,b in snapshots.items():
   h=SHA(b); expected_hash,expected_count=EXPECTED_SNAPSHOTS[n]
   if n.endswith('.json'):
    obj=json.loads(b); count=len(obj)
   else:
    rows=list(csv.reader(io.StringIO(b.decode('utf-8-sig')))); count=len(rows)-1
   snap_report[n]={'bytes':len(b),'sha256':h,'count':count}
   check('raw_snapshot_'+n,h==expected_hash and count==expected_count,{'expected_hash':expected_hash,'expected_count':expected_count,'actual':snap_report[n]})
  crlf={}
  for n,h in EXPECTED_HISTORICAL.items():
   b=snapshots[n]; transformed=b.replace(b'\n',b'\r\n'); actual=SHA(transformed)
   crlf[n]={'crlf_bytes':len(transformed),'crlf_sha256':actual,'roundtrip_exact':transformed.replace(b'\r\n',b'\n')==b,'contains_crlf_in_source':b'\r\n' in b}
  check('crlf_lf_mismatch_cause',all(x['crlf_sha256']==EXPECTED_HISTORICAL[n] and x['roundtrip_exact'] and not x['contains_crlf_in_source'] for n,x in crlf.items()),crlf)
  registry=[json.loads(x) for x in content['03-COMPLETE-4504-REGISTRY.jsonl'].decode().splitlines() if x.strip()]
  expected_objects=[]
  for src in ['iirepresent.json','Радар.json']:
   for idx,obj in enumerate(json.loads(snapshots[src]),1):
    collection='iirepresent' if src=='iirepresent.json' else 'Радар'; expected_objects.append((collection,idx,obj))
  identity_bad=raw_bad=raw_json_bad=status_bad=0
  for r,(collection,idx,obj) in zip(registry,expected_objects):
   o=r.get('origin',{}); ident=r.get('identity',{})
   if o.get('collection')!=collection or o.get('original_row_number')!=idx or o.get('raw_json_pointer')!='/'+str(idx-1) or ident.get('raw_url')!=obj.get('link'):identity_bad+=1
   if r.get('raw')!=obj:raw_bad+=1
   if r.get('raw_record_json')!=json.dumps(obj,ensure_ascii=False,sort_keys=True,separators=(',',':')):raw_json_bad+=1
   st=r.get('status',{})
   if r.get('evidence',{}).get('level')!='L1' or st.get('readiness')!='UNVETTED' or st.get('verdict')!='H':status_bad+=1
  ids=[r.get('record_id') for r in registry]
  reg_detail={'records':len(registry),'unique_record_ids':len(set(ids)),'source_counts':dict(collections.Counter(r.get('origin',{}).get('collection') for r in registry)), 'identity_or_pointer_failures':identity_bad,'raw_object_failures':raw_bad,'raw_record_json_failures':raw_json_bad,'L1_UNVETTED_H_failures':status_bad}
  check('registry_4504_exact_reconciliation',len(registry)==4504 and len(set(ids))==4504 and not any([identity_bad,raw_bad,raw_json_bad,status_bad]),reg_detail)
  rawcsv=list(csv.DictReader(io.StringIO(snapshots['catalog-all-4504.csv'].decode('utf-8-sig'))))
  csv_bad=0
  for r,s in zip(registry,rawcsv):
   flat=r.get('flat_export_all_fields',{}); hist=r.get('historical',{}); o=r.get('origin',{}); ident=r.get('identity',{})
   expected={'id':r.get('record_id'),'source':o.get('collection'),'source_row':str(o.get('original_row_number')),'url':ident.get('raw_url'),'description':r.get('raw',{}).get('description'),'host':ident.get('url_host'),'category':hist.get('historical_category'),'confidence':hist.get('historical_confidence'),'resource_type':hist.get('historical_resource_type'),'note_path':r.get('crosswalk',{}).get('card_path'),'flags':hist.get('historical_flags'),'exact_duplicate_group_size':str(len(r.get('crosswalk',{}).get('exact_candidate_members',[]))),'address_group_size':str(len(r.get('crosswalk',{}).get('address_candidate_members',[])))}
   if any(s.get(k)!=v for k,v in expected.items() if k!='host') or s.get('host') not in (expected['host'],'www.'+expected['host']):csv_bad+=1
  check('raw_csv_4504_registry_mapping',len(rawcsv)==4504 and csv_bad==0,{'csv_records':len(rawcsv),'core_field_mismatches':csv_bad,'csv_fields':list(rawcsv[0]) if rawcsv else []})
  matrix=list(csv.DictReader(io.StringIO(content['REQUIREMENTS-18-MATRIX.csv'].decode('utf-8-sig')))); mat=[]; matrix_bad=[]
  for row in matrix:
   fid=row['family_id']; actual=row['actual_file'].replace('../','').split('; ')[0].replace('../',''); expected=EXPECTED_FAMILIES.get(fid)
   exists=any(n==actual or n.startswith(actual) for n in names)
   mat.append({'family_id':fid,'actual_file':actual,'status':row['status'],'present':exists})
   if expected is None or expected!=(actual,row['status']) or not exists:matrix_bad.append(fid)
  check('18_canonical_families_and_matrix',len(matrix)==18 and not matrix_bad,{'rows':mat,'failures':matrix_bad})
  tickets=json.loads(content['15-OPENCODE-EXECUTION-PACK/tickets.json']); tids=[t['ticket_id'] for t in tickets['tickets']]
  ticket_paths=['15-OPENCODE-EXECUTION-PACK/'+t['path'] for t in tickets['tickets']]
  oc_ok=tids==['OC-%02d'%i for i in range(1,13)] and tickets['order']==tids and all(p in content and len(content[p])>0 for p in ticket_paths) and len(content['OPENCODE-HANDOFF-READYNESS.md'])>0
  check('opencode_12_tickets_handoff',oc_ok,{'ticket_ids':tids,'missing_ticket_files':[p for p in ticket_paths if p not in content],'handoff_bytes':len(content['OPENCODE-HANDOFF-READYNESS.md'])})
  pending=[]
  for n,b in content.items():
   if re.search(rb'(?i)\bPENDING\b',b):pending.append(n)
  with zipfile.ZipFile(io.BytesIO(nested)) as nz:
   for i in nz.infolist():
    if not i.is_dir() and re.search(rb'(?i)\bPENDING\b',nz.read(i)):pending.append('solutions-research.zip!'+i.filename)
  R['pending_scan']={'files_containing_case_insensitive_pending':pending,'interpretation':'Literal PENDING is not itself a defect when used as prose such as pending approval/domain proof. Classify contexts separately; this audit does not treat ordinary English usage as a blocking marker.'}
  check('no_unresolved_PENDING_status_marker',not any(re.search(rb'(?i)(?:status|state|validation|provenance|matrix)[\"_:=, ]+PENDING\\b',content[n]) for n in content),{'literal_occurrence_files':pending,'note':'See pending_scan; occurrences in source documents and descriptive prose are not automatically unresolved statuses.'})
  missing=[n for n in ['raw-provenance/verify_raw_provenance.py','raw-provenance/validation.log'] if n not in content]
  check('declared_provenance_helpers_absent',len(missing)==2,{'absent':missing,'impact':'Does not prevent independent reproduction: source snapshots, byte hashes, CSV and ordered registry permit independent reconciliation. No external Git identity is proven by this offline audit; validation.log is only a console transcript.'})
  # Literal/high-confidence secret and email scan, outer plus nested. No report full addresses/tokens.
  private=[]; token=[]; emails=collections.defaultdict(set)
  pats=[re.compile(rb'AKIA[0-9A-Z]{16}'),re.compile(rb'gh[pousr]_[A-Za-z0-9_]{30,}'),re.compile(rb'github_pat_[A-Za-z0-9_]{30,}'),re.compile(rb'sk-[A-Za-z0-9_-]{24,}'),re.compile(rb'xox[baprs]-[A-Za-z0-9-]{10,}'),re.compile(rb'AIza[0-9A-Za-z_-]{30,}')]
  epat=re.compile(rb'(?<![A-Za-z0-9._%+-])[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}(?![A-Za-z0-9.-])')
  items=list(content.items())
  with zipfile.ZipFile(io.BytesIO(nested)) as nz:items += [('solutions-research.zip!'+i.filename,nz.read(i)) for i in nz.infolist() if not i.is_dir()]
  for n,b in items:
   if re.search(rb'-----BEGIN (?:RSA |EC |OPENSSH |DSA )?PRIVATE KEY-----',b):private.append(n)
   for p in pats:
    if p.search(b):token.append({'file':n,'pattern':p.pattern.decode('ascii','replace')})
   for m in epat.findall(b):emails[n].add(m.decode('ascii','ignore'))
  # sk- false positives occur inside HTML data-chat-payload-element-id=..._skills_... attributes.
  genuine_token=[x for x in token if not (x['pattern'].startswith('sk-') and x['file'].endswith('.html'))]
  check('obvious_private_keys_and_tokens',not private and not genuine_token,{'private_key_files':private,'token_pattern_matches':genuine_token,'triage_false_positive_html_files':sorted(set(x['file'] for x in token if x not in genuine_token)),'note':'HTML sk- matches inspected in attributes such as data-chat-payload-element-id; no credential context. Literal scan, not entropy analysis.'})
  email_summary={n:sorted(v) for n,v in emails.items()}
  R['security_observations']={'email_addresses_by_file':email_summary,'email_files':len(email_summary),'interpretation':'Email syntax alone does not establish a personal/private address; inspect listed public role and repository metadata addresses before treating as a defect.'}
  R['runtime_boundary']={'current_nox':'UNKNOWN','T01_T12':'NOT_RUN','L3_L4':'NOT_TESTED','R2':'NOT_ACCEPTED','note':'This audit executed only its own stdlib parser/verifier; it did not run Nox, package scripts, installs or acceptance tests.'}
 R['status']='PASS' if not R['defects'] else 'FAIL'
 with open(a.output,'w',encoding='utf-8') as f:json.dump(R,f,ensure_ascii=False,indent=2)
 print(json.dumps({'status':R['status'],'defects':R['defects'],'checks':{k:v['status'] for k,v in R['checks'].items()}},ensure_ascii=False,indent=2))
 return 0 if R['status']=='PASS' else 1
if __name__=='__main__':sys.exit(main())
