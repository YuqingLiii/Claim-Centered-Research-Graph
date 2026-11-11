#!/usr/bin/env python3
"""Independently replay the twelve exact EFSSC transitions and fresh frontier."""
from pathlib import Path
import argparse
import gzip
import hashlib
import json
import sys


def canonical_sha256(obj):
    return hashlib.sha256(
        json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def load(path):
    path = Path(path)
    data = path.read_bytes()
    return json.loads(gzip.decompress(data) if path.suffix == ".gz" else data)


parser = argparse.ArgumentParser()
parser.add_argument("--root", type=Path, required=True)
parser.add_argument("--output", type=Path, required=True)
args = parser.parse_args()
root = args.root.resolve()
vendor = root / "vendor/round80"
sys.path[:0] = [str(vendor / "src/round63_src"), str(vendor / "src")]
import model
import round68_build

_, _, logical_x, logical_z = round68_build.load_context()
state = json.loads((root / "bindings/round88/final_state.json").read_text())
assert state["next_iteration"] == 112 and state["started"] is False
assert state["selector_count"] == len(state["selectors"]) == 140
assert state["selector_state_sha256"] == "a0364547f846fd68ace7cdba85d89c0f8e6326145243fb0fea7ff543420994cb"

initial_selectors = list(state["selectors"])
selectors = list(initial_selectors)
rows = []
for iteration in range(112, 124):
    formula = root / f"formulas/iter{iteration}"
    evidence = root / f"iterations/iter{iteration}"
    source = load(formula / "source.json.gz")
    semantic = dict(source)
    recorded_semantic_sha = semantic.pop("semantic_payload_sha256")
    assert canonical_sha256(semantic) == recorded_semantic_sha
    assert source["expected"]["selectors"] == len(selectors)
    assert len(source["selectors"]) == len(selectors)

    candidate = json.loads((evidence / "outer/candidate.json").read_text())
    direct = json.loads((evidence / "direct/direct_verification.json").read_text())
    record = json.loads((evidence / "record.json").read_text())
    metadata = json.loads((formula / "metadata.json").read_text())
    times = {str(key): int(value) for key, value in candidate["compressed_times"].items()}
    schedule_sha = canonical_sha256(times)
    assert candidate["compressed_schedule_sha256"] == schedule_sha
    assert direct["candidate_sha256"] == schedule_sha
    audit = model.audit_schedule(times, True)
    assert audit == candidate["frozen_audit"] and audit["ok"] and audit["global_interleaved"]
    sectors = round68_build.sectors(times, logical_x, logical_z)
    assert not any(
        model.verify_named_selection(
            sectors[selector["sector"]], selector["selected_names"], 10
        )["ok"]
        for selector in selectors
    )

    new_selectors = []
    for label in ("Xerr", "Zerr"):
        sector_result = direct["sectors"][label]
        mechanism = sector_result["mechanism"]
        assert sector_result["status"] == "SATISFIABLE"
        assert sector_result["all_dimacs_clauses_satisfied"] is True
        assert sector_result["formula_summary"]["complete_query"] is True
        assert 1 <= mechanism["fault_count"] <= 10
        assert mechanism["physical_syndrome"] == []
        assert mechanism["physical_nontrivial"] is True
        assert mechanism["canonical_physical_parities_equal"] is True
        exact = model.verify_named_selection(sectors[label], mechanism["selected_names"], 10)
        assert exact["ok"] and exact["weight"] == mechanism["fault_count"]

        data_support = []
        group_kinds = {}
        for name in mechanism["selected_names"]:
            parts = name.split(":")
            if parts[0] == "D":
                data_support.append(int(parts[1]))
            else:
                assert parts[0] == "R"
                group_kinds.setdefault(parts[1], []).append(int(parts[2]))
        selector = {
            "mechanism_id": f"r90-i{iteration}-{label}",
            "source_iteration": iteration,
            "sector": label,
            "fault_count": mechanism["fault_count"],
            "selected_names": mechanism["selected_names"],
            "data_support": sorted(data_support),
            "group_kinds": {
                key: sorted(value)
                for key, value in sorted(group_kinds.items(), key=lambda item: int(item[0]))
            },
            "source_schedule_sha256": schedule_sha,
            "source_times": times,
            "canonical_support": mechanism["canonical_replay"]["net_support"],
            "physical_support": mechanism["physical_net_support"],
            "source_atoms": mechanism["sound_outer_block"]["atoms"],
            "source_atom_count": mechanism["sound_outer_block"]["atom_count"],
            "origin": f"round90_proof_outer_iteration{iteration}_direct360",
            "source_symbolic_validity": "True",
        }
        selector["selector_semantic_sha256"] = canonical_sha256(
            {
                key: selector[key]
                for key in ("sector", "selected_names", "data_support", "group_kinds")
            }
        )
        new_selectors.append(selector)

    selectors += new_selectors
    state_keys = (
        "mechanism_id",
        "sector",
        "selected_names",
        "data_support",
        "group_kinds",
        "selector_semantic_sha256",
    )
    state_hash = canonical_sha256(
        [{key: selector.get(key) for key in state_keys} for selector in selectors]
    )
    assert record["iteration"] == iteration
    assert record["source_selector_count"] == len(selectors) - 2
    assert record["outer_cnf_sha256"] == metadata["cnf_sha256"]
    assert record["outer_status"] == "SATISFIABLE"
    assert record["candidate_schedule_sha256"] == schedule_sha
    assert record["new_selectors"] == [selector["mechanism_id"] for selector in new_selectors]
    assert record["state_after_sha256"] == state_hash
    assert record["next_iteration"] == iteration + 1
    assert record["state_mutated_atomically"] is True
    assert record["repair_entered"] is False

    next_source = load(root / f"formulas/iter{iteration + 1}/source.json.gz")
    assert len(next_source["selectors"]) == len(selectors)
    for compact, full in zip(next_source["selectors"][-2:], new_selectors):
        for key in (
            "mechanism_id",
            "source_iteration",
            "sector",
            "fault_count",
            "selected_names",
            "data_support",
            "group_kinds",
            "source_schedule_sha256",
            "origin",
            "selector_semantic_sha256",
        ):
            assert compact[key] == full[key]
    rows.append(
        {
            "iteration": iteration,
            "schedule_sha256": schedule_sha,
            "source_selector_count": len(selectors) - 2,
            "new_selector_count": 2,
            "state_after_sha256": state_hash,
            "weights": {
                label: direct["sectors"][label]["mechanism"]["fault_count"]
                for label in ("Xerr", "Zerr")
            },
        }
    )

final_state = json.loads((root / "continuation/final_state.json").read_text())
assert final_state["selectors"] == selectors
assert final_state["selector_count"] == len(selectors) == 164
assert final_state["selector_state_sha256"] == rows[-1]["state_after_sha256"]
assert final_state["selector_state_sha256"] == "854c2b50a07fa955356932311eb3229a164e16f125e5b2991c6c2916d5fce2c3"
assert final_state["next_iteration"] == 124 and final_state["started"] is False
assert final_state["stop"] is None and final_state["round90_completed_candidates"] == 12
assert not (root / "iterations/iter124").exists()
fresh_metadata = json.loads((root / "formulas/iter124/metadata.json").read_text())
assert fresh_metadata["selector_count"] == 164
assert fresh_metadata["cnf_sha256"] == "2dd07d33ff0b29c1f06a7452c3b1c7ca9b6df950e819046f8a712dacb0dd7e5a"

out = {
    "schema": "circdist-round90-continuation-audit-v1",
    "status": "PASS",
    "initial_iteration": 112,
    "initial_selector_count": 140,
    "completed_candidates": 12,
    "new_selectors": 24,
    "final_selector_count": 164,
    "final_selector_state_sha256": final_state["selector_state_sha256"],
    "fresh_next_iteration": 124,
    "fresh_next_source_semantic_sha256": "d155a897b8771a9821ef4ef14041bb910e7bbb6aaaad7f6cf08b6db1de0f397e",
    "fresh_next_cnf_sha256": fresh_metadata["cnf_sha256"],
    "iterations": rows,
}
args.output.parent.mkdir(parents=True, exist_ok=True)
args.output.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n")
print(json.dumps({key: value for key, value in out.items() if key != "iterations"}, sort_keys=True))
