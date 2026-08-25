#!/usr/bin/env python3
"""Exact intermediate-constant sweep for the q=5, K=2 orbit family.

This imports the independently reconstructed exact rational engine from
ksum_l2p14_target_scale_sweep.py.  D is a polynomial-degree cutoff, never a
query count; the associated polynomial-method query scale is D/2.
"""

from __future__ import annotations

import argparse
import json
import math
import time
from fractions import Fraction
from pathlib import Path

from ksum_l2p14_target_scale_sweep import run_case


CONSTANTS = (Fraction(5, 4), Fraction(3, 2), Fraction(7, 4))


def ceil_c_sqrt_n(c: Fraction, N: int) -> int:
    # Exact integer comparison avoids a floating-point ceiling error.
    d = math.isqrt(N * c.numerator * c.numerator // (c.denominator * c.denominator))
    while d * d * c.denominator * c.denominator < N * c.numerator * c.numerator:
        d += 1
    while d > 0 and (d - 1) * (d - 1) * c.denominator * c.denominator >= N * c.numerator * c.numerator:
        d -= 1
    return d


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--output", required=True)
    ap.add_argument("--min-n", type=int, default=6)
    ap.add_argument("--max-n", type=int, default=16)
    args = ap.parse_args()
    if args.min_n < 2 or args.max_n < args.min_n:
        raise ValueError("require 2 <= min-n <= max-n")

    requested = []
    unique = set()
    for N in range(args.min_n, args.max_n + 1):
        for c in CONSTANTS:
            D = ceil_c_sqrt_n(c, N)
            requested.append((N, c, D))
            unique.add((N, D))

    computed = {}
    timings = {}
    started = time.perf_counter()
    for N, D in sorted(unique):
        t0 = time.perf_counter()
        computed[(N, D)] = run_case(N, D, do_tail=True)
        timings[(N, D)] = time.perf_counter() - t0

    cases = []
    for N, c, D in requested:
        cases.append({
            "constant": f"{c.numerator}/{c.denominator}",
            "constant_decimal": float(c),
            "N": N,
            "D_polynomial_cutoff": D,
            "query_lower_bound_scale_if_used": f"{D}/2",
            "shared_result_key": f"N={N},D={D}",
        })

    unique_results = []
    for key in sorted(computed):
        item = dict(computed[key])
        item["elapsed_seconds"] = round(timings[key], 6)
        unique_results.append(item)

    out = {
        "scope": "q=5, K=2 variable-pair-total orbit family",
        "tier": "NUMERICAL",
        "constants": [f"{c.numerator}/{c.denominator}" for c in CONSTANTS],
        "requested_N_range": [args.min_n, args.max_n],
        "maximum_N_completed": args.max_n,
        "degree_convention": "D=ceil(c sqrt(N)) is a polynomial cutoff; moments have degree <D; query scale is D/2",
        "tail_gate": "absolute mass >=1/4 on C_t>=ceil(D^2/4)",
        "requested_cases": cases,
        "unique_results": unique_results,
        "total_elapsed_seconds": round(time.perf_counter() - started, 6),
    }
    path = Path(args.output)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({
        "maximum_N_completed": args.max_n,
        "requested_case_count": len(cases),
        "unique_case_count": len(unique_results),
        "total_elapsed_seconds": out["total_elapsed_seconds"],
    }, indent=2))


if __name__ == "__main__":
    main()
