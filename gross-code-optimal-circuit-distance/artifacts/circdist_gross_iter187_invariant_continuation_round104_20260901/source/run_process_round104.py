#!/usr/bin/env python3
"""Run exactly one foreground child, retain streams, timing, PID and rusage.

The wrapper never detaches its child.  On timeout it sends TERM, waits fifteen
seconds, sends KILL if necessary, and reaps the same PID before writing the
record.  SAT-competition return codes 10 and 20 are wrapper successes while
the raw child return code remains explicit in the JSON record.
"""
from pathlib import Path
import argparse
import datetime
import json
import os
import resource
import signal
import subprocess
import time


ap = argparse.ArgumentParser()
ap.add_argument("--name", required=True)
ap.add_argument("--timeout", type=float, required=True)
ap.add_argument("--stdout", type=Path, required=True)
ap.add_argument("--stderr", type=Path, required=True)
ap.add_argument("--record", type=Path, required=True)
ap.add_argument("command", nargs=argparse.REMAINDER)
args = ap.parse_args()
cmd = args.command[1:] if args.command and args.command[0] == "--" else args.command
if not cmd:
    raise SystemExit("missing command")

for path in (args.stdout, args.stderr, args.record):
    path.parent.mkdir(parents=True, exist_ok=True)

safe_env_names = ("PATH", "PYTHONPATH", "LANG", "LC_ALL", "LC_CTYPE", "TMPDIR", "SHELL")
safe_env = {key: os.environ[key] for key in safe_env_names if key in os.environ}
start_wall = time.time()
start_mono = time.monotonic()
start_iso = datetime.datetime.now(datetime.timezone.utc).isoformat()
r0 = resource.getrusage(resource.RUSAGE_CHILDREN)
timed_out = False
term_sent = False
kill_sent = False

with args.stdout.open("wb") as out, args.stderr.open("wb") as err:
    child = subprocess.Popen(cmd, stdout=out, stderr=err, start_new_session=False)
    print(json.dumps({
        "event": "START", "name": args.name, "runner_pid": os.getpid(),
        "parent_pid": os.getppid(), "child_pid": child.pid, "command": cmd,
        "cwd": os.getcwd(), "environment": safe_env, "started_utc": start_iso,
        "timeout_seconds": args.timeout, "stdout": str(args.stdout),
        "stderr": str(args.stderr),
    }, sort_keys=True), flush=True)
    try:
        rc = child.wait(timeout=args.timeout)
    except subprocess.TimeoutExpired:
        timed_out = True
        term_sent = True
        child.send_signal(signal.SIGTERM)
        try:
            rc = child.wait(timeout=15)
        except subprocess.TimeoutExpired:
            kill_sent = True
            child.kill()
            rc = child.wait()

end_wall = time.time()
end_iso = datetime.datetime.now(datetime.timezone.utc).isoformat()
r1 = resource.getrusage(resource.RUSAGE_CHILDREN)
record = {
    "schema": "circdist-gross-round104-process-record-v1",
    "name": args.name,
    "runner_pid": os.getpid(),
    "parent_pid": os.getppid(),
    "child_pid": child.pid,
    "command": cmd,
    "cwd": os.getcwd(),
    "environment": safe_env,
    "stdout": str(args.stdout),
    "stderr": str(args.stderr),
    "timeout_seconds": args.timeout,
    "started_unix": start_wall,
    "ended_unix": end_wall,
    "started_utc": start_iso,
    "ended_utc": end_iso,
    "wall_seconds": round(time.monotonic() - start_mono, 6),
    "child_user_seconds": round(r1.ru_utime - r0.ru_utime, 6),
    "child_system_seconds": round(r1.ru_stime - r0.ru_stime, 6),
    "child_maxrss_raw": r1.ru_maxrss,
    "timed_out": timed_out,
    "term_sent": term_sent,
    "kill_sent": kill_sent,
    "returncode": rc,
    "final_status": "timed_out_and_reaped" if timed_out else "exited_and_reaped",
    "reaped": True,
    "detached": False,
}
args.record.write_text(json.dumps(record, indent=2, sort_keys=True) + "\n")
print(json.dumps({"event": "END", **record}, sort_keys=True), flush=True)
raise SystemExit(0 if rc in (0, 10, 20) else rc if 0 <= rc <= 255 else 1)
