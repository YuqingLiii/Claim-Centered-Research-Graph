#!/usr/bin/env python3
"""Finite full-orbit projection gates for the Phase-21 critical mixture."""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from collections import defaultdict
from itertools import product
from pathlib import Path

import numpy as np


def count_vectors(values, slots, total):
    out = []

    def rec(i, left_slots, left_total, acc):
        if i == len(values) - 1:
            v = values[i]
            if left_slots >= 0 and left_slots * v == left_total:
                out.append(tuple(acc + [left_slots]))
            return
        v = values[i]
        for n in range(left_slots + 1):
            rem = left_total - n * v
            if rem < 0:
                break
            rec(i + 1, left_slots - n, rem, acc + [n])

    rec(0, slots, total, [])
    return out


def weak_compositions(n, k):
    if k == 1:
        yield (n,)
        return
    for first in range(n + 1):
        for rest in weak_compositions(n - first, k - 1):
            yield (first,) + rest


def mult_coeff(n, counts):
    z = math.factorial(n)
    for c in counts:
        z //= math.factorial(c)
    return z


def add_hist(dst, hist, weight):
    key = tuple(sorted((tau, c) for tau, c in hist.items() if c))
    dst[key] += weight


def dense_component(N, L):
    totals = list(range(2, L + 2))
    total_counts = count_vectors(totals, L, N)
    c_size = sum(mult_coeff(L, ns) for ns in total_counts)
    out = defaultdict(float)
    for ns in total_counts:
        ranges = [range(n + 1) for n in ns]
        for active_counts in product(*ranges):
            hist = defaultdict(int)
            state_counts = []
            for s, n, j in zip(totals, ns, active_counts):
                if n - j:
                    hist[(0, s)] += n - j
                    state_counts.append(n - j)
                if j:
                    hist[(1, s - 1)] += j
                    state_counts.append(j)
            weight = mult_coeff(L, state_counts) / (c_size * (2.0**L))
            add_hist(out, hist, weight)
    return out, c_size


def balanced_component(N, L):
    U = math.ceil(2 * (N ** (1 / 3)))
    M = L - U
    nbulk = N - 2 * U
    a, h = divmod(nbulk, M)
    totals = list(range(a - 2, a + 3))
    total_counts = count_vectors(totals, M, nbulk)
    c_size = sum(mult_coeff(M, ns) for ns in total_counts)
    out = defaultdict(float)
    for unit_active in range(U + 1):
        unit_prob = math.comb(U, unit_active) / (2.0**U)
        for ns in total_counts:
            split_comps = [list(weak_compositions(n, s // 2 + 1)) for s, n in zip(totals, ns)]
            for choices in product(*split_comps):
                hist = defaultdict(int)
                if U - unit_active:
                    hist[(0, 2)] += U - unit_active
                if unit_active:
                    hist[(1, 1)] += unit_active
                state_counts = []
                split_weight = 1.0
                for s, counts in zip(totals, choices):
                    for r, cnt in enumerate(counts):
                        if not cnt:
                            continue
                        hist[(r, s - r)] += cnt
                        state_counts.append(cnt)
                        w = 0.5 if r == 0 else 1.0 / (2 * (s // 2))
                        split_weight *= w**cnt
                bulk_orderings = mult_coeff(M, state_counts)
                weight = unit_prob * bulk_orderings * split_weight / c_size
                add_hist(out, hist, weight)
    tmax = 0
    for ns in total_counts:
        tmax = max(tmax, U + sum(n * ((s // 2) * (s - s // 2)) for s, n in zip(totals, ns)))
    return out, c_size, U, M, a, tmax


def falling(x, k):
    z = 1
    for j in range(k):
        z *= x - j
    return z


def feature_dict(hist_key, D):
    patterns = [(a, b) for w in range(1, D) for a in range(w + 1) for b in [w - a] if a <= b]
    weights = [a + b for a, b in patterns]
    dp = {(): 1.0}
    slots = []
    for tau, cnt in hist_key:
        slots.extend([tau] * cnt)
    for r, u in slots:
        vals = [0.5 * (falling(r, a) * falling(u, b) + falling(r, b) * falling(u, a)) for a, b in patterns]
        nxt = dict(dp)
        for key, val in dp.items():
            degree = sum(weights[j] for j in key)
            for j, av in enumerate(vals):
                if av and degree + weights[j] < D:
                    nk = tuple(sorted(key + (j,)))
                    nxt[nk] = nxt.get(nk, 0.0) + val * av
        dp = nxt
    return dp, patterns


def analyze(N):
    L = int(N ** (2 / 3))
    while (L + 1) ** 3 <= N * N:
        L += 1
    while L**3 > N * N:
        L -= 1
    D = L // 2
    dense, dense_c = dense_component(N, L)
    bal, bal_c, U, M, a, tmax = balanced_component(N, L)
    dense_mass = sum(dense.values())
    balanced_mass = sum(bal.values())
    support = sorted(set(dense) | set(bal))
    overlap = set(dense) & set(bal)
    pi = np.array([0.5 * dense.get(h, 0.0) + 0.5 * bal.get(h, 0.0) for h in support])
    pi /= pi.sum()
    feats = []
    all_keys = set()
    patterns = None
    for h in support:
        fd, patterns = feature_dict(h, D)
        feats.append(fd)
        all_keys.update(fd)
    keys = sorted(all_keys, key=lambda z: (sum(patterns[j][0] + patterns[j][1] for j in z), z))
    X = np.array([[fd.get(k, 0.0) for k in keys] for fd in feats], dtype=float)
    scales = np.max(np.abs(X), axis=0)
    scales[scales == 0] = 1.0
    X /= scales
    labels_no = np.array([1.0 if all(r == 0 for (r, u), cnt in h) else 0.0 for h in support])
    sw = np.sqrt(pi)
    Xw = X * sw[:, None]
    bw = labels_no * sw
    coef, _, rank, sing = np.linalg.lstsq(Xw, bw, rcond=1e-11)
    g = labels_no - X @ coef
    l2sq = float(np.sum(pi * g * g))
    l1 = float(np.sum(pi * np.abs(g)))
    corr = 0.0 if l1 == 0 else 2 * l2sq / l1
    cts = np.array([sum(cnt * r * u for (r, u), cnt in h) for h in support], dtype=float)
    tail = 0.0 if l1 == 0 else float(np.sum(pi[cts >= tmax / 2] * np.abs(g[cts >= tmax / 2])) / l1)
    scalar_degree = (D - 1) // 2
    XS = np.column_stack([cts**j for j in range(scalar_degree + 1)])
    scalar_scales = np.max(np.abs(XS), axis=0)
    scalar_scales[scalar_scales == 0] = 1.0
    XS /= scalar_scales
    coefs, _, scalar_rank, _ = np.linalg.lstsq(XS * sw[:, None], bw, rcond=1e-11)
    gs = labels_no - XS @ coefs
    scalar_l2sq = float(np.sum(pi * gs * gs))
    scalar_l1 = float(np.sum(pi * np.abs(gs)))
    scalar_corr = 0.0 if scalar_l1 == 0 else 2 * scalar_l2sq / scalar_l1
    overlap_dense_mass = sum(dense[h] for h in overlap)
    overlap_bal_mass = sum(bal[h] for h in overlap)
    return {
        "N": N,
        "L": L,
        "D": D,
        "U": U,
        "M": M,
        "a": a,
        "dense_ordered_total_count": dense_c,
        "balanced_ordered_total_count": bal_c,
        "dense_component_mass": dense_mass,
        "balanced_component_mass": balanced_mass,
        "dense_support": len(dense),
        "balanced_support": len(bal),
        "union_support": len(support),
        "overlap_support": len(overlap),
        "dense_component_mass_on_overlap": overlap_dense_mass,
        "balanced_component_mass_on_overlap": overlap_bal_mass,
        "raw_feature_columns": len(keys),
        "weighted_rank": int(rank),
        "nullity": len(support) - int(rank),
        "smallest_retained_singular": float(sing[rank - 1]) if rank else None,
        "projection_l2sq": l2sq,
        "projection_l1": l1,
        "normalized_correlation": corr,
        "scalar_ct_max_power": scalar_degree,
        "scalar_ct_rank": int(scalar_rank),
        "scalar_ct_normalized_correlation": scalar_corr,
        "balanced_tmax": tmax,
        "residual_abs_mass_ct_ge_tmax_over_2": tail,
        "pi_mass": float(pi.sum()),
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--Ns", nargs="+", type=int, default=[15, 21, 27])
    args = parser.parse_args()
    results = [analyze(N) for N in args.Ns]
    script_sha = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    payload = {"script_sha256": script_sha, "results": results}
    print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
