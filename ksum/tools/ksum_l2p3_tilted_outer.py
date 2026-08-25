"""Construct and exactly check the L2 phase-3 correlated outer kernel.

The inner axis/interior probabilities are those underlying the reviewed M1
kernel.  The outer signed measure is an exchangeable divided-difference
functional on the number K of interior pairs, supported at
0, 1, 5, 25, ... up to the number of complementary pairs.
"""
from __future__ import annotations

import argparse
import itertools
import json
import math
from fractions import Fraction
from pathlib import Path


CASES = ((5, 5), (7, 3))
OUTER_BASE = 5


def weak_compositions(total: int, parts: int):
    if parts == 1:
        yield (total,)
        return
    for first in range(total + 1):
        for tail in weak_compositions(total - first, parts - 1):
            yield (first,) + tail


def falling(value: int, order: int) -> int:
    return math.prod(value - offset for offset in range(order))


def sigma_structure(q: int, target: int):
    if q % 2 != 1:
        raise ValueError("phase 3 uses the canonical odd-q route")
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


def balanced_size_assignments(n: int, pair_count: int):
    if n < 2 * pair_count + 1:
        raise ValueError("construction requires N >= q")
    quotient, remainder = divmod(n - 1, pair_count)
    sizes = (quotient + 1,) * remainder + (quotient,) * (pair_count - remainder)
    return tuple(sorted(set(itertools.permutations(sizes))))


def axis_probability(size: int):
    return {(size, 0): Fraction(1, 2), (0, size): Fraction(1, 2)}


def interior_probability(size: int):
    left = size // 2
    right = size - left
    if left == right:
        return {(left, right): Fraction(1)}
    return {(left, right): Fraction(1, 2), (right, left): Fraction(1, 2)}


def outer_support(pair_count: int):
    support = []
    value = 1
    while value <= pair_count:
        support.append(value)
        value *= OUTER_BASE
    return (0, *support)


def outer_layer_weights(pair_count: int):
    """Normalized divided-difference weights, oriented negative at K=0."""
    support = outer_support(pair_count)
    raw = {}
    for point in support:
        denominator = math.prod(point - other for other in support if other != point)
        raw[point] = Fraction(1, denominator)
    if raw[0] > 0:
        raw = {point: -weight for point, weight in raw.items()}
    norm = sum(abs(weight) for weight in raw.values())
    weights = {point: weight / norm for point, weight in raw.items()}
    moment_order = len(support) - 1
    assert weights[0] < 0
    assert sum(abs(weight) for weight in weights.values()) == 1
    for degree in range(moment_order):
        assert sum(weight * falling(point, degree) for point, weight in weights.items()) == 0
    return moment_order, weights


def construct(n: int, q: int, target: int):
    fixed, pairs = sigma_structure(q, target)
    moment_order, layer_weights = outer_layer_weights(len(pairs))
    size_assignments = balanced_size_assignments(n, len(pairs))
    weights: dict[tuple[int, ...], Fraction] = {}
    for sizes in size_assignments:
        assignment_weight = Fraction(1, len(size_assignments))
        for active_count, layer_weight in layer_weights.items():
            for active in itertools.combinations(range(len(pairs)), active_count):
                active_set = frozenset(active)
                pattern_weight = layer_weight / math.comb(len(pairs), active_count)
                local_tables = [
                    interior_probability(size) if index in active_set else axis_probability(size)
                    for index, size in enumerate(sizes)
                ]
                for selected in itertools.product(*(tuple(table.items()) for table in local_tables)):
                    counts = [0] * q
                    counts[fixed] = 1
                    weight = assignment_weight * pattern_weight
                    for (a, b), ((i, j), local_weight) in zip(pairs, selected):
                        counts[a], counts[b] = i, j
                        weight *= local_weight
                    key = tuple(counts)
                    weights[key] = weights.get(key, Fraction(0)) + weight
    return fixed, pairs, size_assignments, moment_order, layer_weights, {
        key: value for key, value in weights.items() if value
    }


def function_sign(counts, q: int, target: int):
    for a in range(q):
        b = (target - a) % q
        if (a == b and counts[a] >= 2) or (a != b and counts[a] and counts[b]):
            return 1
    return -1


def check_case(n: int, q: int, target: int):
    fixed, pairs, assignments, moment_order, layer_weights, weights = construct(n, q, target)
    band = 2 * moment_order
    rows = 0
    for total in range(band):
        for alpha in weak_compositions(total, q):
            rows += 1
            residual = sum(
                weight
                * math.prod(falling(counts[a], alpha[a]) for a in range(q))
                for counts, weight in weights.items()
            )
            assert residual == 0
    l1 = sum(abs(weight) for weight in weights.values())
    total_mass = sum(weights.values())
    correlation = sum(
        weight * function_sign(counts, q, target) for counts, weight in weights.items()
    )
    assert total_mass == 0
    assert l1 == 1
    assert correlation == -2 * layer_weights[0]
    assert correlation > Fraction(2, 3)
    return {
        "case": [n, q, target],
        "fixed_point": fixed,
        "sigma_pairs": [list(pair) for pair in pairs],
        "pair_total_assignments": [list(row) for row in assignments],
        "outer_support": list(layer_weights),
        "outer_layer_weights": {str(key): str(value) for key, value in layer_weights.items()},
        "outer_moment_order": moment_order,
        "pure_high_degree_at_least": band,
        "factorial_rows_checked": rows,
        "max_exact_moment_residual": "0",
        "support_size": len(weights),
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
    results = [check_case(n, q, target) for n, q in CASES for target in range(q)]
    payload = {
        "arithmetic": "exact rational (fractions.Fraction)",
        "mechanism": "M1 axis/interior product tilted by a signed exchangeable K-functional",
        "m2_condition_violated": 5,
        "outer_base": OUTER_BASE,
        "general_band": "degree < 2*(1+floor(log_5((q-1)/2)))",
        "general_correlation_claim": "> 3/4",
        "results": results,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({
        "arithmetic": payload["arithmetic"],
        "mechanism": payload["mechanism"],
        "m2_condition_violated": payload["m2_condition_violated"],
        "general_band": payload["general_band"],
        "general_correlation_claim": payload["general_correlation_claim"],
        "checks": [
            {key: record[key] for key in (
                "case", "pure_high_degree_at_least", "factorial_rows_checked",
                "support_size", "l1_exact", "correlation_exact",
                "strictly_above_two_thirds",
            )}
            for record in results
        ],
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
