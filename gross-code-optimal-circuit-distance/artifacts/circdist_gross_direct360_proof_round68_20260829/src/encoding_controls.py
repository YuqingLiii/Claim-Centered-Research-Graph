#!/usr/bin/env python3
from __future__ import annotations
import itertools,json,sys
from pathlib import Path
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE))
from round68_build import Encoder
from pysat.solvers import Solver

def check_atmost(n,k):
 e=Encoder('control','none');x=[e.var(f'x{i}','control',{'i':i}) for i in range(n)];e.atmost(x,k)
 cls=[c['lits'] for c in e.clauses];rows=[]
 with Solver(name='cadical195',bootstrap_with=cls) as s:
  for bits in itertools.product((0,1),repeat=n):
   assumptions=[x[i] if bits[i] else -x[i] for i in range(n)]
   sat=s.solve(assumptions=assumptions);expected=sum(bits)<=k
   assert sat==expected;rows.append({'bits':bits,'sat':sat,'expected':expected})
 return {'n':n,'k':k,'assignments':len(rows),'all_match':True,'variables':len(e.vars),'clauses':len(e.clauses)}
def check_xor():
 rows=[]
 for av,bv in itertools.product((0,1),repeat=2):
  e=Encoder('control','none');a=e.var('a','control',{});b=e.var('b','control',{});y=e.var('y','control',{});e.xor_link(a,b,y,{})
  cls=[c['lits'] for c in e.clauses]
  with Solver(name='cadical195',bootstrap_with=cls) as s:
   for yv in (0,1):
    sat=s.solve(assumptions=[a if av else -a,b if bv else -b,y if yv else -y])
    assert sat==(yv==(av^bv));rows.append({'a':av,'b':bv,'y':yv,'sat':sat})
 return {'rows':rows,'all_match':True}
out={'schema':'circdist-round68-encoding-controls-v1','xor2':check_xor(),'atmost_controls':[check_atmost(5,0+1),check_atmost(5,2),check_atmost(6,5)]}
Path(sys.argv[1]).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
print(json.dumps(out['atmost_controls']))
