"""LEMMA D in action.

LEMMA D (proposer level, proof by inspection of the frozen model).  E(M) = {suffixes of the hook
checks' CNOT ORDERS} u {singletons} u {empty}; every extended-code column is a function of the 72
within-check ORDERS alone.  Hence d_eff = d_ext(E(M)) is INVARIANT under any re-timing that
preserves the within-check orders -- interleaving included.  (MC), legality and `repair` are NOT.

Consequence for the hunt: the expensive half of a D* = 12 witness (certifying d_eff = 11 in both
sectors) can be INHERITED.  The campaign already spent ~160 CPU-hours certifying d_ext = 11 for
M_cand's order classes.  Any legal + (MC) + INTERLEAVED re-timing of those same orders starts with
d_eff = 11 already certified, and only the repair side remains open.

This script searches the 36-slot three-colour-tiled time family for such a re-timing.
"""
import itertools, random, sys, time
import core2 as C
from orderlib import orders_from_slotorders

CLS = {0: (0, 1, 2, 3, 4, 5), 1: (0, 1, 2, 4, 3, 5), 2: (0, 1, 2, 5, 3, 4),
       14: (0, 2, 1, 5, 3, 4), 62: (1, 2, 0, 5, 3, 4)}
TRZ = tuple(int(x) for x in sys.argv[1].split(',')) if len(sys.argv) > 1 else (1, 62, 2)
TRX = tuple(int(x) for x in sys.argv[2].split(',')) if len(sys.argv) > 2 else (14, 2, 0)
NTRY = int(sys.argv[3]) if len(sys.argv) > 3 else 300000
soZ = {c: CLS[TRZ[c]] for c in range(3)}
soX = {c: CLS[TRX[c]] for c in range(3)}
oZ = orders_from_slotorders(soZ, 'Z')
oX = orders_from_slotorders(soX, 'X')

# ---- the tiled time vector: index 3c+i = XL[c][i], 9+3c+j = XR[c][j],
#                             18+3c+j = ZL[c][j], 27+3c+i = ZR[c][i]
def iXL(c, i): return 3 * c + i
def iXR(c, j): return 9 + 3 * c + j
def iZL(c, j): return 18 + 3 * c + j
def iZR(c, i): return 27 + 3 * c + i


# ---- (MC) reduced to its distinct slot-level constraints (translation invariance)
def mc_constraints():
    cons = set()
    for (a, b, sh) in C.OV:
        ca, cb = C.cls(a), C.cls(b)
        pairs = []
        for q in sh:
            ia = C.Xslots[a].index(q)
            ib = C.Zslots[b].index(q)
            pairs.append((ia, ib))
        pairs.sort()
        assert len(pairs) == 2
        (ia1, ib1), (ia2, ib2) = pairs          # one left qubit (slots 0..2), one right (3..5)
        cons.add((ca, cb, ia1, ib1, ia2, ib2))
    return sorted(cons)


CONS = mc_constraints()


def slot_time(t, kind, c, s):
    """kind 'X' : slot s of an X-check of colour c ; 'Z' likewise."""
    if kind == 'X':
        return t[iXL(c, s)] if s < 3 else t[iXR(c, s - 3)]
    return t[iZL(c, s)] if s < 3 else t[iZR(c, s - 3)]


def mc_ok(t):
    for (ca, cb, ia1, ib1, ia2, ib2) in CONS:
        p = slot_time(t, 'Z', cb, ib1) < slot_time(t, 'X', ca, ia1)
        q = slot_time(t, 'Z', cb, ib2) < slot_time(t, 'X', ca, ia2)
        if p != q:
            return False
    return True


# ---- chains: the 6 within-check orders, expressed as ordered lists of time-vector indices
CHAINS = []
for c in range(3):
    CHAINS.append([(iXL(c, s) if s < 3 else iXR(c, s - 3)) for s in soX[c]])
    CHAINS.append([(iZL(c, s) if s < 3 else iZR(c, s - 3)) for s in soZ[c]])


def random_linext(rng):
    """uniform-ish random interleaving of the 6 chains -> a time vector t (a permutation)."""
    pos = [0] * 6
    t = [0] * 36
    for step in range(36):
        live = [k for k in range(6) if pos[k] < 6]
        k = rng.choice(live)
        t[CHAINS[k][pos[k]]] = step
        pos[k] += 1
    return t


def build(t):
    XL = [[t[iXL(c, i)] for i in range(3)] for c in range(3)]
    XR = [[t[iXR(c, j)] for j in range(3)] for c in range(3)]
    ZL = [[t[iZL(c, j)] for j in range(3)] for c in range(3)]
    ZR = [[t[iZR(c, i)] for i in range(3)] for c in range(3)]
    tX, tZ = {}, {}
    for g in range(C.NG):
        c = C.cls(g)
        for i, m in enumerate(C.Amon):
            tX[(g, C.gadd(g, m))] = XL[c][i]
        for j, m in enumerate(C.Bmon):
            tX[(g, C.NG + C.gadd(g, m))] = XR[c][j]
        for j, m in enumerate(C.Bmon):
            tZ[(C.gadd(g, (-m[0], -m[1])), g)] = ZL[c][j]
        for i, m in enumerate(C.Amon):
            tZ[(C.NG + C.gadd(g, (-m[0], -m[1])), g)] = ZR[c][i]
    return tX, tZ


if __name__ == '__main__':
    rng = random.Random(20260823)
    t0 = time.time()
    nmc = 0
    best = None
    seen = set()
    for it in range(NTRY):
        t = random_linext(rng)
        if not mc_ok(t):
            continue
        nmc += 1
        tX, tZ = build(t)
        assert C.legal(tX, tZ)
        assert not C.mc_violations(tX, tZ)
        for g in range(C.NG):
            assert sorted(C.Xchk[g], key=lambda q: tX[(g, q)]) == oX[g]
            assert sorted(C.Zchk[g], key=lambda q: tZ[(q, g)]) == oZ[g]
        pi, si, gint = C.interleave_stats(tX, tZ)
        key = (pi, si, gint)
        if best is None or (gint, pi) > (best[0][2], best[0][0]):
            best = ((pi, si, gint), list(t))
        seen.add(key)
    print("Z-triple %s  X-triple %s   random linear extensions tried %d   legal+(MC) hits %d (%.2f%%)"
          "   %.1fs" % (TRZ, TRX, NTRY, nmc, 100.0 * nmc / NTRY, time.time() - t0))
    print("distinct (overlap-interleaved pairs, whole-check-interleaved pairs, globally interleaved)"
          " profiles among the hits:")
    for k in sorted(seen):
        print("   ", k)
    if best:
        (pi, si, gint), t = best
        print("BEST: overlap-interleaved %d/648, whole-check-interleaved %d/648, globally interleaved %s"
              % (pi, si, gint))
        print("  time vector =", t)
        print("  -> by LEMMA D this schedule has the SAME d_eff as M_cand, i.e. d_eff = 11 in both")
        print("     sectors, INHERITED from the campaign's 990-slot certification.")
