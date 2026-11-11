"""exp_d9.py -- growth test for the doubly hook-misaligned family at d = 9
(and d = 11 if it fits).  Method: exact MILP on my spacetime matrix, plus stim
where it terminates.  Purpose: test the conjecture d_R = max(d-R, (d+1)/2),
R_stab = (d-1)/2, seen at d = 3, 5, 7."""
import sys, time, json
import sat_core as S, milp, stimx as X, run_transfer as RT
d = int(sys.argv[1]); meth = sys.argv[2]
code = S.rotated_surface_code(d)
sch = S.uniform_schedule(code, ('NW','SW','NE','SE'), ('NW','NE','SW','SE'), 'mis_both_d%d' % d)
print("# d=%d mis_both legal=%s MC=%s" % (d, sch.legal_ok, sch.mc_ok), flush=True)
Rmax = (d + 1) // 2 + 2
for R in range(1, Rmax + 1):
    t = time.time()
    if meth == "milp":
        v, wit = milp.dR_milp(sch, R, ub=d, time_limit=3600.0)
        a = RT.audit(sch, R, wit) if v is not None else {}
        print("d=%d R=%d MILP d_R^Z=%s (%.1fs) witness rounds=%s undetectable=%s logical=%s"
              % (d, R, v, time.time() - t, sorted(set(x[0] for x in wit)) if v else None,
                 a.get('undetectable'), a.get('logical')), flush=True)
    else:
        w, _ = X.stim_distance(sch, R, 'Z')
        print("d=%d R=%d stim d_R^Z=%d (%.1fs)" % (d, R, w, time.time() - t), flush=True)
