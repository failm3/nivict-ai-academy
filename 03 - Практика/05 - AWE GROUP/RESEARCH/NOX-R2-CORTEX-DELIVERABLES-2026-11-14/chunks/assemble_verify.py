#!/usr/bin/env python3
"""Reconstruct chunked originals and verify hashes; stdlib only, no network."""
from pathlib import Path
import argparse,hashlib,json,sys
root=Path(__file__).resolve().parent.parent
manifest=json.loads((Path(__file__).parent/'ASSEMBLY-MANIFEST.json').read_text())
parser=argparse.ArgumentParser();parser.add_argument('--verify',action='store_true',help='assemble and verify (default)');args=parser.parse_args()
errors=[]
for rel,item in manifest['originals'].items():
 out=root/rel;out.parent.mkdir(parents=True,exist_ok=True)
 h=hashlib.sha256();total=0
 with out.open('wb') as w:
  for c in item['chunks']:
   b=(root/c['chunk_path']).read_bytes()
   if len(b)!=c['chunk_bytes'] or hashlib.sha256(b).hexdigest()!=c['chunk_sha256']:errors.append(c['chunk_path'])
   w.write(b);h.update(b);total+=len(b)
 if total!=item['bytes'] or h.hexdigest()!=item['sha256']:errors.append(rel)
 print(rel,total,h.hexdigest(),'PASS' if rel not in errors else 'FAIL')
if errors:
 print('FAILED:',errors,file=sys.stderr);sys.exit(1)
print(f"ASSEMBLY PASS: {len(manifest['originals'])} originals")
