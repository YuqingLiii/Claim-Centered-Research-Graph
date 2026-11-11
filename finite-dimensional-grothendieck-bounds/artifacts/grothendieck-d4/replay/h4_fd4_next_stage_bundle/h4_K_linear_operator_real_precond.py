#!/usr/bin/env python3
"""Batched real matrix-free A/A* backend for unrestricted FD4 discovery.

Mathematical operator is identical to h4_K_linear_operator_real.py.  The only
change is batching the 14,400-element Fourier transforms into large BLAS GEMMs.
No restricted moment ansatz is introduced.

Characteristic-zero representation/cache conventions are those of the audited
canonical K-pencil manifest. Floating output is discovery only.

Python 3.9+. numpy/scipy/h5py.
"""
import sys,json,hashlib,importlib.util,math,time
from pathlib import Path
import numpy as np
import h5py

P=24001;ORDER=14400
EXPECTED_MANIFEST='41eaa1a24984bdc456ec325c9e45f6e0d989d86dadfcbb7e88db2e10fc04a86b'
EXPECTED_ACTION='1a5582d7fd1ce1c01135421413aa8fb7c6761fc953622e37387231f58c5f0097'

def die(x):raise SystemExit('ERROR: '+str(x))
def sha(p):
 h=hashlib.sha256();
 with open(p,'rb') as f:
  for z in iter(lambda:f.read(1<<20),b''):h.update(z)
 return h.hexdigest()
def load(p,n):
 s=importlib.util.spec_from_file_location(n,p);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
def field_eval(A):
 A=np.asarray(A,dtype=np.float64);s=math.sqrt(5.0);return A[...,0]+s*A[...,1]+1j*(A[...,2]+s*A[...,3])
def parse_pairs(path):
 d={}
 for line in open(path):r,i,j=map(int,line.split());d[(i,j)]=r
 return d

class RealOperatorBatched:
 def __init__(self,mat_path,system_path,nogap_path,dual_path,specdir,cachedir,blocks=None,verbose=True,pair_batch=192):
  self.specdir=Path(specdir);self.cachedir=Path(cachedir);self.verbose=verbose;self.pair_batch=pair_batch
  if sha(self.cachedir/'canonical_K_pencil_manifest.json')!=EXPECTED_MANIFEST:die('manifest SHA')
  self.ng=load(nogap_path,'ng_realbatch');self.base=load(dual_path,'base_realbatch');self.base.init_pairs();Q,Qd,self.G,Hd,ff=self.ng.structural_construction();sys0,self.els,self.gens,ash=self.ng.load_and_match_certified_action(system_path,self.G)
  if ash!=EXPECTED_ACTION:die('action SHA')
  self.ids=np.memmap(self.specdir/'product_map.id.i32',dtype='<i4',mode='r',shape=(1485,ORDER));self.sgn=np.memmap(self.specdir/'product_map.sgn.i8',dtype='i1',mode='r',shape=(1485,ORDER));self.pairidx=parse_pairs(self.specdir/'product_map.pairs.txt')
  used=np.unique(np.asarray(self.ids).ravel());used=used[used>=0].astype(np.int64);self.eff_to_global=np.sort(used);self.global_to_eff=np.full(int(self.eff_to_global[-1])+1,-1,dtype=np.int32);self.global_to_eff[self.eff_to_global]=np.arange(len(used),dtype=np.int32)
  if len(used)!=746825:die('effective dimension')
  with h5py.File(mat_path,'r') as f:
   ax=np.asarray(f['ax'][()]).reshape(-1).astype(np.int8);by=np.asarray(f['by'][()]).reshape(-1).astype(np.int8)
  Arel,_=self.base.enumerate_pair_support_orbits(self.gens);Zlines=[46,56,85,99,131,148];killed,kbool=self.base.killed_pair_data(Arel,Zlines);faceR=self.base.Face(ax,by,'y',Zlines);faceL=self.base.Face(by,ax,'x',Zlines)
  self.Rseed=np.vstack([self.base.direct_residual_seed_matrix(faceR,kbool),self.base.direct_residual_seed_matrix(faceL,kbool)]).astype(np.float64)
  if blocks is None:blocks=range(1,21)
  self.blocks=[self._load_block(ir) for ir in blocks]
 def _build_Rhat(self,gens):
  d=gens[0].shape[0];R=np.empty((ORDER,d,d),dtype=np.complex128);R[0]=np.eye(d)
  for a in range(1,ORDER):R[a]=R[int(self.G['parent'][a])]@gens[int(self.G['parent_gen'][a])]
  return R[np.asarray(self.G['inv_idx'],dtype=np.int64)]
 def _rvals(self,rep_mid):
  rv=np.empty((ORDER,14),float)
  for g,(p,s) in enumerate(self.els):
   mm,sg=self.base.act_mid(int(rep_mid),p,s);rv[g]=int(sg)*self.Rseed[:,mm]
  return rv
 def _load_block(self,ir):
  t=time.time();meta=json.load(open(self.cachedir/f'block_{ir:02d}.json'));z=np.load(self.cachedir/f'block_{ir:02d}.npz');d=int(meta['degree']);den=float(meta['representation_common_denominator'])
  gens=field_eval(z['generator_exact_num'])/den;Rhat=self._build_Rhat(list(gens));Rflat=Rhat.reshape(ORDER,d*d);V=field_eval(z['V_exact_num'])/den;H=np.diag(z['hermitian_metric_diag'].astype(float));mods=meta['active_modules'];m=int(meta['m_W_minus_D'])
  # one batched restriction transform: (14*nmods)xG times Gxd^2
  RR=np.empty((14*len(mods),ORDER),dtype=np.float64)
  for oi,rec in enumerate(mods):RR[14*oi:14*(oi+1)]=self._rvals(rec['rep_mid']).T
  FF=(RR@Rflat).reshape(len(mods),14,d,d);del RR
  C=np.zeros((14*d,m),dtype=np.complex128)
  for oi,rec in enumerate(mods):
   sl=slice(int(rec['copy_start']),int(rec['copy_end']));Vi=V[:,sl]
   for ss in range(14):C[ss*d:(ss+1)*d,sl]=FF[oi,ss]@Vi
  del FF
  rows=z['pivot_rows'].astype(int);pc=z['pivot_columns'].astype(int);free=z['free_columns'].astype(int);CP=C[np.ix_(rows,pc)];CF=C[np.ix_(rows,free)];Z=np.zeros((m,len(free)),dtype=np.complex128);Z[free,:]=np.eye(len(free));Z[pc,:]=-np.linalg.solve(CP,CF)
  res=np.linalg.norm(C@Z,ord=np.inf);scale=max(1,np.linalg.norm(C,ord=np.inf)*np.linalg.norm(Z,ord=np.inf));rel=res/scale
  if rel>3e-9:die(f'block {ir} canonical Z residual {rel}')
  Zcanon=Z
  Z,_Rz=np.linalg.qr(Zcanon,mode='reduced')
  qres=np.linalg.norm(C@Z,ord=np.inf)/max(1,np.linalg.norm(C,ord=np.inf)*np.linalg.norm(Z,ord=np.inf))
  if qres>3e-9:die(f'block {ir} QR K basis residual {qres}')
  pairs=[]
  for ai,Oi in enumerate(mods):
   for aj in range(ai,len(mods)):
    Oj=mods[aj];pairs.append((ai,aj,int(self.pairidx[tuple(sorted((int(Oi['nonD_index']),int(Oj['nonD_index']))))])))
  # static pair arrays and left/right slices
  pairrows=np.array([q[2] for q in pairs],dtype=np.int32)
  if self.verbose:print(f'loaded batched real block {ir} d={d} m={m} k={len(free)} pairs={len(pairs)} Zrel={rel:.3e} condR={np.linalg.cond(_Rz):.3e} sec={time.time()-t:.2f}',file=sys.stderr,flush=True)
  return {'ir':ir,'meta':meta,'Rflat':Rflat,'H':H,'V':V,'Z':Z,'pairs':pairs,'pairrows':pairrows,'Zrel':rel,'Zcanon_condition_estimate':float(np.linalg.cond(_Rz))}
 def _ell_batch(self,x,rows):
  mids=np.asarray(self.ids[rows],dtype=np.int64);sg=np.asarray(self.sgn[rows],dtype=np.float64);valid=mids>=0;E=np.zeros(mids.shape,dtype=np.float64);ei=self.global_to_eff[mids[valid]];E[valid]=sg[valid]*x[ei];return E
 def A_block(self,x,b):
  x=np.asarray(x,float);meta=b['meta'];V=b['V'];H=b['H'];Rflat=b['Rflat'];mods=meta['active_modules'];m=int(meta['m_W_minus_D']);d=int(meta['degree']);B=np.zeros((m,m),complex);pairs=b['pairs']
  for lo in range(0,len(pairs),self.pair_batch):
   hi=min(len(pairs),lo+self.pair_batch);rows=b['pairrows'][lo:hi];E=self._ell_batch(x,rows);F=(E@Rflat).reshape(hi-lo,d,d);del E
   for t,(ai,aj,pr) in enumerate(pairs[lo:hi]):
    Oi,Oj=mods[ai],mods[aj];si=slice(int(Oi['copy_start']),int(Oi['copy_end']));sj=slice(int(Oj['copy_start']),int(Oj['copy_end']));M=V[:,si].conj().T@H@F[t]@V[:,sj];B[si,sj]=M
    if ai!=aj:B[sj,si]=M.conj().T
  Z=b['Z'];M=Z.conj().T@B@Z;return (M+M.conj().T)/2
 def A(self,x):return [self.A_block(x,b) for b in self.blocks]
 def AT_block(self,Y,b,gout):
  Y=np.asarray(Y,complex);meta=b['meta'];V=b['V'];H=b['H'];Rflat=b['Rflat'];Z=b['Z'];mods=meta['active_modules'];pairs=b['pairs'];Yw=Z@<email-redacted>().T;d=int(meta['degree'])
  for lo in range(0,len(pairs),self.pair_batch):
   hi=min(len(pairs),lo+self.pair_batch);Qflat=np.empty((hi-lo,d*d),dtype=np.complex128)
   for t,(ai,aj,pr) in enumerate(pairs[lo:hi]):
    Oi,Oj=mods[ai],mods[aj];si=slice(int(Oi['copy_start']),int(Oi['copy_end']));sj=slice(int(Oj['copy_start']),int(Oj['copy_end']));Vi=V[:,si];Vj=V[:,sj];Yij=Yw[si,sj];Q=<email-redacted>()<email-redacted>().T@H;Qflat[t]=Q.T.reshape(-1)
    if ai!=aj:Qflat[t]*=2.0
   # G x d2 @ d2 x batch, real trace
   HH=np.real(Rflat@Qflat.T).T;rows=b['pairrows'][lo:hi];mids=np.asarray(self.ids[rows],dtype=np.int64);sg=np.asarray(self.sgn[rows],dtype=np.float64);valid=mids>=0;ei=self.global_to_eff[mids[valid]];vals=(sg*HH)[valid];np.add.at(gout,ei,vals)
 def AT(self,Ys):
  g=np.zeros(len(self.eff_to_global),float)
  for Y,b in zip(Ys,self.blocks):self.AT_block(Y,b,g)
  return g

def selftest(args):
 if len(args)!=7:die('selftest MAT SYSTEM NOGAP DUAL SPECDIR CACHEDIR BLOCKS')
 mat,sys0,ng,dual,spec,cache,bcsv=args;blocks=[int(x) for x in bcsv.split(',')];t=time.time();O=RealOperatorBatched(mat,sys0,ng,dual,spec,cache,blocks);loadsec=time.time()-t;rng=np.random.default_rng(20260829);x=rng.normal(size=len(O.eff_to_global));t=time.time();AX=O.A(x);Asec=time.time()-t;Ys=[];lhs=0.0
 for M in AX:
  k=M.shape[0];R=rng.normal(size=(k,k))+1j*rng.normal(size=(k,k));Y=(R+R.conj().T)/2;Ys.append(Y);lhs+=float(np.vdot(Y,M).real)
 t=time.time();g=O.AT(Ys);ATsec=time.time()-t;rhs=float(np.dot(x,g));rel=abs(lhs-rhs)/max(1,abs(lhs),abs(rhs));
 if rel>3e-8:die(f'adjoint rel {rel}')
 out={'status':'BATCHED_REAL_MATRIXFREE_A_AT_SELFTEST_PASSED','blocks':blocks,'lhs':lhs,'rhs':rhs,'relative_error':rel,'effective_dimension':len(x),'load_seconds':loadsec,'A_seconds':Asec,'AT_seconds':ATsec};raw=json.dumps(out,sort_keys=True,separators=(',',':')).encode();print(json.dumps({**out,'output_sha256':hashlib.sha256(raw).hexdigest()},indent=2,sort_keys=True))
if __name__=='__main__':
 if len(sys.argv)<2 or sys.argv[1]!='selftest':die('selftest')
 selftest(sys.argv[2:])
