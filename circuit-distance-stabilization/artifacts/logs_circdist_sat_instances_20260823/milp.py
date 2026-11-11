"""
milp.py -- THIRD method: exact integer program for d_R^sector(M).

min sum_i x_i   s.t.  A x = 2k (detectors silent, GF(2) via integer slacks),
                      L^(j) x = 2k_j + 1 for one chosen logical j.
Solved with scipy/HiGHS.  Columns are the deduplicated spacetime effect vectors
built by sat_core.spacetime_columns (my own propagation), so this shares no
search code with stim and no state-space code with the transfer engine.
"""

import numpy as np
from scipy.optimize import milp, LinearConstraint, Bounds
import sat_core as S


def dR_milp(sch, R, jlog=None, ub=None, time_limit=600.0, filt=None, require=None):
    """filt(r, loc, E, u) -> bool : column allowed.
       require(r, loc, E, u) -> bool : at least one such column must be used."""
    code = sch.code
    cols, nrow, labels = S.spacetime_columns(sch, R)
    nobs = len(code.zlog)
    ndet = nrow - nobs
    eff = {}
    seen, req = {}, {}
    for c, lab in zip(cols, labels):
        (r, loc) = lab
        if (filt is not None) or (require is not None):
            E, u = S.simulate(sch, [loc])
        if filt is not None and not filt(r, loc, E, u):
            continue
        seen.setdefault(c, lab)
        if require is not None and require(r, loc, E, u):
            req[c] = True
    ucols = sorted(seen)
    m = len(ucols)
    A = np.zeros((ndet + 1, m))
    for i, c in enumerate(ucols):
        for r in range(ndet):
            if (c >> r) & 1:
                A[r, i] = 1
    best = None
    js = range(nobs) if jlog is None else [jlog]
    for j in js:
        for i, c in enumerate(ucols):
            A[ndet, i] = 1 if (c >> (ndet + j)) & 1 else 0
        # variables: x (m binary), k (ndet+1 integers)
        n = m + ndet + 1
        M = np.zeros((ndet + 1, n))
        M[:, :m] = A
        for r in range(ndet + 1):
            M[r, m + r] = -2
        lb = np.zeros(ndet + 1)
        lb[ndet] = 1
        cons = [LinearConstraint(M, lb, lb)]
        if ub is not None:
            cap = np.zeros(n); cap[:m] = 1
            cons.append(LinearConstraint(cap.reshape(1, -1), [0], [ub]))
        if require is not None:
            rq = np.zeros(n)
            for i, c in enumerate(ucols):
                if c in req:
                    rq[i] = 1
            if rq.sum() == 0:
                return None, "no column satisfies require()"
            cons.append(LinearConstraint(rq.reshape(1, -1), [1], [np.inf]))
        cost = np.zeros(n)
        cost[:m] = 1
        integrality = np.ones(n)
        upper = np.concatenate([np.ones(m), np.full(ndet + 1, 10 ** 6)])
        res = milp(c=cost, constraints=cons, integrality=integrality,
                   bounds=Bounds(np.zeros(n), upper),
                   options=dict(time_limit=time_limit, mip_rel_gap=0.0))
        if res.status == 2:
            continue                      # infeasible for this observable
        if res.status != 0:
            return None, "solver status %d (%s) for j=%d" % (res.status, res.message[:40], j)
        v = int(round(res.fun))
        wit = [seen[ucols[i]] for i in range(m) if res.x[i] > 0.5]
        if best is None or v < best[0]:
            best = (v, wit)
    if best is None:
        return None, "infeasible for every observable"
    return best[0], best[1]
