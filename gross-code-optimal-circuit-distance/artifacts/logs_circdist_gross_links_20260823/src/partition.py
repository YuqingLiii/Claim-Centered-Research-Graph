"""Does the reconstructed candidate admit the global X/Z instance partition that
[SBB26] Corollary 1's proof assumes ('partition each round of SEC into X and Z parts')?"""
import pickle
from gr import *
from geom import LAB
from filt import COLS, phiv
R=pickle.load(open('readings_geom.pkl','rb'))
cands=[r for r in R if r['t']==6 and r['tripX']==(14,0,2)]
print("readings at 6 CNOT layers (= depth 8 by SBB Eq.(6)) with X-triple (14,0,2):",len(cands))
import itertools
def times(r):
    """rebuild tau tables for this reading"""
    ph=r['phi']; t=r['t']
    invX=r['invX']; invZ=r['invZ']
    upper=r['upper']
    panelX='upper' if upper=='X' else 'lower'
    panelZ='lower' if upper=='X' else 'upper'
    from geom import blocks
    def tau(panel,inv,st):
        out={}
        for c in COLS:
            lab=LAB[panel][c]; b1=set(blocks(panel,c)[0])
            out[c]=[lab[inv[s]]+(t if (st and inv[s] in b1) else 0) for s in range(6)]
        return out
    return tau(panelX,invX,r['stX']), tau(panelZ,invZ,r['stZ']), ph, t
ok_all=True
for r in cands[:3]:
    tauX,tauZ,ph,t=times(r)
    # recover the colour map from the recorded triples is not stored; re-derive by matching
    from filt import CLS
    def cls_of(tab,c,st):
        order=sorted(range(6),key=lambda s: tab[c][s])
        return None
    # instead: use each colour-map and keep those reproducing the recorded triples
    from itertools import permutations
    from filt import CANON
    def trip(tab,cm):
        out=[]
        for k in range(3):
            c=cm[k]; order=tuple(sorted(range(6),key=lambda s: tab[c][s]))
            # class index
            for ci,p in enumerate(CANON):
                pass
            out.append(order)
        return out
    from filt import CLS as CLSMAP
    good=None
    for cm in permutations(COLS):
        tX=[tuple(sorted(range(6),key=lambda s: tauX[cm[k]][s])) for k in range(3)]
        tZ=[tuple(sorted(range(6),key=lambda s: tauZ[cm[k]][s])) for k in range(3)]
        if tuple(CLSMAP[o] for o in tX)==r['tripX'] and tuple(CLSMAP[o] for o in tZ)==r['tripZ']:
            good=cm; break
    assert good
    TX=[tauX[good[k]] for k in range(3)]; TZ=[tauZ[good[k]] for k in range(3)]
    P=r['P']
    bad=0; dirs=set()
    for q in range(N):
        a=[];b=[]
        if q<NG:
            for i,mo in enumerate(Amon): a.append(TX[phiv(ph,gadd(q,(-mo[0],-mo[1])))][i])
            for i,mo in enumerate(Bmon): b.append(P+TZ[phiv(ph,gadd(q,mo))][i])
        else:
            p=q-NG
            for i,mo in enumerate(Bmon): a.append(TX[phiv(ph,gadd(p,(-mo[0],-mo[1])))][3+i])
            for i,mo in enumerate(Amon): b.append(P+TZ[phiv(ph,gadd(p,mo))][3+i])
        # Z-instance k before X-instance k before Z-instance k+1  (or the mirror)
        f1 = max(b)<min(a) and max(a)<min(b)+t
        f2 = max(a)<min(b) and max(b)<min(a)+t
        if f1: dirs.add('Z<X')
        if f2: dirs.add('X<Z')
        if not (f1 or f2): bad+=1
    print("  reading phi=%s upper=%s st=(%d,%d): qubits without a consistent instance order: %d ; directions seen: %s"
          %(ph,r['upper'],r['stX'],r['stZ'],bad,sorted(dirs)))
    ok_all &= (bad==0 and len(dirs)==1)
print("GLOBAL X/Z INSTANCE PARTITION EXISTS (order-preserving re-timing):", ok_all)
