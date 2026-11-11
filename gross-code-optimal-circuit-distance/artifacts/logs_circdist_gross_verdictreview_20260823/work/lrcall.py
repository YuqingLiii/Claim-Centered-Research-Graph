"""For every one of the four group 3-colourings, and both LRC block orientations, compute
   (i) the order-class triples realisable by a legal 3-colour-tiled STAGGERED left-right circuit
       with 6 CNOT layers per period (depth 8), and
   (ii) their intersection with that colouring's cascade survivors."""
import itertools, json
import numpy as np
from gross import NG
from sched import make_phi, colour_valid
from cascade import CLS_OF, REPS, collect_rules, survivors
import lrc

def realisable(phi, orient):
    al, be = lrc.colours_of_monos(phi)
    if orient == 'LX_first':
        XL = lrc.ok_rows(phi, +1, al); XR = lrc.ok_rows(phi, +1, be)
        ZL = lrc.ok_rows(phi, -1, be); ZR = lrc.ok_rows(phi, -1, al)
    else:   # mirrored: block A = R_X || L_Z, block B = L_X || R_Z
        XL = lrc.ok_rows(phi, +1, al); XR = lrc.ok_rows(phi, +1, be)
        ZL = lrc.ok_rows(phi, -1, be); ZR = lrc.ok_rows(phi, -1, al)
    xt = sorted({lrc.x_triple(a, b) for a in XL for b in XR})
    zt = sorted({lrc.z_triple(a, b) for a in ZL for b in ZR})
    return xt, zt, (len(XL), len(XR), len(ZL), len(ZR))

out = {}
for (s, t) in [(1,1),(1,2),(2,1),(2,2)]:
    phi = make_phi(s, t); assert colour_valid(phi)
    xt, zt, sz = realisable(phi, 'LX_first')
    row = {}
    for sector, tr in (('X', xt), ('Z', zt)):
        r1, r2 = collect_rules(sector, phi)
        alive, _, _ = survivors(r1, r2)
        surv = {tuple(int(x) for x in v) for v in np.argwhere(alive)}
        inter = sorted(set(tr) & surv)
        row[sector] = dict(nrealisable=len(tr), nsurvivors=len(surv),
                           intersection=[list(v) for v in inter])
        print(f"phi={s}a+{t}b sector {sector}: {len(tr)} realisable triples, {len(surv)} cascade "
              f"survivors, intersection {len(inter)} -> {inter}")
    row['blocksizes'] = sz
    out[f"{s}{t}"] = row
json.dump(out, open("lrcall.json", "w"), indent=1)
