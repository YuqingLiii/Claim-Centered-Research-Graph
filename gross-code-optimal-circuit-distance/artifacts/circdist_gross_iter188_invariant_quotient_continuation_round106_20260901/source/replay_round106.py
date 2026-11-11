#!/usr/bin/env python3
"""Strict-serial, source-entry replay for the sealed Round106 package."""
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
        for block in iter(lambda: f.read(8 << 20), b""):
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
    output = args.output if args.output.is_absolute() else package / args.output
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
            "wall_seconds": round(ended-started, 6), "returncode": child.returncode,
            "stdout": stdout, "stderr": stderr, "timed_out": timed_out,
            "term_sent": term_sent, "kill_sent": kill_sent, "reaped": True, "detached": False,
        }
        records.append(row)
        assert child.returncode == 0 and not timed_out, (name, child.returncode, stdout[-2000:], stderr[-2000:])
        return row

    with tempfile.TemporaryDirectory(prefix="circdist-round106-replay.") as td:
        temp = Path(td)
        bindings = temp / "bindings.json"
        run("package_bindings_allowlists_freshness", [sys.executable,
            "source/check_package_bindings_round106.py", "--root", package, "--output", bindings])
        assert json.loads(bindings.read_text())["status"] == "PASS"

        assignment = temp / "assignment.dimacs"
        assignment_check = temp / "assignment_check.json"
        run("complete_iter188_quotient_assignment", [sys.executable,
            "source/extract_and_check_assignment.py", "--cnf",
            "inputs/round104/frontier/iter188_full_invariant_quotient/outer.cnf",
            "--solver-log", "solver/iter188/solver.log", "--assignment", assignment,
            "--output", assignment_check])
        assert assignment.read_bytes() == (package / "solver/iter188/assignment.dimacs").read_bytes()
        assert assignment_check.read_bytes() == (package / "solver/iter188/assignment_check.json").read_bytes()

        replay_assignment, candidate, model_replay = (temp / "assignment.replay.dimacs",
                                                       temp / "candidate.json", temp / "model_replay.json")
        run("iter188_frozen_source_geometry_model_replay", [sys.executable,
            "source/verify_outer_sat_model.py", "--solver-log", "solver/iter188/solver.log",
            "--cnf", "inputs/round104/frontier/iter188_full_invariant_quotient/outer.cnf",
            "--source", "inputs/round104/frontier/iter188_full_invariant/source.json.gz",
            "--metadata", "inputs/round104/frontier/iter188_full_invariant_quotient/metadata.json",
            "--frozen", "vendor/round80", "--assignment", replay_assignment,
            "--candidate", candidate, "--output", model_replay])
        assert replay_assignment.read_bytes() == (package / "solver/iter188/assignment.replay.dimacs").read_bytes()
        assert candidate.read_bytes() == (package / "solver/iter188/candidate.json").read_bytes()
        assert without(model_replay, ("seconds",)) == without(package / "solver/iter188/replay.json", ("seconds",))

        orbit = temp / "orbit.json"
        run("iter188_quotient_unique_extension_controls", [sys.executable,
            "source/check_sat_orbit_controls_round102.py", "--cnf",
            "inputs/round104/frontier/iter188_full_invariant_quotient/outer.cnf",
            "--metadata", "inputs/round104/frontier/iter188_full_invariant_quotient/metadata.json",
            "--source", "inputs/round104/frontier/iter188_full_invariant/source.json.gz",
            "--assignment", "solver/iter188/assignment.replay.dimacs", "--candidate",
            "solver/iter188/candidate.json", "--trace",
            "inputs/round104/frontier/iter188_full_invariant_quotient/translation_trace.json.gz",
            "--output", orbit])
        assert orbit.read_bytes() == (package / "controls/iter188_sat_orbit_controls.json").read_bytes()

        rebuilt_direct = temp / "direct"
        run("rebuild_iter188_complete_unrestricted_direct360", [sys.executable,
            "source/build_direct_from_candidate.py", "--candidate", "solver/iter188/candidate.json",
            "--output", rebuilt_direct, "--vendor", "vendor/round80", "--source-selector-count", "24156"])
        assert tree_hashes(rebuilt_direct / "direct360") == tree_hashes(package / "solver/iter188/direct/direct360")
        assert (rebuilt_direct / "candidate.json").read_bytes() == (package / "solver/iter188/direct/candidate.json").read_bytes()
        assert (rebuilt_direct / "build_summary.json").read_bytes() == (package / "solver/iter188/direct/build_summary.json").read_bytes()

        direct_replay = temp / "direct_replay.json"
        run("iter188_both_sector_physical_replay", [sys.executable,
            "vendor/round80/src/replay_direct_candidate.py", "--root", "solver/iter188/direct",
            "--output", direct_replay])
        assert direct_replay.read_bytes() == (package / "solver/iter188/direct/direct_verification.json").read_bytes()

        direct_independent = temp / "direct_independent.json"
        run("iter188_independent_stdlib_direct_audit", [sys.executable,
            "source/independent_iter188_direct_audit_round106.py", "--root", package,
            "--output", direct_independent])
        assert direct_independent.read_bytes() == (package / "verification/iter188_direct_independent_audit.json").read_bytes()

        fresh_source, fresh_state, fresh_audit = (temp / "iter189.source.json.gz",
                                                  temp / "iter189.state.json", temp / "iter189.audit.json")
        run("rebuild_complete_iter188_translation_orbits", [sys.executable,
            "source/advance_full_invariant_frontier_round106.py", "--source",
            "inputs/round104/frontier/iter188_full_invariant/source.json.gz", "--state",
            "inputs/round104/frontier/iter188_full_invariant/state.json", "--candidate",
            "solver/iter188/candidate.json", "--direct", "solver/iter188/direct/direct_verification.json",
            "--vendor", "vendor/round80", "--output-source", fresh_source,
            "--output-state", fresh_state, "--output-audit", fresh_audit])
        assert fresh_source.read_bytes() == (package / "frontier/iter189_full_invariant/source.json.gz").read_bytes()
        assert fresh_state.read_bytes() == (package / "frontier/iter189_full_invariant/state.json").read_bytes()
        assert fresh_audit.read_bytes() == (package / "frontier/iter189_full_invariant/orbit_audit.json").read_bytes()

        closure = temp / "closure.json"
        run("iter189_independent_full_registry_invariance", [sys.executable,
            "source/check_incremental_orbit_closure_round106.py", "--root", package,
            "--output", closure])
        assert closure.read_bytes() == (package / "verification/iter189_incremental_orbit_closure_independent.json").read_bytes()

        base_check = temp / "base_check.json"
        run("iter189_source_base_cnf_bijection", [sys.executable,
            "source/check_outer_encoding.py", "--source", "frontier/iter189_full_invariant/source.json.gz",
            "--cnf", "frontier/iter189_full_invariant/formula/outer.cnf", "--metadata",
            "frontier/iter189_full_invariant/formula/metadata.json", "--assertion-map",
            "frontier/iter189_full_invariant/formula/assertion_map.jsonl", "--definitions",
            "frontier/iter189_full_invariant/formula/definitions.json.gz", "--output", base_check])
        assert without(base_check, ("seconds",)) == without(
            package / "frontier/iter189_full_invariant/formula/encoding_check.json", ("seconds",))

        quotient_check = temp / "quotient_check.json"
        run("iter189_exact_group_quotient_reconstruction", [sys.executable,
            "source/check_translation_quotient_round102.py", "--base-cnf",
            "frontier/iter189_full_invariant/formula/outer.cnf", "--base-metadata",
            "frontier/iter189_full_invariant/formula/metadata.json", "--source",
            "frontier/iter189_full_invariant/source.json.gz", "--quotient-cnf",
            "frontier/iter189_full_invariant_quotient/outer.cnf", "--quotient-metadata",
            "frontier/iter189_full_invariant_quotient/metadata.json", "--roots",
            "frontier/iter189_full_invariant_quotient/translation_roots.jsonl", "--trace",
            "frontier/iter189_full_invariant_quotient/translation_trace.json.gz", "--vendor",
            "vendor/round80", "--candidate", "solver/iter188/candidate.json", "--direct",
            "solver/iter188/direct/direct_verification.json", "--output", quotient_check])
        assert without(quotient_check, ("wall_seconds",)) == without(
            package / "frontier/iter189_full_invariant_quotient/independent_check.json", ("wall_seconds",))

        traces = temp / "traces.json"
        run("lossless_SAT_trace_streams", [sys.executable,
            "source/check_sat_trace_streams_round106.py", "--root", package, "--output", traces])
        assert traces.read_bytes() == (package / "verification/iter188_sat_trace_stream_check.json").read_bytes()

        proof = temp / "proof.json"
        run("valid_corrupt_truncated_proof_controls", [sys.executable,
            "source/check_proof_controls.py", "--root", package, "--output", proof])
        p = json.loads(proof.read_text())
        assert all(p[key] is True for key in ("valid_drat_accepted", "generated_lrat_accepted",
            "corrupt_drat_rejected", "truncated_drat_rejected", "corrupt_lrat_rejected",
            "truncated_lrat_rejected"))

    manifests = []
    for name in ("PAYLOAD_SHA256SUMS.txt", "SHA256SUMS.txt"):
        if (package / name).exists():
            manifests.append(check_manifest(package, name))
    intervals = sorted((r["started_unix"], r["ended_unix"]) for r in records)
    strict_nonoverlap = all(intervals[i][1] <= intervals[i+1][0] for i in range(len(intervals)-1))
    assert strict_nonoverlap and all(r["reaped"] and not r["detached"] for r in records)
    result = {
        "schema": "circdist-gross-round106-scientific-replay-v1", "status": "PASS",
        "package": str(package), "output": str(output), "python": sys.executable,
        "python_sha256": sha(sys.executable), "clean_environment": clean_env,
        "strict_serial": True, "strict_child_nonoverlap": strict_nonoverlap,
        "children": records, "direct_child_count": len(records), "all_children_reaped": True,
        "detached_processes": 0, "manifests": manifests,
        "checks": [r["name"] for r in records],
        "verdict": "MATERIAL-CHECKED-CONTINUATION-NOT-CLOSED",
        "fresh_frontier": {"iteration": 189, "started": False, "stop": None,
            "quotient_sha256": sha(package / "frontier/iter189_full_invariant_quotient/outer.cnf"),
            "variables": 2460741, "clauses": 11816927},
    }
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps({"status": "PASS", "children": len(records),
                      "all_children_reaped": True, "manifests": len(manifests),
                      "output": str(output)}, sort_keys=True))


if __name__ == "__main__":
    main()
