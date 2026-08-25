"""Fresh exact-rational review of the KSUM L2 phase-2 finite kernels.

This driver deliberately does not import or read either proposer script or its JSON
output.  It reconstructs the measure from the mathematical definition, checks all
falling-factorial occupancy rows in the claimed band, checks every compatible raw
one-hot monomial on the lifted string measure, and checks the full alphabet
centralizer action.
"""
from __future__ import annotations

import argparse
import itertools
import json
import math
from fractions import Fraction
from pathlib import Path


CASES = ((5, 5), (7, 3))


def falling(value: int, order: int) -> int:
    result = 1
    for offset in range(order):
        result *= value - offset
    return result


def weak_compositions(total: int, parts: int):
    if parts == 1:
        yield (total,)
        return
    for first in range(total + 1):
        for tail in weak_compositions(total - first, parts - 1):
            yield (first,) + tail


def involution_data(q: int, target: int):
    assert q % 2 == 1
    sigma = tuple((target - a) % q for a in range(q))
    fixed = [a for a in range(q) if sigma[a] == a]
    assert len(fixed) == 1
    seen = set(fixed)
    pairs = []
    for a in range(q):
        if a not in seen:
            b = sigma[a]
            pairs.append((a, b))
            seen.update((a, b))
    assert len(pairs) == (q - 1) // 2
    return sigma, fixed[0], tuple(pairs)


def balanced_assignments(n: int, pair_count: int):
    base, extra = divmod(n - 1, pair_count)
    sizes = (base + 1,) * extra + (base,) * (pair_count - extra)
    assert min(sizes) >= 2 and sum(sizes) == n - 1
    return tuple(sorted(set(itertools.permutations(sizes))))


def local_measure(size: int):
    result = {
        (size, 0): Fraction(-1, 4),
        (0, size): Fraction(-1, 4),
    }
    lo, hi = size // 2, size - size // 2
    if lo == hi:
        result[(lo, hi)] = Fraction(1, 2)
    else:
        result[(lo, hi)] = Fraction(1, 4)
        result[(hi, lo)] = Fraction(1, 4)
    assert sum(result.values()) == 0
    assert sum(weight * i for (i, _), weight in result.items()) == 0
    assert sum(weight * j for (_, j), weight in result.items()) == 0
    assert sum(abs(weight) for weight in result.values()) == 1
    return result


def construct(n: int, q: int, target: int):
    sigma, fixed, pairs = involution_data(q, target)
    assignments = balanced_assignments(n, len(pairs))
    weights = {}
    outer_sign = Fraction((-1) ** (len(pairs) + 1), len(assignments))
    for sizes in assignments:
        factors = [tuple(local_measure(size).items()) for size in sizes]
        for choices in itertools.product(*factors):
            counts = [0] * q
            counts[fixed] = 1
            weight = outer_sign
            for (a, b), ((i, j), local_weight) in zip(pairs, choices):
                counts[a], counts[b] = i, j
                weight *= local_weight
            key = tuple(counts)
            weights[key] = weights.get(key, Fraction(0)) + weight
    return sigma, fixed, pairs, assignments, {key: value for key, value in weights.items() if value}


def function_value(counts, sigma):
    for a, b in enumerate(sigma):
        if (a == b and counts[a] >= 2) or (a != b and counts[a] and counts[b]):
            return 1
    return -1


def centralizer(q: int, sigma):
    return tuple(
        perm
        for perm in itertools.permutations(range(q))
        if all(perm[sigma[a]] == sigma[perm[a]] for a in range(q))
    )


def relabel(counts, perm):
    result = [0] * len(counts)
    for old, new in enumerate(perm):
        result[new] = counts[old]
    return tuple(result)


def multinomial(counts):
    result = math.factorial(sum(counts))
    for count in counts:
        result //= math.factorial(count)
    return result


def lifted_string_weights(n: int, q: int, occupancy_weights):
    result = {}
    for string in itertools.product(range(q), repeat=n):
        counts = tuple(string.count(a) for a in range(q))
        orbit_weight = occupancy_weights.get(counts, Fraction(0))
        result[string] = orbit_weight / multinomial(counts)
    return result


def check_raw_query_rows(n: int, q: int, degree: int, string_weights):
    rows = 0
    for order in range(degree):
        for positions in itertools.combinations(range(n), order):
            for symbols in itertools.product(range(q), repeat=order):
                rows += 1
                residual = sum(
                    weight
                    for string, weight in string_weights.items()
                    if all(string[position] == symbol for position, symbol in zip(positions, symbols))
                )
                assert residual == 0
    return rows


def verify_target(n: int, q: int, target: int, raw_query_check: bool):
    sigma, fixed, pairs, assignments, weights = construct(n, q, target)
    degree = q - 1
    assert fixed == (target * pow(2, -1, q)) % q
    assert all(sum(counts) == n and counts[fixed] == 1 for counts in weights)

    occupancy_rows = 0
    for total in range(degree):
        for alpha in weak_compositions(total, q):
            occupancy_rows += 1
            residual = sum(
                weight
                * math.prod(falling(counts[a], alpha[a]) for a in range(q))
                for counts, weight in weights.items()
            )
            assert residual == 0

    l1 = sum(abs(weight) for weight in weights.values())
    mass = sum(weights.values())
    correlation = sum(weight * function_value(counts, sigma) for counts, weight in weights.items())
    assert mass == 0
    assert l1 == 1
    assert correlation == Fraction(1, 2 ** (len(pairs) - 1))

    group = centralizer(q, sigma)
    for counts, weight in weights.items():
        for perm in group:
            assert weights.get(relabel(counts, perm), Fraction(0)) == weight

    raw_rows = None
    strings_scanned = None
    if raw_query_check:
        string_weights = lifted_string_weights(n, q, weights)
        strings_scanned = len(string_weights)
        assert sum(abs(weight) for weight in string_weights.values()) == 1
        assert sum(string_weights.values()) == 0
        assert sum(
            weight * function_value(tuple(string.count(a) for a in range(q)), sigma)
            for string, weight in string_weights.items()
        ) == correlation
        raw_rows = check_raw_query_rows(n, q, degree, string_weights)

    return {
        "case": [n, q, target],
        "pair_total_assignments": [list(row) for row in assignments],
        "support_size": len(weights),
        "degree_band": f"all query degrees < {degree}",
        "occupancy_factorial_rows": occupancy_rows,
        "raw_one_hot_rows": raw_rows,
        "strings_scanned": strings_scanned,
        "centralizer_order": len(group),
        "total_mass": str(mass),
        "l1": str(l1),
        "correlation": str(correlation),
        "result": "PASS",
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    checks = []
    for n, q in CASES:
        for target in range(q):
            checks.append(verify_target(n, q, target, raw_query_check=(target == 0)))
    payload = {
        "implementation": "fresh reconstruction; no proposer code or output imported",
        "arithmetic": "fractions.Fraction",
        "checks": checks,
        "verification": "PASS",
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
