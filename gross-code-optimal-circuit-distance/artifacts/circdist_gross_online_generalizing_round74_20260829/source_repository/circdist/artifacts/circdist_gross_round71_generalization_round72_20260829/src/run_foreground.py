#!/usr/bin/env python3
import argparse,datetime,json,os,signal,subprocess,sys,time
from pathlib import Path
ap=argparse.ArgumentParser()
ap.add_argument('--timeout-seconds',type=float,required=True)
ap.add_argument('--grace-seconds',type=float,default=5.0)
ap.add_argument('--log',type=Path,required=True)
ap.add_argument('--record',type=Path,required=True)
ap.add_argument('command',nargs=argparse.REMAINDER)
a=ap.parse_args()
cmd=a.command[1:] if a.command and a.command[0]=='--' else a.command
if not cmd: raise SystemExit('missing command')
a.log.parent.mkdir(parents=True,exist_ok=True); a.record.parent.mkdir(parents=True,exist_ok=True)
started=datetime.datetime.now(datetime.timezone.utc).isoformat(); t0=time.monotonic(); timed_out=False; term_sent=False; kill_sent=False; rc=None; pid=None; pgid=None
with a.log.open('wb') as out:
    p=subprocess.Popen(cmd,stdout=out,stderr=subprocess.STDOUT,start_new_session=True)
    pid=p.pid; pgid=os.getpgid(p.pid)
    try:
        rc=p.wait(timeout=a.timeout_seconds)
    except subprocess.TimeoutExpired:
        timed_out=True; term_sent=True
        try: os.killpg(pgid,signal.SIGTERM)
        except ProcessLookupError: pass
        try: rc=p.wait(timeout=a.grace_seconds)
        except subprocess.TimeoutExpired:
            kill_sent=True
            try: os.killpg(pgid,signal.SIGKILL)
            except ProcessLookupError: pass
            rc=p.wait()
ended=datetime.datetime.now(datetime.timezone.utc).isoformat(); wall=time.monotonic()-t0
record={'schema':'foreground-hard-limit-run-v1','argv':cmd,'started_utc':started,'ended_utc':ended,'pid':pid,'process_group':pgid,'timeout_seconds':a.timeout_seconds,'grace_seconds':a.grace_seconds,'timed_out':timed_out,'sigterm_sent':term_sent,'sigkill_sent':kill_sent,'exit_code':rc,'wall_seconds':wall,'log':str(a.log)}
a.record.write_text(json.dumps(record,indent=2,sort_keys=True)+'\n')
print(json.dumps(record,sort_keys=True))
raise SystemExit(124 if timed_out else (0 if rc in (0,10,20) else rc if isinstance(rc,int) else 1))
