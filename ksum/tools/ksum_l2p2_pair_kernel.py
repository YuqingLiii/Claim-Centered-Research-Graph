"""Construct and exactly check the phase-2 coefficientwise pair kernel.

For odd q and N >= q, put one item at the unique fixed point of
sigma(a)=t-a and distribute N-1 items among the r=(q-1)/2 two-cycles.
On a pair with total size s, the signed local kernel is half an interior
probability measure minus half the symmetric axis probability measure.
It has l1 one and annihilates constants and both first factorial moments.

The tensor product therefore annihilates every global factorial monomial of
total degree below 2r.  Conditioning is coefficientwise: the assertion holds
for every fixed vector of pair totals before those vectors are mixed.
"""
from __future__ import annotations

import argparse
import itertools
import json
import math
from fractions import Fraction
from pathlib import Path


CASES = ((5, 5, 0), (7, 3, 0))


def compositions(total: int, parts: int):
    if parts == 1:
        yield (total,)
        return
    for first in range(total + 1):
        for rest in compositions(total - first, parts - 1):
            yield (first,) + rest


def falling(value: int, order: int) -> int:
    return math.prod(value - offset for offset in range(order))


def sigma_structure(q: int, target: int):
    if q % 2 != 1:
        raise ValueError("the canonical phase-2 route is odd-q only")
    sigma = tuple((target - a) % q for a in range(q))
    fixed = next(a for a in range(q) if sigma[a] == a)
    pairs = []
    seen = {fixed}
    for a in range(q):
        if a not in seen:
            b = sigma[a]
            pairs.append((min(a, b), max(a, b)))
            seen.update((a, b))
    return fixed, tuple(sorted(pairs))


def balanced_sizes(n: int, pair_count: int):
    if n < 2 * pair_count + 1:
        raise ValueError("construction requires N >= q")
    quotient, remainder = divmod(n - 1, pair_count)
    sizes = (quotient + 1,) * remainder + (quotient,) * (pair_count - remainder)
    assert min(sizes) >= 2 and sum(sizes) == n - 1
    return tuple(sorted(sizes))


def local_kernel(size: int):
    """Return kappa_s=(interior-axis)/2 as exact pair-count weights."""
    weights = {(size, 0): Fraction(-1, 4), (0, size): Fraction(-1, 4)}
    left = size // 2
    right = size - left
    if left == right:
        weights[(left, right)] = Fraction(1, 2)
    else:
        weights[(left, right)] = Fraction(1, 4)
        weights[(right, left)] = Fraction(1, 4)
    assert sum(weights.values()) == 0
    assert sum(abs(value) for value in weights.values()) == 1
    assert sum(value * i for (i, _), value in weights.items()) == 0
    assert sum(value * j for (_, j), value in weights.items()) == 0
    return weights


def unique_permutations(values):
    return tuple(sorted(set(itertools.permutations(values))))


def construct(n: int, q: int, target: int):
    fixed, pairs = sigma_structure(q, target)
    size_assignments = unique_permutations(balanced_sizes(n, len(pairs)))
    weights: dict[tuple[int, ...], Fraction] = {}
    global_sign = -1 if len(pairs) % 2 == 0 else 1
    assignment_weight = Fraction(1, len(size_assignments))
    for sizes in size_assignments:
        choices = [tuple(local_kernel(size).items()) for size in sizes]
        for selected in itertools.product(*choices):
            counts = [0] * q
            counts[fixed] = 1
            weight = Fraction(global_sign) * assignment_weight
            for ((a, b), ((i, j), local_weight)) in zip(pairs, selected):
                counts[a], counts[b] = i, j
                weight *= local_weight
            key = tuple(counts)
            weights[key] = weights.get(key, Fraction(0)) + weight
    return fixed, pairs, size_assignments, {key: value for key, value in weights.items() if value}


def sign(counts, q: int, target: int):
    for a in range(q):
        b = (target - a) % q
        if (a == b and counts[a] >= 2) or (a != b and counts[a] and counts[b]):
            return 1
    return -1


def exact_checks(n: int, q: int, target: int):
    fixed, pairs, assignments, weights = construct(n, q, target)
    degree = 2 * len(pairs)
    residuals = []
    raw_rows = 0
    for total in range(degree):
        for alpha in compositions(total, q):
            raw_rows += 1
            residual = sum(
                weight
                * math.prod(falling(counts[a], alpha[a]) for a in range(q))
                for counts, weight in weights.items()
            )
            residuals.append(residual)
    l1 = sum(abs(weight) for weight in weights.values())
    correlation = sum(weight * sign(counts, q, target) for counts, weight in weights.items())
    total_mass = sum(weights.values())
    expected_correlation = Fraction(1, 2 ** (len(pairs) - 1))
    assert total_mass == 0
    assert l1 == 1
    assert not any(residuals)
    assert correlation == expected_correlation
    assert all(sum(counts) == n for counts in weights)
    return {
        "case": [n, q, target],
        "fixed_point": fixed,
        "sigma_pairs": [list(pair) for pair in pairs],
        "pair_total_assignments": [list(row) for row in assignments],
        "support_size": len(weights),
        "pure_high_degree_at_least": degree,
        "annihilated_factorial_degrees": f"0 through {degree - 1}",
        "raw_moment_rows_checked": raw_rows,
        "max_exact_moment_residual": "0",
        "total_mass_exact": str(total_mass),
        "l1_exact": str(l1),
        "correlation_exact": str(correlation),
        "strictly_above_two_thirds": correlation > Fraction(2, 3),
        "nonzero_weights": [
            {"counts": list(counts), "weight": str(weight)}
            for counts, weight in sorted(weights.items())
        ],
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    results = [exact_checks(*case) for case in CASES]
    payload = {
        "arithmetic": "exact rational (fractions.Fraction)",
        "scope": "odd q, N >= q, target arbitrary; finite run uses target 0",
        "family": "coefficientwise-conditioned tensor of sign-separated pair kernels",
        "general_annihilation_band": "all falling-factorial occupancy monomials of degree < q-1",
        "general_l1": "1",
        "general_correlation": "2^(1-(q-1)/2)",
        "results": results,
        "asymptotic_route_threshold_met": False,
        "reason": "correlation is at most 1/2 for every odd q >= 5",
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
