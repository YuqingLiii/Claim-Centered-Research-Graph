#!/usr/bin/env python3
"""Exhaustive exact certificate for GROTHORB.d3-half-shift-value."""

from collections import Counter
from fractions import Fraction
from itertools import product


def dot(a, b):
    return sum(x * y for x, y in zip(a, b))


def main():
    edges = ((0, 1), (0, 2), (1, 2))
    roots = []
    for i, j in edges:
        for epsilon in (-1, 1):
            w = [0, 0, 0]
            w[i], w[j] = 1, epsilon
            roots.append(tuple(w))
    h_matrix = tuple(tuple(3 * dot(u, v) - 4 * (i == j)
                           for j, v in enumerate(roots))
                     for i, u in enumerate(roots))
    assert h_matrix == (
        (2, 0, 3, 3, -3, -3), (0, 2, 3, 3, 3, 3),
        (3, 3, 2, 0, 3, -3), (3, 3, 0, 2, -3, 3),
        (-3, 3, 3, -3, 2, 0), (-3, 3, -3, 3, 0, 2),
    )
    signs = tuple(product((-1, 1), repeat=6))
    histogram = Counter()
    cases = Counter()
    images = {}
    for bob in signs:
        ht = tuple(dot(row, bob) for row in h_matrix)
        images[bob] = ht
        numerator = sum(map(abs, ht))
        histogram[numerator] += 1
        selections = []
        occupancy = [0, 0, 0]
        v = [0, 0, 0]
        for edge_index, (i, j) in enumerate(edges):
            minus, plus = bob[2 * edge_index:2 * edge_index + 2]
            a = [0, 0, 0]
            a[i], a[j] = (minus + plus) // 2, (plus - minus) // 2
            assert sum(map(abs, a)) == 1
            selected = i if a[i] else j
            occupancy[selected] += 1
            v[selected] += a[selected]
            selections.append(a)
        root_image = tuple(sum(t * w[k] for t, w in zip(bob, roots))
                           for k in range(3))
        assert root_image == tuple(2 * x for x in v)
        for edge_index, ((i, j), a) in enumerate(zip(edges, selections)):
            row_sum = abs(ht[2 * edge_index]) + abs(ht[2 * edge_index + 1])
            assert row_sum == 4 * max(abs(3 * v[i] - 2 * a[i]),
                                     abs(3 * v[j] - 2 * a[j]))
        if sorted(occupancy) == [1, 1, 1]:
            case = "balanced"
            assert numerator == 36
        else:
            assert sorted(occupancy) == [0, 1, 2]
            double = occupancy.index(2)
            if v[double] == 0:
                case = "double_canceling"
                assert numerator == 24
            else:
                assert abs(v[double]) == 2
                case = "double_agreeing"
                assert numerator == 36
        cases[case] += 1

    assert histogram == {24: 24, 36: 40}
    assert cases == {"double_agreeing": 24, "double_canceling": 24, "balanced": 16}
    maximum_numerator = max(histogram)
    assert Fraction(maximum_numerator, 12) == 3
    direct_maximum = max(dot(alice, images[bob]) for alice in signs for bob in signs)
    assert direct_maximum == maximum_numerator
    ones = (1,) * 6
    assert images[ones] == (2, 14, 8, 8, 2, 2)
    assert dot(ones, images[ones]) == 36
    print("Exact U row order: 12-,12+,13-,13+,23-,23+; H=3UU^T-4I; B=H/12.")
    print("All 64 Bob signs enumerated; exact Alice optimum=max_t ||Ht||_1/12=3; PASS")
    print("Numerator histogram: 24 occurs 24 times; 36 occurs 40 times; PASS")
    print("Cases: double agreeing=24, double canceling=24, balanced=16; PASS")
    print("Every row-pair identity and signed-edge case classification checked; PASS")
    print("All 4096 ordered Alice/Bob pairs enumerated; maximum numerator=36; PASS")
    print("Witness s=t=(1,1,1,1,1,1), Ht=(2,14,8,8,2,2), value=3; PASS")
    print("Scope: exact certificate for the registered six-root matrix at lambda=1/3.")


if __name__ == "__main__":
    main()
