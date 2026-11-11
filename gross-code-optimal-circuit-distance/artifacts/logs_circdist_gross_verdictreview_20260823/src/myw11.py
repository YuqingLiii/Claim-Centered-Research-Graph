#!/usr/bin/env python3
"""Reviewer-independent check of the d_ext <= 11 side: (i) that the project's H_X/H_Z really is the
gross code (compared against a from-scratch build), (ii) the 720-witness count per sector,
(iii) full F2 re-verification of a random sample of witnesses with reviewer-written algebra."""
import sys, os, json, random, collections
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', 'work'))

# ---------- (i) from-scratch build, compared with gross.py ----------
L, M = 12, 6; NQ = L*M; N = 2*NQ
def shift(a,b):
    P=np.zeros((NQ,NQ),np.uint8)
    for i in range(L):
        for j in range(M): P[i*M+j, ((i+a)%L)*M+((j+b)%M)]=1
    return P
def poly(ms): 
    S=np.zeros((NQ,NQ),np.uint8)
    for m in ms: S=(S+shift(*m))%2
    return S
A=poly([(3,0),(0,1),(0,2)]); B=poly([(0,3),(1,0),(2,0)])
myHX=np.concatenate([A,B],1); myHZ=np.concatenate([B.T,A.T],1)
import gross as G
sw=lambda H: np.concatenate([H[:,NQ:],H[:,:NQ]],1)
print("(i) from-scratch gross code vs project gross.py")
print("    project HX == my HZ with halves swapped :", bool((G.HX==sw(myHZ)).all()))
print("    project HZ == my HX with halves swapped :", bool((G.HZ==sw(myHX)).all()))
print("    (a relabelling of the shift convention + the X<->Z naming; same code)")

def rref(Mat):
    Mt=Mat.copy()%2; r=0; piv=[]
    for c in range(Mt.shape[1]):
        p=next((i for i in range(r,Mt.shape[0]) if Mt[i,c]), None)
        if p is None: continue
        Mt[[r,p]]=Mt[[p,r]]
        for i in range(Mt.shape[0]):
            if i!=r and Mt[i,c]: Mt[i]^=Mt[r]
        piv.append(c); r+=1
    return Mt[:r],piv
def inspan(R,piv,v):
    v=v.copy()%2
    for i,c in enumerate(piv):
        if v[c]: v^=R[i]
    return not v.any()

RX,pX=rref(G.HX); RZ,pZ=rref(G.HZ)
print("    rank HX=%d rank HZ=%d  k=%d ; HX HZ^T = 0 : %s"
      % (len(RX),len(RZ),N-len(RX)-len(RZ), bool(((<email-redacted>.T)%2==0).all())))
ones=np.ones(N,np.uint8)
print("(ii) all-ones in rowspace(HX)=%s rowspace(HZ)=%s  => zero-syndrome => EVEN weight"
      % (inspan(RX,pX,ones), inspan(RZ,pZ,ones)))

# ---------- residual sets and wmax ----------
from sched import make_phi
from cert import tiled_orders
import dext, pool as poolmod
CAND={'Z':(1,2,62),'X':(14,0,2)}
phi=make_phi(1,1)
PZ,PX,LX,LZ=poolmod.get()
print()
rng=random.Random(20260823)
for sector in ('Z','X'):
    orders,_=tiled_orders(sector,phi,CAND[sector])
    ctx,Hstab=dext.sector_ctx(orders,sector)
    Hdet = G.HX if sector=='Z' else G.HZ
    Rd,pd = (RX,pX) if sector=='Z' else (RZ,pZ)
    Rs,ps = rref(Hstab)
    P = PZ if sector=='Z' else PX
    hist=collections.Counter(len(ctx.res[c][k]) for c in range(G.NG) for k in range(3))
    print("[%s] residual-set weight histogram over %d checks x 3: %s  -> wmax = %d"
          % (sector, G.NG, dict(sorted(hist.items())), max(hist)))
    print("     pool: %d words, all weight 12: %s, all even: %s"
          % (len(P), bool(all(int(v.sum())==12 for v in P)),
             bool(all(int(v.sum())%2==0 for v in P))))
    hits=[(Li,c,k) for Li,Lv in enumerate(P) for c in range(G.NG) for k in (0,1,2)
          if len(ctx.res[c][k])==2 and all(Lv[q] for q in ctx.res[c][k])]
    print("     weight-11 witnesses (L, check, k) with |r|=2 and r subset of L : %d"
          % len(hits))
    print("     distinct logicals: %d ; distinct checks: %d ; k values used: %s"
          % (len({h[0] for h in hits}), len({h[1] for h in hits}),
             sorted({h[2] for h in hits})))
    # full independent F2 verification of a random sample
    samp=rng.sample(hits, 25)
    ok=0; details=[]
    for (Li,c,k) in samp:
        Lv=P[Li]; r=sorted(ctx.res[c][k])
        E=Lv.copy()
        d=E.copy()
        for q in r: d[q]^=1
        c1 = int(E.sum())==12
        c2 = not ((Hdet@E)%2).any()            # zero syndrome, MY rref-free product
        c3 = not inspan(Rs,ps,E)               # non-stabiliser
        c4 = int(d.sum())+1 == 11              # |d| + |R| = 11
        chk = np.zeros(N,np.uint8)
        for q in r: chk[q]=1
        c5 = bool((((d+chk)%2)==E).all())      # E = d xor rho_R
        if c1 and c2 and c3 and c4 and c5: ok+=1
        else: details.append((Li,c,k,c1,c2,c3,c4,c5))
    print("     INDEPENDENT F2 re-verification of %d random witnesses: %d/%d PASS  %s"
          % (len(samp), ok, len(samp), details[:3]))
