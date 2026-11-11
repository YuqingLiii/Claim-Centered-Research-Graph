#!/usr/bin/env python3
"""Check a real DRAT, generate/check LRAT, and retain PID-bearing rejection controls."""
from pathlib import Path
import argparse
import hashlib
import json
import os
import subprocess
import time


parser = argparse.ArgumentParser()
parser.add_argument("--formula", type=Path, required=True)
parser.add_argument("--proof", type=Path, required=True)
parser.add_argument("--tooling", type=Path, required=True)
parser.add_argument("--output", type=Path, required=True)
args = parser.parse_args()
args.output.mkdir(parents=True, exist_ok=True)
drat_trim = args.tooling / "drat-trim-arm64-macos"
lrat_check = args.tooling / "lrat-check-arm64-macos"


def file_sha256(path):
    digest = hashlib.sha256()
    with Path(path).open("rb") as source:
        for block in iter(lambda: source.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


processes = []


def run(name, command, expected):
    started = time.time()
    child = subprocess.Popen([str(value) for value in command], stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE, text=True, start_new_session=False)
    timed_out = False
    try:
        stdout, stderr = child.communicate(timeout=1800)
    except subprocess.TimeoutExpired:
        timed_out = True
        child.terminate()
        try:
            stdout, stderr = child.communicate(timeout=15)
        except subprocess.TimeoutExpired:
            child.kill()
            stdout, stderr = child.communicate()
    row = {
        "name": name,
        "command": [str(value) for value in command],
        "parent_pid": os.getpid(),
        "child_pid": child.pid,
        "returncode": child.returncode,
        "expected_returncode": expected,
        "stdout": stdout,
        "stderr": stderr,
        "wall_seconds": round(time.time() - started, 6),
        "timed_out": timed_out,
        "reaped": True,
        "detached": False,
    }
    processes.append(row)
    assert not timed_out and child.returncode == expected, (name, child.returncode, stdout[-2000:], stderr[-2000:])


assert args.formula.is_file() and args.proof.is_file() and args.proof.stat().st_size > 0
lrat = args.output / "accepted.lrat"
run("valid_drat_generate_lrat", [drat_trim, args.formula, args.proof, "-t", "1700", "-L", lrat], 0)
assert lrat.stat().st_size > 0
run("valid_lrat", [lrat_check, args.formula, lrat], 0)
drat_bytes = args.proof.read_bytes()
lrat_bytes = lrat.read_bytes()
truncated_drat = args.output / "truncated.drat"
corrupt_drat = args.output / "corrupt.drat"
truncated_lrat = args.output / "truncated.lrat"
corrupt_lrat = args.output / "corrupt.lrat"
truncated_drat.write_bytes(drat_bytes[:max(1, len(drat_bytes) // 2)])
corrupt_drat.write_bytes(b"not-a-valid-proof\n")
truncated_lrat.write_bytes(lrat_bytes[:max(1, len(lrat_bytes) // 2)])
corrupt_lrat.write_bytes(b"not-a-valid-lrat\n")
run("truncated_drat_rejected", [drat_trim, args.formula, truncated_drat, "-t", "1700"], 1)
run("corrupt_drat_rejected", [drat_trim, args.formula, corrupt_drat, "-t", "1700"], 1)
run("truncated_lrat_rejected", [lrat_check, args.formula, truncated_lrat], 1)
run("corrupt_lrat_rejected", [lrat_check, args.formula, corrupt_lrat], 1)
result = {
    "schema": "circdist-round100-actual-unsat-certificate-v1",
    "status": "PASS",
    "checker_pid": os.getpid(),
    "checker_parent_pid": os.getppid(),
    "formula_sha256": file_sha256(args.formula),
    "drat_sha256": file_sha256(args.proof),
    "lrat_sha256": file_sha256(lrat),
    "drat_bytes": args.proof.stat().st_size,
    "lrat_bytes": lrat.stat().st_size,
    "valid_drat_accepted": True,
    "generated_lrat_accepted": True,
    "corrupt_drat_rejected": True,
    "truncated_drat_rejected": True,
    "corrupt_lrat_rejected": True,
    "truncated_lrat_rejected": True,
    "processes": processes,
    "all_children_reaped": True,
    "detached_processes": 0,
}
(args.output / "certificate.json").write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
print(json.dumps({key: result[key] for key in ("status", "formula_sha256", "drat_sha256", "lrat_sha256")}, sort_keys=True))
