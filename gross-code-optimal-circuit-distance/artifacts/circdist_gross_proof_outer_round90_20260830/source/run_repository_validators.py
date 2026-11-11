#!/usr/bin/env python3
"""Run and durably record the repository validators required at Round90 seal."""
from pathlib import Path
import argparse
import hashlib
import json
import subprocess
import time

parser = argparse.ArgumentParser()
parser.add_argument("--repository", type=Path, required=True)
parser.add_argument("--package", type=Path, required=True)
args = parser.parse_args()
repo = args.repository.resolve()
package = args.package.resolve()
output = package / "verification/repository_validators"
output.mkdir(parents=True, exist_ok=True)
commands = [
    ("proof_dag_circdist", ["/usr/bin/python3", "tools/proof_dag_check.py", "--problem", "circdist"], 0),
    ("proof_dag_previous_state", ["/usr/bin/python3", "tools/proof_dag_check.py", "--problem", "circdist", "--previous-state", str(package / "bindings/initial_proof_dag")], 0),
    ("circdist_migration", ["/usr/bin/python3", "tools/check_circdist_migration.py"], 0),
    ("release_contracts", ["/usr/bin/python3", "tools/test_release_contracts.py"], 0),
    ("dag_contracts", ["/usr/bin/python3", "tools/test_dag_contracts.py"], 0),
    ("lean_dag_selftest", ["/usr/bin/python3", "tools/lean_dag_check.py", "--selftest"], 0),
    ("duplicate_yaml", ["/usr/bin/python3", str(package / "source/duplicate_yaml_scan.py"), "--root", str(repo), "--output", str(output / "duplicate_yaml.result.json")], 0),
    ("git_diff_check", ["git", "diff", "--check"], 0),
    ("evidence_closure", ["/usr/bin/python3", "tools/evidence_closure_check.py", "--problem", "circdist"], 1),
]
rows = []
for name, command, expected in commands:
    started = time.time()
    proc = subprocess.run(command, cwd=repo, stdout=subprocess.PIPE,
                          stderr=subprocess.PIPE, timeout=600)
    ended = time.time()
    stdout_path = output / f"{name}.stdout.log"
    stderr_path = output / f"{name}.stderr.log"
    stdout_path.write_bytes(proc.stdout)
    stderr_path.write_bytes(proc.stderr)
    row = {
        "schema": "circdist-round90-validator-run-v1",
        "name": name,
        "command": command,
        "expected_returncode": expected,
        "returncode": proc.returncode,
        "returncode_matches": proc.returncode == expected,
        "started_unix": started,
        "ended_unix": ended,
        "wall_seconds": round(ended - started, 6),
        "stdout": stdout_path.relative_to(package).as_posix(),
        "stdout_sha256": hashlib.sha256(proc.stdout).hexdigest(),
        "stdout_bytes": len(proc.stdout),
        "stderr": stderr_path.relative_to(package).as_posix(),
        "stderr_sha256": hashlib.sha256(proc.stderr).hexdigest(),
        "stderr_bytes": len(proc.stderr),
    }
    (output / f"{name}.run.json").write_text(json.dumps(row, indent=2, sort_keys=True) + "\n")
    rows.append(row)
summary = {
    "schema": "circdist-round90-repository-validator-summary-v1",
    "status": "PASS" if all(row["returncode_matches"] for row in rows) else "FAIL",
    "checks": rows,
    "evidence_closure_expected_semantics": "exit 1 is accepted only after separate output parsing confirms that every reported unlinked path lies under the one new Round90 package",
}
(output / "summary.json").write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n")
print(json.dumps({"status": summary["status"], "returncodes": {row["name"]: row["returncode"] for row in rows}}, sort_keys=True))
raise SystemExit(0 if summary["status"] == "PASS" else 1)
