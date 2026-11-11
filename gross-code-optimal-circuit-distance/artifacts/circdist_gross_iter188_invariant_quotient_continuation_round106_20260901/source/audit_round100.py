#!/usr/bin/env python3
"""Independent cross-check of the Round100 exact SAT campaign and frontier."""
from pathlib import Path
import argparse
import gzip
import hashlib
import json
import math
import sys
import time


def canonical(obj):
    return json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()


def object_sha(obj):
    return hashlib.sha256(canonical(obj)).hexdigest()


def file_sha(path):
    h = hashlib.sha256()
    with Path(path).open("rb") as f:
        for block in iter(lambda: f.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()


def stored(path):
    """Return actual storage path and whether its content is gzip-compressed."""
    path = Path(path)
    if path.exists():
        return path, path.suffix == ".gz"
    gz = path.with_name(path.name + ".gz")
    if gz.exists():
        return gz, True
    raise FileNotFoundError(path)


def open_data(path, text=False):
    actual, compressed = stored(path)
    if compressed:
        return gzip.open(actual, "rt", encoding="utf-8") if text else gzip.open(actual, "rb")
    return actual.open("r", encoding="utf-8") if text else actual.open("rb")


def data_sha(path):
    h = hashlib.sha256()
    with open_data(path) as f:
        for block in iter(lambda: f.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()


def data_bytes(path):
    with open_data(path) as f:
        return f.read()


def load_json(path):
    return json.loads(data_bytes(path))


def parse_assignment(path, variables):
    values = [None] * (variables + 1)
    seen = 0
    with open_data(path, text=True) as f:
        for line in f:
            if not line or line[0] in "cs":
                continue
            fields = line.split()
            if fields and fields[0] == "v":
                fields = fields[1:]
            for token in fields:
                literal = int(token)
                if literal == 0:
                    continue
                var = abs(literal)
                assert 1 <= var <= variables, (path, var, variables)
                value = literal > 0
                assert values[var] is None, (path, "duplicate", var)
                values[var] = value
                seen += 1
    assert seen == variables and all(v is not None for v in values[1:]), (path, seen, variables)
    return values


def verify_cnf(path, assignments):
    """Parse one DIMACS and check every clause under every complete assignment."""
    variables = clauses_expected = None
    clauses_seen = 0
    failures = [0] * len(assignments)
    with open_data(path, text=True) as f:
        for line in f:
            if not line or line.startswith("c"):
                continue
            fields = line.split()
            if fields[0] == "p":
                assert fields[:2] == ["p", "cnf"] and len(fields) == 4
                variables, clauses_expected = map(int, fields[2:])
                continue
            assert variables is not None
            literals = [int(x) for x in fields]
            assert literals and literals[-1] == 0 and 0 not in literals[:-1]
            literals.pop()
            clauses_seen += 1
            for j, assignment in enumerate(assignments):
                if not any(assignment[abs(lit)] == (lit > 0) for lit in literals):
                    failures[j] += 1
    assert clauses_seen == clauses_expected
    assert failures == [0] * len(assignments), (path, failures)
    return variables, clauses_seen


def source_semantic(source):
    source = dict(source)
    recorded = source.pop("semantic_payload_sha256")
    assert object_sha(source) == recorded
    return recorded


def state_semantic(selectors):
    keys = (
        "mechanism_id", "sector", "selected_names", "data_support",
        "group_kinds", "selector_semantic_sha256",
    )
    return object_sha([{k: s.get(k) for k in keys} for s in selectors])


ap = argparse.ArgumentParser()
ap.add_argument("--root", type=Path, required=True)
ap.add_argument("--logs", type=Path)
ap.add_argument("--vendor", type=Path, required=True)
ap.add_argument("--output", type=Path, required=True)
a = ap.parse_args()
R = a.root.resolve()
L = (a.logs or (R / "logs")).resolve()
V = a.vendor.resolve()
t0 = time.time()

sys.path[:0] = [str(V / "src" / "round63_src"), str(V / "src")]
import model
import round68_build as builder

_, _, logical_x, logical_z = builder.load_context()

# The inherited reviewed Round98 frontier must be the commissioned iter172 state.
initial_state_path = R / "state" / "iter172_state.json"
assert file_sha(initial_state_path) == "9fd675be9712a28dd625fba7cce95f75a8a3b9bdf7edc3f398bfa8b13844d2be"
initial = load_json(initial_state_path)
assert initial["next_iteration"] == 172 and initial["started"] is False and initial["stop"] is None
assert initial["selector_count"] == 304
assert initial["selector_state_sha256"] == "a5c64ae41f474844ecd3ac41829331f54d419a81573e4f0e11528db0b49e25d1"
assert len(initial["selectors"]) == 304 and state_semantic(initial["selectors"]) == initial["selector_state_sha256"]

iteration_rows = []
solver_intervals = []
trace_rows = []
for iteration in range(172, 185):
    formula = R / "formulas" / f"iter{iteration}"
    state = load_json(R / "state" / f"iter{iteration}_state.json")
    source_path = formula / "source.json.gz"
    source = load_json(source_path)
    metadata = load_json(formula / "metadata.json")
    encoding = load_json(formula / "encoding_check.json")
    semantic = source_semantic(source)
    selector_count = 304 + 2 * (iteration - 172)
    assert state["selector_count"] == selector_count == len(state["selectors"])
    assert state["next_iteration"] == iteration and state["started"] is False and state["stop"] is None
    assert state_semantic(state["selectors"]) == state["selector_state_sha256"]
    assert source["expected"]["selectors"] == selector_count == len(source["selectors"])
    assert source["expected"]["assertions"] == 18882 + selector_count
    assert metadata["selector_count"] == selector_count
    assert metadata["assertions"] == 18882 + selector_count
    assert metadata["block_family_counts"] == {"unary": 1440, "round62": 20, "generalized": 12820, "dynamic": 204}
    assert sum(metadata["block_family_counts"].values()) == 14484
    assert metadata["source_semantic_payload_sha256"] == semantic == encoding["source_semantic_payload_sha256"]
    assert metadata["source_file_sha256"] == file_sha(source_path)
    assert metadata["cnf_sha256"] == data_sha(formula / "outer.cnf") == encoding["cnf_sha256"]
    assert metadata["assertion_map_sha256"] == data_sha(formula / "assertion_map.jsonl")
    assert metadata["definitions_sha256"] == file_sha(formula / "circuit_trace.json.gz")
    with open_data(formula / "assertion_map.jsonl", text=True) as f:
        assert sum(1 for _ in f) == metadata["assertions"]
    assert encoding["status"] == "PASS"
    assert encoding["all_clause_ids_partitioned_once"] and encoding["all_source_roots_reconstructed"]
    assert encoding["all_variables_primary_or_uniquely_defined"]
    assert encoding["reviewed_blocks"] == 14484 and encoding["efssc_selectors"] == selector_count
    assert encoding["assertions"] == metadata["assertions"]
    assert encoding["variables"] == metadata["variables"] and encoding["clauses"] == metadata["clauses"]
    if iteration == 172:
        assert semantic == "cfa261df8b148622c80248d398df20f1ff5a4cf3f04eb76a31b2795185cc6412"
        assert file_sha(source_path) == "99faca59521b675844d0c10eb12afcfe925f474d3eac9d5cac56e11537397b08"
        assert metadata["cnf_sha256"] == "f86b8db36af1df3877ca1d9dbafb171b6173ddc8b6c2f045a808dd6c71f98342"
        assert (metadata["assertions"], metadata["variables"], metadata["clauses"]) == (19186, 413646, 1406245)
    if iteration == 184:
        continue

    I = R / "iterations" / f"iter{iteration}"
    outer = I / "outer"
    replay = load_json(outer / "replay.json")
    candidate = load_json(outer / "candidate.json")
    independent = load_json(outer / "assignment_independent_check.json")
    assert replay["status"] == "PASS" and replay["solver_status"] == "SATISFIABLE"
    assert replay["all_dimacs_clauses_satisfied"] and replay["complete_assignment_variables"] == metadata["variables"]
    assert replay["dimacs_clauses_checked"] == metadata["clauses"]
    assert replay["efssc_named_frozen_valid_selectors"] == replay["efssc_symbolic_valid_selectors"] == 0
    assert replay["reviewed_block_hits"] == 0
    assert candidate["cnf_sha256"] == metadata["cnf_sha256"]
    assert candidate["source_semantic_payload_sha256"] == semantic
    assert candidate["solver_log_sha256"] == data_sha(outer / "solver.log")
    assert candidate["assignment_sha256"] == data_sha(outer / "assignment.dimacs")
    assert replay["assignment_sha256"] == candidate["assignment_sha256"]
    assert candidate["compressed_schedule_sha256"] == object_sha(candidate["compressed_times"])
    assert candidate["frozen_audit"] == replay["frozen_schedule_audit"]
    assert model.audit_schedule(candidate["compressed_times"], True) == candidate["frozen_audit"]
    assert candidate["frozen_audit"]["ok"] and candidate["frozen_audit"]["global_interleaved"]
    assert candidate["frozen_audit"]["edge_count"] == 864 and candidate["frozen_audit"]["overlaps"] == 648
    assert not candidate["frozen_audit"]["conflicts"] and not candidate["frozen_audit"]["mc_violations"]
    assert independent["status"] == "PASS" and independent["all_dimacs_clauses_satisfied"]
    assert independent["all_variables_assigned_exactly_once"] and independent["formula_sha256"] == metadata["cnf_sha256"]
    assert independent["assignment_sha256"] == data_sha(outer / "assignment.independent.dimacs")
    primary_values = parse_assignment(outer / "assignment.dimacs", metadata["variables"])
    independent_values = parse_assignment(outer / "assignment.independent.dimacs", metadata["variables"])
    assert primary_values == independent_values
    variables, clauses = verify_cnf(formula / "outer.cnf", [primary_values, independent_values])
    assert (variables, clauses) == (metadata["variables"], metadata["clauses"])

    direct_root = I / "direct"
    direct = load_json(direct_root / "direct_verification.json")
    assert direct["candidate_sha256"] == candidate["compressed_schedule_sha256"]
    assert direct["schedule_audit"] == candidate["frozen_audit"]
    assert direct["repair_gate"]["entered"] is False
    sectors = builder.sectors(candidate["compressed_times"], logical_x, logical_z)
    weights = {}
    mechanisms = {}
    for sector in ("Xerr", "Zerr"):
        row = direct["sectors"][sector]
        formula_summary = row["formula_summary"]
        mechanism = row["mechanism"]
        summary = load_json(direct_root / "direct360" / f"{sector}.summary.json")
        assignment_check = load_json(direct_root / "solver" / f"{sector}.assignment_check.json")
        assert row["status"] == "SATISFIABLE" and row["all_dimacs_clauses_satisfied"]
        assert formula_summary["complete_query"] and summary["complete_query"]
        exclusions = ["no pool restriction", "no residual-pattern restriction", "no check-count restriction", "no within-check order family restriction"]
        assert formula_summary["excluded_restrictions"] == exclusions == summary["excluded_restrictions"]
        assert formula_summary["dimacs_sha256"] == data_sha(direct_root / "direct360" / f"{sector}.cnf")
        assert formula_summary["dimacs_sha256"] == summary["dimacs_sha256"]
        assert assignment_check["status"] == "PASS" and assignment_check["all_dimacs_clauses_satisfied"]
        assert assignment_check["all_variables_assigned_exactly_once"]
        assert assignment_check["formula_sha256"] == formula_summary["dimacs_sha256"]
        assert assignment_check["solver_log_sha256"] == data_sha(direct_root / "solver" / f"{sector}.solver.log")
        assert assignment_check["assignment_sha256"] == data_sha(direct_root / "solver" / f"{sector}.assignment.dimacs")
        values = parse_assignment(direct_root / "solver" / f"{sector}.assignment.dimacs", formula_summary["variables"])
        dv, dc = verify_cnf(direct_root / "direct360" / f"{sector}.cnf", [values])
        assert (dv, dc) == (formula_summary["variables"], formula_summary["clauses"])
        exact = model.verify_named_selection(sectors[sector], mechanism["selected_names"], 10)
        assert exact == mechanism["canonical_replay"]
        assert mechanism["fault_count"] == len(mechanism["selected_names"]) == exact["weight"]
        assert 1 <= mechanism["fault_count"] <= 10
        assert exact["ok"] and exact["syndrome"] == [] and exact["nontrivial"]
        assert mechanism["physical_syndrome"] == [] and mechanism["physical_nontrivial"]
        assert mechanism["canonical_physical_parities_equal"]
        assert mechanism["sound_outer_block"]["antecedent_holds_on_source_candidate"]
        assert mechanism["sound_outer_block"]["atom_count"] == len(mechanism["sound_outer_block"]["atoms"])
        weights[sector] = mechanism["fault_count"]
        mechanisms[sector] = object_sha(mechanism)
        trace = load_json(direct_root / "solver" / f"{sector}.sat_trace_summary.json")
        assert trace["iteration"] == iteration and trace["query"] == sector
        assert trace["solver_status"] == "SATISFIABLE" and trace["proof_output_enabled"]
        assert trace["certificate_disposition"] == "not an UNSAT certificate"
        assert trace["empty_clause_lines"] == 0 and not trace["full_trace_retained"] and trace["trace_absent_after_deletion"]
        assert not (direct_root / "solver" / f"{sector}.drat").exists()
        trace_rows.append(trace)

    outer_trace = load_json(outer / "sat_trace_summary.json")
    assert outer_trace["iteration"] == iteration and outer_trace["query"] == "outer"
    assert outer_trace["solver_status"] == "SATISFIABLE" and outer_trace["proof_output_enabled"]
    assert outer_trace["certificate_disposition"] == "not an UNSAT certificate"
    assert outer_trace["empty_clause_lines"] == 0 and not outer_trace["full_trace_retained"] and outer_trace["trace_absent_after_deletion"]
    assert not (outer / "outer.drat").exists()
    trace_rows.append(outer_trace)

    record = load_json(I / "record.json")
    next_state = load_json(R / "state" / f"iter{iteration + 1}_state.json")
    assert record["iteration"] == iteration and record["source_selector_count"] == selector_count
    assert record["source_selector_state_sha256"] == state["selector_state_sha256"]
    assert record["outer_status"] == "SATISFIABLE" and record["repair_entered"] is False
    assert record["new_selectors"] == [f"r100-i{iteration}-Xerr", f"r100-i{iteration}-Zerr"]
    assert record["state_mutated_atomically"] and record["state_after_sha256"] == next_state["selector_state_sha256"]
    assert next_state["parent_selector_count"] == selector_count
    assert next_state["parent_selector_state_sha256"] == state["selector_state_sha256"]
    assert next_state["selector_count"] == selector_count + 2
    assert next_state["round100_completed_candidates"] == iteration - 171
    assert next_state["completed_iterations"][-1] == iteration and next_state["iterations"][-1] == record
    assert next_state["atomicity"]["both_direct_replays_before_commit"]
    assert next_state["atomicity"]["later_cuts_retroactive"] is False
    for j, sector in enumerate(("Xerr", "Zerr")):
        selector = next_state["selectors"][-2 + j]
        mechanism = direct["sectors"][sector]["mechanism"]
        assert selector["mechanism_id"] == f"r100-i{iteration}-{sector}"
        assert selector["sector"] == sector and selector["selected_names"] == mechanism["selected_names"]
        assert selector["fault_count"] == weights[sector]
        assert selector["source_schedule_sha256"] == candidate["compressed_schedule_sha256"]
        assert selector["source_times"] == candidate["compressed_times"]
        assert selector["canonical_support"] == mechanism["canonical_replay"]["net_support"]
        assert selector["physical_support"] == mechanism["physical_net_support"]
        assert selector["source_atoms"] == mechanism["sound_outer_block"]["atoms"]
        selector_semantic = {k: selector.get(k) for k in ("sector", "selected_names", "data_support", "group_kinds")}
        assert object_sha(selector_semantic) == selector["selector_semantic_sha256"]
    transition = load_json(R / "transitions" / f"iter{iteration}_to{iteration + 1}" / "atomic_commit.json")
    pending = load_json(R / "transitions" / f"iter{iteration}_to{iteration + 1}" / "pending_intent.json")
    assert pending["status"] == "PENDING" and transition["status"] == "COMMITTED"
    assert transition["state_promoted_last"] and transition["all_outputs_present"]
    payload = transition["payload"]
    assert payload["selector_count"] == next_state["selector_count"]
    assert payload["selector_state_sha256"] == next_state["selector_state_sha256"]
    assert payload["state_file_sha256"] == file_sha(R / "state" / f"iter{iteration + 1}_state.json")
    assert payload["record_file_sha256"] == file_sha(I / "record.json")
    assert payload["source_file_sha256"] == file_sha(R / "formulas" / f"iter{iteration + 1}" / "source.json.gz")
    assert payload["cnf_sha256"] == data_sha(R / "formulas" / f"iter{iteration + 1}" / "outer.cnf")

    iteration_rows.append({
        "iteration": iteration,
        "source_selector_count": selector_count,
        "outer": {
            "status": "SATISFIABLE", "variables": metadata["variables"],
            "clauses": metadata["clauses"], "assertions": metadata["assertions"],
            "cnf_sha256": metadata["cnf_sha256"],
            "source_semantic_sha256": semantic,
            "schedule_sha256": candidate["compressed_schedule_sha256"],
            "complete_assignment": True,
            "solver_wall_seconds": load_json(L / "process" / f"outer_iter{iteration}_cadical_proof.json")["wall_seconds"],
        },
        "direct": {
            sector: {
                "status": "SATISFIABLE", "weight": weights[sector],
                "canonical_support_weight": direct["sectors"][sector]["mechanism"]["canonical_replay"]["net_weight"],
                "physical_support_weight": direct["sectors"][sector]["mechanism"]["physical_net_weight"],
                "physical_detector_syndrome": direct["sectors"][sector]["mechanism"]["physical_syndrome"],
                "physical_logical_action": direct["sectors"][sector]["mechanism"]["physical_logical_parities"],
                "canonical_physical_parities_equal": direct["sectors"][sector]["mechanism"]["canonical_physical_parities_equal"],
                "mechanism_semantic_sha256": mechanisms[sector],
                "formula_sha256": direct["sectors"][sector]["formula_summary"]["dimacs_sha256"],
                "complete_assignment": True, "physical_replay": True,
                "solver_wall_seconds": load_json(L / "process" / f"direct_iter{iteration}_{sector}_cadical_proof.json")["wall_seconds"],
            } for sector in ("Xerr", "Zerr")
        },
        "transition": {
            "new_selectors": record["new_selectors"],
            "next_selector_count": next_state["selector_count"],
            "next_selector_state_sha256": next_state["selector_state_sha256"],
            "atomic": True,
        },
    })

# Fresh frontier is compiled/checked but deliberately has no solve disposition or iteration directory.
final_state = load_json(R / "state" / "iter184_state.json")
final_meta = load_json(R / "formulas" / "iter184" / "metadata.json")
final_source = load_json(R / "formulas" / "iter184" / "source.json.gz")
assert final_state["selector_count"] == 328 and final_state["round100_completed_candidates"] == 12
assert final_state["selector_state_sha256"] == "7296aa70690e01852519b78826b173af35998cec0e9c124c46ea30101dd0777d"
assert file_sha(R / "state/iter184_state.json") == "3b128ef192074a3bc0c163502e97eff99ab9d15c546381e98e1e178471552d7b"
assert final_state["next_iteration"] == 184 and final_state["started"] is False and final_state["stop"] is None
assert not (R / "iterations/iter184").exists()
assert not list((R / "pending").glob("*")) if (R / "pending").exists() else True
assert final_meta["selector_count"] == 328 and final_meta["assertions"] == 19210
assert final_meta["variables"] == 415793 and final_meta["clauses"] == 1416404
assert final_meta["cnf_sha256"] == "2b0030fd15b0ef8154e2dbc37508e03481f11d8c876c4fe59e6541cb3bfacd62"
assert source_semantic(final_source) == "d601f297e8b2a1b7d6179d19452da8b0abca2e4f16d7404b6395a8254e949268"
assert file_sha(R / "formulas/iter184/source.json.gz") == "5eb1607bebea7bfc44b693a4a3a9ae19f2ab5ae498407290863b34d6eb9b66b0"

# Exact six-distinct same-sector MITM theorem and independent physical-model replay.
order6 = load_json(R / "synthesis/order6/order6_exact_validation.json")
assert order6["status"] == "PASS" and order6["retained_term_count"] == 0
assert order6["full_domain_size"] == math.comb(125, 6) + math.comb(109, 6) == 6715648864
assert order6["small_n_bijection_controls"] == {str(n): math.comb(n, 6) for n in range(6, 13)}
for sector, count in (("Xerr", 125), ("Zerr", 109)):
    summary = load_json(R / f"synthesis/order6/{sector}.order6.summary.json")
    checked = order6["sector_results"][sector]
    assert summary["status"] == "PASS" and summary["selector_count"] == count
    assert summary["triple_count_enumerated"] == summary["triple_count_expected"] == math.comb(count, 3)
    assert summary["full_six_distinct_domain_closed_form"] == checked["full_domain"] == math.comb(count, 6)
    assert summary["canonical_syndrome_zero_six_tuples"] == checked["canonical_syndrome_zero"] == 0
    assert summary["combined_syndrome_zero_six_tuples"] == checked["combined_syndrome_zero"] == 0
    assert summary["eligible_named_weight_1_to_10_occurrences"] == checked["eligible_occurrences"] == 0
    assert summary["unique_conservative_source_valid_results"] == checked["conservative_valid_occurrences"] == 0
    assert sum(summary["combined_zero_named_weight_histogram"]) == 0
    assert summary["equality_semantics"].startswith("std::array lexicographic")

# Stronger complete-span theorem: two proof-producing CNFs plus direct Z3 semantics.
span = load_json(R / "synthesis/span/span_exact_validation.json")
assert span["status"] == "PASS" and span["z3_version"] == "5.1.0"
assert span["gate_truth_table_cases"] == 8 and span["cardinality_recurrence_cases"] == 544766
for sector, count in (("Xerr", 125), ("Zerr", 109)):
    row = span["sector_results"][sector]
    certificate = load_json(R / f"synthesis/span/{sector}.unsat_certificate/certificate.json")
    metadata = load_json(R / f"synthesis/span/{sector}.metadata.json")
    assert row["status"] == row["z3_direct_semantics"] == "UNSAT"
    assert row["row_count"] == count and row["existing_full_named_masks_blocked"] == count
    assert row["cnf_sha256"] == metadata["cnf_sha256"] == certificate["formula_sha256"]
    assert row["drat_sha256"] == certificate["drat_sha256"]
    assert row["lrat_sha256"] == certificate["lrat_sha256"]
    assert certificate["status"] == "PASS" and certificate["valid_drat_accepted"]
    assert certificate["generated_lrat_accepted"] and certificate["all_children_reaped"]
    assert certificate["corrupt_drat_rejected"] and certificate["truncated_drat_rejected"]
    assert certificate["corrupt_lrat_rejected"] and certificate["truncated_lrat_rejected"]
    assert len(certificate["processes"]) == 6 and all(p["reaped"] and not p["detached"] for p in certificate["processes"])

# Process records and strict serialization, including the two checked synthesis UNSAT solvers.
process_records = []
for path in sorted((L / "process").glob("*.json")):
    # The science census was closed before packaging.  Later compression,
    # replay, and this audit's own wrapper records are audited separately in
    # PROCESS_LEDGER.json and must not change the immutable 204-row census.
    if path.name == "independent_campaign_audit.json" or path.name.startswith("round100_"):
        continue
    row = load_json(path)
    assert row["timed_out"] is False and row["final_status"] == "exited_and_reaped"
    assert row["returncode"] in (0, 1, 10, 20)
    assert row["reaped"] is True and row["detached"] is False
    process_records.append((path.name, row))
assert len(process_records) == 204
assert sum(row["returncode"] == 10 for _, row in process_records) == 36
assert sum(row["returncode"] == 20 for _, row in process_records) == 2
rejected = [(name, row["returncode"]) for name, row in process_records if row["returncode"] not in (0, 10, 20)]
assert rejected == [("span_independent_validation.json", 1)]
all_solver_intervals = []
for name, row in process_records:
    if "cadical_proof" in name and row["returncode"] in (10, 20):
        all_solver_intervals.append((row["started_unix"], row["ended_unix"], name, row["returncode"]))
all_solver_intervals.sort()
assert len(all_solver_intervals) == 38
for left, right in zip(all_solver_intervals, all_solver_intervals[1:]):
    assert left[1] <= right[0], (left, right)
drivers = [load_json(path) for path in sorted((R / "campaign").glob("driver_process_*.json"))]
assert len(drivers) == 2 and sum(row["child_wrapper_processes_started_serially"] for row in drivers) == 192
assert all(row["status"] == "SAT_PREFIX_COMPLETE" and row["detached_processes"] == 0 for row in drivers)

assert len(iteration_rows) == 12 and len(trace_rows) == 36
assert all(1 <= row["direct"][sector]["weight"] <= 10 for row in iteration_rows for sector in ("Xerr", "Zerr"))
fresh_frontier = {
    "next_iteration": 184,
    "started": False,
    "selector_count": 328,
    "selector_state_sha256": final_state["selector_state_sha256"],
    "state_file_sha256": file_sha(R / "state/iter184_state.json"),
    "source_file_sha256": file_sha(R / "formulas/iter184/source.json.gz"),
    "source_semantic_sha256": source_semantic(final_source),
    "assertions": final_meta["assertions"],
    "variables": final_meta["variables"],
    "clauses": final_meta["clauses"],
    "cnf_sha256": final_meta["cnf_sha256"],
}
out = {
    "schema": "circdist-gross-round100-independent-campaign-audit-v1",
    "status": "PASS",
    "scientific_verdict": "MATERIAL-CHECKED-PROGRESS-NOT-CLOSED",
    "root_status": "CONJECTURED",
    "route_status": "CONJECTURED",
    "D_star_Gross": [11, 12],
    "completed_candidate_count": 12,
    "strict_serial": True,
    "outer_sat_count": 12,
    "direct_sat_count": 24,
    "outer_direct_unsat_count": 0,
    "synthesis_unsat_count": 2,
    "unknown_count": 0,
    "timeout_count": 0,
    "repair_entered": False,
    "iterations": iteration_rows,
    "sat_trace_summaries": {"count": 36, "all_empty_clause_lines_zero": True,
                            "all_full_traces_deleted_as_noncertificates": True},
    "synthesis": {
        "order6_full_domain_size": 6715648864,
        "order6_exact_reduced_candidates": 0,
        "order6_retained_terms": 0,
        "full_span_sector_unsat_proofs": 2,
        "full_span_independent_z3_unsat": 2,
        "scope": "reviewed post-iteration-136 schedule and 125/109 selector bases only",
    },
    "fresh_frontier": fresh_frontier,
    "processes": {"record_count": 204, "science_solver_children": 36,
                  "synthesis_solver_children": 2, "all_reaped": True,
                  "survivors": 0, "timeouts": 0, "rejected_attempts": rejected},
    "limitations": [
        "No outer or direct query returned UNSAT; there is no Gross universal schedule absence certificate.",
        "The order-6 and full-span theorems cover only their declared reviewed schedule and bases.",
        "The span theorem quotients existing masks and excludes no arbitrary mechanism outside the reviewed spans.",
        "A positive direct mechanism kills only its concrete source outer candidate.",
        "Mixed-sector reduction adds no new direct-sector closure but does not globalize either same-sector theorem.",
        "The frozen root and gap-via-lift route remain conjectured; D*_Gross remains {11,12}.",
    ],
    "seconds": round(time.time() - t0, 6),
}
a.output.parent.mkdir(parents=True, exist_ok=True)
a.output.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n")
print(json.dumps({"status": "PASS", "iterations": 12, "outer_sat": 12,
                  "direct_sat": 24, "order6_domain": 6715648864,
                  "span_unsat": 2, "frontier": fresh_frontier,
                  "seconds": out["seconds"]}, sort_keys=True))
