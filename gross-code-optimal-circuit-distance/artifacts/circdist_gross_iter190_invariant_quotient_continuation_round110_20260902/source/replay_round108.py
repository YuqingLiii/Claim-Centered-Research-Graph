#!/usr/bin/env python3
"""Clean-environment, strict-serial replay of the Round108 scientific package."""
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
    with Path(path).open("rb") as handle:
        for block in iter(lambda: handle.read(8 << 20), b""):
            h.update(block)
    return h.hexdigest()


def without(path, keys=()):
    value = json.loads(Path(path).read_text())
    for key in keys:
        value.pop(key, None)
    return value


def tree_hashes(root):
    return {p.relative_to(root).as_posix(): sha(p)
            for p in sorted(root.rglob("*")) if p.is_file()}


def check_manifest(package, name):
    path = package / name
    seen = set()
    rows = 0
    for line in path.read_text().splitlines():
        digest, rel = line.split("  ", 1)
        assert rel not in seen and sha(package / rel) == digest
        seen.add(rel)
        rows += 1
    return {"name": name, "sha256": sha(path), "rows": rows, "status": "PASS"}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", type=Path, required=True)
    ap.add_argument("--output", type=Path, required=True)
    args = ap.parse_args()
    package = args.root.resolve()
    output = args.output.resolve()
    assert output != package and package not in output.parents, "replay output must be external to package"
    clean_env = {
        "PATH": "/usr/bin:/bin:/usr/sbin:/sbin", "LANG": "C.UTF-8", "LC_ALL": "C.UTF-8",
        "PYTHONDONTWRITEBYTECODE": "1", "PYTHONPATH": str(package / "python/site-packages"),
        "TMPDIR": os.environ.get("TMPDIR", "/tmp"),
    }
    records = []

    def run(name, command, timeout=3600):
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
        row = {
            "name": name, "command": command, "parent_pid": os.getpid(), "child_pid": child.pid,
            "started_unix": started, "ended_unix": ended,
            "started_utc": datetime.datetime.fromtimestamp(started, datetime.timezone.utc).isoformat(),
            "ended_utc": datetime.datetime.fromtimestamp(ended, datetime.timezone.utc).isoformat(),
            "wall_seconds": round(ended - started, 6), "returncode": child.returncode,
            "stdout": stdout, "stderr": stderr, "timed_out": timed_out,
            "term_sent": term_sent, "kill_sent": kill_sent, "reaped": True, "detached": False,
        }
        records.append(row)
        print(json.dumps({"event": "REPLAY_CHILD", "name": name, "child_pid": child.pid,
                          "returncode": child.returncode, "wall_seconds": row["wall_seconds"]},
                         sort_keys=True), flush=True)
        assert child.returncode == 0 and not timed_out, (name, child.returncode,
                                                         stdout[-2000:], stderr[-2000:])
        return row

    with tempfile.TemporaryDirectory(prefix="circdist-round108-replay.") as td:
        temp = Path(td)
        bindings = temp / "bindings.json"
        run("package_bindings_allowlists_freshness", [sys.executable,
            "source/check_package_bindings_round108.py", "--root", package, "--output", bindings])
        assert json.loads(bindings.read_text())["status"] == "PASS"

        input_base = temp / "input_base.json"
        run("reviewed_iter189_source_base_bijection", [sys.executable,
            "source/check_outer_encoding.py", "--source",
            "inputs/round106/frontier/iter189_full_invariant/source.json.gz", "--cnf",
            "inputs/round106/frontier/iter189_full_invariant/formula/outer.cnf", "--metadata",
            "inputs/round106/frontier/iter189_full_invariant/formula/metadata.json", "--assertion-map",
            "inputs/round106/frontier/iter189_full_invariant/formula/assertion_map.jsonl", "--definitions",
            "inputs/round106/frontier/iter189_full_invariant/formula/definitions.json.gz", "--output", input_base])
        assert without(input_base, ("seconds",)) == without(
            package / "verification/input_base_bijection.json", ("seconds",))

        input_registry = temp / "input_registry.json"
        run("reviewed_iter189_full_registry_invariance", [sys.executable,
            "source/check_input_registry_invariance_round108.py", "--source",
            "inputs/round106/frontier/iter189_full_invariant/source.json.gz", "--state",
            "inputs/round106/frontier/iter189_full_invariant/state.json", "--output", input_registry])
        assert input_registry.read_bytes() == (package / "verification/input_registry_invariance.json").read_bytes()

        input_quotient = temp / "input_quotient.json"
        run("reviewed_iter189_quotient_reconstruction", [sys.executable,
            "source/check_translation_quotient_round102.py", "--base-cnf",
            "inputs/round106/frontier/iter189_full_invariant/formula/outer.cnf", "--base-metadata",
            "inputs/round106/frontier/iter189_full_invariant/formula/metadata.json", "--source",
            "inputs/round106/frontier/iter189_full_invariant/source.json.gz", "--quotient-cnf",
            "inputs/round106/frontier/iter189_full_invariant_quotient/outer.cnf", "--quotient-metadata",
            "inputs/round106/frontier/iter189_full_invariant_quotient/metadata.json", "--roots",
            "inputs/round106/frontier/iter189_full_invariant_quotient/translation_roots.jsonl", "--trace",
            "inputs/round106/frontier/iter189_full_invariant_quotient/translation_trace.json.gz", "--vendor",
            "vendor/round80", "--candidate", "inputs/round106/iter188_adjudication/candidate.json",
            "--direct", "inputs/round106/iter188_adjudication/direct_verification.json",
            "--output", input_quotient])
        assert without(input_quotient, ("wall_seconds",)) == without(
            package / "verification/input_quotient_reconstruction.json", ("wall_seconds",))

        assignment = temp / "assignment.dimacs"
        assignment_check = temp / "assignment_check.json"
        run("complete_iter189_quotient_assignment", [sys.executable,
            "source/extract_and_check_assignment.py", "--cnf",
            "inputs/round106/frontier/iter189_full_invariant_quotient/outer.cnf",
            "--solver-log", "solver/iter189/solver.log", "--assignment", assignment,
            "--output", assignment_check])
        assert assignment.read_bytes() == (package / "solver/iter189/assignment.dimacs").read_bytes()
        assert assignment_check.read_bytes() == (package / "solver/iter189/assignment_check.json").read_bytes()

        replay_assignment, candidate, model_replay = (temp / "assignment.replay.dimacs",
                                                       temp / "candidate.json", temp / "model_replay.json")
        run("iter189_frozen_source_geometry_model_replay", [sys.executable,
            "source/verify_outer_sat_model.py", "--solver-log", "solver/iter189/solver.log",
            "--cnf", "inputs/round106/frontier/iter189_full_invariant_quotient/outer.cnf",
            "--source", "inputs/round106/frontier/iter189_full_invariant/source.json.gz",
            "--metadata", "inputs/round106/frontier/iter189_full_invariant_quotient/metadata.json",
            "--frozen", "vendor/round80", "--assignment", replay_assignment,
            "--candidate", candidate, "--output", model_replay])
        assert replay_assignment.read_bytes() == (package / "solver/iter189/assignment.replay.dimacs").read_bytes()
        assert candidate.read_bytes() == (package / "solver/iter189/candidate.json").read_bytes()
        assert without(model_replay, ("seconds",)) == without(
            package / "solver/iter189/replay.json", ("seconds",))

        orbit = temp / "orbit.json"
        run("iter189_quotient_unique_extension_controls", [sys.executable,
            "source/check_sat_orbit_controls_round102.py", "--cnf",
            "inputs/round106/frontier/iter189_full_invariant_quotient/outer.cnf", "--metadata",
            "inputs/round106/frontier/iter189_full_invariant_quotient/metadata.json", "--source",
            "inputs/round106/frontier/iter189_full_invariant/source.json.gz", "--assignment",
            "solver/iter189/assignment.dimacs", "--candidate", "solver/iter189/candidate.json", "--trace",
            "inputs/round106/frontier/iter189_full_invariant_quotient/translation_trace.json.gz",
            "--output", orbit])
        assert orbit.read_bytes() == (package / "verification/iter189_sat_orbit_controls.json").read_bytes()

        rebuilt_direct = temp / "direct"
        run("rebuild_iter189_complete_unrestricted_direct360", [sys.executable,
            "source/build_direct_from_candidate.py", "--candidate", "solver/iter189/candidate.json",
            "--output", rebuilt_direct, "--vendor", "vendor/round80", "--source-selector-count", "24300"])
        assert tree_hashes(rebuilt_direct / "direct360") == tree_hashes(
            package / "solver/iter189/direct/direct360")
        assert (rebuilt_direct / "candidate.json").read_bytes() == (
            package / "solver/iter189/direct/candidate.json").read_bytes()
        assert (rebuilt_direct / "build_summary.json").read_bytes() == (
            package / "solver/iter189/direct/build_summary.json").read_bytes()

        for sector in ("Xerr", "Zerr"):
            direct_assignment = temp / f"{sector}.assignment.dimacs"
            direct_check = temp / f"{sector}.assignment_check.json"
            run(f"complete_iter189_{sector}_direct_assignment", [sys.executable,
                "source/extract_and_check_assignment.py", "--cnf",
                f"solver/iter189/direct/direct360/{sector}.cnf", "--solver-log",
                f"solver/iter189/direct/solver/{sector}.solver.log", "--assignment",
                direct_assignment, "--output", direct_check])
            assert direct_assignment.read_bytes() == (
                package / f"solver/iter189/direct/solver/{sector}.assignment.dimacs").read_bytes()
            assert direct_check.read_bytes() == (
                package / f"solver/iter189/direct/solver/{sector}.assignment_check.json").read_bytes()

        direct_replay = temp / "direct_replay.json"
        run("iter189_both_sector_physical_replay", [sys.executable,
            "vendor/round80/src/replay_direct_candidate.py", "--root", "solver/iter189/direct",
            "--output", direct_replay])
        assert direct_replay.read_bytes() == (
            package / "solver/iter189/direct/direct_verification.json").read_bytes()

        direct_independent = temp / "direct_independent.json"
        run("iter189_independent_stdlib_direct_audit", [sys.executable,
            "source/independent_iter189_direct_audit_round108.py", "--root", package,
            "--output", direct_independent])
        assert direct_independent.read_bytes() == (
            package / "verification/iter189_direct_independent_audit.json").read_bytes()

        fresh_source, fresh_state, fresh_audit = (temp / "iter190.source.json.gz",
                                                  temp / "iter190.state.json", temp / "iter190.audit.json")
        run("rebuild_complete_iter189_translation_orbits", [sys.executable,
            "source/advance_full_invariant_frontier_round108.py", "--source",
            "inputs/round106/frontier/iter189_full_invariant/source.json.gz", "--state",
            "inputs/round106/frontier/iter189_full_invariant/state.json", "--candidate",
            "solver/iter189/candidate.json", "--direct", "solver/iter189/direct/direct_verification.json",
            "--vendor", "vendor/round80", "--output-source", fresh_source,
            "--output-state", fresh_state, "--output-audit", fresh_audit])
        assert fresh_source.read_bytes() == (
            package / "frontier/iter190_full_invariant/source.json.gz").read_bytes()
        assert fresh_state.read_bytes() == (
            package / "frontier/iter190_full_invariant/state.json").read_bytes()
        assert fresh_audit.read_bytes() == (
            package / "frontier/iter190_full_invariant/orbit_audit.json").read_bytes()

        closure = temp / "closure.json"
        run("iter190_independent_full_registry_invariance", [sys.executable,
            "source/check_incremental_orbit_closure_round108.py", "--root", package,
            "--output", closure])
        assert closure.read_bytes() == (
            package / "verification/iter190_incremental_orbit_closure_independent.json").read_bytes()

        base_check = temp / "base_check.json"
        run("iter190_source_base_cnf_bijection", [sys.executable,
            "source/check_outer_encoding.py", "--source", "frontier/iter190_full_invariant/source.json.gz",
            "--cnf", "frontier/iter190_full_invariant/formula/outer.cnf", "--metadata",
            "frontier/iter190_full_invariant/formula/metadata.json", "--assertion-map",
            "frontier/iter190_full_invariant/formula/assertion_map.jsonl", "--definitions",
            "frontier/iter190_full_invariant/formula/definitions.json.gz", "--output", base_check])
        assert without(base_check, ("seconds",)) == without(
            package / "frontier/iter190_full_invariant/formula/encoding_check.json", ("seconds",))

        quotient_check = temp / "quotient_check.json"
        run("iter190_exact_group_quotient_reconstruction", [sys.executable,
            "source/check_translation_quotient_round102.py", "--base-cnf",
            "frontier/iter190_full_invariant/formula/outer.cnf", "--base-metadata",
            "frontier/iter190_full_invariant/formula/metadata.json", "--source",
            "frontier/iter190_full_invariant/source.json.gz", "--quotient-cnf",
            "frontier/iter190_full_invariant_quotient/outer.cnf", "--quotient-metadata",
            "frontier/iter190_full_invariant_quotient/metadata.json", "--roots",
            "frontier/iter190_full_invariant_quotient/translation_roots.jsonl", "--trace",
            "frontier/iter190_full_invariant_quotient/translation_trace.json.gz", "--vendor",
            "vendor/round80", "--candidate", "solver/iter189/candidate.json", "--direct",
            "solver/iter189/direct/direct_verification.json", "--output", quotient_check])
        assert without(quotient_check, ("wall_seconds",)) == without(
            package / "frontier/iter190_full_invariant_quotient/independent_check.json", ("wall_seconds",))

        traces = temp / "traces.json"
        run("lossless_SAT_trace_streams", [sys.executable,
            "source/check_sat_trace_streams_round108.py", "--root", package, "--output", traces])
        assert traces.read_bytes() == (package / "verification/iter189_sat_trace_streams.json").read_bytes()

        proof = temp / "proof.json"
        run("valid_corrupt_truncated_proof_controls", [sys.executable,
            "source/check_proof_controls.py", "--root", package, "--output", proof])
        checked_proof = json.loads(proof.read_text())
        assert all(checked_proof[key] is True for key in (
            "valid_drat_accepted", "generated_lrat_accepted", "corrupt_drat_rejected",
            "truncated_drat_rejected", "corrupt_lrat_rejected", "truncated_lrat_rejected"))

    manifests = []
    for name in ("PAYLOAD_SHA256SUMS.txt", "SHA256SUMS.txt"):
        if (package / name).exists():
            manifests.append(check_manifest(package, name))
    intervals = sorted((row["started_unix"], row["ended_unix"]) for row in records)
    strict_nonoverlap = all(intervals[i][1] <= intervals[i + 1][0]
                            for i in range(len(intervals) - 1))
    assert strict_nonoverlap and all(row["reaped"] and not row["detached"] for row in records)
    result = {
        "schema": "circdist-gross-round108-scientific-replay-v1", "status": "PASS",
        "package": str(package), "output": str(output), "python": sys.executable,
        "python_sha256": sha(sys.executable), "clean_environment": clean_env,
        "strict_serial": True, "strict_child_nonoverlap": strict_nonoverlap,
        "children": records, "direct_child_count": len(records), "all_children_reaped": True,
        "detached_processes": 0, "manifests": manifests,
        "checks": [row["name"] for row in records],
        "verdict": "MATERIAL-CHECKED-CONTINUATION-NOT-CLOSED",
        "root_branches": {"A_distance12_witness": "OPEN", "B_universal_ceiling": "OPEN"},
        "fresh_frontier": {"iteration": 190, "started": False, "stop": None,
            "quotient_sha256": sha(package / "frontier/iter190_full_invariant_quotient/outer.cnf"),
            "variables": 2464197, "clauses": 11827887},
    }
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps({"status": "PASS", "children": len(records),
                      "all_children_reaped": True, "manifests": len(manifests),
                      "output": str(output)}, sort_keys=True))


if __name__ == "__main__":
    main()
