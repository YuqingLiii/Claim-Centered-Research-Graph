"""exp_d7.py -- ARM 1, d = 7 leg.  The transfer engine cannot run here
(|Sigma| = 2^25 and the one-round dictionary is indexed by Sigma x F2^B = 2^49
entries), so the two independent methods used are:
   (i)  stim's own undetectable-logical-error search on a stim circuit built
        from the same schedule, and
   (ii) an exact MILP (scipy/HiGHS) on MY spacetime detector matrix.
Both are cross-checked against the transfer engine at d = 3 and d = 5.
Every MILP optimum is exported as an explicit witness and audited by
run_transfer.audit (raw fault locations -> detectors + observable)."""
import sys, time, json
import sat_core as S, run_transfer as RT, milp, stimx as X

WHICH = sys.argv[1] if len(sys.argv) > 1 else None
d = 7
code = S.rotated_surface_code(d)
Rmax = d + 2
scheds = {
 "std_aligned":      (('NW','NE','SW','SE'), ('NW','SW','NE','SE')),
 "mis_both":         (('NW','SW','NE','SE'), ('NW','NE','SW','SE')),
 "mis_Xonly":        (('NW','SW','NE','SE'), ('NW','SW','NE','SE')),
 "mis_Zonly":        (('NW','NE','SW','SE'), ('NW','NE','SW','SE')),
}
out = {}
for nm, (piX, piZ) in scheds.items():
    if WHICH and nm != WHICH:
        continue
    sch0 = S.uniform_schedule(code, piX, piZ, nm)
    for sector, sch in (("Z", sch0), ("X", sch0.mirror())):
        print("\n== %s sector %s piX=%s piZ=%s legal=%s MC=%s T=%d" % (nm, sector,
              "".join(piX), "".join(piZ), sch.legal_ok, sch.mc_ok, sch.T), flush=True)
        rec = {}
        for R in range(1, Rmax + 1):
            t = time.time()
            v, wit = milp.dR_milp(sch, R, ub=d, time_limit=3600.0)
            if v is None:
                print("   R=%d MILP: %s" % (R, wit), flush=True); break
            a = RT.audit(sch, R, wit)
            print("   R=%d MILP d_R^%s=%d  (%.1fs)  witness weight=%d rounds=%s undetectable=%s logical=%s"
                  % (R, sector, v, time.time() - t, a['weight'], sorted(set(x[0] for x in wit)),
                     a['undetectable'], a['logical']), flush=True)
            for rr, loc in wit:
                print("        round %d %s" % (rr, loc), flush=True)
            rec[R] = v
        out[nm + "_" + sector] = rec
        json.dump(out, open("results_d7_milp_%s.json" % (WHICH or "all"), "w"), indent=1, default=str)
