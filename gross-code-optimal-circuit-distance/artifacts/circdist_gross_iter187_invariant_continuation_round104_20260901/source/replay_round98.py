#!/usr/bin/env python3
"""Full deterministic replay of the sealed Round98 proposer package."""
from pathlib import Path
import argparse,gzip,hashlib,json,shutil,subprocess,tempfile,time,traceback

def actual(p):
 p=Path(p)
 if p.exists():return p,p.suffix=='.gz'
 q=p.with_name(p.name+'.gz');assert q.exists(),p;return q,True
def data(p):
 q,z=actual(p);b=q.read_bytes();return gzip.decompress(b) if z else b
def materialize(p,q):q=Path(q);q.parent.mkdir(parents=True,exist_ok=True);q.write_bytes(data(p));return q
def compare(a,b):assert data(a)==data(b),(a,b)
def load(p):return json.loads(data(p))
def compare_json(a,b,ignore=()):
 x=load(a);y=load(b)
 for k in ignore:x.pop(k,None);y.pop(k,None)
 assert x==y,(a,b)

p=argparse.ArgumentParser();p.add_argument('--root',type=Path,required=True);p.add_argument('--python',type=Path,required=True);p.add_argument('--repository',type=Path);p.add_argument('--record-output',type=Path);a=p.parse_args()
R=a.root.resolve();PY=a.python.absolute();REPO=a.repository.resolve() if a.repository else R.parents[2];V=R/'vendor/round80';rows=[];started=time.time();status='RUNNING';failure=None
def run(name,cmd,expected=0):
 t=time.time();cp=subprocess.run([str(x) for x in cmd],capture_output=True,text=True,timeout=900);row={'name':name,'command':[str(x) for x in cmd],'returncode':cp.returncode,'expected_returncode':expected,'stdout':cp.stdout,'stderr':cp.stderr,'wall_seconds':round(time.time()-t,6),'reaped':True,'detached':False};rows.append(row);print(json.dumps({k:row[k] for k in ('name','returncode','expected_returncode','wall_seconds')},sort_keys=True),flush=True);assert cp.returncode==expected,(name,cp.returncode,cp.stdout[-2000:],cp.stderr[-2000:]);return cp
try:
 with tempfile.TemporaryDirectory(prefix='circdist-r98-replay.') as td:
  T=Path(td)
  run('protected_bindings',[PY,R/'source/check_round98_protected.py','--package',R,'--repository',REPO])
  for i in range(160,173):
   F=R/'formulas'/f'iter{i}';D=T/'formulas'/f'iter{i}';D.mkdir(parents=True)
   stored_cnf=materialize(F/'outer.cnf',D/'stored.cnf');stored_map=materialize(F/'assertion_map.jsonl',D/'stored.map')
   run(f'compile_iter{i}',[PY,R/'source/compile_outer_cnf.py','--source',F/'source.json.gz','--cnf',D/'fresh.cnf','--metadata',D/'fresh.metadata.json','--assertion-map',D/'fresh.map','--definitions',D/'fresh.trace.json.gz'])
   assert (D/'fresh.cnf').read_bytes()==stored_cnf.read_bytes();assert (D/'fresh.map').read_bytes()==stored_map.read_bytes();assert (D/'fresh.trace.json.gz').read_bytes()==(F/'circuit_trace.json.gz').read_bytes();compare_json(F/'metadata.json',D/'fresh.metadata.json',('compile_seconds',))
   run(f'encoding_iter{i}',[PY,R/'source/check_outer_encoding.py','--source',F/'source.json.gz','--cnf',D/'fresh.cnf','--metadata',D/'fresh.metadata.json','--assertion-map',D/'fresh.map','--definitions',D/'fresh.trace.json.gz','--output',D/'fresh.encoding.json'])
   compare_json(F/'encoding_check.json',D/'fresh.encoding.json',('seconds',));print('FORMULA_REPLAY_PASS',i,flush=True)
  for i in range(160,172):
   I=R/'iterations'/f'iter{i}';W=T/'iterations'/f'iter{i}';W.mkdir(parents=True);state=load(R/'state'/f'iter{i}_state.json')
   direct=W/'direct';run(f'direct_build_iter{i}',[PY,R/'source/build_direct_from_candidate.py','--candidate',I/'outer/candidate.json','--output',direct,'--vendor',V,'--source-selector-count',state['selector_count']])
   compare(direct/'candidate.json',I/'direct/candidate.json');compare(direct/'build_summary.json',I/'direct/build_summary.json')
   for sector in ('Xerr','Zerr'):
    for suffix in ('cnf','variables.json','columns.json','clauses.jsonl','summary.json'):compare(direct/'direct360'/f'{sector}.{suffix}',I/'direct/direct360'/f'{sector}.{suffix}')
   X=W/'transition';run(f'transition_iter{i}',[PY,R/'source/advance_round98.py','--vendor',V,'--state-in',R/'state'/f'iter{i}_state.json','--source-in',R/'formulas'/f'iter{i}'/'source.json.gz','--iteration',i,'--candidate',I/'outer/candidate.json','--direct',I/'direct/direct_verification.json','--state-out',X/'state.json','--record-out',X/'record.json','--source-out',X/'source.json.gz'])
   compare(X/'state.json',R/'state'/f'iter{i+1}_state.json');compare(X/'record.json',I/'record.json');compare(X/'source.json.gz',R/'formulas'/f'iter{i+1}'/'source.json.gz');print('CANDIDATE_TRANSITION_REPLAY_PASS',i,flush=True)
  run('independent_campaign_audit',[PY,R/'source/audit_round98.py','--root',R,'--logs',R/'logs','--vendor',V,'--output',T/'audit.json']);compare_json(R/'verification/dispatcher_independent_campaign_audit.json',T/'audit.json',('seconds',))
  run('order5_independent_validation',[PY,R/'source/validate_order5.py','--root',R,'--output',T/'order5.json']);compare_json(R/'verification/dispatcher_order5_validation.json',T/'order5.json',('seconds',))
  run('result_crosscheck',[PY,R/'source/check_round98_result.py','--root',R]);run('process_crosscheck',[PY,R/'source/check_round98_process.py','--root',R])
  run('proof_controls',[PY,R/'source/check_proof_controls.py','--root',R,'--output',T/'proof.json'])
  x=load(T/'proof.json');y=load(R/'controls/proof_fixture_controls_round98.json');stable=('status','fixture_cnf_sha256','valid_drat_sha256','generated_lrat_sha256','valid_drat_accepted','generated_lrat_accepted','corrupt_drat_rejected','truncated_drat_rejected','corrupt_lrat_rejected','truncated_lrat_rejected','scope');assert all(x[k]==y[k] for k in stable)
  status='PASS'
except BaseException as e:
 status='FAIL';failure={'type':type(e).__name__,'message':str(e),'traceback':traceback.format_exc()};raise
finally:
 rec={'schema':'circdist-round98-full-replay-processes-v1','status':status,'started_unix':started,'ended_unix':time.time(),'wall_seconds':round(time.time()-started,6),'children':rows,'child_count':len(rows),'all_children_reaped':True,'detached_processes':0,'failure':failure}
 if a.record_output:a.record_output.parent.mkdir(parents=True,exist_ok=True);a.record_output.write_text(json.dumps(rec,indent=2,sort_keys=True)+'\n')
print('ROUND98_PACKAGE_REPLAY_PASS',len(rows))
