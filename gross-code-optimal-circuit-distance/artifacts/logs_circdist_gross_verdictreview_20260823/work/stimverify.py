"""Third, fully external verification of a witness: build the alternating-XZ circuit in stim,
inject the explicit Pauli faults as error channels, and sample the (noiseless, hence deterministic)
detectors and observables.  All detectors must read 0 and some observable must read 1.

NOTE: stim's detector sampler computes detection events relative to a NOISELESS reference
simulation of the same circuit, so deterministic X/Y/Z gates are absorbed into the reference and
produce no detection events.  Faults must therefore be injected as `Z_ERROR(1)` channels.
"""
import numpy as np, stim
from gross import NG, N, HX, xcheck_nb
import pool as poolmod
import simverify

XA = simverify.XA
ZA = simverify.ZA


def build(ordersX, ordersZ, hook_faults, data_faults, R=2):
    """X-memory experiment: data in |+>, X-check detectors, X-basis transversal readout.
    hook_faults: (zcheck, l) with l in 1..6 -> Z on that ancilla just before its l-th CNOT.
    Faults are inserted in the LAST round.  The layering comes from simverify (legality only);
    the propagation and detector bookkeeping here are stim's, not ours."""
    gates = simverify.alternating_circuit(ordersX, ordersZ)
    hk = {}
    for (g, l) in hook_faults:
        hk.setdefault(simverify.hook_layer(gates, ordersZ, g, l), []).append(g)
    LXb = poolmod.get()[2]
    c = stim.Circuit()
    c.append("RX", list(range(N)))
    nmeas = 0; rec = {}
    for r in range(R):
        c.append("RX", XA); c.append("R", ZA)
        for li, lay in enumerate(gates):
            if r == R - 1 and li in hk:
                c.append("Z_ERROR", [ZA[g] for g in hk[li]], 1.0)
            tg = []
            for (ct, tt) in lay:
                tg += [ct, tt]
            c.append("CX", tg)
        if r == R - 1 and data_faults:
            c.append("Z_ERROR", list(data_faults), 1.0)
        c.append("MX", XA)
        for g in range(NG):
            rec[('X', g, r)] = nmeas + g
        nmeas += NG
        c.append("M", ZA)
        for g in range(NG):
            rec[('Z', g, r)] = nmeas + g
        nmeas += NG
        for g in range(NG):
            if r == 0:
                c.append("DETECTOR", [stim.target_rec(rec[('X', g, 0)] - nmeas)])
            else:
                c.append("DETECTOR", [stim.target_rec(rec[('X', g, r)] - nmeas),
                                      stim.target_rec(rec[('X', g, r - 1)] - nmeas)])
                c.append("DETECTOR", [stim.target_rec(rec[('Z', g, r)] - nmeas),
                                      stim.target_rec(rec[('Z', g, r - 1)] - nmeas)])
    c.append("MX", list(range(N)))
    for q in range(N):
        rec[('d', q)] = nmeas + q
    nmeas += N
    for g in range(NG):
        tg = [stim.target_rec(rec[('X', g, R - 1)] - nmeas)]
        for q in np.nonzero(HX[g])[0]:
            tg.append(stim.target_rec(rec[('d', int(q))] - nmeas))
        c.append("DETECTOR", tg)
    for i in range(12):
        c.append("OBSERVABLE_INCLUDE",
                 [stim.target_rec(rec[('d', int(q))] - nmeas)
                  for q in np.nonzero(LXb[i])[0]], i)
    return c


def check(ordersX, ordersZ, residuals, data_faults, R=2):
    L = {0: 3, 1: 4, 2: 5}
    hooks = [(cc, L[k]) for (cc, k) in residuals]
    circ = build(ordersX, ordersZ, hooks, data_faults, R=R)
    det, ob = circ.compile_detector_sampler().sample(1, separate_observables=True)
    circ0 = build(ordersX, ordersZ, [], [], R=R)
    det0, ob0 = circ0.compile_detector_sampler().sample(1, separate_observables=True)
    return dict(n_faults=len(hooks) + len(data_faults),
                detectors_fired=int(np.array(det)[0].sum()),
                observables_flipped=int(np.array(ob)[0].sum()),
                clean_detectors_fired=int(np.array(det0)[0].sum()),
                clean_observables_flipped=int(np.array(ob0)[0].sum()),
                n_detectors=circ.num_detectors)
