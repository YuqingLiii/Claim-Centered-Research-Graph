#!/usr/bin/env python3
"""Refresh mutable preseal sources, verification records, and logs in the Round122 stage."""
import argparse
import json
import os
import shutil
from pathlib import Path

p = argparse.ArgumentParser()
p.add_argument("--work", type=Path, required=True)
p.add_argument("--root", type=Path, required=True)
a = p.parse_args(); W, R = a.work.resolve(), a.root.resolve()


def copy(src, dst):
    src, dst = Path(src), Path(dst)
    dst.parent.mkdir(parents=True, exist_ok=True)
    if dst.exists():
        os.chmod(dst, 0o644)
    shutil.copy2(src, dst)
    assert dst.stat().st_nlink == 1 and not dst.is_symlink()


for src in sorted(W.glob("*.py")):
    copy(src, R / "source" / src.name)
    os.chmod(R / "source" / src.name, 0o555)
shutil.copytree(W / "logs", R / "logs/session_and_process", dirs_exist_ok=True, copy_function=shutil.copy2)
# Freeze a paired cutpoint: the supervising wrapper has written this sync
# child's STARTED row but cannot write its REAPED row until after this child exits.
live_ledger = W / "logs/process/session_process.jsonl"
rows = [json.loads(line) for line in live_ledger.read_text().splitlines() if line.strip()]
cut = [row for row in rows if row.get("child_pid") != os.getpid()]
target_ledger = R / "logs/session_and_process/process/session_process.jsonl"
target_ledger.write_text("".join(json.dumps(row, sort_keys=True) + "\n" for row in cut))
assert all(sum(1 for other in cut if other.get("child_pid") == row.get("child_pid") and other.get("state") == "REAPED") == 1 for row in cut if row.get("state") == "STARTED")
shutil.copytree(W / "verification", R / "verification", dirs_exist_ok=True, copy_function=shutil.copy2)
copy(W / "verification/process_ledger_check.json", R / "PROCESS_LEDGER_CHECK.json")
copy(W / "process-ledger-preflight.jsonl", R / "logs/preflight/process-ledger-preflight.jsonl")
copy(W / "targeted-inspection.txt", R / "logs/preflight/targeted-inspection.txt")
replay = """#!/bin/sh
set -eu
if [ "$#" -ne 1 ]; then
  echo "usage: $0 ABSOLUTE_EXTERNAL_OUTPUT_DIRECTORY" >&2
  exit 64
fi
ROOT=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
exec /usr/bin/python3 "$ROOT/source/replay_round122.py" --root "$ROOT" --output "$1"
"""
if (R / "replay.sh").exists():
    os.chmod(R / "replay.sh", 0o644)
(R / "replay.sh").write_text(replay)
os.chmod(R / "replay.sh", 0o555)
print("PASS")
