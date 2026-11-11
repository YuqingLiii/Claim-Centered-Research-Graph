from pathlib import Path
import sys,json,time,argparse
R=Path('<repo>/circdist/artifacts/circdist_gross_direct360_proof_round68_20260829')
sys.path[:0]=[str(R/'src/round63_src'),str(R/'src')]
import model as M,round68_build as B
from pysat.formula import IDPool
from pysat.card import CardEnc,EncType
from pysat.solvers import Solver
ap=argparse.ArgumentParser();ap.add_argument('lab');ap.add_argument('output');a=ap.parse_args();lab=a.lab
px,pz,lx,lz=B.load_context();det=M.HZ if lab=='Xerr' else M.HX;stabs=M.HX if lab=='Xerr' else M.HZ;dual=lz if lab=='Xerr' else lx
Rs=[int(x) for x in Path('/tmp/circdist_round69_work_20260829_a/'+lab+'_w14_needed_good.txt').read_text().split()]
p=IDPool();x=[p.id(('x',q)) for q in range(144)];clauses=[]
for h in det:M.xor_chain(p,[x[q] for q in M.bits(h)],clauses,0)
lvs=[]
for i,l in enumerate(dual):
 lv=p.id(('l',i));M.xor_chain(p,[x[q] for q in M.bits(l)]+[lv],clauses,0);lvs.append(lv)
clauses.append(lvs);enc=CardEnc.equals(lits=x,bound=14,top_id=p.top,encoding=EncType.seqcounter);clauses.extend(enc.clauses)
found={};negative=[];t=time.monotonic()
with Solver(name='cadical195',bootstrap_with=clauses) as s:
 for i,rr in enumerate(Rs):
  sat=s.solve(assumptions=[x[q] for q in M.bits(rr)])
  if sat:
   pos={z for z in s.get_model() if z>0};V=sum(1<<q for q in range(144) if x[q] in pos)
   assert M.popcount(V)==14 and V&rr==rr and all(M.popcount(V&h)%2==0 for h in det) and not M.inspan(V,stabs)
   found[str(rr)]={'support':M.bits(V),'mask_hex':hex(V),'logical_parities':[M.popcount(V&z)&1 for z in dual]}
  else:negative.append(rr)
  if (i+1)%250==0:print(lab,i+1,'found',len(found),'sec',round(time.monotonic()-t,2),flush=True)
obj={'schema':'round69-weight14-individual-complete-v1','sector':lab,'candidate_R_count':len(Rs),'positive_R_count':len(found),'negative_R_count':len(negative),'all_queries_decided':len(found)+len(negative)==len(Rs),'seconds':time.monotonic()-t,'variables':max(p.top,enc.nv),'clauses':len(clauses),'weight14_completions':found,'negative_R_masks_hex':[hex(r) for r in negative]}
Path(a.output).write_text(json.dumps(obj,indent=2,sort_keys=True)+'\n');print(json.dumps({k:v for k,v in obj.items() if k not in ('weight14_completions','negative_R_masks_hex')},sort_keys=True),flush=True)
