"""exp_d7_extra.py -- MILP for the reduced sector of the two singly-misaligned
d=7 classes (the sector the other run reaches last)."""
import time, sat_core as S, milp, run_transfer as RT
code = S.rotated_surface_code(7)
for nm, piX, piZ, sector in [("mis_Zonly", ('NW','NE','SW','SE'), ('NW','NE','SW','SE'), "X"),
                             ("mis_Xonly", ('NW','SW','NE','SE'), ('NW','SW','NE','SE'), "Z")]:
    s0 = S.uniform_schedule(code, piX, piZ, nm)
    sch = s0 if sector == "Z" else s0.mirror()
    for R in range(1, 10):
        t = time.time()
        v, wit = milp.dR_milp(sch, R, ub=7)
        a = RT.audit(sch, R, wit)
        print("%s sector %s R=%d MILP d_R=%d (%.1fs) witness rounds=%s undetectable=%s logical=%s"
              % (nm, sector, R, v, time.time()-t, sorted(set(x[0] for x in wit)),
                 a['undetectable'], a['logical']), flush=True)
