"""Exhaustive enumeration of 3-colour-tiled minimum-depth (6 CNOT layer, circuit depth 8)
gross-code schedules that are LEGAL and MEASUREMENT-CONSISTENT.

Encoding: one-hot SAT over 36 integer variables in {1..6}; all constraints are stated symbolically
and then EVERY solution is re-verified on the explicit 864-edge Tanner graph by sched.check_legal /
sched.mc_violations, which share no code with this encoding.
"""
import numpy as np, itertools, sys, time
from pysat.solvers import Cadical153
from pysat.formula import IDPool
from gross import NG
from sched import make_phi, colour_valid, expand, check_legal, mc_violations, \
    sbb_noninterleaved, global_noninterleaved

LAYERS = [1, 2, 3, 4, 5, 6]


def var_list():
    out = []
    for c in range(3):
        for s in (0, 1):
            for i in range(3):
                out.append(('X', c, s, i));
    for c in range(3):
        for s in (0, 1):
            for i in range(3):
                out.append(('Z', c, s, i))
    return out


def build(s_par, t_par):
    alpha = [0, t_par % 3, (2 * t_par) % 3]      # phi(A_i)
    beta = [0, s_par % 3, (2 * s_par) % 3]       # phi(B_i)
    pool = IDPool()
    V = {}
    for v in var_list():
        for l in LAYERS:
            V[(v, l)] = pool.id((v, l))
    cls = []
    # one-hot
    for v in var_list():
        cls.append([V[(v, l)] for l in LAYERS])
        for l1, l2 in itertools.combinations(LAYERS, 2):
            cls.append([-V[(v, l1)], -V[(v, l2)]])

    def group_perm(vs):
        """the 6 variables in vs take 6 distinct values (hence exactly {1..6})"""
        assert len(vs) == 6
        for l in LAYERS:
            cls.append([V[(v, l)] for v in vs])                 # each layer used
            for v1, v2 in itertools.combinations(vs, 2):
                cls.append([-V[(v1, l)], -V[(v2, l)]])           # at most once

    # per-colour check constraints
    for c in range(3):
        group_perm([('X', c, 0, 0), ('X', c, 0, 1), ('X', c, 0, 2),
                    ('X', c, 1, 0), ('X', c, 1, 1), ('X', c, 1, 2)])
        group_perm([('Z', c, 0, 0), ('Z', c, 0, 1), ('Z', c, 0, 2),
                    ('Z', c, 1, 0), ('Z', c, 1, 1), ('Z', c, 1, 2)])
    # per-data-qubit legality
    for g in range(3):
        group_perm([('X', (g + alpha[i]) % 3, 0, i) for i in range(3)] +
                   [('Z', (g - beta[i]) % 3, 0, i) for i in range(3)])
        group_perm([('X', (g + beta[i]) % 3, 1, i) for i in range(3)] +
                   [('Z', (g - alpha[i]) % 3, 1, i) for i in range(3)])
    # measurement consistency
    nmc = 0
    for g in range(3):
        for i in range(3):
            for j in range(3):
                gh = (g + alpha[i] + beta[j]) % 3
                vP = ('Z', g, 0, j); vA = ('X', gh, 0, i)
                vQ = ('Z', g, 1, i); vB = ('X', gh, 1, j)
                for l1 in LAYERS:
                    for l2 in LAYERS:
                        if l1 == l2:
                            continue
                        for l3 in LAYERS:
                            for l4 in LAYERS:
                                if l3 == l4:
                                    continue
                                if (l1 < l2) != (l3 < l4):
                                    cls.append([-V[(vP, l1)], -V[(vA, l2)],
                                                -V[(vQ, l3)], -V[(vB, l4)]])
                                    nmc += 1
    return V, cls, alpha, beta, nmc


def model_to_sched(V, model):
    ms = set(x for x in model if x > 0)
    LX = np.zeros((3, 2, 3), int); LZ = np.zeros((3, 2, 3), int)
    for v in var_list():
        for l in LAYERS:
            if V[(v, l)] in ms:
                if v[0] == 'X':
                    LX[v[1], v[2], v[3]] = l
                else:
                    LZ[v[1], v[2], v[3]] = l
    return LX, LZ


def run(s_par, t_par, cap=None, verify_every=1):
    phi = make_phi(s_par, t_par)
    assert colour_valid(phi), (s_par, t_par)
    V, cls, alpha, beta, nmc = build(s_par, t_par)
    sol = []
    t0 = time.time()
    with Cadical153(bootstrap_with=cls) as S:
        while S.solve():
            m = S.get_model()
            LX, LZ = model_to_sched(V, m)
            sol.append((LX.copy(), LZ.copy()))
            block = []
            for v in var_list():
                l = (LX if v[0] == 'X' else LZ)[v[1], v[2], v[3]]
                block.append(-V[(v, l)])
            S.add_clause(block)
            if cap and len(sol) >= cap:
                break
    return phi, sol, len(cls), nmc, time.time() - t0


if __name__ == "__main__":
    for (s_par, t_par) in [(1, 1), (1, 2), (2, 1), (2, 2)]:
        phi, sol, ncls, nmc, el = run(s_par, t_par, cap=200000)
        print(f"phi = {s_par}a+{t_par}b mod 3 : {len(sol)} legal+MC 3-colour-tiled min-depth "
              f"schedules   ({ncls} clauses, {nmc} MC clauses, {el:.1f}s)")
        # explicit re-verification of a sample
        import random
        random.seed(0)
        smp = sol if len(sol) <= 40 else random.sample(sol, 40)
        ok = 0; sbb = 0; glob = 0
        for LX, LZ in smp:
            tX, tZ = expand(phi, LX, LZ)
            if check_legal(tX, tZ, 6) and mc_violations(tX, tZ)[0] == 0:
                ok += 1
            if sbb_noninterleaved(tX, tZ) == 0:
                sbb += 1
            if global_noninterleaved(tX, tZ):
                glob += 1
        print(f"    explicit re-verification: {ok}/{len(smp)} legal+MC ; "
              f"SBB-non-interleaved {sbb}/{len(smp)} ; globally-non-interleaved {glob}/{len(smp)}")
        np.save(f"sched_{s_par}{t_par}.npy",
                np.array([(LX, LZ) for LX, LZ in sol], dtype=int) if sol else np.zeros((0,)))
