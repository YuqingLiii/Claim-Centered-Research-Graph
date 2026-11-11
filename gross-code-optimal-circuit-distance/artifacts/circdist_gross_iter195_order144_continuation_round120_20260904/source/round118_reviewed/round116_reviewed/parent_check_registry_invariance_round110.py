#!/usr/bin/env python3
"""Parameter-bound full Z_12 x Z_6 source-registry invariance audit."""
from pathlib import Path
import argparse
import gzip
import hashlib
import json

L, M, G = 12, 6, 72


def canonical_sha(obj):
    digest = hashlib.sha256()
    encoder = json.JSONEncoder(sort_keys=True, separators=(",", ":"))
    for text in encoder.iterencode(obj):
        digest.update(text.encode())
    return digest.hexdigest()


def file_sha(path):
    digest = hashlib.sha256()
    with Path(path).open("rb") as handle:
        for block in iter(lambda: handle.read(8 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def add(value, delta):
    i, j = divmod(int(value), M)
    return ((i + delta[0]) % L) * M + ((j + delta[1]) % M)


def translate_qubit(qubit, delta):
    qubit = int(qubit)
    return add(qubit, delta) if qubit < G else G + add(qubit - G, delta)


def translate_edge(edge, delta):
    kind, check, qubit = edge.split(":")
    return f"{kind}:{add(check, delta)}:{translate_qubit(qubit, delta)}"


def block_key(block):
    return tuple(sorted((str(atom[0]), str(atom[1])) for atom in block["atoms"]))


def translate_block(key, delta):
    return tuple(sorted((translate_edge(a, delta), translate_edge(b, delta)) for a, b in key))


def selector_key(selector):
    groups = tuple(sorted((int(check), tuple(sorted(map(int, kinds))))
                          for check, kinds in selector["group_kinds"].items()))
    return (str(selector["sector"]), tuple(sorted(map(int, selector["data_support"]))), groups)


def translate_selector(key, delta):
    sector, data, groups = key
    return (sector, tuple(sorted(translate_qubit(q, delta) for q in data)),
            tuple(sorted((add(check, delta), kinds) for check, kinds in groups)))


def selector_semantics(key):
    sector, data, groups = key
    names = [f"D:{q}" for q in data]
    group_dict = {str(check): list(kinds) for check, kinds in groups}
    for check, kinds in groups:
        names += [f"R:{check}:{kind}" for kind in kinds]
    return {"sector": sector, "selected_names": names,
            "data_support": list(data), "group_kinds": group_dict}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--source", type=Path, required=True)
    ap.add_argument("--state", type=Path, required=True)
    ap.add_argument("--output", type=Path, required=True)
    ap.add_argument("--iteration", type=int, required=True)
    ap.add_argument("--blocks", type=int, required=True)
    ap.add_argument("--selectors", type=int, required=True)
    ap.add_argument("--assertions", type=int, required=True)
    args = ap.parse_args()
    with gzip.open(args.source, "rt") as handle:
        source = json.load(handle)
    state = json.loads(args.state.read_text())

    claimed = source.pop("semantic_payload_sha256")
    observed = canonical_sha(source)
    source["semantic_payload_sha256"] = claimed
    assert observed == claimed
    assert source["schema"] == f"circdist-gross-iteration{args.iteration}-full-translation-closure-finite-source-v1"
    assert len(source["blocks"]) == args.blocks and len(source["selectors"]) == args.selectors
    assert source["expected"]["reviewed_blocks"] == args.blocks
    assert source["expected"]["selectors"] == args.selectors
    assert source["expected"]["assertions"] == args.assertions
    assert state["next_iteration"] == args.iteration and state["started"] is False and state["stop"] is None
    assert state["block_count"] == args.blocks and state["selector_count"] == args.selectors
    assert state["source_file_sha256"] == file_sha(args.source)
    assert state["source_semantic_payload_sha256"] == observed

    edges = list(map(str, source["edges"]))
    edge_set = set(edges)
    assert len(edges) == len(edge_set) == 864
    deltas = [(i, j) for i in range(L) for j in range(M)]
    edge_maps = {delta: {edge: translate_edge(edge, delta) for edge in edges} for delta in deltas}
    assert all(set(mapping) == edge_set and set(mapping.values()) == edge_set for mapping in edge_maps.values())
    assert all(edge_maps[(0, 0)][edge] == edge for edge in edges)
    composition = nonidentity_fixed = 0
    for delta in deltas:
        if delta != (0, 0):
            nonidentity_fixed += sum(edge_maps[delta][edge] == edge for edge in edges)
        for second in deltas:
            total = ((delta[0] + second[0]) % L, (delta[1] + second[1]) % M)
            for edge in edges:
                assert edge_maps[delta][edge_maps[second][edge]] == edge_maps[total][edge]
                composition += 1

    block_keys = [block_key(block) for block in source["blocks"]]
    block_set = set(block_keys)
    assert len(block_keys) == len(block_set) == args.blocks
    selector_keys, selector_hashes = [], set()
    for selector in source["selectors"]:
        key = selector_key(selector)
        semantic = selector_semantics(key)
        digest = canonical_sha(semantic)
        assert selector["selector_semantic_sha256"] == digest
        assert selector["selected_names"] == semantic["selected_names"]
        assert selector["data_support"] == semantic["data_support"]
        assert selector["group_kinds"] == semantic["group_kinds"]
        assert len(selector["selected_names"]) == len(set(selector["selected_names"])) == selector["fault_count"] <= 10
        assert digest not in selector_hashes
        selector_hashes.add(digest)
        selector_keys.append(key)
    selector_set = set(selector_keys)
    assert len(selector_keys) == len(selector_set) == args.selectors
    block_generator_cases = selector_generator_cases = 0
    for delta in ((1, 0), (0, 1)):
        for key in block_keys:
            assert translate_block(key, delta) in block_set
            block_generator_cases += 1
        for key in selector_keys:
            assert translate_selector(key, delta) in selector_set
            selector_generator_cases += 1

    selector_state = canonical_sha([
        {key: selector.get(key) for key in
         ("mechanism_id", "sector", "selected_names", "data_support", "group_kinds", "selector_semantic_sha256")}
        for selector in source["selectors"]
    ])
    assert selector_state == state["selector_state_sha256"]
    families = {}
    for block in source["blocks"]:
        families[block["family"]] = families.get(block["family"], 0) + 1
    result = {
        "schema": "circdist-gross-round110-registry-invariance-v1", "status": "PASS",
        "iteration": args.iteration, "source_sha256": file_sha(args.source),
        "semantic_source_sha256": observed, "state_sha256": file_sha(args.state),
        "selector_state_sha256": selector_state,
        "group": {"name": "Z_12 x Z_6", "order": 72, "elements": 72, "edges": 864,
                  "edge_bijections": 72, "composition_cases": composition,
                  "nonidentity_fixed_edges": nonidentity_fixed, "generators": [[1, 0], [0, 1]]},
        "blocks": {"count": len(block_keys), "unique_exact_tuples": len(block_set),
                   "families": families, "generator_cases": block_generator_cases},
        "selectors": {"count": len(selector_keys), "unique_exact_tuples": len(selector_set),
                      "unique_semantic_hashes": len(selector_hashes),
                      "Xerr": sum(key[0] == "Xerr" for key in selector_keys),
                      "Zerr": sum(key[0] == "Zerr" for key in selector_keys),
                      "generator_cases": selector_generator_cases},
        "invariance_theorem": "Closure under generators (1,0) and (0,1) implies closure under all 72 group elements.",
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps({"status": "PASS", "iteration": args.iteration, "blocks": len(block_keys),
                      "selectors": len(selector_keys), "composition_cases": composition,
                      "block_generator_cases": block_generator_cases,
                      "selector_generator_cases": selector_generator_cases}, sort_keys=True))


if __name__ == "__main__":
    main()
