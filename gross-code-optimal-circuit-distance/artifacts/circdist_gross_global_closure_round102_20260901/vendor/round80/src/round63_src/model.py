#!/usr/bin/env python3
"""Exact frozen Gross-code schedule, 360-column and repair-zero models.

Plain integer bit-vectors are used for all F2 validation. PySAT supplies SAT search and
Z3 supplies the outer schedule layer. No result is accepted without replay by the
standard-library validators in this file.
"""
from __future__ import annotations
import hashlib, itertools, json, time
from dataclasses import dataclass
from pathlib import Path

L, M, G, N = 12, 6, 72, 144
A = ((3, 0), (0, 1), (0, 2))
B = ((0, 3), (1, 0), (2, 0))
RES_POS = ((0, 1), (3, 4, 5), (4, 5))
# Representative 0 is physically the four-suffix, while representatives 1/2 are
# the physical three-/two-suffixes.
PHYS_POS = ((2, 3, 4, 5), (3, 4, 5), (4, 5))


def gi(i: int, j: int) -> int:
    return (i % L) * M + (j % M)


def add(g: int, d) -> int:
    i, j = divmod(g, M)
    return gi(i + d[0], j + d[1])


Xslots = [[add(g, a) for a in A] + [G + add(g, b) for b in B] for g in range(G)]
Zslots = [[add(g, (-b[0], -b[1])) for b in B] +
          [G + add(g, (-a[0], -a[1])) for a in A] for g in range(G)]
Xchecks = [sorted(x) for x in Xslots]
Zchecks = [sorted(x) for x in Zslots]


def mask(qs) -> int:
    v = 0
    for q in qs:
        v |= 1 << int(q)
    return v


def popcount(v: int):
    return bin(v).count("1")


def bits(v: int):
    out = []
    while v:
        b = v & -v
        out.append(b.bit_length() - 1)
        v ^= b
    return out


HX = [mask(x) for x in Xchecks]
HZ = [mask(x) for x in Zchecks]
Xof = [[] for _ in range(N)]
Zof = [[] for _ in range(N)]
for a, row in enumerate(Xchecks):
    for q in row:
        Xof[q].append(a)
for b, row in enumerate(Zchecks):
    for q in row:
        Zof[q].append(b)
OVERLAPS = []
for a, xr in enumerate(Xchecks):
    xs = set(xr)
    for b, zr in enumerate(Zchecks):
        sh = sorted(xs.intersection(zr))
        if sh:
            OVERLAPS.append((a, b, sh))


def rref(rows, n=N):
    rows = [int(x) for x in rows if x]
    piv = []
    r = 0
    for c in range(n - 1, -1, -1):
        p = next((k for k in range(r, len(rows)) if (rows[k] >> c) & 1), None)
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
    return rows[:r], piv


def rank(rows, n=N):
    return len(rref(rows, n)[0])


def inspan(v, rows, n=N):
    rr, piv = rref(rows, n)
    for w, c in zip(rr, piv):
        if (v >> c) & 1:
            v ^= w
    return v == 0


def translate(w, d):
    out = 0
    for half in (0, G):
        t = (w >> half) & ((1 << G) - 1)
        for q in bits(t):
            out |= 1 << (half + add(q, d))
    return out


def load_seed_words(path):
    out = []
    with open(path) as f:
        for line in f:
            if not line.strip():
                continue
            a, b, c, d = [int(t, 16) for t in line.split()]
            out.append((a | (b << 64)) | ((c | (d << 64)) << G))
    return out


def expand_pool(path, stabilizers, detector_rows):
    allw = set()
    for w in load_seed_words(path):
        for di in range(L):
            for dj in range(M):
                allw.add(translate(w, (di, dj)))
    pool = sorted(w for w in allw if not inspan(w, stabilizers))
    assert len(pool) == 1884
    assert all(popcount(w) == 12 for w in pool)
    assert all(all(popcount(w & h) % 2 == 0 for h in detector_rows) for w in pool)
    return pool


def logical_basis(pool, stabilizers):
    out, red = [], []
    for v in pool:
        if rank(red + [v]) > rank(red):
            out.append(v)
            red.append(v)
            if len(out) == 12:
                break
    # Independence must be modulo the stabilizer space, not merely absolute.
    out, quotient_rows = [], list(stabilizers)
    base_rank = rank(quotient_rows)
    for v in pool:
        nr = rank(quotient_rows + [v])
        if nr > base_rank:
            out.append(v)
            quotient_rows.append(v)
            base_rank = nr
            if len(out) == 12:
                break
    assert len(out) == 12
    return out


def edge_key(kind, check, q):
    return f"{kind}:{check}:{q}"


def edge_tuple(key):
    k, a, q = key.split(':')
    return k, int(a), int(q)


ALL_EDGES = ([edge_key('X', a, q) for a, row in enumerate(Xchecks) for q in row] +
             [edge_key('Z', b, q) for b, row in enumerate(Zchecks) for q in row])
assert len(ALL_EDGES) == 864 and len(set(ALL_EDGES)) == 864


def expected_edges():
    return set(ALL_EDGES)


def schedule_from_T(T):
    assert len(T) == 36 and len(set(T)) == 36
    XL = [T[3*c:3*c+3] for c in range(3)]
    XR = [T[9+3*c:12+3*c] for c in range(3)]
    ZL = [T[18+3*c:21+3*c] for c in range(3)]
    ZR = [T[27+3*c:30+3*c] for c in range(3)]
    out = {}
    for g in range(G):
        i, j = divmod(g, M)
        c = (i + j) % 3
        for s, q in enumerate(Xslots[g][:3]): out[edge_key('X', g, q)] = XL[c][s]
        for s, q in enumerate(Xslots[g][3:]): out[edge_key('X', g, q)] = XR[c][s]
        for s, q in enumerate(Zslots[g][:3]): out[edge_key('Z', g, q)] = ZL[c][s]
        for s, q in enumerate(Zslots[g][3:]): out[edge_key('Z', g, q)] = ZR[c][s]
    return out


MCAND_X = {0: (0, 2, 1, 5, 3, 4), 1: (0, 1, 2, 3, 4, 5),
           2: (0, 1, 2, 5, 3, 4)}
MCAND_Z = {0: (0, 1, 2, 4, 3, 5), 1: (0, 1, 2, 5, 3, 4),
           2: (1, 2, 0, 5, 3, 4)}


def candidate_serial_schedule():
    out, t = {}, 0
    for kind, slots, classes in (('X', Xslots, MCAND_X), ('Z', Zslots, MCAND_Z)):
        for g in range(G):
            i, j = divmod(g, M)
            c = (i + j) % 3
            for s in classes[c]:
                q = slots[g][s]
                out[edge_key(kind, g, q)] = t
                t += 1
    assert t == 864
    return out


def compress_schedule(times):
    relabel = {t: i for i, t in enumerate(sorted(set(times.values())))}
    return {e: relabel[t] for e, t in times.items()}


def audit_schedule(times, require_compressed=True):
    errors = []
    if set(times) != expected_edges():
        errors.append({'edge_set_mismatch': {'missing': sorted(expected_edges()-set(times))[:10],
                                             'extra': sorted(set(times)-expected_edges())[:10]}})
    if any(not isinstance(t, int) or t < 0 for t in times.values()):
        errors.append('times_not_nonnegative_integers')
    conflicts = []
    node_time = {}
    for e, t in times.items():
        kind, a, q = edge_tuple(e)
        nodes = ((kind, a), ('D', q))
        for node in nodes:
            z = (node, t)
            if z in node_time:
                conflicts.append((node_time[z], e, t))
            node_time[z] = e
    used = sorted(set(times.values()))
    if require_compressed and used != list(range(len(used))):
        errors.append({'idle_compression': {'used_min': min(used) if used else None,
                                            'used_max': max(used) if used else None,
                                            'used_count': len(used)}})
    mc = []
    for a, b, sh in OVERLAPS:
        assert len(sh) == 2
        vals = [times[edge_key('Z', b, q)] < times[edge_key('X', a, q)] for q in sh]
        if vals[0] != vals[1]:
            mc.append((a, b, sh, vals))
    xs = [times[e] for e in ALL_EDGES if e.startswith('X:')]
    zs = [times[e] for e in ALL_EDGES if e.startswith('Z:')]
    global_interleaved = not (max(xs) < min(zs) or max(zs) < min(xs))
    pair_interleaved = whole_interleaved = 0
    for a, b, sh in OVERLAPS:
        xt = [times[edge_key('X', a, q)] for q in sh]
        zt = [times[edge_key('Z', b, q)] for q in sh]
        if not (max(xt) < min(zt) or max(zt) < min(xt)):
            pair_interleaved += 1
        xt = [times[edge_key('X', a, q)] for q in Xchecks[a]]
        zt = [times[edge_key('Z', b, q)] for q in Zchecks[b]]
        if not (max(xt) < min(zt) or max(zt) < min(xt)):
            whole_interleaved += 1
    return {'ok': not errors and not conflicts and not mc,
            'errors': errors, 'edge_count': len(times), 'conflicts': conflicts,
            'used_layers': len(used), 'min_time': min(used) if used else None,
            'max_time': max(used) if used else None,
            'mc_violations': mc, 'overlaps': len(OVERLAPS),
            'global_interleaved': global_interleaved,
            'overlap_interleaved_pairs': pair_interleaved,
            'whole_check_interleaved_pairs': whole_interleaved}


@dataclass
class Column:
    index: int
    name: str
    support: int              # canonical 360-column data mask
    syndrome: int
    physical_support: int     # support of the actual elementary hook/singleton
    u_options: tuple          # masks over detector checks
    kind: str
    check: int | None = None
    residual_kind: int | None = None


class Sector:
    def __init__(self, label, times, logical_duals):
        assert label in ('Xerr', 'Zerr')
        self.label = label
        self.times = times
        self.mirror = label == 'Zerr'
        if label == 'Xerr':
            self.hook_checks, self.det_of, self.detrows, self.stabilizers = Xchecks, Zof, HZ, HX
            self.hedge = lambda a, q: edge_key('X', a, q)
            self.dedge = lambda b, q: edge_key('Z', b, q)
        else:
            self.hook_checks, self.det_of, self.detrows, self.stabilizers = Zchecks, Xof, HX, HZ
            self.hedge = lambda a, q: edge_key('Z', a, q)
            self.dedge = lambda b, q: edge_key('X', b, q)
        self.logical_duals = logical_duals
        self.orders = [sorted(row, key=lambda q, a=a: times[self.hedge(a, q)])
                       for a, row in enumerate(self.hook_checks)]
        self.qorders = [sorted(self.det_of[q], key=lambda b, q=q: times[self.dedge(b, q)])
                        for q in range(N)]
        self.columns = self._columns()

    def syndrome_of(self, support):
        return sum(((popcount(support & row) & 1) << b) for b, row in enumerate(self.detrows))

    def hook_u(self, a, qs):
        u = 0
        for q in qs:
            for b in self.det_of[q]:
                if self.times[self.dedge(b, q)] > self.times[self.hedge(a, q)]:
                    u ^= 1 << b
        return u

    def singleton_U(self, q):
        out, v = [0], 0
        for b in reversed(self.qorders[q]):
            v |= 1 << b
            out.append(v)
        return tuple(out)

    def _columns(self):
        cols = []
        for q in range(N):
            s = 1 << q
            cols.append(Column(len(cols), f'D:{q}', s, self.syndrome_of(s), s,
                               self.singleton_U(q), 'data'))
        for a, o in enumerate(self.orders):
            for k, pos in enumerate(RES_POS):
                rep = mask(o[p] for p in pos)
                phys = mask(o[p] for p in PHYS_POS[k])
                # Physical suffix and canonical representative differ by the check stabilizer
                # only for k=0; syndrome and logical parities must therefore agree.
                assert self.syndrome_of(rep) == self.syndrome_of(phys)
                cols.append(Column(len(cols), f'R:{a}:{k}', rep, self.syndrome_of(rep), phys,
                                   (self.hook_u(a, bits(phys)),), 'residual', a, k))
        assert len(cols) == 360
        supports = [c.support for c in cols[144:]]
        assert len(set(supports)) == 216
        assert all(popcount(c.support) in (2, 3) for c in cols[144:])
        return cols

    def verify_effective_selection(self, selected, W=10):
        if len(selected) != len(set(selected)) or any(i < 0 or i >= 360 for i in selected):
            return {'ok': False, 'error': 'selected columns are not distinct valid indices'}
        net = 0
        for i in selected:
            net ^= self.columns[i].support
        syn = self.syndrome_of(net)
        nontrivial = not inspan(net, self.stabilizers)
        logical_parities = [(popcount(net & l) & 1) for l in self.logical_duals]
        return {'ok': len(selected) <= W and syn == 0 and nontrivial,
                'weight': len(selected), 'selected': selected,
                'selected_names': [self.columns[i].name for i in selected],
                'net_support': bits(net), 'net_weight': popcount(net),
                'syndrome': bits(syn), 'nontrivial': nontrivial,
                'logical_parities': logical_parities}

    def verify_repair_trace(self, choices, max_round=10):
        # choices: [{'column':j,'round':r,'u':mask}]
        idx = [int(x['column']) for x in choices]
        if len(idx) != 11 or len(set(idx)) != 11:
            return {'ok': False, 'error': 'repair trace must select 11 distinct columns'}
        if any(int(x['round']) < 0 or int(x['round']) > max_round for x in choices):
            return {'ok': False, 'error': 'round outside exact span bound'}
        for x in choices:
            c = self.columns[int(x['column'])]
            if int(x['u']) not in c.u_options:
                return {'ok': False, 'error': f"voltage not in U({c.name})"}
        ev = self.verify_effective_selection(idx, 11)
        if not ev['ok']:
            return {'ok': False, 'error': 'selected columns are not a weight-11 effective logical',
                    'effective': ev}
        acc = 0
        equations = []
        for r in range(max_round + 1):
            U = 0
            for x in choices:
                if int(x['round']) == r:
                    U ^= int(x['u'])
            equations.append({'round': r, 'U': bits(U), 'prefix_syndrome': bits(acc), 'ok': U == acc})
            for x in choices:
                if int(x['round']) == r:
                    acc ^= self.columns[int(x['column'])].syndrome
        ok = acc == 0 and all(x['ok'] for x in equations)
        return {'ok': ok, 'effective': ev, 'equations': equations,
                'terminal_syndrome': bits(acc)}


def parity_clauses(lits, parity=0):
    # Direct truth-table encoding is used only for short rows.
    out = []
    for vals in itertools.product((0, 1), repeat=len(lits)):
        if (sum(vals) & 1) != parity:
            out.append([(-lits[i] if vals[i] else lits[i]) for i in range(len(lits))])
    return out


def xor_chain(pool, lits, clauses, parity=0):
    if not lits:
        if parity:
            clauses.append([])
        return
    if len(lits) <= 6:
        clauses.extend(parity_clauses(lits, parity))
        return
    acc = lits[0]
    for x in lits[1:]:
        nv = pool.id()
        clauses += [[-nv, acc, x], [-nv, -acc, -x], [nv, -acc, x], [nv, acc, -x]]
        acc = nv
    clauses.append([acc if parity else -acc])


def formula_sha256(clauses):
    h = hashlib.sha256()
    for cl in clauses:
        h.update((' '.join(map(str, cl)) + ' 0\n').encode())
    return h.hexdigest()


def _solve_cnf(clauses, solver_name='cadical195', conf_budget=None, with_proof=False):
    from pysat.solvers import Solver
    t0 = time.time()
    result = {'solver': solver_name, 'conf_budget': conf_budget, 'formula_sha256': formula_sha256(clauses),
              'clauses': len(clauses), 'proof_requested': with_proof}
    try:
        with Solver(name=solver_name, bootstrap_with=clauses, with_proof=with_proof) as s:
            if conf_budget is not None:
                try:
                    s.conf_budget(int(conf_budget))
                    sat = s.solve_limited(expect_interrupt=True)
                except Exception as exc:
                    result['budget_api_error'] = repr(exc)
                    sat = s.solve()
            else:
                sat = s.solve()
            result['status'] = 'SAT' if sat is True else ('UNSAT' if sat is False else 'UNKNOWN')
            result['model'] = s.get_model() if sat is True else None
            try:
                result['accum_stats'] = s.accum_stats()
            except Exception:
                pass
            if sat is False and with_proof:
                try:
                    proof = s.get_proof()
                    result['proof'] = proof
                    result['proof_lines'] = len(proof) if proof is not None else 0
                except Exception as exc:
                    result['proof_error'] = repr(exc)
    except Exception as exc:
        result['status'] = 'ERROR'
        result['exception'] = repr(exc)
        result['model'] = None
    result['seconds'] = round(time.time() - t0, 6)
    return result


def effective_adversary(sec: Sector, W=10, solver_name='cadical195', conf_budget=None,
                          with_proof=False):
    from pysat.formula import IDPool
    from pysat.card import CardEnc, EncType
    p = IDPool()
    x = [p.id(('x', j)) for j in range(360)]
    clauses = []
    for b in range(G):
        lits = [x[c.index] for c in sec.columns if (c.syndrome >> b) & 1]
        xor_chain(p, lits, clauses, 0)
    logical_vars = []
    for r, logical in enumerate(sec.logical_duals):
        lits = [x[c.index] for c in sec.columns if popcount(c.support & logical) & 1]
        lv = p.id(('logical', r))
        # lv equals parity(lits).
        if len(lits) <= 6:
            # General equivalence using a chain ending at lv.
            tmp = lits + [lv]
            clauses.extend(parity_clauses(tmp, 0))
        else:
            acc = lits[0]
            for z in lits[1:]:
                nv = p.id()
                clauses += [[-nv, acc, z], [-nv, -acc, -z], [nv, -acc, z], [nv, acc, -z]]
                acc = nv
            clauses += [[-lv, acc], [lv, -acc]]
        logical_vars.append(lv)
    clauses.append(logical_vars)
    enc = CardEnc.atmost(lits=x, bound=W, top_id=p.top, encoding=EncType.seqcounter)
    clauses.extend(enc.clauses)
    solved = _solve_cnf(clauses, solver_name, conf_budget, with_proof)
    model = solved.pop('model', None)
    out = {'kind': 'effective_leq', 'sector': sec.label, 'W': W, 'encoding': 'direct-360-column',
           'distinct_columns': True, **solved}
    if out['status'] == 'SAT':
        pos = set(v for v in model if v > 0)
        selected = [j for j, lit in enumerate(x) if lit in pos]
        out['witness'] = sec.verify_effective_selection(selected, W)
        out['witness']['raw_selected_indices'] = selected
        if not out['witness']['ok']:
            out['status'] = 'VERIFIER_REJECTED'
    return out


def repair_adversary(sec: Sector, solver_name='cadical195', conf_budget=None,
                       max_round=10, with_proof=False):
    """Exact repair=0 existence at weight 11, arbitrary round assignment.

    The PROVED span bound permits rounds 0..10 after translation. Each column is selected at
    most once, enforcing the F2 effective-chain basis semantics. All U(E) choices are included.
    """
    from pysat.formula import IDPool
    from pysat.card import CardEnc, EncType
    p = IDPool()
    y = {}  # (column,round,uindex) -> literal
    by_col = [[] for _ in range(360)]
    for c in sec.columns:
        for r in range(max_round + 1):
            for ui, u in enumerate(c.u_options):
                lit = p.id(('y', c.index, r, ui))
                y[(c.index, r, ui)] = lit
                by_col[c.index].append(lit)
    clauses = []
    # Effective syndrome is zero.
    for b in range(G):
        lits = []
        for (j, r, ui), lit in y.items():
            if (sec.columns[j].syndrome >> b) & 1:
                lits.append(lit)
        xor_chain(p, lits, clauses, 0)
    # Nontrivial logical parity.
    lvars = []
    for k, logical in enumerate(sec.logical_duals):
        lits = []
        for (j, r, ui), lit in y.items():
            if popcount(sec.columns[j].support & logical) & 1:
                lits.append(lit)
        lv = p.id(('logical', k))
        if len(lits) <= 6:
            clauses.extend(parity_clauses(lits + [lv], 0))
        else:
            acc = lits[0]
            for z in lits[1:]:
                nv = p.id()
                clauses += [[-nv, acc, z], [-nv, -acc, -z], [nv, -acc, z], [nv, acc, -z]]
                acc = nv
            clauses += [[-lv, acc], [lv, -acc]]
        lvars.append(lv)
    clauses.append(lvars)
    # LIFT': U_b(r) equals cumulative syndrome before r for every check/round.
    for t in range(max_round + 1):
        for b in range(G):
            lits = []
            for (j, r, ui), lit in y.items():
                c = sec.columns[j]
                u = c.u_options[ui]
                coeff = (((r == t) and ((u >> b) & 1)) ^
                         ((r < t) and ((c.syndrome >> b) & 1)))
                if coeff:
                    lits.append(lit)
            xor_chain(p, lits, clauses, 0)
    # Allocate all cardinality auxiliaries only after every semantic/XOR variable has been
    # allocated through IDPool.  CardEnc's top_id does not advance IDPool itself, so mixing the
    # two allocators earlier would alias variables and can manufacture a spurious UNSAT.
    top = p.top
    for lits in by_col:
        enc = CardEnc.atmost(lits=lits, bound=1, top_id=top, encoding=EncType.seqcounter)
        clauses.extend(enc.clauses)
        top = max(top, enc.nv)
    all_y = list(y.values())
    enc = CardEnc.equals(lits=all_y, bound=11, top_id=top, encoding=EncType.seqcounter)
    clauses.extend(enc.clauses)
    top = max(top, enc.nv)
    solved = _solve_cnf(clauses, solver_name, conf_budget, with_proof)
    model = solved.pop('model', None)
    out = {'kind': 'repair0_weight11', 'sector': sec.label, 'max_round': max_round,
           'arbitrary_round_assignments': True, 'distinct_columns': True, **solved}
    if out['status'] == 'SAT':
        pos = set(v for v in model if v > 0)
        choices = []
        for (j, r, ui), lit in y.items():
            if lit in pos:
                choices.append({'column': j, 'name': sec.columns[j].name, 'round': r,
                                'u_index': ui, 'u': sec.columns[j].u_options[ui]})
        choices.sort(key=lambda z: (z['round'], z['column']))
        out['witness'] = sec.verify_repair_trace(choices, max_round)
        out['witness']['choices'] = choices
        if not out['witness']['ok']:
            out['status'] = 'VERIFIER_REJECTED'
    return out


def support_atoms(sec: Sector, column_index):
    c = sec.columns[column_index]
    if c.kind != 'residual':
        return []
    o = sec.orders[c.check]
    S = set(bits(c.support))
    O = set(o) - S
    atoms = []
    if c.residual_kind == 0:  # prefix two
        for q in sorted(S):
            for r in sorted(O): atoms.append((sec.hedge(c.check, q), '<', sec.hedge(c.check, r)))
    else:  # suffix three/two
        for q in sorted(O):
            for r in sorted(S): atoms.append((sec.hedge(c.check, q), '<', sec.hedge(c.check, r)))
    return atoms


def effective_block_atoms(sec: Sector, witness):
    atoms = []
    for j in witness.get('raw_selected_indices', witness['selected']):
        atoms += support_atoms(sec, j)
    # A <=10 logical cannot consist only of singleton columns because the static distance is 12.
    assert atoms
    return sorted(set(atoms))


def repair_block_atoms(sec: Sector, witness):
    atoms = []
    for ch in witness['choices']:
        c = sec.columns[ch['column']]
        atoms += support_atoms(sec, c.index)
        if c.kind == 'residual':
            # Fix every raw comparison that determined this rigid hook voltage. This is stronger
            # than fixing only the XOR, hence yields a sound but deliberately conservative block.
            for q in bits(c.physical_support):
                for b in sec.det_of[q]:
                    e1, e2 = sec.hedge(c.check, q), sec.dedge(b, q)
                    if sec.times[e1] < sec.times[e2]: atoms.append((e1, '<', e2))
                    else: atoms.append((e2, '<', e1))
        else:
            u = int(ch['u'])
            S = {b for b in range(G) if (u >> b) & 1}
            O = set(sec.det_of[int(c.name.split(':')[1])]) - S
            q = int(c.name.split(':')[1])
            for b0 in sorted(O):
                for b1 in sorted(S):
                    atoms.append((sec.dedge(b0, q), '<', sec.dedge(b1, q)))
    assert atoms
    return sorted(set(atoms))


def block_holds(times, atoms):
    return all(times[a] < times[b] for a, op, b in atoms)


def model_metadata(poolX, poolZ, LX, LZ):
    return {
        'rank_HX': rank(HX), 'rank_HZ': rank(HZ), 'k': N-rank(HX)-rank(HZ),
        'overlap_histogram': {'0': G*G-len(OVERLAPS), '2': len(OVERLAPS)},
        'overlap_halves': sorted({tuple(sum(q < G for q in sh) for _ in [0]) for _,_,sh in OVERLAPS}),
        'pool_X': len(poolX), 'pool_Z': len(poolZ),
        'logical_basis_X': len(LX), 'logical_basis_Z': len(LZ),
        'pairing_rank': rank([sum(((popcount(x & z) & 1) << j) for j, z in enumerate(LZ)) for x in LX], 12),
        'edges': len(ALL_EDGES), 'overlaps': len(OVERLAPS),
    }


def verify_named_selection(sec: Sector, names, W):
    by = {c.name: c.index for c in sec.columns}
    if len(names) != len(set(names)) or any(n not in by for n in names):
        return {'ok': False, 'error': 'invalid/duplicate named columns', 'names': names}
    return sec.verify_effective_selection([by[n] for n in names], W)


def c1_named_certificate(sec: Sector):
    """Map hunt3 C1's physical hooks to the direct 360-column normalization."""
    assert sec.label == 'Zerr'
    # Physical length 5 -> singleton at the earliest qubit; length 2/3/4 -> R k=2/1/0.
    names = []
    names.append(f'D:{sec.orders[7][0]}')
    names += [f'R:31:2', f'D:{sec.orders[31][0]}']
    names += ['R:6:1', 'R:62:0']
    names += [f'D:{q}' for q in [18,26,76,100,116]]
    return verify_named_selection(sec, names, 10)


def fast_w12_adversary(sec: Sector, pool, pair_limit=True):
    """Incomplete SAT-witness finder over the complete weight-12 pool.

    It checks all single residual columns and all pairs of individually positive residuals.
    It is never used to infer absence; the direct CNF remains the completeness authority.
    """
    residuals = sec.columns[144:]
    checked1 = checked2 = 0
    for V in pool:
        positive = []
        for c in residuals:
            checked1 += 1
            cost = 1 + popcount(V ^ c.support)
            if cost <= 10:
                D = V ^ c.support
                selected = [c.index] + [q for q in bits(D)]
                w = sec.verify_effective_selection(selected, 10)
                assert w['ok']
                return {'status':'SAT','method':'complete-weight12-single-residual-witness-finder',
                        'complete_for_absence':False,'checked_single':checked1,'checked_pairs':checked2,
                        'witness':w}
            gain = 12 - cost
            if gain >= 1:
                positive.append(c)
        if pair_limit:
            for i, c in enumerate(positive):
                for d in positive[i+1:]:
                    checked2 += 1
                    D = V ^ c.support ^ d.support
                    if 2 + popcount(D) <= 10:
                        selected = [c.index,d.index] + [q for q in bits(D)]
                        if len(selected) != len(set(selected)):
                            continue
                        w = sec.verify_effective_selection(selected,10)
                        assert w['ok']
                        return {'status':'SAT','method':'complete-weight12-positive-pair-witness-finder',
                                'complete_for_absence':False,'checked_single':checked1,'checked_pairs':checked2,
                                'witness':w}
    return {'status':'NO_WITNESS_IN_INCOMPLETE_PREFILTER','method':'weight12-single-positive-pair',
            'complete_for_absence':False,'checked_single':checked1,'checked_pairs':checked2}


def canonical_same_round_repair0(sec: Sector, pool, max_mechanisms=None):
    """Sound witness finder in the canonical physical two-suffix family.

    Absence is not complete for repair=0; a found trace is a fully valid arbitrary-round witness
    (all assigned to round zero) and is replayed by verify_repair_trace.
    """
    by_name = {c.name: c for c in sec.columns}
    tested = 0
    for a in range(G):
        hook = by_name[f'R:{a}:2']
        S = hook.support
        Vs = [V for V in pool if (V & S) == S]
        for V in Vs:
            singles = bits(V ^ S)
            assert len(singles) == 10
            target = hook.u_options[0]
            h = len(singles)//2
            left, right = singles[:h], singles[h:]
            tab = {}
            for choice in itertools.product(range(4), repeat=len(left)):
                u = 0
                for q,k in zip(left,choice): u ^= by_name[f'D:{q}'].u_options[k]
                if u not in tab: tab[u] = choice
            found = None
            for choice in itertools.product(range(4), repeat=len(right)):
                u = 0
                for q,k in zip(right,choice): u ^= by_name[f'D:{q}'].u_options[k]
                if (u ^ target) in tab:
                    found = list(tab[u ^ target]) + list(choice)
                    break
            tested += 1
            if found is not None:
                choices = [{'column':hook.index,'name':hook.name,'round':0,
                            'u_index':0,'u':hook.u_options[0]}]
                for q,k in zip(singles,found):
                    c=by_name[f'D:{q}']
                    choices.append({'column':c.index,'name':c.name,'round':0,
                                    'u_index':k,'u':c.u_options[k]})
                w=sec.verify_repair_trace(choices,10)
                assert w['ok']
                w['choices']=choices
                return {'status':'SAT','method':'canonical-two-suffix-same-round-witness-finder',
                        'complete_for_absence':False,'mechanisms_tested':tested,'witness':w}
            if max_mechanisms is not None and tested >= max_mechanisms:
                return {'status':'NO_WITNESS_IN_INCOMPLETE_PREFILTER',
                        'method':'canonical-two-suffix-same-round-witness-finder',
                        'complete_for_absence':False,'mechanisms_tested':tested,
                        'stopped_at_limit':max_mechanisms}
    return {'status':'NO_WITNESS_IN_INCOMPLETE_PREFILTER',
            'method':'canonical-two-suffix-same-round-witness-finder',
            'complete_for_absence':False,'mechanisms_tested':tested,'exhausted_canonical_family':True}


def c2_repair_certificate(sec: Sector):
    by={c.name:c for c in sec.columns}
    if sec.label=='Xerr':
        singles=[1,5,9,11,12,16,72,76,77,82]; ks=[1,0,1,0,0,3,0,2,0,1]
    else:
        singles=[2,10,26,42,43,58,66,67,78,124]; ks=[0,0,0,0,0,0,2,0,0,0]
    h=by['R:0:2']
    choices=[{'column':h.index,'name':h.name,'round':0,'u_index':0,'u':h.u_options[0]}]
    for q,k in zip(singles,ks):
        c=by[f'D:{q}'];choices.append({'column':c.index,'name':c.name,'round':0,
                                       'u_index':k,'u':c.u_options[k]})
    w=sec.verify_repair_trace(choices,10);w['choices']=choices
    return w
