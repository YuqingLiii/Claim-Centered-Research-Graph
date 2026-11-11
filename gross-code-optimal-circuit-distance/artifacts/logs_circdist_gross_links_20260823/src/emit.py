from halves import *
import json
def leftinv(cols):
    """cols: list of 72 column masks (over 72 rows). Return (pivcols, colsol[72]) with
       B * (XOR_{g in supp(s)} colsol[g]) == s  for all s in colspace."""
    # column-reduce: find pivot columns
    rows_aug = []           # we row-reduce M^T? easier: build matrix with rows = e_g augmented
    # Build M as 72 rows (one per output coord g) x 72 cols (input p): M[g][p] = (cols[p]>>g)&1
    Mrows = [sum(((cols[p]>>g)&1)<<p for p in range(NG)) for g in range(NG)]
    # find independent set of columns p (pivot columns) by Gaussian elimination on columns
    basis=[]; piv=[]
    red=[]
    for p in range(NG):
        v=cols[p]; comb = 1<<p
        for (bv,bc,bp) in red:
            if (v>>bp)&1: v^=bv; comb^=bc
        if v:
            lead = v.bit_length()-1
            red.append((v,comb,lead)); piv.append(p); basis.append((v,comb,lead))
    # now for target s: reduce s through red, tracking combination
    colsol=[]
    for g in range(NG):
        s = 1<<g; comb=0
        for (bv,bc,bp) in red:
            if (s>>bp)&1: s^=bv; comb^=bc
        colsol.append(comb)      # note: valid only modulo im; verified below
    return piv, colsol

def leftnull(cols):
    """basis of {w : w^T M = 0} i.e. rows of the left null space (12-dim)."""
    Mrows=[sum(((cols[p]>>g)&1)<<p for p in range(NG)) for g in range(NG)]
    # nullspace of M^T acting on w in F2^72:  sum_g w_g * Mrows[g] = 0
    # treat as: find w with XOR_{g in w} Mrows[g] == 0
    red=[]; out=[]
    for g in range(NG):
        v=Mrows[g]; comb=1<<g
        for (bv,bc,bp) in red:
            if (v>>bp)&1: v^=bv; comb^=bc
        if v: red.append((v,comb,v.bit_length()-1))
        else: out.append(comb)
    return out

pivA, solA = leftinv(Acol)
pivB, solB = leftinv(Bcol)
lnA = leftnull(Acol); lnB = leftnull(Bcol)
kerA = null_n(Arow,NG); kerB = null_n(Brow,NG)
def apply(cols, u):
    r=0; t=u
    while t:
        b=t & -t; p=b.bit_length()-1; r ^= cols[p]; t^=b
    return r
# verify right inverses
import random
for cols,sol,lname in ((Acol,solA,'A'),(Bcol,solB,'B')):
    ok=True
    for _ in range(200):
        w=random.getrandbits(NG); s=apply(cols,w)
        v0=0; t=s
        while t:
            b=t&-t; g=b.bit_length()-1; v0^=sol[g]; t^=b
        if apply(cols,v0)!=s: ok=False;break
    print("right-inverse",lname,"OK" if ok else "FAIL")
for name,ln,cols in (('A',lnA,Acol),('B',lnB,Bcol)):
    bad=sum(1 for w in ln for p in range(NG) if popc(w & cols[p])%2)
    print("leftnull",name,"dim",len(ln),"orthogonality failures",bad)
json.dump(dict(Acol=Acol,Bcol=Bcol,solA=solA,solB=solB,lnA=lnA,lnB=lnB,
               kerA=kerA,kerB=kerB,HX=HX,HZ=HZ),open('code.json','w'))
print("wrote code.json")
