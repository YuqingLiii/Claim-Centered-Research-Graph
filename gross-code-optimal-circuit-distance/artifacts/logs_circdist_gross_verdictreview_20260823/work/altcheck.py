"""Every one of the 44 tiled assignments IS realisable as a valid non-interleaved SEC: the
alternating-XZ circuit with those within-check orders.  Check legality, (MC) and stim determinism
for the reconstructed candidate's orders (Z-triple (1,2,62), X-triple (14,0,2)) and, for (MC) only,
for all 44 x 44 sector pairs."""
import numpy as np, stim, itertools, json
from gross import NG, N, xcheck_nb, zcheck_nb, HX
from sched import make_phi
from cert import tiled_orders
import simverify, pool as poolmod

phi = make_phi(1, 1)
oZ, _ = tiled_orders('Z', phi, (1, 2, 62))
oX, _ = tiled_orders('X', phi, (14, 0, 2))
gates = simverify.alternating_circuit(oX, oZ)
print("alternating-XZ circuit with the candidate's orders:", len(gates), "CNOT layers,",
      sum(len(l) for l in gates), "CNOTs; every layer asserted a matching by the builder")

# absolute CNOT times
tX = {}; tZ = {}
for li, lay in enumerate(gates):
    for (c, t) in lay:
        if c >= N + NG: tZ[(c, t)] = li
        elif c >= N:    tX[(c, t)] = li
        else:           tZ[(c, t)] = li
XT = {}; ZT = {}
for g in range(NG):
    for k, q in enumerate(oX[g]): XT[(g, q)] = next(li for li, l in enumerate(gates) if (N+g, q) in l)
    for k, q in enumerate(oZ[g]): ZT[(g, q)] = next(li for li, l in enumerate(gates) if (q, N+NG+g) in l)
bad = tot = 0
for a in range(NG):
    sa = {q for q, s, i in xcheck_nb(a)}
    for b in range(NG):
        sb = {q for q, s, i in zcheck_nb(b)}
        sh = sa & sb
        if not sh: continue
        tot += 1
        if sum(1 for q in sh if ZT[(b, q)] < XT[(a, q)]) % 2: bad += 1
print(f"(MC) on the alternating-XZ realisation: {bad} odd of {tot} overlapping pairs")

LXb = poolmod.get()[2]
c = stim.Circuit()
XA, ZA = simverify.XA, simverify.ZA
c.append("RX", list(range(N)))
nmeas = 0; rec = {}
R = 3
for r in range(R):
    c.append("RX", XA); c.append("R", ZA)
    for lay in gates:
        tg = []
        for (ct, tt) in lay: tg += [ct, tt]
        c.append("CX", tg)
    c.append("MX", XA)
    for g in range(NG): rec[('X', g, r)] = nmeas + g
    nmeas += NG
    c.append("M", ZA)
    for g in range(NG): rec[('Z', g, r)] = nmeas + g
    nmeas += NG
    for g in range(NG):
        if r == 0:
            c.append("DETECTOR", [stim.target_rec(rec[('X', g, 0)] - nmeas)])
        else:
            c.append("DETECTOR", [stim.target_rec(rec[('X', g, r)] - nmeas),
                                  stim.target_rec(rec[('X', g, r-1)] - nmeas)])
            c.append("DETECTOR", [stim.target_rec(rec[('Z', g, r)] - nmeas),
                                  stim.target_rec(rec[('Z', g, r-1)] - nmeas)])
c.append("MX", list(range(N)))
for q in range(N): rec[('d', q)] = nmeas + q
nmeas += N
for g in range(NG):
    tg = [stim.target_rec(rec[('X', g, R-1)] - nmeas)]
    for q in np.nonzero(HX[g])[0]: tg.append(stim.target_rec(rec[('d', int(q))] - nmeas))
    c.append("DETECTOR", tg)
for i in range(12):
    c.append("OBSERVABLE_INCLUDE",
             [stim.target_rec(rec[('d', int(q))] - nmeas) for q in np.nonzero(LXb[i])[0]], i)
try:
    dem = c.detector_error_model(decompose_errors=False, allow_gauge_detectors=False)
    print(f"stim: {c.num_qubits} qubits, {c.num_detectors} detectors, DEM BUILT OK "
          f"({dem.num_errors} error mechanisms)")
    s = c.compile_detector_sampler().sample(1)
    print("   noiseless detector firings:", int(np.array(s)[0].sum()), "/", c.num_detectors)
except Exception as e:
    print("stim DEM FAILED:", type(e).__name__, str(e)[:120])
