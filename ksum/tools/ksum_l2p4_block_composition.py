"""Exact phase-4 two-block composition at (N,q,t,m)=(10,5,0,2).

The two complementary sigma-pairs are assigned to two value-disjoint blocks.
Each block has total occupancy five and uses the r0=1 endpoint of the reviewed
phase-3 kernel, namely (I_5-A_5)/2.  We compare two symmetric OR_2 outers:

* order 1: mass -1/2 at 00 and +1/4 at each weight-one point;
* order 2: the normalized parity functional.

All calculations are on occupancy patterns.  The reviewed falling-factorial
map makes these exact query-degree checks; enumerating all 5^10 strings is not
needed for this finite gate.
"""
from __future__ import annotations

import argparse
import itertools
import json
import math
from fractions import Fraction
from pathlib import Path


N = 10
Q = 5
TARGET = 0
BLOCKS = (((1, 4), 5), ((2, 3), 5))


def falling(value: int, order: int) -> int:
    return math.prod(value - offset for offset in range(order))


def weak_compositions(total: int, parts: int):
    if parts == 1:
        yield (total,)
        return
    for first in range(total + 1):
        for tail in weak_compositions(total - first, parts - 1):
            yield (first,) + tail


def inner_kernel(size: int):
    """The r0=1 phase-3 signed kernel, keyed by sign bit -1/+1."""
    left = size // 2
    right = size - left
    table = {
        (size, 0): Fraction(-1, 4),
        (0, size): Fraction(-1, 4),
        (left, right): Fraction(1, 4),
        (right, left): Fraction(1, 4),
    }
    assert sum(table.values()) == 0
    assert sum(abs(weight) for weight in table.values()) == 1
    return table


def outer_kernels():
    signs = tuple(itertools.product((-1, 1), repeat=2))
    order_one = {sign: Fraction(0) for sign in signs}
    order_one[(-1, -1)] = Fraction(-1, 2)
    order_one[(-1, 1)] = Fraction(1, 4)
    order_one[(1, -1)] = Fraction(1, 4)

    order_two = {
        sign: Fraction(-sign[0] * sign[1], 4)
        for sign in signs
    }
    return {
        "correlated_order_1": (1, order_one),
        "parity_order_2": (2, order_two),
    }


def label(counts):
    for a in range(Q):
        b = (TARGET - a) % Q
        if (a == b and counts[a] >= 2) or (a != b and counts[a] and counts[b]):
            return 1
    return -1


def compose(outer):
    answer = {}
    local = [inner_kernel(size) for _, size in BLOCKS]
    for choices in itertools.product(*(tuple(table.items()) for table in local)):
        counts = [0] * Q
        sign_bits = []
        abs_product = Fraction(1)
        for ((a, b), _), ((i, j), weight) in zip(BLOCKS, choices):
            counts[a], counts[b] = i, j
            sign_bits.append(1 if weight > 0 else -1)
            abs_product *= abs(weight)
        weight = (2 ** len(BLOCKS)) * outer[tuple(sign_bits)] * abs_product
        if weight:
            key = tuple(counts)
            answer[key] = answer.get(key, Fraction(0)) + weight
    return answer


def outer_checks(order, outer):
    assert sum(outer.values()) == 0
    assert sum(abs(weight) for weight in outer.values()) == 1
    for degree in range(order):
        for subset in itertools.combinations(range(2), degree):
            residual = sum(
                weight * math.prod(sign[index] for index in subset)
                for sign, weight in outer.items()
            )
            assert residual == 0


def record(name, order, outer):
    outer_checks(order, outer)
    weights = compose(outer)
    band = 2 * order
    rows = 0
    for total in range(band):
        for alpha in weak_compositions(total, Q):
            rows += 1
            residual = sum(
                weight
                * math.prod(falling(counts[a], alpha[a]) for a in range(Q))
                for counts, weight in weights.items()
            )
            assert residual == 0
    norm = sum(abs(weight) for weight in weights.values())
    correlation = sum(weight * label(counts) for counts, weight in weights.items())
    assert sum(weights.values()) == 0
    assert norm == 1
    return {
        "name": name,
        "outer_pure_high_degree": order,
        "inner_pure_high_degree": 2,
        "composed_pure_high_degree": band,
        "factorial_rows_checked": rows,
        "support_size": len(weights),
        "l1_exact": str(norm),
        "correlation_exact": str(correlation),
        "strictly_above_two_thirds": correlation > Fraction(2, 3),
        "global_K_layers": sorted({
            sum(1 for a, b in (pair for pair, _ in BLOCKS) if counts[a] and counts[b])
            for counts in weights
        }),
        "weights": [
            {"counts": list(counts), "weight": str(weight)}
            for counts, weight in sorted(weights.items())
        ],
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    records = [record(name, order, outer) for name, (order, outer) in outer_kernels().items()]
    payload = {
        "arithmetic": "exact rational (fractions.Fraction)",
        "level": "occupancy-pattern / complete falling-factorial filtration",
        "case": [N, Q, TARGET],
        "blocks": len(BLOCKS),
        "fixed_point_occupancy": 0,
        "pair_blocks": [[list(pair), size] for pair, size in BLOCKS],
        "cross_block_hits": "impossible: each sigma-pair is wholly assigned to one block",
        "records": records,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({
        "case": payload["case"],
        "level": payload["level"],
        "checks": [{key: item[key] for key in (
            "name", "outer_pure_high_degree", "inner_pure_high_degree",
            "composed_pure_high_degree", "factorial_rows_checked", "support_size",
            "l1_exact", "correlation_exact", "strictly_above_two_thirds",
            "global_K_layers",
        )} for item in records],
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()

