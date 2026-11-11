#!/usr/bin/env python3
"""Strict-serial, read-only scientific replay of the Round102 package.

Generated comparison files live in a temporary directory.  Only the final
summary is written under the package, before the package is sealed.
"""
from pathlib import Path
import argparse
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


def cleaned(path, volatile=()):
    value = json.loads(Path(path).read_text())
    for key in volatile:
        value.pop(key, None)
    return value


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    package = args.root.resolve()
    repository = package.parents[2]
    records = []

    def run(name, command, timeout=14400):
        command = [str(value) for value in command]
        started = time.time()
        started_utc = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime(started))
        child = subprocess.Popen(command, cwd=package, env=os.environ.copy(),
                                 stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                 text=True, start_new_session=False)
        timed_out = False
        term_sent = False
        kill_sent = False
        try:
            stdout, stderr = child.communicate(timeout=timeout)
        except subprocess.TimeoutExpired:
            timed_out = True
            term_sent = True
            child.terminate()
            try:
                stdout, stderr = child.communicate(timeout=15)
            except subprocess.TimeoutExpired:
                kill_sent = True
                child.kill()
                stdout, stderr = child.communicate()
        ended = time.time()
        row = {
            "name": name, "command": command, "parent_pid": os.getpid(),
            "child_pid": child.pid, "started_unix": started, "ended_unix": ended,
            "started_utc": started_utc,
            "ended_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime(ended)),
            "wall_seconds": round(ended - started, 6),
            "returncode": child.returncode, "stdout": stdout, "stderr": stderr,
            "timed_out": timed_out, "term_sent": term_sent, "kill_sent": kill_sent,
            "reaped": True, "detached": False,
        }
        records.append(row)
        assert not timed_out and child.returncode == 0, (name, child.returncode,
                                                         stdout[-2000:], stderr[-2000:])

    with tempfile.TemporaryDirectory(prefix="circdist-round102-replay.") as temporary:
        temp = Path(temporary)
        live = temp / "live.json"
        run("live_governance", [sys.executable, "source/check_live_governance_round102.py",
            "--repository", repository, "--package", package, "--output", live])
        assert cleaned(live) == cleaned(package / "verification/live_governance_check.json")

        closure = temp / "closure.json"
        run("full_translation_closure", [sys.executable,
            "source/check_full_translation_closure_round102.py",
            "--input-source", "frontier/iter186_orbit_base/source.json.gz",
            "--closure-source", "frontier/iter186_full_invariant/source.json.gz",
            "--plan", "frontier/iter186_full_invariant/closure_plan.json",
            "--audit", "frontier/iter186_full_invariant/closure_audit.json",
            "--action-check", "global/iter185_translation_quotient/independent_check.json",
            "--encoding-check", "frontier/iter186_full_invariant/formula/encoding_check.json",
            "--output", closure])
        assert cleaned(closure) == cleaned(
            package / "frontier/iter186_full_invariant/independent_closure_check.json")

        fresh_source = temp / "iter187.source.json.gz"
        fresh_state = temp / "iter187.state.json"
        fresh_audit = temp / "iter187.orbit_audit.json"
        run("fresh_iter187_orbit_frontier", [sys.executable,
            "source/advance_full_invariant_frontier_round102.py",
            "--source", "frontier/iter186_full_invariant/source.json.gz",
            "--state", "frontier/iter186_full_invariant/state.json",
            "--candidate", "frontier/iter186_full_invariant_quotient/candidate.json",
            "--direct", "frontier/iter186_full_invariant_quotient/direct/adjudicated/direct_verification.json",
            "--vendor", "vendor/round80",
            "--output-source", fresh_source, "--output-state", fresh_state,
            "--output-audit", fresh_audit])
        assert fresh_source.read_bytes() == (package /
            "frontier/iter187_full_invariant/source.json.gz").read_bytes()
        assert fresh_state.read_bytes() == (package /
            "frontier/iter187_full_invariant/state.json").read_bytes()
        assert fresh_audit.read_bytes() == (package /
            "frontier/iter187_full_invariant/orbit_audit.json").read_bytes()

        fresh_encoding = temp / "iter187.encoding_check.json"
        run("fresh_iter187_encoding", [sys.executable, "source/check_outer_encoding.py",
            "--source", "frontier/iter187_full_invariant/source.json.gz",
            "--cnf", "frontier/iter187_full_invariant/formula/outer.cnf",
            "--metadata", "frontier/iter187_full_invariant/formula/metadata.json",
            "--assertion-map", "frontier/iter187_full_invariant/formula/assertion_map.jsonl",
            "--definitions", "frontier/iter187_full_invariant/formula/definitions.json.gz",
            "--output", fresh_encoding])
        assert cleaned(fresh_encoding, ("seconds",)) == cleaned(package /
            "frontier/iter187_full_invariant/formula/encoding_check.json", ("seconds",))

        quotient = temp / "quotient.json"
        run("corrected_translation_quotient", [sys.executable,
            "source/check_translation_quotient_round102.py",
            "--base-cnf", "frontier/iter186_full_invariant/formula/outer.cnf",
            "--base-metadata", "frontier/iter186_full_invariant/formula/metadata.json",
            "--source", "frontier/iter186_full_invariant/source.json.gz",
            "--quotient-cnf", "frontier/iter186_full_invariant_quotient/outer.cnf",
            "--quotient-metadata", "frontier/iter186_full_invariant_quotient/metadata.json",
            "--roots", "frontier/iter186_full_invariant_quotient/translation_roots.jsonl",
            "--trace", "frontier/iter186_full_invariant_quotient/translation_trace.json.gz",
            "--vendor", "vendor/round80",
            "--candidate", "global/iter185_translation_quotient/candidate.json",
            "--direct", "global/iter185_translation_quotient/direct/direct_verification.json",
            "--output", quotient])
        assert cleaned(quotient, ("wall_seconds",)) == cleaned(
            package / "frontier/iter186_full_invariant_quotient/independent_check.json",
            ("wall_seconds",))

        fresh_quotient = temp / "iter187.quotient_check.json"
        run("fresh_iter187_translation_quotient", [sys.executable,
            "source/check_translation_quotient_round102.py",
            "--base-cnf", "frontier/iter187_full_invariant/formula/outer.cnf",
            "--base-metadata", "frontier/iter187_full_invariant/formula/metadata.json",
            "--source", "frontier/iter187_full_invariant/source.json.gz",
            "--quotient-cnf", "frontier/iter187_full_invariant_quotient/outer.cnf",
            "--quotient-metadata", "frontier/iter187_full_invariant_quotient/metadata.json",
            "--roots", "frontier/iter187_full_invariant_quotient/translation_roots.jsonl",
            "--trace", "frontier/iter187_full_invariant_quotient/translation_trace.json.gz",
            "--vendor", "vendor/round80",
            "--candidate", "global/iter185_translation_quotient/candidate.json",
            "--direct", "global/iter185_translation_quotient/direct/direct_verification.json",
            "--output", fresh_quotient])
        assert cleaned(fresh_quotient, ("wall_seconds",)) == cleaned(package /
            "frontier/iter187_full_invariant_quotient/independent_check.json",
            ("wall_seconds",))

        orbit_controls = temp / "orbit_controls.json"
        run("corrected_sat_orbit_controls", [sys.executable,
            "source/check_sat_orbit_controls_round102.py",
            "--cnf", "frontier/iter186_full_invariant_quotient/outer.cnf",
            "--metadata", "frontier/iter186_full_invariant_quotient/metadata.json",
            "--source", "frontier/iter186_full_invariant/source.json.gz",
            "--assignment", "frontier/iter186_full_invariant_quotient/assignment.dimacs",
            "--candidate", "frontier/iter186_full_invariant_quotient/candidate.json",
            "--trace", "frontier/iter186_full_invariant_quotient/translation_trace.json.gz",
            "--output", orbit_controls])
        stored_controls = package / "controls/full_invariant_sat_orbit_controls.json"
        assert cleaned(orbit_controls) == cleaned(stored_controls)

        assignment = temp / "assignment.dimacs"
        assignment_check = temp / "assignment_check.json"
        run("corrected_assignment", [sys.executable,
            "source/extract_and_check_assignment.py",
            "--cnf", "frontier/iter186_full_invariant_quotient/outer.cnf",
            "--solver-log", "frontier/iter186_full_invariant_quotient/solver.log",
            "--assignment", assignment, "--output", assignment_check])
        assert assignment.read_bytes() == (package /
            "frontier/iter186_full_invariant_quotient/assignment.independent.dimacs").read_bytes()
        assert cleaned(assignment_check) == cleaned(package /
            "frontier/iter186_full_invariant_quotient/assignment_independent_check.json")

        candidate = temp / "candidate.json"
        replay = temp / "replay.json"
        run("corrected_outer_sat_replay", [sys.executable,
            "source/verify_outer_sat_model.py",
            "--solver-log", "frontier/iter186_full_invariant_quotient/solver.log",
            "--cnf", "frontier/iter186_full_invariant_quotient/outer.cnf",
            "--source", "frontier/iter186_full_invariant/source.json.gz",
            "--metadata", "frontier/iter186_full_invariant_quotient/metadata.json",
            "--frozen", "vendor/round80", "--assignment", assignment,
            "--candidate", candidate, "--output", replay])
        assert candidate.read_bytes() == (package /
            "frontier/iter186_full_invariant_quotient/candidate.json").read_bytes()
        assert cleaned(replay, ("seconds",)) == cleaned(package /
            "frontier/iter186_full_invariant_quotient/replay.json", ("seconds",))

        for label, root_path in (
            ("iteration184", "iterations/iter184/direct"),
            ("exploratory_quotient", "global/iter185_translation_quotient/direct"),
            ("corrected_quotient", "frontier/iter186_full_invariant_quotient/direct/adjudicated"),
        ):
            direct = temp / f"{label}_direct.json"
            run(f"{label}_direct_physical_replay", [sys.executable,
                "vendor/round80/src/replay_direct_candidate.py",
                "--root", root_path, "--output", direct])
            assert cleaned(direct) == cleaned(package / root_path / "direct_verification.json")

        proof = temp / "proof_controls.json"
        run("proof_controls", [sys.executable, "source/check_proof_controls.py",
                               "--root", package, "--output", proof])
        assert json.loads(proof.read_text())["status"] == "PASS"

    summary = {
        "schema": "circdist-gross-round102-preseal-replay-v1",
        "status": "PASS",
        "root": str(package), "repository": str(repository),
        "python": sys.executable, "python_sha256": sha(sys.executable),
        "children": records, "direct_child_count": len(records),
        "all_children_reaped": True, "detached_processes": 0,
        "strict_serial": True,
        "checks": [row["name"] for row in records],
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n")
    print(json.dumps({"status": "PASS", "children": len(records),
                      "all_children_reaped": True}, sort_keys=True))


if __name__ == "__main__":
    main()
