"""Independent adversarial re-implementation for CIRCDIST.sat.instances review (2026-08-23).

Written from the STATEMENTS of Definitions 2.1-2.11 (circdist_sat_transfer_proof_20260823.md
sec.2) and CIRCDIST_PROBLEMS.md 公共定义 only.  No code from any prior circdist artifact was
read or reused.  Author: independent reviewer session.

Conventions implemented verbatim:
  * Def 2.3  one ancilla per check; X-ancilla = control of one CNOT onto each q in supp(a);
             Z-ancilla = target of one CNOT from each q in supp(b).
  * Def 2.4  legal = at most one 2q gate per physical qubit per time step.
  * Def 2.5  (MC): c_ab = #{q in supp(a)&supp(b) : t(q->b) < t(a->q)} == 0 mod 2 for all a,b.
  * Def 2.6  C_R^Z: ideal |0>^n init, R verbatim rounds, ideal transversal Z readout.
             m_{b,-1}=0, m_{b,R}= xor_{q in supp(b)} rho_q.
  * Def 2.7  D_{b,r}=m_{b,r}+m_{b,r-1}, r=0..R ; D_{a,r}=m_{a,r}+m_{a,r-1}, r=1..R-1.
             observables lambda^{(j)} = xor_{q in supp(Z_L^{(j)})} rho_q.   (mirror for X-memory)
  * Def 2.8  locations: every CNOT (15 non-identity 2q Paulis after it); every (qubit,layer) with
             the qubit idle, and every ancilla immediately after preparation (3 Paulis); every
             recorded outcome (classical flip).  init/readout ideal.  |F| = #locations used.
  * Def 2.11 d_R^sigma = min |F| undetectable & logical;  d_R = min(d_R^Z, d_R^X).

Signature engine: exact F2 backward propagation.  For every slot (round r, "after layer t",
t = -1..T-1) we hold the signature of X_q and Z_q inserted at that slot, as a pair of bitmasks
(detector mask, observable mask).  Backward recursion across a CNOT layer:
    sig_before(X_c) = sig_after(X_c) ^ sig_after(X_t)      (control c, target t)
    sig_before(Z_t) = sig_after(Z_t) ^ sig_after(Z_c)
    sig_before(X_t) = sig_after(X_t) ;  sig_before(Z_c) = sig_after(Z_c)
Across a measurement boundary the measured ancilla's frame is zeroed and the anticommuting
component picks up the record's detector bits.
"""

import itertools
import sys

# ---------------------------------------------------------------- linear algebra over F2

def rref(rows, ncols):
    """rows: list of int bitmasks. returns (pivots, reduced rows)."""
    rows = [r for r in rows if r]
    piv = []
    out = []
    for c in range(ncols):
        bit = 1 << c
        target = None
        for i, r in enumerate(rows):
            if r & bit:
                target = i
                break
        if target is None:
            continue
        pr = rows.pop(target)
        rows = [r ^ pr if (r & bit) else r for r in rows]
        out = [r ^ pr if (r & bit) else r for r in out]
        out.append(pr)
        piv.append(c)
    return piv, out


def rank_f2(rows, ncols):
    return len(rref(rows, ncols)[0])


def in_span(vec, basis_rows, ncols):
    piv, red = rref(list(basis_rows), ncols)
    v = vec
    for c, r in zip(piv, red):
        if v & (1 << c):
            v ^= r
    return v == 0


def kernel_basis(mat_rows, ncols):
    """basis of {v in F2^ncols : mat_rows . v = 0}, mat_rows given as row bitmasks."""
    # Gaussian elimination on the matrix (rows x cols)
    rows = list(mat_rows)
    piv, red = rref(rows, ncols)
    pivset = set(piv)
    free = [c for c in range(ncols) if c not in pivset]
    basis = []
    for f in free:
        v = 1 << f
        for c, r in zip(piv, red):
            if r & (1 << f):
                v |= 1 << c
        basis.append(v)
    return basis


def popcount(x):
    return bin(x).count("1")


def min_weight_coset(ker_basis, ncols, is_logical):
    """exhaustive min weight over span(ker_basis) restricted to is_logical(v)==True."""
    best = None
    k = len(ker_basis)
    for m in range(1, 1 << k):
        v = 0
        mm = m
        i = 0
        while mm:
            if mm & 1:
                v ^= ker_basis[i]
            mm >>= 1
            i += 1
        if is_logical(v):
            w = popcount(v)
            if best is None or w < best:
                best = w
    return best


# ---------------------------------------------------------------- rotated surface code

CORNERS = ("NW", "NE", "SW", "SE")


class Code:
    def __init__(self, n, xchecks, zchecks, xlog, zlog, name):
        self.n = n
        self.xchecks = xchecks      # list of (support tuple, {corner: qubit} or None)
        self.zchecks = zchecks
        self.xlog = xlog            # list of int bitmasks
        self.zlog = zlog
        self.name = name

    def hx_rows(self):
        return [sum(1 << q for q in s) for s, _ in self.xchecks]

    def hz_rows(self):
        return [sum(1 << q for q in s) for s, _ in self.zchecks]


def rotated_surface(d):
    """data at (r,c) 0<=r,c<d -> index r*d+c.
    plaquette centre (i+.5, j+.5) with i,j in -1..d-1; corners NW=(i,j) NE=(i,j+1)
    SW=(i+1,j) SE=(i+1,j+1); only corners inside the grid are owned.
    type X iff (i+j) even.  Bulk = i,j in 0..d-2 (4 corners).  Boundary plaquettes:
    i in {-1,d-1}, j in 0..d-2 kept only if X-type (2 corners, top/bottom);
    j in {-1,d-1}, i in 0..d-2 kept only if Z-type (2 corners, left/right).
    X_L = column 0 (vertical);  Z_L = row 0 (horizontal)."""
    idx = lambda r, c: r * d + c
    xchecks, zchecks = [], []

    def corners_of(i, j):
        cs = {}
        for name, (rr, cc) in (("NW", (i, j)), ("NE", (i, j + 1)),
                               ("SW", (i + 1, j)), ("SE", (i + 1, j + 1))):
            if 0 <= rr < d and 0 <= cc < d:
                cs[name] = idx(rr, cc)
        return cs

    for i in range(-1, d):
        for j in range(-1, d):
            bulk = (0 <= i <= d - 2) and (0 <= j <= d - 2)
            top_bot = (i in (-1, d - 1)) and (0 <= j <= d - 2)
            left_right = (j in (-1, d - 1)) and (0 <= i <= d - 2)
            xtype = ((i + j) % 2 == 0)
            if bulk:
                keep = True
            elif top_bot and xtype:
                keep = True
            elif left_right and not xtype:
                keep = True
            else:
                keep = False
            if not keep:
                continue
            cs = corners_of(i, j)
            if len(cs) < 2:
                continue
            entry = (tuple(sorted(cs.values())), cs)
            (xchecks if xtype else zchecks).append(entry)

    xlog = [sum(1 << idx(r, 0) for r in range(d))]      # column 0, X-type logical
    zlog = [sum(1 << idx(0, c) for c in range(d))]      # row 0, Z-type logical
    return Code(d * d, xchecks, zchecks, xlog, zlog, "rotated_surface_d%d" % d)


# ---------------------------------------------------------------- schedules

class Schedule:
    def __init__(self, code, layers, T, tag):
        self.code = code
        self.layers = layers      # layers[t] = list of (control, target, kind, checkindex)
        self.T = T
        self.tag = tag
        self.na = len(code.xchecks)
        self.nb = len(code.zchecks)
        self.nq = code.n + self.na + self.nb

    def anc_x(self, i):
        return self.code.n + i

    def anc_z(self, i):
        return self.code.n + self.na + i


def uniform_schedule(code, piX, piZ, tag=""):
    """piX/piZ: tuple of corner names in CNOT time order. every check acts on the corners it
    owns, at the time given by the permutation."""
    tX = {c: k for k, c in enumerate(piX)}
    tZ = {c: k for k, c in enumerate(piZ)}
    T = 4
    layers = [[] for _ in range(T)]
    for i, (supp, cs) in enumerate(code.xchecks):
        a = code.n + i
        for name, q in cs.items():
            layers[tX[name]].append((a, q, "X", i))
    for i, (supp, cs) in enumerate(code.zchecks):
        b = code.n + len(code.xchecks) + i
        for name, q in cs.items():
            layers[tZ[name]].append((q, b, "Z", i))
    return Schedule(code, layers, T, tag or "piX=%s,piZ=%s" % (",".join(piX), ",".join(piZ)))


def is_legal(sch):
    for t in range(sch.T):
        seen = set()
        for (c, tg, kind, ci) in sch.layers[t]:
            if c in seen or tg in seen:
                return False
            seen.add(c)
            seen.add(tg)
    return True


def mc_holds(sch):
    """Def 2.5: c_ab = #{q in supp(a)&supp(b) : t(q->b) < t(a->q)} mod 2 == 0."""
    code = sch.code
    tX = {}   # (checkindex, q) -> layer
    tZ = {}
    for t in range(sch.T):
        for (c, tg, kind, ci) in sch.layers[t]:
            if kind == "X":
                tX[(ci, tg)] = t
            else:
                tZ[(ci, c)] = t
    for ai, (sa, _) in enumerate(code.xchecks):
        sa_set = set(sa)
        for bi, (sb, _) in enumerate(code.zchecks):
            common = sa_set & set(sb)
            if not common:
                continue
            cnt = 0
            for q in common:
                if tZ[(bi, q)] < tX[(ai, q)]:
                    cnt += 1
            if cnt % 2:
                return False, (ai, bi, cnt)
    return True, None


# ---------------------------------------------------------------- signature engine

class Instance:
    """C_R^sigma(M).  sector 'Z' => data |0>^n, ideal Z readout, detectors complete on Z-checks.
                      sector 'X' => data |+>^n, ideal X readout, detectors complete on X-checks."""

    def __init__(self, sch, R, sector):
        assert sector in ("Z", "X")
        self.sch = sch
        self.R = R
        self.sector = sector
        self.code = sch.code
        self._build_detector_index()
        self._propagate()

    # ---- detector indexing
    def _build_detector_index(self):
        R = self.R
        na, nb = self.sch.na, self.sch.nb
        self.det_id = {}
        k = 0
        if self.sector == "Z":
            full, part = ("b", nb), ("a", na)
        else:
            full, part = ("a", na), ("b", nb)
        self.full_fam, self.n_full = full
        self.part_fam, self.n_part = part
        for i in range(self.n_full):
            for r in range(0, R + 1):
                self.det_id[(self.full_fam, i, r)] = k
                k += 1
        for i in range(self.n_part):
            for r in range(1, R):
                self.det_id[(self.part_fam, i, r)] = k
                k += 1
        self.ndet = k
        self.logs = self.code.zlog if self.sector == "Z" else self.code.xlog
        self.nobs = len(self.logs)

    def _record_sig(self, fam, i, r):
        """detector-mask of a flip of the record m_{fam,i,r} (r in 0..R-1)."""
        m = 0
        for rr in (r, r + 1):
            key = (fam, i, rr)
            if key in self.det_id:
                m |= 1 << self.det_id[key]
        return m

    # ---- backward propagation
    def _propagate(self):
        sch, code, R, T = self.sch, self.code, self.R, self.sch.T
        nq = sch.nq
        # final signatures (after last round's measurements, at the readout)
        sx = [0] * nq   # detector mask for an X-Pauli at the current slot
        sz = [0] * nq
        ox = [0] * nq   # observable mask
        oz = [0] * nq
        # readout: sector Z -> rho_q flips iff x_q ; sector X -> flips iff z_q
        for q in range(code.n):
            m = 0
            ob = 0
            for i in range(self.n_full):
                supp = (code.zchecks if self.sector == "Z" else code.xchecks)[i][0]
                if q in supp:
                    m |= 1 << self.det_id[(self.full_fam, i, R)]
            for j, L in enumerate(self.logs):
                if (L >> q) & 1:
                    ob |= 1 << j
            if self.sector == "Z":
                sx[q], ox[q] = m, ob
            else:
                sz[q], oz[q] = m, ob

        self.columns = []      # list of (detmask, obsmask, label)
        self._slotsig = {}

        for r in range(R - 1, -1, -1):
            # measurement boundary at end of round r
            for i in range(sch.na):
                a = sch.anc_x(i)
                sx[a] = 0; ox[a] = 0
                sz[a] = self._record_sig("a", i, r); oz[a] = 0
            for i in range(sch.nb):
                b = sch.anc_z(i)
                sz[b] = 0; oz[b] = 0
                sx[b] = self._record_sig("b", i, r); ox[b] = 0
            # classical record-flip locations of round r
            for i in range(sch.na):
                m = self._record_sig("a", i, r)
                if m:
                    self.columns.append((m, 0, ("rec", r, "a", i)))
            for i in range(sch.nb):
                m = self._record_sig("b", i, r)
                if m:
                    self.columns.append((m, 0, ("rec", r, "b", i)))
            # walk layers backwards
            for t in range(T - 1, -1, -1):
                # slot "after layer t" is the CURRENT (sx,sz)
                self._emit_slot(r, t, sx, sz, ox, oz)
                for (c, tg, kind, ci) in sch.layers[t]:
                    sx[c] ^= sx[tg]; ox[c] ^= ox[tg]
                    sz[tg] ^= sz[c]; oz[tg] ^= oz[c]
            # slot "after preparation" == before layer 0
            self._emit_prep(r, sx, sz, ox, oz)

    def _emit_slot(self, r, t, sx, sz, ox, oz):
        sch = self.sch
        busy = set()
        for (c, tg, kind, ci) in sch.layers[t]:
            busy.add(c); busy.add(tg)
            # 15 non-identity 2-qubit Paulis on (c,tg) immediately AFTER the gate
            for pc in range(4):
                for pt in range(4):
                    if pc == 0 and pt == 0:
                        continue
                    dm = 0; om = 0
                    if pc & 1: dm ^= sx[c]; om ^= ox[c]
                    if pc & 2: dm ^= sz[c]; om ^= oz[c]
                    if pt & 1: dm ^= sx[tg]; om ^= ox[tg]
                    if pt & 2: dm ^= sz[tg]; om ^= oz[tg]
                    if dm or om:
                        self.columns.append((dm, om, ("cnot", r, t, (c, tg), (pc, pt))))
        for q in range(sch.nq):
            if q in busy:
                continue
            for p in range(1, 4):
                dm = 0; om = 0
                if p & 1: dm ^= sx[q]; om ^= ox[q]
                if p & 2: dm ^= sz[q]; om ^= oz[q]
                if dm or om:
                    self.columns.append((dm, om, ("idle", r, t, q, p)))

    def _emit_prep(self, r, sx, sz, ox, oz):
        sch = self.sch
        for q in range(sch.code.n, sch.nq):
            for p in range(1, 4):
                dm = 0; om = 0
                if p & 1: dm ^= sx[q]; om ^= ox[q]
                if p & 2: dm ^= sz[q]; om ^= oz[q]
                if dm or om:
                    self.columns.append((dm, om, ("prep", r, q, p)))

    # ---- distinct effect classes
    def classes(self):
        seen = {}
        for dm, om, lab in self.columns:
            key = (dm, om)
            if key not in seen:
                seen[key] = lab
        return seen


# ---------------------------------------------------------------- exhaustive minimum search

def min_weight_exhaustive(inst, wmax, verbose=False):
    """returns (weight, witness_labels) for the minimum <= wmax, else (None, None).
    Exhaustive over subsets of DISTINCT effect classes (justified: two locations with equal
    effect cancel, so a minimum-weight configuration uses pairwise distinct effects)."""
    cls = inst.classes()
    items = list(cls.items())          # ((det,obs), label)
    N = len(items)
    if verbose:
        print("    distinct nonzero effect classes: %d" % N)
    # weight 1
    for (dm, om), lab in items:
        if dm == 0 and om != 0:
            return 1, [lab]
    if wmax < 2:
        return None, None
    # generic meet in the middle
    for w in range(2, wmax + 1):
        k1 = w // 2
        k2 = w - k1
        table = {}
        for combo in itertools.combinations(range(N), k1):
            dm = 0; om = 0
            for i in combo:
                d, o = items[i][0]
                dm ^= d; om ^= o
            table.setdefault(dm, []).append((om, combo))
        for combo in itertools.combinations(range(N), k2):
            dm = 0; om = 0
            for i in combo:
                d, o = items[i][0]
                dm ^= d; om ^= o
            hit = table.get(dm)
            if not hit:
                continue
            for om1, c1 in hit:
                if (om1 ^ om) == 0:
                    continue
                if set(c1) & set(combo):
                    continue
                idxs = list(c1) + list(combo)
                return w, [items[i][1] for i in idxs]
        del table
    return None, None


def count_classes(inst):
    return len(inst.classes())


# ---------------------------------------------------------------- exact ILP (scipy/HiGHS)

def min_weight_ilp(inst, cap=None, extra_forbid=None, force_meas=False, obs_index=None,
                   time_limit=None):
    """exact minimum weight via binary ILP with parity slacks. Independent second method."""
    import numpy as np
    from scipy.optimize import milp, LinearConstraint, Bounds
    from scipy.sparse import lil_matrix

    cls = inst.classes()
    items = list(cls.items())
    if extra_forbid is not None:
        items = [it for it in items if not extra_forbid(it)]
    N = len(items)
    ndet = inst.ndet
    nobs = inst.nobs
    targets = [obs_index] if obs_index is not None else list(range(nobs))
    best = None
    bestwit = None
    for j in targets:
        nrows = ndet + 1
        nvars = N + nrows
        A = lil_matrix((nrows, nvars))
        lo = np.zeros(nrows)
        hi = np.zeros(nrows)
        for i, ((dm, om), lab) in enumerate(items):
            d = dm
            while d:
                b = (d & -d).bit_length() - 1
                A[b, i] = 1
                d &= d - 1
            if (om >> j) & 1:
                A[ndet, i] = 1
        for rr in range(nrows):
            A[rr, N + rr] = -2
        lo[ndet] = hi[ndet] = 1
        c = np.zeros(nvars)
        c[:N] = 1.0
        integrality = np.ones(nvars)
        ub = np.ones(nvars)
        ub[N:] = np.inf
        cons = LinearConstraint(A.tocsr(), lo, hi)
        opts = {"mip_rel_gap": 0.0, "presolve": True}
        if time_limit:
            opts["time_limit"] = time_limit
        res = milp(c=c, constraints=cons, integrality=integrality,
                   bounds=Bounds(np.zeros(nvars), ub), options=opts)
        if res.status != 0 or res.x is None:
            continue
        w = int(round(res.fun))
        if best is None or w < best:
            best = w
            bestwit = [items[i][1] for i in range(N) if res.x[i] > 0.5]
    return best, bestwit


# ---------------------------------------------------------------- witness audit (raw replay)

def audit_witness(sch, R, sector, labels):
    """Re-derive detector flips and observable flips from the RAW locations by forward
    round-by-round propagation.  Completely separate code path from the backward engine."""
    code = sch.code
    nq = sch.nq
    x = [0] * nq
    z = [0] * nq
    recflip = {}
    byslot = {}
    for lab in labels:
        if lab[0] == "cnot":
            _, r, t, (c, tg), (pc, pt) = lab
            byslot.setdefault((r, t), []).append(("cnot", c, tg, pc, pt))
        elif lab[0] == "idle":
            _, r, t, q, p = lab
            byslot.setdefault((r, t), []).append(("single", q, p))
        elif lab[0] == "prep":
            _, r, q, p = lab
            byslot.setdefault((r, -1), []).append(("single", q, p))
        elif lab[0] == "rec":
            _, r, fam, i = lab
            recflip[(fam, i, r)] = recflip.get((fam, i, r), 0) ^ 1
    m = {}
    for r in range(R):
        for q in range(code.n, nq):
            x[q] = 0; z[q] = 0
        for ev in byslot.get((r, -1), []):
            _, q, p = ev
            if p & 1: x[q] ^= 1
            if p & 2: z[q] ^= 1
        for t in range(sch.T):
            for (c, tg, kind, ci) in sch.layers[t]:
                x[tg] ^= x[c]
                z[c] ^= z[tg]
            for ev in byslot.get((r, t), []):
                if ev[0] == "cnot":
                    _, c, tg, pc, pt = ev
                    if pc & 1: x[c] ^= 1
                    if pc & 2: z[c] ^= 1
                    if pt & 1: x[tg] ^= 1
                    if pt & 2: z[tg] ^= 1
                else:
                    _, q, p = ev
                    if p & 1: x[q] ^= 1
                    if p & 2: z[q] ^= 1
        for i in range(sch.na):
            a = sch.anc_x(i)
            m[("a", i, r)] = z[a] ^ recflip.get(("a", i, r), 0)
        for i in range(sch.nb):
            b = sch.anc_z(i)
            m[("b", i, r)] = x[b] ^ recflip.get(("b", i, r), 0)
    # terminal readout
    rho = [x[q] if sector == "Z" else z[q] for q in range(code.n)]
    full = "b" if sector == "Z" else "a"
    part = "a" if sector == "Z" else "b"
    fullchecks = code.zchecks if sector == "Z" else code.xchecks
    for i, (supp, _) in enumerate(fullchecks):
        m[(full, i, R)] = 0
        for q in supp:
            m[(full, i, R)] ^= rho[q]
    dets = {}
    for i in range(len(fullchecks)):
        for r in range(0, R + 1):
            prev = m[(full, i, r - 1)] if r >= 1 else 0
            dets[(full, i, r)] = m[(full, i, r)] ^ prev
    partchecks = code.xchecks if sector == "Z" else code.zchecks
    for i in range(len(partchecks)):
        for r in range(1, R):
            dets[(part, i, r)] = m[(part, i, r)] ^ m[(part, i, r - 1)]
    logs = code.zlog if sector == "Z" else code.xlog
    obs = []
    for L in logs:
        v = 0
        for q in range(code.n):
            if (L >> q) & 1:
                v ^= rho[q]
        obs.append(v)
    silent = all(v == 0 for v in dets.values())
    nloc = len(set(labels))
    return silent, obs, nloc, sum(dets.values())
