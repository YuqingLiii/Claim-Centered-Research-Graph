"""TARGET 2 -- the Steane [[7,1,3]] gap instance.

RECORD (dossier Sec 5.2/5.3):
  M_IL (interleaved, depth 8)  Z-memory  d_eff=2  d_circ = 3,3,3,3  (R=2..5)
       DEM columns 149/285/421/557, detectors 12/18/24/30
  M_IL                          X-memory  d_circ = 2,2,2,2
  M_NI (non-interleaved, depth 10) both sectors d_circ = 2,2,2,2
  "stim agrees on all 16 entries."
"""
import sys
sys.path.insert(0, '/private/tmp/claude-501/-Users-<author>-Documents-Codex-2026-08-07-i-have-connected-an-old-windows-outputs-Windows-SSD-Recovery-2026-08-07-Research-Projects-discovery-new-algorithms/9cc32a4a-88e5-4ab5-9f80-c6945cff3945/scratchpad')
from xval import *   # noqa

code = CODES['steane']

# Sec 5.2, verbatim from the artifact's "orders and time slots" block
ORD = {'X1': [6, 3, 5, 4], 'X2': [1, 5, 6, 2], 'X3': [4, 2, 6, 0],
       'Z1': [3, 4, 6, 5], 'Z2': [2, 1, 5, 6], 'Z3': [2, 4, 6, 0]}
SLOT = {'X1': [0, 1, 2, 3], 'X2': [4, 5, 6, 7], 'X3': [0, 1, 2, 7],
        'Z1': [0, 1, 3, 4], 'Z2': [2, 3, 6, 7], 'Z3': [0, 4, 5, 6]}
M_IL = {c: list(zip(ORD[c], SLOT[c])) for c in ORD}

print("=" * 78)
print("TARGET 2 -- Steane [[7,1,3]], Sec 5.2 witness")
print("=" * 78)
print("code validation:", code.validate())
print("M_IL depth=%d legal=%s MC-violations=%s"
      % (sched_depth(M_IL), legal(code, M_IL), mc_violations(code, M_IL) or 'none'))
print("\n  transcribed schedule (cross-check against the artifact's t-table):")
for t in range(sched_depth(M_IL)):
    line = []
    for c in code.xnames:
        for (q, tt) in M_IL[c]:
            if tt == t:
                line.append("%s:a->q%d" % (c, q))
    for c in code.znames:
        for (q, tt) in M_IL[c]:
            if tt == t:
                line.append("%s:q%d->a" % (c, q))
    print("    t%d : %s" % (t, "  ".join(line)))

# ---- non-interleaved partner: same within-check orders, X block then Z block
def block_schedule(code, ORD, xfirst=True):
    S = {}
    busy = {}
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

M_NI = block_schedule(code, ORD, xfirst=True)
print("\nM_NI depth=%d legal=%s MC-violations=%s"
      % (sched_depth(M_NI), legal(code, M_NI), mc_violations(code, M_NI) or 'none'))
for t in range(sched_depth(M_NI)):
    line = []
    for c in code.xnames + code.znames:
        for (q, tt) in M_NI[c]:
            if tt == t:
                line.append("%s:q%d" % (c, q))
    print("    t%d : %s" % (t, "  ".join(line)))

print()
print("=" * 78)
print("d_circ FROM STIM DEMs  (my exact GF(2) search  /  stim's native search)")
print("=" * 78)
print("%-8s %-8s %-3s %-10s %-14s %-8s %s"
      % ("sched", "sector", "R", "d_search", "d_stim_native", "cols", "dets"))
for nm, S in (('M_IL', M_IL), ('M_NI', M_NI)):
    for basis in ('Z', 'X'):
        for R in (2, 3, 4, 5):
            r = dcirc(code, S, R, basis, cap=4)
            if not r['ok']:
                print("%-8s %-8s %-3d  DEM REFUSED: %s" % (nm, basis, R, r['why']))
            else:
                print("%-8s %-8s %-3d %-10s %-14s %-8d %d"
                      % (nm, basis, R, r['d_search'], r['d_stim_native'],
                         r['cols'], r['dets']))
print()
print("RECORD: M_IL Z = 3,3,3,3 cols 149/285/421/557 dets 12/18/24/30 ;"
      " M_IL X = 2,2,2,2 ; M_NI both = 2,2,2,2")

# ---------------------------------------------------------------- the probe
print()
print("=" * 78)
print("ADVERSARIAL PROBE -- does the answer survive a COMPILER-REALISTIC")
print("perturbation of the frozen fault inventory?")
print("=" * 78)
print("Convention B ('compiler'): identical circuit, but data qubits also idle-")
print("depolarize during the ancilla RESET layer and the ancilla MEASURE layer --")
print("locations a real compiler has and which the frozen model's 'time step'")
print("reading arguably omits (公共定义 counts idle slots only WITHIN the schedule).")
print("Convention C ('noisyro'): frozen + NOISY terminal readout (deliberately")
print("breaks the stated ideal-readout boundary; a control, not a defect test).")
print()
print("%-8s %-8s %-3s %-10s %-12s %-12s" % ("sched", "sector", "R", "A=frozen", "B=compiler", "C=noisyro"))
for nm, S in (('M_IL', M_IL), ('M_NI', M_NI)):
    for basis in ('Z', 'X'):
        for R in (2, 3):
            a = dcirc(code, S, R, basis, cap=4, native=False, conv=CONV_FROZEN)
            b = dcirc(code, S, R, basis, cap=4, native=False, conv=CONV_COMPILER)
            cc = dcirc(code, S, R, basis, cap=4, native=False, conv=CONV_NOISYRO)
            f = lambda r: (str(r['d_search']) + ' (%d cols)' % r['cols']) if r['ok'] else 'REFUSED'
            print("%-8s %-8s %-3d %-10s %-12s %-12s" % (nm, basis, R, f(a), f(b), f(cc)))

# also probe the [[4,2,2]] witness 1
print()
print("  same probe on the [[4,2,2]] witness 1 (a=[0,3,4,5], b=[0,1,2,6]):")
c422 = CODES['422']
W1 = {'a': list(zip([0, 1, 2, 3], [0, 3, 4, 5])),
      'b': list(zip([2, 0, 1, 3], [0, 1, 2, 6]))}
for basis in ('Z', 'X'):
    for R in (2, 3):
        a = dcirc(c422, W1, R, basis, cap=3, native=False, conv=CONV_FROZEN)
        b = dcirc(c422, W1, R, basis, cap=3, native=False, conv=CONV_COMPILER)
        cc = dcirc(c422, W1, R, basis, cap=3, native=False, conv=CONV_NOISYRO)
        f = lambda r: (str(r['d_search']) + ' (%d cols)' % r['cols']) if r['ok'] else 'REFUSED'
        print("%-8s %-8s %-3d %-10s %-12s %-12s" % ('W1', basis, R, f(a), f(b), f(cc)))
