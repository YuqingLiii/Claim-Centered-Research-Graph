"""Independent exact verifier for the phase-2 pair-kernel output."""
from __future__ import annotations

import argparse
import itertools
import json
import math
from fractions import Fraction
from pathlib import Path


def weak_compositions(total, parts):
    if parts == 1:
        yield (total,)
    else:
        for first in range(total + 1):
            for tail in weak_compositions(total - first, parts - 1):
                yield (first,) + tail


def ff(value, order):
    answer = 1
    for offset in range(order):
        answer *= value - offset
    return answer


def label(counts, q, target):
    for a, amount in enumerate(counts):
        b = (target - a) % q
        if (a == b and amount >= 2) or (a != b and amount > 0 and counts[b] > 0):
            return 1
    return -1


def parse_weights(record):
    weights = {}
    for entry in record["nonzero_weights"]:
        key = tuple(entry["counts"])
        assert key not in weights
        weights[key] = Fraction(entry["weight"])
    return weights


def centralizer_maps(q, target):
    sigma = [(target - a) % q for a in range(q)]
    return [
        perm
        for perm in itertools.permutations(range(q))
        if all(perm[sigma[a]] == sigma[perm[a]] for a in range(q))
    ]


def moved(counts, perm):
    result = [0] * len(counts)
    for old, new in enumerate(perm):
        result[new] = counts[old]
    return tuple(result)


def verify(record):
    n, q, target = record["case"]
    degree = record["pure_high_degree_at_least"]
    weights = parse_weights(record)
    assert all(sum(counts) == n for counts in weights)
    assert sum(weights.values()) == 0
    l1 = sum(abs(weight) for weight in weights.values())
    correlation = sum(weight * label(counts, q, target) for counts, weight in weights.items())
    assert l1 == Fraction(record["l1_exact"]) == 1
    assert correlation == Fraction(record["correlation_exact"])
    assert record["strictly_above_two_thirds"] == (correlation > Fraction(2, 3))

    rows = 0
    for total in range(degree):
        for alpha in weak_compositions(total, q):
            rows += 1
            residual = sum(
                weight * math.prod(ff(counts[a], alpha[a]) for a in range(q))
                for counts, weight in weights.items()
            )
            assert residual == 0
    assert rows == record["raw_moment_rows_checked"]

    group = centralizer_maps(q, target)
    for counts, weight in weights.items():
        for perm in group:
            assert weights.get(moved(counts, perm), Fraction(0)) == weight
    return {
        "case": [n, q, target],
        "implementation": "independent JSON reconstruction and full centralizer-invariance check",
        "support_size": len(weights),
        "centralizer_order": len(group),
        "moment_rows_rechecked": rows,
        "max_exact_moment_residual": "0",
        "l1_exact": str(l1),
        "correlation_exact": str(correlation),
        "strictly_above_two_thirds": correlation > Fraction(2, 3),
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, required=True)
    args = parser.parse_args()
    payload = json.loads(args.input.read_text())
    checks = [verify(record) for record in payload["results"]]
    print(json.dumps({"checks": checks, "verification": "PASS"}, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
