#!/usr/bin/env python3
"""Strictly serial, solver-free, read-only replay of the sealed Round118 package."""
from __future__ import annotations

import argparse
import datetime
import hashlib
import json
import os
import subprocess
import time
from pathlib import Path


def sha(path):
    digest = hashlib.sha256()
    with Path(path).open("rb") as handle:
        for block in iter(lambda: handle.read(8 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def strip_runtime(value):
    ignored = {"seconds", "wall_seconds", "compile_seconds"}
    if isinstance(value, dict):
        return {k: strip_runtime(v) for k, v in value.items() if k not in ignored}
    if isinstance(value, list):
        return [strip_runtime(v) for v in value]
    return value


ap = argparse.ArgumentParser()
ap.add_argument("--root", type=Path, required=True)
ap.add_argument("--output", type=Path, required=True)
ap.add_argument("--skip-seal-check", action="store_true")
ap.add_argument("--skip-sat-streams", action="store_true")
a = ap.parse_args()
R = a.root.resolve()
O = a.output.resolve()
assert R.is_dir() and not O.exists()
O.mkdir(parents=True)
(O / "tmp").mkdir()
(O / "generated").mkdir()

py = "/usr/bin/python3"
S = R / "source"
U = S / "round116_reviewed"
I = R / "input/iter194"
E = R / "output/iter194"
F = R / "frontier/iter195"
G = O / "generated"
env = {
    "PATH": "/usr/bin:/bin:/usr/sbin:/sbin",
    "LANG": "C.UTF-8",
    "LC_ALL": "C.UTF-8",
    "TZ": "UTC",
    "TMPDIR": str(O / "tmp"),
    "PYTHONDONTWRITEBYTECODE": "1",
    "PYTHONPATH": str(S) + ":" + str(U) + ":" + str(R / "python/site-packages"),
}
runs = []
comparisons = []


def run(name, argv, cwd=None):
    assert not any(not row["reaped"] for row in runs)
    argv = [str(value) for value in argv]
    forbidden = {"cadical", "cadical-1.9.5-arm64-macos", "kissat", "minisat", "glucose"}
    assert Path(argv[0]).name.lower() not in forbidden, (name, argv)
    start = time.time()
    child = subprocess.Popen(argv, cwd=str((cwd or R).resolve()), env=env,
                             stdin=subprocess.DEVNULL, stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE, start_new_session=False)
    stdout, stderr = child.communicate()
    end = time.time()
    stdout_path = O / (name + ".stdout")
    stderr_path = O / (name + ".stderr")
    stdout_path.write_bytes(stdout)
    stderr_path.write_bytes(stderr)
    row = {
        "name": name,
        "argv": argv,
        "cwd": str((cwd or R).resolve()),
        "environment": env,
        "parent_pid": os.getpid(),
        "child_pid": child.pid,
        "start_utc": datetime.datetime.fromtimestamp(start, datetime.timezone.utc).isoformat(),
        "end_utc": datetime.datetime.fromtimestamp(end, datetime.timezone.utc).isoformat(),
        "duration_ns": int((end - start) * 1e9),
        "returncode": child.returncode,
        "stdout": str(stdout_path),
        "stdout_sha256": sha(stdout_path),
        "stdout_bytes": len(stdout),
        "stderr": str(stderr_path),
        "stderr_sha256": sha(stderr_path),
        "stderr_bytes": len(stderr),
        "reaped": True,
        "detached": False,
        "timeout_configured": False,
        "timeout_triggered": False,
    }
    (O / (name + ".run.json")).write_text(json.dumps(row, indent=2, sort_keys=True) + "\n")
    runs.append(row)
    print(json.dumps({"name": name, "pid": child.pid, "rc": child.returncode,
                      "seconds": round(end - start, 6)}, sort_keys=True), flush=True)
    assert child.returncode == 0, (name, child.returncode, stdout[-2000:], stderr[-2000:])


def exact(name, left, right):
    left, right = Path(left), Path(right)
    assert sha(left) == sha(right), (name, sha(left), sha(right))
    comparisons.append({"name": name, "kind": "byte_exact", "left": str(left),
                        "right": str(right), "sha256": sha(left)})


def semantic(name, left, right):
    left, right = Path(left), Path(right)
    assert strip_runtime(json.loads(left.read_text())) == strip_runtime(json.loads(right.read_text())), name
    comparisons.append({"name": name, "kind": "JSON_equal_after_removing_runtime_fields",
                        "left": str(left), "right": str(right)})


if not a.skip_seal_check:
    run("sealed_package", [py, S / "check_sealed_package_round118.py", "--root", R,
                           "--output", O / "sealed_package.json"])
run("result", [py, S / "check_result_round118.py", "--root", R, "--output", O / "result.json"])
run("process_ledger", [py, S / "check_session_process_ledger_round118.py",
                       "--ledger", R / "logs/process/session_process.jsonl",
                       "--output", O / "process_ledger.json"])

# Re-extract and check the complete outer assignment against every quotient clause.
run("outer_assignment", [py, U / "parent_extract_and_check_assignment.py",
    "--cnf", I / "order144_quotient/outer.cnf", "--solver-log", E / "solver/solver.log",
    "--assignment", O / "outer.assignment.dimacs", "--output", O / "outer.assignment_check.json"])
exact("outer assignment", O / "outer.assignment.dimacs", E / "solver/assignment.dimacs")
exact("outer assignment check", O / "outer.assignment_check.json", E / "solver/assignment_check.json")

# Decode and physically replay the complete frozen schedule.
run("outer_semantics", [py, U / "parent_verify_outer_sat_model.py",
    "--solver-log", E / "solver/solver.log", "--cnf", I / "order144_quotient/outer.cnf",
    "--source", I / "source.json.gz", "--metadata", I / "order144_quotient/metadata.json",
    "--frozen", R / "vendor/round80", "--assignment", O / "outer.replay.assignment.dimacs",
    "--candidate", O / "outer.candidate.json", "--output", O / "outer.replay.json"])
exact("outer replay assignment", O / "outer.replay.assignment.dimacs", E / "solver/assignment.replay.dimacs")
exact("outer candidate", O / "outer.candidate.json", E / "solver/candidate.json")
semantic("outer semantic replay", O / "outer.replay.json", E / "solver/replay.json")

run("outer_orbit_controls", [py, S / "check_sat_order144_orbit_controls_round118.py",
    "--cnf", I / "order144_quotient/outer.cnf", "--metadata", I / "order144_quotient/metadata.json",
    "--source", I / "source.json.gz", "--assignment", E / "solver/assignment.dimacs",
    "--candidate", E / "solver/candidate.json", "--trace", I / "order144_quotient/trace.json.gz",
    "--output", O / "outer.orbit_controls.json"])
exact("outer orbit controls", O / "outer.orbit_controls.json", E / "solver/orbit_controls.json")

# Rebuild both complete unrestricted formulas outside the package.
run("direct_build", [py, U / "build_direct_from_candidate_round116.py",
    "--candidate", E / "solver/candidate.json", "--output", G / "direct", "--vendor", R / "vendor/round80",
    "--source-selector-count", "50832", "--source-block-count", "814392"])
for relative in (
    "build_summary.json", "candidate.json", "direct360/Xerr.cnf", "direct360/Xerr.columns.json",
    "direct360/Xerr.variables.json", "direct360/Xerr.clauses.jsonl", "direct360/Xerr.summary.json",
    "direct360/Zerr.cnf", "direct360/Zerr.columns.json", "direct360/Zerr.variables.json",
    "direct360/Zerr.clauses.jsonl", "direct360/Zerr.summary.json",
):
    exact("direct build " + relative, G / "direct" / relative, E / "direct" / relative)

for label in ("Xerr", "Zerr"):
    run(label + "_assignment", [py, U / "parent_extract_and_check_assignment.py",
        "--cnf", E / f"direct/direct360/{label}.cnf",
        "--solver-log", E / f"direct/solver/{label}.solver.log",
        "--assignment", O / f"{label}.assignment.dimacs",
        "--output", O / f"{label}.assignment_check.json"])
    exact(label + " assignment", O / f"{label}.assignment.dimacs", E / f"direct/solver/{label}.assignment.dimacs")
    exact(label + " assignment check", O / f"{label}.assignment_check.json", E / f"direct/solver/{label}.assignment_check.json")

run("direct_vendor_replay", [py, R / "vendor/round80/src/replay_direct_candidate.py",
    "--root", E / "direct", "--output", O / "direct.vendor.json"])
exact("vendor direct replay", O / "direct.vendor.json", E / "direct/direct_verification.json")
run("direct_independent", [py, S / "independent_iter194_direct_audit_round118.py",
    "--root", R, "--output", O / "direct.independent.json"])
exact("independent direct replay", O / "direct.independent.json", E / "direct/independent_audit.json")

run("Xerr_orbit", [py, U / "audit_selector_translation_orbit_round116.py", "--sector", "Xerr",
    "--candidate", E / "solver/candidate.json", "--source", I / "source.json.gz",
    "--direct-root", E / "direct", "--cnf", E / "direct/direct360/Xerr.cnf",
    "--assignment", E / "direct/solver/Xerr.assignment.dimacs", "--output", O / "Xerr.orbit.json"])
exact("Xerr orbit", O / "Xerr.orbit.json", E / "verification/Xerr_translation_orbit.json")
run("Zerr_orbit", [py, U / "audit_selector_translation_orbit_round116.py", "--sector", "Zerr",
    "--candidate", E / "solver/candidate.json", "--source", I / "source.json.gz",
    "--direct-root", E / "direct", "--cnf", E / "direct/direct360/Zerr.cnf",
    "--assignment", E / "direct/solver/Zerr.assignment.dimacs", "--prior-audit", O / "Xerr.orbit.json",
    "--output", O / "Zerr.orbit.json"])
exact("Zerr orbit", O / "Zerr.orbit.json", E / "verification/Zerr_translation_orbit.json")
run("css_iter194", [py, U / "audit_css_duality_iter194_round116.py",
    "--source", I / "source.json.gz", "--state", I / "state.json",
    "--candidate", E / "solver/candidate.json", "--output", O / "css.iter194.json"])
exact("iter194 CSS audit", O / "css.iter194.json", E / "verification/css_duality_registry_audit.json")
run("candidate_css_duals", [py, U / "audit_css_dual_selector_orbits_round116.py",
    "--source", I / "source.json.gz", "--candidate", E / "solver/candidate.json",
    "--direct-root", E / "direct", "--x-audit", O / "Xerr.orbit.json", "--z-audit", O / "Zerr.orbit.json",
    "--css-audit", O / "css.iter194.json", "--output", O / "candidate.css_duals.json"])
exact("candidate CSS duals", O / "candidate.css_duals.json", E / "verification/css_dual_selector_orbits.json")

# Deterministically regenerate the next source, but never solve it.
run("regenerate_iter195_source", [py, S / "advance_css_closed_frontier_round118.py",
    "--source", I / "source.json.gz", "--state", I / "state.json", "--candidate", E / "solver/candidate.json",
    "--css-audit", O / "css.iter194.json", "--x-audit", O / "Xerr.orbit.json",
    "--z-audit", O / "Zerr.orbit.json", "--dual-audit", O / "candidate.css_duals.json",
    "--canonical-yaml", R / "bindings/CIRCDIST.gross.yaml", "--scheduler", R / "bindings/SCHEDULER.yaml",
    "--review", R / "bindings/round117_exact_review.md", "--prior-manifest", R / "bindings/round116_SHA256SUMS.txt",
    "--proofpilot", R / "bindings/round118_proofpilot_rank.json", "--output-source", G / "source.json.gz",
    "--output-state", G / "state.json", "--output-audit", G / "advance.json"])
exact("iter195 source regeneration", G / "source.json.gz", F / "source.json.gz")
exact("iter195 state regeneration", G / "state.json", F / "state.json")
exact("iter195 advance audit", G / "advance.json", F / "frontier_advance_audit.json")

run("iter195_translation", [py, U / "parent_check_registry_invariance_round110.py",
    "--source", F / "source.json.gz", "--state", F / "state.json", "--output", O / "iter195.translation.json",
    "--iteration", "195", "--blocks", "814392", "--selectors", "51048", "--assertions", "869838"])
semantic("iter195 translation closure", O / "iter195.translation.json", F / "translation_registry_check.json")
run("iter195_css", [py, S / "audit_css_duality_iter195_round118.py",
    "--source", F / "source.json.gz", "--state", F / "state.json", "--candidate", E / "solver/candidate.json",
    "--output", O / "iter195.css.json"])
exact("iter195 CSS closure", O / "iter195.css.json", F / "css_closure_check.json")
run("iter195_base_encoding", [py, U / "parent_check_outer_encoding.py",
    "--source", F / "source.json.gz", "--cnf", F / "formula/outer.cnf",
    "--metadata", F / "formula/metadata.json", "--assertion-map", F / "formula/assertion_map.jsonl",
    "--definitions", F / "formula/definitions.json.gz", "--output", O / "iter195.base_check.json"])
semantic("iter195 base encoding", O / "iter195.base_check.json", F / "base_encoding_check.json")
run("iter195_order144", [py, U / "check_order144_quotient_round116.py",
    "--base-cnf", F / "formula/outer.cnf", "--base-metadata", F / "formula/metadata.json",
    "--source", F / "source.json.gz", "--quotient-cnf", F / "order144_quotient/outer.cnf",
    "--quotient-metadata", F / "order144_quotient/metadata.json", "--roots", F / "order144_quotient/roots.jsonl",
    "--trace", F / "order144_quotient/trace.json.gz", "--base-encoding-check", F / "base_encoding_check.json",
    "--translation-registry-check", F / "translation_registry_check.json", "--css-closure-check", F / "css_closure_check.json",
    "--output", O / "iter195.order144.json"])
semantic("iter195 order144 check", O / "iter195.order144.json", F / "order144_quotient/check.json")
run("iter195_unstarted", [py, S / "check_frontier_unstarted_round118.py",
    "--frontier", F, "--ledger", R / "logs/process/session_process.jsonl",
    "--output", O / "iter195.unstarted.json"])

if not a.skip_sat_streams:
    run("sat_trace_streams", [py, S / "check_sat_trace_streams_round118.py",
        "--root", R, "--output", O / "sat_trace_streams.json"])

summary = {
    "schema": "circdist-gross-round118-sealed-replay-v1",
    "status": "PASS",
    "root": str(R),
    "output": str(O),
    "parent_pid": os.getpid(),
    "seal_check_skipped": a.skip_seal_check,
    "sat_streams_skipped": a.skip_sat_streams,
    "strict_serial": True,
    "max_simultaneous_children": 1,
    "runs": runs,
    "run_count": len(runs),
    "comparisons": comparisons,
    "comparison_count": len(comparisons),
    "all_children_reaped": True,
    "detached_children": 0,
    "timeouts_configured": 0,
    "timeouts_triggered": 0,
    "solver_invocations": 0,
    "fresh_iter195_remained_unstarted": True,
}
(O / "summary.json").write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n")
print(json.dumps({"status": "PASS", "runs": len(runs), "comparisons": len(comparisons),
                  "sat_streams_skipped": a.skip_sat_streams,
                  "seal_check_skipped": a.skip_seal_check}, sort_keys=True))
