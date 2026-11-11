from gr import *
import sys
def load(fn):
    out=[]
    for line in open(fn):
        a,b,c,d=[int(t,16) for t in line.split()]
        u=a|(b<<64); v=c|(d<<64)
        out.append(u | (v<<NG))
    return out
raw=load('w12.txt')
print("raw",len(raw))
# validate
bad=0
for w in raw:
    if popc(w)!=12: bad+=1; continue
    if any(popc(w & h)%2 for h in HX): bad+=1
print("invalid raw:",bad)
# translations
def trans(w,d):
    r=0
    for half in (0,NG):
        t=(w>>half) & ((1<<NG)-1)
        while t:
            b=t&-t; p=b.bit_length()-1; t^=b
            r |= 1 << (half + gadd(p,d))
    return r
S=set()
for w in raw:
    for di in range(L):
        for dj in range(M):
            S.add(trans(w,(di,dj)))
print("distinct weight-12 in ker(HX):",len(S))
RZ,pivZ = rref(HZ)
triv=[w for w in S if inspan(w,RZ,pivZ)]
nont=[w for w in S if not inspan(w,RZ,pivZ)]
print("trivial (in rowspace HZ):",len(triv)," NONTRIVIAL logicals:",len(nont))
import pickle; pickle.dump(sorted(nont),open('poolZ.pkl','wb'))
