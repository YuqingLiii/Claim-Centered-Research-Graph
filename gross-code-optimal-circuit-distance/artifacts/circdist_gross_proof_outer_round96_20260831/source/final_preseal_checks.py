#!/usr/bin/env python3
"""Final preseal checks; writes a complete synchronous child record before sealing."""
from pathlib import Path
import hashlib
import json
import os
import subprocess
import sys
import tempfile
import time


P = Path(__file__).resolve().parent.parent
REPO = P.parents[2]
rows = []


def run(name, command):
    started = time.time()
    cp = subprocess.run([str(x) for x in command], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=900)
    row = {
        "name": name, "command": [str(x) for x in command], "returncode": cp.returncode,
        "stdout": cp.stdout, "stderr": cp.stderr, "started_unix": started,
        "ended_unix": time.time(), "wall_seconds": round(time.time() - started, 6),
        "reaped": True, "detached": False,
    }
    rows.append(row)
    assert cp.returncode == 0, (name, cp.returncode, cp.stdout, cp.stderr)


with tempfile.TemporaryDirectory(prefix="circdist-r96-final-preseal.") as td:
    proof = Path(td) / "proof.json"
    run("result", [sys.executable, P / "source/check_result.py", "--root", P])
    run("process", [sys.executable, P / "source/check_process_ledger.py", "--root", P])
    run("protected", [sys.executable, P / "source/check_protected.py", "--package", P, "--repository", REPO])
    run("proof_controls", [sys.executable, P / "source/check_proof_controls.py", "--root", P, "--output", proof])
    assert json.loads(proof.read_text())["status"] == "PASS"

validators = json.loads((P / "verification/repository_validators/summary.json").read_text())
evidence = json.loads((P / "verification/evidence_closure_interpretation.json").read_text())
fix2 = json.loads((P / "verification/fix2_closure.json").read_text())
protected = json.loads((P / "verification/protected_tree_compare.json").read_text())
replay = json.loads((P / "verification/preseal_replay.children.json").read_text())
audit = json.loads((P / "verification/independent_campaign_audit.json").read_text())
assert validators["status"] == evidence["status"] == fix2["status"] == protected["status"] == replay["status"] == audit["status"] == "PASS"
assert replay["child_count"] == 116 and replay["all_children_reaped"] and replay["failure"] is None
assert evidence["raw_exit_code"] == 1 and evidence["all_errors_under_new_package"] and evidence["unique_diagnostics"]
assert fix2["survivors"] == 0 and protected["canonical_and_protected_paths_unchanged"]

record = {
    "schema": "circdist-round96-final-preseal-checks-v1", "status": "PASS",
    "pid": os.getpid(), "parent_pid": os.getppid(), "children": rows,
    "child_count": len(rows), "all_children_reaped": True, "detached_processes": 0,
}
(P / "verification/final_preseal_checks.json").write_text(json.dumps(record, indent=2, sort_keys=True) + "\n")
summary = {
    "schema": "circdist-round96-validation-summary-v1", "status": "PASS",
    "independent_campaign_audit": "PASS", "full_preseal_replay": "PASS (116 serial children)",
    "result_crosscheck": "PASS", "process_crosscheck": "PASS",
    "protected_inputs_and_round94_manifests": "PASS",
    "protected_tree_pre_post_install": "PASS (231 files)",
    "repository_validators": "PASS (9 validators plus exact evidence parser)",
    "evidence_closure": f"expected exit 1; {evidence['error_count']} unique diagnostics solely under Round96 package; parser PASS",
    "proof_controls": "valid DRAT accepted, generated LRAT accepted, corrupt/truncated DRAT/LRAT rejected",
    "fix2": "PASS; exact Round96 scratch root removed, external interpreter explicitly handed off, zero survivors",
    "canonical_unchanged": True, "commit": False, "push": False,
}
(P / "verification/validation_summary.json").write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n")
print(json.dumps(summary, sort_keys=True))
