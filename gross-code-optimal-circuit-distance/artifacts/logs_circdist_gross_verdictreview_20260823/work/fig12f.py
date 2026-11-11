"""Figure-12 reading with the ancilla STRADDLE made explicit.

The figure labels CNOTs by their time step within one round window.  [SBB26]'s LRC staggers the Z
ancilla so that its window crosses the round boundary ("the Z ancilla is prepared at time step
t1+3 and measured at time step t1+2"): the two half-blocks a Z ancilla instance performs are the
LATER block of one round window and the EARLIER block of the NEXT round window.  So for a straddled
check type the true within-instance order is (later block) then (earlier block + one period), which
is NOT what the drawing reads off left-to-right.  Both possibilities are tried for each panel.
"""
import itertools, json
import numpy as np
from gross import NG, N, xcheck_nb, zcheck_nb
from sched import make_phi, colour_valid
from cascade import CLS_OF, collect_rules, survivors
from fig12 import XPANEL, ZPANEL, COLS
from fig12e import (XSLOT, ZSLOT, XQ, ZQ, SHARED, XWHITE, XBLACK, ZWHITE, ZBLACK, maps)

def options(panel, white, black, white_is_left, straddle, P):
    out = []
    for m in maps(white, black, white_is_left):
        T = {}
        for col in COLS:
            t = [None] * 6
            for e, tt in panel[col].items():
                t[m[e]] = tt
            if straddle:
                wl = [t[m[e]] for e in white]; bl = [t[m[e]] for e in black]
                # the block drawn LATER in the round is the instance's first block;
                # the earlier-drawn block belongs to the next round window.
                if sum(wl) / 3 < sum(bl) / 3:
                    for e in white: t[m[e]] += P
                else:
                    for e in black: t[m[e]] += P
            T[col] = t
        for perm in itertools.permutations(range(3)):
            out.append((m, perm, {c: T[COLS[perm[c]]] for c in range(3)}))
    return out

def masks(TT, SL, QQ, PHI, P):
    mk = np.zeros(N, np.int64)
    for g in range(NG):
        tt = TT[PHI[g]]
        if len({x % P for x in tt}) != 6:
            return None
        for k in range(6):
            q = QQ[g][k]; t = tt[SL[g][k]] % P
            if mk[q] >> t & 1:
                return None
            mk[q] |= 1 << t
    return mk

def triples(TT):
    return tuple(CLS_OF[tuple(sorted(range(6), key=lambda s: TT[c][s]))] for c in range(3))

def mc_bad(TTX, TTZ, PHI, P):
    bad = 0
    for (a, b, sh) in SHARED:
        ca = PHI[a]; cb = PHI[b]
        for dp in (-3, -2, -1, 0, 1, 2, 3):
            c = sum(1 for (k, l) in sh
                    if TTZ[cb][ZSLOT[b][l]] + P * dp < TTX[ca][XSLOT[a][k]])
            if c % 2:
                bad += 1
    return bad

results = []
for P in (6, 7, 8):
 for stX in (False, True):
  for stZ in (False, True):
   for wl in (True, False):
    for (upper, lower, tag) in ((XPANEL, ZPANEL, 'upper=X'), (ZPANEL, XPANEL, 'upper=Z')):
        uw, ub, us = ((XWHITE, XBLACK, stX) if tag == 'upper=X' else (ZWHITE, ZBLACK, stZ))
        lw, lb, ls = ((ZWHITE, ZBLACK, stZ) if tag == 'upper=X' else (XWHITE, XBLACK, stX))
        XO = options(upper, uw, ub, wl, us, P); ZO = options(lower, lw, lb, wl, ls, P)
        for (s, t) in [(1, 1), (1, 2), (2, 1), (2, 2)]:
            phi = make_phi(s, t)
            PHI = [int(phi[g]) for g in range(NG)]
            SURV = {}
            for sector in ('X', 'Z'):
                r1, r2 = collect_rules(sector, phi)
                alive, _, _ = survivors(r1, r2)
                SURV[sector] = {tuple(int(x) for x in v) for v in np.argwhere(alive)}
            XV = [(m, pm, TT, masks(TT, XSLOT, XQ, PHI, P)) for (m, pm, TT) in XO]
            XV = [v for v in XV if v[3] is not None]
            ZV = [(m, pm, TT, masks(TT, ZSLOT, ZQ, PHI, P)) for (m, pm, TT) in ZO]
            ZV = [v for v in ZV if v[3] is not None]
            good = []; nsurv = 0
            for (mx, px, TTX, kx) in XV:
                tx = triples(TTX)
                for (mz, pz, TTZ, kz) in ZV:
                    tz = triples(TTZ)
                    for d in range(P):
                        kzd = ((kz << d) | (kz >> (P - d))) & ((1 << P) - 1) if d else kz
                        if (kx & kzd).any():
                            continue
                        if tx not in SURV['X'] or tz not in SURV['Z']:
                            continue
                        nsurv += 1
                        TTZd = {c: [x + d for x in TTZ[c]] for c in TTZ}
                        if mc_bad(TTX, TTZd, PHI, P) == 0:
                            good.append((d, mx, px, tx, mz, pz, tz))
            if good:
                print(f"P={P} straddleX={stX} straddleZ={stZ} white={'LEFT' if wl else 'RIGHT'} "
                      f"{tag} phi={s}a+{t}b : surviving-both {nsurv}, (MC)-clean {len(good)}")
                for row in good:
                    print(f"      delta={row[0]}  X-triple {row[3]}  Z-triple {row[6]}")
                    results.append(dict(P=P, stX=stX, stZ=stZ, white_left=wl, tag=tag, phi=[s, t],
                                        delta=row[0], xedge=row[1], colX=list(row[2]),
                                        Xtriple=list(row[3]), zedge=row[4], colZ=list(row[5]),
                                        Ztriple=list(row[6])))
json.dump(results, open("fig12_reading2.json", "w"), indent=1)
print("\nTOTAL legal + (MC)-clean + cascade-surviving readings:", len(results))
