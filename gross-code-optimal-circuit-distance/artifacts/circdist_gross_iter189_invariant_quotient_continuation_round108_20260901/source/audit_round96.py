#!/usr/bin/env python3
"""Independent cross-check of the Round96 exact SAT campaign and frontier."""
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

# The reviewed Round95 frontier must be the commissioned iter148 state.
initial_state_path = R / "state" / "iter148_state.json"
assert file_sha(initial_state_path) == "1902599acc47eb5d354692759b2d09d6ff1cfcd5e013f2b907cc310376ee6e81"
initial = load_json(initial_state_path)
assert initial["next_iteration"] == 148 and initial["started"] is False and initial["stop"] is None
assert initial["selector_count"] == 256
assert initial["selector_state_sha256"] == "9337b0fe78a3f8af54cec263422fe1641b64094d861c87959a82e1dffe6f326f"
assert len(initial["selectors"]) == 256 and state_semantic(initial["selectors"]) == initial["selector_state_sha256"]

iteration_rows = []
solver_intervals = []
trace_rows = []
for iteration in range(148, 161):
    formula = R / "formulas" / f"iter{iteration}"
    state = load_json(R / "state" / f"iter{iteration}_state.json")
    source_path = formula / "source.json.gz"
    source = load_json(source_path)
    metadata = load_json(formula / "metadata.json")
    encoding = load_json(formula / "encoding_check.json")
    semantic = source_semantic(source)
    selector_count = 256 + 2 * (iteration - 148)
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
    if iteration == 148:
        assert semantic == "2fd4a1982e1f6389804f7eee1120706f9d26c9e6a23acc05e2a15e036a67c032"
        assert file_sha(source_path) == "0db20ed8ca0b120cda91eb7a94be25094adb9b77a2cacdd322e330a720d58b5f"
        assert metadata["cnf_sha256"] == "397c12b15859a62bbe4bacbcb43dd8680a93e3bcf0cdee62fea4687d2431c8e4"
        assert (metadata["assertions"], metadata["variables"], metadata["clauses"]) == (19138, 409157, 1385059)
    if iteration == 160:
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
    assert record["new_selectors"] == [f"r96-i{iteration}-Xerr", f"r96-i{iteration}-Zerr"]
    assert record["state_mutated_atomically"] and record["state_after_sha256"] == next_state["selector_state_sha256"]
    assert next_state["parent_selector_count"] == selector_count
    assert next_state["parent_selector_state_sha256"] == state["selector_state_sha256"]
    assert next_state["selector_count"] == selector_count + 2
    assert next_state["round96_completed_candidates"] == iteration - 147
    assert next_state["completed_iterations"][-1] == iteration and next_state["iterations"][-1] == record
    assert next_state["atomicity"]["both_direct_replays_before_commit"]
    assert next_state["atomicity"]["later_cuts_retroactive"] is False
    for j, sector in enumerate(("Xerr", "Zerr")):
        selector = next_state["selectors"][-2 + j]
        mechanism = direct["sectors"][sector]["mechanism"]
        assert selector["mechanism_id"] == f"r96-i{iteration}-{sector}"
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
final_state = load_json(R / "state" / "iter160_state.json")
final_meta = load_json(R / "formulas" / "iter160" / "metadata.json")
final_source = load_json(R / "formulas" / "iter160" / "source.json.gz")
assert final_state["selector_count"] == 280 and final_state["round96_completed_candidates"] == 12
assert final_state["selector_state_sha256"] == "ad3cf364dd9224c14ffb55046ba3dc8eb80035b1eaf997f1d7a5691297ad62a3"
assert final_state["next_iteration"] == 160 and final_state["started"] is False and final_state["stop"] is None
assert not (R / "iterations" / "iter160").exists()
assert not list((R / "pending").glob("*")) if (R / "pending").exists() else True
assert final_meta["selector_count"] == 280 and final_meta["assertions"] == 19162
assert final_meta["variables"] == 411526 and final_meta["clauses"] == 1396722
assert final_meta["cnf_sha256"] == "aa18d2857ed5a7aefacd33bf4fbd42fded914393e123a87f00e84e4920e39d59"
assert source_semantic(final_source) == "bb19e724c66eb6f3df8830a205ba29a297f5795d42d3fe066fa3b873800789ed"
assert file_sha(R / "formulas" / "iter160" / "source.json.gz") == "8b754b649744a83eae6c80e64230f9782909b48e5613dcfd6c3c321d98b2dd66"

# New exact synthesis domain: all 4-subsets in each same-sector frontier,
# with exact canonical MITM coverage and no novel retained term.
synthesis = load_json(R / "synthesis" / "order4_gf2_closure.json")
domain = synthesis["finite_domain"]
assert synthesis["status"] == "PASS"
assert domain["selector_count"] == 234 and domain["sector_counts"] == {"Xerr": 125, "Zerr": 109}
assert domain["unordered_distinct_quadruples_expected"] == domain["unordered_distinct_quadruples_enumerated"]
assert domain["unordered_distinct_quadruples_expected"] == math.comb(125, 4) + math.comb(109, 4) == 15254626
x4, z4 = synthesis["sector_results"]["Xerr"], synthesis["sector_results"]["Zerr"]
assert x4["unordered_distinct_quadruples_enumerated"] == math.comb(125, 4) == 9691375
assert z4["unordered_distinct_quadruples_enumerated"] == math.comb(109, 4) == 5563251
assert x4["eligible_weight_1_to_10_with_multiplicity"] == x4["unique_eligible_named_results"] == 32456
assert z4["eligible_weight_1_to_10_with_multiplicity"] == z4["unique_eligible_named_results"] == 1304
assert x4["maximum_result_multiplicity"] == z4["maximum_result_multiplicity"] == 1
assert x4["canonical_syndrome_zero_results"] == x4["physical_syndrome_zero_results"] == 0
assert z4["canonical_syndrome_zero_results"] == z4["physical_syndrome_zero_results"] == 1
assert x4["unique_existing_predicate_results"] == 0
assert z4["unique_existing_predicate_results"] == 106
assert x4["unique_novel_eligible_results"] == 32456 and z4["unique_novel_eligible_results"] == 1198
assert synthesis["retained_term_count"] == len(synthesis["retained_terms"]) == 0
assert x4["unique_novel_conservative_source_valid_retained"] == 0
assert z4["unique_novel_conservative_source_valid_retained"] == 0
assert all(row["zero_location_results"] == row["zero_canonical_support_results"] == row["zero_physical_support_results"] == 0 for row in (x4, z4))
assert synthesis["audits"]["schedule_globalization"]["source_verification"]["ok"]
assert not synthesis["audits"]["schedule_globalization"]["iteration136_verification"]["ok"]
sw = synthesis["audits"]["support_weight_substitution"]
assert sw["named_location_weight"] != sw["canonical_support_weight"] != sw["physical_support_weight"]

# Process records: the two disclosed, corrected failures are the only nonzero non-SAT records.
process_records = []
for path in sorted((L / "process").glob("*.json")):
    row = load_json(path)
    assert row["timed_out"] is False and row["final_status"] == "exited_and_reaped"
    assert row["returncode"] in (0, 1, 10)
    process_records.append((path.name, row))
assert len(process_records) >= 200
assert sum(row["returncode"] == 10 for _, row in process_records) == 36
failures = [(name, row["returncode"]) for name, row in process_records if row["returncode"] not in (0, 10)]
assert failures == [
    ("order4_exact_synthesis.json", 1),
    ("order4_exact_synthesis_repair1.json", 1),
]

# Strict serialization is checked on all solver child intervals.
for name, row in process_records:
    if row["returncode"] == 10 and "cadical_proof" in name:
        solver_intervals.append((row["started_unix"], row["ended_unix"], name))
solver_intervals.sort()
assert len(solver_intervals) == 36
for left, right in zip(solver_intervals, solver_intervals[1:]):
    assert left[1] <= right[0], (left, right)

assert len(iteration_rows) == 12 and len(trace_rows) == 36
assert all(row["direct"]["Xerr"]["weight"] == 10 for row in iteration_rows)
assert [row["direct"]["Zerr"]["weight"] for row in iteration_rows].count(9) == 2
assert [row["iteration"] for row in iteration_rows if row["direct"]["Zerr"]["weight"] == 9] == [148, 152]
assert all(row["direct"]["Zerr"]["weight"] == 10 for row in iteration_rows if row["iteration"] not in (148, 152))

out = {
    "schema": "circdist-gross-round96-independent-campaign-audit-v1",
    "status": "PASS",
    "scientific_verdict": "MATERIAL-CHECKED-PROGRESS-NOT-CLOSED",
    "root_status": "CONJECTURED",
    "route_status": "CONJECTURED",
    "D_star_Gross": [11, 12],
    "completed_candidate_count": 12,
    "strict_serial": True,
    "outer_sat_count": 12,
    "direct_sat_count": 24,
    "unsat_count": 0,
    "unknown_count": 0,
    "timeout_count": 0,
    "repair_entered": False,
    "iterations": iteration_rows,
    "sat_trace_summaries": {
        "count": len(trace_rows), "all_empty_clause_lines_zero": True,
        "all_full_traces_deleted_as_noncertificates": True,
    },
    "synthesis": {
        "finite_domain_size": 15254626,
        "eligible_results_with_multiplicity": 33760,
        "unique_novel_eligible_results": 33654,
        "retained_terms": 0, "coverage_checked": True,
    },
    "fresh_frontier": {
        "next_iteration": 160, "started": False, "selector_count": 280,
        "selector_state_sha256": final_state["selector_state_sha256"],
        "state_file_sha256": file_sha(R / "state" / "iter160_state.json"),
        "source_file_sha256": file_sha(R / "formulas" / "iter160" / "source.json.gz"),
        "source_semantic_sha256": source_semantic(final_source),
        "assertions": final_meta["assertions"], "variables": final_meta["variables"],
        "clauses": final_meta["clauses"], "cnf_sha256": final_meta["cnf_sha256"],
    },
    "processes": {
        "record_count": len(process_records), "science_solver_children": 36,
        "all_reaped": True, "survivors": 0, "timeouts": 0,
        "disclosed_corrected_failures": failures,
    },
    "limitations": [
        "No outer or direct query returned UNSAT; there is no Gross absence certificate.",
        "The order-4 same-sector GF(2) investigation covers only its declared finite domain.",
        "A positive mechanism kills only the concrete source outer candidate.",
        "The frozen root and gap-via-lift route remain conjectured; D*_Gross remains {11,12}.",
    ],
    "seconds": round(time.time() - t0, 6),
}
a.output.parent.mkdir(parents=True, exist_ok=True)
a.output.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n")
print(json.dumps({
    "status": "PASS", "iterations": 12, "outer_sat": 12, "direct_sat": 24,
    "traces": 36, "frontier": out["fresh_frontier"], "seconds": out["seconds"],
}, sort_keys=True))
