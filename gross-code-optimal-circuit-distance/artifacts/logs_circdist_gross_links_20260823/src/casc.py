"""Reviewer's own reconstruction of [SBB26] Prop.6's 90 -> 45 -> 4 cascade."""
from gr import *
from itertools import permutations
import pickle, sys

# ---- slot -> qubit maps (phicert convention, re-derived from H_X/H_Z above) --
def zslots(g):   # Z-check g: slots 0,1,2 = LEFT (B monomials), 3,4,5 = RIGHT (A monomials)
    return [gadd(g,(-m[0],-m[1])) for m in Bmon] + [NG+gadd(g,(-m[0],-m[1])) for m in Amon]
def xslots(g):   # X-check g: slots 0,1,2 = LEFT (A monomials), 3,4,5 = RIGHT (B monomials)
    return [gadd(g,m) for m in Amon] + [NG+gadd(g,m) for m in Bmon]

# ---- the 90 residual classes ------------------------------------------------
def resid(p):
    r1=frozenset(p[0:2]); r2=frozenset(p[3:6]); r3=frozenset(p[4:6])
    r2c=frozenset(p[0:3])
    return (r1, min(r2,r2c,key=lambda s:sorted(s)), r3, r2)   # r2 canonical + raw
CLASSES=[]; seen={}
for p in permutations(range(6)):
    r1,r2c,r3,r2=resid(p)
    key=(r1,r2c,r3) if sorted(r1)<sorted(r3) else (r3,r2c,r1)
    # reversal maps (r1,r2,r3)->(r3, complement(r2), r1); complement(r2) has same column
    if key not in seen:
        seen[key]=len(CLASSES); CLASSES.append((p,r1,r2,r3))
print("number of residual classes:",len(CLASSES))
for want,idx in ((0,(0,1,2,3,4,5)),(1,(0,1,2,4,3,5)),(2,(0,1,2,5,3,4)),
                 (14,(0,2,1,5,3,4)),(62,(1,2,0,5,3,4))):
    print("  class %-3d canonical order in my numbering: %s   (phicert says %s)"
          %(want, CLASSES[want][0], idx), "MATCH" if CLASSES[want][0]==idx else "DIFFER")

# ---- pools ------------------------------------------------------------------
poolZ=pickle.load(open('poolZ.pkl','rb'))   # nontrivial wt-12 in ker(HX)  (Z sector)
poolX=pickle.load(open('poolX.pkl','rb'))   # nontrivial wt-12 in ker(HZ)  (X sector)

def build(sector):
    slots = zslots if sector=='Z' else xslots
    pool  = poolZ  if sector=='Z' else poolX
    # index: for every 2-subset / 3-subset mask, which logicals contain it
    from collections import defaultdict
    sub2=defaultdict(list); sub3=defaultdict(list)
    for li,Lm in enumerate(pool):
        qs=[]; t=Lm
        while t:
            b=t&-t; qs.append(b.bit_length()-1); t^=b
        for i in range(12):
            for j in range(i+1,12):
                sub2[(qs[i],qs[j])].append(li)
                for k in range(j+1,12): sub3[(qs[i],qs[j],qs[k])].append(li)
    return slots,pool,sub2,sub3

def isolated_elim(sector,ci,slots,sub2,sub3):
    """d_ext <= 10 witness on ONE check (check 0), residual class ci."""
    p,r1,r2,r3=CLASSES[ci]; S=slots(0)
    t3=tuple(sorted(S[s] for s in r2))
    if sub3.get(t3): return 'r2-covered'
    a=tuple(sorted(S[s] for s in r1)); b=tuple(sorted(S[s] for s in r3))
    inter=set(sub2.get(a,[])) & set(sub2.get(b,[]))
    if inter: return 'r1+r3-covered'
    return None

def tiled_elim(sector,ci,colour,phi,slots,sub2):
    """two disjoint weight-2 residuals on same-colour checks inside one wt-12 logical"""
    p,r1,r2,r3=CLASSES[ci]
    masks=[]
    for g in range(NG):
        i,j=divmod(g,M)
        if (phi[0]*i+phi[1]*j)%3!=colour: continue
        S=slots(g)
        for rr in (r1,r3):
            m=0
            for s in rr: m|=1<<S[s]
            masks.append((m,tuple(sorted(S[s] for s in rr))))
    sets=[set(sub2.get(k,[])) for _,k in masks]
    n=len(masks)
    for i in range(n):
        if not sets[i]: continue
        for j in range(i+1,n):
            if masks[i][0]&masks[j][0]: continue
            if sets[i]&sets[j]: return True
    return False

for sector in ('Z','X'):
    slots,pool,sub2,sub3=build(sector)
    surv45=[ci for ci in range(90) if isolated_elim(sector,ci,slots,sub2,sub3) is None]
    print("=== sector %s: 90 -> %d after the single-check filter"%(sector,len(surv45)))
    for phi in ((1,1),(1,2),(2,1),(2,2)):
        per=[]
        for colour in (0,1,2):
            s=[ci for ci in surv45 if not tiled_elim(sector,ci,colour,phi,slots,sub2)]
            per.append(s)
        same = per[0]==per[1]==per[2]
        print("   phi=%da+%db : 45 -> %d per colour  %s   (identical for all three colours: %s)"
              %(phi[0],phi[1],len(per[0]),per[0],same))
