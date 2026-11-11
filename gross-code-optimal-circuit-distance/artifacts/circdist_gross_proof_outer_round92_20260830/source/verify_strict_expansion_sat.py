#!/usr/bin/env python3
from pathlib import Path
import argparse,gzip,hashlib,json,sys

def load(p):
 b=Path(p).read_bytes();return json.loads(gzip.decompress(b) if str(p).endswith('.gz') else b)
def shaf(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def sho(o):return hashlib.sha256(json.dumps(o,sort_keys=True,separators=(',',':')).encode()).hexdigest()
ap=argparse.ArgumentParser();ap.add_argument('--solver-log',type=Path,required=True);ap.add_argument('--cnf',type=Path,required=True);ap.add_argument('--source',type=Path,required=True);ap.add_argument('--metadata',type=Path,required=True);ap.add_argument('--vendor',type=Path,required=True);ap.add_argument('--old-count',type=int,required=True);ap.add_argument('--assignment',type=Path,required=True);ap.add_argument('--candidate',type=Path,required=True);ap.add_argument('--output',type=Path,required=True);a=ap.parse_args()
S=load(a.source);M=load(a.metadata);lines=a.solver_log.read_text().splitlines();assert 's SATISFIABLE' in lines
signed=[]
for line in lines:
 if line.startswith('v '):signed += [int(x) for x in line.split()[1:] if x!='0']
assert len(signed)==M['variables'] and {abs(x) for x in signed}==set(range(1,M['variables']+1))
truth=bytearray(M['variables']+1)
for x in signed:truth[abs(x)]=x>0
assert truth[M['constant_variable']]
a.assignment.write_text('s SATISFIABLE\n'+'\n'.join('v '+' '.join(map(str,signed[i:i+20]))+(' 0' if i+20>=len(signed) else '') for i in range(0,len(signed),20))+'\n')
with a.cnf.open() as f:
 h=f.readline().split();nv,nc=map(int,h[2:]);assert nv==M['variables'];checked=0
 for line in f:
  c=list(map(int,line.split()));assert c[-1]==0 and any(bool(truth[abs(x)])==(x>0) for x in c[:-1]);checked+=1
assert checked==nc
word=lambda bits:sum((1<<i) for i,v in enumerate(bits) if truth[v])
raw={e:word(bits) for e,bits in M['time_bit_variables'].items()};vals=sorted(set(raw.values()));rm={v:i for i,v in enumerate(vals)};times={e:rm[v] for e,v in raw.items()}
P=a.vendor.resolve();sys.path[:0]=[str(P/'src/round63_src'),str(P/'src')]
import model,round68_build as builder
assert model.audit_schedule(times,True)['ok'];_,_,lx,lz=builder.load_context();sectors=builder.sectors(times,lx,lz)
valid=[];details=[]
for i,s in enumerate(S['selectors']):
 v=model.verify_named_selection(sectors[s['sector']],s['selected_names'],10)
 valid.append(v['ok'])
 if i>=a.old_count and v['ok']:
  sec=sectors[s['sector']];by={c.name:c for c in sec.columns};can=0;phys=0
  for n in s['selected_names']:can^=by[n].support;phys^=by[n].physical_support
  cs=sec.syndrome_of(can);ps=sec.syndrome_of(phys)
  cp=[(bin(can&l).count("1")&1) for l in sec.logical_duals];pp=[(bin(phys&l).count("1")&1) for l in sec.logical_duals]
  assert cs==ps==0 and any(cp) and cp==pp and v['nontrivial']
  details.append({'selector_index':i,'mechanism_id':s['mechanism_id'],'sector':s['sector'],'fault_count':len(s['selected_names']),'selected_names':s['selected_names'],'canonical_support':[q for q in range(144) if can>>q&1],'physical_support':[q for q in range(144) if phys>>q&1],'syndrome':[],'logical_bits_lsb_first':cp,'canonical_physical_parities_equal':True,'named_replay':v})
assert not any(valid[:a.old_count]) and any(valid[a.old_count:])
cand={'schema':'round92-strict-expansion-sat-candidate-v1','raw_times':raw,'compressed_times':times,'raw_used_layers':len(vals),'compressed_schedule_sha256':sho(times),'cnf_sha256':shaf(a.cnf),'assignment_sha256':shaf(a.assignment)};a.candidate.write_text(json.dumps(cand,indent=2,sort_keys=True)+'\n')
out={'schema':'round92-strict-expansion-sat-verification-v1','status':'PASS','solver_status':'SATISFIABLE','complete_assignment_variables':len(signed),'all_dimacs_clauses_satisfied':True,'dimacs_clauses_checked':checked,'frozen_schedule_audit':model.audit_schedule(times,True),'old_selector_count':a.old_count,'old_valid_count':sum(valid[:a.old_count]),'new_selector_count':len(valid)-a.old_count,'new_valid_count':sum(valid[a.old_count:]),'new_valid_mechanisms':details,'strict_old_union_expansion_witness':True,'candidate_schedule_sha256':cand['compressed_schedule_sha256'],'assignment_sha256':cand['assignment_sha256'],'query_cnf_sha256':cand['cnf_sha256'],'solver_log_sha256':shaf(a.solver_log)}
a.output.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps({k:out[k] for k in ('status','dimacs_clauses_checked','old_valid_count','new_valid_count','candidate_schedule_sha256','assignment_sha256','query_cnf_sha256','solver_log_sha256')},sort_keys=True))
