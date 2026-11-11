# Full-support probability at fixed channel dimensions

Date: 2026-08-30

Status: proposer-side conditional derivation. No claim is made about a particular Haar,
Stinespring, Grassmannian, or induced-channel ensemble.

## Question isolated

The phrase “counterexamples occur with positive probability” is ambiguous until both the
finite-dimensional ambient space and the sampling law are fixed. This note isolates the weakest
measure-theoretic hypothesis under which the existing open-set argument gives an exact qualitative
probability statement.

Fix finite input/output dimensions and let `K` be either

1. a single CPTP channel body, when self-additivity is being tested; or
2. a product of two CPTP channel bodies, when pair additivity is being tested.

In both cases `K` carries its relative finite-dimensional topology. Let `V_S` denote the set of
strict `p=1` minimum-output-entropy additivity violations and let `V_chi` denote the set of strict
Holevo additivity violations, with the relevant self or pair convention fixed once and for all.

Let `mu` be a Borel probability measure on `K` with full support:

\[
 \operatorname{supp}(\mu)=K.
\]

Equivalently in this compact metric space, every nonempty relatively open subset of `K` has
strictly positive `mu`-measure.

## Conditional dichotomy

For either `V=V_S` or `V=V_chi`, the following implication holds:

\[
 V\ne\varnothing \quad\Longrightarrow\quad 0<\mu(V)<1.
\tag{1}
\]

Consequently, for a full-support law at fixed dimensions,

\[
 \mu(V)=0 \quad\Longleftrightarrow\quad V=\varnothing.
\tag{2}
\]

The reverse alternative is not `mu(V)=1`: whenever a strict witness exists, the probability lies
strictly between zero and one.

## Proof of the implication

Assume `V` is nonempty.

1. `HCPREV.open-set-stability` asserts that every strict witness has a relatively open
   neighborhood consisting of strict witnesses. Hence `V` contains a nonempty relatively open
   subset `U`. Full support gives `mu(U)>0`, and therefore `mu(V)>0`.
2. `HCPREV.additive-open-region` supplies a nonempty relatively open set `A` of strongly additive
   channels or channel pairs. In the self-channel ambient space one can take the relative interior
   of the entanglement-breaking region. In the pair ambient space one can take the product of that
   relative interior in one factor with the entire partner channel body. In either case `A` is
   disjoint from `V`.
3. Full support gives `mu(A)>0`. Thus

   \[
   \mu(V)\le 1-\mu(A)<1.
   \]

This proves (1). If `V` is empty then `mu(V)=0`, which together with (1) proves (2).

The same argument for normalized intrinsic Lebesgue measure recovers the familiar statement that
both the violation region (when nonempty) and an additive region have positive measure.

## What full support does not quantify

Full support supplies no dimension-uniform numerical lower bound on `mu(V)` and no numerical upper
bound separated from one. Across a sequence `(K_d,mu_d)`, the probabilities may tend to zero, tend
to one, or do neither while every `mu_d` has full support. Quantitative asymptotics require
model-specific geometry or concentration estimates.

In particular:

- a Haar/Stinespring pushforward with a fixed environment dimension may be supported only on a
  proper subset of the full CPTP body;
- full support on that proper subset is not full support on `K`;
- high probability in a named random ensemble does not imply density, residuality, or full
  intrinsic measure in `K`; and
- the statement does not transfer a minimum-output-entropy witness to a Holevo witness for the
  same sampled channel pair.

Thus (1) is a fixed-dimensional qualitative bridge between topology and probability, not a
replacement for the ensemble-specific Hastings/ASW/BCN/LLW probability theorems.

## Audit of the eight pre-existing canonical nodes

The following audit was performed before registering the bridge.

| Canonical node | Quantifier boundary retained |
|---|---|
| `HCPREV.goal` | The root is a classification request, not a theorem asserting one universal notion of prevalence. |
| `HCPREV.random-models` | Every probability statement remains attached to a named ensemble, witness, dimension scaling, and limit order. |
| `HCPREV.product-haar-unbounded` | The order is `for every G, choose fixed J, then let per-leg dimension tend to infinity`; it is proposer-side. |
| `HCPREV.open-set-stability` | The conclusion is fixed-dimensional relative openness and intrinsic positive measure, not density or high probability. |
| `HCPREV.additive-open-region` | An additive relative-open region rules out density, residuality, and full intrinsic measure in the whole fixed-dimensional ambient space. |
| `HCPREV.algebraic-witness-existence` | Semidecidable algebraic existence is not a printed or feasibly checkable explicit witness. |
| `HCPREV.explicit-witness-frontier` | A concrete deterministic matrix tuple with a rigorous global certificate remains open in this repository. |
| `HCPREV.dimension-threshold-scope` | `182/183` are model/criterion thresholds, not a global minimum over all finite-dimensional channels. |

No status promotion follows from this audit. The new bridge remains conditional on two
`CONJECTURED` proposer-side premises.
