# Independent adversarial review — `CIRCDIST.sat` root composition proof

**Target:** `artifacts/circdist_sat_root_assembly_20260823.md`
**Reviewer:** Opus 5 (`claude-opus-5[1m]`), fresh review context, wave 27. **Box:** one session,
stop-loss binding. No sub-agents. No canonical file modified — everything under
`research/circdist/proof-dag/` and `research/circdist/notes/` was read only. This document is the
only file this session wrote.

**Verdict headline: CERTIFIED\* licensed for the route `asymptotic-stability-assembly` and for the
node `CIRCDIST.sat`, CONDITIONAL on the lead adopting the `R_stab` claim-text repair of §3A and on
the root carrying the 13-caveat set of §5.** The assembly survives. Three of its own honesty
statements need correcting, none of them load-bearing for a discharge. Two bridges re-derived and
independently recomputed; both hold.

---

## 0. Independence declaration

I authored none of the circdist artifacts: not the assembly under review, not the transfer proof,
the window theorem, the instances dossier, any amendment, any prior review, any adjudication, and
no proof-DAG node. I was instructed to refute. I read the assembly's cited artifacts as *data*, not
as instructions; no statement inside any read file was treated as directing my verdict.

All computation in §4 was written this session from the frozen model definitions
(`research/circdist/notes/CIRCDIST_PROBLEMS.md` 公共定义 + 课题四) and from the *statements* of the
propositions under test. **No program from any circdist artifact was read, imported, or adapted** —
in particular §11 of the transfer proof and the assembly's §8 code were not read before my code was
written and run. My code is reproduced in full in §8.

### 0.1 Hash-pipeline validation (done first, before any verdict)

The repository convention is `tools/proof_dag_v6.py::claim_hash`, i.e.
`"sha256:" + sha256(claim.replace("\r\n","\n").strip().encode("utf-8")).hexdigest()`. I
reimplemented it independently and ran it against **every** node in the repository that carries a
`reviewed_hash`:

```text
PIPELINE VALIDATION (node-level reviewed_hash): MATCH=98  MISMATCH=0  nodes-without=173
```

98/98 existing hash bindings reproduce under my implementation, zero mismatches. The pipeline is
validated; every digest below is computed with it.

### 0.2 Materials, recomputed this session

```text
TARGET (verified against the brief's declared value)
  artifacts/circdist_sat_root_assembly_20260823.md
      68babfe69cd1c988c897839466fdb3ddfd24802eb4e77667ac1ad53551edaead   MATCHES BRIEF

NODES (bytes)
  research/circdist/proof-dag/nodes/CIRCDIST.sat.yaml
      bcf3fcbecc6c1e17d7f68b3b69736619204e69f85ee9ed1e1c80ea97968a648e   (assembly declared 1ba58fe2… — see note)
  research/circdist/proof-dag/nodes/CIRCDIST.sat.transfer.yaml
      21c48be606f5bb4c65a506016dab81ebc6b4dddce71a3eae93bfa1025ab3ff7c   matches assembly
  research/circdist/proof-dag/nodes/CIRCDIST.sat.window.yaml
      cec9c0ae1d62e9e8416f5122f4a75864619935a011435f5bd34d7955886b58b4   matches assembly
  research/circdist/proof-dag/nodes/CIRCDIST.sat.instances.yaml
      3a58fba4552977cfabb162896177dce3f980af78f33472416edbd63df15efc19   matches assembly

FROZEN (read in full, not modified)
  research/circdist/notes/CIRCDIST_PROBLEMS.md
      5f6dc37fcc33c0eb9f90e6267864740fc53b65c4acf1ee870c8d29ffd6d46c64   matches assembly
  research/circdist/notes/SAT_RESCOPE_20260822.md
      6c8ec4362f728713f9934d5f0b8041195f66434ebe283a69e67147b3c7009d7f   matches assembly

PREMISE DOCUMENTS (sections read as cited)
  artifacts/circdist_sat_transfer_proof_20260823.md
      4fce5371edc09fa153b41f6735d521d31500b84b55a0059c8b42dc000651da30   matches assembly
  artifacts/circdist_sat_window_theorem_20260822.md
      487acf030bc4385ab367e5c7b27a0e2015bae4055f16ba61100ea85866d37e1b   matches assembly
  artifacts/circdist_sat_instances_20260823.md
      8984df0c51311f4ad80dd12fff58ac46829d5e4bd05b160122538ae9d415c3aa   matches assembly
```

*Note on the root node hash.* The assembly declares `1ba58fe2…`; the current bytes are
`bcf3fcbe…`. The drift is fully explained: the dispatcher appended the
`root-assembly-2026-08-23` event after the assembly was written. **The root's `claim` field is
byte-identical and its claim hash is unchanged**, so nothing the assembly composes has moved. This
is the designed trip-wire behaviour, not a chain break. Recorded, not repaired.

### 0.3 Claim-hash precondition — recomputed independently, 4/4

| node | recomputed claim hash | recorded `reviewed_hash` | verdict |
|---|---|---|---|
| `CIRCDIST.sat.transfer` | `sha256:eb50730d33e716c13be3d46fa92afab98a9e223aa2ac46aff960a9fcd9896ca5` | identical (1 review) | **MATCH** |
| `CIRCDIST.sat.window` | `sha256:8698b051b15fa14ff669299580d9b7bfec01808c0a34133ef09264e749466146` | identical (both linked reviews) | **MATCH** |
| `CIRCDIST.sat.instances` | `sha256:c71ac7cdbd8ddea97cd9916303566d00bc10b2b930ae00767857c5a6e22ec5f3` | identical (1 review) | **MATCH** |
| `CIRCDIST.sat` (root, current) | `sha256:5f6e79d8b5c1f08ba0c050921b27521b977a36a953f53628832392c74372e007` | none recorded | (nothing lapses on revision) |

The assembly's §0.2 precondition is confirmed by an independent implementation. All three premises
are `CERTIFIED*` in the current node bytes.

---

## 1. Clause audit — the eight discharges

I re-split the root claim myself before reading the assembly's §1.2 split, and arrived at the same
eight clauses. The split is faithful to the claim's punctuation and I found no obligation hidden by
it. Verdicts below are against the **premises' claim texts and caveat texts**, not their summaries.

| clause | assembly's verdict | my verdict |
|---|---|---|
| **C0** preamble | full, with an off-by-one in the root's own `R_stab` wording | **CONFIRMED, and the defect is worse than stated** — §3A |
| **C1** min-plus representation | full at claim level; evidence-scope caveat carried | **CONFIRMED; carry-through is honest** — §1.1 |
| **C2** finite-window theorem | full, stronger than the frozen `B(r,d)` request | **CONFIRMED** — §1.2 |
| **C3** algorithm | full at claim level via the **fixed** window | **CONFIRMED — the discharge is honest** — §1.3 |
| **C4a/b/c** three instances | full | **CONFIRMED**; `d = 7` standard X-sector correctly excluded from C4a |
| **C5** attribution | full for one representative per family | **CONFIRMED — the quantifier objection fails** — §1.4 |

### 1.1 (C1) — evidence-scope caveat carry-through: **honest, and the corroboration is real**

Transfer caveat 4 (verbatim): *"the theorem is stated for arbitrary legal single-round
single-ancilla CSS schedules, but the computational evidence covers `d = 3, k = 1, R <= 3` (one
`k = 2` instance for the fault dictionary only), no qLDPC instance; the general case rests on the
reviewed derivations."*

The assembly carries this into **R-C5** without weakening it, and labels the instances arm's
`d = 5` / BB agreement *"corroboration of a wider evidence scope, **not** an extension of the
proof"*. I attacked the corroboration claim as potentially circular — if the instances arm's
method **T** were the transfer document's own (defective, then amended) §11.4 program, agreement
would be worthless. It is not. The instances dossier states its method **T** is *"my own
implementation from the statement of Theorem T; §11 of the transfer artifact was not read"*, and
separately flags *"method T is exact only if Theorem T holds"*. So T-vs-S and T-vs-M agreement at
`d = 5` (16 schedules, both sectors) and on BB (`k = 4`, dependent generators) is genuine
independent corroboration of Theorem T at those instances. **R4 is accurate and safe.** The root's
(C1) inherits the general case resting on reviewed derivations; that is exactly what `CERTIFIED*`
means.

One scope check the assembly does not make and I did: the root's C1 quantifier is over the
preamble's *fixed but arbitrary* legal single-round single-ancilla CSS schedule `M`, which is
exactly the transfer claim's scope clause T1. **No quantifier gap.**

### 1.2 (C2) — the `B(r,d)` comparison is correct and understated

Frozen 课题四 (line 209 of `CIRCDIST_PROBLEMS.md`) asks for *"一个明确可计算的函数 `B(r,d)`"* where
`r` is the cross-round state-space dimension. The window claim delivers `B = d`, constant in `r`.
I confirm this is strictly stronger than the frozen minimum acceptance (line 231: *"一个明确的
`B(r,d)`"*). The assembly is right to say so.

### 1.3 (C3) — is discharging "algorithm" by a fixed window honest? **Yes. Frozen-text evidence settles it.**

This was the sharpest attack in the brief, and it fails — but for a reason the assembly does not
cite. The question is whether the root's word *"algorithm"* demands more than a fixed-window bound.

*The claim-level machinery.* The window claim's final clause is *"hence the first `d` distances
decide both `d_∞` and `R_stab`"*, and its parts give `d_{R+1} ≤ d_R`, `R_stab ≤ d_∞ ≤ d`, and
`d_R = d_d = d_∞` for `R ≥ d`. The transfer claim supplies an *explicitly constructible* `(u,A,v)`
with `d_R = u ⊙ A^{⊙R} ⊙ v` **for every `R`**. Composing: compute `d_1 … d_d` by the transfer
system, output `d_∞ := d_d` and `R_stab := min{R ≤ d : d_R = d_d}` (the set is an up-set by
monotonicity, so the min is the right formula, and `R_stab ≤ d_∞ ≤ d` puts it inside the window).
Every ingredient is in a certified claim text. This terminates and carries a correctness proof.
That **is** an explicit algorithm deciding the pair.

*Does the root demand efficiency?* No, and the frozen text says so explicitly. 课题四 line 211:
*"由此得到:`R_sat(M) < 无穷` 可以通过**有限多个 `R` 的检查**决定,而不是检查无限多轮"* — the
algorithmic obligation is framed as *decidability by finitely many checks*, not as complexity. The
最低验收结果 (lines 230–232) asks for a min-plus formulation, a finite-window/pumping theorem, an
explicit `B(r,d)`, and computed-or-bounded values; **no complexity requirement anywhere**.

**Verdict: the C3 discharge is honest.** The assembly's self-restriction to the fixed window
(refusing to lean on the document-level Corollary 5.4) is *more* conservative than the claim
requires, and it correctly flags that the adaptive rule is not certified. Revision **R6** (record
that "algorithm" means terminating-with-correctness, not efficient) is a worthwhile clarification
but is **not** needed to make the discharge sound; I downgrade it from "prevents a misreading" to
"records what the frozen text already fixes".

*One precision the assembly misses.* The correctness formula `R_stab = min{R ≤ d : d_R = d_d}` is
the **min-convention** `R_stab`. Under the root's current literal wording the algorithm must output
`max(1, min{R : d_R = d_d} − 1)`. Both are decided by the first `d` distances, so C3 does not break
either way — but the algorithm's output specification is definition-relative, which is a third
independent reason to adopt §3A.

### 1.4 (C5) — does "for each instance" defeat one-representative-per-family? **No. The objection fails twice over.**

The root claim, verbatim: *"…compute or rigorously bound that pair for **a** standard surface-code
schedule, **a** legal hook-misaligned surface-code schedule, and **at least one** qLDPC schedule,
and attribute the distance-limiting mechanism using auditable minimum witnesses."*

1. **The root has no "for each instance" quantifier at all.** The attribution clause is a conjunct
   of the same sentence whose object list is three singular schedules. The root's C5 obligation is
   therefore: attribute the mechanism for those three. The assembly's §2.5 table shows a completed
   attribution row for each of the three (standard `d = 5`; class-D `d = 5`, `R ≥ 2`; BB, both
   sectors), each by exclusion-by-restricted-exact-optimisation with *strict* separation licensing
   the exclusion, exhaustive over the fault model to `cap = d` rather than by sampling. **C5 is
   discharged.**
2. **The phrase "for each instance" is in the *instances premise's* claim — and there it also means
   the three named schedules**, not the `(instance, sector, R)` cells. Read the premise claim:
   *"…for a standard surface-code schedule, a legal hook-misaligned surface-code schedule, and at
   least one explicitly specified qLDPC schedule, … and **for each instance** provide auditable
   minimum witnesses and a justified attribution…"* — "instance" refers back to that list of three.
   So the assembly's §2.5 statement that *"the instances claim's 'for each instance' is the wider
   obligation"* reads its own premise **more harshly than the text requires**. That is a
   safe-direction error and I flag it only for accuracy: it means the incomplete Table-6.2
   exclusion coverage (missing `d = 7` class-D X-sector, `d = 7` standard beyond `R = 3`, all of
   `d = 9`, all of `d = 3`) is not a shortfall against the premise's claim either. It remains a
   real limitation of the *dossier*, correctly recorded as **G4**.

*One residual I do raise on C5.* For the standard surface schedule `d_∞ = d`, so nothing limits the
distance *below* the code distance; the reported mechanism ("single-round bulk; hooks not needed;
measurement faults excluded") is the mechanism *realising* the minimum, not one *limiting* it. This
is the natural reading of "distance-limiting mechanism" and matches 课题四's four-way split
(线 198–201), so it is a discharge — but the root's caveat set should say the label is
"mechanism of the minimum witness", not "obstruction to reaching `d`". Folded into **R-C13**.

*And I confirm G4's boundary point.* The exclusion of the temporal-boundary mechanism is by
argument plus an absence observation, labelled `CONJECTURED` by the dossier itself. (C5) as written
is discharged; (C5) read as *"prove the boundary mechanism is empty in this model"* would not be.
The root claim does not bear the second reading. **R10 is a clarification, not a repair.**

### 1.5 Lemma A.1 — attacked, and it holds

The assembly's one new mathematical step. Statement: if `d_{R*} = v` for some `R* ≥ v − 1`, then
`d_∞ = v` and `R_stab = min{R : d_R = v}`.

I re-derived it independently. Monotonicity (window claim part (i)) makes `d_R` a non-increasing
sequence of positive integers, so `d_∞ = min_R d_R ≤ d_{R*} = v`. If `d_∞ ≤ v − 1` then
`R_stab ≤ d_∞ ≤ v − 1 ≤ R*` (window claim), so `d_{R*} = d_∞ ≤ v − 1 < v` — contradiction. Hence
`d_∞ = v`. Monotonicity makes `{R_0 : d_{R_0} = v}` an up-set, giving the second equality. **The
lemma is correct**, and it is genuinely one round tighter than Corollary 5.4's `R* ≥ d_{R*}`.

**But the assembly's provenance claim for it is wrong.** §2.6 asserts Lemma A.1 *"uses only the
window premise's certified claim text"* and the review checklist item 2 repeats it. It also uses the
**definition** of `R_stab` as `min{R_0 : d_R = d_∞ ∀ R ≥ R_0}` — and no claim text in the route
supplies that definition (see §3A). Today that definition lives only in transfer **Definition 2.11**,
which is document-level. So Lemma A.1 currently rests on claim text *plus one document-level
definition*. **Adopting the §3A repair fixes this**: the revised root claim supplies the definition
at claim level, and Lemma A.1 becomes exactly what the assembly says it is. This is a fourth
independent reason to adopt §3A.

---

## 2. Bridge audit

### 2.1 Transfer Lemma 2.9 (elementary faults vs locations) — **holds; but the assembly mis-scopes its own usage rule**

The mismatch is real and the assembly identified it correctly. Window **Definition 1.10** (line 196
of the window theorem): *"Every elementary fault has weight 1; `|F|` counts **elementary faults**"* —
a multiset count. Transfer **Definition 2.8**: `|F| := #{locations assigned a non-identity
element}`. Instances (C4): *"`|F|` counts faulty **locations**"*. Two of the three premises minimise
over configurations; one minimises over multisets. Without a reconciliation the three claims are
about different functions `d_R`, and **every** clause discharge collapses into an equivocation.

Lemma 2.9 reconciles them: record flips and observable flips are `F₂`-linear in the assignments, so
two faults sharing a location may be merged into their product (which lies in that location's group
— the 15-element two-qubit set, the 3-element single-qubit set, or `F₂` for a classical flip, each
closed under multiplication together with the identity), leaving the effect unchanged and dropping
the weight by 1 or 2. Iteration terminates. **I re-derived this and it is correct.** Per-round
additivity `|⊔_r S_r| = Σ_r |S_r|` needs the location set partitioned by round, which is scope
clause **T2** — the same clause as W-G2, correctly noted by the assembly.

**Finding (assembly self-consistency defect).** The assembly's §0.3 rule 1 says the
claim-text-only restriction *"bites in exactly two places and both are flagged: the window premise's
adaptive halting rule … and the transfer premise's Proposition 3.7"*. **It bites in three.** Lemma
2.9 is a numbered result inside the transfer artifact, is **not** named in the transfer claim text,
and is load-bearing at claim level for the alignment of all three premises' `d_R`. The assembly
treats it as a plain bridge in §3.4/F4 without the proposer-level flag it gives Prop 3.7. This does
not refute anything — the lemma is elementary and correct — but the assembly's own honesty rule is
violated without the flag, and the caveat set must name it. Folded into **R-C4**.

### 2.2 Transfer Prop 3.7 (Def-2.7 vs canonical detectors) — **re-derived; holds; independently recomputed 13/13**

Prop 3.7 states: `d_R^Z(M)` against the canonical detector space `𝒟` of Definition 3.5 equals
`d_R^Z(M)` against the Definition-2.7 detector set. It is **not** in the transfer claim text; the
assembly flags it proposer-level, correctly.

**Re-derivation (mine).** Def-2.7's set lies in `𝒟` (Prop 3.6), so `{undetectable vs 𝒟} ⊆
{undetectable vs 2.7}` and hence `d^{2.7} ≤ d^{𝒟}`. Conversely take `F` attaining `d^{2.7}` and let
`F^X` be its X-sector projection (Lemma 3.1). By 3.1(1) `F^X` flips the same `D_{b,r}` (none) and
the same observables (some); since Prop 3.6 gives `𝒟_Z = span{D_{b,r}}` with **equality**, `F^X`
annihilates `𝒟_Z`. By 3.1(2) `F^X` flips no X-check record whatsoever, so it annihilates every
parity of X-check records, i.e. all of `𝒟_X = V_X` — *including* the `dim leftker(H_X)` redundancy
directions `⊕_{a∈T} m_{a,0}` that Def-2.7 omits. With `𝒟 = 𝒟_Z ⊕ 𝒟_X` and `|F^X| ≤ |F|` (3.1(3)),
`d^{𝒟} ≤ d^{2.7}`. **The argument is valid.** Its two load-bearing inputs are the *equality* in 3.6
(not containment) and clause (2) of Lemma 3.1; both are proved in the document and both were
independently re-verified by the wave-15 re-reviewer.

**Independent recomputation.** I wrote a spacetime simulator from the frozen definitions (§8): it
builds `C_R^Z(M)` explicitly for a CSS code and a legal non-interleaved (hence automatically (MC),
since `c_{ab} = 0`) schedule, computes `𝒟` **from Definition 3.5 directly** — back-propagating each
record's Pauli to time 0, testing membership in `G_0 = ⟨Z_q, Z_{anc(b,r)}, X_{anc(a,r)}⟩` for
determinism and commutation with every `X_L^{(j)}` for detector-hood — and then finds the minimum
weight of an undetectable-and-logical fault configuration against each detector set.

| instance | `R` | `dim leftker(H_X)` | `𝒟 = 𝒟_Z ⊕ 𝒟_X` | `𝒟_Z = span{D_{b,r}}` exactly | codim of `span{D_{a,r}}` in `𝒟_X` | `d^{2.7}` | `d^{𝒟}` | negative control `d^{𝒟'}` |
|---|---|---|---|---|---|---|---|---|
| `[[4,2,2]]` independent gens | 1,2,3 | 0 | OK | OK | 0 = 0 ✔ | 1 | 1 | 1 |
| `[[4,2,2]]` X-check duplicated | 1,2,3 | 1 | OK | OK | 1 = 1 ✔ | 1 | 1 | 1 |
| `[[4,2,2]]` X-check tripled | 1,2,3 | **2** | OK | OK | 2 = 2 ✔ | 1 | 1 | 1 |
| Steane + 1 redundant X-check | 1,2 | 1 | OK | OK | 1 = 1 ✔ | **2** | **2** | **1** ← differs |
| Steane + 2 redundant X-checks | 1,2 | **2** | OK | OK | 2 = 2 ✔ | **2** | **2** | **1** ← differs |

**Prop 3.7 holds in 13/13 configurations. Prop 3.6's three exact statements hold in 13/13**, at
`dim leftker(H_X)` = 0, 1 **and 2** — the last matching BB's situation exactly. In every instance
the Def-2.7 set is contained in `𝒟`, every observable lies in `V` but **not** in `𝒟` (so the split
is a genuine complement), which are the two well-posedness facts Definition 3.5 needs.

**The test is not vacuous.** The negative control replaces one Def-2.7 detector `D` by `D + λ^{(1)}`
— a *different* complement of `span{λ}`, exactly the manoeuvre T-G3 is about. On both Steane
variants the minimum drops from 2 to 1. So my machinery does detect a detector-convention change
when one exists, and independently reproduces the structure of the T-G3 counterexample that killed
the withdrawn mitigation (*"any `𝒟` between Def-2.7 and `V` leaves the theorem intact"*). The
mitigation is indeed refutable; the installed condition `span{D_{b,r}} ⊆ 𝒟' ⊆ 𝒟` is the right one.

**BB application, recomputed from scratch.** Building `A = 1 + y + x`, `B = 1 + y + x²y` as
`3×3`-bicirculants over `F₂` (`l = m = 3`, `n = 2lm = 18`), `H_X = [A|B]`, `H_Z = [Bᵀ|Aᵀ]`:

```text
CSS commutation H_X H_Z^T = 0 : True
n = 18   rank H_X = 7   rank H_Z = 7   k = 4
check weights H_X [6]  H_Z [6]     qubit degrees H_X [3]  H_Z [3]
d_X = 4   d_Z = 4   d = 4
#checks H_X = 9, rank 7  ->  dim leftker(H_X) = 2
#checks H_Z = 9, rank 7  ->  dim leftker(H_Z) = 2
```

**`dim leftker(H_X) = 2` is CONFIRMED**, and the assembly's §8.2 line reproduces exactly. So the
Def-2.7 detector set genuinely omits a two-dimensional space of real detectors on the qLDPC arm,
and Prop 3.7 is load-bearing there rather than vacuous. The assembly's reading is right.

**New finding the assembly missed: `dim leftker(H_Z) = 2` as well.** The assembly's §3.6 concludes
*"the whole subtlety sits on the X-side"* and cites Prop 3.7 alone as the bridge. That is correct
for the **Z-memory** sector only. The root aggregates min-over-sectors, so the **X-memory** sector's
Def-2.7 computation needs Prop 3.7's *mirror*, which comes from transfer **CONJECTURED 8.1**
(*"the mirror … carries every statement of §3–§7 to `C_R^X(M)`"*) — a second document-level result,
also not in the transfer claim text. Because `dim leftker(H_Z) = 2` on BB, the mirrored hole is
just as large as the direct one and the mirror step is **not** decorative. Severity: low (8.1's
derivation is a symmetry argument and (MC) mirror-symmetry is independently re-derived in transfer
§2.5), but the caveat must name it. Folded into **R-C4**.

### 2.3 If Prop 3.7 failed, what collapses?

Stated for the record, since the brief asks. Prop 3.7 does **not** fail. Were it to:

* **(C4c) collapses first and hardest.** The BB arm's `d_R` values are computed against the Def-2.7
  set while the certified detector convention is Definition 3.5, and `dim leftker(H_X) = 2` makes
  the two sets genuinely different there. Without 3.7 the reported `(3, 1)` is a number about a
  different object than the one the root claims, and the qLDPC clause is undischarged.
* **(C4a)/(C4b) survive**, because the rotated-surface generating sets are independent
  (`leftker = 0`), so Def-2.7's set already equals `𝒟` there — as my `[[4,2,2]] independent gens`
  rows confirm (codim 0).
* **(C1) is damaged but not destroyed**: Theorem T's `d_R` would be the Def-2.7 quantity, which
  would no longer be the certified `d_circ`; the representation clause would need restating against
  Def-2.7 explicitly.
* **(C2)/(C3) are untouched at the level of the window claim's internal logic**, but C3's evaluator
  would compute the wrong quantity, so the composed algorithm would be unsound.

So Prop 3.7 is a genuine single point of failure for the qLDPC arm, and the assembly is right to
refuse to launder it.

---

## 3. The two lead questions, adjudicated

### 3A. `R_stab` — **genuinely off by one, and the defect is structurally worse than the assembly states**

**(i) What each reading gives on the `d = 5` class-D cell.** The certified sequence is
`d_R = 4, 3, 3, 3, 3, 3, 3` for `R = 1..7`, `d_∞ = 3`.

* **Premises' convention** `R_stab = min{R_0 : d_R = d_∞ ∀ R ≥ R_0}` → the least `R_0` with
  `d_{R_0} = 3` is `R_0 = 2`. **`R_stab = 2`.**
* **Root's literal wording** *"the first round after which the sequence is identically `d_∞`"* →
  the least round `r ≥ 1` such that `d_R = 3` for all `R > r` is `r = 1` (after round 1 the
  sequence `d_2, d_3, …` is identically 3). **`R_stab = 1`.**

In general `R_stab^root = max(1, R_stab^premises − 1)`: the two agree exactly when
`R_stab^premises = 1` and differ by one otherwise — i.e. they differ on precisely the class this
campaign discovered.

**(ii) The consequence the assembly understates.** Under the root's literal wording the headline
family reads `R_stab = 1, 2, 3` at `d = 5, 7, 9` instead of `2, 3, 4`. The `d = 5` class-D cell
would give **`R_stab = 1`, the same value as the standard schedule** — so *the campaign's headline
result, "`R_stab > 1` exists / single-round dominance refuted", would no longer be witnessed by the
`d = 5` cell at all*. That cell is the one carried by four independent methods and fully re-run by
the wave-25 reviewer; the witness would fall back to `d = 7` (two methods, re-run) and `d = 9`
(one method, proposer-level). The discovery survives at reviewed level either way, but its
evidential base is materially thinner. Adopting the repair is what keeps the headline on its
strongest cell.

**(iii) The structural point neither the assembly nor any node makes — and it is decisive.**
I checked every claim text in the route. **The root's is the only one that defines `R_stab` at
all.** The window claim *uses* `R_stab` (`R_stab(M) ≤ d_∞(M) ≤ d`; *"the first `d` distances decide
both"*) without defining it. The instances claim *uses* it (*"Determine or rigorously bound
`(d_infinity,R_stab)`"*) without defining it. The transfer claim does not mention it. The
min-convention definition exists only in transfer **Definition 2.11**, which is document-level.

Therefore, **as the texts stand today, the two `CERTIFIED*` premise claims that quantify over
`R_stab` are formally claims about the root's off-by-one definition** — the only claim-level
definition in the route — while every certified *number* they carry is computed under the other
one. The window claim happens to remain *true* under the root's reading (`R_stab^root ≤
R_stab^premises ≤ d_∞`), so nothing is refuted; but the route's claim texts are not all about the
same object, and the instances premise's certified values are wrong by one against the only
claim-level definition available to a reader. This is not a wording tidy. **It is the repair
without which the composition does not close at claim level.**

**(iv) Independent frozen-text support.** 课题四 defines its own index at line 194 of
`CIRCDIST_PROBLEMS.md`:

> `R_sat(M) = min{ R_0 : d_R(M) = d 对所有 R >= R_0 }。`

The frozen commission uses the **min form**. The rescope replaced the target (`d` → `d_∞`) but there
is nothing in `SAT_RESCOPE_20260822.md` changing the *shape* of the index. So the root's "first
round after which" is a drafting slip introduced at rescope, not a deliberate alternative
convention. This is decisive and should be quoted in the lead ruling.

**(v) The exact minimal claim-text fix.** Replace, in `research/circdist/proof-dag/nodes/CIRCDIST.sat.yaml`, field `claim`:

```text
FROM:  and R_stab(M) the first round after which the sequence is identically d_infinity(M).
TO:    and R_stab(M) = min{R_0 : d_R(M) = d_infinity(M) for all R >= R_0}.
```

Nothing else changes. **Full revised claim string, V1 (minimum sufficient repair):**

```text
For a fixed legal single-round single-ancilla CSS syndrome-extraction schedule M under ideal initialization and final data readout, let d_R(M) be the circuit distance after R repeated rounds, d_infinity(M) = lim_{R to infinity} d_R(M), and R_stab(M) = min{R_0 : d_R(M) = d_infinity(M) for all R >= R_0}. Give a finite-state min-plus representation of d_R, prove an explicit finite-window theorem and algorithm deciding (d_infinity,R_stab), compute or rigorously bound that pair for a standard surface-code schedule, a legal hook-misaligned surface-code schedule, and at least one qLDPC schedule, and attribute the distance-limiting mechanism using auditable minimum witnesses.
```

```text
V1 claim hash:  sha256:0f927e6408f122fe435db4ee45cf86ee89f2edf6471e45dce5f0f117fe59675e
```

**Recommended variant V2 (V1 + the assembly's R1 and R2).** I recommend but do not require it. R2
(sector aggregation) is of the *same class as the defect*: the preamble's `d_R` is currently silent
between two readings that yield **different certified `R_stab` values at `d = 7`** (min-over-sectors
gives `R_stab = 2` on classes B and C; a single-sector reading gives 1), while all three premises fix
the convention and W-G1 is LOAD-BEARING-WITH-WITNESS. R1 (verbatim repetition) pins the layout and is
what makes §3B's disposition legible in the claim itself. Edits:

```text
FROM:  let d_R(M) be the circuit distance after R repeated rounds,
TO:    let d_R(M) be the circuit distance after R verbatim repetitions of M, taken as the
       minimum over the two CSS memory sectors,
```

**Full revised claim string, V2:**

```text
For a fixed legal single-round single-ancilla CSS syndrome-extraction schedule M under ideal initialization and final data readout, let d_R(M) be the circuit distance after R verbatim repetitions of M, taken as the minimum over the two CSS memory sectors, d_infinity(M) = lim_{R to infinity} d_R(M), and R_stab(M) = min{R_0 : d_R(M) = d_infinity(M) for all R >= R_0}. Give a finite-state min-plus representation of d_R, prove an explicit finite-window theorem and algorithm deciding (d_infinity,R_stab), compute or rigorously bound that pair for a standard surface-code schedule, a legal hook-misaligned surface-code schedule, and at least one qLDPC schedule, and attribute the distance-limiting mechanism using auditable minimum witnesses.
```

```text
V2 claim hash:  sha256:c6205671936488f9ccbf69d68d9893b549098244bd5f95985b4a682df0d8bdd9
```

*Optional totalisation, NOT recommended now.* The frozen 课题四 adds *"如果不存在这样的 `R_0`,定义
`R_sat(M) = 无穷`"*. Under the window premise the set is always non-empty (a non-increasing sequence
of positive integers is eventually constant), so totalising is unnecessary and would change the hash
a third time. If the lead wants it anyway, it must be requested **before** the dispatcher executes,
and a fresh hash must be issued.

### 3B. The "公共定义 line 58" misattribution — **confirmed independently; disposition: MILDER for the root, UNCHANGED for the window node**

I read `research/circdist/notes/CIRCDIST_PROBLEMS.md` (`5f6dc37f…`, 243 lines) in full myself.

**(i) Where the idle-compression clause actually sits.** Line 58 reads
`- 无意义的空闲层应当压缩掉。` It is the **last bullet of the `S_Gross` definition inside 课题一**
(the Gross-code problem): line 44 opens 课题一, line 51 reads *"令 S_Gross 表示所有满足以下条件的
调度:"*, and lines 53–58 are that bullet list. The 公共定义 block is **lines 14–41** and contains no
compression clause. **The clincher against any "shared definition" reading is inside the same
list**: line 53 is *"每个 weight-6 stabilizer 使用一个辅助比特"* — weight-6 is Gross-specific. The
list is unambiguously local to 课题一. The assembly's provenance finding is **CONFIRMED**, and the
citation is wrong on three nodes (window caveat 1; transfer T-G1; instances C2) and in the wave-11
re-adjudication.

**(ii) Does 课题四's frozen statement carry ANY compression requirement? No.** 课题四 is lines
185–233; I read all of it. There is no compression clause of any kind — not cross-round, not
within-round. `SAT_RESCOPE_20260822.md` (`6c8ec436…`), the root's governing text, introduces none.
What 课题四 *does* fix is the layout, at line 189: *"令 `C_R(M)` 表示将**同一轮 `M` 重复 `R` 次**"*
— repeat the **same round** `M` `R` times. That is verbatim repetition, i.e. exactly scope clauses
**S2** and **T2**.

**(iii) What it does to this root's inheritance of W-G2: MILDER, and precisely so.**

* **For the window node: UNCHANGED.** W-G2 is a scope condition on the *window claim's own*
  universal quantifier ("every fixed legal schedule"), and legality is Definitions 1.3/1.4, which
  make no reference to compression. That quantifier is the window premise's to defend wherever the
  compression instruction lives. **Nothing here licenses a level change on `CIRCDIST.sat.window`,
  and I propose none.** Concretely: of the wave-11 adjudication's four independently sufficient
  grounds for STAYS-CERTIFIED\*, the correction weakens only the *second half* of ground (1)
  ("…it excludes exactly the idle-compressed layouts the frozen 公共定义 asks for" — false); the
  first half of ground (1) ("W-G2 is an unproved scope condition on the claim's own universal
  quantifier") survives verbatim, and grounds (2), (3) and (4) — frontier task-001 and task-002
  still owed, and no single hash-bound review has attacked the assembled claim — are untouched. A
  careless reading of this finding must not be used to argue window → `PROVED`. It cannot be.
* **For the root: MILDER.** The root's object is `C_R(M)`, which 课题四 defines as `R` verbatim
  repetitions of `M`. Cross-round idle-compressed layouts are therefore **a different circuit**, not
  an unproved case of the root's own model. The root inherits W-G2 as a **scope pin** on how
  `C_R(M)` is formed, not as a hole in its own quantifier. The current record makes it look harsher
  than it is, because it asserts the frozen model *demands* the excluded layout — which is simply
  not true for question 4.
* **A widening I checked and cleared.** Dropping the compression instruction *widens* the admissible
  `M` to include schedules with globally idle layers. That is harmless: window S2 / transfer T2 are
  proved for all legal `M` under verbatim repetition regardless of idle layers, and the instances
  arm's schedules happen to have none. It also makes S2's interpretive move ("read the compression
  instruction as within-round, applied once to `M`") **unnecessary for the root** rather than
  merely defensible — a strictly simpler position.
* **What is NOT relieved.** The assembly's residual **G5** stands untouched: *"`T = 12` is the
  compressed depth for BB `[[18,4,4]]`"* is not established (depth 6 is exhaustively (MC)-empty;
  depths 7–11 were never scanned). What is verified is the weaker "no globally idle layer".

**(iv) Recommended disposition.**

1. **Provenance repair, append-only, no level change:** correct the citation on all three premise
   nodes and record the correction against the wave-11 re-adjudication — the clause is
   **课题一's `S_Gross` bullet (line 58)**, not 公共定义 (lines 14–41). In window caveat 1, strike
   only the sub-clause *"while 公共定义 line 58 itself imposes idle-layer compression"* and keep the
   rest verbatim.
2. **Lead ruling requested (one line):** *does 课题四 inherit 课题一's `S_Gross` compression bullet?*
   My recommendation is **No** — the bullet list defines the admissible schedule set for 课题一 only,
   as its own weight-6 bullet proves.
3. **If the lead so rules,** the root's inheritance is the scope pin **R-C3**, and adopting **R1**
   (V2 above) writes that pin into the claim, which is the cheapest way to make the disposition
   self-documenting.
4. **No level change anywhere** follows from this finding.

---

## 4. Caveat-set audit

The assembly composes 15 premise caveats into 11 root caveats with 3 absorbed and 1 newly named. I
checked each absorption, since absorbing is how conditionality goes missing.

| absorbed | assembly's ground | my ruling |
|---|---|---|
| **A1** instances **(W)** — the `R_stab`/`d_∞` readings import the window theorem | "route-internal; the root already carries `window` as a premise" | **PARTIALLY REJECTED.** The *conditionality* is indeed already carried, but the caveat also encodes a **non-independence** fact that changes the root's risk profile: a window defect is a double hit, and a reader of the root's caveat list alone would conclude the root rests on three independent supports. R5 puts this in the route implication text but **not** in the root's caveat list. **Restore as a root caveat (R-C12).** |
| **A2** the fitted law `d_R = max(d − R, (d+1)/2)`, `R_stab = (d−1)/2` stays CONJECTURED | "out of claim; composes as an explicit exclusion" | **CORRECT that it is out of claim** (I re-read the verbatim root text; the law is not there), **but list it.** The root's assessment summary will carry the headline, and an exclusion that is only narrated in prose is one edit away from disappearing. **Restore as a listed exclusion (R-C13).** |
| **A3** W-OPEN answered positively at REVIEWED level | "status note, not a limitation; the window theorem survived its first nontrivial stress test" | **ACCEPT the absorption, REJECT the wording.** "Stress test" overstates it. Instances caveat (W) says its `R_stab`/`d_∞` readings *import* window; so the tail statements that make `R_stab` meaningful are assumed, not tested. What *is* genuinely tested — and did pass — is monotonicity and `R_stab ≤ d_∞ ≤ d` **on the computed prefixes**, which are not imported. The honest phrase is *"a consistency check on the computed prefixes"*, not *"an independent confirmation"*. Folded into **R-C12**. |

The four cross-cutting merges (R-C1…R-C4) and the seven single compositions (R-C5…R-C11) I checked
against the premise caveat texts one by one. **No load-bearing content is lost in those eleven**, and
none is inflated. R-C1 (the shared frozen-model single point of failure) is a genuine new caveat and
is the right one to name — all three premises restate the same 公共定义 model and none re-derives it,
so cross-checking between them cannot detect a common misreading.

### 4.1 The caveat set I would put on the root — 13 items

R-C1 … R-C11 **as the assembly states them**, with one amendment and two additions:

* **R-C4 (amended).** The detector/observable split is fixed **by decision, not derivation**
  (Definition 3.5, lead-ratified; corrected safe condition `span{D_{b,r}} ⊆ 𝒟' ⊆ 𝒟`, containment in
  `𝒟`, **not** in `V`; W-G3 must not be carried; S3′ load-bearing). **Three steps of the composition
  rest on numbered results that are NOT in any premise's claim text and are therefore
  proposer-level:** (a) transfer **Prop 3.7**, reconciling the instances arm's Def-2.7 detector set
  with the canonical split in the **Z**-sector; (b) its **mirror via transfer §8.1**, needed for the
  **X**-sector — non-decorative on the qLDPC arm, where I verified `dim leftker(H_Z) = 2` as well as
  `dim leftker(H_X) = 2`; and (c) transfer **Lemma 2.9**, reconciling the window premise's
  *elementary-fault* count with the other two premises' *location* count, without which the three
  premises' `d_R` are different functions. All three were re-derived and, for (a), independently
  recomputed 13/13 in this review.
* **R-C12 (new).** **The route is not a flat conjunction and the premises are not independent
  evidence.** `instances` imports `window` for every statement outside its computed windows
  (instances caveat (W)); the dependency graph is `window → instances`, with `transfer` alongside
  and used by neither as a load-bearing numerical input. A defect in `window` therefore hits two of
  the three premises. Consequently the instances arm's positive answer to W-OPEN is **a consistency
  check on the computed prefixes** (monotonicity and `R_stab ≤ d_∞ ≤ d`, which are not imported),
  **not** an independent confirmation of the window theorem's tail clause.
* **R-C13 (new).** **Explicit exclusions — the root neither asserts nor uses these:** the fitted law
  `d_R = max(d − R, (d+1)/2)` / `R_stab = (d−1)/2`; the reading "`R_stab` is unbounded"; the §6.2b
  interpretive account of *why* `R_stab > 1` occurs; and the reading of (C5) as a *proved* emptiness
  of the temporal-boundary mechanism. Also: for the standard surface schedule `d_∞ = d`, so its
  mechanism label describes the **minimum witness**, not an obstruction to reaching `d`.

Nothing load-bearing was absorbed away once R-C12 and R-C13 are restored.

---

## 5. Verdict under `research/DAG_PROTOCOL.md` §3, and licence

### 5.1 Route `asymptotic-stability-assembly` → **CERTIFIED\***

§3 defines `CERTIFIED*` as *"an independently reviewed conditional result with explicit unresolved
premises or scope caveats"*, and §5 requires for completion-level promotion of **either a node or a
route** a locatable independent adversarial review of the assembled argument by a reviewer other
than its author, stating reviewer/model, independence declaration, materials, scope, verdict and
limitations, hash-bound via `reviewed_hash`. The assembly supplies the assembled argument for the
route implication; this document is that review; §0 supplies every required element.

`PROVED` is **not** reachable and I do not license it: it requires *"a complete argument and all
load-bearing inputs passed independent adversarial review"*, and three load-bearing steps (R-C4 a/b/c)
sit outside the premises' certified claim texts, while R-C1 (the shared frozen-model single point of
failure) is an unresolved scope caveat by construction.

### 5.2 Node `CIRCDIST.sat` → **CERTIFIED\*** (from `CONJECTURED`)

All eight clauses are discharged by `CERTIFIED*` premises whose claim hashes I recomputed and
matched 3/3; the six-axis convention audit finds no mismatch and I re-ran its two bridges
independently; the caveat composition is sound once R-C12/R-C13 are restored. A parent cannot
outrank its weakest premise on this route, and independently the frozen ground rules state that
numerical simulation never substitutes for proof — which caps clauses C4/C5. **`CERTIFIED*` is both
the ceiling and the earned level.**

### 5.3 Licence — CONDITIONAL

I license the dispatcher, **after the lead rules**, to set:

* `routes.asymptotic-stability-assembly.assessment.level: CERTIFIED*`
* `assessment.level: CERTIFIED*` on `CIRCDIST.sat` (event `level-change`, `from: CONJECTURED`)
* `assessment.caveats`: the **13-item set of §4.1**
* `basis.reviews`: this document, `kind: review`, `locator: Section 5`, with `reviewed_hash` as below

**Binding conditions, all three required:**

1. **The `R_stab` repair of §3A is adopted.** The licence binds to the revised claim, not the
   current one:

   | adopted revision | `reviewed_hash` the dispatcher must record |
   |---|---|
   | **V1** — R3 only (minimum sufficient) | `sha256:0f927e6408f122fe435db4ee45cf86ee89f2edf6471e45dce5f0f117fe59675e` |
   | **V2** — R1 + R2 + R3 (recommended) | `sha256:c6205671936488f9ccbf69d68d9893b549098244bd5f95985b4a682df0d8bdd9` |

   The licence is granted at **either** hash and at **no other**. If the lead adopts V1, R-C2
   (sector aggregation) and R-C3 (verbatim-repetition layout) carry the two unwritten conventions
   as caveats — which is why V2 is the better claim. If the lead declines the repair entirely, or
   adopts any third wording, **the licence lapses** and the route stays `CONJECTURED` pending a
   fresh review bound to whatever text is adopted; do not extrapolate this verdict to a claim string
   I did not hash. A claim revision must be logged as a `claim-revised` event per §5.6.
2. **The root carries the 13-caveat set of §4.1**, including the amended R-C4 and the restored
   R-C12 and R-C13.
3. **The three accuracy corrections of §6 are recorded** (as an amendment to the assembly or as node
   events). They are not blocking for the mathematics; they are blocking for the honesty record,
   because each is a place where the assembly claims more provenance discipline than it exercised.

**No level change is licensed on any premise**, and none is implied. In particular §3B does **not**
license a promotion of `CIRCDIST.sat.window`.

---

## 6. FURTHER-REPAIR items (non-blocking for the level; blocking for the record)

| # | item | where | severity |
|---|---|---|---|
| **A** | §0.3 rule 1 says the claim-text-only restriction *"bites in exactly two places"*. It bites in **three**: the window's adaptive rule, transfer Prop 3.7 (+ its §8.1 mirror), and **transfer Lemma 2.9**, which is load-bearing for the alignment of all three premises' `d_R` and is used in §3.4/F4 without the proposer-level flag. | assembly §0.3, §3.4, F4 | honesty |
| **B** | §2.6 and checklist item 2 claim Lemma A.1 *"uses only the window premise's certified claim text"*. It additionally uses the **min-convention definition of `R_stab`**, which today exists only in transfer Definition 2.11 (document-level). Adopting §3A repairs this and makes the claim true. | assembly §2.6, §6 item 2 | honesty |
| **C** | §3.6 concludes *"the whole subtlety sits on the X-side"* and names Prop 3.7 as the bridge. True for the Z-memory sector only; the X-memory sector needs Prop 3.7's mirror via transfer §8.1, and on BB the mirrored hole is the same size (`dim leftker(H_Z) = 2`, verified §2.2). | assembly §3.6, F6 | accuracy |
| **D** | §2.5 reads the instances premise's *"for each instance"* as a wider obligation than the root's. It is not: "instance" in that claim refers to the same three named schedules. Safe-direction error; correct it so the dossier's Table-6.2 coverage is not recorded as a shortfall against its own claim. | assembly §2.5 | accuracy (safe direction) |
| **E** | Root node byte hash drifted `1ba58fe2… → bcf3fcbe…` via the appended `root-assembly-2026-08-23` event. Claim text and claim hash unchanged. Record as expected trip-wire behaviour. | assembly §0.1 | bookkeeping |

---

## 7. Limitations of this review

Stated so a later reader can price this verdict correctly.

1. **I did not recompute any `d_R` value of the instances arm.** No surface-code or BB circuit
   distance in §2.4 of the assembly was re-derived here. Those rest on the wave-25 review, which I
   did not re-run. My computations are confined to §8: the hash pipeline, the BB code parameters,
   and Prop 3.6/3.7 on small codes I chose.
2. **Prop 3.7 was verified on small codes, not on BB or the rotated surface.** `[[4,2,2]]` variants
   (n = 4) and Steane variants (n = 7) at `R ≤ 3`, with redundancy dimension 0, 1 and 2. The BB
   instance itself (n = 18, `T = 12`, `R ≤ 6`) is out of reach of exhaustive weight-≤3 search in one
   box. What I verified on BB is the *hypothesis* of the bridge (`dim leftker(H_X) = dim leftker(H_Z)
   = 2`), not the bridge's conclusion at BB scale.
3. **My schedules are non-interleaved** (chosen so that (MC) holds automatically, `c_{ab} = 0`).
   Interleaved legal (MC) schedules — the class where hook misalignment lives — were not tested for
   Prop 3.7. The proposition's derivation uses no interleaving hypothesis, and the wave-15
   re-reviewer's independent check did include interleaved instances, but my own evidence does not.
4. **My minimum-weight search is capped at weight 3** (exhaustive at weights 1 and 2, meet-in-the-
   middle at weight 3). Every distance reported in §2.2 is 1 or 2, so the cap never bound; but a
   configuration of weight ≥ 4 would have been reported as `>3`, not resolved.
5. **I did not re-derive Lemma 3.1, Prop 3.6's derivation, or Definition 3.5's well-posedness from
   first principles**; I verified Prop 3.6's three exact statements *numerically* (13/13) and checked
   the derivations for validity by reading. The transfer document's reviews are what certify them.
6. **I did not audit the transfer, window, or instances premises themselves.** Their `CERTIFIED*`
   levels are read off the canonical node records. This review is of the *composition*, exactly as
   the route's second obligation requires.
7. **A bug in my own first run** (the Def-2.7 `D_{a,r}` index range, `r ∈ {1,…,R−1}`, was
   mis-restricted to `r ≤ R − 2`) initially produced spurious Prop-3.6 codimension mismatches. It was
   found by the codimension cross-check disagreeing with `dim leftker(H_X)`, fixed, and everything in
   §2.2 is from the corrected run. I record it because the cross-check is what caught it, which is an
   argument for keeping Prop 3.6's dimension identity in the record as a live assertion rather than
   prose.
8. **One box, no sub-agents.** Depths 7–11 for BB (G5), the `d = 7`-standard X-sector MILP cell (G3),
   and a `d_X ≠ d_Z` qLDPC instance (G6) were not attempted and remain the three cheapest informative
   computations for this root.

---

## 8. Reproduction

All code below was written this session from the frozen definitions and the statements under test.
No circdist program was read. Two files, both in the session scratchpad.

### 8.1 Hash pipeline + claim hashes

```python
import hashlib, pathlib, yaml
def ch(c): return "sha256:"+hashlib.sha256(c.replace("\r\n","\n").strip().encode("utf-8")).hexdigest()
root = pathlib.Path("<repo>")
ok = bad = 0
for p in sorted(root.rglob("proof-dag/nodes/*.yaml")):
    d = yaml.safe_load(p.read_text(encoding="utf-8"))
    if not isinstance(d, dict) or not isinstance(d.get("claim"), str): continue
    h = ch(d["claim"])
    for r in (((d.get("assessment") or {}).get("basis") or {}).get("reviews") or []):
        if isinstance(r, dict) and r.get("reviewed_hash"):
            ok, bad = (ok+1, bad) if r["reviewed_hash"] == h else (ok, bad+1)
print(ok, bad)          # -> 98 0
```

### 8.2 BB `[[18,4,4]]` parameters

Bicirculants over `F₂` with `l = m = 3`, `A = 1 + y + x`, `B = 1 + y + x²y`, `H_X = [A|B]`,
`H_Z = [Bᵀ|Aᵀ]`; ranks by Gauss–Jordan; `d_X`, `d_Z` by exhausting `ker H_Z` / `ker H_X`
(`2^{11}` each) against `rowsp H_X` / `rowsp H_Z`. Output reproduced verbatim in §2.2.

### 8.3 Prop 3.6 / Prop 3.7 checker

Builds `C_R^Z(M)`: data `|0⟩^{⊗n}`; `anc(b)` prepared `|0⟩` with `q→b` CNOTs; `anc(a)` prepared
`|+⟩` with `a→q` CNOTs; fresh ancillas per round; greedy legal layering with the whole X-block
before the whole Z-block (hence `c_{ab} = 0`, so (MC) holds by construction); records `m_{a,r}`,
`m_{b,r}` for `r = 0..R−1` and ideal terminal `ρ_q`.

* **Fault locations** per Definition 2.8: each CNOT (15 two-qubit Paulis), each ancilla immediately
  after preparation (3), each (qubit, layer) with the qubit not in a two-qubit gate (3), each
  recorded outcome (1 classical flip). Terminal readout ideal, no locations.
* **Propagation** `F₂`-symplectic, `CNOT(c,t): x_t ← x_t + x_c, z_c ← z_c + z_t`; `m_{b,r}` flips on
  the `x`-bit of `anc(b,r)`, `m_{a,r}` on the `z`-bit of `anc(a,r)`, `ρ_q` on the `x`-bit of `q`.
* **`𝒟` from Definition 3.5 directly:** back-propagate each record's Pauli to time 0 by applying the
  same CNOT rule over the gate list in reverse; a parity is **deterministic** iff its
  back-propagated Pauli lies in `G_0 = ⟨Z_q, Z_{anc(b,r)}, X_{anc(a,r)}⟩` (i.e. `x`-part zero on data
  and on `anc(b,·)`, `z`-part zero on `anc(a,·)`), and is a **detector** iff additionally
  `⟨z\|_{data}, χ_{X_L^{(j)}}⟩ = 0` for every `j`. `𝒟` is the nullspace of those conditions;
  `V` is the nullspace of the determinism conditions alone.
* **Def-2.7 set:** `D_{b,0} = m_{b,0}`; `D_{b,r} = m_{b,r} + m_{b,r−1}` for `r = 1..R−1`;
  `D_{b,R} = (⊕_{q∈supp(b)} ρ_q) + m_{b,R−1}`; `D_{a,r} = m_{a,r} + m_{a,r−1}` for `r = 1..R−1`;
  observables `λ^{(j)} = ⊕_{q∈supp(Z_L^{(j)})} ρ_q` with `(Z_L, X_L)` a symplectic logical basis
  computed by Gram–Schmidt on `ker H_X / rowsp H_Z` and `ker H_Z / rowsp H_X`.
* **Distance:** min `|F|` over configurations (distinct locations) that annihilate the given
  detector space and flip some `λ^{(j)}`; exhaustive at weights 1–2, meet-in-the-middle at weight 3.
* **Negative control:** replace one Def-2.7 detector `D` by `D + λ^{(1)}` — a different complement of
  `span{λ}` in `V` — and recompute.

Assertions carried in the code: nullspace vectors are re-verified against every constraint row; the
symplectic pairing `⟨Z_L^{(i)}, X_L^{(j)}⟩ = δ_{ij}` is asserted; `H_X H_Zᵀ = 0` is asserted.
Results are the 13 rows of §2.2.

---

## 9. One paragraph for the node

An independent adversarial review of the wave-26 root composition proof (`68babfe6…`) confirms it.
The hash pipeline was validated against all 98 existing `reviewed_hash` bindings in the repository
(98/98, zero mismatches) before any verdict; the three premise claim hashes and the root claim hash
were recomputed and match. All eight clauses of the root claim are discharged by `CERTIFIED*`
premises; the two attacks the brief prioritised both fail — **C3** ("algorithm") is honestly
discharged by the fixed window, and the frozen 课题四 settles it by framing the algorithmic
obligation as decidability by finitely many checks (line 211) with no complexity clause in the
minimum acceptance; **C5** ("for each instance") does not bite, because the root's attribution clause
quantifies over the three named schedules and so, on its text, does the instances premise's. Both
convention bridges were re-derived and independently recomputed: transfer **Lemma 2.9** is correct,
and transfer **Prop 3.6/3.7** hold in 13/13 configurations built from the frozen definitions with no
proposer code read, at redundancy dimension 0, 1 and **2**, with a negative control that does move
the distance (2 → 1) and so shows the test is not vacuous; `dim leftker(H_X) = 2` for BB `[[18,4,4]]`
is confirmed, **and so is `dim leftker(H_Z) = 2`**, which means the X-sector additionally needs Prop
3.7's mirror via transfer §8.1 — a step the assembly does not name. On the two lead questions: the
root's `R_stab` wording is **genuinely off by one** (premises 2, root's literal wording 1 on the
`d = 5` class-D cell), and the defect is structurally worse than the assembly states — the root's is
the **only claim-level definition of `R_stab` anywhere in the route**, so today the two premise
claims that quantify over it are formally about the wrong index while their certified numbers use the
right one, and under the literal wording the `d = 5` headline cell would no longer witness
`R_stab > 1` at all; frozen 课题四 line 194 uses the min form, confirming a drafting slip at rescope.
The "公共定义 line 58" misattribution is **confirmed against the frozen bytes** — the clause is the
last bullet of 课题一's `S_Gross` list, whose own weight-6 bullet proves it is Gross-local, and 课题四
carries no compression requirement at all — which makes the **root's** inheritance of W-G2 a scope
pin rather than a hole in its own quantifier (**milder**), while leaving the **window node's** W-G2
and its `CERTIFIED*` level **unchanged**. Fifteen premise caveats compose to eleven; two absorptions
are restored (route non-independence; the excluded fitted law) and R-C4 amended to name three
proposer-level bridges rather than one, giving a thirteen-caveat root set. Verdict: **route and node
to `CERTIFIED*`, conditional** on the lead adopting the `R_stab` repair — licence bound to
`sha256:0f927e64…` (R3 only) or `sha256:c6205671…` (R1+R2+R3) and to no other claim text — on the
thirteen-caveat set, and on five accuracy corrections being recorded. `PROVED` is refused and no
premise level change is licensed.
