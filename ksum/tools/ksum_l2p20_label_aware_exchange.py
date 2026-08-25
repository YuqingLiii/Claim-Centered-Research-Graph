#!/usr/bin/env python3
"""Deterministic label-aware Fekete/Remez basis exchange at q=5,K=2.

Initialization interleaves balanced NO-boundary columns with high-Ct balanced
YES columns, greedily retaining independent feature columns.  The first full
fundamental circuit is then improved by a closed Remez exchange rule: compute
the exact support-interpolating dual, insert its lexicographically first worst
global residual orbit, examine the four smallest-cofactor deletions with
same-label deletions first, and choose among them the deletion maximizing

    score = correlation^2 / global_max_abs_dual_residual,

subject to exact tail mass >=1/4.  Ties use correlation, tail mass, then the
lexicographic support tuple.  No final correlation LP or Phase-16 optimal
support is queried.

All matrix arithmetic is exact SymPy rational arithmetic.  This is finite
proposer reconnaissance, not an asymptotic proof.
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

sys.path.insert(0, str(Path(__file__).resolve().parent))
from ksum_l2p14_target_scale_sweep import (  # noqa: E402
    independent_rows,
    moment_row,
    orbits,
    qstr,
    row_patterns,
)


def digest_json(obj) -> str:
    blob = json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(blob).hexdigest()


def orbit_stats(H):
    totals = [sum(x) for x in H]
    Ct = sum(r * u for r, u in H)
    return totals, Ct


def orbit_record(H, weight=None):
    totals, Ct = orbit_stats(H)
    out = {
        "orbit": [list(x) for x in H],
        "totals": totals,
        "Ct": Ct,
        "label": 1 if Ct > 0 else -1,
    }
    if weight is not None:
        out["weight"] = qstr(weight)
        out["abs_weight"] = qstr(abs(weight))
    return out


def interleaved_order(hs):
    no, yes = [], []
    for j, H in enumerate(hs):
        totals, Ct = orbit_stats(H)
        total_balance = totals[0] * totals[1]
        total_gap = abs(totals[0] - totals[1])
        if Ct == 0:
            no.append(((-total_balance, total_gap, j), j))
        else:
            yes.append(((-Ct, -total_balance, total_gap, j), j))
    no = [j for _key, j in sorted(no)]
    yes = [j for _key, j in sorted(yes)]
    order = []
    for k in range(max(len(no), len(yes))):
        if k < len(no):
            order.append(no[k])
        if k < len(yes):
            order.append(yes[k])
    return order


def initial_support(B: Matrix, order):
    rank = B.rows
    _rref, pivot_positions = B[:, order].rref()
    basis = [order[k] for k in pivot_positions]
    if len(basis) != rank:
        raise RuntimeError("interleaved greedy order did not produce a basis")
    C = B[:, basis]
    Cinv = C.inv()
    bset = set(basis)
    for j in order:
        if j in bset:
            continue
        a = Cinv * B[:, j]
        if all(x != 0 for x in a):
            return tuple(sorted(basis + [j]))
    raise RuntimeError("no full initial fundamental circuit")


def evaluate_support(B: Matrix, hs, labels, support, threshold):
    support = tuple(sorted(support))
    A = B[:, support]
    if A.rank() != B.rows or len(support) != B.rows + 1:
        return None
    null = A.nullspace()
    if len(null) != 1 or any(x == 0 for x in null[0]):
        return None
    raw = list(null[0])
    raw_l1 = sum(abs(x) for x in raw)
    weights = [x / raw_l1 for x in raw]
    corr = sum(labels[j] * weights[k] for k, j in enumerate(support))
    if corr < 0:
        weights = [-x for x in weights]
        corr = -corr
    tail = sum(abs(weights[k]) for k, j in enumerate(support)
               if orbit_stats(hs[j])[1] >= threshold)
    if corr == 0:
        return {
            "support": support,
            "weights": weights,
            "correlation": corr,
            "tail_mass": tail,
            "max_residual": None,
            "argmax": None,
            "score": Rational(0),
            "dual_pass": False,
        }

    signs = [1 if x > 0 else -1 for x in weights]
    rhs = Matrix([labels[j] - corr * signs[k] for k, j in enumerate(support)])
    dual = A.T.gauss_jordan_solve(rhs)[0]
    residuals = [
        Rational(labels[j]) - sum(B[i, j] * dual[i] for i in range(B.rows))
        for j in range(B.cols)
    ]
    maxres = max(abs(x) for x in residuals)
    argmax = next(j for j, x in enumerate(residuals) if abs(x) == maxres)
    score = corr * corr / maxres if tail >= Rational(1, 4) else Rational(0)
    return {
        "support": support,
        "weights": weights,
        "correlation": corr,
        "tail_mass": tail,
        "max_residual": maxres,
        "argmax": argmax,
        "score": score,
        "dual_pass": bool(maxres <= corr),
        "dual_coefficients": dual,
    }


def merit(state):
    return (
        state["score"],
        state["correlation"],
        state["tail_mass"],
        tuple(-j for j in state["support"]),
    )


def exchange(B, hs, labels, initial, threshold, max_iterations, exchange_width=4):
    current = evaluate_support(B, hs, labels, initial, threshold)
    if current is None:
        raise RuntimeError("initial support is not a full circuit")
    history = []
    stop_reason = None
    for iteration in range(max_iterations + 1):
        history.append({
            "iteration": iteration,
            "correlation": qstr(current["correlation"]),
            "tail_mass": qstr(current["tail_mass"]),
            "max_residual": None if current["max_residual"] is None else qstr(current["max_residual"]),
            "score": qstr(current["score"]),
            "dual_pass": current["dual_pass"],
            "worst_orbit_index": current["argmax"],
        })
        if current["dual_pass"]:
            stop_reason = "global dual bound passed"
            break
        if iteration == max_iterations:
            stop_reason = "closed iteration cap reached"
            break
        entering = current["argmax"]
        if entering in current["support"]:
            stop_reason = "worst residual already in support without global pass"
            break
        weight_by_orbit = dict(zip(current["support"], current["weights"]))
        leaving_order = sorted(
            current["support"],
            key=lambda j: (
                labels[j] != labels[entering],
                abs(weight_by_orbit[j]),
                j,
            ),
        )[:exchange_width]
        candidates = []
        for leaving in leaving_order:
            trial_support = tuple(sorted((set(current["support"]) - {leaving}) | {entering}))
            trial = evaluate_support(B, hs, labels, trial_support, threshold)
            if trial is not None and trial["tail_mass"] >= Rational(1, 4):
                candidates.append(trial)
        if not candidates:
            stop_reason = "no full-circuit tail-feasible worst-orbit exchange"
            break
        best = max(candidates, key=merit)
        if merit(best) <= merit(current):
            stop_reason = "strict local score optimum"
            break
        current = best
    return current, history, stop_reason


def run_case(N: int, D: int, max_iterations=None, exchange_width=4):
    started = time.perf_counter()
    hs = orbits(N)
    rps = row_patterns(D)
    rows = [[moment_row(H, rp) for H in hs] for rp in rps]
    B, basis_rows = independent_rows(Matrix(rows))
    labels = [1 if orbit_stats(H)[1] > 0 else -1 for H in hs]
    threshold = math.ceil(D * D / 4)
    order = interleaved_order(hs)
    initial = initial_support(B, order)
    initial_state = evaluate_support(B, hs, labels, initial, threshold)
    if max_iterations is None:
        max_iterations = 2 * B.rows
    final, history, stop = exchange(
        B, hs, labels, initial, threshold, max_iterations, exchange_width=exchange_width
    )
    return {
        "N": N,
        "D_polynomial_cutoff": D,
        "orbit_count": len(hs),
        "feature_rank": B.rows,
        "tail_threshold_Ct": threshold,
        "initial": {
            "support": [orbit_record(hs[j], initial_state["weights"][k])
                        for k, j in enumerate(initial_state["support"])],
            "correlation": qstr(initial_state["correlation"]),
            "tail_mass": qstr(initial_state["tail_mass"]),
            "max_residual": qstr(initial_state["max_residual"]),
            "score": qstr(initial_state["score"]),
        },
        "final": {
            "support_size": len(final["support"]),
            "support_feature_rank": B[:, final["support"]].rank(),
            "support": [orbit_record(hs[j], final["weights"][k])
                        for k, j in enumerate(final["support"])],
            "correlation": qstr(final["correlation"]),
            "above_two_thirds": bool(final["correlation"] > Rational(2, 3)),
            "tail_mass": qstr(final["tail_mass"]),
            "tail_mass_at_least_quarter": bool(final["tail_mass"] >= Rational(1, 4)),
            "max_residual": qstr(final["max_residual"]),
            "dual_violation_ratio_decimal": float(final["max_residual"] / final["correlation"]),
            "global_dual_bound_passes": final["dual_pass"],
            "score": qstr(final["score"]),
            "worst_orbit": orbit_record(hs[final["argmax"]]),
            "dual_coefficients": [qstr(x) for x in final["dual_coefficients"]],
        },
        "exchange_history": history,
        "exchange_count": len(history) - 1,
        "exchange_width": exchange_width,
        "stop_reason": stop,
        "basis_row_indices": basis_rows,
        "orbit_sha256": digest_json(hs),
        "raw_matrix_sha256": digest_json(rows),
        "elapsed_seconds": round(time.perf_counter() - started, 6),
    }


def parse_case(spec: str):
    try:
        n, d = spec.split(":")
        return int(n), int(d)
    except Exception as exc:
        raise argparse.ArgumentTypeError("case must be N:D") from exc


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--output", required=True)
    ap.add_argument("--case", action="append", type=parse_case, default=[])
    ap.add_argument("--max-iterations", type=int)
    ap.add_argument("--exchange-width", type=int, default=4)
    args = ap.parse_args()
    cases = args.case or [(11, 5), (16, 5), (17, 6), (23, 6), (24, 7), (31, 7)]
    results = []
    started = time.perf_counter()
    for N, D in cases:
        print(f"starting N={N},D={D}", flush=True)
        result = run_case(N, D, args.max_iterations, args.exchange_width)
        results.append(result)
        print(
            f"completed corr={result['final']['correlation']}, "
            f"ratio={result['final']['dual_violation_ratio_decimal']:.6g}, "
            f"exchanges={result['exchange_count']}, stop={result['stop_reason']}",
            flush=True,
        )
    out = {
        "scope": "deterministic label-aware Fekete/Remez exchange at q=5,K=2",
        "tier": "exact finite proposer test; no asymptotic inference",
        "objective": "maximize correlation^2/global_max_abs_dual_residual subject to tail mass >=1/4",
        "iteration_cap": args.max_iterations if args.max_iterations is not None else "2*feature_rank",
        "exchange_width": args.exchange_width,
        "results": results,
        "total_elapsed_seconds": round(time.perf_counter() - started, 6),
    }
    path = Path(args.output)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"cases": len(results), "seconds": out["total_elapsed_seconds"]}, indent=2))


if __name__ == "__main__":
    main()
