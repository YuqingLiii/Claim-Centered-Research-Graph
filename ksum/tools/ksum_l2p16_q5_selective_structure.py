#!/usr/bin/env python3
"""Exact q=5,K=2 selective-kernel reconnaissance beyond N=16.

The orbit feature matrix and exact l1 primal are imported from the phase-14
independent engine.  This script retains the returned sparse witness and
extracts its support, feature rank, coefficients, and tail mass.  Every
arithmetic operation used for ranks, LPs, and witness checks is SymPy
rational arithmetic.

This is finite numerical reconnaissance.  It makes no asymptotic claim.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import sys
import time
from pathlib import Path

from sympy import Matrix, Rational
from sympy.solvers.simplex import linprog

sys.path.insert(0, str(Path(__file__).resolve().parent))
from ksum_l2p14_target_scale_sweep import (  # noqa: E402
    exact_primal,
    independent_rows,
    moment_row,
    orbits,
    qstr,
    row_patterns,
)


def digest_json(obj) -> str:
    blob = json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(blob).hexdigest()


def exact_dual_cutting_plane(B: Matrix, labels: list[int]):
    """Exact Chebyshev dual by adding the most violated orbit constraint."""
    rank, n = B.rows, B.cols
    _, pivots = B.rref()
    columns = list(pivots)
    iterations = 0
    while True:
        iterations += 1
        c = [Rational(0)] * (2 * rank) + [Rational(1)]
        A, b = [], []
        for j in columns:
            col = [B[i, j] for i in range(rank)]
            A.append([-x for x in col] + col + [-1])
            b.append(-labels[j])
            A.append(col + [-x for x in col] + [-1])
            b.append(labels[j])
        val, sol = linprog(c, A, b)
        y = [sol[i] - sol[rank + i] for i in range(rank)]
        eps = sol[-1]
        if val != eps:
            raise AssertionError((val, eps))
        residuals = [
            Rational(labels[j]) - sum(B[i, j] * y[i] for i in range(rank))
            for j in range(n)
        ]
        maxabs = max(abs(x) for x in residuals)
        if maxabs <= eps:
            break
        j = max(range(n), key=lambda k: abs(residuals[k]))
        columns.append(j)
    active = [j for j, x in enumerate(residuals) if abs(x) == eps]
    signs = {j: 1 if residuals[j] > 0 else -1 for j in active}
    Aeq = [
        [signs[j] * B[i, j] for j in active]
        for i in range(rank)
    ] + [[1] * len(active)]
    _zero, amps = linprog(
        [0] * len(active), [[0] * len(active)], [0], Aeq, [0] * rank + [1]
    )
    w = [Rational(0)] * n
    for pos, j in enumerate(active):
        w[j] = signs[j] * amps[pos]
    support = [j for j, x in enumerate(w) if x]
    if sum(abs(x) for x in w) != 1:
        raise AssertionError("dual-reconstructed witness has wrong l1")
    if sum(labels[j] * w[j] for j in range(n)) != eps:
        raise AssertionError("dual and reconstructed primal disagree")
    return eps, w, support, iterations, len(columns)


def orbit_record(H, weight):
    slots = [list(x) for x in H]
    totals = [sum(x) for x in H]
    products = [x[0] * x[1] for x in H]
    Ct = sum(products)
    return {
        "orbit": slots,
        "totals": totals,
        "products": products,
        "Ct": Ct,
        "label": 1 if Ct > 0 else -1,
        "weight": qstr(weight),
        "abs_weight": qstr(abs(weight)),
    }


def run_case(N: int, D: int, use_dual: bool = False):
    started = time.perf_counter()
    hs = orbits(N)
    rps = row_patterns(D)
    rows = [[moment_row(H, rp) for H in hs] for rp in rps]
    M = Matrix(rows)
    B, basis_inds = independent_rows(M)
    labels = [1 if sum(r * u for r, u in H) > 0 else -1 for H in hs]
    dual_meta = None
    if use_dual:
        eps, w, support, iterations, constrained = exact_dual_cutting_plane(B, labels)
        dual_meta = {
            "iterations": iterations,
            "final_constrained_orbit_count": constrained,
        }
    else:
        eps, w, l1, _unused_tail, overlap = exact_primal(B, labels)
        if l1 != 1 or overlap != 0:
            raise AssertionError((l1, overlap))
        support = [j for j, x in enumerate(w) if x]
    signs = {j: 1 if w[j] > 0 else -1 for j in support}
    tail_threshold = math.ceil(D * D / 4)
    tail_mass = sum(abs(w[j]) for j in support
                    if sum(r * u for r, u in hs[j]) >= tail_threshold)
    support_matrix = Matrix([[B[i, j] for j in support] for i in range(B.rows)])
    signed_support_matrix = Matrix(
        [[signs[j] * B[i, j] for j in support] for i in range(B.rows)]
        + [[1] * len(support)]
    )
    return {
        "N": N,
        "D_polynomial_cutoff": D,
        "orbit_count": len(hs),
        "raw_row_count": len(rps),
        "exact_rank": B.rows,
        "nullity": len(hs) - B.rows,
        "exact_optimum_correlation": qstr(eps),
        "solver_path": "exact dual cutting-plane" if use_dual else "exact l1 primal",
        "dual_cutting_plane": dual_meta,
        "above_two_thirds": bool(eps > Rational(2, 3)),
        "sparse_primal_support_size": len(support),
        "support_feature_rank": support_matrix.rank(),
        "signed_augmented_support_rank": signed_support_matrix.rank(),
        "tail_threshold_Ct": tail_threshold,
        "sparse_primal_tail_mass": qstr(tail_mass),
        "sparse_primal_tail_mass_at_least_quarter": bool(tail_mass >= Rational(1, 4)),
        "positive_support_count": sum(1 for j in support if w[j] > 0),
        "negative_support_count": sum(1 for j in support if w[j] < 0),
        "support": [orbit_record(hs[j], w[j]) for j in support],
        "basis_row_indices": basis_inds,
        "orbit_sha256": digest_json(hs),
        "raw_matrix_sha256": digest_json(rows),
        "elapsed_seconds": round(time.perf_counter() - started, 6),
    }


def parse_case(spec: str) -> tuple[int, int]:
    try:
        n, d = spec.split(":")
        return int(n), int(d)
    except Exception as exc:
        raise argparse.ArgumentTypeError("case must be N:D") from exc


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--output", required=True)
    ap.add_argument("--case", action="append", type=parse_case, default=[])
    ap.add_argument("--dual", action="store_true")
    args = ap.parse_args()
    cases = args.case or (
        [(N, 5) for N in range(11, 17)]
        + [(N, 6) for N in range(17, 24)]
        + [(17, 7), (18, 7)]
    )
    results = []
    total_started = time.perf_counter()
    for N, D in cases:
        print(f"starting N={N},D={D}", flush=True)
        result = run_case(N, D, use_dual=args.dual)
        results.append(result)
        print(
            f"completed N={N},D={D}, corr={result['exact_optimum_correlation']}, "
            f"support={result['sparse_primal_support_size']}, "
            f"seconds={result['elapsed_seconds']}",
            flush=True,
        )
    out = {
        "scope": "q=5,K=2 selective orbit-feature nullspace",
        "tier": "NUMERICAL exact finite arithmetic; no asymptotic inference",
        "degree_convention": "all orbit moment rows of degree <D",
        "solver": "exact SymPy l1 primal; returned positive/negative decomposition checked disjoint",
        "requested_cases": [{"N": n, "D": d} for n, d in cases],
        "results": results,
        "total_elapsed_seconds": round(time.perf_counter() - total_started, 6),
    }
    path = Path(args.output)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({
        "case_count": len(results),
        "total_elapsed_seconds": out["total_elapsed_seconds"],
    }, indent=2))


if __name__ == "__main__":
    main()
