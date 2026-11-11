#!/usr/bin/env python3
import hashlib,json,sys
from pathlib import Path
import yaml
repo=Path(sys.argv[1]).resolve();out=Path(sys.argv[2])
root_path=repo/'circdist/proof-dag/nodes/CIRCDIST.gross.yaml'
obj=yaml.safe_load(root_path.read_text())
paths=set(['DAG_PROTOCOL.md','FILE_PROTOCOL.md','operations/circdist/SCHEDULER.yaml',
 'circdist/artifacts/definitions/CIRCDIST_PROBLEMS.md',
 'circdist/proof-dag/nodes/CIRCDIST.gross.yaml',
 'circdist/proof-dag/nodes/CIRCDIST.gross.dext-cap.yaml',
 'circdist/proof-dag/nodes/CIRCDIST.gross.mc-equiv.yaml',
 'circdist/proof-dag/nodes/CIRCDIST.lift.iff.yaml',
 'circdist/artifacts/circdist_gross_cegar_round62_20260828',
 'circdist/artifacts/circdist_gross_pattern_cegar_round63_20260828'])
def walk(x):
 if isinstance(x,dict):
  for k,v in x.items():
   if k=='path' and isinstance(v,str):paths.add(v)
   walk(v)
 elif isinstance(x,list):
  for v in x:walk(v)
walk(obj)
def hfile(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def bind(rel):
 p=repo/rel
 if not p.exists():return {'path':rel,'exists':False}
 if p.is_file():return {'path':rel,'exists':True,'kind':'file','bytes':p.stat().st_size,'sha256':hfile(p)}
 rows=[]
 for q in sorted(x for x in p.rglob('*') if x.is_file()):
  rr=q.relative_to(repo).as_posix();rows.append({'path':rr,'bytes':q.stat().st_size,'sha256':hfile(q)})
 hh=hashlib.sha256()
 for r in rows:hh.update(f"{r['path']}\0{r['bytes']}\0{r['sha256']}\n".encode())
 return {'path':rel,'exists':True,'kind':'directory','file_count':len(rows),'bytes':sum(r['bytes'] for r in rows),'tree_sha256':hh.hexdigest(),'files':rows}
result={'schema':'circdist-round68-source-bindings-v1','repository_root_at_run':str(repo),
 'canonical_root_bound_sources':sorted(paths),'bindings':[bind(x) for x in sorted(paths)],
 'all_paths_exist':all((repo/x).exists() for x in paths)}
out.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
print('paths',len(paths),'all_exist',result['all_paths_exist'],'files',sum(1 if b.get('kind')=='file' else b.get('file_count',0) for b in result['bindings']))
