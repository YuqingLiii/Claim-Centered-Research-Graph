# Focused independent re-review — Amendment 1 to `circdist_sat_transfer_proof_20260823.md`

**Re-reviewer:** fresh Opus 5 session, independent. **Date:** 2026-08-23. **Box:** one session,
budget-boxed, no sub-agents. **Artifacts written:** exactly this one. **Canonical files modified:**
none (`research/circdist/proof-dag/` read only, as data).

---

## 0. Independence statement

I did not author the proof document, the review, or the amendment, and I hold no stake in any of
them. I was instructed to **refute**, not to confirm, and no desired verdict was communicated to me.

The amendment discloses (its §6 preamble) that its own verification harness **imports the proof
document's §11.4 simulator** (`transfer_doc`), so its checks are not independent of the document's
model design. That disclosure is accurate and it is the reason this re-review exists. Accordingly:

* I wrote **my own** circuit propagator, detector construction, parity-space computation,
  minimum-weight search, and min-plus transfer system, from Definitions 2.3–2.11 and §§3, 5, 6 of
  the proof document together with the frozen 公共定义 of
  `research/circdist/notes/CIRCDIST_PROBLEMS.md`.
* **No line of `transfer_doc.py` (§11.4) was copied, imported or executed.** I extracted that
  program from the artifact's bytes for one purpose only — to hash it (§5, Repair 3) — and did not
  run it.
* From the document I took only **data**: the code specifications (Steane Hamming checks, the
  rotated-surface check sets and logicals), the block-schedule ordering convention, and the
  corner→slot incidence and the two corner-order pairs of the interleaved surface schedules. These
  are instance specifications, printed largely in prose in the §11 scope paragraph; without them I
  could not be comparing the same instances.

My programs (this session's scratchpad, not part of the repository):

```text
6219b05ab34b989ead42cc64b83f107a31ae35e913cd9a76f236100cd48c1935  indep.py  propagator, detectors, min-weight search
ef8c33388b283a5ffb2c909aed2ca3729cd39ae2c9b170f982f3fa71a63255f9  t2.py     parity spaces V / 𝒟, the T-G3 counterexample
1505df3941641cdea212b709ad022b5efc576f751ef725110029067daa855c2b  t3.py     min-plus transfer system, Remark 6.5 family
edbf4acd720e7b0b7f6bdfdb97046eb2179b1196ddd2035d1c3871b7572ba3ed  t4.py     block-mirror relabelling
cd25f43d6dbe588a2437433c775f5e89e0faf50ad557170f3ec2df0f28a96492  t6.py     "pinned to κ = 0" adjudication
```

No external library, no `stim`, no sampling; single process, `nice -n 19`, a few seconds each.
**Background processes started by this session: none.**

### Method validation, before any repair was checked

My simulator and my transfer system were validated against published values *that are not in
dispute*, so that a later agreement or disagreement means something:

* my direct simulator reproduces Table 11.3 on the eight instances I use, at `R = 1,2,3`, including
  the discriminating `ilv1` pair whose per-sector distances are transposed (`Z: [2,2,2]`,
  `X: [3,3,3]`) — a schedule-sensitive signature;
* my independently built `(u, A, v)` reproduces my own brute force on the unmodified model,
  **24 / 24** values (8 instances × `R = 1,2,3`), which is also an independent re-confirmation of
  NUMERICAL 11.1 on those instances.

---

## 1. Materials, with hashes recomputed by me

```text
6c7a8fb756cfba958f82c70f739ffa90aee19070c2cae8f358d44ccdc20ad07e  artifacts/circdist_sat_transfer_amendment1_20260823.md   (TARGET)
4fce5371edc09fa153b41f6735d521d31500b84b55a0059c8b42dc000651da30  artifacts/circdist_sat_transfer_proof_20260823.md
a9afbf93713634237dfcb795d98e71072537e7370a3fa675dcdf1ac766110003  artifacts/circdist_sat_transfer_review_20260823.md
5f6dc37fcc33c0eb9f90e6267864740fc53b65c4acf1ee870c8d29ffd6d46c64  research/circdist/notes/CIRCDIST_PROBLEMS.md
1d3b8754b72d9dc77a8c16ecfab1c8b81f9dcfd5dd0a9abb2baf1b1a26e64c68  §11.4 program, extracted from the proof's bytes
```

The target's SHA-256 is the one I was given to verify: **it matches**. The amendment's own §0 hash
chain reproduces under my recomputation, including the three input digests it declares.

**Node record.** `research/circdist/proof-dag/nodes/CIRCDIST.sat.transfer.yaml` now hashes to
neither the proof's §0 declaration (`bb3f8464…`) nor the amendment's (`9578ae36…`), because two
further append-only events (`amendment1-2026-08-23`, and the review/ratification pair) have landed
since each was written. Both documents anticipated exactly this drift and recorded it as bookkeeping
rather than tampering. I confirm the drift is additive: the events the amendment quotes are present
and unaltered.

---

## 2. Scope of this re-review

**In scope.** (i) Repair-conformance of the four queued repairs against what the review prescribed
and the lead ratified; (ii) fidelity of every "before" quotation, spot-checked against the proof's
bytes; (iii) completeness of the declared dependent-passage edits and the absence of silent extra
changes; (iv) **independent** re-verification of the two computational repairs and of the mirror
relabelling; (v) the licensing question.

**Out of scope.** I did not re-derive Theorem T. The base review did that independently, before
reading, and recorded it as confirmed; this re-review takes that as its premise and checks only what
the amendment moves. I did not re-check items the review confirmed and the amendment does not touch
(the fault dictionary, §9's non-circularity, Lemma 6.1's 378,720-prediction test).

---

## 3. Repair-conformance sweep

I read the review's four prescriptions and the lead decision, then checked the amendment line by
line against them.

### 3.1 Fidelity of the quoted originals — **CLEAN**

Every "before" text the amendment quotes was spot-grepped against
`circdist_sat_transfer_proof_20260823.md`. All four are **verbatim and complete**, with no elision
that changes force:

| quoted passage | proof lines | verdict |
|---|---|---|
| §12 T-G3 "Three things reduce the risk…", bullets (a)(b)(c) | 1430–1434 | verbatim |
| §12 T-G3 closing "**What is not established…**" | 1434–1437 | verbatim |
| §12 preamble "**T-G3 is the one this session considers the sharpest**…" | 1392–1394 | verbatim |
| §13 final sentence "What this document does **not** settle…" | 1483–1485 | verbatim |
| §6 Remark 6.5 (first two sentences and remainder) | 603–610 | verbatim |
| §6 Remark 6.6 | 612–616 | verbatim |
| Corollary 9.2 | 724–729 | verbatim |
| Theorem T(a) box, "`w > 2` is false" clause | 74–76 | verbatim |
| §11.4 driver `build()` / `sched_corners_mirror` | 1265–1290 | verbatim |

### 3.2 Repair 1 — T-G3 bullet (a) — **CONFORMS**

The lead decision is quoted **verbatim** from node event `tg3-lead-ratification-2026-08-23`; I
compared it against the YAML word for word and it is exact, including the Chinese decision string
`批准 Definition 3.5, 缓解条款不批`. The decision splits three ways and the amendment executes all
three, correctly:

* **Definition 3.5 RATIFIED** — the amendment leaves Definition 3.5, CONJECTURED 3.6 and CONJECTURED
  3.7 **unchanged, verbatim**, and says so explicitly in its dependent-passage table. Correct: the
  lead ratified them, so they must not move.
* **Mitigation NOT ratified** — bullet (a) is retired, not softened. The replacement states plainly
  that containment in `V` is **not** sufficient, quotes the retired text so the record shows what
  was withdrawn, and records the counterexample. This is precisely what the review asked for.
* **Corrected condition installed** — `span{D_{b,r}} ⊆ 𝒟' ⊆ 𝒟`, character-for-character the
  reviewer's formula and the lead's `D-prime within D`. The amendment supplies a derivation the
  review did not (both inequalities, from 3.1(2) plus the 3.6 equality); I checked that derivation
  and it is correct.

The residual risk is restated as **larger**, not smaller, as the review demanded.

**One judgement call, and I endorse it.** The amendment propagates the closure to three further
passages (T-G3's closing sentence, the §12 preamble, the §13 residual list) that the review did not
itemise. This goes beyond the review's queued text but is *required* by the lead's "T-G3 is hereby
closed definitionally"; leaving those passages standing would have left the document contradicting
its own node record. Every one of the three is listed with full before/after. It is declared, not
silent, and I do not count it as scope creep.

**Epistemic hygiene: good.** Each propagated passage says the closure is "by decision, not by
derivation". That is the honest label and the amendment never lets it drift toward "proved".

### 3.3 Repair 2 — Remark 6.5 `v_κ` — **CONFORMS**

The review prescribed `(A_κ, v_κ)` with `H_Z σ_R = κ` and `λ(σ_R) = 1`. The amendment installs
exactly that, adds the one-line derivation of the terminal detector, and correctly explains *why*
Lemma 6.3's shortcut is unavailable (`σ_R ∉ ker H_Z` once `κ ≠ 0`). It also states the containment
that matters — "at `κ = 0` the two coincide, which is why nothing in Theorem T is affected" — and
keeps the derivation status at **CONJECTURED + NUMERICAL**, not proved. The unchanged remainder
("Drop the terminal detector instead…") is correctly left alone.

The amendment flags, rather than edits, a node-event summary phrase that is silent about `v`. Correct
handling: the node is canonical and read-only for an amendment author.

### 3.4 Repair 3 — block-mirror labels — **CONFORMS**

The review prescribed: mirror the physical circuit (swap control/target at the same time step,
relabel the families), do not re-derive block order from the schedule name, re-emit Table 11.3.
The amendment's `mirror_steps` does exactly that, and `sched_corners_mirror` is deleted because the
general rule subsumes it — a simplification I checked is behaviour-preserving on the interleaved
rows (my own construction agrees with the published one there). Values unchanged, `diff` limited to
the wall-clock line.

### 3.5 Repair 4 — F4 / F5 cosmetics — **CONFORMS**

F4: irreducibility language restricted to the single-sector `A^Z`, with the block-diagonal assembled
`A` explicitly called **reducible** and A1 applied blockwise; A1 stays declared non-load-bearing.
F5: "is false" downgraded to "would require enlarging the state space … out of scope", with an added
disclaimer that no smaller sufficient statistic is being ruled out; and §3.6's **equality** credited
with forcing `w = 2` rather than Definition 2.7. Both are what the review asked for, and F5's
replacement is, if anything, more careful than the prescription.

### 3.6 Silent extra changes — **NONE FOUND**

I enumerated every governing change in the amendment: **11 edits** (4 under Repair 1, 1 under Repair
2, 1 under Repair 3, 5 under Repair 4). Every one falls inside the four queued repairs. Every
dependent passage is listed with before/after or unchanged-with-reason; I spot-checked the
"unchanged" rows (§3.3 preamble, §10 danger table S3′ row, §7's (≥)-direction, §8 CONJECTURED 8.1,
NUMERICAL 11.1/11.2) and each reason is correct — in particular the §10 S3′ row does argue from
3.1(2) + the 3.6 equality and never invokes the retired bullet, and NUMERICAL 11.2 genuinely never
took the defective driver branch.

**One declared addition**, not a change: the amendment files its own check as a new **NUMERICAL
11.6**. It is labelled, scoped, and code-backed; my §5 below now supports it from outside.

---

## 4. Independent re-verification — T-G3 counterexample (Repair 1)

Rebuilt `steane+redX` (Steane with `𝒜` enlarged by the sum of its three X-checks) with my own
propagator. Parity spaces computed by my own method: a parity `P` is deterministic iff its
back-propagated Pauli lies in `G_0`, and since `G_0` is a *maximal* stabiliser group this is
equivalent to `P` being unflipped by every generator of `G_0` injected as an input error — which my
forward propagator computes directly. `𝒟` is then the further kernel of the `X_L` value-shift.
This shares nothing with the document's construction.

```
R=2  #records 21   dim V 15   dim 𝒟 14
     λ in V: True   λ in 𝒟: False   P_X in V: True   P_X in 𝒟: True
     rank 𝒟' = 14 (= dim V − 1)   rank 𝒟' ∪ {λ} = 15 (= dim V)   λ ∉ 𝒟': True
     𝒟' ⊇ Def-2.7 set: True   𝒟' ⊆ V: True
     rank span{D_b,r} = 9    rank span{D_b,r} ∪ {D_a,r} = 13
     d_R against Def-2.7 = 2      d_R against 𝒟' = 3
R=3  #records 28   dim V 22   dim 𝒟 21
     λ in V: True   λ in 𝒟: False   P_X in V: True   P_X in 𝒟: True
     rank 𝒟' = 21 (= dim V − 1)   rank 𝒟' ∪ {λ} = 22 (= dim V)   λ ∉ 𝒟': True
     𝒟' ⊇ Def-2.7 set: True   𝒟' ⊆ V: True
     rank span{D_b,r} = 12   rank span{D_b,r} ∪ {D_a,r} = 20
     d_R against Def-2.7 = 2      d_R against 𝒟' = 4
XOR of the four X-checks of steane+redX = 0   (so P_X is deterministic)
```

**CONFIRMED, every figure.** `d^{2.7} = 2` against `d^{𝒟'} = 3` at `R = 2` and `4` at `R = 3`; the
`R = 3` dimension quintuple is **28 / 22 / 21 / 12 / 20**, exactly as claimed. `𝒟'` really does
satisfy the retired bullet's hypothesis *and* the stronger complement-of-the-observables reading.
Bullet (a) is false, and it is false in the dependent-generator case scope clause T0/T1 puts
explicitly in scope.

**Additional probe the amendment did not run.** Refuting the old condition does not establish the
new one, so I tested the *installed* corrected condition at its tightest endpoint — `𝒟'` taken as
`span{D_{b,r}}` alone, the smallest space the condition allows, with every `D_{a,r}` dropped:

```
steane+redX  R=2/3   d against span{D_b,r} = 2 = d against Def-2.7 set
surface913   R=2/3   d against span{D_b,r} = 3 = d against Def-2.7 set
steane713    R=2/3   d against span{D_b,r} = 2 = d against Def-2.7 set
```

The installed replacement survives at the boundary where it is most exposed. This is corroboration,
not proof; the amendment's derivation of it is the actual warrant, and I checked that derivation.

---

## 5. Independent re-verification — `v_κ` (Repair 2)

I implemented the min-plus system **from the amended text alone**: `Σ = F₂ⁿ/S_X` by coset
enumeration; one-round X-sector columns `(E, u)` from my own single-round propagation; `w_M` by my
own BFS over `F₂^{n+|ℬ|}`; `A_κ[σ,σ'] = min_{g ∈ S_X} w(σ+σ'+g, H_Zσ + κ)`; `u`, `v`, `v_κ` as
displayed. Ground truth is my own direct multi-round simulator with **every `D_{b,0}` deleted**.

```
instance                   R=2                              R=3
steane713/blkZ/Z           truth 1  Rem6.5 2  corrected 1   truth 1  Rem6.5 2  corrected 1
steane713/blkZ/X           truth 1  Rem6.5 2  corrected 1   truth 1  Rem6.5 2  corrected 1
surface913/blkZ/Z          truth 1  Rem6.5 3  corrected 1   truth 1  Rem6.5 3  corrected 1
surface913/blkZ/X          truth 1  Rem6.5 2  corrected 1   truth 1  Rem6.5 2  corrected 1
steane+redX/blkZ/Z         truth 1  Rem6.5 2  corrected 1   truth 1  Rem6.5 2  corrected 1
steane+redX/blkZ/X         truth 1  Rem6.5 2  corrected 1   truth 1  Rem6.5 2  corrected 1
surface913/ilv1/Z          truth 1  Rem6.5 2  corrected 1   truth 1  Rem6.5 2  corrected 1
surface913/ilv1/X          truth 1  Rem6.5 3  corrected 1   truth 1  Rem6.5 3  corrected 1

  Remark 6.5 as printed agrees with the truth : 0 of 16
  corrected v_κ agrees                        : 16 of 16
```

**CONFIRMED.** The printed formula is wrong in 16/16, the corrected `(A_κ, v_κ)` right in 16/16, and
the per-instance printed values `2,2,3,2,2,2,2,3` at both `R = 2` and `R = 3` match the review and
the amendment row for row, from a wholly separate implementation.

### Adjudicating the amendment's sharpening — **substantively right, one word too strong**

The amendment (§6.4) sharpens the review's diagnosis to: the printed formula "is pinned to `κ = 0`,
i.e. it returns the value of the *unmodified* model". I tested both halves separately across all 16:

```
printed formula's min over κ == unmodified-model d_R in every case : True   (16/16)
minimum attained ONLY at κ = 0                                     : False  (0/16)
   |argmin| = 3, 4 or 8 depending on instance; e.g. steane713/blkZ/Z argmin = {0,2,4},
   surface913/blkZ/Z argmin = {0,1,2,4,5,6,8,10}
```

* **The substantive claim is CONFIRMED.** Holding `v` fixed makes the family return the *unmodified*
  model's `d_R` — the deletion of `D_{b,0}` becomes invisible. That is the real defect, and it is a
  genuine sharpening of the review, which said only that the formula "computes the wrong number".
* **The phrase "pinned to `κ = 0`" is loose.** Read literally as a statement about the minimiser it
  is false: several `κ` tie for the minimum in every instance I tested. What is pinned is the
  **value**, not the argument. The amendment's own following clause ("i.e. it returns the value of
  the unmodified model") is the accurate statement, so a reader is not misled — but the leading
  phrase, taken alone, would be.

I record this as a **precision note, not a repair item**: it sits in the amendment's §6.4 *reading of
the output*, not in the governing replacement text of §3.2, which is correct as written and is what
would enter the proof document. It does not affect the verdict. Were §6.4's phrasing ever promoted
into governing text, it should read "its value is pinned to the `κ = 0` value".

---

## 6. Independent re-verification — block mirror (Repair 3), and the program hash

Built each block schedule myself and applied my own mirror rule (conjugation by `H^{⊗all}`: same
time step, control↔target, families relabelled), then compared against what the published driver
constructs. All six rows, not the two required:

```
steane713    blkZ X-sector: == mirror of blkZ? False   == mirror of blkX? True
steane713    blkX X-sector: == mirror of blkZ? True    == mirror of blkX? False
surface913   blkZ X-sector: == mirror of blkZ? False   == mirror of blkX? True
surface913   blkX X-sector: == mirror of blkZ? True    == mirror of blkX? False
steane+redX  blkZ X-sector: == mirror of blkZ? False   == mirror of blkX? True
steane+redX  blkX X-sector: == mirror of blkZ? True    == mirror of blkX? False
  block rows built from the WRONG physical schedule: 6 of 6
  surface913 ilv0 / ilv1 X-sector: == my circuit-mirror? True / True
```

**CONFIRMED**, including the amendment's claim that the interleaved rows were already correct. The
correctly-labelled block `X`-sector instances give `[2,2,2]` for all three codes at `R = 1,2,3`, so
**no printed value changes** — the defect is purely denotational, exactly as claimed.

**The hash claim — CONFIRMED, and it matters.** I extracted the §11.4 program from the proof
document's own bytes and hashed it:

```
1d3b8754b72d9dc77a8c16ecfab1c8b81f9dcfd5dd0a9abb2baf1b1a26e64c68  (extracted §11.4 program)
1d3b8754b72d9dc77a8c16ecfab1c8b81f9dcfd5dd0a9abb2baf1b1a26e64c68  (digest declared in the proof's §0)
```

Identical. So the mislabelling is a defect **in the published, hashed verification program**, not a
transcription slip introduced when the code was pasted into the document. The amendment is right to
record this rather than quietly patch it: it means the document's own §0 attestation covered
defective code, and the superseding digest `f3dfa1f9…` must be bound by any future re-run.

---

## 7. Attempts to refute that failed

Recorded so the verdict's weight is legible. I tried and could not: break the corrected T-G3
condition at its smallest allowed endpoint (§4); find a `κ` at which the printed Remark 6.5 formula
beats the unmodified value (none — the fixed `v` bounds it from below); find a seventh mislabelled
row or a mislabelled interleaved row (none); find a governing edit not traceable to one of the four
repairs (none); find a "before" quotation altered in transcription (none); find a value in Table 11.3
that Repair 3 changes (none); find a disagreement between my transfer system and my brute force on
the unmodified model (none in 24 comparisons).

---

## 8. Verdict

> ### CLEAN-PASS
>
> All four queued repairs are applied exactly as the review prescribed and the lead ratified, with
> faithful quotation, complete dependent-passage accounting, and no silent extra change. Both
> computational repairs and the mirror relabelling are **independently reproduced by a method
> sharing no code with the document**, closing the non-independence the amendment itself disclosed.

The one blemish — the over-strong phrase "pinned to `κ = 0`" in the amendment's §6.4 commentary — is
a reading note, not governing text, and its own following clause states the matter correctly. It
does not warrant FURTHER-REPAIR.

---

## 9. What I license

Under `research/DAG_PROTOCOL.md` §3 and §5(5), for node **`CIRCDIST.sat.transfer`**:

> **`CONJECTURED` → `CERTIFIED*`**

`CERTIFIED*` is "an independently reviewed conditional result with explicit unresolved premises or
scope caveats", which is exactly the state of this dossier: the core theorem was independently
confirmed by the base review before reading; that review's FURTHER-REPAIR list is discharged by this
amendment; and this re-review has verified the discharge by an independent method. `PROVED` is
**not** licensed — the caveat set below is non-empty and load-bearing premises remain imported.

**Bound hash** (the node's `claim` field; `yaml.safe_load`, CRLF→LF, `strip`, UTF-8, SHA-256 —
pipeline validated against two existing `reviewed_hash` values elsewhere in the repository,
`SE.denom.decomp` `43772a80…` and `SE.denom.Phi.legal.diag` `b0fad698…`, both reproduced exactly):

```text
reviewed_hash: sha256:eb50730d33e716c13be3d46fa92afab98a9e223aa2ac46aff960a9fcd9896ca5
```

The completion assessment becomes invalid if the claim text changes.

### Caveat set (all must be recorded with the level)

1. **T-G1 — inherited model.** Definition 2.8's fault taxonomy and scope clauses T2, T3 are
   imported, not re-derived. T3 in particular identifies 公共定义's `d_circ` with `min(d_R^Z, d_R^X)`
   by inherited convention.
2. **T-G2 — minimality of `Σ`.** Open, and value-neutral.
3. **T-G3 — closed definitionally, by decision, not by derivation.** Definition 3.5 is ratified as
   the intended reading of the frozen 公共定义 by lead decision. The mitigation is **refuted**; only
   splits satisfying `span{D_{b,r}} ⊆ 𝒟' ⊆ 𝒟` are covered, and a split merely inside `V` can change
   `d_R` (verified: 2 vs 3/4).
4. **T-G4 — computability.** `A` is exponential to build; NP-hardness is explicitly *not* claimed.
5. **T-G5 — scope of finiteness.** A model lacking both weight-1 mechanisms would break Corollary
   9.2's irreducibility and the "no unreachable states" clause of the node claim.
6. **Model dependence of the `Y`-projection.** The weight-non-increasing projection to the `x`-part
   is legitimate only because Definition 2.8 makes all 15 (resp. 3) Paulis available at unit cost.
   Under non-uniform fault weights it fails. This is a caveat on the claim's phrase "unit-fault
   model" and I add it explicitly.
7. **Numerical corroboration scope.** §11 covers `d = 3`, `k = 1`, `R ≤ 3`, three small codes
   (two of them `[[7,1,3]]`), no genuine qLDPC instance, and no claim about `R_stab ≥ 2`. The
   *theorem* is stated generally (scope clause T1: all CSS, `k ≥ 1`, any weights, interleaved or
   not); the *evidence* is not. `d ≥ 5`, `k > 1` and qLDPC are untested, and the `2^k`-vs-`2^{2k}`
   correction and the `2^k − 1` count of finite `v` entries are precisely where `k > 1` would
   discriminate. The review's cheap `[[4,2,2]]` closure was deliberately not folded in.
8. **§11.4's published program carried a real defect** under the document's own §0 digest. Repair 3
   supersedes it with `f3dfa1f9…`; any re-run must bind the new digest.
9. **A1 (cyclicity theorem)** remains an external import, declared non-load-bearing.

I license only. The dispatcher executes the level change, the event append, and the review link.

---

## 10. Limitations of this re-review

* I did **not** re-derive Theorem T. Its independent confirmation rests on the base review, whose
  pre-read derivation I did not see and cannot audit; my agreement with its published numbers is
  evidence for the numbers, not for its sealed derivation.
* My instance data (check sets, logicals, schedule conventions, corner→slot incidence) comes from
  the document. A systematic error in the *specification* would be invisible to me; only the
  *machinery* is independent.
* My exhaustive minimum-weight search runs to weight 4. Every instance resolves at ≤ 4, so the
  reported minima are exact, but a hypothetical minimum above 4 would be reported as absent.
* The `v_κ` and T-G3 checks cover the same 8 (resp. 1) instances the amendment used. I widened the
  T-G3 corrected-condition probe to three codes but did not search for a counterexample to the
  corrected condition outside them.
* The `κ`-adjudication is over `κ ∈ F₂^ℬ` exhaustively for these instances only.
* I read the node record as data. I did not modify it, and I did not verify the repository checker
  would accept the promotion I license.
