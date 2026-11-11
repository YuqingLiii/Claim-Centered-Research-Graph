#!/usr/bin/env python3
from pathlib import Path
import argparse,hashlib,json
p=argparse.ArgumentParser();p.add_argument('--cnf',type=Path,required=True);p.add_argument('--solver-log',type=Path,required=True);p.add_argument('--assignment',type=Path,required=True);p.add_argument('--output',type=Path,required=True);a=p.parse_args()
def sha(p):
 h=hashlib.sha256()
 with p.open('rb') as f:
  for b in iter(lambda:f.read(1<<20),b''):h.update(b)
 return h.hexdigest()
status=[];lits=[]
for line in a.solver_log.read_text().splitlines():
 if line.startswith('s '):status.append(line[2:].strip())
 if line.startswith('v '):
  for z in map(int,line[2:].split()):
   if z:lits.append(z)
assert status and status[-1]=='SATISFIABLE',status
with a.cnf.open() as f:
 while True:
  line=f.readline()
  assert line
  if line.startswith('c') or not line.strip():continue
  h=line.split();assert h[:2]==['p','cnf'];nvars,nclauses=map(int,h[2:]);break
assert len(lits)==nvars,(len(lits),nvars)
assert {abs(x) for x in lits}==set(range(1,nvars+1))
assert len({abs(x) for x in lits})==nvars
vals=bytearray(nvars+1)
for x in lits: vals[abs(x)]=1 if x>0 else 0
seen=0
with a.cnf.open() as f:
 for line in f:
  if line.startswith('c') or line.startswith('p ') or not line.strip():continue
  z=list(map(int,line.split()));assert z and z[-1]==0 and all(x for x in z[:-1]);seen+=1
  assert any(bool(vals[abs(x)])==(x>0) for x in z[:-1]),seen
assert seen==nclauses,(seen,nclauses)
a.assignment.parent.mkdir(parents=True,exist_ok=True)
with a.assignment.open('w',encoding='ascii',newline='\n') as out:
 for i in range(0,len(lits),16):out.write('v '+' '.join(map(str,lits[i:i+16]))+'\n')
 out.write('v 0\n')
out={'schema':'circdist-round94-complete-sat-assignment-check-v1','status':'PASS','solver_status':'SATISFIABLE','formula_sha256':sha(a.cnf),'solver_log_sha256':sha(a.solver_log),'assignment_sha256':sha(a.assignment),'variables':nvars,'assigned_variables':len(lits),'clauses':nclauses,'checked_clauses':seen,'all_variables_assigned_exactly_once':True,'all_dimacs_clauses_satisfied':True}
a.output.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps(out,sort_keys=True))
