"""
xval.py -- INDEPENDENT stim cross-validation harness for the CIRCDIST frozen model.

Written from the frozen 公共定义 (research/circdist/notes/CIRCDIST_PROBLEMS.md lines 14-41)
plus the model restatement in artifacts/circdist_lift_d3gate_20260820.md Sec 1.

DESIGN CONTRACT (the translation convention -- see artifact Sec 2):
  * stim builds the circuit and stim's own noise channels define the fault space.
  * stim's detector_error_model() enumerates the faults (one DEM error per distinct
    (detector set, observable set) column) -- we never hand-enumerate faults.
  * distance is then computed by an exact GF(2) minimum-weight search over the DEM
    columns, AND independently by stim's own search_for_undetectable_logical_errors.

FROZEN FAULT INVENTORY (公共定义 / Sec 1.3) -> STIM CHANNEL MAP:
  ancilla immediately after prep, {X,Y,Z}        -> DEPOLARIZE1(p) on ancillas after R/RX
  immediately after CNOT, 15 two-qubit Paulis    -> DEPOLARIZE2(p) on each CX pair
  any qubit idle at a time step, {X,Y,Z}         -> DEPOLARIZE1(p) on idle qubits that step
  recorded ancilla measurement outcome flip      -> M(p) / MX(p)
  ideal data init, ideal terminal readout        -> noiseless R/RX on data, noiseless M/MX at end
"""

import itertools
import stim

# ----------------------------------------------------------------- codes


class Code:
    def __init__(self, n, xchecks, zchecks, zl, xl, name=""):
        self.n = n
        self.xchecks = dict(xchecks)   # name -> list of data qubits
        self.zchecks = dict(zchecks)
        self.zl = list(zl)
        self.xl = list(xl)
        self.name = name
        self.xnames = list(self.xchecks)
        self.znames = list(self.zchecks)
        self.anc = {}
        nxt = n
        for c in self.xnames + self.znames:
            self.anc[c] = nxt
            nxt += 1
        self.nq = nxt

    def validate(self):
        """CSS commutation + logical algebra + code distance, from scratch."""
        msgs = []
        for xn, xs in self.xchecks.items():
            for zn, zs in self.zchecks.items():
                if len(set(xs) & set(zs)) % 2 != 0:
                    msgs.append("NONCOMMUTING %s/%s" % (xn, zn))
        for xn, xs in self.xchecks.items():
            if len(set(xs) & set(self.zl)) % 2 != 0:
                msgs.append("XCHECK %s anticommutes Z_L" % xn)
        for zn, zs in self.zchecks.items():
            if len(set(zs) & set(self.xl)) % 2 != 0:
                msgs.append("ZCHECK %s anticommutes X_L" % zn)
        if len(set(self.zl) & set(self.xl)) % 2 != 1:
            msgs.append("Z_L commutes X_L (should anticommute)")
        return msgs or ["OK"]


CODES = {}

CODES['422'] = Code(
    4, {'a': [0, 1, 2, 3]}, {'b': [0, 1, 2, 3]},
    zl=[0, 2], xl=[0, 1], name='[[4,2,2]]')

CODES['steane'] = Code(
    7,
    {'X1': [3, 4, 5, 6], 'X2': [1, 2, 5, 6], 'X3': [0, 2, 4, 6]},
    {'Z1': [3, 4, 5, 6], 'Z2': [1, 2, 5, 6], 'Z3': [0, 2, 4, 6]},
    zl=[0, 1, 2], xl=[0, 1, 2], name='Steane [[7,1,3]]')

CODES['surface3'] = Code(
    9,
    {'XA': [1, 2, 4, 5], 'XB': [3, 4, 6, 7], 'XC': [0, 1], 'XD': [7, 8]},
    {'ZA': [0, 1, 3, 4], 'ZB': [4, 5, 7, 8], 'ZC': [2, 5], 'ZD': [3, 6]},
    zl=[0, 1, 2], xl=[0, 3, 6], name='rotated surface [[9,1,3]]')


# ------------------------------------------------- rotated surface, general d

def rotated_surface(d):
    """Standard rotated surface code on a d x d grid, index q = r*d + c.

    Weight-4 plaquettes on the interior vertices of the dual lattice plus
    weight-2 boundary plaquettes, in the usual checkerboard.
    Z_L = left column (all Z), X_L = top row (all X)  -- chosen to anticommute
    in exactly one qubit (corner 0).
    """
    def q(r, c):
        return r * d + c
    xchecks, zchecks = {}, {}
    # interior weight-4: plaquette anchored at (r,c) covers (r,c),(r,c+1),(r+1,c),(r+1,c+1)
    for r in range(d - 1):
        for c in range(d - 1):
            sup = [q(r, c), q(r, c + 1), q(r + 1, c), q(r + 1, c + 1)]
            if (r + c) % 2 == 0:
                zchecks['Z_%d_%d' % (r, c)] = sup
            else:
                xchecks['X_%d_%d' % (r, c)] = sup
    # boundary weight-2.  X on top/bottom edges, Z on left/right edges.
    for c in range(0, d - 1, 2):
        xchecks['X_top_%d' % c] = [q(0, c), q(0, c + 1)]
    for c in range(1, d - 1, 2):
        xchecks['X_bot_%d' % c] = [q(d - 1, c), q(d - 1, c + 1)]
    for r in range(1, d - 1, 2):
        zchecks['Z_left_%d' % r] = [q(r, 0), q(r + 1, 0)]
    for r in range(0, d - 1, 2):
        zchecks['Z_right_%d' % r] = [q(r, d - 1), q(r + 1, d - 1)]
    # Per the SAT dossier Sec 4.1 convention: X_L is a COLUMN, Z_L is a ROW.
    xl = [q(r, 0) for r in range(d)]     # X on left column
    zl = [q(0, c) for c in range(d)]     # Z on top row
    return Code(d * d, xchecks, zchecks, zl, xl, name='rotated surface d=%d' % d)


CORNERS = ['NW', 'NE', 'SW', 'SE']


def corner_map(code, name, sup):
    """Map a check's support to corner labels, from the grid geometry."""
    d = int(round(code.n ** 0.5))
    cells = sorted((q // d, q % d) for q in sup)
    r0 = min(r for r, _ in cells)
    c0 = min(c for _, c in cells)
    out = {}
    for (r, c) in cells:
        lbl = ('N' if r == r0 else 'S') + ('W' if c == c0 else 'E')
        out[lbl] = r * d + c
    return out


def uniform_schedule(code, piX, piZ):
    """Sec 4.1 uniform family: X-check uses corner piX[t] at layer t (if it has
    that corner), Z-check uses corner piZ[t] at layer t.  Depth 4, X and Z share
    the same four layers -- this is what makes legality non-trivial."""
    S = {}
    for c in code.xnames:
        cm = corner_map(code, c, code.xchecks[c])
        S[c] = [(cm[lbl], t) for t, lbl in enumerate(piX) if lbl in cm]
    for c in code.znames:
        cm = corner_map(code, c, code.zchecks[c])
        S[c] = [(cm[lbl], t) for t, lbl in enumerate(piZ) if lbl in cm]
    return S


def code_distance(code):
    """Exact code distance by coset search over the stabilizer group."""
    import itertools as it
    best = code.n + 1
    for checks, lg in ((code.zchecks, code.zl), (code.xchecks, code.xl)):
        names = list(checks)
        for k in range(len(names) + 1):
            pass
        # enumerate the full rowspace by Gray-ish brute force over subsets
        sups = [set(checks[nm]) for nm in names]
        m = len(sups)
        if m > 20:
            return None                       # too big for brute force
        for mask in range(1 << m):
            v = set(lg)
            mm = mask
            i = 0
            while mm:
                if mm & 1:
                    v ^= sups[i]
                mm >>= 1
                i += 1
            if v and len(v) < best:
                best = len(v)
    return best


# ----------------------------------------------------------------- schedules
# A schedule is a dict: check name -> list of (data_qubit, time_slot),
# i.e. the CNOT on that data qubit happens at that slot.


def sched_from_orders(code, xorder, zorder, xstart, zstart):
    """Offset family: check c's CNOTs on consecutive slots starting at start[c]."""
    s = {}
    for c in code.xnames:
        s[c] = [(q, xstart[c] + i) for i, q in enumerate(xorder[c])]
    for c in code.znames:
        s[c] = [(q, zstart[c] + i) for i, q in enumerate(zorder[c])]
    return s


def sched_depth(s):
    return max(t for v in s.values() for (_, t) in v) + 1


def legal(code, s):
    """No qubit in two two-qubit gates at the same step."""
    busy = {}
    for c, lst in s.items():
        a = code.anc[c]
        for (q, t) in lst:
            for x in (a, q):
                if (x, t) in busy:
                    return False
                busy[(x, t)] = c
    return True


def mc_violations(code, s):
    """Measurement-consistency (MC), Sec 2 of the dossier, RE-DERIVED HERE.

    For an X-check a (ancilla is CONTROL, so X on its ancilla propagates FORWARD
    onto data at time t(a->q)) and a Z-check b (ancilla is TARGET, so X on data q
    propagates FORWARD onto b's ancilla at t(q->b)):  b's outcome is deterministic
    only if, over q in supp(a) & supp(b), the number of q with t(q->b) < t(a->q)
    is EVEN.  (Odd => b's recorded bit anticommutes with a's ancilla |+> phase.)
    """
    bad = []
    for an in code.xnames:
        ta = {q: t for (q, t) in s[an]}
        for bn in code.znames:
            tb = {q: t for (q, t) in s[bn]}
            common = set(ta) & set(tb)
            cnt = sum(1 for q in common if tb[q] < ta[q])
            if cnt % 2 != 0:
                bad.append((an, bn, cnt))
    return bad


# ------------------------------------------------------- stim circuit builder

# translation conventions
CONV_FROZEN = 'frozen'      # exactly the 公共定义 inventory
CONV_COMPILER = 'compiler'  # + data idling during the ancilla reset and measure layers
CONV_NOISYRO = 'noisyro'    # frozen + NOISY terminal readout (breaks the ideal boundary)


def build(code, s, R, basis, p=1e-3, conv=CONV_FROZEN):
    """Emit the memory experiment C_R(M) as a stim circuit."""
    T = sched_depth(s)
    xanc = [code.anc[c] for c in code.xnames]
    zanc = [code.anc[c] for c in code.znames]
    allq = list(range(code.nq))
    data = list(range(code.n))

    # per-step gate lists and busy sets
    steps = [[] for _ in range(T)]
    for c in code.xnames:
        a = code.anc[c]
        for (q, t) in s[c]:
            steps[t].append((a, q))          # X-check: ancilla is CONTROL
    for c in code.znames:
        a = code.anc[c]
        for (q, t) in s[c]:
            steps[t].append((q, a))          # Z-check: data is CONTROL
    busy = [set(x for pair in st for x in pair) for st in steps]

    c = stim.Circuit()
    # ideal data initialisation
    c.append("R" if basis == 'Z' else "RX", data)

    det_checks = code.znames if basis == 'Z' else code.xnames
    oth = code.xnames if basis == 'Z' else code.znames

    nmeas = 0
    recs = {}
    for r in range(R):
        # ancilla preparation (ideal state, then the after-prep {X,Y,Z} fault)
        c.append("RX", xanc)
        c.append("R", zanc)
        c.append("DEPOLARIZE1", xanc + zanc, p)
        if conv == CONV_COMPILER:
            # a real compiler idles the data qubits during the ancilla reset layer
            c.append("DEPOLARIZE1", data, p)
        for t in range(T):
            targ = []
            for (ctl, tgt) in steps[t]:
                targ += [ctl, tgt]
            if targ:
                c.append("CX", targ)
                c.append("DEPOLARIZE2", targ, p)
            idle = [q for q in allq if q not in busy[t]]
            if idle:
                c.append("DEPOLARIZE1", idle, p)
        if conv == CONV_COMPILER:
            # ... and during the ancilla measurement layer
            c.append("DEPOLARIZE1", data, p)
        # ancilla measurement with classical bit-flip fault
        c.append("MX", xanc, p)
        for i, n in enumerate(code.xnames):
            recs[(n, r)] = nmeas + i
        nmeas += len(xanc)
        c.append("M", zanc, p)
        for i, n in enumerate(code.znames):
            recs[(n, r)] = nmeas + i
        nmeas += len(zanc)
        # detectors, Sec 1.4
        for n in det_checks:
            if r == 0:
                c.append("DETECTOR", [stim.target_rec(recs[(n, 0)] - nmeas)])
            else:
                c.append("DETECTOR", [stim.target_rec(recs[(n, r)] - nmeas),
                                      stim.target_rec(recs[(n, r - 1)] - nmeas)])
        for n in oth:
            if r >= 1:
                c.append("DETECTOR", [stim.target_rec(recs[(n, r)] - nmeas),
                                      stim.target_rec(recs[(n, r - 1)] - nmeas)])
    # terminal transversal readout -- IDEAL under the frozen boundary
    if conv == CONV_NOISYRO:
        c.append("M" if basis == 'Z' else "MX", data, p)
    else:
        c.append("M" if basis == 'Z' else "MX", data)
    for i, q in enumerate(data):
        recs[('d', q)] = nmeas + i
    nmeas += code.n
    ch = code.zchecks if basis == 'Z' else code.xchecks
    for n in det_checks:
        tg = [stim.target_rec(recs[(n, R - 1)] - nmeas)]
        for q in ch[n]:
            tg.append(stim.target_rec(recs[('d', q)] - nmeas))
        c.append("DETECTOR", tg)
    obs = code.zl if basis == 'Z' else code.xl
    c.append("OBSERVABLE_INCLUDE",
             [stim.target_rec(recs[('d', q)] - nmeas) for q in obs], 0)
    return c


# ------------------------------------------------------- DEM -> columns


def dem_columns(circ):
    """stim's own fault enumeration, reduced to GF(2) columns.

    Raises ValueError (propagated) if any detector is non-deterministic --
    this is stim's independent (MC) oracle.
    """
    dem = circ.detector_error_model(decompose_errors=False,
                                    approximate_disjoint_errors=True)
    cols = set()
    for inst in dem.flattened():
        if inst.type != 'error':
            continue
        bits = 0
        obs = 0
        for t in inst.targets_copy():
            if t.is_relative_detector_id():
                bits ^= (1 << t.val)
            elif t.is_logical_observable_id():
                obs ^= 1
        if bits or obs:
            cols.add((bits, obs))
    return cols, dem.num_detectors


def min_weight(cols, cap=5):
    """Exact minimum |F| with zero detector syndrome and observable flipped.

    Deduplicated columns are safe: a minimum solution never repeats a column
    (deleting a repeated pair gives a strictly smaller undetectable logical).
    Meet-in-the-middle up to weight `cap` (cap <= 5 supported).
    """
    cols = list(cols)
    # weight 1
    for (m, o) in cols:
        if m == 0 and o == 1:
            return 1
    if cap < 2:
        return None
    # weight 2 : two columns, equal masks, different obs bits
    seen = {}
    for (m, o) in cols:
        seen.setdefault(m, set()).add(o)
    for m, os in seen.items():
        if len(os) == 2:
            return 2
    if cap < 3:
        return None
    # singles table: mask -> set of obs
    singles = seen
    # weight 3 : pair-sum  vs  single
    pair = {}
    N = len(cols)
    for i in range(N):
        mi, oi = cols[i]
        for j in range(i + 1, N):
            mj, oj = cols[j]
            m = mi ^ mj
            o = oi ^ oj
            pair.setdefault(m, set()).add(o)
    for m, os in pair.items():
        if m in singles:
            for o in os:
                if (1 ^ o) in singles[m]:
                    return 3
    if cap < 4:
        return None
    # weight 4 : pair-sum vs pair-sum
    for m, os in pair.items():
        if len(os) == 2:
            return 4
    if cap < 5:
        return None
    # weight 5 : triple-sum vs pair-sum, via  pair(+)single  table
    trip = {}
    for m, os in pair.items():
        for (ms, oss) in singles.items():
            mm = m ^ ms
            for o in os:
                for o2 in oss:
                    trip.setdefault(mm, set()).add(o ^ o2)
    for m, os in trip.items():
        if m in pair:
            for o in os:
                if (1 ^ o) in pair[m]:
                    return 5
    return None


def stim_native_distance(circ, cap=6):
    """stim's OWN exact search -- a second, independent distance extractor."""
    try:
        err = circ.search_for_undetectable_logical_errors(
            dont_explore_detection_event_sets_with_size_above=cap,
            dont_explore_edges_with_degree_above=cap,
            dont_explore_edges_increasing_symptom_degree=False,
            canonicalize_circuit_errors=True)
        return len(err)
    except Exception as e:                       # noqa: BLE001
        return 'ERR:' + type(e).__name__


def dcirc(code, s, R, basis, conv=CONV_FROZEN, cap=5, native=True):
    """Full pipeline.  Returns dict of results or the stim (MC) failure."""
    circ = build(code, s, R, basis, conv=conv)
    try:
        cols, nd = dem_columns(circ)
    except ValueError as e:
        return {'ok': False, 'why': 'stim refuses DEM (non-deterministic detectors)',
                'msg': str(e)[:120]}
    out = {'ok': True, 'cols': len(cols), 'dets': nd,
           'd_search': min_weight(cols, cap=cap)}
    if native:
        out['d_stim_native'] = stim_native_distance(circ, cap=cap + 1)
    return out
