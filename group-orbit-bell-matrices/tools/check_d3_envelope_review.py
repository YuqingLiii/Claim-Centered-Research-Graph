#!/usr/bin/env python3
"""Independent integer endpoint proof check; imports no author code/certificate."""
from itertools import product


def demand(condition, message):
    if not condition:
        raise RuntimeError(message)


# Independent construction from the entire coordinate cube, in lexical order.
roots = tuple(v for v in product((-1, 0, 1), repeat=3)
              if sum(x * x for x in v) == 2)
n = len(roots)
demand(n == 12 and len(set(roots)) == 12, "root coverage")
demand(all(tuple(-x for x in v) in roots for v in roots), "antipodes")
dot = lambda a, b: sum(x * y for x, y in zip(a, b))
demand(all(sum(v[i] * v[j] for v in roots) == 8 * (i == j)
           for i in range(3) for j in range(3)), "frame normalization")
# M = 8 A is integral. The three tested parameters are lambda = p / 8.
M = tuple(tuple(dot(v, w) for w in roots) for v in roots)
demand(all(M[i][i] == 2 for i in range(n)), "Gram diagonal")
demand(all(sum(M[i][k] * M[k][j] for k in range(n)) == 8 * M[i][j]
           for i in range(n) for j in range(n)), "A is a projection")
endpoints = ((0, 80), (2, 56), (4, 48))
maxima = [-1] * 3
max_counts = [0] * 3
seen = set()
for mask in range(1 << n):
    t = tuple(1 if (mask >> i) & 1 else -1 for i in range(n))
    seen.add(t)
    mt = tuple(dot(row, t) for row in M)
    for k, (p, cap) in enumerate(endpoints):
        numerator = sum(abs(mt[i] - p * t[i]) for i in range(n))
        demand(numerator <= cap, "endpoint upper bound")
        if numerator > maxima[k]:
            maxima[k], max_counts[k] = numerator, 1
        elif numerator == maxima[k]:
            max_counts[k] += 1
demand(len(seen) == 4096, "all Bob signs")
demand(maxima == [80, 56, 48], "sharp endpoint values")

# The following row/sign data are copied from the dossier, not its code/JSON.
document_order = (
    (-1, -1, 0), (-1, 1, 0), (1, -1, 0), (1, 1, 0),
    (-1, 0, -1), (-1, 0, 1), (1, 0, -1), (1, 0, 1),
    (0, -1, -1), (0, -1, 1), (0, 1, -1), (0, 1, 1),
)
demand(set(document_order) == set(roots), "dossier root set")
witnesses = (
    ((-1, -1, 1, 1, -1, -1, 1, 1, -1, -1, 1, 1),
     (-1, -1, 1, 1, -1, -1, 1, 1, -1, -1, 1, 1), 80, 12),
    ((1, 1, 1, 1, -1, 1, -1, 1, -1, 1, -1, 1),
     (-1, -1, -1, -1, -1, 1, -1, 1, -1, 1, -1, 1), 64, 4),
)
for number, (s_doc, t_doc, intercept8, st) in enumerate(witnesses, 1):
    s_map, t_map = dict(zip(document_order, s_doc)), dict(zip(document_order, t_doc))
    s, t = tuple(s_map[v] for v in roots), tuple(t_map[v] for v in roots)
    demand(all(x in (-1, 1) for x in s + t), "witness signs")
    direct_intercept8 = sum(s[i] * M[i][j] * t[j]
                            for i in range(n) for j in range(n))
    demand(direct_intercept8 == intercept8 and dot(s, t) == st, "fixed affine witness")
    print("witness", number, "8*s^T*A*t =", intercept8, "; s^T*t =", st)
    if number == 2:
        counterexample8 = sum(s[i] * (M[i][j] - 4 * (i == j)) * t[j]
                              for i in range(n) for j in range(n))
        demand(counterexample8 == 48 and counterexample8 > 32, "counterexample 6 > 4")

print("roots = 12; full antipodal coverage; W^T W = 8 I; A^2 = A")
print("Bob vectors independently exhausted =", len(seen))
for (p, cap), maximum, count in zip(endpoints, maxima, max_counts):
    print("lambda =", str(p) + "/8", "; max 8*f_t =", maximum,
          "; prescribed cap =", cap, "; maximizing Bob count =", count)
print("continuum proof: each f_t is convex; endpoint caps imply each affine secant cap")
print("fixed witnesses attain 10-12*lambda and 8-4*lambda; both equal 7 at 1/4")
print("counterexample: at lambda=1/2, witnessed value 48/8 = 6 > 32/8 = 4")
print("PASS: independent integer endpoint upper bounds and fixed-sign lower bounds")
