#!/usr/bin/env python3
"""Atomically append two fully replayed exact EFSSC selectors and emit the next source."""
from pathlib import Path
import argparse
import gzip
import hashlib
import json
import sys


def canonical_bytes(obj):
    return json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()


def semantic_sha256(obj):
    return hashlib.sha256(canonical_bytes(obj)).hexdigest()


def load(path):
    path = Path(path)
    data = path.read_bytes()
    return json.loads(gzip.decompress(data) if path.suffix == ".gz" else data)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--vendor", type=Path, required=True)
    parser.add_argument("--state-in", type=Path, required=True)
    parser.add_argument("--source-in", type=Path, required=True)
    parser.add_argument("--iteration", type=int, required=True)
    parser.add_argument("--candidate", type=Path, required=True)
    parser.add_argument("--direct", type=Path, required=True)
    parser.add_argument("--state-out", type=Path, required=True)
    parser.add_argument("--record-out", type=Path, required=True)
    parser.add_argument("--source-out", type=Path, required=True)
    args = parser.parse_args()

    previous = json.loads(args.state_in.read_text())
    source = load(args.source_in)
    candidate = json.loads(args.candidate.read_text())
    direct = json.loads(args.direct.read_text())
    iteration = args.iteration

    assert previous["next_iteration"] == iteration
    assert previous["started"] is False
    assert previous["stop"] is None
    assert len(previous["selectors"]) == previous["selector_count"]
    assert len(source["selectors"]) == previous["selector_count"]
    assert source["expected"]["selectors"] == previous["selector_count"]

    times = candidate["compressed_times"]
    schedule_sha = semantic_sha256(times)
    assert direct["candidate_sha256"] == schedule_sha
    assert candidate["compressed_schedule_sha256"] == schedule_sha
    for label in ("Xerr", "Zerr"):
        sector = direct["sectors"][label]
        assert sector["status"] == "SATISFIABLE"
        assert sector["all_dimacs_clauses_satisfied"] is True
        assert sector["formula_summary"]["complete_query"] is True
        mechanism = sector["mechanism"]
        assert 1 <= mechanism["fault_count"] <= 10
        assert mechanism["physical_syndrome"] == []
        assert mechanism["physical_nontrivial"] is True
        assert mechanism["canonical_physical_parities_equal"] is True

    vendor = args.vendor.resolve()
    sys.path[:0] = [str(vendor / "src" / "round63_src"), str(vendor / "src")]
    import model as model
    import round68_build as builder

    _, _, logical_x, logical_z = builder.load_context()
    sectors = builder.sectors(times, logical_x, logical_z)
    schedule_audit = model.audit_schedule(times, True)
    assert schedule_audit["ok"] and schedule_audit == candidate["frozen_audit"]
    assert not any(
        model.verify_named_selection(
            sectors[selector["sector"]], selector["selected_names"], 10
        )["ok"]
        for selector in previous["selectors"]
    )

    def make_selector(label):
        mechanism = direct["sectors"][label]["mechanism"]
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
            "mechanism_id": f"r96-i{iteration}-{label}",
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
            "origin": f"round96_proof_outer_iteration{iteration}_direct360",
            "source_symbolic_validity": "True",
        }
        semantic_keys = ("sector", "selected_names", "data_support", "group_kinds")
        selector["selector_semantic_sha256"] = semantic_sha256(
            {key: selector[key] for key in semantic_keys}
        )
        assert selector["fault_count"] == len(selector["data_support"]) + sum(
            len(value) for value in selector["group_kinds"].values()
        )
        assert 1 <= selector["fault_count"] <= 10
        exact = model.verify_named_selection(
            sectors[label], selector["selected_names"], 10
        )
        assert exact["ok"]
        return selector

    new_selectors = [make_selector("Xerr"), make_selector("Zerr")]
    selectors = previous["selectors"] + new_selectors
    assert len({selector["selector_semantic_sha256"] for selector in selectors}) == len(selectors)

    state_keys = (
        "mechanism_id",
        "sector",
        "selected_names",
        "data_support",
        "group_kinds",
        "selector_semantic_sha256",
    )
    state_hash = semantic_sha256(
        [{key: selector.get(key) for key in state_keys} for selector in selectors]
    )
    record = {
        "schema": "round96-proof-outer-iteration-record-v1",
        "iteration": iteration,
        "source_selector_count": len(previous["selectors"]),
        "source_selector_state_sha256": previous["selector_state_sha256"],
        "outer_encoding": "finite 10-bit CNF",
        "outer_cnf_sha256": candidate["cnf_sha256"],
        "outer_status": "SATISFIABLE",
        "candidate_schedule_sha256": schedule_sha,
        "candidate_audit": schedule_audit,
        "complete_outer_assignment": True,
        "reviewed_block_hits": 0,
        "prior_selector_survivors": 0,
        "direct": {
            label: {
                "status": direct["sectors"][label]["status"],
                "complete_query": direct["sectors"][label]["formula_summary"]["complete_query"],
                "variables": direct["sectors"][label]["formula_summary"]["variables"],
                "clauses": direct["sectors"][label]["formula_summary"]["clauses"],
                "dimacs_sha256": direct["sectors"][label]["formula_summary"]["dimacs_sha256"],
                "all_dimacs_clauses_satisfied": direct["sectors"][label]["all_dimacs_clauses_satisfied"],
                "fault_count": direct["sectors"][label]["mechanism"]["fault_count"],
                "mechanism_sha256": semantic_sha256(direct["sectors"][label]["mechanism"]),
            }
            for label in ("Xerr", "Zerr")
        },
        "repair_entered": False,
        "repair_gate_reason": "both unrestricted direct-360 sectors are SAT",
        "new_selectors": [selector["mechanism_id"] for selector in new_selectors],
        "new_cuts_installed": 2,
        "state_mutated_atomically": True,
        "state_after_sha256": state_hash,
        "next_iteration": iteration + 1,
        "started": False,
    }

    state = dict(previous)
    state.update(
        {
            "schema": "round96-proof-outer-continuation-state-v1",
            "status": "PASS",
            "parent_selector_count": len(previous["selectors"]),
            "parent_selector_state_sha256": previous["selector_state_sha256"],
            "round96_initial_selector_count": previous.get(
                "round96_initial_selector_count", previous["selector_count"]
            ),
            "round96_completed_candidates": previous.get(
                "round96_completed_candidates", 0
            )
            + 1,
            "selector_count": len(selectors),
            "selector_state_sha256": state_hash,
            "next_iteration": iteration + 1,
            "started": False,
            "stop": None,
            "completed_iterations": previous.get("completed_iterations", []) + [iteration],
            "iterations": previous.get("iterations", []) + [record],
            "selectors": selectors,
            "atomicity": {
                "candidate_solved_against_selector_prefix": len(previous["selectors"]),
                "both_direct_replays_before_commit": True,
                "commit_selector_indices": [len(previous["selectors"]), len(previous["selectors"]) + 1],
                "later_cuts_retroactive": False,
            },
        }
    )
    args.state_out.parent.mkdir(parents=True, exist_ok=True)
    args.record_out.parent.mkdir(parents=True, exist_ok=True)
    args.source_out.parent.mkdir(parents=True, exist_ok=True)
    args.state_out.write_text(json.dumps(state, indent=2, sort_keys=True) + "\n")
    args.record_out.write_text(json.dumps(record, indent=2, sort_keys=True) + "\n")

    source.pop("semantic_payload_sha256")
    source["schema"] = f"circdist-gross-iteration{iteration + 1}-finite-source-v1"
    compact_keys = (
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
    )
    for selector in new_selectors:
        source["selectors"].append(
            {key: selector[key] for key in compact_keys}
        )
    source["bindings"][f"round96_iteration{iteration}_cnf_sha256"] = candidate["cnf_sha256"]
    source["bindings"]["round96_continuation_selector_state_sha256"] = state_hash
    source["expected"]["selectors"] = len(selectors)
    source["expected"]["assertions"] = 18882 + len(selectors)

    residual_positions = [set(value) for value in source["residual_positions"]]

    def positions(kinds):
        result = set()
        for kind in kinds:
            result.symmetric_difference_update(residual_positions[int(kind)])
        return tuple(sorted(result))

    memberships = set()
    ranks = set()
    for selector in source["selectors"]:
        sector_definition = source["sector_definitions"][selector["sector"]]
        for check_string, kinds in selector["group_kinds"].items():
            check = int(check_string)
            position_set = positions(kinds)
            for qubit in sector_definition["checks"][check]:
                memberships.add((selector["sector"], check, position_set, qubit))
                if position_set and position_set != tuple(range(6)):
                    ranks.add((selector["sector"], check, qubit))
    source["expected"]["membership_expressions"] = len(memberships)
    source["expected"]["rank_expressions"] = len(ranks)
    source["semantic_payload_sha256"] = semantic_sha256(source)
    args.source_out.write_bytes(
        gzip.compress(
            (json.dumps(source, indent=2, sort_keys=True) + "\n").encode(),
            compresslevel=9,
            mtime=0,
        )
    )

    print(
        json.dumps(
            {
                "status": "PASS",
                "iteration": iteration,
                "next_iteration": iteration + 1,
                "selector_count": len(selectors),
                "selector_state_sha256": state_hash,
                "source_semantic_payload_sha256": source["semantic_payload_sha256"],
                "rank_expressions": len(ranks),
                "membership_expressions": len(memberships),
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
