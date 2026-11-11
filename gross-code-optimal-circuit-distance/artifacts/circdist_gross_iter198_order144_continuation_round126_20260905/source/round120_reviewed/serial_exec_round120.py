#!/usr/bin/env python3
"""Foreground-only, lock-serialized child runner with complete start/reap records."""
from __future__ import annotations

import argparse
import datetime
import fcntl
import json
import os
from pathlib import Path
import signal
import subprocess
import sys
import time


def utc_now() -> str:
    return datetime.datetime.now(datetime.timezone.utc).isoformat().replace("+00:00", "Z")


def append_jsonl(path: Path, row: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(row, sort_keys=True, separators=(",", ":")) + "\n")
        handle.flush()
        os.fsync(handle.fileno())


parser = argparse.ArgumentParser()
parser.add_argument("--ledger", type=Path, required=True)
parser.add_argument("--lock", type=Path, required=True)
parser.add_argument("--tag", required=True)
parser.add_argument("--stdout", type=Path, required=True)
parser.add_argument("--stderr", type=Path, required=True)
parser.add_argument("--cwd", type=Path, required=True)
parser.add_argument("--env-json", default="{}")
parser.add_argument("--clean-env", action="store_true")
parser.add_argument("--preview-bytes", type=int, default=0)
parser.add_argument("argv", nargs=argparse.REMAINDER)
args = parser.parse_args()

argv = args.argv[1:] if args.argv and args.argv[0] == "--" else args.argv
if not argv:
    parser.error("missing command")

overrides = {str(k): str(v) for k, v in json.loads(args.env_json).items()}
environment = {} if args.clean_env else dict(os.environ)
environment.update(overrides)
for path in (args.ledger, args.lock, args.stdout, args.stderr):
    path.parent.mkdir(parents=True, exist_ok=True)

with args.lock.open("a+", encoding="utf-8") as lock_handle:
    fcntl.flock(lock_handle, fcntl.LOCK_EX | fcntl.LOCK_NB)
    start = utc_now()
    monotonic_start = time.monotonic_ns()
    forwarded_signal: list[int | None] = [None]
    with args.stdout.open("wb") as stdout_handle, args.stderr.open("wb") as stderr_handle:
        child = subprocess.Popen(
            argv,
            cwd=str(args.cwd.resolve()),
            env=environment,
            stdin=subprocess.DEVNULL,
            stdout=stdout_handle,
            stderr=stderr_handle,
            start_new_session=False,
        )
        started = {
            "tag": args.tag,
            "state": "STARTED",
            "argv": argv,
            "cwd": str(args.cwd.resolve()),
            "clean_env": args.clean_env,
            "env_overrides": overrides,
            "wrapper_pid": os.getpid(),
            "child_pid": child.pid,
            "start_utc": start,
            "detached": False,
            "timeout_configured": False,
        }
        append_jsonl(args.ledger, started)
        print(json.dumps(started, sort_keys=True), flush=True)

        previous_handlers: dict[int, object] = {}

        def forward(signum: int, _frame: object) -> None:
            forwarded_signal[0] = signum
            if child.poll() is None:
                child.send_signal(signum)

        for signum in (signal.SIGINT, signal.SIGTERM, signal.SIGHUP):
            previous_handlers[signum] = signal.signal(signum, forward)
        try:
            returncode = child.wait()
        finally:
            for signum, handler in previous_handlers.items():
                signal.signal(signum, handler)
            if child.poll() is None:
                child.terminate()
                try:
                    returncode = child.wait(timeout=10)
                except subprocess.TimeoutExpired:
                    child.kill()
                    returncode = child.wait()

    end = utc_now()
    reaped = {
        "tag": args.tag,
        "state": "REAPED",
        "argv": argv,
        "cwd": str(args.cwd.resolve()),
        "clean_env": args.clean_env,
        "env_overrides": overrides,
        "wrapper_pid": os.getpid(),
        "child_pid": child.pid,
        "start_utc": start,
        "end_utc": end,
        "duration_ns": time.monotonic_ns() - monotonic_start,
        "rc": returncode,
        "stdout": str(args.stdout.resolve()),
        "stderr": str(args.stderr.resolve()),
        "stdout_bytes": args.stdout.stat().st_size,
        "stderr_bytes": args.stderr.stat().st_size,
        "reaped": True,
        "detached": False,
        "timeout_configured": False,
        "timeout_triggered": False,
        "forwarded_signal": forwarded_signal[0],
    }
    append_jsonl(args.ledger, reaped)
    print(json.dumps(reaped, sort_keys=True), flush=True)
    if args.preview_bytes:
        with args.stdout.open("rb") as preview:
            sys.stdout.buffer.write(preview.read(args.preview_bytes))
        sys.stdout.buffer.flush()
    raise SystemExit(returncode)
