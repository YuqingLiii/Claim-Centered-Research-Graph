from halves import *
from emit import leftinv, leftnull
import json
# X sector: ker(H_Z) with H_Z = [B^T | A^T]; Pcol[p]={p+b}, Qcol[p]={p+a}
Pcol=[sum(1<<gadd(p,mo) for mo in Bmon) for p in range(NG)]
Qcol=[sum(1<<gadd(p,mo) for mo in Amon) for p in range(NG)]
Prow=[sum(1<<p for p in range(NG) if (Pcol[p]>>g)&1) for g in range(NG)]
Qrow=[sum(1<<p for p in range(NG) if (Qcol[p]>>g)&1) for g in range(NG)]
pivP,solP=leftinv(Pcol); pivQ,solQ=leftinv(Qcol)
lnP=leftnull(Pcol); lnQ=leftnull(Qcol)
kerP=null_n(Prow,NG); kerQ=null_n(Qrow,NG)
print("rank P",len(rref_n(Prow,NG)[0]),"rank Q",len(rref_n(Qrow,NG)[0]),
      "nullities",len(kerP),len(kerQ))
def w(f,arr):
    for v in arr: f.write("%x %x\n"%(v & ((1<<64)-1), v>>64))
with open('codeX.txt','w') as f:
    for arr in (Pcol,Qcol,solP,solQ,kerP,kerQ,lnP,lnQ): w(f,arr)
print("wrote codeX.txt")
