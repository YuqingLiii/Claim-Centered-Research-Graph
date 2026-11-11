# Fixed-output hierarchy: a full-size extensive obstruction

Date: 2026-08-29  
Status: proposer-side elementary dimension bound; independent review pending.

## Claim

Consider a hierarchy

\[
L_J=\Phi_1\otimes\cdots\otimes\Phi_J
\]

in which every primitive channel has the same fixed output dimension `k`. Then the actual
minimum-output-entropy additivity defect of `L_J` and its conjugate satisfies

\[
\boxed{\Delta_S(L_J,\overline{L_J})\le 2J\log_2 k.}
\]

Consequently, if the primitive environment dimensions `n_j` tend to infinity, this hierarchy
cannot have a defect extensive in the full input/output/environment qubit size, regardless of how
well the fixed-partner leakage is controlled.

## Proof of the universal upper bound

For channels `N` and `M`,

\[
\Delta_S(N,M)
=S_{\min}(N)+S_{\min}(M)-S_{\min}(N\otimes M).
\]

Entropy is nonnegative and an output on `d_B` dimensions has entropy at most `log_2 d_B`.
Therefore

\[
\Delta_S(N,M)\le \log_2 d_B(N)+\log_2 d_B(M).
\]

Here `d_B(L_J)=k^J` and conjugation preserves the output dimension, giving

\[
\Delta_S(L_J,\overline{L_J})\le 2\log_2(k^J)=2J\log_2 k.
\]

This is an upper bound on the **true optimized defect**, not merely a limitation of the known
tensor-product witness.

## Comparison with full channel cost

For the BCN layers used in the hierarchy, the primitive Stinespring dimensions have the form

\[
d_{A,j}=\Theta(k n_j),\qquad d_{B,j}=k,\qquad d_{E,j}=n_j
\]

with the aspect parameter fixed. Thus

\[
\log_2 d_A(L_J)=\sum_{j\le J}\log_2 n_j+O(J),
\]

\[
\log_2 d_E(L_J)=\sum_{j\le J}\log_2 n_j,
\qquad
\log_2 d_B(L_J)=J\log_2 k.
\]

Let `m_J` be either the maximum or the sum of these three logarithmic costs. Then

\[
m_J=\Theta\!\left(J+\sum_{j\le J}\log_2 n_j\right).
\]

Combining with the universal output bound,

\[
\frac{\Delta_S(L_J,\overline{L_J})}{m_J}
\le
O\!\left(\frac{J}{J+\sum_{j\le J}\log_2 n_j}\right).
\]

If `n_j -> infinity`, then `log n_j -> infinity`, so its Cesaro average also tends to infinity:

\[
\frac1J\sum_{j\le J}\log_2 n_j\longrightarrow\infty.
\]

Hence

\[
\boxed{\Delta_S(L_J,\overline{L_J})/m_J\longrightarrow0.}
\]

## Consequences for the research routes

The pointwise fixed-partner theorem, even if FCEA-2 is proved, can still support an
absolute-unbounded defect by choosing a sufficiently large fresh environment at every depth. But
that same asymptotic choice `n_j -> infinity` rules out full-size extensivity for fixed `k`.

A full-size extensive route must change at least one ingredient:

1. reuse a bounded-cost primitive layer with tensor-stable leakage control;
2. let the per-layer output dimension and certified gap grow commensurately with the environment
   cost; or
3. replace the fixed-output BCN hierarchy by another family.

Merely improving the quantitative convergence rate of the existing `n_j -> infinity`, fixed-`k`
scheme cannot evade this upper bound.

## Scope

This obstruction concerns full-size scaling. It does not refute the conditional absolute-unbounded
construction, whose lower bound grows linearly with hierarchy depth while the total dimensions may
grow much faster.
