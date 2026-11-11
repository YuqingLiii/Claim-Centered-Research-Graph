"""Circuit-level verification of an extended-code witness, by independent Pauli-frame propagation.

The circuit used is the ALTERNATING-XZ (globally non-interleaved) circuit with the candidate's
within-check CNOT orders: all X-check CNOTs in layers 1..6, then all Z-check CNOTs in layers 7..12.
[SBB26] Theorem 1 gives d_circ = d_ext(E) for it (it is the extreme non-interleaved circuit they
name), and it has the SAME within-check orders, hence the SAME residual set, as any depth-8
left-right circuit with those orders.  The in-house Theorem 7.1 gives the same equality.

This module shares no code with dext/dext2: it builds the literal CNOT list and propagates
Z-type Pauli frames  (CNOT(c,t):  z[c] ^= z[t]).
"""
import numpy as np
from gross import NG, N, HX, HZ, xcheck_nb, zcheck_nb, Reducer

XA = [N + g for g in range(NG)]
ZA = [N + NG + g for g in range(NG)]
NQ = N + 2 * NG


def _block(pairs_by_check, anc, control_is_anc):
    """greedy legal layering of one block: check g's p-th CNOT must land strictly later than its
    (p-1)-th, so every check's within-check CNOT order is preserved exactly."""
    layers = []
    busy = []
    last = {g: -1 for g in pairs_by_check}
    for pos in range(6):
        for g in sorted(pairs_by_check):
            q = pairs_by_check[g][pos]
            a = anc[g]
            l = last[g] + 1
            while True:
                while l >= len(layers):
                    layers.append([]); busy.append(set())
                if a not in busy[l] and q not in busy[l]:
                    break
                l += 1
            layers[l].append((a, q) if control_is_anc else (q, a))
            busy[l].add(a); busy[l].add(q)
            last[g] = l
    return layers


def alternating_circuit(ordersX, ordersZ):
    """all X-check CNOTs, then all Z-check CNOTs (the alternating-XZ circuit of [SBB26] S5).
    Returns gates = list of layers, each a list of (control, target)."""
    gates = _block({g: ordersX[g] for g in range(NG)}, XA, True)
    gates += _block({g: ordersZ[g] for g in range(NG)}, ZA, False)
    for lay in gates:
        used = set()
        for (c, t) in lay:
            assert c not in used and t not in used, "illegal layer"
            used.add(c); used.add(t)
    # every check's within-check order must be exactly the requested one
    tim = {}
    for li, lay in enumerate(gates):
        for (c, t) in lay:
            tim[(c, t)] = li
    for g in range(NG):
        ts = [tim[(XA[g], q)] for q in ordersX[g]]
        assert ts == sorted(ts) and len(set(ts)) == 6
        ts = [tim[(q, ZA[g])] for q in ordersZ[g]]
        assert ts == sorted(ts) and len(set(ts)) == 6
    return gates


def hook_layer(gates, ordersZ, g, l):
    """index of the layer holding the l-th CNOT of Z-check g"""
    q = ordersZ[g][l - 1]
    for li, lay in enumerate(gates):
        if (q, ZA[g]) in lay:
            return li
    raise KeyError((g, l))


def run_z(gates, ordersZ, hook_faults, data_faults):
    """hook_faults: list of (zcheck g, position l in 1..6) -- Z on the Z-ancilla just before its
       l-th CNOT.  data_faults: list of data qubits carrying Z at the very end of the round.
       Returns (X-check outcome flips, net data Z error)."""
    z = np.zeros(NQ, np.uint8)
    hooks = {}
    for (g, l) in hook_faults:
        hooks.setdefault(hook_layer(gates, ordersZ, g, l), []).append(g)
    for li, lay in enumerate(gates):
        for g in hooks.get(li, []):
            z[ZA[g]] ^= 1
        for (c, t) in lay:
            z[c] ^= z[t]                # Z propagates target -> control
    for q in data_faults:
        z[q] ^= 1
    flips = np.array([z[XA[g]] for g in range(NG)], np.uint8)   # MX outcome flipped by Z on ancilla
    E = z[:N].copy()
    return flips, E


def run_x(gates, ordersX, hook_faults, data_faults):
    """X sector: X on an X-check ancilla (the CNOT control) just before its l-th CNOT.
       CNOT(c,t) propagates X on the control to the target: x[t] ^= x[c]."""
    x = np.zeros(NQ, np.uint8)
    hooks = {}
    for (g, l) in hook_faults:
        q = ordersX[g][l - 1]
        li = next(i for i, lay in enumerate(gates) if (XA[g], q) in lay)
        hooks.setdefault(li, []).append(g)
    for li, lay in enumerate(gates):
        for g in hooks.get(li, []):
            x[XA[g]] ^= 1
        for (c, t) in lay:
            x[t] ^= x[c]
    for q in data_faults:
        x[q] ^= 1
    flips = np.array([x[ZA[g]] for g in range(NG)], np.uint8)   # M(Z) flipped by X on the ancilla
    return flips, x[:N].copy()


def verify_x(ordersX, residuals, data_faults, ordersZ=None, verbose=True):
    if ordersZ is None:
        ordersZ = [[q for q, s, i in zcheck_nb(g)] for g in range(NG)]
    # X-checks must run LAST here so that their hooks are not seen by the Z-check detectors of
    # this round; the alternating circuit is used with the two blocks swapped.
    gates = _block({g: ordersZ[g] for g in range(NG)}, ZA, False)
    gates += _block({g: ordersX[g] for g in range(NG)}, XA, True)
    L = {0: 3, 1: 4, 2: 5}
    hooks = [(c, L[k]) for (c, k) in residuals]
    flips, E = run_x(gates, ordersX, hooks, data_faults)
    syn = (HZ @ E) % 2
    red = Reducer(HX)
    out = dict(nfaults=len(hooks) + len(data_faults),
               round_detectors_silent=bool(not flips.any()),
               terminal_detectors_silent=bool(not syn.any()),
               net_error_weight=int(E.sum()),
               nontrivial_logical=bool(not red.inspan(E)))
    if verbose:
        print("   circuit-level verification (X sector):", out)
    return out


def verify(ordersZ, residuals, data_faults, ordersX=None, verbose=True):
    """residuals: list of (check, k) with k in {0,1,2} <-> hook position l in {3,4,5}."""
    if ordersX is None:
        ordersX = [[q for q, s, i in xcheck_nb(g)] for g in range(NG)]
    gates = alternating_circuit(ordersX, ordersZ)
    L = {0: 3, 1: 4, 2: 5}
    hooks = [(c, L[k]) for (c, k) in residuals]
    flips, E = run_z(gates, ordersZ, hooks, data_faults)
    syn = (HX @ E) % 2
    red = Reducer(HZ)
    out = dict(nfaults=len(hooks) + len(data_faults),
               round_detectors_silent=bool(not flips.any()),
               terminal_detectors_silent=bool(not syn.any()),
               net_error_weight=int(E.sum()),
               nontrivial_logical=bool(not red.inspan(E)))
    if verbose:
        print("   circuit-level verification:", out)
    return out
