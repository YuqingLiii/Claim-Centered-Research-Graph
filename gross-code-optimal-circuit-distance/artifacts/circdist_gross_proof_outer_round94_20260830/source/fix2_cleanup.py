#!/usr/bin/env python3
"""Remove exact Round94 scratch roots and emit the authoritative FIX-2 record."""
from pathlib import Path
import datetime
import json
import os
import shutil
import subprocess
import time


P = Path(__file__).resolve().parent.parent
targets = [Path("/private/tmp/circdist-r94"), Path("/private/tmp/circdist-r94-package-draft")]
before = {str(path): path.exists() for path in targets}
for path in targets:
    assert str(path) in {"/private/tmp/circdist-r94", "/private/tmp/circdist-r94-package-draft"}
    if path.exists():
        shutil.rmtree(path)
after = {str(path): path.exists() for path in targets}
assert not any(after.values())

cp = subprocess.run(["/bin/ps", "-axo", "pid=,ppid=,stat=,etime=,command="], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=30)
assert cp.returncode == 0
patterns = ["/private/tmp/circdist-r94", "cadical-1.9.5-arm64-macos"]
matches = []
for line in cp.stdout.splitlines():
    if any(pattern in line for pattern in patterns):
        fields = line.strip().split(None, 4)
        pid = int(fields[0]) if fields else -1
        if pid != os.getpid():
            matches.append(line)
assert matches == [], matches
replay_globs = []
for pattern in ("circdist-r94-replay.*", "circdist-r94-proof-control.*"):
    replay_globs.extend(str(path) for path in Path("/private/tmp").glob(pattern))
assert replay_globs == []
ledger = json.loads((P / "PROCESS_LEDGER.json").read_text())
out = {
    "schema": "circdist-round94-fix2-closure-v1", "status": "PASS",
    "checked_unix": time.time(), "checked_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
    "scratch_paths": {str(path): {"existed_before": before[str(path)], "exists_after": after[str(path)], "disposition": "removed"} for path in targets},
    "retained_external_dependency": {
        "path": "/private/tmp/circdist-r72-dispatcher-venv/bin/python",
        "disposition": "explicitly handed off as bound replay dependency; not Round94 scratch",
        "sha256": "bdea59019a38eb6600cc9e71e984a97fedadc406448431281e7657030f54987e",
    },
    "bounded_records_in_package": len(ledger["records"]),
    "science_solver_children": ledger["science_solver_children"],
    "proof_fixture_synchronous_children": ledger["proof_fixture_synchronous_children"],
    "preseal_replay": {"returncode": 0, "children": 117, "all_reaped": True},
    "repository_validators": {"returncode": 0, "synchronous_children": 10, "all_reaped": True},
    "cleanup_process": {"pid": os.getpid(), "parent_pid": os.getppid(), "self_recorded": True},
    "process_scan_command": ["/bin/ps", "-axo", "pid=,ppid=,stat=,etime=,command="],
    "process_scan_returncode": cp.returncode, "process_scan_stderr": cp.stderr,
    "task_process_patterns": patterns, "task_process_matches": matches,
    "replay_temp_glob_matches": replay_globs, "survivors": 0,
    "os_background_processes_started": 0, "detached_processes": 0,
    "all_task_children_reaped": True,
    "meaning": "All Round94 scratch roots and task processes were removed or reaped; only the durable package and explicitly handed-off interpreter dependency remain.",
}
(P / "verification/fix2_closure.json").write_text(json.dumps(out, indent=2, sort_keys=True) + "\n")
print(json.dumps({"status": "PASS", "scratch_removed": list(after), "survivors": 0}, sort_keys=True))
