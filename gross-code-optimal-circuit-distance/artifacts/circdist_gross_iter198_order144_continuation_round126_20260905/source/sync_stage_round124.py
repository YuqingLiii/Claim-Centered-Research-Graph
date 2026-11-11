#!/usr/bin/env python3
"""Refresh mutable preseal package material from the Round124 work tree."""
from __future__ import annotations

import argparse
import hashlib
import os
import shutil
from pathlib import Path


def sha(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(8 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


p = argparse.ArgumentParser()
p.add_argument("--work", type=Path, required=True)
p.add_argument("--root", type=Path, required=True)
a = p.parse_args()
W, R = a.work.resolve(), a.root.resolve()
assert W.is_dir() and R.is_dir()


def refresh_tree(src: Path, dst: Path, executable_python: bool = False) -> int:
    count = 0
    for item in sorted(src.rglob("*")):
        assert not item.is_symlink()
        rel = item.relative_to(src)
        target = dst / rel
        if item.is_dir():
            target.mkdir(parents=True, exist_ok=True)
            continue
        target.parent.mkdir(parents=True, exist_ok=True)
        if target.exists():
            os.chmod(target, 0o644)
        shutil.copy2(item, target)
        assert sha(item) == sha(target)
        assert item.stat().st_ino != target.stat().st_ino or item.stat().st_dev != target.stat().st_dev
        assert target.stat().st_nlink == 1
        if executable_python and target.suffix == ".py":
            os.chmod(target, 0o555)
        count += 1
    return count


source_files = refresh_tree(W / "source", R / "source", True)
verification_files = refresh_tree(W / "verification", R / "verification")
log_files = refresh_tree(W / "logs", R / "logs/session_and_process")
replay = """#!/bin/sh
set -eu
ROOT=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
if [ "$#" -lt 1 ]; then
  echo "usage: $0 OUTPUT_DIR [replay options]" >&2
  exit 2
fi
OUT=$1
shift
exec /usr/bin/python3 "$ROOT/source/replay_round124.py" --root "$ROOT" --output "$OUT" "$@"
"""
if (R / "replay.sh").exists():
    os.chmod(R / "replay.sh", 0o644)
(R / "replay.sh").write_text(replay)
os.chmod(R / "replay.sh", 0o555)
print({"status": "PASS", "source_files": source_files,
       "verification_files": verification_files, "log_files": log_files})
