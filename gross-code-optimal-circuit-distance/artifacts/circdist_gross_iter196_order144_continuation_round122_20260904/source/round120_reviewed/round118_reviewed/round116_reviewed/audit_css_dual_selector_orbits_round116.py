#!/usr/bin/env python3
"""Audit CSS images of possibly nonfree direct-selector translation orbits."""
from __future__ import annotations

import argparse
import gzip
import hashlib
import json
from pathlib import Path

import independent_iter193_direct_audit_round116 as g

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
    return f"{'Z' if kind == 'X' else 'X'}:{neg(check)}:{dq(q)}"


def dmask(value):
    out = 0
    for q in g.bits(value):
        out |= 1 << dq(q)
    return out


def skey(selector):
    return (
        str(selector["sector"]),
        tuple(sorted(map(int, selector["data_support"]))),
        tuple(sorted((int(c), tuple(sorted(map(int, kinds)))) for c, kinds in selector["group_kinds"].items())),
    )


def key_tuple(value):
    return (str(value[0]), tuple(map(int, value[1])), tuple((int(c), tuple(map(int, kinds))) for c, kinds in value[2]))


def key_json(key):
    return [key[0], list(key[1]), [[c, list(kinds)] for c, kinds in key[2]]]


def tkey(key, delta):
    sector, data, groups = key
    return (
        sector,
        tuple(sorted(tq(q, delta) for q in data)),
        tuple(sorted((add(c, delta), kinds) for c, kinds in groups)),
    )


def dkey(key):
    sector, data, groups = key
    return (
        "Zerr" if sector == "Xerr" else "Xerr",
        tuple(sorted(dq(q) for q in data)),
        tuple(sorted((neg(c), kinds) for c, kinds in groups)),
    )


def semantic(key):
    sector, data, groups = key
    names = [f"D:{q}" for q in data]
    group_dict = {str(c): list(kinds) for c, kinds in groups}
    for c, kinds in groups:
        names.extend(f"R:{c}:{kind}" for kind in kinds)
    obj = {"sector": sector, "selected_names": names, "data_support": list(data), "group_kinds": group_dict}
    return obj, csha(obj)


def replay(key, times, logical_duals):
    context = g.reconstruct_sector(key[0], times)
    indices = list(key[1]) + [144 + 3 * c + kind for c, kinds in key[2] for kind in kinds]
    assert len(indices) == len(set(indices)) <= 10
    canonical = physical = 0
    for index in indices:
        column = context["columns"][index]
        canonical ^= g.mask(column["support"])
        physical ^= g.mask(column["physical_support"])
    canonical_syndrome = context["syndrome"](canonical)
    physical_syndrome = context["syndrome"](physical)
    canonical_logical = [g.parity(canonical, dual) for dual in logical_duals]
    physical_logical = [g.parity(physical, dual) for dual in logical_duals]
    assert canonical_syndrome == physical_syndrome == 0
    assert canonical_logical == physical_logical and any(canonical_logical)
    assert not g.inspan(canonical, context["stabilizers"])
    assert not g.inspan(physical, context["stabilizers"])
    return {
        "selected_indices": indices,
        "fault_count": len(indices),
        "canonical_support": g.bits(canonical),
        "physical_support": g.bits(physical),
        "syndrome": [],
        "logical_parities": canonical_logical,
        "canonical_nonstabilizer": True,
        "physical_nonstabilizer": True,
    }


ap = argparse.ArgumentParser()
ap.add_argument("--source", type=Path, required=True)
ap.add_argument("--candidate", type=Path, required=True)
ap.add_argument("--direct-root", type=Path, required=True)
ap.add_argument("--x-audit", type=Path, required=True)
ap.add_argument("--z-audit", type=Path, required=True)
ap.add_argument("--css-audit", type=Path, required=True)
ap.add_argument("--output", type=Path, required=True)
a = ap.parse_args()

with gzip.open(a.source, "rt") as stream:
    source = json.load(stream)
candidate = json.loads(a.candidate.read_text())
times = {str(name): int(value) for name, value in candidate["compressed_times"].items()}
g.audit_schedule(times)
css = json.loads(a.css_audit.read_text())
assert css["status"] == "PASS" and css["bindings"]["source_sha256"] == fsha(a.source)

installed = {skey(selector) for selector in source["selectors"]}
assert len(installed) == len(source["selectors"])
legacy_missing = {dkey(key) for key in installed} - installed
assert len(legacy_missing) == css["selectors"]["missing_dual_image_count"]
future_base = installed | legacy_missing
assert all(tkey(key, gen) in future_base for key in future_base for gen in GENERATORS)
assert {dkey(key) for key in future_base} == future_base

loaded = []
for path, sector in ((a.x_audit, "Xerr"), (a.z_audit, "Zerr")):
    audit = json.loads(path.read_text())
    assert audit["status"] == "PASS" and audit["sector"] == sector and audit["accepted_collision_free"]
    orbit = {key_tuple(row["selector_key"]) for row in audit["orbit_rows"]}
    parent = key_tuple(audit["parent_selector_key"])
    assert len(orbit) == audit["orbit_size"] and parent in orbit and not (orbit & installed)
    assert orbit == {tkey(parent, delta) for delta in DELTAS}
    loaded.append((path, audit, parent, orbit))

dual_times = {de(name): value for name, value in times.items()}
g.audit_schedule(dual_times)
entries = []
raw_sets = []
for path, audit, parent, orbit in loaded:
    dual_parent = dkey(parent)
    target = dual_parent[0]
    columns = json.loads((a.direct_root / "direct360" / target).with_suffix(".columns.json").read_text())
    logical_duals = [g.mask(row["support"]) for row in columns["logical_duals"]]
    dual_orbit = {tkey(dual_parent, delta) for delta in DELTAS}
    assert dual_orbit == {dkey(key) for key in orbit} and len(dual_orbit) == len(orbit)
    stabilizer = [list(delta) for delta in DELTAS if tkey(dual_parent, delta) == dual_parent]
    rows = []
    parent_replay = None
    for delta in DELTAS:
        schedule = {te(name, delta): value for name, value in dual_times.items()}
        schedule_audit = g.audit_schedule(schedule)
        key = tkey(dual_parent, delta)
        semantic_obj, digest = semantic(key)
        mechanism = replay(key, schedule, logical_duals)
        row = {
            "delta": list(delta),
            "selector_key": key_json(key),
            "selector_semantic_sha256": digest,
            "selected_names": semantic_obj["selected_names"],
            "group_kinds": semantic_obj["group_kinds"],
            "translated_dual_schedule_sha256": csha(schedule),
            "used_layers": schedule_audit["used_layers"],
            **mechanism,
        }
        rows.append(row)
        if delta == (0, 0):
            parent_replay = mechanism
    assert parent_replay is not None
    original_replay = audit["parent_replay"]
    assert parent_replay["canonical_support"] == g.bits(dmask(g.mask(original_replay["canonical_support"])))
    assert parent_replay["physical_support"] == g.bits(dmask(g.mask(original_replay["physical_support"])))
    entries.append({
        "source_sector": audit["sector"],
        "target_sector": target,
        "source_audit_sha256": fsha(path),
        "source_parent_selector_key": key_json(parent),
        "dual_parent_selector_key": key_json(dual_parent),
        "dual_parent_semantic_sha256": semantic(dual_parent)[1],
        "orbit_size": len(dual_orbit),
        "stabilizer_size": len(stabilizer),
        "stabilizer_deltas": stabilizer,
        "translated_replay_count": len(rows),
        "parent_support_is_exact_D_image": True,
        "translated_replays": rows,
    })
    raw_sets.extend(((audit["sector"] + "_original", orbit), (target + "_dual_of_" + audit["sector"], dual_orbit)))

# Translation orbits are equal or disjoint.  Deduplicate equal CSS-self-paired orbits.
for i, (left_label, left) in enumerate(raw_sets):
    for right_label, right in raw_sets[:i]:
        overlap = left & right
        assert not overlap or left == right, (left_label, right_label, len(overlap))
unique_orbits = []
for label, orbit in raw_sets:
    prior = next((row for row in unique_orbits if row["set"] == orbit), None)
    if prior:
        prior["labels"].append(label)
    else:
        unique_orbits.append({"labels": [label], "set": orbit})

assert all(not (row["set"] & future_base) for row in unique_orbits)
candidate_union = set().union(*(row["set"] for row in unique_orbits))
final_set = future_base | candidate_union
assert all(tkey(key, gen) in final_set for key in final_set for gen in GENERATORS)
assert {dkey(key) for key in final_set} == final_set

orbit_summary = []
for row in unique_orbits:
    orbit = row["set"]
    representative = min(orbit)
    stabilizer = [list(delta) for delta in DELTAS if tkey(representative, delta) == representative]
    orbit_summary.append({
        "labels": sorted(row["labels"]),
        "representative": key_json(representative),
        "orbit_size": len(orbit),
        "stabilizer_size": len(stabilizer),
        "stabilizer_deltas": stabilizer,
        "selector_keys": [key_json(key) for key in sorted(orbit)],
    })

out = {
    "schema": "circdist-gross-round116-css-dual-selector-orbits-v1",
    "status": "PASS",
    "bindings": {
        "source_sha256": fsha(a.source),
        "candidate_sha256": fsha(a.candidate),
        "candidate_schedule_sha256": candidate["compressed_schedule_sha256"],
        "css_audit_sha256": fsha(a.css_audit),
        "x_audit_sha256": fsha(a.x_audit),
        "z_audit_sha256": fsha(a.z_audit),
    },
    "installed_selectors": len(installed),
    "legacy_missing_dual_selectors": len(legacy_missing),
    "future_base_selectors": len(future_base),
    "raw_candidate_orbit_labels": len(raw_sets),
    "distinct_candidate_translation_orbits": len(unique_orbits),
    "new_candidate_selectors": len(candidate_union),
    "final_selector_count": len(final_set),
    "all_candidate_orbits_collision_free_against_css_closed_base": True,
    "all_distinct_candidate_orbits_pairwise_disjoint": True,
    "all_dual_schedules_legal": True,
    "all_dual_mechanisms_weight_at_most_10_zero_syndrome_nonstabilizer": True,
    "final_registry_translation_closed": True,
    "final_registry_css_closed": True,
    "orbit_summary": orbit_summary,
    "dual_results": entries,
}
a.output.parent.mkdir(parents=True, exist_ok=True)
a.output.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n")
print(json.dumps({k: out[k] for k in ("status", "legacy_missing_dual_selectors", "distinct_candidate_translation_orbits", "new_candidate_selectors", "final_selector_count", "final_registry_css_closed")}, sort_keys=True))
