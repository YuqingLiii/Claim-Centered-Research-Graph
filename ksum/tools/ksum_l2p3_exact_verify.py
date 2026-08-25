"""Independent exact verifier for the phase-3 correlated outer-kernel output."""
from __future__ import annotations

import argparse
import itertools
import json
import math
from fractions import Fraction
from pathlib import Path


def compositions(total: int, parts: int):
    if parts == 1:
        yield (total,)
    else:
        for first in range(total + 1):
            for tail in compositions(total - first, parts - 1):
                yield (first,) + tail


def ff(value: int, order: int):
    answer = 1
    for offset in range(order):
        answer *= value - offset
    return answer


def label(counts, q: int, target: int):
    for a, amount in enumerate(counts):
        b = (target - a) % q
        if (a == b and amount >= 2) or (a != b and amount and counts[b]):
            return 1
    return -1


def parse_weights(record):
    answer = {}
    for entry in record["nonzero_weights"]:
        counts = tuple(entry["counts"])
        assert counts not in answer
        answer[counts] = Fraction(entry["weight"])
    return answer


def centralizer(q: int, target: int):
    sigma = tuple((target - a) % q for a in range(q))
    return tuple(
        perm for perm in itertools.permutations(range(q))
        if all(perm[sigma[a]] == sigma[perm[a]] for a in range(q))
    )


def move(counts, perm):
    result = [0] * len(counts)
    for old, new in enumerate(perm):
        result[new] = counts[old]
    return tuple(result)


def verify_record(record):
    n, q, target = record["case"]
    weights = parse_weights(record)
    band = record["pure_high_degree_at_least"]
    assert all(sum(counts) == n for counts in weights)
    assert sum(weights.values()) == 0
    l1 = sum(abs(weight) for weight in weights.values())
    correlation = sum(weight * label(counts, q, target) for counts, weight in weights.items())
    assert l1 == Fraction(record["l1_exact"]) == 1
    assert correlation == Fraction(record["correlation_exact"])
    assert correlation > Fraction(2, 3)

    rows = 0
    for total in range(band):
        for alpha in compositions(total, q):
            rows += 1
            residual = sum(
                weight * math.prod(ff(counts[a], alpha[a]) for a in range(q))
                for counts, weight in weights.items()
            )
            assert residual == 0
    assert rows == record["factorial_rows_checked"]

    group = centralizer(q, target)
    for counts, weight in weights.items():
        for perm in group:
            assert weights.get(move(counts, perm), Fraction(0)) == weight
    return {
        "case": [n, q, target],
        "support_size": len(weights),
        "moment_rows_rechecked": rows,
        "centralizer_order": len(group),
        "max_exact_moment_residual": "0",
        "l1_exact": str(l1),
        "correlation_exact": str(correlation),
        "strictly_above_two_thirds": True,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, required=True)
    args = parser.parse_args()
    payload = json.loads(args.input.read_text(encoding="utf-8"))
    assert payload["m2_condition_violated"] == 5
    checks = [verify_record(record) for record in payload["results"]]
    print(json.dumps({"checks": checks, "verification": "PASS"}, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
