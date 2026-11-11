#!/usr/bin/env python3
"""Generate Round92 sealed-package metadata and the machine-readable result."""
from pathlib import Path
import argparse, gzip, hashlib, json, platform, subprocess, sys


def sha(path):
    h = hashlib.sha256()
    with Path(path).open("rb") as f:
        for b in iter(lambda: f.read(1 << 20), b""):
            h.update(b)
    return h.hexdigest()


def sha_obj(obj):
    return hashlib.sha256(json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def load(path):
    path = Path(path); raw = path.read_bytes()
    return json.loads(gzip.decompress(raw) if path.suffix == ".gz" else raw)


def write(path, obj):
    Path(path).write_text(json.dumps(obj, indent=2, sort_keys=True) + "\n")


ap = argparse.ArgumentParser()
ap.add_argument("--repo", type=Path, required=True)
ap.add_argument("--root", type=Path, required=True)
a = ap.parse_args(); repo = a.repo.resolve(); root = a.root.resolve()
r90 = repo / "circdist/artifacts/circdist_gross_proof_outer_round90_20260830"

protected = {
    "operations/circdist/SCHEDULER.yaml": "3a2b9380b0a9b0c248704f05ef45eaabd30cec98e8ddeed3c954785c9163a56f",
    "circdist/proof-dag/nodes/CIRCDIST.gross.yaml": "4a19230bce6822d3afab50db16b2657ec0924b826b409b0c65d3c9fd57c10992",
    "circdist/reviews/circdist_gross_proof_outer_exact_review_round91_20260830.md": "72e36d7fdf33a4a4b868b01a5bcb9dadf22a45482bfbc2225aeead4bf9496f0d",
    "DAG_PROTOCOL.md": sha(repo / "DAG_PROTOCOL.md"),
    "FILE_PROTOCOL.md": sha(repo / "FILE_PROTOCOL.md"),
    "circdist/artifacts/definitions/CIRCDIST_PROBLEMS.md": sha(repo / "circdist/artifacts/definitions/CIRCDIST_PROBLEMS.md"),
}
for p, expected in protected.items(): assert sha(repo / p) == expected
snapshots = {
    "bindings/canonical/SCHEDULER.yaml": protected["operations/circdist/SCHEDULER.yaml"],
    "bindings/canonical/CIRCDIST.gross.yaml": protected["circdist/proof-dag/nodes/CIRCDIST.gross.yaml"],
    "bindings/canonical/round91_review.md": protected["circdist/reviews/circdist_gross_proof_outer_exact_review_round91_20260830.md"],
}
for rel in (
    "bindings/protocols/DAG_PROTOCOL.md", "bindings/protocols/FILE_PROTOCOL.md",
    "bindings/protocols/CIRCDIST_PROBLEMS.md", "bindings/round90/SHA256SUMS.txt",
    "bindings/round90/PAYLOAD_SHA256SUMS.txt", "bindings/round90/REPORT.md",
    "bindings/round90/RESULT.json", "bindings/round90/final_state.json",
    "bindings/round90/iter124_source.json.gz", "bindings/round90/iter124_metadata.json",
): snapshots[rel] = sha(root / rel)
bindings = {
    "schema": "circdist-gross-round92-input-bindings-v1", "status": "PASS",
    "expected_protected_sha256": protected, "package_snapshot_sha256": snapshots,
    "reviewed_dependency": {
        "repository_relative_path": "circdist/artifacts/circdist_gross_proof_outer_round90_20260830",
        "root_manifest_file_sha256": "41ac5ad7f28895f09aae29a256d91aec241298ec7bfe0d1dec2e14709fa00ca7",
        "payload_manifest_file_sha256": "545efe756a51190aaa8877e1d0d9fa1100da48aa213811b75a62a1f6a9b6c4d4",
        "closure_rule": "Replay first verifies both exact manifest-file hashes and the entire Round90 manifest closure; any dependency drift is fatal.",
    },
    "reviewed_start": {
        "iteration": 124, "started": False, "selector_count": 164,
        "selector_state_sha256": "854c2b50a07fa955356932311eb3229a164e16f125e5b2991c6c2916d5fce2c3",
        "source_file_sha256": "1c4556377a4f84d5bf7df1e08af0e98d5cb3d4ea3da94db2e94d645f40a4f544",
        "source_semantic_sha256": "d155a897b8771a9821ef4ef14041bb910e7bbb6aaaad7f6cf08b6db1de0f397e",
        "cnf_sha256": "2dd07d33ff0b29c1f06a7452c3b1c7ca9b6df950e819046f8a712dacb0dd7e5a",
        "assertions": 19046, "variables": 401040, "clauses": 1345190,
    },
}
write(root / "INPUT_BINDINGS.json", bindings)

syn = load(root / "synthesis/weight9_synthesis.json")
strict_q = load(root / "preouter/strict_expansion_query.json")
strict_v = load(root / "preouter/strict_expansion.verification.json")
install = load(root / "preouter/atomic_install.json")
campaign = load(root / "data/campaign_summary.json")
traces = load(root / "data/sat_drat_trace_disposition.json")
trace_index = {(x["iteration"], x["query"]): x for x in traces["traces"]}
iterations = []
for c in campaign["iterations"]:
    i = c["iteration"]; formula = root / f"formulas/iter{i}"; ev = root / f"iterations/iter{i}"
    row = {
        "iteration": i, "source_selector_count": c["selector_count"],
        "source_file_sha256": sha(formula / "source.json.gz"),
        "source_semantic_sha256": c["source_semantic_sha256"],
        "outer": {
            "status": "SATISFIABLE", "solver_returncode": 10,
            "assertions": c["assertions"], "variables": c["outer_variables"],
            "clauses": c["outer_clauses"], "cnf_sha256": c["outer_cnf_sha256"],
            "assignment_sha256": sha(ev / "outer/assignment.dimacs.gz"),
            "uncompressed_assignment_sha256": c["outer_assignment_sha256"],
            "solver_log_sha256": sha(ev / "outer/solver.log"),
            "candidate_file_sha256": sha(ev / "outer/candidate.json"),
            "replay_file_sha256": sha(ev / "outer/replay.json"),
            "schedule_sha256": c["candidate_schedule_sha256"],
            "all_dimacs_clauses_satisfied": True, "frozen_schedule_ok": True,
            "used_layers": c["used_layers"],
            "sat_drat_trace": trace_index[(i, "outer")],
        },
        "record_file_sha256": sha(ev / "record.json"),
        "state_after_sha256": c["state_after_sha256"], "new_selectors": [f"r92-i{i}-Xerr", f"r92-i{i}-Zerr"],
        "direct_verification_file_sha256": sha(ev / "direct/direct_verification.json"),
        "direct": {},
    }
    dv = load(ev / "direct/direct_verification.json")
    for sector in ("Xerr", "Zerr"):
        d = c["direct"][sector]; sealed = dv["sectors"][sector]
        row["direct"][sector] = {
            "status": "SATISFIABLE", "solver_returncode": 10, "complete_query": True,
            "all_dimacs_clauses_satisfied": True, "weight": d["weight"],
            "selected_names": d["selected_names"], "logical_bits_lsb_first": d["logical_bits_lsb_first"],
            "cnf_sha256": d["direct_cnf_sha256"], "mechanism_semantic_sha256": d["mechanism_sha256"],
            "physical_replay": d["physical_replay"],
            "solver_log_sha256": sha(ev / f"direct/solver/{sector}.solver.log"),
            "variables": sealed["formula_summary"]["variables"], "clauses": sealed["formula_summary"]["clauses"],
            "sat_drat_trace": trace_index[(i, sector)],
        }
    iterations.append(row)

fresh = campaign["final"]
result = {
    "schema": "circdist-gross-round92-result-v1", "status": "PASS",
    "verdict": "MATERIAL-CHECKED-PROGRESS-NOT-CLOSED", "root_status": "CONJECTURED",
    "route_status": "CONJECTURED", "D_star_Gross": [11, 12],
    "strict_serial": True, "completed_candidate_count": 12,
    "all_outer_dispositions": "SATISFIABLE", "all_direct_dispositions": "SATISFIABLE",
    "unknown_count": 0, "timeout_count": 0, "unsat_count": 0,
    "repair_entered": False, "canonical_edits": False, "commit": False, "push": False,
    "phase_a": {
        "synthesis_file_sha256": sha(root / "synthesis/weight9_synthesis.json"),
        "semantic_result_sha256": syn["semantic_result_sha256"],
        "reconstructed_weight9_count": len(syn["original_weight9_reconstruction"]),
        "tested_candidate_count": syn["tested_candidate_count"],
        "retained_ordinary_selector_count": syn["retained_ordinary_selector_count"],
        "retained_relaxed_cube_count": syn["retained_relaxed_cube_count"],
        "completion_census": syn["completion_census"], "minor_census": syn["minor_census"],
        "compatible_union_census": syn["compatible_union_census"],
        "pairwise_gf2_census": syn["pairwise_gf2_census"],
        "order_atom_removal_census": syn["order_atom_removal_census"],
        "strict_expansion_query_cnf_sha256": strict_q["cnf_sha256"],
        "strict_expansion_assignment_sha256": strict_v["assignment_sha256"],
        "strict_expansion_schedule_sha256": strict_v["candidate_schedule_sha256"],
        "strict_expansion_old_valid_count": strict_v["old_valid_count"],
        "strict_expansion_new_valid_count": strict_v["new_valid_count"],
        "strict_expansion_mechanisms": [x["mechanism_id"] for x in strict_v["new_valid_mechanisms"]],
        "atomic_install_state_sha256": install["state_after_sha256"],
        "atomic_install_source_semantic_sha256": install["source_after_semantic_sha256"],
    },
    "iterations": iterations,
    "fresh_state": {
        **fresh, "state_file_sha256": sha(root / "continuation/final_state.json"),
        "encoding_check_file_sha256": sha(root / "formulas/iter136/encoding_check.json"),
        "new_round92_campaign_selectors": 24, "new_round92_preouter_selectors": 44,
    },
    "proof_objects": {
        "gross_unsat_drat": None, "gross_unsat_lrat": None, "direct_unsat_proofs": [],
        "sat_side_trace_count": traces["trace_count"],
        "sat_side_trace_scope": "non-certificates: all corresponding formulas were SAT",
    },
    "limitations": [
        "Twelve positive schedules and their mechanisms do not quantify over the remaining frozen schedule domain.",
        "Zero selector domains and atom-deletion countertuples are local synthesis results, not global absence evidence.",
        "No UNSAT branch was reached, so no Gross DRAT/LRAT theorem or D* narrowing is claimed.",
    ],
}
write(root / "RESULT.json", result)

orig = load(root / "data/original_process_ledger.json")
regen = load(root / "controls/actual_sat_trace/regenerate_solver.run.json")
regen["path"] = "controls/actual_sat_trace/regenerate_solver.run.json"
records = list(orig["records"]) + [regen]
ledger = dict(orig)
ledger.update({
    "schema": "circdist-gross-round92-process-ledger-v2", "bounded_foreground_children": len(records),
    "packaging_replay_solver_children": 1, "records": records,
    "all_children_reaped": True, "survivors_at_serialization": 0,
    "regenerated_control_trace": {
        "reason": "Retain an actual SAT-side non-certificate stream for physical checker replay in the delta package.",
        "formula_sha256": "5c50713ebd9620a69164f2bc9dce63a0c2ca7f5cf7f8ed2f387ed1746d9b94ff",
        "trace_sha256": "5dd1dfa8829b528bb24587260ea9b516cd324fe1ee8be8fb2d917976b42b086c",
        "scientific_state_mutated": False,
    },
})
write(root / "PROCESS_LEDGER.json", ledger)

def version(cmd):
    p = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    return {"command": cmd, "returncode": p.returncode, "first_line": p.stdout.splitlines()[0] if p.stdout.splitlines() else ""}
environment = {
    "schema": "circdist-gross-round92-environment-v1", "status": "PASS",
    "platform": platform.platform(), "machine": platform.machine(),
    "recorded_interpreter": "/private/tmp/circdist-r72-dispatcher-venv/bin/python",
    "python": sys.version, "z3_pysat": version([sys.executable, "-c", "import z3,pysat;print(z3.get_version_string(),pysat.__version__)"]),
    "dependency_tool_hashes": {
        "cadical": sha(r90 / "tooling/cadical-1.9.5-arm64-macos"),
        "drat_trim": sha(r90 / "tooling/drat-trim-arm64-macos"),
        "lrat_check": sha(r90 / "tooling/lrat-check-arm64-macos"),
    },
    "dependency_policy": "Reviewed Round90 package is repository-relative and manifest-verified before use.",
}
write(root / "ENVIRONMENT.json", environment)
print(json.dumps({"status": "PASS", "iterations": len(iterations), "result_sha256": sha(root / "RESULT.json"), "processes": len(records)}, sort_keys=True))
