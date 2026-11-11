"""Deterministic private-base construction used by round 64.

Vectors over F_2 are Python ints.  This is executable corroboration of the proof in
README.md, not the proof itself.
"""
from itertools import combinations, permutations, product

COPY = ((0,1,1),(0,2,2),(1,0,1),(1,1,0),(2,0,2))
NEGATE = ((0,0,0),(0,1,1),(1,1,0),(1,3,2),(2,0,2))

def parity(x): return bin(x).count("1") & 1
def wt(x): return bin(x).count("1")

def rref(rows, n):
    a=[x for x in rows if x]; rank=0; piv=[]
    for c in range(n):
        j=next((j for j in range(rank,len(a)) if (a[j]>>c)&1),None)
        if j is None: continue
        a[rank],a[j]=a[j],a[rank]
        x=a[rank]
        for j,y in enumerate(a):
            if j != rank and ((y>>c)&1): a[j]^=x
        piv.append(c); rank+=1
    return a[:rank],piv

def in_span(x, rb, piv):
    for r,p in zip(rb,piv):
        if (x>>p)&1: x ^= r
    return x == 0

def kernel_basis(rows,n):
    rb,piv=rref(rows,n); ps=set(piv); ans=[]
    for f in range(n):
        if f in ps: continue
        x=1<<f
        for r,p in zip(rb,piv):
            if (r>>f)&1: x |= 1<<p
        ans.append(x)
    return ans

def span(basis):
    a=[0]
    for x in basis: a += [y^x for y in a]
    return a

def rows_from_cols(cols,t):
    return [sum(1<<q for q,c in enumerate(cols) if (c>>i)&1) for i in range(t)]

class Builder:
    def __init__(self):
        self.P=0; self.B=0; self.cols=[]; self.cindex={}; self.rows=[]
        self.rowmeta=[]; self.planes=[]; self.registry={}; self.connkeys=set()
        self.gcount=0

    def fresh_point(self):
        u=1<<self.P; self.P+=1; return u

    def qubit(self,b,p):
        key=(b,p)
        if key not in self.cindex:
            self.cindex[key]=len(self.cols); self.cols.append(key)
        return self.cindex[key]

    def plane(self,u,v,labels,tag):
        assert u and v and u != v
        b=self.B; self.B+=1
        pts=(0,u,v,u^v)
        row=tuple(self.qubit(b,p) for p in pts)
        # formal qubit labels: 0, phi(u), phi(v), phi(u)+phi(v)
        qlabels=(0,labels[0],labels[1],labels[0]^labels[1])
        assert qlabels[3] == labels[2]
        i=len(self.planes)
        self.planes.append(dict(b=b,u=u,v=v,labels=labels,qlabels=qlabels,row=row,tag=tag))
        self.rows.append(row); self.rowmeta.append(("core",i))
        return i

    def pair(self,i,u):
        pl=self.planes[i]; b=pl['b']
        # The line contains u.  Using 0,u is canonical.
        assert u in (pl['u'],pl['v'],pl['u']^pl['v'])
        return (self.qubit(b,0),self.qubit(b,u))

    def label_at(self,i,u):
        pl=self.planes[i]
        return {pl['u']:pl['labels'][0],pl['v']:pl['labels'][1],pl['u']^pl['v']:pl['labels'][2]}[u]

    def connect(self,i,j,u,tag):
        if i>j: i,j=j,i
        key=(i,j,u)
        if key in self.connkeys: return
        self.connkeys.add(key)
        assert self.label_at(i,u) == self.label_at(j,u)
        a,aa=self.pair(i,u); b,bb=self.pair(j,u)
        row=(a,aa,b,bb)
        # Singleton order selects split {a,bb}, syndrome e_i+e_j+u.
        order=(a,bb,aa,b)
        self.rows.append(row); self.rowmeta.append(("connector",i,j,u,tag,order))

    def name(self,u,name,i):
        key=(u,name)
        if key in self.registry: self.connect(self.registry[key],i,u,("name",name))
        else: self.registry[key]=i

    def gadget(self,kind,u,v,tag):
        gi=self.gcount; self.gcount+=1
        h=1; g=1<<(gi+1)
        table=COPY if kind=="copy" else NEGATE
        def lab(x): return (0,h,g,h^g)[x]
        inds=[self.plane(u,v,tuple(lab(x) for x in triple),tag+(i,))
              for i,triple in enumerate(table)]
        for p,r in ((u,0),(v,1),(u^v,2)):
            groups={}
            for i,tr in enumerate(table): groups.setdefault(tr[r],[]).append(i)
            for value,members in groups.items():
                for a,b in zip(members,members[1:]): self.connect(inds[a],inds[b],p,(tag,r,value))
                if r<2 and value in (0,1): self.name(p,"0" if value==0 else "h",inds[members[0]])
        return inds

    def build_formula(self,nvars,clauses):
        # clauses contain (zero-based variable, positive_boolean).  Unused vars are harmless.
        pv=[self.fresh_point() for _ in range(nvars)]
        for t,cl in enumerate(clauses):
            q1=self.fresh_point(); q2=self.fresh_point(); qs=(q1,q2,q1^q2)
            ci=self.plane(q1,q2,(0,0,0),("clause",t))
            for r,((v,pos),q) in enumerate(zip(cl,qs)):
                # positive literal: q = not p; negative literal: q = p
                self.gadget("negate" if pos else "copy",pv[v],q,("literal",t,r))
                self.name(q,"0",ci)
        # H_Z columns: private base coordinate followed by point coordinates.
        syn=[(1<<(self.P+b))|p for b,p in self.cols]
        return Code(syn,self.rows,self.P+self.B,self)

class Code:
    def __init__(self,cols,rows,t,builder=None):
        self.cols=list(cols); self.rows=[tuple(r) for r in rows]; self.t=t; self.builder=builder
        self.n=len(cols); self.hx=[sum(1<<q for q in r) for r in rows]
        self.hz=rows_from_cols(cols,t)

    def quotient_basis(self): return rref(self.hx,self.n)
    def syndrome(self,v):
        z=0
        for q,c in enumerate(self.cols):
            if (v>>q)&1: z ^= c
        return z

    def cap(self):
        s=set(self.cols)
        return 0 not in s and len(s)==self.n and all((self.cols[i]^self.cols[j]) not in s for i,j in combinations(range(self.n),2))

    def css(self): return all(parity(x&z)==0 for x in self.hx for z in self.hz)

    def exact_distances(self):
        sx,pX=rref(self.hx,self.n); sz,pZ=rref(self.hz,self.n)
        kx=kernel_basis(self.hz,self.n); kz=kernel_basis(self.hx,self.n)
        dx=min(wt(v) for v in span(kx) if v and not in_span(v,sx,pX))
        dz=min(wt(v) for v in span(kz) if v and not in_span(v,sz,pZ))
        return dx,dz,len(kx)-len(sx)

def companion():
    X=[(0,1,2,3),(4,5,6,7),(1,4,8,10),(0,6,8,11),(3,7,9,10)]
    Z=[(1,2,4,7,9),(0,1,6,7,10),(0,1,2,3,8,9),(0,1,4,5,11),
       (0,2,4,6,8,11),(4,5,6,7,10,11),(8,9,10,11)]
    cols=[sum(1<<i for i,r in enumerate(Z) if q in r) for q in range(12)]
    return Code(cols,X,7)

def split_value(code,row,k):
    q0=row[0]; q=row[k+1]
    v=(1<<q0)|(1<<q)
    rb,piv=code.quotient_basis()
    for r,p in zip(rb,piv):
        if (v>>p)&1: v^=r
    return code.syndrome(v),v

def schedule_ok(code,choices):
    vals=[split_value(code,row,k) for row,k in zip(code.rows,choices)]
    return all(not (vals[i][0]==vals[j][0] and vals[i][1]!=vals[j][1])
               for i,j in combinations(range(len(vals)),2))

def find_companion_x_witness():
    c=companion()
    for ch in product(range(3),repeat=len(c.rows)):
        if schedule_ok(c,ch): return ch
    return None

def repetition3(code):
    n=code.n
    cols=[code.cols[q] for q in range(n) for _ in range(3)]
    rows=[]
    for r in code.rows: rows.append(tuple(3*q for q in r))
    for q in range(n): rows.extend(((3*q,3*q+1),(3*q,3*q+2)))
    return Code(cols,rows,code.t)

def prop5_counterexample():
    L=(1,2,3); V=(4,8,12); bases=(16,20,24,28)
    cols=[b^p for b in bases for p in (0,)+L]
    rows=[tuple(range(4*i,4*i+4)) for i in range(4)]
    rows += [(0,4,8,12),(1,5,9,13)]
    return Code(cols,rows,5)

def k4_no():
    # Four sections of one line forming a 2x2 rank-metric code: every pair differs
    # at every nonzero point.  Hence four domain-3 checks require four colours.
    b=Builder(); u=b.fresh_point(); v=b.fresh_point()
    labs=((0,0,0),(1,2,3),(2,3,1),(3,1,2))
    for i,x in enumerate(labs): b.plane(u,v,x,("k4",i))
    return b.build_formula(0,[])
