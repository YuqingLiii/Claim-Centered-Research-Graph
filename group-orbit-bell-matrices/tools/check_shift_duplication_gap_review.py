#!/usr/bin/env python3
"""Reviewer-owned exact C10 matrix mapping and isolated test-point check."""
from fractions import Fraction


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


dot = lambda a, b: sum(x * y for x, y in zip(a, b))
source = (
    (-1, -1, 0), (-1, 1, 0), (1, -1, 0), (1, 1, 0),
    (-1, 0, -1), (-1, 0, 1), (1, 0, -1), (1, 0, 1),
    (0, -1, -1), (0, -1, 1), (0, 1, -1), (0, 1, 1),
)
u = ((1, -1, 0), (1, 1, 0), (1, 0, -1),
     (1, 0, 1), (0, 1, -1), (0, 1, 1))
w = u + tuple(tuple(-x for x in v) for v in u)
require(len(set(w)) == 12 and set(w) == set(source), "full-root coverage")
permutation = tuple(source.index(v) for v in w)
require(set(permutation) == set(range(12)), "permutation bijection")
g = tuple(tuple(dot(v, z) for z in source) for v in source)
k = tuple(tuple(dot(v, z) for z in u) for v in u)
full24 = tuple(tuple(3 * g[permutation[i]][permutation[j]] - 8 * (i == j)
                    for j in range(12)) for i in range(12))
for i in range(12):
    for j in range(12):
        # 8D(C) has blocks K,-K;-K,K since C=K/4.
        block_sign = 1 if (i < 6) == (j < 6) else -1
        gram_entry = block_sign * k[i % 6][j % 6]
        require(g[permutation[i]][permutation[j]] == gram_entry,
                "R A R^T equals D(C), scaled by 8")
        require(full24[i][j] == 3 * gram_entry - 8 * (i == j),
                "shift commutes with simultaneous permutation")
half12 = tuple(tuple(3 * k[i][j] - 4 * (i == j)
                    for j in range(6)) for i in range(6))


def maximum(matrix):
    size = len(matrix)
    best, count = -1, 0
    for mask in range(1 << size):
        bob = tuple(1 if mask & (1 << j) else -1 for j in range(size))
        value = sum(abs(dot(row, bob)) for row in matrix)
        best = max(best, value)
        count += 1
    return best, count


full, full_count = maximum(full24)
half, half_count = maximum(half12)
require((full, full_count) == (160, 4096), "full shifted value")
require((half, half_count) == (36, 64), "half shifted value")
require(Fraction(full, 24) == Fraction(20, 3), "full normalization")
require(2 * Fraction(half, 12) == 6, "doubled half normalization")
gap = Fraction(full, 24) - 2 * Fraction(half, 12)
require(gap == Fraction(2, 3) and gap > 0, "strict shifted-duplication gap")
print("Permutation R selects one-based source rows:", tuple(i + 1 for i in permutation))
print("PASS: all 144 entries match for 8 R A R^T = 8 D(C), and for shifts scaled by 24")
print("Full Bob signs:", full_count, "; max ||24(D(C)-I/3)t||_1 =", full)
print("Half Bob signs:", half_count, "; max ||12(C-I/3)t||_1 =", half)
print("Exact comparison:", Fraction(full, 24), ">", 2 * Fraction(half, 12), "; gap =", gap)
print("PASS: exact C10 matrix permutation and full/half test-point values")
