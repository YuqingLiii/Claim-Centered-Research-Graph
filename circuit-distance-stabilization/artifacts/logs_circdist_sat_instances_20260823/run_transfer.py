"""
run_transfer.py -- driver: emit the transfer spec, call ./transfer, parse.
Also: meet-in-the-middle extraction of an explicit minimum witness, and an
independent audit of that witness against the spacetime detector matrix.
"""

import os, subprocess, itertools, tempfile
import sat_core as S

HERE = os.path.dirname(os.path.abspath(__file__))
BIN = os.path.join(HERE, "transfer")


def flag_hook(E, u, loc):
    return S.popcount(E) >= 2


def flag_meas(E, u, loc):
    return E == 0


FLAGS = {"none": (lambda E, u, l: False), "hook": flag_hook, "meas": flag_meas}


def sector_data(sch):
    """Quotient, generators, HZ table for the X-sector of `sch`."""
    code = sch.code
    Q = S.Quotient(code.xchecks, code.n)
    gens = S.generators(sch)
    nB = sch.nB
    HZ = [0] * (1 << Q.dim)
    for i in range(Q.dim):
        HZ[1 << i] = S.syndrome(code, Q.rep(1 << i), "Z")
    for s in range(1, 1 << Q.dim):
        low = s & (-s)
        HZ[s] = HZ[low] ^ HZ[s ^ low]
    return Q, gens, HZ


def write_spec(path, Q, gens, HZ, nB, Rmax, cap, flagfn):
    keys = {}
    for (E, u, loc) in gens:
        k = (Q.cls(E) << nB) | u
        fl = 1 if flagfn(E, u, loc) else 0
        keys.setdefault((k, fl), 0)
        keys[(k, fl)] += 1
    keys = sorted(keys)
    with open(path, "w") as f:
        f.write("%d %d %d %d %d\n" % (Q.dim, nB, Rmax, cap, len(keys)))
        for (k, fl) in keys:
            f.write("%d %d\n" % (k, fl))
        f.write("\n".join(str(x) for x in HZ))
        f.write("\n")
    return len(keys)


def run(sch, Rmax, cap, flag="none", tag="run", logdir=None):
    Q, gens, HZ = sector_data(sch)
    spec = os.path.join(logdir or tempfile.gettempdir(), "spec_%s.txt" % tag)
    ng = write_spec(spec, Q, gens, HZ, sch.nB, Rmax, cap, FLAGS[flag])
    out = subprocess.run([BIN, spec], capture_output=True, text=True)
    res, paths = {}, {}
    for line in out.stdout.splitlines():
        p = line.split()
        if p[0] == "R":
            res[(int(p[1]), p[2])] = int(p[3])
        elif p[0] == "PATH":
            R = int(p[1])
            i = p.index("|")
            paths[R] = ([int(x) for x in p[2:i]], [int(x) for x in p[i + 1:]])
    return dict(res=res, paths=paths, dim=Q.dim, nB=sch.nB, ngen=ng,
                stderr=out.stderr, spec=spec, Q=Q, gens=gens, HZ=HZ)


# --------------------------------------------------------------------------
# explicit minimum witness: meet in the middle inside one round
# --------------------------------------------------------------------------

def one_round_config(Q, gens, nB, target_key, w):
    """Return a list of w generator indices whose effects XOR to target_key."""
    if w == 0:
        return [] if target_key == 0 else None
    # deduplicate by effect: a minimum-weight multiset never repeats an effect
    # (two identical effects cancel), so one representative per key suffices.
    seen = {}
    for i, (E, u, loc) in enumerate(gens):
        seen.setdefault((Q.cls(E) << nB) | u, i)
    idxs = sorted(seen.values())
    keys = [(Q.cls(gens[i][0]) << nB) | gens[i][1] for i in idxs]
    m = len(keys)
    w1 = w // 2
    w2 = w - w1
    tbl = {}
    for combo in itertools.combinations(range(m), w1):
        k = 0
        for i in combo:
            k ^= keys[i]
        tbl.setdefault(k, combo)
    for combo in itertools.combinations(range(m), w2):
        k = 0
        for i in combo:
            k ^= keys[i]
        other = tbl.get(k ^ target_key)
        if other is not None and len(set(other) | set(combo)) == w:
            return [idxs[i] for i in list(other) + list(combo)]
    return None


def witness(sch, R, path, logdir=None):
    """path = (sigmas, weights) from the C backtrack.  Returns a list of
    (round, location) pairs, plus an audit dict."""
    Q, gens, HZ = sector_data(sch)
    nB = sch.nB
    sig, ws = path
    F = []
    for r in range(R):
        w = ws[r]
        if w == 0:
            continue
        delta = sig[r] ^ sig[r + 1]
        mu = HZ[sig[r]]
        key = (delta << nB) | mu
        combo = one_round_config(Q, gens, nB, key, w)
        if combo is None:
            return None, {"error": "no explicit config for round %d" % r}
        for i in combo:
            F.append((r, gens[i][2]))
    return F, audit(sch, R, F)


def audit(sch, R, F):
    """Independent check: recompute every detector and the observable from the
    raw fault locations, using sat_core.simulate round by round."""
    code = sch.code
    nB = sch.nB
    byround = {}
    for (r, loc) in F:
        byround.setdefault(r, []).append(loc)
    sigma = 0            # accumulated residual (actual vector, not class)
    det = {}
    prev = 0
    for r in range(R):
        E, u = S.simulate(sch, byround.get(r, []))
        cur = u ^ S.syndrome(code, sigma, "Z")     # this round's m_b flips
        for b in range(nB):
            det[(b, r)] = ((cur >> b) & 1) ^ ((prev >> b) & 1)
        prev = cur
        sigma ^= E
    final = S.syndrome(code, sigma, "Z")
    for b in range(nB):
        det[(b, R)] = ((final >> b) & 1) ^ ((prev >> b) & 1)
    obs = [S.popcount(L & sigma) % 2 for L in code.zlog]
    return dict(weight=len(F), detectors_fired=[k for k, v in det.items() if v],
                observable=obs, residual=sigma,
                undetectable=not any(det.values()), logical=any(obs))
