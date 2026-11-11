#!/usr/bin/env python3
"""Install complete translation orbits of the two checked quotient-candidate selectors.

The output is a fresh, unstarted base source/state.  Every added selector is replayed on
the corresponding translated legal source schedule before it is retained.
"""
from pathlib import Path
import argparse
import collections
import gzip
import hashlib
import json
import sys


L, M, G = 12, 6, 72


def canonical(obj):
    return json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()


def semantic_sha(obj):
    return hashlib.sha256(canonical(obj)).hexdigest()


def file_sha(path):
    h = hashlib.sha256()
    with Path(path).open("rb") as handle:
        for chunk in iter(lambda: handle.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def load(path):
    raw = Path(path).read_bytes()
    return json.loads(gzip.decompress(raw) if Path(path).suffix == ".gz" else raw)


def add(g, delta):
    i, j = divmod(int(g), M)
    return ((i + delta[0]) % L) * M + ((j + delta[1]) % M)


def tq(q, delta):
    q = int(q)
    return add(q, delta) if q < G else G + add(q - G, delta)


def te(edge, delta):
    kind, check, qubit = edge.split(":")
    return f"{kind}:{add(int(check), delta)}:{tq(int(qubit), delta)}"


def selector_record(parent, delta, translated_schedule_sha):
    data = sorted(tq(q, delta) for q in parent["data_support"])
    groups = {str(add(int(check), delta)): sorted(map(int, kinds))
              for check, kinds in parent["group_kinds"].items()}
    groups = {key: groups[key] for key in sorted(groups, key=int)}
    names = [f"D:{q}" for q in data]
    for check in sorted(groups, key=int):
        for kind in groups[check]:
            names.append(f"R:{check}:{kind}")
    out = {
        "mechanism_id": f"r102-orbit-{parent['sector']}-d{delta[0]}_{delta[1]}-{parent['selector_semantic_sha256'][:12]}",
        "source_iteration": 185,
        "sector": parent["sector"],
        "fault_count": parent["fault_count"],
        "selected_names": names,
        "data_support": data,
        "group_kinds": groups,
        "source_schedule_sha256": translated_schedule_sha,
        "origin": f"round102_translation_orbit_of:{parent['mechanism_id']}",
        "orbit_parent_selector_semantic_sha256": parent["selector_semantic_sha256"],
        "orbit_delta": list(delta),
    }
    semantic = {key: out[key] for key in ("sector", "selected_names", "data_support", "group_kinds")}
    out["selector_semantic_sha256"] = semantic_sha(semantic)
    assert out["fault_count"] == len(data) + sum(len(kinds) for kinds in groups.values())
    assert len(names) == len(set(names)) == out["fault_count"] <= 10
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--source332", type=Path, required=True)
    ap.add_argument("--state332", type=Path, required=True)
    ap.add_argument("--candidate", type=Path, required=True)
    ap.add_argument("--direct", type=Path, required=True)
    ap.add_argument("--vendor", type=Path, required=True)
    ap.add_argument("--action-check", type=Path, required=True)
    ap.add_argument("--output-source", type=Path, required=True)
    ap.add_argument("--output-state", type=Path, required=True)
    ap.add_argument("--output-audit", type=Path, required=True)
    args = ap.parse_args()
    source = load(args.source332)
    state = json.loads(args.state332.read_text())
    candidate = json.loads(args.candidate.read_text())
    direct = json.loads(args.direct.read_text())
    action_check = json.loads(args.action_check.read_text())
    assert action_check["status"] == "PASS"
    assert len(source["selectors"]) == len(state["selectors"]) == state["selector_count"] == 332
    parents = source["selectors"][-2:]
    assert [parent["sector"] for parent in parents] == ["Xerr", "Zerr"]
    assert all(parent["mechanism_id"].startswith("r100-i185-") for parent in parents)
    assert all(direct["sectors"][label]["status"] == "SATISFIABLE" for label in ("Xerr", "Zerr"))

    vendor = args.vendor.resolve()
    sys.path[:0] = [str(vendor / "src" / "round63_src"), str(vendor / "src")]
    import model
    import round68_build as builder
    _, _, logical_x, logical_z = builder.load_context()
    times = {str(edge): int(value) for edge, value in candidate["compressed_times"].items()}
    assert model.audit_schedule(times, True)["ok"]

    deltas = [(i, j) for i in range(L) for j in range(M)]
    existing = list(source["selectors"][:-2])
    by_semantic = {selector["selector_semantic_sha256"]: selector for selector in existing}
    assert len(by_semantic) == len(existing) == 330
    orbit_rows = []
    schedule_rows = []
    collision_rows = []
    per_parent_orbits = {}
    for delta in deltas:
        translated_times = {te(edge, delta): value for edge, value in times.items()}
        audit = model.audit_schedule(translated_times, True)
        assert audit["ok"] and audit["global_interleaved"]
        schedule_hash = semantic_sha(translated_times)
        sectors = builder.sectors(translated_times, logical_x, logical_z)
        schedule_rows.append({"delta": list(delta), "schedule_sha256": schedule_hash,
                              "used_layers": audit["used_layers"], "max_time": audit["max_time"]})
        for parent in parents:
            selector = selector_record(parent, delta, schedule_hash)
            replay = model.verify_named_selection(
                sectors[selector["sector"]], selector["selected_names"], 10)
            assert replay["ok"] and replay["weight"] == selector["fault_count"] == 10
            assert replay["syndrome"] == [] and replay["nontrivial"]
            key = selector["selector_semantic_sha256"]
            per_parent_orbits.setdefault(parent["selector_semantic_sha256"], set()).add(key)
            if key in by_semantic:
                collision_rows.append({"delta": list(delta), "sector": selector["sector"],
                                       "semantic_sha256": key,
                                       "existing_mechanism_id": by_semantic[key]["mechanism_id"]})
            else:
                by_semantic[key] = selector
                existing.append(selector)
            orbit_rows.append({
                "delta": list(delta), "sector": selector["sector"],
                "mechanism_id": selector["mechanism_id"],
                "selector_semantic_sha256": key,
                "source_schedule_sha256": schedule_hash,
                "selected_names": selector["selected_names"],
                "replay_weight": replay["weight"],
                "replay_syndrome": replay["syndrome"],
                "replay_nontrivial": replay["nontrivial"],
            })
    assert all(len(orbit) in (36, 72) for orbit in per_parent_orbits.values())
    assert len({selector["selector_semantic_sha256"] for selector in existing}) == len(existing)

    source.pop("semantic_payload_sha256")
    source["schema"] = "circdist-gross-iteration186-finite-source-v1"
    source["selectors"] = existing
    source["expected"]["selectors"] = len(existing)
    source["expected"]["assertions"] = 4398 + len(source["blocks"]) + len(existing)
    source["bindings"]["round102_translation_action_check_sha256"] = file_sha(args.action_check)
    source["bindings"]["round102_quotient_candidate_schedule_sha256"] = candidate["compressed_schedule_sha256"]
    source["bindings"]["round102_orbit_parent_selector_sha256"] = [
        parent["selector_semantic_sha256"] for parent in parents]

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
    source["semantic_payload_sha256"] = semantic_sha(source)
    args.output_source.parent.mkdir(parents=True, exist_ok=True)
    args.output_source.write_bytes(gzip.compress(
        (json.dumps(source, indent=2, sort_keys=True) + "\n").encode(),
        compresslevel=9, mtime=0))

    state_keys = ("mechanism_id", "sector", "selected_names", "data_support",
                  "group_kinds", "selector_semantic_sha256")
    state_hash = semantic_sha([{key: selector.get(key) for key in state_keys}
                               for selector in existing])
    frontier_state = {
        "schema": "circdist-gross-round102-translation-frontier-state-v1",
        "status": "PASS",
        "next_iteration": 186,
        "started": False,
        "stop": None,
        "selector_count": len(existing),
        "selector_state_sha256": state_hash,
        "parent_selector_count": 330,
        "direct_parent_selector_count": 332,
        "orbit_parent_count": 2,
        "group_order": 72,
        "orbit_replay_count": len(orbit_rows),
        "orbit_collision_count": len(collision_rows),
        "selectors": existing,
        "source_semantic_payload_sha256": source["semantic_payload_sha256"],
        "source_file_sha256": file_sha(args.output_source),
        "scope": "fresh unstarted translation-quotient frontier; no solver disposition",
    }
    args.output_state.write_text(json.dumps(frontier_state, indent=2, sort_keys=True) + "\n")
    audit = {
        "schema": "circdist-gross-round102-orbit-frontier-audit-v1",
        "status": "PASS",
        "group": {"name": "Z_12 x Z_6", "order": 72},
        "base_selectors": 330,
        "direct_parents": 2,
        "parent_orbit_sizes": {key: len(value) for key, value in per_parent_orbits.items()},
        "parent_translation_pairs": len(orbit_rows),
        "unique_frontier_selectors": len(existing),
        "new_unique_selectors": len(existing) - 330,
        "collisions_with_prior_or_earlier_orbit": len(collision_rows),
        "collision_rows": collision_rows,
        "translated_schedule_rows": schedule_rows,
        "translated_selector_replays": orbit_rows,
        "all_source_schedules_legal": True,
        "all_selectors_weight_10_zero_syndrome_nontrivial": True,
        "injectivity_and_multiplicity": "semantic hashes deduplicate selected-name sets; each parent orbit size is recorded and all 144 parent-translation pairs remain in the replay ledger",
        "source_semantic_payload_sha256": source["semantic_payload_sha256"],
        "source_file_sha256": file_sha(args.output_source),
        "state_file_sha256": file_sha(args.output_state),
        "selector_state_sha256": state_hash,
    }
    args.output_audit.write_text(json.dumps(audit, indent=2, sort_keys=True) + "\n")
    print(json.dumps({key: audit[key] for key in (
        "status", "parent_translation_pairs", "unique_frontier_selectors",
        "new_unique_selectors", "collisions_with_prior_or_earlier_orbit",
        "source_semantic_payload_sha256", "selector_state_sha256")}, sort_keys=True))


if __name__ == "__main__":
    main()
