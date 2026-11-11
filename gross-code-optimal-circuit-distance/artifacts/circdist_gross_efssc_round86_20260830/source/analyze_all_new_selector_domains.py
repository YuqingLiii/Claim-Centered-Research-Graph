#!/usr/bin/env python3
"""Exact order-domain census for every new Round-86 EFSSC selector.

This is deliberately independent of the Z3 EFSSC compiler: it enumerates all
720 local orders, maps them to exact 84-bit (72 detector + 12 logical)
signatures, and combines local multiplicities by an integer XOR dynamic
program.  It also repeats the dynamic program after imposing the legacy
source atom cube, proving containment (or exposing a counterexample).
"""
from pathlib import Path
import argparse, collections, hashlib, itertools, json, math, sys

ap = argparse.ArgumentParser()
ap.add_argument("--package", type=Path, required=True)
ap.add_argument("--state", type=Path, required=True)
ap.add_argument("--seed-direct", type=Path, required=True)
ap.add_argument("--output", type=Path, required=True)
a = ap.parse_args()
P = a.package.resolve()
sys.path[:0] = [str(P / "src/round63_src"), str(P / "src")]
import model as M
import round68_build as B


def canonical_bytes(obj):
    return json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()


def sha_obj(obj):
    return hashlib.sha256(canonical_bytes(obj)).hexdigest()


def signature(mask, detectors, duals):
    answer = 0
    for i, h in enumerate(detectors):
        answer |= (M.popcount(mask & h) & 1) << i
    for i, h in enumerate(duals):
        answer |= (M.popcount(mask & h) & 1) << (72 + i)
    return answer


def position_parity(kinds):
    positions = set()
    for kind in kinds:
        for pos in M.RES_POS[kind]:
            if pos in positions:
                positions.remove(pos)
            else:
                positions.add(pos)
    return tuple(sorted(positions))


def atom_holds(atom, positions):
    qa = int(atom[0].split(":")[2])
    qb = int(atom[2].split(":")[2])
    return positions[qa] < positions[qb]


def combine(class_counters, initial):
    dp = {initial: 1}
    layers = []
    for classes in class_counters:
        nxt = collections.Counter()
        for left, nleft in dp.items():
            for right, nright in classes.items():
                nxt[left ^ right] += nleft * nright
        dp = dict(nxt)
        layers.append({"states": len(dp), "multiplicity_sum": sum(dp.values())})
    return dp, layers


def combine_contributions(class_counters):
    """Exact XOR distribution with no fixed singleton contribution."""
    dp = {0: 1}
    layers = []
    for classes in class_counters:
        nxt = collections.Counter()
        for left, nleft in dp.items():
            for right, nright in classes.items():
                nxt[left ^ right] += nleft * nright
        dp = dict(nxt)
        layers.append({"states": len(dp), "multiplicity_sum": sum(dp.values())})
    return dp, layers


def mitm_valid_count(class_counters, initial):
    """Count valid tuples without materializing the potentially huge full DP.

    Split the checks in two.  For every left signature l, detector cancellation
    fixes the required right detector signature.  Within that detector bucket,
    exactly one right logical signature would make the final logical signature
    zero, so subtract its multiplicity.  All operations are exact integers.
    """
    split = len(class_counters) // 2
    left, left_layers = combine_contributions(class_counters[:split])
    right, right_layers = combine_contributions(class_counters[split:])
    low_mask = (1 << 72) - 1
    right_by_syndrome = collections.Counter()
    for sig, count in right.items():
        right_by_syndrome[sig & low_mask] += count
    initial_syndrome = initial & low_mask
    initial_logical = initial >> 72
    valid = 0
    for left_sig, left_count in left.items():
        wanted_syndrome = initial_syndrome ^ (left_sig & low_mask)
        zero_logical = initial_logical ^ (left_sig >> 72)
        bad_right_sig = wanted_syndrome | (zero_logical << 72)
        valid += left_count * (right_by_syndrome[wanted_syndrome] - right.get(bad_right_sig, 0))
    return valid, {
        "split_after_checks": split,
        "left_states": len(left),
        "right_states": len(right),
        "right_syndrome_buckets": len(right_by_syndrome),
        "left_layers": left_layers,
        "right_layers": right_layers,
    }


def is_valid(sig):
    return (sig & ((1 << 72) - 1)) == 0 and (sig >> 72) != 0


state = json.loads(a.state.read_text())
seed = json.loads(a.seed_direct.read_text())
px, pz, lx, lz = B.load_context()
contexts = {
    "Xerr": (M.Xchecks, M.HZ, lz),
    "Zerr": (M.Zchecks, M.HX, lx),
}

mechanisms = {}
for sector in ("Xerr", "Zerr"):
    mechanisms[f"iter102-{sector}"] = seed["sectors"][sector]["mechanism"]
for iteration in state["iterations"]:
    for sector in ("Xerr", "Zerr"):
        mechanisms[f"r86-i{iteration['iteration']}-{sector}"] = iteration["direct"][sector]["mechanism"]

result = {
    "schema": "round86-all-new-fixed-selector-domain-census-v1",
    "method": {
        "local_enumeration": "all 6! = 720 orders for every participating check",
        "global_combination": "integer XOR dynamic program over exact 84-bit signatures",
        "validity": "all 72 detector parities zero and at least one of 12 logical parities one",
        "legacy_cube_control": "repeat the same DP using only local orders satisfying every source precedence atom",
    },
    "selectors": [],
}

for selector_index, selector in enumerate(state["selectors"]):
    if selector_index < 120:
        continue
    mechanism_id = selector["mechanism_id"]
    mechanism = mechanisms[mechanism_id]
    assert mechanism["selected_names"] == selector["selected_names"]
    sector = selector["sector"]
    rows, detectors, duals = contexts[sector]
    data = [int(name.split(":")[1]) for name in selector["selected_names"] if name.startswith("D:")]
    groups = {int(c): list(kinds) for c, kinds in selector["group_kinds"].items()}
    data_sig = signature(M.mask(data), detectors, duals)
    atoms = [tuple(atom) for atom in mechanism["sound_outer_block"]["atoms"]]
    local_records = []
    full_counters = []
    cube_counters = []
    for check, kinds in sorted(groups.items()):
        positions_used = position_parity(kinds)
        full = collections.Counter()
        cube = collections.Counter()
        relevant_atoms = [atom for atom in atoms if int(atom[0].split(":")[1]) == check]
        for order in itertools.permutations(rows[check]):
            positions = {q: i for i, q in enumerate(order)}
            support = [order[p] for p in positions_used]
            sig = signature(M.mask(support), detectors, duals)
            full[sig] += 1
            if all(atom_holds(atom, positions) for atom in relevant_atoms):
                cube[sig] += 1
        assert sum(full.values()) == math.factorial(6)
        assert sum(cube.values()) > 0
        full_counters.append(full)
        cube_counters.append(cube)
        local_records.append({
            "check": check,
            "kinds": sorted(kinds),
            "position_parity": list(positions_used),
            "support_size": len(positions_used),
            "source_atom_count": len(relevant_atoms),
            "full_order_count": sum(full.values()),
            "full_signature_classes": len(full),
            "cube_order_count": sum(cube.values()),
            "cube_signature_classes": len(cube),
            "full_signature_class_order_multiplicities": {hex(k): v for k, v in sorted(full.items())},
            "cube_signature_class_order_multiplicities": {hex(k): v for k, v in sorted(cube.items())},
        })
    full_total = 720 ** len(groups)
    valid_total, full_mitm = mitm_valid_count(full_counters, data_sig)
    invalid_total = full_total - valid_total
    cube_total = math.prod(sum(classes.values()) for classes in cube_counters)
    cube_valid, cube_mitm = mitm_valid_count(cube_counters, data_sig)
    cube_invalid = cube_total - cube_valid
    assert valid_total > 0
    assert cube_invalid == 0
    assert valid_total >= cube_total
    if valid_total % cube_total == 0:
        factor = valid_total // cube_total
    else:
        factor = {"numerator": valid_total, "denominator": cube_total}
    entry = {
        "selector_index": selector_index,
        "mechanism_id": mechanism_id,
        "source_iteration": selector.get("source_iteration") if selector.get("source_iteration") is not None else 102,
        "sector": sector,
        "selected_names": selector["selected_names"],
        "selector_semantic_sha256": selector["selector_semantic_sha256"],
        "participating_checks": len(groups),
        "full_cartesian_order_tuples": full_total,
        "valid_order_tuples": valid_total,
        "invalid_order_tuples": invalid_total,
        "exact_count_algorithm": "meet-in-the-middle detector-bucket join",
        "full_mitm": full_mitm,
        "source_atom_count": len(atoms),
        "source_cube_order_tuples": cube_total,
        "source_cube_valid_order_tuples": cube_valid,
        "source_cube_invalid_order_tuples": cube_invalid,
        "source_cube_mitm": cube_mitm,
        "exact_cut_to_source_cube_factor": factor,
        "strictly_contains_source_cube": valid_total > cube_total,
        "local_domains": local_records,
    }
    result["selectors"].append(entry)
    print(json.dumps({k: entry[k] for k in (
        "mechanism_id", "participating_checks", "full_cartesian_order_tuples",
        "valid_order_tuples",
        "source_cube_order_tuples", "exact_cut_to_source_cube_factor",
        "strictly_contains_source_cube")}, sort_keys=True), flush=True)

assert len(result["selectors"]) == 14
result["summary"] = {
    "selector_count": len(result["selectors"]),
    "strict_source_cube_expansions": sum(e["strictly_contains_source_cube"] for e in result["selectors"]),
    "equal_to_source_cube": sum(not e["strictly_contains_source_cube"] for e in result["selectors"]),
    "total_valid_order_tuples_sum_across_selectors": sum(e["valid_order_tuples"] for e in result["selectors"]),
    "total_source_cube_order_tuples_sum_across_selectors": sum(e["source_cube_order_tuples"] for e in result["selectors"]),
}
result["selector_entries_sha256"] = sha_obj(result["selectors"])
a.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
print(json.dumps(result["summary"], sort_keys=True))
