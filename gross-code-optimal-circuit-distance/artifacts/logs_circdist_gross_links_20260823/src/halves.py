from gr import *
# A,B as 72x72 over their own half.  Acol[p] = rows g with A[g][p]=1  => g = p - amon
def colmask(mons):
    out=[]
    for p in range(NG):
        v=0
        for mo in mons: v |= 1 << gadd(p,(-mo[0],-mo[1]))
        out.append(v)
    return out
Acol = colmask(Amon); Bcol = colmask(Bmon)
Arow = [sum(1<<p for p in range(NG) if (Acol[p]>>g)&1) for g in range(NG)]
Brow = [sum(1<<p for p in range(NG) if (Bcol[p]>>g)&1) for g in range(NG)]

def rref_n(rows, n):
    rows=list(rows); piv=[]; r=0
    for c in range(n-1,-1,-1):
        p=None
        for k in range(r,len(rows)):
            if rows[k]>>c&1: p=k;break
        if p is None: continue
        rows[r],rows[p]=rows[p],rows[r]
        for k in range(len(rows)):
            if k!=r and (rows[k]>>c&1): rows[k]^=rows[r]
        piv.append(c); r+=1
        if r==len(rows): break
    return rows[:r],piv
def null_n(rows,n):
    R,piv=rref_n(rows,n); free=[c for c in range(n) if c not in piv]; out=[]
    for f in free:
        v=1<<f
        for r,c in zip(R,piv):
            if (r>>f)&1: v|=1<<c
        out.append(v)
    return out
if __name__=="__main__":
    RA,pA=rref_n(Arow,NG); RB,pB=rref_n(Brow,NG)
    print("rank A",len(RA),"rank B",len(RB))
    kA=null_n(Arow,NG); kB=null_n(Brow,NG)
    print("nullity A",len(kA),"nullity B",len(kB))
    print("ker B weights", sorted(popc(z) for z in kB))
