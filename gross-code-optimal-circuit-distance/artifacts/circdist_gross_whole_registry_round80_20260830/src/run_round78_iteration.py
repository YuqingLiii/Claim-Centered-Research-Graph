#!/usr/bin/env python3
from pathlib import Path
import argparse,hashlib,json,os,shutil,subprocess

ap=argparse.ArgumentParser();ap.add_argument('--iteration',type=int,required=True);ap.add_argument('--engine-root',type=Path,required=True);ap.add_argument('--work-root',type=Path,required=True);ap.add_argument('--python',type=Path,required=True);a=ap.parse_args()
assert a.iteration>=78
engine=a.engine_root.resolve();work=a.work_root.resolve();it=work/'cegar'/f'iter{a.iteration}';it.mkdir(parents=True,exist_ok=False)
(it/'solver').mkdir();(it/'generalization').mkdir();pending=it/'pending_state';pending.mkdir()
dynamic=work/'cegar/dynamic_blocks.json';general=work/'classification/installed_generalized_terms.json';registry=work/'classification/online_mechanism_registry.json';raw_mechanisms=work/'classification/full_raw_mechanisms.json'
states={'dynamic':dynamic,'generalized':general,'registry':registry,'raw_mechanisms':raw_mechanisms}
before_names={'dynamic':'dynamic_before.json','generalized':'generalized_before.json','registry':'mechanism_registry_before.json','raw_mechanisms':'raw_mechanisms_before.json'}
pending_names={'dynamic':'dynamic_blocks.json','generalized':'installed_generalized_terms.json','registry':'online_mechanism_registry.json','raw_mechanisms':'full_raw_mechanisms.json'}
for k,p in states.items():shutil.copy2(p,it/before_names[k]);shutil.copy2(p,pending/pending_names[k])
pdyn=pending/pending_names['dynamic'];pgen=pending/pending_names['generalized'];preg=pending/pending_names['registry'];praw=pending/pending_names['raw_mechanisms']
records=[]
def load(p):return json.loads(Path(p).read_text())
def sha(o):return hashlib.sha256(json.dumps(o,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def file_sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def dump(p,o):Path(p).write_text(json.dumps(o,indent=2,sort_keys=True)+'\n')
def run(name,timeout,cmd,log=None):
 log=log or it/f'{name}.log';rec=it/f'{name}.run.json';full=[str(a.python),str(engine/'src/run_supervised.py'),'--timeout-seconds',str(timeout),'--log',str(log),'--record',str(rec),'--']+[str(x) for x in cmd]
 cp=subprocess.run(full,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True);r=load(rec);r['stage']=name;r['iteration']=a.iteration;records.append(r);print(cp.stdout.strip(),flush=True);return cp.returncode,r

# The outer is a fresh subprocess and consumes exactly the last committed bundle.
rc,_=run('outer_build',180,[a.python,engine/'src/build_online_candidate.py','--iteration',a.iteration,'--output',it,'--dynamic-blocks',dynamic,'--generalized-terms',general,'--registry-state',registry,'--raw-mechanisms-state',raw_mechanisms,'--z3-timeout-ms',120000])
if rc!=0:raise SystemExit(f'outer wrapper failed {rc}')
ores=load(it/'outer_result.json')
if ores['status']!='SAT':
 out={'schema':'round78-online-iteration-outcome-v1','iteration':a.iteration,'outer_status':ores['status'],'reason_unknown':ores.get('reason_unknown'),'branch_closed':False,'accepted_outer_exhaustion_proof':False,'state_mutated':False,'stop_reason':'outer result is not SAT; no independently accepted candidate-specific DRAT/LRAT proof exists, and UNKNOWN/timeout has no disposition','process_records':records}
 dump(it/'iteration_outcome.json',out);print(json.dumps(out,sort_keys=True));raise SystemExit(30)
rc,_=run('outer_independent_replay',240,[a.python,engine/'src/verify_online_outer.py','--iteration-root',it,'--output',it/'outer_independent_replay.json'])
if rc!=0:raise SystemExit(f'outer independent replay failed {rc}')
solver=engine/'tooling/cadical-1.9.5-arm64-macos';statuses={}
direct_summaries={lab:load(it/'direct360'/f'{lab}.summary.json') for lab in ('Xerr','Zerr')}
most_constrained=max(('Xerr','Zerr'),key=lambda lab:(direct_summaries[lab]['clauses'],direct_summaries[lab]['variables'],lab))
proof_attempt_path=it/'solver'/f'{most_constrained}.direct_absence_attempt.drat'
proof_output_enabled=(a.iteration==90)
for lab in (most_constrained,)+tuple(x for x in ('Xerr','Zerr') if x!=most_constrained):
 cmd=[solver,'-t','600','--no-binary',it/'direct360'/f'{lab}.cnf']
 if lab==most_constrained and proof_output_enabled:cmd.append(proof_attempt_path)
 rc,r=run(f'{lab}_solver',660,cmd,it/'solver'/f'{lab}.solver.log')
 statuses[lab]='TIMEOUT' if r['timed_out'] else ('SAT' if r['exit_code']==10 else ('UNSAT_UNPROVED' if r['exit_code']==20 else f"UNKNOWN_EXIT_{r['exit_code']}"))
attempt={'schema':'round80-candidate-specific-direct-absence-attempt-v1','iteration':a.iteration,'selection_rule':'maximum complete direct-360 DIMACS clause count, then variables, then sector label','selected_sector':most_constrained,'sector_formula_counts':{lab:{'primary_selection_variables':direct_summaries[lab]['primary_selection_variables'],'variables':direct_summaries[lab]['variables'],'clauses':direct_summaries[lab]['clauses'],'complete_query':direct_summaries[lab]['complete_query']} for lab in ('Xerr','Zerr')},'proof_producing_solver_requested':proof_output_enabled,'proof_output_policy':'iteration 90 retained one proof-output-enabled SAT control; later SAT searches omit non-certificate proof traces, while any UNSAT status immediately enters the mandatory proof-producing DRAT/LRAT branch','proof_output_path':str(proof_attempt_path.relative_to(it)) if proof_output_enabled else None,'proof_output_exists':proof_attempt_path.exists(),'proof_output_bytes':proof_attempt_path.stat().st_size if proof_attempt_path.exists() else 0,'proof_output_sha256':file_sha(proof_attempt_path) if proof_attempt_path.exists() else None,'solver_status':statuses[most_constrained],'absence_accepted':False,'disposition':'SAT constructive witness; no absence conclusion' if statuses[most_constrained]=='SAT' else 'subject to the full candidate-specific DRAT/LRAT gate below; solver status alone is not absence'}
dump(it/'direct_absence_attempt.json',attempt)
if not all(x=='SAT' for x in statuses.values()):
 gate={'schema':'round78-direct-nonsat-gate-v1','iteration':a.iteration,'sector_first_run_statuses':statuses,'accepted_absence':{},'proof_controls':{},'repair_entered':False,'branch_closed':False,'state_mutated':False,'policy':'UNSAT requires retained candidate-specific DRAT, derived LRAT, independent acceptance, and distinct corrupt and truncated negative controls; timeout/UNKNOWN has no conclusion'}
 for lab in ('Xerr','Zerr'):
  if statuses[lab]!='UNSAT_UNPROVED':continue
  cnf=it/'direct360'/f'{lab}.cnf';drat=it/'solver'/f'{lab}.drat';lrat=it/'solver'/f'{lab}.lrat'
  rc,pr=run(f'{lab}_proof_solver',660,[solver,'-t','600','--no-binary',cnf,drat],it/'solver'/f'{lab}.proof_solver.log')
  if pr['exit_code']!=20 or pr['timed_out'] or not drat.exists():gate['accepted_absence'][lab]=False;statuses[lab]='UNSAT_PROOF_RUN_FAILED';continue
  dratc=engine/'tooling/drat-trim-arm64-macos';lratc=engine/'tooling/lrat-check-arm64-macos'
  rc,dr=run(f'{lab}_drat_check',600,[dratc,cnf,drat,'-t','590','-L',lrat]);rc2,lr=run(f'{lab}_lrat_check',600,[lratc,cnf,lrat])
  db=drat.read_bytes().splitlines(keepends=True);lb=lrat.read_bytes().splitlines(keepends=True);assert db and lb
  dt=it/'solver'/f'{lab}.truncated.drat';lt=it/'solver'/f'{lab}.truncated.lrat';dc=it/'solver'/f'{lab}.corrupt.drat';lc=it/'solver'/f'{lab}.corrupt.lrat'
  dt.write_bytes(b''.join(db[:-1]));lt.write_bytes(b''.join(lb[:-1]));dc.write_bytes(b'999999999 0\n'+b''.join(db));lc.write_bytes(b'999999999 0 999999999 0\n'+b''.join(lb))
  _,drt=run(f'{lab}_drat_truncated_check',120,[dratc,cnf,dt,'-t','110']);_,lrt=run(f'{lab}_lrat_truncated_check',120,[lratc,cnf,lt]);_,drc=run(f'{lab}_drat_corrupt_check',120,[dratc,cnf,dc,'-t','110']);_,lrc=run(f'{lab}_lrat_corrupt_check',120,[lratc,cnf,lc])
  accepted=dr['exit_code']==0 and lr['exit_code']==0 and all(z['exit_code']!=0 for z in (drt,lrt,drc,lrc))
  gate['proof_controls'][lab]={'drat_sha256':file_sha(drat),'lrat_sha256':file_sha(lrat),'valid_drat_accepted':dr['exit_code']==0,'valid_lrat_accepted':lr['exit_code']==0,'truncated_drat_rejected':drt['exit_code']!=0,'truncated_lrat_rejected':lrt['exit_code']!=0,'corrupt_drat_rejected':drc['exit_code']!=0,'corrupt_lrat_rejected':lrc['exit_code']!=0}
  gate['accepted_absence'][lab]=accepted;statuses[lab]='UNSAT_PROOFS_ACCEPTED' if accepted else 'UNSAT_PROOF_OR_CONTROL_REJECTED'
 gate['sector_final_statuses']=statuses;gate['repair_entered']=all(statuses.get(x)=='UNSAT_PROOFS_ACCEPTED' for x in ('Xerr','Zerr'))
 gate['stop_reason']='dual checked direct absence reached repair gate; no repair implementation is entered by this proposer' if gate['repair_entered'] else 'mixed, unknown, timeout, or unaccepted absence; no repair and no branch closure'
 dump(it/'direct_nonsat_gate.json',gate);out={'schema':'round78-online-iteration-outcome-v1','iteration':a.iteration,'outer_status':'SAT','sector_statuses':statuses,'accepted_absence':gate['accepted_absence'],'repair_entered':False,'repair_gate_available':gate['repair_entered'],'branch_closed':False,'state_mutated':False,'stop_reason':gate['stop_reason'],'process_records':records};dump(it/'iteration_outcome.json',out);print(json.dumps(out,sort_keys=True));raise SystemExit(32 if gate['repair_entered'] else 31)

rc,_=run('direct_replay',240,[a.python,engine/'src/replay_direct_candidate.py','--root',it,'--output',it/'direct_verification.json'])
if rc!=0:raise SystemExit(f'direct raw replay failed {rc}')
before_dyn=len(load(it/'dynamic_before.json'));before_gen=load(it/'generalized_before.json')['term_count'];before_reg=load(it/'mechanism_registry_before.json')['mechanism_count'];before_raw=load(it/'raw_mechanisms_before.json')['mechanism_count']
rc,_=run('append_candidate_exact_pending',120,[a.python,engine/'src/append_dynamic_blocks.py','--verification',it/'direct_verification.json','--dynamic-blocks',pdyn,'--iteration',a.iteration])
if rc!=0:raise SystemExit(f'exact pending append failed {rc}')
rc,_=run('online_generalization_pending',3600,[a.python,engine/'src/generalize_online.py','--root',engine,'--iteration-root',it,'--generalized-state',pgen,'--registry-state',preg,'--output-root',it/'generalization'])
if rc!=0:raise SystemExit(f'online generalization failed {rc}')
gen=load(it/'generalization/install_result.json')
rc,_=run('cross_registry_synthesis_pending',3600,[a.python,engine/'src/synthesize_cross_registry.py','--root',engine,'--generalized-state',pgen,'--registry-state',preg,'--raw-mechanisms-state',praw,'--dynamic-blocks-state',pdyn,'--append-mechanisms',it/'generalization/mechanisms.json','--output-root',it/'cross_registry','--batch-id',f'post{a.iteration:03d}'])
if rc!=0:raise SystemExit(f'cross-registry synthesis failed {rc}')
xreg=load(it/'cross_registry/install_result.json')

# Publish the already validated four-file state bundle with an intent/completion journal.
after_objs={k:load(pending/pending_names[k]) for k in states};before_objs={k:load(it/before_names[k]) for k in states}
intent={'schema':'round78-state-bundle-commit-intent-v1','iteration':a.iteration,'status':'INTENT','before_semantic_sha256':{k:sha(v) for k,v in before_objs.items()},'after_semantic_sha256':{k:sha(v) for k,v in after_objs.items()},'publish_order':['dynamic','registry','raw_mechanisms','generalized'],'same_filesystem':all(os.stat(p.parent).st_dev==os.stat(work).st_dev for p in states.values())}
dump(it/'state_commit_intent.json',intent)
for k in intent['publish_order']:
 target=states[k];tmp=target.with_name(target.name+f'.round78-i{a.iteration}.publish.tmp');shutil.copy2(pending/pending_names[k],tmp);os.replace(tmp,target)
assert all(sha(load(states[k]))==intent['after_semantic_sha256'][k] for k in states)
complete={**intent,'schema':'round78-state-bundle-commit-complete-v1','status':'PASS','all_live_bindings_match':True};dump(it/'state_commit_complete.json',complete)

after_dyn=len(load(dynamic));after_gen=load(general)['term_count'];after_reg=load(registry)['mechanism_count'];after_raw=load(raw_mechanisms)['mechanism_count']
shutil.copy2(dynamic,it/'dynamic_after.json');shutil.copy2(general,it/'generalized_after.json');shutil.copy2(registry,it/'mechanism_registry_after.json');shutil.copy2(raw_mechanisms,it/'raw_mechanisms_after.json')
ver=load(it/'direct_verification.json');online_inc=gen['retained_increment'];cross_inc=xreg['retained_increment']
out={'schema':'round78-online-iteration-outcome-v1','iteration':a.iteration,'outer_status':'SAT','outer_seconds':ores['seconds'],'candidate_sha256':ver['candidate_sha256'],'fresh_outer_process':True,
 'installed_blocks_before':1440+20+before_gen+before_dyn,'dynamic_blocks_before':before_dyn,'generalized_terms_before':before_gen,'mechanism_registry_before':before_reg,'raw_mechanisms_before':before_raw,
 'sector_statuses':{s:ver['sectors'][s]['status'] for s in ('Xerr','Zerr')},'sector_fault_weights':{s:ver['sectors'][s]['mechanism']['fault_count'] for s in ('Xerr','Zerr')},'all_dimacs_clauses_satisfied':{s:ver['sectors'][s]['all_dimacs_clauses_satisfied'] for s in ('Xerr','Zerr')},'raw_replay_passed':True,
 'candidate_exact_blocks_added':2,'dynamic_blocks_after':after_dyn,'online_generalized_retained_increment':online_inc,'cross_registry_retained_increment':cross_inc,'generalized_terms_after':after_gen,'mechanism_registry_after':after_reg,'raw_mechanisms_after':after_raw,
 'installed_blocks_after':1440+20+after_gen+after_dyn,'accepted_absence_proofs':0,'repair_entered':False,'branch_closed':False,'state_mutated':True,
 'strict_stage_order':['fresh_outer_build','outer_independent_replay',f'{most_constrained}_solver']+[f'{x}_solver' for x in ('Xerr','Zerr') if x!=most_constrained]+['direct_replay','append_candidate_exact_pending','online_generalization_pending','cross_registry_synthesis_pending','validated_state_bundle_commit'],
 'state_commit_complete_sha256':file_sha(it/'state_commit_complete.json'),'process_records':records}
assert after_dyn==before_dyn+2 and after_gen==before_gen+online_inc+cross_inc and after_reg==before_reg+2 and after_raw==before_raw+2
dump(it/'iteration_outcome.json',out);print(json.dumps(out,sort_keys=True))
