"""Build the reconstructed [SBB26] Figure-12 circuit explicitly at period 8 (depth 8) and verify it:
legality layer by layer, (MC) by the parity condition, and determinism of every detector in stim."""
import json, itertools
import numpy as np, stim
from gross import NG, N, HX, HZ, xcheck_nb, zcheck_nb, xchecks_of, zchecks_of, Reducer
from sched import make_phi
from cascade import CLS_OF, REPS
from fig12 import XPANEL, ZPANEL, COLS
import pool as poolmod

P = 8
R = json.load(open("fig12_reading2.json"))
row = next(r for r in R if r['P'] == P and r['tag'] == 'upper=X' and r['white_left']
           and r['stZ'] and not r['stX'] and r['phi'] == [1, 1]
           and r['Xtriple'] == [14, 0, 2])
print("reading:", {k: row[k] for k in ('P','stX','stZ','white_left','phi','delta','Xtriple','Ztriple')})
print("  xedge", row['xedge'], "colX", row['colX'])
print("  zedge", row['zedge'], "colZ", row['colZ'])

def times(panel, edge, colperm, straddle, white, black):
    T = {}
    for col in COLS:
        t = [None]*6
        for e, tt in panel[col].items():
            t[edge[e]] = tt
        if straddle:
            wl = sum(t[edge[e]] for e in white)/3; bl = sum(t[edge[e]] for e in black)/3
            for e in (white if wl < bl else black):
                t[edge[e]] += P
        T[col] = t
    return {c: T[COLS[colperm[c]]] for c in range(3)}

TX = times(XPANEL, row['xedge'], row['colX'], row['stX'], ['e2','e5','e6'], ['e1','e3','e4'])
TZ = times(ZPANEL, row['zedge'], row['colZ'], row['stZ'], ['e3','e4','e6'], ['e1','e2','e5'])
TZ = {c: [x + row['delta'] for x in TZ[c]] for c in TZ}
print("X times per colour:", TX)
print("Z times per colour:", TZ)
phi = make_phi(1, 1); PHI = [int(phi[g]) for g in range(NG)]
ordX = [tuple(sorted(range(6), key=lambda s: TX[PHI[g]][s])) for g in range(NG)]
ordZ = [tuple(sorted(range(6), key=lambda s: TZ[PHI[g]][s])) for g in range(NG)]
print("X classes:", tuple(CLS_OF[ordX[g]] for g in range(3)),
      " Z classes:", tuple(CLS_OF[ordZ[g]] for g in range(3)))

XSLOT = [[(0 if s=='L' else 3)+i for (q,s,i) in xcheck_nb(g)] for g in range(NG)]
ZSLOT = [[(0 if s=='L' else 3)+i for (q,s,i) in zcheck_nb(g)] for g in range(NG)]
XQ = [[q for (q,s,i) in xcheck_nb(g)] for g in range(NG)]
ZQ = [[q for (q,s,i) in zcheck_nb(g)] for g in range(NG)]

# ---- legality: every absolute layer is a matching on the 288 qubits ----
XA = [N+g for g in range(NG)]; ZA = [N+NG+g for g in range(NG)]
busy = {}; ok = True
for p in range(6):
    for g in range(NG):
        for k in range(6):
            t = TX[PHI[g]][XSLOT[g][k]] + P*p
            for qq in (XQ[g][k], XA[g]):
                if (t, qq) in busy: ok = False
                busy[(t, qq)] = 1
        for k in range(6):
            t = TZ[PHI[g]][ZSLOT[g][k]] + P*p
            for qq in (ZQ[g][k], ZA[g]):
                if (t, qq) in busy: ok = False
                busy[(t, qq)] = 1
print("legality over 6 periods (every layer a matching):", ok)
lay = sorted({t for (t, q) in busy})
print("CNOT-carrying layers per period:", len({t % P for (t, q) in busy}),
      " ancilla window lengths:",
      {c: (max(TX[c])-min(TX[c])+3, max(TZ[c])-min(TZ[c])+3) for c in range(3)})

# ---- (MC) ----
bad = tot = 0
for a in range(NG):
    for b in range(NG):
        sh = [(k, ZQ[b].index(XQ[a][k])) for k in range(6) if XQ[a][k] in ZQ[b]]
        if not sh: continue
        for dp in range(-3, 4):
            tot += 1
            c = sum(1 for (k,l) in sh
                    if TZ[PHI[b]][ZSLOT[b][l]] + P*dp < TX[PHI[a]][XSLOT[a][k]])
            if c % 2: bad += 1
print(f"(MC): {bad} odd of {tot} (X-instance, Z-instance) overlapping pairs")

# ---- stim: does the DEM build (all detectors deterministic)? ----
def stim_circuit(rounds, basis):
    LXb = poolmod.get()[2]; LZb = poolmod.get()[3]
    ev = []
    for p in range(rounds):
        for g in range(NG):
            ev.append((min(TX[PHI[g]])-1+P*p, 'rx', g))
            ev.append((max(TX[PHI[g]])+1+P*p, 'mx', g))
            ev.append((min(TZ[PHI[g]])-1+P*p, 'rz', g))
            ev.append((max(TZ[PHI[g]])+1+P*p, 'mz', g))
            for k in range(6):
                ev.append((TX[PHI[g]][XSLOT[g][k]]+P*p, 'cx', (XA[g], XQ[g][k])))
                ev.append((TZ[PHI[g]][ZSLOT[g][k]]+P*p, 'cz', (ZQ[g][k], ZA[g])))
    ev.sort(key=lambda e: e[0])
    c = stim.Circuit()
    c.append("RX" if basis == 'X' else "R", list(range(N)))
    nmeas = 0; rec = {}
    i = 0
    while i < len(ev):
        t = ev[i][0]; grp = []
        while i < len(ev) and ev[i][0] == t:
            grp.append(ev[i]); i += 1
        for kind in ('mx','mz','rx','rz','cx','cz'):
            sel = [g for g in grp if g[1] == kind]
            if not sel: continue
            if kind == 'rx':  c.append("RX", [XA[g[2]] for g in sel])
            elif kind == 'rz': c.append("R", [ZA[g[2]] for g in sel])
            elif kind == 'mx':
                c.append("MX", [XA[g[2]] for g in sel])
                for g in sel: rec[('X', g[2], nmeas)] = nmeas; nmeas += 1
            elif kind == 'mz':
                c.append("M", [ZA[g[2]] for g in sel])
                for g in sel: rec[('Z', g[2], nmeas)] = nmeas; nmeas += 1
            else:
                tg = []
                for g in sel: tg += [g[2][0], g[2][1]]
                c.append("CX", tg)
    return c, nmeas, rec, ev

for basis in ('X', 'Z'):
    circ, nmeas, rec, ev = stim_circuit(5, basis)
    # detectors: repeat each ancilla's consecutive measurements
    seq = {}
    for (kind, g, idx) in rec:
        seq.setdefault((kind, g), []).append(rec[(kind, g, idx)])
    d = stim.Circuit(str(circ))
    for (kind, g), ms in seq.items():
        if (basis == 'X') != (kind == 'X'):
            continue
        for j in range(1, len(ms)):
            d.append("DETECTOR", [stim.target_rec(ms[j]-nmeas), stim.target_rec(ms[j-1]-nmeas)])
    try:
        dem = d.detector_error_model(decompose_errors=False, allow_gauge_detectors=False)
        print(f"stim {basis}-memory: {d.num_qubits} qubits, {d.num_detectors} detectors, "
              f"DEM BUILT OK ({dem.num_errors} error mechanisms)")
        s = d.compile_detector_sampler().sample(1)
        print(f"   noiseless detector firings: {int(np.array(s)[0].sum())} / {d.num_detectors}")
    except Exception as e:
        print(f"stim {basis}-memory: DEM FAILED -> {type(e).__name__}: {str(e)[:150]}")
