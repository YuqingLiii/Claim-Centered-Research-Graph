#!/usr/bin/env python3
"""Independent exact replay of the Round86 seed and six strict-serial steps."""
from pathlib import Path
import argparse, gzip, hashlib, json, sys

ap = argparse.ArgumentParser()
ap.add_argument("--root", type=Path, required=True)
ap.add_argument("--output", type=Path, required=True)
a = ap.parse_args()
R = a.root.resolve()
P = R / "vendor" / "round80"
sys.path[:0] = [str(P / "src" / "round63_src"), str(P / "src")]
import model as M
import round68_build as B
import round68_verify as V


def canonical_bytes(obj):
    return json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()


def sha_obj(obj):
    return hashlib.sha256(canonical_bytes(obj)).hexdigest()


def load(path):
    path = Path(path)
    blob = path.read_bytes()
    return json.loads(gzip.decompress(blob) if path.suffix == ".gz" else blob)


def selector_state_hash(selectors):
    keys = ("mechanism_id", "sector", "selected_names", "data_support", "group_kinds", "selector_semantic_sha256")
    return sha_obj([{key: selector.get(key) for key in keys} for selector in selectors])


def named_valid(sectors, selector):
    return M.verify_named_selection(sectors[selector["sector"]], selector["selected_names"], 10)["ok"]


def schedule_sha(times):
    return sha_obj({key: int(value) for key, value in times.items()})


dynamic = load(P / "restart" / "dynamic_blocks_iteration102.json.gz")
generalized = load(P / "restart" / "installed_generalized_terms_iteration102.json.gz")
registry = load(P / "restart" / "online_mechanism_registry_iteration102.json.gz")
raw = load(P / "restart" / "full_raw_mechanisms_iteration102.json.gz")
semantic_hashes = {
    "dynamic": sha_obj(dynamic),
    "generalized": sha_obj(generalized),
    "registry": sha_obj(registry),
    "raw": sha_obj(raw),
}
assert semantic_hashes == {
    "dynamic": "62cabe5f2925fc0caadd340848ea439219c13dc3d397c67762f852d36b6560e2",
    "generalized": "4547a39d560358ce24c1615f5db99f17735c717a2b10d67ad2cfac515731acf3",
    "registry": "b9816477e347ed095e26fd4a521be8a951e92e1b3aa66c668cd2fa315d652604",
    "raw": "fff897136200a97d12ae1756ca07a8aadd10e80cf11e4cce8e7ba30f8e428600",
}
assert len(dynamic) == 204 and generalized["term_count"] == 12820
assert registry["mechanism_count"] == raw["mechanism_count"] == 120

px, pz, lx, lz = B.load_context()
assert len(px) == len(pz) == 1884
assert len(lx) == len(lz) == 12
round63_x, _ = B.global_single_records("Xerr", M.Xchecks, px, "X")
round63_z, _ = B.global_single_records("Zerr", M.Zchecks, pz, "Z")
round62 = load(P / "src" / "round62_cegar20.json.gz")
B.replay_round62_blocks(round62, lx, lz)
blocks = [[tuple(atom) for atom in record["atoms"]] for record in round63_x + round63_z]
blocks += [[tuple(atom) for atom in block["atoms"]] for block in round62["outer_blocks"]]
blocks += [[tuple(atom) for atom in term["atoms"]] for term in generalized["terms"]]
blocks += [[tuple(atom) for atom in block["atoms"]] for block in dynamic]
assert len(blocks) == 1440 + 20 + 12820 + 204 == 14484

state = json.loads((R / "continuation" / "final_state.json").read_text())
checkpoint = json.loads((R / "continuation" / "checkpoint_state.json").read_text())
assert state["schema"] == "round86-efssc-final-state-v1" and state["status"] == "PASS"
assert state["reviewed_base_semantic_sha256"] == semantic_hashes
assert state["reviewed_base_blocks"] == 14484
assert state["initial_reviewed_selectors"] == 120
assert state["seed_round86_selectors"] == 2
assert state["incremental_completed_candidates"] == 6
assert state["selector_count"] == len(state["selectors"]) == 134
assert selector_state_hash(state["selectors"]) == state["selector_state_sha256"]
assert state["next_iteration"] == 109 and state["started"] is False and state["stop"] is None
assert checkpoint["next_iteration"] == 109 and checkpoint["started"] is False
assert checkpoint["selector_count"] == 134
assert checkpoint["selector_state_sha256"] == state["selector_state_sha256"]
assert checkpoint["selectors"] == state["selectors"]
assert checkpoint["completed_iterations"] == [103, 104, 105, 106, 107, 108]

# Bind the first 120 selectors independently to the reviewed raw ledger.
reviewed_bindings = []
for reviewed, selector in zip(sorted(raw["mechanisms"], key=lambda row: (row["iteration"], row["sector"])), state["selectors"][:120]):
    expected = {
        "mechanism_id": reviewed["mechanism_id"],
        "source_iteration": reviewed["iteration"],
        "sector": reviewed["sector"],
        "fault_count": reviewed["fault_count"],
        "selected_names": reviewed["selected_names"],
        "data_support": reviewed["data_support"],
        "group_kinds": reviewed["group_kinds"],
        "source_schedule_sha256": reviewed["candidate_sha256"],
        "source_times": reviewed["times"],
        "origin": "reviewed_round80_raw_registry",
    }
    for key, value in expected.items():
        assert selector[key] == value, (selector["mechanism_id"], key)
    expected_semantic = sha_obj({key: selector[key] for key in ("sector", "selected_names", "data_support", "group_kinds")})
    assert selector["selector_semantic_sha256"] == expected_semantic
    assert schedule_sha(selector["source_times"]) == selector["source_schedule_sha256"]
    source_sectors = B.sectors(selector["source_times"], lx, lz)
    assert named_valid(source_sectors, selector)
    reviewed_bindings.append(selector["mechanism_id"])
assert len(reviewed_bindings) == 120


def replay_mechanism(sector, stored):
    by_name = {column.name: column.index for column in sector.columns}
    indices = [by_name[name] for name in stored["selected_names"]]
    named = M.verify_named_selection(sector, stored["selected_names"], 10)
    assert named["ok"] and named["weight"] == 10
    rebuilt = V.mechanism(sector, indices)
    assert canonical_bytes(rebuilt) == canonical_bytes(stored)
    assert rebuilt["canonical_replay"]["syndrome"] == []
    assert rebuilt["canonical_replay"]["nontrivial"] is True
    assert rebuilt["physical_syndrome"] == []
    assert rebuilt["physical_nontrivial"] is True
    assert rebuilt["canonical_physical_parities_equal"] is True
    return {
        "sector": sector.label,
        "fault_count": len(indices),
        "canonical_net_weight": rebuilt["canonical_replay"]["net_weight"],
        "physical_net_weight": rebuilt["physical_net_weight"],
        "selected_names_sha256": sha_obj(rebuilt["selected_names"]),
    }


seed_candidate = json.loads((R / "data" / "seed_iter102" / "candidate.json").read_text())
seed_direct = json.loads((R / "data" / "seed_iter102" / "direct_verification.json").read_text())
seed_times = {key: int(value) for key, value in seed_candidate["schedule_times"].items()}
seed_audit = M.audit_schedule(seed_times, True)
assert seed_audit == seed_candidate["audit"] == seed_direct["schedule_audit"]
assert seed_audit["ok"] and seed_audit["global_interleaved"]
assert schedule_sha(seed_times) == seed_candidate["schedule_sha256"] == seed_direct["candidate_sha256"]
seed_old_hits = [index for index, atoms in enumerate(blocks) if M.block_holds(seed_times, atoms)]
assert seed_old_hits == []
seed_sectors = B.sectors(seed_times, lx, lz)
seed_prior_survivors = [selector["mechanism_id"] for selector in state["selectors"][:120] if named_valid(seed_sectors, selector)]
assert seed_prior_survivors == []
seed_mechanisms = {
    sector: replay_mechanism(seed_sectors[sector], seed_direct["sectors"][sector]["mechanism"])
    for sector in ("Xerr", "Zerr")
}
assert all(named_valid(seed_sectors, selector) for selector in state["selectors"][120:122])

# Negative controls for the schedule and named-mechanism validators.
bad_schedule = dict(seed_times)
bad_edge_a = M.edge_key("X", 0, M.Xchecks[0][0])
bad_edge_b = M.edge_key("X", 0, M.Xchecks[0][1])
bad_schedule[bad_edge_b] = bad_schedule[bad_edge_a]
bad_audit = M.audit_schedule(bad_schedule, True)
assert bad_audit["ok"] is False and bad_audit["conflicts"]
duplicate_names = list(state["selectors"][120]["selected_names"])
duplicate_names[-1] = duplicate_names[0]
duplicate_control = M.verify_named_selection(seed_sectors["Xerr"], duplicate_names, 10)
assert duplicate_control["ok"] is False and duplicate_control["error"] == "invalid/duplicate named columns"

iteration_summaries = []
for offset, record in enumerate(state["iterations"]):
    iteration = 103 + offset
    assert record["iteration"] == iteration
    on_disk = json.loads((R / "iterations" / f"iter{iteration}.json").read_text())
    assert on_disk == record
    before = 122 + 2 * offset
    after = before + 2
    assert record["outer_status"] == "SAT" and record["reason_unknown"] is None
    assert record["existing_blocks"] == 14484
    assert record["semantic_cuts_before"] == before and record["semantic_cuts_after"] == after
    assert record["state_before_sha256"] == selector_state_hash(state["selectors"][:before])
    assert record["state_after_sha256"] == selector_state_hash(state["selectors"][:after])
    assert record["state_mutated"] is True and record["new_cuts_installed"] == 2
    assert record["repair_entered"] is False and record["branch_closed"] is False
    times = {key: int(value) for key, value in record["candidate_schedule"].items()}
    audit = M.audit_schedule(times, True)
    assert audit == record["candidate_audit"]
    assert audit["ok"] and audit["global_interleaved"]
    assert schedule_sha(times) == record["candidate_schedule_sha256"]
    old_hits = [index for index, atoms in enumerate(blocks) if M.block_holds(times, atoms)]
    assert old_hits == []
    sectors = B.sectors(times, lx, lz)
    survivors = [selector["mechanism_id"] for selector in state["selectors"][:before] if named_valid(sectors, selector)]
    assert survivors == record["prior_selector_survivors"] == []
    direct_summary = {}
    for sector in ("Xerr", "Zerr"):
        direct = record["direct"][sector]
        assert direct["status"] == "SAT" and direct["kind"] == "effective_leq"
        assert direct["W"] == 10 and direct["distinct_columns"] is True
        direct_summary[sector] = replay_mechanism(sectors[sector], direct["mechanism"])
    new_selectors = state["selectors"][before:after]
    assert record["new_selectors"] == [selector["mechanism_id"] for selector in new_selectors]
    assert all(named_valid(sectors, selector) for selector in new_selectors)
    assert all(selector["source_schedule_sha256"] == record["candidate_schedule_sha256"] for selector in new_selectors)
    iteration_summaries.append({
        "iteration": iteration,
        "schedule_sha256": record["candidate_schedule_sha256"],
        "reviewed_block_hits": len(old_hits),
        "prior_selector_survivors": len(survivors),
        "new_selector_truths": 2,
        "direct": direct_summary,
    })

assert selector_state_hash(state["selectors"]) == state["selector_state_sha256"]
formula_bytes = (R / "formulas" / "final_outer.smt2").read_bytes()
assert hashlib.sha256(formula_bytes).hexdigest() == state["final_formula_sha256"]

domain = json.loads((R / "data" / "new_selector_domain_census.json").read_text())
assert domain["summary"] == {
    "equal_to_source_cube": 5,
    "selector_count": 14,
    "strict_source_cube_expansions": 9,
    "total_source_cube_order_tuples_sum_across_selectors": 89663440921344,
    "total_valid_order_tuples_sum_across_selectors": 25969520291556096,
}
assert [entry["mechanism_id"] for entry in domain["selectors"]] == [selector["mechanism_id"] for selector in state["selectors"][120:]]
assert all(entry["source_cube_invalid_order_tuples"] == 0 for entry in domain["selectors"])
assert all(entry["valid_order_tuples"] > 0 and entry["invalid_order_tuples"] > 0 for entry in domain["selectors"])
assert sum(entry["strictly_contains_source_cube"] for entry in domain["selectors"]) == 9

output = {
    "schema": "round86-independent-state-replay-v1",
    "status": "PASS",
    "frozen_model": {
        "qubits": M.N,
        "checks_per_sector": M.G,
        "named_edges": len(M.ALL_EDGES),
        "overlaps": len(M.OVERLAPS),
        "static_distance_pool_weight": 12,
        "static_logical_pool_per_sector": len(px),
        "logical_basis_per_sector": len(lx),
    },
    "reviewed_restart": {
        "semantic_sha256": semantic_hashes,
        "generalized_blocks": 12820,
        "dynamic_blocks": 204,
        "registry_mechanisms": 120,
        "raw_mechanisms": 120,
        "total_reviewed_blocks": len(blocks),
        "reviewed_selector_bindings": len(reviewed_bindings),
    },
    "seed_iteration102": {
        "schedule_sha256": seed_candidate["schedule_sha256"],
        "reviewed_block_hits": len(seed_old_hits),
        "prior_selector_survivors": len(seed_prior_survivors),
        "new_selector_truths": 2,
        "direct": seed_mechanisms,
    },
    "iterations": iteration_summaries,
    "continuation": {
        "selector_count": 134,
        "selector_state_sha256": state["selector_state_sha256"],
        "next_iteration": 109,
        "started": False,
        "completed_round86_candidates": 7,
        "new_selectors": 14,
    },
    "domain_census": domain["summary"],
    "negative_controls": {
        "schedule_collision_rejected": True,
        "schedule_collision_count": len(bad_audit["conflicts"]),
        "duplicate_named_fault_rejected": True,
    },
    "scientific_disposition": {
        "distance12_witness_found": False,
        "universal_distance11_ceiling_proved": False,
        "root_residual_after_round86": "D* in {11,12}",
        "root_status": "CONJECTURED",
    },
}
a.output.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n")
print(json.dumps({
    "status": output["status"],
    "reviewed_blocks": len(blocks),
    "reviewed_selectors": len(reviewed_bindings),
    "candidates_replayed": 1 + len(iteration_summaries),
    "both_sector_weight10_mechanisms": 2 * (1 + len(iteration_summaries)),
    "next_iteration": 109,
    "started": False,
}, sort_keys=True))
