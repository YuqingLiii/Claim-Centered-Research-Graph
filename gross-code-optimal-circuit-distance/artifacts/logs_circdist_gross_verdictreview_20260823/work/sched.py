"""Schedules for the gross code: explicit legality + measurement-consistency (MC) checks,
plus the symbolic 3-colour-tiled parameterisation and its enumeration.

A schedule is given as two arrays
    LX[c, s, i]  = CNOT layer of the X-check of colour c, side s in {0=L,1=R}, monomial index i
    LZ[c, s, i]  = CNOT layer of the Z-check of colour c, side s in {0=L,1=R}, monomial index i
where for X-checks side L uses A-monomials and side R uses B-monomials, and for Z-checks side L
uses B-monomials and side R uses A-monomials (gross.xcheck_nb / zcheck_nb).

Colouring: phi(x^a y^b) = (s*a + t*b) mod 3 with s,t in {1,2}; these are exactly the 4 group
homomorphisms G -> Z_3 that properly 3-colour both check-conflict graphs.
"""
import numpy as np, itertools
from gross import (ELL, EM, NG, N, gidx, gsum, A_MONOS, B_MONOS, HX, HZ,
                   xcheck_nb, zcheck_nb, xchecks_of, zchecks_of)


def make_phi(s, t):
    ph = np.empty(NG, int)
    for i in range(ELL):
        for j in range(EM):
            ph[gidx(i, j)] = (s * i + t * j) % 3
    return ph


def colour_valid(phi):
    """phi must give distinct colours to any two same-type checks sharing a data qubit."""
    for g in range(NG):
        cs = [phi[gsum(g, m)] for m in A_MONOS]        # X-checks on left qubit g
        if len(set(cs)) != 3:
            return False
        cs = [phi[gsum(g, m)] for m in B_MONOS]        # X-checks on right qubit g
        if len(set(cs)) != 3:
            return False
        cs = [phi[gsum(g, (-m[0], -m[1]))] for m in B_MONOS]   # Z-checks on left qubit g
        if len(set(cs)) != 3:
            return False
        cs = [phi[gsum(g, (-m[0], -m[1]))] for m in A_MONOS]   # Z-checks on right qubit g
        if len(set(cs)) != 3:
            return False
    return True


# ---------------- explicit schedule expansion ----------------
def expand(phi, LX, LZ):
    """Return tX[g][(side,i)] and tZ[g][(side,i)] : explicit CNOT times for every check."""
    tX = [None] * NG; tZ = [None] * NG
    for g in range(NG):
        c = phi[g]
        tX[g] = {('L', i): int(LX[c, 0, i]) for i in range(3)}
        tX[g].update({('R', i): int(LX[c, 1, i]) for i in range(3)})
        tZ[g] = {('L', i): int(LZ[c, 0, i]) for i in range(3)}
        tZ[g].update({('R', i): int(LZ[c, 1, i]) for i in range(3)})
    return tX, tZ


def check_legal(tX, tZ, depth):
    """every check uses 6 distinct layers; every data qubit uses 6 distinct layers."""
    for g in range(NG):
        if len(set(tX[g].values())) != 6 or len(set(tZ[g].values())) != 6:
            return False
        if max(tX[g].values()) > depth or max(tZ[g].values()) > depth:
            return False
    for q in range(N):
        ts = [tX[c][(s, i)] for (c, s, i) in xchecks_of(q)] + \
             [tZ[c][(s, i)] for (c, s, i) in zchecks_of(q)]
        if len(set(ts)) != 6:
            return False
    return True


def mc_violations(tX, tZ):
    """(MC): for every X-check a and Z-check b,
       #{ q in supp(a)&supp(b) : t(q->b) < t(a->q) } must be even."""
    xnb = [xcheck_nb(g) for g in range(NG)]
    znb = [zcheck_nb(g) for g in range(NG)]
    xmap = [{q: (s, i) for q, s, i in xnb[g]} for g in range(NG)]
    zmap = [{q: (s, i) for q, s, i in znb[g]} for g in range(NG)]
    bad = 0; tot = 0
    for a in range(NG):
        for b in range(NG):
            shared = set(xmap[a]) & set(zmap[b])
            if not shared:
                continue
            tot += 1
            cnt = 0
            for q in shared:
                if tZ[b][zmap[b][q]] < tX[a][xmap[a][q]]:
                    cnt += 1
            if cnt % 2:
                bad += 1
    return bad, tot


def sbb_noninterleaved(tX, tZ):
    """SBB non-interleaving, per overlapping (X-check, Z-check) pair:
       either all of a's CNOTs on the overlap precede all of b's on the overlap, or vice versa."""
    xmap = [{q: (s, i) for q, s, i in xcheck_nb(g)} for g in range(NG)]
    zmap = [{q: (s, i) for q, s, i in zcheck_nb(g)} for g in range(NG)]
    bad = 0
    for a in range(NG):
        for b in range(NG):
            shared = set(xmap[a]) & set(zmap[b])
            if not shared:
                continue
            ta = [tX[a][xmap[a][q]] for q in shared]
            tb = [tZ[b][zmap[b][q]] for q in shared]
            if not (max(ta) < min(tb) or max(tb) < min(ta)):
                bad += 1
    return bad


def global_noninterleaved(tX, tZ):
    """the strong (in-house Def 2.4) version: all X-CNOTs before all Z-CNOTs, or vice versa."""
    xs = [v for g in range(NG) for v in tX[g].values()]
    zs = [v for g in range(NG) for v in tZ[g].values()]
    return max(xs) < min(zs) or max(zs) < min(xs)


# ---------------- within-check CNOT orders / residual sets ----------------
def check_orders(phi, LX, LZ):
    """orderX[g] = list of the 6 data qubits of X-check g in CNOT order; same for Z."""
    tX, tZ = expand(phi, LX, LZ)
    oX = []; oZ = []
    for g in range(NG):
        nb = xcheck_nb(g)
        oX.append([q for q, s, i in sorted(nb, key=lambda z: tX[g][(z[1], z[2])])])
        nb = zcheck_nb(g)
        oZ.append([q for q, s, i in sorted(nb, key=lambda z: tZ[g][(z[1], z[2])])])
    return oX, oZ


def residuals_from_order(order):
    """SBB residual errors of one weight-6 check measured in CNOT order i1..i6, reduced modulo
    the check itself and with the weight-<=1 ones dropped (they duplicate data columns):
        {i1,i2} , {i4,i5,i6} , {i5,i6}."""
    i1, i2, i3, i4, i5, i6 = order
    return [(i1, i2), (i4, i5, i6), (i5, i6)]


def full_suffix_residuals(order):
    """all six suffixes S_l = {i_l,...,i_6}, l = 1..6 (the raw hook errors)."""
    return [tuple(order[l:]) for l in range(6)]
