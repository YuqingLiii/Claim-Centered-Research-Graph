# Flower states fail the Gram realization gate

Date: 2026-08-30

Status: proposer-side candidate exclusion; independent review pending.

All logarithms are base two. This note concerns the third Holevo/minimum-output-entropy
additivity question. It does not reopen the completed quantum/private-capacity project.

## Candidate tested

Sen and Lami study generalized flower states on local dimension `D=2k`. For a unitary
`V in M_k`, define

\[
 \rho_V=\frac1{2k}
 \begin{pmatrix}I&V\\ V^\dagger&I\end{pmatrix},
 \qquad
 \Omega_V=\sum_{i,j=1}^{D}(\rho_V)_{ij}|ii\rangle\langle jj|.
\tag{1}
\]

For the Fourier matrix `V=F_k`, the primary source records

\[
 E_C(\Omega_{F_k})=E_F(\Omega_{F_k})=\log(2\sqrt{k}).
\tag{2}
\]

Moreover, `k rho_V` is a rank-`k` projector and `rho_V` has uniform diagonal. Hence
`Omega_V` is a normalized rank-`k` projector with both marginals equal to `I_D/D`.
This makes flower states natural locking candidates for the entanglement-cost surplus in the
fixed-channel Bell route.

Primary source:

- Samrat Sen and Ludovico Lami, *Entanglement of flower states*, arXiv:2608.02587, especially
  equations (1)-(4), the paragraph preceding Section III, and Theorem 1.
- Local copy:
  `holevo-extensive-violation/artifacts/primary-sources/sen-lami-flower-states-2608.02587.pdf`
- SHA-256: `190c9f9c9eb8843254d3d42eee869051e7d5a9a55fd155ee3444c8edab1016db`

## 1. Exact realignment formula for maximally correlated states

For any matrix `rho`, let

\[
 M(\rho)=\sum_{i,j}\rho_{ij}|ii\rangle\langle jj|.
\tag{3}
\]

Under the realignment convention used in
`CONJUGATE_BELL_REALIGNMENT_CONSTRAINT_20260830.md`, a matrix unit obeys

\[
 \mathcal R(|ii\rangle\langle jj|)=|ij\rangle\langle ij|.
\tag{4}
\]

Therefore

\[
 \boxed{\mathcal R(M(\rho))
   =\sum_{i,j}\rho_{ij}|ij\rangle\langle ij|.}
\tag{5}
\]

This operator is diagonal in the `|ij>` basis. Consequently

\[
 \boxed{\mathcal R(M(\rho))\succeq0
   \quad\Longleftrightarrow\quad
   \rho_{ij}\in\mathbb R_{\ge0}\ \text{for every }i,j.}
\tag{6}
\]

This condition is much stronger than ordinary positivity of `rho`.

## 2. Nontrivial flower states cannot be conjugate-Bell outputs

Applying (6) to (1), realignment positivity of `Omega_V` requires every entry of `V` to be real
and nonnegative. A nonnegative unitary matrix must be a permutation matrix: orthogonality of two
distinct rows is a sum of nonnegative terms, so their supports are disjoint; normalization then
forces exactly one unit entry in each row and column.

Thus

\[
 \boxed{\mathcal R(\Omega_V)\succeq0
   \quad\Longrightarrow\quad V\text{ is a permutation matrix}.}
\tag{7}
\]

For `k>=2`, the Fourier matrix has all `k^2` entries of modulus `1/sqrt(k)` and is not a
permutation. Hence

\[
 \boxed{\mathcal R(\Omega_{F_k})\not\succeq0.}
\tag{8}
\]

Every state of the form `(Phi tensor bar(Phi))(Omega)` has positive realignment. Therefore the
standard flower states cannot themselves be the conjugate-Bell output `Z` of any finite channel.
Allowed output basis changes act as `U tensor bar(U)` and transform the realignment by unitary
congruence, so they cannot repair the negative or non-Hermitian diagonal entries in (5).

The only realignment-positive members of the generalized family are permutation cases. After a
local relabeling, such a state is a uniform mixture of `k` orthogonal two-dimensional maximally
entangled states and has entanglement cost exactly one ebit, not the growing flower-state value.

## 3. Rank obstruction when the flower state is used as the Stinespring state

For a square channel `Theta:M_D->M_D` and an isometric Stinespring dilation `W`, the state

\[
 \sigma_{BE}=W(I_D/D)W^\dagger
\tag{9}
\]

is a normalized projector of rank exactly `D`. In contrast, `Omega_V` has local `B` dimension
`D=2k` but rank only `k=D/2`. It therefore cannot directly equal the maximally mixed
Stinespring state of a square Gram channel.

There is a canonical rank completion: attach a maximally mixed local qubit on the environment,

\[
 \widehat\Omega_V=\Omega_V\otimes I_2/2.
\tag{10}
\]

Then `rank(hat(Omega)_V)=D`, its `B` marginal is `I_D/D`, and it is the maximally mixed
projector on a `D`-dimensional subspace. Hence it can be realized as the maximally mixed
Stinespring state of some square bistochastic channel after choosing an isometry from the input
onto that support. This observation alone does not make the channel self-adjoint,
superoperator-positive, or a CP square.

For the Fourier flower state, the rank completion exactly saturates - but does not pass - the
entanglement-cost gate:

\[
 E_C(\widehat\Omega_{F_k})=\log(2\sqrt{k}),
\tag{11}
\]

while

\[
 S(E)_{\widehat\Omega}=\log(2k)+1=\log(4k),
\tag{12}
\]

and therefore

\[
 \boxed{2E_C(\widehat\Omega_{F_k})-S(E)_{\widehat\Omega}=0.}
\tag{13}
\]

Tensoring a local mixed flag does not change entanglement cost, which proves (11). Equations
(2) and (12) then give (13) directly.

## Gate verdict

Flower states do not solve the fixed finite extensive-violation problem in either natural role:

1. as the Bell output `Z`, every nontrivial flower state fails the necessary positive-realignment
   condition;
2. as the Gram channel's maximally mixed Stinespring state, the unmodified flower state has the
   wrong rank;
3. the minimal local rank completion of the Fourier flower state has zero, rather than positive,
   regularized entanglement-cost surplus.

This is a candidate-family exclusion, not a universal no-go theorem. A non-maximally-correlated
locking state could still be realignment-positive, admit a rectangular CP square, and have a
strictly positive `2E_C-S(E)` surplus.

## Exact remaining target

Search outside the maximally correlated flower family for a normalized rank-`D` projector
`sigma_BE` with `sigma_B=I_D/D` and

\[
 2E_C(\sigma_{BE})>S(E)_\sigma,
\tag{14}
\]

then determine whether some orientation of its support yields a self-adjoint,
superoperator-positive bistochastic channel with the required rectangular CP factorization.
