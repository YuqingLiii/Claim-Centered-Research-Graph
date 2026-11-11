# Correlation identities for the Gram-channel Choi state

Date: 2026-08-30

Status: proposer-side elementary bridge; independently directed review pending.

All logarithms are base two.

## Statement

Let `Theta:M_k->M_k` be a bistochastic quantum channel and use the standard Choi ordering

\[
 J_{RB}(\Theta)=(\mathrm{id}_R\otimes\Theta)(\Omega_k).
\tag{1}
\]

Define the Holevo quantity constrained to average input `I_k/k` by

\[
 \chi_\Theta(I_k/k)
 =\sup_{\sum_xp_x\rho_x=I_k/k}
 \left[S(\Theta(I_k/k))-\sum_xp_xS(\Theta(\rho_x))\right].
\tag{2}
\]

The two directional one-way classical correlations of the Choi state are

\[
 \boxed{
 J_{R\to B}(J(\Theta))=\chi_\Theta(I_k/k),\qquad
 J_{B\to R}(J(\Theta))=\chi_{\Theta^*}(I_k/k).}
\tag{3}
\]

Let `V:C^k->B tensor E` be any Stinespring isometry for `Theta` and set

\[
 \sigma_{BE}=V(I_k/k)V^\dagger.
\tag{4}
\]

The first constrained Holevo quantity obeys

\[
 \boxed{\chi_\Theta(I_k/k)=\log k-E_F(B:E)_\sigma.}
\tag{5}
\]

If `Theta=Theta^*`, either direction in (3) has the same value, and

\[
 \boxed{
 I(R:B)_{J(\Theta)}-2J_{R\to B}(J(\Theta))
 =2E_F(B:E)_\sigma-S(E)_\sigma.}
\tag{6}
\]

For a maximally-mixed-preserving `Phi:M_d->M_k`, define its Gram channel

\[
 \Theta=(k/d)\Phi\Phi^*.
\tag{7}
\]

This channel is bistochastic and self-adjoint. With the standard Choi convention (1), the actual
conjugate-Bell output is the swapped Choi state

\[
 Z_{AB}=(\Phi\otimes\bar\Phi)(\Omega_d)
 =\operatorname{SWAP}\,J_{RB}(\Theta)\,\operatorname{SWAP}.
\tag{8}
\]

The hidden-correlation bound measures `A->B` on the left-hand side of (8), which becomes `B->R`
on the standard Choi state. Self-adjointness and (3) therefore match the required direction.
Combining (3), (6), and (8) with that bound gives

\[
 \boxed{
 2S_{\min}(\Phi)-S((\Phi\otimes\bar\Phi)(\Omega_d))
 \le 2E_F(B:E)_\sigma-S(E)_\sigma.}
\tag{9}
\]

Thus a full-size extensive conjugate-Bell certificate through this mechanism requires

\[
 2E_F(B:E)_\sigma-S(E)_\sigma
 =\Omega(\text{full logarithmic size}),
\tag{10}
\]

in addition to a global lower bound on the minimum output entropy of `Phi`.

## 1. The two Choi measurement directions

For a POVM `{E_x}` on the reference leg `R`, measuring the first leg of `Omega_k` prepares on the
channel input the unnormalized operator `E_x^T/k`. Hence

\[
 p_x=\frac{\operatorname{Tr}E_x}{k},\qquad
 \rho_x=\frac{E_x^T}{\operatorname{Tr}E_x},\qquad
 \sum_xp_x\rho_x=I_k/k.
\tag{11}
\]

The conditional state on `B` is `Theta(rho_x)`. Conversely, every finite ensemble satisfying the
last equality in (11) defines the POVM

\[
 E_x=k p_x\rho_x^T.
\tag{12}
\]

This proves the first identity in (3).

For a POVM `{F_x}` on the channel-output leg `B`, the unnormalized conditional reference state is

\[
 p_x\tau_x=\frac1k(\Theta^*(F_x))^T.
\tag{13}
\]

Bistochasticity gives `p_x=Tr(F_x)/k`. The operators
`rho_x=F_x/Tr(F_x)` range over exactly the ensembles averaging to `I_k/k`, and transposition does
not change entropy. This proves the second identity in (3), with `Theta^*` in place of `Theta`.
For a general bistochastic channel the two directions need not be identified. For the Gram channel
they coincide because `Theta=Theta^*`.

Mixed states in either ensemble cause no problem. Refining them into pure states cannot increase
the average output entropy, so the constrained optimization may be restricted to pure inputs.

## 2. Stinespring entanglement-of-formation form

Every pure input ensemble

\[
 I_k/k=\sum_xp_x|\psi_x\rangle\langle\psi_x|
\tag{14}
\]

maps under the isometry `V` to a pure-state decomposition

\[
 \sigma_{BE}=
 \sum_xp_xV|\psi_x\rangle\langle\psi_x|V^\dagger.
\tag{15}
\]

Conversely, every vector in the support of `sigma_BE` lies in the range of `V`. Applying `V^dagger`
to any pure-state decomposition of `sigma_BE` therefore gives a pure-state ensemble of `I_k/k`.
This is a bijection of the relevant decompositions, and

\[
 S(\Theta(|\psi_x\rangle\langle\psi_x|))
 =S(\operatorname{Tr}_B V|\psi_x\rangle\langle\psi_x|V^\dagger).
\tag{16}
\]

The infimum of the average in (16) is precisely `E_F(B:E)_sigma`. Since bistochasticity gives
`S(Theta(I_k/k))=log k`, equation (5) follows.

## 3. Mutual information, direction matching, and environment entropy

The pure state

\[
 |\Psi\rangle_{RBE}=(I_R\otimes V)|\Omega_k\rangle
\tag{17}
\]

purifies both `J(Theta)_RB` and `sigma_E`. Hence `S(J(Theta))=S(E)_sigma`. Bistochasticity makes
both Choi marginals maximally mixed, so

\[
 I(R:B)_{J(\Theta)}=2\log k-S(E)_\sigma.
\tag{18}
\]

Substituting (5) into (18) proves (6) in the `R->B` direction. Equation (8) swaps the direction
selected by the original conjugate-Bell state to `B->R`; equation (3) and Gram-channel
self-adjointness identify that value with the one used in (6). This proves (9).

## 4. Research consequence

The data-hiding language and entanglement-of-formation language describe exactly the same surplus
for a Gram-channel Choi state. This removes an ambiguity in candidate selection:

1. a large generic data-hiding ratio is not the required quantity;
2. the required quantity is the signed entropy surplus `2E_F(B:E)-S(E)`;
3. the associated Choi channel must be of the special CP-square form `(k/d)Phi Phi^*`;
4. the rectangular square root `Phi` must still have a globally high minimum output entropy.

The identity does not create such a channel. It supplies an exact screening functional for future
candidates and a direct bridge to entanglement-of-formation methods.

## Scope and nonclaims

- Equation (3) is constrained to ensembles averaging to the maximally mixed input; it is not the
  unrestricted one-shot Holevo capacity unless a separate symmetry argument proves that equality.
- The Choi swap and measurement direction are load-bearing. For a general bistochastic channel,
  the two directions involve `Theta` and `Theta^*` separately; their identification here uses
  Gram-channel self-adjointness.
- Equation (9) remains an upper bound because the steered outputs used in the classical-correlation
  optimization need not contain a minimum-output state of `Phi`.
- The identities do not prove tensor additivity or nonadditivity of entanglement of formation.
- No extensive channel-capacity violation follows without the CP-factorization and global side
  entropy requirements.

