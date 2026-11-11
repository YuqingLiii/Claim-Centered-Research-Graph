"""
sat_core.py -- CIRCDIST.sat.instances, session 2026-08-23.

Self-contained, independent implementation of:
  * CSS code constructions (rotated surface code, bivariate-bicycle qLDPC code),
  * single-ancilla CNOT syndrome-extraction schedules, legality and (MC) checks,
  * X-sector one-round fault dictionary generators (E(S), u(S)) by explicit
    symplectic propagation written from Definition 2.8 of the frozen model,
  * full spacetime detector matrix for R rounds (for MILP / witness audit),
  * stim circuit export from the *same* schedule object.

No code from any earlier artifact was read or reused; the model is taken from
research/circdist/notes/CIRCDIST_PROBLEMS.md (公共定义) and the definitions
restated in artifacts/circdist_sat_transfer_proof_20260823.md sections 2 and 5.

Conventions (stated because they are load-bearing):
  * aggregation is MIN-OVER-SECTORS: d_R(M) = min(d_R^Z(M), d_R^X(M));
  * detectors have window w = 2, both temporal boundaries present
    (D_{b,0} = m_{b,0} absolute; D_{b,R} closed by the ideal readout);
  * legality includes (MC): c_{ab} = #{q in supp(a)&supp(b) : t(q->b) < t(a->q)} = 0 mod 2.
"""

import itertools

# ----------------------------------------------------------------------------
# F2 linear algebra on int bitmasks (bit q of an int = coordinate q)
# ----------------------------------------------------------------------------

def popcount(x):
    return bin(x).count("1")


def rref(rows):
    """Row-reduce a list of int bitmasks. Returns (basis_rows, pivots)."""
    rows = [r for r in rows if r]
    basis, pivots = [], []
    for r in rows:
        cur = r
        for b, p in zip(basis, pivots):
            if (cur >> p) & 1:
                cur ^= b
        if cur:
            p = cur.bit_length() - 1
            basis.append(cur)
            pivots.append(p)
            # back-substitute
            for i in range(len(basis) - 1):
                if (basis[i] >> p) & 1:
                    basis[i] ^= cur
    order = sorted(range(len(basis)), key=lambda i: -pivots[i])
    basis = [basis[i] for i in order]
    pivots = [pivots[i] for i in order]
    return basis, pivots


def rank(rows):
    return len(rref(rows)[0])


class Quotient:
    """Sigma = F2^n / rowspace(gens), with canonical (pivot-free) representatives."""

    def __init__(self, gens, n):
        self.n = n
        self.basis, self.pivots = rref(list(gens))
        self.pivset = set(self.pivots)
        self.free = [q for q in range(n) if q not in self.pivset]
        self.dim = len(self.free)
        self.pos = {q: i for i, q in enumerate(self.free)}

    def reduce(self, v):
        for b, p in zip(self.basis, self.pivots):
            if (v >> p) & 1:
                v ^= b
        return v

    def cls(self, v):
        """class index in [0, 2^dim)"""
        v = self.reduce(v)
        s = 0
        for q in self.free:
            if (v >> q) & 1:
                s |= 1 << self.pos[q]
        return s

    def rep(self, s):
        """canonical representative vector of class index s"""
        v = 0
        for i, q in enumerate(self.free):
            if (s >> i) & 1:
                v |= 1 << q
        return v


# ----------------------------------------------------------------------------
# Code + schedule containers
# ----------------------------------------------------------------------------

class Code:
    def __init__(self, n, xchecks, zchecks, xlog, zlog, name):
        self.n = n
        self.xchecks = [int(c) for c in xchecks]   # supports as bitmasks
        self.zchecks = [int(c) for c in zchecks]
        self.xlog = [int(v) for v in xlog]         # X logical representatives
        self.zlog = [int(v) for v in zlog]         # Z logical representatives
        self.name = name
        assert all(popcount(a & b) % 2 == 0 for a in self.xchecks for b in self.zchecks), "CSS"
        self.rx = rank(self.xchecks)
        self.rz = rank(self.zchecks)
        self.k = n - self.rx - self.rz


class Schedule:
    """cnots: list of (t, kind, check_index, data_qubit).
    kind 'X': ancilla anc_x[check] is CONTROL, data is TARGET.
    kind 'Z': data is CONTROL, ancilla anc_z[check] is TARGET."""

    def __init__(self, code, cnots, name):
        self.code = code
        self.cnots = sorted(cnots)
        self.name = name
        self.T = max(t for t, _, _, _ in cnots) + 1
        n = code.n
        self.nA, self.nB = len(code.xchecks), len(code.zchecks)
        self.id_data = lambda q: q
        self.id_ax = lambda a: n + a
        self.id_az = lambda b: n + self.nA + b
        self.nq = n + self.nA + self.nB
        # completeness: every (check,data) incidence exactly once
        need = set()
        for a, s in enumerate(code.xchecks):
            for q in range(n):
                if (s >> q) & 1:
                    need.add(("X", a, q))
        for b, s in enumerate(code.zchecks):
            for q in range(n):
                if (s >> q) & 1:
                    need.add(("Z", b, q))
        got = [(k, c, q) for _, k, c, q in self.cnots]
        assert len(got) == len(set(got)) == len(need) and set(got) == need, "schedule incomplete"
        self.legal_ok, self.legal_msg = self._legality()
        self.mc_ok, self.mc_max = self._mc()

    def gate_pairs(self):
        """time -> list of (control_qubit_id, target_qubit_id)"""
        out = {}
        for t, k, c, q in self.cnots:
            if k == "X":
                out.setdefault(t, []).append((self.id_ax(c), self.id_data(q)))
            else:
                out.setdefault(t, []).append((self.id_data(q), self.id_az(c)))
        return out

    def _legality(self):
        seen = {}
        for t, k, c, q in self.cnots:
            ids = (self.id_ax(c), self.id_data(q)) if k == "X" else (self.id_data(q), self.id_az(c))
            for u in ids:
                if (t, u) in seen:
                    return False, "collision at t=%d qubit=%d" % (t, u)
                seen[(t, u)] = 1
        return True, "ok"

    def times(self):
        tx, tz = {}, {}
        for t, k, c, q in self.cnots:
            (tx if k == "X" else tz)[(c, q)] = t
        return tx, tz

    def _mc(self):
        tx, tz = self.times()
        worst = 0
        for a, sa in enumerate(self.code.xchecks):
            for b, sb in enumerate(self.code.zchecks):
                sh = sa & sb
                if not sh:
                    continue
                c = 0
                for q in range(self.code.n):
                    if (sh >> q) & 1 and tz[(b, q)] < tx[(a, q)]:
                        c += 1
                worst = max(worst, c % 2)
        return worst == 0, worst

    def mirror(self):
        """Dual schedule: X-sector analysis of the mirror computes the Z-sector."""
        c2 = Code(self.code.n, self.code.zchecks, self.code.xchecks,
                  self.code.zlog, self.code.xlog, self.code.name + "*")
        cn = [(t, "X" if k == "Z" else "Z", c, q) for t, k, c, q in self.cnots]
        return Schedule(c2, cn, self.name + "*")


# ----------------------------------------------------------------------------
# One-round X-sector propagation and elementary fault generators
# ----------------------------------------------------------------------------
# Fault location kinds (X-sector projections of Definition 2.8):
#   ('cnot', t, idx, pat)  pat in {'c','t','ct'} : X on control / target / both,
#                          applied immediately after the CNOT layer t
#   ('idle', t, qubit)     X on a qubit not in a two-qubit gate at layer t
#   ('prep', qubit)        X immediately after preparation (before layer 0)
#   ('meas', b)            classical flip of the record m_b of this round

def enumerate_locations(sch):
    locs = []
    pairs = sch.gate_pairs()
    for t in sorted(pairs):
        for i, (c, tg) in enumerate(pairs[t]):
            for pat in ("c", "t", "ct"):
                locs.append(("cnot", t, (c, tg), pat))
    busy = {}
    for t in range(sch.T):
        busy[t] = set()
        for (c, tg) in pairs.get(t, []):
            busy[t].add(c)
            busy[t].add(tg)
    for t in range(sch.T):
        for u in range(sch.nq):
            if u not in busy[t]:
                locs.append(("idle", t, u, None))
    for u in range(sch.code.n, sch.nq):
        locs.append(("prep", -1, u, None))
    for b in range(sch.nB):
        locs.append(("meas", None, b, None))
    return locs


def simulate(sch, faults):
    """faults: list of locations (as produced by enumerate_locations).
    Returns (E, u): residual data-X bitmask, and this round's m_b flip bitmask."""
    pairs = sch.gate_pairs()
    xf = [0] * sch.nq
    rec = 0
    after = {}
    for f in faults:
        kind = f[0]
        if kind == "cnot":
            t, (c, tg), pat = f[1], f[2], f[3]
            targets = {"c": [c], "t": [tg], "ct": [c, tg]}[pat]
            after.setdefault(t, []).extend(targets)
        elif kind == "idle":
            after.setdefault(f[1], []).append(f[2])
        elif kind == "prep":
            after.setdefault(-1, []).append(f[2])
        elif kind == "meas":
            rec ^= 1 << f[2]
    for u in after.get(-1, []):
        xf[u] ^= 1
    for t in range(sch.T):
        for (c, tg) in pairs.get(t, []):
            xf[tg] ^= xf[c]
        for u in after.get(t, []):
            xf[u] ^= 1
    E = 0
    for q in range(sch.code.n):
        if xf[q]:
            E |= 1 << q
    uvec = rec
    for b in range(sch.nB):
        if xf[sch.id_az(b)]:
            uvec ^= 1 << b
    return E, uvec


def generators(sch):
    """[(E, u, location)] for every elementary X-sector fault."""
    out = []
    for loc in enumerate_locations(sch):
        E, u = simulate(sch, [loc])
        out.append((E, u, loc))
    return out


def syndrome(code, E, which="Z"):
    checks = code.zchecks if which == "Z" else code.xchecks
    s = 0
    for i, c in enumerate(checks):
        if popcount(c & E) % 2:
            s |= 1 << i
    return s


# ----------------------------------------------------------------------------
# Full spacetime detector matrix over R rounds (X-sector, Z-memory)
# ----------------------------------------------------------------------------

def spacetime_columns(sch, R):
    """Returns (cols, nrows, labels).
    Row layout: rows 0..(R+1)*nB-1 are detectors D_{b,r}, r=0..R;
    the observable rows follow, one per logical Z representative.
    Column = int bitmask of flipped rows."""
    code = sch.code
    nB = sch.nB
    gens = generators(sch)
    nrow_det = (R + 1) * nB
    cols, labels = [], []
    for r in range(R):
        for (E, u, loc) in gens:
            # D_{b,r} gets u ; D_{b,r+1} gets u + H_Z E   (Lemma 6.1)
            v = u ^ syndrome(code, E, "Z")
            col = 0
            for b in range(nB):
                if (u >> b) & 1:
                    col |= 1 << (r * nB + b)
                if (v >> b) & 1:
                    col |= 1 << ((r + 1) * nB + b)
            for j, zl in enumerate(code.zlog):
                if popcount(zl & E) % 2:
                    col |= 1 << (nrow_det + j)
            if col:
                cols.append(col)
                labels.append((r, loc))
    return cols, nrow_det + len(code.zlog), labels


# ----------------------------------------------------------------------------
# Rotated surface code, uniform-permutation schedule family
# ----------------------------------------------------------------------------
# data (r,c), 0<=r,c<d, index r*d+c.  plaquette (i,j) has corners
#   NW=(i,j) NE=(i,j+1) SW=(i+1,j) SE=(i+1,j+1)  for i,j in -1..d-1.
# type X iff (i+j) even.  Bulk: 0<=i,j<=d-2.  Weight-2 X on rows i=-1,i=d-1;
# weight-2 Z on columns j=-1,j=d-1.
OFF = {"NW": (0, 0), "NE": (0, 1), "SW": (1, 0), "SE": (1, 1)}
ORDER_NAMES = list(itertools.permutations(["NW", "NE", "SW", "SE"]))


def rotated_surface_code(d):
    n = d * d
    idx = lambda r, c: r * d + c
    xchecks, zchecks, xoff, zoff = [], [], [], []
    for i in range(-1, d):
        for j in range(-1, d):
            corners = {}
            for nm, (dr, dc) in OFF.items():
                r, c = i + dr, j + dc
                if 0 <= r < d and 0 <= c < d:
                    corners[nm] = idx(r, c)
            if len(corners) not in (2, 4):
                continue
            isX = ((i + j) % 2 == 0)
            if len(corners) == 2:
                # weight-2: X only on top/bottom boundary rows, Z only on left/right
                on_row_bdy = (i == -1 or i == d - 1)
                on_col_bdy = (j == -1 or j == d - 1)
                if on_row_bdy and on_col_bdy:
                    continue
                if isX and not on_row_bdy:
                    continue
                if (not isX) and not on_col_bdy:
                    continue
            supp = 0
            for q in corners.values():
                supp |= 1 << q
            if isX:
                xchecks.append(supp)
                xoff.append(corners)
            else:
                zchecks.append(supp)
                zoff.append(corners)
    xlog = [sum(1 << idx(r, 0) for r in range(d))]   # X logical: column 0
    zlog = [sum(1 << idx(0, c) for c in range(d))]   # Z logical: row 0
    code = Code(n, xchecks, zchecks, xlog, zlog, "rotated_surface_d%d" % d)
    code.xoff, code.zoff = xoff, zoff
    assert code.k == 1, (code.k, code.rx, code.rz)
    return code


def uniform_schedule(code, piX, piY, name):
    """piX, piZ: tuples listing corner names in CNOT time order.
    A check acts on its present corners at the times given by the order."""
    piZ = piY
    tX = {nm: t for t, nm in enumerate(piX)}
    tZ = {nm: t for t, nm in enumerate(piZ)}
    cn = []
    for a, corners in enumerate(code.xoff):
        for nm, q in corners.items():
            cn.append((tX[nm], "X", a, q))
    for b, corners in enumerate(code.zoff):
        for nm, q in corners.items():
            cn.append((tZ[nm], "Z", b, q))
    return Schedule(code, cn, name)


def hook_pairs(code, sch, sector="X"):
    """Residual sets produced by a single ancilla-X fault mid-round, per X-check
    (the 'hook' errors).  Returned as {check: [(residual bitmask, weight)]}."""
    out = {}
    tx, tz = sch.times()
    for a, supp in enumerate(code.xchecks):
        qs = sorted([q for q in range(code.n) if (supp >> q) & 1], key=lambda q: tx[(a, q)])
        res = []
        for cut in range(1, len(qs)):
            m = 0
            for q in qs[cut:]:
                m |= 1 << q
            res.append(m)
        out[a] = res
    return out
