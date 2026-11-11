#!/usr/bin/env python3
"""
h4_K_linear_operator_real_swap_even.py

Lossless party-swap-even wrapper around the audited unrestricted real
matrix-free FD4 operator.

The full effective moment vector has dimension 746825.  The exact signed swap
involution has even dimension 374414.  Let E be the sparse expansion:
  fixed+ i:       x_full[i] = x_even[r]
  pair i<->j,s:  x_full[i] = x_even[r], x_full[j] = s*x_even[r].
Then
  A_even = A E,
  A_even^* = E^T A^*.

Because f and K are swap-stable, feasibility of the full separator problem is
equivalent to feasibility in this even subspace.

Numerical arithmetic here is discovery only.  Exact moment indexing is pinned
by party_swap_effective.npz.

Usage:
  python h4_K_linear_operator_real_swap_even.py selftest \
    MAT SYSTEM NOGAP DUAL SPECDIR CACHEDIR SWAP_NPZ BLOCKSCSV
"""

import sys,json,hashlib,time,importlib.util
from pathlib import Path
import numpy as np

def die(x):raise SystemExit("ERROR: "+str(x))
def load(path,name):
    s=importlib.util.spec_from_file_location(name,path)
    m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m

basepath=Path(__file__).with_name("h4_K_linear_operator_real_precond.py")
if not basepath.exists():die("h4_K_linear_operator_real_precond.py must be beside wrapper")
base=load(str(basepath),"h4realprecond_swap")


class SwapEvenOperator:
    def __init__(self,mat,system,nogap,dual,specdir,cachedir,swap_npz,blocks=None,verbose=True):
        self.full=base.RealOperatorBatched(
            mat,system,nogap,dual,specdir,cachedir,blocks=blocks,verbose=verbose
        )
        z=np.load(swap_npz)
        self.rep=z["even_rep_index"].astype(np.int64)
        self.partner=z["even_expand_partner"].astype(np.int64)
        self.sign=z["even_expand_sign"].astype(np.float64)
        self.n_full=len(self.full.eff_to_global)
        self.n_even=len(self.rep)
        if self.n_full!=746825 or self.n_even!=374414:
            die("swap dimensions mismatch")
    def expand(self,x):
        x=np.asarray(x,float)
        if x.shape!=(self.n_even,):die("even vector shape")
        y=np.zeros(self.n_full,float)
        y[self.rep]=x
        diff=self.partner!=self.rep
        y[self.partner[diff]]=self.sign[diff]*x[diff]
        return y
    def reduce_adjoint(self,g):
        g=np.asarray(g,float)
        out=g[self.rep].copy()
        diff=self.partner!=self.rep
        out[diff]+=self.sign[diff]*g[self.partner[diff]]
        return out
    def A(self,x):
        return self.full.A(self.expand(x))
    def AT(self,Ys):
        return self.reduce_adjoint(self.full.AT(Ys))


def selftest(args):
    if len(args)!=8:
        die("selftest MAT SYSTEM NOGAP DUAL SPECDIR CACHEDIR SWAP_NPZ BLOCKSCSV")
    mat,system,nogap,dual,spec,cache,swap,bcsv=args
    blocks=[int(x) for x in bcsv.split(",")]
    t=time.time()
    O=SwapEvenOperator(mat,system,nogap,dual,spec,cache,swap,blocks)
    loadsec=time.time()-t
    rng=np.random.default_rng(20260830)
    x=rng.normal(size=O.n_even)
    t=time.time();AX=O.A(x);asec=time.time()-t
    Ys=[];lhs=0.0
    for M in AX:
        k=M.shape[0]
        R=rng.normal(size=(k,k))+1j*rng.normal(size=(k,k))
        Y=(R+R.conj().T)/2
        Ys.append(Y);lhs+=float(np.vdot(Y,M).real)
    t=time.time();g=O.AT(Ys);atsec=time.time()-t
    rhs=float(np.dot(x,g))
    rel=abs(lhs-rhs)/max(1,abs(lhs),abs(rhs))
    if rel>3e-8:die("swap-even adjoint mismatch %.3e"%rel)
    out={
      "status":"SWAP_EVEN_REAL_A_AT_SELFTEST_PASSED",
      "blocks":blocks,
      "full_dimension":O.n_full,
      "swap_even_dimension":O.n_even,
      "lhs":lhs,"rhs":rhs,"relative_error":rel,
      "load_seconds":loadsec,"A_seconds":asec,"AT_seconds":atsec,
    }
    raw=json.dumps(out,sort_keys=True,separators=(",",":")).encode()
    print(json.dumps({**out,"output_sha256":hashlib.sha256(raw).hexdigest()},indent=2,sort_keys=True))


if __name__=="__main__":
    if len(sys.argv)<2 or sys.argv[1]!="selftest":die("selftest")
    selftest(sys.argv[2:])
