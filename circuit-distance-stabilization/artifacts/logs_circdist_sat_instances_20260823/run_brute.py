"""run_brute.py -- exhaustive enumeration (method B) for the weights that carry
the R_stab > 1 claim and the d=5 standard lower bound."""
import sat_core as S, brute, time, itertools
c5=S.rotated_surface_code(5); c3=S.rotated_surface_code(3)
cases=[('d5 mis_both',S.uniform_schedule(c5,('NW','SW','NE','SE'),('NW','NE','SW','SE'),'m'),[(1,4),(2,3),(3,3)]),
       ('d5 standard',S.uniform_schedule(c5,('NW','NE','SW','SE'),('NW','SW','NE','SE'),'s'),[(1,4),(2,4)]),
       ('d3 mis_both',S.uniform_schedule(c3,('NW','SW','NE','SE'),('NW','NE','SW','SE'),'m'),[(1,2),(2,2)]),
       ('d3 standard',S.uniform_schedule(c3,('NW','NE','SW','SE'),('NW','SW','NE','SE'),'s'),[(1,3),(2,3)])]
for nm,s,rs in cases:
    Q,keys,eff = brute.prepare(s)
    print("%s : %d distinct one-round effect classes (Z-sector)" % (nm,len(keys)), flush=True)
    for (R,W) in rs:
        for w in range(1,W+1):
            t=time.time(); ok,wit = brute.exists_witness(s,R,w)
            print("   %s R=%d weight<=%d : witness EXISTS=%s (%.1fs) %s"
                  % (nm,R,w,ok,time.time()-t, wit if ok else ""), flush=True)
            if ok: break
