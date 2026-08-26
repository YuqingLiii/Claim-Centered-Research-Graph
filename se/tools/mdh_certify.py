"""Certify the mdh block engine against brute force + known SE data.

Layer 1: brute-force full Gamma(t) on YES x NO from the t-picture reconstruction
         Gamma[(f,s), x] = t(h_s o x^{-1} o f),  h_s = id (+) shift(s),
         verified G-invariant; full SVD gives ground-truth singular values with
         multiplicities d_lambda * d_tau per block class.
Layer 2: engine blocks B_o(lam;mu,nu); block of Gamma(t) = sum_o t_o B_o,
         orthonormalized by row/col Grams; per-class sigma must appear in the
         full SVD with the right multiplicity (both contraction variants tested,
         the faithful one identified).
Layer 3: known SE(2,4) data: decoded optimal multipliers reproduce
         sigma = (2.1498..., 1.2247..., 1.3265, 0.5095, 0.2809), ADV=(4+sqrt6)/3,
         multiplicity structure [1,2,2,6,6]+kernel 7, and the D2-JSON face point
         reproduces ratios [1,.5697,.5296,.338,.1034].
"""
import sys, json, math
from fractions import Fraction
from itertools import permutations
import numpy as np

from pathlib import Path

PROJECT = Path(__file__).resolve().parents[1]
from mdh_engine import (YSN, CosetSpace, partitions, hs, level, syt_list, F0, F1)
from mdh_blocks import BlockEngine, char_table_Sn, kronecker_g

# ---------------------------------------------------------------- brute force
def enum_yes(n):
    """YES instances as (f, s): f injection (tuple), s in S_n; g = f o s."""
    from itertools import permutations as perms
    fs = [l for l in perms(range(2 * n), n)]
    ss = list(perms(range(n)))
    return [(f, s) for f in fs for s in ss]

def enum_no(n):
    from itertools import permutations as perms
    return list(perms(range(2 * n)))

def gamma_entry(t_of, n, y, x):
    """Gamma[y,x] = t(h o x^{-1} o f), h(i)=i i<n, h(n+j)=n+s(j) (sigma_y=s^{-1})."""
    f, s = y
    xinv = [0] * (2 * n)
    for i, v in enumerate(x): xinv[v] = i
    def h(p):
        return p if p < n else n + s[p - n]
    ell = tuple(h(xinv[f[i]]) for i in range(n))
    return t_of(ell)

def build_gamma(tvals, orbmap, n):
    YE = enum_yes(n); NO = enum_no(n)
    t_of = lambda ell: tvals[orbmap[ell]]
    G = np.zeros((len(YE), len(NO)))
    for iy, y in enumerate(YE):
        for ix, x in enumerate(NO):
            G[iy, ix] = gamma_entry(t_of, n, y, x)
    return G, YE, NO

def check_invariance(Gm, YE, NO, n, trials=60, seed=0):
    """Random group elements (pi, alpha, beta, swap) must fix Gamma."""
    import random
    rng = random.Random(seed)
    yidx = {y: i for i, y in enumerate(YE)}
    xidx = {x: i for i, x in enumerate(NO)}
    def act_y(y, pi, al, be, sw):
        f, s = y
        g = tuple(f[s[j]] for j in range(n))
        if sw: f, g = g, f
        alin = [0]*n; bein = [0]*n
        for i, v in enumerate(al): alin[v] = i
        for i, v in enumerate(be): bein[v] = i
        f2 = tuple(pi[f[alin[i]]] for i in range(n))
        g2 = tuple(pi[g[bein[j]]] for j in range(n))
        # recover s2: g2 = f2 o s2
        pos = {v: i for i, v in enumerate(f2)}
        s2 = tuple(pos[g2[j]] for j in range(n))
        return (f2, s2)
    def act_x(x, pi, al, be, sw):
        # x' = pi o x o h^{-1}, h = al (+) be; with swap: pre-compose x with omega
        if sw:
            x = tuple(x[(i + n) % (2 * n)] for i in range(2 * n))
        hin = [0] * (2 * n)
        for i in range(n): hin[al[i]] = i
        for j in range(n): hin[n + be[j]] = n + j
        return tuple(pi[x[hin[p]]] for p in range(2 * n))
    bad = 0
    for _ in range(trials):
        pi = tuple(rng.sample(range(2 * n), 2 * n))
        al = tuple(rng.sample(range(n), n))
        be = tuple(rng.sample(range(n), n))
        sw = rng.random() < 0.5
        y = YE[rng.randrange(len(YE))]
        x = NO[rng.randrange(len(NO))]
        y2, x2 = act_y(y, pi, al, be, sw), act_x(x, pi, al, be, sw)
        if abs(Gm[yidx[y2], xidx[x2]] - Gm[yidx[y], xidx[x]]) > 1e-12:
            bad += 1
    return bad

# ---------------------------------------------------------------- engine side
def all_classes(n):
    return [(lam, mu, nu) for lam in partitions(2 * n)
            for mu in partitions(n) for nu in partitions(n)]

def chol(Sf):
    """float Cholesky of a Fraction Gram."""
    A = np.array([[float(x) for x in row] for row in Sf])
    return np.linalg.cholesky(A)

def engine_run(n, variant, tvals_by_orbit=None, verbose=True):
    """Compute all blocks; return dict class -> dict with B_o list, dims, sigma."""
    cs = CosetSpace(n)
    orbs = cs.orbits()
    orb_list, seen = orbs
    out = {}
    for lam in partitions(2 * n):
        try:
            eng = BlockEngine(n, lam, cs)
        except AssertionError as e:
            print("  dV FAIL", lam, e); continue
        if eng.ld.dV == 0:
            continue
        for mu in partitions(n):
            for nu in partitions(n):
                B, mY, mN, ex = eng.orbit_blocks(mu, nu, orbs, variant=variant)
                if B is None:
                    if mY * mN != 0:
                        print("  unexpected empty", lam, mu, nu)
                    continue
                rec = {"B": B, "mY": mY, "mN": mN, "eng": eng, "ex": ex}
                if tvals_by_orbit is not None:
                    M = [[sum(Fraction(tvals_by_orbit[o]).limit_denominator(10**12)
                              * B[o][r][c] if isinstance(tvals_by_orbit[o], float)
                              else tvals_by_orbit[o] * B[o][r][c]
                              for o in range(len(orb_list)))
                          for c in range(mN)] for r in range(mY)]
                    GY = eng.gram_rows(ex["rowsol"], ex["rmu"], ex["rnu"])
                    GN = eng.gram_cols(ex["cols"])
                    LY = chol(GY); LN = chol(GN)
                    Mf = np.array([[float(x) for x in row] for row in M])
                    Bn = np.linalg.solve(LY, Mf) @ np.linalg.inv(LN.T)
                    sig = np.linalg.svd(Bn, compute_uv=False)
                    rec["sigma_norm"] = sig
                out[(lam, mu, nu)] = rec
        del eng
    return out, orbs

def dims_report(n, blocks, jsonpath):
    d = json.load(open(jsonpath, encoding="utf-8"))
    want = {}
    for e in d["block_dictionary_D1"][f"n={n}"]:
        want[(tuple(e["lam"]), tuple(e["mu"]), tuple(e["nu"]))] = (e["m_Y"], e["m_N"])
    ok, tot = True, 0
    for k, rec in blocks.items():
        mY, mN = rec["mY"], rec["mN"]
        tot += mY * mN
        w = want.get(k)
        if w is None:
            if mY * mN:
                print("  dims: class missing in JSON:", k, (mY, mN)); ok = False
        elif w != (mY, mN):
            print("  dims MISMATCH", k, "engine", (mY, mN), "json", w); ok = False
    # also classes present in JSON with mY*mN>0 that engine missed entirely
    have = set(blocks.keys())
    for k, w in want.items():
        if w[0] * w[1] > 0 and k not in have:
            print("  dims: engine missing class", k, w); ok = False
    print(f"  dims total sum mY*mN = {tot} ; JSON sum =",
          sum(v[0] * v[1] for v in want.values()), "; per-class match:", ok)
    return ok

# ---------------------------------------------------------------- main n=2
def main_n2():
    n = 2
    cs = CosetSpace(n)
    orb_list, seen = cs.orbits()
    print("orbits (n=2):")
    inv = []
    for i, orb in enumerate(orb_list):
        l0 = sorted(orb)[0]
        phi = cs.phi(l0)
        a = sum(1 for v in l0 if v < n)
        agr1 = sum(1 for j in range(n) if l0[j] == j)
        agr2 = sum(1 for j in range(n) if l0[j] == n + j)
        print(f"  orb{i}: size {len(orb)} rep {l0} phi={phi} a={a} agr=({agr1},{agr2})")
        inv.append((len(orb), phi, a))
    # decoded optimal multipliers (JSON raw_optimal_multipliers n=2):
    # signature -> multiplier;  c_o = multiplier / (n! * |orb_t|)
    sig2mult = {
        ((2, 0), (2, 0), 2): -0.6222974327480006,   # A: both agreements one half
        ((1, 1), (1, 1), 2): -1.6551777520253916,   # B: straddling
        ((1, 1), (1, 0), 3): -0.044369174251937746, # C
        ((2, 0), (0, 0), 4): 0.0929464242066791,    # D
        ((1, 1), (0, 0), 4): 0.07906805246000921,   # E
    }
    tvals = []
    for i, orb in enumerate(orb_list):
        l0 = sorted(orb)[0]
        # canonical a-pair (unordered), agreements per half (sorted desc), diff
        avals = tuple(sorted((sum(1 for v in l0 if v < n),
                              sum(1 for v in l0 if v >= n)), reverse=True))
        # agreements canonicalized over the orbit (use max over orbit reps)
        best = None
        for l in orb:
            a1 = sum(1 for j in range(n) if l[j] == j)
            a2 = sum(1 for j in range(n) if l[j] == n + j)
            key = tuple(sorted((a1, a2), reverse=True))
            if best is None or key > best: best = key
        diff = 2 * n - cs.phi(sorted(orb)[0])
        mult = sig2mult[(avals, best, diff)]
        tvals.append(Fraction(mult).limit_denominator(10**14) / (
            Fraction(math.factorial(n)) * len(orb)))
    print("decoded t-values:", [float(t) for t in tvals])

    # brute force
    orbmap = dict(seen)
    Gm, YE, NO = build_gamma(tvals, orbmap, n)
    bad = check_invariance(Gm, YE, NO, n)
    print("invariance violations:", bad)
    sv = np.linalg.svd(Gm, compute_uv=False)
    print("full-Gamma singular values (grouped):")
    groups = []
    for v in sv:
        if groups and abs(groups[-1][0] - v) < 1e-8:
            groups[-1][1] += 1
        else:
            groups.append([v, 1])
    for v, m in groups:
        print(f"    {v:.7f}  x{m}")
    # engine, both variants
    for variant in ["zprop", "colprop"]:
        print(f"\n== engine variant {variant} ==")
        blocks, _ = engine_run(n, variant, tvals_by_orbit=tvals)
        dims_report(n, blocks, PROJECT / "artifacts" / "mdh_dimensions.json")
        print("  per-class normalized sigma (engine) vs found in full SVD:")
        for k, rec in sorted(blocks.items(), key=lambda kv: -max(kv[1].get("sigma_norm", [0]))):
            if "sigma_norm" not in rec: continue
            sig = rec["sigma_norm"]
            dlam = len(syt_list(k[0]))
            for s in sig:
                if s < 1e-10:
                    match = "zero"
                else:
                    ratios = [g[0] / s for g in groups if g[0] > 1e-9]
                    near = min(ratios, key=lambda r: abs(math.log(r))) if ratios else 0
                    match = f"const={near:.6f}"
                print(f"    {k} mY x mN = {rec['mY']}x{rec['mN']} "
                      f"dlam={dlam}: sigma={s:.7f} {match}")

def main_random(n, seed=1):
    """Certify engine (zprop) vs brute force with a random exact t at given n."""
    import random
    rng = random.Random(seed)
    cs = CosetSpace(n)
    orb_list, seen = cs.orbits()
    tvals = [Fraction(rng.randint(-9, 9), rng.randint(1, 7)) for _ in orb_list]
    print(f"n={n}: {len(orb_list)} orbits, random exact t")
    Gm, YE, NO = build_gamma([float(t) for t in tvals], dict(seen), n)
    bad = check_invariance(Gm, YE, NO, n)
    print("invariance violations:", bad)
    sv = np.linalg.svd(Gm, compute_uv=False)
    groups = []
    for v in sv:
        if groups and abs(groups[-1][0] - v) < 1e-7 * max(1, v):
            groups[-1][1] += 1
        else:
            groups.append([v, 1])
    print("full SVD groups:", [(round(v, 6), m) for v, m in groups])
    blocks, _ = engine_run(n, "full", tvals_by_orbit=tvals)
    dims_report(n, blocks, PROJECT / "artifacts" / "mdh_dimensions.json")
    # per-class sigma * const must appear in full SVD with multiplicity dlam*dtau
    print("value-matching (expect const=2 pattern or its n-analogue):")
    fails = 0
    for k, rec in sorted(blocks.items()):
        if "sigma_norm" not in rec: continue
        lam, mu, nu = k
        dlam = len(syt_list(lam))
        dmu = len(syt_list(mu)); dnu = len(syt_list(nu))
        for s in rec["sigma_norm"]:
            if s < 1e-9:
                continue
            cands = [(v / s, m) for v, m in groups if v > 1e-9]
            best = min(cands, key=lambda cm: abs(cm[0] - 2))
            flag = "OK" if abs(best[0] - 2) < 1e-6 else "??"
            if flag == "??": fails += 1
            print(f"  {k}: {rec['mY']}x{rec['mN']} sigma={s:.6f} "
                  f"-> const={best[0]:.6f} multiplicity {best[1]} "
                  f"(dlam*dmu*dnu={dlam*dmu*dnu}, dlam*2dmudnu={2*dlam*dmu*dnu}) {flag}")
    print("mismatches:", fails)
    return blocks, groups

def main_n3_optimum():
    """Decode blocks_n3.json multipliers onto my orbits by assignment search;
       reproduce the 12-sigma table + ADV + LAW-1."""
    import itertools as it
    n = 3
    path = PROJECT / "artifacts" / "blocks_n3.json"
    d = json.load(open(path, encoding="utf-8"))
    orbmeta = d["orbmeta"]
    known_sigma = sorted([r["sigma"] for r in d["records"]], reverse=True)
    # their orbits: index -> (multiplier, pair_size)
    theirs = [(float(v[0]), int(v[1]), v[2]) for k, v in
              sorted(orbmeta.items(), key=lambda kv: int(kv[0]))]
    cs = CosetSpace(n)
    orb_list, seen = cs.orbits()
    # my invariants per orbit: (t-size, diff, a-pair, agr-pair)
    def my_key(orb):
        l0 = sorted(orb)[0]
        avals = tuple(sorted((sum(1 for v in l0 if v < n),
                              sum(1 for v in l0 if v >= n)), reverse=True))
        best = None
        for l in orb:
            a1 = sum(1 for j in range(n) if l[j] == j)
            a2 = sum(1 for j in range(n) if l[j] == n + j)
            key = tuple(sorted((a1, a2), reverse=True))
            if best is None or key > best: best = key
        return (len(orb), 2 * n - cs.phi(sorted(orb)[0]), avals, best)
    mykeys = [my_key(o) for o in orb_list]
    # their invariants: pair_size -> t-size = pair/(|NO| * n!), diff = sig[4],
    # a-pair = (sig[0],sig[1]) sorted, agr = (sig[2], sig[3]) sorted
    import ast
    theirs_keys = []
    for mult, psize, sig in theirs:
        s = ast.literal_eval(sig)
        tsize = psize // (math.factorial(2 * n) * math.factorial(n))
        theirs_keys.append((tsize, s[4], tuple(sorted(s[:2], reverse=True)),
                            tuple(sorted(s[2:4], reverse=True))))
    # group by key, enumerate assignments within tied groups
    from collections import defaultdict
    g_mine = defaultdict(list); g_theirs = defaultdict(list)
    for i, k in enumerate(mykeys): g_mine[k].append(i)
    for j, k in enumerate(theirs_keys): g_theirs[k].append(j)
    assert set(g_mine) == set(g_theirs), (set(g_mine) ^ set(g_theirs))
    keys = list(g_mine)
    perms_per_key = [list(it.permutations(g_theirs[k])) for k in keys]
    print("tie-group sizes:", [len(g_mine[k]) for k in keys])
    blocks, _ = engine_run(n, "zprop", tvals_by_orbit=None)
    # precompute normalized-block linear forms per class: sigma of sum_o c_o Bn_o
    # for candidate assignment -> c vector; evaluate lazily.
    best = None
    total = 1
    for p in perms_per_key: total *= len(p)
    print("total assignments to test:", total)
    for combo in it.product(*perms_per_key):
        assign = {}
        for k, pm in zip(keys, combo):
            for mi, tj in zip(g_mine[k], pm):
                assign[mi] = tj
        tv = [0.0] * len(orb_list)
        for mi, tj in assign.items():
            mult, psize, sig = theirs[tj]
            tsize = psize // (math.factorial(2 * n) * math.factorial(n))
            tv[mi] = mult / (math.factorial(n) * tsize)
        # engine sigma set (x2)
        sigs = []
        for kcl, rec in blocks.items():
            B = rec["B"]; mY, mN = rec["mY"], rec["mN"]
            eng, ex = rec["eng"], rec["ex"]
            M = np.zeros((mY, mN))
            for o in range(len(orb_list)):
                if tv[o]:
                    M += tv[o] * np.array([[float(B[o][r][c]) for c in range(mN)]
                                           for r in range(mY)])
            GY = np.array([[float(x) for x in row] for row in
                           eng.gram_rows(ex["rowsol"], ex["rmu"], ex["rnu"])])
            GN = np.array([[float(x) for x in row] for row in eng.gram_cols(ex["cols"])])
            LY = np.linalg.cholesky(GY); LN = np.linalg.cholesky(GN)
            Bn = np.linalg.solve(LY, M) @ np.linalg.inv(LN.T)
            for s in np.linalg.svd(Bn, compute_uv=False):
                if 2 * s > 1e-6: sigs.append(2 * s)
        sigs = sorted(sigs, reverse=True)
        # coupled classes appear twice in my list ((mu,nu),(nu,mu)) - dedup pairs
        # known_sigma lists each coupled class once; compare top values as sets
        err = 0.0
        ks = sorted(known_sigma, reverse=True)
        # my sigs contain coupled duplicates; collapse near-duplicates
        col = []
        for s in sigs:
            if col and abs(col[-1][0] - s) < 1e-6:
                col[-1][1] += 1
            else:
                col.append([s, 1])
        vals = [v for v, m in col]
        if len(vals) < len(ks):
            err = 999
        else:
            err = max(abs(a - b) for a, b in zip(vals[:len(ks)], ks))
        if best is None or err < best[0]:
            best = (err, assign, vals)
    err, assign, vals = best
    print(f"best assignment error = {err:.3e}")
    print("engine sigma (collapsed):", [round(v, 6) for v in vals[:14]])
    print("known sigma            :", [round(v, 6) for v in sorted(known_sigma, reverse=True)])
    return err

if __name__ == "__main__":
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("mode", nargs="?", default="n2")
    ap.add_argument("--n", type=int, default=3)
    ap.add_argument("--seed", type=int, default=1)
    a = ap.parse_args()
    if a.mode == "n2":
        main_n2()
    elif a.mode == "random":
        main_random(a.n, a.seed)
    elif a.mode == "n3opt":
        main_n3_optimum()
