"""TARGET 4 -- the transfer d=3 table (CIRCDIST.sat.transfer Sec 11.3), and
TARGET 5 -- a LIFT' repair-0 spot check.

RECORD (transfer artifact Sec 11.3 verbatim block), d_R for R = 1,2,3:
    surface913/blkZ   Z [3,3,3]   X [2,2,2]
    surface913/blkX   Z [3,3,3]   X [2,2,2]
    surface913/ilv0   Z [3,3,3]   X [2,2,2]
    surface913/ilv1   Z [2,2,2]   X [3,3,3]
  and "interleaved depth-4 surface schedules, legal AND (MC): 16 of 576",
  with named members (NW,NE,SW,SE)|(NW,NE,SW,SE) and (SW,NW,SE,NE)|(SW,NW,SE,NE).

Also verifies the RECORD's structural claim (sat.instances Table 4.2) that the 16
legal+(MC) members fall into exactly 4 classes of 4 with IDENTICAL d_R sequences.
"""
import sys
from itertools import permutations
sys.path.insert(0, '/private/tmp/claude-501/-Users-<author>-Documents-Codex-2026-08-07-i-have-connected-an-old-windows-outputs-Windows-SSD-Recovery-2026-08-07-Research-Projects-discovery-new-algorithms/9cc32a4a-88e5-4ab5-9f80-c6945cff3945/scratchpad')
from xval import (legal, mc_violations, CORNERS, build, dem_columns,
                  stim_native_distance, sched_depth, CODES)
from t3a_layout import build_surface, usched

CONV = dict(parity=0, top_ns='S', bot_ns='N', left_ew='E', right_ew='W',
            xy_boundary='X_tb')


def dR(code, S, R, basis, cap=5):
    circ = build(code, S, R, basis)
    try:
        cols, _ = dem_columns(circ)
    except ValueError:
        return 'MC-REFUSED'
    return stim_native_distance(circ, cap=cap)


print("=" * 78)
print("TARGET 4 -- surface [[9,1,3]], the four named transfer schedules")
print("=" * 78)
c3 = build_surface(3, **CONV)
print("code: %s  validate=%s" % (c3.name, c3.validate()))

ILV0 = (('NW', 'NE', 'SW', 'SE'), ('NW', 'NE', 'SW', 'SE'))
ILV1 = (('SW', 'NW', 'SE', 'NE'), ('SW', 'NW', 'SE', 'NE'))


def block(code, piX, piZ, xfirst):
    """Non-interleaved: all X-check CNOTs in one block, then all Z (or vice versa),
    each check using its corners in the given corner order."""
    S = {}
    from t3a_layout import build_surface as _b
    grp = [(code.xnames, code._xcorn, piX), (code.znames, code._zcorn, piZ)]
    if not xfirst:
        grp = grp[::-1]
    base = 0
    for names, corn, pi in grp:
        used = set()
        for c in names:
            cm = corn[c]
            S[c] = [(cm[l], base + t) for t, l in enumerate(pi) if l in cm]
            used |= {t for _, t in S[c]}
        base = max(used) + 1
    return S


CASES = [
    ('surface913/ilv0', usched(c3, *ILV0), ([3, 3, 3], [2, 2, 2])),
    ('surface913/ilv1', usched(c3, *ILV1), ([2, 2, 2], [3, 3, 3])),
    ('surface913/blkX', block(c3, *ILV0[0:1] * 2, xfirst=True), ([3, 3, 3], [2, 2, 2])),
    ('surface913/blkZ', block(c3, *ILV0[0:1] * 2, xfirst=False), ([3, 3, 3], [2, 2, 2])),
]
print("\n%-18s %-6s %-6s %-14s %-14s %s"
      % ("instance", "depth", "MC", "Z: d_R (1..3)", "X: d_R (1..3)", "vs RECORD"))
for nm, S, rec in CASES:
    mv = mc_violations(c3, S)
    z = [dR(c3, S, R, 'Z') for R in (1, 2, 3)]
    x = [dR(c3, S, R, 'X') for R in (1, 2, 3)]
    ok = 'MATCH' if (z, x) == (rec[0], rec[1]) else 'MISMATCH (rec %s/%s)' % rec
    print("%-18s %-6d %-6s %-14s %-14s %s"
          % (nm, sched_depth(S), 'yes' if not mv else 'NO', z, x, ok))

# ------------------------------------------------------------------ class structure
print()
print("=" * 78)
print("STRUCTURAL CHECK -- all 16 legal+(MC) members, d=3 and d=5")
print("RECORD (Table 4.2): exactly 4 classes of 4, identical d_R within a class")
print("=" * 78)
for d, Rs in ((3, (1, 2, 3)), (5, (1, 2))):
    code = build_surface(d, **CONV)
    mem = []
    for piX in permutations(CORNERS):
        for piZ in permutations(CORNERS):
            S = usched(code, piX, piZ)
            if legal(code, S) and not mc_violations(code, S):
                mem.append((piX, piZ))
    groups = {}
    for (piX, piZ) in mem:
        S = usched(code, piX, piZ)
        sig = (tuple(dR(code, S, R, 'Z') for R in Rs),
               tuple(dR(code, S, R, 'X') for R in Rs))
        groups.setdefault(sig, []).append((piX, piZ))
    print("\n  d=%d : %d legal+(MC) members -> %d distinct (d_R^Z, d_R^X) signatures"
          % (d, len(mem), len(groups)))
    for sig, ms in sorted(groups.items()):
        print("     Z%s / X%s   : %d members" % (list(sig[0]), list(sig[1]), len(ms)))
    print("     class sizes: %s   [RECORD: four classes of four]"
          % sorted(len(v) for v in groups.values()))

# ------------------------------------------------------------------ TARGET 5
print()
print("=" * 78)
print("TARGET 5 -- LIFT' repair-0 spot check: non-interleaved => d_circ = d_eff")
print("=" * 78)
print("Non-interleaved schedules are the repair-0 case; the criterion predicts")
print("d_circ = d_eff (公共定义: '非交错电路已知满足 d_circ = d_eff').")
print("d_eff values are IMPORTED from the campaign records (not recomputed here).")
print()
print("%-34s %-8s %-8s %-16s %s" % ("instance (non-interleaved)", "sector", "d_eff", "stim d_circ R=1..4", "verdict"))

# Steane block partner (same construction as Target 2)
steane = CODES['steane']
ORD = {'X1': [6, 3, 5, 4], 'X2': [1, 5, 6, 2], 'X3': [4, 2, 6, 0],
       'Z1': [3, 4, 6, 5], 'Z2': [2, 1, 5, 6], 'Z3': [2, 4, 6, 0]}


def block_generic(code, ORD, xfirst=True):
    S, busy = {}, {}
    groups = (code.xnames, code.znames) if xfirst else (code.znames, code.xnames)
    base = 0
    for grp in groups:
        used = set()
        for c in grp:
            a = code.anc[c]
            last = base - 1
            S[c] = []
            for q in ORD[c]:
                t = last + 1
                while (a, t) in busy or (q, t) in busy or t < base:
                    t += 1
                busy[(a, t)] = busy[(q, t)] = c
                S[c].append((q, t))
                used.add(t)
                last = t
        base = max(used) + 1
    return S


ROWS = [
    ('Steane [[7,1,3]] M_NI', steane, block_generic(steane, ORD, True), {'Z': 2, 'X': 2}),
    ('surface [[9,1,3]] blkX', c3, block(c3, *ILV0[0:1] * 2, xfirst=True), {'Z': 3, 'X': 2}),
    ('[[4,2,2]] a-block then b-block', CODES['422'],
     {'a': list(zip([0, 1, 2, 3], [0, 1, 2, 3])),
      'b': list(zip([2, 0, 1, 3], [4, 5, 6, 7]))}, {'Z': 1, 'X': 1}),
]
for nm, code, S, deff in ROWS:
    for basis in ('Z', 'X'):
        vals = [dR(code, S, R, basis, cap=5) for R in (1, 2, 3, 4)]
        ok = 'MATCH' if all(v == deff[basis] for v in vals) else 'MISMATCH'
        print("%-34s %-8s %-8d %-16s %s" % (nm, basis, deff[basis], vals, ok))
