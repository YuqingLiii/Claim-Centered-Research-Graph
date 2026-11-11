"""THE DIRECTED HUNT: 3-colour-TILED schedules (the published candidate's own family,
phi(x^i y^j) = (i+j) mod 3), 36 free times, annealed against
   1000*(MC violations) + 100*(d_eff<=10 in either sector) + 10*(horizontal 2-suffix hooks)
        + (canonical gammas with repair 0).
A state with cost 0 is a stage-1 D*=12 gap candidate in BOTH sectors."""
import itertools, random, sys, json, time, collections
from lift import Schedule, Sector, popc
import gross as G, hunt as H
NG=G.NG; CSSG=G.CSSG
SEED=int(sys.argv[2]) if len(sys.argv)>2 else 5
rng=random.Random(SEED)
PX,PZ=H.pools(); pidxX=H.pair_index(PX); pidxZ=H.pair_index(PZ)
tidxX=H.triple_index(PX); tidxZ=H.triple_index(PZ)

def cls(g):
    i,j=divmod(g,6); return (i+j)%3
REPS=[g for c in range(3) for g in range(NG) if cls(g)==c][:0]
REPS=[]
for c in range(3):
    REPS.append(next(g for g in range(NG) if cls(g)==c))

def build(T):
    """T = list of 36 times: [XL c i]*9, [XR c j]*9, [ZL c j]*9, [ZR c i]*9"""
    XL=[T[0+3*c:3+3*c] for c in range(3)]
    XR=[T[9+3*c:12+3*c] for c in range(3)]
    ZL=[T[18+3*c:21+3*c] for c in range(3)]
    ZR=[T[27+3*c:30+3*c] for c in range(3)]
    tX={};tZ={}
    for g in range(NG):
        c=cls(g)
        for i,mo in enumerate(G.Amon): tX[(g,G.gadd(g,mo))]=XL[c][i]
        for j,mo in enumerate(G.Bmon): tX[(g,NG+G.gadd(g,mo))]=XR[c][j]
        for j,mo in enumerate(G.Bmon): tZ[(G.gadd(g,(-mo[0],-mo[1])),g)]=ZL[c][j]
        for i,mo in enumerate(G.Amon): tZ[(NG+G.gadd(g,(-mo[0],-mo[1])),g)]=ZR[c][i]
    return Schedule(CSSG,tX,tZ)

def cost(T, detail=False):
    s=build(T)
    mv=len(s.mc_violations())
    if mv: return 1000*mv, None
    if not s.legal(): return 900, None
    c=0; det={}
    for lab,mir,pidx,tidx in (('Z',False,pidxX,tidxX),('X',True,pidxZ,tidxZ)):
        sec=Sector(CSSG,s,mirror=mir)
        bad=H.gain2_count(sec,pidx,tidx)
        h=sum(1 for a in REPS if sec.classify_hook(a,sec.hook(a,2))[0] in ('trivial','horizontal'))
        n0=nt=0
        if bad==0 and h==0:
            n0,nt,_=H.decide_rate(sec,pidx,REPS)
        c+= 20*bad + 10*h + n0
        det[lab]=(bad,h,n0,nt)
    return c, (det,s)

import os
if len(sys.argv)>3 and os.path.exists(sys.argv[3]):
    T=json.load(open(sys.argv[3]))
    for _ in range(int(sys.argv[4]) if len(sys.argv)>4 else 0):
        i,j=rng.randrange(36),rng.randrange(36); T[i],T[j]=T[j],T[i]
else:
    T=list(range(36)); rng.shuffle(T)
cur,_=cost(T)
ITERS=int(sys.argv[1]) if len(sys.argv)>1 else 20000
t0=time.time(); bestc=cur; bestT=T[:]
for it in range(ITERS):
    i,j=rng.randrange(36),rng.randrange(36)
    if i==j: continue
    T[i],T[j]=T[j],T[i]
    c,_=cost(T)
    if c<=cur:
        cur=c
        if c<bestc: bestc=c; bestT=T[:]
        if c==0: break
    else:
        T[i],T[j]=T[j],T[i]
    if it%4000==0:
        print("  it %6d cost %5d best %5d  (%.0fs)"%(it,cur,bestc,time.time()-t0)); sys.stdout.flush()
c,info=cost(bestT)
print("seed %d: BEST COST %d after %d proposals (%.0fs)"%(SEED,bestc,it+1,time.time()-t0))
if info:
    det,s=info
    print("   mc=%d legal=%s pair_int=%d strict_pair_int=%d glob_int=%s"
          %(len(s.mc_violations()),s.legal(),s.interleaved_pairs(),
            s.strict_interleaved_pairs(),s.globally_interleaved()))
    print("   per sector (d_eff<=10?, horizontal hooks/3, repair-0 count, family size):",det)
    json.dump(bestT,open('tiled_best_%d.json'%SEED,'w'))
    if c==0:
        print("*** STAGE-1 GAP CANDIDATE, BOTH SECTORS ***")
        json.dump(bestT,open('tiled_gapcand_%d.json'%SEED,'w'))
