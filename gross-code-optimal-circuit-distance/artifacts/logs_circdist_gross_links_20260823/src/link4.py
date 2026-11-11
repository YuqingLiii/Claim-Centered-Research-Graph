"""LINK 4: extended-code encoding fidelity.  Independent rebuild vs the artifact generator."""
import sys, os, json, random
sys.path.insert(0,os.path.abspath('gen'))
import numpy as np
from gross import HX as tHX, HZ as tHZ, NG as tNG, N as tN, gidx as tgidx, Reducer
from sched import make_phi
from cert import tiled_orders
import dext
sys.path.insert(0,os.path.abspath('.'))
import gr as mine
from filt import CANON              # my class -> canonical permutation

L,M=12,6; NG=72; N=144
def neg(q):
    h,p=(0,q) if q<NG else (NG,q-NG); i,j=divmod(p,M); return h+((-i)%L)*M+((-j)%M)
def myslots(sector,g):
    if sector=='X':
        return [mine.gadd(g,m) for m in mine.Amon]+[NG+mine.gadd(g,m) for m in mine.Bmon]
    return [mine.gadd(g,(-m[0],-m[1])) for m in mine.Bmon]+[NG+mine.gadd(g,(-m[0],-m[1])) for m in mine.Amon]
def myphi(g):  # phi = 2a+2b   (mirror of the artifact's 1a+1b under g -> -g)
    i,j=divmod(g,M); return (2*i+2*j)%3
def my_res(sector,triple):
    out={}
    for g in range(NG):
        cl=triple[myphi(g)]; S=myslots(sector,g); o=[S[k] for k in CANON[cl]]
        out[g]=[tuple(o[p] for p in pos) for pos in ((0,1),(3,4,5),(4,5))]
    return out

report={}
for sector,triple in (('Z',(1,2,62)),('X',(14,0,2))):
    orders,Hstab = tiled_orders(sector, make_phi(1,1), triple)
    ctx,Hst = dext.sector_ctx(orders,sector)
    theirs = {g:[tuple(sorted(t)) for t in ctx.res[g]] for g in range(tNG)}
    mineres= my_res(sector,triple)
    # translate mine into their indexing:  my check g  <->  their check -g ; qubit q <-> -q
    trans = {}
    for g in range(NG):
        tg = neg(g) if g<NG else None
        trans[tg]=[tuple(sorted(neg(q) for q in t)) for t in mineres[g]]
    ok = all(sorted(theirs[g])==sorted(trans[g]) for g in range(NG))
    exact_same_slot_order = all(theirs[g]==trans[g] for g in range(NG))
    # column-level comparison of H_ext / L_ext
    Hdet = ctx.Hdet; Lrows = ctx.Lrows
    myH = mine.HX if sector=='Z' else mine.HZ
    hdet_ok = all( (set(np.nonzero(Hdet[e])[0].tolist()) ==
                    {neg(q) for q in range(N) if (myH[neg(e)]>>q)&1}) for e in range(tNG))
    # residual columns (216 of them) as F2^72 vectors
    def colset(res, H):
        S=set()
        for g in range(NG):
            for k in range(3):
                v=0
                for q in res[g][k]: v^= H[q]
                S.add(v)
        return S
    Hcols_theirs=[int(''.join(str(int(b)) for b in Hdet[:,q][::-1]),2) for q in range(tN)]
    Hcols_mine  =[sum(((myH[e]>>q)&1)<<e for e in range(NG)) for q in range(N)]
    ct=colset(theirs,Hcols_theirs)
    cm=colset({neg(g) if g<NG else g:[tuple(neg(q) for q in t) for t in mineres[g]] for g in range(NG)},
              [Hcols_mine[neg(q)] for q in range(N)])
    ncols = 144 + sum(1 for g in range(NG) for k in range(3))
    report[sector]=dict(residual_sets_match=ok, slot_orders_identical=exact_same_slot_order,
                        Hdet_match=hdet_ok, n_ext_columns=ncols,
                        n_distinct_residual_columns_theirs=len(ct),
                        n_distinct_residual_columns_mine=len(cm),
                        residual_column_sets_equal=(ct==cm),
                        Lrows_shape=list(Lrows.shape))
print(json.dumps(report,indent=1))
