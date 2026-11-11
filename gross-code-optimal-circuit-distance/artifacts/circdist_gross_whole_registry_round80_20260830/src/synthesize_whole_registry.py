#!/usr/bin/env python3
"""Exact whole-registry star hitting-cut synthesis.

Each retained multi-check box is covered by a union of complete raw pair-truth
relations.  For every center order the proof chooses one leaf relation that is
positive for *every* allowed order of that leaf.  This is an exact factorized
universal proof, not a sample or an inference from a failed search.
"""
from __future__ import annotations

import argparse
import collections
import gzip
import hashlib
import itertools
import json
import math
import os
from pathlib import Path
import struct
import sys
import time

import z3


ap = argparse.ArgumentParser()
ap.add_argument("--root", type=Path, required=True)
ap.add_argument("--leaf-root", type=Path, required=True)
ap.add_argument("--generalized-state", type=Path, required=True)
ap.add_argument("--output-root", type=Path, required=True)
ap.add_argument("--batch-id", required=True)
ap.add_argument("--max-retained", type=int, default=48)
a = ap.parse_args()
ROOT = a.root.resolve()
LEAF = a.leaf_root.resolve()
OUT = a.output_root.resolve()
OUT.mkdir(parents=True, exist_ok=False)
sys.path.insert(0, str(ROOT / "src/round63_src"))
import model as M  # noqa: E402

ALL = (1 << 720) - 1
SYNMASK = (1 << 72) - 1


def canon(o):
    return json.dumps(o, sort_keys=True, separators=(",", ":")).encode()


def sha_obj(o):
    return hashlib.sha256(canon(o)).hexdigest()


def load(p):
    p = Path(p)
    if not p.exists():
        p = Path(str(p) + ".gz")
    b = p.read_bytes()
    return json.loads(gzip.decompress(b) if p.suffix == ".gz" else b)


def dump(p, o):
    p = Path(p)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(o, indent=2, sort_keys=True) + "\n")


def atomic_dump(p, o):
    p = Path(p)
    q = p.with_name(p.name + ".round80-whole.tmp")
    q.write_text(json.dumps(o, indent=2, sort_keys=True) + "\n")
    os.replace(q, p)


def bits(z):
    while z:
        b = z & -z
        yield b.bit_length() - 1
        z ^= b


def pc(z):
    return bin(z).count("1")


def mask(xs):
    return sum(1 << int(x) for x in xs)


def syndrome(v, rows):
    return sum(((pc(v & h) & 1) << i) for i, h in enumerate(rows))


def logical(v, duals):
    return sum(((pc(v & h) & 1) << i) for i, h in enumerate(duals))


def signature(v, det, duals):
    return syndrome(v, det) | (logical(v, duals) << 72)


def sector_context(lab):
    if lab == "Xerr":
        return M.Xchecks, M.HZ, M.HX, LZ
    return M.Zchecks, M.HX, M.HZ, LX


def parse_atom(atom):
    la, c, q = atom[0].split(":")
    lb, d, r = atom[2].split(":")
    assert la == lb and c == d and atom[1] == "<"
    return la, int(c), int(q), int(r)


def atom_check(atom):
    return int(atom[0].split(":")[1])


PX = M.expand_pool(ROOT / "src/inputs/w12X.txt", M.HX, M.HZ)
PZ = M.expand_pool(ROOT / "src/inputs/w12Z.txt", M.HZ, M.HX)
LX = M.logical_basis(PX, M.HX)
LZ = M.logical_basis(PZ, M.HZ)
assert len(PX) == len(PZ) == 1884 and len(LX) == len(LZ) == 12

state = load(a.generalized_state)
state_before_sha = sha_obj(state)
assert state["term_count"] == len(state["terms"])
catalog_obj = load(LEAF / "local_order_catalog.json")
relation_obj = load(LEAF / "pair_relations.json")
cats = {(x["sector"], int(x["check"])): x for x in catalog_obj["entries"]}
relations = {}
for rel in relation_obj["relations"]:
    key = (rel["sector"], int(rel["a"]), int(rel["b"]))
    assert key not in relations
    rel["_truth"] = [int(x, 16) for x in rel["truth_rows_hex"]]
    rel["_explicit"] = [int(x, 16) for x in rel["explicit_good_good_rows_hex"]]
    relations[key] = rel
assert len(relations) == len(relation_obj["relations"])

# Exact 720-bit comparison masks make candidate minimization a sequence of
# machine-integer intersections rather than repeated catalog scans.
comparison_masks = {}
PERMS = list(itertools.permutations(range(6)))
for lab, rows in (("Xerr", M.Xchecks), ("Zerr", M.Zchecks)):
  for c, row0 in enumerate(rows):
    row = list(map(int, row0))
    if (lab, c) in cats:
        assert [list(map(int, z["qubits"])) for z in cats[(lab, c)]["orders"]] == [[row[j] for j in p] for p in PERMS]
    for q in row:
        for r in row:
            if q == r:
                continue
            z = 0
            for order_id, p in enumerate(PERMS):
                order = [row[j] for j in p]
                if order.index(q) < order.index(r):
                    z |= 1 << order_id
            comparison_masks[(lab, c, q, r)] = z


def cat_mask(lab, c, atoms):
    z = ALL
    for x in atoms:
        la, cc, q, r = parse_atom(x)
        if cc == c:
            assert la == ("X" if lab == "Xerr" else "Z")
            z &= comparison_masks[(lab, c, q, r)]
    return z


def normalized(lab, atoms):
    checks = sorted({atom_check(x) for x in atoms})
    masks = {c: cat_mask(lab, c, atoms) for c in checks}
    return checks, masks


def region_key(lab, checks, masks):
    return (lab, tuple((c, masks[c]) for c in checks))


def relation_for(lab, x, y):
    a0, b0 = sorted((x, y))
    return relations.get((lab, a0, b0))


def truth_holds(rel, x, ox, y, oy):
    if x == rel["a"]:
        return bool((rel["_truth"][ox] >> oy) & 1)
    assert x == rel["b"] and y == rel["a"]
    return bool((rel["_truth"][oy] >> ox) & 1)


good_center_cache = {}


def good_center_mask(rel, center, leaf_mask):
    """Center orders for which every allowed leaf order is a positive pair cell."""
    ck = (rel["sector"], int(rel["a"]), int(rel["b"]), center, leaf_mask)
    if ck in good_center_cache:
        return good_center_cache[ck]
    z = 0
    if center == rel["a"]:
        for oc, row in enumerate(rel["_truth"]):
            if leaf_mask & (ALL ^ row) == 0:
                z |= 1 << oc
    else:
        assert center == rel["b"]
        z = ALL
        for ol in bits(leaf_mask):
            z &= rel["_truth"][ol]
    good_center_cache[ck] = z
    return z


def star_audit(lab, center, leaves, atoms, require_synergy=True):
    checks, masks = normalized(lab, atoms)
    if center not in masks or any(l not in masks for l in leaves) or any(masks[c] == 0 for c in checks):
        return {"sound": False, "reason": "zero_or_missing_domain", "checks": checks, "masks": masks}
    goods = []
    for leaf in leaves:
        rel = relation_for(lab, center, leaf)
        if rel is None:
            return {"sound": False, "reason": "missing_relation", "checks": checks, "masks": masks}
        goods.append(good_center_mask(rel, center, masks[leaf]))
    covered = 0
    partitions = []
    for g in goods:
        take = masks[center] & g & (ALL ^ covered)
        partitions.append(take)
        covered |= g
    miss = masks[center] & (ALL ^ covered)
    used = sum(bool(x) for x in partitions)
    individually_universal = [masks[center] & (ALL ^ g) == 0 for g in goods]
    ok = miss == 0 and (not require_synergy or (used >= 2 and not any(individually_universal)))
    witness = None
    if miss:
        oc = next(bits(miss))
        witness = {"center_order_id": oc, "leaf_order_ids": {}}
        for leaf, rel in zip(leaves, [relation_for(lab, center, l) for l in leaves]):
            ol = next(ol for ol in bits(masks[leaf]) if not truth_holds(rel, leaf, ol, center, oc))
            witness["leaf_order_ids"][str(leaf)] = ol
    return {
        "sound": ok,
        "reason": "covered_synergistically" if ok else ("not_synergistic" if not miss else "miss_tuple"),
        "checks": checks,
        "masks": masks,
        "good_center_masks": goods,
        "partitions": partitions,
        "miss_mask": miss,
        "used_leaf_count": used,
        "individual_universal": individually_universal,
        "countertuple": witness,
    }


def minimize(lab, center, leaves, seed_atoms, reverse):
    cur = sorted(set(tuple(x) for x in seed_atoms))
    controls = []
    order = list(reversed(cur)) if reverse else list(cur)
    for atom in order:
        if atom not in cur:
            continue
        trial = cur.copy()
        trial.remove(atom)
        q = star_audit(lab, center, leaves, trial, False)
        if q["sound"]:
            cur = trial
        else:
            controls.append({
                "removed_atom": list(atom),
                "result": q["reason"],
                "countertuple": q.get("countertuple"),
                "scope": "this fixed star leaf set and exact raw pair relations only; not global installed-union or physical-mechanism minimality",
            })
    q = star_audit(lab, center, leaves, cur, True)
    return (cur, q, controls) if q["sound"] else None


# Normalize the complete installed library once.
installed = []
installed_by_key = collections.defaultdict(list)
for t in state["terms"]:
    lab = t["sector"]
    atoms = [tuple(x) for x in t["atoms"]]
    checks, masks = normalized(lab, atoms)
    x = {"term": t, "sector": lab, "atoms": atoms, "checks": checks, "masks": masks, "key": region_key(lab, checks, masks)}
    installed.append(x)
    installed_by_key[x["key"]].append(t["term_id"])


def dominates(u, v):
    if u["sector"] != v["sector"] or not set(u["checks"]).issubset(v["checks"]):
        return False
    return all(v["masks"][c] & (ALL ^ u["masks"][c]) == 0 for c in u["checks"])


# One deterministic broad seed per relation and center orientation.
seeds = collections.defaultdict(list)
for rel in relation_obj["relations"]:
    terms = rel["generated_terms"]
    if not terms:
        continue
    uniq = {}
    for t in terms:
        atoms = [tuple(x) for x in t["atoms"]]
        checks, masks = normalized(rel["sector"], atoms)
        k = region_key(rel["sector"], checks, masks)
        score = (int(t["covered_tuple_count"]), -len(atoms), canon(atoms))
        if k not in uniq or score > uniq[k][0]:
            uniq[k] = (score, atoms)
    best_atoms = max(uniq.values(), key=lambda x: x[0])[1]
    for center, leaf in ((int(rel["a"]), int(rel["b"])), (int(rel["b"]), int(rel["a"]))):
        seeds[(rel["sector"], center)].append({"leaf": leaf, "atoms": best_atoms, "relation": [rel["a"], rel["b"]]})

raw = []
search_attempts = 0
zero_domain = 0
unsound = 0
not_synergistic = 0
for (lab, center), rows in sorted(seeds.items()):
    # Keep the broadest seed per leaf.  Pair every distinct leaf, then also try
    # deterministic triples among the twelve broadest leaves.
    by_leaf = {}
    for r in rows:
        checks, masks = normalized(lab, r["atoms"])
        score = (math.prod(pc(masks[c]) for c in checks), -len(r["atoms"]), canon(r["atoms"]))
        if r["leaf"] not in by_leaf or score > by_leaf[r["leaf"]][0]:
            by_leaf[r["leaf"]] = (score, r)
    chosen = [x[1] for x in sorted(by_leaf.values(), key=lambda z: z[0], reverse=True)[:24]]
    families = list(itertools.combinations(chosen, 2))
    for fam in families:
        leaves = tuple(sorted(r["leaf"] for r in fam))
        seed_atoms = sorted(set(itertools.chain.from_iterable(r["atoms"] for r in fam)))
        search_attempts += 1
        q0 = star_audit(lab, center, leaves, seed_atoms, False)
        if not q0["sound"]:
            if q0["reason"] == "zero_or_missing_domain":
                zero_domain += 1
            elif q0["reason"] == "not_synergistic":
                not_synergistic += 1
            else:
                unsound += 1
            continue
        for reverse in (False, True):
            result = minimize(lab, center, leaves, seed_atoms, reverse)
            if result is None:
                not_synergistic += 1
                continue
            atoms, q, controls = result
            raw.append({
                "relation_kind": "whole_registry_exact_star_hitting_cut",
                "sector": lab,
                "center": center,
                "leaves": list(leaves),
                "relations": [list(sorted((center, l))) for l in leaves],
                "atoms": [list(x) for x in atoms],
                "checks": q["checks"],
                "allowed_order_masks_hex": {str(c): hex(q["masks"][c]) for c in q["checks"]},
                "allowed_order_counts": {str(c): pc(q["masks"][c]) for c in q["checks"]},
                "good_center_masks_hex": {str(l): hex(g) for l, g in zip(leaves, q["good_center_masks"])},
                "center_partition_masks_hex": {str(l): hex(p) for l, p in zip(leaves, q["partitions"])},
                "center_partition_counts": {str(l): pc(p) for l, p in zip(leaves, q["partitions"])},
                "covered_tuple_count": math.prod(pc(q["masks"][c]) for c in q["checks"]),
                "used_leaf_count": q["used_leaf_count"],
                "no_single_leaf_universal": not any(q["individual_universal"]),
                "proof_mode": "exact_star_center_partition_over_complete_720x720_raw_pair_truth",
                "selector_priority": "ascending leaf; for a center order use the first leaf whose entire allowed leaf domain is pair-positive; within that pair use a-unary, b-unary, then first explicit configuration",
                "deletion_controls": controls,
                "direction": "reverse" if reverse else "forward",
            })

print(json.dumps({"stage": "raw_star_search", "attempts": search_attempts, "sound_raw": len(raw), "zero_domain": zero_domain, "unsound": unsound, "not_synergistic": not_synergistic}, sort_keys=True), flush=True)

# Exact duplicate/dominance classification, followed by a true full-installed-
# union complement SAT witness over all local permutations.
classes = []
unique = []
seen = {}
for i, t in enumerate(raw):
    atoms = [tuple(x) for x in t["atoms"]]
    checks, masks = normalized(t["sector"], atoms)
    x = {"index": i, "term": t, "sector": t["sector"], "atoms": atoms, "checks": checks, "masks": masks, "key": region_key(t["sector"], checks, masks)}
    if any(masks[c] == 0 for c in checks):
        classes.append({"raw_index": i, "classification": "rejected_zero_domain"})
        continue
    if x["key"] in installed_by_key:
        classes.append({"raw_index": i, "classification": "duplicate_old", "installed_ids": installed_by_key[x["key"]][:100]})
        continue
    if x["key"] in seen:
        classes.append({"raw_index": i, "classification": "duplicate_new", "canonical_raw_index": seen[x["key"]]})
        continue
    seen[x["key"]] = i
    dom = [u["term"]["term_id"] for u in installed if dominates(u, x)]
    if dom:
        classes.append({"raw_index": i, "classification": "dominated_old", "dominator_ids": dom[:100], "dominator_count": len(dom)})
        continue
    unique.append(x)

# Strong candidates first: more tuples, fewer atoms, two-leaf before three-leaf
# only as a final deterministic tiebreak.  The budget limits packaging cost, not
# the raw search or the soundness classification.
unique.sort(key=lambda x: (x["term"]["covered_tuple_count"], -len(x["atoms"]), -len(x["term"]["leaves"]), -x["index"]), reverse=True)


def installed_union_complement(candidate, extra_terms):
    solver = z3.Solver()
    positions = {}
    for lab, rows in (("X", M.Xchecks), ("Z", M.Zchecks)):
        for c, row in enumerate(rows):
            vs = []
            for q in row:
                v = z3.Int(f"p_{lab}_{c}_{q}")
                positions[(lab, c, int(q))] = v
                solver.add(v >= 0, v < 6)
                vs.append(v)
            solver.add(z3.Distinct(vs))

    def holds(atom):
        lab, c, q, r = parse_atom(atom)
        return positions[(lab, c, q)] < positions[(lab, c, r)]

    for atom in candidate["atoms"]:
        solver.add(holds(atom))
    avoid = state["terms"] + extra_terms
    for t in avoid:
        solver.add(z3.Or(*[z3.Not(holds(tuple(x))) for x in t["atoms"]]))
    status = solver.check()
    if status != z3.sat:
        return {"status": str(status).upper(), "strictly_outside_union": False}
    model = solver.model()
    orders = {}
    for lab, rows in (("X", M.Xchecks), ("Z", M.Zchecks)):
        for c, row in enumerate(rows):
            orders[f"{lab}:{c}"] = sorted(map(int, row), key=lambda q: model.eval(positions[(lab, c, q)]).as_long())
    assert all(all(orders[f"{parse_atom(x)[0]}:{parse_atom(x)[1]}"].index(parse_atom(x)[2]) < orders[f"{parse_atom(x)[0]}:{parse_atom(x)[1]}"].index(parse_atom(x)[3]) for x in candidate["atoms"]) for _ in [0])
    return {"status": "SAT", "strictly_outside_union": True, "complete_local_orders": orders, "complete_local_orders_sha256": sha_obj(orders), "avoided_installed_terms": len(avoid)}


retained = []
for x in unique:
    if len(retained) >= a.max_retained:
        classes.append({"raw_index": x["index"], "classification": "sound_not_selected_after_deterministic_packaging_budget"})
        continue
    prior_public = [{"atoms": [list(z) for z in r["atoms"]]} for r in retained]
    wit = installed_union_complement(x, prior_public)
    if not wit["strictly_outside_union"]:
        classes.append({"raw_index": x["index"], "classification": "covered_by_full_evolving_union", "solver_status": wit["status"]})
        continue
    x["union_witness"] = wit
    classes.append({"raw_index": x["index"], "classification": "retained_strict_union_expansion", "complete_local_orders_sha256": wit["complete_local_orders_sha256"]})
    retained.append(x)

print(json.dumps({"stage": "semantic_classification", "raw": len(raw), "unique_nondominated": len(unique), "retained": len(retained), "counts": dict(collections.Counter(x["classification"] for x in classes))}, sort_keys=True), flush=True)


def validate_support(lab, cv, pv):
    rows, det, stabs, duals = sector_context(lab)
    cs = signature(cv, det, duals)
    ps = signature(pv, det, duals)
    assert cs == ps and (cs & SYNMASK) == 0 and (cs >> 72) != 0
    assert not M.inspan(cv, stabs) and not M.inspan(pv, stabs)
    return cs


def option_for(cat, order_id, kind):
    rec = cat["orders"][order_id]
    z = rec["options"][kind]
    assert int(z["kind"]) == kind
    return mask(z["canonical_support"]), mask(z["physical_support"])


def pair_selector(rel, oa, ob):
    ca = cats[(rel["sector"], int(rel["a"]))]
    cb = cats[(rel["sector"], int(rel["b"]))]
    wa = ca["orders"][oa]["unary_witness"]
    if wa is not None:
        v = mask(wa["logical_support"])
        return v, v, int(wa["fault_weight"]), {"kind": "a_unary", "check": rel["a"], "order_id": oa, "residual_kind": 1, "data_support": wa["singleton_support"], "canonical_support": wa["logical_support"], "physical_support": wa["logical_support"]}
    wb = cb["orders"][ob]["unary_witness"]
    if wb is not None:
        v = mask(wb["logical_support"])
        return v, v, int(wb["fault_weight"]), {"kind": "b_unary", "check": rel["b"], "order_id": ob, "residual_kind": 1, "data_support": wb["singleton_support"], "canonical_support": wb["logical_support"], "physical_support": wb["logical_support"]}
    for conf in rel["positive_configurations"]:
        ac, ap = option_for(ca, oa, int(conf["a_kind"]))
        bc, bp = option_for(cb, ob, int(conf["b_kind"]))
        if ac == mask(conf["a_support"]) and bc == mask(conf["b_support"]):
            d = mask(conf["singleton_support"])
            cv, pv = ac ^ bc ^ d, ap ^ bp ^ d
            return cv, pv, int(conf["fault_weight"]), {"kind": "explicit_pair", "configuration_id": conf["configuration_id"], "checks": [rel["a"], rel["b"]], "order_ids": [oa, ob], "residual_kinds": [conf["a_kind"], conf["b_kind"]], "data_support": conf["singleton_support"], "a_source_mechanisms": conf["a_source_mechanisms"], "b_source_mechanisms": conf["b_source_mechanisms"], "canonical_support": M.bits(cv), "physical_support": M.bits(pv)}
    raise AssertionError("truth cell has no constructive selector")


proofs = []
installed_terms = []
for j, x in enumerate(retained):
    t = x["term"]
    lab, center, leaves = t["sector"], int(t["center"]), list(map(int, t["leaves"]))
    checks, masks = normalized(lab, x["atoms"])
    goods = [good_center_mask(relation_for(lab, center, leaf), center, masks[leaf]) for leaf in leaves]
    covered = 0
    partitions = []
    for g in goods:
        p = masks[center] & g & (ALL ^ covered)
        partitions.append(p)
        covered |= g
    assert masks[center] & (ALL ^ covered) == 0 and sum(pc(p) for p in partitions) == pc(masks[center]) and sum(bool(p) for p in partitions) >= 2
    h = hashlib.sha256()
    pair_replays = selector_full_multiplicity = 0
    hist = collections.Counter()
    selector_kinds = collections.Counter()
    signatures = set()
    samples = []
    leaf_product = math.prod(pc(masks[l]) for l in leaves)
    for leaf_index, (leaf, part) in enumerate(zip(leaves, partitions)):
        rel = relation_for(lab, center, leaf)
        other_multiplier = math.prod(pc(masks[l]) for l in leaves if l != leaf)
        for oc in bits(part):
            for ol in bits(masks[leaf]):
                oa, ob = (oc, ol) if center == rel["a"] else (ol, oc)
                assert (rel["_truth"][oa] >> ob) & 1
                cv, pv, faults, selector = pair_selector(rel, oa, ob)
                sig = validate_support(lab, cv, pv)
                assert faults <= 10
                pair_replays += 1
                selector_full_multiplicity += other_multiplier
                hist[faults] += 1
                selector_kinds[selector["kind"]] += 1
                signatures.add(sig)
                h.update(struct.pack(">BBHH", leaf_index, len(leaves), oc, ol) + cv.to_bytes(18, "big") + pv.to_bytes(18, "big") + struct.pack(">B", faults))
                if len(samples) < 6:
                    samples.append({"center_order_id": oc, "leaf": leaf, "leaf_order_id": ol, "canonical_support": M.bits(cv), "physical_support": M.bits(pv), "fault_count": faults, "signature_hex": hex(sig), "explicit_raw_physical_selector": selector})
    full_product = pc(masks[center]) * leaf_product
    assert selector_full_multiplicity == full_product == t["covered_tuple_count"]
    term_id = f"r80-whole-{a.batch_id}-{lab}-{j:04d}"
    public = {
        "term_id": term_id,
        "source_round": 80,
        "source_phase": "whole_registry_exact_hitting_cut",
        "source_batch": a.batch_id,
        "relation_kind": t["relation_kind"],
        "sector": lab,
        "atoms": [list(z) for z in x["atoms"]],
        "center": center,
        "leaves": leaves,
        "source_pair_relations": t["relations"],
        "selector_rule": t["selector_priority"],
        "source_term_sha256": sha_obj(t),
    }
    x["installed_term"] = public
    installed_terms.append(public)
    proofs.append({
        "term_id": term_id,
        "sector": lab,
        "center": center,
        "leaves": leaves,
        "checks": checks,
        "atoms": [list(z) for z in x["atoms"]],
        "allowed_order_masks_hex": {str(c): hex(masks[c]) for c in checks},
        "allowed_order_counts": {str(c): pc(masks[c]) for c in checks},
        "good_center_masks_hex": {str(l): hex(g) for l, g in zip(leaves, goods)},
        "center_partition_masks_hex": {str(l): hex(p) for l, p in zip(leaves, partitions)},
        "center_partition_counts": {str(l): pc(p) for l, p in zip(leaves, partitions)},
        "complete_factorized_product_tuples": full_product,
        "literal_pair_cells_replayed": pair_replays,
        "selector_induced_full_tuple_multiplicity": selector_full_multiplicity,
        "selector_stream_encoding": ">B leaf-index; >B leaf-count; >H center-order; >H leaf-order; 18-byte canonical; 18-byte physical; >B faults",
        "selector_stream_sha256": h.hexdigest(),
        "fault_count_histogram_on_literal_pair_cells": dict(hist),
        "selector_kind_histogram_on_literal_pair_cells": dict(selector_kinds),
        "signature_count": len(signatures),
        "signature_set_sha256": sha_obj([hex(s) for s in sorted(signatures)]),
        "explicit_raw_physical_selector_samples": samples,
        "universal_argument": "center partitions are exhaustive and disjoint; chosen leaf pair is valid for every allowed leaf order; selector ignores other leaves, whose exact multiplicity is restored by the factorized product",
        "all_pair_cells_canonical_physical_replayed": True,
        "deletion_controls": t["deletion_controls"],
        "strict_installed_union_expansion_witness": x["union_witness"],
    })

after = dict(state)
if installed_terms:
    after["schema"] = "circdist-gross-whole-registry-round80-generalized-library-v1"
    after["terms"] = state["terms"] + installed_terms
    after["term_count"] = len(after["terms"])
    after["round80_whole_registry_terms"] = len(installed_terms)
assert after["term_count"] == state["term_count"] + len(installed_terms)

summary = {
    "schema": "circdist-gross-whole-registry-round80-summary-v1",
    "status": "PASS",
    "batch_id": a.batch_id,
    "input_generalized_count": state["term_count"],
    "input_generalized_semantic_sha256": state_before_sha,
    "raw_mechanisms": 96,
    "local_catalogs": len(cats),
    "pair_relations": len(relations),
    "pair_truth_positive_cells": sum(pc(z) for r in relations.values() for z in r["_truth"]),
    "star_seed_attempts": search_attempts,
    "raw_sound_star_candidates": len(raw),
    "initial_zero_domain_attempts": zero_domain,
    "initial_unsound_attempts": unsound,
    "initial_not_synergistic_attempts": not_synergistic,
    "classification_counts": dict(collections.Counter(x["classification"] for x in classes)),
    "retained": len(installed_terms),
    "generalized_after": after["term_count"],
    "generalized_after_semantic_sha256": sha_obj(after),
    "literal_pair_cells_replayed": sum(x["literal_pair_cells_replayed"] for x in proofs),
    "complete_factorized_product_tuples": sum(x["complete_factorized_product_tuples"] for x in proofs),
    "strict_installed_union_expansions": sum(x["strict_installed_union_expansion_witness"]["strictly_outside_union"] for x in proofs),
    "zero_cells_used_as_absence": 0,
    "positive_misses_used_as_absence": 0,
    "deletion_countertuples_used_as_global_minimality_or_absence": 0,
    "claim_scope": "constructive sound multi-check exclusion regions only; no absence, repair, exhaustion, or D-star inference",
}
dump(OUT / "raw_candidates.json", {"schema": "round80-whole-registry-raw-candidates-v1", "terms": raw})
dump(OUT / "classification_ledger.json", {"schema": "round80-whole-registry-classification-v1", "classifications": classes})
dump(OUT / "retained_terms.json", {"schema": "round80-whole-registry-retained-v1", "terms": installed_terms})
dump(OUT / "factorized_selector_proofs.json", {"schema": "round80-whole-registry-factorized-proofs-v1", "proofs": proofs, "all_passed": True})
dump(OUT / "generalized_before.json", state)
dump(OUT / "generalized_after.json", after)
dump(OUT / "summary.json", summary)
atomic_dump(a.generalized_state, after)
dump(OUT / "install_result.json", {
    "schema": "round80-whole-registry-install-v1",
    "status": "PASS",
    "batch_id": a.batch_id,
    "state_before_semantic_sha256": state_before_sha,
    "state_after_semantic_sha256": sha_obj(after),
    "retained_increment": len(installed_terms),
    "generalized_count_after": after["term_count"],
    "strict_order": "complete leaf reconstruction -> raw star search -> exact soundness -> semantic duplicate/dominance -> full installed-union complement SAT -> literal/factorized canonical-physical replay -> atomic install",
})
print(json.dumps(summary, sort_keys=True), flush=True)
