"""Generic one-round LIFT machinery for single-ancilla CSS syndrome extraction.

Frozen model (公共定义 / circdist_lift_iff_proof_20260820.md sections 1.1-1.7):
  A = X-checks (ancilla is CONTROL of CNOTs onto data), B = Z-checks (ancilla is TARGET).
  Z-memory sector -> X-sector faults; detectors are the Z-checks (B).
  residual set  E  =  {suffixes of X-check CNOT orders} u {singletons} u {empty}
  s_b(E) = |supp(b) cap E| mod 2                       (Def 1.10)
  u_b(hook S of a) = #{q in supp(b) cap S : t(q->b) > t(a->q)} mod 2      (1.13.2)
  U({q})  = { suffixes of q's Z-gate time order }                        (1.13.1 / Def 1.15)
  repair(gamma) = min over (rounds r_i, u_i in U(E_i)) of wt(A_0 + xC)   (Def 5.2)
  criterion (Thm 5.7): d_circ = d_eff  iff some minimum-weight gamma has repair = 0.

Everything is plain python ints used as F2 bit-vectors.  Independent of all prior campaign code.
"""
import itertools


# ---------------------------------------------------------------- generic CSS instance
class CSS:
    """checks given as lists of qubit indices.  n qubits."""

    def __init__(self, n, Xchecks, Zchecks):
        self.n = n
        self.Xchecks = [sorted(c) for c in Xchecks]
        self.Zchecks = [sorted(c) for c in Zchecks]
        self.nA = len(Xchecks)
        self.nB = len(Zchecks)
        self.Xmask = [self._m(c) for c in self.Xchecks]
        self.Zmask = [self._m(c) for c in self.Zchecks]
        # incidence
        self.Xof = [[] for _ in range(n)]   # X-checks containing q
        self.Zof = [[] for _ in range(n)]   # Z-checks containing q
        for i, c in enumerate(self.Xchecks):
            for q in c:
                self.Xof[q].append(i)
        for i, c in enumerate(self.Zchecks):
            for q in c:
                self.Zof[q].append(i)
        # s of a singleton, as a mask over B
        self.sq = [self._m(self.Zof[q]) for q in range(n)]
        # s of a singleton in the mirror sector, as a mask over A
        self.sqX = [self._m(self.Xof[q]) for q in range(n)]
        # overlapping (X-check, Z-check) pairs and their shared qubits
        self.overlaps = []
        for i, a in enumerate(self.Xchecks):
            sa = set(a)
            for j, b in enumerate(self.Zchecks):
                sh = sorted(sa & set(b))
                if sh:
                    self.overlaps.append((i, j, sh))
        self.overlap_sizes = sorted(set(len(o[2]) for o in self.overlaps))

    @staticmethod
    def _m(lst):
        v = 0
        for x in lst:
            v |= 1 << x
        return v

    def commutes(self):
        return all(bin(a & b).count('1') % 2 == 0
                   for a in self.Xmask for b in self.Zmask)


def popc(x):
    return bin(x).count('1')


# ---------------------------------------------------------------- schedule
class Schedule:
    """tX[(a,q)] = time of CNOT anc(a)->q ;  tZ[(q,b)] = time of CNOT q->anc(b)."""

    def __init__(self, css, tX, tZ):
        self.css = css
        self.tX = tX
        self.tZ = tZ

    # ---- legality: at each time step every qubit (data or ancilla) in <=1 gate
    def legal(self):
        used = {}
        for (a, q), t in self.tX.items():
            for node in (('A', a), ('q', q)):
                if (node, t) in used:
                    return False
                used[(node, t)] = 1
        for (q, b), t in self.tZ.items():
            for node in (('B', b), ('q', q)):
                if (node, t) in used:
                    return False
                used[(node, t)] = 1
        return True

    # ---- (MC), Definition 2.1
    def mc_violations(self):
        tX, tZ = self.tX, self.tZ
        bad = []
        for (a, b, sh) in self.css.overlaps:
            c = 0
            for q in sh:
                if tZ[(q, b)] < tX[(a, q)]:
                    c ^= 1
            if c:
                bad.append((a, b))
        return bad

    def eps(self):
        """eps[(a,b)] = 1 iff b's CNOTs on the a-b overlap come BEFORE a's.  Well defined
        exactly when (MC) holds and every overlap has size <= 2."""
        tX, tZ = self.tX, self.tZ
        return {(a, b): int(tZ[(sh[0], b)] < tX[(a, sh[0])])
                for (a, b, sh) in self.css.overlaps}

    def interleaved_pairs(self):
        """SBB per-pair non-interleaving: all of a's CNOTs on the overlap before all of b's
        (or vice versa).  Counts pairs where that fails."""
        tX, tZ = self.tX, self.tZ
        n = 0
        for (a, b, sh) in self.css.overlaps:
            A = [tX[(a, q)] for q in sh]
            Bt = [tZ[(q, b)] for q in sh]
            if not (max(A) < min(Bt) or max(Bt) < min(A)):
                n += 1
        return n

    def strict_interleaved_pairs(self):
        """the STRONG per-pair reading: all of a's SIX CNOTs before all of b's six, or vice
        versa (SBB's 'non-interleaved' applied pairwise to whole checks)."""
        tX, tZ = self.tX, self.tZ
        css = self.css
        n = 0
        for (a, b, sh) in css.overlaps:
            A = [tX[(a, q)] for q in css.Xchecks[a]]
            Bt = [tZ[(q, b)] for q in css.Zchecks[b]]
            if not (max(A) < min(Bt) or max(Bt) < min(A)):
                n += 1
        return n

    def globally_interleaved(self):
        """Definition 1.3: non-interleaved = one whole block before the other."""
        mx = max(self.tX.values()); mnx = min(self.tX.values())
        mz = max(self.tZ.values()); mnz = min(self.tZ.values())
        return not (mx < mnz or mz < mnx)


# ---------------------------------------------------------------- one-round data, Z-memory
class Sector:
    """Z-memory sector (hooks from X-check ancillas, detectors = Z-checks).
    Set mirror=True for the X-memory sector (roles of A and B swapped)."""

    def __init__(self, css, sched, mirror=False):
        self.css = css
        self.sched = sched
        self.mirror = mirror
        if not mirror:
            self.hook_checks = css.Xchecks          # ancillas that make hooks
            self.det_of_q = css.Zof                 # detectors touched by data qubit q
            self.sq = css.sq
            self.ndet = css.nB
            self.tH = lambda a, q: sched.tX[(a, q)]     # time of hook-ancilla -> q
            self.tD = lambda q, b: sched.tZ[(q, b)]     # time of q -> detector ancilla
        else:
            self.hook_checks = css.Zchecks
            self.det_of_q = css.Xof
            self.sq = css.sqX
            self.ndet = css.nA
            self.tH = lambda a, q: sched.tZ[(q, a)]
            self.tD = lambda q, b: sched.tX[(b, q)]
        self._build()

    def _build(self):
        # per-check CNOT order (time sorted) -> suffixes
        self.order = [sorted(c, key=lambda q: self.tH(i, q))
                      for i, c in enumerate(self.hook_checks)]
        # per data qubit: detector-gate time order  (b_1 < b_2 < b_3 ...)
        self.qorder = [sorted(self.det_of_q[q], key=lambda b: self.tD(q, b))
                       for q in range(self.css.n)]
        # U({q}) = suffix masks of qorder[q]  (Def 1.15) -- nested chain incl. 0 and full
        self.Uq = []
        for q in range(self.css.n):
            ch = [0]
            v = 0
            for b in reversed(self.qorder[q]):
                v |= 1 << b
                ch.append(v)
            self.Uq.append(ch)           # length deg+1, ch[0]=0, ch[-1]=s({q})

    # s of a set of qubits, as detector mask
    def s_of(self, qs):
        v = 0
        for q in qs:
            v ^= self.sq[q]
        return v

    def hook(self, a, k):
        """suffix of length k of check a's CNOT order."""
        return self.order[a][len(self.order[a]) - k:]

    def u_hook(self, a, S):
        """u(S) for the hook residual S (suffix of a's order), computed from the raw times."""
        u = 0
        for b in range(self.ndet):
            cnt = 0
            for q in S:
                if b in self.det_of_q[q] and self.tD(q, b) > self.tH(a, q):
                    cnt += 1
            if cnt % 2:
                u |= 1 << b
        return u

    def classify_hook(self, a, S):
        s = self.s_of(S)
        u = self.u_hook(a, S)
        if s == 0 and u == 0:
            return 'trivial', u, s
        if u == 0 or u == s:
            return 'horizontal', u, s
        if s == 0:
            return 'VERTICAL', u, s
        return 'diagonal', u, s


# ---------------------------------------------------------------- repair
def sameround_repair0(sec, hook_a, S, singles):
    """Is there a SAME-ROUND repair certificate of weight 0 for
       gamma = {hook S of check hook_a} u {singletons in `singles`} ?
    Condition:  u(S) + sum_q u_q = 0  with u_q in U({q}).   (Def 5.2 with all r_i equal;
    then B = sum s_i = 0, C = 0, so wt(A_0 + xC) = |sum u_i|.)
    Returns a witness (list of chain indices) or None.  Meet in the middle."""
    target = sec.u_hook(hook_a, S)
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


def multiround_repair0(sec, hook_a, S, singles, maxgroups=3):
    """General repair(gamma)=0 test allowing several rounds.  gamma is split into
    consecutive round-groups G_0..G_m; condition (LIFT'):
        sum_{i in G_r} u_i  =  sum_{r'<r} s(G_{r'})    for every r,
    and the accumulated syndrome must vanish at any empty round, so the groups are
    consecutive.  Exhaustive over set partitions into <= maxgroups ordered groups is
    exponential; we run it only for small gamma or as a spot check with random splits."""
    items = [('h', hook_a, S)] + [('s', None, [q]) for q in singles]
    n = len(items)
    if maxgroups < 2:
        return None
    # ordered set partitions into exactly g nonempty groups, g = 2..maxgroups
    def s_item(it):
        return sec.s_of(it[2])

    def U_item(it):
        if it[0] == 'h':
            return [sec.u_hook(it[1], it[2])]
        return sec.Uq[it[2][0]]

    for g in range(2, maxgroups + 1):
        for assign in itertools.product(range(g), repeat=n):
            if len(set(assign)) != g:
                continue
            groups = [[items[i] for i in range(n) if assign[i] == r] for r in range(g)]
            acc = 0
            ok = True
            for r in range(g):
                need = acc                      # sum_{r'<r} s(G_{r'})
                # can we hit `need` with the u-choices in this group?
                opts = [U_item(it) for it in groups[r]]
                found = False
                for combo in itertools.product(*opts):
                    v = 0
                    for x in combo:
                        v ^= x
                    if v == need:
                        found = True
                        break
                if not found:
                    ok = False
                    break
                for it in groups[r]:
                    acc ^= s_item(it)
            if ok and acc == 0:
                return assign
    return None
