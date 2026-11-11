#!/usr/bin/env python3
"""Strict single-child display runner for small read-only inspection commands."""

import argparse
import datetime as dt
import fcntl
import json
import os
import subprocess
import sys
import time
from pathlib import Path


def now_utc():
    return dt.datetime.now(dt.timezone.utc).isoformat().replace("+00:00", "Z")


p = argparse.ArgumentParser()
p.add_argument("--ledger", type=Path, required=True)
p.add_argument("--lock", type=Path, required=True)
p.add_argument("--tag", required=True)
p.add_argument("--cwd", type=Path, required=True)
p.add_argument("--transcript", type=Path, required=True)
p.add_argument("cmd", nargs=argparse.REMAINDER)
a = p.parse_args()
if a.cmd and a.cmd[0] == "--":
    a.cmd = a.cmd[1:]
if not a.cmd:
    p.error("missing command")
a.ledger.parent.mkdir(parents=True, exist_ok=True)
a.lock.parent.mkdir(parents=True, exist_ok=True)
a.transcript.parent.mkdir(parents=True, exist_ok=True)
clean_env = {
    "LANG": "C.UTF-8",
    "LC_ALL": "C.UTF-8",
    "PATH": "/usr/bin:/bin:/usr/sbin:/sbin",
    "PYTHONDONTWRITEBYTECODE": "1",
    "TMPDIR": "/private/tmp/circdist-round122-proposer/tmp",
    "TZ": "UTC",
}
wrapper_pid = os.getpid()
with a.lock.open("a+b") as lock_handle:
    fcntl.flock(lock_handle.fileno(), fcntl.LOCK_EX)
    start = now_utc()
    t0 = time.monotonic_ns()
    proc = subprocess.Popen(
        a.cmd,
        cwd=str(a.cwd),
        env=clean_env,
        stdin=subprocess.DEVNULL,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    started = {
        "argv": a.cmd,
        "child_pid": proc.pid,
        "clean_env": True,
        "cwd": str(a.cwd),
        "detached": False,
        "start_utc": start,
        "state": "STARTED",
        "tag": a.tag,
        "timeout_configured": False,
        "wrapper_pid": wrapper_pid,
    }
    with a.ledger.open("a", encoding="utf-8") as fh:
        fh.write(json.dumps(started, sort_keys=True) + "\n")
        fh.flush()
        os.fsync(fh.fileno())
    out, err = proc.communicate()
    end = now_utc()
    ended = dict(started)
    ended.update({
        "duration_ns": time.monotonic_ns() - t0,
        "end_utc": end,
        "rc": proc.returncode,
        "reaped": True,
        "state": "REAPED",
        "stdout": str(a.transcript),
        "stdout_bytes": len(out),
        "stderr_bytes": len(err),
    })
    a.transcript.write_bytes(out)
    with a.ledger.open("a", encoding="utf-8") as fh:
        fh.write(json.dumps(ended, sort_keys=True) + "\n")
        fh.flush()
        os.fsync(fh.fileno())
    sys.stdout.buffer.write(out)
    sys.stdout.buffer.flush()
    sys.stderr.buffer.write(err)
    sys.stderr.buffer.flush()
    raise SystemExit(proc.returncode)
