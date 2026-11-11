"""Audit the best tiled state: (1) the class-orbit symmetry that licenses REPS-only decisions,
(2) the full canonical family over all 72 checks, (3) MULTI-ROUND repair-0 (not just
same-round) on every gamma of the surviving sector, (4) hook classification."""
import itertools, json, sys, time, collections
from lift import Schedule, Sector, popc, sameround_repair0
import gross as G, hunt as H
NG=G.NG; CSSG=G.CSSG
PX,PZ=H.pools(); pidxX=H.pair_index(PX); pidxZ=H.pair_index(PZ)
tidxX=H.triple_index(PX); tidxZ=H.triple_index(PZ)

def cls(g):
    i,j=divmod(g,6); return (i+j)%3
REPS=[next(g for g in range(NG) if cls(g)==c) for c in range(3)]
def build(T):
    XL=[T[0+3*c:3+3*c] for c in range(3)]; XR=[T[9+3*c:12+3*c] for c in range(3)]
    ZL=[T[18+3*c:21+3*c] for c in range(3)]; ZR=[T[27+3*c:30+3*c] for c in range(3)]
    tX={};tZ={}
    for g in range(NG):
        c=cls(g)
        for i,mo in enumerate(G.Amon): tX[(g,G.gadd(g,mo))]=XL[c][i]
        for j,mo in enumerate(G.Bmon): tX[(g,NG+G.gadd(g,mo))]=XR[c][j]
        for j,mo in enumerate(G.Bmon): tZ[(G.gadd(g,(-mo[0],-mo[1])),g)]=ZL[c][j]
        for i,mo in enumerate(G.Amon): tZ[(NG+G.gadd(g,(-mo[0],-mo[1])),g)]=ZR[c][i]
    return Schedule(CSSG,tX,tZ)
class T0:  build=staticmethod(build); REPS=REPS

T=json.load(open(sys.argv[1]))
s=T0.build(T)
print("legal=%s  mc_violations=%d  pair_int=%d  strict_pair_int=%d  glob_int=%s"
      %(s.legal(),len(s.mc_violations()),s.interleaved_pairs(),
        s.strict_interleaved_pairs(),s.globally_interleaved()))

def multiround0(sec,a,S,singles,maxg=3):
    """repair(gamma)=0 with the gamma split over consecutive rounds (LIFT')."""
    items=[('h',a,S)]+[('s',None,[q]) for q in singles]
    n=len(items)
    Us=[]; Ss=[]
    for it in items:
        Ss.append(sec.s_of(it[2]))
        Us.append([sec.u_hook(it[1],it[2])] if it[0]=='h' else sec.Uq[it[2][0]])
    for g in range(2,maxg+1):
        # assign items to g consecutive rounds; brute force is 3^11 = 177k for g=3
        for assign in itertools.product(range(g),repeat=n):
            if len(set(assign))!=g: continue
            acc=0; ok=True
            for r in range(g):
                grp=[i for i in range(n) if assign[i]==r]
                need=acc
                # meet in the middle inside the group
                h=len(grp)//2
                tab=set()
                for cmb in itertools.product(*[Us[i] for i in grp[:h]]):
                    v=0
                    for x in cmb: v^=x
                    tab.add(v)
                found=False
                for cmb in itertools.product(*[Us[i] for i in grp[h:]]):
                    v=0
                    for x in cmb: v^=x
                    if (v^need) in tab: found=True; break
                if not found: ok=False; break
                for i in grp: acc^=Ss[i]
            if ok and acc==0: return assign
    return None

for lab,mir,pidx,tidx in (('Zmem',False,pidxX,tidxX),('Xmem',True,pidxZ,tidxZ)):
    sec=Sector(CSSG,s,mirror=mir)
    g2=H.gain2_count(sec,pidx,tidx)
    kinds=collections.Counter(sec.classify_hook(a,sec.hook(a,2))[0] for a in range(NG))
    n0f,ntf,_=H.decide_rate(sec,pidx)                 # all 72 checks
    n0r,ntr,_=H.decide_rate(sec,pidx,T0.REPS)         # 3 class representatives
    print("%s: gain2=%d hooks2=%s  FULL(72 checks) repair-0 %d/%d   REPS(3) %d/%d  [x24 = %d/%d]"
          %(lab,g2,dict(kinds),n0f,ntf,n0r,ntr,24*n0r,24*ntr))
    if n0f==0 and ntf>0:
        # multi-round audit on every canonical gamma
        bad=0; tot=0; t0=time.time()
        for a in range(NG):
            S=sec.hook(a,2)
            for V in pidx.get(tuple(sorted(S)),[]):
                singles=[q for q in H.bits(V) if q not in S]
                tot+=1
                if multiround0(sec,a,S,singles,maxg=2) is not None: bad+=1
            if time.time()-t0>240: print("   (multi-round audit truncated at check",a,")"); break
        print("   MULTI-ROUND (2-group) repair-0 found on %d of %d audited canonical gammas"%(bad,tot))
