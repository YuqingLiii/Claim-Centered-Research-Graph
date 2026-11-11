#!/usr/bin/env python3
from pathlib import Path
import argparse,datetime,json,os,subprocess,sys,time,traceback
p=argparse.ArgumentParser();p.add_argument('--repo',type=Path,required=True);p.add_argument('--root',type=Path,required=True);p.add_argument('--first',type=int,required=True);p.add_argument('--last',type=int,required=True);a=p.parse_args()
repo=a.repo.resolve();root=a.root.resolve();python=Path(sys.executable);runner=root/'source/run_logged.py';vendor=root/'vendor/round80';solver=root/'tooling/cadical-1.9.5-arm64-macos';logs=root/'logs';campaign=root/'campaign';campaign.mkdir(parents=True,exist_ok=True);start=time.time();start_iso=datetime.datetime.now(datetime.timezone.utc).isoformat();child_wrapper_count=0;status='RUNNING';exception=None
def atomic_json(path,obj):
 tmp=path.with_suffix(path.suffix+'.tmp');tmp.write_text(json.dumps(obj,indent=2,sort_keys=True)+'\n');os.replace(tmp,path)
def phase(iteration,name,extra=None):
 o={'iteration':iteration,'phase':name,'utc':datetime.datetime.now(datetime.timezone.utc).isoformat()};o.update(extra or {});atomic_json(campaign/'current.json',o);print(json.dumps({'campaign_event':'PHASE',**o},sort_keys=True),flush=True)
def run(name,timeout,cmd,stdout=None,stderr=None):
 global child_wrapper_count
 child_wrapper_count+=1;stdout=stdout or logs/f'stdout/{name}.log';stderr=stderr or logs/f'stderr/{name}.log';rec=logs/f'process/{name}.json'
 command=[str(python),str(runner),'--name',name,'--timeout',str(timeout),'--stdout',str(stdout),'--stderr',str(stderr),'--record',str(rec),'--']+[str(x) for x in cmd]
 print(json.dumps({'campaign_event':'COMMAND','name':name,'command':command},sort_keys=True),flush=True);cp=subprocess.run(command,stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True);wdir=logs/'wrapper';wdir.mkdir(parents=True,exist_ok=True);(wdir/f'{name}.stdout.log').write_text(cp.stdout);(wdir/f'{name}.stderr.log').write_text(cp.stderr);childrec=json.loads(rec.read_text()) if rec.exists() else None;print(json.dumps({'campaign_event':'WRAPPER_END','name':name,'wrapper_returncode':cp.returncode,'child_returncode':childrec.get('returncode') if childrec else None,'wall_seconds':childrec.get('wall_seconds') if childrec else None},sort_keys=True),flush=True)
 if cp.returncode!=0:raise RuntimeError(f'wrapper failure {name} rc={cp.returncode}')
 return childrec
def append_progress(row):
 with (campaign/'progress.jsonl').open('a',encoding='utf-8',newline='\n') as f:f.write(json.dumps(row,sort_keys=True)+'\n')
try:
 for i in range(a.first,a.last+1):
  formula=root/f'formulas/iter{i}';state_path=root/f'state/iter{i}_state.json';state=json.loads(state_path.read_text());assert state['next_iteration']==i and state['started'] is False and state['stop'] is None
  outer=root/f'iterations/iter{i}/outer';outer.mkdir(parents=True,exist_ok=True)
  phase(i,'outer_solve',{'selector_count':state['selector_count']})
  rec=run(f'outer_iter{i}_cadical_proof',900,[solver,'-t','890','--no-binary',formula/'outer.cnf',outer/'outer.drat'],outer/'solver.log',outer/'solver.stderr.log');orc=rec['returncode']
  if orc!=10:
   if orc==20:
    phase(i,'outer_unsat_proof_check')
    run(f'outer_iter{i}_unsat_certificate_check',1800,[python,root/'source/verify_actual_unsat.py','--formula',formula/'outer.cnf','--proof',outer/'outer.drat','--tooling',root/'tooling','--output',outer/'unsat_certificate'])
    status='CLOSURE_OUTER_UNSAT_CHECKED'
   else: status='STOP_OUTER_UNKNOWN_OR_TIMEOUT'
   append_progress({'iteration':i,'outer_returncode':orc,'status':status});phase(i,status,{'returncode':orc});break
  phase(i,'outer_verify')
  run(f'outer_iter{i}_verify_sat',900,[python,root/'source/verify_outer_sat_model.py','--solver-log',outer/'solver.log','--cnf',formula/'outer.cnf','--source',formula/'source.json.gz','--metadata',formula/'metadata.json','--frozen',vendor,'--assignment',outer/'assignment.dimacs','--candidate',outer/'candidate.json','--output',outer/'replay.json'])
  run(f'outer_iter{i}_assignment_independent_check',300,[python,root/'source/extract_and_check_assignment.py','--cnf',formula/'outer.cnf','--solver-log',outer/'solver.log','--assignment',outer/'assignment.independent.dimacs','--output',outer/'assignment_independent_check.json'])
  direct=root/f'iterations/iter{i}/direct';phase(i,'direct_build')
  run(f'direct_iter{i}_build',900,[python,root/'source/build_direct_from_candidate.py','--candidate',outer/'candidate.json','--output',direct,'--vendor',vendor,'--source-selector-count',str(state['selector_count'])])
  codes={}
  for sec in ('Xerr','Zerr'):
   phase(i,f'direct_{sec}_solve')
   r=run(f'direct_iter{i}_{sec}_cadical_proof',900,[solver,'-t','890','--no-binary',direct/f'direct360/{sec}.cnf',direct/f'solver/{sec}.drat'],direct/f'solver/{sec}.solver.log',direct/f'solver/{sec}.stderr.log');codes[sec]=r['returncode']
  if set(codes.values())!={10}:
   for sec in ('Xerr','Zerr'):
    if codes[sec]==20:
     phase(i,f'direct_{sec}_unsat_proof_check')
     run(f'direct_iter{i}_{sec}_unsat_certificate_check',1800,[python,root/'source/verify_actual_unsat.py','--formula',direct/f'direct360/{sec}.cnf','--proof',direct/f'solver/{sec}.drat','--tooling',root/'tooling','--output',direct/f'solver/{sec}.unsat_certificate'])
   status='BOTH_DIRECT_UNSAT_CHECKED_REPAIR_GATE_OPEN' if set(codes.values())=={20} else 'STOP_DIRECT_MIXED_OR_UNKNOWN'
   append_progress({'iteration':i,'outer_returncode':orc,'direct_returncodes':codes,'status':status});phase(i,status,{'returncodes':codes});break
  phase(i,'direct_replay')
  run(f'direct_iter{i}_replay',900,[python,vendor/'src/replay_direct_candidate.py','--root',direct,'--output',direct/'direct_verification.json'])
  for sec in ('Xerr','Zerr'):
   run(f'direct_iter{i}_{sec}_assignment_check',300,[python,root/'source/extract_and_check_assignment.py','--cnf',direct/f'direct360/{sec}.cnf','--solver-log',direct/f'solver/{sec}.solver.log','--assignment',direct/f'solver/{sec}.assignment.dimacs','--output',direct/f'solver/{sec}.assignment_check.json'])
  dv=json.loads((direct/'direct_verification.json').read_text());weights={sec:dv['sectors'][sec]['mechanism']['fault_count'] for sec in ('Xerr','Zerr')}
  # Summarize and remove SAT-only non-certificate streams after every assignment/replay check.
  run(f'outer_iter{i}_sat_trace_summary',600,[python,root/'source/summarize_sat_trace.py','--formula',formula/'outer.cnf','--trace',outer/'outer.drat','--solver-log',outer/'solver.log','--iteration',str(i),'--query','outer','--output',outer/'sat_trace_summary.json','--delete'])
  for sec in ('Xerr','Zerr'):
   run(f'direct_iter{i}_{sec}_sat_trace_summary',600,[python,root/'source/summarize_sat_trace.py','--formula',direct/f'direct360/{sec}.cnf','--trace',direct/f'solver/{sec}.drat','--solver-log',direct/f'solver/{sec}.solver.log','--iteration',str(i),'--query',sec,'--output',direct/f'solver/{sec}.sat_trace_summary.json','--delete'])
  phase(i,'pending_transition')
  pend=root/f'pending/iter{i}_to{i+1}'
  run(f'iter{i}_pending_transition_build',900,[python,root/'source/advance_round96.py','--vendor',vendor,'--state-in',state_path,'--source-in',formula/'source.json.gz','--iteration',str(i),'--candidate',outer/'candidate.json','--direct',direct/'direct_verification.json','--state-out',pend/'state.json','--record-out',pend/'record.json','--source-out',pend/'source.json.gz'])
  run(f'iter{i+1}_pending_compile',900,[python,root/'source/compile_outer_cnf.py','--source',pend/'source.json.gz','--cnf',pend/'formula/outer.cnf','--metadata',pend/'formula/metadata.json','--assertion-map',pend/'formula/assertion_map.jsonl','--definitions',pend/'formula/circuit_trace.json.gz'])
  run(f'iter{i+1}_pending_encoding_check',900,[python,root/'source/check_outer_encoding.py','--source',pend/'source.json.gz','--cnf',pend/'formula/outer.cnf','--metadata',pend/'formula/metadata.json','--assertion-map',pend/'formula/assertion_map.jsonl','--definitions',pend/'formula/circuit_trace.json.gz','--output',pend/'formula/encoding_check.json'])
  run(f'iter{i}_atomic_commit',300,[python,root/'source/atomic_promote_round96.py','--root',root,'--iteration',str(i)])
  next_state=json.loads((root/f'state/iter{i+1}_state.json').read_text());row={'iteration':i,'status':'COMPLETE_SAT','outer_returncode':10,'direct_returncodes':codes,'weights':weights,'source_selector_count':state['selector_count'],'next_selector_count':next_state['selector_count'],'next_iteration':i+1,'next_started':next_state['started'],'next_selector_state_sha256':next_state['selector_state_sha256']};append_progress(row);phase(i,'iteration_complete',row)
 else:status='SAT_PREFIX_COMPLETE'
except BaseException as e:
 status='DRIVER_EXCEPTION';exception={'type':type(e).__name__,'message':str(e),'traceback':traceback.format_exc()};atomic_json(campaign/'exception.json',exception);print(json.dumps({'campaign_event':'EXCEPTION',**exception},sort_keys=True),flush=True);raise
finally:
 end=time.time();end_iso=datetime.datetime.now(datetime.timezone.utc).isoformat();record={'schema':'circdist-round96-campaign-driver-process-v1','pid':os.getpid(),'parent_pid':os.getppid(),'command':sys.argv,'started_unix':start,'ended_unix':end,'started_utc':start_iso,'ended_utc':end_iso,'wall_seconds':round(end-start,6),'first':a.first,'last':a.last,'status':status,'exception':exception,'child_wrapper_processes_started_serially':child_wrapper_count,'all_subprocess_run_calls_returned_or_exception_reaped':True,'detached_processes':0,'final_status':'exited_and_reaped_by_exec_parent'};driver_name=f'driver_process_{a.first}_{a.last}.json';atomic_json(campaign/driver_name,record);atomic_json(campaign/f'summary_{a.first}_{a.last}.json',{'schema':'circdist-round96-campaign-summary-v1','status':status,'first':a.first,'last':a.last,'progress_rows':sum(1 for _ in (campaign/'progress.jsonl').open()) if (campaign/'progress.jsonl').exists() else 0,'driver_process':'campaign/'+driver_name});print(json.dumps({'campaign_event':'DRIVER_END',**record},sort_keys=True),flush=True)
