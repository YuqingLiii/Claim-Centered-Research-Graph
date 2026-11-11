#!/usr/bin/env python3
"""Fresh valid/corrupt/truncated DRAT and LRAT controls."""
from pathlib import Path
import argparse, hashlib, json, subprocess, tempfile, time


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


ap = argparse.ArgumentParser()
ap.add_argument("--root", type=Path, required=True)
ap.add_argument("--output", type=Path, required=True)
a = ap.parse_args()
R = a.root.resolve()
C = R / "controls" / "proof_checker"
T = R / "tooling"


def run(name, command, expected):
    started = time.time()
    p = subprocess.run(command, text=True, stdout=subprocess.PIPE,
                       stderr=subprocess.PIPE, timeout=180)
    assert p.returncode == expected, (name, p.returncode, p.stdout, p.stderr)
    return {
        "name": name,
        "command": [str(x) for x in command],
        "returncode": p.returncode,
        "stdout": p.stdout,
        "stderr": p.stderr,
        "wall_seconds": round(time.time() - started, 6),
    }


with tempfile.TemporaryDirectory(prefix="circdist-r88-proof-control.") as td:
    generated = Path(td) / "generated.lrat"
    rows = []
    rows.append(run("valid_drat_generate_lrat", [
        T / "drat-trim-arm64-macos", C / "php6_5.cnf",
        C / "php6_5.fresh.drat", "-t", "170", "-L", generated
    ], 0))
    assert generated.exists() and generated.stat().st_size > 0
    rows.append(run("valid_generated_lrat", [
        T / "lrat-check-arm64-macos", C / "php6_5.cnf", generated
    ], 0))
    rows.append(run("corrupt_drat", [
        T / "drat-trim-arm64-macos", C / "php6_5.cnf",
        C / "php6_5.corrupt.drat", "-t", "170"
    ], 1))
    rows.append(run("truncated_drat", [
        T / "drat-trim-arm64-macos", C / "php6_5.cnf",
        C / "php6_5.truncated.drat", "-t", "170"
    ], 1))
    rows.append(run("corrupt_lrat", [
        T / "lrat-check-arm64-macos", C / "php6_5.cnf",
        C / "php6_5.corrupt.lrat"
    ], 1))
    rows.append(run("truncated_lrat", [
        T / "lrat-check-arm64-macos", C / "php6_5.cnf",
        C / "php6_5.truncated.lrat"
    ], 1))
    generated_sha = sha(generated)

out = {
    "schema": "circdist-round88-proof-controls-v1",
    "status": "PASS",
    "fixture_cnf_sha256": sha(C / "php6_5.cnf"),
    "valid_drat_sha256": sha(C / "php6_5.fresh.drat"),
    "generated_lrat_sha256": generated_sha,
    "valid_drat_accepted": True,
    "generated_lrat_accepted": True,
    "corrupt_drat_rejected": True,
    "truncated_drat_rejected": True,
    "corrupt_lrat_rejected": True,
    "truncated_lrat_rejected": True,
    "scope": "tool-chain controls only; no Gross UNSAT occurred",
    "runs": rows,
}
a.output.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n")
print(json.dumps({k: out[k] for k in out if k != "runs"}, sort_keys=True))
