#!/usr/bin/env python3
"""Refresh complete pre-cutpoint session logs without copying this active operation."""
import argparse
import os
import shutil
from pathlib import Path


ap = argparse.ArgumentParser()
ap.add_argument("--source", type=Path, required=True)
ap.add_argument("--destination", type=Path, required=True)
ap.add_argument("--exclude-prefix", required=True)
a = ap.parse_args()
a.destination.mkdir(parents=True, exist_ok=True)
for stale in ("session_process.jsonl", "science.lock"):
    path = a.destination / stale
    if path.exists():
        path.unlink()
copied = 0
for source in sorted(p for p in a.source.rglob("*") if p.is_file()):
    relative = source.relative_to(a.source)
    if relative.as_posix() == "session_process.jsonl" or source.suffix == ".lock":
        continue
    if source.name.startswith(a.exclude_prefix):
        continue
    destination = a.destination / relative
    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source, destination)
    assert (source.stat().st_dev, source.stat().st_ino) != (destination.stat().st_dev, destination.stat().st_ino)
    assert destination.stat().st_nlink == 1
    copied += 1
print(f"PASS copied={copied}")
