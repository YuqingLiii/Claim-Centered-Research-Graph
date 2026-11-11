# A qubit Gram channel passes the cost and CP-factor gates but fails side entropy

Date: 2026-08-30

Status: proposer-side finite-dimensional candidate exclusion; independent review pending.

All logarithms are base two.

## Statement

Let `T:M_2->M_2` be the Pauli channel

\[
 T(X)=\frac12X+\frac14\sigma_yX\sigma_y+\frac14\sigma_zX\sigma_z.
\tag{1}
\]

Its Pauli transfer eigenvalues on `(I,sigma_x,sigma_y,sigma_z)` are

\[
 (1,0,1/2,1/2).
\tag{2}
\]

Thus `T` is completely positive, bistochastic, Hilbert-Schmidt self-adjoint, and
Hilbert-Schmidt positive semidefinite. It has all the abstract structure of a Gram channel.

This example passes two nontrivial gates:

1. its maximally mixed Stinespring state has strict entanglement-cost surplus;
2. it has an explicit rectangular CPTP factor `T=(2/4)Phi_0 Phi_0^*`.

Nevertheless, every rectangular CPTP factor `Phi` of `T` has a one-shot minimum output entropy
too small for a conjugate-Bell violation. The candidate therefore fails before the all-copy gate.

## 1. Exact entanglement cost of the maximally mixed Stinespring state

Let `sigma_BE=V(I_2/2)V^dagger` be a Stinespring output of a unital qubit channel `N`. The
Hughston-Jozsa-Wootters correspondence identifies decompositions of `sigma_BE^tensor n` with
pure-state ensembles of `I_2^tensor n/2^n`. Consequently

\[
 E_F(\sigma_{BE}^{\otimes n})
 \ge S_{\min}(N^{\otimes n}).
\tag{3}
\]

For one copy, a minimizing pure qubit state has a Bloch antipode. Unitality makes the two output
spectra equal, and the antipodal pair averages to `I_2/2`. Taking product ensembles gives the
opposite inequality at every copy once minimum output entropy is additive.

King's Theorem 1 proves strong minimum-output-entropy additivity for a unital qubit channel and an
arbitrary partner. Iterating it yields

\[
 S_{\min}(N^{\otimes n})=nS_{\min}(N).
\tag{4}
\]

Equations (3)-(4) and the antipodal product ensemble therefore give

\[
 \boxed{E_C(\sigma_{BE})=S_{\min}(N)}
 \quad\text{for every unital qubit channel }N.
\tag{5}
\]

For the channel `T` in (1), the largest Bloch contraction is `1/2`, so

\[
 E_C(\sigma_{BE})=S_{\min}(T)=h_2(3/4).
\tag{6}
\]

The complementary output on the maximally mixed input has the Pauli probability spectrum
`(1/2,0,1/4,1/4)`, hence

\[
 S(E)_\sigma=\frac32.
\tag{7}
\]

It follows that

\[
 \boxed{2E_C(\sigma_{BE})-S(E)_\sigma
 =2h_2(3/4)-\frac32
 \approx0.122556>0.}
\tag{8}
\]

Primary source for (4):

- Christopher King, *Additivity for unital qubit channels*, arXiv:quant-ph/0103156,
  Theorem 1, page 4.
- Local copy:
  `holevo-extensive-violation/artifacts/primary-sources/king-unital-qubit-additivity-quant-ph-0103156.pdf`
- SHA-256: `0e8b627c523e32c908f30ba6f206c876f7d88bd8a36df7d00ae82fb3e1132b6d`

## 2. Explicit rectangular CP factor

Let the four input basis labels be `+y,-y,+z,-z`, and define the measure-prepare channel
`Phi_0:M_4->M_2` by

\[
 \Phi_0(\rho)=
 \sum_{s\in\{+y,-y,+z,-z\}}
 \langle s|\rho|s\rangle\,\tau_s,
\tag{9}
\]

where `tau_s=(I+s dot sigma)/2` is the indicated pure qubit state. The four states average to
`I_2/2`, so `Phi_0(I_4/4)=I_2/2`.

For a Pauli observable,

\[
 \Phi_0^*(\sigma_x)=0,
\tag{10}
\]

while `Phi_0^*(sigma_y)` and `Phi_0^*(sigma_z)` are the diagonal vectors
`(1,-1,0,0)` and `(0,0,1,-1)`. Applying `Phi_0` again gives

\[
 \frac12\Phi_0\Phi_0^*(I)=I,
 \quad
 \frac12\Phi_0\Phi_0^*(\sigma_x)=0,
 \quad
 \frac12\Phi_0\Phi_0^*(\sigma_y)=\frac12\sigma_y,
 \quad
 \frac12\Phi_0\Phi_0^*(\sigma_z)=\frac12\sigma_z.
\tag{11}
\]

Therefore

\[
 \boxed{T=\frac{2}{4}\Phi_0\Phi_0^*.}
\tag{12}
\]

This proves that the positive-cost Gram channel is not excluded by the rectangular CP-factor
condition. The displayed factor is entanglement breaking and has `S_min(Phi_0)=0`, but the next
section rules out every other factor as well.

## 3. Universal side-entropy obstruction for every rectangular factor

Assume `Phi:M_d->M_2` is any channel satisfying

\[
 T=\frac2d\Phi\Phi^*.
\tag{13}
\]

Since `T` is unital, (13) and trace preservation imply `Phi(I_d/d)=I_2/2`. Define the Hermitian
operator

\[
 A_y=\Phi^*(\sigma_y)\in M_d.
\tag{14}
\]

Using the Hilbert-Schmidt inner product and `T(sigma_y)=sigma_y/2`,

\[
 1=\operatorname{Tr}(\sigma_yT(\sigma_y))
  =\frac2d\operatorname{Tr}(A_y^2).
\tag{15}
\]

Thus `Tr(A_y^2)=d/2`, and hence

\[
 \|A_y\|_\infty^2\ge\frac1d\operatorname{Tr}(A_y^2)=\frac12.
\tag{16}
\]

Choose a unit eigenvector `|psi>` for an eigenvalue of largest magnitude. The `y` component of
the output Bloch vector is

\[
 \operatorname{Tr}(\sigma_y\Phi(|\psi\rangle\langle\psi|))
 =\langle\psi|A_y|\psi\rangle,
\tag{17}
\]

whose absolute value is at least `1/sqrt(2)`. Therefore

\[
 S_{\min}(\Phi)
 \le h_2\!\left(\frac{1+1/\sqrt2}{2}\right)
 \approx0.600876.
\tag{18}
\]

The conjugate-Bell output associated with the Gram channel `T` is its normalized Choi state. It
has the same Bell-diagonal probability spectrum as (1), so

\[
 S(Z)=\frac32.
\tag{19}
\]

Combining (18)-(19),

\[
 \boxed{
 2\overline S_{\min}(\Phi)-S(Z)
 \le2S_{\min}(\Phi)-\frac32
 <0.}
\tag{20}
\]

The strict inequality can be checked without decimals from the elementary binary-entropy bound
`h_2(p)<=2sqrt(p(1-p))`: its right side at (18) is `1/sqrt(2)`, so the first two terms in (20) are
at most `sqrt(2)<3/2`.

## Gate verdict

The channel (1) is a complete three-stage near-miss:

1. it is a Hilbert-Schmidt-positive bistochastic Gram channel;
2. its maximally mixed Stinespring state strictly passes `E_C>S(E)/2`;
3. it admits an explicit finite rectangular CPTP factor;
4. but every such factor has too small a minimum output entropy, already at one copy, to produce
   a Bell-certified defect.

Thus high entanglement cost and CP factorability can coexist. The genuinely load-bearing final
gate is the factor's global side entropy, not merely the state-level surplus.
