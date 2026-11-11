#!/usr/bin/env python3
"""Exact Q(sqrt(5),i) structural representation model for H4.
Python 3.9+. Dependencies: numpy, sympy.

Field coefficient convention: (a,b,c,d) = a+b*sqrt(5)+i(c+d*sqrt(5)).
Each representation stores a common positive integer denominator separately.
"""
import itertools,collections,math,importlib.util,numpy as np,sympy as sp
P=24001

def add(x,y): return tuple(int(x[i])+int(y[i]) for i in range(4))
def neg(x): return tuple(-int(t) for t in x)
def scl(x,n): return tuple(int(n)*int(t) for t in x)
def mul(x,y):
 a,b,c,d=map(int,x);e,f,g,h=map(int,y)
 return (a*e+5*b*f-c*g-5*d*h,a*f+b*e-c*h-d*g,a*g+5*b*h+c*e+5*d*f,a*h+b*g+c*f+d*e)
def pw(x,n):
 r=(1,0,0,0); b=x
 while n:
  if n&1:r=mul(r,b)
  b=mul(b,b);n//=2
 return r

def q5mul(x,y):return (x[0]*y[0]+5*x[1]*y[1],x[0]*y[1]+x[1]*y[0])
def parity(p):return sum(p[i]>p[j] for i in range(len(p)) for j in range(i+1,len(p)))&1

def exact_2I():
 V=[]
 for i in range(4):
  for sg in (-1,1):
   q=[(0,0)]*4;q[i]=(4*sg,0);V.append(tuple(q))
 for ss in itertools.product((-1,1),repeat=4):V.append(tuple((2*s,0) for s in ss))
 base=((0,0),(2,0),(1,1),(-1,1))
 for p in itertools.permutations(range(4)):
  if parity(p):continue
  arr=[base[p[i]] for i in range(4)];nz=[i for i,x in enumerate(arr) if x!=(0,0)]
  for ss in itertools.product((-1,1),repeat=3):
   q=list(arr)
   for i,s in zip(nz,ss):q[i]=(s*q[i][0],s*q[i][1])
   V.append(tuple(q))
 V=list(dict.fromkeys(V)); assert len(V)==120
 lk={q:i for i,q in enumerate(V)}
 def qm(q,r):
  w,x,y,z=q;W,X,Y,Z=r
  A=lambda u,v:(u[0]+v[0],u[1]+v[1]);S=lambda u,v:(u[0]-v[0],u[1]-v[1]);M=q5mul
  o=[S(S(S(M(w,W),M(x,X)),M(y,Y)),M(z,Z)), A(A(M(w,X),M(x,W)),S(M(y,Z),M(z,Y))), A(S(A(M(w,Y),M(y,W)),M(x,Z)),M(z,X)), A(A(S(M(w,Z),M(y,X)),M(z,W)),M(x,Y))]
  assert all(a%4==0 and b%4==0 for a,b in o);return tuple((a//4,b//4) for a,b in o)
 mt=np.empty((120,120),np.int16)
 for i in range(120):
  for j in range(120):mt[i,j]=lk[qm(V[i],V[j])]
 eid=lk[((4,0),(0,0),(0,0),(0,0))]
 return V,mt,eid

def qmat(q):
 w,x,y,z=q
 R=lambda t:(t[0],t[1],0,0); I=lambda t:(0,0,t[0],t[1])
 M=[[add(R(w),I(x)),add(R(y),I(z))],[add(neg(R(y)),I(z)),add(R(w),neg(I(x)))]]
 A=np.empty((2,2,4),dtype=object)
 for i in range(2):
  for j in range(2):A[i,j,:]=M[i][j]
 return A

def kron(A,B):
 m,n,_=A.shape;p,q,_=B.shape;O=np.empty((m*p,n*q,4),dtype=object)
 for i in range(m):
  for j in range(n):
   for k in range(p):
    for l in range(q):O[i*p+k,j*q+l,:]=mul(A[i,j],B[k,l])
 return O

def sympow(U,n):
 if n==0:
  O=np.zeros((1,1,4),dtype=object);O[0,0,0]=1;return O,1,[1]
 a,b,c,d=[tuple(U[i,j,:]) for i,j in [(0,0),(0,1),(1,0),(1,1)]]
 O=np.empty((n+1,n+1,4),dtype=object)
 pa=[pw(a,k) for k in range(n+1)];pb=[pw(b,k) for k in range(n+1)];pc=[pw(c,k) for k in range(n+1)];pd=[pw(d,k) for k in range(n+1)]
 for ell in range(n+1):
  for k in range(n+1):
   z=(0,0,0,0)
   for r in range(max(0,k-(n-ell)),min(k,ell)+1):
    co=math.comb(ell,r)*math.comb(n-ell,k-r)
    term=mul(mul(pa[n-ell-k+r],pb[k-r]),mul(pc[ell-r],pd[r]));z=add(z,scl(term,co))
   O[ell,k,:]=z
 return O,4**n,[math.comb(n,k) for k in range(n+1)]

def order(mt,e,a):
 x=e
 for k in range(1,121):
  x=int(mt[x,a])
  if x==e:return k

def gen(mt,e,gs):
 S={e};q=collections.deque([e])
 while q:
  x=q.popleft()
  for g in gs:
   y=int(mt[x,g])
   if y not in S:S.add(y);q.append(y)
 return S

def iso(mtA,eA,gA,mtB,eB,gB):
 mp={eA:eB};rv={eB:eA};q=collections.deque([eA])
 while q:
  x=q.popleft();y=mp[x]
  for a,b in zip(gA,gB):
   xx=int(mtA[x,a]);yy=int(mtB[y,b])
   if xx in mp:
    if mp[xx]!=yy:return
   else:
    if yy in rv:return
    mp[xx]=yy;rv[yy]=xx;q.append(xx)
 if len(mp)!=len(mtA):return
 return mp

def cmod(z,s,i):return (z[0]+z[1]*s+i*(z[2]+z[3]*s))%P
def char(M,D,s,i):return sum(cmod(M[j,j,:],s,i) for j in range(M.shape[0]))*pow(D,P-2,P)%P

def build_exact_Q_irreps(Q,Qd):
 V,mt,e=exact_2I();oq=[order(Q['mul'],Q['I'],i) for i in range(120)];ov=[order(mt,e,i) for i in range(120)]
 qp=next((a,b) for a in range(120) if oq[a]==4 for b in range(120) if oq[b]==6 and order(Q['mul'],Q['I'],int(Q['mul'][a,b]))==10 and len(gen(Q['mul'],Q['I'],[a,b]))==120)
 mp=vp=None
 for a in range(120):
  if ov[a]!=4:continue
  for b in range(120):
   if ov[b]!=6 or order(mt,e,int(mt[a,b]))!=10:continue
   z=iso(Q['mul'],Q['I'],qp,mt,e,(a,b))
   if z is not None:mp=z;vp=(a,b);break
  if mp:break
 fund=[qmat(V[mp[i]]) for i in range(120)]
 sr=sorted(map(int,sp.sqrt_mod(5,P,all_roots=True)))[0];ir=sorted(map(int,sp.sqrt_mod(-1,P,all_roots=True)))[0]
 fch=[char(fund[g],4,sr,ir) for g in range(120)]
 tw=[i for i,r in enumerate(Qd['irreps']) if r['degree']==2]; fid=[i for i in tw if all(int(Qd['irreps'][i]['character'][g])%P==fch[g] for g in range(120))]
 fid=fid[0];oid=[x for x in tw if x!=fid][0]
 auto=None
 for a in range(120):
  if oq[a]!=4:continue
  for b in range(120):
   if oq[b]!=6 or order(Q['mul'],Q['I'],int(Q['mul'][a,b]))!=10:continue
   z=iso(Q['mul'],Q['I'],qp,Q['mul'],Q['I'],(a,b))
   if z and all(fch[z[g]]==int(Qd['irreps'][oid]['character'][g])%P for g in range(120)):auto=z;break
  if auto:break
 fg=[fund[auto[i]] for i in range(120)]
 reps=[None]*9
 def install(mats,D,metric):
  ch=[char(mats[g],D,sr,ir) for g in range(120)];hits=[i for i,r in enumerate(Qd['irreps']) if r['degree']==mats[0].shape[0] and all(int(r['character'][g])%P==ch[g] for g in range(120))]
  assert len(hits)==1,(mats[0].shape,hits);i=hits[0]
  if reps[i] is None:reps[i]=(mats,D,metric)
 for base in (fund,fg):
  for n in range(6):
   L=[]
   for g in range(120):M,D,met=sympow(base[g],n);L.append(M)
   install(L,D,met)
 L=[kron(fund[g],fg[g]) for g in range(120)];install(L,16,[1]*4)
 return reps,{'sqrt5_root_mod_p':sr,'i_root_mod_p':ir,'structural_Q_pair':list(qp),'quaternion_pair':list(vp),'fundamental_Qdata_id':fid,'galois_Qdata_id':oid}

def blockdiag(A,B):
 m,n,_=A.shape;p,q,_=B.shape;O=np.zeros((m+p,n+q,4),dtype=object);O[:m,:n,:]=A;O[m:,n:,:]=B;return O

def flipmap(du,dv):
 r=du*dv; F=np.empty(r,dtype=np.int32)
 for i in range(du):
  for j in range(dv):F[i*dv+j]=j*du+i
 return F

def rightperm(M,src_for_col,sg=1):
 O=np.empty_like(M)
 for c,src in enumerate(src_for_col):
  O[:,c,:]=M[:,int(src),:]
  if sg==-1:O[:,c,:]=-O[:,c,:]
 return O

def h_elem(meta,reps,G,gi):
 pid,e=G['elements'][gi];a,b=G['pairs'][pid]
 if meta['type']=='diagonal_extension':
  U,D,met=reps[int(meta['i'])];M=kron(U[a],U[b]);du=U[0].shape[0]
  if e:
   F=flipmap(du,du);M=rightperm(M,F,int(meta['extension_sign']))
  return M,D*D,[x*y for x in met for y in met]
 U,DU,mU=reps[int(meta['i'])];V,DV,mV=reps[int(meta['j'])];du=U[0].shape[0];dv=V[0].shape[0];r=du*dv
 A=kron(U[a],V[b]);B=kron(V[a],U[b]);M=blockdiag(A,B)
 if e:
  F=flipmap(du,dv);inv=np.empty(r,dtype=np.int32)
  for src,dst in enumerate(F):inv[dst]=src
  src=np.empty(2*r,dtype=np.int32)
  for c in range(r):src[c]=r+F[c];src[r+c]=inv[c]
  M=rightperm(M,src,1)
 return M,DU*DV,[x*y for x in mU for y in mV]+[x*y for x in mV for y in mU]

def mat_mod(M,D,sr,ir):
 d=M.shape[0];O=np.empty((d,d),dtype=np.int64);iv=pow(D,P-2,P)
 for i in range(d):
  for j in range(d):O[i,j]=cmod(tuple(M[i,j,:]),sr,ir)*iv%P
 return O
