# A universal one-bit cap for an isotropic conjugate-Bell certificate

Date: 2026-08-30

Status: proposer-side elementary theorem; independent review pending.

All logarithms are base two.

## Theorem

Let `Phi:M_d -> M_k` be a finite-dimensional quantum channel, let `bar(Phi)` be its
entrywise-conjugate channel in the bases used to define the maximally entangled state, and suppose

\[
 Z=(\Phi\otimes\overline\Phi)(\Omega_d)
   =r\Omega_k+(1-r)\frac{I_{k^2}}{k^2},\qquad 0\le r\le1.
\tag{1}
\]

Write the spectrum of `Z` as

\[
 (\alpha,\underbrace{\beta,\ldots,\beta}_{k^2-1}),\qquad
 \alpha=r+\frac{1-r}{k^2},\quad \beta=\frac{1-r}{k^2}.
\tag{2}
\]

Then the minimum-output-entropy additivity defect certified by this Bell input satisfies

\[
 2S_{\min}(\Phi)-S(Z)\le1\ \text{bit}.
\tag{3}
\]

The same conclusion holds for a fixed-`k` limiting output body and limiting isotropic Bell state
when both arise as limits of finite channels. Consequently every LLW limiting
conjugate-channel/Bell certificate is at most one bit, uniformly over every admissible `k,t` and
therefore over every sequence `t=t_k`.

This is a cap on the **isotropic Bell certificate**, not on arbitrary inputs, arbitrary channel
pairs, or tensor products of several nonidentical isotropic layers.

## 1. Measuring one Bell-output leg creates a legal one-channel output

Measure the first `k`-dimensional output of `Z` in the basis containing `|x>`. Equation (1) has
maximally mixed marginals, so the outcome probability is `1/k`. The normalized conditional state
on the second output is

\[
 \tau_x=r|\bar x\rangle\langle\bar x|+(1-r)\frac{I_k}{k}.
\tag{4}
\]

This conditional state is not merely an abstract state with a convenient spectrum. The standard
maximally-entangled transpose identity gives

\[
 \operatorname{Tr}_{B}\!\left[(|x\rangle\langle x|\otimes I)
 (\Phi\otimes\overline\Phi)(\Omega_d)\right]
 =\frac1d\overline\Phi\!\left((\Phi^*(|x\rangle\langle x|))^T\right).
\tag{5}
\]

After division by its trace `1/k`, the operator entering `bar(Phi)` is a density matrix. Hence
`tau_x` is a genuine output of `bar(Phi)`. Conjugation preserves all output spectra and therefore

\[
 S_{\min}(\Phi)=S_{\min}(\overline\Phi)\le S(\tau_x).
\tag{6}
\]

The spectrum of `tau_x` is

\[
 (p,\underbrace{q,\ldots,q}_{k-1}),\qquad
 p=\alpha+(k-1)\beta=\frac{k\alpha+1}{k+1},\quad q=k\beta.
\tag{7}
\]

Put

\[
 H_k(s)=h_2(s)+(1-s)\log(k-1).
\tag{8}
\]

Then `S(tau_x)=H_k(p)` and

\[
 S(Z)=h_2(\alpha)+(1-\alpha)\log(k^2-1).
\tag{9}
\]

It remains only to prove a scalar entropy inequality.

## 2. Scalar entropy inequality

The physical range `0<=r<=1` is equivalent to `1/k^2<=alpha<=1`, and (7) gives `p>=alpha`.

### Case A: `alpha>=1/k`

The function `H_k(s)` decreases on `[1/k,1]`. Therefore `H_k(p)<=H_k(alpha)`, and

\[
\begin{aligned}
 2H_k(p)-S(Z)
 &\le 2H_k(\alpha)-S(Z)\\
 &=h_2(\alpha)+(1-\alpha)\log\frac{(k-1)^2}{k^2-1}\\
 &=h_2(\alpha)+(1-\alpha)\log\frac{k-1}{k+1}\\
 &\le h_2(\alpha)\le1.
\end{aligned}
\tag{10}
\]

### Case B: `1/k^2<=alpha<=1/k`

Here `H_k(p)<=log k`. The entropy deficit of the Bell spectrum from the uniform distribution is

\[
 D_k(\alpha)=2\log k-S(Z).
\tag{11}
\]

It is increasing for `alpha>=1/k^2`, since its derivative is

\[
 D_k'(\alpha)=\log\frac{\alpha(k^2-1)}{1-\alpha}\ge0.
\tag{12}
\]

At the endpoint,

\[
 D_k(1/k)=\frac{\log k}{k}
 +(1-1/k)\log\frac{k}{k+1}
 \le\frac{\log k}{k}\le1.
\tag{13}
\]

Thus

\[
 2H_k(p)-S(Z)\le2\log k-S(Z)=D_k(\alpha)\le1.
\tag{14}
\]

Equations (6), (10), and (14) prove (3).

## 3. Passage to LLW limiting output bodies

For every fixed admissible `k,t`, LLW Theorem 4.1 gives convergence of the finite Bell output to
an isotropic state of the form (1), while Theorem 3.1 gives Hausdorff convergence of the
one-channel output set to `K_{k,t}`. Apply the one-leg measurement above before taking the limit.
Because the outcome probability tends to `1/k`, the normalized conditional outputs converge to
`tau_x`; closedness and Hausdorff convergence imply `tau_x in K_{k,t}`. Hence

\[
 2\min_{\sigma\in K_{k,t}}S(\sigma)
 -S(\lambda^{\mathrm{Bell}}_{k,t})\le1
\tag{15}
\]

for every fixed admissible `k,t`. The bound is independent of both parameters, so it remains true
along an arbitrary sequence `t=t_k in (1/k^2,1)` without importing LLW's fixed-`t` large-`k`
expansion outside its quantifiers.

The quantifier order here is the one supplied by LLW: for each chosen finite `k,t_k`, first take
the auxiliary projection dimension to infinity and pass to the limiting body, and only then vary
`k`. No rate-uniform assertion is made for an uncontrolled simultaneous finite sequence
`k,n(k)->infinity`.

The earlier direct calculation at `t=c/k^2` remains useful because it gives the sharper asymptotic
cap `h_2(1/c)` and displays the matching-spike cancellation explicitly. Equation (15) closes the
previously open uniform-boundary gate.

## 4. Scope and consequence

The proof uses two special features simultaneously:

1. the tested input is the maximally entangled input for a channel and its conjugate; and
2. the resulting output is isotropic.

It does not bound an optimized joint input whose output is not isotropic. It also does not apply
to a product of distinct isotropic layers as though that product were itself isotropic. Such a
product can accumulate up to a constant contribution per layer, which is compatible with the
separate finite-dimensional absolute-unbounded construction in this project.

Primary source used for the LLW specialization:

- Debbie Leung, Benjamin Lovitz, Peixue Wu, arXiv:2607.15210v1, Theorem 3.1 and Corollary 3.2
  (limiting output body), Theorem 4.1 and Corollary 4.2 (limiting isotropic Bell output).
- Local PDF: `holevo-extensive-violation/artifacts/primary-sources/leung-lovitz-wu-2607.15210.pdf`.
- SHA-256: `688f09cb2a6800b4cfe290da80e26e6561b0144493ba94693f518c582164a5e0`.
