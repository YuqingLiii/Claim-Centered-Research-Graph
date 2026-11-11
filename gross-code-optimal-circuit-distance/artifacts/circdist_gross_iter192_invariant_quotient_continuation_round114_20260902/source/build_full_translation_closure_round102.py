#!/usr/bin/env python3
"""Materialize the exact translation-invariant Gross cut registry.

Every inherited block and exact selector is translated by every element of
Z_12 x Z_6 and deduplicated by its full semantic tuple.  The result is a fresh,
unstarted source suitable for a sound orbit quotient.
"""
from pathlib import Path
import argparse
import collections
import gzip
import hashlib
import io
import json


L, M, G = 12, 6, 72


def load(path):
    raw = Path(path).read_bytes()
    return json.loads(gzip.decompress(raw) if Path(path).suffix == ".gz" else raw)


def file_sha(path):
    sha = hashlib.sha256()
    with Path(path).open("rb") as handle:
        for chunk in iter(lambda: handle.read(1 << 20), b""):
            sha.update(chunk)
    return sha.hexdigest()


def semantic_sha(value):
    sha = hashlib.sha256()
    encoder = json.JSONEncoder(sort_keys=True, separators=(",", ":"))
    for piece in encoder.iterencode(value):
        sha.update(piece.encode())
    return sha.hexdigest()


def add(g, delta):
    i, j = divmod(int(g), M)
    return ((i + delta[0]) % L) * M + ((j + delta[1]) % M)


def tq(q, delta):
    q = int(q)
    return add(q, delta) if q < G else G + add(q - G, delta)


def te(edge, delta):
    kind, check, qubit = edge.split(":")
    return f"{kind}:{add(int(check), delta)}:{tq(int(qubit), delta)}"


def selector_key(selector, delta):
    data = tuple(sorted(tq(q, delta) for q in selector["data_support"]))
    groups = tuple(sorted((add(int(check), delta), tuple(sorted(map(int, kinds))))
                          for check, kinds in selector["group_kinds"].items()))
    return selector["sector"], data, groups


def selector_from_key(parent, parent_index, delta, key, ordinal):
    sector, data, groups = key
    group_dict = {str(check): list(kinds) for check, kinds in groups}
    selected_names = [f"D:{q}" for q in data]
    for check, kinds in groups:
        for kind in kinds:
            selected_names.append(f"R:{check}:{kind}")
    semantic = {
        "sector": sector,
        "selected_names": selected_names,
        "data_support": list(data),
        "group_kinds": group_dict,
    }
    result = {
        "mechanism_id": f"r102-fullorbit-s{ordinal}-p{parent_index}-d{delta[0]}_{delta[1]}",
        "source_iteration": parent.get("source_iteration", 185),
        "sector": sector,
        "fault_count": int(parent["fault_count"]),
        "selected_names": selected_names,
        "data_support": list(data),
        "group_kinds": group_dict,
        "origin": "round102_full_translation_closure",
        "selector_semantic_sha256": semantic_sha(semantic),
        "translation_parent_mechanism_id": parent["mechanism_id"],
        "translation_parent_selector_semantic_sha256": parent["selector_semantic_sha256"],
        "translation_delta": list(delta),
        "soundness_provenance": "inverse-translation lift of reviewed exact selector; finite action theorem applies to every schedule",
    }
    if delta == (0, 0) and "source_schedule_sha256" in parent:
        result["source_schedule_sha256"] = parent["source_schedule_sha256"]
    elif "source_schedule_sha256" in parent:
        result["source_schedule_parent_sha256"] = parent["source_schedule_sha256"]
    assert len(selected_names) == len(set(selected_names)) == result["fault_count"] <= 10
    return result


def write_gzip_json(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("wb") as raw:
        with gzip.GzipFile(filename="", mode="wb", fileobj=raw,
                           compresslevel=9, mtime=0) as encoded:
            with io.TextIOWrapper(encoded, encoding="utf-8", newline="\n") as text:
                json.dump(value, text, sort_keys=True, separators=(",", ":"))
                text.write("\n")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", type=Path, required=True)
    parser.add_argument("--plan", type=Path, required=True)
    parser.add_argument("--action-check", type=Path, required=True)
    parser.add_argument("--output-source", type=Path, required=True)
    parser.add_argument("--output-state", type=Path, required=True)
    parser.add_argument("--output-audit", type=Path, required=True)
    args = parser.parse_args()
    source = load(args.source)
    plan = json.loads(args.plan.read_text())
    action = json.loads(args.action_check.read_text())
    assert plan["status"] == action["status"] == "PASS"
    assert file_sha(args.source) == plan["input_source_sha256"]
    assert source["semantic_payload_sha256"] == plan["input_semantic_sha256"]
    deltas = [(i, j) for i in range(L) for j in range(M)]
    edges = list(source["edges"])
    edge_index = {edge: index for index, edge in enumerate(edges)}
    assert len(edges) == len(edge_index) == 864

    edge_maps = []
    for delta in deltas:
        mapping = tuple(edge_index[te(edge, delta)] for edge in edges)
        assert len(set(mapping)) == 864
        edge_maps.append(mapping)

    parent_blocks = source["blocks"]
    block_semantics = {}
    family_counts = collections.Counter()
    parent_orbits = collections.Counter()
    for parent_index, block in enumerate(parent_blocks):
        base = tuple((edge_index[left], edge_index[right]) for left, right in block["atoms"])
        orbit = set()
        for delta, mapping in zip(deltas, edge_maps):
            key = tuple(sorted((mapping[left], mapping[right]) for left, right in base))
            orbit.add(key)
            if key not in block_semantics:
                block_semantics[key] = (parent_index, delta, block["family"], block["source_id"])
                family_counts[block["family"]] += 1
        parent_orbits[len(orbit)] += 1
    assert len(block_semantics) == plan["block_closure_unique"]
    assert dict(sorted(family_counts.items())) == plan["block_family_incremental_union_contributions"]
    assert {str(key): value for key, value in sorted(parent_orbits.items())} == \
        plan["block_orbit_size_histogram_per_parent"]

    blocks = []
    family_indices = collections.Counter()
    for ordinal, (key, provenance) in enumerate(block_semantics.items()):
        parent_index, delta, family, parent_source_id = provenance
        atoms = [[edges[left], edges[right]] for left, right in key]
        blocks.append({
            "atoms": atoms,
            "family": family,
            "family_index": family_indices[family],
            "source_id": f"r102-fullorbit-b{ordinal}-p{parent_index}-d{delta[0]}_{delta[1]}",
            "translation_parent_source_id": parent_source_id,
            "translation_delta": list(delta),
            "soundness_provenance": "inverse-translation lift of inherited sound order exclusion",
        })
        family_indices[family] += 1
    del block_semantics

    parent_selectors = source["selectors"]
    selector_semantics = {}
    selector_orbits = collections.Counter()
    for parent_index, selector in enumerate(parent_selectors):
        orbit = set()
        for delta in deltas:
            key = selector_key(selector, delta)
            orbit.add(key)
            selector_semantics.setdefault(key, (parent_index, delta))
        selector_orbits[len(orbit)] += 1
    assert len(selector_semantics) == plan["selector_closure_unique"]
    assert {str(key): value for key, value in sorted(selector_orbits.items())} == \
        plan["selector_orbit_size_histogram_per_parent"]
    selectors = []
    for ordinal, (key, (parent_index, delta)) in enumerate(selector_semantics.items()):
        selectors.append(selector_from_key(parent_selectors[parent_index], parent_index,
                                           delta, key, ordinal))
    del selector_semantics
    assert len({selector["selector_semantic_sha256"] for selector in selectors}) == len(selectors)
    assert collections.Counter(selector["sector"] for selector in selectors) == \
        collections.Counter(plan["selector_closure_by_sector"])

    source.pop("semantic_payload_sha256")
    source["schema"] = "circdist-gross-iteration186-full-translation-closure-finite-source-v1"
    source["blocks"] = blocks
    source["selectors"] = selectors
    source["bindings"]["round102_full_translation_closure_plan_sha256"] = file_sha(args.plan)
    source["bindings"]["round102_translation_action_check_sha256"] = file_sha(args.action_check)
    source["bindings"]["round102_full_translation_group"] = "Z_12 x Z_6"
    source["bindings"]["round102_full_translation_group_order"] = 72
    source["expected"]["reviewed_blocks"] = len(blocks)
    source["expected"]["selectors"] = len(selectors)
    source["expected"]["block_family_counts"] = dict(sorted(family_counts.items()))
    source["expected"]["assertions"] = 4398 + len(blocks) + len(selectors)

    residual_positions = [set(value) for value in source["residual_positions"]]
    def positions(kinds):
        result = set()
        for kind in kinds:
            result.symmetric_difference_update(residual_positions[int(kind)])
        return tuple(sorted(result))
    memberships = set()
    ranks = set()
    for selector in selectors:
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
    write_gzip_json(args.output_source, source)

    state_fields = ("mechanism_id", "sector", "selected_names", "data_support",
                    "group_kinds", "selector_semantic_sha256")
    selector_state_sha = semantic_sha([
        {field: selector.get(field) for field in state_fields} for selector in selectors
    ])
    state = {
        "schema": "circdist-gross-round102-full-translation-frontier-state-v1",
        "status": "PASS",
        "next_iteration": 186,
        "started": False,
        "stop": None,
        "block_count": len(blocks),
        "selector_count": len(selectors),
        "selector_state_sha256": selector_state_sha,
        "source_semantic_payload_sha256": source["semantic_payload_sha256"],
        "source_file_sha256": file_sha(args.output_source),
        "translation_group": "Z_12 x Z_6",
        "translation_group_order": 72,
        "scope": "fresh unstarted fully translation-invariant base; no solver disposition",
    }
    args.output_state.parent.mkdir(parents=True, exist_ok=True)
    args.output_state.write_text(json.dumps(state, indent=2, sort_keys=True) + "\n")
    audit = {
        "schema": "circdist-gross-round102-full-translation-closure-audit-v1",
        "status": "PASS",
        "input_source_sha256": file_sha(args.source),
        "closure_plan_sha256": file_sha(args.plan),
        "action_check_sha256": file_sha(args.action_check),
        "group": {"name": "Z_12 x Z_6", "order": 72},
        "input_blocks": len(parent_blocks),
        "input_unique_block_semantics": plan["input_unique_block_semantics"],
        "input_block_semantic_duplicates": plan["input_block_semantic_duplicates"],
        "block_parent_translation_pairs": plan["block_pair_multiplicity"],
        "block_closure_unique": len(blocks),
        "block_collision_count": plan["block_collision_count"],
        "block_orbit_size_histogram_per_parent": plan["block_orbit_size_histogram_per_parent"],
        "block_family_counts": dict(sorted(family_counts.items())),
        "input_selectors": len(parent_selectors),
        "selector_parent_translation_pairs": plan["selector_pair_multiplicity"],
        "selector_closure_unique": len(selectors),
        "selector_collision_count": plan["selector_collision_count"],
        "selector_orbit_size_histogram_per_parent": plan["selector_orbit_size_histogram_per_parent"],
        "selector_closure_by_sector": plan["selector_closure_by_sector"],
        "membership_expressions": len(memberships),
        "rank_expressions": len(ranks),
        "source_semantic_payload_sha256": source["semantic_payload_sha256"],
        "source_file_sha256": file_sha(args.output_source),
        "state_file_sha256": file_sha(args.output_state),
        "selector_state_sha256": selector_state_sha,
        "closure_soundness": "each translated exclusion is the inverse-action lift of an inherited sound exclusion",
        "invariance": "the deduplicated semantic sets equal their image under every one of 72 translations",
        "collision_handling": "full atom tuples and full (sector,data,groups) tuples decide identity; hashes are labels only",
        "integer_safety": plan["integer_safety"],
    }
    args.output_audit.write_text(json.dumps(audit, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "status": "PASS",
        "blocks": len(blocks),
        "selectors": len(selectors),
        "source_sha256": audit["source_file_sha256"],
        "semantic_sha256": audit["source_semantic_payload_sha256"],
        "selector_state_sha256": selector_state_sha,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
