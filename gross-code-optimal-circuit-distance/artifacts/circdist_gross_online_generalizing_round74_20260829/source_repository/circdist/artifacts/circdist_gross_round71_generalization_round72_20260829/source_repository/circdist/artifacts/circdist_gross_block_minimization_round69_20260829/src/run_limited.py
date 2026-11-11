#!/usr/bin/env python3
import argparse, datetime, json, subprocess
from pathlib import Path
p=argparse.ArgumentParser();p.add_argument('--timeout',type=int,required=True);p.add_argument('--log',required=True);p.add_argument('--record',required=True);p.add_argument('command',nargs=argparse.REMAINDER);a=p.parse_args()
if a.command and a.command[0]=='--':a.command=a.command[1:]
started=datetime.datetime.now(datetime.timezone.utc).isoformat()
status='completed';rc=None
try:
 with open(a.log,'wb') as f:
  cp=subprocess.run(a.command,stdout=f,stderr=subprocess.STDOUT,timeout=a.timeout,check=False)
  rc=cp.returncode
except subprocess.TimeoutExpired:
 status='timeout';rc=124
ended=datetime.datetime.now(datetime.timezone.utc).isoformat()
Path(a.record).write_text(json.dumps({'started_utc':started,'ended_utc':ended,'timeout_seconds':a.timeout,'status':status,'exit_code':rc,'command':a.command},indent=2)+'\n')
raise SystemExit(0)
