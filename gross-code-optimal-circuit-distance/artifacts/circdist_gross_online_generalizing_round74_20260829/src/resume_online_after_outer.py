#!/usr/bin/env python3
from pathlib import Path
import argparse,json,shutil,subprocess
ap=argparse.ArgumentParser();ap.add_argument('--iteration',type=int,required=True);ap.add_argument('--engine-root',type=Path,required=True);ap.add_argument('--work-root',type=Path,required=True);ap.add_argument('--python',type=Path,required=True);a=ap.parse_args();engine=a.engine_root.resolve();work=a.work_root.resolve();it=work/'cegar'/f'iter{a.iteration}';dynamic=work/'cegar/dynamic_blocks.json';general=work/'classification/installed_generalized_terms.json';registry=work/'classification/online_mechanism_registry.json'
def load(p):return json.loads(Path(p).read_text())
records=[]
def run(name,timeout,cmd,log=None):
 log=log or it/f'{name}.log';rec=it/f'{name}.run.json';full=[str(a.python),str(engine/'src/run_foreground.py'),'--timeout-seconds',str(timeout),'--log',str(log),'--record',str(rec),'--']+[str(x) for x in cmd];cp=subprocess.run(full,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True);r=load(rec);r['stage']=name;r['iteration']=a.iteration;records.append(r);print(cp.stdout.strip(),flush=True);return cp.returncode,r
solver=engine/'tooling/cadical-1.9.5-arm64-macos';statuses={}
for lab in ('Xerr','Zerr'):
 rc,r=run(f'{lab}_solver',660,[solver,'-t','600','--no-binary',it/'direct360'/f'{lab}.cnf'],it/'solver'/f'{lab}.solver.log');statuses[lab]='TIMEOUT' if r['timed_out'] else ('SAT' if r['exit_code']==10 else ('UNSAT_UNPROVED' if r['exit_code']==20 else f"UNKNOWN_EXIT_{r['exit_code']}"))
if not all(x=='SAT' for x in statuses.values()):
 gate={'schema':'round74-direct-nonsat-gate-v1','iteration':a.iteration,'sector_first_run_statuses':statuses,'accepted_absence':{},'repair_entered':False,'branch_closed':False,'policy':'resume path stopped before proof escalation; use primary runner proof gate'};(it/'direct_nonsat_gate.json').write_text(json.dumps(gate,indent=2,sort_keys=True)+'\n');raise SystemExit(31)
rc,_=run('direct_replay',240,[a.python,engine/'src/replay_direct_candidate.py','--root',it,'--output',it/'direct_verification.json']);assert rc==0
before_dyn=len(load(it/'dynamic_before.json'));before_gen=load(it/'generalized_before.json')['term_count'];rc,_=run('append_candidate_exact',120,[a.python,engine/'src/append_dynamic_blocks.py','--verification',it/'direct_verification.json','--dynamic-blocks',dynamic,'--iteration',a.iteration]);assert rc==0
rc,_=run('online_generalization',3600,[a.python,engine/'src/generalize_online.py','--root',engine,'--iteration-root',it,'--generalized-state',general,'--registry-state',registry,'--output-root',it/'generalization']);assert rc==0
gen=load(it/'generalization/install_result.json');after_dyn=len(load(dynamic));after_gen=load(general)['term_count'];shutil.copy2(dynamic,it/'dynamic_after.json');shutil.copy2(general,it/'generalized_after.json');shutil.copy2(registry,it/'mechanism_registry_after.json');ver=load(it/'direct_verification.json');ores=load(it/'outer_result.json')
all_records=[]
for p in [it/'outer_build.run.json',it/'outer_independent_replay.failed_v1.run.json',it/'outer_independent_replay.run.json']:
 if p.exists():
  r=load(p);r['stage']=p.name.replace('.run.json','');r['iteration']=a.iteration;all_records.append(r)
all_records+=records
out={'schema':'round74-online-iteration-outcome-v1','iteration':a.iteration,'outer_status':'SAT','outer_seconds':ores['seconds'],'candidate_sha256':ver['candidate_sha256'],'installed_blocks_before':1440+20+before_gen+before_dyn,'dynamic_blocks_before':before_dyn,'generalized_terms_before':before_gen,'sector_statuses':{s:ver['sectors'][s]['status'] for s in ('Xerr','Zerr')},'sector_fault_weights':{s:ver['sectors'][s]['mechanism']['fault_count'] for s in ('Xerr','Zerr')},'all_dimacs_clauses_satisfied':{s:ver['sectors'][s]['all_dimacs_clauses_satisfied'] for s in ('Xerr','Zerr')},'raw_replay_passed':True,'candidate_exact_blocks_added':2,'dynamic_blocks_after':after_dyn,'online_generalized_retained_increment':gen['retained_increment'],'generalized_terms_after':after_gen,'installed_blocks_after':1440+20+after_gen+after_dyn,'accepted_absence_proofs':0,'repair_entered':False,'branch_closed':False,'strict_stage_order':['outer_build','outer_independent_replay_failed_schema_only','outer_independent_replay','Xerr_solver','Zerr_solver','direct_replay','append_candidate_exact','online_generalization'],'process_records':all_records};assert after_dyn==before_dyn+2 and after_gen==before_gen+gen['retained_increment'];(it/'iteration_outcome.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps(out,sort_keys=True))
