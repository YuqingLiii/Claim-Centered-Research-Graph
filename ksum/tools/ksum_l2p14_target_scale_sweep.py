#!/usr/bin/env python3
"""Exact finite sweep for the q=5, K=2 variable-pair-total orbit family.

All linear algebra and LP arithmetic is rational (SymPy).  D denotes the
polynomial-degree cutoff: rows are orbit averages of monomials of degree < D.
Consequently D corresponds only to the usual query lower-bound scale D/2;
the script never identifies D with a number of queries.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path

from sympy import Matrix, Rational
from sympy.solvers.simplex import linprog


def fall(x: int, a: int) -> int:
    out = 1
    for j in range(a):
        out *= x - j
    return out


def pair_kernel(slot: tuple[int, int], pattern: tuple[int, int]) -> int:
    """Twice A_{a,b}(r,u), avoiding row-irrelevant denominators."""
    r, u = slot
    a, b = pattern
    return fall(r, a) * fall(u, b) + fall(r, b) * fall(u, a)


def orbits(N: int) -> list[tuple[tuple[int, int], tuple[int, int]]]:
    types = [(r, u) for r in range(N + 1) for u in range(r, N + 1)
             if r + u >= 1]
    return [(x, y) for i, x in enumerate(types) for y in types[i:]
            if sum(x) + sum(y) == N]


def row_patterns(D: int):
    pats = [(a, b) for a in range(D) for b in range(a, D)
            if 0 < a + b < D]
    rows: list[tuple[tuple[int, int], ...]] = [()]
    rows.extend((p,) for p in pats)
    rows.extend((p, q) for i, p in enumerate(pats) for q in pats[i:]
                if sum(p) + sum(q) < D)
    return rows


def moment_row(H, patterns):
    if not patterns:
        return 1
    if len(patterns) == 1:
        p = patterns[0]
        return pair_kernel(H[0], p) + pair_kernel(H[1], p)
    p, q = patterns
    return (pair_kernel(H[0], p) * pair_kernel(H[1], q)
            + pair_kernel(H[1], p) * pair_kernel(H[0], q))


def independent_rows(M: Matrix) -> tuple[Matrix, list[int]]:
    # Pivot columns of M.T are independent rows of M.
    _, inds = M.T.rref()
    return Matrix([list(M[i, :]) for i in inds]), list(inds)


def exact_primal(B: Matrix, labels: list[int], tail=None):
    """Max labels.w with B w=0, represented as w=p-n, sum(p+n)=1.

    If tail is supplied, the LP adds sum_tail(p+n)>=1/4.  The returned
    diagnostics explicitly check whether the relaxation has p,n disjoint,
    hence really represents absolute mass rather than artificial cancellation.
    """
    rank, n = B.rows, B.cols
    c = [-Rational(x) for x in labels] + [Rational(x) for x in labels]
    Aeq, beq = [], []
    for i in range(rank):
        row = [B[i, j] for j in range(n)]
        Aeq.append(row + [-x for x in row])
        beq.append(0)
    Aeq.append([1] * (2 * n))
    beq.append(1)
    # SymPy 1.14 has a dimension bug when A/b are None but A_eq is present;
    # retain one harmless inequality in the ungated problem.
    A, b = [[0] * (2 * n)], [0]
    if tail is not None:
        tr = [-1 if j in tail else 0 for j in range(n)]
        A, b = [tr + tr], [-Rational(1, 4)]
    negval, sol = linprog(c, A, b, Aeq, beq)
    p, nvec = sol[:n], sol[n:]
    w = [p[j] - nvec[j] for j in range(n)]
    l1 = sum(abs(x) for x in w)
    tail_l1 = None if tail is None else sum(abs(w[j]) for j in tail)
    overlap = sum(min(p[j], nvec[j]) for j in range(n))
    return -negval, w, l1, tail_l1, overlap


def qstr(x):
    x = Rational(x)
    return str(x.p) if x.q == 1 else f"{x.p}/{x.q}"


def digest_json(obj) -> str:
    blob = json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(blob).hexdigest()


def run_case(N: int, D: int, do_tail: bool):
    hs = orbits(N)
    rps = row_patterns(D)
    rows = [[moment_row(H, rp) for H in hs] for rp in rps]
    M = Matrix(rows)
    B, basis_inds = independent_rows(M)
    labels = [1 if sum(r * u for r, u in H) > 0 else -1 for H in hs]
    pcorr, w, wl1, _, overlap = exact_primal(B, labels)
    corr = pcorr
    nullity = len(hs) - B.rows
    if nullity > 0 and (wl1 != 1 or overlap != 0):
        raise AssertionError((N, D, corr, wl1, overlap))
    Ct = [sum(r * u for r, u in H) for H in hs]
    threshold = max(1, math.ceil(D * D / 4))
    tail = {j for j, x in enumerate(Ct) if x >= threshold}
    tail_result = None
    if do_tail and not tail:
        tail_result = {
            "threshold": threshold,
            "orbit_count": 0,
            "feasible": False,
            "reason": "no orbit reaches the chosen threshold",
        }
    elif do_tail and tail and nullity > 0:
        tcorr, tw, tl1, tmass, toverlap = exact_primal(B, labels, tail)
        certified = bool(tl1 == 1 and tmass >= Rational(1, 4) and toverlap == 0)
        method = "absolute-value LP; valid only when returned decomposition is disjoint"
        tail_result = {
            "threshold": threshold,
            "orbit_count": len(tail),
            "feasible": True,
            "method": method,
            "lp_correlation": qstr(tcorr),
            "true_l1": qstr(tl1),
            "true_tail_l1": qstr(tmass),
            "positive_negative_overlap": qstr(toverlap),
            "verified_as_true_absolute_mass_lp": certified,
        }
    return {
        "N": N,
        "D_polynomial_cutoff": D,
        "monomials_have_degree": f"< {D}",
        "query_lower_bound_scale_if_used": qstr(Rational(D, 2)),
        "orbit_count": len(hs),
        "raw_rows": len(rps),
        "exact_rank": B.rows,
        "nullity": nullity,
        "nonzero_annihilator_exists": bool(nullity > 0),
        "unit_l1_max_sign_correlation": qstr(corr),
        "unconstrained_optimum_true_l1": qstr(wl1),
        "unconstrained_optimum_tail_l1_at_threshold": qstr(
            sum(abs(w[j]) for j in tail)
        ),
        "tail_gate": tail_result,
        "orbit_sha256": digest_json(hs),
        "matrix_sha256": digest_json(rows),
        "basis_row_indices": basis_inds,
    }


def phase13_tail_reproduction():
    N, D = 8, 8
    hs = orbits(N)
    rps = row_patterns(D)
    M = Matrix([[moment_row(H, rp) for H in hs] for rp in rps])
    B, _ = independent_rows(M)
    labels = [1 if sum(r * u for r, u in H) > 0 else -1 for H in hs]
    Ct = [sum(r * u for r, u in H) for H in hs]
    out = []
    for threshold in (4, 6, 8):
        tail = {j for j, x in enumerate(Ct) if x >= threshold}
        corr, _w, l1, mass, overlap = exact_primal(B, labels, tail)
        out.append({
            "threshold": threshold,
            "required_absolute_mass": "1/4",
            "unit_l1_max_sign_correlation": qstr(corr),
            "true_l1": qstr(l1),
            "true_tail_l1": qstr(mass),
            "positive_negative_overlap": qstr(overlap),
            "verified_as_true_absolute_mass_lp": bool(
                l1 == 1 and mass >= Rational(1, 4) and overlap == 0
            ),
        })
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--output", required=True)
    args = ap.parse_args()
    cases = []
    for N in range(6, 13):
        Ds = sorted({math.floor(math.sqrt(N)), math.ceil(math.sqrt(N)),
                     math.ceil(2 * math.sqrt(N))})
        for D in Ds:
            cases.append(run_case(N, D, do_tail=True))
    reproduction = [run_case(8, D, do_tail=False) for D in (2, 8, 9)]
    out = {
        "scope": "q=5, K=2 variable-pair-total orbit family",
        "arithmetic": "exact integers/rationals via SymPy",
        "degree_convention": "D is a polynomial cutoff; moment degree is <D; query scale is D/2",
        "phase13_reproduction": reproduction,
        "phase13_D8_tail_reproduction": phase13_tail_reproduction(),
        "target_scale_sweep": cases,
    }
    path = Path(args.output)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(out, indent=2))


if __name__ == "__main__":
    main()
