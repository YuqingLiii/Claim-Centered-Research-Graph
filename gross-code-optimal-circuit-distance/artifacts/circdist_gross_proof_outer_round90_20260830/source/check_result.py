#!/usr/bin/env python3
"""Cross-check RESULT.json against every sealed Round90 evidence object."""
from pathlib import Path
import argparse
import gzip
import hashlib
import json


def sha_bytes(data):
    return hashlib.sha256(data).hexdigest()


def sha_file(path):
    digest = hashlib.sha256()
    with Path(path).open("rb") as handle:
        for chunk in iter(lambda: handle.read(1 << 20), b""):
            digest.update(chunk)
    return digest.hexdigest()


def canonical_sha(obj):
    return sha_bytes(json.dumps(obj, sort_keys=True, separators=(",", ":")).encode())


def load(path):
    path = Path(path)
    raw = path.read_bytes()
    return json.loads(gzip.decompress(raw) if path.suffix == ".gz" else raw)


parser = argparse.ArgumentParser()
parser.add_argument("--root", type=Path, required=True)
args = parser.parse_args()
root = args.root.resolve()
result = json.loads((root / "RESULT.json").read_text())

assert result["status"] == "PASS"
assert result["verdict"] == "MATERIAL-CHECKED-PROGRESS-NOT-CLOSED"
assert result["completed_candidate_count"] == 12
assert result["all_outer_dispositions"] == "SATISFIABLE"
assert result["all_direct_dispositions"] == "SATISFIABLE"
assert result["repair_entered"] is False
assert result["canonical_edits"] is False
assert result["commit"] is False and result["push"] is False
assert len(result["iterations"]) == 12

trace_data = json.loads((root / "data/sat_drat_trace_disposition.json").read_text())
assert trace_data["status"] == "PASS" and trace_data["trace_count"] == 36
trace_rows = {
    (row["iteration"], row["query"]): row for row in trace_data["traces"]
}
assert len(trace_rows) == 36

for expected_iteration, row in zip(range(112, 124), result["iterations"]):
    assert row["iteration"] == expected_iteration
    formula = root / f"formulas/iter{expected_iteration}"
    evidence = root / f"iterations/iter{expected_iteration}"
    metadata = json.loads((formula / "metadata.json").read_text())
    source = load(formula / "source.json.gz")
    semantic = dict(source)
    recorded_semantic = semantic.pop("semantic_payload_sha256")
    assert canonical_sha(semantic) == recorded_semantic
    assert recorded_semantic == row["source_semantic_payload_sha256"]
    assert metadata["selector_count"] == row["source_selector_count"]

    outer = row["outer"]
    assert outer["status"] == "SATISFIABLE"
    assert outer["solver_returncode"] == 10
    assert outer["all_dimacs_clauses_satisfied"] is True
    for key in ("assertions", "variables", "clauses", "cnf_sha256"):
        assert outer[key] == metadata[key]
    cnf = gzip.decompress((formula / "outer.cnf.gz").read_bytes())
    assert sha_bytes(cnf) == outer["cnf_sha256"]
    assignment = gzip.decompress((evidence / "outer/assignment.dimacs.gz").read_bytes())
    assert sha_bytes(assignment) == outer["assignment_sha256"]
    assert sha_file(evidence / "outer/solver.log") == outer["solver_log_sha256"]
    assert sha_file(evidence / "outer/candidate.json") == outer["candidate_file_sha256"]
    assert sha_file(evidence / "outer/replay.json") == outer["outer_replay_file_sha256"]
    candidate = json.loads((evidence / "outer/candidate.json").read_text())
    assert candidate["cnf_sha256"] == outer["cnf_sha256"]
    assert candidate["compressed_schedule_sha256"] == outer["compressed_schedule_sha256"]
    assert candidate["frozen_audit"] == outer["schedule_audit"]
    assert candidate["frozen_audit"]["edge_count"] == 864
    assert candidate["frozen_audit"]["overlaps"] == 648
    assert candidate["frozen_audit"]["ok"] is True
    assert candidate["frozen_audit"]["global_interleaved"] is True

    record = json.loads((evidence / "record.json").read_text())
    assert sha_file(evidence / "record.json") == row["record_file_sha256"]
    assert record["outer_status"] == "SATISFIABLE"
    assert record["candidate_schedule_sha256"] == outer["compressed_schedule_sha256"]
    assert record["state_after_sha256"] == row["state_after_sha256"]
    assert record["state_mutated_atomically"] is True
    assert record["repair_entered"] is False
    assert record["new_selectors"] == row["new_selectors"]
    assert len(row["new_selectors"]) == 2

    verification_path = evidence / "direct/direct_verification.json"
    verification = json.loads(verification_path.read_text())
    assert sha_file(verification_path) == row["direct_verification_file_sha256"]
    assert verification["candidate_sha256"] == outer["compressed_schedule_sha256"]
    assert verification["repair_gate"]["entered"] is False
    for label in ("Xerr", "Zerr"):
        direct = row["direct"][label]
        sealed = verification["sectors"][label]
        summary = json.loads(
            (evidence / f"direct/direct360/{label}.summary.json").read_text()
        )
        assert direct["status"] == sealed["status"] == "SATISFIABLE"
        assert direct["solver_returncode"] == 10
        assert direct["all_dimacs_clauses_satisfied"] is True
        assert direct["complete_query"] is True
        assert sealed["all_dimacs_clauses_satisfied"] is True
        assert summary["complete_query"] is True
        assert summary["excluded_restrictions"] == [
            "no pool restriction",
            "no residual-pattern restriction",
            "no check-count restriction",
            "no within-check order family restriction",
        ]
        assert summary["variables"] == direct["variables"]
        assert summary["clauses"] == direct["clauses"]
        assert summary["dimacs_sha256"] == direct["dimacs_sha256"]
        assert sha_file(evidence / f"direct/direct360/{label}.cnf") == direct["dimacs_sha256"]
        assert sha_file(evidence / f"direct/solver/{label}.solver.log") == direct["solver_log_sha256"]
        mechanism = sealed["mechanism"]
        assert mechanism["fault_count"] == direct["fault_count"]
        assert 1 <= mechanism["fault_count"] <= 10
        assert mechanism["physical_syndrome"] == []
        assert mechanism["physical_nontrivial"] is True
        assert mechanism["canonical_physical_parities_equal"] is True
        assert canonical_sha(mechanism) == direct["mechanism_semantic_sha256"]
        trace = trace_rows[(expected_iteration, label)]
        assert trace["formula_sha256"] == direct["dimacs_sha256"]
        assert trace["sha256"] == direct["sat_drat_trace_sha256"]
        assert trace["bytes"] == direct["sat_drat_trace_bytes"]
        assert trace["empty_clause_lines"] == direct["sat_drat_empty_clause_lines"] == 0
    trace = trace_rows[(expected_iteration, "outer")]
    assert trace["formula_sha256"] == outer["cnf_sha256"]
    assert trace["sha256"] == outer["sat_drat_trace_sha256"]
    assert trace["bytes"] == outer["sat_drat_trace_bytes"]
    assert trace["empty_clause_lines"] == outer["sat_drat_empty_clause_lines"] == 0

fresh = result["fresh_state"]
assert fresh["next_iteration"] == 124 and fresh["started"] is False
assert fresh["selector_count"] == 164 and fresh["new_round90_selectors"] == 24
assert fresh["selector_state_sha256"] == "854c2b50a07fa955356932311eb3229a164e16f125e5b2991c6c2916d5fce2c3"
fresh_formula = root / "formulas/iter124"
fresh_metadata = json.loads((fresh_formula / "metadata.json").read_text())
for key in ("assertions", "variables", "clauses", "cnf_sha256"):
    assert fresh[key] == fresh_metadata[key]
assert sha_file(fresh_formula / "source.json.gz") == fresh["source_file_sha256"]
assert sha_file(fresh_formula / "encoding_check.json") == fresh["encoding_check_file_sha256"]
assert sha_file(root / "continuation/final_state.json") == fresh["state_file_sha256"]
assert not (root / "iterations/iter124").exists()
assert result["proof_objects"]["gross_unsat_drat"] is None
assert result["proof_objects"]["gross_unsat_lrat"] is None
assert result["proof_objects"]["direct_unsat_proofs"] == []
assert all(row["empty_clause_lines"] == 0 for row in trace_data["traces"])
print("RESULT_CROSSCHECK_PASS", len(result["iterations"]), len(trace_data["traces"]))
