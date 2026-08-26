"""
Finite matched-degree legality check, restored from the archived checker.
Requires NumPy. Run: python3 se/tools/se_matched_degree_lemma_check.py

Tests ||R_m P_(k,lambda)||^2 <= r_top(q,k,theta) on the explicitly enumerated
small cases below, with lambda=(q-k,theta). R_m restricts uniform words to
injective words; P combines weight-k and alphabet-isotypic projectors.
In normalized bases, ||R_m P||^2 is the norm of q^m/(q)_m times the injective
principal block of P. The alphabet projector preserves injective words.

The numerical body and its original shape filters are retained. This checks
40 finite rows, not every parameter of the proposed general lemma. Matrix
norms are floating-point values with tolerance 1e-8; EQ is numerical equality.
All k>=1 rows are outside the small taper window of the SE witness.
"""
import itertools
from fractions import Fraction
from math import factorial

import numpy as np


def partitions(m, maxpart=None):
    if maxpart is None:
        maxpart = m
    if m == 0:
        yield ()
        return
    for first in range(min(m, maxpart), 0, -1):
        for rest in partitions(m - first, first):
            yield (first,) + rest


def hook_dim(lam):
    lam = [p for p in lam if p > 0]
    if not lam:
        return 1
    n = sum(lam)
    conj = [sum(1 for r in lam if r > j) for j in range(lam[0])]
    num, den = factorial(n), 1
    for i, row in enumerate(lam):
        for j in range(row):
            den *= (row - j) + (conj[j] - i) - 1
    return num // den


def mn_char(lam, rho):
    lam = tuple(p for p in lam if p > 0)
    rho = tuple(p for p in rho if p > 0)
    if not rho:
        return 1 if not lam else 0
    r, rest = rho[0], rho[1:]
    L = list(lam)
    rows = len(L)
    beta = [L[i] + (rows - 1 - i) for i in range(rows)]
    bset = set(beta)
    tot = 0
    for b in beta:
        if b - r >= 0 and (b - r) not in bset:
            nb = sorted([x for x in beta if x != b] + [b - r], reverse=True)
            ht = sum(1 for x in beta if (b - r) < x < b)
            nl = tuple(nb[i] - (len(nb) - 1 - i) for i in range(len(nb)))
            tot += (-1) ** ht * mn_char(tuple(p for p in nl if p > 0), rest)
    return tot


def cycle_type(g):
    m = len(g)
    seen = [False] * m
    ct = []
    for i in range(m):
        if not seen[i]:
            L, j = 0, i
            while not seen[j]:
                seen[j] = True
                j = g[j]
                L += 1
            ct.append(L)
    return tuple(sorted(ct, reverse=True))


def falling(q, m):
    p = 1
    for i in range(m):
        p *= (q - i)
    return p


def r_top(q, k, theta):
    lam = (q - k,) + tuple(theta)
    return Fraction(q ** k * hook_dim(theta), factorial(k) * hook_dim(lam))


def run(q, m):
    inj = [t for t in itertools.product(range(q), repeat=m) if len(set(t)) == m]
    idx = {t: i for i, t in enumerate(inj)}
    D = len(inj)
    assert D == falling(q, m)
    SQ = list(itertools.permutations(range(q)))

    # weight projector, Inj x Inj block:  Pi^{wt=k}[x,y] = q^{-(m-k)} e_k(t_1..t_m),
    # t_i = delta_{x_i y_i} - 1/q.        (BR:363 Pi_0=J/q, Pi_1=I-J/q; BR:371-5)
    def Wt(k):
        M = np.zeros((D, D))
        for i, x in enumerate(inj):
            for j, y in enumerate(inj):
                t = [(1.0 if x[a] == y[a] else 0.0) - 1.0 / q for a in range(m)]
                ek = 0.0
                for sub in itertools.combinations(range(m), k):
                    p = 1.0
                    for a in sub:
                        p *= t[a]
                    ek += p
                M[i, j] = ek / q ** (m - k)
        return M

    # alphabet isotypic projector, Inj x Inj block
    def Alph(lam):
        f = hook_dim(lam)
        M = np.zeros((D, D))
        for g in SQ:
            ch = mn_char(lam, cycle_type(g))
            if ch == 0:
                continue
            w = f * ch / factorial(q)
            for i, x in enumerate(inj):
                M[idx[tuple(g[v] for v in x)], i] += w
        return M

    checked, violations = 0, 0
    scale = q ** m / falling(q, m)
    print("\n  q=%d  m=%d   (q)_m=%d" % (q, m, D))
    print("  %-6s %-10s %-16s %-16s %-16s %-8s"
          % ("k", "theta", "||R_m P||^2", "r_top(q,k,th)", "ratio", "verdict"))
    for k in range(0, min(m, q - 1) + 1):
        Wk = Wt(k)
        for th in (list(partitions(k)) if k > 0 else [()]):
            if len(th) > q - k:          # lambda=(q-k,theta) must be a partition
                continue
            if th and th[0] > q - k:
                continue
            lam = (q - k,) + tuple(th)
            P = Wk @ Alph(lam)
            val = np.linalg.norm(scale * P, 2)
            rt = float(r_top(q, k, th))
            ok = "EQ" if abs(val - rt) < 1e-8 else ("<=" if val <= rt + 1e-8 else "VIOLATED")
            checked += 1
            violations += int(ok == "VIOLATED")
            print("  %-6d %-10s %-16.10f %-16.10f %-16.10f %-8s"
                  % (k, str(th), val, rt, (val / rt if rt else float("nan")), ok))
    return checked, violations


print("=" * 92)
print("MATCHED-DEGREE LEGALITY LEMMA   ||R_m . Pi^{wt=k} . Pi^alph_{(q-k,theta)}||^2 "
      "<= r_top(q,k,theta)")
print("=" * 92)
# (8,8)/(8,4) are out of reach for this pure-Python character loop (40320! orbit sums).
# The SE case of record is q=2n=6, m=2n=6 (NO side) and m=n=3 (YES side), at n=3.
total_rows, total_violations = 0, 0
for (q, m) in [(6, 6), (6, 3), (6, 4), (5, 5), (5, 3), (7, 3)]:
    rows, violations = run(q, m)
    total_rows += rows
    total_violations += violations
print("\nCHECKED ROWS: %d; VIOLATIONS: %d" % (total_rows, total_violations))
print("DONE")
raise SystemExit(0 if total_violations == 0 else 1)
