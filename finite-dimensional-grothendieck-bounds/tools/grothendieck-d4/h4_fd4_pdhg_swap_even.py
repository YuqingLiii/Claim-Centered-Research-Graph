#!/usr/bin/env python3
"""
h4_fd4_pdhg_swap_even.py

Lossless party-swap-even matrix-free PDHG discovery solver for FD4.

This is NOT a restricted moment ansatz.  Since tau:(x,y)<->(y,x) preserves
A=A^T, f=C-x^T A y, and the complete equality set defining K, every separator
may be averaged with tau.  The 746825 effective moments reduce exactly to
374414 swap-even coordinates.

The PSD blocks remain the same 20 complete-K blocks.  The worker backend is
the audited QR-congruent real operator; all numerical output is discovery only.

The driver is process-isolated block-by-block to avoid retaining all rho(g)
tables simultaneously.  It supports checkpoints and deterministic output
hashes.

Usage:
  python h4_fd4_pdhg_swap_even.py \
    MAT SYSTEM NOGAP DUAL SPECDIR CACHEDIR SWAP_NPZ \
    --iters 5 --tau 1e-10 --sigma 1e-6 --workdir fd4_swap_work

A final theorem requires exact reconstruction; this script never labels a
numerical point PROVED.
"""

import sys,argparse,json,hashlib,subprocess
from pathlib import Path
import numpy as np

CVAL=2081044153087351400.0


def sha(p):
    h=hashlib.sha256()
    with open(p,'rb') as f:
        for z in iter(lambda:f.read(1<<20),b''):h.update(z)
    return h.hexdigest()


def expand_even(x,z):
    rep=z['even_rep_index'].astype(np.int64)
    partner=z['even_expand_partner'].astype(np.int64)
    sign=z['even_expand_sign'].astype(float)
    full=np.zeros(746825,float)
    full[rep]=x
    q=partner!=rep
    full[partner[q]]=sign[q]*x[q]
    return full


def reduce_adjoint(g,z):
    rep=z['even_rep_index'].astype(np.int64)
    partner=z['even_expand_partner'].astype(np.int64)
    sign=z['even_expand_sign'].astype(float)
    out=g[rep].copy()
    q=partner!=rep
    out[q]+=sign[q]*g[partner[q]]
    return out


def full_objective(specdir):
    # Need only mapping effective global IDs and the 55 objective coefficients.
    ids=np.memmap(Path(specdir)/'product_map.id.i32',dtype='<i4',mode='r',
                  shape=(1485,14400))
    used=np.unique(np.asarray(ids).ravel());used=np.sort(used[used>=0])
    g2e={int(g):i for i,g in enumerate(used)}
    B=np.array(json.load(open(Path(specdir)/'objective_B_coeffs55.json')),float)
    c=np.zeros(len(used),float)
    for gid in range(55):
        c[g2e[gid]]=1.0 if gid==0 else -B[gid]/CVAL
    return c


def proj_h(x,c):
    return x-c*((np.dot(c,x)+1.0)/np.dot(c,c))


def main():
    ap=argparse.ArgumentParser()
    for q in ['mat','system','nogap','dual','specdir','cachedir','swap_npz']:
        ap.add_argument(q)
    ap.add_argument('--iters',type=int,default=1)
    ap.add_argument('--tau',type=float,default=1e-10)
    ap.add_argument('--sigma',type=float,default=1e-6)
    ap.add_argument('--omega',type=float,default=1.0)
    ap.add_argument('--workdir',default='fd4_swap_even_work')
    args=ap.parse_args()

    z=np.load(args.swap_npz)
    n=len(z['even_rep_index'])
    if n!=374414:
        raise RuntimeError('swap-even dimension mismatch')

    cfull=full_objective(args.specdir)
    ceven=reduce_adjoint(cfull,z)
    x=proj_h(np.zeros(n),ceven)
    xbar=x.copy()

    wd=Path(args.workdir);wd.mkdir(parents=True,exist_ok=True)
    worker=Path(__file__).with_name('h4_fd4_block_worker_precond.py')
    if not worker.exists():
        raise RuntimeError('h4_fd4_block_worker_precond.py must be beside driver')

    history=[]
    for it in range(args.iters):
        xf=expand_even(xbar,z)
        xp=wd/f'xbar_full_{it:04d}.npy'
        np.save(xp,xf)
        gfull=np.zeros(746825,float)
        rows=[]
        for ir in range(1,21):
            yp=wd/f'Y_{ir:02d}.npy'
            cmd=[
                sys.executable,str(worker),
                args.mat,args.system,args.nogap,args.dual,args.specdir,args.cachedir,
                str(ir),str(xp),str(wd),'--sigma',str(args.sigma)
            ]
            if yp.exists():
                cmd+=['--Yprev',str(yp)]
            r=subprocess.run(cmd,check=True,capture_output=True,text=True)
            rec=json.loads(r.stdout);rows.append(rec)
            gfull+=np.load(wd/f'g_{ir:02d}.npy')
        geven=reduce_adjoint(gfull,z)
        xnew=proj_h(x-args.tau*geven,ceven)
        xbar=xnew+args.omega*(xnew-x)
        dx=float(np.linalg.norm(xnew-x))
        x=xnew

        # Q=-Y => A^*Q=-gfull, and reduced stationarity is E^T(-gfull).
        gs=-geven
        mu=float(np.dot(ceven,gs)/np.dot(ceven,ceven))
        rel=float(np.linalg.norm(gs-mu*ceven)/
                  max(1,np.linalg.norm(gs),abs(mu)*np.linalg.norm(ceven)))

        rec={
          'iteration':it,
          'swap_even_dimension':n,
          'normalization_residual':float(np.dot(ceven,x)+1.0),
          'global_min_eigenvalue_at_xbar':min(r['min_eig'] for r in rows),
          'negative_frobenius_at_xbar':float(np.sqrt(sum(
              r['negative_frobenius']**2 for r in rows
          ))),
          'dual_mu':mu,
          'dual_stationarity_relative_residual':rel,
          'primal_step_l2':dx,
          'x_l2':float(np.linalg.norm(x)),
          'x_linf':float(np.max(np.abs(x))),
          'block_worker_hashes':[r['output_sha256'] for r in rows],
        }
        history.append(rec)
        print(json.dumps(rec,sort_keys=True),flush=True)
        np.save(wd/'x_even_current.npy',x)

    out={
      'status':'NUMERICAL_DISCOVERY_ONLY_SWAP_EVEN_FULL_FD4',
      'lossless_symmetry_reduction':True,
      'full_effective_dimension':746825,
      'swap_even_dimension':n,
      'iterations':args.iters,
      'tau':args.tau,'sigma':args.sigma,
      'history':history,
      'x_even_sha256':sha(wd/'x_even_current.npy'),
    }
    raw=json.dumps(out,sort_keys=True,separators=(",",":")).encode()
    p=wd/'pdhg_swap_even_result.json';p.write_bytes(raw)
    print(json.dumps({**out,'output_path':str(p),
                      'output_sha256':hashlib.sha256(raw).hexdigest()},
                     indent=2,sort_keys=True))


if __name__=='__main__':
    main()
