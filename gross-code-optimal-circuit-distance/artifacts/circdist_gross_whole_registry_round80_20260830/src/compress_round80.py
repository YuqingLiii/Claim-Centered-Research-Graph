#!/usr/bin/env python3
"""Round-80 target adaptation of the exact reviewed 2,760-byte compressor.

The reviewed compressor remains byte-for-byte at src/compress_deterministic.py.
This adaptation changes only iteration ranges and round-80 aggregate target names.
"""
from pathlib import Path
import argparse,gzip,hashlib,json,os
ap=argparse.ArgumentParser();ap.add_argument('--root',type=Path,required=True);a=ap.parse_args();R=a.root.resolve();targets=[]
for i in range(90,102):
 d=R/'cegar'/f'iter{i}'
 for p in d.rglob('*'):
  if not p.is_file() or p.suffix=='.gz' or p.name.endswith('.run.json') or p.name=='iteration_outcome.json':continue
  if p.suffix in {'.json','.jsonl','.cnf','.smt2','.log','.drat','.lrat'}:targets.append(p)
targets.append(R/'cegar/dynamic_blocks.json')
for name in ['round80_online_retained_terms.json','round80_mechanisms.json','round80_formula_raw_replay_bindings.json','installed_generalized_terms.json','online_mechanism_registry.json','full_raw_mechanisms.json','source_mechanism_cover.json']:
 targets.append(R/'classification'/name)
for p in (R/'restart').glob('*.json'):
 if p.name!='restart_state.json':targets.append(p)
for sub in ('cross_registry','whole_registry','development'):
 for p in (R/sub).rglob('*'):
  if p.is_file() and p.suffix in {'.json','.jsonl','.log','.drat','.lrat'}:targets.append(p)
targets += [R/'controls/truncated_assignment_iter90_Xerr.solver.log',R/'verification/development_precompression_full.log',R/'preflight/repository_inventory_before.jsonl',R/'preflight/git_status_before.z']
# Compress all remaining large finite ledgers, while preserving source snapshots,
# executable tooling, seal files, scripts and small human-readable summaries.
for p in R.rglob('*'):
 if not p.is_file() or p.suffix=='.gz' or p.stat().st_size<262144:continue
 rel=p.relative_to(R).as_posix()
 if rel.startswith(('source_bindings/','tooling/')) or p.name in {'SHA256SUMS.txt','PAYLOAD_SHA256SUMS.txt','COMPRESSED_INVENTORY.json'}:continue
 if p.suffix in {'.json','.jsonl','.cnf','.smt2','.log','.z','.txt','.drat','.lrat'}:targets.append(p)
seen=set()
for p in sorted(targets):
 if p in seen or not p.exists():continue
 seen.add(p);raw=p.read_bytes();q=Path(str(p)+'.gz');assert not q.exists(),q;tmp=Path(str(q)+'.tmp')
 with tmp.open('wb') as f:
  with gzip.GzipFile(filename='',mode='wb',fileobj=f,compresslevel=9,mtime=0) as g:g.write(raw)
 os.replace(tmp,q);p.unlink()
files=[];ut=ct=0
for p in sorted(R.rglob('*.gz')):
 raw=p.read_bytes();assert raw[:2]==b'\x1f\x8b' and int.from_bytes(raw[4:8],'little')==0,p;z=gzip.decompress(raw);rel=p.relative_to(R).as_posix();orig=rel[:-3];assert not (R/orig).exists(),orig
 files.append({'path':rel,'original_path':orig,'gzip_mtime':0,'compressed_bytes':len(raw),'compressed_sha256':hashlib.sha256(raw).hexdigest(),'uncompressed_bytes':len(z),'uncompressed_sha256':hashlib.sha256(z).hexdigest()});ut+=len(z);ct+=len(raw)
obj={'schema':'round80-deterministic-gzip-dual-hash-inventory-v1','reviewed_compressor_provenance':{'path':'src/compress_deterministic.py','bytes':2760,'sha256':'d4abdf75b066d8a2507d5c010f96c1c1760f36c6d1d242048fb45c5928cb8dde'},'adaptation':'iteration range 90..101 plus round80 whole/cross-registry aggregate target names and SAT proof-output trace compression only','file_count':len(files),'uncompressed_bytes':ut,'compressed_bytes':ct,'files':files}
(R/'COMPRESSED_INVENTORY.json').write_text(json.dumps(obj,indent=2,sort_keys=True)+'\n');print(json.dumps({k:obj[k] for k in ['file_count','uncompressed_bytes','compressed_bytes']},sort_keys=True))
