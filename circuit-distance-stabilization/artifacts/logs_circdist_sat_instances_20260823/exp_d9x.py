import time, sat_core as S, milp, run_transfer as RT
code = S.rotated_surface_code(9)
s0 = S.uniform_schedule(code, ('NW','SW','NE','SE'), ('NW','NE','SW','SE'), 'mis_both_d9')
sch = s0.mirror()
for R in range(1, 8):
    t = time.time()
    v, wit = milp.dR_milp(sch, R, ub=9)
    a = RT.audit(sch, R, wit)
    print("d=9 mis_both sector X R=%d MILP d_R=%d (%.1fs) witness rounds=%s undetectable=%s logical=%s"
          % (R, v, time.time()-t, sorted(set(x[0] for x in wit)), a['undetectable'], a['logical']), flush=True)
