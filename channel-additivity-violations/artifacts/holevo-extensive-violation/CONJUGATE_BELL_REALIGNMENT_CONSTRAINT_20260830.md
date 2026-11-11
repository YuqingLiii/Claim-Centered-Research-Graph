# Conjugate-Bell outputs have positive realignment

Date: 2026-08-30

Status: proposer-side elementary theorem; independent review pending.

All vectorizations and transposes below use the product bases that define the entrywise conjugate
channel. This is a necessary channel-realization constraint, not a sufficient characterization.

## Statement

Let `Phi:M_d->M_k` be a finite quantum channel, let `bar(Phi)` be its entrywise conjugate, and set

\[
 Z=(\Phi\otimes\bar\Phi)(\Omega_d),\qquad
 |\Omega_d\rangle=d^{-1/2}\sum_{i=1}^d|ii\rangle .
\tag{1}
\]

Write the Liouville matrix of `Phi` as

\[
 L_{(\mu,\alpha),(i,j)}
   =\langle\mu|\Phi(|i\rangle\langle j|)|\alpha\rangle,
\tag{2}
\]

and define realignment by

\[
 [\mathcal R(X)]_{(\mu,\alpha),(\nu,\beta)}
   =X_{(\mu,\nu),(\alpha,\beta)}.
\tag{3}
\]

Then

\[
 \boxed{\mathcal R(Z)=\frac1d LL^\dagger\succeq0.}
\tag{4}
\]

Consequently

\[
 \operatorname{rank}\mathcal R(Z)=\operatorname{rank}L\le \min\{d^2,k^2\}.
\tag{5}
\]

If `{A_a}` is any Kraus family for `Phi` and `|X\rangle\rangle` denotes column vectorization, the
same Bell output also has the positive frame decomposition

\[
 Z=\frac1d\sum_{a,b}
 |A_aA_b^\dagger\rangle\rangle
 \langle\langle A_aA_b^\dagger|.
\tag{6}
\]

Equation (4) is stronger than the ordinary positivity of `Z`: realignment does not preserve the
positive cone for a general bipartite state.

## 1. Liouville-Gram proof

Expand the normalized Bell projector as

\[
 \Omega_d=\frac1d\sum_{i,j}|i\rangle\langle j|\otimes|i\rangle\langle j|.
\tag{7}
\]

Matrix units are real in the chosen basis, hence

\[
 \bar\Phi(|i\rangle\langle j|)
 =\overline{\Phi(|i\rangle\langle j|)}.
\tag{8}
\]

Taking the `(mu,nu;alpha,beta)` matrix entry of (1) gives

\[
 Z_{(\mu,\nu),(\alpha,\beta)}
 =\frac1d\sum_{i,j}
 L_{(\mu,\alpha),(i,j)}
 \overline{L_{(\nu,\beta),(i,j)}}.
\tag{9}
\]

After applying the index permutation (3), the right-hand side is exactly the
`((mu,alpha),(nu,beta))` entry of `LL^dagger/d`. This proves (4), and (5) follows immediately.

## 2. Kraus-product proof and convention check

For Kraus operators `A_a,A_b`, the vectorization identity gives

\[
 (A_a\otimes\bar A_b)|\Omega_d\rangle
 =d^{-1/2}|A_aA_b^\dagger\rangle\rangle.
\tag{10}
\]

Summing the corresponding rank-one projectors proves (6). This also checks that the second
channel must be the entrywise conjugate in the same product bases; replacing it by an unrelated
channel does not imply (4).

As further consistency checks,

\[
 \operatorname{Tr}_B Z=\Phi(I_d/d),\qquad
 \operatorname{Tr}_A Z=\overline{\Phi(I_d/d)}.
\tag{11}
\]

Thus a channel satisfying `Phi(I_d/d)=I_k/k` produces the maximally mixed marginals assumed in
the hidden-correlation bound, while (4) supplies an additional, previously unused restriction on
the joint state.

## 3. Normalized Choi form of a Gram channel

The realignment identity has a basis-independent channel interpretation. Let `Phi^*` denote the
Hilbert--Schmidt adjoint and define

\[
 \Theta=\frac{k}{d}\,\Phi\circ\Phi^*:M_k\longrightarrow M_k.
\tag{12}
\]

For the normalized **output-first** Choi convention

\[
 J(\Theta)=(\Theta\otimes\mathrm{id}_k)(\Omega_k),
\tag{13}
\]

realignment of the Choi matrix gives

\[
 \mathcal R(J(\Theta))=\frac1k L_\Theta
 =\frac1d L_\Phi L_\Phi^\dagger
 =\mathcal R(Z).
\tag{14}
\]

Since realignment is invertible,

\[
 \boxed{Z=J(\Theta).}
\tag{15}
\]

If instead one uses the standard reference-first convention
`J_std(Theta)=(id tensor Theta)(Omega_k)`, then
`Z=SWAP J_std(Theta) SWAP`. This swap matters when specifying which leg is measured in a
directional classical-correlation quantity; Gram-channel self-adjointness is what later identifies
the two constrained Holevo expressions.

If `Phi(I_d/d)=I_k/k`, then `Theta` is a quantum channel with extra structure:

- it is completely positive because it is a positive scalar times a composition of CP maps;
- it is Hilbert--Schmidt self-adjoint;
- it is positive semidefinite as a superoperator because
  `inner(X,Theta(X))=(k/d)*norm(Phi^*(X))_2^2`;
- it is unital since `Phi^*(I_k)=I_d` and `Phi(I_d)=(d/k)I_k`;
- self-adjointness plus unitality makes it trace preserving.

Thus a maximally-mixed-marginal conjugate-Bell output is not merely realignment-positive. It is the
normalized Choi state of a bistochastic, self-adjoint, superoperator-positive CP map that admits the
specific rectangular factorization `(k/d)Phi Phi^*`. The converse square-root problem is stronger:
the positive superoperator square root of a CP map need not itself be completely positive or obey
the required rectangular trace and marginal constraints.

## 4. Exact exclusion of nontrivial Werner states

Let `F` be the swap on `C^k tensor C^k`, let `K` be the commutation operator on the vectorized
matrix space, and consider any Hermitian Werner-form operator

\[
 W=aI+bF.
\tag{16}
\]

Directly from (3),

\[
 \mathcal R(I)=|I\rangle\rangle\langle\langle I|,
 \qquad
 \mathcal R(F)=K,
\tag{17}
\]

so

\[
 \mathcal R(W)=a|I\rangle\rangle\langle\langle I|+bK.
\tag{18}
\]

For every `k>=2`, the vectorized space contains a nonzero symmetric traceless subspace and a
nonzero antisymmetric subspace. On these two subspaces the first term in (18) vanishes, while `K`
has eigenvalues `+1` and `-1`, respectively. Positivity of (18) therefore requires both `b>=0`
and `b<=0`, hence

\[
 \boxed{\mathcal R(W)\succeq0\quad\Longrightarrow\quad b=0.}
\tag{19}
\]

In particular, neither normalized Werner endpoint

\[
 \rho_\pm=\frac{I\pm F}{k(k\pm1)}
\tag{20}
\]

can equal `(Phi tensor bar(Phi))(Omega_d)` for any finite channel when `k>=2`. More generally, the
only state in the full `U tensor U`-invariant affine Werner family compatible with the necessary
realignment positivity condition is the maximally mixed state.

This does not exclude isotropic states: their symmetry is `U tensor bar(U)`, and their
realignments can be positive. It instead separates the already analyzed isotropic mechanism from
the familiar symmetric/antisymmetric Werner mechanism.

## 5. Consequence for the data-hiding route

The correlation inequality in `BELL_GAP_CLASSICAL_CORRELATION_BOUND_20260830.md` suggested using a
state with large total correlation but little one-way accessible classical correlation. Equations
(4), (15), and (19) show that such a candidate cannot simply be chosen as an arbitrary
data-hiding state:

1. its realignment must be positive;
2. it must be the Choi state of a bistochastic, self-adjoint, superoperator-positive CP map;
3. that map must admit the stronger factorization `(k/d)Phi Phi^*` for one rectangular CPTP map;
4. the same rectangular map's complete output set must still have a sufficiently high minimum
   entropy.

The nontrivial Werner family fails already at item 1. The surviving search target is therefore a
realignment-positive, non-isotropic hiding/locking state with a CP-square-compatible Gram factor,
or a proof that no such state can coexist with the required global side entropy bound.

## Scope and nonclaims

- Positive realignment is necessary, not sufficient. An arbitrary square root of
  `d*R(Z)` need not be the Liouville matrix of a completely positive trace-preserving map.
- Even being the Choi state of a bistochastic self-adjoint superoperator-positive CP map is not
  sufficient unless the map admits the required rectangular CP factorization.
- The theorem concerns the maximally entangled input to `Phi tensor bar(Phi)`. It does not restrict
  the globally minimizing input for a general channel pair.
- Excluding Werner states does not exclude general data-hiding or locking states.
- No full-size extensive additivity violation, and no impossibility theorem for one, follows from
  this constraint alone.
