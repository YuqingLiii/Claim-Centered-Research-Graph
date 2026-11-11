#!/usr/bin/env python3
"""Run and retain the complete Round100 repository gate set, strictly serially."""
from pathlib import Path
import argparse,hashlib,json,os,subprocess,sys,time
ap=argparse.ArgumentParser();ap.add_argument('--repository',type=Path,required=True);ap.add_argument('--package',type=Path,required=True);a=ap.parse_args();R=a.repository.resolve();P=a.package.resolve();O=P/'verification/repository_validators';O.mkdir(parents=True,exist_ok=True)
commands=[
 ('live_protected',[sys.executable,P/'source/check_live_protected_round100.py','--root',P,'--repository',R],0),
 ('proof_dag_circdist',['/usr/bin/python3','tools/proof_dag_check.py','--problem','circdist'],0),
 ('proof_dag_previous_state',['/usr/bin/python3','tools/proof_dag_check.py','--problem','circdist','--previous-state',P/'bindings/initial_proof_dag'],0),
 ('proof_dag_all',['/usr/bin/python3','tools/proof_dag_check.py','--problem','all'],0),
 ('circdist_migration',['/usr/bin/python3','tools/check_circdist_migration.py'],0),
 ('release_contracts',['/usr/bin/python3','tools/test_release_contracts.py'],0),
 ('dag_contracts',['/usr/bin/python3','tools/test_dag_contracts.py'],0),
 ('lean_dag_selftest',['/usr/bin/python3','tools/lean_dag_check.py','--selftest'],0),
 ('duplicate_yaml',['/usr/bin/python3',P/'source/duplicate_yaml_scan.py','--root',R,'--output',O/'duplicate_yaml.result.json'],0),
 ('git_diff_check',['git','diff','--check'],0),
 ('evidence_closure',['/usr/bin/python3','tools/evidence_closure_check.py','--problem','circdist'],1),
]
rows=[]
def run(name,command,expected,timeout=1200):
 command=[str(x) for x in command];t=time.time();child=subprocess.Popen(command,cwd=R,stdout=subprocess.PIPE,stderr=subprocess.PIPE,start_new_session=False);timed=False;term=False;kill=False
 try:stdout,stderr=child.communicate(timeout=timeout)
 except subprocess.TimeoutExpired:
  timed=True;term=True;child.terminate()
  try:stdout,stderr=child.communicate(timeout=15)
  except subprocess.TimeoutExpired:kill=True;child.kill();stdout,stderr=child.communicate()
 for suffix,payload in (('stdout.log',stdout),('stderr.log',stderr)):(O/f'{name}.{suffix}').write_bytes(payload)
 row={'schema':'circdist-round100-validator-run-v1','name':name,'command':command,'expected_returncode':expected,'returncode':child.returncode,'returncode_matches':not timed and child.returncode==expected,'parent_pid':os.getpid(),'child_pid':child.pid,'started_unix':t,'ended_unix':time.time(),'wall_seconds':round(time.time()-t,6),'stdout':f'verification/repository_validators/{name}.stdout.log','stdout_sha256':hashlib.sha256(stdout).hexdigest(),'stdout_bytes':len(stdout),'stderr':f'verification/repository_validators/{name}.stderr.log','stderr_sha256':hashlib.sha256(stderr).hexdigest(),'stderr_bytes':len(stderr),'timed_out':timed,'term_sent':term,'kill_sent':kill,'reaped':True,'detached':False}
 (O/f'{name}.run.json').write_text(json.dumps(row,indent=2,sort_keys=True)+'\n');rows.append(row);print(json.dumps({'name':name,'child_pid':child.pid,'returncode':child.returncode,'expected':expected,'seconds':row['wall_seconds']},sort_keys=True),flush=True);assert row['returncode_matches'],(name,child.returncode,stdout[-2000:],stderr[-2000:])
for row in commands:run(*row)
run('evidence_closure_parser',[sys.executable,P/'source/check_evidence_closure_expected.py','--log',O/'evidence_closure.stdout.log','--output',P/'verification/evidence_closure_interpretation.json'],0,300)
summary={'schema':'circdist-round100-repository-validator-summary-v1','status':'PASS','checks':rows,'check_count':len(rows),'strict_serial':True,'all_children_reaped':all(x['reaped'] for x in rows),'detached_processes':0,'evidence_closure_expected_semantics':'exit 1 accepted only because every unique diagnostic lies under the sole new unlinked Round100 package'}
(O/'summary.json').write_text(json.dumps(summary,indent=2,sort_keys=True)+'\n');print(json.dumps({'status':'PASS','checks':len(rows),'returncodes':{x['name']:x['returncode'] for x in rows}},sort_keys=True))
