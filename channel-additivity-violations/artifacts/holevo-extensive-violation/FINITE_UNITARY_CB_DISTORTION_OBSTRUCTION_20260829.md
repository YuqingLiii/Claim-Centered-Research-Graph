# Fixed finite unitary tuples have large complete distortion

Date: 2026-08-29

Status: proposer-side proof-method obstruction.

## Purpose

The finite-dimensional unbounded-gap proof approximates a product-free-group norm at every fixed
tensor depth by increasing the matrix dimension. A tempting shortcut to full-size extensivity is:

1. choose one sufficiently large but fixed finite unitary tuple;
2. prove that its one-layer operator system is a `(1+epsilon)` complete approximation to the free
   one; and
3. tensor that complete bound indefinitely at fixed per-layer cost.

This note rules out that shortcut. Every finite unitary tuple has a matrix-amplification witness
with distortion at least `(m-1)/5`, where `m` is the number of unitaries. The obstruction is the
same conjugate/Bell invariant that creates the additivity violation.

## Operator-system map

Let `u_1,...,u_m` be the canonical free Haar unitaries in `C_r^*(F_m)` and let

\[
 E_m=\operatorname{span}\{u_i^*u_j:1\le i,j\le m\}.
\]

For an arbitrary finite-dimensional unitary tuple `U_1,...,U_m in U(D)`, define the unital
self-adjoint linear map on this span by

\[
 \theta_U(u_i^*u_j)=U_i^*U_j.
\]

The definition respects the only diagonal identification `u_i^*u_i=1`.

## Amplification witness

At matrix level `D`, choose coefficients

\[
 a_{ij}=\overline U_i^*\overline U_j-\delta_{ij}I_D.
\]

Their block trace vanishes:

\[
 \sum_i a_{ii}=0.
\]

Put

\[
 Z=\sum_{i,j}a_{ij}\otimes u_i^*u_j\in M_D\otimes E_m.
\]

On the finite side, with

\[
 B_U=\sum_i\overline U_i\otimes U_i,
\]

we have

\[
 (\operatorname{id}_D\otimes\theta_U)(Z)=B_U^*B_U-mI.
\tag{1}
\]

The normalized maximally entangled vector `Omega_D` is fixed by every
`bar(U_i) tensor U_i`. Hence `B_U Omega_D=m Omega_D`, and (1) gives

\[
 \|(\operatorname{id}_D\otimes\theta_U)(Z)\|\ge m^2-m.
\tag{2}
\]

On the free side, set

\[
 B_f=\sum_i\overline U_i\otimes u_i.
\]

The free absorption principle says that `bar(U_i) tensor u_i` are again free Haar unitaries.
The degree-one Haagerup inequality gives

\[
 \|B_f\|\le2\sqrt m.
\]

Therefore

\[
 \|Z\|=\|B_f^*B_f-mI\|\le\|B_f\|^2+m\le5m.
\tag{3}
\]

Combining (2)--(3),

\[
 \|\theta_U\|_{\mathrm{cb}}
 \ge\|\operatorname{id}_D\otimes\theta_U\|
 \ge\frac{m^2-m}{5m}=\frac{m-1}{5}.
\tag{4}
\]

This holds for every finite `D` and every unitary tuple.

## Consequence

For the unbounded-gap construction `m>e^18`, the lower bound (4) is enormous. Thus no fixed finite
unitary realization can be a small-distortion complete approximation of the free length-two
operator system. In particular, exactness/MF heuristics cannot justify tensoring one fixed
finite-dimensional scalar strong-convergence estimate through arbitrarily large coefficient
levels.

The obstruction is consistent with Bordenave--Collins: their theorem controls every **fixed**
matrix coefficient level after the random-matrix dimension grows, not all levels uniformly at one
fixed dimension.

## Scope limit

The coefficients `a_ij` above prove failure of an all-matrix-level norm certificate. They are not
shown to be centered complementary-channel outputs arising from physical input states. Therefore
this note does not prove that the true regularized minimum output entropy of every finite random-
unitary tuple collapses, and it does not refute the full-size extensive conjecture. It closes only
the proposed complete-bounded-tensorization proof route.

## Source input

The only imported fact is the standard free absorption principle and the degree-one Haagerup norm
bound; Bordenave--Collins discuss the absorption principle in Section 9.2 of
`primary-sources/bordenave-collins-2304.05714.pdf`, PDF pp. 61--62.
