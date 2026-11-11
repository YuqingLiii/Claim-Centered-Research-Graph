#!/usr/bin/env python3
import argparse,json,time
from pysat.formula import CNF
from pysat.solvers import Solver
p=argparse.ArgumentParser();p.add_argument('--cnf',required=True);p.add_argument('--solver',default='glucose42');p.add_argument('--output',required=True);a=p.parse_args()
f=CNF(from_file=a.cnf);t=time.time()
with Solver(name=a.solver,bootstrap_with=f.clauses) as s:
 ans=s.solve();model=s.get_model() if ans else None;stats=s.accum_stats()
out={'solver':a.solver,'status':'SAT' if ans else 'UNSAT','seconds':time.time()-t,'variables':f.nv,'clauses':len(f.clauses),'model':model,'stats':stats}
open(a.output,'w').write(json.dumps(out,indent=2,sort_keys=True)+'\n')
