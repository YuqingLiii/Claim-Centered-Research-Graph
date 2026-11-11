"""Decode the CNOT schedule drawn in Figure 12 of arXiv:2603.05481 from the PDF's own vector
coordinates, and test every geometry-consistent reading against the code's legality and (MC).

Recovered from the figure (label positions matched to edge endpoints; see artifact):
  edges of a cell, relative to the check:  e1 (+33.5,+47.9) long diagonal, e2 (0,+21.4) vertical,
  e3 (-27.3,0) horizontal, e4 (+26.7,0) horizontal, e5 (0,-26.6) vertical, e6 (-48,-27.3) long
  diagonal.  White circles = LEFT half, black = RIGHT half (verified: for X-checks the white set is
  {2 vertical, 1 diagonal} = the A monomials {y,y^2,x^3}; for Z-checks the white set is
  {2 horizontal, 1 diagonal} = the B monomials {x,x^2,y^3}).

  X panel (filled squares = X checks), CNOT time per edge:
     blue  : e6=2 e2=3 e5=4 e3=5 e1=6 e4=7
     red   : e5=1 e6=2 e2=3 e1=4 e4=5 e3=6
     green : e5=1 e6=2 e2=3 e3=4 e1=5 e4=6
  Z panel (empty squares = Z checks):
     blue  : e2=2 e1=3 e5=4 e6=5 e3=6 e4=7
     red   : e5=1 e2=2 e1=3 e6=4 e3=5 e4=6
     green : e5=1 e2=2 e1=3 e3=4 e4=5 e6=6
"""
import itertools, json
import numpy as np
from gross import NG, N, gsum, A_MONOS, B_MONOS, xcheck_nb, zcheck_nb, xchecks_of, zchecks_of
from sched import make_phi, colour_valid
from cascade import CLS_OF, REPS

XPANEL = {'blue':  {'e6':2,'e2':3,'e5':4,'e3':5,'e1':6,'e4':7},
          'red':   {'e5':1,'e6':2,'e2':3,'e1':4,'e4':5,'e3':6},
          'green': {'e5':1,'e6':2,'e2':3,'e3':4,'e1':5,'e4':6}}
ZPANEL = {'blue':  {'e2':2,'e1':3,'e5':4,'e6':5,'e3':6,'e4':7},
          'red':   {'e5':1,'e2':2,'e1':3,'e6':4,'e3':5,'e4':6},
          'green': {'e5':1,'e2':2,'e1':3,'e3':4,'e4':5,'e6':6}}
COLS = ['blue', 'red', 'green']

# slot conventions of gross.py:
#   X slots 0,1,2 = A monomials (x^3, y, y^2) on the LEFT half; 3,4,5 = B (y^3, x, x^2) RIGHT
#   Z slots 0,1,2 = B monomials (y^3, x, x^2) on the LEFT half; 3,4,5 = A (x^3, y, y^2) RIGHT
# Figure geometry forces: the long diagonal in each half is the degree-3 monomial (x^3 resp. y^3),
# the two nearest-neighbour edges are the remaining two.  Only their order is free (2 x 2 per panel).
def xmaps():
    for a in ((1, 2), (2, 1)):          # (e2,e5) -> (y, y^2) slots (1,2)
        for b in ((4, 5), (5, 4)):      # (e3,e4) -> (x, x^2) slots (4,5)
            yield {'e6': 0, 'e2': a[0], 'e5': a[1], 'e1': 3, 'e3': b[0], 'e4': b[1]}

def zmaps():
    for a in ((1, 2), (2, 1)):          # (e3,e4) -> (x, x^2) slots (1,2)
        for b in ((4, 5), (5, 4)):      # (e2,e5) -> (y, y^2) slots (4,5)
            yield {'e6': 0, 'e3': a[0], 'e4': a[1], 'e1': 3, 'e2': b[0], 'e5': b[1]}

def slot_times(panel, mp):
    """panel colour -> array t[slot] of CNOT times"""
    out = {}
    for col in COLS:
        t = [None] * 6
        for e, tt in panel[col].items():
            t[mp[e]] = tt
        out[col] = t
    return out

def order_class(t):
    return CLS_OF[tuple(sorted(range(6), key=lambda s: t[s]))]

def legal_mc(phi, TX, TZ, permX, permZ, P):
    """explicit legality (all 6 CNOT times of a data qubit distinct mod P) and (MC)."""
    tX = [[TX[COLS[permX[int(phi[g])]]][s] for s in range(6)] for g in range(NG)]
    tZ = [[TZ[COLS[permZ[int(phi[g])]]][s] for s in range(6)] for g in range(NG)]
    for q in range(N):
        ts = [tX[c][(0 if s == 'L' else 3) + i] % P for (c, s, i) in xchecks_of(q)] + \
             [tZ[c][(0 if s == 'L' else 3) + i] % P for (c, s, i) in zchecks_of(q)]
        if len(set(ts)) != 6:
            return False, None
    bad = 0; tot = 0
    for a in range(NG):
        xs = {q: (0 if s == 'L' else 3) + i for q, s, i in xcheck_nb(a)}
        for b in range(NG):
            zs = {q: (0 if s == 'L' else 3) + i for q, s, i in zcheck_nb(b)}
            sh = set(xs) & set(zs)
            if not sh:
                continue
            for dp in (-2, -1, 0, 1, 2):
                tot += 1
                c = sum(1 for q in sh if tZ[b][zs[q]] + P * dp < tX[a][xs[q]])
                if c % 2:
                    bad += 1
    return True, (tot, bad)

if __name__ == "__main__":
    phi = make_phi(1, 1); assert colour_valid(phi)
    rows = []
    for xi, xm in enumerate(xmaps()):
        TX = slot_times(XPANEL, xm)
        xtr = {col: order_class(TX[col]) for col in COLS}
        for zi, zm in enumerate(zmaps()):
            TZ = slot_times(ZPANEL, zm)
            ztr = {col: order_class(TZ[col]) for col in COLS}
            for permX in itertools.permutations(range(3)):
                for permZ in itertools.permutations(range(3)):
                    for P in (6, 7, 8):
                        ok, mc = legal_mc(phi, TX, TZ, permX, permZ, P)
                        if ok:
                            rows.append(dict(xmap=xi, zmap=zi, permX=permX, permZ=permZ, P=P,
                                             mc=mc,
                                             Xtriple=tuple(xtr[COLS[permX[c]]] for c in range(3)),
                                             Ztriple=tuple(ztr[COLS[permZ[c]]] for c in range(3))))
    print("legal (xmap,zmap,colour-assignment,period) readings:", len(rows))
    seen = set()
    for r in rows:
        k = (r['Xtriple'], r['Ztriple'], r['P'], r['mc'][1])
        if k in seen: continue
        seen.add(k)
        print(f"  P={r['P']}  X-triple {r['Xtriple']}  Z-triple {r['Ztriple']}  "
              f"(MC) violations {r['mc'][1]}/{r['mc'][0]}  xmap={r['xmap']} zmap={r['zmap']}")
    for xi, xm in enumerate(xmaps()):
        TX = slot_times(XPANEL, xm)
        print(f"xmap{xi}: X classes per panel colour:",
              {c: order_class(TX[c]) for c in COLS}, "orders",
              {c: tuple(sorted(range(6), key=lambda s: TX[c][s])) for c in COLS})
    for zi, zm in enumerate(zmaps()):
        TZ = slot_times(ZPANEL, zm)
        print(f"zmap{zi}: Z classes per panel colour:",
              {c: order_class(TZ[c]) for c in COLS}, "orders",
              {c: tuple(sorted(range(6), key=lambda s: TZ[c][s])) for c in COLS})
