#!/usr/bin/env python3
from pathlib import Path
import argparse,hashlib,json

def sha(p):
 h=hashlib.sha256()
 with Path(p).open('rb') as f:
  for b in iter(lambda:f.read(8<<20),b''):h.update(b)
 return h.hexdigest()
def assignment(path,nvars):
 vals={}
 for line in Path(path).read_text().splitlines():
  if line.startswith('v '):
   for x in map(int,line[2:].split()):
    if x:
     assert 1<=abs(x)<=nvars and abs(x) not in vals
     vals[abs(x)]=x>0
 assert set(vals)==set(range(1,nvars+1))
 return vals
ap=argparse.ArgumentParser();ap.add_argument('--base',type=Path,required=True);ap.add_argument('--assignment',type=Path,action='append',default=[]);ap.add_argument('--output',type=Path,required=True);ap.add_argument('--metadata',type=Path,required=True);a=ap.parse_args()
raw=a.base.read_bytes();lines=raw.splitlines(keepends=True)
header_indices=[i for i,line in enumerate(lines) if line.startswith(b'p cnf ')]
assert len(header_indices)==1
hi=header_indices[0];parts=lines[hi].split();assert parts[:2]==[b'p',b'cnf'] and len(parts)==4
nv,nc=int(parts[2]),int(parts[3]);prefix=b''.join(lines[:hi]);body=b''.join(lines[hi+1:])
assert body.endswith(b'\n')
models=[assignment(p,nv) for p in a.assignment]
blocks=[]
for values in models:
 lits=[-v if values[v] else v for v in range(1,361)]
 blocks.append((' '.join(map(str,lits))+' 0\n').encode())
a.output.parent.mkdir(parents=True,exist_ok=True)
with a.output.open('wb') as out:
 out.write(prefix);out.write(f'p cnf {nv} {nc+len(blocks)}\n'.encode());out.write(body)
 for b in blocks:out.write(b)
meta={'schema':'circdist-gross-round112-cumulative-direct-enumeration-cnf-v1','status':'PASS','base_cnf_sha256':sha(a.base),'base_variables':nv,'base_clauses':nc,'blocking_assignment_sha256':[sha(p) for p in a.assignment],'blocking_clause_count':len(blocks),'blocking_clause_width':360,'variables':nv,'clauses':nc+len(blocks),'output_cnf_sha256':sha(a.output),'exact_primary_blocking':True}
a.metadata.parent.mkdir(parents=True,exist_ok=True);a.metadata.write_text(json.dumps(meta,indent=2,sort_keys=True)+'\n');print(json.dumps(meta,sort_keys=True))
