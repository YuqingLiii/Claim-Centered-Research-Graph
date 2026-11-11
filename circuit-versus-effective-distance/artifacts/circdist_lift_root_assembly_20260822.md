# `CIRCDIST.lift` — the root composition proof, assembled

**Node:** `CIRCDIST.lift` (root) · **Date:** 2026-08-22 · **Role:** Opus 5 executor, proposer.
**Box:** one session, stop-loss binding. No sub-agents. No Lean. No proof-DAG object touched.

**What this document is.** The parent obligation of the route `criterion-corollary-example` is the
implication

> `CIRCDIST.lift.iff` **and** `CIRCDIST.lift.nonint` **and** `CIRCDIST.lift.gap-example`
> jointly establish the `CIRCDIST.lift` root claim.

The node currently records that implication only as a blueprint ("assembling them is definitional
bookkeeping plus consistency of the three formalizations"). This document writes the implication
out so it can be reviewed: it restates the root claim, splits it into clauses, maps each clause to
the **certified claim text** of the child that discharges it, does the scope arithmetic that the
blueprint deferred, carries forward the child caveats, and ends with the checklist a completion
review of the **root** must run.

**Epistemic ceiling (binding on every line below).** Nothing here is labelled PROVED or
CERTIFIED\*. The assembly argument is **CONJECTURED**; the one computation is **NUMERICAL** with
its code inline (§9). This session is a proposer and cannot grant itself a completion level. The
three children's `CERTIFIED*` levels are read off the canonical node records; this document does
not re-certify them and does not re-review their contents.

**One finding stated up front.** The blueprint's phrase *"definitional bookkeeping"* is accurate
for four of the five root clauses and **inaccurate for the fifth**. The existence clause (the
explicit interleaved `d_circ > d_eff` example) does not descend into the root's graph-like
restriction for free, because existence statements do not restrict downward. Resolving it required
a computation, which §4.3 performs: the `[[4,2,2]]` witness **is** graph-like in both sectors
(schedule-independently, because its detector sector has a single check), so the clause survives
inside the restriction; the stronger Steane witness is **not** graph-like and therefore
corroborates only the unrestricted reading. The assembly is complete, but not by bookkeeping alone.

---

## 0. Inputs, hash chain, and what "may be used"

### 0.1 Bound inputs

Recomputed from the current bytes this session (`shasum -a 256`):

```text
root node        research/circdist/proof-dag/nodes/CIRCDIST.lift.yaml
                 64963af70bf27195987bc3ce58319b36d24aeb66ce975823f334779e13223de5   4746 B,  94 L
child nodes      research/circdist/proof-dag/nodes/CIRCDIST.lift.iff.yaml
                 6f6ea03fe546775f4447707c10fc3e0b26b67a941646f81445f5867b01b22c23  11275 B, 187 L
                 research/circdist/proof-dag/nodes/CIRCDIST.lift.nonint.yaml
                 2675c3b6027e41719c3e6933b260f6ca8f4fadf3b68d55ffd85962221e33ee90   5420 B,  93 L
                 research/circdist/proof-dag/nodes/CIRCDIST.lift.gap-example.yaml
                 67c0e106cac34ed73a9e0cf1e19783ba58b10f7d0a6a7d69b495d896f715106f   6421 B, 106 L

iff dossier      artifacts/circdist_lift_iff_proof_20260820.md
                 97cb3c8da839d1b96f58c281145cec8b70269ed3e6dfb29136f0bda00f564979  90225 B, 1497 L
                 artifacts/circdist_lift_iff_amendment1_20260820.md
                 7220d538a9ee680711f591de30dbcc52bb80aa669a778ed3468cc9781c80a467  34143 B,  618 L
                 artifacts/circdist_lift_iff_amendment2_20260820.md
                 0ab3ce438fe6a3971be43a7090518087a9bd06566345d33326ca8e3e19079603  11783 B,  239 L
nonint dossier   artifacts/circdist_lift_nonint_proof_20260820.md
                 42d6c138c1ea19127db76ab4f22d2a64c1d1e1e96adf76af975076b529a71f4c  58543 B,  942 L

reviews          artifacts/circdist_lift_proofs_review_20260820.md      (base, Opus 5)
                 fa75f0405a9e233cc45aae2cf01458caef45d65cfef9bc0a44cbca19f0d0189f  45878 B,  703 L
                 artifacts/circdist_amendments_review_20260820.md       (focused rereview, Opus 5)
                 daa476804959fec7a39c5aedd0ed8191c4b495a670dd83f58aeb5a7247fcd90c  36265 B,  570 L
                 artifacts/circdist_amendments2_review_20260820.md      (completion review)
                 7b7ac0d5c78968ccf194fe176196d79d275fd82df79a3d3bb7f5666ead931842  21003 B,  361 L
                 artifacts/circdist_numerical_review_20260820.md        (gap-example, Opus 5)
                 b542aea1da06e489dccce2d9b689ad5c608a20ffd28399cb7017144821bc54ee 104455 B, 2245 L

context          artifacts/circdist_lift_d3gate_20260820.md
                 882bdf2a922d51c4e0ddc056840c5c8694960423a07581871962c340343d185f  53117 B, 1169 L
frozen defs      research/circdist/notes/CIRCDIST_PROBLEMS.md          (not modified)
                 5f6dc37fcc33c0eb9f90e6267864740fc53b65c4acf1ee870c8d29ffd6d46c64  10199 B,  243 L
```

The three Amendment-1/Amendment-2 hash chains and the amendment-2 review's §1.1 table all
reproduced against these bytes, with the single expected exception that the amendment-2 review does
not hash itself. If any hash above fails to reproduce, this assembly is void until re-derived.

### 0.2 Claim-hash freshness of the three children (NUMERICAL, §9.1)

Under the repository convention `sha256(claim.replace("\r\n","\n").strip().encode("utf-8"))`:

| child | level | recomputed claim hash | equals the recorded `reviewed_hash`? |
|---|---|---|---|
| `CIRCDIST.lift.iff` | CERTIFIED\* | `sha256:c3a841984a07038d…f0061` | **yes** |
| `CIRCDIST.lift.nonint` | CERTIFIED\* | `sha256:864bcc604035c712…fed4e` | **yes** |
| `CIRCDIST.lift.gap-example` | CERTIFIED\* | `sha256:487340464e4d0c68…5769c` | **yes** |

This is a precondition of the assembly, not a decoration: it establishes that the claim text each
review bound itself to is still the claim text this document composes. The root's own current claim
hashes to `sha256:ccad7fa605be1ae14a2dbc1d6c5758300bb8a5f0a3023fcef84725be40e78d8a`; if any of the
revisions of §7 is adopted, that value changes and any review bound to the old value lapses.

### 0.3 The usage rule this document obeys

**Only what a review certified may be used, and only in the scope in which it was certified.**
Concretely:

1. A child discharges a root clause only via the child's **canonical claim text**, not via an
   arbitrary numbered result inside its artifact. Where a numbered result is needed that is *not*
   named in the child's claim, this document says so explicitly and marks the step
   proposer-level (§2, clause 4; §5.2).
2. The amendment-2 review's §9 exclusion list, the `CIRCDIST.lift.iff` node caveats, the
   `CIRCDIST.lift.nonint` node caveats, and the `CIRCDIST.lift.gap-example` node caveats are
   treated as hard boundaries. Nothing outside them is imported (§6).
3. Where the base proof and an amendment conflict, Amendment 2 governs Amendment 1 on L1/L2/L3 and
   Amendment 1 governs the base proof elsewhere — the order the amendments themselves declare. Two
   base-proof statements are **retracted** and are not used anywhere below: the original
   Definition 5.1 (superseded by 5.1′) and `R_sat(M) ≤ d` (retracted by A2, replaced by L2's
   `R_sat ∈ {1, ∞}` dichotomy).

---

## 1. The root claim, restated exactly and split

### 1.1 Verbatim

From `research/circdist/proof-dag/nodes/CIRCDIST.lift.yaml`, field `claim`, reflowed only:

> In graph-like detector error models with fixed boundaries, a proven necessary-and-sufficient
> structural criterion (in graph-covering, voltage-graph, or chain-complex form) characterizes when
> d_circ = d_eff, of the shape "d_circ equals the minimum over nontrivial effective logicals gamma
> of the length of the shortest closed spacetime lift of gamma", with zero time-direction
> voltage/monodromy as the equal-weight liftability condition; the criterion recovers the
> non-interleaved equality d_circ = d_eff as a corollary and is accompanied by an explicit
> interleaved example with d_circ > d_eff.

### 1.2 The five clauses

Splitting is itself an interpretive act, so it is done once, here, and every later section refers
to these labels. The split follows the claim's own punctuation.

| clause | text | kind |
|---|---|---|
| **(C1)** | in graph-like DEMs with fixed boundaries, a **necessary-and-sufficient structural criterion** (in graph-covering, voltage-graph, or chain-complex form) characterizes when `d_circ = d_eff` | universal, biconditional |
| **(C2)** | the criterion is **of the shape** `d_circ = min_{γ ∈ L_eff} ℓ(γ)`, `ℓ(γ)` = length of the shortest closed spacetime lift of `γ` | universal, identity |
| **(C3)** | **zero time-direction voltage/monodromy** is the equal-weight liftability condition | definitional content of (C1)/(C2) |
| **(C4)** | the criterion **recovers the non-interleaved equality** `d_circ = d_eff` as a corollary | universal, derivational |
| **(C5)** | the criterion **is accompanied by an explicit interleaved example** with `d_circ > d_eff` | **existential** |

The kind column is what makes §4 necessary: (C1)–(C4) are universally quantified over the model
class, and (C5) is existential inside it. Restricting the model class weakens the first four and
**strengthens** the fifth. That asymmetry is the whole scope problem.

### 1.3 The frozen ambient conventions all five clauses inherit

From the 公共定义 (`CIRCDIST_PROBLEMS.md`, §公共定义 and 课题二), unchanged:
CSS code `Q = [[n,k,d]]`; single ancilla per stabilizer generator, prepared once and measured once
per round, one CNOT per data qubit of the generator's support; `d_eff(M) := d_ext(E(M))`;
`d_circ(C) = min{|F| : F` fires no detector and flips a nontrivial logical `}`; standard memory
experiment with equal elementary-fault weights and ideal final readout;
`d_eff(M) ≤ d_circ(C(M)) ≤ d`.

Plus the **measurement-consistency legality constraint (MC)** added across the round-2+ artifacts
and now part of the model: for every `(a,b) ∈ 𝒜 × ℬ`,
`c_{ab}(M) = #{q ∈ supp(a) ∩ supp(b) : t(q→b) < t(a→q)} ≡ 0 (mod 2)`. A schedule violating (MC)
has non-deterministic detectors and therefore **no `d_circ` at all** — so (MC) is a hypothesis of
every clause, silently, and any future instance offered against this root must be checked for it
first. This is the constraint that invalidated the round-1 recon's original `[[4,2,2]]` witness.

---

## 2. Clause-to-child map

### 2.0 The map at a glance

| clause | discharged by | via the certified claim text | residual proposer-level step |
|---|---|---|---|
| **C1** | `CIRCDIST.lift.iff` | "…an intrinsic zero-voltage/monodromy condition characterizing same-weight liftability…" (= Thm 5.7, the minimum-weight repair-0 biconditional) | none; but "proven" must be read as CERTIFIED\*, §7 R1 |
| **C2** | `CIRCDIST.lift.iff` | "…d_circ equals the minimum over nontrivial effective logicals gamma of the length of the shortest closed spacetime lift of gamma…" (= Thm 5.6(a)) | none |
| **C3** | `CIRCDIST.lift.iff` | same clause of the child claim, plus the non-vacuity bar | wording: "zero voltage" is a **minimum over a voltage spectrum**, not a scalar, §7 R2 |
| **C4** | `CIRCDIST.lift.nonint` | "every non-interleaved schedule satisfies d_circ = d_eff, **derived (not assumed) from the framework**" (= Thm 7.1) | the *literal* corollary reading is iff §5.11, which is **not named** in either child's claim — §2.4 |
| **C5** | `CIRCDIST.lift.gap-example` | "There exists an explicit legal interleaved single-ancilla CNOT syndrome-extraction circuit with d_circ strictly greater than d_eff; witnessed at [[4,2,2]]…and at Steane [[7,1,3]]…" | the graph-like descent, §4.3 (NUMERICAL) |

### 2.1 C1 — the biconditional

`CIRCDIST.lift.iff` is CERTIFIED\* on the claim text quoted in §2.0. The criterion it certifies is,
in the dossier's numbering, Theorem 5.7 as amended:

> For every legal, measurement-consistent single-ancilla CSS schedule `M`, and `R ≥ d`,
> `d_circ(C_R(M)) = d_eff(M)` **⟺** `∃ γ ∈ L_eff` with `|γ| = d_eff(M)` and `repair(γ) = 0`.

Both directions are inside the certified scope, and — this is the point most easily lost — **neither
direction carries a `repair ≤ 2` hypothesis**:

* (⟸) is Lemma 5.3′ (Amendment 1 §2.4) giving `d_circ ≤ |γ| + repair(γ) = d_eff` **in either
  collision branch**, together with `d_circ ≥ d_eff` from 5.4(1). Amendment 2's L1 supplies the
  schedule-independent reason the collision branch cannot be forced at minimum weight, for
  arbitrary legal interleaving; the amendment-2 review CLEAN-PASSED it at value and printed
  derivation.
* (⟹) needs no hypothesis on `repair` at all: if `|F| = d_eff` then the weight loss of 5.4(2) is
  zero, so `n_∅ = 0` and `m = 0`, so `A_∅ = 0`, so `A_ess + xC = 0` by (LIFT), so the certificate
  read off `F` has weight `0`. The case `repair(γ) ≥ 3` **cannot arise when `d_circ = d_eff`**;
  that is why the excluded regime does not touch this clause.

"Structural" and "in … chain-complex form" are satisfied by the delivered formalization: the
spacetime complex is the free `Λ = F₂[x,x⁻¹]`-module `V = Λ^ℬ` with
`∂(f,r) = x^r(u_f(1+x) + s_f x)`, the effective complex is `∂_eff = s`, and the projection
`(π_1, π_0)` is a weight-non-increasing chain map with `π_0 = ε` the augmentation (iff §§1.16–1.18,
§4.1–4.2). See §3 for why this is the same complex the sibling document uses.

**Which disjunct of "graph-covering, voltage-graph, or chain-complex" is delivered — and which is
refuted.** The claim offers three forms disjunctively, so delivering one satisfies it; but the
record should not leave the impression that all three are available:

* **chain-complex — delivered.** As above.
* **graph-covering — not available, with reason.** iff §4.4: `(π_1, π_0)` is *not* a graph
  covering. The obstruction is not the boundary (§4.1 removes that) but the voltage spectrum
  `U(E)` — a base residual `E` has several unit-weight lifts of *different* voltage, so `G_circ` is
  a derived graph of a voltage assignment on the **multigraph** `G̃_eff` in which `E` is replaced by
  `|U(E)|` parallel edges.
* **voltage-graph — available only after passing to `G̃_eff`.** iff §4.4 states that route R2
  "stated on `G_eff` … is not merely hard, it is false". Any future re-registration of the
  voltage-graph form must be on `G̃_eff`.

### 2.2 C2 — the shape

`d_circ(C_R(M)) = min_{γ ∈ L_eff} ℓ(γ)` is Theorem 5.6(a), and Amendment 1 §2.6 records it as
surviving **verbatim** under the corrected Definition 5.1′ (one Pauli per location): `≤` because a
closed lift is an undetectable observable-flipping configuration, `≥` because a minimum-weight such
configuration `F` is itself a closed lift of `γ = π_1 F`. It is also the leading phrase of the
child's certified claim text, so it is discharged directly.

**Where the content of C2 actually sits, so nobody mistakes it for a tautology.** The round-1 recon
flagged that `d_circ = min_γ ℓ(γ)` risks being a renaming. Two things stop it from being one, and
both are inside the certified scope:

1. **5.4(1): the projection cannot destroy non-triviality.** `λ_circ = λ_eff ∘ π_1` as an identity
   of linear maps, because the observable is read exactly once, at the end, from the accumulated
   residual. This is what makes `γ = π_1 F` land in `L_eff` *identically* rather than generically,
   and it is the answer to the litverify warning that homology systole is not monotone under
   covers. It uses the ideal terminal readout of the frozen boundary conditions and nothing else.
2. **The non-vacuity bar**, which the child's claim carries explicitly ("the voltage is computable
   without constructing the full multi-round circuit"): `repair` is a one-round quantity
   (Definition 5.2), and the **contiguity theorem** 5.9 (a minimum-weight undetectable logical
   occupies a contiguous block of rounds, of span `≤ |F| = d_circ ≤ d`) makes the minimisation
   finite and `d`-bounded. Without these, C2 would be a definition; with them it is a decision
   procedure for the equality question.

### 2.3 C3 — "zero time-direction voltage/monodromy"

Discharged by the same child clause, with one wording correction that the assembly must not paper
over.

The certified realisation of "zero voltage" is `repair(γ) = 0`, which by (LIFT′) reads:

> there exist a round assignment `r_1,…,r_w` and unit-weight voltage representatives
> `u_i ∈ U(E_i)` such that in **every** round and on **every** Z-check, the in-round measurement
> flips equal the parity of the syndrome accumulated by all earlier rounds:
> `U_b(r) = c_b(r−1)` for all `b, r`.

This is `F₂`-valued (so the recon's `F₂`-versus-`Z` orientation crux does not arise), it is
computed from one round's `(E, s, u, λ)` data plus a round assignment, and no multi-round circuit
is ever built. The recon's earlier `Σ_i u_i = 0` is the same-round special case.

**The correction.** The root says "*zero* time-direction voltage/monodromy", which reads as the
vanishing of a single well-defined quantity attached to `γ`. It is not one. Because a residual `E`
admits a *set* `U(E)` of unit-weight voltages, the voltage of `γ` is a set, and the liftability
condition is a **minimum over that set and over round assignments** being zero, not the vanishing
of a scalar. §7 R2 proposes the minimal rewording. Substantively the clause is discharged; verbally
it overstates the sharpness of the object.

**Scope of the equal-weight statement.** The biconditional `ℓ(γ) = |γ| ⟺ repair(γ) = 0` holds in
both directions **at minimum weight**:

* (⟹) unconditional, from 5.4(4): `ℓ(γ) ≥ |γ| + min(repair(γ), 2)`.
* (⟸) at minimum weight for **any legal schedule**, by Lemma 5.3′(a) plus Amendment-2 Lemma 2.5′
  (L1). For a **fixed non-minimal** `γ`, Amendment 1 §7 item 3 is explicit that the
  distinct-location proviso is *not* discharged and must be checked per `γ`.

Since C1/C2/C3 quantify the criterion over minimum-weight `γ`, this is exactly the case needed; but
the non-minimal proviso is a live caveat and is carried forward in §6.

### 2.4 C4 — the non-interleaved corollary (the one clause with a seam)

Two distinct statements are in play and they discharge C4 to different degrees.

**(a) The certified child.** `CIRCDIST.lift.nonint` is CERTIFIED\* on: "*Within the closed-lift
framework, every non-interleaved schedule satisfies d_circ = d_eff, **derived (not assumed) from
the framework***". Theorem 7.1 proves it inside the same `Λ`-module frame: `≥` by the augmentation
chain map, `≤` by the weight-preserving section `ι_r` built from horizontal representatives, with
all boundary cases discharged. Its own review confirmed it line-by-line and by independent
reconstruction across 112 non-interleaved configurations over 4 codes, `R = 1..4`, including a
non-graph-like `[[15,7,3]]` instance.

**(b) The literal corollary.** The root's word is "**recovers … as a corollary**", and the frozen
technical requirement 6 is "从一般定理推出" — *derive it from the general theorem*. The statement
that does this literally is iff §5.11: a non-interleaved schedule admits a **uniform** flavour
(`0 ∈ U(E)` for all `E` when Z-block-first; `s(E) ∈ U(E)` for all `E` when X-block-first), hence
`repair(γ) = 0` for **every** `γ ∈ L_eff`, hence Theorem 5.7 fires and gives `d_circ = d_eff`.
Six lines, and it is a corollary of the criterion in the strict sense.

**The seam, stated plainly.** §5.11 lives inside the `CIRCDIST.lift.iff` dossier and its survival
across both amendments was affirmed by the review chain (Amendment 1 §2.7 amends its two citations
of 5.3; the focused rereview records "5.7/5.11 genuinely survive"). But **§5.11 is not named in
either child's canonical claim text**, so under the usage rule of §0.3 it is available to this
assembly only as a proposer-level step, not as a certified one.

Therefore C4 is discharged as follows, and a completion review should ratify or reject this
reading:

* The **content** of C4 — that non-interleaved schedules satisfy `d_circ = d_eff`, established
  inside the closed-lift framework rather than imported — is discharged **certified**, by
  `CIRCDIST.lift.nonint`'s claim, which says exactly that.
* The **stronger reading** — that it is literally a corollary of the criterion of C1 — is
  discharged **proposer-level**, by iff §5.11, corroborated by the fact that the two derivations
  agree in detail (iff §5.8's cross-reference lists the three things they agree on, including that
  §5.11's `k = 1` branch is nonint's Remark 6.4). If the lead wants C4 at the stronger reading and
  at certified level, the minimal act is to name §5.11 in `CIRCDIST.lift.iff`'s claim or to
  register it as its own reviewed sub-result; see §7 R5.

Under either reading nothing is imported from outside a certified scope, because the weaker reading
alone already discharges the clause as written ("recovers … as a corollary" is satisfied by a
derivation inside the framework; Theorem 7.1 is one).

### 2.5 C5 — the explicit interleaved example

`CIRCDIST.lift.gap-example` is CERTIFIED\* on an existence claim naming two families of witness:

* `[[4,2,2]]`, measurement-consistent depth-7 interleaved schedules (3 of the 176 consistent ones),
  `d_eff = 1`, `d_circ = 2`, with the identical-within-check-order non-interleaved partner at
  `d_circ = 1`;
* Steane `[[7,1,3]]`, interleaved depth-8, `d_eff = 2`, `d_circ = 3`, non-interleaved partner
  `d_circ = 2` — i.e. completion gap `g(C) = 1` at `d = 3`.

Its independent review re-derived the (MC) constraint from scratch, validated it 524/524 against
`stim` determinism, confirmed the repaired witnesses and their partners at `R = 2..5`, confirmed
the invalidity of the retracted depth-5 circuit, and independently reconstructed the Steane
instance with 9936 DEM columns cross-validated at 0 disagreements.

**Coherence with C1–C3 (NUMERICAL, §9.3).** The witnesses are not merely compatible with the
criterion; the criterion *predicts* them from one round. For the `[[4,2,2]]` depth-7 witness, the
one-round data computed independently this session gives a single nontrivial weight-1 effective
logical `γ = {E}` with `E = {2,3}` (the hook suffix of `a`'s order after its second CNOT),
`s(E) = 0`, `λ(E) = 1`, and a **rigid** voltage spectrum `U(E) = {1}`. Hence
`repair(γ) = min_{u ∈ U(E)}|u| = 1 ≠ 0`; every minimum-weight `γ` has `repair ≥ 1`; Theorem 5.7
therefore forces `d_circ > d_eff`, and Theorem 5.6(c) (applicable since `repair = 1 ≤ 2`) forces
`ℓ(γ) = 2` exactly. The measured `d_circ = 2` matches. The criterion and the example are the same
statement seen from two sides, which is what "accompanied by" should mean.

**The descent into the graph-like restriction is not free and is done in §4.3.**

---

## 3. The three children speak one language

The blueprint's second condition was "consistency of the three formalizations". This is not
automatic — the record shows one genuine contradiction between the iff and nonint documents that
had to be found and repaired — so the check is written out.

### 3.1 The detector chain is literally the same formula

* iff (∂-L), §4.1: `∂(f, r) = x^r ( u_f (1+x) + s_f x )`.
* nonint, Lemma 2.13(2): `∂(x^r e_i) = x^r u_i + x^{r+1}(u_i + s_i)`.

Expand the first: `x^r u_f + x^{r+1} u_f + x^{r+1} s_f = x^r u_f + x^{r+1}(u_f + s_f)`. **Identical.**
Both are over `Λ = F₂[x,x⁻¹]` with `x` the time-translation generator and `ε : x ↦ 1` the
augmentation.

### 3.2 The four conventions that had to agree, and do

| convention | iff | nonint | agree? |
|---|---|---|---|
| `d_eff` indexes residual **classes** `ℰ`, not fault types | Def. 1.16 | Def. 2.11 / sharpening 0.3.1 | yes |
| residual inventory `ℰ = {∅} ∪ {singletons} ∪ {suffixes of X-check CNOT orders}` | Prop. 1.13 | Lemma 4.1 | yes |
| **both** temporal boundary detectors present (`D_{b,0}` and `D_{b,R}`); truncation is an isometric embedding, not a quotient | Lemma 4.1 | Lemma 2.13 + Rmk. 2.14 | yes |
| fault weight is **per location**, one Pauli per location | Def. 5.1′ (Amdt. 1), adopting the sibling verbatim | Def. 2.8 | yes, by explicit adoption |
| X-check detector index range in the Z-memory sector | `1 ≤ r ≤ R−1` after A3c | Def. 2.7 | yes, after the amendment |

### 3.3 The one contradiction that existed, and its repair

Base iff §5.10(1) asserted `R_sat(M) ≤ d`; nonint Corollary 7.3 asserted
`R_sat ∈ {1, ∞}` with `R_sat = ∞` whenever `d_eff < d`. These are inconsistent, and the
non-interleaved Steane instance (`d_eff = 2 < 3 = d`) is a counterexample to the former.
Amendment 1 **retracted** `R_sat ≤ d` outright; Amendment 2's L2 sharpened the finite branch to
`R_sat = 1`, at which point the two documents coincide exactly and the amendment-2 review confirmed
there is "no quantifier or endpoint mismatch". The surviving general statement is:

```text
   d_R(M) is non-increasing in R and constant for R >= d ;  B(r,d) = d ;
   R_sat(M) = 1        if d_infty(M) = d ,
   R_sat(M) = infinity if d_infty(M) < d ,
   and the dichotomy is decided by inspecting R = 1,...,d.
```

**Assembly consequence.** The composition is *not* pure bookkeeping in the sense of being
risk-free: the one non-trivial consistency question between the two framework documents had a real
answer, it was "they contradict", and it took two amendment rounds and two independent reviews to
resolve. The route's `implication` text should be amended to say so (§7 R6). What is true is that
after those repairs the three children are mutually consistent on every convention the assembly
uses.

---

## 4. Scope alignment I — graph-likeness

### 4.1 The situation

**Definition (iff Def. 1.12).** `M` is graph-like in a sector if `|u(f)| + |u(f)+s(f)| ≤ 2` for
every elementary fault `f` — i.e. every DEM column of `∂` has weight `≤ 2`.

Three facts are in tension and all three are on the record:

1. The **root claim** and the **`CIRCDIST.lift.iff` certified claim** both begin "In graph-like
   detector error models with fixed boundaries".
2. The **certified claims of the other two children carry no graph-like restriction**:
   `lift.nonint` says "every non-interleaved schedule", `lift.gap-example` says "There exists an
   explicit legal interleaved … circuit".
3. **No step of either core theorem uses graph-likeness.** iff §7.3 and §7.1's hypothesis table
   record that Definition 1.12 is invoked exactly once in the whole iff document, in Lemma 7.1,
   which is inside the *excluded* `repair ≥ 3` analysis. nonint settlement S1 reaches the same
   conclusion independently.

### 4.2 Which direction of generalization is free

**Free: (C1)–(C4), restricting downward.** These clauses are universally quantified over the model
class. A statement proved for all legal, (MC), single-ancilla CSS schedules with the frozen ideal
boundaries specialises, with no further argument, to the graph-like subclass. So:

* C1/C2/C3: nothing to do — `CIRCDIST.lift.iff`'s certified claim is *itself* stated on graph-like
  models, so the child claim and the root clause have **the same domain**. The extra generality of
  the underlying derivations is a bonus and is *not needed by the root*.
* C4: `CIRCDIST.lift.nonint`'s certified claim has the **larger** domain (no graph-like
  restriction). Restricting it to graph-like schedules is free. This is a strict surplus.

**A caution attached to the free direction.** The completion review certified `lift.iff` "for the
exact current node claim". That claim is the graph-like-restricted one. The hypergraph-level
statement — that Theorems 1 and 2 hold verbatim for arbitrary detector *hypergraph* models — is
therefore **proposer-level (CONJECTURED)**, however well corroborated by two reviews confirming
derivations that never invoke Definition 1.12. This assembly does **not** use the hypergraph
reading anywhere, and no future session may silently promote it by citing this root.

**Needs a remark: (C5), which does not descend.** An existence statement inside a larger class is
not an existence statement inside a subclass. `lift.gap-example`'s certified claim exhibits
witnesses in the unrestricted class; the root asserts one in the graph-like class. If both certified
witnesses happened to be non-graph-like, **C5 would be undischarged on the root's stated domain and
the root claim would need the restriction dropped**. So the descent has to be checked, not assumed.

### 4.3 The descent, checked (NUMERICAL; code and output in §9.2)

**Result.**

| witness | sector | detector checks in sector | `max_f (|u| + |u+s|)` | graph-like? |
|---|---|---|---|---|
| `[[4,2,2]]` depth-7 MC interleaved witness | Z-memory | 1 | **2** | **yes** |
| `[[4,2,2]]` depth-7 MC interleaved witness | X-memory | 1 | **2** | **yes** |
| Steane `[[7,1,3]]` | Z-memory | 3 | **3** | **no** |

**Search scope of this check.** Enumeration is over the complete one-round X-sector elementary-fault
inventory of Proposition 1.13 for the named schedule — every hook (every suffix of every X-check
CNOT order, including the improper hook `S_a(0) = supp(a)`), every bare data `X` at every distinct
insertion time, and the empty-residual faults with `u ∈ {0} ∪ {e_b}` — 39 faults per sector for
`[[4,2,2]]`, 82 for Steane. It is *not* a scan over other schedules or other codes; it is a check
of the two named certified witnesses.

**Why the `[[4,2,2]]` answer is schedule-independent (exact argument, not just the scan).** The
`[[4,2,2]]` code as used in this campaign is `𝒜 = {a}` with `supp(a) = {0,1,2,3}` and
`ℬ = {b}` with `supp(b) = {0,1,2,3}` — **one X-check and one Z-check**. In the Z-memory sector the
detector algebra is `F₂^ℬ ≅ F₂`, so every fault has `|u| ≤ 1` and `|u+s| ≤ 1`, hence
`|u| + |u+s| ≤ 2` identically, for **every** schedule. The X-memory sector is the mirror with
`|𝒜| = 1`. So graph-likeness of the `[[4,2,2]]` witnesses is a structural fact about the code, not
a lucky property of the three surviving schedules — including the two further depth-8 witnesses
that survive idle-layer compression.

**Why Steane fails.** Data qubit `6` lies in all three Z-checks `Z0 = {3,4,5,6}`, `Z1 = {1,2,5,6}`,
`Z2 = {0,2,4,6}`, so the bare error `X₆` has `s = (1,1,1)` and the scan finds
`|u| + |u+s| = 3` on it and on the three hooks with residual `{6}`. This reproduces the statement
already made independently in iff §1.5, iff §7.2, and nonint §8.3.

### 4.4 What C5 is therefore discharged by, and what it is not

> **Assembly step (CONJECTURED).** C5 is discharged **inside the root's graph-like restriction** by
> the `[[4,2,2]]` family alone: those witnesses are legal, interleaved, measurement-consistent,
> single-ancilla, have the frozen memory-experiment boundaries, are graph-like in both sectors, and
> have `d_circ = 2 > 1 = d_eff`, all certified except the graph-likeness, which is §9.2.
>
> The **Steane** witness — the campaign's only `d = 3`, `g(C) = 1` instance and by far the more
> informative one — is **outside** the graph-like restriction and therefore corroborates only the
> unrestricted reading of C5. It must not be cited as a graph-like example.

This is the honest cost of the root's restriction: it is satisfiable, but only by the weaker
witness. The lead should note that the restriction is discarding the campaign's best evidence for
its own root claim, which is the practical argument for §7 R4.

---

## 5. Scope alignment II — the `repair ≥ 3` exclusion

### 5.1 What exactly is excluded

`CIRCDIST.lift.iff`'s node caveats and the amendment-2 review's §7.1/§9 exclude, from certification:

* the general lift-length formula for `repair ≥ 3`, and the min-cost-covering extension;
* the pre-existing 5.6(d) concern;
* the large proposer scans (`3855/3855`, `98811` schedules, the unexplained `321059/321059`
  symmetry), which were not independently reproduced;
* general formulas for `d_∞`.

What **is** certified is "the reviewed minimum-weight repair-0/closed-lift criterion".

The technical shape of the exclusion: Theorem 5.6(b) is the two-sided sandwich

```text
        |gamma| + min( repair(gamma), 2 )   <=   ell(gamma)   <=   |gamma| + repair(gamma) ,
```

whose upper half needs the distinct-location proviso (discharged at minimum weight by L1). The two
sides meet exactly when `repair ≤ 2`. The escape that keeps them apart is real, not hypothetical:
the weight-2 **pair gadget** (5.6bis) reproduces the detector chain of `|s(E′)|` measurement flips
at cost 2, and the **split-pair** gadget survives even under graph-likeness. So the clean formula
should be expected to be *false* in general, and the extension target is the min-cost-covering form
`ℓ(γ) = |γ| + min_{m≥0}(2m + repair_m(γ))`. That is `CIRCDIST.lift.iff` frontier task-006, not a
root obligation.

### 5.2 Does any root clause need the excluded part? — No, under the reading of §1.2

Checked clause by clause. **Scope of this absence claim:** it covers exactly the five clauses as
split in §1.2 and the readings recorded there; it was carried out by tracing each clause to a
named numbered result and reading that result's hypothesis row in iff §7.1's table plus its
amendment status. Other splits or other readings of the same English could differ, which is why
the alternative reading is recorded explicitly in §5.3.

| clause | the result that discharges it | does it carry a `repair ≤ 2` hypothesis? |
|---|---|---|
| C1 (⟸) | Lemma 5.3′ + 5.4(1), with L1 | **no** |
| C1 (⟹) | 5.4(2)+(3) + (LIFT) | **no** — and the certified text says so: "this direction needs no hypothesis on `repair` — the case `repair(γ) ≥ 3` cannot arise when `d_circ = d_eff`" |
| C2 | Thm 5.6(a) | **no** — proved from 5.3′ and 5.4(1), not from the sandwich |
| C3 (⟹) | 5.4(4) | **no** |
| C3 (⟸) at minimum weight | 5.3′(a) + L1 | **no** |
| C4 | Thm 7.1 (`lift.nonint`); §5.11 gives `repair ≡ 0` | **no** — `repair = 0 ≤ 2` a fortiori |
| C5 | `[[4,2,2]]`: `repair = 1`; Steane: `repair = 1` | **no** — both instances sit in `repair ∈ {0,1}` |

So no clause of the root claim as written requires the excluded regime. The reason is structural
rather than lucky: the root is a claim about the **equality** `d_circ = d_eff`, and equality forces
`repair = 0`; the excluded regime is about the **magnitude** of the gap when it is large.

### 5.3 The one reading that would need it, and how to insulate the root

If C2 is read not as an identity but as **"the criterion computes the value of `d_circ`"** — i.e.
as delivering the 课题二 希望结果 "给出不需要构造完整多轮电路的等号判定算法" in its *gap-formula*
form — then the excluded regime bites immediately, because `ℓ(γ)` is only pinned for
`repair(γ) ≤ 2`. Precisely what is available at certified level is the computable sandwich

```text
    min_{gamma in L_eff} ( |gamma| + min(repair(gamma), 2) )   <=   d_circ
                                                              <=   min_{gamma in L_eff} ( |gamma| + repair(gamma) ) ,
```

both sides one-round computable with a `d`-bounded round window (5.9, 5.10(2)), collapsing to an
equality exactly when the right-hand minimiser has `repair ≤ 2`. In particular the **equality
decision** (`d_circ = d_eff`?) is answered unconditionally, while the **gap value** `g(C)` is
determined only in that regime and otherwise bracketed.

**This is not a wall for the root**, because the root claim's C2 says "`d_circ` equals the minimum
… of the length of the shortest closed spacetime lift", which is the identity, not the algorithm.
But the two readings are one comma apart, and a future session will conflate them unless the record
says otherwise. §7 R3 proposes the one-sentence insulation.

---

## 6. Caveats carried forward into the root

Every item below is inherited; none is new, and none may be dropped by a promotion of the root.

### 6.1 Review-chain caveats (all three children)

* **C-R1. Single same-stack independent review chain; no cross-stack or human verification.** This
  is the recorded caveat on all three children and it is the reason all three are `CERTIFIED*`
  rather than `CERTIFIED`. It propagates to the root unchanged: **a root assembled from three
  starred children is itself at most `CERTIFIED*`,** and this session (an Opus 5 proposer, the same
  stack again) cannot lift the star.
* **C-R2. A discrepancy in the record about C-R1, flagged not resolved.** The base review
  (`circdist_lift_proofs_review_20260820.md`), the focused rereview
  (`circdist_amendments_review_20260820.md`) and the gap-example review
  (`circdist_numerical_review_20260820.md`) each self-identify as "fresh Opus 5" sessions. The
  **completion** review that carries `lift.iff`'s promotion
  (`circdist_amendments2_review_20260820.md`, §0) self-identifies differently: "Model identity
  available to the session: Codex, GPT-5-based." The `lift.iff` node caveat nonetheless records the
  chain as same-stack. This document treats the self-report as *data inside a file*, not as a
  verified fact about which model executed, and does **not** resolve it — but the resolution matters
  to the root, because if the final link is genuinely cross-stack the star may be liftable for
  `lift.iff`, and if it is not, the caveat is correct as recorded. Registered for the root's
  completion review, §8 item 7.
* **C-R3. Verification breadth is finite and named.** `lift.nonint`'s certification rests on
  Def. 2.8 + Lemma 7.2 and 112 non-interleaved configurations across 4 codes at `R = 1..4`
  (including a `[[15,7,3]]` Hamming-CSS instance with Z-degree 4 and overlaps up to 8); beyond
  those finite checks it rests on reviewed prose. `lift.gap-example`'s rests on the reviewer's own
  simulator, 524/524 `stim` determinism agreements and 9936 cross-validated DEM columns.

### 6.2 Model caveats (bind every clause)

* **C-M1. `(V)` is everything.** `U(∅) ⊆ {0} ∪ {e_b}` — a unit-weight, unit-voltage fault exists on
  every check in every round (the classical measurement flip) and empty-residual faults contribute
  at most one voltage monomial. This is the single point where "single-ancilla CSS, one classical
  outcome per check per round" enters, and it is what makes `repair` a *count*. Multi-ancilla,
  flag, or cat-state schedules (out of scope per the 公共定义) would break 5.4(3) and collapse the
  entire lower bound. Any extension beyond the 公共定义 must re-derive `(V)` first.
* **C-M2. Ideal boundaries are load-bearing at both ends.** Lemma 4.1 (finite complex embeds
  isometrically, no boundary correction) needs the ideal `|0⟩^n` initialisation *and* the ideal
  transversal final readout. With noisy initialisation `D_{b,0}` is absent and contiguity 5.9 fails
  at the first boundary; with a non-ideal readout `D_{b,R}` is absent. "Fixed boundaries" in the
  root claim must be read as exactly these.
* **C-M3. Per sector.** Everything is stated for one memory sector; `d_circ(C) = min` of the two
  and `repair` must be computed twice. The Steane witness lifts the **Z-memory** sector only (the
  X-memory sector gives 2); one `[[4,2,2]]` witness lifts both.
* **C-M4. `d_eff` counts residual *classes*, not qubits.** `|γ|` counts residuals. This is what
  makes `π_1` weight-non-increasing, and it matches `d_ext` of the 公共定义.
* **C-M5. Identical rounds.** Time-translation invariance in the bulk is used (Definition 5.2). A
  round-varying schedule breaks the definition of `repair`, though not (LIFT′).
* **C-M6. (MC) is a hypothesis, not hygiene.** Non-(MC) schedules have no `d_circ`. It is also
  load-bearing for Theorem 1: at overlap exactly 2 a hook carries vertical voltage **iff** (MC)
  fails on that pair.

### 6.3 Idle-layer / schedule-space conventions (C5 only)

* **C-S1. The denominators in the gap-example claim are pre-compression.** Under the frozen
  idle-layer-compression rule of 课题一 ("无意义的空闲层应当压缩掉"), the depth-7 `[[4,2,2]]`
  denominator is **44, not 176**; the depth-8 witness count drops from 26 to **5**. The
  **witnesses themselves are unaffected** — the existence claim, which is all C5 needs, is
  untouched — but any *density* or *fraction* statement built on `3/176` or `26/769` is
  conventionally wrong and must be restated. This assembly uses only the existence.
* **C-S2. The retracted depth-5 circuit must never be cited.** The round-1 recon's original
  `[[4,2,2]]` witness violates (MC) (odd back-propagation count for the single pair) and `stim`
  refuses its DEM; its reported `d_eff = 1, d_circ = 2` is not a circuit distance. The valid
  replacement is the depth-7 schedule reproduced in §9.2.
* **C-S3. Observable scope of the `[[4,2,2]]` re-check.** The d3-gate re-check tracks the `Z₀Z₂`
  observable; §9.3 of this document uses the same convention.

### 6.4 Open items inside the iff dossier that survive assembly

* **C-O1.** `ℓ(γ)` for a **fixed non-minimal** `γ` is weaker than the base proof originally
  claimed: the distinct-location proviso is not discharged there and must be checked per `γ`
  (Amendment 1 §7 item 3). Evidence, not proof: zero *forced* collisions in 180 schedules, but
  non-forced collisions in all 180.
* **C-O2.** The proposer's re-implementations share their *model design* (which locations exist,
  which residual classes arise) with the documents they check. A systematic modelling error against
  `stim`'s conventions would survive them. This applies to §9 of this document too.
* **C-O3.** `d_∞(M)` is not computed anywhere for a general interleaved schedule; L2's dichotomy
  says only that it is decided by `R = 1,…,d`.
* **C-O4.** The `321059 / 321059` symmetry in the diagonal-hook scan remains unexplained and
  NOT-REVIEWED.
* **C-O5.** `k > 1` was raised as a residual concern in the base review and left as raised.
* **C-O6.** Cross-node leads that this root must **not** re-export: the d3-gate's "no hook in any
  measurement-consistent gross-code schedule can carry timelike voltage" is **withdrawn**; what
  survives is the per-pair statement that no gross-code hook is a *vertical* edge, and (per L3) the
  improper hook `S_a(0) = supp(a)` has `s = 0, λ = 0` and never enters a **minimum-weight** `γ` —
  the unqualified "never enters a `γ`" is false.

---

## 7. Claim-revision proposals for the lead

None of these is applied here; all are dispatcher acts. Adopting any of R1–R4 changes the root's
claim hash from `sha256:ccad7fa6…e78d8a` and lapses any review bound to the old text.

**R1 — bind "proven" to the available level (necessary if the root is promoted).**
The claim says "a **proven** necessary-and-sufficient structural criterion". All three children are
`CERTIFIED*`, and a conjunction cannot exceed its weakest premise. Either read "proven" as "reviewed
to the DAG's completion level `CERTIFIED*`" and record that reading in the assessment, or reword to
"an independently reviewed necessary-and-sufficient structural criterion". The second is cleaner,
because "proven" invites a later session to cite this root as a theorem.

**R2 — replace "zero time-direction voltage/monodromy" by the object that was actually certified.**
Suggested minimal wording: *"…with vanishing minimal time-direction repair cost — zero mismatch
between in-round measurement flips and accumulated syndrome parity, for some admissible choice of
one-round voltage representatives and round assignment — as the equal-weight liftability
condition"*. Reason: the voltage of `γ` is a **set** (the spectrum `U(E)` gives a residual several
unit-weight lifts of different voltage), so the condition is a minimum, not a vanishing scalar.
Same edit should note that of the three offered forms, the **chain-complex** one is delivered, the
**graph-covering** one is unavailable (iff §4.4), and the **voltage-graph** one is available only on
the multigraph `G̃_eff`.

**R3 — insulate C2's identity reading from the excluded regime (one sentence, no claim change).**
Append to the assessment, not the claim: *"The formula clause is an identity; the certified
computable content is the sandwich `min_γ(|γ| + min(repair,2)) ≤ d_circ ≤ min_γ(|γ| + repair)`,
which collapses exactly on `repair ≤ 2`. The equality decision `d_circ = d_eff` is unconditional;
the gap value `g(C)` is exact only in that regime and otherwise bracketed. The general lift-length
formula is `CIRCDIST.lift.iff` task-006 and is not claimed here."*

**R4 — consider dropping "graph-like" from the root claim (a free strengthening, with one cost).**
Arguments for: (i) no step of either core theorem uses it; (ii) two of the three children are
already certified without it; (iii) the campaign's strongest gap instance (Steane, `d = 3`,
`g(C) = 1`) is **not** graph-like, so the restriction excludes the best evidence for the root's own
C5; (iv) the cross-root consumer `CIRCDIST.gross` needs the unrestricted form, since the gross code
is not graph-like either. Argument against, and it is decisive for the *current* record: the
`CIRCDIST.lift.iff` completion review certified **the exact graph-like-restricted claim**, so
dropping the restriction from the root would make the root claim strictly wider than its
load-bearing child's certified scope. **Recommended sequencing:** do not drop it at the root until
`CIRCDIST.lift.iff`'s own claim is rewidened and re-reviewed; register the rewidening as a frontier
item on `lift.iff`, not as an edit to this root.

**R5 — decide how C4 is discharged, and record the decision.** Either (a) accept the weaker reading
("recovers the equality inside the framework"), which `CIRCDIST.lift.nonint`'s certified claim
discharges outright, or (b) require the literal-corollary reading, in which case iff §5.11 must be
named in `CIRCDIST.lift.iff`'s claim text or registered as its own reviewed sub-result, because it
is currently certified only implicitly. §2.4.

**R6 — amend the route's `implication` text.** It currently reads "assembling them is definitional
bookkeeping plus consistency of the three formalizations". Two corrections: the existence clause
C5 needed a genuine (small) computation to descend into the graph-like restriction (§4.3), and the
"consistency of the three formalizations" step was **not** free — it turned up a real contradiction
(`R_sat ≤ d` versus Corollary 7.3) that took two amendment rounds and two independent reviews to
settle (§3.3). Suggested replacement: *"Assembly is a clause-to-child map plus two scope arguments:
the universal clauses restrict downward for free, while the existence clause requires the exhibited
witness to be verified graph-like; formalization consistency was checked and one contradiction was
found and repaired."*

---

## 8. What a completion review of the ROOT must check

Exactly this list. Items 1–4 are preconditions; 5–9 are the mathematical content; 10–12 are hygiene.

1. **Hash freshness.** Recompute all fourteen hashes of §0.1 from current bytes. Recompute the
   three children's claim hashes under `sha256(claim.replace("\r\n","\n").strip().utf-8)` and
   confirm each still equals the `reviewed_hash` recorded in that child's `basis.reviews` entry
   (§0.2). If any child's claim text has drifted, its review has lapsed and the root cannot be
   assembled from it.
2. **Child levels.** Confirm all three children are still `CERTIFIED*` and that none has acquired a
   REFUTE or FURTHER-REPAIR event since 2026-08-20.
3. **Clause split.** Accept or reject the five-clause split of §1.2. Every later item depends on
   it; a different split may relocate the burden.
4. **Usage discipline.** Verify that no step of §2 uses a numbered result outside its child's
   *certified claim scope* except where this document flags it (§2.4's iff §5.11, marked
   proposer-level). In particular verify that nothing from the amendment-2 review's §9 exclusion
   list — `repair ≥ 3`, min-cost covering, 5.6(d), the large unreproduced scans, general `d_∞` —
   has leaked in.
5. **The clause map itself (§2).** For each of C1–C5, check that the quoted child claim really
   entails the clause. The two places to press hardest: **C2**, whether the identity is
   substantive or a renaming (the answer offered is 5.4(1) plus the non-vacuity bar, §2.2); and
   **C4**, whether "recovers … as a corollary" is satisfied by an independent proof in the same
   framework or demands the literal corollary (§2.4, and R5).
6. **Scope alignment I — graph-likeness (§4).** Confirm the free/needs-remark direction analysis:
   C1–C4 restrict downward for free; C5 does not. Then **re-run §9.2** and confirm
   (i) the `[[4,2,2]]` witness is graph-like in both sectors — including the schedule-independent
   single-check argument, which is stronger than the scan — and (ii) Steane is not. If (i) fails,
   C5 is undischarged on the root's stated domain and the root must not be promoted without R4.
7. **Scope alignment II — the `repair ≥ 3` exclusion (§5).** Verify the clause-by-clause table of
   §5.2, especially the certified text's own statement that the (⟹) direction of the criterion
   needs no hypothesis on `repair`. Then decide whether the record adopts the identity reading or
   the algorithm reading of C2 (§5.3, R3), because only the first is discharged.
8. **Formalization consistency (§3).** Re-verify that
   `x^r(u(1+x) + sx) = x^r u + x^{r+1}(u+s)` identifies the two documents' boundary maps, and that
   the five conventions of §3.2 agree post-amendment. Confirm the `R_sat` contradiction of §3.3 is
   genuinely closed in the current bytes (i.e. that `R_sat ≤ d` appears nowhere as a live claim).
9. **Adversarial pass.** The strongest available attack on the root is not on the assembly but on
   the criterion in the regime the assembly avoids: look for a legal, (MC), single-ancilla CSS,
   graph-like, ideal-boundary schedule on a code with `d ≥ 5` where a split-pair gadget makes
   `min_{m≥1}(2m + repair_m(γ)) < repair(γ)` for a minimum-weight `γ`. Such an instance would not
   refute C1 (equality forces `repair = 0`) but would refute the algorithm reading of C2 and would
   have to be recorded before promotion. Note that no instance in this campaign has `d ≥ 5`.
10. **Caveat carry-forward (§6).** Verify that all of C-R1..3, C-M1..6, C-S1..3, C-O1..6 appear in
    the root's assessment caveats if the root is promoted, and that none is silently dropped. In
    particular C-R1 (single same-stack chain) is what caps the root at `CERTIFIED*`.
11. **Review-stack discrepancy (C-R2).** Resolve whether the completion review of `lift.iff` was
    executed on a different stack from the proposer, as that file's §0 self-reports, or whether the
    node's "single same-stack" caveat is correct. This decides whether any star in the subtree is
    liftable. Do not resolve it from the file's own self-report alone.
12. **Non-mutation.** Confirm that this session created exactly one file
    (`artifacts/circdist_lift_root_assembly_20260822.md`), modified no existing file, and touched
    nothing under `research/circdist/proof-dag/`.

**Level ceiling for the root.** With three `CERTIFIED*` children, a proposer-authored assembly, and
the same-stack review-chain caveat, the maximum the root can reach on this route is `CERTIFIED*`,
and only after an independent review of *this document* (the assembly), not merely of the children.
`PROVED` is unreachable on this route: it would require the children to be `PROVED`, and each
carries at least one NOT-REVIEWED exclusion.

---

## 9. NUMERICAL — code and outputs

Python 3, standard library only. Exact over `F₂` (subsets of `[n]` as integer bit-masks). No
`stim`, no external libraries, no proposer base layer imported: the code below re-implements the
one-round `(E, s, u, λ)` inventory from Proposition 1.13 of the iff document. See caveat **C-O2**:
the *model design* is inherited from the documents being assembled, so a systematic modelling error
against `stim`'s conventions would survive these checks.

### 9.1 Claim-hash freshness of the three children

```python
import hashlib, yaml
for nid, expected in [
    ('CIRCDIST.lift.iff',
     'sha256:c3a841984a07038dfbe3390f0b25cca633d04877ff92fb04bd0e3eaf480f0061'),
    ('CIRCDIST.lift.nonint',
     'sha256:864bcc604035c7124b7fa23977e00375862520a28f347d092453ddd89b6fed4e'),
    ('CIRCDIST.lift.gap-example',
     'sha256:487340464e4d0c6b6820d134e40bcda128ed400f131806fe091deedd64a5769c')]:
    d = yaml.safe_load(open('research/circdist/proof-dag/nodes/%s.yaml' % nid))
    h = 'sha256:' + hashlib.sha256(
        d['claim'].replace('\r\n', '\n').strip().encode('utf-8')).hexdigest()
    print(nid, d['assessment']['level'], h == expected)
```

```text
CIRCDIST.lift.iff            CERTIFIED*  True
CIRCDIST.lift.nonint         CERTIFIED*  True
CIRCDIST.lift.gap-example    CERTIFIED*  True

root CIRCDIST.lift  level CONJECTURED
root claim hash     sha256:ccad7fa605be1ae14a2dbc1d6c5758300bb8a5f0a3023fcef84725be40e78d8a
```

### 9.2 Graph-likeness of the two certified gap witnesses (§4.3)

The `[[4,2,2]]` schedule is the d3-gate report's explicit valid witness: depth 7, interleaved,
measurement-consistent, `stim`-confirmed `d_circ = 2` at `R = 2..5`, slots `a = [0,3,4,5]`,
`b = [0,1,2,6]` in the within-check orders `a = (0,1,2,3)`, `b = (2,0,1,3)`.

```python
def pc(x): return bin(x).count('1')
def mk(s):
    v = 0
    for q in s: v |= 1 << q
    return v

def one_round_faults(nq, xchecks, zchecks, xorder, xtime, ztime):
    """(label, s, u) over the detector algebra F2^{zchecks}, per Prop. 1.13."""
    zn = list(zchecks)
    def syn(E):
        v = 0
        for i, b in enumerate(zn):
            if pc(E & mk(zchecks[b])) % 2: v |= 1 << i
        return v
    out = []
    for a, order in xorder.items():                      # hooks = suffixes of a's order
        for j in range(len(order) + 1):
            S = order[j:]; u = 0
            for i, b in enumerate(zn):
                c = sum(1 for q in S if q in zchecks[b] and ztime[b][q] > xtime[a][q])
                if c % 2: u |= 1 << i
            out.append(("hook %s S=%s" % (a, S), syn(mk(S)), u))
    alltimes = sorted({t for b in zn for t in ztime[b].values()} |
                      {t for a in xtime for t in xtime[a].values()})
    for q in range(nq):                                  # bare data X at every insertion time
        for t in [-1] + alltimes:
            u = 0
            for i, b in enumerate(zn):
                if q in zchecks[b] and ztime[b][q] > t: u |= 1 << i
            out.append(("data X%d @t>%s" % (q, t), syn(1 << q), u))
    out.append(("empty u=0", 0, 0))                      # (V): U(empty) = {0} u {e_b}
    for i, b in enumerate(zn):
        out.append(("meas flip %s" % b, 0, 1 << i))
    return out

def report(name, nq, xchecks, zchecks, xorder, xtime, ztime):
    fl = one_round_faults(nq, xchecks, zchecks, xorder, xtime, ztime)
    worst = max(pc(u) + pc(u ^ s) for _, s, u in fl)     # Definition 1.12
    print("%-42s checks=%d faults=%d  max(|u|+|u+s|)=%d  GRAPH-LIKE=%s"
          % (name, len(zchecks), len(fl), worst, worst <= 2))
    return worst

X422, Z422 = {'a': [0,1,2,3]}, {'b': [0,1,2,3]}
XT422 = {'a': {0:0, 1:3, 2:4, 3:5}}          # t(a->q)
ZT422 = {'b': {2:0, 0:1, 1:2, 3:6}}          # t(q->b)
print("(MC) count for the single pair (a,b):",
      sum(1 for q in [0,1,2,3] if ZT422['b'][q] < XT422['a'][q]), "(must be even)")
report("[[4,2,2]] witness, Z-memory sector", 4, X422, Z422, {'a':[0,1,2,3]}, XT422, ZT422)
report("[[4,2,2]] witness, X-memory sector", 4, Z422, X422, {'b':[2,0,1,3]},
       {'b': ZT422['b']}, {'a': XT422['a']})            # mirror: A <-> B

ST = [[3,4,5,6], [1,2,5,6], [0,2,4,6]]                   # Steane [[7,1,3]]
report("Steane [[7,1,3]], Z-memory sector", 7,
       {'X%d'%i: c for i,c in enumerate(ST)}, {'Z%d'%i: c for i,c in enumerate(ST)},
       {'X%d'%i: c for i,c in enumerate(ST)},
       {'X%d'%i: {q:j for j,q in enumerate(c)} for i,c in enumerate(ST)},
       {'Z%d'%i: {q:100+j for j,q in enumerate(c)} for i,c in enumerate(ST)})
```

```text
(MC) count for the single pair (a,b): 2 (must be even)
[[4,2,2]] witness, Z-memory sector      checks=1 faults=39  max(|u|+|u+s|)=2  GRAPH-LIKE=True
[[4,2,2]] witness, X-memory sector      checks=1 faults=39  max(|u|+|u+s|)=2  GRAPH-LIKE=True
Steane [[7,1,3]], Z-memory sector       checks=3 faults=82  max(|u|+|u+s|)=3  GRAPH-LIKE=False
    violators (4 of them): hook X0 S=[6], hook X1 S=[6], hook X2 S=[6], data X6 @t>-1
                           each with s=0b111, u=0b111, |u|+|u+s| = 3
    reason: qubit 6 lies in Z0, Z1, Z2, so bare X6 has |s| = 3
```

**Search scope.** Complete over the one-round X-sector elementary-fault inventory of Prop. 1.13 for
the named schedules (39 faults per `[[4,2,2]]` sector, 82 for Steane); **not** a scan over other
schedules or codes. The `[[4,2,2]]` conclusion is additionally schedule-independent by the exact
single-detector-check argument of §4.3, which the scan corroborates rather than establishes.

### 9.3 The criterion predicts the `[[4,2,2]]` witness (§2.5)

Same schedule, observable `Z₀Z₂` (the d3-gate convention, caveat C-S3); residual classes grouped
with their full voltage spectra `U(E)`.

```text
residual classes of the [[4,2,2]] depth-7 witness, Z-memory sector

   E = []          U(E) = {0,1}    s = 0   lambda = 0
   E = [0]         U(E) = {0,1}    s = 1   lambda = 1
   E = [1]         U(E) = {0,1}    s = 1   lambda = 0
   E = [2]         U(E) = {0,1}    s = 1   lambda = 1
   E = [3]         U(E) = {0,1}    s = 1   lambda = 0
   E = [2,3]       U(E) = {1}      s = 0   lambda = 1     <-- weight-1 effective logical, RIGID
   E = [1,2,3]     U(E) = {1}      s = 1   lambda = 1
   E = [0,1,2,3]   U(E) = {0}      s = 0   lambda = 0     (improper hook: stabiliser residual)

nontrivial weight-1 effective logicals (s = 0, lambda = 1):  exactly one, gamma = { {2,3} }
   |gamma| = 1 = d_eff
   repair(gamma) = min_{u in U(E)} |u| = 1        (|gamma| = 1 so B = 0, C = 0, A_0 = u)
   Theorem 5.6(c) (applicable: repair = 1 <= 2)   =>  ell(gamma) = 1 + 1 = 2
   Theorem 5.7: no minimum-weight gamma has repair 0  =>  d_circ > d_eff        PREDICTED
   measured (certified child, stim-confirmed R = 2..5): d_circ = 2              MATCHES
```

The improper hook `S_a(0) = supp(a) = {0,1,2,3}` appears with `s = 0` and `λ = 0` — the
stabiliser residual of Amendment 2's L3 — and correctly does not enter the minimum-weight `γ`.

---

## 10. What this document does not do

1. **It does not promote anything.** The root stays as the dispatcher finds it. The assembly is a
   proposer artifact; a completion review of it (§8) is a separate act by an independent session.
2. **It does not re-review the children.** Their proofs, amendments and reviews were read to
   extract certified scope and caveats, not to re-verify. No child verdict is confirmed or
   disputed here except where §6.1 flags a *record* discrepancy (C-R2), which is not a mathematical
   dispute.
3. **It does not touch the `repair ≥ 3` gap**, the min-cost-covering extension, the 5.6(d) concern,
   `d_∞`, the `321059/321059` symmetry, or `k > 1`. All remain exactly as their sources leave them.
4. **It does not apply any claim revision.** §7 is a list of proposals; every one is a dispatcher
   act, and R1–R4 would change the root's claim hash.
5. **It does not modify any existing file** and touched nothing under
   `research/circdist/proof-dag/`. One new file was created: this one.
