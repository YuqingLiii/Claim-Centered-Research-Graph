"""modelcheck.py -- set-equality of stim's detector error model with MY spacetime
detector matrix, for every legal+(MC) uniform schedule at d=3 and for the two
decisive d=5 and d=7 schedules.  This is what licenses methods M and T against S."""
import sat_core as S, stimx as X, sys

def check(sch, R, code):
    nA,nB = sch.nA, sch.nB
    ids={}; k=0
    for r in range(R):
        for b in range(nB): ids[k]=('b',b,r); k+=1
        if r>=1:
            for a in range(nA): ids[k]=('a',a,r); k+=1
    for b in range(nB): ids[k]=('b',b,R); k+=1
    proj=set()
    for ds,os_ in X.dem_signatures(sch,R,'Z'):
        proj.add((frozenset(ids[i] for i in ds if ids[i][0]=='b'),frozenset(os_)))
    proj.discard((frozenset(),frozenset()))
    cols,nrow,labels = S.spacetime_columns(sch,R)
    mine=set()
    for col in cols:
        pr=[];ob=[]
        for r in range(R+1):
            for b in range(nB):
                if (col>>(r*nB+b))&1: pr.append(('b',b,r))
        for j in range(len(code.zlog)):
            if (col>>((R+1)*nB+j))&1: ob.append(j)
        mine.add((frozenset(pr),frozenset(ob)))
    return proj==mine, len(mine), len(proj-mine), len(mine-proj)

c3=S.rotated_surface_code(3)
n=0
for piX in S.ORDER_NAMES:
    for piZ in S.ORDER_NAMES:
        s=S.uniform_schedule(c3,piX,piZ,'x')
        if not (s.legal_ok and s.mc_ok): continue
        n+=1
        for R in (1,2,3):
            ok,m,a,b = check(s,R,c3)
            print("d=3 [%s|%s] R=%d equal=%s classes=%d onlystim=%d onlymine=%d"
                  % ("".join(piX),"".join(piZ),R,ok,m,a,b), flush=True)
print("# d=3: %d legal+(MC) schedules checked" % n)
c5=S.rotated_surface_code(5)
for nm,piX,piZ in [('std',('NW','NE','SW','SE'),('NW','SW','NE','SE')),
                   ('mis_both',('NW','SW','NE','SE'),('NW','NE','SW','SE'))]:
    s=S.uniform_schedule(c5,piX,piZ,nm)
    for R in (1,2,3):
        print("d=5 %s R=%d equal=%s classes=%d onlystim=%d onlymine=%d" % ((nm,R)+check(s,R,c5)), flush=True)
c7=S.rotated_surface_code(7)
for nm,piX,piZ in [('std',('NW','NE','SW','SE'),('NW','SW','NE','SE')),
                   ('mis_both',('NW','SW','NE','SE'),('NW','NE','SW','SE'))]:
    s=S.uniform_schedule(c7,piX,piZ,nm)
    for R in (1,2):
        print("d=7 %s R=%d equal=%s classes=%d onlystim=%d onlymine=%d" % ((nm,R)+check(s,R,c7)), flush=True)
import bb
A=[(0,0),(0,1),(1,0)]; B=[(0,0),(0,1),(2,1)]
cb=bb.bb_code(3,3,A,B)
sigX={"A0":0,"A1":1,"A2":2,"B0":3,"B1":4,"B2":5}
sigZ={"Bt0":6,"Bt1":7,"Bt2":8,"At0":9,"At1":10,"At2":11}
sb=bb.build_schedule(cb,3,3,A,B,sigX,sigZ,"NI")
for R in (1,2,3):
    print("BB NI R=%d equal=%s classes=%d onlystim=%d onlymine=%d" % ((R,)+check(sb,R,cb)), flush=True)
