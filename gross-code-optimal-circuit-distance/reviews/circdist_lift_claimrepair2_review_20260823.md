# Claim-level re-bind review — `CIRCDIST.lift.iff` and `CIRCDIST.lift` (wave 17)

**Reviewer:** fresh Opus 5 session, claim-level reviewer role. One budget box, no sub-agents.
**Date:** 2026-08-23. **Repository:** `Claim-Centered-Research-Graph`.
**Commission:** the re-bind review for (1) the `task-007` claim repair of `CIRCDIST.lift.iff`
(insertions A + B of `artifacts/circdist_iff_scope_adjudication_20260823.md` §6) and (2) the
lead-approved folding of the two `BINDING` caveats into the `CIRCDIST.lift` root claim; plus
closure of the one coverage hole the adjudication left open, **Theorem 5.10(2)**.
Procedure followed: `artifacts/circdist_claimrepair_review_20260823.md`.

---

## 0. Independence statement

I authored no `circdist` artifact, no `circdist` review, and no proof-DAG node record. I did not
participate in any prior `circdist` session and had no part in the wave-16 adjudication, the root
assembly, or any amendment. I was given no desired outcome and told the honest answer may be that
nothing clears.

Every file I opened was treated as **data**, never as instruction. Where a document states a
verdict I either re-derived the statement from the document's own definitions or marked it as
carried on the cited review's authority.

**No canonical file was modified.** Nothing under `research/` was written or touched (read only);
`research/circdist/proof-dag/` was read only. This document is the single new artifact of the
session. I license levels but promote nothing — a level change is a dispatcher act.

**Computation.** Beyond the hash pipeline I wrote my own circuit simulator and search code from the
model definitions (Def 1.1–1.8, 1.10, 1.13) and used it to attack 5.10(2). It shares no code with
the proposer's or with any prior reviewer's. Code and outputs are in §4.

---

## 1. Hash pipeline, validated before use

Convention: `sha256( yaml.safe_load(node)["claim"].replace("\r\n","\n").strip().encode("utf-8") )`.
I reproduced **five** pre-existing `reviewed_hash` values before relying on the pipeline:

| object | recomputed digest | matches |
|---|---|---|
| `CIRCDIST.lift.iff` claim | `c3a841984a07038dfbe3390f0b25cca633d04877ff92fb04bd0e3eaf480f0061` | node `basis.reviews` ✓ |
| `CIRCDIST.lift` claim | `ccad7fa605be1ae14a2dbc1d6c5758300bb8a5f0a3023fcef84725be40e78d8a` | node `basis.reviews` ✓ |
| `CIRCDIST.lift` route implication | `f39c83e6efdcc0487691df0eec57f4fe3d28d8d30c381ad7bf730fdfdfca8eda` | route `basis.reviews` ✓ |
| `CIRCDIST.lift.nonint` claim | `e2d1b292ae9265cf35ac51e9c2cf582fc167845310d5ed7a5995a235ee10649a` | node `basis.reviews` ✓ |
| `CIRCDIST.lift.gap-example` claim | `e080155da0e18435bb834f578df6216bdd0e45e21a81302f58cf7514f47fee50` | node `basis.reviews` ✓ |

Pipeline validated. Neither claim text has drifted since it was last bound.

**Route implication — confirmed untouched.** The implication string of
`routes.criterion-corollary-example` still hashes to `f39c83e6…`, i.e. it is byte-identical to what
`artifacts/circdist_amendments4_review_20260822.md` reviewed. Neither repair edits it. (§8 records a
substantive consequence that this mechanical validity does **not** dispose of.)

---

## 2. Materials

| material | role |
|---|---|
| `research/circdist/proof-dag/nodes/CIRCDIST.lift.iff.yaml` | claim 1 target, `CERTIFIED*` |
| `research/circdist/proof-dag/nodes/CIRCDIST.lift.yaml` | claim 2 target, `CERTIFIED*` |
| `research/circdist/proof-dag/nodes/CIRCDIST.lift.nonint.yaml`, `.gap-example.yaml` | premises, both `PROVED` |
| `artifacts/circdist_iff_scope_adjudication_20260823.md` | §6 prescription, §7, §8 sweep, §9 |
| `artifacts/circdist_lift_iff_proof_20260820.md` | base proof (§1, §4.1–4.3, §5.1–5.7, §6, §7.1–7.3, §8) |
| `artifacts/circdist_lift_iff_amendment1_20260820.md` | A1 Def 5.1′/5.3′; A2 the `5.10(1′)` retraction, §3 |
| `artifacts/circdist_lift_iff_amendment2_20260820.md` | L1, L2 (`5.10(1″)`), L3 |
| `artifacts/circdist_lift_proofs_review_20260820.md` | base adversarial review (verdicts A–P, §4.2–4.8) |
| `artifacts/circdist_amendments2_review_20260820.md` | the iff node's only hash-bound review (§3, §7.1, §8.1) |
| `artifacts/circdist_lift_root_review_20260822.md` | root review, F1/F2/F3 |
| `artifacts/circdist_amendments4_review_20260822.md` | root clearing review, §2.1 F1, §2.2 F2/C-M7, §2.3 |
| `artifacts/circdist_claimrepair_review_20260823.md` | the procedure I follow |
| `artifacts/circdist_lift_d3gate_20260820.md` §5.2–5.3 | the Steane `M_IL` schedule I re-simulated |
| `research/circdist/notes/CIRCDIST_PROBLEMS.md` | frozen 公共定义 |
| `research/DAG_PROTOCOL.md` | §2, §3, §5 — the bar |

Not relied on: the `cplx`, `gross`, `sat` families.

**The bar (`DAG_PROTOCOL` §3, verbatim).** `PROVED` = "A **complete argument** and **all
load-bearing inputs** passed independent adversarial review." `CERTIFIED*` = "An independently
reviewed **conditional** result with **explicit unresolved premises or scope caveats**." I adopt the
wave-11/wave-16 rule that *an exclusion is not a caveat*: material outside the claim does not force
`CERTIFIED*`; a condition the claim **as written** needs and does not have, does.

---

## 3. Task 1 — drift check, both proposed claims

I did this **mechanically**, not by eye: I loaded each current claim through the validated pipeline,
applied only the prescribed edits programmatically, and compared to the proposed string.

### 3.1 Claim 1 — `CIRCDIST.lift.iff`. **PASS, exact.**

Test: take the current claim, apply insertion **A** by replacing `fixed boundaries, d_circ equals` →
`fixed boundaries, for memory experiments C_R(M) with R >= d, d_circ equals`, then insertion **B**
by replacing `characterizing same-weight liftability —` → `characterizing same-weight liftability at
minimum weight —`. Both anchors found and unique. Result, whitespace-normalized, is **identical** to
the proposed string. No third edit, no reordering, no punctuation drift. Insertion placement matches
adjudication §6 word for word (`at minimum weight` qualifies the liftability clause, per Amendment 2
L1/L3 and the node's existing caveat 2).

**Exact string hashed** (single line, U+2014 em dash, terminal period, no trailing whitespace):

> In graph-like detector error models with fixed boundaries, for memory experiments C_R(M) with R >= d, d_circ equals the minimum over nontrivial effective logicals gamma of the length of the shortest closed spacetime lift of gamma, with an intrinsic zero-voltage/monodromy condition characterizing same-weight liftability at minimum weight — and the voltage is computable without constructing the full multi-round circuit (non-vacuity bar).

**New hash:** `sha256:2c8fe9e3a670367c1c321149d76ae33f0df05fefe101c74c6b0f76406ace8926` (439 chars).

### 3.2 Claim 2 — `CIRCDIST.lift`. **PASS mechanically; TWO semantic findings.**

Test: delete the dash-clause ` — graph-like read per-sector (iff Def 1.12) and quantified over
memory experiments C_R(M) with R >= d rounds —` and restore the comma. Result is **identical** to
the current root claim. So the only textual change is the folded clause. ✓

Fidelity of the clause to the two `BINDING` caveats it replaces:

* Caveat 1 → "graph-like read per-sector (iff Def 1.12)". **Faithful.** It drops only the
  justification rider ("under the whole-DEM reading the existential clause fails"), which is a
  reason, not a condition.
* Caveat 2 → "quantified over memory experiments C_R(M) with R >= d rounds". **Faithful to the
  wording** (the caveat reads "the claim as certified is quantified over memory experiments with
  R >= d rounds").

**Finding S1 — the minimum-weight qualifier is absent at the root (blocking).** Claim 1 now
*acquires* "at minimum weight" on the equal-weight-liftability clause. The root's corresponding
clause — "with zero time-direction voltage/monodromy as the equal-weight liftability condition" —
carries **no** such qualifier and no caveat naming one (root caveat 3 names only `repair >= 3`, the
min-cost-covering extension, and the large scans). After the repair the root therefore asserts,
unrestrictedly, exactly what its sole supporting premise now restricts to minimum weight. This is
the same species of defect wave-16 used to block the child: *the claim as written is strictly
broader than what is argued*. It is not cured by the approved two-caveat fold, because insertion B
has no counterpart at the root. Under §3 this is an explicit scope caveat on its own.

**Finding S2 — the `R >= d` restriction is scoped wider than the caveat scopes it (non-blocking).**
Caveat 2 attaches the hypothesis to **the criterion clause** ("*the criterion clause* carries
Theorem 5.7's `R >= d` hypothesis"). The folded clause sits at the head of the sentence and so
scopes over all three clauses, including "recovers the non-interleaved equality … as a corollary"
and "is accompanied by an explicit interleaved example". Both of those premises are `PROVED`
**without** an `R` restriction — `CIRCDIST.lift.nonint`'s Theorem 7.1 concludes "for all `R >= 1`"
(adjudication §6 notes this asymmetry is real). The fold therefore silently *weakens* two clauses
below what is proved. It cannot make the root false, so I do not block on it, but it is not the
faithful capture the commission specifies. Recommended: attach the `R` clause to the criterion
clause, or record the deliberate weakening in the fold event.

**Exact string hashed** (single line, two U+2014 em dashes, straight double quotes around the
inner shape, terminal period):

> In graph-like detector error models with fixed boundaries — graph-like read per-sector (iff Def 1.12) and quantified over memory experiments C_R(M) with R >= d rounds — a proven necessary-and-sufficient structural criterion (in graph-covering, voltage-graph, or chain-complex form) characterizes when d_circ = d_eff, of the shape "d_circ equals the minimum over nontrivial effective logicals gamma of the length of the shortest closed spacetime lift of gamma", with zero time-direction voltage/monodromy as the equal-weight liftability condition; the criterion recovers the non-interleaved equality d_circ = d_eff as a corollary and is accompanied by an explicit interleaved example with d_circ > d_eff.

**New hash:** `sha256:bd1aa84ed25a14c4f0c731d7a8359b1ed14dce6f385223beadabb2f8d7b03b4c`.

---

## 4. Task 2 — closing the 5.10(2) coverage hole

### 4.1 The statement under review

> **5.10(2).** "`d_circ` is computable from the one-round data `{(E(f), s(f), u(f), λ(f)) : f ∈ 𝔽}`
> alone, by a search over fault multisets of size `≤ d` distributed over `≤ d` consecutive rounds.
> No multi-round circuit is constructed at any point."
> *Derivation:* "5.9 plus (LIFT'): membership in `ker ∂` is decided by the one-round data and the
> round assignment." *Status:* "(1) and (2) complete." Amendment 1 §2.6 records it **unchanged**.

Wave-16 §8 is right that this sentence has no verdict anywhere: base review verdict **I** covers
5.10(**1**), its §5 item 4 covers 5.10(**3**), and the amendments2 review's scope is L1–L3 plus the
assembled dossier. I state a verdict.

### 4.2 Re-derivation (mechanism)

I reconstructed the argument from the document's own definitions.

*Soundness.* Any `F ⊆ 𝔽 × {0,…,K−1}` satisfying (LIFT') `U_b(r) = c_b(r−1)` for all `b,r` and
`λ(F) ≠ 0` is a genuine undetectable logical of `C_R(M)` for `R ≥ K`: (LIFT') ⟺ `∂F = 0` is 4.3, and
the finite-`R` detector set is the full interval `ℬ × {0,…,R}` with no truncation, which is 4.1
(ideal boundaries, both ends). `λ` is additive over `F` because `λ(f) = |E(f) ∩ supp(Z_L)| mod 2` is
`F₂`-linear in `E(f)` and the observable is a functional of `Σ_f E(f)` — the identity of linear maps
`λ_circ = λ_eff ∘ π_1` (5.4(1), base review §4.3 item 1 "Correct"). ✓

*Completeness.* A minimum-weight undetectable logical `F` of `C_R(M)` occupies a contiguous round
interval of span `≤ |F|` (5.9); the bulk is time-translation invariant with both temporal boundaries
fully detectored (4.1), so `F` translates to start at round 0 without changing weight, landing
inside the window. ✓

*5.9 itself.* I re-derived the split argument and it is correct: at an idle round `r`, (LIFT') gives
`U_b(r) = 0 = c_b(r−1)`; then for `r' ≤ r` the later half contributes nothing to `U(r')` or
`c(r'−1)`, and for `r' > r` the earlier half has `U = 0` and `c(r'−1) = c(r−1) = 0`; so both halves
are separately undetectable, both non-empty, and `λ(F) = λ(F_1) + λ(F_2) ≠ 0` puts a logical in one
of them at strictly smaller weight. Contiguity ⟹ `#rounds ≤ #faults`. ✓ (Independently CONFIRMED
before, base review verdict **H**, 203 186/203 186.)

**The mechanism is sound and I confirm it.** One-round `(E,s,u,λ)` plus a round assignment decides
both membership in `ker ∂` and the observable; no multi-round circuit is built. The finiteness of
the `repair(γ) = 0` zero-test (adjudication §5 item 3) is likewise fine — there the bound used is
span `≤ |γ|`, which is known.

### 4.3 **DEFECT — the stated bound is the wrong constant, and it is false per sector**

5.10(2) fixes the search size **and** the window at the **code distance `d`**. That constant comes
from the trailing chain of 5.9, "round-span(`F`) `≤ |F| = d_circ ≤ d`", and from 5.10(1)/(1′),
"`d_R` … constant for all `R ≥ d`" — which Amendment 1 §3 restates explicitly **"per sector"**, and
whose ceiling Amendment 2 §3 sources to the 公共定义: *"The 公共定义 gives `d_R(M) <= d` for every
`R`"*.

The 公共定义's inequality is `d_eff(M) <= d_circ(C(M)) <= d`, written for the **circuit** `C(M)`.
Definition 1.5 of the proof document defines `d_circ(C)` as the **min over the two memory sectors**.
But all of §5 is per-sector ("All statements below are for the Z-memory"). Per sector the only
available bound is `d_circ^{Z-mem} ≤ d_X`, and `d = min(d_X, d_Z)`. **For a CSS code with
`d_Z < d_X` the transposition fails.**

I built such an instance and measured it (§4.5): `n = 6`, X-checks `{0,1},{2,3},{4,5}`, Z-checks
`{0,1,2,3},{2,3,4,5}`, `k = 1`; `d_X = 3`, `d_Z = 2`, so `d = 2`. Non-interleaved list-scheduled
single-ancilla CSS circuit (hence legal and (MC)-automatic), ideal boundaries. **This instance is
`graph-like` in the Z-memory sector (Def 1.12 verified on all 91 elementary faults, 0 violations),
so it lies inside the repaired claim's own scope.** Measured, by direct multi-round simulation:

```
  d_eff = 3 ;  d_circ(Z-memory) = 3  at R = 1,2,3,4     while  d = 2
  5.10(2) as stated, W = d = 2      ->  returns NOTHING     <-- defect
  5.10(2) with W = d_X = 3          ->  returns 3           <-- correct
```

Both halves of the stated bound fail: the **size** bound `≤ d = 2` excludes every witness, and the
**window** `≤ d = 2` rounds excludes the 1 224 of 27 562 minimum-weight witnesses whose span is 3.
Contiguity itself is untouched — all 27 562 are contiguous with span `≤ weight = 3`, a third
independent corroboration of 5.9's actual content.

**Scope of the defect.** It is a defect in the *constant*, not the *mechanism*. Three repairs each
close it and none needs new mathematics: (i) replace `d` by the sector's own `d_X` (computable from
the code alone, so the non-vacuity bar survives intact); (ii) state the bound as `≤ W` for any known
upper bound `W ≥ d_circ`; (iii) best — run the search at increasing `w = 1,2,3,…` with window `w`
and stop at the first hit, which needs no a-priori bound and terminates at `w = d_circ`.

**The claim is not refuted by this.** On the same witness, conjunct 1 holds: `d_circ = 3 =
min_γ ℓ(γ)` (non-interleaved ⟹ `repair ≡ 0` by 5.11, so `ℓ(γ) = |γ| = 3`).

**Propagation (recorded, not adjudicated).** The same unjustified per-sector ceiling is the stated
support for `R >= d` — `amendments4` §2.2 traces C-M7 to "§5.10(1) / Amendment 1 §253". So for
asymmetric codes the sub-regime `d ≤ R < d_circ` is inside the repaired claim's quantifier but
outside what the document's argument reaches. I did **not** find an instance where the claim fails
there (on my witness, `d_R = 3` for every `R ≥ 1`). Separately, Amendment 2's L2 branch `R_sat = 1`
invokes the same ceiling per sector; whether L2 survives per-sector for asymmetric codes is a
question for the `sat` family and I do not adjudicate it — I flag it only because L2 was
CLEAN-PASSED on a derivation that uses this step.

### 4.4 **VERDICT on Theorem 5.10(2): CONFIRM-WITH-REQUIRED-REPAIR**

The repair-free one-round decision procedure for `d_circ` is **correct in mechanism and correctly
derived from 5.9 + (LIFT') + 4.1**, and I reproduce it computationally. Its **stated search bound is
false per sector** for asymmetric CSS codes and must be re-stated. Not refuted; not clean.

### 4.5 Independent computation

Code written this session from the model definitions only; direct simulator (F₂ frames, CNOT
`x` control→target, ancilla reset, detectors `D_{b,r} = m_{b,r} + m_{b,r−1}`, `m_{b,−1} = 0`,
`m_{b,R}` = ideal readout parity) with **no** use of (LIFT'), one-round data, or any repair/voltage
notion; the 5.10(2) procedure implemented separately from one-round `(E,s,u,λ)` and (LIFT') only.

**Corroboration on a campaign instance** — Steane `[[7,1,3]]`, `M_IL` exactly as printed in
`circdist_lift_d3gate_20260820.md` §5.2 (legality of the printed slot table re-verified), and my own
list-scheduled non-interleaved partner:

```
  Steane M_IL (interleaved, depth 8) :  direct brute force  R=2,3,4  -> d_circ = 3
                                        5.10(2), window W=3          -> d_circ = 3
  Steane M_NI (non-interleaved,  11) :  direct brute force  R=2,3,4  -> d_circ = 2
                                        5.10(2), window W=2,3,4      -> d_circ = 2
```

These reproduce the d3-gate's `(3,3,3,3)` / `(2,2,2,2)` table and iff §9.4 under an independently
written detector layer and an independently written propagator. The one-round procedure agrees with
the multi-round ground truth in every cell. (Note: Steane's Z-memory sector is **not** graph-like —
26/144 faults violate Def 1.12 — exactly as the document's §1.12 scope note says; this is a
corroboration of the procedure, not of the claim's restricted scope.)

Asymmetric witness as in §4.3. Files:
`…/scratchpad/lift510.py`, `run_steane.py`, `run_asym.py`.

### 4.6 Wave-16 §8 sweep — citation audit (5 rows, ≥ 3 required)

| row | claimed citation | verified |
|---|---|---|
| 5.9 contiguity | base review verdict **H** CONFIRM [V][D][N], re-derived pre-reading; 203 186/203 186 | ✓ exact — verdict table row H; §4.4 "I derived the same argument before reading"; "**Measured: 203 186 / 203 186**" |
| model fact (V) | base review §4.2 — structural derivation from the frozen fault menu **plus** 440/440 | ✓ exact — §4.2 "**440 / 440** distinct empty-residual voltage vectors … weight `≤ 1`", with the two-Z-ancillas structural reason |
| residual inventory 1.13 | base review §4.2 — 1 994/1 994 realised classes, partition exhaustive | ✓ exact — §4.2, "over 180 legal (MC) schedules on three codes, **1 994 / 1 994**" |
| 5.4(1) `λ_circ = λ_eff ∘ π_1` | base review §4.3 item 1 — "Correct"; answers the litverify2 systole hazard | ✓ exact — §4.3 item 1 ends "Correct", and says "This is the step that answers the systolic-non-monotonicity warning" |
| 5.7 the biconditional | base review verdict **G** CONFIRM [D][N]; 282/282 | ✓ — verdict G is CONFIRM [D][N] **"survives F, but the printed (⟸) needs the one-line repair in §3.2"**; §4.3 measures 282/282. The repair is applied in Amendment 1 §2.7 and re-reviewed, as the adjudication states |

The §8 table's review citations exist as described. **One correction to it:** the base review's
verdict **H** is printed as covering "*span ≤ weight ≤ d*" — i.e. it nominally CONFIRMs the very
clause I refute in §4.3. Its §4.4 scope paragraph and its measurement cover only contiguity and
span ≤ weight, and its 282 instances are Steane / rotated surface / `[[4,2,2]]`, all with
`d_X = d_Z`. The "`≤ d`" tail rode along in the verdict statement and was never attacked. That is
why the defect survived to this session, and it is a caution about reading verdict statements as
if every conjunct had been probed.

---

## 5. Task 3 — verdict on repaired claim 1 (`CIRCDIST.lift.iff`)

What the repair **does** fix, and I confirm:

1. `R >= d` is now **in the claim text** — the F2/C-M7 finding that decided wave 16 is discharged as
   a *registration* matter.
2. `at minimum weight` is now in the text, so the all-`γ` reading of conjunct 2 (which Amendment 1
   §2.6 only establishes at minimum weight, via 5.3′ branch (a) / Amendment 2 L1) is no longer
   asserted.
3. Model fact **(V)** is registered in the node's `assumptions` block with its establishing evidence
   and is **established, not assumed** (base review §4.2: structural + 440/440). ✓
4. `repair >= 3` and 5.6(d) are genuine **exclusions outside the claim**. I re-checked the
   adjudication's load-bearing steps at source rather than carrying them: 5.7's (⟹) status line does
   say "*this direction needs no hypothesis on `repair`*"; (⟸) invokes only 5.4(4)
   `|F| ≥ |γ| + min(repair,2)`, which Amendment 1 §2.6 records as surviving verbatim; and the half
   that fails for `repair ≥ 3` is the **upper** bound, which no conjunct uses beyond `repair = 0`. ✓
5. The 5.10(2) coverage hole now has a reviewer verdict (§4.4). ✓

What blocks `PROVED`:

* **(B1) The one load-bearing input I was sent to close did not clean-pass.** 5.10(2) carries a
  required repair (§4.3). The repository's own precedent is explicit — after the base review's
  GAP-AT-5.3, the node stayed `NUMERICAL` until Amendment 1 applied the repair ("SE precedent:
  repair before promotion"). A verdict of CONFIRM-WITH-REQUIRED-REPAIR on an unrepaired document is
  not "passed independent adversarial review" in §3's sense.
* **(B2) The repaired claim's own quantifier outruns the argument.** The claim now says "for memory
  experiments `C_R(M)` with `R >= d`". The justification that `R >= d` suffices is
  span `≤ |F| = d_circ ≤ d`, whose last inequality I refute per sector on a **graph-like** instance
  inside the claim's scope. For asymmetric CSS codes the band `d ≤ R < d_circ` is asserted and not
  argued. Note this defect is *created by the repair*: the pre-repair claim had no `R` quantifier.
  A one-word fix (`R >= d_X`, or "for `R` large enough") removes it.
* **(B3) A new ambiguity.** The claim uses the bare symbol `d` with no definition. Under the
  document's Def 1.1 it is the code distance `min(d_X,d_Z)`; a per-sector reading would make it
  `d_X`. Only the second reading is supported. The claim should say which.

### **VERDICT: `CERTIFIED*`. I do not license `PROVED`.**

Bound to `sha256:2c8fe9e3a670367c1c321149d76ae33f0df05fefe101c74c6b0f76406ace8926` (string in §3.1).

The repair is **faithful and worth applying** — it strictly improves the node and discharges the
wave-16 blocker. It simply does not reach `PROVED`, and it fails for a reason wave 16 could not have
seen, because closing the 5.10(2) hole is what exposed it.

**Caveat set that should survive on the repaired node:**

1. **NEW, BINDING:** the `R >= d` hypothesis in the claim rests on the per-sector reading of
   `d_circ ≤ d`, which is **false** for CSS codes with `d_Z < d_X` (witness: `n=6`, `d_X=3`,
   `d_Z=2`, graph-like, `d_circ(Z-mem) = 3 > d = 2`; this review §4.3). Established only for
   `R >= d_circ`; `d_X` is a sound and one-round-computable substitute.
2. **NEW:** Theorem 5.10(2)'s stated search bound ("size `≤ d` over `≤ d` consecutive rounds")
   requires the same repair; the decision procedure's mechanism is confirmed (this review §4.2, §4.4).
3. **KEEP:** `EXCLUSION` — the general lift-length formula for `repair >= 3` and its
   min-cost-covering replacement lie outside this claim (adjudication §7.2 text, which I endorse).
4. **KEEP:** certification is for the exact claim and the reviewed minimum-weight repair-0/closed-lift
   criterion, not for stronger formulas named as future work.
5. **KEEP:** the large proposer scans (98 811 schedules, 3 855/3 855, 321 059/321 059) were never
   independently reproduced. I reproduced neither; my own runs are small and are listed in §4.5.
6. **KEEP:** 5.6(d) is unreviewed and is **not** a premise of this claim.
7. **KEEP:** model fact (V) registered in `assumptions`, established.
8. **KEEP:** per-sector scope — everything is stated for one memory sector. (§4.3 shows this caveat
   is doing more work than the record assumed.)

---

## 6. Task 4 — verdict on the root with claim 2 installed

Inputs, as commissioned and as I verified them: `nonint` = `PROVED`, hash-bound `e2d1b292…` ✓;
`gap-example` = `PROVED`, hash-bound `e080155d…` ✓; route implication review `f39c83e6…` hash-valid
and untouched ✓; `iff` = `CERTIFIED*` per §5.

Three independently sufficient grounds against `PROVED`:

* **(R1) The route premise is conditional.** `criterion-corollary-example` requires `CIRCDIST.lift.iff`,
  which §5 licenses at `CERTIFIED*`. `DAG_PROTOCOL` §2: "A level never propagates automatically
  across a route"; §3 requires *all* load-bearing inputs to have passed review. A premise at a
  conditional level is not a premise that passed for `PROVED`.
* **(R2) Finding S1 (§3.2).** The root's equal-weight-liftability clause carries no minimum-weight
  qualifier while its only supporting premise now does. The root claim as written is strictly
  broader than what is argued — a scope caveat under §3, independent of (R1).
* **(R3) The assembly review chain does not cover the folded claim.** `amendments4` is bound to
  `ccad7fa6…`; the fold moves the node claim to `bd1aa84e…`, and §5 is explicit that "a completion
  assessment becomes invalid if that statement later changes". No review has read the folded string
  except this one, and this one does not clear it.

### **VERDICT: `CERTIFIED*`. I do not license `PROVED`.**

Bound to `sha256:bd1aa84ed25a14c4f0c731d7a8359b1ed14dce6f385223beadabb2f8d7b03b4c` (string in §3.2).

The fold is nonetheless **worth applying**: it converts the root's own contribution from
"claim-as-written broader than certified" to "claim-as-written restricted", which was the whole
point of the lead's approval, and it removes two `BINDING` caveats from the assessment.

**Caveat set that should survive on the folded root:**

1. **BINDING, NEW (S1):** the equal-weight-liftability clause is licensed only at **minimum weight**
   (premise `CIRCDIST.lift.iff` after insertion B); the root text does not carry the qualifier.
2. **NEW (S2):** the folded `R >= d` clause scopes over all three clauses, while caveat C-M7 scoped
   it to the criterion clause; the corollary and example clauses are thereby stated more narrowly
   than their `PROVED` premises support. Weakening only — recorded, not blocking.
3. **NEW, inherited from the child:** `R >= d` itself is the wrong constant per sector (§4.3);
   `R >= d_X` is what is argued.
4. **KEEP:** `repair >= 3`, the min-cost-covering extension, and the large proposer scans remain
   excluded, per the children's certifications.
5. **KEEP:** under the min-over-sectors convention the `[[4,2,2]]` witness is the **sole**
   load-bearing example for the existential clause (Steane witnesses a single sector only).
6. **KEEP (implicit until now, now explicit):** the root level remains governed by
   `CIRCDIST.lift.iff`.

The two folded conditions themselves I confirm as correctly captured at the level of wording
(§3.2), and the per-sector pin is now doing real work: §4.3's defect is precisely a per-sector/
whole-circuit confusion, so the fold's own "read per-sector" clause is well judged.

---

## 7. Task 5 — review links to demote, and the one that stands

**Demote to `basis.evidence` (`kind: text`) — bound to hashes the repairs invalidate:**

1. **`CIRCDIST.lift.iff`**, `assessment.basis.reviews[0]`:
   `artifacts/circdist_amendments2_review_20260820.md`, `reviewed_hash:
   sha256:c3a84198…480f0061`. The claim moves to `2c8fe9e3…`; `DAG_PROTOCOL` §5 invalidates the
   completion assessment. Its mathematical findings (L1–L3 CLEAN-PASS, §7.1's exclusions) remain
   fully citable as evidence, and its §7.1 boundary sentence is the source the adjudication relies
   on for the `repair >= 3` exclusion.
2. **`CIRCDIST.lift`**, `assessment.basis.reviews[0]`:
   `artifacts/circdist_amendments4_review_20260822.md`, `reviewed_hash:
   sha256:ccad7fa6…40e78d8a`. The node claim moves to `bd1aa84e…`; same rule. Note the same file is
   linked twice with two different hashes — only the node-level link is demoted.

Neither demotion is a retraction of the review; it is the protocol's hash discipline, and it is
exactly the situation `amendments4` §2.2 anticipated ("a claim edit moves `ccad7fa6…` and lapses any
review bound to it").

**Remains valid — do not touch:**

3. **`CIRCDIST.lift`**, `routes.criterion-corollary-example.assessment.basis.reviews[0]`:
   `artifacts/circdist_amendments4_review_20260822.md`, `reviewed_hash: sha256:f39c83e6…fdfdfca8eda`.
   I recomputed the route implication digest from the current file and it reproduces `f39c83e6…`
   exactly. The implication text is byte-identical and **untouched by both repairs**; the link stays
   under `basis.reviews`. ✓

   **But an audit note, since §5 says adequacy "remains an audit question, not a filename check":**
   the implication asserts that "the claim is the conjunction of its three components". After the
   repairs that sentence has more work to do than when it was reviewed — the root's clause is now
   *stronger* than child conjunct 2 (S1), and the root's `R >= d` is *stronger* than what `nonint`
   needs (S2). The hash binding is intact; the mathematical adequacy of the implication under the
   new premise/claim pair has not been reviewed by anyone, including me. A route-level re-review is
   the cheapest way to close S1/S2 if the lead wants the root's own contribution complete.

**Also worth registering (not a demotion):** the iff node's `basis.evidence` entry for
`circdist_lift_proofs_review_20260820.md` should stay evidence-only, per adjudication §9, and this
review takes option (i) of §9 explicitly — **the base review's verdicts A–P are the source of the
underlying mathematics I rely on in §4**, except verdict H's "`≤ d`" tail, which I refute.

---

## 8. Limitations — what I did not do

1. **I did not re-derive Theorems 1, 5.3′, 5.4, 5.6, or 5.7.** For those I rely on the base review
   and the amendments reviews, cited row by row in §4.6. My own derivation work is confined to 5.9,
   5.10(2), 4.1/4.3, 1.9, 1.13 and the algebra they need.
2. **I did not reproduce any large proposer scan** — 98 811 schedules, 3 855/3 855, 349/349,
   321 059/321 059 all remain NOT-REVIEWED as such.
3. **My asymmetric witness is one code with one schedule.** I did not survey how common
   `d_Z < d_X` is in the campaign's intended target class, and every instance in the record
   (`[[4,2,2]]`, Steane, rotated surface, gross `[[144,12,12]]`) has `d_X = d_Z`, so the defect is
   **vacuous on everything the campaign has actually computed**. I claim it bites the *statements*,
   not the *numbers*.
4. **I did not exhibit a failure of `R >= d`.** On my witness `d_R = 3` for every `R ≥ 1`, so the
   band `d ≤ R < d_circ` is non-empty but harmless there. B2 is a gap in the argument's coverage, not
   a refutation. If a future session proves 5.7 for all `R ≥ 1`, or restates the constant as `d_X`,
   B2 and root caveat 3 both vanish.
5. **I did not adjudicate the `sat` family**, though §4.3's propagation note touches Amendment 2's
   L2 branch `R_sat = 1`.
6. **I did not attack the frozen 公共定义.** I read its `d_circ(C(M)) ≤ d` as a whole-circuit
   statement, which is how it is written and which my measurements confirm; the defect is in
   transposing it per sector, downstream.
7. **I did not verify graph-likeness for the Steane instances beyond Def 1.12 as written**, and I
   note my Steane runs are outside the claim's graph-like restriction (the document says so too).
   The asymmetric witness, which carries the finding, **is** graph-like and is inside it.
8. **This review is itself unreviewed.** It licenses two `CERTIFIED*` levels and no promotion.
