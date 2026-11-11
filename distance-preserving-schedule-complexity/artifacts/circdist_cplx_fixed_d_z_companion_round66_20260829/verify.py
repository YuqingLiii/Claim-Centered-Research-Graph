#!/usr/bin/env python3
"""Clean-room finite checker for the round-66 theorem package.

Finite runs corroborate the universal proof in README.md; they are not used as
inductive evidence for untested formulas.
"""

import hashlib
import json
import random
import sys
from itertools import combinations, product
from pathlib import Path

from construction import (Builder, companion, in_span, k4_no, rref,
                          schedule_ok, span, wt)
from make_counterexample import build_counterexample
from z_companion import (block_contiguous_orders, canonical, decorate_z,
                         detector_columns, direct_sum, from_code, parity,
                         rank, repetition3_matrix, sentinel_state_audit,
                         support, transformed_rowspace_expected,
                         two_fault_audit, weight, xor_columns)


checks = []
EXPECTED_THEOREM_SHA256 = "49cf956fe5afa49caa8707f15fd157ab27fedadc79c56bdec0a57c0a89a0e184"
EXPECTED_X_THEOREM_SHA256 = "01cf8fd10f48db13e23a09f884eb24b0b17c860c121c336c324123ff222594c0"


def check(name, condition, detail=None):
    if not condition:
        raise AssertionError(name + (": " + repr(detail) if detail is not None else ""))
    checks.append({"check": name, "status": "PASS", "detail": detail})


def logical(v, detectors, stabilizers, n):
    rb, piv = rref(list(stabilizers), n)
    return all(parity(v & x) == 0 for x in detectors) and not in_span(v, rb, piv)


def min_logical_at_most(code, sector, max_weight):
    if sector == "Z":
        det, stab = code.hx, code.hz
    else:
        det, stab = code.hz, code.hx
    rb, piv = rref(list(stab), code.n)
    for w in range(1, max_weight + 1):
        for qs in combinations(range(code.n), w):
            v = sum(1 << q for q in qs)
            if all(parity(v & x) == 0 for x in det) and not in_span(v, rb, piv):
                return qs
    return None


def degrees(code):
    dx = [0] * code.n
    dz = [0] * code.n
    for row in code.hx:
        for q in support(row, code.n):
            dx[q] += 1
    for row in code.hz:
        for q in support(row, code.n):
            dz[q] += 1
    return max(dx[i] + dz[i] for i in range(code.n)), max(dx), max(dz)


def quotient_partition_preserved(old, new):
    """Compare every old X-row proper subset, plus every old data column."""
    vals = {1 << q for q in range(old.n)}
    for row in old.hx:
        qs = support(row, old.n)
        for mask in range(1, (1 << len(qs)) - 1):
            vals.add(sum(1 << qs[i] for i in range(len(qs)) if (mask >> i) & 1))
    vals = sorted(vals)

    old_sx, old_px = rref(list(old.hx), old.n)
    new_sx, new_px = rref(list(new.hx), new.n)
    old_dcols = detector_columns(old.hz, old.n)
    new_dcols = detector_columns(new.hz, new.n)

    maps = [({}, {}), ({}, {})]
    for v in vals:
        old_syn = xor_columns(old_dcols, v)
        new_syn = xor_columns(new_dcols, v)
        old_cls = canonical(v, old_sx, old_px)
        new_cls = canonical(v, new_sx, new_px)
        for a, b, pair in ((old_syn, new_syn, maps[0]), (old_cls, new_cls, maps[1])):
            fwd, rev = pair
            if a in fwd and fwd[a] != b:
                return False, "forward partition split"
            if b in rev and rev[b] != a:
                return False, "reverse partition merge"
            fwd[a] = b
            rev[b] = a
    return True, {"values": len(vals), "syndromes": len(maps[0][0]), "classes": len(maps[1][0])}


def safe_seed_orders(old, limit=100):
    lifted = repetition3_matrix(old)
    for seed in range(limit):
        rng = random.Random(seed)
        orders = []
        for z in old.hz:
            order = support(z, old.n)
            rng.shuffle(order)
            orders.append(order)
        audit = two_fault_audit(lifted, "Z", block_contiguous_orders(old, lifted, orders))
        if audit["safe"]:
            return seed, orders, audit
    return None


def raw_block_obstruction(old):
    """The exact one-clause increasing-order witness in old and lifted coordinates."""
    rows = [(0, 8), (9, 2)]
    old_prefix = 0
    old_suffix = 0
    lifted_orders = []
    for ri, cut in rows:
        order = support(old.hz[ri], old.n)
        lifted_orders.append([(q, a) for q in order for a in range(3)])
        for q in order[:cut]:
            old_prefix ^= 1 << q
        for q in order[cut:]:
            old_suffix ^= 1 << q
    sz, pz = rref(list(old.hz), old.n)
    return {
        "rows_and_old_cuts": rows,
        "old_prefix_xor": support(old_prefix, old.n),
        "old_suffix_xor": support(old_suffix, old.n),
        "old_suffix_weight": weight(old_suffix),
        "old_suffix_is_Z_logical": logical(old_suffix, old.hx, old.hz, old.n),
        "prefix_suffix_same_Z_class": in_span(old_prefix ^ old_suffix, sz, pz),
        "lifted_gate_cuts": [24, 6],
        "lifted_orders": lifted_orders,
    }


def main():
    package = Path(__file__).resolve().parent
    theorem = (package / "THEOREM.txt").read_text(encoding="utf-8").rstrip("\n")
    theorem_hash = hashlib.sha256(theorem.encode()).hexdigest()
    check("exact theorem length/hash",
          len(theorem) == 999 and theorem_hash == EXPECTED_THEOREM_SHA256,
          {"characters": len(theorem), "sha256": theorem_hash})
    x_theorem = (package / "LICENSED_X_THEOREM.txt").read_text(
        encoding="utf-8").rstrip("\n")
    x_theorem_hash = hashlib.sha256(x_theorem.encode()).hexdigest()
    check("exact licensed X theorem length/hash",
          len(x_theorem) == 883 and x_theorem_hash == EXPECTED_X_THEOREM_SHA256,
          {"characters": len(x_theorem), "sha256": x_theorem_hash})

    comp = companion()
    check("companion exact CSS parameters", comp.css() and comp.exact_distances() == (4, 3, 2),
          comp.exact_distances())
    comp_m = from_code(comp, "G_neq3")
    xwit = min_logical_at_most(comp_m, "X", 4)
    zwit = min_logical_at_most(comp_m, "Z", 3)
    check("companion exact distance witnesses", len(xwit) == 4 and len(zwit) == 3,
          {"X": xwit, "Z": zwit})

    b = Builder()
    one_c = b.build_formula(3, [((0, True), (1, True), (2, True))])
    one = from_code(one_c, "one_clause_C0")
    check("one-clause C0 cap/CSS/shape", one_c.cap() and one.css() and
          (one.n, len(one.hx), len(one.hz)) == (64, 37, 21),
          {"n": one.n, "mx": len(one.hx), "mz": len(one.hz)})
    one_dz = min_logical_at_most(one, "Z", 4)
    check("one-clause C0 adversarial low-Z search", one_dz is not None and len(one_dz) == 4,
          one_dz)

    lifted = repetition3_matrix(one, "R3(one)")
    natural_orders = block_contiguous_orders(one, lifted)
    natural_audit = two_fault_audit(lifted, "Z", natural_orders)
    raw = raw_block_obstruction(one)
    check("increasing block-contiguous order is unsafe",
          not natural_audit["safe"] and raw["old_suffix_is_Z_logical"] and
          raw["prefix_suffix_same_Z_class"],
          {"audit": natural_audit, "raw": raw})

    counterexample_on_disk = json.loads(
        (package / "COUNTEREXAMPLE.json").read_text(encoding="utf-8")
    )
    counterexample_rebuilt = build_counterexample()
    raw_cert = counterexample_on_disk["certificate"]
    union_cert = counterexample_on_disk["row_union_audit"]
    check("raw counterexample file exactly rebuilds and certifies the obstruction",
          counterexample_on_disk == counterexample_rebuilt and
          raw_cert["old_H_X_syndrome_nonzero_rows"] == [] and
          raw_cert["old_logical_not_in_H_Z_rowspan"] and
          raw_cert["lifted_H_X_syndrome_nonzero_rows"] == [] and
          raw_cert["lifted_logical_not_in_H_Z_rowspan"] and
          union_cert["all_single_row_restricted_quotients_trivial"] and
          union_cert["pairs_with_nontrivial_restricted_quotient"] == 14,
          {"sha256": hashlib.sha256(
              (package / "COUNTEREXAMPLE.json").read_bytes()).hexdigest(),
           "single_rows": union_cert["single_rows_checked"],
           "row_pairs": union_cert["row_pairs_checked"],
           "extra_pairs": union_cert["pairs_with_nontrivial_restricted_quotient"]})

    safe_seed = safe_seed_orders(one)
    check("block-contiguous failure is order-specific, not an all-orders claim",
          safe_seed is not None and safe_seed[0] == 0,
          {"first_safe_seed": safe_seed[0], "audit": safe_seed[2]})

    full_one = direct_sum(lifted, comp_m, "R3(one)+G")
    dec_one = decorate_z(full_one, "DZ(R3(one)+G)")
    identity_one = transformed_rowspace_expected(full_one, dec_one)
    check("one-clause transform rank/CSS identity",
          identity_one["css"] and identity_one["rank_identity"], identity_one)
    state_one = sentinel_state_audit(dec_one)
    check("one-clause sentinel path invariant",
          all(x["all_duplicates_one_data"] for x in state_one),
          {"rows": len(state_one),
           "states": sum(x["states"] for x in state_one),
           "duplicates": sum(len(x["duplicate_state_deltas"]) for x in state_one)})
    z_one = two_fault_audit(dec_one.code, "Z", dec_one.z_orders)
    check("one-clause exhaustive one/two-column Z audit", z_one["safe"], z_one)
    check("one-clause transformed structural bounds",
          max(map(weight, dec_one.code.hx)) <= 4 and
          max(map(weight, dec_one.code.hz)) <= 486 and degrees(dec_one.code)[0] <= 20,
          {"n": dec_one.code.n, "blocks": dec_one.total_blocks,
           "max_X_weight": max(map(weight, dec_one.code.hx)),
           "max_Z_weight": max(map(weight, dec_one.code.hz)),
           "degrees_total_X_Z": degrees(dec_one.code)})
    qp = quotient_partition_preserved(full_one, dec_one.code)
    check("all old weight-at-most-4 X values preserve syndrome/quotient partitions", qp[0], qp[1])

    mixed_clauses = [
        ((0, True), (1, True), (2, False)),
        ((0, False), (3, True), (4, False)),
        ((0, True), (5, False), (6, True)),
        ((0, False), (7, True), (8, False)),
    ]
    bm = Builder()
    mixed_c = bm.build_formula(9, mixed_clauses)
    mixed = from_code(mixed_c, "occurrence4_mixed")
    mixed_full = direct_sum(repetition3_matrix(mixed), comp_m, "mixed+G")
    mixed_dec = decorate_z(mixed_full, "DZ(mixed+G)")
    mixed_id = transformed_rowspace_expected(mixed_full, mixed_dec)
    mixed_states = sentinel_state_audit(mixed_dec)
    mixed_z = two_fault_audit(mixed_dec.code, "Z", mixed_dec.z_orders)
    check("occurrence-four instance hits the universal weight constants",
          max(map(weight, mixed.hz)) == 40 and
          max(map(weight, mixed_full.hz)) == 120 and
          max(map(weight, mixed_dec.code.hz)) == 486,
          {"old": max(map(weight, mixed.hz)),
           "R3": max(map(weight, mixed_full.hz)),
           "decorated": max(map(weight, mixed_dec.code.hz))})
    check("occurrence-four transform identities and sentinel invariant",
          mixed_id["css"] and mixed_id["rank_identity"] and
          all(x["all_duplicates_one_data"] for x in mixed_states),
          {"identity": mixed_id, "n": mixed_dec.code.n,
           "blocks": mixed_dec.total_blocks,
           "state_duplicates": sum(len(x["duplicate_state_deltas"]) for x in mixed_states)})
    check("occurrence-four exhaustive one/two-column Z audit", mixed_z["safe"], mixed_z)

    k4 = k4_no()
    k4_schedules = [ch for ch in product(range(3), repeat=4) if schedule_ok(k4, ch)]
    check("K4 malformed-input X negative control", len(k4_schedules) == 0,
          {"safe": len(k4_schedules), "total": 81})
    k4_full = direct_sum(repetition3_matrix(from_code(k4, "K4")), comp_m, "R3(K4)+G")
    k4_dec = decorate_z(k4_full, "DZ(R3(K4)+G)")
    k4_id = transformed_rowspace_expected(k4_full, k4_dec)
    k4_z = two_fault_audit(k4_dec.code, "Z", k4_dec.z_orders)
    check("decorated malformed branch rank/CSS/Z safety",
          k4_id["css"] and k4_id["rank_identity"] and k4_z["safe"],
          {"identity": k4_id, "Z": k4_z})

    # Real negative control for the order invariant.  In companion Z row 2,
    # grouping all marker openings before the old data gates makes the static
    # weight-3 logical {0,1,8} sit between two equal marker states.
    bad_dec = decorate_z(comp_m, "bad-order-negative-control")
    source_ri = 2
    blocks = bad_dec.blocks_by_row[source_ri]
    source_support = support(comp_m.hz[source_ri], comp_m.n)
    logical_first = [0, 1, 8]
    bad_data_order = logical_first + [q for q in source_support
                                      if q not in logical_first]
    bad_main_order = ([a for a, b, c in blocks] + bad_data_order +
                      [q for a, b, c in blocks for q in (b, c)])
    bad_orders = list(bad_dec.z_orders)
    bad_orders[bad_dec.decorated_row_indices[source_ri]] = tuple(bad_main_order)
    bad_audit = two_fault_audit(bad_dec.code, "Z", bad_orders)
    check("grouped-opening sentinel order mutation is rejected",
          not bad_audit["safe"] and
          bad_audit["kind"] == "two-column" and
          bad_audit["logical_support"] == logical_first,
          bad_audit)

    report = {
        "verdict": "PASS",
        "python": sys.version.split()[0],
        "checks": len(checks),
        "theorem": {"characters": len(theorem), "sha256": theorem_hash},
        "details": checks,
    }
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
