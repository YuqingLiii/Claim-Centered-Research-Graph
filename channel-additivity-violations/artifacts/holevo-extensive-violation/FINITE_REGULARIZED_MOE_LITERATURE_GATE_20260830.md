# Finite-dimensional regularized-MOE literature gate

Date: 2026-08-30

Status: proposer-side primary-source scope audit; no completion-level review.

## Question

Do either of the following post-Collins--Youn results supply the missing all-tensor-power estimate
for one fixed finite-dimensional channel?

1. Kalantar--Shobeiri, arXiv:2501.15462; or
2. Magee--de la Salle, arXiv:2409.03626v2.

The answer is **no**. The first result remains in the infinite-dimensional commuting-operator
model. The second is a substantially stronger finite-matrix strong-convergence theorem, but its
order of quantifiers and its representation class do not establish a finite-dimensional
regularized minimum-output-entropy (`MOE`) defect.

## The regularized finite-dimensional quantifiers

For one fixed finite-dimensional channel `Phi_D`, the required quantity is

\[
 \overline S_{\min}(\Phi_D)
 =\inf_{r\ge 1}\frac1r S_{\min}(\Phi_D^{\otimes r}).
\]

Thus the matrix dimension `D` is fixed **before** the tensor exponent `r` is allowed to tend to
infinity. A theorem that controls every `r` after taking `D` sufficiently large as a function of
`r` proves finite-depth statements, but does not give this regularized quantity for any one finite
`D`.

## Kalantar--Shobeiri does not change the finite-dimensional status

Kalantar--Shobeiri state in the first page of the Introduction that additivity of regularized MOE
is still completely open, then describe Collins--Youn as giving the first concrete violation in
the infinite-dimensional commuting-operator setup. Their own channels again use left and right
regular representations on `ell_2(G)` and their Theorem 3 proves a regularized defect for the
composition of those commuting channels.

Consequently arXiv:2501.15462 enlarges the class of **infinite-dimensional commuting-operator**
examples; it does not provide a finite-dimensional tensor-product pair and does not bound the
self-regularization loss of the finite product-Haar blocks in this project.

Primary source: `primary-sources/kalantar-shobeiri-2501.15462.pdf`, PDF p. 1 and Theorem 3.
Local SHA-256:
`a2237d7b2383baed55a9f38e93ae5800c172b927bd968f24ec8e7c8e4be4db20`.

## Magee--de la Salle has the wrong order of limits for regularization

Magee--de la Salle Theorem 1.1 takes i.i.d. Haar matrices
`U_1^(n),...,U_m^(n) in U(n)` and proves, almost surely, strong convergence uniformly over
representations `pi_(k,l)` satisfying

\[
 k+\ell\le n^A,\qquad A<1/42,
\]

as `n` tends to infinity. Their Corollary 1.2 equivalently permits nontrivial irreducible
representations of dimension at most `exp(n^A)`. This is a major improvement over the earlier
`O(log n/log log n)` representation-degree range.

It still has the form

\[
 \lim_{n\to\infty}
 \sup_{k+\ell\le n^A}
 \left|\|\pi_{k,\ell}(p(U^{(n)}))\|-\|p(u)\|\right|=0.
\]

For every fixed finite `n`, the certified representation degree is finite. The theorem does not
assert one realization for which the estimate holds for all `k+ell`, so it cannot be sent through
the infimum over every tensor exponent in the definition of `overline S_min(Phi_D)`.

There is a second scope mismatch. `pi_(k,l)(p(U_1,...,U_m))` is a diagonal representation: the
same free-group word acts through the whole representation. A general centered output coefficient
for `Phi_D^tensor r` contains independently indexed factors

\[
 (U_{i_1}^*U_{j_1})\otimes\cdots\otimes(U_{i_r}^*U_{j_r}),
\]

and therefore ranges over the full repeated-channel coefficient system, not merely the diagonal
word subalgebra controlled by Theorem 1.1. An additional reduction would be required even inside
the theorem's growing-degree window.

Primary source: `primary-sources/magee-de-la-salle-2409.03626.pdf`, Theorem 1.1 and Corollary 1.2,
PDF pp. 3-5. Local SHA-256:
`873d0bd1d874635ef75b092185c044c0e051f927eb5747a5bedfc86495a7d589`.

## Consequence for the current proof

Neither source supplies the open node `HEXT.unbounded-family-self-leakage`. In particular, neither
justifies exchanging

\[
 \forall r\;\exists D(r)
 \quad\text{with}\quad
 \exists D\;\forall r.
\]

The first quantifier pattern is enough for the project's finite-dimensional **absolute-unbounded**
construction, because each target depth may choose a new finite dimension. The second is needed to
select one finite block with positive regularized cross defect and then tensor it indefinitely.

This is a theorem-scope obstruction, not evidence that finite-dimensional regularized MOE is
additive. The live mathematical gate remains a physical-output-specific all-copy estimate for one
fixed finite tuple, or a different construction whose gap pays for every added logarithmic
dimension.
