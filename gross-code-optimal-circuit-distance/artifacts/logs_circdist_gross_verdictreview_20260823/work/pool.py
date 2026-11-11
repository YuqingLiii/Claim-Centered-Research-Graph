"""Weight-12 logical pools of the gross code + low-weight logical bases (for SAT encoding)."""
import numpy as np, itertools, time, os
from gross import HX, HZ, N, rref, nullspace, Reducer, TRANS


def isd(Gb, wmax, trials, found, rng):
    nc = Gb.shape[1]
    for _ in range(trials):
        perm = rng.permutation(nc)
        R, _ = rref(Gb[:, perm])
        inv = np.empty(nc, int); inv[perm] = np.arange(nc)
        rows = R[:, inv]
        wts = rows.sum(1)
        for i in np.nonzero(wts <= wmax)[0]:
            found.setdefault(rows[i].tobytes(), rows[i])
        light = np.argsort(wts)[:40]
        for a, b in itertools.combinations(light, 2):
            v = rows[a] ^ rows[b]
            if v.sum() <= wmax:
                found.setdefault(v.tobytes(), v)
        light3 = np.argsort(wts)[:22]
        for a, b, c in itertools.combinations(light3, 3):
            v = rows[a] ^ rows[b] ^ rows[c]
            if v.sum() <= wmax:
                found.setdefault(v.tobytes(), v)
    return found


def build_pool(Hdet, Hstab, seed, trials=600):
    rng = np.random.default_rng(seed)
    Ker = nullspace(Hdet); red = Reducer(Hstab)
    found = {}
    isd(Ker, 12, trials, found, rng)
    words = [v for v in found.values() if v.sum() == 12 and not red.inspan(v)]
    d = {}
    for v in words:
        for p in TRANS:
            u = v[p]; d[u.tobytes()] = u
    P = np.array(list(d.values()), np.uint8)
    assert ((Hdet @ P.T) % 2 == 0).all() and (P.sum(1) == 12).all()
    assert all(not red.inspan(v) for v in P)
    return P


def logical_basis(P, Hstab):
    """pick 12 words from the pool that are independent modulo rowspace(Hstab)."""
    red = Reducer(Hstab)
    rows = []; basis = []
    cur = np.zeros((0, N), np.uint8)
    for v in P:
        w = red.red(v)
        test = np.concatenate([cur, w[None, :]], 0)
        if len(rref(test)[1]) > len(rref(cur)[1]) if len(cur) else True:
            cur = test; basis.append(v)
            if len(basis) == 12:
                break
    assert len(basis) == 12
    return np.array(basis, np.uint8)


def get(cache=True):
    f = "pools.npz"
    if cache and os.path.exists(f):
        z = np.load(f)
        return z['PZ'], z['PX'], z['LX'], z['LZ']
    t0 = time.time()
    PZ = build_pool(HX, HZ, 101)     # Z-type logicals: ker(HX) \ rowspace(HZ)
    PX = build_pool(HZ, HX, 202)     # X-type logicals: ker(HZ) \ rowspace(HX)
    LX = logical_basis(PX, HX)       # 12 X-logicals  -> detect nontriviality of Z-errors
    LZ = logical_basis(PZ, HZ)       # 12 Z-logicals  -> detect nontriviality of X-errors
    np.savez(f, PZ=PZ, PX=PX, LX=LX, LZ=LZ)
    print("pools built in %.1fs: |PZ|=%d |PX|=%d" % (time.time() - t0, len(PZ), len(PX)))
    return PZ, PX, LX, LZ


if __name__ == "__main__":
    PZ, PX, LX, LZ = get(cache=False)
    print("pool sizes:", PZ.shape, PX.shape)
    print("logical basis row weights: LX", sorted(LX.sum(1)), " LZ", sorted(LZ.sum(1)))
    # sanity: LX rows are X-logicals -> commute with HZ, independent mod rowspace(HX)
    assert ((HZ @ LX.T) % 2 == 0).all()
    assert ((HX @ LZ.T) % 2 == 0).all()
    # the 12x12 pairing matrix between LX and LZ must be invertible
    Mp = (LX @ LZ.T) % 2
    print("rank of LX.LZ^T pairing:", len(rref(Mp)[1]))
