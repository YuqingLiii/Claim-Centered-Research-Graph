"""
exp_bb.py -- ARM 2 (task-002): explicit qLDPC instance.

Code: bivariate-bicycle [[18,4,4]] with l = m = 3,
      A = 1 + y + x        (monomial exponents (0,0),(0,1),(1,0))
      B = 1 + y + x^2 y    (monomial exponents (0,0),(0,1),(2,1))
      H_X = [A|B], H_Z = [B^T|A^T]; every check has weight 6, every qubit has
      degree 3 in H_X and 3 in H_Z, and BOTH check families are DEPENDENT
      (9 checks, rank 7) -- which exercises scope clause T0 of the transfer node.

Schedule: the depth-6 monomial-slot family has 25920 legal members and ZERO
measurement-consistent ones (exhaustive, see search_schedules), so the instance
uses the non-interleaved schedule NI: X-check CNOTs in slots 0..5 (monomial
order A1,A2,A3,B1,B2,B3), Z-check CNOTs in slots 6..11 (B1^T,B2^T,B3^T,A1^T,
A2^T,A3^T).  (MC) holds identically because every Z-CNOT follows every X-CNOT.

AGGREGATION CONVENTION: d_R = min(d_R^Z, d_R^X), as everywhere in this session.
"""

import sys, time, json
import sat_core as S
import bb, run_transfer as RT, milp, stimx as X

A = [(0, 0), (0, 1), (1, 0)]
B = [(0, 0), (0, 1), (2, 1)]
code = bb.bb_code(3, 3, A, B)
print("# BB code l=m=3  A=%s  B=%s" % (A, B))
print("# n=%d k=%d rank(H_X)=%d rank(H_Z)=%d |A|=%d |B|=%d dim Sigma=%d"
      % (code.n, code.k, code.rx, code.rz, len(code.xchecks), len(code.zchecks),
         code.n - code.rx))
print("# check weights: X %s  Z %s ; qubit degree in H_X: %s"
      % (sorted(set(S.popcount(x) for x in code.xchecks)),
         sorted(set(S.popcount(x) for x in code.zchecks)),
         sorted(set(sum(1 for a in code.xchecks if (a >> q) & 1) for q in range(code.n)))))
print("# H_X rows:", [bin(x)[2:].zfill(code.n)[::-1] for x in code.xchecks])
print("# H_Z rows:", [bin(x)[2:].zfill(code.n)[::-1] for x in code.zchecks])
print("# X logicals:", [bin(x)[2:].zfill(code.n)[::-1] for x in code.xlog])
print("# Z logicals:", [bin(x)[2:].zfill(code.n)[::-1] for x in code.zlog])

# exhaustive check of the observable convention (Standing fact 2.2 for this code)
ker = bb.nullspace(code.zchecks, code.n)
Q = S.Quotient(code.xchecks, code.n)
bad = 0
for msk in range(1 << len(ker)):
    v, t, i = 0, msk, 0
    while t:
        if t & 1:
            v ^= ker[i]
        t >>= 1
        i += 1
    lam = any(S.popcount(L & v) % 2 for L in code.zlog)
    if lam != (Q.cls(v) != 0):
        bad += 1
print("# observable convention exhaustively verified over ker H_Z (%d vectors): %d mismatches"
      % (1 << len(ker), bad))
dX = bb.brute_distance(code, "X")
dZ = bb.brute_distance(code, "Z")
print("# exhaustive code distances: d_X=%d d_Z=%d  -> d=%d" % (dX, dZ, min(dX, dZ)))
d = min(dX, dZ)

nl, nmc, keep = bb.search_schedules(code, 3, 3, A, B, want=4)
print("# depth-6 monomial-slot family: 6!*6! = 518400 candidates, %d legal, %d legal+(MC)"
      % (nl, nmc))

# non-interleaved schedule
sigX = {"A0": 0, "A1": 1, "A2": 2, "B0": 3, "B1": 4, "B2": 5}
sigZ = {"Bt0": 6, "Bt1": 7, "Bt2": 8, "At0": 9, "At1": 10, "At2": 11}
sch = bb.build_schedule(code, 3, 3, A, B, sigX, sigZ, "NI")
print("# schedule NI: T=%d legal=%s (MC)=%s" % (sch.T, sch.legal_ok, sch.mc_ok))
print("# CNOT list (time, kind, check, data):")
for cn in sch.cnots:
    print("#   ", cn)
occupied = set(t for t, _, _, _ in sch.cnots)
print("# idle layers (no CNOT at all): %s -> schedule space is %s"
      % (sorted(set(range(sch.T)) - occupied),
         "compressed" if len(occupied) == sch.T else "NOT compressed"))

Rmax = d + 2
out = {}
for sector, s in (("Z", sch), ("X", sch.mirror())):
    t0 = time.time()
    r = RT.run(s, Rmax, d, "hook", "bb_%s_hook" % sector, ".")
    rm = RT.run(s, Rmax, d, "meas", "bb_%s_meas" % sector, ".")
    vals = [r["res"][(R, "all")] for R in range(1, Rmax + 1)]
    print("\nsector %s : transfer d_R = %s  (dimSigma=%d ngen=%d %.1fs)"
          % (sector, vals, r["dim"], r["ngen"], time.time() - t0))
    print("  one round only  : %s" % [r["res"][(R, "rounds1")] for R in range(1, Rmax + 1)])
    print("  >= 2 rounds     : %s" % [r["res"][(R, "rounds2")] for R in range(1, Rmax + 1)])
    print("  uses hook fault : %s" % [r["res"][(R, "flag1")] for R in range(1, Rmax + 1)])
    print("  no hook fault   : %s" % [r["res"][(R, "flag0")] for R in range(1, Rmax + 1)])
    print("  uses meas fault : %s" % [rm["res"][(R, "flag1")] for R in range(1, Rmax + 1)])
    print("  no meas fault   : %s" % [rm["res"][(R, "flag0")] for R in range(1, Rmax + 1)])
    out["transfer_" + sector] = vals
    out["restr_" + sector] = {k: [r["res"][(R, k)] for R in range(1, Rmax + 1)]
                              for k in ("rounds1", "rounds2", "flag1", "flag0")}
    out["restr_" + sector]["meas1"] = [rm["res"][(R, "flag1")] for R in range(1, Rmax + 1)]
    out["restr_" + sector]["meas0"] = [rm["res"][(R, "flag0")] for R in range(1, Rmax + 1)]
    for R in range(1, Rmax + 1):
        if R in r["paths"]:
            F, a = RT.witness(s, R, r["paths"][R])
            if F is None:
                print("  witness R=%d FAILED %s" % (R, a))
                continue
            print("  WITNESS R=%d weight=%d rounds=%s undetectable=%s logical=%s obs=%s"
                  % (R, a["weight"], sorted(set(x[0] for x in F)), a["undetectable"],
                     a["logical"], a["observable"]))
            for rr, loc in F:
                print("     round %d  %s" % (rr, loc))

for basis in ("Z", "X"):
    vs = []
    for R in range(1, Rmax + 1):
        w, _ = X.stim_distance(sch, R, basis)
        vs.append(w)
    print("sector %s : stim     d_R = %s   AGREE=%s"
          % (basis, vs, vs == out["transfer_" + basis]))
    out["stim_" + basis] = vs

mv = []
for R in range(1, Rmax + 1):
    v, w = milp.dR_milp(sch, R)
    mv.append(v)
print("sector Z : MILP     d_R = %s   AGREE=%s" % (mv, mv == out["transfer_Z"]))
out["milp_Z"] = mv

dmin = [min(a, b) for a, b in zip(out["transfer_Z"], out["transfer_X"])]
out["d_R"] = dmin
out["d_inf"] = dmin[-1]
out["R_stab"] = next(R for R in range(1, Rmax + 1) if all(v == dmin[-1] for v in dmin[R - 1:]))
print("\n>>> BB [[18,4,4]] schedule NI : d_R (min over sectors) = %s  d_infinity=%d  R_stab=%d"
      % (dmin, out["d_inf"], out["R_stab"]))
json.dump(out, open("results_bb.json", "w"), indent=1, default=str)
