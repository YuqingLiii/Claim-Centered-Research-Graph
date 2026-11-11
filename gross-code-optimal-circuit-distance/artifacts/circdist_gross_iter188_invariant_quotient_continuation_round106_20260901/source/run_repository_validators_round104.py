#!/usr/bin/env python3
"""Run the Round104 repository gate set strictly serially and retain each child."""
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
outdir = package / "verification/repository_validators"
outdir.mkdir(parents=True, exist_ok=True)
commands = [
    ("live_governance", [sys.executable, package / "source/check_live_governance_round104.py",
                         "--repository", repo, "--package", package,
                         "--output", package / "verification/live_governance_check.json"], 0),
    ("proof_dag_circdist", ["/usr/bin/python3", "tools/proof_dag_check.py", "--problem", "circdist"], 0),
    ("proof_dag_all", ["/usr/bin/python3", "tools/proof_dag_check.py", "--problem", "all"], 0),
    ("circdist_migration", ["/usr/bin/python3", "tools/check_circdist_migration.py"], 0),
    ("release_contracts", ["/usr/bin/python3", "tools/test_release_contracts.py"], 0),
    ("dag_contracts", ["/usr/bin/python3", "tools/test_dag_contracts.py"], 0),
    ("lean_dag_selftest", ["/usr/bin/python3", "tools/lean_dag_check.py", "--selftest"], 0),
    ("duplicate_yaml", ["/usr/bin/python3", package / "source/duplicate_yaml_scan.py",
                        "--root", repo, "--output", outdir / "duplicate_yaml.result.json"], 0),
    ("git_diff_check", ["/usr/bin/git", "diff", "--check"], 0),
    ("evidence_closure", ["/usr/bin/python3", "tools/evidence_closure_check.py",
                          "--problem", "circdist"], 1),
]
rows = []
for name, command, expected in commands:
    command = [str(x) for x in command]
    started = time.time()
    child = subprocess.Popen(command, cwd=repo, stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE, start_new_session=False)
    timed_out = term_sent = kill_sent = False
    try:
        stdout, stderr = child.communicate(timeout=1800)
    except subprocess.TimeoutExpired:
        timed_out = term_sent = True
        child.terminate()
        try:
            stdout, stderr = child.communicate(timeout=15)
        except subprocess.TimeoutExpired:
            kill_sent = True
            child.kill()
            stdout, stderr = child.communicate()
    ended = time.time()
    stdout_path, stderr_path = outdir / f"{name}.stdout.log", outdir / f"{name}.stderr.log"
    stdout_path.write_bytes(stdout)
    stderr_path.write_bytes(stderr)
    row = {"schema": "circdist-gross-round104-validator-child-v1", "name": name,
           "command": command, "expected_returncode": expected, "returncode": child.returncode,
           "returncode_matches": not timed_out and child.returncode == expected,
           "parent_pid": os.getpid(), "child_pid": child.pid,
           "started_unix": started, "ended_unix": ended,
           "started_utc": datetime.datetime.fromtimestamp(started, datetime.timezone.utc).isoformat(),
           "ended_utc": datetime.datetime.fromtimestamp(ended, datetime.timezone.utc).isoformat(),
           "wall_seconds": round(ended - started, 6),
           "stdout": stdout_path.relative_to(package).as_posix(),
           "stdout_sha256": hashlib.sha256(stdout).hexdigest(), "stdout_bytes": len(stdout),
           "stderr": stderr_path.relative_to(package).as_posix(),
           "stderr_sha256": hashlib.sha256(stderr).hexdigest(), "stderr_bytes": len(stderr),
           "timed_out": timed_out, "term_sent": term_sent, "kill_sent": kill_sent,
           "reaped": True, "detached": False}
    (outdir / f"{name}.run.json").write_text(json.dumps(row, indent=2, sort_keys=True) + "\n")
    rows.append(row)
    print(json.dumps({"name": name, "child_pid": child.pid,
                      "returncode": child.returncode, "expected": expected,
                      "wall_seconds": row["wall_seconds"]}, sort_keys=True), flush=True)
    assert row["returncode_matches"], (name, child.returncode, stdout[-2000:], stderr[-2000:])

evidence = (outdir / "evidence_closure.stdout.log").read_text().splitlines()
lines = [line for line in evidence if line.strip()]
prefix = "ERROR: circdist: unlinked evidence: "
package_prefix = "circdist/artifacts/" + package.name + "/"
assert lines and all(line.startswith(prefix) for line in lines)
paths = [line[len(prefix):] for line in lines]
assert len(paths) == len(set(paths)) and all(path.startswith(package_prefix) for path in paths)
interpretation = {"schema": "circdist-gross-round104-evidence-closure-interpretation-v1",
                  "status": "PASS", "raw_exit_code": 1, "error_count": len(paths),
                  "unique_diagnostics": True, "all_errors_under_new_uninstalled_package": True,
                  "package_prefix": package_prefix,
                  "meaning": "expected pre-review unlinked proposer package; canonical evidence was not edited"}
(package / "verification/evidence_closure_interpretation.json").write_text(
    json.dumps(interpretation, indent=2, sort_keys=True) + "\n")
summary = {"schema": "circdist-gross-round104-repository-validator-summary-v1",
           "status": "PASS", "checks": rows, "check_count": len(rows),
           "strict_serial": True, "all_children_reaped": True, "detached_processes": 0,
           "evidence_closure": interpretation,
           "duplicate_key_scan": "PASS", "git_diff_check": "PASS"}
(outdir / "summary.json").write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n")
print(json.dumps({"status": "PASS", "checks": len(rows),
                  "evidence_diagnostics": len(paths)}, sort_keys=True))
