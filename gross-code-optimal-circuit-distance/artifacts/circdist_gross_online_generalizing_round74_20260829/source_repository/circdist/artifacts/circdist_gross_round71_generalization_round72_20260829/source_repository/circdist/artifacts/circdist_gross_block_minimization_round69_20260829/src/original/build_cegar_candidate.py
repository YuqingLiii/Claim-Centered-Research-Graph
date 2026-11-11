from pathlib import Path
import sys,json,hashlib,argparse,time
R68=Path('<repo>/circdist/artifacts/circdist_gross_direct360_proof_round68_20260829')
SCR=Path('/tmp/circdist_round69_work_20260829_a')
sys.path[:0]=[str(R68/'src/round63_src'),str(R68/'src')]
import model as M,pattern as P,round68_build as B
from outer import OuterScheduler

def dump(p,o):p=Path(p);p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(o,indent=2,sort_keys=True)+'\n')
def sha(o):return hashlib.sha256(json.dumps(o,sort_keys=True,separators=(',',':')).encode()).hexdigest()
ap=argparse.ArgumentParser();ap.add_argument('--iteration',type=int,required=True);ap.add_argument('--output',required=True);ap.add_argument('--dynamic-blocks',required=True);a=ap.parse_args();out=Path(a.output);out.mkdir(parents=True,exist_ok=True)
px,pz,lx,lz=B.load_context();rx,sx=B.global_single_records('Xerr',M.Xchecks,px,'X');rz,sz=B.global_single_records('Zerr',M.Zchecks,pz,'Z');records=rx+rz
r62=json.loads((R68/'src/round62_cegar20.json').read_text());B.replay_round62_blocks(r62,lx,lz)
pairs=json.loads((SCR/'pair_classification.json').read_text())['pairs'];general=[(f"r69-{p['sector']}-{p['a']}-{p['b']}-{i}",[tuple(x) for x in t['atoms']]) for p in pairs for i,t in enumerate(p['deletion_minimal_terms'])]
dyn=json.loads(Path(a.dynamic_blocks).read_text()) if Path(a.dynamic_blocks).exists() else []
outer=OuterScheduler(True)
for i,r in enumerate(records):outer.add_block([tuple(x) for x in r['atoms']],f'r63-{i}')
for b in r62['outer_blocks']:outer.add_block([tuple(x) for x in b['atoms']],'r62-'+b['tag'],b['trace_sha256'])
for tag,atoms in general:outer.add_block(atoms,tag)
for i,b in enumerate(dyn):outer.add_block([tuple(x) for x in b['atoms']],f"dynamic-{i}-{b['sector']}",b.get('mechanism_sha256'))
assert len(outer.blocks)==1460+4740+len(dyn)
smt=outer.s.to_smt2();(out/'outer.smt2').write_text(smt)
solved=outer.solve(120000);dump(out/'outer_result.json',solved)
if solved['status']!='SAT':
 print(json.dumps({'iteration':a.iteration,'status':solved['status'],'blocks':len(outer.blocks),'seconds':solved['seconds'],'reason_unknown':solved.get('reason_unknown')}));raise SystemExit(0)
times=solved.pop('compressed_schedule');audit=M.audit_schedule(times,True);assert audit['ok'] and audit['global_interleaved']
assert all(not M.block_holds(times,[tuple(x) for x in t['atoms']]) for p in pairs for t in p['deletion_minimal_terms'])
ss=B.sectors(times,lx,lz);candidate={'schema':'round69-generalized-cegar-candidate-v1','iteration':a.iteration,'schedule_sha256':sha(times),'schedule_times':times,'schedule_times_sorted':[{'edge':e,'time':times[e]} for e in sorted(times)],'audit':audit,'order_bindings':{'X':B.order_bindings(times,'X',M.Xchecks),'Z':B.order_bindings(times,'Z',M.Zchecks)},'outer':solved,'outer_smt2_sha256':hashlib.sha256(smt.encode()).hexdigest(),'asserted_blocks':{'round63_single':1440,'round62':20,'round69_generalized':4740,'round69_dynamic':len(dyn),'total':len(outer.blocks),'exploratory_round63_pair':0},'model_metadata':M.model_metadata(px,pz,lx,lz),'pool_bindings':{'Xerr_pool_count':len(px),'Zerr_pool_count':len(pz),'Xerr_pool_sha256':sha(px),'Zerr_pool_sha256':sha(pz),'X_logical_basis':[M.bits(x) for x in lx],'Z_logical_basis':[M.bits(x) for x in lz]},'columns':{lab:[B.column_public(sec,col) for col in sec.columns] for lab,sec in ss.items()}}
dump(out/'candidate.json',candidate)
for lab in ('Xerr','Zerr'):B.build_direct_cnf(ss[lab],out/'direct360'/lab,candidate['schedule_sha256'],10)
print(json.dumps({'iteration':a.iteration,'status':'SAT','schedule_sha256':candidate['schedule_sha256'],'blocks':len(outer.blocks),'outer_seconds':solved['seconds'],'audit':audit},sort_keys=True))
