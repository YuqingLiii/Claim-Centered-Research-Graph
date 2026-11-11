#!/usr/bin/env python3
from pathlib import Path
import argparse,json,os,subprocess,time,signal
ap=argparse.ArgumentParser();ap.add_argument('--name',required=True);ap.add_argument('--timeout',type=int,required=True)
ap.add_argument('--stdout',type=Path,required=True);ap.add_argument('--stderr',type=Path,required=True)
ap.add_argument('--record',type=Path,required=True);ap.add_argument('command',nargs=argparse.REMAINDER)
a=ap.parse_args();cmd=a.command
if cmd and cmd[0]=='--':cmd=cmd[1:]
assert cmd
a.stdout.parent.mkdir(parents=True,exist_ok=True);start=time.time()
with a.stdout.open('wb') as out,a.stderr.open('wb') as err:
 p=subprocess.Popen(cmd,stdout=out,stderr=err,start_new_session=False)
 print(json.dumps({'event':'START','name':a.name,'runner_pid':os.getpid(),'parent_pid':os.getppid(),
  'child_pid':p.pid,'command':cmd,'timeout_seconds':a.timeout,'stdout':str(a.stdout),'stderr':str(a.stderr)}),flush=True)
 timed=False
 try:rc=p.wait(timeout=a.timeout)
 except subprocess.TimeoutExpired:
  timed=True;p.send_signal(signal.SIGTERM)
  try:rc=p.wait(timeout=10)
  except subprocess.TimeoutExpired:p.kill();rc=p.wait()
end=time.time()
rec={'schema':'round88-process-record-v1','name':a.name,'runner_pid':os.getpid(),'parent_pid':os.getppid(),
 'child_pid':p.pid,'command':cmd,'stdout':str(a.stdout),'stderr':str(a.stderr),'timeout_seconds':a.timeout,
 'expected_runtime':'seconds to 15 minutes','started_unix':start,'ended_unix':end,'wall_seconds':round(end-start,6),
 'timed_out':timed,'returncode':rc,'final_status':'timed_out_and_reaped' if timed else 'exited_and_reaped',
 'kill_harvest':'already reaped; inspect named logs and record'}
a.record.write_text(json.dumps(rec,indent=2,sort_keys=True)+'\n')
print(json.dumps({'event':'END',**rec},sort_keys=True),flush=True)
