#!/usr/bin/env python3
from pathlib import Path
import argparse,gzip,hashlib,json,sys,time
ap=argparse.ArgumentParser();ap.add_argument('--engine-root',type=Path,required=True);ap.add_argument('--iteration-root',type=Path,required=True);ap.add_argument('--dynamic-before',type=Path,required=True);ap.add_argument('--output',type=Path,required=True);a=ap.parse_args();root=a.engine_root.resolve();sys.path[:0]=[str(root/'src/round63_src'),str(root/'src')]
import z3
import model as M,round68_build as B
from outer import OuterScheduler
def load(p):
 p=Path(p)
 if p.suffix=='.gz':
  with gzip.open(p,'rt') as f:return json.load(f)
 return json.loads(p.read_text())
def sha_obj(o):return hashlib.sha256(json.dumps(o,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def sha_bytes(b):return hashlib.sha256(b).hexdigest()
t0=time.monotonic();it=a.iteration_root;cand=load(it/'candidate.json');ores=load(it/'outer_result.json');dyn=load(a.dynamic_before);iteration=int(cand['iteration']);assert len(dyn)==60+2*(iteration-30)
px,pz,lx,lz=B.load_context();rx,_=B.global_single_records('Xerr',M.Xchecks,px,'X');rz,_=B.global_single_records('Zerr',M.Zchecks,pz,'Z');records=rx+rz;assert len(records)==1440
r62=load(root/'src/round62_cegar20.json');B.replay_round62_blocks(r62,lx,lz);assert len(r62['outer_blocks'])==20
old=load(root/'classification/round69_pair_classification.json.gz')['pairs'];oldgen=[(f"r69-{p['sector']}-{p['a']}-{p['b']}-{j}",[tuple(x) for x in term['atoms']]) for p in old for j,term in enumerate(p['deletion_minimal_terms'])];assert len(oldgen)==4740
new=load(root/'classification/retained_terms.json.gz' if (root/'classification/retained_terms.json.gz').exists() else root/'classification/retained_terms.json')['terms'];newgen=[(x['term_id'],[tuple(y) for y in x['atoms']]) for x in new];assert len(newgen)==566
outer=OuterScheduler(True)
for j,r in enumerate(records):outer.add_block([tuple(x) for x in r['atoms']],f'r63-{j}')
for b in r62['outer_blocks']:outer.add_block([tuple(x) for x in b['atoms']],'r62-'+b['tag'],b['trace_sha256'])
for tag,atoms in oldgen+newgen:outer.add_block(atoms,tag)
for j,b in enumerate(dyn):outer.add_block([tuple(x) for x in b['atoms']],f"dynamic-{j}-{b['sector']}",b.get('mechanism_sha256'))
smt=outer.s.to_smt2().encode();saved=(it/'outer.smt2').read_bytes();assert smt==saved
assert ores['status']=='SAT';times={k:int(v) for k,v in cand['schedule_times'].items()};assert ores['compressed_schedule']==times
assert set(times)==set(M.ALL_EDGES) and len(times)==864 and len(M.OVERLAPS)==648
audit=M.audit_schedule(times,True);assert audit==cand['audit'] and audit['ok'] and audit['mc_violations']==[] and audit['conflicts']==[] and audit['global_interleaved'] and audit['min_time']==0 and audit['max_time']==audit['used_layers']-1
fixed=z3.Solver();fixed.add(z3.parse_smt2_string(saved.decode()))
for e in M.ALL_EDGES:fixed.add(z3.Int('t_'+e.replace(':','_'))==times[e])
assert fixed.check()==z3.sat and len(outer.blocks)==6766+len(dyn)
assert cand['asserted_blocks']=={'round63_single':1440,'round62':20,'round69_generalized':4740,'round72_generalized':566,'dynamic_exact':len(dyn),'total':6766+len(dyn),'exploratory_round63_pair':0}
for _,atoms in oldgen+newgen:assert not M.block_holds(times,atoms)
for b in dyn:assert not M.block_holds(times,[tuple(x) for x in b['atoms']])
for r in records:assert not M.block_holds(times,[tuple(x) for x in r['atoms']])
for b in r62['outer_blocks']:assert not M.block_holds(times,[tuple(x) for x in b['atoms']])
assert sha_obj(times)==cand['schedule_sha256'] and sha_bytes(saved)==cand['outer_smt2_sha256']==ores['smt2_sha256']
assert cand['order_bindings']=={'X':B.order_bindings(times,'X',M.Xchecks),'Z':B.order_bindings(times,'Z',M.Zchecks)}
ss=B.sectors(times,lx,lz);cols={lab:[B.column_public(sec,col) for col in sec.columns] for lab,sec in ss.items()};assert cand['columns']==cols and all(len(v)==360 for v in cols.values())
out={'schema':'round72-independent-outer-replay-v1','status':'PASS','iteration':iteration,'schedule_sha256':cand['schedule_sha256'],'outer_smt2_sha256':sha_bytes(saved),'serialized_formula_fixed_model_status':'SAT','named_edge_count':864,'mc_constraint_count':648,'block_counts':cand['asserted_blocks'],'schedule_audit':audit,'sector_column_counts':{k:len(v) for k,v in cols.items()},'logical_pool_counts':{'Xerr':len(px),'Zerr':len(pz)},'wall_seconds':time.monotonic()-t0};a.output.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps(out,sort_keys=True))
