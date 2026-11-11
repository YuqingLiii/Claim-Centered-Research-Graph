# Depolarizing Gram channels: a small-input Bell no-go theorem

Date: 2026-08-30

Status: proposer-side finite-dimensional theorem; independent review pending.

All logarithms are base two. Hilbert--Schmidt adjoints are denoted by a star.

## Theorem

Let `Phi:M_d->M_k` be a quantum channel satisfying

\[
 \Phi(I_d/d)=I_k/k,
\tag{1}
\]

and suppose its Gram channel is depolarizing:

\[
 T:=\frac{k}{d}\Phi\Phi^*=\Delta_t,
 \qquad
 \Delta_t(X)=tX+(1-t)\operatorname{Tr}(X)\frac{I_k}{k},
 \qquad 0\le t\le1.
\tag{2}
\]

If `d<=k`, then for the conjugate-Bell output

\[
 Z=(\Phi\otimes\bar\Phi)(\Omega_d)
\tag{3}
\]

one has

\[
 \boxed{
 2\overline S_{\min}(\Phi)
 \le 2S_{\min}(\Phi)
 \le S(Z).}
\tag{4}
\]

Consequently no depolarizing Gram factor with input dimension at most its output dimension can
produce a positive fixed-channel conjugate-Bell regularized defect. For qutrit output, every
surviving depolarizing-Gram Bell candidate must therefore have input dimension at least four.

The theorem is specific to the maximally entangled Bell witness and to a depolarizing Gram
channel. It is not a no-go theorem for general qutrit Gram channels or for non-Bell collective
inputs.

## 1. Exact Haar-average output purity

For a Haar-random pure input `psi`, the two-copy identity

\[
 \mathbb E_\psi\,\psi^{\otimes2}=\frac{I+F_d}{d(d+1)}
\tag{5}
\]

gives

\[
 \mathbb E_\psi\operatorname{Tr}\Phi(\psi)^2
 =\frac{
   \operatorname{Tr}\Phi(I_d)^2+operatorname{Tr}_{\rm HS}(\Phi\Phi^*)
 }{d(d+1)}.
\tag{6}
\]

Equation (1) gives `Phi(I_d)=dI_k/k`, while (2) gives

\[
 \operatorname{Tr}_{\rm HS}(\Phi\Phi^*)
 =\frac{d}{k}\operatorname{Tr}_{\rm HS}(\Delta_t)
 =\frac{d}{k}\bigl(1+(k^2-1)t\bigr).
\tag{7}
\]

Therefore

\[
 \boxed{
 \mathbb E_\psi\operatorname{Tr}\Phi(\psi)^2
 =\frac1k+\frac{(k^2-1)t}{k(d+1)}.}
\tag{8}
\]

If `d<=k`, some pure input `psi_0` consequently satisfies

\[
 \operatorname{Tr}\Phi(\psi_0)^2
 \ge \frac1k+\frac{(k-1)t}{k}.
\tag{9}
\]

The right side is exactly the purity of a pure-state output of the depolarizing channel
`Delta_{sqrt(t)}`.

## 2. Entropy extremizer at fixed purity

The following elementary form of the sharp entropy/index-of-coincidence bound is used.

**Lemma.** Let `rho` be a `k`-dimensional state and suppose

\[
 \operatorname{Tr}\rho^2\ge \frac1k+\frac{k-1}{k}s^2,
 \qquad 0\le s\le1.
\tag{10}
\]

Then

\[
 S(\rho)\le H_k(s),
\tag{11}
\]

where

\[
 H_k(s)=H\left(
 \frac{1+(k-1)s}{k},
 \underbrace{\frac{1-s}{k},\ldots,\frac{1-s}{k}}_{k-1}
 \right).
\tag{12}
\]

**Proof.** Fix a collision value `c` in `[1/k,1]` and maximize Shannon entropy over probability
vectors with collision probability at least `c`. Compactness gives a maximizer. Unless `c=1/k`,
mixing any vector of collision strictly larger than `c` with the uniform vector increases entropy
and continuously lowers collision to `c`; hence the maximum lies at exact collision `c`.

For `1/k<c<1`, a maximizer has full support. Indeed, if one component were zero, inserting a new
component of size `epsilon` and adjusting two positive components to preserve normalization and
collision produces an `epsilon log(1/epsilon)` entropy gain while all compensating changes are
only `O(epsilon)`. The constraint gradients are then independent, so the Lagrange equations imply
that the positive components take at most two values `a>b`: the equation

\[
 -(\log p_i+1)=\alpha+2\beta p_i
\tag{13}
\]

has at most two positive solutions. If the larger value occurred at least twice, the tangent
variation `(1,-1,0,...)` between two such components would preserve both constraints to first
order. Subtracting the two stationarity equations gives

\[
 -2\beta=\frac{\log(a/b)}{a-b}.
\tag{14}
\]

The constrained Lagrangian Hessian on that tangent direction has coefficient

\[
 -\frac1a-2\beta
 =-\frac1a+\frac{\log(a/b)}{a-b}>0,
\tag{15}
\]

because `log r>1-1/r` for `r>1`. This contradicts the second-order necessary condition for a
maximum. Thus the larger value occurs exactly once and the remaining `k-1` values are equal.
Solving normalization and collision gives

\[
 a=\frac{1+\sqrt{(k-1)(kc-1)}}{k},
 \qquad
 b=\frac{1-\sqrt{(kc-1)/(k-1)}}{k}.
\tag{16}
\]

The endpoint cases follow by continuity. Substituting
`c=1/k+(k-1)s^2/k` gives (12), proving the lemma. This is also the upper arc of the exact
entropy/index-of-coincidence diagram of Harremoes and Topsoe, Theorem 2.5(i), but the argument
above makes the present use self-contained.

Applying the lemma to (9), with `s=sqrt(t)`, yields

\[
 S_{\min}(\Phi)\le S(\Phi(\psi_0))\le H_k(\sqrt t).
\tag{17}
\]

## 3. The Bell output is bounded from below by strong depolarizing additivity

The Gram/realignment identity identifies `Z`, up to a fixed swap/transposition convention, with
the normalized Choi state of `T=Delta_t`. Since depolarizing contractions compose
multiplicatively,

\[
 \Delta_t=\Delta_{\sqrt t}\circ\Delta_{\sqrt t},
\tag{18}
\]

and therefore

\[
 Z\simeq J(\Delta_t)
 =(\Delta_{\sqrt t}\otimes\overline{\Delta_{\sqrt t}})(\Omega_k).
\tag{19}
\]

King's arbitrary-dimension depolarizing theorem states that for every channel `Psi`,

\[
 S_{\min}(\Delta_s\otimes\Psi)
 =S_{\min}(\Delta_s)+S_{\min}(\Psi).
\tag{20}
\]

Using `Psi=overline{Delta_{sqrt(t)}}` and the fact that every pure-state output of a depolarizing
channel has entropy `H_k(sqrt(t))`, equation (19) gives

\[
 S(Z)\ge
 S_{\min}(\Delta_{\sqrt t}\otimes\overline{\Delta_{\sqrt t}})
 =2H_k(\sqrt t).
\tag{21}
\]

Combining (17) and (21) proves

\[
 2\overline S_{\min}(\Phi)
 \le2S_{\min}(\Phi)
 \le2H_k(\sqrt t)
 \le S(Z),
\tag{22}
\]

which is (4).

## 4. Research consequence

The positive entanglement-cost surplus of a depolarizing Gram channel is not sufficient to create
a Bell gap when the factor input is no larger than the output. The obstruction is exact: the same
depolarizing square root that lower-bounds the Bell entropy also gives the sharp fixed-purity
entropy benchmark forced on some factor output by the Gram identity.

For the first surviving output dimension `k=3`, the depolarizing branch is now reduced from all
rectangular factors to the genuinely oversized regime

\[
 d\ge4.
\tag{23}
\]

The next live question is whether complete positivity and the exact depolarizing frame equations
impose a stronger low-entropy output bound in this oversized regime, or whether an `M_d->M_3`
factor with `d>=4` can evade (22).

## Primary-source audit

- Christopher King, *The capacity of the quantum depolarizing channel*, arXiv:quant-ph/0204172,
  Theorem 3, page 8: arbitrary-partner multiplicativity and minimum-output-entropy additivity for
  the `d`-dimensional depolarizing channel.
- Peter Harremoes and Flemming Topsoe, *Inequalities between entropy and index of coincidence
  derived from information diagrams*, IEEE Transactions on Information Theory 47 (2001),
  Theorem 2.5(i): the same sharp upper entropy curve used in Section 2. The present artifact also
  supplies a direct proof.

Local primary source:
`artifacts/primary-sources/king-depolarizing-additivity-quant-ph-0204172.pdf`, SHA-256
`f7e098a10363b3d10b4123ea2ba488adce00b565248e4ea8d1f227e589ca5b60`.

