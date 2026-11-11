#!/usr/bin/env python3
"""Run the pre-install Round110 repository gates strictly serially."""
from pathlib import Path
import argparse, datetime, hashlib, json, os, subprocess, sys, time

ap = argparse.ArgumentParser(); ap.add_argument("--repository", type=Path, required=True)
ap.add_argument("--package", type=Path, required=True); args = ap.parse_args()
repo, package = args.repository.resolve(), args.package.resolve()
outdir = package / "verification/repository_validators"; outdir.mkdir(parents=True, exist_ok=True)
commands = [
    ("live_governance", [sys.executable, package / "source/check_live_governance_round110.py", "--repository", repo,
                         "--package", package, "--output", package / "verification/live_governance_check.json"]),
    ("proof_dag_circdist", ["/usr/bin/python3", "tools/proof_dag_check.py", "--problem", "circdist"]),
    ("proof_dag_all", ["/usr/bin/python3", "tools/proof_dag_check.py", "--problem", "all"]),
    ("circdist_migration", ["/usr/bin/python3", "tools/check_circdist_migration.py"]),
    ("release_contracts", ["/usr/bin/python3", "tools/test_release_contracts.py"]),
    ("dag_contracts", ["/usr/bin/python3", "tools/test_dag_contracts.py"]),
    ("lean_dag_selftest", ["/usr/bin/python3", "tools/lean_dag_check.py", "--selftest"]),
    ("duplicate_yaml", ["/usr/bin/python3", package / "source/duplicate_yaml_scan.py", "--root", repo,
                        "--output", outdir / "duplicate_yaml.result.json"]),
    ("git_diff_check", ["/usr/bin/git", "diff", "--check"]),
]
rows = []
for name, command in commands:
    command = [str(x) for x in command]; started = time.time()
    child = subprocess.Popen(command, cwd=repo, stdout=subprocess.PIPE, stderr=subprocess.PIPE, start_new_session=False)
    timed_out = term_sent = kill_sent = False
    try: stdout, stderr = child.communicate(timeout=1800)
    except subprocess.TimeoutExpired:
        timed_out = term_sent = True; child.terminate()
        try: stdout, stderr = child.communicate(timeout=15)
        except subprocess.TimeoutExpired:
            kill_sent = True; child.kill(); stdout, stderr = child.communicate()
    ended = time.time(); stdout_path, stderr_path = outdir/f"{name}.stdout.log", outdir/f"{name}.stderr.log"
    stdout_path.write_bytes(stdout); stderr_path.write_bytes(stderr)
    row = {"schema": "circdist-gross-round110-validator-child-v1", "name": name, "argv": command,
           "cwd": str(repo), "environment": {k: os.environ[k] for k in ("PATH","LANG","LC_ALL","PYTHONPATH") if k in os.environ},
           "expected_returncode": 0, "returncode": child.returncode,
           "returncode_matches": not timed_out and child.returncode == 0,
           "parent_pid": os.getpid(), "child_pid": child.pid, "started_unix": started, "ended_unix": ended,
           "started_utc": datetime.datetime.fromtimestamp(started, datetime.timezone.utc).isoformat(),
           "ended_utc": datetime.datetime.fromtimestamp(ended, datetime.timezone.utc).isoformat(),
           "wall_seconds": round(ended-started,6), "stdout": stdout_path.relative_to(package).as_posix(),
           "stdout_sha256": hashlib.sha256(stdout).hexdigest(), "stdout_bytes": len(stdout),
           "stderr": stderr_path.relative_to(package).as_posix(), "stderr_sha256": hashlib.sha256(stderr).hexdigest(),
           "stderr_bytes": len(stderr), "timed_out": timed_out, "term_sent": term_sent, "kill_sent": kill_sent,
           "reaped": True, "detached": False}
    (outdir/f"{name}.run.json").write_text(json.dumps(row,indent=2,sort_keys=True)+"\n"); rows.append(row)
    print(json.dumps({"name":name,"child_pid":child.pid,"returncode":child.returncode,"wall_seconds":row["wall_seconds"]},sort_keys=True),flush=True)
    assert row["returncode_matches"], (name,child.returncode,stdout[-2000:],stderr[-2000:])
summary = {"schema":"circdist-gross-round110-preinstall-repository-validator-summary-v1","status":"PASS",
           "checks":rows,"check_count":len(rows),"strict_serial":True,"all_children_reaped":True,
           "detached_processes":0,"duplicate_key_scan":"PASS","git_diff_check":"PASS",
           "evidence_closure":"DEFERRED_UNTIL_ATOMIC_INSTALL_BECAUSE_CHECKER_ENUMERATES_REPOSITORY_ARTIFACT_PATHS"}
(outdir/"summary.json").write_text(json.dumps(summary,indent=2,sort_keys=True)+"\n")
print(json.dumps({"status":"PASS","checks":len(rows),"evidence_closure":"post-install"},sort_keys=True))
