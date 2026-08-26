"""Exact per-class singular values of SE adversary matrices via the NO-side
Gram kernel  K = Gamma^T Gamma  (an H-conjugation-invariant kernel on
C[NO] = C[S_2n]) -- no YES-side multiplicity geometry needed.

Derivation (certified conventions from mdh_certify):
  Gamma[y,x] = t(h_sigma o x^{-1} o f)  for y=(f, s), sigma_y = s^{-1},
               h_s(i)=i (i<n), h_s(n+j)=n+s(j).
  K(x,x') = sum_y Gamma[y,x] Gamma[y,x']
          = sum_{s in S_n} sum_{g in X_L} t(h_s o g) t(h_s o x'^{-1} x o g).
  Fourier: khat(lam) = n! * sum_s T_s P_V Ttil_s,
     T_s   = sum_u t(h_s o u) rho(x_u),      (forward BFS propagation)
     Ttil_s= sum_g t(h_s o g) rho(x_g^{-1})  (reverse-BFS accumulation).
  khat(lam) commutes with rho(H) (JM elements included), hence preserves the
  joint JM eigenspace W_N(mu,nu); the class-(lam;mu,nu) singular values obey
     sigma^2 = eigenvalues of the pencil (M, S),
     M[c,c'] = w_c^T G khat(lam) w_c',   S[c,c'] = w_c^T G w_c'.
  Exact: charpoly of S^{-1} M over Q.
"""
import math, sys
from fractions import Fraction
from pathlib import Path

PROJECT = Path(__file__).resolve().parents[1]
from mdh_engine import (YSN, CosetSpace, LambdaData, partitions, syt_list,
                        solve_linear, F0, F1, perm_word)
from mdh_blocks import BlockEngine

def hmap(s, n):
    """position map h_s on [2n] as a tuple."""
    return tuple(list(range(n)) + [n + s[j] for j in range(n)])

def t_shift(tvals, seen, cs, s, n):
    """coefficients c_i = t(h_s o ell_i) for every coset index i."""
    h = hmap(s, n)
    out = [None] * cs.size
    for i, ell in enumerate(cs.ell):
        ell2 = tuple(h[v] for v in ell)
        out[i] = tvals[seen[ell2]]
    return out

class SigmaEngine:
    def __init__(self, n, lam, cs=None):
        self.n = n
        self.lam = lam
        self.cs = cs if cs is not None else CosetSpace(n)
        self.eng = BlockEngine(n, lam, self.cs)
        self.rep = self.eng.rep
        self.orbs = self.cs.orbits()

    def khat_on(self, tvals_by_orbit, vecs):
        """Apply khat(lam) = n! sum_s T_s P_V Ttil_s to each vector in vecs."""
        n, cs, rep = self.n, self.cs, self.rep
        d = rep.dim
        orb_list, seen = self.orbs
        tcos = [tvals_by_orbit[seen[ell]] for ell in cs.ell]  # t at each coset
        from itertools import permutations as perms
        out = [[F0] * d for _ in vecs]
        # children lists for reverse accumulation
        children = [[] for _ in range(cs.size)]
        for i in range(1, cs.size):
            par, k = cs.tree[i]
            children[par].append((i, k))
        for s in perms(range(n)):
            # coefficients t(h_s o ell_i)
            h = hmap(s, n)
            coef = [None] * cs.size
            for i, ell in enumerate(cs.ell):
                coef[i] = tvals_by_orbit[seen[tuple(h[v] for v in ell)]]
            for vi, w in enumerate(vecs):
                # ---- reverse accumulation: a = sum_g coef[g] rho(x_g^{-1}) w
                acc = [None] * cs.size
                for i in range(cs.size - 1, -1, -1):
                    a = [coef[i] * x for x in w] if coef[i] else [F0] * d
                    for (j, k) in children[i]:
                        cj = acc[j]
                        # add rho(s_k) acc[j]
                        tmp = self.rep.apply_s(k, cj)
                        for r in range(d):
                            if tmp[r]: a[r] += tmp[r]
                        acc[j] = None
                    acc[i] = a
                a = acc[0]
                # ---- project to V
                a = self.eng.ld.PV_apply(a)
                # ---- forward propagation: out += sum_u coef[u] rho(x_u) a
                fwd = [None] * cs.size
                fwd[0] = a
                tgt = out[vi]
                for i in range(cs.size):
                    if i > 0:
                        par, k = cs.tree[i]
                        fwd[i] = self.rep.apply_s(k, fwd[par])
                    ci = coef[i]
                    if ci:
                        vv = fwd[i]
                        for r in range(d):
                            if vv[r]: tgt[r] += ci * vv[r]
        fnf = Fraction(math.factorial(self.n))
        return [[fnf * x for x in v] for v in out]

    def class_sigma2(self, mu, nu, tvals_by_orbit):
        """Exact pencil (M,S) on W_N(mu,nu); returns (M, S, cols)."""
        cols = self.eng.columns(mu, nu)
        if not cols:
            return None, None, []
        img = self.khat_on(tvals_by_orbit, cols)
        G = self.rep.gram
        d = self.rep.dim
        M = [[sum(a[i] * G[i] * b[i] for i in range(d)) for b in img] for a in cols]
        S = [[sum(a[i] * G[i] * b[i] for i in range(d)) for b in cols] for a in cols]
        return M, S, cols

def charpoly(A):
    """Exact characteristic polynomial of a small Fraction matrix (Leverrier)."""
    m = len(A)
    I = [[F1 if i == j else F0 for j in range(m)] for i in range(m)]
    coeffs = [F1]
    Mk = [row[:] for row in I]
    Ak = A
    B = [row[:] for row in I]
    cs = [F1]
    for k in range(1, m + 1):
        # B = A @ B
        B = [[sum(A[i][r] * B[r][j] for r in range(m)) for j in range(m)]
             for i in range(m)]
        c = -Fraction(sum(B[i][i] for i in range(m)), k)
        cs.append(c)
        for i in range(m):
            B[i][i] += c
    return cs  # t^m + cs[1] t^{m-1} + ... + cs[m]

def solve_pencil(M, S):
    """eigvals of S^{-1} M exactly via charpoly; returns (coeffs, floats)."""
    m = len(M)
    # X = S^{-1} M  column by column
    X = []
    for j in range(m):
        col = solve_linear([row[:] for row in S], [M[i][j] for i in range(m)])
        X.append(col)
    A = [[X[j][i] for j in range(m)] for i in range(m)]
    cs = charpoly(A)
    import numpy as np
    ev = np.roots([float(c) for c in cs])
    return cs, sorted([complex(e).real for e in ev], reverse=True)

def main_n2():
    n = 2
    cs = CosetSpace(n)
    orb_list, seen = cs.orbits()
    # decoded optimal multipliers (certified in mdh_certify)
    sig2mult = {
        ((2, 0), (2, 0), 2): Fraction(-6222974327480006, 10**16),
        ((1, 1), (1, 1), 2): Fraction(-16551777520253916, 10**16),
        ((1, 1), (1, 0), 3): Fraction(-44369174251937746, 10**18),
        ((2, 0), (0, 0), 4): Fraction(929464242066791, 10**16),
        ((1, 1), (0, 0), 4): Fraction(7906805246000921, 10**17),
    }
    tvals = []
    for i, orb in enumerate(orb_list):
        l0 = sorted(orb)[0]
        avals = tuple(sorted((sum(1 for v in l0 if v < n),
                              sum(1 for v in l0 if v >= n)), reverse=True))
        best = None
        for l in orb:
            a1 = sum(1 for j in range(n) if l[j] == j)
            a2 = sum(1 for j in range(n) if l[j] == n + j)
            key = tuple(sorted((a1, a2), reverse=True))
            if best is None or key > best: best = key
        diff = 2 * n - cs.phi(sorted(orb)[0])
        tvals.append(sig2mult[(avals, best, diff)] /
                     (math.factorial(n) * len(orb)))
    print("t:", [float(t) for t in tvals])
    for lam in partitions(2 * n):
        ld = LambdaData(lam, n, cs)
        if ld.dV == 0: continue
        se = SigmaEngine(n, lam, cs)
        for mu in partitions(n):
            for nu in partitions(n):
                M, S, cols = se.class_sigma2(mu, nu, tvals)
                if not cols: continue
                cs_poly, ev = solve_pencil(M, S)
                sig = [math.sqrt(max(e, 0)) for e in ev]
                print(f"lam={lam} mu={mu} nu={nu}: sigma={['%.7f' % s for s in sig]}"
                      f"  charpoly={[str(c) for c in cs_poly]}")

def sweep(n, tvals, cs=None, float_only=True):
    """Pencil sigma for every class; returns dict class -> sorted sigma list."""
    cs = cs or CosetSpace(n)
    out = {}
    for lam in partitions(2 * n):
        ld = LambdaData(lam, n, cs)
        if ld.dV == 0: continue
        se = SigmaEngine(n, lam, cs)
        for mu in partitions(n):
            for nu in partitions(n):
                M, S, cols = se.class_sigma2(mu, nu, tvals)
                if not cols: continue
                _, ev = solve_pencil(M, S)
                out[(lam, mu, nu)] = [math.sqrt(max(e, 0)) for e in ev]
    return out

def main_random_n(n, seed=1):
    import random, numpy as np
    from mdh_certify import build_gamma, check_invariance
    rng = random.Random(seed)
    cs = CosetSpace(n)
    orb_list, seen = cs.orbits()
    tvals = [Fraction(rng.randint(-9, 9), rng.randint(1, 7)) for _ in orb_list]
    Gm, YE, NO = build_gamma([float(t) for t in tvals], dict(seen), n)
    sv = np.linalg.svd(Gm, compute_uv=False)
    groups = []
    for v in sv:
        if groups and abs(groups[-1][0] - v) < 1e-7 * max(1, v): groups[-1][1] += 1
        else: groups.append([v, 1])
    print("brute-force SVD groups:", [(round(v, 6), m) for v, m in groups])
    res = sweep(n, tvals, cs)
    print("pencil sigma per class (expect EXACT match, no constants):")
    nbad = 0
    for k, sigs in sorted(res.items()):
        for s in sigs:
            if s < 1e-9: continue
            ok = any(abs(v - s) < 1e-6 * max(1, v) for v, m in groups)
            if not ok: nbad += 1
            print(f"  {k}: {s:.7f} {'OK' if ok else 'MISSING'}")
    print("mismatches:", nbad)

def main_n3_opt():
    """Assignment search of blocks_n3 multipliers onto my orbits; exact pencil."""
    import itertools as it, json, ast
    n = 3
    d = json.load(open(PROJECT / "artifacts" / "blocks_n3.json", encoding="utf-8"))
    theirs = [(Fraction(v[0]).limit_denominator(10**13), int(v[1]), v[2])
              for k, v in sorted(d["orbmeta"].items(), key=lambda kv: int(kv[0]))]
    known = sorted((r["sigma"] for r in d["records"]), reverse=True)
    cs = CosetSpace(n)
    orb_list, seen = cs.orbits()
    def my_key(orb):
        l0 = sorted(orb)[0]
        avals = tuple(sorted((sum(1 for v in l0 if v < n),
                              sum(1 for v in l0 if v >= n)), reverse=True))
        best = None
        for l in orb:
            a1 = sum(1 for j in range(n) if l[j] == j)
            a2 = sum(1 for j in range(n) if l[j] == n + j)
            key = tuple(sorted((a1, a2), reverse=True))
            if best is None or key > best: best = key
        return (len(orb), 2 * n - cs.phi(sorted(orb)[0]), avals, best)
    from collections import defaultdict
    g_mine, g_theirs = defaultdict(list), defaultdict(list)
    for i, o in enumerate(orb_list): g_mine[my_key(o)].append(i)
    for j, (mult, ps, sig) in enumerate(theirs):
        s = ast.literal_eval(sig)
        tsize = ps // (math.factorial(2 * n) * math.factorial(n))
        g_theirs[(tsize, s[4], tuple(sorted(s[:2], reverse=True)),
                  tuple(sorted(s[2:4], reverse=True)))].append(j)
    assert set(g_mine) == set(g_theirs), set(g_mine) ^ set(g_theirs)
    keys = list(g_mine)
    print("tie groups:", {k: len(v) for k, v in g_mine.items() if len(v) > 1})
    best = None
    for combo in it.product(*[list(it.permutations(g_theirs[k])) for k in keys]):
        tv = [None] * len(orb_list)
        for k, pm in zip(keys, combo):
            for mi, tj in zip(g_mine[k], pm):
                mult, ps, sig = theirs[tj]
                tsize = ps // (math.factorial(2 * n) * math.factorial(n))
                tv[mi] = mult / (math.factorial(n) * tsize)
        res = sweep(n, tv, cs)
        sigs = []
        for k2, ss in res.items():
            lam, mu, nu = k2
            for s in ss:
                if s > 1e-7:
                    # coupled classes appear in both orientations; count once
                    if mu > nu: continue
                    sigs.append(s)
        sigs = sorted(sigs, reverse=True)
        err = 999.0
        if len(sigs) >= len(known):
            err = max(abs(a - b) for a, b in zip(sigs[:len(known)], known))
        if best is None or err < best[0]:
            best = (err, combo, sigs)
    err, combo, sigs = best
    print(f"best assignment error {err:.2e}")
    print("pencil:", [round(s, 6) for s in sigs])
    print("known :", [round(s, 6) for s in known])
    s0 = sigs[0]; s1 = sigs[1]
    print(f"LAW-1: (2n-1)s0-(2n-2)s1 = {5*s0-4*s1:.6f} (target {2*n})")

if __name__ == "__main__":
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("mode", nargs="?", default="n2")
    ap.add_argument("--n", type=int, default=3)
    ap.add_argument("--seed", type=int, default=1)
    a = ap.parse_args()
    if a.mode == "n2": main_n2()
    elif a.mode == "random": main_random_n(a.n, a.seed)
    elif a.mode == "n3opt": main_n3_opt()
