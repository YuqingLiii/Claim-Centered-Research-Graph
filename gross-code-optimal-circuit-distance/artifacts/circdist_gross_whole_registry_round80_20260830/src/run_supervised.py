#!/usr/bin/env python3
"""Run one foreground process group with hard timeout and sampled resource ledger."""
from __future__ import annotations

import argparse
import datetime
import json
import os
from pathlib import Path
import signal
import subprocess
import time

import psutil


ap = argparse.ArgumentParser()
ap.add_argument("--timeout-seconds", type=float, required=True)
ap.add_argument("--grace-seconds", type=float, default=5.0)
ap.add_argument("--sample-seconds", type=float, default=0.05)
ap.add_argument("--log", type=Path, required=True)
ap.add_argument("--record", type=Path, required=True)
ap.add_argument("command", nargs=argparse.REMAINDER)
a = ap.parse_args()
cmd = a.command[1:] if a.command and a.command[0] == "--" else a.command
if not cmd:
    raise SystemExit("missing command")

a.log.parent.mkdir(parents=True, exist_ok=True)
a.record.parent.mkdir(parents=True, exist_ok=True)
started = datetime.datetime.now(datetime.timezone.utc).isoformat()
t0 = time.monotonic()
timed_out = term_sent = kill_sent = False
max_rss = max_vms = max_processes = samples = 0


def sample_tree(pid: int) -> None:
    global max_rss, max_vms, max_processes, samples
    try:
        root = psutil.Process(pid)
        procs = [root] + root.children(recursive=True)
    except (psutil.NoSuchProcess, psutil.AccessDenied):
        return
    rss = vms = live = 0
    for proc in procs:
        try:
            mem = proc.memory_info()
            rss += mem.rss
            vms += mem.vms
            live += 1
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            pass
    max_rss = max(max_rss, rss)
    max_vms = max(max_vms, vms)
    max_processes = max(max_processes, live)
    samples += 1


with a.log.open("wb") as out:
    p = subprocess.Popen(cmd, stdout=out, stderr=subprocess.STDOUT, start_new_session=True)
    pid = p.pid
    pgid = os.getpgid(pid)
    deadline = t0 + a.timeout_seconds
    while p.poll() is None and time.monotonic() < deadline:
        sample_tree(pid)
        time.sleep(a.sample_seconds)
    sample_tree(pid)
    if p.poll() is None:
        timed_out = term_sent = True
        try:
            os.killpg(pgid, signal.SIGTERM)
        except ProcessLookupError:
            pass
        grace_deadline = time.monotonic() + a.grace_seconds
        while p.poll() is None and time.monotonic() < grace_deadline:
            sample_tree(pid)
            time.sleep(a.sample_seconds)
        if p.poll() is None:
            kill_sent = True
            try:
                os.killpg(pgid, signal.SIGKILL)
            except ProcessLookupError:
                pass
    rc = p.wait()

ended = datetime.datetime.now(datetime.timezone.utc).isoformat()
record = {
    "schema": "foreground-hard-limit-resource-run-v2",
    "argv": cmd,
    "started_utc": started,
    "ended_utc": ended,
    "pid": pid,
    "process_group": pgid,
    "timeout_seconds": a.timeout_seconds,
    "grace_seconds": a.grace_seconds,
    "sample_seconds": a.sample_seconds,
    "sample_count": samples,
    "timed_out": timed_out,
    "sigterm_sent": term_sent,
    "sigkill_sent": kill_sent,
    "exit_code": rc,
    "wall_seconds": time.monotonic() - t0,
    "max_rss_bytes": max_rss,
    "max_vms_bytes": max_vms,
    "max_processes": max_processes,
    "log": str(a.log),
}
a.record.write_text(json.dumps(record, indent=2, sort_keys=True) + "\n")
print(json.dumps(record, sort_keys=True))
raise SystemExit(124 if timed_out else (0 if rc in (0, 10, 20) else rc if isinstance(rc, int) else 1))
