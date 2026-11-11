# LLW critical scaling `t=c/k^2`: logarithmic terms cancel and the Bell certificate stays at most one bit

Date: 2026-08-30

Status: proposer-side asymptotic derivation from the exact LLW output body and Bell spectrum;
independent review pending.

All logarithms in this note are base two.  Leung--Lovitz--Wu (LLW) use natural logarithms; changing
base multiplies every entropy consistently and does not affect the comparisons.

## Why this scaling needs a separate audit

LLW prove, for fixed `t in (0,1)` and `k->infinity`, that the one-channel and Bell-output entropy
deficits are of order `k^-2`.  Their Appendix B explicitly fixes `t` before taking `k` large.
Those expansions cannot be substituted into a family with `t=t_k` approaching the lower
admissible boundary `1/k^2`.

The potentially dangerous scaling is

\[
 t_k=\frac{c}{k^2},\qquad c>1\ \text{fixed}.
\tag{1}
\]

In this regime the exceptional eigenvalue of the conjugate-pair Bell output tends to `1/c`, so its
entropy lies below `2 log k` by order `log k`.  Taken alone, that looks like a possible full-size
violation.  The exact output-body constraint shows that a one-channel output develops a matching
spike, and the logarithmic terms cancel.

Primary source:

- Debbie Leung, Benjamin Lovitz, Peixue Wu, *Counterexamples to additivity of minimum output
  p-Renyi entropy of quantum channels for all p>3/4 and 0<=p<1/4*, arXiv:2607.15210v1.
- Local copy: `holevo-extensive-violation/artifacts/primary-sources/leung-lovitz-wu-2607.15210.pdf`.
- SHA-256: `688f09cb2a6800b4cfe290da80e26e6561b0144493ba94693f518c582164a5e0`.
- Imported statements: Theorem 3.1 and Corollary 3.2 (limiting one-channel output body), Theorem
  4.1 and Corollary 4.2 (limiting Bell output).

## 1. Exact LLW output body

For fixed `k` and `t>1/k^2`, LLW identify the limiting eigenvalue body as normalized vectors

\[
 \lambda_i=\frac{u_i}{\sum_j u_j},\qquad u\in\mathscr D_{k,t},
\]

where

\[
 \mathscr D_{k,t}
 =\left\{u\in[0,1]^k:
 \sum_{i=1}^k c_t(u_i)\le\frac1k\right\},
\tag{2}
\]

and

\[
 c_t(u)=\left(\sqrt{t(1-u)}-\sqrt{u(1-t)}\right)^2.
\tag{3}
\]

Write

\[
 t=\sin^2\theta,\qquad u=\sin^2\phi.
\]

Then the constraint has the exact angular form

\[
 c_t(u)=\sin^2(\phi-\theta).
\tag{4}
\]

## 2. A feasible one-channel spectrum at the critical scale

Let `e=(1,...,1)/sqrt(k)` and let

\[
 w_k=\frac{e_1-k^{-1/2}e}{\sqrt{1-1/k}},
\]

so `e` and `w_k` are orthonormal.  Put

\[
 \delta^{(k)}=-\frac1{\sqrt c}e+\sqrt{1-\frac1c}\,w_k.
\tag{5}
\]

Thus `||delta^(k)||_2=1`.  With `theta_k=arcsin(sqrt(c)/k)`, define for every sufficiently large
`k`

\[
 \phi_i^{(k)}=\theta_k+arcsin\left(\frac{\delta_i^{(k)}}{\sqrt k}\right),
 \qquad
 u_i^{(k)}=\sin^2\phi_i^{(k)}.
\tag{6}
\]

The angles lie in `[0,pi/2]` because `c>1`.  Equations (4)--(6) give the constraint exactly:

\[
 \sum_i c_{t_k}(u_i^{(k)})
 =\sum_i\frac{(\delta_i^{(k)})^2}{k}=\frac1k.
\]

Hence `u^(k)` is a valid point of the LLW output body, not a formal Taylor candidate.

Let

\[
 \lambda_i^{(k)}=u_i^{(k)}/\sum_j u_j^{(k)}.
\]

The first coordinate of `delta^(k)` is `sqrt(1-1/c)+O(k^-1/2)` and all remaining coordinates are
`-1/(sqrt(c k))+O(k^-1)`.  Expanding (6) now gives

\[
 u_1^{(k)}=\frac{c-1}{ck}+O(k^{-3/2}),
\tag{7}
\]

\[
 u_i^{(k)}=\frac{(c-1)^2}{c k^2}+O(k^{-5/2})\quad(i>1),
\tag{8}
\]

and

\[
 \sum_i u_i^{(k)}=\frac{c-1}{k}+O(k^{-3/2}).
\tag{9}
\]

All `i>1` coordinates are equal.  Consequently

\[
 \lambda_1^{(k)}\longrightarrow\frac1c,
 \qquad
 \lambda_i^{(k)}=\frac{1-1/c}{k-1}+o(k^{-1})\quad(i>1),
\]

and the entropy of this feasible one-channel output is

\[
 S(\lambda^{(k)})
 =h_2(1/c)+(1-1/c)\log(k-1)+o(1).
\tag{10}
\]

Because the LLW one-channel quantity is a minimum over the entire output body,

\[
 \min_{\sigma\in\mathscr K_{k,t_k}}S(\sigma)
 \le S(\lambda^{(k)}).
\tag{11}
\]

## 3. Exact Bell spectrum at the same scale

LLW's limiting Bell output is isotropic.  Its exceptional-minus-flat parameter is

\[
 r_{k,t}=\frac{k^2(1-t)}{(k^2-1)^2t+1-t}.
\]

Substituting `t_k=c/k^2` gives `r_{k,t_k}->1/c`; the exceptional Bell eigenvalue also tends to
`1/c`, while the other `k^2-1` eigenvalues are equal.  Therefore

\[
 S(\lambda^{\mathrm{Bell}}_{k,t_k})
 =h_2(1/c)+(1-1/c)\log(k^2-1)+o(1)
\]

\[
 =h_2(1/c)+2(1-1/c)\log k+o(1).
\tag{12}
\]

## 4. Cancellation of the apparent extensive term

The asymptotic gap certified by the LLW Bell comparison is

\[
 G_k(c)=2\min_{\sigma\in\mathscr K_{k,t_k}}S(\sigma)
       -S(\lambda^{\mathrm{Bell}}_{k,t_k}).
\]

Using the feasible one-channel output (11), rather than assuming an unproved formula for the true
minimum, gives the rigorous upper estimate

\[
 G_k(c)
 \le 2S(\lambda^{(k)})-S(\lambda^{\mathrm{Bell}}_{k,t_k})
 =h_2(1/c)+o(1).
\tag{13}
\]

In particular,

\[
 \boxed{\limsup_{k\to\infty}G_k(c)\le h_2(1/c)\le1\ \text{bit}.}
\tag{14}
\]

The coefficient of `log k` is exactly zero.  The upper envelope is maximized at `c=2`, where
`h_2(1/2)=1` bit.  This recovers, at the level of the critical parameter geometry, why the familiar
projection/conjugate/Bell mechanism approaches one bit rather than an extensive fraction of the
output size.

Equation (14) is an upper bound on this **specific limiting-output-body plus Bell-witness
certificate**.  It is not a universal one-bit upper bound for arbitrary finite-dimensional channel
pairs, and it does not contradict the separate product-free-group construction of absolute
unbounded gaps.

## 5. Quantifier verdict

Three regimes must be kept distinct:

1. `t` fixed before `k->infinity`: LLW's published expansion gives a gap of order `k^-2`.
2. `t=c/k^2`, `c>1` fixed: the published fixed-`t` expansion is inapplicable, but the exact output
   body and Bell spectrum give the new bound (14).
3. arbitrary `t=t_k`: the present matching-spike calculation alone does not cover this case, but
   the subsequent steering theorem in `ISOTROPIC_BELL_ONE_BIT_CAP_20260830.md` gives a uniform
   one-bit cap for every admissible LLW `k,t` and therefore closes all such sequences.

Thus the most obvious dimension-paying scaling does not solve the Hayden--Penington problem. It
also exhibits the sharper limiting cap `h_2(1/c)`, while the later isotropic-steering argument
supersedes the former LLW boundary frontier. Other channel families and non-isotropic witnesses
remain outside both bounds.
