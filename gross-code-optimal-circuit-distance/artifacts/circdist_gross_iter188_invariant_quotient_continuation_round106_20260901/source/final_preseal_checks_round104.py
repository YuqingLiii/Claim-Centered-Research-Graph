#!/usr/bin/env python3
"""Run the final result, duplicate-key, and diff-hygiene checks serially."""
from pathlib import Path
import argparse
import datetime
import hashlib
import json
import os
import subprocess
import sys
import time


ap = argparse.ArgumentParser()
ap.add_argument("--repository", type=Path, required=True)
ap.add_argument("--package", type=Path, required=True)
args = ap.parse_args()
repo, package = args.repository.resolve(), args.package.resolve()
commands = [
    ("result_consistency", [sys.executable, package / "source/check_result_round104.py",
                            "--root", package, "--output",
                            package / "verification/result_consistency.json"]),
    ("duplicate_yaml_final", ["/usr/bin/python3", package / "source/duplicate_yaml_scan.py",
                              "--root", repo, "--output",
                              package / "verification/duplicate_yaml_final.json"]),
    ("git_diff_check_final", ["/usr/bin/git", "diff", "--check"]),
]
rows = []
for name, command in commands:
    command = [str(x) for x in command]
    started = time.time()
    child = subprocess.Popen(command, cwd=repo, stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE, text=True, start_new_session=False)
    stdout, stderr = child.communicate(timeout=1800)
    ended = time.time()
    assert child.returncode == 0, (name, child.returncode, stdout[-2000:], stderr[-2000:])
    rows.append({"name": name, "command": command, "parent_pid": os.getpid(),
                 "child_pid": child.pid, "started_unix": started, "ended_unix": ended,
                 "started_utc": datetime.datetime.fromtimestamp(started, datetime.timezone.utc).isoformat(),
                 "ended_utc": datetime.datetime.fromtimestamp(ended, datetime.timezone.utc).isoformat(),
                 "wall_seconds": round(ended - started, 6), "returncode": child.returncode,
                 "stdout": stdout, "stderr": stderr, "reaped": True, "detached": False,
                 "timed_out": False})
result = {"schema": "circdist-gross-round104-final-preseal-checks-v1",
          "status": "PASS", "strict_serial": True, "children": rows,
          "child_count": len(rows), "all_children_reaped": True,
          "detached_processes": 0, "result_consistency": "PASS",
          "duplicate_yaml": "PASS", "git_diff_check": "PASS"}
(package / "verification/final_preseal_checks.json").write_text(
    json.dumps(result, indent=2, sort_keys=True) + "\n")
print(json.dumps({"status": "PASS", "children": len(rows)}, sort_keys=True))
