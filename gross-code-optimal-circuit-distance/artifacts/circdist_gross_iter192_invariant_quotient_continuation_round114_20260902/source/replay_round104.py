#!/usr/bin/env python3
"""Strict-serial, read-only scientific replay for the Round104 package."""
from pathlib import Path
import argparse
import datetime
import hashlib
import json
import os
import subprocess
import sys
import tempfile
import time


def sha(path):
    h = hashlib.sha256()
    with Path(path).open("rb") as f:
        for chunk in iter(lambda: f.read(8 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def json_without(path, keys=()):
    value = json.loads(Path(path).read_text())
    for key in keys:
        value.pop(key, None)
    return value


def tree_hashes(root):
    return {p.relative_to(root).as_posix(): sha(p) for p in sorted(root.rglob("*")) if p.is_file()}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", type=Path, required=True)
    ap.add_argument("--output", type=Path, required=True)
    args = ap.parse_args()
    package = args.root.resolve()
    output = args.output if args.output.is_absolute() else package / args.output
    records = []
    clean_env = {
        "PATH": "/usr/bin:/bin:/usr/sbin:/sbin",
        "LANG": "C.UTF-8", "LC_ALL": "C.UTF-8",
        "PYTHONDONTWRITEBYTECODE": "1",
        "PYTHONPATH": str(package / "python/site-packages"),
        "TMPDIR": os.environ.get("TMPDIR", "/tmp"),
    }

    def run(name, command, timeout=1800):
        command = [str(x) for x in command]
        started = time.time()
        child = subprocess.Popen(command, cwd=package, env=clean_env,
                                 stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                 text=True, start_new_session=False)
        timed_out = term_sent = kill_sent = False
        try:
            stdout, stderr = child.communicate(timeout=timeout)
        except subprocess.TimeoutExpired:
            timed_out = term_sent = True
            child.terminate()
            try:
                stdout, stderr = child.communicate(timeout=15)
            except subprocess.TimeoutExpired:
                kill_sent = True
                child.kill()
                stdout, stderr = child.communicate()
        ended = time.time()
        row = {"name": name, "command": command, "child_pid": child.pid,
               "parent_pid": os.getpid(), "started_unix": started,
               "ended_unix": ended, "started_utc": datetime.datetime.fromtimestamp(
                   started, datetime.timezone.utc).isoformat(),
               "ended_utc": datetime.datetime.fromtimestamp(
                   ended, datetime.timezone.utc).isoformat(),
               "wall_seconds": round(ended - started, 6),
               "returncode": child.returncode, "stdout": stdout, "stderr": stderr,
               "timed_out": timed_out, "term_sent": term_sent, "kill_sent": kill_sent,
               "reaped": True, "detached": False}
        records.append(row)
        assert not timed_out and child.returncode == 0, (name, child.returncode,
                                                          stdout[-2000:], stderr[-2000:])
        return row

    with tempfile.TemporaryDirectory(prefix="circdist-round104-replay.") as td:
        temp = Path(td)
        bindings = temp / "bindings.json"
        run("immutable_input_bindings", [sys.executable, "source/bind_inputs_round104.py",
                                          "--root", package, "--output", bindings])
        fresh_binding = json.loads(bindings.read_text())
        stored_binding = json.loads((package / "INPUT_BINDINGS.json").read_text())
        for key in ("schema", "status", "expected_and_observed",
                    "round102_root_sha256sums_digest", "frontier", "tooling"):
            assert fresh_binding[key] == stored_binding[key]
        assert {k: v for k, v in fresh_binding["environment"].items() if k != "cwd"} == {
            k: v for k, v in stored_binding["environment"].items() if k != "cwd"}

        assignment = temp / "assignment.dimacs"
        assignment_check = temp / "assignment_check.json"
        run("complete_quotient_assignment", [sys.executable,
            "source/extract_and_check_assignment.py", "--cnf",
            "inputs/round102/frontier/iter187_full_invariant_quotient/outer.cnf",
            "--solver-log", "solver/iter187/solver.log", "--assignment", assignment,
            "--output", assignment_check])
        assert assignment.read_bytes() == (package / "solver/iter187/assignment.dimacs").read_bytes()
        assert assignment_check.read_bytes() == (package / "solver/iter187/assignment_check.json").read_bytes()

        verifier_assignment = temp / "assignment.replay.dimacs"
        candidate = temp / "candidate.json"
        outer_replay = temp / "outer_replay.json"
        run("frozen_outer_model_and_schedule_replay", [sys.executable,
            "source/verify_outer_sat_model.py", "--solver-log", "solver/iter187/solver.log",
            "--cnf", "inputs/round102/frontier/iter187_full_invariant_quotient/outer.cnf",
            "--source", "inputs/round102/frontier/iter187_full_invariant/source.json.gz",
            "--metadata", "inputs/round102/frontier/iter187_full_invariant_quotient/metadata.json",
            "--frozen", "vendor/round80", "--assignment", verifier_assignment,
            "--candidate", candidate, "--output", outer_replay], timeout=3600)
        assert verifier_assignment.read_bytes() == (package / "solver/iter187/assignment.replay.dimacs").read_bytes()
        assert candidate.read_bytes() == (package / "solver/iter187/candidate.json").read_bytes()
        assert json_without(outer_replay, ("seconds",)) == json_without(
            package / "solver/iter187/replay.json", ("seconds",))

        orbit = temp / "orbit.json"
        run("quotient_clause_orbit_and_negative_controls", [sys.executable,
            "source/check_sat_orbit_controls_round102.py", "--cnf",
            "inputs/round102/frontier/iter187_full_invariant_quotient/outer.cnf",
            "--metadata", "inputs/round102/frontier/iter187_full_invariant_quotient/metadata.json",
            "--source", "inputs/round102/frontier/iter187_full_invariant/source.json.gz",
            "--assignment", "solver/iter187/assignment.replay.dimacs",
            "--candidate", "solver/iter187/candidate.json",
            "--trace", "inputs/round102/frontier/iter187_full_invariant_quotient/translation_trace.json.gz",
            "--output", orbit])
        assert orbit.read_bytes() == (package / "controls/iter187_sat_orbit_controls.json").read_bytes()

        fresh_direct = temp / "direct"
        run("rebuild_complete_unrestricted_direct_formulas", [sys.executable,
            "source/build_direct_from_candidate.py", "--candidate", "solver/iter187/candidate.json",
            "--output", fresh_direct, "--vendor", "vendor/round80",
            "--source-selector-count", "24012"])
        expected_direct = tree_hashes(package / "solver/iter187/direct/direct360")
        observed_direct = tree_hashes(fresh_direct / "direct360")
        assert observed_direct == expected_direct
        assert (fresh_direct / "candidate.json").read_bytes() == (
            package / "solver/iter187/direct/candidate.json").read_bytes()
        assert (fresh_direct / "build_summary.json").read_bytes() == (
            package / "solver/iter187/direct/build_summary.json").read_bytes()

        direct_replay = temp / "direct_replay.json"
        run("frozen_both_direct_sector_physical_replay", [sys.executable,
            "vendor/round80/src/replay_direct_candidate.py", "--root",
            "solver/iter187/direct", "--output", direct_replay])
        assert direct_replay.read_bytes() == (
            package / "solver/iter187/direct/direct_verification.json").read_bytes()

        independent_direct = temp / "independent_direct.json"
        run("independent_stdlib_direct_audit", [sys.executable,
            "source/independent_iter187_direct_audit.py", "--root", package,
            "--output", independent_direct])
        assert independent_direct.read_bytes() == (
            package / "verification/iter187_direct_independent_audit.json").read_bytes()

        fresh_source = temp / "iter188.source.json.gz"
        fresh_state = temp / "iter188.state.json"
        fresh_audit = temp / "iter188.orbit_audit.json"
        run("rebuild_iter188_full_translation_orbits", [sys.executable,
            "source/advance_full_invariant_frontier_round104.py", "--source",
            "inputs/round102/frontier/iter187_full_invariant/source.json.gz", "--state",
            "inputs/round102/frontier/iter187_full_invariant/state.json", "--candidate",
            "solver/iter187/candidate.json", "--direct",
            "solver/iter187/direct/direct_verification.json", "--vendor", "vendor/round80",
            "--output-source", fresh_source, "--output-state", fresh_state,
            "--output-audit", fresh_audit], timeout=3600)
        assert fresh_source.read_bytes() == (package / "frontier/iter188_full_invariant/source.json.gz").read_bytes()
        assert fresh_state.read_bytes() == (package / "frontier/iter188_full_invariant/state.json").read_bytes()
        assert fresh_audit.read_bytes() == (package / "frontier/iter188_full_invariant/orbit_audit.json").read_bytes()

        closure = temp / "closure.json"
        run("independent_full_registry_invariance", [sys.executable,
            "source/check_incremental_orbit_closure_round104.py", "--root", package,
            "--output", closure], timeout=3600)
        assert closure.read_bytes() == (
            package / "verification/iter188_incremental_orbit_closure_independent.json").read_bytes()

        encoding = temp / "encoding.json"
        run("iter188_base_source_cnf_bijection", [sys.executable,
            "source/check_outer_encoding.py", "--source", "frontier/iter188_full_invariant/source.json.gz",
            "--cnf", "frontier/iter188_full_invariant/formula/outer.cnf", "--metadata",
            "frontier/iter188_full_invariant/formula/metadata.json", "--assertion-map",
            "frontier/iter188_full_invariant/formula/assertion_map.jsonl", "--definitions",
            "frontier/iter188_full_invariant/formula/definitions.json.gz", "--output", encoding],
            timeout=3600)
        assert json_without(encoding, ("seconds",)) == json_without(
            package / "frontier/iter188_full_invariant/formula/encoding_check.json", ("seconds",))

        quotient = temp / "quotient.json"
        run("iter188_quotient_exact_clause_reconstruction", [sys.executable,
            "source/check_translation_quotient_round102.py", "--base-cnf",
            "frontier/iter188_full_invariant/formula/outer.cnf", "--base-metadata",
            "frontier/iter188_full_invariant/formula/metadata.json", "--source",
            "frontier/iter188_full_invariant/source.json.gz", "--quotient-cnf",
            "frontier/iter188_full_invariant_quotient/outer.cnf", "--quotient-metadata",
            "frontier/iter188_full_invariant_quotient/metadata.json", "--roots",
            "frontier/iter188_full_invariant_quotient/translation_roots.jsonl", "--trace",
            "frontier/iter188_full_invariant_quotient/translation_trace.json.gz", "--vendor",
            "vendor/round80", "--candidate", "solver/iter187/candidate.json", "--direct",
            "solver/iter187/direct/direct_verification.json", "--output", quotient], timeout=3600)
        assert json_without(quotient, ("wall_seconds",)) == json_without(
            package / "frontier/iter188_full_invariant_quotient/independent_check.json",
            ("wall_seconds",))

        traces = temp / "traces.json"
        run("lossless_sat_trace_streams", [sys.executable,
            "source/check_sat_trace_streams_round104.py", "--root", package,
            "--output", traces])
        assert traces.read_bytes() == (
            package / "verification/iter187_sat_trace_stream_check.json").read_bytes()

        proof = temp / "proof.json"
        run("valid_corrupt_truncated_proof_tool_controls", [sys.executable,
            "source/check_proof_controls.py", "--root", package, "--output", proof])
        assert json.loads(proof.read_text())["status"] == "PASS"

        if (package / "SHA256SUMS.txt").exists():
            run("sealed_package_manifests", [sys.executable, "source/check_manifests.py",
                                              "--root", package], timeout=3600)

    result = {
        "schema": "circdist-gross-round104-scientific-replay-v1", "status": "PASS",
        "package": str(package), "output": str(output), "python": sys.executable,
        "python_sha256": sha(sys.executable), "clean_environment": clean_env,
        "strict_serial": True, "children": records, "direct_child_count": len(records),
        "all_children_reaped": all(row["reaped"] for row in records),
        "detached_processes": 0, "checks": [row["name"] for row in records],
        "verdict": "MATERIAL-CHECKED-CONTINUATION-NOT-CLOSED",
        "fresh_frontier": {"iteration": 188, "started": False,
                           "quotient_sha256": sha(package / "frontier/iter188_full_invariant_quotient/outer.cnf"),
                           "variables": 2455196, "clauses": 11798572}}
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps({"status": "PASS", "children": len(records),
                      "all_children_reaped": True, "output": str(output)}, sort_keys=True))


if __name__ == "__main__":
    main()
