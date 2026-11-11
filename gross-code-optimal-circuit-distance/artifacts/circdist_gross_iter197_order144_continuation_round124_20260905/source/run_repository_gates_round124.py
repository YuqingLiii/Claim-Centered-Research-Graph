#!/usr/bin/env python3
"""Run repository gates strictly serially with exact nested-child records."""
import argparse
import datetime
import hashlib
import json
import os
import subprocess
import time
from pathlib import Path


def sha(path):
    h = hashlib.sha256()
    with Path(path).open("rb") as f:
        for block in iter(lambda: f.read(8 << 20), b""):
            h.update(block)
    return h.hexdigest()


ap = argparse.ArgumentParser()
ap.add_argument("--repository", type=Path, required=True)
ap.add_argument("--package", type=Path, required=True)
ap.add_argument("--package-relative", required=True)
ap.add_argument("--output", type=Path, required=True)
a = ap.parse_args()
repo, pkg, out = a.repository.resolve(), a.package.resolve(), a.output.resolve()
assert repo.is_dir() and pkg.is_dir() and not out.exists()
out.mkdir(parents=True)
(out / "tmp").mkdir()
env = {"PATH": "/usr/bin:/bin:/usr/sbin:/sbin", "LANG": "C.UTF-8", "LC_ALL": "C.UTF-8",
       "TZ": "UTC", "TMPDIR": str(out / "tmp"), "PYTHONDONTWRITEBYTECODE": "1"}
commands = [
    ("proof_dag_circdist", ["/usr/bin/python3", "tools/proof_dag_check.py", "--problem", "circdist"], [0]),
    ("proof_dag_all", ["/usr/bin/python3", "tools/proof_dag_check.py", "--problem", "all"], [0]),
    ("circdist_migration", ["/usr/bin/python3", "tools/check_circdist_migration.py"], [0]),
    ("release_contracts", ["/usr/bin/python3", "tools/test_release_contracts.py"], [0]),
    ("dag_contracts", ["/usr/bin/python3", "tools/test_dag_contracts.py"], [0]),
    ("lean_dag_selftest", ["/usr/bin/python3", "tools/lean_dag_check.py", "--selftest"], [0]),
    ("duplicate_yaml", ["/usr/bin/python3", str(pkg / "source/round120_reviewed/round118_reviewed/round116_reviewed/parent_duplicate_yaml_scan.py"),
                        "--root", str(repo), "--output", str(out / "duplicate_yaml.json")], [0]),
    ("git_diff_check", ["/usr/bin/git", "diff", "--check"], [0]),
    ("evidence_closure_raw", ["/usr/bin/python3", "tools/evidence_closure_check.py", "--problem", "circdist"], [0, 1]),
]
rows = []


def run(name, argv, expected):
    assert all(row["reaped"] for row in rows)
    start = time.time()
    child = subprocess.Popen(argv, cwd=repo, env=env, stdin=subprocess.DEVNULL,
                             stdout=subprocess.PIPE, stderr=subprocess.PIPE, start_new_session=False)
    stdout, stderr = child.communicate()
    end = time.time()
    stdout_path, stderr_path = out / (name + ".stdout"), out / (name + ".stderr")
    stdout_path.write_bytes(stdout)
    stderr_path.write_bytes(stderr)
    row = {
        "name": name, "argv": argv, "cwd": str(repo), "environment": env,
        "parent_pid": os.getpid(), "child_pid": child.pid,
        "start_utc": datetime.datetime.fromtimestamp(start, datetime.timezone.utc).isoformat(),
        "end_utc": datetime.datetime.fromtimestamp(end, datetime.timezone.utc).isoformat(),
        "duration_ns": int((end - start) * 1e9), "returncode": child.returncode,
        "expected_returncodes": expected, "returncode_matches": child.returncode in expected,
        "stdout": str(stdout_path), "stdout_sha256": sha(stdout_path), "stdout_bytes": len(stdout),
        "stderr": str(stderr_path), "stderr_sha256": sha(stderr_path), "stderr_bytes": len(stderr),
        "reaped": True, "detached": False, "timeout_configured": False, "timeout_triggered": False,
    }
    (out / (name + ".run.json")).write_text(json.dumps(row, indent=2, sort_keys=True) + "\n")
    rows.append(row)
    print(json.dumps({"name": name, "pid": child.pid, "rc": child.returncode,
                      "seconds": round(end - start, 6)}, sort_keys=True), flush=True)
    assert row["returncode_matches"], (name, child.returncode, stdout[-2000:], stderr[-2000:])


for command in commands:
    run(*command)
closure = next(row for row in rows if row["name"] == "evidence_closure_raw")
merged = out / "evidence_closure.merged"
merged.write_bytes((out / "evidence_closure_raw.stdout").read_bytes() +
                   (out / "evidence_closure_raw.stderr").read_bytes())
if closure["returncode"] == 1:
    run("evidence_closure_interpret", ["/usr/bin/python3", str(pkg / "source/check_evidence_closure_round124.py"),
        "--log", str(merged), "--package-relative", a.package_relative,
        "--output", str(out / "evidence_closure_interpretation.json")], [0])
    interpretation = json.loads((out / "evidence_closure_interpretation.json").read_text())
    assert interpretation["status"] == "PASS" and interpretation["all_errors_under_new_package"]
else:
    success_lines = [line for line in merged.read_text().splitlines() if line.strip()]
    assert len(success_lines) == 1
    assert success_lines[0].startswith("circdist: evidence closure OK, ")
    assert success_lines[0].endswith(" structured paths; all evidence project-local and linked")
    interpretation = {
        "schema": "circdist-round124-evidence-closure-interpretation-v1", "status": "PASS",
        "raw_exit_code": 0, "error_count": 0, "all_errors_under_new_package": True,
        "meaning": "repository evidence closure passed directly",
    }
    (out / "evidence_closure_interpretation.json").write_text(json.dumps(interpretation, indent=2, sort_keys=True) + "\n")
summary = {
    "schema": "circdist-gross-round124-repository-gates-v1", "status": "PASS",
    "checks": rows, "check_count": len(rows), "strict_serial": True,
    "all_children_reaped": True, "detached_children": 0, "timeouts_configured": 0,
    "timeouts_triggered": 0, "solver_invocations": 0,
    "evidence_closure_raw_exit": closure["returncode"],
    "evidence_closure_interpretation": interpretation,
}
(out / "summary.json").write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n")
print(json.dumps({"status": "PASS", "checks": len(rows),
                  "unlinked_paths": interpretation["error_count"], "solver_invocations": 0}, sort_keys=True))
