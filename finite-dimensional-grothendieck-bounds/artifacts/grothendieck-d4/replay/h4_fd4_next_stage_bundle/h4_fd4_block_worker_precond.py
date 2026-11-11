#!/usr/bin/env python3
"""One-block worker for unrestricted FD4 PDHG discovery. Numerical only."""
import sys,argparse,json,hashlib,time
from pathlib import Path
import numpy as np
from scipy.linalg import eigh
from h4_K_linear_operator_real_precond import RealOperatorBatched

def sha(p):
 h=hashlib.sha256();
 with open(p,'rb') as f:
  for z in iter(lambda:f.read(1<<20),b''):h.update(z)
 return h.hexdigest()

def main():
 ap=argparse.ArgumentParser();ap.add_argument('mat');ap.add_argument('system');ap.add_argument('nogap');ap.add_argument('dual');ap.add_argument('specdir');ap.add_argument('cachedir');ap.add_argument('ir',type=int);ap.add_argument('x');ap.add_argument('outdir');ap.add_argument('--sigma',type=float,default=2e-4);ap.add_argument('--Yprev');ap.add_argument('--no-at',action='store_true');a=ap.parse_args();t=time.time();outdir=Path(a.outdir);outdir.mkdir(parents=True,exist_ok=True)
 O=RealOperatorBatched(a.mat,a.system,a.nogap,a.dual,a.specdir,a.cachedir,blocks=[a.ir],verbose=False);x=np.load(a.x).astype(float);M=O.A(x)[0];w,V=eigh((M+M.conj().T)/2,check_finite=False,driver='evd');neg=w[w<0]
 if a.Yprev:Y0=np.load(a.Yprev).astype(complex)
 else:Y0=np.zeros_like(M)
 T=Y0+a.sigma*M;wy,Vy=eigh((T+T.conj().T)/2,check_finite=False,driver='evd');Y=(Vy*np.minimum(wy,0.0))@Vy.conj().T
 yp=outdir/f'Y_{a.ir:02d}.npy';np.save(yp,Y)
 gp=None
 if not a.no_at:
  gp=outdir/f'g_{a.ir:02d}.npy';g=O.AT([Y]);np.save(gp,g)
 rec={'ir':a.ir,'k':M.shape[0],'x_sha256':sha(a.x),'min_eig':float(w[0]),'max_eig':float(w[-1]),'negative_count':int(np.sum(w<0)),'negative_frobenius':float(np.linalg.norm(neg)),'M_float_sha256':hashlib.sha256(np.ascontiguousarray(M).view(np.float64).tobytes()).hexdigest(),'Y_sha256':sha(yp),'Y_frobenius':float(np.linalg.norm(Y,'fro')),'seconds':time.time()-t}
 if gp is not None:rec['g_sha256']=sha(gp);rec['g_l2']=float(np.linalg.norm(g))
 raw=json.dumps(rec,sort_keys=True,separators=(',',':')).encode();jp=outdir/f'block_{a.ir:02d}.json';jp.write_bytes(raw);print(json.dumps({**rec,'output_sha256':hashlib.sha256(raw).hexdigest()},sort_keys=True))
if __name__=='__main__':main()
