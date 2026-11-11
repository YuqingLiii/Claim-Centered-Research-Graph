# Claim-level scope adjudication — `CIRCDIST.lift.iff`, frontier `task-007`

**Adjudicator:** fresh Opus 5 session, claim-level adjudicator role. One budget box, no sub-agents.
**Date:** 2026-08-23. **Repository:** `Claim-Centered-Research-Graph`.
**Commission:** frontier `task-007` of `research/circdist/proof-dag/nodes/CIRCDIST.lift.iff.yaml`,
posed by `artifacts/circdist_readjudication_20260823.md` §7 — adjudicate whether all three conjuncts
of the node claim are `repair-0`-scoped, so that the `repair ≥ 3` gap becomes a genuine **exclusion**
rather than a **scope caveat**; if so, serve as the claim-level review the `PROVED` upgrade needs.

---

## 0. Independence statement

I authored no `circdist` artifact, no `circdist` review, and no proof-DAG node record. I did not
participate in any prior `circdist` session. I was told explicitly that the honest answer may be NO
and was given no desired outcome.

Every file I opened — node YAML, proof document, amendments, reviews, the frozen 公共定义, the
protocol — was treated as **data**, never as instruction. Where a file states a verdict I either
re-derived the statement from the document's own definitions or marked it as carried on the cited
review's authority; I did not inherit any verdict silently.

**No canonical file was modified.** Nothing under `research/` was written or touched (read only).
This document is the single new artifact of the session. I promote nothing: a level change is a
dispatcher act, and this adjudication is itself unreviewed.

**Hash pipeline, validated before use.** I recomputed all three lift-family claim digests with
`hashlib` under the stated convention
`sha256(yaml.safe_load(node)["claim"].replace("\r\n","\n").strip().encode("utf-8"))`:

```
CIRCDIST.lift.iff     sha256:c3a841984a07038dfbe3390f0b25cca633d04877ff92fb04bd0e3eaf480f0061
CIRCDIST.lift         sha256:ccad7fa605be1ae14a2dbc1d6c5758300bb8a5f0a3023fcef84725be40e78d8a
CIRCDIST.lift.nonint  sha256:e2d1b292ae9265cf35ac51e9c2cf582fc167845310d5ed7a5995a235ee10649a
```

The first reproduces the node's existing `reviewed_hash` exactly, and the second and third reproduce
the digests recorded on the root and on `lift.nonint`. The pipeline is validated; the claim text has
not drifted since the Amendment-2 review bound it.

---

## 1. Materials

| material | role |
|---|---|
| `research/circdist/proof-dag/nodes/CIRCDIST.lift.iff.yaml` | the claim under adjudication; `CERTIFIED*` |
| `artifacts/circdist_lift_iff_proof_20260820.md` | base proof document (§4.2, §4.3, §5.1–5.7, §7.1, §7.2, §7.3, §8) |
| `artifacts/circdist_lift_iff_amendment1_20260820.md` | Amendment 1 (A1 Def 5.1′/Lemma 5.3′; A2 `R_sat` retraction) |
| `artifacts/circdist_lift_iff_amendment2_20260820.md` | Amendment 2 (L1 minimum-weight collision argument; L2; L3) |
| `artifacts/circdist_lift_proofs_review_20260820.md` | base independent adversarial review (the theorems) |
| `artifacts/circdist_amendments_review_20260820.md` | focused rereview of Amendment 1 (registers L1–L3) |
| `artifacts/circdist_amendments2_review_20260820.md` | the node's **only** hash-bound review; §7.1, §8.1, §9 |
| `artifacts/circdist_readjudication_20260823.md` | wave-11 re-adjudication, §7 (the question), §9 (the root) |
| `artifacts/circdist_lift_root_review_20260822.md` | root clearing review, §4.2 finding **F2** |
| `artifacts/circdist_amendments4_review_20260822.md` | §2.2 — **C-M7 CONFIRM** |
| `research/circdist/notes/CIRCDIST_PROBLEMS.md` | frozen 公共定义 (lines 31, 103, 110, 126) |
| `research/DAG_PROTOCOL.md` | §2, §3, §5 — the bar |
| `research/circdist/proof-dag/nodes/CIRCDIST.lift.yaml`, `.nonint.yaml` | parent and sibling, for consistency |

Not read as evidence, and not relied on: the `cplx`, `gross`, and `sat` families beyond the
cross-node notes quoted in the lift documents.

---

## 2. The bar I applied

`DAG_PROTOCOL.md` §3, verbatim: `PROVED` = "A **complete argument** and **all load-bearing inputs**
passed independent adversarial review"; `CERTIFIED*` = "An independently reviewed **conditional**
result with **explicit unresolved premises or scope caveats**."

I adopt the wave-11 adjudicator's rule 2 unchanged, because `task-007` is built on it: *an exclusion
is not a caveat*. Material lying **outside** the claim does not force `CERTIFIED*`; what forces
`CERTIFIED*` is a condition the claim **as written** needs and does not have. The whole of `task-007`
is the question of which side of that line the `repair ≥ 3` gap falls on.

The deciding question, as commissioned: **does the claim as hashed, read with the proof's own
definitions, assert anything whose proof needs `repair ≥ 3`?**

---

## 3. Conjunct 1 — the lift identity

**Claim text.** "*`d_circ` equals the minimum over nontrivial effective logicals `gamma` of the
length of the shortest closed spacetime lift of `gamma`*".

**Referent.** This is Theorem 5.6**(a)** of the proof document verbatim:
`d_circ(C_R(M)) = min_{γ ∈ L_eff} ℓ(γ)`, with `ℓ` Definition 5.1 as corrected to Definition 5.1′
(Amendment 1 §2.3). It is also 公共定义 line 110 verbatim.

**RULING: repair-independent — the term `repair` does not occur in the statement or in either half
of its proof.**

Chapter and verse:

* Proof §5.4, derivation of 5.6: "*(a) `≤`: every closed lift of every `γ ∈ L_eff` is an undetectable
  fault set with `λ ≠ 0` (5.3). `≥`: 5.4(1) sends a minimum-weight undetectable logical `F` to
  `γ = π_1 F ∈ L_eff`, and `F` is itself a closed lift of `γ`, so `|F| ≥ ℓ(γ)`.*" The status line
  reads "*(a), (b), (c) complete*". The sandwich is 5.6(b); (a) does not cite it.
* Amendment 1 §2.6, row 1: "**5.6(a)** `d_circ = min_γ ℓ(γ)` — **survives verbatim** under 5.1′",
  with both directions restated. Amendment 2 touches L1/L2/L3 only and does not reach 5.6(a).
* Proof §7.1 status table lists "5.6 for `repair ≥ 3`" as a **separate row** from every row that
  carries (a); the GAP row is `5.6` in its `repair ≥ 3` reading only.

**On the "renaming" reading.** The wave-11 decisive sentence rests on proof §4.3: "*`d_circ = min_γ
ℓ(γ)` alone is a renaming*". That sentence is accurate and I do not dispute it — but it is a remark
about the identity **stripped of its `≥` direction's content**, and §4.3's own subject is the
*decision-procedure* requirement (it closes by naming 公共定义 line 126, the
"不需要构造完整多轮电路的等号判定算法"), i.e. conjunct 3, not conjunct 1. As **proved**, 5.6(a)'s `≥`
direction is 5.4(1), which is not bookkeeping: it is the statement that the projection **cannot**
destroy non-triviality, established via the identity of linear maps `λ_circ = λ_eff ∘ π_1` (proof
Remark 5.5). That step is exactly what defeats the load-bearing literature hazard imported from
`circdist_lift_litverify2_20260820.md` — homology systole is *not* monotone under covers, so
"a lifted cycle projects to a nontrivial cycle" is false in general and had to be earned here. The
base review reconstructed it line by line and ruled "**Correct**", calling it "*the step that answers
the systolic-non-monotonicity warning*" (`circdist_lift_proofs_review_20260820.md` §4.3, item 1).
A renaming does not require a theorem to rule out a published counterexample mechanism.

**Hypothesis it does carry:** `R ≥ d`. See §6.

---

## 4. Conjunct 2 — the zero-voltage characterization of same-weight liftability

**Claim text.** "*with an intrinsic zero-voltage/monodromy condition characterizing same-weight
liftability*".

**Referent.** Theorem 5.7, with the proof's own gloss (proof §5.5, immediately after the derivation):
"*This is the node's requested iff, with `volt(γ) = 0` made precise as `repair(γ) = 0`, i.e. by
(LIFT′)*". "Same-weight liftability" is `ℓ(γ) = |γ|`; the condition is `repair(γ) = 0`. This is
公共定义 line 103.

**RULING: `repair-0`-scoped, and unconditional in `repair` — proved at `repair(γ) = 0` on both sides,
with the `repair ≥ 3` regime provably unable to arise.**

Chapter and verse:

* **(⟹) is explicitly hypothesis-free.** Proof §5.5, derivation status line of 5.7: "*complete. Note
  this direction needs no hypothesis on `repair` — the case `repair(γ) ≥ 3` cannot arise when
  `d_circ = d_eff`.*" The argument: `|F| = d_eff` forces `n_∅ = 0` and `m = 0`, hence `A_∅ = 0`,
  hence by (LIFT) `A_ess + xC = 0`, hence the certificate read off `F` has weight `0`.
* **(⟸) uses the sandwich only at its weakest point.** The lower bound invoked is 5.4(4),
  `|F| ≥ |γ| + min(repair(γ), 2)`. At `repair ≥ 1` this already gives `ℓ(γ) ≥ |γ| + 1`, which is all
  the biconditional needs; the `repair ≥ 3` gap lives entirely in the difference between
  `min(repair,2)` and `repair`, and that difference is **identically zero at `repair = 0`** and
  irrelevant to a statement that only distinguishes `repair = 0` from `repair ≥ 1`. 5.4(4) itself is
  a theorem for all `repair` — Amendment 1 §2.6 row 3: "**5.6(b)** lower `|γ| + min(repair,2) ≤ ℓ(γ)`
  — **survives verbatim** (it is 5.4(4), untouched)". The half that is *not* a theorem for
  `repair ≥ 3` is the **upper** half `ℓ(γ) ≤ |γ| + repair(γ)`, which conjunct 2 never uses beyond
  `repair = 0`, where it is 5.3′ applied to a zero-weight certificate.
* **Independent review.** Base review verdict **G**: "*CONFIRM [D][N] — survives F*"; proof §7.1
  status table, row "5.7 **the iff** — **complete**". The one-line collision repair the base review
  demanded is applied in Amendment 1 §2.7 ("in either branch") and re-reviewed.

**Hypotheses it does carry:** `R ≥ d` (§6), and — for the reading quantified over *all* `γ ∈ L_eff`
rather than minimum-weight `γ` — the distinct-location proviso. Amendment 1 §2.6 records that the
upper half of 5.6(b)/(c) is "**weakened**: holds when the optimal certificate admits distinct-location
representatives (5.3′(a)); unconditionally only in the form `d_circ ≤ |γ| + repair(γ)`", and §2.5
plus Amendment 2 §2 (L1) establish branch (a) **at minimum weight**. This is a live restriction of
conjunct 2 as written, partially registered in the node's existing caveat 2 ("the reviewed
**minimum-weight** repair-0/closed-lift criterion"). It is *not* a `repair ≥ 3` matter.

---

## 5. Conjunct 3 — the non-vacuity bar

**Claim text.** "*and the voltage is computable without constructing the full multi-round circuit
(non-vacuity bar)*".

**What "the voltage" refers to.** The phrase is anaphoric: conjunct 2 has just introduced "an
intrinsic **zero-voltage**/monodromy condition", and conjunct 3 says "**the** voltage". Read with the
proof's own definitions, the referent is fixed by proof §5.5 — `volt(γ)` **is** `repair(γ)`, defined
through (LIFT′). It is **not** `ℓ(γ)`: the proof never calls `ℓ` a voltage, `ℓ` is a *length*
(Definition 5.1′), and the claim already spent conjunct 1 on `ℓ`. Reading "the voltage" as `ℓ(γ)`
would also make conjunct 3 a restatement of conjunct 1 rather than the separate non-vacuity bar the
parenthesis announces.

**RULING: `repair-0`-scoped/unconditional — the one-round computability of the (LIFT′) data is proved
without any hypothesis on `repair`, by two independent routes.**

Chapter and verse:

1. **The object is one-round by definition.** Definition 5.2, closing sentence: "*`repair(γ)` depends
   only on the one-round data `{(E, s(E), U(E), λ(E)) : E ∈ ℰ}`.*"
2. **(LIFT′) is one-round by construction.** Proof §4.2, the boxed gloss: "*This is the intrinsic
   'voltage' the node asked for. It is `F₂`-valued (no orientation ambiguity), it is computed from
   one round's `(E, s, u)` data plus a round assignment, and **no multi-round circuit is ever
   built**.*" Derivation status of 4.2 and 4.3: **complete**; §7.1 table row "4.2 / 4.3 (LIFT),
   (LIFT′)" needs only ideal boundaries — no (V), no (MC), no graph-likeness, no `repair` bound.
3. **The zero test is decidable from one round.** Theorem 5.7, second sentence: "*Moreover
   `repair(γ) = 0` is decidable from one round of `M`*". The search is finite without 5.10(3):
   a `repair-0` certificate yields (5.3′) a closed lift of weight `|γ|`, which at minimum weight is a
   minimum-weight undetectable logical, whose round-span is `≤ |γ| ≤ d` by contiguity (5.9).
4. **And `d_circ` itself is one-round computable, unconditionally.** 5.10(2): "*`d_circ` is computable
   from the one-round data `{(E(f), s(f), u(f), λ(f)) : f ∈ 𝔽}` alone, by a search over fault
   multisets of size `≤ d` distributed over `≤ d` consecutive rounds. **No multi-round circuit is
   constructed at any point.**" Derivation: "*5.9 plus (LIFT′)*"; status "*(1) and (2) complete*".
   Amendment 1 §2.6, last row: "**5.9 / 5.10(2),(3)** — **unchanged.**" This route uses **no**
   `repair` term at all, and the proof itself deploys it as the non-vacuity deliverable — §8 item 3:
   "*That is a one-round computation per schedule (5.10(2)) — expensive but not exponential in `R`.*"

**Disposing of the wave-11 reading.** §7 of the re-adjudication pins conjunct 3 to proof §4.3's
"(a)+(b)+(c) together are a decision procedure", of which (b) is the sandwich. That is a fair reading
of §4.3 taken alone, and §4.3 *is* the section that answers 公共定义 line 126. But two things move it:

* §4.3's route is **sufficient, not necessary**. 5.10(2) supplies a strictly stronger, `repair`-free
  decision procedure for the same object in the same document. A claim is not conditional because
  *one* of its available proofs is conditional.
* The node's **own hash-bound review** already puts `repair ≥ 3` outside the claim. Its completion
  verdict (`circdist_amendments2_review_20260820.md` §7.1) reads: "*the general `repair >= 3` formula
  and the pre-existing 5.6(d) concern remain **outside this claim/review**.*" The reviewer that
  licensed the star treats the gap as an exclusion, not as a qualifier on the clause.

**A note on the other reading of "computable".** If conjunct 3 were read as "`repair(γ)` is computable
**as a number** for every `γ`", then 5.10(3) would bite: its own status line restricts it to "*the
minimum over certificates that are realised by a minimum-weight closed lift*", and the base review
agrees (§5 item 4: "*flagged by its own status line as complete only in a weaker reading … it is not
used by (a)–(d)*"). This is a further, independent reason to read conjunct 3 at `repair = 0`, which
is what the non-vacuity bar actually needs and what 5.7 and 5.10(2) deliver.

---

## 6. The finding that decides the level — `R ≥ d`, unregistered on this node

`task-007` asks a `repair`-scoping question and I answer it in the affirmative (§7). But the
commission also asks whether the node clears to `PROVED`, and it does not — on a ground `task-007`
did not consider, and one that is **already an independent reviewer's required finding against this
node's claim text**.

**The hypothesis.** Theorem 5.7 as printed reads "*For every legal, measurement-consistent
single-ancilla CSS schedule `M`, **and `R ≥ d`**, …*", and Theorem 5.6 opens "*Then for `R` large
enough (`R ≥ d` suffices, by §5.7)*". The hypothesis is load-bearing on the (⟸) side: a `repair-0`
certificate of round-span `σ` produces a closed lift only in a circuit with `R > σ`, and `d_R` is
known only to be non-increasing and constant for `R ≥ d` (5.10(1′), Amendment 1 §3).

**It was already found, and found against *this* claim.** `circdist_lift_root_review_20260822.md`
§4.2, finding **F2 (required)**:

> "*the **root claim** has no `R` quantifier and no `C_R(M)` … the **`lift.iff` child claim** has no
> `R` quantifier either*"

and the type-audit sentence: "*`d_circ` has type `(circuit) → ℤ`, the circuit is `C_R(M)`, and the
root claim never binds `R`.*" That reviewer probed for a live counterexample at `d = 2` and did not
find one, and said so — then declined to discharge the hypothesis: "*a hypothesis of the certified
theorem is a hypothesis of anything assembled from it*". `circdist_amendments4_review_20260822.md`
§2.2 **CONFIRMs** it, and it now rides on the parent as
`CIRCDIST.lift` caveat 2, "BINDING (review condition, C-M7)".

**Why it blocks here.** The parent's criterion clause is the child's conjuncts 1–2 — the first is
word-for-word identical ("`d_circ` equals the minimum over nontrivial effective logicals gamma of the
length of the shortest closed spacetime lift of gamma"). The wave-11 adjudicator's own decisive
sentence for the root (§9) is that this hypothesis, absent from the claim text, makes "*the claim as
written strictly broader than what is argued: §3's 'explicit … scope caveat', i.e. `CERTIFIED*`*".
That reasoning transfers to `CIRCDIST.lift.iff` unchanged. `CIRCDIST.lift.iff`'s caveat list carries
per-sector scope, `repair ≥ 3`, the unreproduced scans, 5.6(d), and model fact (V) — and **no `R`
condition at all**. Wave-11 §7 does not discuss `R ≥ d`; the finding predates it by a day and was
raised at the root, where it stopped.

I checked the parallel case for consistency: `CIRCDIST.lift.nonint` is at `PROVED` with no `R`
qualifier, and correctly so — its Theorem 7.1 / 5.11 concludes "*for all `R ≥ 1`*", so there is
nothing to bind. The asymmetry is real, not an artefact.

**Minimal scope qualifier (exact proposed wording).** Two insertions into the claim text; nothing
else changes. Insertion **A** is required; insertion **B** is required under the all-`γ` reading of
conjunct 2 and is otherwise a sharpening of existing caveat 2.

> In graph-like detector error models with fixed boundaries, **for memory experiments C_R(M) with
> R >= d,** d_circ equals the minimum over nontrivial effective logicals gamma of the length of the
> shortest closed spacetime lift of gamma, with an intrinsic zero-voltage/monodromy condition
> characterizing same-weight liftability **at minimum weight** — and the voltage is computable
> without constructing the full multi-round circuit (non-vacuity bar).

Adopting this rewrites the claim and therefore **invalidates `reviewed_hash` `c3a84198…`**
(`DAG_PROTOCOL` §5: "*a completion assessment becomes invalid if that statement later changes*"). The
repaired string must be re-hashed and re-bound by a review that reads it — the procedure
`CIRCDIST.lift.nonint` already went through on 2026-08-23 with
`artifacts/circdist_claimrepair_review_20260823.md`. The alternative — leaving the claim text alone
and adding an `R ≥ d` caveat — is hash-neutral but *keeps the node at `CERTIFIED*` by construction*,
since a caveat restricting the claim as written is precisely what §3 calls a scope caveat.

---

## 7. Verdicts

### 7.1 Per conjunct

| # | conjunct | referent | ruling on `repair` scope | other live hypotheses |
|---|---|---|---|---|
| 1 | `d_circ = min_γ ℓ(γ)` | Thm 5.6(a) + Def 5.1′ | **repair-independent**; unconditional. Not a renaming: the `≥` direction is 5.4(1), which earns non-triviality-under-projection against the systole hazard | `R ≥ d` |
| 2 | zero-voltage ⟺ same-weight liftability | Thm 5.7, `volt := repair` (§5.5) | **`repair-0`-scoped**; (⟹) explicitly hypothesis-free, (⟸) uses only `min(repair,2) ≥ 1` | `R ≥ d`; minimum-weight `γ` for the all-`γ` reading |
| 3 | voltage computable without the multi-round circuit | (LIFT′) / Def 5.2 / 5.7 / 5.10(2) | **`repair-0`-scoped**; and 5.10(2) gives a `repair`-free decision procedure for `d_circ` itself | `R ≥ d` (5.10(2) searches `≤ d` rounds) |

### 7.2 The deciding question

**Does the claim as hashed, read with the proof's own definitions, assert anything whose proof needs
`repair ≥ 3`? — NO.** No conjunct asserts `ℓ(γ) = |γ| + repair(γ)` in general; the general formula
appears in the dossier only as future work (proof §7.2, §5.4's min-cost-covering form), and the
node's own hash-bound review already places it "outside this claim/review".

**Consequence for the node record:** caveat 1 should revert from a **scope caveat on the non-vacuity
clause** to a plain **exclusion** — the wave-11 prescription's "*KEEP … Promote this from an exclusion
to a scope caveat*" is, on this adjudication, the wrong direction. Proposed replacement text:

> EXCLUSION (adjudicated 2026-08-23, artifacts/circdist_iff_scope_adjudication_20260823.md): the
> general lift-length formula for repair >= 3 and its min-cost-covering replacement lie OUTSIDE this
> claim. All three conjuncts are repair-0-scoped: conjunct 1 is Theorem 5.6(a), in which no repair
> term occurs; conjunct 2 is Theorem 5.7, whose (=>) needs no hypothesis on repair and whose (<=)
> uses only min(repair,2) >= 1; conjunct 3's "voltage" is the (LIFT')/repair data of Definition 5.2,
> one-round computable unconditionally, with 5.10(2) supplying a repair-free decision procedure for
> d_circ. The hash-bound review states the same boundary (§7.1: repair >= 3 "outside this
> claim/review").

### 7.3 Overall

**NO — the node does not clear to `PROVED`, and I license nothing.**

The `task-007` question resolves in the affirmative, and that is real progress: the `repair ≥ 3` gap
is an exclusion, and the wave-11 decisive sentence for `CIRCDIST.lift.iff` no longer holds. But a
second, independently sourced scope condition — Theorem 5.7's `R ≥ d`, raised against this claim text
by name in `circdist_lift_root_review_20260822.md` §4.2 (F2), confirmed as C-M7, and binding on the
parent — restricts the claim as written and is registered nowhere on this node. Under `DAG_PROTOCOL`
§3 that is exactly "an explicit … scope caveat": `CERTIFIED*`.

**Level: STAYS-`CERTIFIED*`.** Not for the reason recorded on 2026-08-23.

### 7.4 What a `PROVED` upgrade now needs (short, and all of it cheap)

1. Apply the claim repair of §6 (insertion A, and B if the all-`γ` reading is intended).
2. Commission one claim-level review of the repaired string that re-hashes and binds it — the
   `lift.nonint` / `circdist_claimrepair_review_20260823.md` procedure.
3. Have that review close the one coverage note of §8 below (5.10(2)).
4. Fold §7.2's replacement caveat text in, and register model fact (V) once the protocol gap on
   route-free nodes is resolved by the lead (wave-11 §7, §6.3).

---

## 8. Completeness sweep of the three conjuncts' load-bearing inputs

Commissioned only for a YES, but the `repair` question *is* YES, so I record it — it is the sweep the
upgrade review inherits. Wave-11 §7 supplied the starting table; the review column below is what I
verified in the cited reviews myself.

| load-bearing input | where established | independent review covering it |
|---|---|---|
| (MC) ⟺ deterministic detectors (well-definedness of `d_circ`) | proof §2.2 | base review verdict **B** CONFIRM [V][D], re-derived pre-reading (§6.1) |
| 4.1 no temporal boundary correction (both ends detectored) | proof §4.1 | base review verdict **J** CONFIRM [D][N], §4.8 |
| 4.2 / 4.3 (LIFT), (LIFT′) | proof §4.2 | base review §4.3–§4.4 (used and re-derived line by line); end-to-end 3855/3855 (proposer), 282 instances (reviewer) |
| 5.4(1) `λ_circ = λ_eff ∘ π_1`; non-triviality survives projection | proof §5.3 | base review §4.3 item 1 — "**Correct**"; answers the litverify2 systole hazard |
| 5.4(2)(3)(4) exact weight accounting, `n_∅ + 2m` | proof §5.3 | base review verdict **E** CONFIRM [D][N], §4.3 all four parts |
| model fact (V) `U(∅) ⊆ {0} ∪ {e_b}` | proof §1.6, §7.3 | base review §4.2 — structural derivation from the frozen fault menu **plus** 440/440; wave-11 §1.1(3) re-confirms it is derived, not assumed |
| residual inventory 1.13 (`ℰ` = singletons ∪ X-check suffixes) | proof §1.6 | base review §4.2 — 1994/1994 realised classes, partition checked exhaustive |
| sector decoupling 1.9 | proof §1.4 | base review §4.7 CONFIRM (full two-sector search) |
| Def 5.1′ per-location weight convention | Amendment 1 §2.3 | base review verdict **M** CONFIRM ("the correct treatment of exactly the defect in F"); amendments rereview; amendments2 review §7.1 |
| 5.3′ (`≤`), branch (a) at minimum weight | Amendment 1 §2.4–2.5, Amendment 2 §2 (L1) | amendments2 review §3 — **CLEAN-PASS** on L1, schedule-independent |
| 5.6(a) | proof §5.4; Amendment 1 §2.6 | base review E/G neighbourhood; amendments2 review §7.1 assembled dossier |
| 5.7 the biconditional | proof §5.5; Amendment 1 §2.7 | base review verdict **G** CONFIRM [D][N]; 282/282 |
| 5.9 contiguity / finite window | proof §5.7 | base review verdict **H** CONFIRM [V][D][N], re-derived pre-reading; 203186/203186 |
| **5.10(2) one-round computability of `d_circ`** | proof §5.7 | **coverage note — see below** |

**Coverage note (the one hole).** 5.10(2) is the sentence that carries conjunct 3 unconditionally, and
it has **no verdict of its own** in any review. The base review's verdict **I** covers 5.10(**1**)
(REFUTE as stated, retracted by Amendment 1 A2); its §5 item 4 covers 5.10(**3**); the amendments2
review's scope is L1–L3 plus the assembled dossier. Both of 5.10(2)'s stated inputs — 5.9 and (LIFT′)
— are independently CONFIRMED, and Amendment 1 §2.6 records it unchanged, so I expect this to close
on a reading rather than on new mathematics. But under §3's "**all** load-bearing inputs passed
independent adversarial review" it is not yet closed, and I do not close it by assertion: a reviewer
other than me should state a verdict on the two-line corollary. This is item 3 of §7.4.

Everything else in the table carries an explicit independent verdict. In particular I confirm
wave-11's two audit corrections: 5.6(d) is **not** a premise of any of the three conjuncts (conjunct 1
is 5.6(a); nothing cites 5.6(d)), and (V) is **established** rather than assumed.

---

## 9. Task 4 — can the base review be added as a second properly-bound review link?

**Ruling: NO — `artifacts/circdist_lift_proofs_review_20260820.md` must stay `basis.evidence`
(`kind: text`), where wave-11 already put it.** Three reasons, in decreasing weight.

1. **It reviewed neither a claim nor a route implication.** `DAG_PROTOCOL` §5: the review link records
   `reviewed_hash`, "*the digest of the exact node claim or route implication reviewed*". The base
   review's own independence statement closes: "*I touched no file other than this one.
   `research/circdist/proof-dag/` was not read or written.*" It never saw the claim string, never
   computed a digest, and states no verdict on any claim. Attaching `c3a84198…` to it would be a
   third party asserting, after the fact, that a reviewer reviewed a sentence he did not read. The
   hash would validate mechanically and mean nothing — precisely the "filename check" §5 warns is not
   the point.
2. **Its verdict was not a completion clean-pass, and the dossier it reviewed is no longer the
   dossier.** It returned **GAP-AT-5.3** (verdict F — the `≤` direction's printed justification "*is
   false and self-contradicted*") and **REFUTE as stated** on 5.10(1) (verdict I), and issued six
   required edits. Both findings were repaired *afterwards*, by Amendment 1 (A1, A2) and Amendment 2
   (L1), and Amendment 1 governs where it conflicts with the base text. A §5 review link supports a
   *completion-level promotion of the assembled argument*; this review's subject is the pre-amendment
   assembly, and two of its verdicts were adverse. Binding it as a completion review would
   misrepresent what it certified.
3. **The repository's own current precedent says so.** `CIRCDIST.lift.nonint` sits at `PROVED` and
   faces exactly this situation: the base review is its principal mathematical attack (verdicts K, L,
   M, §4.5), yet its `basis.reviews` binds `artifacts/circdist_claimrepair_review_20260823.md`
   (`reviewed_hash: sha256:e2d1b292…`, which I recomputed and confirm), while
   `circdist_lift_proofs_review_20260820.md` is carried under `basis.evidence` as `kind: text`. The
   claimrepair review's `scope` field is explicit that it "*rests on the base review's Theorem 7.1
   verdicts*". That is the correct instrument, and it is already in service on the sibling.

**What to do instead.** The base review's authority is real and should be made reachable, not
retroactively re-typed. Two hash-neutral options, either acceptable:

* **(i) Preferred.** When the §6 claim repair is made and re-bound (§7.4 item 2), have that
  claim-level review name the base review in its `scope` string as the source of the underlying
  verdicts, exactly as `lift.nonint`'s does. The base review then carries binding force *through* a
  review that did read the claim.
* **(ii)** Sharpen the existing `basis.evidence` entry to a `basis.runs`-style scope line recording
  what it actually established — CONFIRM on Theorem 1, (MC) both directions, overlap-2 sharpness, the
  diagonal-hook correction, 5.4's accounting, 5.7, contiguity, boundary-freeness, sector decoupling,
  (V), and nonint Thm 7.1; GAP-AT-5.3 and REFUTE-5.10(1), both since repaired and independently
  re-reviewed; 282 / 203186 / 440 / 1994 instance counts on the reviewer's own code. That is
  informative without claiming a binding it does not have.

I take no position on whether the dispatcher prefers (i) or (ii); both are honest, and neither is a
promotion.

---

## 10. Limitations — what I did **not** do

1. **No new mathematics, and no re-derivation of any theorem.** This is a wording and scope
   adjudication, as `task-007` commissions. I did not re-derive Theorem 1, Theorem 2, 5.7, 5.9, or
   5.10, and I ran **no** quantum-circuit simulation. Where I rely on a mathematical fact I cite the
   document that states it and the review that attacked it; where a fact is unreviewed (5.10(2)) I say
   so rather than supply the verdict myself.
2. **My only computation is the hash pipeline** (§0), ~6 lines of `yaml` + `hashlib`, run against
   three nodes and validated against three pre-existing `reviewed_hash` values.
3. **I did not reproduce any proposer scan** — 98811 surface schedules, 3855/3855, 349/349,
   321059/321059 all remain NOT-REVIEWED as such, exactly as the node's caveat 3 records. None is
   load-bearing for the three conjuncts (they corroborate; the conjuncts rest on derivations).
4. **I did not attack the shared-model caveat.** The 公共定义 fault inventory is the frozen problem
   statement; I applied wave-11's rule 3 unchanged, with its qualification that the one singled-out
   model fact, (V), was checked and is derived.
5. **`R ≥ d` is not demonstrably load-bearing on any instance in the campaign.** The root reviewer
   probed at `d = 2` and found `d_circ` unchanged at `R = 1`; I did not probe further and I did not
   look for a witness with `d_1 > d_eff = d_∞`. My finding is that the hypothesis is *stated* by the
   certified theorem and *unregistered* on the claim — a type/scope finding, not a refutation. If a
   future session proves 5.7 for all `R ≥ 1`, insertion A becomes unnecessary and this node clears
   without a claim rewrite.
6. **I adjudicated `CIRCDIST.lift.iff` only.** I did not audit the root, `lift.nonint`,
   `lift.gap-example`, or any `cplx`/`gross`/`sat` node, and nothing here should be read as
   revisiting their levels — including the root, whose own C-M7 caveat is already correct and whose
   level is separately gated on this node.
7. **This adjudication is unreviewed**, by me or anyone. It licenses no promotion and binds no hash.
