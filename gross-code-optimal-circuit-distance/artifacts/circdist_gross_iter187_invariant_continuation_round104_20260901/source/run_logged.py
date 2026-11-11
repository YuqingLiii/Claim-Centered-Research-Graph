#!/usr/bin/env python3
from pathlib import Path
import argparse,datetime,json,os,signal,subprocess,time
p=argparse.ArgumentParser()
p.add_argument('--name',required=True);p.add_argument('--timeout',type=int,required=True)
p.add_argument('--stdout',type=Path,required=True);p.add_argument('--stderr',type=Path,required=True);p.add_argument('--record',type=Path,required=True)
p.add_argument('command',nargs=argparse.REMAINDER)
a=p.parse_args();cmd=a.command[1:] if a.command and a.command[0]=='--' else a.command
if not cmd: raise SystemExit('missing command')
a.stdout.parent.mkdir(parents=True,exist_ok=True);a.stderr.parent.mkdir(parents=True,exist_ok=True);a.record.parent.mkdir(parents=True,exist_ok=True)
start=time.time();start_iso=datetime.datetime.now(datetime.timezone.utc).isoformat()
with a.stdout.open('wb') as out,a.stderr.open('wb') as err:
 child=subprocess.Popen(cmd,stdout=out,stderr=err,start_new_session=False)
 print(json.dumps({'event':'START','name':a.name,'runner_pid':os.getpid(),'parent_pid':os.getppid(),'child_pid':child.pid,'command':cmd,'started_utc':start_iso,'timeout_seconds':a.timeout,'stdout':str(a.stdout),'stderr':str(a.stderr)},sort_keys=True),flush=True)
 timed=False;term_sent=False;kill_sent=False
 try: rc=child.wait(timeout=a.timeout)
 except subprocess.TimeoutExpired:
  timed=True;term_sent=True;child.send_signal(signal.SIGTERM)
  try: rc=child.wait(timeout=15)
  except subprocess.TimeoutExpired:
   kill_sent=True;child.kill();rc=child.wait()
end=time.time();end_iso=datetime.datetime.now(datetime.timezone.utc).isoformat()
rec={'schema':'circdist-round94-process-record-v1','name':a.name,'runner_pid':os.getpid(),'parent_pid':os.getppid(),'child_pid':child.pid,'command':cmd,'stdout':str(a.stdout),'stderr':str(a.stderr),'timeout_seconds':a.timeout,'started_unix':start,'ended_unix':end,'started_utc':start_iso,'ended_utc':end_iso,'wall_seconds':round(end-start,6),'timed_out':timed,'term_sent':term_sent,'kill_sent':kill_sent,'returncode':rc,'final_status':'timed_out_and_reaped' if timed else 'exited_and_reaped','reaped':True,'detached':False}
with a.record.open('w',encoding='utf-8',newline='\n') as f: json.dump(rec,f,indent=2,sort_keys=True);f.write('\n')
print(json.dumps({'event':'END',**rec},sort_keys=True),flush=True)
raise SystemExit(0 if rc in (0,10,20) else rc if 0<=rc<=255 else 1)
