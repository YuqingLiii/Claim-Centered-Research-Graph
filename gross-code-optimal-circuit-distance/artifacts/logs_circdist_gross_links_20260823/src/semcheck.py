"""End-to-end semantic validation of the CNF encoding against the reviewer's exhaustive pool."""
import sys,os,pickle,time,json
sys.path.insert(0,os.path.abspath('gen')); sys.path.append(os.path.abspath('.'))
import numpy as np
from sched import make_phi
from cert import tiled_orders
import dext
import gr as mine
L,M=12,6; NG=72; N=144
def neg(q):
    h,p=(0,q) if q<NG else (NG,q-NG); i,j=divmod(p,M); return h+((-i)%L)*M+((-j)%M)
res={}
for sec,triple in (('Z',(1,2,62)),('X',(14,0,2))):
    orders,_=tiled_orders(sec,make_phi(1,1),triple)
    ctx,Hst=dext.sector_ctx(orders,sec)
    pool=set(pickle.load(open('poolZ.pkl' if sec=='Z' else 'poolX.pkl','rb')))
    out={}
    for W in (11,12):
        t0=time.time(); sat,wit,el,nc=dext.query(ctx,W,Hst,use_residuals=False)
        d=dict(W=W,verdict='SAT' if sat else 'UNSAT',seconds=round(el,1),nclauses=nc)
        if sat:
            E,R,D,info=wit
            m=0
            for q in range(N):
                if E[q]: m|=1<<neg(q)          # bring into my index space
            d['witness_weight']=info['weight']; d['in_my_exhaustive_1884_pool']=(m in pool)
            d['nres_used']=len(R)
        out[W]=d
        print(sec,d,flush=True)
    res[sec]=out
json.dump(res,open('semcheck.json','w'),indent=1)
