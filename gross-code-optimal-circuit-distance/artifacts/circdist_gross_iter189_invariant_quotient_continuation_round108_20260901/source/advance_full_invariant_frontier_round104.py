#!/usr/bin/env python3
"""Append both iteration-187 selector orbits to the invariant frontier.

This runs only after both complete direct sectors are SAT and physically
replayed.  Blocks are already exactly invariant and remain byte-for-byte
semantically unchanged.  Every one of the 144 parent/translation selector
pairs is independently replayed on its translated legal source schedule.
"""
from pathlib import Path
import argparse
import gzip
import hashlib
import json
import sys


L, M, G = 12, 6, 72


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":")).encode()


def semantic_sha(value):
    return hashlib.sha256(canonical(value)).hexdigest()


def file_sha(path):
    digest = hashlib.sha256()
    with Path(path).open("rb") as handle:
        for block in iter(lambda: handle.read(8 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def load(path):
    raw = Path(path).read_bytes()
    return json.loads(gzip.decompress(raw) if Path(path).suffix == ".gz" else raw)


def add(index, delta):
    i, j = divmod(int(index), M)
    return ((i + delta[0]) % L) * M + ((j + delta[1]) % M)


def tq(qubit, delta):
    qubit = int(qubit)
    return add(qubit, delta) if qubit < G else G + add(qubit - G, delta)


def te(edge, delta):
    kind, check, qubit = edge.split(":")
    return f"{kind}:{add(check, delta)}:{tq(qubit, delta)}"


def selector_key(selector):
    return (str(selector["sector"]),
            tuple(sorted(map(int, selector["data_support"]))),
            tuple(sorted((int(check), tuple(sorted(map(int, kinds))))
                         for check, kinds in selector["group_kinds"].items())))


def selector_hash_from_key(key):
    sector, data, groups = key
    names = [f"D:{qubit}" for qubit in data]
    group_dict = {str(check): list(kinds) for check, kinds in groups}
    for check, kinds in groups:
        names.extend(f"R:{check}:{kind}" for kind in kinds)
    semantic = {"sector": sector, "selected_names": names,
                "data_support": list(data), "group_kinds": group_dict}
    return semantic_sha(semantic), names, group_dict


def parent_from_mechanism(sector, mechanism, schedule_sha):
    data = []
    groups = {}
    for name in mechanism["selected_names"]:
        fields = name.split(":")
        if fields[0] == "D":
            data.append(int(fields[1]))
        else:
            assert fields[0] == "R"
            groups.setdefault(int(fields[1]), []).append(int(fields[2]))
    key = (sector, tuple(sorted(data)),
           tuple(sorted((check, tuple(sorted(kinds))) for check, kinds in groups.items())))
    digest, names, group_dict = selector_hash_from_key(key)
    assert names == mechanism["selected_names"]
    return {
        "mechanism_id": f"r104-i187-{sector}",
        "source_iteration": 187,
        "sector": sector,
        "fault_count": mechanism["fault_count"],
        "selected_names": names,
        "data_support": list(key[1]),
        "group_kinds": group_dict,
        "source_schedule_sha256": schedule_sha,
        "origin": "round104_iter187_full_invariant_quotient_direct360",
        "selector_semantic_sha256": digest,
    }


def translate_selector(parent, delta, translated_schedule_sha, index):
    key = selector_key(parent)
    sector, data, groups = key
    translated_key = (sector,
                      tuple(sorted(tq(qubit, delta) for qubit in data)),
                      tuple(sorted((add(check, delta), kinds) for check, kinds in groups)))
    digest, names, group_dict = selector_hash_from_key(translated_key)
    result = {
        "mechanism_id": f"r104-iter187-orbit-s{index}-p{parent['sector']}-d{delta[0]}_{delta[1]}",
        "source_iteration": 187,
        "sector": sector,
        "fault_count": parent["fault_count"],
        "selected_names": names,
        "data_support": list(translated_key[1]),
        "group_kinds": group_dict,
        "selector_semantic_sha256": digest,
        "origin": "round104_iter187_candidate_translation_orbit",
        "source_schedule_parent_sha256": translated_schedule_sha,
        "translation_parent_mechanism_id": parent["mechanism_id"],
        "translation_parent_selector_semantic_sha256": parent["selector_semantic_sha256"],
        "translation_delta": list(delta),
        "soundness_provenance": "direct SAT/physical replay on translated legal source schedule",
    }
    assert len(names) == len(set(names)) == result["fault_count"] <= 10
    return result, translated_key


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", type=Path, required=True)
    parser.add_argument("--state", type=Path, required=True)
    parser.add_argument("--candidate", type=Path, required=True)
    parser.add_argument("--direct", type=Path, required=True)
    parser.add_argument("--vendor", type=Path, required=True)
    parser.add_argument("--output-source", type=Path, required=True)
    parser.add_argument("--output-state", type=Path, required=True)
    parser.add_argument("--output-audit", type=Path, required=True)
    args = parser.parse_args()
    source = load(args.source)
    state = json.loads(args.state.read_text())
    candidate = json.loads(args.candidate.read_text())
    direct = json.loads(args.direct.read_text())
    assert state["started"] is False and state["next_iteration"] == 187
    assert len(source["blocks"]) == state["block_count"] == 517140
    assert len(source["selectors"]) == state["selector_count"] == 24012
    assert all(direct["sectors"][sector]["status"] == "SATISFIABLE"
               for sector in ("Xerr", "Zerr"))
    assert all(direct["sectors"][sector]["all_dimacs_clauses_satisfied"]
               for sector in ("Xerr", "Zerr"))

    times = {str(edge): int(value) for edge, value in candidate["compressed_times"].items()}
    schedule_sha = semantic_sha(times)
    assert schedule_sha == candidate["compressed_schedule_sha256"] == direct["candidate_sha256"]
    parents = [parent_from_mechanism(sector, direct["sectors"][sector]["mechanism"], schedule_sha)
               for sector in ("Xerr", "Zerr")]

    vendor = args.vendor.resolve()
    sys.path[:0] = [str(vendor / "src/round63_src"), str(vendor / "src")]
    import model
    import round68_build as builder
    _, _, logical_x, logical_z = builder.load_context()

    existing = list(source["selectors"])
    by_key = {selector_key(selector): selector for selector in existing}
    assert len(by_key) == len(existing)
    by_hash = {selector["selector_semantic_sha256"]: selector_key(selector)
               for selector in existing}
    assert len(by_hash) == len(existing)
    deltas = [(i, j) for i in range(L) for j in range(M)]
    replay_rows = []
    schedule_rows = []
    collisions = []
    parent_orbits = {parent["sector"]: set() for parent in parents}
    for delta in deltas:
        translated_times = {te(edge, delta): value for edge, value in times.items()}
        schedule_audit = model.audit_schedule(translated_times, True)
        assert schedule_audit["ok"] and schedule_audit["global_interleaved"]
        translated_schedule_sha = semantic_sha(translated_times)
        sectors = builder.sectors(translated_times, logical_x, logical_z)
        schedule_rows.append({"delta": list(delta), "schedule_sha256": translated_schedule_sha,
                              "used_layers": schedule_audit["used_layers"],
                              "max_time": schedule_audit["max_time"]})
        for parent in parents:
            selector, key = translate_selector(parent, delta, translated_schedule_sha,
                                               len(existing))
            assert selector["selector_semantic_sha256"] == selector_hash_from_key(key)[0]
            prior_key = by_hash.get(selector["selector_semantic_sha256"])
            assert prior_key is None or prior_key == key, "semantic hash collision"
            replay = model.verify_named_selection(sectors[selector["sector"]],
                                                  selector["selected_names"], 10)
            assert replay["ok"] and replay["weight"] == selector["fault_count"]
            assert replay["syndrome"] == [] and replay["nontrivial"]
            parent_orbits[parent["sector"]].add(key)
            if key in by_key:
                collisions.append({"sector": selector["sector"], "delta": list(delta),
                                   "selector_semantic_sha256": selector["selector_semantic_sha256"],
                                   "existing_mechanism_id": by_key[key]["mechanism_id"]})
            else:
                by_key[key] = selector
                by_hash[selector["selector_semantic_sha256"]] = key
                existing.append(selector)
            replay_rows.append({
                "sector": selector["sector"], "delta": list(delta),
                "selector_semantic_sha256": selector["selector_semantic_sha256"],
                "selected_names": selector["selected_names"],
                "source_schedule_sha256": translated_schedule_sha,
                "weight": replay["weight"], "syndrome": replay["syndrome"],
                "nontrivial": replay["nontrivial"],
            })
    assert all(len(orbit) in (36, 72) for orbit in parent_orbits.values())
    observed_keys = set(by_key)
    generator_cases = 0
    for generator in ((1, 0), (0, 1)):
        for key in observed_keys:
            sector, data, groups = key
            translated = (sector,
                          tuple(sorted(tq(qubit, generator) for qubit in data)),
                          tuple(sorted((add(check, generator), kinds) for check, kinds in groups)))
            assert translated in observed_keys
            generator_cases += 1

    source.pop("semantic_payload_sha256")
    # Keep the compiler-recognized finite-source suffix used by the invariant
    # iteration-187 source.  The iteration number and frontier disposition are
    # carried independently by this schema and the state record.
    source["schema"] = "circdist-gross-iteration188-full-translation-closure-finite-source-v1"
    source["selectors"] = existing
    source["expected"]["selectors"] = len(existing)
    source["expected"]["assertions"] = 4398 + len(source["blocks"]) + len(existing)
    source["bindings"]["round104_iter187_candidate_schedule_sha256"] = schedule_sha
    source["bindings"]["round104_iter187_candidate_orbit_parent_selectors"] = [
        parent["selector_semantic_sha256"] for parent in parents]

    residual_positions = [set(value) for value in source["residual_positions"]]
    def positions(kinds):
        result = set()
        for kind in kinds:
            result.symmetric_difference_update(residual_positions[int(kind)])
        return tuple(sorted(result))
    memberships = set()
    ranks = set()
    for selector in existing:
        definition = source["sector_definitions"][selector["sector"]]
        for check_string, kinds in selector["group_kinds"].items():
            check = int(check_string)
            position_set = positions(kinds)
            for qubit in definition["checks"][check]:
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

    state_out = {
        "schema": "circdist-gross-round104-iteration188-full-translation-frontier-state-v1",
        "status": "PASS", "next_iteration": 188, "started": False, "stop": None,
        "block_count": len(source["blocks"]), "selector_count": len(existing),
        "selector_state_sha256": semantic_sha([
            {key: selector.get(key) for key in ("mechanism_id", "sector", "selected_names",
                                                "data_support", "group_kinds",
                                                "selector_semantic_sha256")}
            for selector in existing]),
        "source_semantic_payload_sha256": source["semantic_payload_sha256"],
        "source_file_sha256": file_sha(args.output_source),
        "translation_group": "Z_12 x Z_6", "translation_group_order": 72,
        "scope": "fresh unstarted corrected-candidate orbit-closed outer frontier",
    }
    args.output_state.write_text(json.dumps(state_out, indent=2, sort_keys=True) + "\n")
    audit = {
        "schema": "circdist-gross-round104-iteration188-orbit-frontier-audit-v1",
        "status": "PASS", "group": {"name": "Z_12 x Z_6", "order": 72},
        "parent_selectors": parents,
        "parent_orbit_sizes": {sector: len(orbit) for sector, orbit in parent_orbits.items()},
        "parent_translation_pairs": len(replay_rows),
        "base_selectors": state["selector_count"], "fresh_selectors": len(existing),
        "new_unique_selectors": len(existing) - state["selector_count"],
        "collisions": collisions, "collision_count": len(collisions),
        "translated_schedule_rows": schedule_rows,
        "translated_selector_replays": replay_rows,
        "all_source_schedules_legal": True,
        "all_selectors_named_weight_at_most_10_zero_syndrome_nontrivial": True,
        "generator_invariance_cases": generator_cases,
        "identity_and_collision_handling": "complete normalized tuples; SHA-256 labels checked against tuple semantics",
        "source_file_sha256": file_sha(args.output_source),
        "source_semantic_payload_sha256": source["semantic_payload_sha256"],
        "state_file_sha256": file_sha(args.output_state),
        "selector_state_sha256": state_out["selector_state_sha256"],
    }
    args.output_audit.write_text(json.dumps(audit, indent=2, sort_keys=True) + "\n")
    print(json.dumps({key: audit[key] for key in
                      ("status", "parent_orbit_sizes", "parent_translation_pairs",
                       "fresh_selectors", "new_unique_selectors", "collision_count",
                       "source_file_sha256", "source_semantic_payload_sha256",
                       "state_file_sha256", "selector_state_sha256")}, sort_keys=True))


if __name__ == "__main__":
    main()
