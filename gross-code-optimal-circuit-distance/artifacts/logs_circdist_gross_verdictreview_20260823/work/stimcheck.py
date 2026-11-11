"""Independent oracle for measurement consistency: build the literal stim circuit of a gross-code
schedule and ask stim for a detector error model.  stim raises ValueError exactly when a detector
is non-deterministic, i.e. exactly when the schedule is not a syndrome-extraction circuit."""
import numpy as np, itertools, stim
from gross import NG, N, xcheck_nb, zcheck_nb
from sched import expand, check_legal, mc_violations

XANC = [N + g for g in range(NG)]          # 144..215
ZANC = [N + NG + g for g in range(NG)]     # 216..287


def stim_circuit(tX, tZ, R=3, basis='Z', p=1e-3):
    """standard memory experiment: ideal data init, R rounds, ideal transversal readout."""
    layers = sorted({v for g in range(NG) for v in tX[g].values()} |
                    {v for g in range(NG) for v in tZ[g].values()})
    gates = {l: [] for l in layers}
    for g in range(NG):
        for q, s, i in xcheck_nb(g):
            gates[tX[g][(s, i)]] += [XANC[g], q]      # X ancilla is control
        for q, s, i in zcheck_nb(g):
            gates[tZ[g][(s, i)]] += [q, ZANC[g]]      # Z ancilla is target
    data = list(range(N))
    c = stim.Circuit()
    c.append("R" if basis == 'Z' else "RX", data)
    nmeas = 0; rec = {}
    for r in range(R):
        c.append("RX", XANC); c.append("R", ZANC)
        c.append("DEPOLARIZE1", XANC + ZANC, p)
        for l in layers:
            tg = gates[l]
            used = set(tg)
            assert len(tg) == len(used), "illegal layer: qubit in two gates"
            c.append("CX", tg); c.append("DEPOLARIZE2", tg, p)
        c.append("MX", XANC, p)
        for g in range(NG):
            rec[('X', g, r)] = nmeas + g
        nmeas += NG
        c.append("M", ZANC, p)
        for g in range(NG):
            rec[('Z', g, r)] = nmeas + g
        nmeas += NG
        det = 'Z' if basis == 'Z' else 'X'
        oth = 'X' if basis == 'Z' else 'Z'
        for g in range(NG):
            if r == 0:
                c.append("DETECTOR", [stim.target_rec(rec[(det, g, 0)] - nmeas)])
            else:
                c.append("DETECTOR", [stim.target_rec(rec[(det, g, r)] - nmeas),
                                      stim.target_rec(rec[(det, g, r - 1)] - nmeas)])
            if r >= 1:
                c.append("DETECTOR", [stim.target_rec(rec[(oth, g, r)] - nmeas),
                                      stim.target_rec(rec[(oth, g, r - 1)] - nmeas)])
    c.append("M" if basis == 'Z' else "MX", data)
    for q in range(N):
        rec[('d', q)] = nmeas + q
    nmeas += N
    H = None
    from gross import HX, HZ
    H = HZ if basis == 'Z' else HX
    for g in range(NG):
        tg = [stim.target_rec(rec[(det, g, R - 1)] - nmeas)]
        for q in np.nonzero(H[g])[0]:
            tg.append(stim.target_rec(rec[('d', int(q))] - nmeas))
        c.append("DETECTOR", tg)
    return c


def stim_ok(tX, tZ, R=3, basis='Z'):
    try:
        c = stim_circuit(tX, tZ, R=R, basis=basis)
        dem = c.detector_error_model(decompose_errors=False, approximate_disjoint_errors=True)
        return True, dem.num_detectors, len([1 for _ in dem.flattened() if _.type == 'error'])
    except ValueError as e:
        return False, str(e)[:80], None


if __name__ == "__main__":
    phi0 = np.zeros(NG, int)
    # (a) a legal 6-CNOT-layer translation-invariant schedule (MC-violating by ti_mc.py)
    LX = np.zeros((3, 2, 3), int); LZ = np.zeros((3, 2, 3), int)
    for c in range(3):
        LX[c, 0, :] = [1, 2, 3]; LX[c, 1, :] = [4, 5, 6]
        LZ[c, 0, :] = [4, 5, 6]; LZ[c, 1, :] = [1, 2, 3]
    tX, tZ = expand(phi0, LX, LZ)
    print("(a) legal 6-layer LRC-style TI schedule: legal =", check_legal(tX, tZ, 6),
          " MC violations =", mc_violations(tX, tZ))
    print("    stim:", stim_ok(tX, tZ))
    # (b) fully non-interleaved: all X CNOTs in layers 1-6, all Z CNOTs in layers 7-12
    LX2 = np.zeros((3, 2, 3), int); LZ2 = np.zeros((3, 2, 3), int)
    for c in range(3):
        LX2[c, 0, :] = [1, 2, 3]; LX2[c, 1, :] = [4, 5, 6]
        LZ2[c, 0, :] = [7, 8, 9]; LZ2[c, 1, :] = [10, 11, 12]
    tX2, tZ2 = expand(phi0, LX2, LZ2)
    print("(b) 12-layer X-then-Z (globally non-interleaved): MC violations =",
          mc_violations(tX2, tZ2))
    print("    stim:", stim_ok(tX2, tZ2))
    print("    stim X-memory:", stim_ok(tX2, tZ2, basis='X'))
