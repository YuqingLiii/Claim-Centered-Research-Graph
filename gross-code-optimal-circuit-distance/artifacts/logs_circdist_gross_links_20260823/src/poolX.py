from gr import *
import pickle
def load(fn):
    out=[]
    for line in open(fn):
        a,b,c,d=[int(t,16) for t in line.split()]
        out.append((a|(b<<64)) | ((c|(d<<64))<<NG))
    return out
raw=load('w12X.txt')
bad=sum(1 for w in raw if popc(w)!=12 or any(popc(w&h)%2 for h in HZ))
print("raw",len(raw),"invalid",bad)
def trans(w,d):
    r=0
    for half in (0,NG):
        t=(w>>half)&((1<<NG)-1)
        while t:
            b=t&-t; p=b.bit_length()-1; t^=b; r|=1<<(half+gadd(p,d))
    return r
S=set()
for w in raw:
    for di in range(L):
        for dj in range(M): S.add(trans(w,(di,dj)))
RX,pivX=rref(HX)
nont=[w for w in S if not inspan(w,RX,pivX)]
print("distinct wt-12 in ker(HZ):",len(S)," NONTRIVIAL X-logicals:",len(nont))
pickle.dump(sorted(nont),open('poolX.pkl','wb'))
