#!/usr/bin/env python3
from pathlib import Path
import argparse,json,shutil,subprocess,sys
ap=argparse.ArgumentParser();ap.add_argument('--iteration',type=int,required=True);ap.add_argument('--engine-root',type=Path,required=True);ap.add_argument('--work-root',type=Path,required=True);ap.add_argument('--python',type=Path,required=True);a=ap.parse_args()
engine=a.engine_root.resolve();work=a.work_root.resolve();it=work/'cegar'/f'iter{a.iteration}';it.mkdir(parents=True,exist_ok=False);(it/'solver').mkdir();dynamic=work/'cegar/dynamic_blocks.json';shutil.copy2(dynamic,it/'dynamic_before.json')
def run(name,timeout,cmd,log=None):
 log=log or it/f'{name}.log';rec=it/f'{name}.run.json';full=[str(a.python),str(engine/'src/run_foreground.py'),'--timeout-seconds',str(timeout),'--log',str(log),'--record',str(rec),'--']+[str(x) for x in cmd];cp=subprocess.run(full,check=False,text=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT);print(cp.stdout.strip(),flush=True);return cp.returncode,json.loads(rec.read_text())
rc,b=run('outer_build',180,[a.python,engine/'src/build_cegar_candidate.py','--iteration',str(a.iteration),'--output',it,'--dynamic-blocks',dynamic,'--z3-timeout-ms','120000'])
if rc!=0:raise SystemExit(f'outer build wrapper failed {rc}')
ores=json.loads((it/'outer_result.json').read_text());status=ores['status']
if status!='SAT':
 (it/'iteration_outcome.json').write_text(json.dumps({'schema':'round72-iteration-outcome-v1','iteration':a.iteration,'outer_status':status,'branch_closed':False,'accepted_outer_exhaustion_proof':False,'stop_reason':'outer result is not SAT; no proof-producing equivalent encoding/independent proof is present'},indent=2,sort_keys=True)+'\n');raise SystemExit(30)
rc,ov=run('outer_independent_replay',180,[a.python,engine/'src/verify_outer_candidate.py','--engine-root',engine,'--iteration-root',it,'--dynamic-before',it/'dynamic_before.json','--output',it/'outer_independent_replay.json'])
if rc!=0:raise SystemExit(f'outer replay failed {rc}')
solver=engine/'tooling/cadical-1.9.5-arm64-macos';statuses={}
for lab in ('Xerr','Zerr'):
 rc,sr=run(f'{lab}_solver',660,[solver,'-t','600','--no-binary',it/'direct360'/f'{lab}.cnf'],it/'solver'/f'{lab}.solver.log')
 statuses[lab]='TIMEOUT' if sr['timed_out'] else ('SAT' if sr['exit_code']==10 else ('UNSAT_NO_PROOF_FIRST_RUN' if sr['exit_code']==20 else f"UNKNOWN_EXIT_{sr['exit_code']}"))
if not all(x=='SAT' for x in statuses.values()):
 accepted={}
 for lab in ('Xerr','Zerr'):
  if statuses[lab]!='UNSAT_NO_PROOF_FIRST_RUN':continue
  cnf=it/'direct360'/f'{lab}.cnf';proof=it/'solver'/f'{lab}.drat';lrat=it/'solver'/f'{lab}.lrat';rc,pr=run(f'{lab}_proof_solver',660,[solver,'-t','600','--no-binary',cnf,proof],it/'solver'/f'{lab}.proof_solver.log')
  if pr['exit_code']!=20 or pr['timed_out'] or not proof.exists():statuses[lab]='UNSAT_PROOF_RUN_FAILED';continue
  drat=engine/'tooling/drat-trim-arm64-macos';lratc=engine/'tooling/lrat-check-arm64-macos';rc,dr=run(f'{lab}_drat_check',600,[drat,cnf,proof,'-t','590','-L',lrat]);rc2,lr=run(f'{lab}_lrat_check',600,[lratc,cnf,lrat])
  if dr['exit_code']==0 and lr['exit_code']==0:statuses[lab]='UNSAT_PROOFS_ACCEPTED';accepted[lab]=True
  else:statuses[lab]='UNSAT_PROOF_REJECTED';accepted[lab]=False
 (it/'iteration_outcome.json').write_text(json.dumps({'schema':'round72-iteration-outcome-v1','iteration':a.iteration,'outer_status':'SAT','sector_statuses':statuses,'accepted_absence':accepted,'branch_closed':False,'repair_entered':False,'stop_reason':'non-SAT sector encountered; dual accepted absence and full repair are required before branch closure'},indent=2,sort_keys=True)+'\n');raise SystemExit(31)
rc,vr=run('direct_replay',180,[a.python,engine/'src/replay_direct_candidate.py','--root',it,'--output',it/'direct_verification.json'])
if rc!=0:raise SystemExit(f'direct replay failed {rc}')
before=len(json.loads((it/'dynamic_before.json').read_text()));rc,ar=run('append_dynamic',120,[a.python,engine/'src/append_dynamic_blocks.py','--verification',it/'direct_verification.json','--dynamic-blocks',dynamic,'--iteration',str(a.iteration)])
if rc!=0:raise SystemExit(f'append failed {rc}')
ver=json.loads((it/'direct_verification.json').read_text());out={'schema':'round72-iteration-outcome-v1','iteration':a.iteration,'outer_status':'SAT','outer_seconds':ores['seconds'],'candidate_sha256':ver['candidate_sha256'],'installed_blocks_before':6766+before,'dynamic_blocks_before':before,'sector_statuses':{s:ver['sectors'][s]['status'] for s in ('Xerr','Zerr')},'sector_fault_weights':{s:ver['sectors'][s]['mechanism']['fault_count'] for s in ('Xerr','Zerr')},'sector_atom_counts':{s:ver['sectors'][s]['mechanism']['sound_outer_block']['atom_count'] for s in ('Xerr','Zerr')},'all_dimacs_clauses_satisfied':{s:ver['sectors'][s]['all_dimacs_clauses_satisfied'] for s in ('Xerr','Zerr')},'raw_replay_passed':True,'new_dynamic_blocks':2,'dynamic_blocks_after':before+2,'accepted_absence_proofs':0,'repair_entered':False,'branch_closed':False};(it/'iteration_outcome.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps(out,sort_keys=True),flush=True)
