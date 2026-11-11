"""d_ext(R) for R = the residual set of a SINGLE check -- the object [SBB26] Prop. 4 and the
90 -> 45 pruning actually bound.  Theorem 1 gives d'_circ <= d_ext(R) for every R subset of E,
and d'_circ = d_ext(E) for the FULL set.  This script measures the gap between the two."""
import sys, time
import numpy as np
from gross import NG, N, HX, HZ, zcheck_nb, xcheck_nb, Reducer
from sched import make_phi
from cert import tiled_orders
from cascade import REPS
import dext, dext2


def single_ctx(orders, sector, keep):
    ctx, Hstab = dext.sector_ctx(orders, sector)
    for c in range(NG):
        if c not in keep:
            ctx.res[c] = [(), (), ()]
    ctx.hit = [[] for _ in range(N)]
    for c in range(NG):
        for k in range(3):
            for q in ctx.res[c][k]:
                ctx.hit[q].append((c, k))
    return ctx, Hstab


if __name__ == "__main__":
    phi = make_phi(1, 2)
    for sector in ('Z', 'X'):
        for tr in [(2, 2, 9)]:
            orders, _ = tiled_orders(sector, phi, tr)
            for keep in ({0}, {0, 1}):
                ctx, Hstab = single_ctx(orders, sector, keep)
                for W in (10, 11):
                    sat, wit, el, ncls = dext.query(ctx, W, Hstab)
                    print(f"sector {sector} triple {tr} R = residuals of checks {sorted(keep)} "
                          f"W={W}: {'SAT ' + str(wit[3]) if sat else 'UNSAT'}  ({el:.1f}s)")
                    sys.stdout.flush()
                    if sat:
                        break
