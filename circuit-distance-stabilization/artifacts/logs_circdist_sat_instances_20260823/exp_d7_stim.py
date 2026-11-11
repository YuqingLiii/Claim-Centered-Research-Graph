import sys, time, json
import sat_core as S, stimx as X
d = 7
code = S.rotated_surface_code(d)
Rmax = d + 2
scheds = {
 "std_aligned":      (('NW','NE','SW','SE'), ('NW','SW','NE','SE')),
 "mis_both":         (('NW','SW','NE','SE'), ('NW','NE','SW','SE')),
 "mis_Xonly":        (('NW','SW','NE','SE'), ('NW','SW','NE','SE')),
 "mis_Zonly":        (('NW','NE','SW','SE'), ('NW','NE','SW','SE')),
}
which = sys.argv[1]
basis = sys.argv[2]
piX, piZ = scheds[which]
sch = S.uniform_schedule(code, piX, piZ, which)
res = {}
for R in range(1, Rmax + 1):
    t = time.time()
    w, err = X.stim_distance(sch, R, basis)
    print("%s %s R=%d stim d_R=%d (%.1fs)" % (which, basis, R, w, time.time() - t), flush=True)
    res[R] = w
    json.dump(res, open("results_d7_stim_%s_%s.json" % (which, basis), "w"), indent=1)
