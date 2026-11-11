# Slater-convex antisymmetric states fail the regularized cost gate

Date: 2026-08-30

Status: proposer-side finite-dimensional obstruction; independent review pending.

All logarithms are base two.

## Statement

Let `sigma_BE` be a state on `C^d tensor C^d`, supported in the antisymmetric sector, with

\[
 \sigma_E=\frac{I_d}{d}.
\tag{1}
\]

Suppose `sigma_BE` belongs to the convex hull of normalized Slater determinants:

\[
 \sigma_{BE}=\sum_a p_a
 |u_a\wedge v_a\rangle\!\langle u_a\wedge v_a|,
\qquad
 \langle u_a|v_a\rangle=0.
\tag{2}
\]

Then

\[
 E_C(\sigma_{BE})\le1.
\tag{3}
\]

Consequently every such state with `d>=4` fails the strict necessary condition

\[
 E_C(\sigma_{BE})>\frac12S(E)_\sigma=\frac12\log d
\tag{4}
\]

for a positive-rate fixed-channel conjugate-Bell certificate.

## Proof

Every normalized Slater determinant has Schmidt spectrum `(1/2,1/2)` and therefore exactly one
ebit of entanglement.  The displayed ensemble immediately gives

\[
 E_F(\sigma_{BE})\le\sum_a p_a=1.
\tag{5}
\]

Entanglement cost is the regularized entanglement of formation, and subadditivity of `E_F`
implies

\[
 E_C(\sigma_{BE})
 =\lim_{n\to\infty}\frac1nE_F(\sigma_{BE}^{\otimes n})
 \le E_F(\sigma_{BE})\le1.
\tag{6}
\]

Equation (1) gives `S(E)=log d`.  For `d>=4`, equations (4) and (6) are incompatible; at `d=4`
the non-strict upper bound only reaches equality, whereas the channel gate requires strict
positivity.

## Consequences for candidate search

This lemma simultaneously covers:

- every normalized full antisymmetric projector in dimensions `d>=4`;
- the rank-four `d=4` proper supports classified in
  `FOUR_DIMENSIONAL_ANTISYMMETRIC_SQUARE_SUPPORT_NO_GO_20260830.md`; and
- any higher-dimensional support projector for which a Slater tight frame or other Slater
  ensemble resolves its normalized projector.

A surviving proper antisymmetric support in `d>=5` must therefore be fermionically entangled in
the precise sense of lying outside the Slater convex hull.  Merely having high-entanglement basis
vectors is not enough: the required inequality concerns tensor-stable entanglement cost, not a
chosen ensemble or one-shot pure-state minimum.

The lemma does not prove that all maximally-mixed-marginal antisymmetric support states are
Slater-convex, and it makes no statement about coherent mixtures with non-antisymmetric sectors or
non-Bell witnesses.
