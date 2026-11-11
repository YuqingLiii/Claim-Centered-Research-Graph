"""STAGGERED left-right circuits (LRCs) for the gross code, 6 CNOT layers per period.

Structure (SBB Fig. 3, with the staggering that makes the Z-ancilla window straddle the period
boundary):
    block A = layers 0,1,2 of a period :  L_X  (X-checks on LEFT data)  ||  R_Z (Z on RIGHT data)
    block B = layers 3,4,5 of a period :  R_X  (X-checks on RIGHT data) ||  L_Z (Z on LEFT data)
X-ancilla instance p : L_X in block A of period p, R_X in block B of period p.
Z-ancilla instance p : L_Z in block B of period p, R_Z in block A of period p+1.
So both check types run one contiguous LEFT block then one contiguous RIGHT block, and the Z
window straddles the boundary.  A 3-colour-tiled LRC lets the within-block layer depend on the
check's colour phi(g).

Free parameters (per colour c, per monomial index i, each row a bijection {0,1,2}->{0,1,2}):
    LXL[c][i] layer-in-block-A of X-check colour c, LEFT  qubit via A_i
    LXR[c][i] layer-in-block-B of X-check colour c, RIGHT qubit via B_i
    LZL[c][i] layer-in-block-B of Z-check colour c, LEFT  qubit via B_i
    LZR[c][i] layer-in-block-A of Z-check colour c, RIGHT qubit via A_i
"""
import numpy as np, itertools, json, sys
from gross import (NG, N, ELL, EM, gidx, gsum, A_MONOS, B_MONOS, HX, HZ,
                   xcheck_nb, zcheck_nb)
from sched import make_phi, colour_valid
from cascade import CLS_OF

BIJ = list(itertools.permutations(range(3)))          # 6 bijections i -> layer


def colours_of_monos(phi):
    al = [int(phi[gsum(0, m)]) for m in A_MONOS]       # phi(A_i)
    be = [int(phi[gsum(0, m)]) for m in B_MONOS]       # phi(B_i)
    return al, be


def ok_rows(phi, sign, mono_cols):
    """All (row_0,row_1,row_2) triples of bijections such that for every v in {0,1,2},
    i -> row[(v + sign*mono_cols[i]) % 3][i] is a bijection.  This is exactly the perfect-matching
    condition for the corresponding block/half."""
    out = []
    for rows in itertools.product(BIJ, repeat=3):
        good = True
        for v in range(3):
            vals = [rows[(v + sign * mono_cols[i]) % 3][i] for i in range(3)]
            if len(set(vals)) != 3:
                good = False; break
        if good:
            out.append(rows)
    return out


def x_triple(LXL, LXR):
    """within-check order class per colour, X sector (slots 0,1,2 = A monomials/left)."""
    tr = []
    for c in range(3):
        left = sorted(range(3), key=lambda i: LXL[c][i])
        right = sorted(range(3), key=lambda i: LXR[c][i])
        tr.append(CLS_OF[tuple(left) + tuple(3 + j for j in right)])
    return tuple(tr)


def z_triple(LZL, LZR):
    """Z sector (slots 0,1,2 = B monomials/left, 3,4,5 = A monomials/right)."""
    tr = []
    for c in range(3):
        left = sorted(range(3), key=lambda i: LZL[c][i])
        right = sorted(range(3), key=lambda i: LZR[c][i])
        tr.append(CLS_OF[tuple(left) + tuple(3 + j for j in right)])
    return tuple(tr)


# ---------------- explicit absolute times, legality and (MC) ----------------
P = 6      # CNOT layers per period


def times(phi, LXL, LXR, LZL, LZR, p):
    """absolute CNOT times.  tX[(g,'L',i)] etc. for X-instance p and Z-instance p."""
    tX, tZ = {}, {}
    for g in range(NG):
        c = int(phi[g])
        for i in range(3):
            tX[(g, 'L', i)] = P * p + LXL[c][i]
            tX[(g, 'R', i)] = P * p + 3 + LXR[c][i]
            tZ[(g, 'L', i)] = P * p + 3 + LZL[c][i]
            tZ[(g, 'R', i)] = P * (p + 1) + LZR[c][i]
    return tX, tZ


def legality(phi, LXL, LXR, LZL, LZR):
    """explicit check that every absolute layer is a matching on the 288 qubits, over 4 periods."""
    busy = {}
    for p in range(4):
        tX, tZ = times(phi, LXL, LXR, LZL, LZR, p)
        for g in range(NG):
            xa, za = N + g, N + NG + g
            for q, s, i in xcheck_nb(g):
                t = tX[(g, s, i)]
                for qq in (q, xa):
                    if (t, qq) in busy:
                        return False
                    busy[(t, qq)] = 1
            for q, s, i in zcheck_nb(g):
                t = tZ[(g, s, i)]
                for qq in (q, za):
                    if (t, qq) in busy:
                        return False
                    busy[(t, qq)] = 1
    return True


def mc_violations(phi, LXL, LXR, LZL, LZR, dp_range=(-2, -1, 0, 1, 2)):
    """(MC): for every overlapping X-check instance a and Z-check instance b,
    #{ q in supp(a) cap supp(b) : t(q->b) < t(a->q) } must be even."""
    tot = 0; bad = 0; per_dp = {}
    for dp in dp_range:
        tXa, _ = times(phi, LXL, LXR, LZL, LZR, 2)
        _, tZb = times(phi, LXL, LXR, LZL, LZR, 2 + dp)
        nb = 0
        for a in range(NG):
            xs = {q: (s, i) for q, s, i in xcheck_nb(a)}
            for b in range(NG):
                zs = {q: (s, i) for q, s, i in zcheck_nb(b)}
                sh = set(xs) & set(zs)
                if not sh:
                    continue
                tot += 1
                c = 0
                for q in sh:
                    s, i = xs[q]; s2, i2 = zs[q]
                    if tZb[(b, s2, i2)] < tXa[(a, s, i)]:
                        c += 1
                if c % 2:
                    bad += 1; nb += 1
        per_dp[dp] = nb
    return tot, bad, per_dp


def overlap_structure():
    """check the 'one left, one right, index pair swapped' fact used in the parity argument."""
    halves = set(); swapped = 0; pairs = 0
    for a in range(NG):
        xs = {q: (s, i) for q, s, i in xcheck_nb(a)}
        for b in range(NG):
            zs = {q: (s, i) for q, s, i in zcheck_nb(b)}
            sh = sorted(set(xs) & set(zs))
            if not sh:
                continue
            pairs += 1
            halves.add(tuple(sorted(xs[q][0] for q in sh)))
            L = [q for q in sh if xs[q][0] == 'L'][0]
            R = [q for q in sh if xs[q][0] == 'R'][0]
            # X uses A_i on the left qubit and B_j on the right; Z uses B_j' on the left and A_i'
            # on the right.  claim: i == i' and j == j'
            if xs[L][1] == zs[R][1] and xs[R][1] == zs[L][1]:
                swapped += 1
    return pairs, sorted(halves), swapped


if __name__ == "__main__":
    s, t = (int(sys.argv[1]), int(sys.argv[2])) if len(sys.argv) > 2 else (1, 1)
    phi = make_phi(s, t); assert colour_valid(phi)
    al, be = colours_of_monos(phi)
    print(f"phi = {s}a+{t}b   phi(A_i) = {al}   phi(B_i) = {be}")
    pairs, halves, swapped = overlap_structure()
    print(f"overlapping (X,Z) check pairs: {pairs}; shared-qubit halves: {halves}; "
          f"index-pair-swapped: {swapped}/{pairs}")

    XL = ok_rows(phi, +1, al)      # block A, left  (X on left, checks g+A_i)
    ZR = ok_rows(phi, -1, al)      # block A, right (Z on right, checks g-A_i)
    XR = ok_rows(phi, +1, be)      # block B, right (X on right, checks g+B_i)
    ZL = ok_rows(phi, -1, be)      # block B, left  (Z on left, checks g-B_i)
    print(f"legal within-block layer patterns: |LXL|={len(XL)} |LXR|={len(XR)} "
          f"|LZL|={len(ZL)} |LZR|={len(ZR)}  -> {len(XL)*len(XR)*len(ZL)*len(ZR)} tiled LRCs")

    xt = sorted({x_triple(a, b) for a in XL for b in XR})
    zt = sorted({z_triple(a, b) for a in ZL for b in ZR})
    print(f"realisable X-sector order-class triples: {len(xt)}")
    print(f"realisable Z-sector order-class triples: {len(zt)}")
    json.dump(dict(x=[list(v) for v in xt], z=[list(v) for v in zt]),
              open(f"lrc_triples_{s}{t}.json", "w"))

    # legality + (MC) on a random sample of full schedules
    rng = np.random.default_rng(7)
    nleg = 0; nmc = 0; ns = 40
    for _ in range(ns):
        A1 = XL[rng.integers(len(XL))]; B1 = XR[rng.integers(len(XR))]
        A2 = ZL[rng.integers(len(ZL))]; B2 = ZR[rng.integers(len(ZR))]
        nleg += legality(phi, A1, B1, A2, B2)
        tot, bad, per = mc_violations(phi, A1, B1, A2, B2)
        nmc += (bad == 0)
    print(f"random sample of {ns} tiled staggered LRCs: legal {nleg}/{ns}, "
          f"(MC)-clean {nmc}/{ns}")
    A1, B1, A2, B2 = XL[0], XR[0], ZL[0], ZR[0]
    tot, bad, per = mc_violations(phi, A1, B1, A2, B2)
    print(f"   one example: {tot} (X-instance, Z-instance) overlapping pairs examined, "
          f"{bad} odd; per period offset: {per}")
    print("   its (Z,X) class triples:", z_triple(A2, B2), x_triple(A1, B1))
