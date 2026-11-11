"""Verify cert4.cls subset cert5/6.cls subset cert7.cls, with identical variable numbering and
identical column-literal maps, on EVERY cell of both sectors.  This is what licenses mixing a
cert4 UNSAT and a cert7 UNSAT within one cell."""
from sched import make_phi
from cert import tiled_orders
import dext, dext2, cert4, cert5, cert6, cert7
phi=make_phi(1,1); CAND={'Z':(1,2,62),'X':(14,0,2)}
cells=cert4.cells(10)
bad=[]; n=0
for sec,trip in CAND.items():
    orders,_=tiled_orders(sec,phi,trip)
    ctx=dext.sector_ctx(orders,sec)[0]
    cols=[rep for rep,_ in dext2.column_orbits(phi,trip)[1]]
    for (K,Ew) in cells:
        n+=1
        c4=cert4.Cert4(ctx,10,K,Ew); c5=cert5.Cert5(ctx,10,K,Ew)
        c6=cert6.Cert6(ctx,10,K,Ew); c7=cert7.Cert7(ctx,10,K,Ew)
        S4={frozenset(c) for c in c4.cls}; S5={frozenset(c) for c in c5.cls}
        S6={frozenset(c) for c in c6.cls}; S7={frozenset(c) for c in c7.cls}
        checks = {
          'vars_equal':  c4.top==c6.top==c7.top,
          'c4<=c6':      S4<=S6,
          'c4<=c7':      S4<=S7,
          'c6<=c7':      S6<=S7,
          'c4<=c5':      S4<=S5,
          'col_lit_46':  all(c4.col_lit(r)==c6.col_lit(r) for r in cols),
          'col_lit_47':  all(c4.col_lit(r)==c7.col_lit(r) for r in cols),
        }
        if not all(checks.values()):
            bad.append((sec,K,Ew,{k:v for k,v in checks.items() if not v}))
import collections
cnt=collections.Counter()
for _,_,_,d in bad:
    for k in d: cnt[k]+=1
print(f"cells checked: {n} (55 per sector x 2)")
print(f"cells with >=1 failing check: {len(bad)}")
print("failing check breakdown:", dict(cnt))
core=['vars_equal','c4<=c6','c4<=c7','c6<=c7','col_lit_46','col_lit_47']
print()
print("CORE CHAIN (cert4 <= cert6 <= cert7, same vars, same col_lit):")
print("   failures:", sum(cnt[k] for k in core), " -> holds on all 110 cells:", sum(cnt[k] for k in core)==0)
print("SIDE BRANCH (cert5, the bench-only encoding):")
print("   c4<=c5 failures:", cnt['c4<=c5'])
