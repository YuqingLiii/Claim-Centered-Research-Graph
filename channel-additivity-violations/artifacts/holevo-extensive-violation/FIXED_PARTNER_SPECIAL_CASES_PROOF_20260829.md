# Fixed-partner entropy gate: exact special cases

Date: 2026-08-29  
Status: proposer-side derivation plus a primary-source specialization; independent review pending.

## Setting

For channels `Xi` and `Phi`, write

\[
S_{\min}(\Xi)=\min_{|\psi\rangle}S\!\left(\Xi(|\psi\rangle\langle\psi|)\right)
\]

and define the nonnegative minimum-output-entropy defect

\[
D(\Xi,\Phi)=S_{\min}(\Xi)+S_{\min}(\Phi)-S_{\min}(\Xi\otimes\Phi).
\]

The general fixed-partner gate asks whether `D(Xi,Phi_n)` tends to zero for every fixed
finite-dimensional `Xi` along the selected BCN random-channel family. This note records two
large classes for which the defect is identically zero for **every** partner and every `n`.

## Isometric fixed partners

Let `Xi(rho)=V rho V*` for an isometry `V`. Tensoring the output by the local isometry `V`
does not change its nonzero spectrum, so

\[
S_{\min}(\Xi\otimes\Phi)=S_{\min}(\operatorname{id}\otimes\Phi).
\]

For a pure input `|psi>_{RA}`, let `U:A -> B E` be a Stinespring isometry for `Phi`. The
post-isometry state on `RBE` is pure, hence

\[
S\!\left((\operatorname{id}_R\otimes\Phi)(\psi)\right)
=S\!\left(\Phi^c(\rho_A)\right),
\qquad \rho_A=\operatorname{Tr}_R\psi.
\]

The function `rho -> S(Phi^c(rho))` is concave. Its minimum over the compact convex state
space is attained at a pure state. On pure inputs the two complementary outputs have the same
nonzero spectrum, so

\[
\min_{\rho_A}S(\Phi^c(\rho_A))=S_{\min}(\Phi^c)=S_{\min}(\Phi).
\]

Therefore

\[
\boxed{S_{\min}(\Xi\otimes\Phi)=S_{\min}(\Phi)
=S_{\min}(\Xi)+S_{\min}(\Phi)}
\]

because an isometric channel has zero minimum output entropy.

This also explains a subtle point in Collins--Fukuda--Nechita: their limiting product-output
body may remain hard to describe even for an identity fixed partner, while its **minimum entropy**
is nevertheless exactly known.

## Entanglement-breaking fixed partners

Shor proves the stronger arbitrary-partner theorem: if `Xi` is entanglement breaking, then for
every channel `Phi`,

\[
\boxed{S_{\min}(\Xi\otimes\Phi)
=S_{\min}(\Xi)+S_{\min}(\Phi).}
\]

The proof uses the separable decomposition created by the entanglement-breaking output and
strong subadditivity. In the local primary-source copy, the concluding minimum-output-entropy
inequality and equality are on PDF page 3, equations (9)--(14). Page 4 begins the corresponding
Holevo theorem.

Primary source: `primary-sources/shor-eb-0201149.pdf`.

## Consequence for FCEA

For either class and for every sequence `Phi_n`,

\[
D(\Xi,\Phi_n)=0
\]

pointwise, so the limiting FCEA defect is zero without probability, asymptotics, or a
free-compression calculation. Replacer channels and unitary channels are contained in these
classes.

The unresolved gate is therefore narrower than “all fixed partners”: it begins with fixed,
finite-dimensional, non-entanglement-breaking, non-isometric channels. None of these exact
special cases controls that remaining class, and none supplies the dimension-dependent rate needed
for a full Hayden--Penington extensive construction.

## Audit boundary

This note does **not** prove FCEA-2 for a general fixed partner. CFN Theorem 8.1 proves existence
of the limiting product-output body, while the paper explicitly says that this body is difficult to
analyze in general. Existence of that body alone does not identify its minimum entropy.
