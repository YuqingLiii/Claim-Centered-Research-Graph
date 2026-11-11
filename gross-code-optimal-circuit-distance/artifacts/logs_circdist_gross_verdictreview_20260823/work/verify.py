"""Independent re-verification of the SAT witnesses: exact F2 algebra from the definitions, an
own-code Pauli-frame simulation of the literal alternating-XZ circuit with the tiled orders, and
stim (Z-sector witnesses)."""
import json, glob, sys
import numpy as np
from gross import NG, N, HX, HZ, xcheck_nb, zcheck_nb, Reducer
from sched import make_phi
from cert import tiled_orders
import dext, simverify, stimverify

phi = make_phi(1, 1)
rows = []
for f in sorted(glob.glob('out/*_W10.json')):
    try: r = json.load(open(f))
    except: continue
    if r['verdict'] != 'SAT': continue
    rows.append(r)
which = sys.argv[1:] if len(sys.argv) > 1 else None
nz = 0
for r in rows:
    sec = r['sector']; tr = tuple(r['triple'])
    tag = f"{sec}{tr}"
    if which and tag not in which: continue
    orders, Hstab = tiled_orders(sec, phi, tr)
    ctx, Hst = dext.sector_ctx(orders, sec)
    R = [(a, b) for a, b in r['R']]
    D = np.zeros(N, np.uint8); D[r['D']] = 1
    E = np.zeros(N, np.uint8); E[r['E']] = 1
    alg = dext.verify_witness(ctx, E, R, D, Hst)
    out = {'triple': tr, 'sector': sec, 'algebra': alg}
    if sec == 'Z':
        out['circuit'] = simverify.verify(orders, R, r['D'], verbose=False)
        oX = [[q for q, s, i in xcheck_nb(g)] for g in range(NG)]
        if nz < 12:
            out['stim'] = stimverify.check(oX, orders, R, r['D']); nz += 1
    else:
        out['circuit'] = simverify.verify_x(orders, R, r['D'], verbose=False)
    print(json.dumps(out))
