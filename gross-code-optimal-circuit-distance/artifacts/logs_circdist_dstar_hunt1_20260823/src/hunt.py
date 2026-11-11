"""CIRCDIST.gross D* hunt, stage 1 -- the repair-0 decider on the canonical minimum-weight
effective-logical family, swept over structured schedule families.

Canonical family (per CIRCDIST.gross.dext-cap):  gamma = {S} u (V \\ S) where V is a weight-12
logical of the sector and S is the 2-element SUFFIX of some check's CNOT order with S subset V.
|gamma| = 11 = d_eff.  If ANY such gamma has repair 0 then d_circ = d_eff = 11 (Thm 5.7 <=),
so the schedule cannot witness D* = 12.  Only schedules where EVERY canonical gamma has
repair >= 1 survive as gap candidates.
"""
import itertools, random, sys, json, time
from lift import CSS, Schedule, Sector, popc, sameround_repair0, multiround_repair0
import gross as G

NG, N = G.NG, G.N
CSSG = G.CSSG


# ---------------------------------------------------------------- pools
def pools():
    base = ('<repo>/'
            'artifacts/logs_circdist_gross_links_20260823/')
    px, _ = G.expand(G.load_pool(base + 'w12X.txt'), G.HXm)   # X-logicals: Z-memory sector
    pz, _ = G.expand(G.load_pool(base + 'w12.txt'), G.HZm)    # Z-logicals: X-memory sector
    return px, pz


def bits(w):
    out = []
    while w:
        b = w & -w
        out.append(b.bit_length() - 1)
        w ^= b
    return out


def pair_index(pool):
    """map frozenset{q,q'} -> list of logicals containing both, restricted to pairs that lie
    inside a common check support (that is all the decider ever asks for)."""
    idx = {}
    for w in pool:
        qs = bits(w)
        for x, y in itertools.combinations(qs, 2):
            idx.setdefault((x, y), []).append(w)
    return idx


# ---------------------------------------------------------------- schedules
def sched_TI(XL, XR, ZL, ZR):
    tX, tZ = {}, {}
    for g in range(NG):
        for i, m in enumerate(G.Amon):
            tX[(g, G.gadd(g, m))] = XL[i]
        for j, m in enumerate(G.Bmon):
            tX[(g, NG + G.gadd(g, m))] = XR[j]
    for g in range(NG):
        for j, m in enumerate(G.Bmon):
            tZ[(G.gadd(g, (-m[0], -m[1])), g)] = ZL[j]
        for i, m in enumerate(G.Amon):
            tZ[(NG + G.gadd(g, (-m[0], -m[1])), g)] = ZR[i]
    return Schedule(CSSG, tX, tZ)


def ti_ok(XL, XR, ZL, ZR):
    """legality (4 six-element unions distinct) + (MC) as the 9 slot constraints."""
    if len(set(XL) | set(XR)) != 6 or len(set(ZL) | set(ZR)) != 6:
        return False
    if len(set(XL) | set(ZL)) != 6 or len(set(XR) | set(ZR)) != 6:
        return False
    for i in range(3):
        for j in range(3):
            if (ZL[j] < XL[i]) != (ZR[i] < XR[j]):
                return False
    return True


def sched_check_serial(rng, orderX=None, orderZ=None):
    """every check does its 6 CNOTs consecutively; random global check order."""
    tX, tZ = {}, {}
    seq = [('X', g) for g in range(NG)] + [('Z', g) for g in range(NG)]
    rng.shuffle(seq)
    t = 0
    for typ, g in seq:
        qs = list(CSSG.Xchecks[g] if typ == 'X' else CSSG.Zchecks[g])
        rng.shuffle(qs)
        for q in qs:
            if typ == 'X':
                tX[(g, q)] = t
            else:
                tZ[(q, g)] = t
            t += 1
    return Schedule(CSSG, tX, tZ)


# ---------------------------------------------------------------- diagnostics
def hook_stats(sec, alist=None):
    """classify the 2-suffix hook of every check."""
    c = {'trivial': 0, 'horizontal': 0, 'VERTICAL': 0, 'diagonal': 0}
    for a in range(len(sec.hook_checks)):
        S = sec.hook(a, 2)
        k, u, s = sec.classify_hook(a, S)
        c[k] += 1
    return c


def misalignment(sec):
    """for each check a, count data qubits q whose After(a)-pattern is NOT a suffix of q's
    detector-gate order (the obstruction to the check-serial repair-0 proof)."""
    nd = sec.ndet
    css = sec.css
    # eps[a][b]
    tot = 0
    per_a = []
    for a in range(len(sec.hook_checks)):
        after = 0
        for b in range(nd):
            sh = [q for q in sec.hook_checks[a] if b in sec.det_of_q[q]]
            if not sh:
                continue
            if sec.tD(sh[0], b) > sec.tH(a, sh[0]):
                after |= 1 << b
        bad = 0
        for q in range(css.n):
            m = after & sec.sq[q]
            if m not in sec.Uq[q]:
                bad += 1
        per_a.append(bad)
        tot += bad
    return tot, per_a


# ---------------------------------------------------------------- the decider
def decide(sec, pidx, budget=None, want_all=False):
    """Search the canonical minimum-weight family for a repair-0 certificate.
    Returns (verdict, info).  verdict 'NOGAP' if some canonical gamma has repair 0,
    'GAPCAND' if none does over the whole family."""
    nchk = len(sec.hook_checks)
    tried = 0
    hooks_diag = 0
    per_hook = []
    for a in range(nchk):
        S = sec.hook(a, 2)
        kind, u, s = sec.classify_hook(a, S)
        key = tuple(sorted(S))
        Vs = pidx.get(key, [])
        if not Vs:
            per_hook.append((a, kind, 0, None))
            continue
        if kind in ('trivial', 'horizontal'):
            # u in {0, s}: repair 0 with the all-zero / all-full singleton certificate
            if not want_all:
                return 'NOGAP', {'a': a, 'S': S, 'kind': kind, 'nV': len(Vs),
                                 'reason': 'horizontal hook (u in {0,s})'}
            per_hook.append((a, kind, len(Vs), 0))
            continue
        hooks_diag += 1
        found = None
        for V in Vs:
            singles = [q for q in bits(V) if q not in S]
            tried += 1
            w = sameround_repair0(sec, a, S, singles)
            if w is not None:
                found = (a, V)
                break
        if found and not want_all:
            return 'NOGAP', {'a': a, 'S': S, 'kind': kind, 'nV': len(Vs),
                             'reason': 'same-round certificate on a diagonal hook',
                             'tried': tried}
        per_hook.append((a, kind, len(Vs), 0 if found else 1))
    if want_all:
        return ('NOGAP' if any(p[3] == 0 for p in per_hook if p[3] is not None) else 'GAPCAND',
                {'per_hook': per_hook, 'diag': hooks_diag, 'tried': tried})
    return 'GAPCAND', {'diag': hooks_diag, 'tried': tried}


def triple_index(pool):
    idx = {}
    for w in pool:
        qs = bits(w)
        for t in itertools.combinations(qs, 3):
            idx.setdefault(t, []).append(w)
    return idx


def dext_le10(sec, pidx, tidx):
    """SOUND disqualifier for d_eff = 11 on the weight-12 logical pool: a gamma of weight
    <= 10 exists iff some weight-12 logical V admits total hook gain >= 2, i.e. either
    (a) the 3-SUFFIX of some check lies inside V, or
    (b) the 2-suffixes of two checks lie disjointly inside V.
    (|V cap supp(check)| <= 3 for the own sector, so no longer suffix can fit.)"""
    nch = len(sec.hook_checks)
    for a in range(nch):
        T = tuple(sorted(sec.hook(a, 3)))
        if tidx.get(T):
            return True, ('3-suffix of check %d inside a weight-12 logical' % a)
    perV = {}
    for a in range(nch):
        S = sec.hook(a, 2)
        for V in pidx.get(tuple(sorted(S)), []):
            perV.setdefault(V, []).append((a, frozenset(S)))
    for V, lst in perV.items():
        for (a1, s1), (a2, s2) in itertools.combinations(lst, 2):
            if not (s1 & s2):
                return True, ('disjoint 2-suffixes of checks %d,%d inside one logical' % (a1, a2))
    return False, None


def decide_rate(sec, pidx, checks=None):
    """Full repair-0 RATE over the canonical minimum-weight family, restricted to the
    given hook checks (translation invariance lets a TI schedule use checks=[0])."""
    if checks is None:
        checks = range(len(sec.hook_checks))
    n0 = ntot = 0
    kinds = {'trivial': 0, 'horizontal': 0, 'VERTICAL': 0, 'diagonal': 0}
    for a in checks:
        S = sec.hook(a, 2)
        kind, u, s = sec.classify_hook(a, S)
        kinds[kind] += 1
        Vs = pidx.get(tuple(sorted(S)), [])
        for V in Vs:
            ntot += 1
            if kind in ('trivial', 'horizontal'):
                n0 += 1
                continue
            singles = [q for q in bits(V) if q not in S]
            if sameround_repair0(sec, a, S, singles) is not None:
                n0 += 1
    return n0, ntot, kinds


# ---------------------------------------------------------------- coset-TI schedules
def sched_coset(m, XL, XR, ZL, ZR):
    """times depend on the class  c(g) = (g // 6) mod m  of the check's group element.
    XL[c][i], XR[c][j], ZL[c][j], ZR[c][i].  m = 1 recovers the TI family."""
    tX, tZ = {}, {}
    for g in range(NG):
        c = (g // 6) % m
        for i, mo in enumerate(G.Amon):
            tX[(g, G.gadd(g, mo))] = XL[c][i]
        for j, mo in enumerate(G.Bmon):
            tX[(g, NG + G.gadd(g, mo))] = XR[c][j]
    for g in range(NG):
        c = (g // 6) % m
        for j, mo in enumerate(G.Bmon):
            tZ[(G.gadd(g, (-mo[0], -mo[1])), g)] = ZL[c][j]
        for i, mo in enumerate(G.Amon):
            tZ[(NG + G.gadd(g, (-mo[0], -mo[1])), g)] = ZR[c][i]
    return Schedule(CSSG, tX, tZ)


# ---------------------------------------------------------------- main
def run(sched, tag, pidx_Z, pidx_X, verbose=True):
    out = {'tag': tag}
    if not sched.legal():
        out['status'] = 'ILLEGAL'
        return out
    mcv = sched.mc_violations()
    out['mc_violations'] = len(mcv)
    if mcv:
        out['status'] = 'NOT-MC'
        return out
    out['globally_interleaved'] = sched.globally_interleaved()
    out['pair_interleaved'] = sched.interleaved_pairs()
    out['strict_pair_interleaved'] = sched.strict_interleaved_pairs()
    for lab, mir, pidx in (('Zmem', False, pidx_Z), ('Xmem', True, pidx_X)):
        sec = Sector(CSSG, sched, mirror=mir)
        hs = hook_stats(sec)
        mis, per_a = misalignment(sec)
        v, info = decide(sec, pidx)
        out[lab] = {'hooks2': hs, 'misalign_total': mis,
                    'misalign_checks': sum(1 for x in per_a if x), 'verdict': v,
                    'info': {k: (list(vv) if isinstance(vv, tuple) else vv)
                             for k, vv in info.items() if k != 'per_hook'}}
    out['status'] = 'OK'
    if verbose:
        print(json.dumps(out))
        sys.stdout.flush()
    return out


def gain2_count(sec, pidx, tidx, checks=None):
    """graded version of dext_le10: how many weight-<=10 gamma configurations exist."""
    if checks is None:
        checks = range(len(sec.hook_checks))
    n = 0
    perV = {}
    for a in checks:
        if tidx.get(tuple(sorted(sec.hook(a, 3)))):
            n += 1
        S = sec.hook(a, 2)
        for V in pidx.get(tuple(sorted(S)), []):
            perV.setdefault(V, []).append(frozenset(S))
    for V, lst in perV.items():
        for s1, s2 in itertools.combinations(lst, 2):
            if not (s1 & s2):
                n += 1
    return n
