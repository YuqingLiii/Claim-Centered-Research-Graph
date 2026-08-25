# k-Sum review-repair batch — R-A1-1, R-A1-3, R-B4-1, and the `goal → B4` re-typing

**Date:** 2026-07-30 · **Role:** executor (Opus subagent) · **Scope:** the four repairs queued
behind tier T2 in `ksum/notes/ksum_lean_campaign_state_20260730.md` ("QUEUED BEHIND T2",
items 1–3, plus the header block of item 4).
**Primary node:** `KSUM.A1`; also touched `KSUM.A1a`, `KSUM.A1c`, `KSUM.B4`, `KSUM.goal`.
**Licences consumed:** `ksum/artifacts/ksum_composition_layer_review_20260730.md` §3.1 (R-A1-1,
R-A1-3), §3.4 (R-B4-1), §5.4 (`goal → B4` ENDORSED).
**Evidence:** `ksum/artifacts/logs_ksum_lean_repair_20260730/` (`build.log`, `print_axioms.txt`,
`SHA256SUMS.txt`).

---

## 0. PRE-ACTION REPORT (per `research/PRETASK_RELOAD_PROMPT.md`)

Read from disk before any work, in order: `DAG_PROTOCOL.md` (whole file; §2 ladder, §3
rules 1–8, §4–§6, §7.1–§7.10), `research/RESEARCH_STRUCTURE_PROTOCOL.md`, `ksum/README.md`,
the header of `ksum/notes/KSUM_PROOF_DAG.md`, `ksum/proof-dag/NODE_INDEX.md`,
then `KSUM.A1.yaml`, `KSUM.A1a.yaml`, `KSUM.A1c.yaml`, `KSUM.B4.yaml`, `KSUM.goal.yaml`, the campaign-state
ledger, review §§3.1/3.4/5.4, and T2 report §§3/5/6.

- **Target node and status as read from disk:** `KSUM.A1`, **CONJECTURED**
  (`status_source: recomputed-2026-07-30 under DAG_PROTOCOL.md §1`). Also read: `KSUM.A1a` PROVED
  (legacy-mirror), `KSUM.A1c` PROVED (legacy-mirror), `KSUM.B4` OPEN, `KSUM.goal` OPEN (root).
- **Role:** executor. Not a reviewer; this batch opens no review gate.
- **Highest status my evidence could license (§2):** **NUMERICAL**, with a `pending-review:`
  marker — a green `lake build` is a *run* (command + log + SHA), and §7.1 says a mechanization
  attribute never promotes a node by itself. Who may write it: the proposer, i.e. me, and only at
  that tier. **The PROVED on `KSUM.A1` that review §3.1 licenses may NOT be written by me**
  (rule 2: proposer ≠ checker; rule 6: the write cites the review and belongs to the lead after
  verifying the repairs match the prescription).
- **Gates / deliverables, one line each.**
  1. `A1a`/`A1c` Claim restatement (prose + Lean) + `A1` composition re-closed against the
     repaired Claims + `claim_hash` and `lean:` blocks re-synced (§7.6).
  2. `KSUM/B4.lean` vacuity fix: restrict `B4bClaim`'s `q`-quantifier to the paper's matching
     regime.
  3. `goal → B4` re-typed `children → related`, applied atomically across frontmatter, prose,
     Mermaid and the Lean import graph.
  4. Rebuild (exit 0, zero warnings, zero `sorry`/`axiom`/`native_decide`), `#print axioms`
     manifest, this artifact, the log directory, node updates, view sync, both validators exit 0,
     campaign ledger updated.
- **Conflicts between the commission text and the disk:** **one, cosmetic, reported not resolved.**
  The commission says T2 §6 writes the generalized core as "core constant `U` on the first `k−3`
  entries, last entry `U + r` where `t = t₀ + r`". The disk (T2 report §6, and §3's `lem:core` row)
  writes the last entry as `t − (k−3)U`. These are the same object: `t = t₀ + r = (k−2)U + r`, so
  `t − (k−3)U = U + r`. I implemented the disk form and record the identity here. No other
  conflict; in particular the disk's status ladder and rule-2 constraint agree with the
  commission's "you may NOT write PROVED on KSUM.A1 yourself".

---

## 1. PER-ITEM OUTCOME

| # | Item | Outcome | Where |
|---|---|---|---|
| 1a | `KSUM.A1a` prose Claim widened (parked coordinate + every window target) | **DONE** | `nodes/KSUM.A1a.yaml` §Claim; hash `d9b25ae9… → 5a70591b…` |
| 1b | `KSUM/A1a.lean` `Claim` restated in the every-window-target form | **DONE** | `KSUM/A1a.lean` |
| 1c | The generalization arithmetic **implemented** (not merely stated) | **DONE — IMPLEMENTED, sorry-free** | `KsumAudit/T2KFloor.lean` `core_reduction_at`, `sum_coreIdxAt`, `coreVecAt`, `coreVecAt_zero`; `KSUM.A1a.holds` |
| 1d | `KSUM/A1c.lean` `Claim` restated as the coset-covering form and wired from `Q_window_cover` | **DONE**, and *proved* (`holds`, `C = 2`) | `KSUM/A1c.lean` |
| 1e | `KSUM.A1c` prose Claim updated to match | **DONE** | `nodes/KSUM.A1c.yaml`; hash `049957e5… → ed56ed4d…` |
| 1f | `not_reachable_k3_q21` + the old all-pairs statement kept as a documented non-Claim relic | **DONE** | `KSUM.A1c.ClaimAllPairs` (docstringed as the refuted rendering), `not_reachable_k3_q21`, `k3_q21_in_range` all retained |
| 1g | `KSUM/A1.lean` `composition` **re-proved** against the repaired child Claims | **DONE** (re-proved, not patched) | `KSUM/A1.lean` |
| 1h | `claim_hash` + `lean:` blocks re-synced on A1, A1a, A1c | **DONE** | three node files; no new hash-drift warning from the checker |
| 2 | `KSUM/B4.lean` vacuity fix (R-B4-1) | **DONE** — `q` odd, `5 ≤ q ≤ N` | `KSUM/B4.lean`; `nodes/KSUM.B4.yaml` lean block + caveat updated |
| 3 | `goal → B4` re-typed to `related`, atomically | **DONE** — frontmatter, prose, `related`, Mermaid `G -.-> B4`, `import KSUM.B4` removed from `KSUM/goal.lean` | `nodes/KSUM.goal.yaml`, `nodes/KSUM.B4.yaml`, `KSUM_PROOF_DAG.md`, `KSUM/goal.lean`, `KSUM/Trust.lean` |
| 4 | Rebuild + axioms + artifact + logs + node updates + views + validators + ledger | **DONE** | this file and the log directory |

**Nothing resisted.** No item was downgraded to "stated", no proof was reshaped to make it compile,
and no hypothesis was added to any statement to make it provable (the one hypothesis *change* — the
range condition on `A1c.Claim` — is analysed in §3.2 below and is weaker in the direction that
matters).

### 1.1 The A1a generalization: IMPLEMENTED

T2 left this as the one narrowing on the `A1` branch: `core_reduction` was proved at the base
window target `t₀ = (k−2)(kK+1)` only. It is now proved at every window target.

- **New definition** `KsumAudit.KFloor.coreVecAt k κ q m r` — the manuscript's core at
  `t = t₀ + r`: `c_i = U = kK+1` for `i ≤ k−3`, `c_{k−2} = t − (k−3)U = U + r`, and (when
  `m = k−1`) the parked value `v = t + (k−1)K + 1 = parkedVal + r`.
- **New theorems** `sum_coreIdxAt` (`lem:core` at a general window target: the core sums to
  `t₀ + r`) and `core_reduction_at` (`prop:core-even` + `lem:core-odd` at every window target,
  `r < k`).
- **`coreVecAt_zero : coreVecAt … 0 = coreVec …`**, so the T2 statement is recovered exactly:
  `core_reduction` is now a two-line corollary at `r = 0` **with its original statement byte for
  byte**, and T2's four `witness_*` non-vacuity checks are untouched.
- **What changed in the proof, precisely.** The forward direction's core-sum bookkeeping gains one
  filter split: inside `A` (the used genuine-core positions) the last position `k−3` carries
  `U + r` instead of `U`, so `Σ_A c = a·U + ε·r` with `ε = |A ∩ {k−3}| ∈ {0,1}`, and the parked
  contribution becomes `b·(v + r)`. The divisibility takes the shape
  `q ∣ Z + (a + (b−1)(k−2))·U + (ε + b − 1)·r + b·((k−1)K+1)`. The three case bounds then need
  `(k−2)U + r + 2(k−1)K + 2 ≤ q`, and `ε = 1` is *forced* in the good pattern (`a = k−2` means the
  whole core is used, so the last position is in it) — that is what keeps the good pattern's
  conclusion exactly `q ∣ Z`, i.e. the live pair still sums to `0`.
- **The window hypothesis did not have to move, and the reason is worth recording.** Expanding
  `(k−2)U + (k−1) + 2(k−1)K + 2` gives exactly `(k²−2)K + 2k−1` — the manuscript's own odd-window
  threshold. So `(k²−2)K + 2k−1 ≤ q` *is* the master inequality at the rightmost window target
  `r = k−1`, tight there, and every window target `r < k` is covered by the same hypothesis. This
  also explains, rather than assumes, why `lem:core-odd` and `lem:transl-cover`(ii) carry the same
  threshold in the manuscript.

---

## 2. THE NEW CLAIM TEXTS, SIDE BY SIDE WITH THE REVIEW PRESCRIPTIONS

### 2.1 `KSUM.A1a`

**Review prescription (R-A1-1, §3.1):** *"it must be fixed by widening `A1a`'s frozen Claim to
'a frozen core of `k−2` coordinates, plus the parked coordinate when `N−(k−2)` is odd', or by
adding the odd branch as an explicit `rel` entry citing `lem:core-odd`."*
**Review prescription (R-A1-3, §3.1):** *"state `A1a` for every window target rather than for an
existential `t₀`."*

| | Text |
|---|---|
| **Before** | `freeze k−2 coords: CONSTANT C₀=⌊q/(k−1)⌋ (as authored) OR positive CORE summing to t / (kills all d≥1 bad patterns) [PROVED — both variants F1-verified]` |
| **After** | `freeze a core of k−2 coords: CONSTANT C₀=⌊q/(k−1)⌋ (as authored) OR positive CORE summing to the target (kills all d≥1 bad patterns), PLUS the parked coordinate v=t+(k−1)K+1 when N−(k−2) is odd; valid at EVERY window target t ∈ [t₀, t₀+k) with t₀=(k−2)(kK+1), not merely at one [PROVED — both variants F1-verified; widened 2026-07-30 per review R-A1-1/R-A1-3]` |

**Lean `Claim`, before → after** (the load-bearing difference is `∃ t₀` → `∀ s` in the window):

```lean
-- before
∀ (k q n m κ : ℕ) [NeZero q], 3 ≤ k → k-2 ≤ m → m ≤ k-1 → 2 ≤ κ →
  (k^2-2)*κ + 2*k-1 ≤ q → 2 ≤ n →
    ∃ t₀ : ZMod q, ∃ c : Fin m → ZMod q, ∀ y, kSum … t₀ … = twoSum … 0 …

-- after
∀ (k q n m κ s : ℕ) [NeZero q], 3 ≤ k → k-2 ≤ m → m ≤ k-1 → 2 ≤ κ →
  (k^2-2)*κ + 2*k-1 ≤ q → 2 ≤ n →
  KFloor.baseTarget k κ ≤ s → s < KFloor.baseTarget k κ + k →
    ∃ c : Fin m → ZMod q, ∀ y, kSum … ((s : ℕ) : ZMod q) … = twoSum … 0 …
```

Quantifier check against the standing failure-mode list: the target moved from **existential** to
**universal over the window** (strictly stronger Claim, which is the direction that makes the
composition *safer*, and it is proved); `m ∈ {k−2, k−1}` (the parked coordinate) was already
present and is retained; no hypothesis was added or weakened; the residual target stays `0`.

### 2.2 `KSUM.A1c`

**Review prescription (R-A1-3, §3.1):** *"state `A1c` as the coset-covering statement ('for every
`t` there is a window target `t′ ∈ t+kZ_q` with `Q(kSum_t) ≥ Q(kSum_{t′})/C`')."*

| | Text |
|---|---|
| **Before** | `target coverage: window family + translation identity / k-Sum_t(x)=k-Sum_{t+ka}(x+a·1), all t via gcd argument, no parity cond. [PROVED]` |
| **After** | `target coverage, COSET-COVERING form: window family + translation identity / k-Sum_t(x)=k-Sum_{t+ka}(x+a·1); for EVERY target t there is a window target t′ ∈ t+kZ_q with Q(kSum_t) ≥ Q(kSum_{t′})/C for one absolute constant C — no parity and no coprimality condition [PROVED — restated 2026-07-30 per review R-A1-3; the earlier all-pairs-of-targets rendering is NOT what lem:transl-cover proves and is kept only as a refuted relic]` |

```lean
-- before  (now retained, unproved and unconsumed, as `ClaimAllPairs`)
∃ C > 0, ∀ (k N q : ℕ) [NeZero q], 3 ≤ k → 2*k^2+2*k-5 ≤ q →
  ∀ t₀ t : ZMod q, M.Q (kSum … t₀ N) ≤ C * M.Q (kSum … t N)

-- after   (`Claim`, PROVED by `holds` with C = 2)
∃ C > 0, ∀ (k N q κ : ℕ) [NeZero q], 3 ≤ k → (k^2-2)*κ + 2*k-1 ≤ q →
  ∀ t : ZMod q, ∃ (a : ZMod q) (s : ℕ),
    KFloor.baseTarget k κ ≤ s ∧ s < KFloor.baseTarget k κ + k ∧
      ((s : ℕ) : ZMod q) = t + k • a ∧                       -- the COSET membership
      M.Q (kSum … ((s:ℕ) : ZMod q) N) ≤ C * M.Q (kSum … t N) -- i.e. Q(kSum_t) ≥ Q(kSum_s)/C
```

Three things the standing failure-mode list says to check, checked:

- **the `/C` constant is not dropped** and its direction is unchanged
  (`Q(kSum_s) ≤ C·Q(kSum_t)` ⟺ `Q(kSum_t) ≥ Q(kSum_s)/C`); it is moreover *pinned* to `2` by the
  proof, and `2` is one application of `sec:prelim` fact (ii) — **the absolute factor 2 of fact
  (ii) is not lost anywhere in this batch**;
- **the coset membership is in the statement**, not only in the proof (`s = t + k·a`). This is the
  clause whose absence produced the refuted all-pairs form, so burying it in a proof would have
  reproduced the defect one level down;
- **no coprimality hypothesis was smuggled in.** Coverage runs off the window length
  `≥ k ≥ gcd(k,q)` (Bézout, `exists_shift_into_window`), exactly as `lem:transl-cover` argues.

### 2.3 `KSUM.B4` (R-B4-1)

**Review prescription (§3.4):** *"restrict both the claim and `B4bClaim` to the non-degenerate
window in which the exponent question lives — at minimum `q ≥ 5`, and per S5 the intersection of
the two sides' scopes, `G = Z_q` with `q` odd and `N ≥ q`."*

**Chosen range: `Odd q → 5 ≤ q → q ≤ N`,** applied to `B4bClaim` and to the matching half of
`Claim`, inside the shared quantifier. Why this one:

1. it is the regime of `thm:main-odd`, which is where the paper's matching claim lives;
2. it is the intersection of the two sides' scopes — every registered `B4b` route (`M1`, the `L2`
   group) is stated for odd `q` with `N ≥ q`, while `B4a` holds for all `q`, so the restriction
   costs the upper side nothing;
3. `q ≤ N` keeps the statement inside the small-alphabet window this problem is about.

**What it fixes:** the reviewer's unsatisfiability witness (`q = 2, t = 0, N ≥ 3`: pigeonhole gives
`x_i = x_j`, `2x_i = 0` in `Z_2`, so `2Sum ≡ true`, `Q = 0`, while the claim demanded
`c·√N·2^{1/4} > 0`) is now out of scope, so `KSUM.B4.composition` is no longer vacuous in the
intended interpretation. **What it does NOT establish:** that `B4bClaim` is *satisfiable* in the
restricted regime — that is the open `B4b` lower bound itself; no model was exhibited and none is
claimed. **Still owed (recorded on the node):** the *prose* half of R-B4-1 — the frozen
`composition.claim` on `KSUM.B4.yaml` still states no `q`-range. Rewriting a reviewed frozen claim is
a decision-layer write, so it is left as an Open obligation with the intended text spelled out.

### 2.4 `goal → B4` (§5.4)

**Review prescription:** *"Re-type to `related`. Consequences the lead must apply in the same diff:
GOAL's `children` becomes `[B1, B2, B3]`; `B4`'s `parents` becomes `[]`; the root's `max` is
unaffected (it was `OPEN` on every route); and the Mermaid edge `G --> B4` becomes dotted."*

All four applied, plus the Lean consequence §7.6 check 6 requires: `import KSUM.B4` removed from
`KSUM/goal.lean`. Nothing else in `goal.lean` referenced `B4` (the module is deliberately
theorem-free; its only other import is `KSUM.B2`). `KSUM.B4` stays in the build — `lakefile.lean`
globs `.submodules KSUM` — and remains in the axiom manifest because `KSUM/Trust.lean` now imports
it directly. The retired route entry is **not deleted**: it is kept verbatim in `KSUM.goal.yaml`'s
frontmatter under the renamed key `KSUM.B4_RETYPED_2026-07-30`, with `status: RETIRED-EDGE` and the
review citation (append-only, rule 4).

---

## 3. THE `KSUM.A1` COMPOSITION, RE-PROVED

The old machine proof consumed `A1c.Claim` in its all-pairs form (`hlift k N q hk hq0 t₀ t`), which
is exactly the premise the review refuted. It could not be patched; the argument was re-ordered
into the manuscript's own order.

```
0. A1c (coset covering)   for the given t: a shift a and a WINDOW target s = t + k·a ∈ [t₀,t₀+k)
                          with Q(kSum_s) ≤ C·Q(kSum_t)                       ← chosen by covering
1. A1a (every window tgt) a frozen core c at THAT s, turning kSum_s into 2Sum at 0 on the codewords
2. A1b (encoding)         2Sum at 0 through E is Claw_{n→κ}
3. transfer               facts (i)+(ii) cost the absolute factor 2; freezing costs nothing (F1)
4. arithmetic             tani: c_ABI·√n·κ^{1/6} ≤ Q(Claw) ≤ 2·Q(kSum_s) ≤ 2C·Q(kSum_t);
                          combine_bound converts (n,κ) → (N,q) via N ≤ 3n and q ≤ 2k²κ
```

The direction of step 0 is the whole repair: the window target is produced by the covering
argument, not chosen by `A1a`. Constants unchanged and still exhibited: `C_k = 1`, `c_k = 1/2`,
`N₀ = 40k+40`, `A = c_ABI/(2·C·√3·(2k²)^{1/6})`, `B = A·(1/2)^{1/6}`, with `C = 2` now *pinned*
rather than existential.

**Non-vacuity — finding F-R8 is CLOSED, not narrowed.** All three child Claims are now theorems
(`KSUM.A1a.holds`, `KSUM.A1b.holds`, `KSUM.A1c.holds`), so they are jointly satisfiable for every
`M`, and the optional `holds : Claim` of §7.4 exists:

```lean
theorem holds (M : QueryModel) : Claim M :=
  composition M KSUM.A1a.holds KSUM.A1b.holds (KSUM.A1c.holds M)
```

`KSUM.A1.Claim` (= `KSUM.A1d.Claim`) therefore holds **relative to the `QueryModel` interface and
nothing else**: `M.tani` is ABI21/Tani24 on trust, `M.restrict`/`M.relabel` are `sec:prelim` facts
(i)/(ii), `M.freeze` is the unstated coordinate-freezing principle F1. A theorem proved against an
abstract interface is exactly as strong as the results that interface cites, and not one notch
stronger.

### 3.1 F-R13 trap check (a range hypothesis STRONGER than the prose ⇒ vacuous composition)

The one hypothesis that changed is `A1c.Claim`'s range condition: the floor `2k²+2k−5 ≤ q` became
the κ-indexed window `(k²−2)κ + 2k−1 ≤ q`. Audited in both directions:

- **Is it stronger than the manuscript's?** No — it *is* the manuscript's: `lem:transl-cover`(ii)
  is stated under exactly this condition, and the earlier floor was a paraphrase inherited from
  `A1d`'s window.
- **Does it make the composition vacuous?** No, and this is now machine-checked rather than
  argued: `A1c.Claim` is *proved*, so it has no vacuity mode at all, and `A1`'s composition
  establishes the hypothesis for its own choice of `κ = ⌊(q−2k+1)/(k²−2)⌋` before using it.
- **Does it lose any modulus?** No: `2 ≤ κ` together with that window is *equivalent* to
  `q ≥ q₀(k) = 2k²+2k−5`, which is `A1d`'s window floor. (Machine-checked at the boundary by
  `KsumAudit.KFloor.witness_q0_three`: at `k=3, κ=2` the threshold is exactly `19 = q₀(3)`.)

### 3.2 What was NOT done, deliberately

- **No status was promoted.** `KSUM.A1` still reads CONJECTURED, `composition.status` still reads
  CONJECTURED. Review §3.1's PROVED licence is now unconditional in its own terms, and that write
  is queued for the lead (rule 2). It is recorded as an Open obligation on the node, with the exact
  transition spelled out.
- **`A1a`/`A1c` epistemic statuses were not touched** (both stay PROVED, from their 2026-07-18/19
  reviews of the manuscript propositions). What moved is the *text* of their Claims and their
  `lean.state`. Both nodes now carry an explicit flag that **no reviewer has read the new text**,
  addressed to `KSUM.LEAN.statement-fidelity`.
- **Whether `ClaimAllPairs` is FALSE (rather than merely underivable) is still open.** Settling it
  needs a `QueryModel` separating the two target orbits at `k=3, q=21` while satisfying
  `restrict`, `relabel`, `freeze`, `constQ`, `abi`, `tani`. Nothing now depends on the answer, and
  no attempt was made.
- **No new nodes were created**, no other node's status was touched, and no `git` command was run.

---

## 4. BUILD COMMAND, RESULT, AND EVIDENCE

```
cd ksum/proof-dag/lean
lake build
→ Build completed successfully (3011 jobs)
→ BUILD_RESULT: exit=0
```

- Full transcript: `ksum/artifacts/logs_ksum_lean_repair_20260730/build.log` (217 lines, ends with the
  `BUILD_RESULT` line; both libraries, `KsumAudit` and `KSUM`).
- **Hygiene, both libraries:** `sorry` **0**, `axiom` declarations **0**, `native_decide` **0**,
  `implemented_by` **0**, build warnings **0**, errors **0**. (Every textual match for those words
  in the sources is inside a docstring or comment saying there are none; verified line by line.)
- **`#print axioms` manifest:** `ksum/artifacts/logs_ksum_lean_repair_20260730/print_axioms.txt` —
  **176 declarations printed, 0 outside `{propext, Classical.choice, Quot.sound}`.**
  Diff against `ksum/artifacts/logs_ksum_lean_T2_20260730/build.log`: **8 added, 0 removed** —
  `KSUM.A1.holds`, `KSUM.A1a.holds_base`, `KSUM.A1c.ClaimAllPairs`,
  `KSUM.A1c.Q_window_cover_coset`, `KSUM.A1c.holds`, `KsumAudit.KFloor.coreVecAt_zero`,
  `KsumAudit.KFloor.core_reduction_at`, `KsumAudit.KFloor.sum_coreIdxAt`.
  *Counting convention, made explicit because it differs from T2's:* 176 counts every record,
  including the 6 axiom-free ones; under T2's narrower convention (records carrying an axiom list)
  this run is 170 and the T2 log re-parsed is 168 against its reported 162 — the same 6-record
  offset, so the two runs are consistent.

### 4.1 `#print axioms` for the declarations this batch created or changed

```
KsumAudit.KFloor.coreVecAt_zero        propext, Quot.sound
KsumAudit.KFloor.sum_coreIdxAt         propext, Classical.choice, Quot.sound
KsumAudit.KFloor.core_reduction_at     propext, Classical.choice, Quot.sound
KsumAudit.KFloor.core_reduction        propext, Classical.choice, Quot.sound
KsumAudit.KFloor.sum_coreIdx           propext, Classical.choice, Quot.sound
KSUM.A1a.Claim                         propext, Classical.choice, Quot.sound
KSUM.A1a.holds                         propext, Classical.choice, Quot.sound
KSUM.A1a.holds_base                    propext, Classical.choice, Quot.sound
KSUM.A1a.frozen_form                   propext, Classical.choice, Quot.sound
KSUM.A1c.Claim                         propext, Classical.choice, Quot.sound
KSUM.A1c.ClaimAllPairs                 propext, Classical.choice, Quot.sound
KSUM.A1c.holds                         propext, Classical.choice, Quot.sound
KSUM.A1c.Q_window_cover_coset          propext, Classical.choice, Quot.sound
KSUM.A1c.Q_window_cover                propext, Classical.choice, Quot.sound
KSUM.A1c.Q_kSum_translate_le           propext, Classical.choice, Quot.sound
KSUM.A1c.Q_le_of_coprime               propext, Classical.choice, Quot.sound
KSUM.A1c.not_reachable_k3_q21          propext, Classical.choice, Quot.sound
KSUM.A1c.k3_q21_in_range               propext
KSUM.A1.Claim                          propext, Classical.choice, Quot.sound
KSUM.A1.composition                    propext, Classical.choice, Quot.sound
KSUM.A1.holds                          propext, Classical.choice, Quot.sound
KSUM.B4.B4bClaim                       propext, Classical.choice, Quot.sound
KSUM.B4.Claim                          propext, Classical.choice, Quot.sound
KSUM.B4.composition                    propext, Classical.choice, Quot.sound
```

### 4.2 Changed Lean sources

| File | Change |
|---|---|
| `KsumAudit/T2KFloor.lean` | `coreVecAt`, `coreVecAt_zero`, `sum_coreIdxAt`, `core_reduction_at` added; `core_reduction` becomes the `r = 0` corollary with its statement unchanged; witnesses untouched. |
| `KSUM/A1a.lean` | `Claim` restated (every window target); `holds` re-proved from `core_reduction_at`; `holds_base` added; `frozen_form` updated; header, PROSE↔Claim diff, and `claim_hash` re-synced (old text + old hash kept). |
| `KSUM/A1c.lean` | `Claim` restated (coset covering) and PROVED (`holds`); `Q_window_cover_coset` added and `Q_window_cover` derived from it; `ClaimAllPairs` retains the refuted rendering; header box rewritten as defect + repair; `claim_hash` re-synced (old text + old hash kept). |
| `KSUM/A1.lean` | `composition` re-proved against the repaired Claims (cover first, then freeze); `holds` added; header steps and non-vacuity box updated. |
| `KSUM/B4.lean` | `B4bClaim` and `Claim` restricted to `q` odd, `5 ≤ q ≤ N`; `composition` updated; docstrings record the vacuity and the choice of regime. |
| `KSUM/goal.lean` | `import KSUM.B4` removed (§7.6 check 6); route table records the re-typing. |
| `KSUM/Trust.lean` | `import KSUM.B4` added so the module stays in the manifest; census (c) rewritten (F-R8 closed, the three repairs); T2 table rows updated to FAITHFUL where the repair closed the narrowing; 8 new `#print axioms` lines. |

---

## 5. STANDING FAILURE-MODE LIST (rule 7e) — how each was handled

- **Quantifier drift.** The two directions the commission named were checked explicitly and are
  recorded in §2: `A1a` did **not** weaken back to existential-in-`t₀` (it is `∀ s` in the window,
  and the Lean type shows it); `A1c` kept **both** the `/C` constant and the coset membership, the
  latter promoted from a proof step into the statement.
- **Hypotheses smuggled into definitions.** `coreVecAt`, `coreUnit`, `baseTarget`, `parkedVal` are
  total and hypothesis-free; every constraint (`3 ≤ k`, `k−2 ≤ m ≤ k−1`, the window, `r < k`) lives
  in a theorem binder.
- **The F-R13 trap (range hypothesis stronger than the prose ⇒ vacuous composition).** Audited in
  §3.1 for the one hypothesis that changed, in both directions, with the equivalence
  `2 ≤ κ ∧ window ⟺ q ≥ q₀(k)` re-derived.
- **Dropped normalization factors, in particular the absolute factor 2 of fact (ii).** It survives
  in three places and is pinned rather than existential: `Q_kSum_translate_le` (the single
  application the manuscript uses), `A1c.holds`'s `C = 2`, and `A1.composition`'s
  `Q(Claw) ≤ 2·Q(kSum_s)` from `relabel_inj`. The composition's constants were recomputed with
  `C = 2` and are unchanged in form.
- **Vacuity / satisfiability.** Improved on two nodes and stated honestly on the third:
  `A1.composition` is now provably non-vacuous (all premises are theorems); `B4.composition`'s
  *unsatisfiable* regime is excluded, but satisfiability in the restricted regime is **not**
  established and is not claimed.
- **Numerics validating values while the derivation is broken.** Not applicable — nothing here is
  numerical; the four `core_reduction` witnesses continue to be `decide`d *through* the theorem.

---

## 6. VIEWS, VALIDATORS, LEDGER

- Node files updated with dated Work record + Evidence entries (rule 8c): `KSUM.A1.yaml`,
  `KSUM.A1a.yaml`, `KSUM.A1c.yaml`, `KSUM.B4.yaml`, `KSUM.goal.yaml`. **No status write above
  NUMERICAL·pending-review, and none at all on any node not repaired here.** (In fact no epistemic
  status was written at all: the repairs changed Claim texts, mechanization states, and edges.)
- `NODE_INDEX.md`: Lean column updated for `A1a`, `A1c`, `A1`; edge notes added to the `G` and
  `B4` rows. Node count unchanged (142; no node was created or removed by this batch).
- `KSUM_PROOF_DAG.md`: new "Most recent change" block prepended (the T2 block becomes "Previous
  change"); Mermaid `G --> B4` → `G -.-> B4` with a "RELATED, NOT A ROUTE" label; the `A1a` and
  `A1c` Mermaid labels and outline bullets re-synced to the new Claims.
- Validators: `python tools/proof_dag_check.py --problem ksum` → **exit 0**;
  `python tools/literature_check.py` → **exit 0** (interpreter
  `<machine-local-path-redacted>`). Pre-existing warnings unrelated
  to this batch (the `migration_status` block, plus frozen-Claim hash drift on `KSUM.A2b` and
  `KSUM.B1`) are unchanged; **no new warning was introduced, and in particular no hash-drift
  warning for `A1a`/`A1c`, which is the mechanical check that the re-sync worked.**
- `ksum/notes/ksum_lean_campaign_state_20260730.md`: queue items 1–3 marked done.

---

## 7. WHAT THE LEAD IS OWED NEXT

1. **The review-licensed promotion of `KSUM.A1`** (rule 2, the executor may not write it): verify
   that the repairs above match review §3.1's prescription, then set `composition.status` and
   `status` to PROVED citing review §3.1 + this batch. Recomputation after that write:
   `status(A1) = min(PROVED, A1a=PROVED, A1b=PROVED, A1c=PROVED, A1d=PROVED) = PROVED`.
2. **The prose half of R-B4-1** — restrict the frozen `composition.claim` on `KSUM.B4.yaml` to the
   same regime (intended text is on the node).
3. **Statement-fidelity review coverage of the two new Claim texts** (`A1a`, `A1c`) — flagged as an
   Open obligation on both nodes for `KSUM.LEAN.statement-fidelity`.
4. Unchanged from T2: `prop:rosmanis` has no DAG node (rule-8a decision), the `demoEmbed` witness
   for `KSUM.Support.EmbedData` (R-A2-3) is still undone, and `KSUM.LEAN.yaml`'s "Current status"
   paragraph still describes T2 as OPEN (queue item 0, out of this batch's file ownership).
