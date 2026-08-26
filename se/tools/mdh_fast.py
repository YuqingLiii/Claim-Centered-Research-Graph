"""Float fast-path for SE adversary norms via NO-side Gram kernels.

Factorized form (exactly mirrors mdh_sigma's khat):
   khat(lam)(t) = n! * sum_{s in S_n} W_s S_V^{-1} W~_s^T G,
   W_s(t)  = sum_o t_o Q_{s,o},          Q_{s,o}  = sum_{i: orb(h_s l_i)=o} rho(x_i) Vb
   W~_s(t) = sum_o t_o Q~_{s,o} with the SAME coefficients (both sides carry
             t(h_s o u)); Q~ = Q, so khat = n! sum_s W_s S_V^{-1} W_s^T G.
   Delta_0-masked version: Q^D_{s,o} = sum_{i: orb(h_s l_i)=o} m_i rho(x_i) Vb,
   m_i = [l_i(0) != 0];  khat_D = n! sum_s W^D_s S_V^{-1} (W^D_s)^T G.

   ||Gamma||^2 = max_lam lammax(G^{1/2} khat G^{-1/2});  same masked for Delta.

Verified anchors: n=2 decoded optimum gives (2.1498299, 1.0000000);
optimizer targets ADV(3)=2.4543437, ADV(4)=2.7325236.
"""
import sys, math, time
import numpy as np
from itertools import permutations as iperms
from pathlib import Path

PROJECT = Path(__file__).resolve().parents[1]
from mdh_engine import YSN, CosetSpace, LambdaData, partitions

def hmap(s, n):
    return tuple(list(range(n)) + [n + s[j] for j in range(n)])

class FastLambda:
    def __init__(self, n, lam, cs, shift, mask0):
        self.n, self.lam = n, lam
        ysn = YSN(lam)
        d = self.d = ysn.dim
        S = []
        for k in range(2 * n - 1):
            M = np.zeros((d, d))
            for i in range(d):
                for j, c in ysn.act[k][i]:
                    M[j, i] = float(c)
            S.append(M)
        self.G = np.array([float(g) for g in ysn.gram])
        ld = LambdaData(lam, n, cs)
        self.dV = ld.dV
        Vb = np.array([[float(x) for x in v] for v in ld.Vbasis]).T  # d x dV
        SV = Vb.T @ (self.G[:, None] * Vb)
        self.SVinv = np.linalg.inv(SV)
        # bucket accumulation: propagate Vb down the BFS tree
        nper = math.factorial(n)
        norb = shift[next(iter(shift))].max() + 1
        slist = list(shift.keys())
        Q = np.zeros((len(slist), norb, d, self.dV))
        QD = np.zeros((len(slist), norb, d, self.dV))
        FWD = [None] * cs.size
        FWD[0] = Vb
        for i in range(cs.size):
            if i > 0:
                par, k = cs.tree[i]
                FWD[i] = S[k] @ FWD[par]
            Fi = FWD[i]
            m = mask0[i]
            for si, s in enumerate(slist):
                o = shift[s][i]
                Q[si, o] += Fi
                if m:
                    QD[si, o] += Fi
        self.Q, self.QD = Q, QD
        self.slist = slist
        self.sqrtG = np.sqrt(self.G)
        self.fact = float(math.factorial(n))

    def pencil_max(self, t, masked=False):
        Q = self.QD if masked else self.Q
        d = self.d
        K = np.zeros((d, d))
        for si in range(len(self.slist)):
            W = np.tensordot(t, Q[si], axes=(0, 0))     # d x dV
            K += W @ self.SVinv @ W.T
        K *= self.fact
        # G-symmetrize: M = G^{1/2} K G^{1/2}?? K here = khat G^{-1}-form:
        # khat = K * G (right-mult).  G^{1/2} khat G^{-1/2} = G^{1/2} K G^{1/2}.
        M = (self.sqrtG[:, None] * K) * self.sqrtG[None, :]
        M = 0.5 * (M + M.T)
        w, V = np.linalg.eigh(M)
        return w[-1], V[:, -1]

    def grad_max(self, t, masked=False):
        """(lammax, gradient d lammax / dt_o) via top eigvec."""
        Q = self.QD if masked else self.Q
        val, v = self.pencil_max(t, masked)
        u = self.sqrtG * v            # vector s.t. lam = u^T K u with K-form
        g = np.zeros(len(t))
        for si in range(len(self.slist)):
            W = np.tensordot(t, Q[si], axes=(0, 0))
            a = (u @ W) @ self.SVinv                      # dV
            # d/dt_o  u^T W SVinv W^T u = 2 a . (Q[si,o]^T u)
            g += 2.0 * np.tensordot(Q[si], u, axes=(1, 0)) @ a
        return val, g * self.fact

class FastSE:
    def __init__(self, n, lams=None, verbose=True):
        self.n = n
        self.cs = CosetSpace(n)
        self.orb_list, self.seen = self.cs.orbits()
        self.norb = len(self.orb_list)
        self.shift = {}
        for s in iperms(range(n)):
            h = hmap(s, n)
            self.shift[s] = np.array([self.seen[tuple(h[v] for v in l)]
                                      for l in self.cs.ell])
        self.mask0 = np.array([1.0 if l[0] != 0 else 0.0 for l in self.cs.ell])
        if lams is None:
            lams = list(partitions(2 * n))
        self.fl = []
        t0 = time.time()
        for lam in lams:
            ld = LambdaData(lam, n, self.cs)
            if ld.dV == 0: continue
            self.fl.append(FastLambda(n, lam, self.cs, self.shift, self.mask0))
            if verbose:
                print(f"  lam {lam} d={self.fl[-1].d} ready "
                      f"({time.time()-t0:.0f}s)", flush=True)

    def norms(self, t):
        A = max(f.pencil_max(t)[0] for f in self.fl)
        B = max(f.pencil_max(t, True)[0] for f in self.fl)
        return A, B

    def detail(self, t):
        return {f.lam: (math.sqrt(max(f.pencil_max(t)[0], 0)),
                        math.sqrt(max(f.pencil_max(t, True)[0], 0)))
                for f in self.fl}

def optimize(fs, iters=200, seed=0, t0=None, lr=0.15, softmax_T=200.0):
    """Subgradient ascent on log lam_max(K) - log lam_max(K_D), softmax over
       lambdas for smoothness near degeneracy."""
    rng = np.random.default_rng(seed)
    t = np.array(t0, float) if t0 is not None else rng.standard_normal(fs.norb)
    best = (-1, None)
    for it in range(iters):
        vals, grads, valsD, gradsD = [], [], [], []
        for f in fs.fl:
            v, g = f.grad_max(t); vals.append(v); grads.append(g)
            v2, g2 = f.grad_max(t, True); valsD.append(v2); gradsD.append(g2)
        vals, valsD = np.array(vals), np.array(valsD)
        A, B = vals.max(), valsD.max()
        r = math.sqrt(A / B)
        if r > best[0]: best = (r, t.copy())
        # softmax weights
        wA = np.exp(softmax_T * (vals / A - 1)); wA /= wA.sum()
        wB = np.exp(softmax_T * (valsD / B - 1)); wB /= wB.sum()
        gA = sum(w * g for w, g in zip(wA, grads)) / A
        gB = sum(w * g for w, g in zip(wB, gradsD)) / B
        g = gA - gB
        t = t + lr * g / (np.linalg.norm(g) + 1e-12)
        t /= np.linalg.norm(t)
        if it % 20 == 0:
            print(f"  it {it}: ratio {r:.8f}", flush=True)
    print(f"  best ratio {best[0]:.8f}")
    return best[1], best[0]

def cut_matrix(f, t, masked=True):
    """PSD cut M_cut with t'^T M_cut t' = v^T M(t') v, v = top eigvec at t."""
    val, v = f.pencil_max(t, masked)
    Q = f.QD if masked else f.Q
    gv = f.sqrtG * v
    norb = Q.shape[1]
    Mc = np.zeros((norb, norb))
    for si in range(Q.shape[0]):
        # Q[si] shape (norb, d, dV); contract over d:
        y = np.einsum("odk,d->ok", Q[si], gv)
        Mc += y @ f.SVinv @ y.T
    return val, Mc * f.fact

def barrier_lp(b, cuts, R=50.0, iters=80):
    """max b^T t  s.t.  t^T M_j t <= 1  (plus ||t||<=R), log-barrier Newton."""
    nvar = len(b)
    cuts = list(cuts) + [np.eye(nvar) / (R * R)]
    t = np.zeros(nvar)
    kappa = 1.0
    for outer in range(30):
        for _ in range(iters):
            g = -kappa * b
            H = np.zeros((nvar, nvar))
            for M in cuts:
                Mt = M @ t
                s = 1.0 - t @ Mt
                if s <= 1e-12:
                    s = 1e-12
                g += (2.0 / s) * Mt
                H += (2.0 / s) * M + (4.0 / (s * s)) * np.outer(Mt, Mt)
            try:
                dt = np.linalg.solve(H + 1e-12 * np.eye(nvar), -g)
            except np.linalg.LinAlgError:
                dt = -g
            # line search to stay strictly feasible
            step = 1.0
            for _ in range(60):
                t2 = t + step * dt
                if all(t2 @ M @ t2 < 1.0 - 1e-13 for M in cuts):
                    break
                step *= 0.5
            else:
                break
            t = t + step * dt
            if np.linalg.norm(step * dt) < 1e-12:
                break
        kappa *= 4.0
        if kappa > 1e9:
            break
    return t

def kelley(fs, b0, tol=1e-7, max_outer=120, verbose=True):
    cuts = []
    t = None
    for outer in range(max_outer):
        t = barrier_lp(b0, cuts)
        # true constraint check
        worst, worst_f = 0.0, None
        vals = []
        for f in fs.fl:
            val, _ = f.pencil_max(t, True)
            vals.append(val)
            if val > worst:
                worst, worst_f = val, f
        obj = float(b0 @ t)
        if verbose and outer % 5 == 0:
            print(f"  outer {outer}: obj {obj:.8f} worst {worst:.6f} cuts {len(cuts)}",
                  flush=True)
        if worst <= 1.0 + tol:
            print(f"  converged: obj {obj:.8f} (outer {outer}, cuts {len(cuts)})")
            return t, obj
        # add cuts for all lambdas within 1e-3 of worst
        for f, val in zip(fs.fl, vals):
            if val > max(1.0, worst - 1e-3):
                _, Mc = cut_matrix(f, t, True)
                # normalize cut so that t^T Mc t = val  (it already is)
                cuts.append(Mc)
    print("  kelley: max_outer reached")
    return t, float(b0 @ t)

def trivial_form(n, fs):
    """Exact linear form b0[o] = trivial-block value of delta_o, as floats."""
    from mdh_blocks import BlockEngine
    eng = BlockEngine(n, (2 * n,), fs.cs)
    B, mY, mN, ex = eng.orbit_blocks((n,), (n,), (fs.orb_list, fs.seen),
                                     variant="full")
    return np.array([float(B[o][0][0]) for o in range(fs.norb)])

if __name__ == "__main__":
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("--n", type=int, default=2)
    ap.add_argument("--output", type=Path, help="Optional new NumPy file; no file is written by default.")
    a = ap.parse_args()
    if a.output and a.output.exists():
        ap.error(f"refusing to overwrite {a.output}")
    fs = FastSE(a.n)
    if a.n == 2:
        t = [-0.15557435818700016, 0.023236606051669776, -0.005546146781492218,
             0.019767013115002303, -0.4137944380063479]
        A, B = fs.norms(t)
        print("n=2 anchor:", math.sqrt(A), math.sqrt(B), math.sqrt(A / B))
    b0 = trivial_form(a.n, fs)
    print("b0 =", b0)
    best = (-1, None)
    for sgn in [+1, -1]:
        print(f"kelley sign {sgn}:")
        t, obj = kelley(fs, sgn * b0)
        if obj > best[0]:
            best = (obj, t)
    obj, t = best
    A, B = fs.norms(t)
    print(f"\nFINAL n={a.n}: sigma0 = {obj:.8f}  ||Gamma|| = {math.sqrt(A):.8f} "
          f"||GoD|| = {math.sqrt(B):.8f}  ratio = {math.sqrt(A/B):.8f}")
    print("per-lambda (sigma, sigmaD):")
    for lam, (s1, s2) in fs.detail(t).items():
        print(f"  {lam}: {s1:.7f} {s2:.7f}")
    if a.output:
        a.output.parent.mkdir(parents=True, exist_ok=True)
        with a.output.open("xb") as stream:
            np.save(stream, t)
