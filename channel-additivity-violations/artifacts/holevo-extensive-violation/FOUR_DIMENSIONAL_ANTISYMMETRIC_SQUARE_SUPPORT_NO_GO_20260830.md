# Every four-dimensional antisymmetric square support fails the cost gate

Date: 2026-08-30

Status: proposer-side finite-dimensional obstruction; independent review pending.

All logarithms are base two.  This note closes the first proper-support case left open by the
full antisymmetric-projector family audit.

## Statement

Let `S` be a four-dimensional subspace of `wedge^2 C^4`, let `P_S` be its projector, and suppose

\[
 \sigma_S=\frac{P_S}{4},
 \qquad
 (\sigma_S)_B=(\sigma_S)_E=\frac{I_4}{4}.
\tag{1}
\]

Then `sigma_S` has an ensemble of four orthonormal one-ebit Slater determinants.  Consequently

\[
 E_C(\sigma_S)\le E_F(\sigma_S)\le1
 =\frac12 S(E)_{\sigma_S}.
\tag{2}
\]

It therefore fails the strict entanglement-cost condition required by every positive-rate
fixed-channel conjugate-Bell certificate.

## 1. Matrix representation and the two-dimensional complement

Represent a bipartite vector by its coefficient matrix:

\[
 |A\rangle=\sum_{i,j=1}^4 A_{ij}|i\rangle|j\rangle,
 \qquad A^T=-A,
 \qquad \langle A|B\rangle=\operatorname{Tr}(A^\dagger B).
\tag{3}
\]

The reduced density matrix of `|A>` is `AA^dagger`.  Let

\[
 K=S^\perp\subset\wedge^2\mathbb C^4,
 \qquad \dim K=2,
\tag{4}
\]

and choose an orthonormal matrix basis `A,B` of `K`.  The full antisymmetric projector has

\[
 \operatorname{Tr}_E P_-^{(4)}=\frac32 I_4.
\tag{5}
\]

Equation (1) gives `Tr_E P_S=I_4`, hence

\[
 AA^\dagger+BB^\dagger=\frac12 I_4.
\tag{6}
\]

## 2. The complement contains an invertible skew matrix

For a `4 by 4` skew matrix, invertibility is equivalent to a nonzero Pfaffian.  If every element
of `K` were singular, then for two independent decomposable two-forms `a,b` spanning `K`,
`a+t b` would be decomposable for every `t`.  Since

\[
 (a+t b)\wedge(a+t b)=2t\,a\wedge b,
\tag{7}
\]

this forces `a wedge b=0`.  The two underlying two-planes then intersect, so both forms are
supported in one three-dimensional subspace of `C^4`.  The left side of (6) would have a common
kernel, contradicting its being `I_4/2`.  After a unitary change of basis inside `K`, we may
therefore take `A` invertible.

## 3. Simultaneous canonical form

Unitary skew-Takagi factorization gives, after a unitary congruence on `C^4`,

\[
 A=aJ\oplus bJ,
 \qquad
 J=\begin{pmatrix}0&1\\-1&0\end{pmatrix},
 \qquad
 a,b\ge0,
 \qquad a^2+b^2=\frac12.
\tag{8}
\]

Equation (6) then fixes

\[
 BB^\dagger=b^2 I_2\oplus a^2 I_2.
\tag{9}
\]

### Distinct singular values

If `a!=b`, skew-Takagi uniqueness of the two singular subspaces makes `B` block diagonal:

\[
 B=b e^{i\theta}J\oplus a e^{i\phi}J.
\tag{10}
\]

Orthogonality `Tr(A^dagger B)=0` gives `e^{i\phi}=-e^{i\theta}` when `ab!=0`; the endpoint
`ab=0` is immediate.  In all cases the two coefficient pairs in (8) and (10) are linearly
independent, and hence

\[
 K=\operatorname{span}\{J\oplus0,\ 0\oplus J\}.
\tag{11}
\]

### Equal singular values

If `a=b=1/2`, put `\widehat A=2A` and `\widehat B=2B`.  These are skew unitary matrices, and

\[
 C=\widehat A^\dagger\widehat B
\tag{12}
\]

is unitary with `Tr C=0`.  Moreover

\[
 \det(C-\lambda I)
 =\det(\widehat A^\dagger)\det(\widehat B-\lambda\widehat A)
\tag{13}
\]

is a square polynomial, because the determinant of every even skew matrix is the square of its
Pfaffian.  Thus every eigenvalue of `C` has even algebraic multiplicity.  Since `C` is normal on a
four-dimensional space and has trace zero, its spectrum is

\[
 \{\lambda,\lambda,-\lambda,-\lambda\}.
\tag{14}
\]

The skew relation for `\widehat B=\widehat A C` is

\[
 C^T\widehat A=\widehat A C.
\tag{15}
\]

It makes the two distinct eigenspaces in (14) orthogonal for the nondegenerate alternating form
defined by `\widehat A`.  Because `C` is normal they are also Hermitian-orthogonal.  Choosing a
unitary symplectic basis in each two-dimensional eigenspace puts

\[
 \widehat A=J\oplus J,
 \qquad
 \widehat B=\lambda J\oplus(-\lambda J).
\tag{16}
\]

Equation (11) follows again.

## 4. A one-ebit orthonormal basis of the original support

In exterior-form notation, equation (11) says

\[
 K=\operatorname{span}\{e_1\wedge e_2,\ e_3\wedge e_4\}.
\tag{17}
\]

Therefore

\[
 S=K^\perp
 =\operatorname{span}\{
 e_1\wedge e_3,
 e_1\wedge e_4,
 e_2\wedge e_3,
 e_2\wedge e_4
 \}.
\tag{18}
\]

The four displayed normalized wedges are orthonormal Slater determinants.  Each has Schmidt
spectrum `(1/2,1/2)` and one ebit, so their uniform ensemble is exactly `P_S/4` and proves (2).

## Verdict and limitations

Every rank-four antisymmetric support with maximally mixed four-dimensional marginals fails the
strict regularized cost gate.  Together with the normalized full-projector no-go, this removes the
first square proper-support candidate beyond qutrits.

The proof does not classify rank-`d` proper antisymmetric supports for `d>=5`.  It also does not
exclude coherent mixtures with non-antisymmetric representation sectors or non-Bell joint inputs.
