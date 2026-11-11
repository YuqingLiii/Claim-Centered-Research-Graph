"""
transfer.py -- independent min-plus transfer implementation for d_R^sector(M).

State space Sigma = F2^n / rowspace(H_X)  (Z-memory / X-sector).
Dictionary   w_M([delta], mu) = min |S| over one-round X-sector configurations
             with [E(S)] = [delta], u(S) = mu     (BFS on a Cayley graph:
             the map (delta,mu) -> (delta+E(f), mu+u(f)) is an XOR of the packed index).
Transfer     A[s,s'] = w_M(s'-s, H_Z s), u[s] = 0 iff s = 0, v[s] = 0 iff H_Z s = 0, s != 0.
d_R          = min over paths  = u (x) A^{(x)R} (x) v.

Optional flag bit tracks whether a distinguished class of elementary faults was
used, so that "no minimum witness uses a fault of class C" can be decided by an
exhaustive minimum over the complementary class (see mechanism attribution).
"""

import sat_core as S

INF = 63


def build(sch, cap=None, flagfn=None):
    """Returns a dict with the quotient, dictionary array W, HZsig, and generators."""
    code = sch.code
    Q = S.Quotient(code.xchecks, code.n)
    nB = sch.nB
    gens = S.generators(sch)
    packed = {}
    for (E, u, loc) in gens:
        key = (Q.cls(E) << nB) | u
        fl = 1 if (flagfn and flagfn(loc)) else 0
        # keep the cheapest flag-status: both flag values are separate generators
        packed.setdefault((key, fl), loc)
    genkeys = sorted(set(k for (k, f) in packed))
    genflag = {}
    for (k, f) in packed:
        genflag.setdefault(k, set()).add(f)
    size = 1 << (Q.dim + nB)
    if cap is None:
        cap = INF
    # BFS with flag bit: index = state | (flag << (Q.dim+nB))
    W = bytearray([INF]) * 1
    W = bytearray([INF] * (2 * size))
    W[0] = 0
    frontier = [0]
    lvl = 0
    while frontier and lvl < cap:
        nxt = []
        for s in frontier:
            base = s & (size - 1)
            fl = s >> (Q.dim + nB)
            for k in genkeys:
                for gf in genflag[k]:
                    t = (base ^ k) | ((fl | gf) << (Q.dim + nB))
                    if W[t] == INF:
                        W[t] = lvl + 1
                        nxt.append(t)
        frontier = nxt
        lvl += 1
    HZ = [0] * (1 << Q.dim)
    for i in range(Q.dim):
        HZ[1 << i] = S.syndrome(code, Q.rep(1 << i), "Z")
    for s in range(1, 1 << Q.dim):
        low = s & (-s)
        HZ[s] = HZ[low] ^ HZ[s ^ low]
    return dict(Q=Q, nB=nB, W=W, size=size, HZ=HZ, gens=gens, sch=sch)


def dR(B, Rmax, need_flag=False, min_rounds=1):
    """d_R for R=1..Rmax.  need_flag: require >=1 flagged fault.
    min_rounds: require faults in at least this many distinct rounds."""
    Q, nB, W, size, HZ = B["Q"], B["nB"], B["W"], B["size"], B["HZ"]
    N = 1 << Q.dim
    nf = 2 if need_flag else 1
    nr = min_rounds
    # f[(flag, rounds_used_capped)][sigma]
    def newvec():
        return [[INF] * N for _ in range(2 * (nr + 1))]
    f = newvec()
    f[0][0] = 0
    out = []
    for R in range(1, Rmax + 1):
        g = newvec()
        for st in range(2 * (nr + 1)):
            fl, rc = st // (nr + 1), st % (nr + 1)
            row = f[st]
            for s in range(N):
                c = row[s]
                if c >= INF:
                    continue
                mu = HZ[s]
                base = (s << nB) | mu
                for sp in range(N):
                    idx = base ^ (sp << nB)
                    w0 = W[idx]
                    w1 = W[idx | size]
                    for (w, gf) in ((w0, 0), (w1, 1)):
                        if w >= INF:
                            continue
                        nrc = rc + (1 if w > 0 else 0)
                        if nrc > nr:
                            nrc = nr
                        nst = (fl | gf) * (nr + 1) + nrc
                        if c + w < g[nst][sp]:
                            g[nst][sp] = c + w
        f = g
        best = INF
        for st in range(2 * (nr + 1)):
            fl, rc = st // (nr + 1), st % (nr + 1)
            if need_flag and fl == 0:
                continue
            if rc < nr:
                continue
            for s in range(N):
                if f[st][s] >= INF:
                    continue
                if HZ[s] == 0 and s != 0:
                    best = min(best, f[st][s])
        out.append(best)
    return out
