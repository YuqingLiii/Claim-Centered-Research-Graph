#!/usr/bin/env python3
from __future__ import annotations
from pathlib import Path
import argparse,gzip,hashlib,json,sys,time

ROOT=Path(__file__).resolve().parent.parent
sys.path[:0]=[str(ROOT/'src/round63_src'),str(ROOT/'src')]
import model as M, round68_build as B
from outer import OuterScheduler

def load(p):
 p=Path(p);p=p if p.exists() else Path(str(p)+'.gz');b=p.read_bytes();return json.loads(gzip.decompress(b) if p.suffix=='.gz' else b)
def dump(p,o):
 p=Path(p);p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(o,indent=2,sort_keys=True)+'\n')
def sha(o):return hashlib.sha256(json.dumps(o,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def sha_bytes(b):return hashlib.sha256(b).hexdigest()

ap=argparse.ArgumentParser();ap.add_argument('--iteration',type=int,required=True);ap.add_argument('--output',type=Path,required=True)
ap.add_argument('--dynamic-blocks',type=Path,required=True);ap.add_argument('--generalized-terms',type=Path,required=True)
ap.add_argument('--registry-state',type=Path,required=True);ap.add_argument('--raw-mechanisms-state',type=Path,required=True)
ap.add_argument('--z3-timeout-ms',type=int,default=120000);a=ap.parse_args()
out=a.output;out.mkdir(parents=True,exist_ok=True)
px,pz,lx,lz=B.load_context();rx,_=B.global_single_records('Xerr',M.Xchecks,px,'X');rz,_=B.global_single_records('Zerr',M.Zchecks,pz,'Z');unary=rx+rz
r62=load(ROOT/'src/round62_cegar20.json');B.replay_round62_blocks(r62,lx,lz)
gens=load(a.generalized_terms);dyn=load(a.dynamic_blocks);registry=load(a.registry_state);raw_mechanisms=load(a.raw_mechanisms_state)
assert gens['term_count']==len(gens['terms']) and gens['reviewed_round69_terms']==4740 and gens['reviewed_round72_terms']==566
assert gens['round74_retained_terms']==134
assert gens.get('round76_retained_terms',0)==303
assert gens['term_count']==5743+gens.get('round78_cross_registry_terms',0)+gens.get('round78_online_terms',0)+gens.get('round80_whole_registry_terms',0)
assert a.iteration>=78 and len(dyn)==156+2*(a.iteration-78),(a.iteration,len(dyn))
assert registry['mechanism_count']==len(registry['mechanisms'])==72+2*(a.iteration-78)
assert raw_mechanisms['mechanism_count']==len(raw_mechanisms['mechanisms'])==registry['mechanism_count']
assert {m['mechanism_id'] for m in raw_mechanisms['mechanisms']}=={m['mechanism_id'] for m in registry['mechanisms']}
outer=OuterScheduler(True)
for i,r in enumerate(unary):outer.add_block([tuple(x) for x in r['atoms']],f'r63-{i}')
for b in r62['outer_blocks']:outer.add_block([tuple(x) for x in b['atoms']],'r62-'+b['tag'],b['trace_sha256'])
for t in gens['terms']:outer.add_block([tuple(x) for x in t['atoms']],t['term_id'],t.get('source_term_sha256'))
for i,b in enumerate(dyn):outer.add_block([tuple(x) for x in b['atoms']],f"dynamic-{i}-{b['sector']}",b.get('mechanism_sha256'))
assert len(outer.blocks)==1440+20+len(gens['terms'])+len(dyn)
smt=outer.s.to_smt2();(out/'outer.smt2').write_text(smt)
solved=outer.solve(a.z3_timeout_ms);dump(out/'outer_result.json',solved)
counts={'round63_single':1440,'round62':20,'round69_generalized':4740,'round72_generalized':566,
        'round74_online_generalized':gens['round74_retained_terms'],'round76_online_generalized':gens.get('round76_retained_terms',0),
        'round78_cross_registry_generalized':gens.get('round78_cross_registry_terms',0),'round78_online_generalized':gens.get('round78_online_terms',0),'round80_whole_registry_generalized':gens.get('round80_whole_registry_terms',0),'merged_generalized':len(gens['terms']),
        'dynamic_exact':len(dyn),'total':len(outer.blocks),'exploratory_round63_pair':0}
if solved['status']!='SAT':
 dump(out/'outer_terminal.json',{'schema':'round78-outer-terminal-v1','iteration':a.iteration,'status':solved['status'],
      'reason_unknown':solved.get('reason_unknown'),'asserted_blocks':counts,'absence_or_exhaustion_accepted':False})
 print(json.dumps({'iteration':a.iteration,'status':solved['status'],'blocks':len(outer.blocks),'seconds':solved['seconds'],'reason_unknown':solved.get('reason_unknown')},sort_keys=True));raise SystemExit(0)
times=solved.pop('compressed_schedule');audit=M.audit_schedule(times,True)
assert audit['ok'] and audit['global_interleaved'] and audit['edge_count']==864 and audit['overlaps']==648 and not audit['conflicts'] and not audit['mc_violations']
assert all(not M.block_holds(times,[tuple(x) for x in t['atoms']]) for t in gens['terms'])
assert all(not M.block_holds(times,[tuple(x) for x in b['atoms']]) for b in dyn)
assert all(not M.block_holds(times,[tuple(x) for x in r['atoms']]) for r in unary)
assert all(not M.block_holds(times,[tuple(x) for x in b['atoms']]) for b in r62['outer_blocks'])
ss=B.sectors(times,lx,lz)
cand={'schema':'round78-cross-registry-online-generalizing-candidate-v1','iteration':a.iteration,'schedule_sha256':sha(times),'schedule_times':times,
      'schedule_times_sorted':[{'edge':e,'time':times[e]} for e in sorted(times)],'audit':audit,
      'order_bindings':{'X':B.order_bindings(times,'X',M.Xchecks),'Z':B.order_bindings(times,'Z',M.Zchecks)},
      'outer':solved,'outer_smt2_sha256':sha_bytes(smt.encode()),'asserted_blocks':counts,
      'state_bindings':{'dynamic_before_sha256':sha(dyn),'dynamic_before_count':len(dyn),'generalized_before_sha256':sha(gens),'generalized_before_count':len(gens['terms']),
       'registry_before_sha256':sha(registry),'registry_before_count':registry['mechanism_count'],'raw_mechanisms_before_sha256':sha(raw_mechanisms),'raw_mechanisms_before_count':raw_mechanisms['mechanism_count']},
      'model_metadata':M.model_metadata(px,pz,lx,lz),'actual_primary_domain':{'per_sector_total':360,'data_singletons':144,'residual_elementary_fault_columns':216,'residuals_per_check':3,'checks':72,'weight12_pool_is_not_primary_domain':True},'pool_bindings':{'Xerr_pool_count':len(px),'Zerr_pool_count':len(pz),
       'Xerr_pool_sha256':sha(px),'Zerr_pool_sha256':sha(pz),'X_logical_basis':[M.bits(x) for x in lx],'Z_logical_basis':[M.bits(x) for x in lz]},
      'columns':{lab:[B.column_public(sec,col) for col in sec.columns] for lab,sec in ss.items()}}
dump(out/'candidate.json',cand)
for lab in ('Xerr','Zerr'):B.build_direct_cnf(ss[lab],out/'direct360'/lab,cand['schedule_sha256'],10)
print(json.dumps({'iteration':a.iteration,'status':'SAT','schedule_sha256':cand['schedule_sha256'],'blocks':len(outer.blocks),'outer_seconds':solved['seconds'],'audit':audit},sort_keys=True))
