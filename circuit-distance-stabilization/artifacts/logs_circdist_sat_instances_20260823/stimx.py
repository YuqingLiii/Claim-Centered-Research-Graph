"""
stimx.py -- export a Schedule to a stim memory circuit and run stim's own
undetectable-logical-error search.  This is the second, independent method:
stim does its own Pauli propagation, its own detector-error-model extraction and
its own graph search; sat_core/transfer share no code with it.

basis 'Z': |0>^n init, ideal transversal Z readout, primary detectors from the
           Z-checks (records m_b), observable = Z_L  ->  d_R^Z.
basis 'X': mirror                                    ->  d_R^X.
"""

import stim
import sat_core as S


def build_circuit(sch, R, basis="Z", p=1e-3):
    code = sch.code
    n, nA, nB = code.n, sch.nA, sch.nB
    ax = [n + a for a in range(nA)]
    az = [n + nA + b for b in range(nB)]
    pairs = sch.gate_pairs()
    lines = []
    mcount = 0
    mrec = {}          # ('a'|'b', check, round) -> absolute measurement index
    dat = list(range(n))
    lines.append(("RX " if basis == "X" else "R ") + " ".join(map(str, dat)))
    for r in range(R):
        lines.append("TICK")          # one TICK per round: tick_offset = round index
        lines.append("RX " + " ".join(map(str, ax)))
        lines.append("R " + " ".join(map(str, az)))
        lines.append("DEPOLARIZE1(%g) " % p + " ".join(map(str, ax + az)))
        for t in range(sch.T):
            ps = pairs.get(t, [])
            flat = []
            for (c, tg) in ps:
                flat += [c, tg]
            if flat:
                lines.append("CX " + " ".join(map(str, flat)))
                lines.append("DEPOLARIZE2(%g) " % p + " ".join(map(str, flat)))
            busy = set(flat)
            idle = [q for q in range(sch.nq) if q not in busy]
            if idle:
                lines.append("DEPOLARIZE1(%g) " % p + " ".join(map(str, idle)))
        lines.append("MX(%g) " % p + " ".join(map(str, ax)))
        for a in range(nA):
            mrec[("a", a, r)] = mcount
            mcount += 1
        lines.append("M(%g) " % p + " ".join(map(str, az)))
        for b in range(nB):
            mrec[("b", b, r)] = mcount
            mcount += 1
        # detectors available at this point
        prim, sec = ("b", "a") if basis == "Z" else ("a", "b")
        nprim = nB if basis == "Z" else nA
        nsec = nA if basis == "Z" else nB
        for g in range(nprim):
            ts = [mrec[(prim, g, r)]] + ([mrec[(prim, g, r - 1)]] if r > 0 else [])
            lines.append("DETECTOR " + " ".join("rec[%d]" % (m - mcount) for m in ts))
        if r >= 1:
            for g in range(nsec):
                ts = [mrec[(sec, g, r)], mrec[(sec, g, r - 1)]]
                lines.append("DETECTOR " + " ".join("rec[%d]" % (m - mcount) for m in ts))
    lines.append(("MX " if basis == "X" else "M ") + " ".join(map(str, dat)))
    rd = {}
    for q in range(n):
        rd[q] = mcount
        mcount += 1
    checks = code.zchecks if basis == "Z" else code.xchecks
    for g, supp in enumerate(checks):
        key = ("b", g, R - 1) if basis == "Z" else ("a", g, R - 1)
        ts = [mrec[key]] + [rd[q] for q in range(n) if (supp >> q) & 1]
        lines.append("DETECTOR " + " ".join("rec[%d]" % (m - mcount) for m in ts))
    logs = code.zlog if basis == "Z" else code.xlog
    for j, L in enumerate(logs):
        ts = [rd[q] for q in range(n) if (L >> q) & 1]
        lines.append("OBSERVABLE_INCLUDE(%d) " % j + " ".join("rec[%d]" % (m - mcount) for m in ts))
    return stim.Circuit("\n".join(lines))


def stim_distance(sch, R, basis="Z", maxsize=8, maxdeg=8):
    c = build_circuit(sch, R, basis)
    err = c.search_for_undetectable_logical_errors(
        dont_explore_detection_event_sets_with_size_above=maxsize,
        dont_explore_edges_with_degree_above=maxdeg,
        dont_explore_edges_increasing_symptom_degree=False,
        canonicalize_circuit_errors=True,
    )
    return len(err), err


def dem_signatures(sch, R, basis="Z"):
    """Set of (frozenset(detector ids), frozenset(observable ids)) of the DEM's
    error mechanisms -- compared against sat_core.spacetime_columns."""
    c = build_circuit(sch, R, basis)
    dem = c.detector_error_model(decompose_errors=False, allow_gauge_detectors=True)
    out = set()
    for inst in dem.flattened():
        if inst.type != "error":
            continue
        ds, os_ = [], []
        for t in inst.targets_copy():
            if t.is_relative_detector_id():
                ds.append(t.val)
            elif t.is_logical_observable_id():
                os_.append(t.val)
        out.add((frozenset(ds), frozenset(os_)))
    return out
