# Flagged-erasure damping: exact variational gate

Date: 2026-08-30

Status: proposer-side elementary derivation; no independent review.

All logarithms are base two.

## Wrapper

For a channel `N` and `0<=p<=1`, define the visibly flagged erasure wrapper

\[
 \mathsf E_p[N](\rho)
 =p\,|1\rangle\!\langle1|\otimes N(\rho)
 +(1-p)|0\rangle\!\langle0|\otimes |e\rangle\!\langle e|\operatorname{Tr}\rho,
\]

where the two flag sectors are orthogonal and the erasure output is pure. This is the most direct
version of the noise/flag proposal in `HEXT.noise-flag-damping`.

Write `h_2(p)` for binary entropy.

## Exact one-shot side entropy

For every input state,

\[
 S(\mathsf E_p[N](\rho))=h_2(p)+pS(N(\rho)).
\]

Consequently

\[
 \boxed{S_{\min}(\mathsf E_p[N])=h_2(p)+pS_{\min}(N).}
\tag{1}
\]

## The cross defect is at most bilinear

Let

\[
 \Delta(N,M)=S_{\min}(N)+S_{\min}(M)-S_{\min}(N\otimes M).
\]

For an arbitrary joint input `rho_AB`, the four visible flag sectors give

\[
\begin{aligned}
 S((\mathsf E_p[N]\otimes\mathsf E_q[M])(\rho))
 ={}&h_2(p)+h_2(q)\\
 &+p(1-q)S(N(\rho_A))+(1-p)qS(M(\rho_B))\\
 &+pqS((N\otimes M)(\rho)).
\end{aligned}
\tag{2}
\]

Replacing every branch entropy by its corresponding global minimum and using (1) yields

\[
 \boxed{\Delta(\mathsf E_p[N],\mathsf E_q[M])\le pq\,\Delta(N,M).}
\tag{3}
\]

There is also a matching witness lower bound with explicit marginal penalties. If `psi` minimizes
`S_min(N tensor M)` and

\[
 d_N(\psi)=S(N(\psi_A))-S_{\min}(N),\qquad
 d_M(\psi)=S(M(\psi_B))-S_{\min}(M),
\]

then evaluating (2) on `psi` gives

\[
\begin{aligned}
 \Delta(\mathsf E_p[N],\mathsf E_q[M])
 \ge{}&pq\Delta(N,M)\\
 &-p(1-q)d_N(\psi)-(1-p)q d_M(\psi).
\end{aligned}
\tag{4}
\]

Thus the cross gap is exactly `pq Delta` when a joint minimizing witness also has side-minimizing
marginals. In general it can be damped even more strongly.

## Exact all-copy thinning functional

For `r` uses, the receiver sees the random surviving set `A subseteq [r]`. For a pure input `psi`
on all `r` inputs, block-diagonal entropy gives the exact identity

\[
\begin{aligned}
 S(\mathsf E_p[N]^{\otimes r}(\psi))
 ={}&r h_2(p)\\
 &+\sum_{A\subseteq[r]}p^{|A|}(1-p)^{r-|A|}
 S\!\left(N^{\otimes A}(\psi_A)\right).
\end{aligned}
\tag{5}
\]

Define

\[
 \mathcal F_p(N)=
 \inf_{r\ge1}\frac1r\min_{\psi}
 \sum_{A\subseteq[r]}p^{|A|}(1-p)^{r-|A|}
 S\!\left(N^{\otimes A}(\psi_A)\right).
\tag{6}
\]

Subadditivity and (5) show

\[
 \boxed{\overline S_{\min}(\mathsf E_p[N])=h_2(p)+\mathcal F_p(N).}
\tag{7}
\]

This formula is the exact mathematical object that a successful erasure-damping proof must
control. It cannot be replaced by a calculation at two or three copies.

## Universal bounds are not a rate separation

Let `a_k=S_min(N^tensor k)` and `a_0=0`. Equation (5) gives for every input

\[
 S(\mathsf E_p[N]^{\otimes r}(\psi))
 \ge r h_2(p)+\mathbb E[a_{K_r}],
 \qquad K_r\sim\operatorname{Binomial}(r,p).
\]

Since `a_k/k -> overline S_min(N)` and `0<=a_k<=k log d_B`, dominated convergence gives

\[
 \mathcal F_p(N)\ge p\overline S_{\min}(N).
\tag{8}
\]

A product of one-shot minimizers gives

\[
 \mathcal F_p(N)\le pS_{\min}(N).
\tag{9}
\]

For the absolute self-regularization loss

\[
 \ell_N=S_{\min}(N)-\overline S_{\min}(N),
\]

(7)--(9) imply only

\[
 0\le \ell_{\mathsf E_p[N]}
 =pS_{\min}(N)-\mathcal F_p(N)
 \le p\ell_N.
\tag{10}
\]

The cross advantage has the bilinear upper bound `pq Delta`, while the generic leakage allowance
in (10) is linear in `p` or `q`. Therefore these universal inequalities cannot certify a rate
separation that was absent before wrapping. Indeed, if

\[
 \Delta(N,M)\le\ell_N+\ell_M,
\]

then for every `p,q<=1`,

\[
 pq\Delta(N,M)\le p\ell_N+q\ell_M.
\tag{11}
\]

Equation (11) is a proof-method obstruction, not a bound on the true wrapped leakages: the exact
quantities in (10) may be much smaller than their linear upper bounds.

## Exact revival condition

The flagged-erasure route becomes substantive only after proving a channel-specific estimate of
the form

\[
 pS_{\min}(N)-\mathcal F_p(N)
 +qS_{\min}(M)-\mathcal F_q(M)
 <\Delta(\mathsf E_p[N],\mathsf E_q[M]),
\tag{12}
\]

with the right-hand side bounded below using (4) or a better witness. For the product-Haar blocks,
this requires control over all random surviving marginals of one many-copy input, not merely the
known fixed-depth strong-convergence estimate.

Thus simple visible erasure does not by itself solve self-leakage. It converts the open problem
into the explicit thinning functional (6), which is the precise revival target for this route.
