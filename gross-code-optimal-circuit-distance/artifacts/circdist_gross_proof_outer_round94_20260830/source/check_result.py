#!/usr/bin/env python3
"""Cross-check RESULT.json against sealed Round94 evidence."""
from pathlib import Path
import argparse
import gzip
import hashlib
import json


def sha_file(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def actual(path):
    path = Path(path)
    if path.exists():
        return path, path.suffix == ".gz"
    gz = path.with_name(path.name + ".gz")
    assert gz.exists(), path
    return gz, True


def data_sha(path):
    path, compressed = actual(path)
    data = gzip.decompress(path.read_bytes()) if compressed else path.read_bytes()
    return hashlib.sha256(data).hexdigest()


def load(path):
    path = Path(path)
    data = path.read_bytes()
    return json.loads(gzip.decompress(data) if path.suffix == ".gz" else data)


def object_sha(obj):
    return hashlib.sha256(json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


ap = argparse.ArgumentParser()
ap.add_argument("--root", type=Path, required=True)
a = ap.parse_args()
R = a.root.resolve()
x = load(R / "RESULT.json")
audit = load(R / "verification/independent_campaign_audit.json")
assert x["status"] == audit["status"] == "PASS"
assert x["verdict"] == audit["scientific_verdict"] == "MATERIAL-CHECKED-PROGRESS-NOT-CLOSED"
assert x["root_status"] == x["route_status"] == "CONJECTURED" and x["D_star_Gross"] == [11, 12]
assert x["completed_candidate_count"] == 12 and x["strict_serial"]
assert x["all_outer_dispositions"] == x["all_direct_dispositions"] == "SATISFIABLE"
assert x["outer_sat_count"] == 12 and x["direct_sat_count"] == 24
assert x["unsat_count"] == x["unknown_count"] == x["timeout_count"] == 0
assert x["repair_entered"] is False and x["canonical_edits"] is False and x["commit"] is False and x["push"] is False
assert x["source_model"]["inherited_order_predicates"] == 14484
assert x["source_model"]["block_family_counts"] == {"unary": 1440, "round62": 20, "generalized": 12820, "dynamic": 204}

initial = x["initial_frontier"]
assert sha_file(R / "state/iter136_state.json") == initial["state_file_sha256"] == "58781b46cc177df046ec334420046e1ccc8a23517f21fe4491e6412741ced57c"
assert initial["selector_count"] == 232 and initial["selector_state_sha256"] == "1692d905120d2dcf51b949ce4a70ed4b8f1b270c2d07a1ddbf5813d20d80fa81"
assert sha_file(R / "formulas/iter136/source.json.gz") == initial["source_file_sha256"]
assert data_sha(R / "formulas/iter136/outer.cnf") == initial["cnf_sha256"]

synthesis = load(R / "synthesis/triple_gf2_closure.json")
assert sha_file(R / x["synthesis"]["file"]) == x["synthesis"]["file_sha256"]
assert synthesis["finite_domain"]["unordered_distinct_triples_enumerated"] == x["synthesis"]["finite_domain_size"] == 527684
assert synthesis["counts"]["eligible_weight_1_to_10_triples"] == x["synthesis"]["eligible_weight_1_to_10_results"] == 4232
assert len(synthesis["retained_terms"]) == x["synthesis"]["retained_terms"] == 0

assert len(x["iterations"]) == 12
for iteration, row in zip(range(136, 148), x["iterations"]):
    assert row["iteration"] == iteration and row == audit["iterations"][iteration - 136]
    F = R / "formulas" / f"iter{iteration}"
    I = R / "iterations" / f"iter{iteration}"
    metadata = load(F / "metadata.json")
    candidate = load(I / "outer/candidate.json")
    direct = load(I / "direct/direct_verification.json")
    record = load(I / "record.json")
    assert row["source_selector_count"] == 232 + 2 * (iteration - 136) == metadata["selector_count"]
    assert row["outer"]["status"] == "SATISFIABLE" and row["outer"]["complete_assignment"]
    assert row["outer"]["cnf_sha256"] == metadata["cnf_sha256"] == data_sha(F / "outer.cnf")
    assert row["outer"]["schedule_sha256"] == candidate["compressed_schedule_sha256"]
    assert record["new_selectors"] == [f"r94-i{iteration}-Xerr", f"r94-i{iteration}-Zerr"]
    assert record["state_mutated_atomically"] and record["repair_entered"] is False
    for sector in ("Xerr", "Zerr"):
        r = row["direct"][sector]
        d = direct["sectors"][sector]
        mechanism = d["mechanism"]
        assert r["status"] == d["status"] == "SATISFIABLE" and r["complete_assignment"] and r["physical_replay"]
        assert r["weight"] == mechanism["fault_count"]
        assert r["mechanism_semantic_sha256"] == object_sha(mechanism)
        assert d["all_dimacs_clauses_satisfied"] and d["formula_summary"]["complete_query"]
        assert mechanism["physical_syndrome"] == [] and mechanism["physical_nontrivial"]
        assert mechanism["canonical_physical_parities_equal"]

assert x["weight_summary"]["Xerr"]["weight_9_iterations"] == [138]
assert x["weight_summary"]["Zerr"]["weight_9_iterations"] == []
assert x["sat_proof_streams"]["count"] == 36 and x["sat_proof_streams"]["empty_clause_lines"] == 0
assert x["proof_objects"]["actual_unsat_count"] == 0
assert x["proof_objects"]["gross_unsat_drat"] is None and x["proof_objects"]["gross_unsat_lrat"] is None
assert x["proof_objects"]["direct_unsat_proofs"] == []
proof = load(R / "controls/proof_fixture_controls.json")
assert proof["status"] == "PASS" and proof["scope"] == "tool-chain controls only; no Gross UNSAT occurred"
for key in ("valid_drat_accepted", "generated_lrat_accepted", "corrupt_drat_rejected", "truncated_drat_rejected", "corrupt_lrat_rejected", "truncated_lrat_rejected"):
    assert proof[key] and x["proof_objects"]["fixture_controls"][key]

fresh = x["fresh_state"]
state = load(R / "state/iter148_state.json")
metadata = load(R / "formulas/iter148/metadata.json")
assert state["next_iteration"] == fresh["next_iteration"] == 148 and state["started"] is fresh["started"] is False
assert state["selector_count"] == fresh["selector_count"] == 256
assert state["selector_state_sha256"] == fresh["selector_state_sha256"] == "9337b0fe78a3f8af54cec263422fe1641b64094d861c87959a82e1dffe6f326f"
assert sha_file(R / "state/iter148_state.json") == fresh["state_file_sha256"]
assert sha_file(R / "formulas/iter148/source.json.gz") == fresh["source_file_sha256"]
assert metadata["assertions"] == fresh["assertions"] == 19138
assert metadata["variables"] == fresh["variables"] == 409157
assert metadata["clauses"] == fresh["clauses"] == 1385059
assert metadata["cnf_sha256"] == fresh["cnf_sha256"] == data_sha(R / "formulas/iter148/outer.cnf")
assert not (R / "iterations/iter148").exists()
print("ROUND94_RESULT_CROSSCHECK_PASS", len(x["iterations"]), fresh["selector_count"])
