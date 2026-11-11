#!/usr/bin/env python3
"""Build deterministic iteration 198 with full order-144 closure and new sound exclusions."""
from __future__ import annotations

import argparse
import collections
import gzip
import hashlib
import io
import json
from pathlib import Path

L, M, G = 12, 6, 72
DELTAS = tuple((i, j) for i in range(L) for j in range(M))
GENERATORS = ((1, 0), (0, 1))


def csha(obj):
    return hashlib.sha256(json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def fsha(path):
    h = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for chunk in iter(lambda: stream.read(8 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def write_gz(path, obj):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("wb") as raw:
        with gzip.GzipFile(filename="", mode="wb", fileobj=raw, compresslevel=9, mtime=0) as encoded:
            with io.TextIOWrapper(encoded, encoding="utf-8", newline="\n") as text:
                json.dump(obj, text, sort_keys=True, separators=(",", ":"))
                text.write("\n")


def add(value, delta):
    i, j = divmod(int(value), M)
    return ((i + delta[0]) % L) * M + (j + delta[1]) % M


def neg(value):
    i, j = divmod(int(value), M)
    return ((-i) % L) * M + ((-j) % M)


def tq(q, delta):
    q = int(q)
    return add(q, delta) if q < G else G + add(q - G, delta)


def dq(q):
    q = int(q)
    return G + neg(q) if q < G else neg(q - G)


def te(name, delta):
    kind, check, q = name.split(":")
    return f"{kind}:{add(check, delta)}:{tq(q, delta)}"


def de(name):
    kind, check, q = name.split(":")
    assert kind in ("X", "Z")
    return f"{'Z' if kind == 'X' else 'X'}:{neg(check)}:{dq(q)}"


def bkey(block):
    return tuple(sorted((str(left), str(right)) for left, right in block["atoms"]))


def tb(key, delta):
    return tuple(sorted((te(left, delta), te(right, delta)) for left, right in key))


def db(key):
    return tuple(sorted((de(left), de(right)) for left, right in key))


def bjson(key):
    return [[left, right] for left, right in key]


def skey(selector):
    return (
        str(selector["sector"]),
        tuple(sorted(map(int, selector["data_support"]))),
        tuple(sorted((int(c), tuple(sorted(map(int, kinds)))) for c, kinds in selector["group_kinds"].items())),
    )


def ts(key, delta):
    sector, data, groups = key
    return (
        sector,
        tuple(sorted(tq(q, delta) for q in data)),
        tuple(sorted((add(c, delta), kinds) for c, kinds in groups)),
    )


def ds(key):
    sector, data, groups = key
    return (
        "Zerr" if sector == "Xerr" else "Xerr",
        tuple(sorted(dq(q) for q in data)),
        tuple(sorted((neg(c), kinds) for c, kinds in groups)),
    )


def kt(value):
    return (str(value[0]), tuple(map(int, value[1])), tuple((int(c), tuple(map(int, kinds))) for c, kinds in value[2]))


def kjson(key):
    return [key[0], list(key[1]), [[c, list(kinds)] for c, kinds in key[2]]]


def sem(key):
    sector, data, groups = key
    names = [f"D:{q}" for q in data]
    group_dict = {str(c): list(kinds) for c, kinds in groups}
    for c, kinds in groups:
        names.extend(f"R:{c}:{kind}" for kind in kinds)
    obj = {"sector": sector, "selected_names": names, "data_support": list(data), "group_kinds": group_dict}
    return obj, csha(obj)


def partition(keys, action):
    remaining = set(keys)
    parts = []
    while remaining:
        seed = min(remaining)
        orbit = {action(seed, delta) for delta in DELTAS}
        assert orbit <= set(keys)
        parts.append((min(orbit), orbit))
        remaining -= orbit
    return sorted(parts, key=lambda row: row[0])


def realizers(rep, key, action):
    return [list(delta) for delta in DELTAS if action(rep, delta) == key]


ap = argparse.ArgumentParser()
ap.add_argument("--source", type=Path, required=True)
ap.add_argument("--state", type=Path, required=True)
ap.add_argument("--candidate", type=Path, required=True)
ap.add_argument("--css-audit", type=Path, required=True)
ap.add_argument("--x-audit", type=Path, required=True)
ap.add_argument("--z-audit", type=Path, required=True)
ap.add_argument("--dual-audit", type=Path, required=True)
ap.add_argument("--canonical-yaml", type=Path, required=True)
ap.add_argument("--scheduler", type=Path, required=True)
ap.add_argument("--review", type=Path, required=True)
ap.add_argument("--prior-manifest", type=Path, required=True)
ap.add_argument("--proofpilot", type=Path, required=True)
ap.add_argument("--output-source", type=Path, required=True)
ap.add_argument("--output-state", type=Path, required=True)
ap.add_argument("--output-audit", type=Path, required=True)
a = ap.parse_args()

with gzip.open(a.source, "rt") as stream:
    source = json.load(stream)
state = json.loads(a.state.read_text())
candidate = json.loads(a.candidate.read_text())
css = json.loads(a.css_audit.read_text())
xa = json.loads(a.x_audit.read_text())
za = json.loads(a.z_audit.read_text())
dual = json.loads(a.dual_audit.read_text())
assert state["source_file_sha256"] == fsha(a.source)
assert css["status"] == xa["status"] == za["status"] == dual["status"] == "PASS"
assert css["bindings"]["source_sha256"] == fsha(a.source)
assert dual["bindings"]["source_sha256"] == fsha(a.source)
assert dual["final_registry_css_closed"] and dual["final_registry_translation_closed"]
assert xa["bindings"]["candidate_schedule_sha256"] == za["bindings"]["candidate_schedule_sha256"] == candidate["compressed_schedule_sha256"]

claimed_semantic = source.pop("semantic_payload_sha256")
assert csha(source) == claimed_semantic == state["source_semantic_payload_sha256"]
old_blocks = list(source["blocks"])
old_selectors = list(source["selectors"])
old_bkeys = [bkey(block) for block in old_blocks]
old_skeys = [skey(selector) for selector in old_selectors]
old_bset, old_sset = set(old_bkeys), set(old_skeys)
assert len(old_bkeys) == len(old_bset) == 814392
assert len(old_skeys) == len(old_sset) == 51552
assert all(tb(key, gen) in old_bset for key in old_bset for gen in GENERATORS)
assert all(ts(key, gen) in old_sset for key in old_sset for gen in GENERATORS)

# Close the exact inherited nonfree D-image gaps.  Every image has a unique D-parent.
bparent = {key: (index, block) for index, (key, block) in enumerate(zip(old_bkeys, old_blocks))}
sparent = {key: (index, selector) for index, (key, selector) in enumerate(zip(old_skeys, old_selectors))}
missing_blocks = {db(key) for key in old_bset} - old_bset
missing_selectors = {ds(key) for key in old_sset} - old_sset
bparts = partition(missing_blocks, tb)
sparts = partition(missing_selectors, ts)
assert len(missing_blocks) == 0 and len(bparts) == 0
assert len(missing_selectors) == 0 and len(sparts) == 0

blocks = list(old_blocks)
family_next = collections.Counter(block["family"] for block in blocks)
new_block_family = collections.Counter()
block_orbit_rows = []
for orbit_index, (rep, orbit) in enumerate(bparts):
    stabilizer = realizers(rep, rep, tb)
    assert len(stabilizer) == 2
    families = {bparent[db(key)][1]["family"] for key in orbit}
    assert len(families) == 1
    added = []
    for key in sorted(orbit):
        parent_index, parent = bparent[db(key)]
        family = parent["family"]
        deltas = realizers(rep, key, tb)
        assert len(deltas) == 2
        record = {
            "atoms": bjson(key),
            "family": family,
            "family_index": family_next[family],
            "source_id": f"r124-cssclosure-block-o{orbit_index}-k{len(added)}",
            "source_iteration": 197,
            "round124_translation_orbit_id": f"r124-cssclosure-block-o{orbit_index}",
            "round124_translation_orbit_representative_sha256": csha(bjson(rep)),
            "round124_translation_realizing_deltas": deltas,
            "round124_translation_stabilizer_deltas": stabilizer,
            "css_duality_parent_index": parent_index,
            "css_duality_parent_source_id": parent["source_id"],
            "css_duality_parent_semantic_sha256": csha(bjson(db(key))),
            "css_duality_action": "X:c:q <-> Z:-c:D(q)",
            "soundness_provenance": "exact CSS-duality transport of inherited reviewed sound order exclusion; complete nonfree size-36 orbit installed once per semantic key",
        }
        blocks.append(record)
        family_next[family] += 1
        new_block_family[family] += 1
        added.append(csha(bjson(key)))
    block_orbit_rows.append({
        "orbit_id": f"r124-cssclosure-block-o{orbit_index}",
        "representative_sha256": csha(bjson(rep)),
        "orbit_size": len(orbit),
        "stabilizer_size": len(stabilizer),
        "stabilizer_deltas": stabilizer,
        "family": next(iter(families)),
        "member_semantic_sha256": added,
    })

selectors = list(old_selectors)
selector_orbit_rows = []
new_selector_sector = collections.Counter()
for orbit_index, (rep, orbit) in enumerate(sparts):
    stabilizer = realizers(rep, rep, ts)
    assert len(stabilizer) == 2
    added = []
    for key in sorted(orbit):
        parent_index, parent = sparent[ds(key)]
        semantic, digest = sem(key)
        deltas = realizers(rep, key, ts)
        assert len(deltas) == 2
        record = {
            "mechanism_id": f"r124-cssclosure-selector-o{orbit_index}-k{len(added)}",
            "source_iteration": 197,
            "sector": key[0],
            "fault_count": len(semantic["selected_names"]),
            "selected_names": semantic["selected_names"],
            "data_support": semantic["data_support"],
            "group_kinds": semantic["group_kinds"],
            "selector_semantic_sha256": digest,
            "origin": "round124_exact_nonfree_css_registry_closure",
            "round124_translation_orbit_id": f"r124-cssclosure-selector-o{orbit_index}",
            "round124_translation_orbit_representative_semantic_sha256": sem(rep)[1],
            "round124_translation_realizing_deltas": deltas,
            "round124_translation_stabilizer_deltas": stabilizer,
            "css_duality_parent_index": parent_index,
            "css_duality_parent_mechanism_id": parent["mechanism_id"],
            "css_duality_parent_selector_semantic_sha256": parent["selector_semantic_sha256"],
            "css_duality_action": "Xerr <-> Zerr, q -> D(q), check -> -check, residual kind fixed",
            "soundness_provenance": "exact CSS-duality transport of inherited reviewed selector; complete nonfree size-36 orbit installed once per semantic key",
        }
        selectors.append(record)
        new_selector_sector[key[0]] += 1
        added.append(digest)
    selector_orbit_rows.append({
        "orbit_id": f"r124-cssclosure-selector-o{orbit_index}",
        "representative_semantic_sha256": sem(rep)[1],
        "orbit_size": len(orbit),
        "stabilizer_size": len(stabilizer),
        "stabilizer_deltas": stabilizer,
        "member_semantic_sha256": added,
    })

# Collect the original and CSS-dual candidate orbits from the fully replayed audits.
candidate_specs = []
for tag, audit, schedule_field, audit_path in (
    ("direct-Xerr", xa, "translated_schedule_sha256", a.x_audit),
    ("direct-Zerr", za, "translated_schedule_sha256", a.z_audit),
):
    rows = audit["orbit_rows"]
    row_map = {kt(row["selector_key"]): row for row in rows}
    candidate_specs.append((tag, set(row_map), row_map, fsha(audit_path), audit["parent_selector_semantic_sha256"], schedule_field, "direct"))
for result in dual["dual_results"]:
    tag = f"cssdual-{result['source_sector']}-to-{result['target_sector']}"
    row_map = {}
    for row in result["translated_replays"]:
        row_map.setdefault(kt(row["selector_key"]), row)
    candidate_specs.append((tag, set(row_map), row_map, fsha(a.dual_audit), result["dual_parent_semantic_sha256"], "translated_dual_schedule_sha256", "dual"))

pre_candidate = {skey(selector) for selector in selectors}
candidate_sets = []
for spec_index, (tag, orbit, row_map, audit_sha, parent_digest, schedule_field, origin_kind) in enumerate(candidate_specs):
    assert orbit and not (orbit & pre_candidate)
    rep = min(orbit)
    full = {ts(rep, delta) for delta in DELTAS}
    assert full == orbit
    stabilizer = realizers(rep, rep, ts)
    assert len(orbit) * len(stabilizer) == 72
    added = []
    for key in sorted(orbit):
        semantic, digest = sem(key)
        row = row_map[key]
        assert row["selector_semantic_sha256"] == digest
        deltas = realizers(rep, key, ts)
        assert len(deltas) == len(stabilizer)
        record = {
            "mechanism_id": f"r124-{tag}-k{len(added)}",
            "source_iteration": 197,
            "sector": key[0],
            "fault_count": len(semantic["selected_names"]),
            "selected_names": semantic["selected_names"],
            "data_support": semantic["data_support"],
            "group_kinds": semantic["group_kinds"],
            "selector_semantic_sha256": digest,
            "origin": "round124_iter197_direct_and_css_dual_exact_orbit",
            "round124_translation_orbit_id": f"r124-{tag}",
            "round124_translation_orbit_representative_semantic_sha256": sem(rep)[1],
            "round124_translation_realizing_deltas": deltas,
            "round124_translation_stabilizer_deltas": stabilizer,
            "round124_orbit_audit_sha256": audit_sha,
            "source_schedule_sha256": row[schedule_field],
            "soundness_provenance": "complete unrestricted direct-360 SAT assignment plus canonical and physical replay on every translated legal schedule; CSS images use the independently checked exact involution" if origin_kind == "direct" else "exact CSS-duality image of a complete unrestricted direct-360 SAT mechanism, replayed physically on all 72 translated dual schedules",
        }
        selectors.append(record)
        new_selector_sector[key[0]] += 1
        added.append(digest)
    candidate_sets.append(orbit)
    selector_orbit_rows.append({
        "orbit_id": f"r124-{tag}",
        "representative_semantic_sha256": sem(rep)[1],
        "orbit_size": len(orbit),
        "stabilizer_size": len(stabilizer),
        "stabilizer_deltas": stabilizer,
        "audit_sha256": audit_sha,
        "member_semantic_sha256": added,
    })
    pre_candidate |= orbit

for i, orbit in enumerate(candidate_sets):
    for prior in candidate_sets[:i]:
        assert not (orbit & prior)
assert [len(orbit) for orbit in candidate_sets] == [72, 72, 72, 72]
assert len(blocks) == 814392
assert len(selectors) == 51840
final_bset = {bkey(block) for block in blocks}
final_sset = {skey(selector) for selector in selectors}
assert len(final_bset) == len(blocks) and len(final_sset) == len(selectors)
assert all(tb(key, gen) in final_bset for key in final_bset for gen in GENERATORS)
assert all(ts(key, gen) in final_sset for key in final_sset for gen in GENERATORS)
assert {db(key) for key in final_bset} == final_bset
assert {ds(key) for key in final_sset} == final_sset

# Update source semantic bindings and exact compiler counts.
source["schema"] = "circdist-gross-iteration198-full-translation-closure-finite-source-v1"
source["blocks"] = blocks
source["selectors"] = selectors
source["bindings"].update({
    "round124_canonical_gross_sha256": fsha(a.canonical_yaml),
    "round124_scheduler_sha256": fsha(a.scheduler),
    "round124_review_sha256": fsha(a.review),
    "round124_reviewed_parent_package_manifest_sha256": fsha(a.prior_manifest),
    "round124_proofpilot_sha256": fsha(a.proofpilot),
    "round124_iter197_candidate_schedule_sha256": candidate["compressed_schedule_sha256"],
    "round124_css_duality_audit_sha256": fsha(a.css_audit),
    "round124_xerr_orbit_audit_sha256": fsha(a.x_audit),
    "round124_zerr_orbit_audit_sha256": fsha(a.z_audit),
    "round124_css_dual_orbit_audit_sha256": fsha(a.dual_audit),
    "round124_inherited_nonfree_block_orbits_installed": 0,
    "round124_inherited_nonfree_selector_orbits_installed": 0,
    "round124_candidate_selector_orbit_sizes": [72, 72, 72, 72],
    "round124_registry_action": "(Z_12 x Z_6) semidirect C_2 generated by translations and CSS involution",
    "round124_registry_action_order": 144,
})
expected = source["expected"]
expected["reviewed_blocks"] = len(blocks)
expected["selectors"] = len(selectors)
expected["block_family_counts"] = dict(sorted(collections.Counter(block["family"] for block in blocks).items()))
residual = [set(map(int, values)) for values in source["residual_positions"]]


def positions(kinds):
    out = set()
    for kind in kinds:
        out.symmetric_difference_update(residual[int(kind)])
    return tuple(sorted(out))


members, ranks = set(), set()
for selector in selectors:
    definition = source["sector_definitions"][selector["sector"]]
    for check_string, kinds in selector["group_kinds"].items():
        check = int(check_string)
        pos = positions(kinds)
        for q in definition["checks"][check]:
            members.add((selector["sector"], check, pos, q))
            if pos and pos != tuple(range(6)):
                ranks.add((selector["sector"], check, q))
expected["membership_expressions"] = len(members)
expected["rank_expressions"] = len(ranks)
expected["assertions"] = 4398 + len(blocks) + len(selectors)
source["semantic_payload_sha256"] = csha(source)
write_gz(a.output_source, source)

state_fields = ("mechanism_id", "sector", "selected_names", "data_support", "group_kinds", "selector_semantic_sha256")
selector_state = csha([{key: selector.get(key) for key in state_fields} for selector in selectors])
output_state = {
    "schema": "circdist-gross-round124-css-closed-frontier-state-v1",
    "status": "PASS",
    "next_iteration": 198,
    "started": False,
    "stop": None,
    "block_count": len(blocks),
    "selector_count": len(selectors),
    "selector_state_sha256": selector_state,
    "source_semantic_payload_sha256": source["semantic_payload_sha256"],
    "source_file_sha256": fsha(a.output_source),
    "translation_group": "Z_12 x Z_6",
    "translation_group_order": 72,
    "extended_group": "(Z_12 x Z_6) semidirect C_2",
    "extended_group_order": 144,
    "scope": "fresh checked unstarted iteration-198 source after four sound iter197 mechanism/CSS orbits; no iteration-198 solver disposition",
}
a.output_state.parent.mkdir(parents=True, exist_ok=True)
a.output_state.write_text(json.dumps(output_state, indent=2, sort_keys=True) + "\n")

audit = {
    "schema": "circdist-gross-round124-css-closed-frontier-advance-v1",
    "status": "PASS",
    "bindings": {
        "input_source_sha256": fsha(a.source),
        "input_state_sha256": fsha(a.state),
        "candidate_sha256": fsha(a.candidate),
        "css_audit_sha256": fsha(a.css_audit),
        "x_audit_sha256": fsha(a.x_audit),
        "z_audit_sha256": fsha(a.z_audit),
        "dual_audit_sha256": fsha(a.dual_audit),
    },
    "input": {"blocks": len(old_blocks), "selectors": len(old_selectors)},
    "inherited_nonfree_css_closure": {
        "blocks": len(missing_blocks),
        "block_orbits": len(bparts),
        "selectors": len(missing_selectors),
        "selector_orbits": len(sparts),
        "block_orbits_detail": block_orbit_rows,
        "selector_orbits_detail": selector_orbit_rows[:len(sparts)],
        "new_blocks_by_family": dict(sorted(new_block_family.items())),
    },
    "iter197_mechanism_exclusions": {
        "translation_orbits": len(candidate_sets),
        "orbit_sizes": [len(orbit) for orbit in candidate_sets],
        "selectors": sum(map(len, candidate_sets)),
        "pairwise_disjoint": True,
        "collision_free_against_css_closed_input": True,
        "all_288_group_element_replays_covering_288_distinct_original_and_dual_selectors": True,
        "orbit_detail": selector_orbit_rows[len(sparts):],
        "new_selectors_by_sector_including_inherited_closure": dict(sorted(new_selector_sector.items())),
    },
    "closure": {
        "translation_generators": [[1, 0], [0, 1]],
        "block_generator_cases": len(final_bset) * 2,
        "selector_generator_cases": len(final_sset) * 2,
        "block_css_cases": len(final_bset),
        "selector_css_cases": len(final_sset),
        "translation_closed": True,
        "css_involution_closed": True,
        "extended_action_order": 144,
    },
    "output": {
        "blocks": len(blocks),
        "selectors": len(selectors),
        "assertions": expected["assertions"],
        "membership_expressions": expected["membership_expressions"],
        "rank_expressions": expected["rank_expressions"],
        "block_family_counts": expected["block_family_counts"],
        "source_sha256": fsha(a.output_source),
        "source_semantic_payload_sha256": source["semantic_payload_sha256"],
        "state_sha256": fsha(a.output_state),
        "selector_state_sha256": selector_state,
    },
    "fresh_frontier": {"iteration": 198, "started": False, "solver_invocations": 0},
}
a.output_audit.write_text(json.dumps(audit, indent=2, sort_keys=True) + "\n")
print(json.dumps({
    "status": "PASS",
    "blocks": len(blocks),
    "selectors": len(selectors),
    "assertions": expected["assertions"],
    "membership_expressions": expected["membership_expressions"],
    "rank_expressions": expected["rank_expressions"],
    "source_sha256": audit["output"]["source_sha256"],
    "semantic_sha256": source["semantic_payload_sha256"],
    "state_sha256": audit["output"]["state_sha256"],
    "selector_state_sha256": selector_state,
    "extended_action_order": 144,
}, sort_keys=True))
