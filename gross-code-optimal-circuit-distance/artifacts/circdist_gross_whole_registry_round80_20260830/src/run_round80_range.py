#!/usr/bin/env python3
"""Strict-serial range driver; stops on any non-PASS iteration or closure."""
from pathlib import Path
import argparse
import json
import subprocess
import sys


ap = argparse.ArgumentParser()
ap.add_argument("--start", type=int, required=True)
ap.add_argument("--end", type=int, required=True)
ap.add_argument("--root", type=Path, required=True)
ap.add_argument("--python", type=Path, required=True)
a = ap.parse_args()
root = a.root.resolve()
for iteration in range(a.start, a.end + 1):
    cmd = [
        str(a.python), str(root / "src/run_supervised.py"),
        "--timeout-seconds", "7200",
        "--log", str(root / f"cegar/iter{iteration}.driver.log"),
        "--record", str(root / f"cegar/iter{iteration}.driver.run.json"),
        "--", str(a.python), str(root / "src/run_round78_iteration.py"),
        "--iteration", str(iteration), "--engine-root", str(root),
        "--work-root", str(root), "--python", str(a.python),
    ]
    cp = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    print(cp.stdout.strip(), flush=True)
    if cp.returncode:
        raise SystemExit(cp.returncode)
    outcome = json.loads((root / f"cegar/iter{iteration}/iteration_outcome.json").read_text())
    compact = {k: outcome.get(k) for k in (
        "iteration", "outer_status", "sector_statuses", "online_generalized_retained_increment",
        "cross_registry_retained_increment", "generalized_terms_after", "dynamic_blocks_after",
        "mechanism_registry_after", "raw_mechanisms_after", "installed_blocks_after",
        "accepted_absence_proofs", "repair_entered", "branch_closed",
    )}
    print(json.dumps({"stage": "iteration_complete", **compact}, sort_keys=True), flush=True)
    if outcome.get("branch_closed"):
        break
