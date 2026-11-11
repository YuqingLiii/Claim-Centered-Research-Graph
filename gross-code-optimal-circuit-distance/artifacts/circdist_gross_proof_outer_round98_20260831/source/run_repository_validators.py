#!/usr/bin/env python3
"""Run the complete Round98 repository gate set and retain exact outputs."""
from pathlib import Path
import argparse
import hashlib
import json
import subprocess
import sys
import time


ap = argparse.ArgumentParser()
ap.add_argument("--repository", type=Path, required=True)
ap.add_argument("--package", type=Path, required=True)
a = ap.parse_args()
R = a.repository.resolve()
P = a.package.resolve()
O = P / "verification/repository_validators"
O.mkdir(parents=True, exist_ok=True)
commands = [
    ("proof_dag_circdist", ["/usr/bin/python3", "tools/proof_dag_check.py", "--problem", "circdist"], 0),
    ("proof_dag_previous_state", ["/usr/bin/python3", "tools/proof_dag_check.py", "--problem", "circdist", "--previous-state", str(P / "bindings/initial_proof_dag")], 0),
    ("circdist_migration", ["/usr/bin/python3", "tools/check_circdist_migration.py"], 0),
    ("release_contracts", ["/usr/bin/python3", "tools/test_release_contracts.py"], 0),
    ("dag_contracts", ["/usr/bin/python3", "tools/test_dag_contracts.py"], 0),
    ("lean_dag_selftest", ["/usr/bin/python3", "tools/lean_dag_check.py", "--selftest"], 0),
    ("duplicate_yaml", ["/usr/bin/python3", str(P / "source/duplicate_yaml_scan.py"), "--root", str(R), "--output", str(O / "duplicate_yaml.result.json")], 0),
    ("git_diff_check", ["git", "diff", "--check"], 0),
    ("evidence_closure", ["/usr/bin/python3", "tools/evidence_closure_check.py", "--problem", "circdist"], 1),
]
rows = []
for name, command, expected in commands:
    started = time.time()
    cp = subprocess.run(command, cwd=R, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=600)
    ended = time.time()
    stdout = O / f"{name}.stdout.log"
    stderr = O / f"{name}.stderr.log"
    stdout.write_bytes(cp.stdout)
    stderr.write_bytes(cp.stderr)
    row = {
        "schema": "circdist-round98-validator-run-v1", "name": name,
        "command": command, "expected_returncode": expected, "returncode": cp.returncode,
        "returncode_matches": cp.returncode == expected, "started_unix": started,
        "ended_unix": ended, "wall_seconds": round(ended - started, 6),
        "stdout": stdout.relative_to(P).as_posix(), "stdout_sha256": hashlib.sha256(cp.stdout).hexdigest(),
        "stdout_bytes": len(cp.stdout), "stderr": stderr.relative_to(P).as_posix(),
        "stderr_sha256": hashlib.sha256(cp.stderr).hexdigest(), "stderr_bytes": len(cp.stderr),
        "reaped": True, "detached": False,
    }
    (O / f"{name}.run.json").write_text(json.dumps(row, indent=2, sort_keys=True) + "\n")
    rows.append(row)

# Evidence checker uses stdout for its diagnostics in this repository.
parser = [sys.executable, str(P / "source/check_evidence_closure_expected.py"),
          "--log", str(O / "evidence_closure.stdout.log"),
          "--output", str(P / "verification/evidence_closure_interpretation.json")]
started = time.time()
cp = subprocess.run(parser, cwd=R, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=60)
ended = time.time()
(O / "evidence_closure_parser.stdout.log").write_bytes(cp.stdout)
(O / "evidence_closure_parser.stderr.log").write_bytes(cp.stderr)
parser_row = {
    "schema": "circdist-round98-validator-run-v1", "name": "evidence_closure_parser",
    "command": parser, "expected_returncode": 0, "returncode": cp.returncode,
    "returncode_matches": cp.returncode == 0, "started_unix": started, "ended_unix": ended,
    "wall_seconds": round(ended - started, 6), "stdout": "verification/repository_validators/evidence_closure_parser.stdout.log",
    "stdout_sha256": hashlib.sha256(cp.stdout).hexdigest(), "stdout_bytes": len(cp.stdout),
    "stderr": "verification/repository_validators/evidence_closure_parser.stderr.log",
    "stderr_sha256": hashlib.sha256(cp.stderr).hexdigest(), "stderr_bytes": len(cp.stderr),
    "reaped": True, "detached": False,
}
(O / "evidence_closure_parser.run.json").write_text(json.dumps(parser_row, indent=2, sort_keys=True) + "\n")
rows.append(parser_row)
status = "PASS" if all(row["returncode_matches"] for row in rows) else "FAIL"
summary = {
    "schema": "circdist-round98-repository-validator-summary-v1", "status": status,
    "checks": rows, "all_children_reaped": True, "detached_processes": 0,
    "evidence_closure_expected_semantics": "exit 1 accepted only because the parser proves every unique diagnostic lies under the sole new unlinked Round98 package",
}
(O / "summary.json").write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n")
print(json.dumps({"status": status, "returncodes": {row["name"]: row["returncode"] for row in rows}}, sort_keys=True))
raise SystemExit(0 if status == "PASS" else 1)
