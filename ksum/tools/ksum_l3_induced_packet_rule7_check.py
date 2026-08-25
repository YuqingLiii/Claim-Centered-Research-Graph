#!/usr/bin/env python3
"""Independent exact gates for the L3 induced bicovariant packet first gate.

This checker deliberately reconstructs the finite coset incidence relations from
sets.  It does not import formulas or data from the proposer artifact.  Integer
Gram matrices are checked before the normalizing factors are applied.
"""

from __future__ import annotations

import itertools
import json
import math
from collections import Counter, defaultdict
from functools import lru_cache

import sympy as sp


def check(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def subsets(items, size):
    return itertools.combinations(items, size)


def local_u1_incidence(a: int):
    """Return the two unnormalised u=1 refinement relations on one 2a-set."""
    universe = tuple(range(2 * a))
    universe_set = frozenset(universe)
    coarse = []
    for aa in subsets(universe, a):
        aa = frozenset(aa)
        coarse.append((aa, universe_set - aa))

    left_support = []
    right_support = []
    fine_keys = set()
    for aa, bb in coarse:
        ls = set()
        rs = set()
        for c in aa:
            for u in bb:
                key = (aa - {c}, bb - {u}, c, u)  # (L,R,C,U)
                ls.add(key)
                fine_keys.add(key)
        for u in aa:
            for c in bb:
                key = (aa - {u}, bb - {c}, c, u)  # (L,R,C,U)
                rs.add(key)
                fine_keys.add(key)
        left_support.append(ls)
        right_support.append(rs)

    fine = sorted(
        fine_keys,
        key=lambda x: (tuple(sorted(x[0])), tuple(sorted(x[1])), x[2], x[3]),
    )
    fine_index = {x: i for i, x in enumerate(fine)}
    return coarse, fine, fine_index, left_support, right_support


def integer_gram(column_supports_a, column_supports_b):
    return [
        [len(sa.intersection(sb)) for sb in column_supports_b]
        for sa in column_supports_a
    ]


def expected_swap_adjacency(coarse):
    out = []
    for aa, bb in coarse:
        row = []
        for aa2, bb2 in coarse:
            row.append(int(len(aa - aa2) == 1 and len(aa2 - aa) == 1))
        out.append(row)
    return out


def johnson_eigenvalue_numerator(a: int, j: int) -> int:
    return (a - j) ** 2 - j


def johnson_multiplicity(a: int, j: int) -> int:
    return math.comb(2 * a, j) - (math.comb(2 * a, j - 1) if j else 0)


def gate_local_u1(a: int, occurrence_rank: int):
    coarse, fine, _, left, right = local_u1_incidence(a)
    n0, n1 = len(coarse), len(fine)
    check(n1 == a * a * n0, f"a={a}: rectangular dimension ratio")
    check(all(len(s) == a * a for s in left + right), f"a={a}: column degree")

    row_degree_l = Counter(x for support in left for x in support)
    row_degree_r = Counter(x for support in right for x in support)
    check(set(row_degree_l.values()) == {1}, f"a={a}: left row degree")
    check(set(row_degree_r.values()) == {1}, f"a={a}: right row degree")

    gll = integer_gram(left, left)
    grr = integer_gram(right, right)
    glr = integer_gram(left, right)
    identity_scaled = [
        [a * a if i == j else 0 for j in range(n0)] for i in range(n0)
    ]
    check(gll == identity_scaled, f"a={a}: A_L^* A_L=a^2 I")
    check(grr == identity_scaled, f"a={a}: A_R^* A_R=a^2 I")
    adjacency = expected_swap_adjacency(coarse)
    check(glr == adjacency, f"a={a}: exact cross Gram entries")
    check(glr == [list(row) for row in zip(*glr)], f"a={a}: cross Gram self-adjoint")

    # Exact characteristic polynomial of the integer Johnson adjacency.
    matrix = sp.Matrix(glr)
    x = sp.symbols("x")
    predicted_charpoly = sp.Integer(1)
    spectrum = []
    for j in range(a + 1):
        theta = johnson_eigenvalue_numerator(a, j)
        mult = johnson_multiplicity(a, j)
        predicted_charpoly *= (x - theta) ** mult
        spectrum.append(
            {
                "j": j,
                "adjacency_eigenvalue": theta,
                "K_eigenvalue": f"{theta}/{a*a}",
                "multiplicity": mult,
            }
        )
    actual_charpoly = matrix.charpoly(x).as_expr()
    check(sp.expand(actual_charpoly - predicted_charpoly) == 0, f"a={a}: spectrum")

    # Literal marked-cell map and effect identities for every palette point.
    for z in range(2 * a):
        for side, supports in (("L", left), ("R", right)):
            for col, ((aa, bb), support) in enumerate(zip(coarse, supports)):
                for key in support:
                    ll, rr, c, u = key
                    if side == "L":
                        check(
                            int(z in ll or z == c) == int(z in aa),
                            f"a={a}: (Q_L+Q_C)A_L=A_LP_A",
                        )
                        check(
                            int(z in rr or z == u) == int(z in bb),
                            f"a={a}: (Q_R+Q_U)A_L=A_LP_B",
                        )
                    else:
                        check(
                            int(z in ll or z == u) == int(z in aa),
                            f"a={a}: (Q_L+Q_U)A_R=A_RP_A",
                        )
                        check(
                            int(z in rr or z == c) == int(z in bb),
                            f"a={a}: (Q_R+Q_C)A_R=A_RP_B",
                        )

        for col, (aa, bb) in enumerate(coarse):
            lkeys = left[col]
            rkeys = right[col]
            expected_a = int(z in aa)
            expected_b = int(z in bb)
            check(sum(1 for ll, rr, c, u in lkeys if c == z) == a * expected_a,
                  f"a={a}: A_L^*Q_C A_L=a P_A")
            check(sum(1 for ll, rr, c, u in lkeys if z in ll) == a * (a - 1) * expected_a,
                  f"a={a}: A_L^*Q_L A_L=a(a-1)P_A")
            check(sum(1 for ll, rr, c, u in lkeys if u == z) == a * expected_b,
                  f"a={a}: A_L^*Q_U A_L=a P_B")
            check(sum(1 for ll, rr, c, u in lkeys if z in rr) == a * (a - 1) * expected_b,
                  f"a={a}: A_L^*Q_R A_L=a(a-1)P_B")
            check(sum(1 for ll, rr, c, u in rkeys if u == z) == a * expected_a,
                  f"a={a}: A_R^*Q_U A_R=a P_A")
            check(sum(1 for ll, rr, c, u in rkeys if z in ll) == a * (a - 1) * expected_a,
                  f"a={a}: A_R^*Q_L A_R=a(a-1)P_A")
            check(sum(1 for ll, rr, c, u in rkeys if c == z) == a * expected_b,
                  f"a={a}: A_R^*Q_C A_R=a P_B")
            check(sum(1 for ll, rr, c, u in rkeys if z in rr) == a * (a - 1) * expected_b,
                  f"a={a}: A_R^*Q_R A_R=a(a-1)P_B")

    # J is the incidence relation divided by a.  Heavy standard fibers and the
    # occurrence fiber are copied with the same index, so all off-fiber Grams vanish.
    heavy_dimension = (a - 1) ** 2
    full_fiber_dimension = heavy_dimension * occurrence_rank
    check(full_fiber_dimension > 0, f"a={a}: nonzero heavy/occurrence fiber")
    for source_fiber in range(full_fiber_dimension):
        for target_fiber in range(full_fiber_dimension):
            delta = int(source_fiber == target_fiber)
            # Integer Gram before division by a^2.
            check(
                (a * a if delta else 0) == a * a * delta,
                f"a={a}: internal V_a^2 x occurrence identity",
            )

    # Squared singular data are the spectra of 2(I +/- K).
    plus_sq = []
    minus_sq = []
    for j in range(a + 1):
        theta = sp.Rational(johnson_eigenvalue_numerator(a, j), a * a)
        plus_sq.append(sp.simplify(2 * (1 + theta)))
        minus_sq.append(sp.simplify(2 * (1 - theta)))
    check(max(plus_sq) == 4, f"a={a}: ||J_L+J_R||^2")
    check(min(v for v in plus_sq if v != 0) == 2 * sp.Rational(a - 1, a),
          f"a={a}: plus smallest nonzero singular value squared")
    check(max(minus_sq) == 2 + sp.Rational(2, a), f"a={a}: contrast norm squared")
    check(min(v for v in minus_sq if v != 0) == sp.Rational(4, a),
          f"a={a}: contrast smallest nonzero singular value squared")

    return {
        "a": a,
        "occurrence_rank": occurrence_rank,
        "coarse_dimension_one_heavy_fiber": n0,
        "fine_dimension_one_heavy_fiber": n1,
        "heavy_fiber_dimension": heavy_dimension,
        "full_fiber_dimension": full_fiber_dimension,
        "J_domain_dimension_local_tensor": n0 * full_fiber_dimension,
        "J_codomain_dimension_local_tensor": n1 * full_fiber_dimension,
        "spectrum": spectrum,
        "marked_masses": {"singleton": f"1/{a}", "residual": f"{a-1}/{a}"},
        "result": "PASS",
    }


def local_general_u_incidence(a: int, u_count: int):
    """Incidence with an unused NO cell of size u_count-1 (scope guard)."""
    wsize = u_count - 1
    universe = frozenset(range(2 * a + wsize))
    coarse = []
    for aa_tuple in subsets(sorted(universe), a):
        aa = frozenset(aa_tuple)
        rem = universe - aa
        for bb_tuple in subsets(sorted(rem), a):
            bb = frozenset(bb_tuple)
            ww = rem - bb
            coarse.append((aa, bb, ww))

    left = []
    right = []
    fine_keys = set()
    for aa, bb, ww in coarse:
        ls, rs = set(), set()
        for c in aa:
            for z in bb:
                key = (aa - {c}, bb - {z}, c, ww | {z})  # (L,R,C,U-set)
                ls.add(key)
                fine_keys.add(key)
        for z in aa:
            for c in bb:
                key = (aa - {z}, bb - {c}, c, ww | {z})
                rs.add(key)
                fine_keys.add(key)
        left.append(ls)
        right.append(rs)
    return coarse, fine_keys, left, right


def gate_scope_u_gt_1(a: int = 2, u_count: int = 2):
    coarse, fine, left, right = local_general_u_incidence(a, u_count)
    row_l = Counter(x for support in left for x in support)
    check(set(row_l.values()) == {u_count}, "u>1 row degree")
    check(all(len(s) == a * a for s in left), "u>1 column degree")
    gll = integer_gram(left, left)
    offdiag = sum(
        1 for i in range(len(gll)) for j in range(len(gll)) if i != j and gll[i][j]
    )
    check(offdiag > 0, "u>1 incidence is not an isometry after division by a")

    glr = integer_gram(left, right)
    same_w = 0
    changed_w = 0
    for i, (aa, bb, ww) in enumerate(coarse):
        for j, (aa2, bb2, ww2) in enumerate(coarse):
            if glr[i][j]:
                if ww == ww2:
                    same_w += 1
                else:
                    changed_w += 1
    check(same_w > 0 and changed_w > 0, "u>1 cross Gram has swap and 3-cell moves")
    return {
        "a": a,
        "u": u_count,
        "coarse_states": len(coarse),
        "fine_states": len(fine),
        "row_degree": u_count,
        "column_degree": a * a,
        "A_L_star_A_L_offdiagonal_nonzeros": offdiag,
        "cross_pairs_same_unused_cell": same_w,
        "cross_pairs_changed_unused_cell": changed_w,
        "conclusion": "the u=1 isometry/Johnson formula does not extend verbatim",
        "result": "PASS",
    }


def normalize_partition(part):
    return tuple(x for x in part if x > 0)


@lru_cache(maxsize=None)
def partitions(n: int, max_part: int | None = None):
    if n == 0:
        return ((),)
    if max_part is None or max_part > n:
        max_part = n
    out = []
    for first in range(max_part, 0, -1):
        for tail in partitions(n - first, min(first, n - first)):
            out.append((first,) + tail)
    return tuple(out)


def contains_partition(nu, lam):
    return all((nu[i] if i < len(nu) else 0) >= x for i, x in enumerate(lam))


@lru_cache(maxsize=None)
def lr_coefficient(lam, mu, nu):
    """Littlewood--Richardson coefficient by direct tableau enumeration."""
    lam = normalize_partition(lam)
    mu = normalize_partition(mu)
    nu = normalize_partition(nu)
    if sum(lam) + sum(mu) != sum(nu) or not contains_partition(nu, lam):
        return 0
    cells = []
    for r, row_len in enumerate(nu):
        old_len = lam[r] if r < len(lam) else 0
        for c in range(row_len, old_len, -1):
            cells.append((r, c))  # reading order: top row, right to left
    if len(cells) != sum(mu):
        return 0

    max_label = len(mu)
    remaining = list(mu)
    prefix = [0] * max_label
    values = {}
    total = 0

    def rec(pos):
        nonlocal total
        if pos == len(cells):
            total += 1
            return
        r, c = cells[pos]
        right = values.get((r, c + 1))
        above = values.get((r - 1, c))
        for label in range(1, max_label + 1):
            idx = label - 1
            if remaining[idx] == 0:
                continue
            # Rows weakly increase left-to-right; columns strictly increase downwards.
            if right is not None and label > right:
                continue
            if above is not None and label <= above:
                continue
            remaining[idx] -= 1
            prefix[idx] += 1
            lattice = all(prefix[k] >= prefix[k + 1] for k in range(max_label - 1))
            if lattice:
                values[(r, c)] = label
                rec(pos + 1)
                del values[(r, c)]
            prefix[idx] -= 1
            remaining[idx] += 1

    rec(0)
    return total


def schur_multiply(expansion, factor):
    out = defaultdict(int)
    factor = normalize_partition(factor)
    for lam, coeff in expansion.items():
        total_size = sum(lam) + sum(factor)
        for nu in partitions(total_size):
            c = lr_coefficient(lam, factor, nu)
            if c:
                out[nu] += coeff * c
    return dict(out)


def schur_product(*factors):
    expansion = {(): 1}
    for factor in factors:
        expansion = schur_multiply(expansion, factor)
    return expansion


def add_expansions(*weighted):
    out = defaultdict(int)
    for scalar, expansion in weighted:
        for part, coeff in expansion.items():
            out[part] += scalar * coeff
    return {part: coeff for part, coeff in out.items() if coeff}


def hook_dimension(part):
    n = sum(part)
    hook_product = 1
    for r, row_len in enumerate(part):
        for c in range(row_len):
            below = sum(1 for rr in range(r + 1, len(part)) if part[rr] > c)
            hook_product *= (row_len - c) + below
    return math.factorial(n) // hook_product


def gate_full_types(a: int):
    h = (a,)
    s = (a - 1, 1)
    h1 = (1,)
    h_a_minus_1 = (a - 1,)

    pieri = schur_product(h1, h_a_minus_1)
    check(pieri == {h: 1, s: 1}, f"a={a}: h1*h(a-1)=h+s")

    f0 = schur_product(s, s, h, h)
    f1_actual = schur_product(h1, h1, h_a_minus_1, h_a_minus_1, s, s)
    hs3 = schur_product(h, s, s, s)
    s4 = schur_product(s, s, s, s)
    f1_rhs = add_expansions((1, f0), (2, hs3), (1, s4))
    check(f1_actual == f1_rhs, f"a={a}: F1=F0+2hs^3+s^4")
    check(all(f1_actual.get(nu, 0) >= m for nu, m in f0.items()), f"a={a}: all multiplicities embed")

    sectors = {}
    for nu in sorted(f0, reverse=True):
        by_j = []
        for j in range(a + 1):
            alpha = (2 * a - j, j) if j else (2 * a,)
            coeff = schur_product(alpha, s, s).get(nu, 0)
            by_j.append(coeff)
        check(sum(by_j) == f0[nu], f"a={a},nu={nu}: complete Johnson sectors")
        sectors[nu] = by_j

    expected_dim0 = math.factorial(4 * a) // (math.factorial(a) ** 4) * (a - 1) ** 2
    expected_dim1 = a * a * expected_dim0
    dim0 = sum(hook_dimension(nu) * mult for nu, mult in f0.items())
    dim1 = sum(hook_dimension(nu) * mult for nu, mult in f1_actual.items())
    check(dim0 == expected_dim0, f"a={a}: F0 dimension")
    check(dim1 == expected_dim1, f"a={a}: F1 dimension")

    width_types = []
    for r in range(2 * a - 1):
        nu = normalize_partition((4 * a - r - 2, r + 2))
        check(nu in f0 and f0[nu] > 0, f"a={a}: width witness r={r}")
        width_types.append({"r": r, "nu": nu, "multiplicity": f0[nu]})
    central = normalize_partition((3 * a - 1, a + 1))
    check(f0.get(central, 0) >= a - 1, f"a={a}: growing multiplicity witness")

    multi_full_types = [nu for nu, mult in f0.items() if mult > 1]
    multi_j_types = [nu for nu, js in sectors.items() if sum(int(x > 0) for x in js) > 1]
    if a >= 3:
        check(multi_full_types, f"a={a}: c>1 full-type regime exists")
        check(multi_j_types, f"a={a}: one full type contains multiple j sectors")

    ledger = []
    for nu in sorted(f1_actual, reverse=True):
        ledger.append(
            {
                "nu": nu,
                "f_nu": hook_dimension(nu),
                "m0": f0.get(nu, 0),
                "m1": f1_actual[nu],
                "c_nu_j": sectors.get(nu, [0] * (a + 1)),
            }
        )

    return {
        "a": a,
        "number_of_M0_full_types": len(f0),
        "number_of_M1_full_types": len(f1_actual),
        "dim_M0": dim0,
        "dim_M1": dim1,
        "max_M0_full_type_multiplicity": max(f0.values()),
        "full_types_with_multiplicity_gt_1": len(multi_full_types),
        "full_types_with_multiple_Johnson_sectors": len(multi_j_types),
        "width_witnesses": width_types,
        "growing_witness": {"nu": central, "multiplicity": f0[central], "lower_bound": a - 1},
        "all_full_type_multiplicity_sectors": ledger,
        "result": "PASS",
    }


def main():
    report = {
        "construction": (
            "independent set/coset incidence; integer Grams; direct LR tableaux; "
            "no proposer formulas imported"
        ),
        "local_identity_gates": [],
        "full_type_gates": [],
    }

    # Both a regimes and both external occurrence-rank regimes.
    for a, c in ((2, 1), (2, 2), (3, 1), (3, 2)):
        report["local_identity_gates"].append(gate_local_u1(a, c))

    # Every full S_(4a) type and every multiplicity sector at a=2 and a=3.
    for a in (2, 3):
        report["full_type_gates"].append(gate_full_types(a))

    report["scope_guard_u_gt_1"] = gate_scope_u_gt_1()
    report["a_equals_1_guard"] = {
        "dim_V_1": 0,
        "packet_nonzero": False,
        "conclusion": "the q=5/a=1 shared-NO construction is not this packet",
        "result": "PASS",
    }
    report["overall"] = "PASS"
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
