# The seven-dimensional G2 antisymmetric support is a one-shot high-cost Gram near-miss

Date: 2026-08-30

Status: proposer-side exact finite-dimensional obstruction; independent review pending.

All logarithms are base two.  This note screens one candidate for the fixed-channel
conjugate-Bell route.  It does not prove or disprove the full-size extensive question.

## Statement

Let `phi` be the standard real `G2`-invariant alternating three-form on `R^7`, extended
complex-linearly, and define the isometry

\[
 V|a\rangle={1\over\sqrt 6}\sum_{b,e=1}^7\phi_{abe}|b\rangle_B|e\rangle_E.
\tag{1}
\]

Its range `S` is a seven-dimensional subspace of `wedge^2 C^7`.  The normalized support
projector

\[
 \sigma_{BE}=V{I_7\over7}V^\dagger={P_S\over7}
\tag{2}
\]

has maximally mixed marginals and exact one-shot entanglement of formation

\[
 \sigma_B=\sigma_E={I_7\over7},\qquad
 E_F(\sigma)=\log 3+{1\over3}>{1\over2}\log7.
\tag{3}
\]

Thus this proper antisymmetric square support lies outside the simple one-ebit Slater screen and
passes the *one-shot* analogue of the state-cost threshold.  No claim is made that its
entanglement cost equals its one-shot entanglement of formation.

Nevertheless, the square support channel

\[
 T(X)=\operatorname{Tr}_E(VXV^\dagger)
\tag{4}
\]

has Hilbert--Schmidt spectrum

\[
 1^{(1)},\quad(-1/2)^{(7)},\quad(1/2)^{(14)},\quad(-1/6)^{(27)}.
\tag{5}
\]

Its polar sign therefore has a 34-dimensional negative eigenspace.  That sign is not an inner
automorphism of `M_7`, so the polar-orientation criterion excludes every input/output local-unitary
orientation of this support from being a Hilbert--Schmidt-positive Gram channel.

## 1. Isometry and maximally mixed marginals

Use the normalization

\[
 \sum_{b,e}\phi_{abe}\phi_{cbe}=6\delta_{ac}.
\tag{6}
\]

Equation (6) gives `V^dagger V=I_7`.  The same contraction on the other pair of indices gives

\[
 T(I_7)=I_7,
\tag{7}
\]

and trace preservation follows from the isometry.  Because the range is antisymmetric, the two
partial traces of (2) agree.  Equations (2) and (7) therefore give both marginal identities in
(3), while the seven equal nonzero eigenvalues of (2) give

\[
 S(BE)_\sigma=S(E)_\sigma=\log7.
\tag{8}
\]

## 2. Exact pure-state entropy on the support

Every vector in `S` is `V|x>` for a unique `x in C^7`.  After multiplying `x` by a global phase,
write its real and imaginary parts as orthogonal vectors.  The transitivity chain

\[
 G_2/SU(3)=S^6,\qquad SU(3)/SU(2)=S^5
\tag{9}
\]

then puts every unit vector in the normal form

\[
 x=a e_1+i b e_2,qquad a,b\ge0,\qquad a^2+b^2=1.
\tag{10}
\]

Direct contraction of the standard seven nonzero triples of `phi` gives the reduced spectrum

\[
 \operatorname{spec}\operatorname{Tr}_E(V|x\rangle\langle x|V^\dagger)
 =\left\{
 0,
 { (a-b)^2\over6}^{(2)},
 {1\over6}^{(2)},
 { (a+b)^2\over6}^{(2)}
 \right\}.
\tag{11}
\]

Set `t=2ab in [0,1]`.  Differentiating the entropy of (11) gives

\[
 H'(t)=-{1\over3}\log {1+t\over1-t}\le0.
\tag{12}
\]

The least entangled support vectors are consequently the complex-null vectors `x^T x=0`, at
`a=b=1/sqrt(2)`, with spectrum

\[
 \{1/3,1/3,1/6,1/6,0,0,0\}
\tag{13}
\]

and entropy

\[
 H_{\min,S}=\log3+{1\over3}.
\tag{14}
\]

This lower bound is attained in a decomposition of (2).  For every `i<j`, take both null vectors

\[
 x_{ij}^{\pm}={e_i\pm i e_j\over\sqrt2}.
\tag{15}
\]

The uniform ensemble over the 42 vectors in (15) averages to `I_7/7`; applying `V` gives a
decomposition of `sigma` in which every member has entropy (14).  Conversely, every pure-state
decomposition of `sigma` stays in `S`, so (14) lower-bounds every member.  This proves the exact
one-shot formula in (3).

The distinction between `E_F` and `E_C` is load-bearing: no tensor-power lower bound is asserted.

## 3. Exact spectrum of the support channel

In matrix units, six times (4) has integer entries

\[
 (6T)_{bd,ac}=\sum_e\phi_{abe}\phi_{cde}.
\tag{16}
\]

It is real symmetric on Hilbert--Schmidt space.  A direct `G2` decomposition

\[
 M_7=\mathbf1\oplus\mathbf7\oplus\mathbf{14}\oplus\mathbf{27}
\tag{17}
\]

and the contraction identity for (16) give eigenvalues

\[
 6,-3,3,-1
\tag{18}
\]

on the four summands respectively, proving (5).  The accompanying exact checker independently
constructs the full integer `49 x 49` matrix, verifies

\[
 (6T-6I)(6T+3I)(6T-3I)(6T+I)=0,
\tag{19}
\]

and computes the four rational nullities `1,7,14,27` by exact Gaussian elimination.  It also
checks trace preservation, unitality, self-adjointness, and the null-vector spectrum (13) without
floating-point arithmetic.

## 4. Polar-sign obstruction

Because none of the four eigenvalues in (5) vanishes, `T` is invertible.  Its polar unitary `Q`
is the Hermitian involution that is positive on the `1+14=15` dimensional positive spectral
space and negative on the `7+27=34` dimensional negative spectral space.

Suppose `Q=Ad_R` were an inner automorphism.  Since `Q` is a Hermitian involution,
`Ad_{R^2}=I`; after an irrelevant phase, `R` is a Hermitian involution.  If its `+1` eigenspace has
dimension `r`, the negative eigenspace of `Ad_R` consists of the two off-diagonal matrix blocks and
has dimension

\[
 2r(7-r)\le24.
\tag{20}
\]

This contradicts the 34-dimensional negative space of `Q`.  Hence `Q` is not inner.  The exact
polar-orientation criterion now gives

\[
 \operatorname{Ad}_W\circ T\circ\operatorname{Ad}_U\not\succ0
 \quad\text{for every }U,W\in U(7).
\tag{21}
\]

A Gram channel must be Hilbert--Schmidt positive semidefinite, so no local orientation of this
support can reach the later rectangular CP-square or global side-entropy gates.

## Verdict and limitations

This candidate is stronger than the previously closed Slater-convex supports at the one-shot
state level: it has the correct square rank, exact maximally mixed marginals, and
`E_F>S(E)/2`.  It is nevertheless excluded exactly by its polar sign.

The result does **not** show that `E_C(sigma)>S(E)/2`, does not classify other rank-seven supports
inside `wedge^2 C^7`, and does not constrain nonantisymmetric, noncovariant, or non-Bell routes.
The full-size extensive Holevo/MOE question remains open.

Reproduction:

```text
python3 holevo-extensive-violation/tools/check_g2_antisymmetric_support.py
```

Expected output:

```text
G2 support exact checks passed
spectrum(6T): 6^1, (-3)^7, 3^14, (-1)^27
spectrum(rho_null): 0^3, (1/6)^2, (1/3)^2
```

