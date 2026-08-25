"""Independent exact verifier for the phase-4 block-composition JSON."""
from __future__ import annotations

import argparse
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


def function_label(counts, q, target):
    for a in range(q):
        b = (target - a) % q
        if (a == b and counts[a] >= 2) or (a != b and counts[a] and counts[b]):
            return 1
    return -1


def parse_weights(record):
    answer = {}
    for item in record["weights"]:
        key = tuple(item["counts"])
        assert key not in answer
        answer[key] = Fraction(item["weight"])
    return answer


def verify(payload, record):
    n, q, target = payload["case"]
    weights = parse_weights(record)
    assert all(sum(counts) == n for counts in weights)
    assert all(counts[0] == 0 for counts in weights)

    # Recheck cross-block soundness from the declared sigma-pair allocation.
    pairs = [tuple(item[0]) for item in payload["pair_blocks"]]
    assert sorted(a for pair in pairs for a in pair) == list(range(1, q))
    assert all((target - a) % q == b for a, b in pairs)
    for counts in weights:
        hit_pairs = [pair for pair in pairs if counts[pair[0]] and counts[pair[1]]]
        assert function_label(counts, q, target) == (1 if hit_pairs else -1)

    assert sum(weights.values()) == 0
    norm = sum(abs(weight) for weight in weights.values())
    correlation = sum(
        weight * function_label(counts, q, target)
        for counts, weight in weights.items()
    )
    assert norm == Fraction(record["l1_exact"]) == 1
    assert correlation == Fraction(record["correlation_exact"])
    assert record["strictly_above_two_thirds"] == (correlation > Fraction(2, 3))

    band = record["composed_pure_high_degree"]
    rows = 0
    for total in range(band):
        for alpha in weak_compositions(total, q):
            rows += 1
            residual = sum(
                weight * math.prod(ff(counts[a], alpha[a]) for a in range(q))
                for counts, weight in weights.items()
            )
            assert residual == 0
    assert rows == record["factorial_rows_checked"]

    layers = sorted({
        sum(1 for a, b in pairs if counts[a] and counts[b])
        for counts in weights
    })
    assert layers == record["global_K_layers"]
    return {
        "name": record["name"],
        "support_size": len(weights),
        "moment_rows_rechecked": rows,
        "max_exact_moment_residual": "0",
        "l1_exact": str(norm),
        "correlation_exact": str(correlation),
        "strictly_above_two_thirds": correlation > Fraction(2, 3),
        "cross_block_soundness": "PASS",
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, required=True)
    args = parser.parse_args()
    payload = json.loads(args.input.read_text(encoding="utf-8"))
    checks = [verify(payload, record) for record in payload["records"]]
    print(json.dumps({"checks": checks, "verification": "PASS"}, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
