#!/usr/bin/env python3
from pathlib import Path
import argparse,datetime,hashlib,json,shutil,subprocess,sys
ap=argparse.ArgumentParser();ap.add_argument('--iteration',type=int,required=True);ap.add_argument('--engine-root',type=Path,required=True);ap.add_argument('--work-root',type=Path,required=True);ap.add_argument('--python',type=Path,required=True);a=ap.parse_args()
engine=a.engine_root.resolve();work=a.work_root.resolve();it=work/'cegar'/f'iter{a.iteration}';it.mkdir(parents=True,exist_ok=False);(it/'solver').mkdir();(it/'generalization').mkdir()
dynamic=work/'cegar/dynamic_blocks.json';general=work/'classification/installed_generalized_terms.json';registry=work/'classification/online_mechanism_registry.json'
shutil.copy2(dynamic,it/'dynamic_before.json');shutil.copy2(general,it/'generalized_before.json');shutil.copy2(registry,it/'mechanism_registry_before.json')
records=[]
def load(p):return json.loads(Path(p).read_text())
def sha(o):return hashlib.sha256(json.dumps(o,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def run(name,timeout,cmd,log=None):
 log=log or it/f'{name}.log';rec=it/f'{name}.run.json';full=[str(a.python),str(engine/'src/run_foreground.py'),'--timeout-seconds',str(timeout),'--log',str(log),'--record',str(rec),'--']+[str(x) for x in cmd]
 cp=subprocess.run(full,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True);r=load(rec);r['stage']=name;r['iteration']=a.iteration;records.append(r);print(cp.stdout.strip(),flush=True);return cp.returncode,r
rc,_=run('outer_build',180,[a.python,engine/'src/build_online_candidate.py','--iteration',a.iteration,'--output',it,'--dynamic-blocks',dynamic,'--generalized-terms',general,'--z3-timeout-ms',120000])
if rc!=0:raise SystemExit(f'outer wrapper failed {rc}')
ores=load(it/'outer_result.json')
if ores['status']!='SAT':
 out={'schema':'round76-online-iteration-outcome-v1','iteration':a.iteration,'outer_status':ores['status'],'reason_unknown':ores.get('reason_unknown'),'branch_closed':False,
      'accepted_outer_exhaustion_proof':False,'stop_reason':'outer result is not SAT; UNKNOWN/timeout has no conclusion and no proof-producing equivalent outer proof is present','process_records':records}
 (it/'iteration_outcome.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps(out,sort_keys=True));raise SystemExit(30)
rc,_=run('outer_independent_replay',240,[a.python,engine/'src/verify_online_outer.py','--iteration-root',it,'--output',it/'outer_independent_replay.json'])
if rc!=0:raise SystemExit(f'outer independent replay failed {rc}')
solver=engine/'tooling/cadical-1.9.5-arm64-macos';statuses={}
for lab in ('Xerr','Zerr'):
 rc,r=run(f'{lab}_solver',660,[solver,'-t','600','--no-binary',it/'direct360'/f'{lab}.cnf'],it/'solver'/f'{lab}.solver.log')
 statuses[lab]='TIMEOUT' if r['timed_out'] else ('SAT' if r['exit_code']==10 else ('UNSAT_UNPROVED' if r['exit_code']==20 else f"UNKNOWN_EXIT_{r['exit_code']}"))
if not all(x=='SAT' for x in statuses.values()):
 gate={'schema':'round76-direct-nonsat-gate-v1','iteration':a.iteration,'sector_first_run_statuses':statuses,'accepted_absence':{},'repair_entered':False,'branch_closed':False,
       'policy':'UNSAT requires retained DRAT and LRAT plus independent valid/corrupt/truncated controls; timeout and UNKNOWN have no conclusion'}
 # Preserve candidate-specific proof material whenever the first run returned UNSAT.
 for lab in ('Xerr','Zerr'):
  if statuses[lab]!='UNSAT_UNPROVED':continue
  cnf=it/'direct360'/f'{lab}.cnf';drat=it/'solver'/f'{lab}.drat';lrat=it/'solver'/f'{lab}.lrat'
  rc,pr=run(f'{lab}_proof_solver',660,[solver,'-t','600','--no-binary',cnf,drat],it/'solver'/f'{lab}.proof_solver.log')
  if pr['exit_code']!=20 or pr['timed_out'] or not drat.exists():gate['accepted_absence'][lab]=False;statuses[lab]='UNSAT_PROOF_RUN_FAILED';continue
  dratc=engine/'tooling/drat-trim-arm64-macos';lratc=engine/'tooling/lrat-check-arm64-macos'
  rc,dr=run(f'{lab}_drat_check',600,[dratc,cnf,drat,'-t','590','-L',lrat]);rc2,lr=run(f'{lab}_lrat_check',600,[lratc,cnf,lrat])
  # Corrupt/truncated controls are generated deterministically from the accepted proof candidates.
  db=drat.read_bytes().splitlines(keepends=True);lb=lrat.read_bytes().splitlines(keepends=True);dcor=it/'solver'/f'{lab}.corrupt_truncated_10_lines.drat';lcor=it/'solver'/f'{lab}.corrupt_truncated_10_lines.lrat';dcor.write_bytes(b''.join(db[:10]));lcor.write_bytes(b''.join(lb[:10]))
  rc3,dc=run(f'{lab}_drat_corrupt_check',120,[dratc,cnf,dcor,'-t','110']);rc4,lc=run(f'{lab}_lrat_corrupt_check',120,[lratc,cnf,lcor])
  accepted=dr['exit_code']==0 and lr['exit_code']==0 and dc['exit_code']!=0 and lc['exit_code']!=0
  gate['accepted_absence'][lab]=accepted;statuses[lab]='UNSAT_PROOFS_ACCEPTED' if accepted else 'UNSAT_PROOF_OR_CONTROL_REJECTED'
 gate['sector_final_statuses']=statuses;gate['repair_entered']=all(statuses.get(x)=='UNSAT_PROOFS_ACCEPTED' for x in ('Xerr','Zerr'))
 gate['stop_reason']='dual checked absence reached repair gate' if gate['repair_entered'] else 'mixed, unknown, timeout, or unaccepted absence; no repair and no branch closure'
 (it/'direct_nonsat_gate.json').write_text(json.dumps(gate,indent=2,sort_keys=True)+'\n');out={'schema':'round76-online-iteration-outcome-v1','iteration':a.iteration,'outer_status':'SAT','sector_statuses':statuses,'accepted_absence':gate['accepted_absence'],
  'repair_entered':gate['repair_entered'],'branch_closed':False,'stop_reason':gate['stop_reason'],'process_records':records};(it/'iteration_outcome.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps(out,sort_keys=True));raise SystemExit(31 if not gate['repair_entered'] else 32)
rc,_=run('direct_replay',240,[a.python,engine/'src/replay_direct_candidate.py','--root',it,'--output',it/'direct_verification.json'])
if rc!=0:raise SystemExit(f'direct raw replay failed {rc}')
before_dyn=len(load(it/'dynamic_before.json'));before_gen=load(it/'generalized_before.json')['term_count']
rc,_=run('append_candidate_exact',120,[a.python,engine/'src/append_dynamic_blocks.py','--verification',it/'direct_verification.json','--dynamic-blocks',dynamic,'--iteration',a.iteration])
if rc!=0:raise SystemExit(f'exact append failed {rc}')
rc,_=run('online_generalization',3600,[a.python,engine/'src/generalize_online.py','--root',engine,'--iteration-root',it,'--generalized-state',general,'--registry-state',registry,'--output-root',it/'generalization'])
if rc!=0:raise SystemExit(f'online generalization failed {rc}')
gen=load(it/'generalization/install_result.json');after_dyn=len(load(dynamic));after_gen=load(general)['term_count'];shutil.copy2(dynamic,it/'dynamic_after.json');shutil.copy2(general,it/'generalized_after.json');shutil.copy2(registry,it/'mechanism_registry_after.json')
ver=load(it/'direct_verification.json');out={'schema':'round76-online-iteration-outcome-v1','iteration':a.iteration,'outer_status':'SAT','outer_seconds':ores['seconds'],'candidate_sha256':ver['candidate_sha256'],
 'installed_blocks_before':1440+20+before_gen+before_dyn,'dynamic_blocks_before':before_dyn,'generalized_terms_before':before_gen,
 'sector_statuses':{s:ver['sectors'][s]['status'] for s in ('Xerr','Zerr')},'sector_fault_weights':{s:ver['sectors'][s]['mechanism']['fault_count'] for s in ('Xerr','Zerr')},
 'all_dimacs_clauses_satisfied':{s:ver['sectors'][s]['all_dimacs_clauses_satisfied'] for s in ('Xerr','Zerr')},'raw_replay_passed':True,
 'candidate_exact_blocks_added':2,'dynamic_blocks_after':after_dyn,'online_generalized_retained_increment':gen['retained_increment'],'generalized_terms_after':after_gen,
 'installed_blocks_after':1440+20+after_gen+after_dyn,'accepted_absence_proofs':0,'repair_entered':False,'branch_closed':False,
 'strict_stage_order':['outer_build','outer_independent_replay','Xerr_solver','Zerr_solver','direct_replay','append_candidate_exact','online_generalization'],
 'process_records':records};assert after_dyn==before_dyn+2 and after_gen==before_gen+gen['retained_increment'];(it/'iteration_outcome.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps(out,sort_keys=True))
