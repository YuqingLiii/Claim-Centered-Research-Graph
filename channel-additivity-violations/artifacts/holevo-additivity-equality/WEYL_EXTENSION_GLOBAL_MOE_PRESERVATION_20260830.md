# Weyl extension: global minimum-output-entropy preservation

Date: 2026-08-30

Status: historical pre-review proposer-side derivation. The exact preservation claim was
subsequently independently reviewed and promoted to `PROVED`; its canonical YAML is authoritative
for current status.

All logarithms are base two. This note closes a specific missing step in the local specialization
of Shor's Section 9 construction. It does not promote any canonical claim to `PROVED`.

## Canonical audit and route selection

The seven pre-existing canonical nodes were audited together with all project artifacts.

- `HAEQ.goal` has one load-bearing route. Its three premises are the Hastings MOE existence
  theorem, the explicit Weyl transfer, and the flagged pair-to-self reduction.
- `HAEQ.hastings-moe-counterexample` is source-bound to Hastings' finite-dimensional existence
  theorem; its remaining work is independent source/scope review rather than a new local argument.
- `HAEQ.pair-to-self-reduction` already contains the full four-block log-sum-exp calculation.
- `HAEQ.fixed-channel-regularization` is a complete elementary proposer-side argument, and the root
  needs only its easier `n=2` consequence.
- `HAEQ.universal-additivity-equivalence` is useful background but is no longer load-bearing.
- `HAEQ.special-additive-classes` is background and deliberately has narrower source-audit work.
- `HAEQ.direct-moe-to-holevo-transfer` is load-bearing and had the highest-leverage local gap.

The last node's previous product argument constructed an ensemble with Holevo value

\[
  2\log d-S_{\min}(N_1\otimes N_2),
\]

but did not explicitly prove the global identity

\[
 S_{\min}(N'_1\otimes N'_2)=S_{\min}(N_1\otimes N_2).
\]

Without that identity, citing the generic output-dimension upper bound for the extended product
channel leaves a logical gap. The rest of this note proves the identity over **all** inputs,
including inputs correlated with the label registers and inputs entangled across the two extended
channels.

## Exact channel definition

Let

\[
 N_i:\mathcal B(A_i)\longrightarrow\mathcal B(B_i),\qquad i\in\{1,2\},
\]

be finite-dimensional channels. Isometrically embed both output spaces in a common
`d`-dimensional space `B`. This padding does not change any output entropy, either singly or for
the product channel.

Let `Z` be a classical register of dimension `d^2`, with basis indexed by the discrete Weyl
operators \(\{W_z:z\in\mathbb Z_d^2\}\). Define the completely dephasing Weyl extension by

\[
 \widetilde N_i(\omega)
 =\sum_z W_z N_i(\omega_z)W_z^\dagger,
 \qquad
 \omega_z=(I_{A_i}\otimes\langle z|)\omega(I_{A_i}\otimes|z\rangle).
 \tag{1}
\]

Each \(\omega_z\) is positive and subnormalized, and
\(\sum_z\operatorname{Tr}\omega_z=1\). Equation (1) specifies the action on arbitrary input
operators, including off-diagonal label blocks: the latter are deleted.

## One-channel minimum-output entropy

For an arbitrary input state \(\omega\), put

\[
 p_z=\operatorname{Tr}\omega_z,
 \qquad
 \rho_z=\omega_z/p_z
\]

whenever \(p_z>0\). Then

\[
 \widetilde N_i(\omega)=\sum_{z:p_z>0}p_z W_zN_i(\rho_z)W_z^\dagger.
\]

Concavity of von Neumann entropy and unitary invariance give

\[
 \begin{aligned}
 S(\widetilde N_i(\omega))
 &\geq \sum_zp_z S(W_zN_i(\rho_z)W_z^\dagger)\\
 &=\sum_zp_z S(N_i(\rho_z))\\
 &\geq S_{\min}(N_i).
 \end{aligned}
 \tag{2}
\]

Conversely, choose a minimizing state \(\rho_i^*\) for \(N_i\) and any fixed label \(z_0\).
The input \(\rho_i^*\otimes|z_0\rangle\langle z_0|\) produces a unitary conjugate of
\(N_i(\rho_i^*)\). Hence

\[
 S_{\min}(\widetilde N_i)=S_{\min}(N_i).
 \tag{3}
\]

## Product-channel minimum-output entropy

Let \(\omega\) now be an arbitrary state on
\((A_1\otimes Z_1)\otimes(A_2\otimes Z_2)\). Its diagonal label blocks determine probabilities
\(p_{z_1,z_2}\) and conditional states \(\rho_{z_1,z_2}\) on \(A_1\otimes A_2\). Directly from
(1),

\[
 \begin{aligned}
 &(\widetilde N_1\otimes\widetilde N_2)(\omega)\\
 &\quad=\sum_{z_1,z_2}p_{z_1,z_2}
 (W_{z_1}\otimes W_{z_2})
 (N_1\otimes N_2)(\rho_{z_1,z_2})
 (W_{z_1}\otimes W_{z_2})^\dagger.
 \end{aligned}
 \tag{4}
\]

This formula does not assume that \(\omega\), or any conditional state
\(\rho_{z_1,z_2}\), is separable across the two channel inputs. Concavity and local-unitary
invariance therefore imply

\[
 \begin{aligned}
 S((\widetilde N_1\otimes\widetilde N_2)(\omega))
 &\geq\sum_{z_1,z_2}p_{z_1,z_2}
 S((N_1\otimes N_2)(\rho_{z_1,z_2}))\\
 &\geq S_{\min}(N_1\otimes N_2).
 \end{aligned}
 \tag{5}
\]

For the reverse inequality, take a joint minimizing state \(\rho_{12}^*\) for
\(N_1\otimes N_2\) and fixed labels \((z_1^0,z_2^0)\). Equation (4) then gives a local-unitary
conjugate of \((N_1\otimes N_2)(\rho_{12}^*)\). Thus

\[
 \boxed{
 S_{\min}(\widetilde N_1\otimes\widetilde N_2)
 =S_{\min}(N_1\otimes N_2).
 }
 \tag{6}
\]

No additivity assumption was used in (2)-(6).

## Consequence for the exact Holevo transfer

For any channel \(\Phi\) with output dimension `D`,

\[
 \chi(\Phi)\leq\log D-S_{\min}(\Phi).
 \tag{7}
\]

For \(\widetilde N_i\), the uniform ensemble consisting of one minimizing input and all `d^2`
labels has maximally mixed average output by the Weyl twirl and signal entropy
\(S_{\min}(N_i)\). Equations (3) and (7) therefore give

\[
 \chi(\widetilde N_i)=\log d-S_{\min}(N_i).
 \tag{8}
\]

For \(\widetilde N_1\otimes\widetilde N_2\), use a joint minimizing input and all `d^4` label
pairs. The average output is \(I_d/d\otimes I_d/d\), and every signal output has entropy
\(S_{\min}(N_1\otimes N_2)\). Equations (6) and (7), now with output dimension `d^2`, give

\[
 \chi(\widetilde N_1\otimes\widetilde N_2)
 =2\log d-S_{\min}(N_1\otimes N_2).
 \tag{9}
\]

Subtracting (8) from (9) proves exact numerical defect preservation.

## Scope and remaining gate

This argument is finite-dimensional and covers arbitrary input states of the extensions. It does
not say that the original Hastings channel pair itself violates Holevo additivity; the extensions
change the channels and multiply each input dimension by `d^2`. It also does not concern quantum
capacity or private capacity.

At the time of this snapshot the derivation remained proposer-side, and the new atomic preservation
claim and assembled direct-transfer route still required an independent hash-bound adversarial
review before promotion. That review subsequently passed; the canonical node YAML files record the
current `PROVED` statuses and their binding review evidence.

## Source checked

Peter W. Shor, *Equivalence of Additivity Questions in Quantum Information Theory*,
arXiv:quant-ph/0305035, Section 9, local PDF pp. 18-19. Shor defines the Weyl-labelled extension
and the minimizing-label ensemble there. The global lower-bound calculation (2)-(6) above is the
local completion of the specialization. Local PDF SHA-256:
`300a97664fe8d05531230cd6f3a812b23e2c2cbf22c429436e50442993f415d6`.
