from fractions import Fraction
from itertools import combinations, product

S = [
    tuple(Fraction(x, 2) for x in (1, -1, -1, -1, -1, -1, -1, 1)),
    tuple(map(Fraction, (1, 1, 0, 0, 0, 0, 0, 0))),
    tuple(map(Fraction, (-1, 1, 0, 0, 0, 0, 0, 0))),
    tuple(map(Fraction, (0, -1, 1, 0, 0, 0, 0, 0))),
    tuple(map(Fraction, (0, 0, -1, 1, 0, 0, 0, 0))),
    tuple(map(Fraction, (0, 0, 0, -1, 1, 0, 0, 0))),
    tuple(map(Fraction, (0, 0, 0, 0, -1, 1, 0, 0))),
    tuple(map(Fraction, (0, 0, 0, 0, 0, -1, 1, 0))),
]


def dot(a, b):
    return sum(x * y for x, y in zip(a, b))


C = [[dot(S[i], S[j]) for j in range(8)] for i in range(8)]

EXPECTED_C = [
    [2, 0, -1, 0, 0, 0, 0, 0],
    [0, 2, 0, -1, 0, 0, 0, 0],
    [-1, 0, 2, -1, 0, 0, 0, 0],
    [0, -1, -1, 2, -1, 0, 0, 0],
    [0, 0, 0, -1, 2, -1, 0, 0],
    [0, 0, 0, 0, -1, 2, -1, 0],
    [0, 0, 0, 0, 0, -1, 2, -1],
    [0, 0, 0, 0, 0, 0, -1, 2],
]

assert C == [list(map(Fraction, row)) for row in EXPECTED_C]


def det_bareiss(A):
    A = [list(map(int, row)) for row in A]
    n = len(A)
    prev = 1
    sign = 1
    for k in range(n - 1):
        if A[k][k] == 0:
            r = next(r for r in range(k + 1, n) if A[r][k] != 0)
            A[k], A[r] = A[r], A[k]
            sign = -sign
        p = A[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                A[i][j] = (A[i][j] * p - A[i][k] * A[k][j]) // prev
        prev = p
    return sign * A[-1][-1]


assert det_bareiss(EXPECTED_C) == 1

ambient = set()
for i, j in combinations(range(8), 2):
    for si, sj in product((1, -1), repeat=2):
        v = [Fraction(0)] * 8
        v[i] = si
        v[j] = sj
        ambient.add(tuple(v))

for signs in product((1, -1), repeat=8):
    if sum(s < 0 for s in signs) % 2 == 0:
        ambient.add(tuple(Fraction(s, 2) for s in signs))

assert len(ambient) == 240
assert all(dot(r, r) == 2 for r in ambient)


def solve(A, b):
    n = len(A)
    M = [list(A[i]) + [Fraction(b[i])] for i in range(n)]
    for col in range(n):
        p = next(r for r in range(col, n) if M[r][col] != 0)
        M[col], M[p] = M[p], M[col]
        q = M[col][col]
        M[col] = [x / q for x in M[col]]
        for r in range(n):
            if r != col and M[r][col] != 0:
                q = M[r][col]
                M[r] = [M[r][j] - q * M[col][j] for j in range(n + 1)]
    return tuple(M[i][-1] for i in range(n))


Aambient = [[S[i][j] for i in range(8)] for j in range(8)]
coeff = set()
for r in ambient:
    x = solve(Aambient, r)
    assert all(t.denominator == 1 for t in x)
    coeff.add(tuple(int(t) for t in x))

assert len(coeff) == 240
assert all(
    all(x >= 0 for x in r) or all(x <= 0 for x in r)
    for r in coeff
)

pos = sorted(
    (r for r in coeff if all(x >= 0 for x in r)),
    key=lambda r: (-sum(r), r),
)
assert len(pos) == 120

n = 120
strict_up = [0] * n
for i, a in enumerate(pos):
    for j, b in enumerate(pos):
        if i != j and all(x <= y for x, y in zip(a, b)):
            assert j < i
            strict_up[i] |= 1 << j


def norm2(z):
    return sum(z[i] * C[i][j] * z[j] for i in range(8) for j in range(8))


F = [-1] * 121
count = 0


def dfs(i, selected, z, k):
    global count
    if i == n:
        count += 1
        F[k] = max(F[k], norm2(z))
        return
    dfs(i + 1, selected, z, k)
    if (strict_up[i] & ~selected) == 0:
        a = pos[i]
        dfs(
            i + 1,
            selected | (1 << i),
            tuple(z[j] + a[j] for j in range(8)),
            k + 1,
        )


dfs(0, 0, (0,) * 8, 0)

EXPECTED_F = (
    0, 2, 6, 12, 20, 30, 42, 56, 72, 86, 104, 124, 146, 170, 196, 212,
    230, 250, 272, 300, 322, 350, 372, 402, 430, 460, 492, 526, 562, 600,
    622, 646, 672, 700, 730, 762, 800, 826, 862, 900, 932, 966, 1004, 1044,
    1086, 1130, 1166, 1204, 1244, 1286, 1332, 1376, 1422, 1470, 1520, 1572,
    1626, 1682, 1684, 1688, 1694, 1702, 1712, 1724, 1738, 1748, 1764, 1782,
    1794, 1808, 1824, 1850, 1882, 1916, 1952, 1990, 2030, 2072, 2116, 2118,
    2122, 2128, 2136, 2166, 2168, 2172, 2184, 2200, 2218, 2238, 2260, 2280,
    2312, 2314, 2318, 2324, 2332, 2352, 2366, 2368, 2372, 2378, 2386, 2400,
    2420, 2422, 2430, 2432, 2440, 2442, 2450, 2452, 2460, 2462, 2466, 2468,
    2472, 2474, 2476, 2478, 2480,
)

assert count == 25080
assert tuple(F) == EXPECTED_F
assert [
    (k, F[k], 3 * F[k] - 26 * k)
    for k in range(121)
    if 3 * F[k] - 26 * k > 4544
] == [(98, 2366, 4550), (104, 2420, 4556)]

print(f"ambient roots, positive roots, filters = {len(ambient)} {len(pos)} {count}")
print(f"F_98 = {F[98]}")
print(f"F_104 = {F[104]}")
