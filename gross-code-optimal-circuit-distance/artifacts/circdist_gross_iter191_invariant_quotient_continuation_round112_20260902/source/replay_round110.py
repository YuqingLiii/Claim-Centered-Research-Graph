#!/usr/bin/env python3
"""Clean-environment, strict-serial replay of the Round110 continuation package."""
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
    digest = hashlib.sha256()
    with Path(path).open("rb") as handle:
        for block in iter(lambda: handle.read(8 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def without(path, keys=()):
    value = json.loads(Path(path).read_text())
    for key in keys:
        value.pop(key, None)
    return value


def tree_hashes(root):
    return {p.relative_to(root).as_posix(): sha(p) for p in sorted(root.rglob("*")) if p.is_file()}


def snapshot(root):
    return {p.relative_to(root).as_posix(): (p.stat().st_size, p.stat().st_mtime_ns, p.stat().st_mode & 0o7777)
            for p in sorted(root.rglob("*")) if p.is_file()}


def check_manifest(package, name, exact=False):
    path = package / name
    rows, seen = 0, set()
    for line in path.read_text().splitlines():
        digest, rel = line.split("  ", 1)
        assert rel not in seen and (package / rel).is_file() and sha(package / rel) == digest
        seen.add(rel); rows += 1
    if exact:
        actual = {p.relative_to(package).as_posix() for p in package.rglob("*") if p.is_file()}
        actual.discard(name)
        assert seen == actual
    return {"name": name, "sha256": sha(path), "rows": rows, "status": "PASS", "exact": exact}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", type=Path, required=True)
    ap.add_argument("--output", type=Path, required=True)
    args = ap.parse_args()
    package, output = args.root.resolve(), args.output.resolve()
    assert output != package and package not in output.parents
    initial_snapshot = snapshot(package)
    env = {"PATH": "/usr/bin:/bin:/usr/sbin:/sbin", "LANG": "C.UTF-8", "LC_ALL": "C.UTF-8",
           "PYTHONDONTWRITEBYTECODE": "1", "PYTHONPATH": str(package / "python/site-packages"),
           "TMPDIR": os.environ.get("TMPDIR", "/tmp")}
    records = []

    def run(name, command, timeout=3600):
        command = [str(item) for item in command]
        started = time.time()
        child = subprocess.Popen(command, cwd=package, env=env, stdout=subprocess.PIPE,
                                 stderr=subprocess.PIPE, text=True, start_new_session=False)
        timed_out = term_sent = kill_sent = False
        try:
            stdout, stderr = child.communicate(timeout=timeout)
        except subprocess.TimeoutExpired:
            timed_out = term_sent = True; child.terminate()
            try:
                stdout, stderr = child.communicate(timeout=15)
            except subprocess.TimeoutExpired:
                kill_sent = True; child.kill(); stdout, stderr = child.communicate()
        ended = time.time()
        row = {"name": name, "argv": command, "cwd": str(package), "environment": env,
               "parent_pid": os.getpid(), "child_pid": child.pid, "started_unix": started,
               "ended_unix": ended,
               "started_utc": datetime.datetime.fromtimestamp(started, datetime.timezone.utc).isoformat(),
               "ended_utc": datetime.datetime.fromtimestamp(ended, datetime.timezone.utc).isoformat(),
               "wall_seconds": round(ended-started, 6), "returncode": child.returncode,
               "stdout": stdout, "stderr": stderr, "stdout_sha256": hashlib.sha256(stdout.encode()).hexdigest(),
               "stderr_sha256": hashlib.sha256(stderr.encode()).hexdigest(),
               "stdout_bytes": len(stdout.encode()), "stderr_bytes": len(stderr.encode()),
               "timed_out": timed_out, "term_sent": term_sent, "kill_sent": kill_sent,
               "reaped": True, "detached": False}
        records.append(row)
        print(json.dumps({"event": "REPLAY_CHILD", "name": name, "child_pid": child.pid,
                          "returncode": child.returncode, "wall_seconds": row["wall_seconds"]}, sort_keys=True), flush=True)
        assert child.returncode == 0 and not timed_out, (name, child.returncode, stdout[-2000:], stderr[-2000:])
        return row

    with tempfile.TemporaryDirectory(prefix="circdist-round110-replay.") as td:
        temp = Path(td)
        binding = temp / "bindings.json"
        run("package_bindings_and_freshness", [sys.executable, "source/check_package_bindings_round110.py",
            "--root", package, "--output", binding])
        assert json.loads(binding.read_text())["status"] == "PASS"

        input_base = temp / "input_base.json"
        run("reviewed_iter190_source_base_bijection", [sys.executable, "source/check_outer_encoding.py",
            "--source", "inputs/round108/frontier/iter190_full_invariant/source.json.gz",
            "--cnf", "inputs/round108/frontier/iter190_full_invariant/formula/outer.cnf",
            "--metadata", "inputs/round108/frontier/iter190_full_invariant/formula/metadata.json",
            "--assertion-map", "inputs/round108/frontier/iter190_full_invariant/formula/assertion_map.jsonl",
            "--definitions", "inputs/round108/frontier/iter190_full_invariant/formula/definitions.json.gz",
            "--output", input_base])
        assert without(input_base, ("seconds",)) == without(package / "verification/input_base_bijection.json", ("seconds",))

        input_registry = temp / "input_registry.json"
        run("reviewed_iter190_full_registry_invariance", [sys.executable,
            "source/check_registry_invariance_round110.py", "--source",
            "inputs/round108/frontier/iter190_full_invariant/source.json.gz", "--state",
            "inputs/round108/frontier/iter190_full_invariant/state.json", "--output", input_registry,
            "--iteration", "190", "--blocks", "517140", "--selectors", "24444", "--assertions", "545982"])
        assert input_registry.read_bytes() == (package / "verification/input_registry_invariance.json").read_bytes()

        input_quotient = temp / "input_quotient.json"
        run("reviewed_iter190_quotient_reconstruction", [sys.executable,
            "source/check_translation_quotient_round102.py", "--base-cnf",
            "inputs/round108/frontier/iter190_full_invariant/formula/outer.cnf", "--base-metadata",
            "inputs/round108/frontier/iter190_full_invariant/formula/metadata.json", "--source",
            "inputs/round108/frontier/iter190_full_invariant/source.json.gz", "--quotient-cnf",
            "inputs/round108/frontier/iter190_full_invariant_quotient/outer.cnf", "--quotient-metadata",
            "inputs/round108/frontier/iter190_full_invariant_quotient/metadata.json", "--roots",
            "inputs/round108/frontier/iter190_full_invariant_quotient/translation_roots.jsonl", "--trace",
            "inputs/round108/frontier/iter190_full_invariant_quotient/translation_trace.json.gz", "--vendor",
            "vendor/round80", "--candidate", "inputs/round108/iter189_adjudication/candidate.json",
            "--direct", "inputs/round108/iter189_adjudication/direct_verification.json", "--output", input_quotient])
        assert without(input_quotient, ("wall_seconds",)) == without(package / "verification/input_quotient_reconstruction.json", ("wall_seconds",))

        assignment, assignment_check = temp / "assignment.dimacs", temp / "assignment_check.json"
        run("complete_iter190_quotient_assignment", [sys.executable, "source/extract_and_check_assignment.py",
            "--cnf", "inputs/round108/frontier/iter190_full_invariant_quotient/outer.cnf",
            "--solver-log", "solver/iter190/solver.log", "--assignment", assignment, "--output", assignment_check])
        assert assignment.read_bytes() == (package / "solver/iter190/assignment.dimacs").read_bytes()
        assert assignment_check.read_bytes() == (package / "solver/iter190/assignment_check.json").read_bytes()

        replay_assignment, candidate, model = temp / "assignment.replay.dimacs", temp / "candidate.json", temp / "model.json"
        run("iter190_frozen_model_and_schedule_replay", [sys.executable, "source/verify_outer_sat_model.py",
            "--solver-log", "solver/iter190/solver.log", "--cnf",
            "inputs/round108/frontier/iter190_full_invariant_quotient/outer.cnf", "--source",
            "inputs/round108/frontier/iter190_full_invariant/source.json.gz", "--metadata",
            "inputs/round108/frontier/iter190_full_invariant_quotient/metadata.json", "--frozen", "vendor/round80",
            "--assignment", replay_assignment, "--candidate", candidate, "--output", model])
        assert replay_assignment.read_bytes() == (package / "solver/iter190/assignment.replay.dimacs").read_bytes()
        assert candidate.read_bytes() == (package / "solver/iter190/candidate.json").read_bytes()
        assert without(model, ("seconds",)) == without(package / "solver/iter190/replay.json", ("seconds",))

        orbit = temp / "orbit.json"
        run("iter190_quotient_orbit_controls", [sys.executable, "source/check_sat_orbit_controls_round102.py",
            "--cnf", "inputs/round108/frontier/iter190_full_invariant_quotient/outer.cnf", "--metadata",
            "inputs/round108/frontier/iter190_full_invariant_quotient/metadata.json", "--source",
            "inputs/round108/frontier/iter190_full_invariant/source.json.gz", "--assignment",
            "solver/iter190/assignment.dimacs", "--candidate", "solver/iter190/candidate.json", "--trace",
            "inputs/round108/frontier/iter190_full_invariant_quotient/translation_trace.json.gz", "--output", orbit])
        assert orbit.read_bytes() == (package / "verification/iter190_sat_orbit_controls.json").read_bytes()

        rebuilt_direct = temp / "direct"
        run("rebuild_iter190_unrestricted_direct360", [sys.executable, "source/build_direct_from_candidate.py",
            "--candidate", "solver/iter190/candidate.json", "--output", rebuilt_direct,
            "--vendor", "vendor/round80", "--source-selector-count", "24444"])
        assert tree_hashes(rebuilt_direct / "direct360") == tree_hashes(package / "solver/iter190/direct/direct360")
        assert (rebuilt_direct / "candidate.json").read_bytes() == (package / "solver/iter190/direct/candidate.json").read_bytes()
        assert (rebuilt_direct / "build_summary.json").read_bytes() == (package / "solver/iter190/direct/build_summary.json").read_bytes()

        for sector in ("Xerr", "Zerr"):
            out_assignment, out_check = temp / f"{sector}.assignment.dimacs", temp / f"{sector}.check.json"
            run(f"complete_iter190_{sector}_assignment", [sys.executable, "source/extract_and_check_assignment.py",
                "--cnf", f"solver/iter190/direct/direct360/{sector}.cnf", "--solver-log",
                f"solver/iter190/direct/solver/{sector}.solver.log", "--assignment", out_assignment,
                "--output", out_check])
            assert out_assignment.read_bytes() == (package / f"solver/iter190/direct/solver/{sector}.assignment.dimacs").read_bytes()
            assert out_check.read_bytes() == (package / f"solver/iter190/direct/solver/{sector}.assignment_check.json").read_bytes()

        direct_replay = temp / "direct_replay.json"
        run("iter190_both_sector_physical_replay", [sys.executable,
            "vendor/round80/src/replay_direct_candidate.py", "--root", "solver/iter190/direct", "--output", direct_replay])
        assert direct_replay.read_bytes() == (package / "solver/iter190/direct/direct_verification.json").read_bytes()

        direct_independent = temp / "direct_independent.json"
        run("iter190_independent_stdlib_direct_audit", [sys.executable,
            "source/independent_iter190_direct_audit_round110.py", "--root", package, "--output", direct_independent])
        assert direct_independent.read_bytes() == (package / "verification/iter190_direct_independent_audit.json").read_bytes()

        fresh_source, fresh_state, fresh_audit = temp / "source.json.gz", temp / "state.json", temp / "audit.json"
        run("rebuild_complete_iter190_mechanism_orbits", [sys.executable,
            "source/advance_full_invariant_frontier_round110.py", "--source",
            "inputs/round108/frontier/iter190_full_invariant/source.json.gz", "--state",
            "inputs/round108/frontier/iter190_full_invariant/state.json", "--candidate",
            "solver/iter190/candidate.json", "--direct", "solver/iter190/direct/direct_verification.json",
            "--vendor", "vendor/round80", "--output-source", fresh_source,
            "--output-state", fresh_state, "--output-audit", fresh_audit])
        assert fresh_source.read_bytes() == (package / "frontier/iter191_full_invariant/source.json.gz").read_bytes()
        assert fresh_state.read_bytes() == (package / "frontier/iter191_full_invariant/state.json").read_bytes()
        assert fresh_audit.read_bytes() == (package / "frontier/iter191_full_invariant/orbit_audit.json").read_bytes()

        closure = temp / "closure.json"
        run("iter191_independent_incremental_orbit_closure", [sys.executable,
            "source/check_incremental_orbit_closure_round110.py", "--root", package, "--output", closure])
        assert closure.read_bytes() == (package / "verification/iter191_incremental_orbit_closure_independent.json").read_bytes()

        fresh_base = temp / "fresh_base.json"
        run("iter191_source_base_bijection", [sys.executable, "source/check_outer_encoding.py",
            "--source", "frontier/iter191_full_invariant/source.json.gz", "--cnf",
            "frontier/iter191_full_invariant/formula/outer.cnf", "--metadata",
            "frontier/iter191_full_invariant/formula/metadata.json", "--assertion-map",
            "frontier/iter191_full_invariant/formula/assertion_map.jsonl", "--definitions",
            "frontier/iter191_full_invariant/formula/definitions.json.gz", "--output", fresh_base])
        assert without(fresh_base, ("seconds",)) == without(package / "frontier/iter191_full_invariant/formula/encoding_check.json", ("seconds",))

        fresh_quotient = temp / "fresh_quotient.json"
        run("iter191_exact_quotient_reconstruction", [sys.executable,
            "source/check_translation_quotient_round102.py", "--base-cnf",
            "frontier/iter191_full_invariant/formula/outer.cnf", "--base-metadata",
            "frontier/iter191_full_invariant/formula/metadata.json", "--source",
            "frontier/iter191_full_invariant/source.json.gz", "--quotient-cnf",
            "frontier/iter191_full_invariant_quotient/outer.cnf", "--quotient-metadata",
            "frontier/iter191_full_invariant_quotient/metadata.json", "--roots",
            "frontier/iter191_full_invariant_quotient/translation_roots.jsonl", "--trace",
            "frontier/iter191_full_invariant_quotient/translation_trace.json.gz", "--vendor", "vendor/round80",
            "--candidate", "solver/iter190/candidate.json", "--direct",
            "solver/iter190/direct/direct_verification.json", "--output", fresh_quotient])
        assert without(fresh_quotient, ("wall_seconds",)) == without(
            package / "frontier/iter191_full_invariant_quotient/independent_check.json", ("wall_seconds",))

        traces = temp / "traces.json"
        run("lossless_iter190_SAT_trace_streams", [sys.executable,
            "source/check_sat_trace_streams_round110.py", "--root", package, "--output", traces])
        assert traces.read_bytes() == (package / "verification/iter190_sat_trace_streams.json").read_bytes()

        proof = temp / "proof.json"
        run("valid_corrupt_truncated_proof_controls", [sys.executable,
            "source/check_proof_controls.py", "--root", package, "--output", proof])
        proof_value = json.loads(proof.read_text())
        assert all(proof_value[key] is True for key in ("valid_drat_accepted", "generated_lrat_accepted",
            "corrupt_drat_rejected", "truncated_drat_rejected", "corrupt_lrat_rejected", "truncated_lrat_rejected"))

        result_check = temp / "result.json"
        run("honest_result_and_residual", [sys.executable, "source/check_result_round110.py",
            "--root", package, "--output", result_check])
        assert json.loads(result_check.read_text())["status"] == "PASS"

    manifests = []
    if (package / "PAYLOAD_SHA256SUMS.txt").exists():
        manifests.append(check_manifest(package, "PAYLOAD_SHA256SUMS.txt"))
    if (package / "SHA256SUMS.txt").exists():
        manifests.append(check_manifest(package, "SHA256SUMS.txt", exact=True))
    intervals = sorted((row["started_unix"], row["ended_unix"]) for row in records)
    strict_nonoverlap = all(intervals[i][1] <= intervals[i+1][0] for i in range(len(intervals)-1))
    assert strict_nonoverlap and all(row["reaped"] and not row["detached"] for row in records)
    assert snapshot(package) == initial_snapshot, "replay mutated package"
    result = {"schema": "circdist-gross-round110-clean-replay-v1", "status": "PASS",
              "package": str(package), "clean_environment": env, "children": records,
              "child_count": len(records), "strict_serial": True,
              "strict_child_nonoverlap": strict_nonoverlap,
              "all_children_reaped": True, "detached_processes": 0, "timeouts": 0,
              "package_mutated": False, "manifests": manifests,
              "root_closed": False, "canonical_level": "CONJECTURED", "interval": [11, 12],
              "fresh_iteration": 191, "fresh_unstarted": True}
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps({"status": "PASS", "child_count": len(records), "strict_serial": True,
                      "package_mutated": False, "fresh_iteration": 191}, sort_keys=True))


if __name__ == "__main__":
    main()
