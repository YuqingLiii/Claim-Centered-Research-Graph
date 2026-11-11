#!/usr/bin/env python3
"""Record a final process census and prove that no Round104 work survives."""
from pathlib import Path
import argparse
import datetime
import json
import os
import subprocess
import tempfile
import time


ap = argparse.ArgumentParser()
ap.add_argument("--root", type=Path, required=True)
ap.add_argument("--output", type=Path, required=True)
args = ap.parse_args()
root = args.root.resolve()
started = time.time()
child = subprocess.Popen(["/bin/ps", "-axo", "pid=,ppid=,stat=,etime=,command="],
                         stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True,
                         start_new_session=False)
stdout, stderr = child.communicate(timeout=30)
assert child.returncode == 0
patterns = [root.name, "cadical-1.9.5", "drat-trim-arm64", "lrat-check-arm64",
            "replay_round104.py", "advance_full_invariant_frontier_round104.py",
            "check_incremental_orbit_closure_round104.py", "compile_outer_cnf.py",
            "check_translation_quotient_round102.py"]
excluded_pids = {os.getpid(), os.getppid(), child.pid}
raw_matches, survivors = [], []
for line in stdout.splitlines():
    if not any(pattern in line for pattern in patterns):
        continue
    raw_matches.append(line)
    fields = line.strip().split(None, 4)
    pid = int(fields[0]) if fields else -1
    if pid not in excluded_pids and "/bin/ps -axo" not in line:
        survivors.append(line)
assert not survivors, survivors
tmp = Path(tempfile.gettempdir())
temporary_matches = sorted(str(p) for p in tmp.glob("circdist-round104-replay.*"))
assert not temporary_matches
result = {"schema": "circdist-gross-round104-final-process-census-v1",
          "status": "PASS", "checked_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
          "checked_unix": time.time(), "package": str(root), "patterns": patterns,
          "command": ["/bin/ps", "-axo", "pid=,ppid=,stat=,etime=,command="],
          "census_parent_pid": os.getpid(), "census_wrapper_pid": os.getppid(),
          "ps_child_pid": child.pid, "ps_returncode": child.returncode,
          "ps_child_reaped": True, "ps_stderr": stderr,
          "raw_pattern_matches": raw_matches, "excluded_pids": sorted(excluded_pids),
          "matching_live_science_processes": survivors, "science_survivor_count": 0,
          "detached_processes": 0, "replay_temporary_matches": temporary_matches,
          "wall_seconds": round(time.time() - started, 6)}
args.output.parent.mkdir(parents=True, exist_ok=True)
args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
print(json.dumps({"status": "PASS", "science_survivor_count": 0,
                  "ps_child_pid": child.pid, "temporary_matches": 0}, sort_keys=True))
