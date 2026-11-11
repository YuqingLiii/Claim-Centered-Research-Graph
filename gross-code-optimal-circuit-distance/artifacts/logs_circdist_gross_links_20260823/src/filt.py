"""LINK 3: reviewer's own re-derivation of the legality + (MC) + cascade filter."""
from gr import *
from geom import LAB, TYPE, blocks, xslots, zslots, overlaps
from itertools import permutations, product
import sys, pickle

SURV={('Z',(1,1)):{1,2,9,62},('Z',(2,2)):{1,2,9,62},('Z',(1,2)):{2,9},('Z',(2,1)):{2,9},
      ('X',(1,1)):{0,2,9,14},('X',(2,2)):{0,2,9,14},('X',(1,2)):{2,9},('X',(2,1)):{2,9}}
# residual-class table (same construction as casc.py)
CLS={}
def build_classes():
    idx=0; seen={}; out=[]
    for p in permutations(range(6)):
        r1=frozenset(p[0:2]); r2=frozenset(p[3:6]); r3=frozenset(p[4:6]); r2c=frozenset(p[0:3])
        key=(r1,min(r2,r2c,key=lambda s:sorted(s)),r3)
        key2=(r3,min(r2,r2c,key=lambda s:sorted(s)),r1)
        k=key if sorted(r1)<sorted(r3) else key2
        if k not in seen: seen[k]=len(out); out.append(p)
        CLS[p]=seen[k]
    return out
CANON=build_classes()
COLS=('blue','red','green'); EDGES=('e1','e2','e3','e4','e5','e6')
OV=overlaps()
PHIS=[(1,1),(1,2),(2,1),(2,2)]
def phiv(ph,g):
    i,j=divmod(g,M); return (ph[0]*i+ph[1]*j)%3

# ---- per-panel readings ------------------------------------------------------
def panel_readings(panel, sector, ph, t, restrict_geom):
    """returns list of (inv, straddle, triple, tau) with triple[c]=residual class"""
    out=[]
    b1={c:set(blocks(panel,c)[0]) for c in COLS}
    for perm in permutations(range(6)):          # perm[k] = slot of EDGES[k]
        inv=[None]*6
        for k,s in enumerate(perm): inv[s]=EDGES[k]
        if restrict_geom:
            # slots 0,1,2 must be one geometric half {D,V,V} or {D,H,H}
            ty=[TYPE[inv[s]] for s in range(3)]; ty2=[TYPE[inv[s]] for s in range(3,6)]
            if sorted(ty) not in (['D','V','V'],['D','H','H']): continue
            if sorted(ty2)==sorted(ty): continue
        for st in (0,1):
            trip={}; tau={}; ok=True
            for c in COLS:
                lab=LAB[panel][c]
                order=sorted(range(6), key=lambda s: lab[inv[s]])
                if st: order=order[3:]+order[:3]
                cl=CLS[tuple(order)]
                if cl not in SURV[(sector,ph)]: ok=False; break
                trip[c]=cl
                tau[c]=[lab[inv[s]]+(t if (st and inv[s] in b1[c]) else 0) for s in range(6)]
            if ok: out.append((tuple(inv),st,trip,tau))
    return out

SHARED=True
def run(restrict_geom, verbose=True):
    results=[]
    for ph in PHIS:
      for upper_is in ('X','Z'):
        lower_is='Z' if upper_is=='X' else 'X'
        for t in (6,7,8):
            RU=panel_readings('upper',upper_is,ph,t,restrict_geom)
            RL=panel_readings('lower',lower_is,ph,t,restrict_geom)
            if not RU or not RL: continue
            PX,PZ=(RU,RL) if upper_is=='X' else (RL,RU)
            for (invX,stX,tripX,tauX) in PX:
             for (invZ,stZ,tripZ,tauZ) in PZ:
              for cmX in permutations(COLS):        # cmX[kappa] = drawn colour of class kappa
               tX=[tauX[cmX[k]] for k in range(3)]
               # legality is independent of P and of the Z colour map only partially -> full loop
               for cmZ in ([cmX] if SHARED else permutations(COLS)):
                tZ=[tauZ[cmZ[k]] for k in range(3)]
                for P in range(t):
                    # legality: all 144 data qubits
                    good=True
                    for q in range(N):
                        ts=[]
                        if q<NG:
                            p=q
                            for i,mo in enumerate(Amon):
                                g=gadd(p,(-mo[0],-mo[1])); ts.append(tX[phiv(ph,g)][i]%t)
                            for i,mo in enumerate(Bmon):
                                g=gadd(p,mo);              ts.append((P+tZ[phiv(ph,g)][i])%t)
                        else:
                            p=q-NG
                            for i,mo in enumerate(Bmon):
                                g=gadd(p,(-mo[0],-mo[1])); ts.append(tX[phiv(ph,g)][3+i]%t)
                            for i,mo in enumerate(Amon):
                                g=gadd(p,mo);              ts.append((P+tZ[phiv(ph,g)][3+i])%t)
                        if len(set(ts))!=6: good=False; break
                    if not good: continue
                    # (MC)
                    for gx,gz,lst in OV:
                        (sx1,sz1),(sx2,sz2)=lst
                        d1=tX[phiv(ph,gx)][sx1]-(P+tZ[phiv(ph,gz)][sz1])
                        d2=tX[phiv(ph,gx)][sx2]-(P+tZ[phiv(ph,gz)][sz2])
                        if (d1//t)!=(d2//t): good=False; break
                    if good:
                        results.append(dict(phi=ph,upper=upper_is,t=t,P=P,
                            stX=stX,stZ=stZ,
                            tripX=tuple(tripX[cmX[k]] for k in range(3)),
                            tripZ=tuple(tripZ[cmZ[k]] for k in range(3)),
                            invX=invX,invZ=invZ))
    return results
if __name__=='__main__':
    rg = (sys.argv[1]=='geom') if len(sys.argv)>1 else False
    if len(sys.argv)>2 and sys.argv[2]=='indep':
        import builtins; globals()['SHARED']=False
    R=run(rg)
    print("restrict_geom=",rg,"  surviving readings:",len(R))
    from collections import Counter
    print("objects (tripX,tripZ):",Counter((r['tripX'],r['tripZ']) for r in R))
    print("phi values:",Counter(r['phi'] for r in R))
    print("straddle (stX,stZ):",Counter((r['stX'],r['stZ']) for r in R))
    print("periods:",Counter(r['t'] for r in R))
    pickle.dump(R,open('readings_%s.pkl'%('geom' if rg else 'free'),'wb'))
