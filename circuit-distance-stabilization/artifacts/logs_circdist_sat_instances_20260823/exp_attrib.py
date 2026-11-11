"""exp_attrib.py -- ARM 3 (task-003): exact mechanism attribution by restricted
exact optimisation.  For each instance and each R, four MILPs are solved over MY
spacetime matrix:
   plain         d_R
   single-round  min over r0 of (min weight with all faults inside round r0)
   no-hook       min weight using only faults whose one-round residual has
                 weight <= 1 (i.e. no correlated/hook fault)
   need-meas     min weight subject to using at least one fault whose one-round
                 residual is empty (a pure measurement/record mechanism)
Every one of these is an EXACT minimum over fault configurations, so
   single-round > d_R      proves  every minimum witness spans >= 2 rounds
   no-hook      > d_R      proves  every minimum witness uses a hook fault
   need-meas    > d_R      proves  NO minimum witness uses a measurement fault
and each such statement is an absence claim whose licensing scope is the whole
fault model of Definition 2.8 restricted to the stated sector -- i.e. exhaustive,
not sampled."""
import sys, time, json
import sat_core as S, bb, milp, run_transfer as RT

INST = sys.argv[1]
if INST.startswith("surf"):
    _, d, kind = INST.split("_", 2)
    d = int(d)
    code = S.rotated_surface_code(d)
    P = {"std": (('NW','NE','SW','SE'), ('NW','SW','NE','SE')),
         "misboth": (('NW','SW','NE','SE'), ('NW','NE','SW','SE'))}[kind]
    sch0 = S.uniform_schedule(code, P[0], P[1], INST)
    Rmax = d + 2
    cap = d
else:
    A = [(0, 0), (0, 1), (1, 0)]; B = [(0, 0), (0, 1), (2, 1)]
    code = bb.bb_code(3, 3, A, B)
    sigX = {"A0":0,"A1":1,"A2":2,"B0":3,"B1":4,"B2":5}
    sigZ = {"Bt0":6,"Bt1":7,"Bt2":8,"At0":9,"At1":10,"At2":11}
    sch0 = bb.build_schedule(code, 3, 3, A, B, sigX, sigZ, "NI")
    Rmax = 6; cap = 4

print("# instance %s  Rmax=%d" % (INST, Rmax), flush=True)
for sector, sch in (("Z", sch0), ("X", sch0.mirror())):
    for R in range(1, Rmax + 1):
        t = time.time()
        v, wit = milp.dR_milp(sch, R, ub=cap)
        sr = 99
        for r0 in range(R):
            x, _ = milp.dR_milp(sch, R, ub=cap, filt=lambda r, l, E, u, r0=r0: r == r0)
            if x is not None:
                sr = min(sr, x)
        nh, _ = milp.dR_milp(sch, R, ub=cap, filt=lambda r, l, E, u: S.popcount(E) < 2)
        nm, _ = milp.dR_milp(sch, R, ub=cap, require=lambda r, l, E, u: E == 0)
        a = RT.audit(sch, R, wit)
        print("%s sector %s R=%2d : d_R=%s single-round=%s no-hook=%s need-meas=%s "
              "| witness rounds=%s undetectable=%s logical=%s (%.1fs)"
              % (INST, sector, R, v, sr if sr < 99 else ">cap", nh, nm,
                 sorted(set(x[0] for x in wit)), a['undetectable'], a['logical'],
                 time.time() - t), flush=True)
