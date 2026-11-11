"""Figure-12 reading, done properly.

Period.  [SBB26] Eq. (3): t >= max(c(H_XZ), r(H_XZ)+2) = max(6,8) = 8 for the gross code, and their
LRC saturates it, so the SEC's PERIOD is 8 time steps, of which each check uses 6 for CNOTs (the
other two carry its ancilla preparation and measurement).  Legality is therefore "the 6 CNOT times
of a data qubit are distinct mod 8", not mod 6.

Panel consistency.  Circles are drawn black/white; three of each around every check, the same
pattern in Figures 11 and 12 and in both panels -- so the two circle colours are the two data
sublattices (left/right halves).  For X-checks the white set is {2 vertical, 1 long diagonal} and
for Z-checks {2 horizontal, 1 long diagonal}; the X-check's LEFT neighbours are the A monomials
{y, y^2, x^3} (two y-shifts and one long x-shift) and the Z-check's LEFT neighbours are the B
monomials {x, x^2, y^3}, so WHITE = LEFT half in both panels.  Both possible half assignments are
tried anyway.
"""
import itertools, json, sys
import numpy as np
from gross import NG, N, xcheck_nb, zcheck_nb
from sched import make_phi, colour_valid
from cascade import CLS_OF, collect_rules, survivors
from fig12 import XPANEL, ZPANEL, COLS

XSLOT = [[(0 if s == 'L' else 3) + i for (q, s, i) in xcheck_nb(g)] for g in range(NG)]
ZSLOT = [[(0 if s == 'L' else 3) + i for (q, s, i) in zcheck_nb(g)] for g in range(NG)]
XQ = [[q for (q, s, i) in xcheck_nb(g)] for g in range(NG)]
ZQ = [[q for (q, s, i) in zcheck_nb(g)] for g in range(NG)]
SHARED = []
for a in range(NG):
    for b in range(NG):
        sh = [(k, ZQ[b].index(XQ[a][k])) for k in range(6) if XQ[a][k] in ZQ[b]]
        if sh:
            SHARED.append((a, b, sh))

XWHITE = ['e2','e5','e6']; XBLACK = ['e1','e3','e4']
ZWHITE = ['e3','e4','e6']; ZBLACK = ['e1','e2','e5']

def maps(white, black, white_is_left):
    lo = (0,1,2) if white_is_left else (3,4,5)
    hi = (3,4,5) if white_is_left else (0,1,2)
    for pw in itertools.permutations(lo):
        for pb in itertools.permutations(hi):
            yield dict(zip(white, pw)) | dict(zip(black, pb))

def options(panel, white, black, white_is_left):
    out = []
    for m in maps(white, black, white_is_left):
        T = {}
        for col in COLS:
            t = [None]*6
            for e, tt in panel[col].items():
                t[m[e]] = tt
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
        for dp in (-2,-1,0,1,2):
            c = sum(1 for (k, l) in sh
                    if TTZ[cb][ZSLOT[b][l]] + P*dp < TTX[ca][XSLOT[a][k]])
            if c % 2:
                bad += 1
    return bad

results = []
for P in (6, 7, 8):
  for wl in (True, False):
    for (upper, lower, tag) in ((XPANEL, ZPANEL, 'upper=X'), (ZPANEL, XPANEL, 'upper=Z')):
        uw, ub = (XWHITE, XBLACK) if tag == 'upper=X' else (ZWHITE, ZBLACK)
        lw, lb = (ZWHITE, ZBLACK) if tag == 'upper=X' else (XWHITE, XBLACK)
        XO = options(upper, uw, ub, wl); ZO = options(lower, lw, lb, wl)
        for (s, t) in [(1,1),(1,2),(2,1),(2,2)]:
            phi = make_phi(s, t)
            PHI = [int(phi[g]) for g in range(NG)]
            SURV = {}
            for sector in ('X','Z'):
                r1, r2 = collect_rules(sector, phi)
                alive, _, _ = survivors(r1, r2)
                SURV[sector] = {tuple(int(x) for x in v) for v in np.argwhere(alive)}
            XV = [(m,pm,TT,masks(TT,XSLOT,XQ,PHI,P)) for (m,pm,TT) in XO]
            XV = [v for v in XV if v[3] is not None]
            ZV = [(m,pm,TT,masks(TT,ZSLOT,ZQ,PHI,P)) for (m,pm,TT) in ZO]
            ZV = [v for v in ZV if v[3] is not None]
            nleg=0; nsurv=0; good=[]
            for (mx,px,TTX,kx) in XV:
                tx = triples(TTX)
                for (mz,pz,TTZ,kz) in ZV:
                    tz = triples(TTZ)
                    for d in range(P):
                        kzd = ((kz << d) | (kz >> (P-d))) & ((1<<P)-1) if d else kz
                        if (kx & kzd).any():
                            continue
                        nleg += 1
                        if tx not in SURV['X'] or tz not in SURV['Z']:
                            continue
                        nsurv += 1
                        TTZd = {c: [x+d for x in TTZ[c]] for c in TTZ}
                        if mc_bad(TTX, TTZd, PHI, P) == 0:
                            good.append((d, mx, px, tx, mz, pz, tz))
            if nleg or good:
                print(f"P={P} white={'LEFT' if wl else 'RIGHT'} {tag} phi={s}a+{t}b : "
                      f"legal {nleg}, surviving-both {nsurv}, (MC)-clean {len(good)}")
            for row in good:
                print("      delta=%d  X-triple %s  Z-triple %s" % (row[0], row[3], row[6]))
                print("         xedge", row[1], "colX", row[2], " zedge", row[4], "colZ", row[5])
                results.append(dict(P=P, white_left=wl, tag=tag, phi=[s,t], delta=row[0],
                                    xedge=row[1], colX=list(row[2]), Xtriple=list(row[3]),
                                    zedge=row[4], colZ=list(row[5]), Ztriple=list(row[6])))
json.dump(results, open("fig12_reading.json","w"), indent=1)
print("\nTOTAL fully-consistent readings:", len(results))
