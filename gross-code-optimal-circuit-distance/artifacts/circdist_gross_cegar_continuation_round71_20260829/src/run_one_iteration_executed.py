#!/usr/bin/env python3
from pathlib import Path
import argparse,datetime,hashlib,json,shutil,subprocess,sys,time
ap=argparse.ArgumentParser();ap.add_argument('--iteration',type=int,required=True);ap.add_argument('--repo-root',type=Path,required=True);ap.add_argument('--work-root',type=Path,required=True);ap.add_argument('--python',type=Path,required=True);a=ap.parse_args()
repo=a.repo_root.resolve();engine=repo/'circdist/artifacts/circdist_gross_block_minimization_round69_20260829';work=a.work_root.resolve();scripts=work.parent/'scripts';it=work/'cegar'/f'iter{a.iteration}';it.mkdir(parents=True,exist_ok=False);(it/'solver').mkdir();dynamic=work/'cegar/dynamic_blocks.json';shutil.copy2(dynamic,it/'dynamic_before.json')
def run(name,timeout,cmd,log=None):
 log=log or it/f'{name}.log';rec=it/f'{name}.run.json'
 full=[str(a.python),str(scripts/'run_foreground.py'),'--timeout-seconds',str(timeout),'--log',str(log),'--record',str(rec),'--']+[str(x) for x in cmd]
 cp=subprocess.run(full,check=False,text=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
 print(cp.stdout.strip(),flush=True)
 d=json.loads(rec.read_text());return cp.returncode,d
rc,b=run('outer_build',180,[a.python,engine/'src/build_cegar_candidate.py','--iteration',str(a.iteration),'--output',it,'--dynamic-blocks',dynamic,'--z3-timeout-ms','120000'])
if rc!=0: raise SystemExit(f'outer build wrapper failed {rc}')
ores=json.loads((it/'outer_result.json').read_text());status=ores['status']
if status!='SAT':
 (it/'iteration_outcome.json').write_text(json.dumps({'iteration':a.iteration,'outer_status':status,'branch_closed':False,'stop_reason':'outer result is not SAT; no independently checked exhaustion certificate'},indent=2,sort_keys=True)+'\n');print(json.dumps({'iteration':a.iteration,'stop':status}),flush=True);raise SystemExit(30)
rc,ov=run('outer_independent_replay',180,[a.python,scripts/'verify_outer_candidate.py','--engine-root',engine,'--iteration-root',it,'--dynamic-before',it/'dynamic_before.json','--output',it/'outer_independent_replay.json'])
if rc!=0: raise SystemExit(f'outer independent replay failed {rc}')
solver=engine/'tooling/cadical-1.9.5-arm64-macos';statuses={}
for lab in ('Xerr','Zerr'):
 rc,sr=run(f'{lab}_solver',660,[solver,'-t','600','--no-binary',it/'direct360'/f'{lab}.cnf'],it/'solver'/f'{lab}.solver.log')
 if sr['timed_out']:statuses[lab]='TIMEOUT'
 elif sr['exit_code']==10:statuses[lab]='SAT'
 elif sr['exit_code']==20:statuses[lab]='UNSAT_NO_PROOF_FIRST_RUN'
 else:statuses[lab]=f"UNKNOWN_EXIT_{sr['exit_code']}"
# Both sectors were run before any disposition.
if not all(v=='SAT' for v in statuses.values()):
 # A solver-grade UNSAT is rerun proof-producing. Unknown/timeout remains no absence.
 for lab in ('Xerr','Zerr'):
  if statuses[lab]=='UNSAT_NO_PROOF_FIRST_RUN':
   proof=it/'solver'/f'{lab}.drat';rc,pr=run(f'{lab}_proof_solver',660,[solver,'-t','600','--no-binary',it/'direct360'/f'{lab}.cnf',proof],it/'solver'/f'{lab}.proof_solver.log')
   if pr['exit_code']!=20 or pr['timed_out'] or not proof.exists():statuses[lab]='UNSAT_PROOF_RUN_FAILED';continue
   drat=engine/'tooling/drat-trim-arm64-macos';lratc=engine/'tooling/lrat-check-arm64-macos';lrat=it/'solver'/f'{lab}.lrat'
   rc,dr=run(f'{lab}_drat_check',600,[drat,it/'direct360'/f'{lab}.cnf',proof,'-t','590','-L',lrat])
   rc2,lr=run(f'{lab}_lrat_check',600,[lratc,it/'direct360'/f'{lab}.cnf',lrat])
   if dr['exit_code']==0 and lr['exit_code']==0:statuses[lab]='UNSAT_PROOFS_ACCEPTED'
   else:statuses[lab]='UNSAT_PROOF_REJECTED'
 (it/'iteration_outcome.json').write_text(json.dumps({'iteration':a.iteration,'outer_status':'SAT','sector_statuses':statuses,'branch_closed':False,'stop_reason':'non-SAT sector encountered; inspect proof objects and repair gate'},indent=2,sort_keys=True)+'\n');print(json.dumps({'iteration':a.iteration,'sectors':statuses,'stop':True}),flush=True);raise SystemExit(31)
rc,vr=run('direct_replay',180,[a.python,engine/'src/replay_direct_candidate.py','--root',it,'--output',it/'direct_verification.json'])
if rc!=0: raise SystemExit(f'direct replay failed {rc}')
rc,ar=run('append_dynamic',120,[a.python,engine/'src/append_dynamic_blocks.py','--verification',it/'direct_verification.json','--dynamic-blocks',dynamic,'--iteration',str(a.iteration)])
if rc!=0: raise SystemExit(f'append failed {rc}')
ver=json.loads((it/'direct_verification.json').read_text());out={'schema':'round71-iteration-outcome-v1','iteration':a.iteration,'outer_status':'SAT','outer_seconds':ores['seconds'],'candidate_sha256':ver['candidate_sha256'],'installed_blocks_before':6200+2*a.iteration,'sector_statuses':{s:ver['sectors'][s]['status'] for s in ('Xerr','Zerr')},'sector_fault_weights':{s:ver['sectors'][s]['mechanism']['fault_count'] for s in ('Xerr','Zerr')},'sector_atom_counts':{s:ver['sectors'][s]['mechanism']['sound_outer_block']['atom_count'] for s in ('Xerr','Zerr')},'all_dimacs_clauses_satisfied':{s:ver['sectors'][s]['all_dimacs_clauses_satisfied'] for s in ('Xerr','Zerr')},'raw_replay_passed':True,'new_dynamic_blocks':2,'dynamic_blocks_after':2*(a.iteration+1),'repair_entered':False,'branch_closed':False}
(it/'iteration_outcome.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps(out,sort_keys=True),flush=True)
