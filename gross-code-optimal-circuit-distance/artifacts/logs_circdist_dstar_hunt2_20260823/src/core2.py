"""CIRCDIST.gross D* hunt, STAGE 2 -- independent rebuild of the gross code, the wave-37 tiled
gap candidate, the one-round LIFT sector data, and the exact d_ext stratum machinery.

Written fresh this session.  The ONLY imported data are the two weight-12 logical seed files
w12.txt / w12X.txt from artifacts/logs_circdist_gross_links_20260823/ (every element revalidated
here) and the 36-integer candidate schedule tiled_gapcand_32.json from the stage-1 log dir.

Frozen model (公共定义 / circdist_lift_iff_proof_20260820.md 1.1-1.7, 5.1-5.5):
  A = X-checks (ancilla CONTROLS the CNOTs onto data), B = Z-checks (ancilla is TARGET).
  Z-memory sector -> X-type faults; detectors are the Z-checks.
  residual set E(M) = {suffixes of X-check CNOT orders} u {singletons} u {empty}
  s(E) = H_Z E ; u_b(hook S of a) = #{q in supp(b) cap S : t(q->b) > t(a->q)} mod 2
  U({q}) = suffixes of q's detector-gate time order (nested chain, 4 elements: deg 3)
  d_eff = d_ext(E(M)) = min #residuals whose XOR is a NONTRIVIAL logical of the sector.
"""
import itertools, json, os, sys

L, EM = 12, 6
NG = L * EM          # 72 group elements
N = 2 * NG           # 144 data qubits
Amon = [(3, 0), (0, 1), (0, 2)]     # A = x^3 + y + y^2
Bmon = [(0, 3), (1, 0), (2, 0)]     # B = y^3 + x + x^2

BASE = '<repo>/'
LINKS = BASE + 'artifacts/logs_circdist_gross_links_20260823/'
STAGE1 = BASE + 'artifacts/logs_circdist_dstar_hunt1_20260823/'


def gi(i, j):
    return (i % L) * EM + (j % EM)


def gadd(g, d):
    i, j = divmod(g, EM)
    return gi(i + d[0], j + d[1])


# ------------------------------------------------------------------ code
# H_X row g : left cols g+Amon[i] (SLOT i), right cols NG+g+Bmon[j] (SLOT j)
Xslots = [[gadd(g, m) for m in Amon] + [NG + gadd(g, m) for m in Bmon] for g in range(NG)]
# H_Z row g : left cols g-Bmon[j] (SLOT j), right cols NG+g-Amon[i] (SLOT i)
Zslots = [[gadd(g, (-m[0], -m[1])) for m in Bmon] +
          [NG + gadd(g, (-m[0], -m[1])) for m in Amon] for g in range(NG)]
Xchk = [sorted(s) for s in Xslots]
Zchk = [sorted(s) for s in Zslots]


def msk(lst):
    v = 0
    for x in lst:
        v |= 1 << x
    return v


HXm = [msk(c) for c in Xchk]
HZm = [msk(c) for c in Zchk]
Xof = [[] for _ in range(N)]     # X-checks containing q
Zof = [[] for _ in range(N)]     # Z-checks containing q
for i, c in enumerate(Xchk):
    for q in c:
        Xof[q].append(i)
for i, c in enumerate(Zchk):
    for q in c:
        Zof[q].append(i)
sqZ = [msk(Zof[q]) for q in range(N)]    # syndrome of singleton q on Z-detectors
sqX = [msk(Xof[q]) for q in range(N)]


def popc(x):
    return bin(x).count('1')


def bits(w):
    out = []
    while w:
        b = w & -w
        out.append(b.bit_length() - 1)
        w ^= b
    return out


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


def load_seeds(path):
    out = []
    for line in open(path):
        a, b, c, d = [int(t, 16) for t in line.split()]
        out.append((a | (b << 64)) | ((c | (d << 64)) << NG))
    return out


def build_pool(seedfile, stabrows, checkrows):
    """expand seeds under the 72 translations, drop stabilisers, validate every element."""
    S = set()
    for w in load_seeds(seedfile):
        for di in range(L):
            for dj in range(EM):
                S.add(trans(w, (di, dj)))
    R, piv = rref(stabrows)
    pool = sorted(w for w in S if not inspan(w, R, piv))
    bad = sum(1 for w in pool if popc(w) != 12 or any(popc(w & h) % 2 for h in checkrows))
    return pool, len(S), bad


# ------------------------------------------------------------------ schedule
def cls(g):
    i, j = divmod(g, EM)
    return (i + j) % 3


def build_tiled(T):
    """T: 36 ints.  XL[c][i] = T[3c+i], XR[c][j] = T[9+3c+j],
       ZL[c][j] = T[18+3c+j], ZR[c][i] = T[27+3c+i]."""
    XL = [T[3 * c:3 * c + 3] for c in range(3)]
    XR = [T[9 + 3 * c:12 + 3 * c] for c in range(3)]
    ZL = [T[18 + 3 * c:21 + 3 * c] for c in range(3)]
    ZR = [T[27 + 3 * c:30 + 3 * c] for c in range(3)]
    tX, tZ = {}, {}
    for g in range(NG):
        c = cls(g)
        for i, m in enumerate(Amon):
            tX[(g, gadd(g, m))] = XL[c][i]
        for j, m in enumerate(Bmon):
            tX[(g, NG + gadd(g, m))] = XR[c][j]
        for j, m in enumerate(Bmon):
            tZ[(gadd(g, (-m[0], -m[1])), g)] = ZL[c][j]
        for i, m in enumerate(Amon):
            tZ[(NG + gadd(g, (-m[0], -m[1])), g)] = ZR[c][i]
    return tX, tZ


def legal(tX, tZ):
    used = set()
    for (a, q), t in tX.items():
        for node in (('A', a), ('q', q)):
            if (node, t) in used:
                return False
            used.add((node, t))
    for (q, b), t in tZ.items():
        for node in (('B', b), ('q', q)):
            if (node, t) in used:
                return False
            used.add((node, t))
    return True


def overlaps():
    out = []
    for i, a in enumerate(Xchk):
        sa = set(a)
        for j, b in enumerate(Zchk):
            sh = sorted(sa & set(b))
            if sh:
                out.append((i, j, sh))
    return out


OV = overlaps()


def mc_violations(tX, tZ):
    bad = []
    for (a, b, sh) in OV:
        c = 0
        for q in sh:
            if tZ[(q, b)] < tX[(a, q)]:
                c ^= 1
        if c:
            bad.append((a, b))
    return bad


def interleave_stats(tX, tZ):
    pi = si = 0
    for (a, b, sh) in OV:
        A = [tX[(a, q)] for q in sh]
        B = [tZ[(q, b)] for q in sh]
        if not (max(A) < min(B) or max(B) < min(A)):
            pi += 1
        A2 = [tX[(a, q)] for q in Xchk[a]]
        B2 = [tZ[(q, b)] for q in Zchk[b]]
        if not (max(A2) < min(B2) or max(B2) < min(A2)):
            si += 1
    mx, mnx = max(tX.values()), min(tX.values())
    mz, mnz = max(tZ.values()), min(tZ.values())
    return pi, si, not (mx < mnz or mz < mnx)


# ------------------------------------------------------------------ sector
class Sector:
    """mirror=False: Z-memory (hooks from X-check ancillas, detectors = Z-checks).
       mirror=True : X-memory."""

    def __init__(self, tX, tZ, mirror=False):
        self.mirror = mirror
        if not mirror:
            self.hchk, self.detof, self.sq, self.ndet = Xchk, Zof, sqZ, NG
            self.tH = lambda a, q: tX[(a, q)]
            self.tD = lambda q, b: tZ[(q, b)]
        else:
            self.hchk, self.detof, self.sq, self.ndet = Zchk, Xof, sqX, NG
            self.tH = lambda a, q: tZ[(q, a)]
            self.tD = lambda q, b: tX[(b, q)]
        # CNOT order of each hook check, EARLIEST FIRST; suffix of length l = last l entries
        self.order = [sorted(c, key=lambda q: self.tH(i, q)) for i, c in enumerate(self.hchk)]
        self.qorder = [sorted(self.detof[q], key=lambda b: self.tD(q, b)) for q in range(N)]
        self.Uq = []
        for q in range(N):
            ch, v = [0], 0
            for b in reversed(self.qorder[q]):
                v |= 1 << b
                ch.append(v)
            self.Uq.append(ch)
        self.hm = [msk(c) for c in self.hchk]

    def suffix(self, a, l):
        return self.order[a][6 - l:]

    def s_of(self, qs):
        v = 0
        for q in qs:
            v ^= self.sq[q]
        return v

    def u_hook(self, a, S):
        u = 0
        for q in S:
            for b in self.detof[q]:
                if self.tD(q, b) > self.tH(a, q):
                    u ^= 1 << b
        return u

    def classify(self, a, S):
        s, u = self.s_of(S), self.u_hook(a, S)
        if s == 0 and u == 0:
            return 'trivial'
        if u == 0 or u == s:
            return 'horizontal'
        if s == 0:
            return 'VERTICAL'
        return 'diagonal'


# ------------------------------------------------------------------ residual column set
# WLOG-reduction lemmas (proved in the artifact, section 2):
#   R1  a length-6 suffix is supp(a) in rowspace(H_X); deleting it and replacing V by
#       V + supp(a) (same logical class) strictly LOWERS the fault count.  So l <= 5.
#   R2  a length-1 suffix has the same support as a singleton, so it may be replaced by the
#       singleton at no cost; and U(1-suffix) is a single element of U(singleton), so the
#       singleton also dominates it for the repair test.  So l >= 2.
# The XOR of the suffixes of lengths in K (subset of {2,3,4,5}) is the set of positions p
# (counted from the END, p = 1 is the LAST CNOT) with #{l in K : l >= p} odd.
def kset_positions(K):
    return tuple(p for p in range(1, 6) if sum(1 for l in K if l >= p) % 2)


# options with POSITIVE raw gain g = |C| - n  (drop-lemma: any option with g <= 0 may be
# deleted from an optimal configuration without increasing the cost)
OPTS = []
for r in range(1, 5):
    for K in itertools.combinations((2, 3, 4, 5), r):
        P = kset_positions(K)
        if len(P) - len(K) >= 1:
            OPTS.append((K, P, len(K), len(P)))
OPTS.sort(key=lambda o: (o[2], o[0]))


def opt_mask(sec, a, P):
    """qubit mask of the option with position-set P on hook check a (positions from the end)."""
    o = sec.order[a]
    v = 0
    for p in P:
        v |= 1 << o[6 - p]
    return v


# ------------------------------------------------------------------ repair
def sameround_repair0(sec, hooks, singles):
    """hooks: list of (a, qubit-list).  singles: list of qubits.
    Same-round repair 0  <=>  sum_hooks u(S) + sum_singles u_q = 0, u_q in U({q}).
    (all faults in one round => B = sum s_i = 0 => C = 0 => repair = |sum u_i|)"""
    target = 0
    for (a, S) in hooks:
        target ^= sec.u_hook(a, S)
    m = len(singles)
    h = m // 2
    left, right = singles[:h], singles[h:]
    tab = {}
    for combo in itertools.product(*[range(len(sec.Uq[q])) for q in left]):
        v = 0
        for q, i in zip(left, combo):
            v ^= sec.Uq[q][i]
        tab.setdefault(v, combo)
    for combo in itertools.product(*[range(len(sec.Uq[q])) for q in right]):
        v = 0
        for q, i in zip(right, combo):
            v ^= sec.Uq[q][i]
        w = tab.get(v ^ target)
        if w is not None:
            return list(w) + list(combo)
    return None


def multiround_repair0(sec, hooks, singles, maxg=2):
    """(LIFT') repair 0 with gamma split into g consecutive round-groups:
       sum_{i in G_r} u_i = sum_{r'<r} s(G_{r'}) for every r, and the accumulated
       syndrome vanishes at the end."""
    items = [('h', a, S) for (a, S) in hooks] + [('s', None, [q]) for q in singles]
    n = len(items)
    Us, Ss = [], []
    for it in items:
        Ss.append(sec.s_of(it[2]))
        Us.append([sec.u_hook(it[1], it[2])] if it[0] == 'h' else sec.Uq[it[2][0]])
    for g in range(2, maxg + 1):
        for assign in itertools.product(range(g), repeat=n):
            if len(set(assign)) != g:
                continue
            acc, ok = 0, True
            for r in range(g):
                grp = [i for i in range(n) if assign[i] == r]
                need = acc
                h = len(grp) // 2
                tab = set()
                for cmb in itertools.product(*[Us[i] for i in grp[:h]]):
                    v = 0
                    for x in cmb:
                        v ^= x
                    tab.add(v)
                found = False
                for cmb in itertools.product(*[Us[i] for i in grp[h:]]):
                    v = 0
                    for x in cmb:
                        v ^= x
                    if (v ^ need) in tab:
                        found = True
                        break
                if not found:
                    ok = False
                    break
                for i in grp:
                    acc ^= Ss[i]
            if ok and acc == 0:
                return assign
    return None


# ------------------------------------------------------------------ convenience
def load_candidate():
    T = json.load(open(STAGE1 + 'tiled_gapcand_32.json'))
    return build_tiled(T), T


def pools():
    """(Zmem pool, Xmem pool).  Z-memory faults are X-type: kernel of H_Z, mod rowspace H_X."""
    pz, nz, bz = build_pool(LINKS + 'w12X.txt', HXm, HZm)     # X-type logicals -> Z-memory
    px, nx, bx = build_pool(LINKS + 'w12.txt', HZm, HXm)      # Z-type logicals -> X-memory
    return (pz, nz, bz), (px, nx, bx)
