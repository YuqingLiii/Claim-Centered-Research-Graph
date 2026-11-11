#!/usr/bin/env python3
from pathlib import Path
import argparse,gzip,hashlib,json,os
ap=argparse.ArgumentParser();ap.add_argument('--root',type=Path,required=True);a=ap.parse_args();R=a.root.resolve();targets=[]
for i in range(42,54):
 d=R/'cegar'/f'iter{i}'
 for p in d.rglob('*'):
  if not p.is_file() or p.suffix=='.gz' or p.name.endswith('.run.json') or p.name=='iteration_outcome.json':continue
  if p.suffix in {'.json','.jsonl','.cnf','.smt2','.log'}:targets.append(p)
for p in (R/'cegar').glob('iter*.driver.log'):targets.append(p)
for name in ['round74_retained_terms.json','round74_mechanisms.json','round74_formula_raw_replay_bindings.json']:
 targets.append(R/'classification'/name)
for p in (R/'restart').glob('*.json'):
 if p.name!='restart_state.json':targets.append(p)
targets.append(R/'controls/truncated_assignment_iter42_Xerr.solver.log')
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
obj={'schema':'deterministic-gzip-dual-hash-inventory-v1','file_count':len(files),'uncompressed_bytes':ut,'compressed_bytes':ct,'files':files}
(R/'COMPRESSED_INVENTORY.json').write_text(json.dumps(obj,indent=2,sort_keys=True)+'\n');print(json.dumps({k:obj[k] for k in ['file_count','uncompressed_bytes','compressed_bytes']},sort_keys=True))
