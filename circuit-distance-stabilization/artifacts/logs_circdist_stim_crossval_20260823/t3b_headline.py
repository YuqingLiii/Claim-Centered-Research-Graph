"""T3b -- THE HEADLINE CELL, with the layout convention pinned by T3a.

Convention (UNIQUE solution of the 96/16 funnel over 64 candidate conventions):
  interior parity 0 = Z ; X boundary on top/bottom, Z on left/right ;
  a weight-2 boundary check is HALF a virtual plaquette lying OUTSIDE the array,
  so top-boundary qubits are its SOUTH corners, bottom-boundary its NORTH,
  left-boundary its EAST, right-boundary its WEST.

RECORD (Table 4.3, FINDING 4.4): d=5 class D -> d_1 = 4, d_R = 3 for R >= 2,
both sectors value for value; d=3 class D -> 2 at every R.
"""
import sys
from itertools import permutations
sys.path.insert(0, '/private/tmp/claude-501/-Users-<author>-Documents-Codex-2026-08-07-i-have-connected-an-old-windows-outputs-Windows-SSD-Recovery-2026-08-07-Research-Projects-discovery-new-algorithms/9cc32a4a-88e5-4ab5-9f80-c6945cff3945/scratchpad')
from xval import (legal, mc_violations, CORNERS, code_distance, build,
                  dem_columns, min_weight, stim_native_distance, sched_depth,
                  CONV_FROZEN, CONV_COMPILER, CONV_NOISYRO)
from t3a_layout import build_surface, usched, funnel

PIX = ('NW', 'SW', 'NE', 'SE')      # class D
PIZ = ('NW', 'NE', 'SW', 'SE')
CONV = dict(parity=0, top_ns='S', bot_ns='N', left_ew='E', right_ew='W',
            xy_boundary='X_tb')


def mk(d):
    return build_surface(d, **CONV)


print("=" * 78)
print("TARGET 3 -- d=5 rotated surface, class D (piX=%s ; piZ=%s)"
      % (','.join(PIX), ','.join(PIZ)))
print("=" * 78)
for d in (3, 5):
    c = mk(d)
    nl, nm, mem = funnel(c)
    S = usched(c, PIX, PIZ)
    print("  d=%d  n=%d  validate=%s  code_distance=%s  funnel 576->%d->%d  "
          "classD in (MC) set: %s  depth=%d"
          % (d, c.n, c.validate(), code_distance(c), nl, nm,
             (PIX, PIZ) in mem, sched_depth(S)))


def orient(d, pair):
    a, b = sorted(pair)
    return 'vertical' if (a % d) == (b % d) else ('horizontal' if (a // d) == (b // d) else 'diag')


c5 = mk(5)
S5 = usched(c5, PIX, PIZ)
xh = [orient(5, [q for q, _ in sorted(S5[c], key=lambda z: z[1])][-2:])
      for c in c5.xnames if len(S5[c]) == 4]
zh = [orient(5, [q for q, _ in sorted(S5[c], key=lambda z: z[1])][-2:])
      for c in c5.znames if len(S5[c]) == 4]
print("\n  hook geometry (d=5, weight-4 checks): X-hooks %s ; Z-hooks %s"
      % ({k: xh.count(k) for k in set(xh)}, {k: zh.count(k) for k in set(zh)}))
print("  X_L is a COLUMN, Z_L is a ROW -> both hook families PARALLEL = doubly misaligned")
print("  [RECORD: 'N-order for the X-checks makes every bulk X-hook vertical (8 of 8 at d=5)']")

print()
print("=" * 78)
print("d_R FROM STIM DEMs")
print("=" * 78)
print("%-3s %-7s %-3s %-7s %-7s %-9s %-16s %s"
      % ("d", "sector", "R", "cols", "dets", "d_search", "d_stim_native", "time"))
import time
res = {}
for d, Rs, cap in ((3, (1, 2, 3), 3), (5, (1, 2), 4)):
    code = mk(d)
    S = usched(code, PIX, PIZ)
    for basis in ('Z', 'X'):
        for R in Rs:
            t0 = time.time()
            circ = build(code, S, R, basis, conv=CONV_FROZEN)
            try:
                cols, nd = dem_columns(circ)
            except ValueError as e:
                print("%-3d %-7s %-3d  DEM REFUSED %s" % (d, basis, R, str(e)[:60]))
                continue
            nat = stim_native_distance(circ, cap=cap + 1)
            ds = min_weight(cols, cap=cap) if len(cols) <= 6000 else 'SKIPPED(too many cols)'
            res[(d, basis, R)] = nat
            print("%-3d %-7s %-3d %-7d %-7d %-9s %-16s %.1fs"
                  % (d, basis, R, len(cols), nd, ds, nat, time.time() - t0))
            sys.stdout.flush()

print()
print("  d=5 min-over-sectors : d_1 = %s , d_2 = %s     [RECORD: d_1=4, d_2=3, R_stab=2]"
      % (min(res[(5, 'Z', 1)], res[(5, 'X', 1)]), min(res[(5, 'Z', 2)], res[(5, 'X', 2)])))
print("  d=3 min-over-sectors : %s     [RECORD: 2,2,2 -> R_stab=1]"
      % [min(res[(3, 'Z', R)], res[(3, 'X', R)]) for R in (1, 2, 3)])

# ---- adversarial convention probe on the discovery cell -------------------
print()
print("=" * 78)
print("ADVERSARIAL CONVENTION PROBE on the discovery cell (d=5, R=1 and 2)")
print("=" * 78)
print("%-7s %-3s %-14s %-14s %-14s" % ("sector", "R", "A=frozen", "B=compiler", "C=noisyro"))
code = mk(5)
S = usched(code, PIX, PIZ)
for basis in ('Z', 'X'):
    for R in (1, 2):
        row = []
        for conv in (CONV_FROZEN, CONV_COMPILER, CONV_NOISYRO):
            circ = build(code, S, R, basis, conv=conv)
            cols, _ = dem_columns(circ)
            nat = stim_native_distance(circ, cap=5)
            row.append("%s (%d cols)" % (nat, len(cols)))
        print("%-7s %-3d %-14s %-14s %-14s" % (basis, R, row[0], row[1], row[2]))
