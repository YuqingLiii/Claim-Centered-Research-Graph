#!/usr/bin/env python3
"""Test a formula-defined moving q=5 orbit-feature circuit.

For each (N,D), form the lexicographically first feature-column basis and
adjoin the lexicographically first later orbit whose fundamental circuit has
full support.  This is a deterministic linear-algebra formula, not an LP
selected support.  The script computes its exact cofactor kernel and the
candidate dual equioscillation interpolant, then checks all legal orbits.

All arithmetic is exact SymPy integer/rational arithmetic.  Results are
finite proposer reconnaissance, never an asymptotic proof.
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


def orbit_record(H, weight=None):
    Ct = sum(r * u for r, u in H)
    out = {
        "orbit": [list(x) for x in H],
        "Ct": Ct,
        "label": 1 if Ct > 0 else -1,
    }
    if weight is not None:
        out["weight"] = qstr(weight)
        out["abs_weight"] = qstr(abs(weight))
    return out


def solve_candidate_dual(B: Matrix, labels, support, w, corr):
    """Interpolate the complementary-slackness residual on the circuit."""
    signs = [1 if w[j] > 0 else -1 for j in support]
    rhs = Matrix([labels[j] - corr * signs[k] for k, j in enumerate(support)])
    A = Matrix([[B[i, j] for i in range(B.rows)] for j in support])
    solset = A.gauss_jordan_solve(rhs)
    y = solset[0]
    params = solset[1]
    if params.rows:
        y = y.subs({p: 0 for p in params})
    residuals = [
        Rational(labels[j]) - sum(B[i, j] * y[i] for i in range(B.rows))
        for j in range(B.cols)
    ]
    maxabs = max(abs(x) for x in residuals)
    argmax = next(j for j, x in enumerate(residuals) if abs(x) == maxabs)
    support_ok = all(residuals[j] == corr * signs[k]
                     for k, j in enumerate(support))
    return y, residuals, maxabs, argmax, support_ok


def run_case(N: int, D: int):
    started = time.perf_counter()
    hs = orbits(N)
    rps = row_patterns(D)
    rows = [[moment_row(H, rp) for H in hs] for rp in rps]
    M = Matrix(rows)
    B, basis_row_indices = independent_rows(M)
    rank = B.rows
    _rref, basis_columns = B.rref()
    basis_columns = list(basis_columns)
    C = B[:, basis_columns]
    if C.det() == 0:
        raise AssertionError("pivot-column basis unexpectedly singular")
    Cinv = C.inv()

    extra = None
    coeff = None
    full_circuit_count = 0
    best_extra = None
    best_extra_corr = Rational(-1)
    best_extra_tail = None
    basis_set = set(basis_columns)
    for j in range(B.cols):
        if j in basis_set:
            continue
        trial = Cinv * B[:, j]
        if all(x != 0 for x in trial):
            full_circuit_count += 1
            trial_raw = [-x for x in trial] + [Rational(1)]
            trial_support = basis_columns + [j]
            trial_l1 = sum(abs(x) for x in trial_raw)
            trial_corr = abs(sum(
                (1 if sum(r * u for r, u in hs[k]) > 0 else -1) * x
                for k, x in zip(trial_support, trial_raw)
            )) / trial_l1
            threshold = math.ceil(D * D / 4)
            trial_tail = sum(
                abs(x) for k, x in zip(trial_support, trial_raw)
                if sum(r * u for r, u in hs[k]) >= threshold
            ) / trial_l1
            if extra is None:
                extra = j
                coeff = trial
            if trial_corr > best_extra_corr:
                best_extra = j
                best_extra_corr = trial_corr
                best_extra_tail = trial_tail
    if extra is None:
        raise RuntimeError("no full-support fundamental circuit exists after pivot basis")

    support = basis_columns + [extra]
    raw = [-x for x in coeff] + [Rational(1)]
    raw_corr = sum(labels * weight for labels, weight in zip(
        [1 if sum(r * u for r, u in hs[j]) > 0 else -1 for j in support], raw
    ))
    if raw_corr < 0:
        raw = [-x for x in raw]
        raw_corr = -raw_corr
    raw_l1 = sum(abs(x) for x in raw)
    weights = [x / raw_l1 for x in raw]
    w = [Rational(0)] * B.cols
    for j, x in zip(support, weights):
        w[j] = x
    labels = [1 if sum(r * u for r, u in H) > 0 else -1 for H in hs]
    corr = sum(labels[j] * w[j] for j in range(B.cols))
    moments = [sum(B[i, j] * w[j] for j in support) for i in range(rank)]
    if any(moments) or sum(abs(x) for x in w) != 1:
        raise AssertionError("circuit witness check failed")

    threshold = math.ceil(D * D / 4)
    tail_mass = sum(abs(w[j]) for j in support
                    if sum(r * u for r, u in hs[j]) >= threshold)

    dual = None
    if corr > 0:
        y, residuals, maxabs, argmax, support_ok = solve_candidate_dual(
            B, labels, support, w, corr
        )
        dual = {
            "support_equioscillation_exact": support_ok,
            "global_max_abs_residual": qstr(maxabs),
            "candidate_epsilon": qstr(corr),
            "global_bound_passes": bool(maxabs <= corr),
            "violation_ratio_decimal": float(maxabs / corr),
            "first_maximizing_orbit_index": argmax,
            "first_maximizing_orbit": orbit_record(hs[argmax]),
            "dual_coefficients": [qstr(x) for x in y],
        }

    return {
        "N": N,
        "D_polynomial_cutoff": D,
        "orbit_count": len(hs),
        "feature_rank": rank,
        "support_size": len(support),
        "support_is_rank_plus_one": len(support) == rank + 1,
        "support_feature_rank": B[:, support].rank(),
        "exact_correlation": qstr(corr),
        "above_two_thirds": bool(corr > Rational(2, 3)),
        "tail_threshold_Ct": threshold,
        "exact_tail_mass": qstr(tail_mass),
        "tail_mass_at_least_quarter": bool(tail_mass >= Rational(1, 4)),
        "basis_column_indices": basis_columns,
        "extra_column_index": extra,
        "fixed_basis_all_extra_diagnostic": {
            "full_fundamental_circuit_count": full_circuit_count,
            "best_extra_orbit_index": best_extra,
            "best_extra_orbit": orbit_record(hs[best_extra]),
            "best_exact_correlation": qstr(best_extra_corr),
            "best_above_two_thirds": bool(best_extra_corr > Rational(2, 3)),
            "best_tail_mass": qstr(best_extra_tail),
        },
        "support": [orbit_record(hs[j], w[j]) for j in support],
        "candidate_dual": dual,
        "basis_row_indices": basis_row_indices,
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
    args = ap.parse_args()
    cases = args.case or (
        [(N, 5) for N in range(11, 17)]
        + [(N, 6) for N in range(17, 24)]
        + [(N, 7) for N in range(24, 32)]
    )
    results = []
    started = time.perf_counter()
    for N, D in cases:
        print(f"starting N={N},D={D}", flush=True)
        result = run_case(N, D)
        results.append(result)
        dual = result["candidate_dual"]
        print(
            f"completed corr={result['exact_correlation']}, "
            f"tail={result['exact_tail_mass']}, "
            f"dual_pass={None if dual is None else dual['global_bound_passes']}",
            flush=True,
        )
    out = {
        "scope": "formula-defined canonical moving circuit at q=5,K=2",
        "tier": "exact finite proposer test; no asymptotic inference",
        "support_formula": "lexicographic pivot-column basis plus first later full fundamental circuit",
        "results": results,
        "total_elapsed_seconds": round(time.perf_counter() - started, 6),
    }
    path = Path(args.output)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"cases": len(results), "seconds": out["total_elapsed_seconds"]}, indent=2))


if __name__ == "__main__":
    main()
