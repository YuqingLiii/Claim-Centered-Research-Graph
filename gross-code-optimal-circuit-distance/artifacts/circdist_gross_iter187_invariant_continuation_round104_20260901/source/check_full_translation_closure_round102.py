#!/usr/bin/env python3
"""Independent set-level checker for the full Round102 translation closure."""
from pathlib import Path
import argparse
import collections
import gzip
import hashlib
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


def block_key(block):
    return tuple(sorted((str(left), str(right)) for left, right in block["atoms"]))


def translate_block_key(key, delta):
    return tuple(sorted((te(left, delta), te(right, delta)) for left, right in key))


def selector_key(selector):
    return (str(selector["sector"]),
            tuple(sorted(map(int, selector["data_support"]))),
            tuple(sorted((int(check), tuple(sorted(map(int, kinds))))
                         for check, kinds in selector["group_kinds"].items())))


def translate_selector_key(key, delta):
    sector, data, groups = key
    return (sector,
            tuple(sorted(tq(q, delta) for q in data)),
            tuple(sorted((add(check, delta), kinds) for check, kinds in groups)))


def selector_semantic_hash(selector):
    value = {
        "sector": selector["sector"],
        "selected_names": selector["selected_names"],
        "data_support": selector["data_support"],
        "group_kinds": selector["group_kinds"],
    }
    return semantic_sha(value)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input-source", type=Path, required=True)
    parser.add_argument("--closure-source", type=Path, required=True)
    parser.add_argument("--plan", type=Path, required=True)
    parser.add_argument("--audit", type=Path, required=True)
    parser.add_argument("--action-check", type=Path, required=True)
    parser.add_argument("--encoding-check", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    source = load(args.input_source)
    closure = load(args.closure_source)
    plan = json.loads(args.plan.read_text())
    audit = json.loads(args.audit.read_text())
    action = json.loads(args.action_check.read_text())
    encoding = json.loads(args.encoding_check.read_text())
    assert plan["status"] == audit["status"] == action["status"] == encoding["status"] == "PASS"
    assert file_sha(args.input_source) == plan["input_source_sha256"] == audit["input_source_sha256"]
    assert file_sha(args.closure_source) == audit["source_file_sha256"]
    semantic = closure.pop("semantic_payload_sha256")
    assert semantic_sha(closure) == semantic == audit["source_semantic_payload_sha256"]
    closure["semantic_payload_sha256"] = semantic

    deltas = [(i, j) for i in range(L) for j in range(M)]
    expected_blocks = set()
    block_orbits = collections.Counter()
    parent_block_keys = [block_key(block) for block in source["blocks"]]
    for key in parent_block_keys:
        orbit = {translate_block_key(key, delta) for delta in deltas}
        expected_blocks.update(orbit)
        block_orbits[len(orbit)] += 1
    observed_block_keys = [block_key(block) for block in closure["blocks"]]
    observed_blocks = set(observed_block_keys)
    assert len(observed_blocks) == len(observed_block_keys) == plan["block_closure_unique"]
    assert observed_blocks == expected_blocks
    assert {str(key): value for key, value in sorted(block_orbits.items())} == \
        plan["block_orbit_size_histogram_per_parent"]

    # Independently verify each output provenance record maps its cited parent.
    block_provenance_cases = 0
    for block in closure["blocks"]:
        parent_index = int(block["source_id"].split("-p", 1)[1].split("-d", 1)[0])
        delta_part = block["source_id"].rsplit("-d", 1)[1]
        delta = tuple(map(int, delta_part.split("_")))
        assert block_key(block) == translate_block_key(parent_block_keys[parent_index], delta)
        block_provenance_cases += 1

    expected_selectors = set()
    selector_orbits = collections.Counter()
    parent_selector_keys = [selector_key(selector) for selector in source["selectors"]]
    for key in parent_selector_keys:
        orbit = {translate_selector_key(key, delta) for delta in deltas}
        expected_selectors.update(orbit)
        selector_orbits[len(orbit)] += 1
    observed_selector_keys = [selector_key(selector) for selector in closure["selectors"]]
    observed_selectors = set(observed_selector_keys)
    assert len(observed_selectors) == len(observed_selector_keys) == plan["selector_closure_unique"]
    assert observed_selectors == expected_selectors
    assert {str(key): value for key, value in sorted(selector_orbits.items())} == \
        plan["selector_orbit_size_histogram_per_parent"]
    selector_provenance_cases = 0
    selector_hash_cases = 0
    for selector in closure["selectors"]:
        identifier = selector["mechanism_id"]
        parent_index = int(identifier.split("-p", 1)[1].split("-d", 1)[0])
        delta = tuple(map(int, identifier.rsplit("-d", 1)[1].split("_")))
        assert selector_key(selector) == translate_selector_key(parent_selector_keys[parent_index], delta)
        assert selector["selector_semantic_sha256"] == selector_semantic_hash(selector)
        assert len(selector["selected_names"]) == len(set(selector["selected_names"])) == \
            selector["fault_count"] <= 10
        selector_provenance_cases += 1
        selector_hash_cases += 1

    # Generator invariance is enough for every element of the finite product group.
    generator_invariance_block_cases = 0
    generator_invariance_selector_cases = 0
    for generator in ((1, 0), (0, 1)):
        for key in observed_blocks:
            assert translate_block_key(key, generator) in observed_blocks
            generator_invariance_block_cases += 1
        for key in observed_selectors:
            assert translate_selector_key(key, generator) in observed_selectors
            generator_invariance_selector_cases += 1

    assert encoding["reviewed_blocks"] == len(observed_blocks)
    assert encoding["efssc_selectors"] == len(observed_selectors)
    assert encoding["source_semantic_payload_sha256"] == semantic
    result = {
        "schema": "circdist-gross-round102-independent-full-translation-closure-check-v1",
        "status": "PASS",
        "group": {"name": "Z_12 x Z_6", "order": 72,
                  "generators": [[1, 0], [0, 1]]},
        "blocks": {
            "parent_records": len(parent_block_keys),
            "parent_translation_pairs": len(parent_block_keys) * len(deltas),
            "unique_semantics": len(observed_blocks),
            "collisions": len(parent_block_keys) * len(deltas) - len(observed_blocks),
            "provenance_cases": block_provenance_cases,
            "generator_invariance_cases": generator_invariance_block_cases,
            "exact_expected_observed_set_equality": True,
        },
        "selectors": {
            "parent_records": len(parent_selector_keys),
            "parent_translation_pairs": len(parent_selector_keys) * len(deltas),
            "unique_semantics": len(observed_selectors),
            "collisions": len(parent_selector_keys) * len(deltas) - len(observed_selectors),
            "provenance_cases": selector_provenance_cases,
            "semantic_hash_cases": selector_hash_cases,
            "generator_invariance_cases": generator_invariance_selector_cases,
            "exact_expected_observed_set_equality": True,
        },
        "encoding_link": {
            "status": "PASS",
            "cnf_sha256": encoding["cnf_sha256"],
            "variables": encoding["variables"],
            "clauses": encoding["clauses"],
            "assertions": encoding["assertions"],
        },
        "action_link": {
            "status": "PASS",
            "edge_composition_cases": action["group_action"]["edge_composition_cases"],
            "direct_column_equivariance_cases": action["group_action"]["direct_column_equivariance_cases"],
        },
        "finite_coverage": "the output is exactly the semantic orbit closure, is invariant under both generators, and every record has a checked inverse-action provenance",
        "collision_handling": "full tuples decide set identity; semantic hashes are checked labels only",
        "source_file_sha256": file_sha(args.closure_source),
        "source_semantic_payload_sha256": semantic,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
