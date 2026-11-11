#!/usr/bin/env python3
"""Exact rational finite checks; the general statements use the linked proof."""
from fractions import Fraction as F
from itertools import product


def transpose(a):
    return list(map(list, zip(*a)))


def mm(a, b):
    return [[sum(x*y for x, y in zip(row, col)) for col in zip(*b)] for row in a]


def norm2(a):
    return sum(x*x for row in a for x in row)


def check(a, projector, sigma, tau, sqrt_mn, vectors):
    m, n = len(a), len(a[0])
    assert all(sum(x*x for x in v) == 1 for v in vectors)
    identity_minus_p = [[F(i == j)-projector[i][j] for j in range(n)] for i in range(n)]
    count = 0
    best = None
    for yr in product(vectors, repeat=n):
        ay = mm(a, yr)
        out = norm2(mm(identity_minus_p, yr))/n
        ay2 = norm2(ay)/(sigma*sigma*n)
        for xr in product(vectors, repeat=m):
            objective = sum(x*y for u, v in zip(xr, ay) for x, y in zip(u, v))
            q = objective/(sigma*sqrt_mn)
            best = q if best is None else max(best, q)
            assert q <= 1
            if q < 0:
                continue
            epsilon = 1-q
            assert out*(1-(tau/sigma)**2) <= 2*epsilon-epsilon**2
            assert 1+ay2-2*q <= 2*epsilon
            count += 1
    return count, best


def main():
    p3 = [[F(i == j)-F(1, 3) for j in range(3)] for i in range(3)]
    signs = [(F(1),), (F(-1),)]
    count, best = check(p3, p3, F(1), F(0), F(3), signs)
    assert best == F(8, 9)
    # P3's balance-map least squared singular value is 2/3 in Frobenius coordinates.
    # The proof of this constant is in the run record, not inferred from enumeration.
    threshold = 1-F(2, 3)/(16*2**2)
    assert best <= threshold
    print(f'P3 signs: nonnegative_pairs={count}, best_relative_score={best}, dimension_gap_threshold={threshold}, PASS')
    rational_vectors = [(F(1), F(0)), (F(-1), F(0)),
                        (F(3, 5), F(4, 5)), (F(-3, 5), F(-4, 5))]
    count, best = check(p3, p3, F(1), F(0), F(3), rational_vectors)
    print(f'P3 rational planar strategies: nonnegative_pairs={count}, best_relative_score={best}, PASS')
    a = [[F(2), F(0)], [F(0), F(1)]]
    p = [[F(1), F(0)], [F(0), F(0)]]
    count, best = check(a, p, F(2), F(1), F(2), rational_vectors)
    print(f'diag(2,1) imbalanced strategies: nonnegative_pairs={count}, best_relative_score={best}, PASS')
    a = [[F(1)]*4]
    p = [[F(1, 4)]*4 for _ in range(4)]
    count, best = check(a, p, F(2), F(0), F(2), rational_vectors)
    print(f'1x4 rectangular strategies: nonnegative_pairs={count}, best_relative_score={best}, PASS')
    print('All checks use exact Fraction arithmetic. This finite run is not a universal proof.')


if __name__ == '__main__':
    main()
