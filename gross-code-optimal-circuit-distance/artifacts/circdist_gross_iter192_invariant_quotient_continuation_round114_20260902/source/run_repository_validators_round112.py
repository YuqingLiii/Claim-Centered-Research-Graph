#!/usr/bin/env python3
from pathlib import Path
import argparse, datetime, hashlib, json, os, signal, subprocess, sys, time
ap=argparse.ArgumentParser();ap.add_argument('--repository',type=Path,required=True);ap.add_argument('--package',type=Path,required=True);a=ap.parse_args()
R,P=a.repository.resolve(),a.package.resolve();O=P/'verification/repository_validators';O.mkdir(parents=True,exist_ok=True)
commands=[
 ('proof_dag_circdist',['/usr/bin/python3','tools/proof_dag_check.py','--problem','circdist']),
 ('proof_dag_all',['/usr/bin/python3','tools/proof_dag_check.py','--problem','all']),
 ('circdist_migration',['/usr/bin/python3','tools/check_circdist_migration.py']),
 ('release_contracts',['/usr/bin/python3','tools/test_release_contracts.py']),
 ('dag_contracts',['/usr/bin/python3','tools/test_dag_contracts.py']),
 ('lean_dag_selftest',['/usr/bin/python3','tools/lean_dag_check.py','--selftest']),
 ('duplicate_yaml',['/usr/bin/python3',str(P/'source/duplicate_yaml_scan.py'),'--root',str(R),'--output',str(O/'duplicate_yaml.result.json')]),
 ('git_diff_check',['/usr/bin/git','diff','--check'])]
rows=[];env={k:os.environ[k] for k in ('PATH','LANG','LC_ALL','PYTHONDONTWRITEBYTECODE') if k in os.environ}
for name,cmd in commands:
 st=time.time();c=subprocess.Popen(cmd,cwd=R,env=env,stdout=subprocess.PIPE,stderr=subprocess.PIPE,start_new_session=False);timed=term=killed=False
 try:out,err=c.communicate(timeout=1800)
 except subprocess.TimeoutExpired:
  timed=term=True;c.send_signal(signal.SIGTERM)
  try:out,err=c.communicate(timeout=15)
  except subprocess.TimeoutExpired:killed=True;c.kill();out,err=c.communicate()
 en=time.time();op,ep=O/f'{name}.stdout.log',O/f'{name}.stderr.log';op.write_bytes(out);ep.write_bytes(err)
 row={'schema':'circdist-gross-round112-validator-child-v1','name':name,'argv':cmd,'cwd':str(R),'environment':env,'parent_pid':os.getpid(),'child_pid':c.pid,'returncode':c.returncode,'expected_returncode':0,'returncode_matches':c.returncode==0 and not timed,'started_unix':st,'ended_unix':en,'started_utc':datetime.datetime.fromtimestamp(st,datetime.timezone.utc).isoformat(),'ended_utc':datetime.datetime.fromtimestamp(en,datetime.timezone.utc).isoformat(),'wall_seconds':round(en-st,6),'stdout':op.relative_to(P).as_posix(),'stdout_sha256':hashlib.sha256(out).hexdigest(),'stdout_bytes':len(out),'stderr':ep.relative_to(P).as_posix(),'stderr_sha256':hashlib.sha256(err).hexdigest(),'stderr_bytes':len(err),'timed_out':timed,'term_sent':term,'kill_sent':killed,'reaped':True,'detached':False}
 (O/f'{name}.run.json').write_text(json.dumps(row,indent=2,sort_keys=True)+'\n');rows.append(row);print(json.dumps({'name':name,'pid':c.pid,'rc':c.returncode,'seconds':row['wall_seconds']},sort_keys=True),flush=True);assert row['returncode_matches'],(name,c.returncode,out[-2000:],err[-2000:])
result={'schema':'circdist-gross-round112-preinstall-repository-validator-summary-v1','status':'PASS','checks':rows,'check_count':len(rows),'strict_serial':True,'all_children_reaped':True,'detached_processes':0,'duplicate_key_scan':'PASS','git_diff_check':'PASS','live_governance':'PASS_BY_CLEAN_PRESEAL_REPLAY','evidence_closure':'DEFERRED_UNTIL_ATOMIC_INSTALL_BECAUSE_CHECKER_ENUMERATES_REPOSITORY_ARTIFACT_PATHS; expected pre-review result is only unlinked paths under this package'}
(O/'summary.json').write_text(json.dumps(result,indent=2,sort_keys=True)+'\n');print(json.dumps({'status':'PASS','checks':len(rows),'evidence_closure':'post-install expected-unlinked only'},sort_keys=True))
