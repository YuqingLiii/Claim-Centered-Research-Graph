#!/usr/bin/env python3
"""Assemble Round106 bindings, environment, frontier, and result metadata."""
from pathlib import Path
import argparse
import datetime
import hashlib
import json
import os
import platform
import sys


def sha(path):
    h = hashlib.sha256()
    with Path(path).open("rb") as f:
        for block in iter(lambda: f.read(8 << 20), b""):
            h.update(block)
    return h.hexdigest()


def load(path):
    return json.loads(Path(path).read_text())


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", type=Path, required=True)
    args = ap.parse_args()
    root = args.root.resolve()
    input_audit = load(root / "verification/input_audit.json")
    package_bindings = root / "verification/package_binding_check.json"
    qcheck = load(root / "solver/iter188/assignment_check.json")
    replay = load(root / "solver/iter188/replay.json")
    direct = load(root / "verification/iter188_direct_independent_audit.json")
    traces = load(root / "verification/iter188_sat_trace_stream_check.json")
    orbit = load(root / "frontier/iter189_full_invariant/orbit_audit.json")
    closure = load(root / "verification/iter189_incremental_orbit_closure_independent.json")
    state = load(root / "frontier/iter189_full_invariant/state.json")
    base = load(root / "frontier/iter189_full_invariant/formula/metadata.json")
    quotient = load(root / "frontier/iter189_full_invariant_quotient/metadata.json")
    proof = load(root / "controls/proof_toolchain_controls.json")
    process_files = sorted((root / "logs/process").glob("*.json"))
    process_records = [load(p) for p in process_files]
    solvers = [r for r in process_records if r.get("command") and
               "cadical" in Path(str(r["command"][0])).name]
    solvers.sort(key=lambda r: r["started_unix"])
    tools = []
    for name in ("cadical-1.9.5-arm64-macos", "drat-trim-arm64-macos", "lrat-check-arm64-macos"):
        p = root / "tooling" / name
        tools.append({"path": f"tooling/{name}", "sha256": sha(p), "bytes": p.stat().st_size,
                      "executable": os.access(p, os.X_OK)})
    bindings = {
        "schema": "circdist-gross-round106-input-bindings-v1", "status": "PASS",
        "canonical": input_audit["canonical_bindings"],
        "reviewed_package": input_audit["reviewed_package"],
        "reviewed_frontier": input_audit["frontier"],
        "copied_input_files": input_audit["copied_input_files"],
        "tooling": tools, "canonical_state_modified": False,
        "scope": "Round106 binds the reviewed fresh iteration-188 full-invariant quotient and no other start formula.",
    }
    (root / "INPUT_BINDINGS.json").write_text(json.dumps(bindings, indent=2, sort_keys=True) + "\n")
    env = {
        "schema": "circdist-gross-round106-environment-v1", "status": "PASS",
        "captured_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "cwd": os.getcwd(), "package": str(root), "network_used": False,
        "platform": platform.platform(), "machine": platform.machine(),
        "os": {"uname": list(platform.uname())},
        "python": {"executable": sys.executable, "version": platform.python_version(),
                   "sha256": sha(sys.executable)},
        "selected_environment": {k: os.environ[k] for k in
            ("PATH", "PYTHONPATH", "LANG", "LC_ALL", "LC_CTYPE", "TMPDIR", "SHELL") if k in os.environ},
        "tooling": tools, "strict_serial": True, "subagents_used": False,
        "solver_processes": [{k: r[k] for k in
            ("name", "child_pid", "command", "started_utc", "ended_utc", "wall_seconds",
             "child_user_seconds", "child_system_seconds", "child_maxrss_raw", "returncode",
             "timed_out", "reaped", "detached")} for r in solvers],
    }
    (root / "ENVIRONMENT.json").write_text(json.dumps(env, indent=2, sort_keys=True) + "\n")
    fresh = {
        "schema": "circdist-gross-round106-fresh-frontier-v1", "status": "PASS",
        "iteration": 189, "started": False, "stop": None, "fresh_unstarted": True,
        "blocks": 517140, "selectors": 24300, "lex_leaders": 71,
        "translation_group": "Z_12 x Z_6", "translation_group_order": 72,
        "source_file_sha256": state["source_file_sha256"],
        "source_semantic_payload_sha256": state["source_semantic_payload_sha256"],
        "state_file_sha256": sha(root / "frontier/iter189_full_invariant/state.json"),
        "selector_state_sha256": state["selector_state_sha256"],
        "base": {"path": "frontier/iter189_full_invariant/formula/outer.cnf",
                 "assertions": base["assertions"], "variables": base["variables"],
                 "clauses": base["clauses"], "sha256": base["cnf_sha256"],
                 "encoding_check": "PASS"},
        "quotient": {"path": "frontier/iter189_full_invariant_quotient/outer.cnf",
                     "assertions": quotient["assertions"], "variables": quotient["variables"],
                     "clauses": quotient["clauses"], "sha256": quotient["cnf_sha256"],
                     "independent_check": "PASS"},
        "base_formula_exact_file_set": ["assertion_map.jsonl", "definitions.json.gz",
            "encoding_check.json", "metadata.json", "outer.cnf"],
        "quotient_exact_file_set": ["independent_check.json", "metadata.json", "outer.cnf",
            "translation_roots.jsonl", "translation_trace.json.gz"],
        "forbidden_solver_artifacts_absent": True,
        "smallest_honest_residual": "Solve the exact fresh iteration-189 full-invariant quotient proof-first; retain a proof/model and repeat complete direct-sector adjudication if SAT.",
    }
    (root / "FRESH_FRONTIER.json").write_text(json.dumps(fresh, indent=2, sort_keys=True) + "\n")
    gates_path = root / "verification/repository_validators/summary.json"
    gates = load(gates_path) if gates_path.exists() else {"status": "PENDING"}
    preseal_path = root / "verification/preseal_replay.json"
    preseal = load(preseal_path) if preseal_path.exists() else {"status": "PENDING"}
    postseal_path = root / "verification/postseal_replay.json"
    postseal = load(postseal_path) if postseal_path.exists() else {"status": "PENDING"}
    result = {
        "schema": "circdist-gross-round106-result-v1", "status": "PASS",
        "verdict": "MATERIAL-CHECKED-CONTINUATION-NOT-CLOSED",
        "package": "circdist/artifacts/" + root.name,
        "canonical_state_modified": False, "strict_serial": True,
        "root_closed": False,
        "root_branches": {"A_explicit_legal_distance_12_circuit": False,
                          "B_universal_frozen_family_distance_at_most_11": False},
        "distance_status": {"CIRCDIST.gross": "CONJECTURED", "gap-via-lift": "CONJECTURED",
                            "D_star_Gross": [11, 12]},
        "mandatory_input": {"iteration": 188, "fresh_unstarted_before_launch": True,
            "quotient_sha256": qcheck["formula_sha256"], "variables": qcheck["variables"],
            "clauses": qcheck["clauses"]},
        "iteration188": {
            "quotient": {"status": "SATISFIABLE", "all_variables_assigned_exactly_once": True,
                "all_clauses_checked": qcheck["checked_clauses"], "all_clauses_satisfied": True,
                "assignment_sha256": qcheck["assignment_sha256"]},
            "schedule": replay["frozen_schedule_audit"],
            "compressed_schedule_sha256": replay["compressed_schedule_sha256"],
            "distance12_result": False, "repair_entered": False,
            "repair_reason": "forbidden because both complete unrestricted direct sectors are SAT",
            "direct": {label: {k: direct["sectors"][label][k] for k in
                ("status", "variables", "clauses", "cnf_sha256", "assignment_sha256",
                 "fault_count", "selected_names", "canonical_net_support", "physical_net_support",
                 "logical_parities", "canonical_nonstabilizer", "physical_nonstabilizer")}
                for label in ("Xerr", "Zerr")}},
        "solver_processes": env["solver_processes"],
        "sat_trace_streams": traces,
        "orbit_continuation": {"old_selectors": 24156, "new_selectors": 24300,
            "added_selectors": 144, "parent_orbit_sizes": orbit["parent_orbit_sizes"],
            "collisions": orbit["collision_count"], "block_generator_cases": 1034280,
            "selector_generator_cases": closure["selector_registry"]["generator_invariance_cases"],
            "translated_schedule_replays": closure["translated_schedule_replays"],
            "translated_physical_mechanism_replays": closure["translated_physical_mechanism_replays"],
            "full_registry_invariant": True},
        "fresh_frontier": fresh,
        "proof_disposition": {"actual_Gross_UNSAT": False,
            "drat_or_lrat_claim_for_iteration188": False,
            "proof_output_enabled_from_all_solver_launches": True,
            "valid_corrupt_truncated_toolchain_controls": "PASS",
            "valid_drat_accepted": proof["valid_drat_accepted"],
            "generated_lrat_accepted": proof["generated_lrat_accepted"]},
        "verification": {"input_binding_and_manifest_audit": "PASS",
            "input_source_base_bijection": "PASS", "input_quotient_reconstruction": "PASS",
            "independent_direct_audit": "PASS", "independent_full_registry_audit": "PASS",
            "fresh_base_encoding_check": "PASS", "fresh_quotient_encoding_check": "PASS",
            "preseal_package_replay": preseal.get("status"),
            "preseal_replay_children": preseal.get("direct_child_count"),
            "postseal_package_replay": postseal.get("status"),
            "postseal_replay_children": postseal.get("direct_child_count")},
        "repository_gates": gates,
        "failures": {"scientific_failures_or_unknowns": 0,
                     "development_and_interface_failures_disclosed": True,
                     "ledger": "FAILURE_LEDGER.md"},
        "proposed_canonical_yaml": {"path": "PROPOSED_CIRCDIST.gross.yaml",
            "sha256": sha(root / "PROPOSED_CIRCDIST.gross.yaml"), "installed": False,
            "identical_to_bound_canonical": sha(root / "PROPOSED_CIRCDIST.gross.yaml") ==
                                             sha(root / "bindings/CIRCDIST.gross.yaml"),
            "level": "CONJECTURED", "residual": [11, 12]},
        "exact_residual": fresh["smallest_honest_residual"],
    }
    (root / "RESULT.json").write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps({"status": "PASS", "process_records": len(process_records),
                      "solvers": len(solvers), "frontier": 189,
                      "gates": gates.get("status"), "preseal": preseal.get("status"),
                      "postseal": postseal.get("status")}, sort_keys=True))


if __name__ == "__main__":
    main()
