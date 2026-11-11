# Qutrit antisymmetric state: positive cost surplus but no Gram orientation

Date: 2026-08-30

Status: proposer-side finite-dimensional obstruction; independent review pending.

All logarithms are base two. This note uses a qutrit antisymmetric state only to test the third
Holevo/minimum-output-entropy additivity question. It is not a quantum/private-capacity threshold
calculation.

## Statement

Let `P_-=(I-F)/2` be the projector onto the antisymmetric subspace of
`C^3 tensor C^3`, and let

\[
 \alpha_3=\frac{P_-}{3}=\frac{I-F}{6}.
\tag{1}
\]

Then `alpha_3` has the exact rank and marginal data required of the maximally mixed Stinespring
state of a square qutrit bistochastic channel:

\[
 \operatorname{rank}\alpha_3=3,
 \qquad
 (\alpha_3)_B=(\alpha_3)_E=I_3/3,
 \qquad
 S(BE)_{\alpha_3}=S(E)_{\alpha_3}=\log 3.
\tag{2}
\]

Yura proved that every state supported on the qutrit antisymmetric subspace has entanglement cost
one ebit. In particular,

\[
 E_C(\alpha_3)=1,
 \qquad
 2E_C(\alpha_3)-S(E)_{\alpha_3}=2-\log3>0.
\tag{3}
\]

Thus the strict entanglement-cost gate is feasible for a finite normalized projector with the
correct rank and maximally mixed marginal. Nevertheless, no local-unitary orientation of this
support can be the maximally mixed Stinespring state of a Hilbert-Schmidt-positive Gram channel.

Primary source for the entanglement cost:

- Fumitaka Yura, *Entanglement Cost of Three-Level Antisymmetric States*,
  arXiv:quant-ph/0302163, Corollary 3 on page 3.
- Local copy:
  `holevo-extensive-violation/artifacts/primary-sources/yura-three-level-antisymmetric-entanglement-cost-quant-ph-0302163.pdf`
- SHA-256: `fb83b63737e5be0c63f9bb6549f19107dfaf065e6ed76541011c3f7d4e0f5a0f`

## 1. Canonical square channel determined by the support

Choose the isometry `V:C^3->C^3 tensor C^3`

\[
 V|\ell\rangle
 =\frac1{\sqrt2}\sum_{i,j=1}^3\varepsilon_{ij\ell}|i\rangle_B|j\rangle_E.
\tag{4}
\]

Its range is the antisymmetric subspace and

\[
 V(I_3/3)V^\dagger=\alpha_3.
\tag{5}
\]

Tracing out `E` gives the square qutrit channel

\[
 A(X)=\operatorname{Tr}_E(VXV^\dagger)
     =\frac12\bigl(\operatorname{Tr}(X)I-X^T\bigr).
\tag{6}
\]

The formula follows from contraction of two Levi-Civita tensors. The channel is completely
positive, trace preserving, unital, and Hilbert-Schmidt self-adjoint.

Every isometry onto the same support is `VU` for an input unitary `U`. If the support is also
changed by local unitaries `W` on `B` and `Y` on `E`, the environment unitary disappears under
the partial trace. Hence every square channel whose maximally mixed Stinespring state is locally
unitarily equivalent to `alpha_3` has the form

\[
 A_{W,U}=\operatorname{Ad}_W\circ A\circ\operatorname{Ad}_U.
\tag{7}
\]

## 2. Polar sign of the canonical channel

Decompose the Hilbert-Schmidt matrix space as

\[
 M_3=\mathbb CI\ \oplus\
 \{X:X^T=X,\ \operatorname{Tr}X=0\}\ \oplus\
 \{X:X^T=-X\}.
\tag{8}
\]

On these three mutually orthogonal subspaces, `A` has eigenvalues

\[
 1,\qquad -\frac12,\qquad +\frac12,
\tag{9}
\]

respectively. It is invertible. Its polar sign is therefore the unitary Hermitian superoperator

\[
 \Sigma=\operatorname{sign}(A),
 \qquad
 \Sigma(X)=\frac23\operatorname{Tr}(X)I-X^T.
\tag{10}
\]

This sign is not a unitary conjugation. Indeed,

\[
 \Sigma(|1\rangle\langle1|)
 =\frac23I-|1\rangle\langle1|
\tag{11}
\]

has eigenvalue `-1/3`, whereas every map `Ad_R` is positive.

## 3. No input/output orientation can make the channel Gram-positive

Write `L_W=Ad_W` and `R_U=Ad_U` as unitary operators on Hilbert-Schmidt space. Since `A` is
invertible and has polar decomposition `A=Sigma |A|`, the polar unitary of

\[
 C=L_W A R_U
\tag{12}
\]

is

\[
 Q_C=L_W\Sigma R_U.
\tag{13}
\]

If `C` were positive semidefinite as a Hilbert-Schmidt superoperator, invertibility would make it
positive definite, whose polar unitary is the identity. Equation (13) would then imply

\[
 \Sigma=L_W^\dagger R_U^\dagger
       =\operatorname{Ad}_{W^\dagger U^\dagger}.
\tag{14}
\]

This contradicts (11). Consequently

\[
 \boxed{
 \operatorname{Ad}_W\circ A\circ\operatorname{Ad}_U
 \not\succeq0
 \quad\text{for all qutrit unitaries }U,W.}
\tag{15}
\]

A Gram channel `(k/d)Phi Phi^*` must be positive semidefinite on Hilbert-Schmidt space. Therefore
no local-unitary orientation of the qutrit antisymmetric projector can provide the Gram-channel
Stinespring state required by the fixed-channel conjugate-Bell route.

## Why the same polar-sign proof does not automatically cover higher dimension

For `C^d tensor C^d`, the antisymmetric projector has rank

\[
 r_d=\frac{d(d-1)}2.
\]

An isometry onto that support therefore induces a channel from an `r_d`-dimensional input to a
`d`-dimensional output.  The square-channel polar-orientation criterion used above applies only
when these dimensions coincide.  The equality `r_d=d` holds, among positive dimensions, only for
`d=3`.  Thus the qutrit case has a special rank coincidence: for every `d>3` the support channel is
rectangular, has no polar unitary on one common Hilbert-Schmidt matrix space, and the inner-
automorphism contradiction in equations (12)--(14) is not available.

In particular, comparing the positive and negative eigenspace multiplicities of the formal
Werner--Holevo superoperator on `M_d` would analyze a different square map; it would not certify
the rectangular support channel of the normalized antisymmetric projector.  A genuine
higher-dimensional exclusion would require the still-open rectangular partial-isometry/CP-factor
criterion, together with a separately verified entanglement-cost surplus.

## Gate verdict

This example separates two previously conflated issues:

1. the state-level condition `E_C>S(E)/2` is genuinely attainable in the correct finite rank and
   marginal class;
2. the additional Gram/CP-square channel-realization condition can still fail exactly;
3. for the qutrit antisymmetric support it fails for every input and output unitary orientation,
   not merely for the canonical basis choice.

The remaining target is therefore not just a high-entanglement normalized projector. It must have
a support isometry whose square channel is Hilbert-Schmidt positive and admits a rectangular CP
square, while its rectangular factor retains a global all-copy output-entropy lower bound.
