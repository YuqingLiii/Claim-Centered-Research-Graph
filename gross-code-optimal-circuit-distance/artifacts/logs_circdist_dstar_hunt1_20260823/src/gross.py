"""Independent Gross-code [[144,12,12]] build + weight-12 logical pool loading/validation.
G = Z_12 x Z_6, index (i,j) -> i*6+j.  A = x^3+y+y^2, B = y^3+x+x^2.
H_X = [A|B], H_Z = [B^T|A^T].  Left qubits 0..71, right qubits 72..143.
"""
import itertools, os
from lift import CSS, popc

L, EM = 12, 6
NG = L * EM
N = 2 * NG
Amon = [(3, 0), (0, 1), (0, 2)]
Bmon = [(0, 3), (1, 0), (2, 0)]


def gi(i, j):
    return (i % L) * EM + (j % EM)


def gadd(g, d):
    i, j = divmod(g, EM)
    return gi(i + d[0], j + d[1])


# H_X row g : left cols g+Amon[i]  (slot i), right cols NG+g+Bmon[j] (slot j)
Xchecks, Xslots = [], []
for g in range(NG):
    sl = [gadd(g, m) for m in Amon] + [NG + gadd(g, m) for m in Bmon]
    Xslots.append(sl)
    Xchecks.append(sorted(sl))
# H_Z row g : left cols g-Bmon[j] (slot j), right cols NG+g-Amon[i] (slot i)
Zchecks, Zslots = [], []
for g in range(NG):
    sl = [gadd(g, (-m[0], -m[1])) for m in Bmon] + [NG + gadd(g, (-m[0], -m[1])) for m in Amon]
    Zslots.append(sl)
    Zchecks.append(sorted(sl))

CSSG = CSS(N, Xchecks, Zchecks)


# ---------------------------------------------------------------- F2 linear algebra
def rref(rows, n=N):
    rows = list(rows)
    piv = []
    r = 0
    for c in range(n - 1, -1, -1):
        p = None
        for k in range(r, len(rows)):
            if (rows[k] >> c) & 1:
                p = k
                break
        if p is None:
            continue
        rows[r], rows[p] = rows[p], rows[r]
        for k in range(len(rows)):
            if k != r and ((rows[k] >> c) & 1):
                rows[k] ^= rows[r]
        piv.append(c)
        r += 1
        if r == len(rows):
            break
    return [x for x in rows[:r] if x], piv


def inspan(v, R, piv):
    for rr, c in zip(R, piv):
        if (v >> c) & 1:
            v ^= rr
    return v == 0


def trans(w, d):
    r = 0
    for half in (0, NG):
        t = (w >> half) & ((1 << NG) - 1)
        while t:
            b = t & -t
            p = b.bit_length() - 1
            t ^= b
            r |= 1 << (half + gadd(p, d))
    return r


def load_pool(path):
    """seed weight-12 codewords, hex quads (low64 low, high, low64 high-half, high)."""
    out = []
    for line in open(path):
        a, b, c, d = [int(t, 16) for t in line.split()]
        out.append((a | (b << 64)) | ((c | (d << 64)) << NG))
    return out


def expand(seeds, Hstab_rows):
    """close under the 72 translations, drop stabilisers, return the nontrivial logicals."""
    S = set()
    for w in seeds:
        for di in range(L):
            for dj in range(EM):
                S.add(trans(w, (di, dj)))
    R, piv = rref(Hstab_rows)
    return sorted(w for w in S if not inspan(w, R, piv)), len(S)


HXm = CSSG.Xmask
HZm = CSSG.Zmask

if __name__ == '__main__':
    print("commutation failures:", sum(1 for a in HXm for b in HZm if popc(a & b) % 2))
    ov = {}
    for (a, b, sh) in CSSG.overlaps:
        ov[len(sh)] = ov.get(len(sh), 0) + 1
    print("overlap-size histogram over ALL (X,Z) pairs: {0: %d, %s}"
          % (72 * 72 - len(CSSG.overlaps), ov))
    lr = set()
    for (a, b, sh) in CSSG.overlaps:
        lr.add((sum(1 for q in sh if q < NG), sum(1 for q in sh if q >= NG)))
    print("(left,right) split of every overlap:", lr)
    rx = len(rref(HXm)[0]); rz = len(rref(HZm)[0])
    print("rank HX =", rx, " rank HZ =", rz, " k =", N - rx - rz)
    base = ('<repo>/'
            'artifacts/logs_circdist_gross_links_20260823/')
    for tag, fn, stab in (('X-sector (ker HZ, mod rowspace HX)', 'w12X.txt', HXm),
                          ('Z-sector (ker HX, mod rowspace HZ)', 'w12.txt', HZm)):
        seeds = load_pool(base + fn)
        chk = HZm if 'w12X' in fn else HXm
        bad = sum(1 for w in seeds if popc(w) != 12 or any(popc(w & h) % 2 for h in chk))
        pool, nS = expand(seeds, stab)
        print("%s: seeds %d invalid %d -> %d wt-12 in kernel, %d NONTRIVIAL logicals"
              % (tag, len(seeds), bad, nS, len(pool)))
