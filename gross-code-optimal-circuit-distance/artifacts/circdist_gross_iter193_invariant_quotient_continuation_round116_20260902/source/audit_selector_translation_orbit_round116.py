#!/usr/bin/env python3
"""Audit a possibly nonfree Z12 x Z6 orbit of one direct SAT selector."""
from __future__ import annotations

import argparse
import gzip
import hashlib
import json
from pathlib import Path

import independent_iter193_direct_audit_round116 as g

L, M, G = 12, 6, 72
DELTAS = tuple((i, j) for i in range(L) for j in range(M))


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


def tq(q, delta):
    q = int(q)
    return add(q, delta) if q < G else G + add(q - G, delta)


def te(name, delta):
    kind, check, q = name.split(":")
    return f"{kind}:{add(check, delta)}:{tq(q, delta)}"


def key_from_names(sector, names):
    data, groups = [], {}
    for name in names:
        parts = name.split(":")
        if parts[0] == "D":
            data.append(int(parts[1]))
        else:
            groups.setdefault(int(parts[1]), []).append(int(parts[2]))
    return (sector, tuple(sorted(data)), tuple(sorted((c, tuple(sorted(kinds))) for c, kinds in groups.items())))


def trans_key(key, delta):
    sector, data, groups = key
    return (
        sector,
        tuple(sorted(tq(q, delta) for q in data)),
        tuple(sorted((add(c, delta), kinds) for c, kinds in groups)),
    )


def key_json(key):
    return [key[0], list(key[1]), [[c, list(kinds)] for c, kinds in key[2]]]


def key_tuple(value):
    return (str(value[0]), tuple(map(int, value[1])), tuple((int(c), tuple(map(int, kinds))) for c, kinds in value[2]))


def semantic(key):
    sector, data, groups = key
    names = [f"D:{q}" for q in data]
    group_dict = {str(c): list(kinds) for c, kinds in groups}
    for c, kinds in groups:
        names.extend(f"R:{c}:{kind}" for kind in kinds)
    obj = {"sector": sector, "selected_names": names, "data_support": list(data), "group_kinds": group_dict}
    return csha(obj), names, group_dict


def replay(key, sector_context, logical_duals):
    indices = list(key[1]) + [144 + 3 * c + kind for c, kinds in key[2] for kind in kinds]
    assert len(indices) == len(set(indices)) <= 10
    canonical = physical = 0
    for index in indices:
        column = sector_context["columns"][index]
        canonical ^= g.mask(column["support"])
        physical ^= g.mask(column["physical_support"])
    canonical_syndrome = sector_context["syndrome"](canonical)
    physical_syndrome = sector_context["syndrome"](physical)
    canonical_logical = [g.parity(canonical, dual) for dual in logical_duals]
    physical_logical = [g.parity(physical, dual) for dual in logical_duals]
    assert canonical_syndrome == physical_syndrome == 0
    assert canonical_logical == physical_logical and any(canonical_logical)
    assert not g.inspan(canonical, sector_context["stabilizers"])
    assert not g.inspan(physical, sector_context["stabilizers"])
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
ap.add_argument("--sector", choices=("Xerr", "Zerr"), required=True)
ap.add_argument("--candidate", type=Path, required=True)
ap.add_argument("--source", type=Path, required=True)
ap.add_argument("--direct-root", type=Path, required=True)
ap.add_argument("--cnf", type=Path, required=True)
ap.add_argument("--assignment", type=Path, required=True)
ap.add_argument("--prior-audit", type=Path, action="append", default=[])
ap.add_argument("--output", type=Path, required=True)
a = ap.parse_args()

base = a.direct_root / "direct360" / a.sector
nvars, clauses = g.parse_cnf(a.cnf)
values = g.parse_assignment(a.assignment, nvars)
assert not g.failed_clauses(clauses, values)
selected = [i for i in range(360) if values[i + 1]]
assert len(selected) <= 10
columns = json.loads(base.with_suffix(".columns.json").read_text())
names = [columns["columns"][i]["name"] for i in selected]
parent = key_from_names(a.sector, names)
parent_digest, normalized_names, _ = semantic(parent)
assert normalized_names == names

candidate = json.loads(a.candidate.read_text())
times = {str(name): int(value) for name, value in candidate["compressed_times"].items()}
assert csha(times) == candidate["compressed_schedule_sha256"]
g.audit_schedule(times)
logical_duals = [g.mask(row["support"]) for row in columns["logical_duals"]]
parent_replay = replay(parent, g.reconstruct_sector(a.sector, times), logical_duals)

with gzip.open(a.source, "rt") as stream:
    source = json.load(stream)
installed = {}
for selector in source["selectors"]:
    key = key_from_names(selector["sector"], selector["selected_names"])
    digest, _, _ = semantic(key)
    assert digest == selector["selector_semantic_sha256"] and key not in installed
    installed[key] = selector["mechanism_id"]

prior = {}
for path in a.prior_audit:
    audit = json.loads(path.read_text())
    assert audit["status"] == "PASS" and audit["accepted_collision_free"]
    for row in audit["orbit_rows"]:
        key = key_tuple(row["selector_key"])
        assert key not in prior
        prior[key] = str(path)

replays = []
unique = {}
for delta in DELTAS:
    translated_times = {te(name, delta): value for name, value in times.items()}
    schedule = g.audit_schedule(translated_times)
    key = trans_key(parent, delta)
    digest, translated_names, groups = semantic(key)
    mechanism = replay(key, g.reconstruct_sector(a.sector, translated_times), logical_duals)
    row = {
        "delta": list(delta),
        "selector_key": key_json(key),
        "selector_semantic_sha256": digest,
        "selected_names": translated_names,
        "group_kinds": groups,
        "translated_schedule_sha256": csha(translated_times),
        "used_layers": schedule["used_layers"],
        **mechanism,
    }
    replays.append(row)
    unique.setdefault(key, []).append(row)

stabilizer = [list(delta) for delta in DELTAS if trans_key(parent, delta) == parent]
orbit_rows = []
for key in sorted(unique):
    rows = unique[key]
    representative = dict(rows[0])
    representative["realizing_deltas"] = [row["delta"] for row in rows]
    representative["translation_multiplicity"] = len(rows)
    orbit_rows.append(representative)

collisions = []
for key in sorted(unique):
    digest, _, _ = semantic(key)
    if key in installed:
        collisions.append({"kind": "installed", "selector_key": key_json(key), "mechanism_id": installed[key], "selector_semantic_sha256": digest})
    if key in prior:
        collisions.append({"kind": "prior_batch", "selector_key": key_json(key), "prior_audit": prior[key], "selector_semantic_sha256": digest})

assert len(unique) * len(stabilizer) == len(DELTAS)
assert all(len(rows) == len(stabilizer) for rows in unique.values())
out = {
    "schema": "circdist-gross-round116-direct-selector-orbit-audit-v1",
    "status": "PASS",
    "sector": a.sector,
    "bindings": {
        "source_sha256": fsha(a.source),
        "candidate_sha256": fsha(a.candidate),
        "candidate_schedule_sha256": candidate["compressed_schedule_sha256"],
        "cnf_sha256": fsha(a.cnf),
        "assignment_sha256": fsha(a.assignment),
    },
    "variables": nvars,
    "clauses": len(clauses),
    "all_variables_assigned_exactly_once": True,
    "all_clauses_checked": len(clauses),
    "all_clauses_satisfied": True,
    "selected_indices": selected,
    "selected_names": names,
    "parent_selector_key": key_json(parent),
    "parent_selector_semantic_sha256": parent_digest,
    "parent_replay": parent_replay,
    "group_order": len(DELTAS),
    "orbit_size": len(unique),
    "stabilizer_size": len(stabilizer),
    "stabilizer_deltas": stabilizer,
    "orbit_stabilizer_product": len(unique) * len(stabilizer),
    "translation_multiplicity_per_selector": len(stabilizer),
    "translated_replay_count": len(replays),
    "orbit_rows": orbit_rows,
    "translated_replays": replays,
    "installed_selector_count": len(installed),
    "prior_selector_count": len(prior),
    "collisions": collisions,
    "collision_count": len(collisions),
    "accepted_collision_free": not collisions,
    "all_72_translated_schedules_legal": True,
    "all_72_translated_mechanisms_weight_at_most_10_zero_syndrome_nonstabilizer": True,
}
a.output.parent.mkdir(parents=True, exist_ok=True)
a.output.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n")
print(json.dumps({k: out[k] for k in ("status", "sector", "orbit_size", "stabilizer_size", "stabilizer_deltas", "collision_count", "accepted_collision_free")}, sort_keys=True))
