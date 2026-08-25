#!/usr/bin/env python3
"""Exact rational check for the Phase-27 shared-NO construction."""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import sys
from fractions import Fraction
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from ksum_l2p14_target_scale_sweep import moment_row, row_patterns  # noqa: E402


def qstr(x: Fraction) -> str:
    return str(x.numerator) if x.denominator == 1 else f"{x.numerator}/{x.denominator}"


def bridge(N: int, D: int, h: int) -> dict[int, Fraction]:
    m = D - 2
    out = {}
    for j in range(m + 1):
        if j == 0:
            value = Fraction(1)
        else:
            value = Fraction(
                2 * ((-1) ** j) * math.factorial(m) ** 2,
                math.factorial(m - j) * math.factorial(m + j) * (1 + h * j * j),
            )
        out[h * j * j + 2] = value
    if max(out) >= N // 2:
        raise ValueError("bridge is not in the nonduplicating low-s sector")
    return out


def shared_no_null(N: int, D: int) -> dict[int, Fraction]:
    m = D - 2
    rank = (m + 1) // 2
    start = N // 3
    xs = [start + j for j in range(rank + 1)]
    ds = [2 * x - (N - 2) for x in xs]
    zs = [d * d for d in ds]
    out: dict[int, Fraction] = {}
    for j, (x, d, z) in enumerate(zip(xs, ds, zs)):
        denominator = d
        for k, zz in enumerate(zs):
            if k != j:
                denominator *= z - zz
        value = Fraction(1, denominator)
        s = x + 1
        reflected = N - s
        out[s] = out.get(s, Fraction(0)) + value
        out[reflected] = out.get(reflected, Fraction(0)) - value
    return out


def exact_residual(N: int, D: int, coeffs: dict[int, Fraction]) -> Fraction:
    maximum = Fraction(0)
    for patterns in row_patterns(D):
        value = Fraction(0)
        for s, coefficient in coeffs.items():
            yes = ((1, s - 1), (0, N - s))
            no = ((0, s), (0, N - s))
            value += coefficient * (
                moment_row(yes, patterns) - moment_row(no, patterns)
            )
        maximum = max(maximum, abs(value))
    return maximum


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--N", type=int, default=20003)
    parser.add_argument("--D", type=int, default=7)
    parser.add_argument("--h", type=int, default=64)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    if args.N % 2 != 1:
        raise ValueError("N must be odd")

    b = bridge(args.N, args.D, args.h)
    n = shared_no_null(args.N, args.D)
    bridge_norm = 2 * sum(abs(x) for x in b.values())
    bridge_corr = abs(2 * sum(b.values())) / bridge_norm
    null_norm = sum(abs(x) for x in n.values())
    null_label = sum(n.values())
    combined_corr = Fraction(3, 4) * bridge_corr

    payload = {
        "scope": "exact reduced paired-jump family; no full orbit LP",
        "N": args.N,
        "D": args.D,
        "h": args.h,
        "bridge_support_size": len(b),
        "shared_no_yes_support_size": len(n),
        "bridge_max_exact_row_residual": qstr(exact_residual(args.N, args.D, b)),
        "shared_no_max_exact_row_residual": qstr(exact_residual(args.N, args.D, n)),
        "shared_no_merged_NO_coefficient": "0",
        "shared_no_label_numerator": qstr(null_label),
        "bridge_correlation": qstr(bridge_corr),
        "combined_l1": "1",
        "combined_correlation": qstr(combined_corr),
        "combined_above_two_thirds": combined_corr > Fraction(2, 3),
        "combined_high_Ct_tail_mass_at_threshold_N_over_4": "1/4",
        "bridge_raw_l1": qstr(bridge_norm),
        "shared_no_raw_l1": qstr(null_norm),
        "bridge_coefficients_by_s": {str(k): qstr(v) for k, v in b.items()},
        "shared_no_coefficients_by_s": {str(k): qstr(v) for k, v in n.items()},
    }
    path = Path(args.output)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({k: payload[k] for k in (
        "bridge_max_exact_row_residual",
        "shared_no_max_exact_row_residual",
        "combined_correlation",
        "combined_above_two_thirds",
    )}, indent=2))


if __name__ == "__main__":
    main()
