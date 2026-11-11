#!/usr/bin/env python3
from pathlib import Path
import argparse, datetime, hashlib, json, os, resource, signal, subprocess, time

def sha256(path):
    h=hashlib.sha256()
    with Path(path).open('rb') as f:
        for b in iter(lambda:f.read(8<<20),b''): h.update(b)
    return h.hexdigest()

ap=argparse.ArgumentParser()
ap.add_argument('--name',required=True)
ap.add_argument('--timeout',type=float,required=True)
ap.add_argument('--stdout',type=Path,required=True)
ap.add_argument('--stderr',type=Path,required=True)
ap.add_argument('--record',type=Path,required=True)
ap.add_argument('--expected-rc',type=int,action='append',default=[])
ap.add_argument('command',nargs=argparse.REMAINDER)
a=ap.parse_args(); cmd=a.command[1:] if a.command and a.command[0]=='--' else a.command
if not cmd: raise SystemExit('missing command')
for p in (a.stdout,a.stderr,a.record): p.parent.mkdir(parents=True,exist_ok=True)
safe=('PATH','PYTHONPATH','LANG','LC_ALL','LC_CTYPE','TMPDIR','SHELL','PYTHONDONTWRITEBYTECODE')
env={k:os.environ[k] for k in safe if k in os.environ}
start_wall=time.time(); start_mono=time.monotonic(); start_iso=datetime.datetime.now(datetime.timezone.utc).isoformat()
r0=resource.getrusage(resource.RUSAGE_CHILDREN); timed_out=term_sent=kill_sent=False
with a.stdout.open('wb') as out, a.stderr.open('wb') as err:
    child=subprocess.Popen(cmd,stdout=out,stderr=err,start_new_session=False)
    print(json.dumps({'event':'START','name':a.name,'runner_pid':os.getpid(),'parent_pid':os.getppid(),'child_pid':child.pid,'argv':cmd,'cwd':os.getcwd(),'environment':env,'started_utc':start_iso,'timeout_seconds':a.timeout},sort_keys=True),flush=True)
    try: rc=child.wait(timeout=a.timeout)
    except subprocess.TimeoutExpired:
        timed_out=term_sent=True; child.send_signal(signal.SIGTERM)
        try: rc=child.wait(timeout=15)
        except subprocess.TimeoutExpired:
            kill_sent=True; child.kill(); rc=child.wait()
end_wall=time.time(); r1=resource.getrusage(resource.RUSAGE_CHILDREN)
expected=a.expected_rc or [0]
record={'schema':'circdist-gross-round110-process-record-v1','name':a.name,'runner_pid':os.getpid(),'parent_pid':os.getppid(),'child_pid':child.pid,'argv':cmd,'cwd':os.getcwd(),'environment':env,'stdout':str(a.stdout),'stderr':str(a.stderr),'timeout_seconds':a.timeout,'started_unix':start_wall,'ended_unix':end_wall,'started_utc':start_iso,'ended_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'wall_seconds':round(time.monotonic()-start_mono,6),'child_user_seconds':round(r1.ru_utime-r0.ru_utime,6),'child_system_seconds':round(r1.ru_stime-r0.ru_stime,6),'child_maxrss_raw':r1.ru_maxrss,'timed_out':timed_out,'term_sent':term_sent,'kill_sent':kill_sent,'returncode':rc,'expected_returncodes':expected,'returncode_matches':rc in expected,'final_status':'timed_out_and_reaped' if timed_out else 'exited_and_reaped','reaped':True,'detached':False,'stdout_sha256':sha256(a.stdout),'stdout_bytes':a.stdout.stat().st_size,'stderr_sha256':sha256(a.stderr),'stderr_bytes':a.stderr.stat().st_size}
a.record.write_text(json.dumps(record,indent=2,sort_keys=True)+'\n')
print(json.dumps({'event':'END',**record},sort_keys=True),flush=True)
raise SystemExit(0 if (rc in expected and not timed_out) else 124 if timed_out else rc if 0<=rc<=255 else 1)
