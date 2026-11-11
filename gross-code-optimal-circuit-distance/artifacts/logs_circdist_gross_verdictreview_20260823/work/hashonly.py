
"""Rebuild one sub-query's CNF and print its hash + shape. No solve.
usage: hashonly.py <sector> <a,b,c> <W> <K> <Ew> <orbit>"""
import sys, json, hashlib, time
from sched import make_phi
from cert import tiled_orders
import dext, dext2, cert7
sector=sys.argv[1]; triple=tuple(int(c) for c in sys.argv[2].split(','))
W=int(sys.argv[3]); K=int(sys.argv[4]); Ew=int(sys.argv[5]); oi=int(sys.argv[6])
t0=time.time()
phi=make_phi(1,1)
orders,_=tiled_orders(sector,phi,triple)
ctx,Hstab=dext.sector_ctx(orders,sector)
c=cert7.Cert7(ctx,W,K,Ew)
cls=list(c.cls)
rec=dict(sector=sector,triple=list(triple),W=W,K=K,Ew=Ew,orbit=oi,
         nclauses=len(cls),nvars=c.top)
if oi>=0:
    S,orbits=dext2.column_orbits(phi,triple)
    rorb=[(rep,orb) for (rep,orb) in orbits if rep[0]=='r']
    rec['norbits']=len(rorb); rec['stab']=len(S)
    rep,orb=rorb[oi]; rec['rep']=str(rep)
    cls.append([c.col_lit(rep)])
    for jj in range(oi):
        for col in rorb[jj][1]:
            cls.append([-c.col_lit(col)])
h=hashlib.sha256()
for cl in cls: h.update((" ".join(map(str,cl))+"\n").encode())
rec['cnf_sha256']=h.hexdigest()[:32]; rec['nclauses_final']=len(cls)
rec['build_s']=round(time.time()-t0,1)
print(json.dumps(rec))
