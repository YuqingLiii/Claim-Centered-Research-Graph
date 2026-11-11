#!/usr/bin/env python3
"""Run final Round108 consistency and repository hygiene checks serially."""
from pathlib import Path
import argparse, datetime, json, os, subprocess, sys, time
ap=argparse.ArgumentParser(); ap.add_argument('--repository',type=Path,required=True); ap.add_argument('--package',type=Path,required=True); a=ap.parse_args(); repo=a.repository.resolve(); pkg=a.package.resolve()
commands=[
 ('result_consistency',[sys.executable,pkg/'source/check_result_round108.py','--root',pkg,'--output',pkg/'verification/result_consistency_pre_payload.json']),
 ('package_bindings',[sys.executable,pkg/'source/check_package_bindings_round108.py','--root',pkg,'--output',pkg/'verification/package_binding_check_final.json']),
 ('live_governance',[sys.executable,pkg/'source/check_live_governance_round108.py','--repository',repo,'--package',pkg,'--output',pkg/'verification/live_governance_final.json']),
 ('duplicate_yaml_final',['/usr/bin/python3',pkg/'source/duplicate_yaml_scan.py','--root',repo,'--output',pkg/'verification/duplicate_yaml_final.json']),
 ('git_diff_check_final',['/usr/bin/git','diff','--check'])]
rows=[]
for name,cmd in commands:
 cmd=[str(x) for x in cmd]; start=time.time(); child=subprocess.Popen(cmd,cwd=repo,stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True,start_new_session=False)
 try: out,err=child.communicate(timeout=1800)
 except subprocess.TimeoutExpired:
  child.terminate()
  try: out,err=child.communicate(timeout=10)
  except subprocess.TimeoutExpired: child.kill(); out,err=child.communicate()
  raise AssertionError((name,'timeout',child.pid))
 end=time.time(); assert child.returncode==0,(name,child.returncode,out[-2000:],err[-2000:])
 rows.append({'schema':'circdist-gross-round108-final-preseal-child-v1','name':name,'command':cmd,'parent_pid':os.getpid(),'child_pid':child.pid,'started_unix':start,'ended_unix':end,'started_utc':datetime.datetime.fromtimestamp(start,datetime.timezone.utc).isoformat(),'ended_utc':datetime.datetime.fromtimestamp(end,datetime.timezone.utc).isoformat(),'wall_seconds':round(end-start,6),'returncode':child.returncode,'stdout':out,'stderr':err,'reaped':True,'detached':False,'timed_out':False})
result={'schema':'circdist-gross-round108-final-preseal-checks-v1','status':'PASS','strict_serial':True,'children':rows,'child_count':len(rows),'all_children_reaped':True,'detached_processes':0,'result_consistency':'PASS','package_bindings':'PASS','live_governance':'PASS','duplicate_yaml':'PASS','git_diff_check':'PASS'}
(pkg/'verification/final_preseal_checks.json').write_text(json.dumps(result,indent=2,sort_keys=True)+'\n'); print(json.dumps({'status':'PASS','children':len(rows)},sort_keys=True))
