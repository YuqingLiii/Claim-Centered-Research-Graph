"""verify_rstab2.py -- hard verification of the R_stab = 2 finding on the
doubly hook-misaligned rotated surface d=5 schedule (member [2] of the uniform
family: piX = NW,SW,NE,SE ; piZ = NW,NE,SW,SE).

Three independent confirmations:
 (1) my spacetime detector matrix == stim's detector error model (projected),
 (2) stim's own search returns weight 4 at R=1 and weight 3 at R=2, with the
     R=2 witness spread over two rounds (stim's own circuit-error explanation),
 (3) my transfer witness at R=2 re-audited from raw fault locations.
"""
import sat_core as S, stimx as X, run_transfer as RT

c = S.rotated_surface_code(5)
sch = S.uniform_schedule(c, ('NW','SW','NE','SE'), ('NW','NE','SW','SE'), 'misalign2')
print("legal", sch.legal_ok, "MC", sch.mc_ok, "T", sch.T)

for R in (1,2,3):
    nA,nB = sch.nA, sch.nB
    ids={}; k=0
    for r in range(R):
        for b in range(nB): ids[k]=('b',b,r); k+=1
        if r>=1:
            for a in range(nA): ids[k]=('a',a,r); k+=1
    for b in range(nB): ids[k]=('b',b,R); k+=1
    sig = X.dem_signatures(sch,R,'Z')
    proj=set()
    for ds,os_ in sig:
        pr=frozenset(ids[i] for i in ds if ids[i][0]=='b')
        proj.add((pr,frozenset(os_)))
    proj.discard((frozenset(),frozenset()))
    cols,nrow,labels = S.spacetime_columns(sch,R)
    mine=set()
    for col in cols:
        pr=[];ob=[]
        for r in range(R+1):
            for b in range(nB):
                if (col>>(r*nB+b))&1: pr.append(('b',b,r))
        for j in range(len(c.zlog)):
            if (col>>((R+1)*nB+j))&1: ob.append(j)
        mine.add((frozenset(pr),frozenset(ob)))
    print("R=%d  model cross-check: stim DEM projected == my spacetime columns : %s  (%d classes)"
          % (R, proj==mine, len(mine)))

for R in (1,2,3):
    w, err = X.stim_distance(sch, R, 'Z')
    print("\nR=%d  stim min undetectable logical: weight %d" % (R,w))
    rounds=set()
    for e in err:
        for loc in e.circuit_error_locations:
            t = loc.tick_offset
            g = loc.instruction_targets.gate
            pp = "".join(str(p)[0] for p in loc.flipped_pauli_product) if loc.flipped_pauli_product else "?"
            print("    round %d  gate %-12s pauli %s" % (t, g, str(loc.flipped_pauli_product)[:90]))
            rounds.add(t)
    print("    STIM WITNESS spans rounds: %s" % sorted(rounds))

r = RT.run(sch, 3, 5, 'hook', 'verif', '.')
print("\ntransfer d_R (R=1..3):", [r['res'][(R,'all')] for R in (1,2,3)])
for R in (1,2,3):
    F,a = RT.witness(sch, R, r['paths'][R])
    print(" R=%d witness weight=%d rounds=%s undetectable=%s logical=%s distinct-locations=%d"
          % (R, a['weight'], sorted(set(x[0] for x in F)), a['undetectable'], a['logical'],
             len(set(map(str,F)))))
    for rr,loc in F: print("     round %d %s" % (rr,loc))
