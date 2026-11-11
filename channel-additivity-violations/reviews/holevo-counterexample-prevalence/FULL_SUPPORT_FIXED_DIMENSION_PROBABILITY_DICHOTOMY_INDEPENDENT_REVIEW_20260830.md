# Independent review: fixed-dimensional full-support probability dichotomy

Date: 2026-08-30

Reviewer: independent Codex review context `/root/q2_probability_review`.

## Independence declaration and scope

I did not author
`artifacts/FULL_SUPPORT_FIXED_DIMENSION_PROBABILITY_DICHOTOMY_20260830.md`,
`artifacts/STABILITY_AND_MEASURE_PROOF_20260829.md`,
`artifacts/ADDITIVE_OPEN_REGION_PROOF_20260829.md`, or any of the three canonical
nodes reviewed below. I read `DAG_PROTOCOL.md` and `FILE_PROTOCOL.md` in full and
made no change to any proposer artifact or canonical node.

This review checks the exact fixed-dimensional CPTP topology, the definition of full
support, measurability and positive mass of nonempty relative-open sets, openness of the
strict minimum-output-entropy and one-shot Holevo violation sets, the existence of a
disjoint relative-open entanglement-breaking region for both the self-channel and
two-channel conventions, and every probability quantifier in the proposed dichotomy. It
also checks that no pointwise transfer between minimum output entropy and Holevo quantity
is used.

The following local primary-source pages were inspected directly:

- Audenaert, `artifacts/primary-sources/audenaert-0610146.pdf`, Theorem 1, PDF p. 2;
- Shor, `artifacts/primary-sources/shor-eb-0201149.pdf`, Theorems 1 and 2, PDF pp. 2--5;
- Gurvits--Barnum, `artifacts/primary-sources/gurvits-barnum-0204159.pdf`, setup and
  Theorem 1 / Corollary 3, PDF pp. 1--5.

This review does not examine the named random-channel ensembles or their asymptotic
probabilities. They are not premises of the fixed-dimensional full-support statement.

## Executive verdict

The elementary probability implication is mathematically correct once the two stated
topological premises are available. For a fixed self-channel body or a fixed product of
two channel bodies, the strict violation set is Borel and relative open; a nonempty such
set has positive mass under every full-support Borel probability. A nonempty relative-open
entanglement-breaking additive set is Borel, disjoint from the violation set, and also has
positive mass. Hence a nonempty violation set has probability strictly between zero and
one, while the empty set has probability zero.

The self/pair quantifiers are correct. In the self-channel ambient space, any channel in
the relative interior of the entanglement-breaking set is additive with itself. In the
pair ambient space,

```text
relint(EB(A -> B)) x C(C -> D)
```

is a nonempty relatively open subset of the product and Shor's theorems make every pair
in it additive for both minimum output entropy and one-shot Holevo quantity. The whole
second factor is open in its own relative topology. No minimum-output-entropy witness is
transferred to a Holevo witness.

However, **no reviewed node is currently eligible for `PROVED`**. Both load-bearing
premise nodes are route-free direct proofs that use external theorems and model facts but
have no canonical `assumptions` block. This violates the machine-visible input requirement
in `DAG_PROTOCOL.md` Sections 2 and 6. In addition, the written continuity modulus uses
`log_2(d-1)` without separately treating output dimension `d=1`, whereas the exact claim
says all fixed finite dimensions. That edge case is harmless mathematically--no strict
violation can exist when a relevant output is one-dimensional--but the current proof does
not state the branch or restrict the claim to output dimensions at least two.

The required disposition is therefore:

- mathematical implication and topology analysis: **PASS**;
- exact current completion dossier: **FAIL**;
- `HCPREV.open-set-stability`: remain `CONJECTURED`;
- `HCPREV.additive-open-region`: remain `CONJECTURED`;
- route `open-violation-and-open-additive-complement`: remain `CONJECTURED` under the
  instruction that all load-bearing premises must first be certified;
- `HCPREV.full-support-probability-dichotomy`: remain `CONJECTURED`.

No conclusion here supplies a dimension-uniform probability bound, a probability law on a
disjoint union of dimensions, or an ensemble-specific probability theorem.

## Immutable inputs and exact statement hashes

The exact bytes inspected were:

| object | SHA-256 |
|---|---|
| `DAG_PROTOCOL.md` | `d8775b511431e6e9dc7a5be6200af80bd612e7e7d5f5ff10bb14ef748791a095` |
| `FILE_PROTOCOL.md` | `d9d6fb57a26fef3b70fc05bda74a29101d83a43df60e06eaeb345e76980fc595` |
| full-support proposer artifact | `f9e55d086e9b9fbd2929c0b822b64ff3f2ae37b55d1e6a0482e7a06ea8e4f80e` |
| stability proposer artifact | `2c37f467940913cea6d2197e963de1916f697a0d4f964d27f033b5d250801fc4` |
| additive-region proposer artifact | `8fa6b701a9ca658ae8b091a685effc8ecb8010465a75882dae3258ed40ecc528` |
| proposer topology audit | `6b15702d154c2b4cdc859c1f65ca97aa38c5ea272202493e7d178d7c99d0bc45` |
| primary-source audit | `6435d74e4da92db4e0e97c490cf6ec937b0c937420aebb0ecb9c474d51a3b246` |
| Audenaert PDF | `dc2265209fd7fb86aa7ce03a541c15d8b9f5a29b70c281728650eef0ad87bdb7` |
| Shor EB PDF | `9e68b70e36383ceb42dbbfbd3cefdbad0d5757ee76941f1d590b6c15cefcbca4` |
| Gurvits--Barnum PDF | `c35027eb1e981bf70b2767c229daac7812d3226773ad5d0f7a7a335c363adf85` |

The exact current claim and implication hashes are:

| canonical object | exact hash |
|---|---|
| `HCPREV.open-set-stability` claim | `sha256:5e48fcbc53334cc32e190854c3339a1c042116b5da998f877b152d81c3dd4310` |
| `HCPREV.additive-open-region` claim | `sha256:9d5a1f22a2f633e0b931441177a99c8b704b63fef0a3ad7ca99c190db9adb9a4` |
| `HCPREV.full-support-probability-dichotomy` claim | `sha256:4cf4c6718cac0081c6dd806e0042d2f908caa2ecc9819972de0ce05c44a54178` |
| route `open-violation-and-open-additive-complement` implication | `sha256:10eadfd4851f1fb6637ef01f264598c54a33223ef8583deda567b6ab7981461a` |

## Finding HCP-FS-IR-01 -- PASS: topology and support equivalence

For fixed finite dimensions, the CPTP set is a compact convex subset of the finite-dimensional
real affine space of Hermiticity-preserving trace-preserving maps. The diamond norm induces
the same topology as any other norm on this affine hull. A product of two such bodies is again
compact metrizable in the product topology.

For a Borel probability `mu` on a metric space `K`, `supp(mu)=K` is equivalent to every
nonempty relatively open subset of `K` having positive `mu`-measure. One direction follows
from the neighborhood definition of support. Conversely, a point outside the support has an
open neighborhood of measure zero. No compactness is needed for this equivalence, although it
is available here.

Both violation and additive regions used below are relative open, hence Borel. Thus every
displayed probability is defined.

**Verdict:** PASS for the topology and measure-theoretic interface used by the route.

## Finding HCP-FS-IR-02 -- PASS with one written edge-case repair: strict violation sets are open

For a pair `(N,M)`, define

```text
g_S(N,M)   = S_min(N) + S_min(M) - S_min(N tensor M),
g_chi(N,M) = chi(N tensor M) - chi(N) - chi(M).
```

Audenaert's theorem and diamond-norm contraction give a uniform entropy modulus over all
input states. It passes through the infimum defining `S_min`. For a fixed input ensemble,
both terms of its Holevo information change by at most the entropy modulus; the uniform
factor-two estimate therefore passes through the supremum defining `chi`. The tensor estimate

```text
(1/2)||N tensor M - N' tensor M'||_diamond
    <= (1/2)||N-N'||_diamond + (1/2)||M-M'||_diamond
```

follows from the tensor multiplicativity of the diamond norm and norm one of CPTP maps.
Consequently both gap functions are continuous, and their strict-positive inverse images are
relative open.

The self-channel version is the restriction to the continuous diagonal map `N -> (N,N)`;
hence its violation set is also relative open. This removes any possible self/pair quantifier
ambiguity.

The written formula `f_d(eps)=eps log_2(d-1)+h_2(eps)` is undefined at `d=1`. The exact claim
allows arbitrary finite output dimensions. The repair is elementary and does not change the
claim: either state explicitly that a one-dimensional output admits no strict violation and
treat it separately, or state the modulus only for `d>=2`. Until this branch is written, the
artifact is not literally complete over the full claimed range.

**Verdict:** mathematical claim PASS; current completion dossier FAIL because of the missing
`d=1` branch and missing canonical assumptions described in Finding HCP-FS-IR-06.

## Finding HCP-FS-IR-03 -- PASS: relative-open implies positive intrinsic measure

The depolarizing channel is in the relative interior of the CPTP body. If `U` is a nonempty
relative-open subset of a convex body `K`, choose `x in U` and `y in relint(K)`. For sufficiently
small positive `t`, `(1-t)x+ty` stays in `U`, while the standard convex relative-interior lemma
puts it in `relint(K)`. A sufficiently small affine ball around that point lies in `U`, so `U`
has positive Lebesgue measure in `aff(K)`. The same proof applies to a product body.

This intrinsic-Lebesgue conclusion is separate from, and not needed for, the arbitrary
full-support probability conclusion except as a special example.

**Verdict:** PASS. It proves neither density nor an asymptotic probability bound.

## Finding HCP-FS-IR-04 -- PASS: nonempty relative-open strongly additive region

For a channel `Phi:A->B`, the normalized Choi matrix obeys
`Tr_B rho_Phi=I_A/d_A`. The depolarizing Choi state
`I_A/d_A tensor I_B/d_B` is the center of the Gurvits--Barnum separable ball and belongs to
this affine slice. Intersecting a sufficiently small Frobenius ball with the trace-preserving
slice gives a nonempty relative neighborhood made entirely of separable Choi states. By the
Choi/measure-and-prepare equivalence, these are entanglement-breaking channels.

Shor's Theorem 1 states, for every finite channel `Psi` and every entanglement-breaking `Phi`,

```text
S_min(Psi tensor Phi)=S_min(Psi)+S_min(Phi).
```

Shor's Theorem 2 states in the same quantifier regime

```text
chi(Psi tensor Phi)=chi(Psi)+chi(Phi).
```

The second theorem is about the one-shot Holevo quantity `chi*`, exactly the quantity used in
the reviewed claim; it is not being silently replaced by a regularized classical capacity.

Thus `relint(EB)` is disjoint from both self-violation sets, and
`relint(EB) x C` is disjoint from both pair-violation sets. Both sets are nonempty and relative
open in their respective ambient spaces.

**Verdict:** mathematical claim PASS. The current canonical node still lacks machine-visible
external assumptions and is therefore not eligible for completion.

## Finding HCP-FS-IR-05 -- PASS: exact probability dichotomy and logical quantifiers

Let `V` be either one fixed MOE violation set or one fixed Holevo violation set under one fixed
self/pair convention. If `V` is nonempty, Findings HCP-FS-IR-01--04 give a nonempty open
`U subseteq V` and a nonempty open `A subseteq K\V`. Full support implies
`mu(U)>0` and `mu(A)>0`. Hence

```text
0 < mu(V) <= 1-mu(A) < 1.
```

If `V` is empty then `mu(V)=0`. Combining the two cases gives
`mu(V)=0` if and only if `V` is empty. The argument never says `mu(V)=1` when a witness exists,
never compares different dimensions, and never transfers a MOE witness, open set, or law to
Holevo.

**Verdict:** the implication at
`sha256:10eadfd4851f1fb6637ef01f264598c54a33223ef8583deda567b6ab7981461a`
and target claim at
`sha256:4cf4c6718cac0081c6dd806e0042d2f908caa2ecc9819972de0ce05c44a54178`
are mathematically correct. They are not eligible for `PROVED` until both canonical premises
become completion-level claims.

## Finding HCP-FS-IR-06 -- BLOCKER: external assumptions are not machine-visible

`HCPREV.open-set-stability` is a route-free direct proof and uses at least:

1. Audenaert's exact entropy continuity theorem;
2. output trace-distance control by diamond distance;
3. multiplicativity of diamond norm under tensor products and diamond norm one for CPTP maps.

`HCPREV.additive-open-region` is a route-free direct proof and uses at least:

1. the Gurvits--Barnum separable Frobenius ball for arbitrary finite bipartite dimensions;
2. the equivalence between separable normalized Choi states and entanglement-breaking channels;
3. Shor's strong additivity Theorems 1 and 2 for an arbitrary finite partner.

Neither node has an `assumptions` block. Listing PDFs under a prose artifact or under generic
`basis.evidence` is not the canonical registry required by `DAG_PROTOCOL.md`. Before any
completion-level promotion, each imported theorem/model fact must be registered on the node with
its exact statement, regime, and repository-relative source/locator. The standard diamond-norm
and Choi facts must either be proved locally in a linked artifact or registered as sourced model
facts.

This is a protocol blocker, not a mathematical counterexample. Adding assumptions without changing
the claim statements would preserve the exact reviewed claim hashes above, but the added statements
must match the scope audited here.

**Verdict:** FAIL for current completion-level promotion of both premises and therefore of the
target node.

## Finding HCP-FS-IR-07 -- PASS: no MOE/Holevo conflation

The proof is duplicated parametrically for `V_S` and `V_chi`; it does not invoke Shor's universal
equivalence theorem and does not map one violation set into the other. Shor's entanglement-breaking
paper is used only to exhibit a common additive complement, through two separate theorems. The
random-ensemble caveats correctly remain outside the route.

**Verdict:** PASS. No same-channel, same-pair, same-dimension, or same-law Holevo consequence is
inferred from a MOE result.

## Required repair before re-review or promotion

1. Add exact node-level `assumptions` blocks to both route-free premise nodes, with the primary
   source paths and theorem locators listed above.
2. Register or prove the diamond-norm facts and Choi/entanglement-breaking equivalence instead of
   leaving them implicit.
3. Add the `d=1` branch to the stability artifact or narrow the stability claim to output
   dimensions at least two. The former preserves the intended exact claim.
4. Link an independent completion finding from each repaired premise node at the exact claim hash.
5. Only after both premises are `PROVED` should the probability route and target node be considered
   for `PROVED`.

No proposer artifact needs to be deleted or replaced; the gaps are local, auditable repairs.

## Limitations

This review establishes no lower bound on `mu(V)` other than strict positivity, no upper bound
uniformly separated from one, no conclusion for measures whose support is a proper subset of the
ambient channel body, and no asymptotic statement as channel dimensions vary. It does not review
whether any strict witness exists in a particular fixed dimension.
