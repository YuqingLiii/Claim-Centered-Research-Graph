"""An explicit legal, measurement-consistent, depth-8 staggered left-right circuit of the gross
code, built from scratch and handed to stim.  Period 8 time steps: X instance p does its LEFT block
at 8p+{1,2,3} and its RIGHT block at 8p+{4,5,6} (prep 8p+0, measure 8p+7); the Z instance is
staggered by half a period, doing its LEFT block at 8p+{5,6,7} and its RIGHT block at 8p+{8,9,10}
(prep 8p+4, measure 8p+11).  Within each block the layer is the monomial index, which is a matching
because phi(A_i) (resp phi(B_i)) are distinct mod 3 -- no colouring is needed for the uniform case.
This is the object the review's section 5.3 exhibited; the point here is that (MC) holds for
structural reasons (section 3.2) and that stim confirms every detector is deterministic."""
import numpy as np, stim
from gross import NG, N, HX, HZ, xcheck_nb, zcheck_nb, xchecks_of, zchecks_of
import pool as poolmod

P = 8
XA = [N + g for g in range(NG)]; ZA = [N + NG + g for g in range(NG)]
def tX(slot):  return 1 + slot if slot < 3 else 4 + (slot - 3)
def tZ(slot):  return 5 + slot if slot < 3 else 8 + (slot - 3)

XSLOT = [[(0 if s == 'L' else 3) + i for (q, s, i) in xcheck_nb(g)] for g in range(NG)]
ZSLOT = [[(0 if s == 'L' else 3) + i for (q, s, i) in zcheck_nb(g)] for g in range(NG)]
XQ = [[q for (q, s, i) in xcheck_nb(g)] for g in range(NG)]
ZQ = [[q for (q, s, i) in zcheck_nb(g)] for g in range(NG)]

busy = {}; ok = True
for p in range(6):
    for g in range(NG):
        for k in range(6):
            for (t, q, a) in ((tX(XSLOT[g][k]) + P*p, XQ[g][k], XA[g]),
                              (tZ(ZSLOT[g][k]) + P*p, ZQ[g][k], ZA[g])):
                for qq in (q, a):
                    if (t, qq) in busy: ok = False
                    busy[(t, qq)] = 1
print("legality over 6 periods, every layer a matching:", ok)
print("CNOT layers used per period:", len({t % P for (t, q) in busy}),
      "; ancilla window (prep..measure):", "X 8 steps, Z 8 steps")
bad = tot = 0
for a in range(NG):
    for b in range(NG):
        sh = [(k, ZQ[b].index(XQ[a][k])) for k in range(6) if XQ[a][k] in ZQ[b]]
        if not sh: continue
        for dp in range(-3, 4):
            tot += 1
            if sum(1 for (k, l) in sh
                   if tZ(ZSLOT[b][l]) + P*dp < tX(XSLOT[a][k])) % 2:
                bad += 1
print(f"(MC): {bad} odd of {tot} (X-instance, Z-instance) overlapping pairs")

R = 5
ev = []
for p in range(R):
    for g in range(NG):
        ev.append((P*p + 0, 'rx', g)); ev.append((P*p + 7, 'mx', g))
        ev.append((P*p + 4, 'rz', g)); ev.append((P*p + 11, 'mz', g))
        for k in range(6):
            ev.append((tX(XSLOT[g][k]) + P*p, 'cx', (XA[g], XQ[g][k])))
            ev.append((tZ(ZSLOT[g][k]) + P*p, 'cz', (ZQ[g][k], ZA[g])))
ev.sort(key=lambda e: e[0])
c = stim.Circuit(); c.append("RX", list(range(N)))
nmeas = 0; seq = {}
i = 0
while i < len(ev):
    t = ev[i][0]; grp = []
    while i < len(ev) and ev[i][0] == t:
        grp.append(ev[i]); i += 1
    for kind in ('mx', 'mz', 'rx', 'rz', 'cx', 'cz'):
        sel = [g for g in grp if g[1] == kind]
        if not sel: continue
        if kind == 'rx': c.append("RX", [XA[g[2]] for g in sel])
        elif kind == 'rz': c.append("R", [ZA[g[2]] for g in sel])
        elif kind == 'mx':
            c.append("MX", [XA[g[2]] for g in sel])
            for g in sel: seq.setdefault(('X', g[2]), []).append(nmeas); nmeas += 1
        elif kind == 'mz':
            c.append("M", [ZA[g[2]] for g in sel])
            for g in sel: seq.setdefault(('Z', g[2]), []).append(nmeas); nmeas += 1
        else:
            tg = []
            for g in sel: tg += [g[2][0], g[2][1]]
            c.append("CX", tg)
for (kind, g), ms in seq.items():
    if kind != 'X': continue
    for j in range(1, len(ms)):
        c.append("DETECTOR", [stim.target_rec(ms[j] - nmeas), stim.target_rec(ms[j-1] - nmeas)])
try:
    dem = c.detector_error_model(decompose_errors=False, allow_gauge_detectors=False)
    print(f"stim X-memory: {c.num_qubits} qubits, {c.num_detectors} detectors, "
          f"6 CNOT layers per period, DEM BUILT OK")
    s = c.compile_detector_sampler().sample(1)
    print("   noiseless detector firings:", int(np.array(s)[0].sum()), "/", c.num_detectors)
except Exception as e:
    print("stim DEM FAILED:", type(e).__name__, str(e)[:140])
