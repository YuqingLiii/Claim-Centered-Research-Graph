"""TARGET 1 -- the [[4,2,2]] arm.

RECORD (CIRCDIST.lift.gap-example, PROVED; dossier Sec 7):
  within-check orders a=[0,1,2,3], b=[2,0,1,3]; depth 7; 176 measurement-consistent
  schedules, of which 173 have d_circ = 1 and *3* have d_circ = 2 with d_eff = 1,
  stable for R = 2..5.  Non-interleaved partners have d_circ = 1.
  Node caveat: "witness 1 gaps BOTH sectors, witnesses 2-3 gap Z-memory only".

This file RE-ENUMERATES the family from the schedule model (general increasing time
slots per check, dossier Sec 10.3) and lets stim decide every d_circ.
"""
import sys
from itertools import combinations
sys.path.insert(0, '/private/tmp/claude-501/-Users-<author>-Documents-Codex-2026-08-07-i-have-connected-an-old-windows-outputs-Windows-SSD-Recovery-2026-08-07-Research-Projects-discovery-new-algorithms/9cc32a4a-88e5-4ab5-9f80-c6945cff3945/scratchpad')
from xval import *   # noqa

code = CODES['422']
AORD = [0, 1, 2, 3]
BORD = [2, 0, 1, 3]
DEPTH = 7

print("=" * 78)
print("TARGET 1 -- [[4,2,2]] depth-%d family, orders a=%s b=%s" % (DEPTH, AORD, BORD))
print("=" * 78)

# ---- enumerate the family from the model ---------------------------------
allsl = list(combinations(range(DEPTH), 4))     # increasing slots, 4 CNOTs per check
cand = []
for sa in allsl:
    for sb in allsl:
        if max(max(sa), max(sb)) != DEPTH - 1:
            continue                             # depth EXACTLY 7
        S = {'a': [(q, t) for q, t in zip(AORD, sa)],
             'b': [(q, t) for q, t in zip(BORD, sb)]}
        if not legal(code, S):
            continue
        cand.append((sa, sb, S))

mc_ok = [(sa, sb, S) for (sa, sb, S) in cand if not mc_violations(code, S)]
print("legal depth-7 schedules            : %d" % len(cand))
print("measurement-consistent (my (MC))   : %d      [RECORD: 176]" % len(mc_ok))

# interleaved = the two checks' slot-blocks overlap in time
def interleaved(sa, sb):
    return not (min(sa) > max(sb) or min(sb) > max(sa))

print("of which interleaved               : %d" % sum(1 for a, b, _ in mc_ok if interleaved(a, b)))
print()

# ---- stim decides every d_circ -------------------------------------------
print("Running stim on all %d consistent schedules, R=2, both sectors ..." % len(mc_ok))
refused = 0
byd = {}
gap = []
for (sa, sb, S) in mc_ok:
    rz = dcirc(code, S, 2, 'Z', cap=3, native=False)
    rx = dcirc(code, S, 2, 'X', cap=3, native=False)
    if not rz['ok'] or not rx['ok']:
        refused += 1
        continue
    dz, dx = rz['d_search'], rx['d_search']
    byd[(dz, dx)] = byd.get((dz, dx), 0) + 1
    if dz >= 2 or dx >= 2:
        gap.append((sa, sb, dz, dx))

print("  stim refused DEM (non-deterministic) : %d   [expect 0 -- (MC) filter should be exact]"
      % refused)
print("  (d_Z, d_X) histogram over the family : %s" % dict(sorted(byd.items())))
print()
zgap = [g for g in gap if g[2] >= 2]
both = [g for g in gap if g[2] >= 2 and g[3] >= 2]
print("  schedules with d_circ^Z = 2  : %d      [RECORD: 3]" % len(zgap))
print("  of those, BOTH sectors = 2   : %d      [RECORD: 1 (witness 1)]" % len(both))
print()

# ---- the three witnesses, R = 2..5, with their non-interleaved partners ---
print("=" * 78)
print("THE WITNESSES, R = 2..5 (stim DEM + two independent distance extractors)")
print("=" * 78)
for idx, (sa, sb, dz, dx) in enumerate(sorted(zgap), 1):
    S = {'a': [(q, t) for q, t in zip(AORD, sa)],
         'b': [(q, t) for q, t in zip(BORD, sb)]}
    print("\n  WITNESS %d : a-slots %s  b-slots %s   interleaved=%s"
          % (idx, list(sa), list(sb), interleaved(sa, sb)))
    print("    schedule:")
    for t in range(DEPTH):
        line = []
        for (q, tt) in S['a']:
            if tt == t:
                line.append("a:anc->q%d" % q)
        for (q, tt) in S['b']:
            if tt == t:
                line.append("b:q%d->anc" % q)
        print("      t%d : %s" % (t, "  ".join(line) if line else "-"))
    for basis in ('Z', 'X'):
        vals, nat, cols = [], [], []
        for R in (2, 3, 4, 5):
            r = dcirc(code, S, R, basis, cap=3)
            vals.append(r['d_search'])
            nat.append(r['d_stim_native'])
            cols.append(r['cols'])
        print("    %s-memory  d_circ R=2..5 : %s   stim-native: %s   cols: %s"
              % (basis, vals, nat, cols))

# ---- non-interleaved partners -------------------------------------------
print()
print("=" * 78)
print("NON-INTERLEAVED PARTNERS (same within-check orders, block form)")
print("=" * 78)
for nm, sa, sb in (('a-block then b-block', (0, 1, 2, 3), (4, 5, 6, 7)),
                   ('b-block then a-block', (4, 5, 6, 7), (0, 1, 2, 3))):
    S = {'a': [(q, t) for q, t in zip(AORD, sa)],
         'b': [(q, t) for q, t in zip(BORD, sb)]}
    mv = mc_violations(code, S)
    print("\n  %s : depth=%d MC=%s" % (nm, sched_depth(S), mv or 'consistent'))
    for basis in ('Z', 'X'):
        vals = []
        for R in (2, 3, 4, 5):
            r = dcirc(code, S, R, basis, cap=3, native=False)
            vals.append(r['d_search'] if r['ok'] else 'DEM-REFUSED')
        print("    %s-memory  d_circ R=2..5 : %s      [RECORD: 1]" % (basis, vals))
