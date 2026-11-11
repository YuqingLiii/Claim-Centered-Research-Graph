#!/usr/bin/env python3
"""Cross-check the public Round102 verdict against retained machine evidence."""
from pathlib import Path
import argparse
import json


parser = argparse.ArgumentParser()
parser.add_argument("--root", type=Path, required=True)
parser.add_argument("--output", type=Path, required=True)
args = parser.parse_args()
root = args.root.resolve()


def load(relative):
    return json.loads((root / relative).read_text())


result = load("RESULT.json")
assert result["verdict"] == "MATERIAL-CHECKED-GLOBAL-PROGRESS-NOT-CLOSED"
assert result["root_branches"] == {
    "A_legal_schedule_distance_12": False,
    "B_all_legal_schedules_distance_at_most_11": False,
}
assert result["distance_status"] == {
    "D_star_Gross": [11, 12],
    "CIRCDIST.gross": "CONJECTURED",
    "gap-via-lift": "CONJECTURED",
}
assert result["canonical_state_modified"] is False
assert result["repair_entered"] is False

bindings = load("INPUT_BINDINGS.json")
assert bindings["iteration184"] == {
    "clauses": 1416404,
    "cnf_sha256": "2b0030fd15b0ef8154e2dbc37508e03481f11d8c876c4fe59e6541cb3bfacd62",
    "reviewed_order_predicates": 14484,
    "selector_count": 328,
    "selector_state_sha256": "7296aa70690e01852519b78826b173af35998cec0e9c124c46ea30101dd0777d",
    "source_assertions": 19210,
    "source_file_sha256": "5eb1607bebea7bfc44b693a4a3a9ae19f2ab5ae498407290863b34d6eb9b66b0",
    "source_semantic_sha256": "d601f297e8b2a1b7d6179d19452da8b0abca2e4f16d7404b6395a8254e949268",
    "state_file_sha256": "3b128ef192074a3bc0c163502e97eff99ab9d15c546381e98e1e178471552d7b",
    "variables": 415793,
}
i184 = load("iterations/iter184/record.json")
assert i184["outer_status"] == "SATISFIABLE"
assert all(i184["direct"][sector]["status"] == "SATISFIABLE"
           for sector in ("Xerr", "Zerr"))
assert i184["new_cuts_installed"] == 2 and i184["repair_entered"] is False

closure = load("frontier/iter186_full_invariant/independent_closure_check.json")
assert closure["status"] == "PASS"
assert closure["blocks"]["unique_semantics"] == 517140
assert closure["selectors"]["unique_semantics"] == 23868
assert closure["blocks"]["exact_expected_observed_set_equality"]
assert closure["selectors"]["exact_expected_observed_set_equality"]

quotient = load("frontier/iter186_full_invariant_quotient/metadata.json")
assert quotient["cnf_sha256"] == result["global_coverage"]["corrected_quotient_cnf_sha256"]
assert (quotient["variables"], quotient["clauses"]) == (2447800, 11774686)
outer_replay = load("frontier/iter186_full_invariant_quotient/replay.json")
assert outer_replay["status"] == "PASS" and outer_replay["solver_status"] == "SATISFIABLE"
assert outer_replay["all_dimacs_clauses_satisfied"]
direct = load("frontier/iter186_full_invariant_quotient/direct/adjudicated/direct_verification.json")
assert all(direct["sectors"][sector]["all_dimacs_clauses_satisfied"]
           and direct["sectors"][sector]["mechanism"]["physical_syndrome"] == []
           and direct["sectors"][sector]["mechanism"]["physical_nontrivial"]
           for sector in ("Xerr", "Zerr"))
disposition = load("frontier/iter186_full_invariant_quotient/direct/DISPOSITION.json")
assert all(disposition["sectors"][sector]["disposition"] == "SATISFIABLE"
           for sector in ("Xerr", "Zerr"))
assert disposition["both_direct_independently_proof_checked_unsat"] is False

fresh = load("frontier/iter187_full_invariant/state.json")
assert fresh["status"] == "PASS" and fresh["next_iteration"] == 187
assert fresh["started"] is False and fresh["stop"] is None
assert fresh["block_count"] == 517140 and fresh["selector_count"] == 24012
assert fresh["source_file_sha256"] == result["fresh_frontier"]["source_file_sha256"]
fresh_encoding = load("frontier/iter187_full_invariant/formula/encoding_check.json")
fresh_quotient = load("frontier/iter187_full_invariant_quotient/independent_check.json")
assert fresh_encoding["status"] == fresh_quotient["status"] == "PASS"
assert fresh_encoding["cnf_sha256"] == result["fresh_frontier"]["base_cnf"]["sha256"]
assert fresh_quotient["quotient_cnf_sha256"] == result["fresh_frontier"]["lex_quotient_cnf"]["sha256"]

replay = load("verification/preseal_replay.json")
gates = load("verification/repository_validators/summary.json")
evidence = load("verification/evidence_closure_interpretation.json")
process = load("verification/process_ledger.json")
survivor = load("verification/final_survivor_scan.json")
scratch = load("verification/scratch_cleanup.json")
assert replay["status"] == "PASS" and replay["direct_child_count"] == 13
assert replay["all_children_reaped"] and replay["detached_processes"] == 0
assert gates["status"] == evidence["status"] == process["status"] == "PASS"
assert evidence["raw_exit_code"] == 1 and evidence["all_errors_under_new_package"]
assert process["strict_solver_nonoverlap"] and process["solver_interval_count"] == 11
assert survivor["science_survivor_count"] == 0
assert scratch["scratch_survivor_count"] == 0
assert scratch["raw_large_stream_survivor_count"] == 0

assert not list((root / "frontier/iter186_full_invariant_quotient").rglob("*.drat"))
assert sum(line.startswith("| F") for line in (root / "FAILURE_LEDGER.md").read_text().splitlines()) == 13
for relative in ("REPORT.md", "GLOBAL_TRANSLATION_THEOREM.md",
                 "ITERATION184_DISPOSITION.md", "PROPOSED_CANONICAL_DELTA.md"):
    text = (root / relative).read_text()
    assert text.strip() and "PENDING_FINAL_RERUN" not in text and "TODO" not in text
assert "PENDING_FINAL_RERUN" not in (root / "RESULT.json").read_text()

out = {
    "schema": "circdist-gross-round102-result-check-v1",
    "status": "PASS",
    "verdict": result["verdict"],
    "root_branches_proved": 0,
    "D_star_Gross": [11, 12],
    "iteration184": "outer SAT; Xerr SAT; Zerr SAT; two selectors installed",
    "corrected_quotient": "SAT; Xerr SAT; Zerr SAT",
    "fresh_iteration": 187,
    "fresh_started": False,
    "process_records_indexed": process["retained_process_records"],
    "solver_intervals": process["solver_interval_count"],
}
args.output.parent.mkdir(parents=True, exist_ok=True)
args.output.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n")
print(json.dumps(out, sort_keys=True))
