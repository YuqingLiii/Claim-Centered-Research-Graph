#!/usr/bin/env python3
"""Full self-contained replay of the sealed Round94 package."""
from pathlib import Path
import argparse
import gzip
import hashlib
import json
import shutil
import subprocess
import sys
import tempfile
import time
import traceback


def actual(path):
    path = Path(path)
    if path.exists():
        return path, path.suffix == ".gz"
    gz = path.with_name(path.name + ".gz")
    if gz.exists():
        return gz, True
    raise FileNotFoundError(path)


def materialize(path, target):
    source, compressed = actual(path)
    target = Path(target)
    target.parent.mkdir(parents=True, exist_ok=True)
    if compressed:
        with gzip.open(source, "rb") as fi, target.open("wb") as fo:
            shutil.copyfileobj(fi, fo, 1 << 20)
    else:
        shutil.copyfile(source, target)
    return target


def data_bytes(path):
    source, compressed = actual(path)
    return gzip.decompress(source.read_bytes()) if compressed else source.read_bytes()


def compare_data(a, b):
    assert data_bytes(a) == data_bytes(b), (a, b)


def compare_json(a, b, ignored=()):
    x = json.loads(Path(a).read_text())
    y = json.loads(Path(b).read_text())
    for key in ignored:
        x.pop(key, None)
        y.pop(key, None)
    assert x == y, (a, b)


ap = argparse.ArgumentParser()
ap.add_argument("--root", type=Path, required=True)
ap.add_argument("--python", type=Path, default=Path(sys.executable))
ap.add_argument("--repository", type=Path)
ap.add_argument("--record-output", type=Path)
a = ap.parse_args()
R = a.root.resolve()
PY = a.python.absolute()
REPO = a.repository.resolve() if a.repository else R.parents[2]
VENDOR = R / "vendor/round80"
rows = []
started = time.time()
status = "RUNNING"
failure = None


def run(name, command, expected=0):
    t0 = time.time()
    cp = subprocess.run([str(x) for x in command], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=900)
    row = {
        "name": name, "command": [str(x) for x in command], "returncode": cp.returncode,
        "expected_returncode": expected, "stdout": cp.stdout, "stderr": cp.stderr,
        "wall_seconds": round(time.time() - t0, 6), "reaped": True, "detached": False,
    }
    rows.append(row)
    print(json.dumps({k: row[k] for k in ("name", "returncode", "expected_returncode", "wall_seconds")}, sort_keys=True), flush=True)
    assert cp.returncode == expected, (name, cp.returncode, cp.stdout[-4000:], cp.stderr[-4000:])
    return cp


try:
    with tempfile.TemporaryDirectory(prefix="circdist-r94-replay.") as td:
        T = Path(td)
        run("protected_bindings", [PY, R / "source/check_protected.py", "--package", R, "--repository", REPO])

        # Deterministically rebuild and independently check all 13 exact outer encodings.
        for iteration in range(136, 149):
            F = R / "formulas" / f"iter{iteration}"
            D = T / "formulas" / f"iter{iteration}"
            D.mkdir(parents=True)
            stored_cnf = materialize(F / "outer.cnf", D / "stored.cnf")
            stored_map = materialize(F / "assertion_map.jsonl", D / "stored.map")
            run(f"compile_iter{iteration}", [
                PY, R / "source/compile_outer_cnf.py", "--source", F / "source.json.gz",
                "--cnf", D / "fresh.cnf", "--metadata", D / "fresh.metadata.json",
                "--assertion-map", D / "fresh.map", "--definitions", D / "fresh.trace.json.gz",
            ])
            assert (D / "fresh.cnf").read_bytes() == stored_cnf.read_bytes()
            assert (D / "fresh.map").read_bytes() == stored_map.read_bytes()
            assert (D / "fresh.trace.json.gz").read_bytes() == (F / "circuit_trace.json.gz").read_bytes()
            compare_json(F / "metadata.json", D / "fresh.metadata.json", ("compile_seconds",))
            run(f"encoding_iter{iteration}", [
                PY, R / "source/check_outer_encoding.py", "--source", F / "source.json.gz",
                "--cnf", D / "fresh.cnf", "--metadata", D / "fresh.metadata.json",
                "--assertion-map", D / "fresh.map", "--definitions", D / "fresh.trace.json.gz",
                "--output", D / "fresh.encoding.json",
            ])
            compare_json(F / "encoding_check.json", D / "fresh.encoding.json", ("seconds",))
            print(f"FORMULA_REPLAY_PASS {iteration}", flush=True)

        state_path = R / "state/iter136_state.json"
        for iteration in range(136, 148):
            F = R / "formulas" / f"iter{iteration}"
            I = R / "iterations" / f"iter{iteration}"
            D = T / "formulas" / f"iter{iteration}"
            W = T / "iterations" / f"iter{iteration}"
            W.mkdir(parents=True)
            solver_log = materialize(I / "outer/solver.log", W / "outer.solver.log")
            run(f"outer_replay_iter{iteration}", [
                PY, R / "source/verify_outer_sat_model.py", "--solver-log", solver_log,
                "--cnf", D / "fresh.cnf", "--source", F / "source.json.gz",
                "--metadata", F / "metadata.json", "--frozen", VENDOR,
                "--assignment", W / "outer.assignment", "--candidate", W / "candidate.json",
                "--output", W / "outer.replay.json",
            ])
            compare_data(W / "outer.assignment", I / "outer/assignment.dimacs")
            compare_data(W / "candidate.json", I / "outer/candidate.json")
            compare_json(I / "outer/replay.json", W / "outer.replay.json", ("seconds",))
            run(f"outer_assignment_iter{iteration}", [
                PY, R / "source/extract_and_check_assignment.py", "--cnf", D / "fresh.cnf",
                "--solver-log", solver_log, "--assignment", W / "outer.independent.assignment",
                "--output", W / "outer.independent.check.json",
            ])
            compare_data(W / "outer.independent.assignment", I / "outer/assignment.independent.dimacs")
            compare_data(W / "outer.independent.check.json", I / "outer/assignment_independent_check.json")

            state = json.loads(Path(state_path).read_text())
            direct = W / "direct"
            run(f"direct_build_iter{iteration}", [
                PY, R / "source/build_direct_from_candidate.py", "--candidate", W / "candidate.json",
                "--output", direct, "--vendor", VENDOR,
                "--source-selector-count", state["selector_count"],
            ])
            compare_data(direct / "candidate.json", I / "direct/candidate.json")
            compare_data(direct / "build_summary.json", I / "direct/build_summary.json")
            for sector in ("Xerr", "Zerr"):
                for suffix in ("cnf", "variables.json", "columns.json", "clauses.jsonl", "summary.json"):
                    compare_data(direct / "direct360" / f"{sector}.{suffix}", I / "direct/direct360" / f"{sector}.{suffix}")
                stored_solver = materialize(I / "direct/solver" / f"{sector}.solver.log", direct / "solver" / f"{sector}.solver.log")
                run(f"direct_assignment_iter{iteration}_{sector}", [
                    PY, R / "source/extract_and_check_assignment.py",
                    "--cnf", direct / "direct360" / f"{sector}.cnf", "--solver-log", stored_solver,
                    "--assignment", direct / "solver" / f"{sector}.assignment.dimacs",
                    "--output", direct / "solver" / f"{sector}.assignment_check.json",
                ])
                compare_data(direct / "solver" / f"{sector}.assignment.dimacs", I / "direct/solver" / f"{sector}.assignment.dimacs")
                compare_data(direct / "solver" / f"{sector}.assignment_check.json", I / "direct/solver" / f"{sector}.assignment_check.json")
            run(f"direct_replay_iter{iteration}", [
                PY, VENDOR / "src/replay_direct_candidate.py", "--root", direct,
                "--output", W / "direct_verification.json",
            ])
            compare_data(W / "direct_verification.json", I / "direct/direct_verification.json")

            X = W / "transition"
            run(f"transition_iter{iteration}", [
                PY, R / "source/advance_round94.py", "--vendor", VENDOR,
                "--state-in", state_path, "--source-in", F / "source.json.gz",
                "--iteration", iteration, "--candidate", W / "candidate.json",
                "--direct", W / "direct_verification.json", "--state-out", X / "state.json",
                "--record-out", X / "record.json", "--source-out", X / "source.json.gz",
            ])
            compare_data(X / "state.json", R / "state" / f"iter{iteration + 1}_state.json")
            compare_data(X / "record.json", I / "record.json")
            compare_data(X / "source.json.gz", R / "formulas" / f"iter{iteration + 1}/source.json.gz")
            state_path = X / "state.json"
            print(f"CANDIDATE_REPLAY_PASS {iteration}", flush=True)

        compare_data(state_path, R / "state/iter148_state.json")

        run("triple_synthesis", [
            PY, R / "source/triple_gf2_closure.py", "--state", R / "state/iter137_state.json",
            "--candidate", R / "iterations/iter136/outer/candidate.json", "--vendor", VENDOR,
            "--output", T / "triple.json",
        ])
        compare_json(R / "synthesis/triple_gf2_closure.json", T / "triple.json", ("seconds",))
        run("relaxation_controls", [
            PY, R / "source/closure_relaxation_controls.py", "--state", R / "state/iter136_state.json",
            "--candidate", R / "iterations/iter136/outer/candidate.json",
            "--direct", R / "iterations/iter136/direct/direct_verification.json",
            "--vendor", VENDOR, "--output", T / "relaxation.json",
        ])
        compare_data(T / "relaxation.json", R / "synthesis/relaxation_controls.json")

        run("independent_campaign_audit", [
            PY, R / "source/audit_round94.py", "--root", R, "--logs", R / "logs",
            "--vendor", VENDOR, "--output", T / "audit.json",
        ])
        assert json.loads((T / "audit.json").read_text())["status"] == "PASS"
        run("result_crosscheck", [PY, R / "source/check_result.py", "--root", R])
        run("process_crosscheck", [PY, R / "source/check_process_ledger.py", "--root", R])
        run("proof_controls", [
            PY, R / "source/check_proof_controls.py", "--root", R,
            "--output", T / "proof_controls.json",
        ])
        stable = [
            "status", "fixture_cnf_sha256", "valid_drat_sha256", "generated_lrat_sha256",
            "valid_drat_accepted", "generated_lrat_accepted", "corrupt_drat_rejected",
            "truncated_drat_rejected", "corrupt_lrat_rejected", "truncated_lrat_rejected", "scope",
        ]
        x = json.loads((T / "proof_controls.json").read_text())
        y = json.loads((R / "controls/proof_fixture_controls.json").read_text())
        assert all(x[k] == y[k] for k in stable)
        status = "PASS"
except BaseException as exc:
    status = "FAIL"
    failure = {"type": type(exc).__name__, "message": str(exc), "traceback": traceback.format_exc()}
    raise
finally:
    record = {
        "schema": "circdist-round94-full-replay-processes-v1", "status": status,
        "started_unix": started, "ended_unix": time.time(),
        "wall_seconds": round(time.time() - started, 6), "children": rows,
        "child_count": len(rows), "all_children_reaped": True,
        "detached_processes": 0, "failure": failure,
    }
    if a.record_output:
        a.record_output.parent.mkdir(parents=True, exist_ok=True)
        a.record_output.write_text(json.dumps(record, indent=2, sort_keys=True) + "\n")

print("ROUND94_PACKAGE_REPLAY_PASS", len(rows))
