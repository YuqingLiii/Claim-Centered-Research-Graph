"""T0 -- harness calibration against records that publish exact DEM column counts.

Record (artifact circdist_lift_d3gate_20260820.md Sec 4.4): rotated surface d=3,
M_IL and M_NI, Z-memory d_circ = 2,2,2,2 with 117/227/337/447 columns at R=2..5;
X-memory d_circ = 3,3,3,3.
"""
import sys
sys.path.insert(0, '/private/tmp/claude-501/-Users-<author>-Documents-Codex-2026-08-07-i-have-connected-an-old-windows-outputs-Windows-SSD-Recovery-2026-08-07-Research-Projects-discovery-new-algorithms/9cc32a4a-88e5-4ab5-9f80-c6945cff3945/scratchpad')
from xval import *   # noqa

print("=" * 78)
print("T0.1  CODE VALIDATION (re-derived from scratch, not imported)")
print("=" * 78)
for k in ('422', 'steane', 'surface3'):
    print("  %-10s %-24s %s" % (k, CODES[k].name, CODES[k].validate()))

print()
print("=" * 78)
print("T0.2  Sec 4.4 A/B pair, rotated surface d=3 -- schedule from the artifact text")
print("=" * 78)

# Sec 4.4 M_IL, transcribed from the artifact's t-table:
#  t0 : XA:a->q2  XB:a->q3  XC:a->q0  XD:a->q7
#  t1 : XA:a->q5  XB:a->q4  XC:a->q1  XD:a->q8  ZC:q2->a
#  t2 : XA:a->q1  XB:a->q6  ZA:q0->a  ZC:q5->a  ZD:q3->a
#  t3 : XA:a->q4  XB:a->q7  ZA:q3->a  ZD:q6->a
#  t4 : ZA:q1->a  ZB:q4->a
#  t5 : ZA:q4->a  ZB:q7->a
#  t6 : ZB:q5->a
#  t7 : ZB:q8->a
M_IL = {
    'XA': [(2, 0), (5, 1), (1, 2), (4, 3)],
    'XB': [(3, 0), (4, 1), (6, 2), (7, 3)],
    'XC': [(0, 0), (1, 1)],
    'XD': [(7, 0), (8, 1)],
    'ZA': [(0, 2), (3, 3), (1, 4), (4, 5)],
    'ZB': [(4, 4), (7, 5), (5, 6), (8, 7)],
    'ZC': [(2, 1), (5, 2)],
    'ZD': [(3, 2), (6, 3)],
}
# M_NI: same within-check orders, X block t0..t3, Z block t4..t7
XORD = {'XA': [2, 5, 1, 4], 'XB': [3, 4, 6, 7], 'XC': [0, 1], 'XD': [7, 8]}
ZORD = {'ZA': [0, 3, 1, 4], 'ZB': [4, 7, 5, 8], 'ZC': [2, 5], 'ZD': [3, 6]}
M_NI = {}
for c, o in XORD.items():
    M_NI[c] = [(q, i) for i, q in enumerate(o)]
for c, o in ZORD.items():
    M_NI[c] = [(q, 4 + i) for i, q in enumerate(o)]

code = CODES['surface3']
for nm, S in (('M_IL', M_IL), ('M_NI', M_NI)):
    print("\n  %s : depth=%d legal=%s  MC-violations=%s"
          % (nm, sched_depth(S), legal(code, S), mc_violations(code, S) or 'none'))
    for basis in ('Z', 'X'):
        row = []
        for R in (2, 3, 4, 5):
            r = dcirc(code, S, R, basis, cap=4)
            if not r['ok']:
                row.append('DEM-REFUSED')
            else:
                row.append("R=%d d=%s/native=%s cols=%d dets=%d"
                           % (R, r['d_search'], r['d_stim_native'], r['cols'], r['dets']))
        print("    %s-memory:" % basis)
        for x in row:
            print("       ", x)
print()
print("RECORD to match: Z-memory d=2 all R, cols 117/227/337/447 ; X-memory d=3 all R")
