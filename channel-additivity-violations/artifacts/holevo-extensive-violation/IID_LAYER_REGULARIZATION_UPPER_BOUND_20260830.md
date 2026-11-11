# Arbitrary fixed-dimensional heterogeneous layers expose fixed-channel regularization

Date: 2026-08-30

Status: proposer-side proof; independent review pending.

All logarithms are base two.

## Statement

Let `X` be a compact metric space, let `mu` be a Borel probability measure on `X`, and let

\[
 x\longmapsto\Phi_x:M_a\longrightarrow M_b
\]

be diamond-norm continuous.  Let `X_1,X_2,...` be iid with law `mu`, and define the heterogeneous
product channel

\[
 L_J=\Phi_{X_1}\otimes\cdots\otimes\Phi_{X_J}.
\]

Then, almost surely,

\[
 \boxed{
 \limsup_{J\to\infty}\frac1J S_{\min}(L_J)
 \le \int_X \overline S_{\min}(\Phi_x)\,d\mu(x),}
\tag{1}
\]

where

\[
 \overline S_{\min}(\Phi_x)
 :=\lim_{r\to\infty}\frac1rS_{\min}(\Phi_x^{\otimes r}).
\]

More generally, no randomness or genericity is needed for the model-independent consequence. For
**every deterministic sequence** `x_1,x_2,...` in `X`,

\[
 \boxed{
 \limsup_{J\to\infty}\frac1J
 S_{\min}(\Phi_{x_1}\otimes\cdots\otimes\Phi_{x_J})
 \le \sup_{x\in X}\overline S_{\min}(\Phi_x).}
\tag{1a}
\]

If the empirical measures `J^{-1}sum_{j<=J} delta_{x_j}` converge weakly to `mu`, then the sharper
right-hand side in (1) holds deterministically. The iid theorem is the almost-sure special case.

## Proof for a fixed block length

Fix `r>=1`.  Put

\[
 f_r(x)=S_{\min}(\Phi_x^{\otimes r}).
\]

The map `f_r` is continuous.  Indeed, a telescoping product estimate gives

\[
 \|\Phi_{x_1}\otimes\cdots\otimes\Phi_{x_r}
   -\Phi_y^{\otimes r}\|_\diamond
 \le\sum_{t=1}^r\|\Phi_{x_t}-\Phi_y\|_\diamond,
\tag{2}
\]

and the Fannes--Audenaert inequality on output dimension `b^r` makes the optimized minimum output
entropy uniformly continuous.

Choose a finite Borel partition `P_delta` of `X` into continuity cells small enough that every
`r`-fold product of channels from one cell is within a prescribed entropy error `omega_r(delta)`
of `f_r(x_C)`, for a representative `x_C` of that cell.  Boundaries can be chosen to have
`mu`-measure zero.

Within each cell `C`, group the sampled indices into disjoint blocks of exactly `r`; fewer than `r`
indices per cell remain ungrouped.  For each full group, use an input which minimizes
`Phi_{x_C}^{tensor r}`.  Equation (2) and entropy continuity show that the corresponding actual
heterogeneous output has entropy at most

\[
 f_r(x_C)+\omega_r(\delta).
\]

Use the tensor product of all these group inputs, and arbitrary pure inputs for the finitely many
ungrouped indices.  Output entropy is additive for this chosen product across groups.  Since the
number of cells is fixed and each leftover output entropy is at most `log b`, the leftover
contribution is `o(J)`.

The strong law gives `N_C(J)/J -> mu(C)` simultaneously for the finite partition.  Hence almost
surely

\[
 \limsup_{J\to\infty}\frac1J S_{\min}(L_J)
 \le \sum_{C\in P_\delta}\frac{\mu(C)}r f_r(x_C)
      +\frac{\omega_r(\delta)}r.
\tag{3}
\]

Refining a fixed countable sequence of partitions with mesh tending to zero, and intersecting the
corresponding probability-one events, gives

\[
 \limsup_{J\to\infty}\frac1J S_{\min}(L_J)
 \le\frac1r\int_X f_r(x)\,d\mu(x)
\tag{4}
\]

for every integer `r` simultaneously.

## Passage to the regularized rate

For every `x`, subadditivity of `S_min(Phi_x^{tensor r})` gives

\[
 \frac{f_r(x)}r\longrightarrow\overline S_{\min}(\Phi_x).
\]

Moreover `0<=f_r(x)/r<=log b`.  Dominated convergence therefore yields

\[
 \lim_{r\to\infty}\frac1r\int_X f_r(x)\,d\mu(x)
 =\int_X\overline S_{\min}(\Phi_x)\,d\mu(x).
\]

Taking `r->infinity` in (4) proves (1).

## Removal of the iid assumption

Let `x_1,x_2,...` be arbitrary and write

\[
 \nu_J=\frac1J\sum_{j=1}^J\delta_{x_j}.
\]

First suppose `nu_J` converges weakly to `mu`. For each fixed block length `r`, choose the finite
small-mesh partition in the preceding proof with `mu`-null cell boundaries. Weak convergence then
gives `N_C(J)/J -> mu(C)` for every cell. Nothing else in the grouping argument used independence,
so (3)--(4), dominated convergence, and therefore (1) hold verbatim.

For a completely arbitrary sequence, choose a subsequence `J_l` along which the entropy rates
converge to their global limsup. Compactness of the probability measures on compact `X` gives a
further subsequence, not relabeled, for which `nu_{J_l}` converges weakly to some probability
measure `mu`. Apply the preceding deterministic empirical-limit statement along that subsequence:

\[
\begin{aligned}
 \limsup_{J\to\infty}\frac1J S_{\min}(L_J)
 &=\lim_{l\to\infty}\frac1{J_l}S_{\min}(L_{J_l})\\
 &\le\int_X\overline S_{\min}(\Phi_x)\,d\mu(x)\\
 &\le\sup_{x\in X}\overline S_{\min}(\Phi_x).
\end{aligned}
\]

This proves (1a).

## Consequence for an oriented layer ensemble

Conditioning or otherwise orienting a Haar-like distribution so that its support stays away from
its entrywise conjugate can evade the particular approximate-conjugate matching in
`FIXED_DIMENSION_CONJUGATE_COLLISION_OBSTRUCTION_20260830.md`.  It does not, however, create a new
independent amplification principle.

At fixed local dimensions, every sufficiently long sequence contains many near-repetitions after
partitioning the compact parameter space into finitely many small cells. Grouping those
repetitions into `r`-blocks exposes fixed-channel regularization exactly as above. For an empirical
limit `mu`, any lower bound claimed for the heterogeneous side must be compatible with

\[
 \int\overline S_{\min}(\Phi_x)d\mu(x),
\]

not merely with the average one-shot entropy.  In particular, if the desired side rate exceeds
this integral, the oriented hierarchy fails. Without an empirical limit, the rate is still at most
the best regularized rate of any one channel in the compact family. Proving that this supremum is
high requires control of exactly the fixed-channel self-regularization loss that heterogeneity was
meant to avoid.

For the product-random-unitary setting one may apply the lemma to the complementary channels
`Phi_U^c:M_D->M_m`, which form a continuous fixed-output-dimensional family and have the same
minimum output entropies, including at every tensor power, as the original channels.

## Scope

Equations (1) and (1a) are upper bounds obtained from specific regrouped inputs. They do not assert
matching lower bounds and therefore do not evaluate heterogeneous product entropy exactly. They
show that random, oriented, adaptive, or deterministic fixed-dimensional heterogeneity cannot by
itself bypass the fixed-channel regularization problem.

## External inputs

- Fannes--Audenaert entropy continuity: Theorem 1 of
  `holevo-extensive-violation/artifacts/primary-sources/audenaert-0610146.pdf`.
- The strong law of large numbers for the finitely many cell-indicator variables of each fixed
  partition.
