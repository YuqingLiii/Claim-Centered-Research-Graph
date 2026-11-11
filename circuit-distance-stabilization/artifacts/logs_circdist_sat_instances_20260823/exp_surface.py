"""
exp_surface.py <d> [--stim] [--only i] -- ARM 1 of CIRCDIST.sat.instances.

Scans the uniform-permutation schedule family of the rotated surface code:
    S_unif(d) = { (piX, piZ) in S_4 x S_4 } , |S_unif| = 576,
every check acting on its present corners at the times given by its order.
Reports for each legal + (MC) member:
    hook geometry, d_R^Z and d_R^X for R = 1..d+2 by the independent min-plus
    transfer engine, the same by stim, the mechanism-restricted minima, and an
    explicit audited minimum witness.

AGGREGATION CONVENTION (stated because it is load-bearing, cf. W-G1 /
cor73-sector-flag-2026-08-23):  d_R(M) = min(d_R^Z(M), d_R^X(M)).
"""

import sys, time, json
import sat_core as S
import run_transfer as RT

STIM = "--stim" in sys.argv
d = int(sys.argv[1])
ONLY = None
if "--only" in sys.argv:
    ONLY = int(sys.argv[sys.argv.index("--only") + 1])

code = S.rotated_surface_code(d)
Rmax = d + 2
print("# rotated surface code d=%d : n=%d |A|=%d |B|=%d rank(H_X)=%d k=%d"
      % (d, code.n, len(code.xchecks), len(code.zchecks), code.rx, code.k))
print("# X_L = column 0 (vertical), Z_L = row 0 (horizontal)")
print("# aggregation convention: d_R = min(d_R^Z, d_R^X)")


def hook_geometry(sch, kind):
    """For each weight-4 check of the given type, the geometry of the weight-2
    hook (the last two data qubits in that check's CNOT order)."""
    tx, tz = sch.times()
    tt = tx if kind == "X" else tz
    checks = code.xchecks if kind == "X" else code.zchecks
    vert = horiz = other = 0
    for c, supp in enumerate(checks):
        qs = [q for q in range(code.n) if (supp >> q) & 1]
        if len(qs) != 4:
            continue
        qs.sort(key=lambda q: tt[(c, q)])
        a, b = qs[-2], qs[-1]
        if a % d == b % d:
            vert += 1
        elif a // d == b // d:
            horiz += 1
        else:
            other += 1
    return vert, horiz, other


members = []
for piX in S.ORDER_NAMES:
    for piZ in S.ORDER_NAMES:
        sch = S.uniform_schedule(code, piX, piZ, "x")
        if sch.legal_ok and sch.mc_ok:
            members.append((piX, piZ))
print("# search space 576 uniform (piX,piZ); legal: %d; legal+MC: %d"
      % (sum(1 for a in S.ORDER_NAMES for b in S.ORDER_NAMES
             if S.uniform_schedule(code, a, b, "x").legal_ok), len(members)))

results = []
for mi, (piX, piZ) in enumerate(members):
    if ONLY is not None and mi != ONLY:
        continue
    name = "".join(x[0] + x[1].lower() for x in piX) + "_" + "".join(x[0] + x[1].lower() for x in piZ)
    sch = S.uniform_schedule(code, piX, piZ, name)
    mir = sch.mirror()
    xv, xh, xo = hook_geometry(sch, "X")
    zv, zh, zo = hook_geometry(sch, "Z")
    # X hooks parallel to X_L (column, vertical) are the misaligned case for d^Z
    xmis = xv > 0
    zmis = zh > 0
    print("\n== [%d] piX=%s piZ=%s   T=%d  idle_layers=%d" %
          (mi, "".join(piX), "".join(piZ), sch.T, 0))
    print("   X-check hooks: vertical=%d horizontal=%d  -> %s (X_L is vertical)"
          % (xv, xh, "MISALIGNED" if xmis else "aligned"))
    print("   Z-check hooks: vertical=%d horizontal=%d  -> %s (Z_L is horizontal)"
          % (zv, zh, "MISALIGNED" if zmis else "aligned"))
    row = dict(idx=mi, piX=piX, piZ=piZ, xmis=xmis, zmis=zmis,
               hooks=[xv, xh, zv, zh])
    for sector, s in (("Z", sch), ("X", mir)):
        t0 = time.time()
        r = RT.run(s, Rmax, d, "hook", "d%d_%d_%s_hook" % (d, mi, sector), ".")
        rm = RT.run(s, Rmax, d, "meas", "d%d_%d_%s_meas" % (d, mi, sector), ".")
        vals = [r["res"][(R, "all")] for R in range(1, Rmax + 1)]
        print("   sector %s : transfer d_R = %s   (dimSigma=%d ngen=%d %.1fs)"
              % (sector, vals, r["dim"], r["ngen"], time.time() - t0))
        print("     restricted minima (63 = no witness of weight <= %d in that class):" % d)
        print("       one round only   : %s" % [r["res"][(R, "rounds1")] for R in range(1, Rmax + 1)])
        print("       >= 2 rounds      : %s" % [r["res"][(R, "rounds2")] for R in range(1, Rmax + 1)])
        print("       uses hook fault  : %s" % [r["res"][(R, "flag1")] for R in range(1, Rmax + 1)])
        print("       no hook fault    : %s" % [r["res"][(R, "flag0")] for R in range(1, Rmax + 1)])
        print("       uses meas fault  : %s" % [rm["res"][(R, "flag1")] for R in range(1, Rmax + 1)])
        print("       no meas fault    : %s" % [rm["res"][(R, "flag0")] for R in range(1, Rmax + 1)])
        row["transfer_" + sector] = vals
        row["restr_" + sector] = dict(
            rounds1=[r["res"][(R, "rounds1")] for R in range(1, Rmax + 1)],
            rounds2=[r["res"][(R, "rounds2")] for R in range(1, Rmax + 1)],
            hook1=[r["res"][(R, "flag1")] for R in range(1, Rmax + 1)],
            hook0=[r["res"][(R, "flag0")] for R in range(1, Rmax + 1)],
            meas1=[rm["res"][(R, "flag1")] for R in range(1, Rmax + 1)],
            meas0=[rm["res"][(R, "flag0")] for R in range(1, Rmax + 1)])
        # explicit witnesses
        for R in (1, Rmax):
            if R in r["paths"]:
                F, a = RT.witness(s, R, r["paths"][R])
                if F is None:
                    print("     witness R=%d: FAILED %s" % (R, a))
                else:
                    print("     WITNESS R=%d weight=%d rounds=%s undetectable=%s logical=%s"
                          % (R, a["weight"], sorted(set(x[0] for x in F)),
                             a["undetectable"], a["logical"]))
                    for (rr, loc) in F:
                        print("        round %d  %s" % (rr, loc))
                    row.setdefault("witness_" + sector, {})[R] = (
                        [(rr, list(map(str, loc))) for rr, loc in F], a["weight"],
                        a["undetectable"], a["logical"], sorted(set(x[0] for x in F)))
    if STIM:
        import stimx as X
        for basis in ("Z", "X"):
            vs = []
            for R in range(1, Rmax + 1):
                w, _ = X.stim_distance(sch, R, basis)
                vs.append(w)
            print("   sector %s : stim     d_R = %s" % (basis, vs))
            row["stim_" + basis] = vs
            key = "transfer_" + basis
            print("   AGREE %s: %s" % (basis, vs == row[key]))
            row["agree_" + basis] = (vs == row[key])
    dmin = [min(a, b) for a, b in zip(row["transfer_Z"], row["transfer_X"])]
    row["d_R"] = dmin
    row["d_inf"] = dmin[-1]
    row["R_stab"] = next(R for R in range(1, Rmax + 1)
                         if all(v == dmin[-1] for v in dmin[R - 1:]))
    print("   >>> d_R (min over sectors) = %s   d_infinity = %d  R_stab = %d  [R_stab valid: "
          "window theorem gives d_R = d_d for R >= d]" % (dmin, row["d_inf"], row["R_stab"]))
    results.append(row)

with open("results_surface_d%d%s.json" % (d, "" if ONLY is None else "_%d" % ONLY), "w") as f:
    json.dump(results, f, indent=1, default=str)
print("\n# done")
