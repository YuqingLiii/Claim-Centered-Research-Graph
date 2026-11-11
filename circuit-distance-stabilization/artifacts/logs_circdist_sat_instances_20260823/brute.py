"""
brute.py -- FOURTH method, used only for the small weights that carry the
R_stab > 1 claim: exhaustive enumeration of every fault configuration of weight
<= w over R rounds, tested directly against criterion (W).

No C code, no stim, no solver: this walks all multisets of distinct one-round
effect classes, round by round, and applies
    undetectable  <=>  u(S_r) = H_Z sigma_r for all r, and H_Z sigma_R = 0
    logical       <=>  sigma_R != 0   (class in Sigma = F2^n / rowspace H_X)
A minimum-weight configuration never repeats an effect inside a round (two equal
effects cancel), so deduplicating the one-round effect list is lossless.
"""

import itertools
import sat_core as S


def prepare(sch):
    code = sch.code
    Q = S.Quotient(code.xchecks, code.n)
    eff = {}
    for (E, u, loc) in S.generators(sch):
        eff.setdefault((Q.cls(E), u), loc)
    keys = sorted(eff)
    HZ = {}
    return Q, keys, eff


def hz(code, Q, s):
    return S.syndrome(code, Q.rep(s), "Z")


def exists_witness(sch, R, w):
    """True iff some configuration of weight exactly w is undetectable+logical."""
    code = sch.code
    Q, keys, eff = prepare(sch)
    n = len(keys)
    hzc = {}

    def HZ(s):
        if s not in hzc:
            hzc[s] = S.syndrome(code, Q.rep(s), "Z")
        return hzc[s]

    # per-round options of weight j: dict from (delta, mu) -> witness tuple
    opts = {0: {(0, 0): ()}}
    for j in range(1, w + 1):
        cur = {}
        for combo in itertools.combinations(range(n), j):
            d = u = 0
            for i in combo:
                d ^= keys[i][0]
                u ^= keys[i][1]
            cur.setdefault((d, u), combo)
        opts[j] = cur

    def rec(r, sigma, left):
        if r == R:
            return (left == 0 and sigma != 0 and HZ(sigma) == 0), []
        mu = HZ(sigma)
        for j in range(0, left + 1):
            for (d, uu), combo in opts[j].items():
                if uu != mu:
                    continue
                ok, tail = rec(r + 1, sigma ^ d, left - j)
                if ok:
                    return True, [(r, combo)] + tail
        return False, []

    return rec(0, 0, w)


def min_weight(sch, R, wmax):
    for w in range(1, wmax + 1):
        ok, wit = exists_witness(sch, R, w)
        if ok:
            return w, wit
    return None, None
