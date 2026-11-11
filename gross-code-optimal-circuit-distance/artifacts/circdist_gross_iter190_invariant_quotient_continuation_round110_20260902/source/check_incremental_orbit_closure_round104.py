#!/usr/bin/env python3
"""Independent check of the iteration-187 -> 188 invariant registry update."""
from __future__ import annotations

import argparse
import gc
import gzip
import hashlib
import json
from pathlib import Path

import independent_iter187_direct_audit as geometry

L, M, G = 12, 6, 72


def canonical_sha(obj):
    h = hashlib.sha256()
    encoder = json.JSONEncoder(sort_keys=True, separators=(",", ":"))
    for chunk in encoder.iterencode(obj):
        h.update(chunk.encode())
    return h.hexdigest()


def file_sha(path):
    h = hashlib.sha256()
    with Path(path).open("rb") as f:
        for chunk in iter(lambda: f.read(8 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def load_gz(path):
    with gzip.open(path, "rt") as f:
        return json.load(f)


def add(index, delta):
    i, j = divmod(int(index), M)
    return ((i + delta[0]) % L) * M + ((j + delta[1]) % M)


def tq(q, delta):
    q = int(q)
    return add(q, delta) if q < G else G + add(q - G, delta)


def te(name, delta):
    kind, check, q = name.split(":")
    return f"{kind}:{add(check, delta)}:{tq(q, delta)}"


def selector_key(selector):
    return (str(selector["sector"]), tuple(sorted(map(int, selector["data_support"]))),
            tuple(sorted((int(check), tuple(sorted(map(int, kinds))))
                         for check, kinds in selector["group_kinds"].items())))


def translate_selector_key(key, delta):
    sector, data, groups = key
    return (sector, tuple(sorted(tq(q, delta) for q in data)),
            tuple(sorted((add(check, delta), kinds) for check, kinds in groups)))


def selector_semantics(key):
    sector, data, groups = key
    names = [f"D:{q}" for q in data]
    group_dict = {str(check): list(kinds) for check, kinds in groups}
    for check, kinds in groups:
        names.extend(f"R:{check}:{kind}" for kind in kinds)
    semantic = {"sector": sector, "selected_names": names,
                "data_support": list(data), "group_kinds": group_dict}
    return canonical_sha(semantic), names, group_dict


def block_key(block):
    return tuple(sorted((str(atom[0]), str(atom[1])) for atom in block["atoms"]))


def block_digest(key):
    return canonical_sha(key)


def translated_block_key(key, delta):
    return tuple(sorted((te(left, delta), te(right, delta)) for left, right in key))


def validate_selectors(selectors):
    keys = []
    hashes = set()
    serialized = []
    for selector in selectors:
        key = selector_key(selector)
        digest, names, group_dict = selector_semantics(key)
        assert selector["selector_semantic_sha256"] == digest
        assert selector["selected_names"] == names
        assert selector["data_support"] == list(key[1])
        assert selector["group_kinds"] == group_dict
        assert len(names) == len(set(names)) == selector["fault_count"] <= 10
        assert digest not in hashes
        hashes.add(digest)
        keys.append(key)
        serialized.append(canonical_sha(selector))
    assert len(set(keys)) == len(keys)
    return keys, serialized


def semantic_payload_check(source):
    claimed = source.pop("semantic_payload_sha256")
    observed = canonical_sha(source)
    source["semantic_payload_sha256"] = claimed
    assert observed == claimed
    return observed


def mechanism_key(label, selected_names):
    data, groups = [], {}
    for name in selected_names:
        fields = name.split(":")
        if fields[0] == "D":
            data.append(int(fields[1]))
        else:
            assert fields[0] == "R"
            groups.setdefault(int(fields[1]), []).append(int(fields[2]))
    return (label, tuple(sorted(data)),
            tuple(sorted((check, tuple(sorted(kinds))) for check, kinds in groups.items())))


def replay_named(key, sector):
    selected = list(key[1]) + [144 + 3 * check + kind
                               for check, kinds in key[2] for kind in kinds]
    assert len(selected) == len(set(selected)) == 10
    canonical = physical = 0
    for index in selected:
        column = sector["columns"][index]
        canonical ^= geometry.mask(column["support"])
        physical ^= geometry.mask(column["physical_support"])
    assert sector["syndrome"](canonical) == sector["syndrome"](physical) == 0
    assert not geometry.inspan(canonical, sector["stabilizers"])
    assert not geometry.inspan(physical, sector["stabilizers"])
    return {"fault_count": 10, "canonical_net_support": geometry.bits(canonical),
            "physical_net_support": geometry.bits(physical), "syndrome": [],
            "canonical_nonstabilizer": True, "physical_nonstabilizer": True}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", type=Path, required=True)
    ap.add_argument("--output", type=Path, required=True)
    args = ap.parse_args()
    root = args.root.resolve()
    old_path = root / "inputs/round102/frontier/iter187_full_invariant/source.json.gz"
    new_path = root / "frontier/iter188_full_invariant/source.json.gz"
    old = load_gz(old_path)
    assert old["schema"] == "circdist-gross-iteration187-full-translation-closure-finite-source-v1"
    assert len(old["blocks"]) == 517140 and len(old["selectors"]) == 24012
    old_semantic = semantic_payload_check(old)
    old_block_stream_sha = canonical_sha(old["blocks"])
    fixed_names = ["data_incidence", "edges", "frozen_semantics", "overlaps",
                   "residual_positions", "sector_definitions", "x_checks", "z_checks"]
    old_fixed = {name: canonical_sha(old[name]) for name in fixed_names}
    old_keys, old_serialized = validate_selectors(old["selectors"])
    old_key_set = set(old_keys)
    del old
    gc.collect()

    new = load_gz(new_path)
    assert new["schema"] == "circdist-gross-iteration188-full-translation-closure-finite-source-v1"
    assert len(new["blocks"]) == 517140 and len(new["selectors"]) == 24156
    new_semantic = semantic_payload_check(new)
    assert canonical_sha(new["blocks"]) == old_block_stream_sha
    assert all(canonical_sha(new[name]) == old_fixed[name] for name in fixed_names)
    new_keys, new_serialized = validate_selectors(new["selectors"])
    assert new_serialized[:len(old_serialized)] == old_serialized
    new_key_set = set(new_keys)
    assert old_key_set < new_key_set and len(new_key_set - old_key_set) == 144
    assert new["expected"]["reviewed_blocks"] == 517140
    assert new["expected"]["selectors"] == 24156
    assert new["expected"]["assertions"] == 4398 + 517140 + 24156 == 545694

    # Check the entire block formula registry under the two group generators.
    block_hashes = set()
    block_keys = []
    for block in new["blocks"]:
        key = block_key(block)
        digest = block_digest(key)
        assert digest not in block_hashes
        block_hashes.add(digest)
        block_keys.append(key)
    assert len(block_hashes) == 517140
    block_generator_cases = 0
    for delta in ((1, 0), (0, 1)):
        for key in block_keys:
            assert block_digest(translated_block_key(key, delta)) in block_hashes
            block_generator_cases += 1

    candidate = json.loads((root / "solver/iter187/candidate.json").read_text())
    direct = json.loads((root / "solver/iter187/direct/direct_verification.json").read_text())
    times = {str(k): int(v) for k, v in candidate["compressed_times"].items()}
    assert canonical_sha(times) == candidate["compressed_schedule_sha256"]
    parent_keys = {label: mechanism_key(label, direct["sectors"][label]["mechanism"]["selected_names"])
                   for label in ("Xerr", "Zerr")}
    expected = {}
    schedule_rows = []
    physical_rows = []
    for delta in ((i, j) for i in range(L) for j in range(M)):
        translated_times = {te(name, delta): value for name, value in times.items()}
        schedule_audit = geometry.audit_schedule(translated_times)
        schedule_sha = canonical_sha(translated_times)
        schedule_rows.append({"delta": list(delta), "schedule_sha256": schedule_sha,
                              "used_layers": schedule_audit["used_layers"],
                              "max_time": schedule_audit["max_time"]})
        sectors = {label: geometry.reconstruct_sector(label, translated_times)
                   for label in ("Xerr", "Zerr")}
        for label in ("Xerr", "Zerr"):
            key = translate_selector_key(parent_keys[label], delta)
            assert key not in expected
            digest, names, _ = selector_semantics(key)
            expected[key] = {"sector": label, "delta": list(delta),
                             "selector_semantic_sha256": digest,
                             "selected_names": names, "source_schedule_sha256": schedule_sha}
            replay = replay_named(key, sectors[label])
            physical_rows.append({**expected[key], **replay})
    assert len(expected) == 144 and set(expected) == new_key_set - old_key_set
    by_key = {selector_key(selector): selector for selector in new["selectors"]}
    for key, row in expected.items():
        selector = by_key[key]
        assert selector["source_iteration"] == 187
        assert selector["origin"] == "round104_iter187_candidate_translation_orbit"
        assert selector["translation_delta"] == row["delta"]
        assert selector["selector_semantic_sha256"] == row["selector_semantic_sha256"]
        assert selector["selected_names"] == row["selected_names"]
        assert selector["source_schedule_parent_sha256"] == row["source_schedule_sha256"]
        assert selector["soundness_provenance"] == "direct SAT/physical replay on translated legal source schedule"

    selector_generator_cases = 0
    for delta in ((1, 0), (0, 1)):
        for key in new_key_set:
            assert translate_selector_key(key, delta) in new_key_set
            selector_generator_cases += 1
    state = json.loads((root / "frontier/iter188_full_invariant/state.json").read_text())
    selector_state = canonical_sha([
        {key: selector.get(key) for key in ("mechanism_id", "sector", "selected_names",
                                            "data_support", "group_kinds",
                                            "selector_semantic_sha256")}
        for selector in new["selectors"]])
    assert state["status"] == "PASS" and state["next_iteration"] == 188
    assert state["started"] is False and state["stop"] is None
    assert state["block_count"] == 517140 and state["selector_count"] == 24156
    assert state["selector_state_sha256"] == selector_state
    assert state["source_file_sha256"] == file_sha(new_path)
    assert state["source_semantic_payload_sha256"] == new_semantic
    audit = json.loads((root / "frontier/iter188_full_invariant/orbit_audit.json").read_text())
    assert audit["status"] == "PASS" and audit["parent_orbit_sizes"] == {"Xerr": 72, "Zerr": 72}
    assert audit["parent_translation_pairs"] == 144 and audit["new_unique_selectors"] == 144
    assert audit["collision_count"] == 0 and audit["generator_invariance_cases"] == selector_generator_cases
    assert audit["source_file_sha256"] == file_sha(new_path)
    assert audit["source_semantic_payload_sha256"] == new_semantic
    assert audit["state_file_sha256"] == file_sha(root / "frontier/iter188_full_invariant/state.json")
    assert audit["selector_state_sha256"] == selector_state
    result = {
        "schema": "circdist-gross-round104-independent-incremental-orbit-closure-check-v1",
        "status": "PASS", "old_source_sha256": file_sha(old_path),
        "old_semantic_payload_sha256": old_semantic,
        "new_source_sha256": file_sha(new_path), "new_semantic_payload_sha256": new_semantic,
        "block_registry": {"old_count": 517140, "new_count": 517140,
                           "byte_semantic_stream_sha256": old_block_stream_sha,
                           "unique_formula_digests": len(block_hashes),
                           "generator_invariance_cases": block_generator_cases},
        "selector_registry": {"old_count": 24012, "new_count": 24156,
                              "prefix_exact": True, "added": 144, "collisions": 0,
                              "parent_orbit_sizes": {"Xerr": 72, "Zerr": 72},
                              "generator_invariance_cases": selector_generator_cases,
                              "selector_state_sha256": selector_state},
        "translated_schedule_replays": len(schedule_rows),
        "translated_physical_mechanism_replays": len(physical_rows),
        "all_translated_schedules_legal": True,
        "all_translated_mechanisms_weight10_zero_syndrome_nonstabilizer": True,
        "fresh_state": {"iteration": 188, "started": False, "stop": None,
                        "source_sha256": state["source_file_sha256"]}}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
