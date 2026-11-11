#!/usr/bin/env python3
"""
Exact degree<=4 invariant equality-restriction rank certificate.
Python 3.9+. Dependencies numpy,h5py.

Proves rank=28 for restriction of H4-invariant Boolean polynomials of degree
<=4 to the two base equality-face orbits.

Upper bound: each order-6 face stabilizer acts on six free singleton Fourier
modes as the regular permutation action of S3. Burnside through Fourier degree
4 gives (57+3*7+2*3)/6=14 per face, hence <=28 for two face orbits.

Lower bound: 28 explicitly listed H4 Reynolds orbit sums have a 28x28
restriction minor nonzero mod 24001. Reduction rank cannot exceed
characteristic-zero rank, so rank>=28 over Q. Together: rank=28.

The script computes Reynolds restrictions exactly as integer group sums using
the certified signed action. No floating arithmetic enters the rank test.
"""
import sys,json,hashlib,importlib.util,math
from pathlib import Path
import numpy as np,h5py
P=24001;N=300;NV=600;ORDER=14400
EXPECTED_MD5='b5223ca2fd5c4cbe52e93a23a4570b9f'
EXPECTED_ACTION='1a5582d7fd1ce1c01135421413aa8fb7c6761fc953622e37387231f58c5f0097'
ZLINES=[46,56,85,99,131,148]
# Explicit independent invariant orbit-sum representatives found by exhaustive search.
SUPPORTS=[
 (),
 (0,300), (300,304),(300,331),(300,405),
 (300,301,302,382),(300,418),(300,301,349,409),(300,304,369,409),
 (300,301,302,419),(300,304,369,436),(300,301,391,395),(300,304,369,450),(300,304,436,450),
 (0,1),(0,4),(0,13),(0,31),(0,105),(0,1,2,82),(0,118),(0,1,49,109),(0,4,69,109),
 (0,1,2,119),(0,4,69,136),(0,1,91,95),(0,4,69,150),(0,4,136,150)
]

def die(x): raise SystemExit('ERROR: '+str(x))
def md5(path):
 h=hashlib.md5();
 with open(path,'rb') as f:
  for z in iter(lambda:f.read(1<<20),b''):h.update(z)
 return h.hexdigest()
def load(path,name):
 s=importlib.util.spec_from_file_location(name,path);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m

def rank_rref(A,p=P):
 A=np.array(A,dtype=np.int64,copy=True)%p;m,n=A.shape;r=0;pivs=[]
 for c in range(n):
  z=np.flatnonzero(A[r:,c])
  if not len(z):continue
  i=r+int(z[0]);A[[r,i]]=A[[i,r]]
  A[r]=(A[r]*pow(int(A[r,c]),p-2,p))%p
  rr=np.flatnonzero(A[:,c]);rr=rr[rr!=r]
  for lo in range(0,len(rr),64):
   q=rr[lo:lo+64];fac=A[q,c].copy();A[q]=(A[q]-fac[:,None]*A[r])%p
  pivs.append(c);r+=1
  if r==m:break
 return r,pivs,A

def det_mod(M,p=P):
 A=np.array(M,dtype=np.int64,copy=True)%p;n=A.shape[0];d=1
 for c in range(n):
  z=np.flatnonzero(A[c:,c])
  if not len(z):return 0
  i=c+int(z[0])
  if i!=c:A[[c,i]]=A[[i,c]];d=(-d)%p
  pv=int(A[c,c]);d=d*pv%p;inv=pow(pv,p-2,p);A[c]=(A[c]*inv)%p
  for r in range(c+1,n):
   if A[r,c]:A[r]=(A[r]-int(A[r,c])*A[c])%p
 return int(d)

def main():
 if len(sys.argv)!=5:
  die('usage: python h4_degree4_equality_restriction_rank.py MAT SYSTEM NOGAP SPECDIR')
 mat,system,nogap,specdir0=sys.argv[1:];specdir=Path(specdir0)
 if md5(mat)!=EXPECTED_MD5:die('MAT MD5')
 ng=load(nogap,'h4ng_face28');Q,Qd,G,Hd,ff=ng.structural_construction();sys0,els,gens,asha=ng.load_and_match_certified_action(system,G)
 if asha!=EXPECTED_ACTION:die('action SHA')
 perm=np.memmap(specdir/'h4_perm_u16.bin',dtype='<u2',mode='r',shape=(ORDER,N));sgn=np.memmap(specdir/'h4_sign_i8.bin',dtype='i1',mode='r',shape=(ORDER,N))
 with h5py.File(mat,'r') as f:
  ax=np.asarray(f['ax'][()]).reshape(-1).astype(np.int8);by=np.asarray(f['by'][()]).reshape(-1).astype(np.int8)
 zR=np.concatenate([ax,by]);zL=np.concatenate([by,ax])
 freeR={300+j:k for k,j in enumerate(ZLINES)};freeL={j:k for k,j in enumerate(ZLINES)}
 masks=[m for m in range(64) if bin(m).count('1')<=4]
 bitR=np.zeros(NV,dtype=np.int64);bitL=np.zeros(NV,dtype=np.int64);isR=np.zeros(NV,bool);isL=np.zeros(NV,bool)
 for v,k in freeR.items():bitR[v]=1<<k;isR[v]=1
 for v,k in freeL.items():bitL[v]=1<<k;isL[v]=1
 def restr(supp):
  sp=np.ones(ORDER,dtype=np.int64);trs=[]
  for v in supp:
   party=v>=N;line=v%N;sp*=sgn[:,line].astype(np.int64);trs.append(perm[:,line].astype(np.int64)+(N if party else 0))
  out=[]
  for bit,isf,z in [(bitR,isR,zR),(bitL,isL,zL)]:
   ma=np.zeros(ORDER,dtype=np.int64);va=sp.copy()
   for t in trs:ma|=bit[t];va*=np.where(isf[t],1,z[t].astype(np.int64))
   bc=np.bincount(ma,weights=va,minlength=64).astype(np.int64)
   out.extend(int(bc[m]) for m in masks)
  return out
 A=np.column_stack([restr(s) for s in SUPPORTS])
 r,_,_=rank_rref(A)
 if r!=28:die('explicit columns rank %d !=28'%r)
 rr,rows,_=rank_rref(A.T)
 rows=rows[:28]
 M=A[rows,:];det=det_mod(M)
 if det==0:die('minor det zero')
 # Upper bound from exact S3 regular cycle types.
 face_dim=(57+3*7+2*3)//6
 if face_dim!=14:die('Burnside face dim')
 out={
  'status':'PROVED_INVARIANT_DEGREE4_EQUALITY_RESTRICTION_RANK_28',
  'face_stabilizer_order':6,
  'free_singleton_action':'regular permutation representation of S3',
  'cycle_types':{'identity':'1^6 x1','order2':'2^3 x3','order3':'3^2 x2'},
  'face_invariant_fourier_dimension_degree_le4':14,
  'two_face_upper_bound':28,
  'explicit_column_count':28,
  'rank_mod_24001':28,
  'minor_rows':rows,
  'minor_det_mod_24001':det,
  'representative_supports':[list(x) for x in SUPPORTS],
  'restriction_matrix_sha256':hashlib.sha256(np.asarray(A,dtype='<i8').tobytes()).hexdigest(),
  'consequence_effective_746825_rank_upper_bound':746797,
  'kernel_dimension_lower_bound':28,
 }
 raw=json.dumps(out,sort_keys=True,separators=(',',':')).encode();p=Path(mat+'.degree4_equality_restriction_rank.json');p.write_bytes(raw);disp=dict(out);disp['output_path']=str(p);disp['output_sha256']=hashlib.sha256(raw).hexdigest();print(json.dumps(disp,indent=2,sort_keys=True))
if __name__=='__main__':main()
