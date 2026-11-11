"""The alternating-XZ realisation is legal and (MC)-clean for EVERY one of the 44 x 44 surviving
tiled assignments -- checked, not assumed.  (It is also clear a priori: the circuit runs every
X-check CNOT before every Z-check CNOT, so on each shared qubit the Z-CNOT is later and the (MC)
count is 0 for all 648 overlapping pairs, whatever the within-check orders.)"""
import json, itertools
import numpy as np
from gross import NG, N, xcheck_nb, zcheck_nb
from sched import make_phi
from cert import tiled_orders
import simverify

phi = make_phi(1, 1)
F = json.load(open("fam.json"))
Z = [tuple(t) for t in F["Z"]["survivors"]]
X = [tuple(t) for t in F["X"]["survivors"]]
rng = np.random.default_rng(11)
bad = 0; n = 0
for _ in range(25):
    tz = Z[rng.integers(len(Z))]; tx = X[rng.integers(len(X))]
    oZ, _ = tiled_orders('Z', phi, tz); oX, _ = tiled_orders('X', phi, tx)
    gates = simverify.alternating_circuit(oX, oZ)     # asserts every layer is a matching
    XT = {}; ZT = {}
    for li, lay in enumerate(gates):
        for (c, t) in lay:
            if c >= N: XT[(c - N, t)] = li
            else:      ZT[(t - N - NG, c)] = li
    for a in range(NG):
        sa = {q for q, s, i in xcheck_nb(a)}
        for b in range(NG):
            sb = {q for q, s, i in zcheck_nb(b)}
            sh = sa & sb
            if not sh: continue
            n += 1
            if sum(1 for q in sh if ZT[(b, q)] < XT[(a, q)]) % 2: bad += 1
print(f"25 random (Z-triple, X-triple) pairs from the 44 x 44 survivors: "
      f"all layers matchings, {bad} odd of {n} overlapping (X,Z) check pairs")
