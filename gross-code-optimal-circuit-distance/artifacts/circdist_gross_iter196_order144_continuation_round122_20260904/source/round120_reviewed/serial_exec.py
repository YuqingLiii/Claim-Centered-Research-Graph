#!/usr/bin/env python3
import argparse, datetime, fcntl, json, os, pathlib, subprocess, sys, time

def utc_now():
    return datetime.datetime.now(datetime.timezone.utc).isoformat().replace('+00:00','Z')

p=argparse.ArgumentParser()
p.add_argument('--ledger', required=True)
p.add_argument('--lock', required=True)
p.add_argument('--tag', required=True)
p.add_argument('--stdout', required=True)
p.add_argument('--stderr', required=True)
p.add_argument('--cwd', required=True)
p.add_argument('--env-json', default='{}')
p.add_argument('--clean-env', action='store_true')
p.add_argument('--preview-bytes', type=int, default=0)
p.add_argument('argv', nargs=argparse.REMAINDER)
a=p.parse_args()
argv=a.argv[1:] if a.argv and a.argv[0]=='--' else a.argv
if not argv: p.error('missing command')
env_overrides=json.loads(a.env_json)
if a.clean_env:
    env={}
else:
    env=dict(os.environ)
env.update({str(k):str(v) for k,v in env_overrides.items()})
for path in (a.ledger,a.lock,a.stdout,a.stderr): pathlib.Path(path).parent.mkdir(parents=True,exist_ok=True)
with open(a.lock,'a+',encoding='utf-8') as lock:
    fcntl.flock(lock, fcntl.LOCK_EX|fcntl.LOCK_NB)
    start=utc_now(); mono=time.monotonic_ns()
    with open(a.stdout,'wb') as out, open(a.stderr,'wb') as err:
        proc=subprocess.Popen(argv,cwd=a.cwd,env=env,stdin=subprocess.DEVNULL,stdout=out,stderr=err,start_new_session=False)
        rec0={'tag':a.tag,'state':'STARTED','argv':argv,'cwd':os.path.abspath(a.cwd),'clean_env':a.clean_env,'env_overrides':env_overrides,'wrapper_pid':os.getpid(),'child_pid':proc.pid,'start_utc':start}
        with open(a.ledger,'a',encoding='utf-8') as lf:
            lf.write(json.dumps(rec0,sort_keys=True,separators=(',',':'))+'\n'); lf.flush(); os.fsync(lf.fileno())
        rc=proc.wait()
    end=utc_now(); dur=time.monotonic_ns()-mono
    rec1={'tag':a.tag,'state':'REAPED','argv':argv,'cwd':os.path.abspath(a.cwd),'clean_env':a.clean_env,'env_overrides':env_overrides,'wrapper_pid':os.getpid(),'child_pid':proc.pid,'start_utc':start,'end_utc':end,'duration_ns':dur,'rc':rc,'stdout':os.path.abspath(a.stdout),'stderr':os.path.abspath(a.stderr),'stdout_bytes':os.path.getsize(a.stdout),'stderr_bytes':os.path.getsize(a.stderr)}
    with open(a.ledger,'a',encoding='utf-8') as lf:
        lf.write(json.dumps(rec1,sort_keys=True,separators=(',',':'))+'\n'); lf.flush(); os.fsync(lf.fileno())
    print(json.dumps(rec1,sort_keys=True))
    if a.preview_bytes:
        with open(a.stdout,'rb') as preview:
            sys.stdout.buffer.write(preview.read(a.preview_bytes))
        sys.stdout.buffer.flush()
    sys.exit(rc)
