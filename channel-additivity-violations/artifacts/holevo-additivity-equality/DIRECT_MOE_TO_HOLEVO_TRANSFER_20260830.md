# Direct finite-dimensional MOE-to-Holevo transfer from Shor Section 9

Date: 2026-08-30

Status: historical pre-review proposer-side specialization of Shor's explicit construction. The
exact transfer claim was subsequently independently reviewed and promoted to `PROVED`; its
canonical YAML is authoritative for current status.

All logarithms are base two.

## Statement

Let `N_1,N_2` be finite-dimensional channels. After isometrically embedding their outputs into a
common `d`-dimensional output space, Shor's Section 9 construction produces finite channels
`N'_1,N'_2` such that

\[
 \chi(N'_i)=\log d-S_{\min}(N_i),\qquad i=1,2,
\tag{1}
\]

and

\[
 \chi(N'_1\otimes N'_2)=2\log d-S_{\min}(N_1\otimes N_2).
\tag{2}
\]

Consequently the numerical pair defect is preserved exactly:

\[
\begin{aligned}
 &\chi(N'_1\otimes N'_2)-\chi(N'_1)-\chi(N'_2)\\
 &=S_{\min}(N_1)+S_{\min}(N_2)-S_{\min}(N_1\otimes N_2).
\end{aligned}
\tag{3}
\]

The extension changes the channels. It does not assert that the original Hastings random pair has
nonadditive Holevo quantity.

## Construction

Let `{W_z:z in Z_d^2}` be the discrete Weyl operators. Define `N'_i` on the original input plus a
classical `d^2`-symbol register by

\[
 N'_i(\rho\otimes|z\rangle\langle z|)=W_zN_i(\rho)W_z^*.
\tag{4}
\]

Off-diagonal blocks of the classical register are deleted. The Weyl twirl obeys

\[
 \frac1{d^2}\sum_zW_z\sigma W_z^*=\frac{I_d}{d}.
\tag{5}
\]

## One-channel identity

For every channel with `d`-dimensional output,

\[
 \chi(\Phi)\le\log d-S_{\min}(\Phi),
\tag{6}
\]

because the average output entropy is at most `log d` and every signal-state output entropy is at
least `S_min(Phi)`.

Choose a pure input minimizing `S_min(N_i)`, attach each classical Weyl label with probability
`1/d^2`, and use (5). The average output is maximally mixed while every signal output has entropy
`S_min(N_i)`. Hence (6) is attained and gives (1).

## Product identity

The output-dimension upper bound for the extended product channel requires the global identity

\[
 S_{\min}(N'_1\otimes N'_2)=S_{\min}(N_1\otimes N_2),
\]

including inputs correlated with the classical labels. The arbitrary-input block decomposition,
entropy-concavity lower bound and fixed-label achievability are proved in
`WEYL_EXTENSION_GLOBAL_MOE_PRESERVATION_20260830.md`. This is the load-bearing step that makes the
following achievability argument an exact identity rather than only a lower bound.

Choose a pure joint input minimizing `S_min(N_1 tensor N_2)`. Attach every pair of Weyl labels
`(z_1,z_2)` uniformly. The local twirls make the average joint output `I_d/d tensor I_d/d`, whose
entropy is `2 log d`; every signal output is a local-unitary conjugate of the minimizing joint
output. The universal output-dimension upper bound is therefore attained for the product channel,
which proves (2).

Subtracting the one-channel identities proves (3).

## Finite-dimensionality and role in the root proof

Each extension multiplies the input dimension by `d^2` and leaves the padded output dimension
equal to `d`, so all spaces remain finite. Applying this construction to the finite Hastings MOE
pair gives a finite Holevo-nonadditive pair with the same positive numerical gap. The local
Fukuda--Wolf direct-sum proof then converts that pair into one channel `T` with

\[
 \chi(T^{\otimes2})>2\chi(T),
\]

and therefore `C(T)>chi(T)`.

This direct route is stronger and more witness-transparent than using only the contrapositive of
Shor's universal equivalence theorem.

## Primary source

Peter W. Shor, *Equivalence of Additivity Questions in Quantum Information Theory*,
arXiv:quant-ph/0305035, Section 9, local PDF pp. 18--19. Local SHA-256:
`300a97664fe8d05531230cd6f3a812b23e2c2cbf22c429436e50442993f415d6`.
