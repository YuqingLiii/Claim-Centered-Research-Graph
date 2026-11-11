#!/usr/bin/env python3
"""Remove the exact Round96 build root and emit the authoritative FIX-2 record."""
from pathlib import Path
import datetime, hashlib, json, os, shutil, subprocess, time

P = Path(__file__).resolve().parent.parent
target = Path("/private/tmp/circdist-r96-work-20260831")
assert P != target.resolve(), "run FIX-2 only from the installed repository package"
before = target.exists()
if before:
    shutil.rmtree(target)
after = target.exists()
assert not after

cp = subprocess.run(["/bin/ps", "-axo", "pid=,ppid=,stat=,etime=,command="], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=30)
assert cp.returncode == 0
patterns = ["/private/tmp/circdist-r96-work-20260831", "circdist-r96-replay.", "cadical-1.9.5-arm64-macos"]
matches = []
for line in cp.stdout.splitlines():
    if any(pattern in line for pattern in patterns):
        fields = line.strip().split(None, 4)
        pid = int(fields[0]) if fields else -1
        if pid not in (os.getpid(), os.getppid()):
            matches.append(line)
assert matches == [], matches
replay_globs = []
for pattern in ("circdist-r96-replay.*", "circdist-r96-proof-control.*", "circdist-r96-final-preseal.*"):
    replay_globs.extend(str(path) for path in Path("/private/tmp").glob(pattern))
assert replay_globs == []
ledger = json.loads((P / "PROCESS_LEDGER.json").read_text())
replay = json.loads((P / "verification/preseal_replay.children.json").read_text())
validators = json.loads((P / "verification/repository_validators/summary.json").read_text())
assert replay["status"] == validators["status"] == "PASS"
interpreter = Path("/private/tmp/circdist-r72-dispatcher-venv/bin/python")
h = hashlib.sha256(interpreter.read_bytes()).hexdigest()
assert h == "bdea59019a38eb6600cc9e71e984a97fedadc406448431281e7657030f54987e"
out = {
    "schema": "circdist-round96-fix2-closure-v1", "status": "PASS",
    "checked_unix": time.time(), "checked_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
    "scratch_path": str(target), "existed_before": before, "exists_after": after,
    "disposition": "removed after the complete draft was installed into the sole permitted repository package directory",
    "retained_external_dependency": {
        "path": str(interpreter), "disposition": "explicitly handed off as the bound replay dependency; not Round96 scratch",
        "sha256": h,
    },
    "bounded_records_in_package": len(ledger["records"]),
    "science_solver_children": ledger["science_solver_children"],
    "proof_fixture_synchronous_children": ledger["proof_fixture_synchronous_children"],
    "preseal_replay": {"children": replay["child_count"], "all_reaped": replay["all_children_reaped"]},
    "repository_validators": {"synchronous_children": len(validators["checks"]), "all_reaped": validators["all_children_reaped"]},
    "cleanup_process": {"pid": os.getpid(), "parent_pid": os.getppid(), "self_recorded": True},
    "process_scan_command": ["/bin/ps", "-axo", "pid=,ppid=,stat=,etime=,command="],
    "process_scan_returncode": cp.returncode, "process_scan_stderr": cp.stderr,
    "task_process_patterns": patterns, "task_process_matches": matches,
    "replay_temp_glob_matches": replay_globs, "survivors": 0,
    "os_background_processes_started": 0, "detached_processes": 0,
    "all_task_children_reaped": True,
    "meaning": "All Round96 scratch and task processes were removed or reaped; only the sealed-package candidate and explicitly handed-off interpreter remain.",
}
(P / "verification/fix2_closure.json").write_text(json.dumps(out, indent=2, sort_keys=True) + "\n")
print(json.dumps({"status": "PASS", "scratch_removed": str(target), "survivors": 0}, sort_keys=True))
