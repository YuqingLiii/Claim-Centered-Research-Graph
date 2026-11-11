#!/usr/bin/env python3
"""Run the Round102 read-only repository gate set strictly serially."""
from pathlib import Path
import argparse
import datetime
import hashlib
import json
import os
import subprocess
import sys
import time


parser = argparse.ArgumentParser()
parser.add_argument("--repository", type=Path, required=True)
parser.add_argument("--package", type=Path, required=True)
args = parser.parse_args()
repository = args.repository.resolve()
package = args.package.resolve()
output = package / "verification" / "repository_validators"
output.mkdir(parents=True, exist_ok=True)

commands = [
    ("live_governance", [sys.executable, package / "source/check_live_governance_round102.py",
                         "--repository", repository, "--package", package,
                         "--output", package / "verification/live_governance_check.json"], 0),
    ("proof_dag_circdist", ["/usr/bin/python3", "tools/proof_dag_check.py", "--problem", "circdist"], 0),
    ("proof_dag_all", ["/usr/bin/python3", "tools/proof_dag_check.py", "--problem", "all"], 0),
    ("circdist_migration", ["/usr/bin/python3", "tools/check_circdist_migration.py"], 0),
    ("release_contracts", ["/usr/bin/python3", "tools/test_release_contracts.py"], 0),
    ("dag_contracts", ["/usr/bin/python3", "tools/test_dag_contracts.py"], 0),
    ("lean_dag_selftest", ["/usr/bin/python3", "tools/lean_dag_check.py", "--selftest"], 0),
    ("duplicate_yaml", ["/usr/bin/python3", package / "source/duplicate_yaml_scan.py",
                        "--root", repository,
                        "--output", output / "duplicate_yaml.result.json"], 0),
    ("git_diff_check", ["/usr/bin/git", "diff", "--check"], 0),
    ("evidence_closure", ["/usr/bin/python3", "tools/evidence_closure_check.py",
                          "--problem", "circdist"], 1),
]

rows = []
for name, command, expected in commands:
    command = [str(value) for value in command]
    started = time.time()
    started_utc = datetime.datetime.now(datetime.timezone.utc).isoformat()
    child = subprocess.Popen(command, cwd=repository, stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE, start_new_session=False)
    timed_out = term_sent = kill_sent = False
    try:
        stdout, stderr = child.communicate(timeout=1200)
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
    ended_utc = datetime.datetime.now(datetime.timezone.utc).isoformat()
    stdout_path = output / f"{name}.stdout.log"
    stderr_path = output / f"{name}.stderr.log"
    stdout_path.write_bytes(stdout)
    stderr_path.write_bytes(stderr)
    row = {
        "schema": "circdist-gross-round102-validator-run-v1",
        "name": name,
        "command": command,
        "expected_returncode": expected,
        "returncode": child.returncode,
        "returncode_matches": not timed_out and child.returncode == expected,
        "parent_pid": os.getpid(),
        "child_pid": child.pid,
        "started_unix": started,
        "ended_unix": ended,
        "started_utc": started_utc,
        "ended_utc": ended_utc,
        "wall_seconds": round(ended - started, 6),
        "stdout": stdout_path.relative_to(package).as_posix(),
        "stdout_sha256": hashlib.sha256(stdout).hexdigest(),
        "stdout_bytes": len(stdout),
        "stderr": stderr_path.relative_to(package).as_posix(),
        "stderr_sha256": hashlib.sha256(stderr).hexdigest(),
        "stderr_bytes": len(stderr),
        "timed_out": timed_out,
        "term_sent": term_sent,
        "kill_sent": kill_sent,
        "reaped": True,
        "detached": False,
    }
    (output / f"{name}.run.json").write_text(
        json.dumps(row, indent=2, sort_keys=True) + "\n")
    rows.append(row)
    print(json.dumps({"name": name, "child_pid": child.pid,
                      "returncode": child.returncode, "expected": expected,
                      "seconds": row["wall_seconds"]}, sort_keys=True), flush=True)
    assert row["returncode_matches"], (name, child.returncode,
                                        stdout[-2000:], stderr[-2000:])

# The parser is itself separately PID/interval recorded here.
name = "evidence_closure_parser"
command = [sys.executable, str(package / "source/check_evidence_closure_round102.py"),
           "--log", str(output / "evidence_closure.stdout.log"),
           "--output", str(package / "verification/evidence_closure_interpretation.json")]
started = time.time()
started_utc = datetime.datetime.now(datetime.timezone.utc).isoformat()
child = subprocess.Popen(command, cwd=repository, stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE, start_new_session=False)
stdout, stderr = child.communicate(timeout=300)
ended = time.time()
ended_utc = datetime.datetime.now(datetime.timezone.utc).isoformat()
stdout_path = output / f"{name}.stdout.log"
stderr_path = output / f"{name}.stderr.log"
stdout_path.write_bytes(stdout)
stderr_path.write_bytes(stderr)
row = {
    "schema": "circdist-gross-round102-validator-run-v1",
    "name": name, "command": command, "expected_returncode": 0,
    "returncode": child.returncode, "returncode_matches": child.returncode == 0,
    "parent_pid": os.getpid(), "child_pid": child.pid,
    "started_unix": started, "ended_unix": ended,
    "started_utc": started_utc, "ended_utc": ended_utc,
    "wall_seconds": round(ended - started, 6),
    "stdout": stdout_path.relative_to(package).as_posix(),
    "stdout_sha256": hashlib.sha256(stdout).hexdigest(), "stdout_bytes": len(stdout),
    "stderr": stderr_path.relative_to(package).as_posix(),
    "stderr_sha256": hashlib.sha256(stderr).hexdigest(), "stderr_bytes": len(stderr),
    "timed_out": False, "term_sent": False, "kill_sent": False,
    "reaped": True, "detached": False,
}
(output / f"{name}.run.json").write_text(json.dumps(row, indent=2, sort_keys=True) + "\n")
rows.append(row)
print(json.dumps({"name": name, "child_pid": child.pid,
                  "returncode": child.returncode, "expected": 0,
                  "seconds": row["wall_seconds"]}, sort_keys=True), flush=True)
assert child.returncode == 0, (stdout[-2000:], stderr[-2000:])

summary = {
    "schema": "circdist-gross-round102-repository-validator-summary-v1",
    "status": "PASS",
    "checks": rows,
    "check_count": len(rows),
    "strict_serial": True,
    "all_children_reaped": all(row["reaped"] for row in rows),
    "detached_processes": 0,
    "evidence_closure_expected_semantics": "exit 1 accepted only because every unique diagnostic lies under the sole new unlinked Round102 package",
}
(output / "summary.json").write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n")
print(json.dumps({"status": "PASS", "checks": len(rows),
                  "returncodes": {row["name"]: row["returncode"] for row in rows}},
                 sort_keys=True))
