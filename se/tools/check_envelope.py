#!/usr/bin/env python3
"""Finite scalar envelope check for SE.denom.assembly.envelope.

Reconstructs the scalar scan in the archived se_leakage_j_le_k_suffices.py.
Unlike that program, this checker uses an exact integer cube root and a
rational Taylor lower bound for exp. It makes no representation-theoretic
inference from the finite scan. It is not a proof for unbounded n.

Run from the repository root:
  python3 se/tools/check_envelope.py --max-n 600 --output <new-output.json>
No third-party dependencies are required.
"""

import argparse
from datetime import datetime, timezone
from fractions import Fraction
from functools import lru_cache
import hashlib
import json
import math
from pathlib import Path
import platform


def partitions(n, largest=None):
    if n == 0:
        yield ()
        return
    for first in range(min(n, n if largest is None else largest), 0, -1):
        for rest in partitions(n - first, first):
            yield (first,) + rest


def floor_cube_root(n):
    low, high = 0, n + 1
    while high - low > 1:
        mid = (low + high) // 2
        if mid ** 3 <= n:
            low = mid
        else:
            high = mid
    return low


@lru_cache(maxsize=None)
def hook_dimension(shape):
    columns = [sum(row >= j for row in shape) for j in range(1, max(shape, default=0) + 1)]
    denominator = 1
    for i, row in enumerate(shape):
        for j in range(row):
            denominator *= row - j + columns[j] - i - 1
    value, remainder = divmod(math.factorial(sum(shape)), denominator)
    if remainder:
        raise ArithmeticError("Hook dimension is not integral")
    return value


def r_top(q, j, theta):
    shape = (q - j,) + theta
    if any(a < b for a, b in zip(shape, shape[1:])):
        raise ValueError("The requested shape is not a partition")
    return Fraction(q ** j * hook_dimension(theta), math.factorial(j) * hook_dimension(shape))


def exp_lower_bound(x, degree=20):
    """For x>=0, sum(x**i/i!, i=0..degree) <= exp(x), in exact arithmetic."""
    if x < 0:
        raise ValueError("The lower bound requires a nonnegative exponent")
    total = term = Fraction(1)
    for i in range(1, degree + 1):
        term *= x / i
        total += term
    return total


def scan(max_n):
    checked, unresolved = 0, []
    maximum, witness = Fraction(0), None
    for n in range(2, max_n + 1):
        for k in range(floor_cube_root(n)):
            exponent = Fraction(k * (k - 1), 2 * (2 * n - k + 1)) + Fraction(k, 2 * n - 2 * k + 1)
            lower = exp_lower_bound(exponent)
            for j in range(k + 1):
                for theta in partitions(j):
                    value = r_top(2 * n, j, theta)
                    checked += 1
                    point = {"n": n, "k": k, "j": j, "theta": list(theta)}
                    if value > lower:
                        # This is inconclusive, not necessarily a counterexample to exp(x).
                        unresolved.append(point)
                    if value > maximum:
                        maximum, witness = value, point
    return {
        "scope": {"n_min": 2, "n_max_inclusive": max_n,
                  "q": "2*n", "k": "0 <= k < floor(cuberoot(n))",
                  "j": "0 <= j <= k", "theta": "every partition of j"},
        "comparison": "r_top(2*n,j,theta) <= R(n,k)",
        "r_top": "q^j*f(theta)/(j!*f((q-j,theta))) with hook dimensions f",
        "R": "exp(k*(k-1)/(2*(2*n-k+1)) + k/(2*n-2*k+1))",
        "method": "exact rational r_top <= degree-20 Taylor lower bound <= R",
        "checked_tuples": checked,
        "unresolved_tuples": unresolved,
        "all_finite_comparisons_verified": not unresolved,
        "max_r_top": str(maximum),
        "maximum_witness": witness,
        "boundary": "Finite scalar comparisons only; no asymptotic or legal-sector identification theorem is established.",
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--max-n", type=int, default=600)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    if args.max_n < 2:
        parser.error("--max-n must be at least 2")
    result = scan(args.max_n)
    result.update({
        "recorded_at_utc": datetime.now(timezone.utc).isoformat(),
        "python": platform.python_version(),
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "command": f"python3 se/tools/check_envelope.py --max-n {args.max_n}",
        "record_kind": "New rerun, not a recovered historical output log",
    })
    rendered = json.dumps(result, indent=2) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        # Existing evidence must not be silently overwritten by a later rerun.
        with args.output.open("x", encoding="utf-8") as output:
            output.write(rendered)
    print(rendered, end="")
    return 0 if result["all_finite_comparisons_verified"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
