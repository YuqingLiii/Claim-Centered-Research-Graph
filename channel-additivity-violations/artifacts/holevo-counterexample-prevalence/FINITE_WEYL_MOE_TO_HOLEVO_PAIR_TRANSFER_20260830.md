# Finite dephasing-Weyl transfer from a p=1 MOE pair defect to a Holevo pair defect

Date: 2026-08-30

Status history: written as a Q2-local proposer-side proof while the canonical atom was
`CONJECTURED`; the canonical atom was subsequently upgraded to `PROVED` by the hash-bound review
recorded in the node YAML. This artifact is historical evidence, not a live status authority.
The transformation is deterministic and does not say that the original sampled channels
themselves have the transferred Holevo defect.

All logarithms are base two.

## 1. Exact statement

Let

\[
 N_i:\mathcal B(A_i)\longrightarrow\mathcal B(B_i),\qquad i=1,2,
\]

be arbitrary finite-dimensional channels. Isometrically embed `B_1` and `B_2` into a common
`d`-dimensional output space `B`. Padding by an output isometry preserves every output spectrum,
including spectra of the product channel.

There are explicit finite-dimensional dephasing-Weyl extensions `tilde(N_i)` such that

\[
 S_{\min}(\widetilde N_i)=S_{\min}(N_i),\qquad i=1,2,          \tag{1}
\]

\[
 S_{\min}(\widetilde N_1\otimes\widetilde N_2)
 =S_{\min}(N_1\otimes N_2),                                  \tag{2}
\]

and

\[
 \chi(\widetilde N_i)=\log_2d-S_{\min}(N_i),                 \tag{3}
\]

\[
 \chi(\widetilde N_1\otimes\widetilde N_2)
 =2\log_2d-S_{\min}(N_1\otimes N_2).                         \tag{4}
\]

Consequently the numerical pair defect is preserved exactly:

\[
 \chi(\widetilde N_1\otimes\widetilde N_2)
 -\chi(\widetilde N_1)-\chi(\widetilde N_2)
 =S_{\min}(N_1)+S_{\min}(N_2)-S_{\min}(N_1\otimes N_2).     \tag{5}
\]

## 2. Exact Shor Section 9 interface

Shor considers two finite channels with outputs embedded in the same `d`-dimensional space. For
the generalized Pauli/Weyl family indexed by `z=da+b`,

\[
 W_z=T^aR^b,\qquad 0\le z<d^2,
\]

Section 9 defines the labelled action

\[
 N_i'(\rho\otimes|z\rangle\langle z|)
 =W_zN_i(\rho)W_z^*.                                        \tag{6}
\]

For one minimum-output input, Shor uses all `d^2` labels uniformly; for a lower-entropy joint
input of `N_1 tensor N_2`, he uses all `d^4` label pairs uniformly. The generalized Pauli average
is maximally mixed, so these ensembles attain the output-entropy upper bounds once the global
minimum-output entropies of the extensions are identified.

Local source:
`artifacts/primary-sources/shor-quant-ph-0305035.pdf`, Section 9, PDF pp. 18--19. The source defines
the classical-labelled action and the two uniform orbits. The arbitrary-input dephasing completion
and global identities (1)--(2) are supplied below rather than silently attributed to Shor.

## 3. Completely dephasing CPTP extension

Let `Z` be a `d^2`-dimensional label register with basis `|z>`. Define, on every input operator
`omega` on `A_i tensor Z`,

\[
 \widetilde N_i(\omega)
 =\sum_z W_zN_i(\omega_z)W_z^*,
 \qquad
 \omega_z=(I_{A_i}\otimes\langle z|)\omega
           (I_{A_i}\otimes|z\rangle).                       \tag{7}
\]

This first completely dephases/measures the label, applies `N_i`, and conjugates by the selected
Weyl unitary. Hence it is completely positive and trace preserving. Off-diagonal label blocks are
discarded; equation (7) is not a coherence-preserving controlled channel.

## 4. Global one-channel minimum-output entropy

For any input state `omega`, let `p_z=Tr(omega_z)` and, when `p_z>0`, let
`rho_z=omega_z/p_z`. Then

\[
 \widetilde N_i(\omega)=\sum_zp_zW_zN_i(\rho_z)W_z^*.
\]

Entropy concavity and unitary invariance give

\[
 S(\widetilde N_i(\omega))
 \ge\sum_zp_zS(N_i(\rho_z))
 \ge S_{\min}(N_i).                                        \tag{8}
\]

Conversely, attach any fixed label to a minimizing input of `N_i`; its output is a unitary
conjugate of the minimizing output. This proves (1) over all label-coherent inputs.

## 5. Global product minimum-output entropy

Let `omega` be an arbitrary state on
`(A_1 tensor Z_1) tensor (A_2 tensor Z_2)`, including states entangled across the two channel
inputs and coherent or correlated across the labels. Its diagonal label blocks give probabilities
`p_(z_1,z_2)` and conditional states `rho_(z_1,z_2)` on `A_1 tensor A_2`. Directly from (7),

\[
 (\widetilde N_1\otimes\widetilde N_2)(\omega)
 =\sum_{z_1,z_2}p_{z_1,z_2}(W_{z_1}\otimes W_{z_2})
 (N_1\otimes N_2)(\rho_{z_1,z_2})
 (W_{z_1}\otimes W_{z_2})^*.                               \tag{9}
\]

Entropy concavity gives the lower bound `S_min(N_1 tensor N_2)`. A joint minimizing input with
any fixed label pair gives the reverse inequality. Thus (2) is a global equality and does not
assume MOE additivity.

## 6. Exact Holevo identities

Every channel `Phi` with output dimension `D` satisfies

\[
 \chi(\Phi)\le\log_2D-S_{\min}(\Phi),                       \tag{10}
\]

because the average output entropy is at most `log_2 D` and each signal output entropy is at least
the global minimum.

The discrete Weyl twirl is

\[
 {1\over d^2}\sum_zW_z\sigma W_z^*=I_d/d.                  \tag{11}
\]

Choose one minimizing input of `N_i` and use every label uniformly. Each signal output has entropy
`S_min(N_i)`, while (11) makes the average output maximally mixed. The upper bound (10) is attained,
which proves (3).

For the product, choose one joint minimizing input of `N_1 tensor N_2` and all label pairs
uniformly. Equation (11) on both legs makes the average output `I_d/d tensor I_d/d`; every signal
output is a local-unitary conjugate of the joint minimizing output. Equation (2) and (10), now for
output dimension `d^2`, prove (4). Subtraction proves (5).

## 7. Conjugate-pair balance and transformed law

If `N_2=bar(N_1)`, then `S_min(N_2)=S_min(N_1)` because conjugating both the channel and input
conjugates the output spectrum. Equations (3) therefore give

\[
 \chi(\widetilde N_1)=\chi(\widetilde N_2).                 \tag{12}
\]

Applied sample-by-sample to a random channel pair, the construction is deterministic and finite
dimensional. An event defined by the original MOE defect is exactly the corresponding event for
the transformed Holevo pair defect by (5). Thus its probability is preserved under the
pushforward law of the Weyl transformation. The transformed law is not the original product-Haar
law on the original sampled channels and is not asserted to be Haar or full-support on a CPTP
body.

## 8. Dimensions and strict boundary

The common padded output dimension of each extension is `d`. The label multiplies the input
dimension of `N_i` by `d^2`; all spaces remain finite.

This atom proves only a pair transfer. It does not produce a same-channel witness, does not retain
the original sampled channel identities or dimensions, and gives no quantum/private-capacity or
full-size extensive conclusion. Those scopes require separate nodes.

## 9. Review gate

A fresh independent reviewer must verify the Shor PDF interface, CPTP completion, all arbitrary
label-correlated and cross-channel-entangled inputs in (8)--(9), both global minimum identities,
the Weyl twirl, the one-channel and product Holevo upper-bound attainments, defect sign and the
pushforward-law boundary before the new atom may be promoted.

## 10. Registered exact hash

The repository-normalized exact claim hash of
`HCPREV.finite-weyl-moe-to-holevo-pair-transfer` is

`sha256:5141db41a2972b86e9fbf83419dbfb5e739e4cb98656ec64c721858f6d793a9c`.

This is a route-free local direct proof with one exact external Shor interface; no artificial
route hash is registered.
