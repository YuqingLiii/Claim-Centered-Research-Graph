#!/usr/bin/env python3
"""Run post-install repository gates and interpret the sole expected evidence-closure delta."""
from pathlib import Path
import argparse, datetime, hashlib, json, os, signal, subprocess, time

parser = argparse.ArgumentParser()
parser.add_argument("--repository", type=Path, required=True)
parser.add_argument("--package", type=Path, required=True)
parser.add_argument("--output-directory", type=Path, required=True)
args = parser.parse_args()
repository, package, output = args.repository.resolve(), args.package.resolve(), args.output_directory.resolve()
output.mkdir(parents=True, exist_ok=True)
commands = [
    ("proof_dag_circdist", ["/usr/bin/python3", "tools/proof_dag_check.py", "--problem", "circdist"], [0]),
    ("proof_dag_all", ["/usr/bin/python3", "tools/proof_dag_check.py", "--problem", "all"], [0]),
    ("circdist_migration", ["/usr/bin/python3", "tools/check_circdist_migration.py"], [0]),
    ("release_contracts", ["/usr/bin/python3", "tools/test_release_contracts.py"], [0]),
    ("dag_contracts", ["/usr/bin/python3", "tools/test_dag_contracts.py"], [0]),
    ("lean_dag_selftest", ["/usr/bin/python3", "tools/lean_dag_check.py", "--selftest"], [0]),
    ("duplicate_yaml", ["/usr/bin/python3", str(package / "source/duplicate_yaml_scan.py"), "--root", str(repository), "--output", str(output / "duplicate_yaml.result.json")], [0]),
    ("git_diff_check", ["/usr/bin/git", "diff", "--check"], [0]),
    ("evidence_closure_raw", ["/usr/bin/python3", "tools/evidence_closure_check.py", "--problem", "circdist"], [1]),
]
rows = []
environment = {k: os.environ[k] for k in ("PATH", "LANG", "LC_ALL", "LC_CTYPE") if k in os.environ}
environment["PYTHONDONTWRITEBYTECODE"] = "1"
for name, command, expected in commands:
    started = time.time()
    child = subprocess.Popen(command, cwd=repository, env=environment, stdout=subprocess.PIPE, stderr=subprocess.PIPE, start_new_session=False)
    timed_out = terminated = killed = False
    try:
        stdout, stderr = child.communicate(timeout=1800)
    except subprocess.TimeoutExpired:
        timed_out = terminated = True
        child.send_signal(signal.SIGTERM)
        try:
            stdout, stderr = child.communicate(timeout=15)
        except subprocess.TimeoutExpired:
            killed = True
            child.kill()
            stdout, stderr = child.communicate()
    ended = time.time()
    stdout_path, stderr_path = output / f"{name}.stdout.log", output / f"{name}.stderr.log"
    stdout_path.write_bytes(stdout)
    stderr_path.write_bytes(stderr)
    row = {
        "schema": "circdist-gross-round114-postinstall-child-v1",
        "name": name,
        "argv": command,
        "cwd": str(repository),
        "environment": environment,
        "parent_pid": os.getpid(),
        "child_pid": child.pid,
        "returncode": child.returncode,
        "expected_returncodes": expected,
        "returncode_matches": child.returncode in expected and not timed_out,
        "started_utc": datetime.datetime.fromtimestamp(started, datetime.timezone.utc).isoformat(),
        "ended_utc": datetime.datetime.fromtimestamp(ended, datetime.timezone.utc).isoformat(),
        "wall_seconds": round(ended - started, 6),
        "stdout": str(stdout_path),
        "stdout_sha256": hashlib.sha256(stdout).hexdigest(),
        "stdout_bytes": len(stdout),
        "stderr": str(stderr_path),
        "stderr_sha256": hashlib.sha256(stderr).hexdigest(),
        "stderr_bytes": len(stderr),
        "timed_out": timed_out,
        "term_sent": terminated,
        "kill_sent": killed,
        "reaped": True,
        "detached": False,
    }
    (output / f"{name}.run.json").write_text(json.dumps(row, indent=2, sort_keys=True) + "\n")
    rows.append(row)
    print(json.dumps({"name": name, "pid": child.pid, "rc": child.returncode, "seconds": row["wall_seconds"]}, sort_keys=True), flush=True)
    assert row["returncode_matches"], (name, child.returncode, stdout[-2000:], stderr[-2000:])

raw_stdout = (output / "evidence_closure_raw.stdout.log").read_bytes()
raw_stderr = (output / "evidence_closure_raw.stderr.log").read_bytes()
merged = output / "evidence_closure_raw.merged.log"
merged.write_bytes(raw_stdout + raw_stderr)
interpret_command = ["/usr/bin/python3", str(package / "source/check_evidence_closure_round114.py"), "--log", str(merged), "--output", str(output / "evidence_closure_interpretation.json")]
started = time.time()
child = subprocess.Popen(interpret_command, cwd=repository, env=environment, stdout=subprocess.PIPE, stderr=subprocess.PIPE, start_new_session=False)
stdout, stderr = child.communicate(timeout=600)
ended = time.time()
(output / "evidence_closure_interpret.stdout.log").write_bytes(stdout)
(output / "evidence_closure_interpret.stderr.log").write_bytes(stderr)
row = {
    "schema": "circdist-gross-round114-postinstall-child-v1",
    "name": "evidence_closure_interpret",
    "argv": interpret_command,
    "cwd": str(repository),
    "environment": environment,
    "parent_pid": os.getpid(),
    "child_pid": child.pid,
    "returncode": child.returncode,
    "expected_returncodes": [0],
    "returncode_matches": child.returncode == 0,
    "started_utc": datetime.datetime.fromtimestamp(started, datetime.timezone.utc).isoformat(),
    "ended_utc": datetime.datetime.fromtimestamp(ended, datetime.timezone.utc).isoformat(),
    "wall_seconds": round(ended - started, 6),
    "stdout_sha256": hashlib.sha256(stdout).hexdigest(),
    "stdout_bytes": len(stdout),
    "stderr_sha256": hashlib.sha256(stderr).hexdigest(),
    "stderr_bytes": len(stderr),
    "timed_out": False,
    "term_sent": False,
    "kill_sent": False,
    "reaped": True,
    "detached": False,
}
(output / "evidence_closure_interpret.run.json").write_text(json.dumps(row, indent=2, sort_keys=True) + "\n")
rows.append(row)
assert row["returncode_matches"], (child.returncode, stdout[-2000:], stderr[-2000:])
interpretation = json.loads((output / "evidence_closure_interpretation.json").read_text())
assert interpretation["status"] == "PASS" and interpretation["all_errors_under_new_package"]
result = {
    "schema": "circdist-gross-round114-postinstall-gates-v1",
    "status": "PASS",
    "checks": rows,
    "check_count": len(rows),
    "strict_serial": True,
    "all_children_reaped": True,
    "detached_processes": 0,
    "timed_out_processes": 0,
    "standard_zero_exit_gates": 8,
    "evidence_closure_raw_exit": 1,
    "evidence_closure_interpretation": interpretation,
}
(output / "summary.json").write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
print(json.dumps({"status": "PASS", "checks": len(rows), "unlinked_paths": interpretation["error_count"]}, sort_keys=True))
