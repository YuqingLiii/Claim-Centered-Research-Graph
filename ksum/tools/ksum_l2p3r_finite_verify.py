"""Fresh exact finite reconstruction for the L2 phase-3 review.

No proposer module or proposer JSON is imported.  The script reconstructs the
occupancy measure, lifts it to strings, and checks all targets at (5,5) and
(7,3), including every raw degree-zero/one one-hot query monomial.
"""
from __future__ import annotations

import itertools
import json
import math
from fractions import Fraction


CASES = ((5, 5), (7, 3))


def involution_orbits(q: int, target: int):
    sigma = tuple((target - a) % q for a in range(q))
    fixed = [a for a in range(q) if sigma[a] == a]
    assert len(fixed) == 1
    used = set(fixed)
    pairs = []
    for a in range(q):
        if a not in used:
            b = sigma[a]
            pairs.append(tuple(sorted((a, b))))
            used.update((a, b))
    return fixed[0], tuple(sorted(pairs))


def distinct_balanced_totals(n: int, r: int):
    low, extra = divmod(n - 1, r)
    assert low >= 2
    row = (low + 1,) * extra + (low,) * (r - extra)
    return tuple(sorted(set(itertools.permutations(row))))


def local_axis(s: int):
    return (((s, 0), Fraction(1, 2)), ((0, s), Fraction(1, 2)))


def local_interior(s: int):
    a = s // 2
    b = s - a
    if a == b:
        return (((a, b), Fraction(1)),)
    return (((a, b), Fraction(1, 2)), ((b, a), Fraction(1, 2)))


def outer(r: int):
    points = [0]
    power = 1
    while power <= r:
        points.append(power)
        power *= 5
    raw = {}
    for k in points:
        denominator = math.prod(k - u for u in points if u != k)
        raw[k] = Fraction(1, denominator)
    if raw[0] > 0:
        raw = {k: -value for k, value in raw.items()}
    z = sum(abs(value) for value in raw.values())
    return {k: value / z for k, value in raw.items()}


def occupancy_measure(n: int, q: int, target: int):
    fixed, pairs = involution_orbits(q, target)
    totals = distinct_balanced_totals(n, len(pairs))
    layers = outer(len(pairs))
    measure = {}
    for row in totals:
        row_weight = Fraction(1, len(totals))
        for k, layer_weight in layers.items():
            for active_tuple in itertools.combinations(range(len(pairs)), k):
                active = set(active_tuple)
                pattern_weight = layer_weight / math.comb(len(pairs), k)
                tables = [
                    local_interior(s) if c in active else local_axis(s)
                    for c, s in enumerate(row)
                ]
                for choices in itertools.product(*tables):
                    counts = [0] * q
                    counts[fixed] = 1
                    weight = row_weight * pattern_weight
                    for (a, b), ((i, j), local_weight) in zip(pairs, choices):
                        counts[a], counts[b] = i, j
                        weight *= local_weight
                    key = tuple(counts)
                    measure[key] = measure.get(key, Fraction(0)) + weight
    return fixed, pairs, layers, {x: w for x, w in measure.items() if w}


def sign(counts: tuple[int, ...], target: int) -> int:
    q = len(counts)
    for a in range(q):
        b = (target - a) % q
        if a == b:
            if counts[a] >= 2:
                return 1
        elif counts[a] and counts[b]:
            return 1
    return -1


def multinomial_orbit_size(counts: tuple[int, ...]) -> int:
    value = math.factorial(sum(counts))
    for count in counts:
        value //= math.factorial(count)
    return value


def lifted_strings(n: int, q: int, occupancy):
    lifted = {}
    for word in itertools.product(range(q), repeat=n):
        counts = tuple(word.count(a) for a in range(q))
        weight = occupancy.get(counts, Fraction(0))
        if weight:
            lifted[word] = weight / multinomial_orbit_size(counts)
    return lifted


def centralizer(q: int, target: int):
    sigma = tuple((target - a) % q for a in range(q))
    return tuple(
        perm for perm in itertools.permutations(range(q))
        if all(perm[sigma[a]] == sigma[perm[a]] for a in range(q))
    )


def move_counts(counts, perm):
    result = [0] * len(counts)
    for old, new in enumerate(perm):
        result[new] = counts[old]
    return tuple(result)


def verify(n: int, q: int, target: int):
    fixed, pairs, layers, occupancy = occupancy_measure(n, q, target)
    assert sum(occupancy.values()) == 0
    assert sum(abs(w) for w in occupancy.values()) == 1
    correlation = sum(w * sign(x, target) for x, w in occupancy.items())
    assert correlation == 1
    assert correlation > Fraction(2, 3)

    # At both commissioned points m=1, so the claimed band is degree <2.
    factorial_residuals = [sum(occupancy.values())]
    factorial_residuals.extend(
        sum(w * counts[a] for counts, w in occupancy.items()) for a in range(q)
    )
    assert factorial_residuals == [0] * (q + 1)

    group = centralizer(q, target)
    for counts, weight in occupancy.items():
        for perm in group:
            assert occupancy.get(move_counts(counts, perm), 0) == weight

    strings = lifted_strings(n, q, occupancy)
    assert sum(strings.values()) == 0
    assert sum(abs(w) for w in strings.values()) == 1
    raw_residuals = [sum(strings.values())]
    for position in range(n):
        for symbol in range(q):
            raw_residuals.append(sum(
                weight for word, weight in strings.items() if word[position] == symbol
            ))
    assert raw_residuals == [0] * (1 + n * q)
    string_correlation = sum(w * sign(tuple(word.count(a) for a in range(q)), target)
                             for word, w in strings.items())
    assert string_correlation == correlation

    return {
        "case": [n, q, target],
        "fixed": fixed,
        "pairs": [list(pair) for pair in pairs],
        "outer_weights": {str(k): str(w) for k, w in layers.items()},
        "occupancy_support": len(occupancy),
        "lifted_string_support": len(strings),
        "factorial_rows_checked": len(factorial_residuals),
        "raw_one_hot_rows_checked": len(raw_residuals),
        "centralizer_order": len(group),
        "l1": "1",
        "correlation": str(correlation),
        "all_residuals": "0",
    }


def main() -> None:
    checks = [verify(n, q, target) for n, q in CASES for target in range(q)]
    print(json.dumps({
        "arithmetic": "fractions.Fraction",
        "independent_of_proposer_code_and_json": True,
        "checks": checks,
        "verification": "PASS",
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
