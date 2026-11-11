#!/usr/bin/env python3
"""Batched exact GF(24001) A/A* backend for the canonical full K pencil.

Same operator as h4_K_linear_operator_modp.py, but all orbit-pair Fourier
transforms are batched. Every float64 GEMM is exact integer arithmetic under
an explicit absolute-sum <2^53 bound, and bitwise integrality is checked.

Python 3.9+.
"""
import sys,json,hashlib,importlib.util,time
from pathlib import Path
import numpy as np
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
def parse_pairs(p):
 d={}
 for line in open(p):r,i,j=map(int,line.split());d[(i,j)]=r
 return d
def mm(A,B):
 A=np.asarray(A,dtype=np.int64)%P;B=np.asarray(B,dtype=np.int64)%P;k=A.shape[1];out=np.zeros((A.shape[0],B.shape[1]),dtype=np.int64)
 # modular stage small matrices to avoid int64 overflow
 for lo in range(0,k,64):out=(out+A[:,lo:lo+64]@B[lo:lo+64])%P
 return out
def exact_float_gemm(A,B,inner_bound):
 if inner_bound*(P-1)*(P-1)>=(1<<53):die('exact float GEMM bound >=2^53')
 X=np.asarray(A,dtype=np.float64)@np.asarray(B,dtype=np.float64);R=np.rint(X)
 if not np.array_equal(X,R):die('nonintegral exact GEMM')
 if R.size and np.max(np.abs(R))>=(1<<53):die('exact GEMM result >=2^53')
 return R.astype(np.int64)%P

class OperatorBatched:
 def __init__(self,system_path,nogap_path,specdir,cachedir,blocks=None,pair_batch=192,verbose=True):
  self.specdir=Path(specdir);self.cachedir=Path(cachedir);self.pair_batch=pair_batch;self.verbose=verbose
  if sha(self.cachedir/'canonical_K_pencil_manifest.json')!=EXPECTED_MANIFEST:die('manifest SHA')
  self.ng=load(nogap_path,'ng_modbatch');Q,Qd,self.G,Hd,ff=self.ng.structural_construction();sys0,els,gens,ash=self.ng.load_and_match_certified_action(system_path,self.G)
  if ash!=EXPECTED_ACTION:die('action SHA')
  self.op=load(str(Path(__file__).with_name('h4_full_K_pencil_operator.py')),'h4op_modbatch')
  self.ids=np.memmap(self.specdir/'product_map.id.i32',dtype='<i4',mode='r',shape=(1485,ORDER));self.sgn=np.memmap(self.specdir/'product_map.sgn.i8',dtype='i1',mode='r',shape=(1485,ORDER));self.pairidx=parse_pairs(self.specdir/'product_map.pairs.txt')
  used=np.unique(np.asarray(self.ids).ravel());used=used[used>=0].astype(np.int64);self.eff_to_global=np.sort(used);self.global_to_eff=np.full(int(self.eff_to_global[-1])+1,-1,dtype=np.int32);self.global_to_eff[self.eff_to_global]=np.arange(len(used),dtype=np.int32)
  if len(used)!=746825:die('effective dimension')
  if blocks is None:blocks=range(1,21)
  self.blocks=[self._load_block(ir) for ir in blocks]
 def _load_block(self,ir):
  t=time.time();meta=json.load(open(self.cachedir/f'block_{ir:02d}.json'));z=np.load(self.cachedir/f'block_{ir:02d}.npz');gmods=z['generator_modp'].astype(np.int64);R=self.op.build_rall_from_generators(list(gmods),self.G);Rhat=R[np.asarray(self.G['inv_idx'],dtype=np.int64)].astype(np.uint16);del R;mods=meta['active_modules'];pairs=[]
  for ai,Oi in enumerate(mods):
   for aj in range(ai,len(mods)):
    Oj=mods[aj];pairs.append((ai,aj,int(self.pairidx[tuple(sorted((int(Oi['nonD_index']),int(Oj['nonD_index']))))])))
  b={'ir':ir,'meta':meta,'Rhat':Rhat,'Rflat':Rhat.reshape(ORDER,-1),'J':z['bilinear_J_modp'].astype(np.uint16),'V':z['V_modp'].astype(np.uint16),'Z':z['Z_modp'].astype(np.uint16),'pairs':pairs,'pairrows':np.array([x[2] for x in pairs],dtype=np.int32)}
  if self.verbose:print(f'loaded exact batched block {ir} d={meta["degree"]} k={meta["m_K"]} sec={time.time()-t:.2f}',file=sys.stderr,flush=True)
  return b
 def _E(self,x,rows):
  mids=np.asarray(self.ids[rows],dtype=np.int64);valid=mids>=0;E=np.zeros(mids.shape,dtype=np.uint16);ei=self.global_to_eff[mids[valid]];E[valid]=(self.sgn[rows][valid].astype(np.int64)*x[ei])%P;return E
 def A_block(self,x,b):
  x=np.asarray(x,dtype=np.int64)%P;meta=b['meta'];V=b['V'];J=b['J'];Rflat=b['Rflat'];mods=meta['active_modules'];m=int(meta['m_W_minus_D']);d=int(meta['degree']);B=np.zeros((m,m),dtype=np.int64);pairs=b['pairs']
  for lo in range(0,len(pairs),self.pair_batch):
   hi=min(len(pairs),lo+self.pair_batch);E=self._E(x,b['pairrows'][lo:hi]);F=exact_float_gemm(E,Rflat,ORDER).reshape(hi-lo,d,d);del E
   for t,(ai,aj,pr) in enumerate(pairs[lo:hi]):
    Oi,Oj=mods[ai],mods[aj];si=slice(int(Oi['copy_start']),int(Oi['copy_end']));sj=slice(int(Oj['copy_start']),int(Oj['copy_end']));M=mm(mm((V[:,si].T.astype(np.int64)@J.astype(np.int64))%P,F[t]),V[:,sj]);B[si,sj]=M
    if ai!=aj:B[sj,si]=M.T
  Z=b['Z'];return mm(Z.T,mm(B,Z))
 def A(self,x):return [self.A_block(x,b) for b in self.blocks]
 def AT_block(self,Y,b,gout):
  Y=np.asarray(Y,dtype=np.int64)%P;meta=b['meta'];V=b['V'];J=b['J'];Rflat=b['Rflat'];Z=b['Z'];mods=meta['active_modules'];pairs=b['pairs'];Yw=mm(Z,mm(Y,Z.T));d=int(meta['degree'])
  for lo in range(0,len(pairs),self.pair_batch):
   hi=min(len(pairs),lo+self.pair_batch);Qflat=np.empty((hi-lo,d*d),dtype=np.uint16)
   for t,(ai,aj,pr) in enumerate(pairs[lo:hi]):
    Oi,Oj=mods[ai],mods[aj];si=slice(int(Oi['copy_start']),int(Oi['copy_end']));sj=slice(int(Oj['copy_start']),int(Oj['copy_end']));Vi=V[:,si];Vj=V[:,sj];Yij=Yw[si,sj];Q=mm(mm(Vj,Yij.T),(Vi.T.astype(np.int64)@J.astype(np.int64))%P)
    if ai!=aj:Q=(2*Q)%P
    Qflat[t]=Q.T.reshape(-1).astype(np.uint16)
   H=exact_float_gemm(Rflat,Qflat.T,d*d).T;rows=b['pairrows'][lo:hi];mids=np.asarray(self.ids[rows],dtype=np.int64);valid=mids>=0;ei=self.global_to_eff[mids[valid]];vals=(self.sgn[rows][valid].astype(np.int64)*H[valid])%P;np.add.at(gout,ei,vals);gout%=P
 def AT(self,Ys):
  g=np.zeros(len(self.eff_to_global),dtype=np.int64)
  for Y,b in zip(Ys,self.blocks):self.AT_block(Y,b,g)
  return g%P

def selftest(args):
 if len(args)!=5:die('selftest SYSTEM NOGAP SPECDIR CACHEDIR BLOCKSCSV')
 system,ng,spec,cache,bcsv=args;blocks=[int(x) for x in bcsv.split(',')];t=time.time();O=OperatorBatched(system,ng,spec,cache,blocks);loadsec=time.time()-t;rng=np.random.default_rng(20260829);x=rng.integers(0,P,size=len(O.eff_to_global),dtype=np.int64);Ys=[]
 t=time.time();AX=O.A(x);Asec=time.time()-t;lhs=0
 for b,M in zip(O.blocks,AX):
  k=int(b['meta']['m_K']);R=rng.integers(0,P,size=(k,k),dtype=np.int64);Y=(R+R.T)%P;Ys.append(Y);lhs=(lhs+int(np.sum((Y*M)%P,dtype=np.int64)))%P
 t=time.time();g=O.AT(Ys);ATsec=time.time()-t;rhs=int(np.dot(x%P,g%P))%P
 if lhs!=rhs:die(f'adjoint mismatch {lhs}!={rhs}')
 out={'status':'BATCHED_EXACT_GF24001_A_AT_SELFTEST_PASSED','blocks':blocks,'effective_dimension':len(x),'lhs':lhs,'rhs':rhs,'load_seconds':loadsec,'A_seconds':Asec,'AT_seconds':ATsec,'x_sha256':hashlib.sha256(x.astype('<u2').tobytes()).hexdigest(),'AT_sha256':hashlib.sha256(g.astype('<u2').tobytes()).hexdigest()};raw=json.dumps(out,sort_keys=True,separators=(',',':')).encode();print(json.dumps({**out,'output_sha256':hashlib.sha256(raw).hexdigest()},indent=2,sort_keys=True))
if __name__=='__main__':
 if len(sys.argv)<2 or sys.argv[1]!='selftest':die('selftest')
 selftest(sys.argv[2:])
