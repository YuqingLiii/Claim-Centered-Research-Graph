#!/usr/bin/env python3
"""Round126 strict foreground runner with durable dual streams and checkpointing."""
from __future__ import annotations

import argparse
import datetime as dt
import fcntl
import json
import os
from pathlib import Path
import signal
import subprocess
import sys
import time


def now_utc() -> str:
    return dt.datetime.now(dt.timezone.utc).isoformat().replace("+00:00", "Z")


def append_jsonl(path: Path, row: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(row, sort_keys=True, separators=(",", ":")) + "\n")
        handle.flush()
        os.fsync(handle.fileno())


def atomic_json(path: Path, row: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(path.name + ".tmp")
    with temporary.open("w", encoding="utf-8") as handle:
        json.dump(row, handle, indent=2, sort_keys=True)
        handle.write("\n")
        handle.flush()
        os.fsync(handle.fileno())
    os.replace(temporary, path)


parser = argparse.ArgumentParser()
parser.add_argument("--ledger", type=Path, required=True)
parser.add_argument("--lock", type=Path, required=True)
parser.add_argument("--tag", required=True)
parser.add_argument("--cwd", type=Path, required=True)
parser.add_argument("--stdout", type=Path, required=True)
parser.add_argument("--stderr", type=Path, required=True)
parser.add_argument("--checkpoint", type=Path, required=True)
parser.add_argument("--env-json", default="{}")
parser.add_argument("--clean-env", action="store_true")
parser.add_argument("argv", nargs=argparse.REMAINDER)
args = parser.parse_args()

argv = args.argv[1:] if args.argv and args.argv[0] == "--" else args.argv
if not argv:
    parser.error("missing command")
overrides = {str(k): str(v) for k, v in json.loads(args.env_json).items()}
environment = {} if args.clean_env else dict(os.environ)
environment.update(overrides)
for path in (args.ledger, args.lock, args.stdout, args.stderr, args.checkpoint):
    path.parent.mkdir(parents=True, exist_ok=True)

with args.lock.open("a+b") as lock_handle:
    try:
        fcntl.flock(lock_handle.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
    except BlockingIOError:
        blocked = {
            "argv": argv,
            "checkpoint_utc": now_utc(),
            "next_action": "Do not launch; another Round126 child holds the serial lock.",
            "phase": "BLOCKED_BY_SERIAL_LOCK",
            "tag": args.tag,
            "wrapper_pid": os.getpid(),
        }
        atomic_json(args.checkpoint, blocked)
        append_jsonl(args.ledger, {**blocked, "state": "LOCK_REJECTED"})
        raise SystemExit(75)

    start = now_utc()
    start_ns = time.monotonic_ns()
    forwarded_signal: list[int | None] = [None]
    with args.stdout.open("xb") as stdout_handle, args.stderr.open("xb") as stderr_handle:
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
            "argv": argv,
            "child_pid": child.pid,
            "clean_env": args.clean_env,
            "cwd": str(args.cwd.resolve()),
            "detached": False,
            "env_overrides": overrides,
            "start_utc": start,
            "state": "STARTED",
            "stderr": str(args.stderr.resolve()),
            "stdout": str(args.stdout.resolve()),
            "tag": args.tag,
            "timeout_configured": False,
            "wrapper_pid": os.getpid(),
        }
        append_jsonl(args.ledger, started)
        atomic_json(args.checkpoint, {
            **started,
            "checkpoint_utc": start,
            "next_action": "Await and reap this exact child; do not launch another scientific child.",
            "phase": "SCIENTIFIC_CHILD_RUNNING",
        })
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
            for signum, previous in previous_handlers.items():
                signal.signal(signum, previous)
            if child.poll() is None:
                child.terminate()
                try:
                    returncode = child.wait(timeout=10)
                except subprocess.TimeoutExpired:
                    child.kill()
                    returncode = child.wait()

    end = now_utc()
    reaped = {
        **started,
        "duration_ns": time.monotonic_ns() - start_ns,
        "end_utc": end,
        "forwarded_signal": forwarded_signal[0],
        "rc": returncode,
        "reaped": True,
        "state": "REAPED",
        "stderr_bytes": args.stderr.stat().st_size,
        "stdout_bytes": args.stdout.stat().st_size,
        "timeout_triggered": False,
    }
    append_jsonl(args.ledger, reaped)
    atomic_json(args.checkpoint, {
        **reaped,
        "checkpoint_utc": end,
        "next_action": "Inspect the retained outputs before deciding the next strict-serial action.",
        "phase": "SCIENTIFIC_CHILD_REAPED",
    })
    print(json.dumps(reaped, sort_keys=True), flush=True)
    raise SystemExit(returncode)
