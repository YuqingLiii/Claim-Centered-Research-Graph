#!/usr/bin/env python3
"""Phase-17 q=5 explicit-base-law diagnostic.

The base law is the orbit pushforward of the symmetric Dirichlet--multinomial
law on the four nonzero symbols.  Alpha=1 is the uniform-composition law, so
its unnormalised orbit weight is just the size of the wreath-product orbit.

This script evaluates the exact phase-16 weighted projection numerically.  It
uses the actual q=5 orbit-feature rows of weighted degree <D, removes numerical
row dependencies by an SVD, and reports the residual correlation and tail.
It is diagnostic evidence only, not a proof certificate.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path

import numpy as np


def fall(x: int, a: int) -> int:
    out = 1
    for j in range(a):
        out *= x - j
    return out


def pair_kernel(slot: tuple[int, int], pattern: tuple[int, int]) -> int:
    r, u = slot
    a, b = pattern
    return fall(r, a) * fall(u, b) + fall(r, b) * fall(u, a)


def orbits(N: int) -> list[tuple[tuple[int, int], tuple[int, int]]]:
    types = [(r, u) for r in range(N + 1) for u in range(r, N + 1)
             if r + u >= 1]
    return [(x, y) for i, x in enumerate(types) for y in types[i:]
            if sum(x) + sum(y) == N]


def ordered_images(H):
    (a, b), (c, d) = H
    out = set()
    for x in ((a, b), (b, a)):
        for y in ((c, d), (d, c)):
            out.add(x + y)
            out.add(y + x)
    return sorted(out)


def log_dm_mass(counts, alpha: float) -> float:
    # Terms independent of counts are intentionally omitted.
    return float(sum(math.lgamma(x + alpha) - math.lgamma(x + 1)
                     for x in counts))


def orbit_log_weight(H, alpha: float) -> float:
    vals = [log_dm_mass(x, alpha) for x in ordered_images(H)]
    top = max(vals)
    return top + math.log(sum(math.exp(x - top) for x in vals))


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


def digest(obj) -> str:
    return hashlib.sha256(json.dumps(obj, sort_keys=True,
                                     separators=(",", ":")).encode()).hexdigest()


def run_case(N: int, D: int, alpha: float):
    hs = orbits(N)
    rp = row_patterns(D)
    logw = np.array([orbit_log_weight(H, alpha) for H in hs])
    logw -= np.max(logw)
    w = np.exp(logw)
    w /= np.sum(w)
    b = np.array([float(sum(r * u for r, u in H) == 0) for H in hs])
    A = np.array([[float(moment_row(H, p)) for H in hs] for p in rp])

    # Weighted row normalisation prevents falling-factorial magnitudes from
    # deciding the numerical rank.  X maps feature coefficients to L2(pi).
    norms = np.sqrt(np.sum(A * A * w[None, :], axis=1))
    keep = norms > 0
    A = A[keep] / norms[keep, None]
    X = A.T * np.sqrt(w)[:, None]
    y = b * np.sqrt(w)
    U, s, _ = np.linalg.svd(X, full_matrices=False)
    tol = max(X.shape) * np.finfo(float).eps * s[0]
    rank = int(np.sum(s > tol))
    projection_weighted = U[:, :rank] @ (U[:, :rank].T @ y)
    p = projection_weighted / np.sqrt(w)
    g = b - p
    l2sq = float(np.dot(w, g * g))
    l1 = float(np.dot(w, np.abs(g)))
    corr = 2 * l2sq / l1
    ct = np.array([sum(r * u for r, u in H) for H in hs])
    thresholds = {
        "N_log_N": N * math.log(max(N, 2)),
        "N_3_over_2_quarter": (N ** 1.5) / 4,
        "N_squared_32": N * N / 32,
    }
    tails = {name: float(np.dot(w[ct >= t], np.abs(g[ct >= t])) / l1)
             for name, t in thresholds.items()}
    return {
        "N": N,
        "D": D,
        "alpha": alpha,
        "orbit_count": len(hs),
        "raw_feature_rows": len(rp),
        "numerical_rank": rank,
        "no_probability": float(np.dot(w, b)),
        "residual_l2_squared": l2sq,
        "residual_l1": l1,
        "correlation": corr,
        "passes_strict_two_thirds": bool(corr > 2 / 3 + 1e-10),
        "tail_absolute_mass_fraction": tails,
        "weighted_orthogonality_residual": float(np.max(np.abs(A @ (w * g)))),
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--output", required=True)
    ap.add_argument("--alpha", type=float, default=1.0)
    ap.add_argument("--max-n", type=int, default=80)
    args = ap.parse_args()
    ns = [n for n in (8, 12, 16, 20, 24, 32, 40, 50, 64, 80)
          if n <= args.max_n]
    cases = []
    for N in ns:
        for scale, D in (("half_sqrt", max(3, math.ceil(0.5 * math.sqrt(N)))),
                         ("sqrt", max(3, math.ceil(math.sqrt(N))))):
            rec = run_case(N, D, args.alpha)
            rec["scale"] = scale
            cases.append(rec)
    out = {
        "law": "wreath-orbit pushforward of symmetric Dirichlet-multinomial(alpha)",
        "alpha": args.alpha,
        "arithmetic": "float64 SVD diagnostic",
        "cases": cases,
        "case_input_sha256": digest([(x["N"], x["D"], x["alpha"]) for x in cases]),
    }
    path = Path(args.output)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(out, indent=2))


if __name__ == "__main__":
    main()
