# The rank-eight octonionic Hurwitz support: exact one-shot threshold crossing and triality no-go

Date: 2026-08-30

Status: proposer-side exact finite-dimensional obstruction; independent review pending.

All logarithms are base two.  This note screens a coherent scalar-plus-antisymmetric support for
the fixed-channel conjugate-Bell route.  It does not settle the full-size extensive question.

## Statement

Let `L_a`, `a=0,...,7`, be the real `8 x 8` matrices of left multiplication by the standard
orthonormal octonion basis, with `L_0=I`.  Norm composition gives the Hurwitz relations

\[
 L_a^T L_b+L_b^T L_a=2\delta_{ab}I_8.
\tag{1}
\]

Define

\[
 V|a\rangle={1\over\sqrt8}\operatorname{vec}(L_a),
 \qquad
 \sigma={1\over8}VV^\dagger.
\tag{2}
\]

Then `V:C^8->C^8 tensor C^8` is an isometry, `sigma` has rank eight and maximally mixed
marginals, and

\[
 E_F(\sigma)=2>{1\over2}\log8={3\over2}.
\tag{3}
\]

The square support channel `T(X)=Tr_E(VXV^dagger)` is self-adjoint but singular, with

\[
 \operatorname{spec}T=
 \{1^{(1)},(-1/2)^{(7)},(1/2)^{(21)},0^{(35)}\}.
\tag{4}

Its polar sign on the 29-dimensional support cannot be extended to a support-preserving inner
automorphism of `M_8`.  By the kernel-compatible polar criterion, no input/output local-unitary
orientation of this support is a Hilbert--Schmidt-positive Gram channel.

## 1. Exact one-shot entanglement of formation

For a unit complex coefficient vector write `x=u+iv` with real `u,v`.  A global phase makes
`u` and `v` orthogonal.  Set `a=||u||`, `b=||v||`; then `a^2+b^2=1`.  Polarizing the norm-composition
identity in (1) shows that the reduced output of `V|x>` has spectrum

\[
 \left\{ {(1+2ab)\over8}^{(4)},
          {(1-2ab)\over8}^{(4)}\right\}.
\tag{5}
\]

Its entropy decreases with `2ab in [0,1]` and is minimized for a complex-null coefficient vector,
where

\[
 \operatorname{spec}\rho_B=\{(1/4)^{(4)},0^{(4)}\},
 \qquad S(\rho_B)=2.
\tag{6}
\]

The uniform ensemble over

\[
 (e_i\pm i e_j)/\sqrt2,\qquad 0\le i<j\le7,
\tag{7}

averages to `I_8/8`, so (6) is attained by a decomposition of `sigma`.  Every decomposition stays
inside the support and is lower-bounded by (6), proving (3).  As in the `G2` near-miss, this is an
exact `E_F` statement, not an all-copy `E_C` statement.

## 2. Support-channel spectrum

Eight times the channel has the integer matrix

\[
 (8T)_{bd,ac}=\sum_e(L_a)_{be}(L_c)_{de}.
\tag{8}
\]

Direct contraction gives the orthogonal decomposition

\[
 M_8=
 \mathbb CI\oplus\mathfrak m_7\oplus\mathfrak{spin}(7)\oplus\operatorname{Sym}^2_0,
\tag{9}
\]

of dimensions `1,7,21,35`, on which `8T` has eigenvalues `8,-4,4,0`.  In particular

\[
 \mathcal S=(\ker T)^\perp=\mathbb CI\oplus\mathfrak{so}(8),
\tag{10}
\]

and its polar sign is negative on `m_7` and positive on the scalar and `spin(7)` summands.

The exact checker constructs (8), verifies the annihilating polynomial

\[
 (8T)(8T-8I)(8T+4I)(8T-4I)=0,
\tag{11}
\]

computes nullities `1,7,21,35`, identifies the kernel with the symmetric-traceless matrices, and
proves that the positive 21-dimensional skew eigenspace has zero common vector kernel.

## 3. Why the partial polar sign is not inner

Assume that the sign on `S` were the restriction of `Ad_R` with `Ad_R(S)=S`.  Since conjugation
fixes the scalar, `Ad_R` normalizes `so(8,C)`.  For every transpose-skew `X`, preservation of
transpose skewness gives

\[
 (R^\dagger\bar R)X=X(R^\dagger\bar R).
\tag{12}
\]

The defining representation of `so(8,C)` is irreducible, so its commutant is scalar.  After a
phase, `R` is therefore real orthogonal.

The sign squares to the identity on `S`; because `so(8)` generates the full matrix algebra, this
forces `R^2` to be scalar.  For a real orthogonal `R`, there are two cases.

1. If `R^2=-I`, its fixed algebra in `so(8)` is `u(4)`, of dimension 16, so its negative space in
   `so(8)` has dimension 12 rather than 7.
2. If `R^2=I` and the real `+/-` multiplicities are `r,8-r`, the negative space in `so(8)` has
   dimension `r(8-r)`.  Matching the required dimension seven forces `r=1` or `7`.  The fixed
   21-dimensional algebra is then a standard `so(7)` that annihilates the one-dimensional
   reflected axis.

But the exact `+1/2` eigenspace of `T` has common kernel zero.  It is the irreducible spinorial
`spin(7)` embedding, not a reflection-fixed `so(7)`.  Both cases contradict the required polar
sign.  The kernel-compatible criterion therefore excludes every local Gram-positive orientation.

## Verdict and limitations

The octonionic support is the first checked coherent multi-sector square support with exact
`E_F>S(E)/2`; unlike the antisymmetric `G2` support, its channel has a large kernel and requires the
partial-polar theorem.  It still fails before CP factorization.

The result does not determine `E_C(sigma)`, classify other rank-eight supports, or constrain
non-Bell witnesses.  Full-size extensivity remains open.

Reproduction:

```text
python3 holevo-extensive-violation/tools/check_octonionic_hurwitz_support.py
```

Expected output:

```text
octonionic Hurwitz support exact checks passed
spectrum(8T): 8^1, (-4)^7, 4^21, 0^35
positive 21-space common kernel dimension: 0
spectrum(rho_null): 0^4, (1/4)^4
```

