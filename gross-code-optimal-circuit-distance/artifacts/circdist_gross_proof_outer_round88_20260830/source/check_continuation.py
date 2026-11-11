#!/usr/bin/env python3
"""Independent strict-serial audit of the Round-88 state transition."""
from pathlib import Path
import argparse, gzip, hashlib, json, sys


def canonical(obj):
    return json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()


def sha_obj(obj):
    return hashlib.sha256(canonical(obj)).hexdigest()


def load(path):
    path = Path(path)
    blob = path.read_bytes()
    return json.loads(gzip.decompress(blob) if path.suffix == ".gz" else blob)


ap = argparse.ArgumentParser()
ap.add_argument("--root", type=Path, required=True)
ap.add_argument("--output", type=Path, required=True)
a = ap.parse_args()
R = a.root.resolve()
P = R / "vendor" / "round80"
sys.path[:0] = [str(P / "src" / "round63_src"), str(P / "src")]
import model as M
import round68_build as B

parent = load(R / "bindings" / "round86" / "continuation" / "final_state.json.gz")
final = load(R / "continuation" / "final_state.json")
keys = ("mechanism_id", "sector", "selected_names", "data_support",
        "group_kinds", "selector_semantic_sha256")


def state_hash(selectors):
    return sha_obj([{k: s.get(k) for k in keys} for s in selectors])


assert parent["next_iteration"] == 109 and parent["started"] is False
assert len(parent["selectors"]) == parent["selector_count"] == 134
assert state_hash(parent["selectors"]) == parent["selector_state_sha256"]
assert final["next_iteration"] == 112 and final["started"] is False
assert final["selector_count"] == len(final["selectors"]) == 140
assert final["completed_iterations"] == [109, 110, 111]
assert final["round88_completed_candidates"] == 3
assert final["stop"] is None

px, pz, lx, lz = B.load_context()
prefix = list(parent["selectors"])
summaries = []
for iteration in (109, 110, 111):
    source = load(R / "formulas" / f"iter{iteration}" / "source.json.gz")
    semantic = source.pop("semantic_payload_sha256")
    assert sha_obj(source) == semantic
    source["semantic_payload_sha256"] = semantic
    assert source["expected"]["selectors"] == len(prefix)
    assert len(source["selectors"]) == len(prefix)
    for compact, full in zip(source["selectors"], prefix):
        assert all(compact[k] == full[k] for k in keys)

    record = load(R / "iterations" / f"iter{iteration}_record.json")
    candidate = load(R / "iterations" / f"iter{iteration}" / "outer" / "candidate.json")
    replay = load(R / "iterations" / f"iter{iteration}" / "outer" / "replay.json")
    direct = load(R / "iterations" / f"iter{iteration}" / "direct" / "direct_verification.json")
    times = {k: int(v) for k, v in candidate["compressed_times"].items()}
    schedule_hash = sha_obj(times)
    audit = M.audit_schedule(times, True)
    assert audit["ok"] and audit["global_interleaved"]
    assert audit == candidate["frozen_audit"] == replay["frozen_schedule_audit"]
    assert schedule_hash == candidate["compressed_schedule_sha256"]
    assert schedule_hash == direct["candidate_sha256"] == record["candidate_schedule_sha256"]
    sectors = B.sectors(times, lx, lz)
    survivors = [
        s["mechanism_id"] for s in prefix
        if M.verify_named_selection(sectors[s["sector"]], s["selected_names"], 10)["ok"]
    ]
    assert survivors == []

    new = final["selectors"][len(prefix):len(prefix) + 2]
    assert [s["mechanism_id"] for s in new] == record["new_selectors"]
    assert {s["sector"] for s in new} == {"Xerr", "Zerr"}
    for selector in new:
        label = selector["sector"]
        sec = direct["sectors"][label]
        mechanism = sec["mechanism"]
        assert sec["status"] == "SATISFIABLE"
        assert sec["all_dimacs_clauses_satisfied"] is True
        assert sec["formula_summary"]["complete_query"] is True
        assert sec["formula_summary"]["primary_selection_variables"] == 360
        assert sec["formula_summary"]["W"] == 10
        assert mechanism["fault_count"] == 10
        assert mechanism["canonical_replay"]["ok"]
        assert mechanism["physical_syndrome"] == []
        assert mechanism["physical_nontrivial"] is True
        assert mechanism["canonical_physical_parities_equal"] is True
        assert selector["selected_names"] == mechanism["selected_names"]
        assert selector["source_times"] == times
        assert selector["source_schedule_sha256"] == schedule_hash
        assert selector["source_symbolic_validity"] == "True"
        expected_semantic = sha_obj({
            k: selector[k] for k in ("sector", "selected_names", "data_support", "group_kinds")
        })
        assert selector["selector_semantic_sha256"] == expected_semantic
        assert M.verify_named_selection(
            sectors[label], selector["selected_names"], 10
        )["ok"]

    prefix.extend(new)
    assert record["source_selector_count"] == len(prefix) - 2
    assert record["source_selector_state_sha256"] == state_hash(prefix[:-2])
    assert record["state_after_sha256"] == state_hash(prefix)
    assert record["state_mutated_atomically"] is True
    assert record["repair_entered"] is False
    assert record["next_iteration"] == iteration + 1
    assert record["started"] is False
    summaries.append({
        "iteration": iteration,
        "source_selectors": len(prefix) - 2,
        "schedule_sha256": schedule_hash,
        "new_selectors": record["new_selectors"],
        "direct_fault_weights": {
            s: direct["sectors"][s]["mechanism"]["fault_count"]
            for s in ("Xerr", "Zerr")
        },
    })

assert prefix == final["selectors"]
assert state_hash(prefix) == final["selector_state_sha256"]
assert final["selector_state_sha256"] == (
    "a0364547f846fd68ace7cdba85d89c0f8e6326145243fb0fea7ff543420994cb"
)

source112 = load(R / "formulas" / "iter112" / "source.json.gz")
semantic112 = source112.pop("semantic_payload_sha256")
assert sha_obj(source112) == semantic112
source112["semantic_payload_sha256"] = semantic112
assert len(source112["selectors"]) == source112["expected"]["selectors"] == 140
for compact, full in zip(source112["selectors"], final["selectors"]):
    assert all(compact[k] == full[k] for k in keys)
metadata112 = load(R / "formulas" / "iter112" / "metadata.json")
check112 = load(R / "formulas" / "iter112" / "encoding_check.json")
assert metadata112["assertions"] == 19022
assert metadata112["variables"] == 398488
assert metadata112["clauses"] == 1330104
assert metadata112["cnf_sha256"] == (
    "a8b917845427a0f746e72200a9a58eb5fac86d5e3c845eeaae69082038c86594"
)
assert check112["status"] == "PASS"
assert check112["all_source_roots_reconstructed"]
assert check112["all_clause_ids_partitioned_once"]
assert not (R / "iterations" / "iter112").exists()

out = {
    "schema": "circdist-gross-round88-continuation-audit-v1",
    "status": "PASS",
    "parent_iteration": 109,
    "parent_selector_count": 134,
    "iterations": summaries,
    "atomic_commits": 3,
    "new_selectors": 6,
    "final_selector_count": 140,
    "final_selector_state_sha256": final["selector_state_sha256"],
    "next_iteration": 112,
    "started": False,
    "iteration112_solved": False,
    "iteration112_cnf_sha256": metadata112["cnf_sha256"],
}
a.output.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n")
print(json.dumps(out, sort_keys=True))
