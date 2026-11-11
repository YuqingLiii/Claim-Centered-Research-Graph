#!/usr/bin/env python3
"""Count the exact Z_12 x Z_6 translation closure of a Gross outer source.

This planning pass uses compact integer keys so a potentially large block closure can
be measured before any expanded source is written.  It does not solve a formula.
"""
from pathlib import Path
import argparse
import collections
import gzip
import hashlib
import json
import time


L, M, G = 12, 6, 72


def add(g, delta):
    i, j = divmod(int(g), M)
    return ((i + delta[0]) % L) * M + ((j + delta[1]) % M)


def tq(q, delta):
    q = int(q)
    return add(q, delta) if q < G else G + add(q - G, delta)


def load(path):
    raw = Path(path).read_bytes()
    return json.loads(gzip.decompress(raw) if Path(path).suffix == ".gz" else raw)


def canonical(obj):
    return json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()


def selector_key(selector, delta):
    data = tuple(sorted(tq(q, delta) for q in selector["data_support"]))
    groups = tuple(sorted((add(int(check), delta), tuple(sorted(map(int, kinds))))
                          for check, kinds in selector["group_kinds"].items()))
    return selector["sector"], data, groups


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--source", type=Path, required=True)
    ap.add_argument("--output", type=Path, required=True)
    args = ap.parse_args()
    started = time.time()
    source = load(args.source)
    deltas = [(i, j) for i in range(L) for j in range(M)]
    edges = list(source["edges"])
    edge_index = {edge: i for i, edge in enumerate(edges)}
    assert len(edges) == len(edge_index) == 864

    edge_maps = []
    for delta in deltas:
        row = []
        for edge in edges:
            kind, check, qubit = edge.split(":")
            mapped = f"{kind}:{add(int(check), delta)}:{tq(int(qubit), delta)}"
            row.append(edge_index[mapped])
        assert len(set(row)) == 864
        edge_maps.append(tuple(row))

    block_union = set()
    block_orbit_histogram = collections.Counter()
    block_family_added = collections.Counter()
    original_block_keys = set()
    for block in source["blocks"]:
        base = tuple(sorted((edge_index[left], edge_index[right])
                            for left, right in block["atoms"]))
        original_block_keys.add(base)
    original_block_semantic_duplicates = len(source["blocks"]) - len(original_block_keys)
    for block in source["blocks"]:
        base = tuple((edge_index[left], edge_index[right]) for left, right in block["atoms"])
        orbit = set()
        for mapping in edge_maps:
            orbit.add(tuple(sorted((mapping[left], mapping[right]) for left, right in base)))
        block_orbit_histogram[len(orbit)] += 1
        before = len(block_union)
        block_union.update(orbit)
        block_family_added[block["family"]] += len(block_union) - before

    selector_union = set()
    original_selector_keys = set()
    selector_orbit_histogram = collections.Counter()
    sector_union = collections.Counter()
    for selector in source["selectors"]:
        key = selector_key(selector, (0, 0))
        assert key not in original_selector_keys
        original_selector_keys.add(key)
    for selector in source["selectors"]:
        orbit = {selector_key(selector, delta) for delta in deltas}
        selector_orbit_histogram[len(orbit)] += 1
        selector_union.update(orbit)
    for key in selector_union:
        sector_union[key[0]] += 1

    result = {
        "schema": "circdist-gross-round102-translation-closure-plan-v1",
        "status": "PASS",
        "group": {"name": "Z_12 x Z_6", "order": 72, "deltas": deltas},
        "input_source_sha256": hashlib.sha256(args.source.read_bytes()).hexdigest(),
        "input_semantic_sha256": source["semantic_payload_sha256"],
        "input_blocks": len(source["blocks"]),
        "input_unique_block_semantics": len(original_block_keys),
        "input_block_semantic_duplicates": original_block_semantic_duplicates,
        "input_selectors": len(source["selectors"]),
        "block_closure_unique": len(block_union),
        "block_closure_new": len(block_union - original_block_keys),
        "block_pair_multiplicity": len(source["blocks"]) * 72,
        "block_collision_count": len(source["blocks"]) * 72 - len(block_union),
        "block_orbit_size_histogram_per_parent": dict(sorted(block_orbit_histogram.items())),
        "block_family_incremental_union_contributions": dict(sorted(block_family_added.items())),
        "selector_closure_unique": len(selector_union),
        "selector_closure_new": len(selector_union - original_selector_keys),
        "selector_pair_multiplicity": len(source["selectors"]) * 72,
        "selector_collision_count": len(source["selectors"]) * 72 - len(selector_union),
        "selector_orbit_size_histogram_per_parent": dict(sorted(selector_orbit_histogram.items())),
        "selector_closure_by_sector": dict(sorted(sector_union.items())),
        "integer_safety": {
            "edge_indices_half_open": [0, 864],
            "translation_pairs": len(deltas) * len(edges),
            "block_parent_translation_pairs": len(source["blocks"]) * len(deltas),
            "selector_parent_translation_pairs": len(source["selectors"]) * len(deltas),
            "python_integers_unbounded": True,
        },
        "wall_seconds": round(time.time() - started, 6),
        "scope": "count only; no formula solved and no absence claim",
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
