"""Exact certification of d_ext for the surviving three-colour-tiled assignments."""
import numpy as np, itertools, sys, time, json
from gross import NG, N, zcheck_nb, xcheck_nb, HX, HZ
from sched import make_phi
from cascade import REPS, sector_data
import dext


def tiled_orders(sector, phi, triple):
    slots, Pl, Hstab, Hdet = sector_data(sector)
    orders = []
    for g in range(NG):
        sig = REPS[triple[int(phi[g])]]
        orders.append([slots[g][k] for k in sig])
    return orders, Hstab


def certify(sector, phi, triple, Wlist=(10,), verbose=True):
    orders, Hstab = tiled_orders(sector, phi, triple)
    ctx, Hst = dext.sector_ctx(orders, sector)
    out = {}
    for W in Wlist:
        sat, wit, el, ncls = dext.query(ctx, W, Hst)
        out[W] = (sat, wit[3] if sat else None, el, ncls)
        if verbose:
            if sat:
                print(f"   sector {sector} triple {triple} W={W}: SAT  {wit[3]}  ({el:.1f}s)")
            else:
                print(f"   sector {sector} triple {triple} W={W}: UNSAT  ({el:.1f}s, {ncls} clauses)")
    return out, ctx, Hst


if __name__ == "__main__":
    s_par, t_par = 1, 2
    phi = make_phi(s_par, t_par)
    triples = [(2, 2, 2), (2, 2, 9), (2, 9, 2), (2, 9, 9),
               (9, 2, 2), (9, 2, 9), (9, 9, 2), (9, 9, 9)]
    which = sys.argv[1:] if len(sys.argv) > 1 else None
    for sector in ('Z', 'X'):
        for tr in triples:
            if which and f"{sector}{tr[0]}{tr[1]}{tr[2]}" not in which:
                continue
            t0 = time.time()
            certify(sector, phi, tr, Wlist=(10,))
            sys.stdout.flush()
