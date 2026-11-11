#!/usr/bin/env python3
"""Remove superseded caches and assert the Round108 fresh/frontier cleanup contract."""
from pathlib import Path
import argparse, json, shutil
ap=argparse.ArgumentParser(); ap.add_argument('--root',type=Path,required=True); ap.add_argument('--output',type=Path,required=True); a=ap.parse_args(); r=a.root.resolve()
removed=[]
for p in sorted(r.rglob('__pycache__'),key=lambda x:len(x.parts),reverse=True):
 if p.is_dir():
  removed.append(p.relative_to(r).as_posix()); shutil.rmtree(p)
for p in sorted(r.rglob('*.pyc')):
 removed.append(p.relative_to(r).as_posix()); p.unlink()
for p in sorted(r.rglob('.DS_Store')):
 removed.append(p.relative_to(r).as_posix()); p.unlink()
raw=[r/'solver/iter189/outer.drat',r/'solver/iter189/direct/solver/Xerr.drat',r/'solver/iter189/direct/solver/Zerr.drat']
assert not any(p.exists() for p in raw)
for p in (r/'solver/iter189/outer.drat.gz',r/'solver/iter189/direct/solver/Xerr.drat.gz',r/'solver/iter189/direct/solver/Zerr.drat.gz'): assert p.is_file()
for q in (r/'frontier/iter190_full_invariant',r/'frontier/iter190_full_invariant_quotient'):
 forbidden=[p.relative_to(r).as_posix() for p in q.rglob('*') if p.is_file() and any(x in p.name.lower() for x in ('assignment','solver','model','.drat','.lrat'))]
 assert not forbidden,forbidden
left=[p.relative_to(r).as_posix() for p in r.rglob('*') if p.name=='__pycache__' or p.suffix=='.pyc']
assert not left,left
out={'schema':'circdist-gross-round108-cleanup-v1','status':'PASS','removed':removed,'removed_count':len(removed),'raw_solver_streams_removed':3,'verified_gzip_streams':3,'fresh_frontier_forbidden_artifacts':[],'remaining_python_caches':[]}
a.output.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n'); print(json.dumps({'status':'PASS','removed':len(removed),'raw_solver_streams_absent':3,'fresh_forbidden':0},sort_keys=True))
