# k-Sum Lean audit — tier T2: the Rosmanis barrier and the `k`-floor cores

**Node:** `KSUM.LEAN.T2.rosmanis-kfloor` · **Date:** 2026-07-30 · **Role:** executor (Opus 5)
**Lean project:** `ksum/lean/` (Lean `v4.31.0`, Mathlib `v4.31.0`)
**Evidence:** [`ksum/artifacts/logs_ksum_lean_T2_20260730/`](logs_ksum_lean_T2_20260730/)
(`build.log` with `BUILD_RESULT: exit=0`, `print_axioms.txt`, `SHA256SUMS.txt`)

---

## 0. PRE-ACTION REPORT

- **Target node and its status as read from disk:** `KSUM.LEAN.T2.rosmanis-kfloor`, **OPEN**
  (`status_source: rule8a-registration-2026-07-30`). Parent `KSUM.LEAN` is an AND node at OPEN.
- **Role:** executor. Not a reviewer; nothing here opens a completion gate.
- **Highest status my planned evidence could license (§2):** **NUMERICAL**, proposer-writable,
  carrying an explicit `pending-review:` marker. A green Lean build is a run (command + log +
  SHA), so by `DAG_PROTOCOL.md` §2 and §7.1 it caps at NUMERICAL; a completion tier on this node
  requires `KSUM.LEAN.statement-fidelity` to complete under rules 6 and 7, and would be written by
  the independent reviewer, not by me.
- **Gates and deliverables, one line each:**
  - G-T2a — is `KSUM.A1a.Claim` proved `sorry`-free?
  - G-T2b — is `KSUM.A1c.Claim` proved `sorry`-free?
  - G-T2c — is `prop:rosmanis`(1) proved, and in the orbit-proper or the invariant-class form?
  - G-T2d — does every new theorem have a compiling non-vacuity witness?
  - G-T2e — is `#print axioms` clean (Lean's three standard axioms only) for every new theorem?
  - Deliverables: Lean sources built green; this artifact; the log directory; node/index/DAG-view
    updates; both validators exit 0; the campaign-state ledger moved from IN FLIGHT to DONE.
- **Conflicts between the commission and the disk:** **two, both reported rather than resolved.**
  1. The commission's deliverable 2 ("prove `KSUM.A1c.Claim`") was superseded mid-flight by a lead
     advisory citing finding **R-A1-3** of the concurrent composition-layer review
     (`ksum/artifacts/ksum_composition_layer_review_20260730.md`): the Claim is an over-strong rendering
     and must not be proved or reshaped. I had reached the same conclusion independently before the
     advisory arrived (§5 below records both derivations).
  2. **Scope discrepancy inside that advisory, reported per "disk is authoritative".** The review's
     witness is `k = 3, q = 3`. `Claim`'s own range hypothesis is `2k²+2k−5 ≤ q`, which at `k = 3`
     reads `19 ≤ q`, so `q = 3` does **not** satisfy it. R-A1-3 therefore refutes the *prose* claim
     and the pre-window form, but does not by itself falsify the Lean `Claim` as literally stated.
     I supply the in-range obstruction (`k = 3, q = 21`) below.
- **Ownership respected:** I wrote only `KsumAudit/T2KFloor.lean`, `KsumAudit/RosmanisBarrier.lean`,
  `KsumAudit.lean` (import list + header), `KSUM/A1a.lean`, `KSUM/A1c.lean`, `KSUM/Trust.lean`, the
  `lean:` blocks of `KSUM.A1a.yaml` / `KSUM.A1c.yaml`, my own node file, the `LeanT2` row/label/entry of
  `NODE_INDEX.md` and `KSUM_PROOF_DAG.md`, and the artifact/log files. `KSUM/A1b.lean` needed no
  edit (see §4). No `git` command was run.

---

## 1. GATE TABLE

| Gate | Verdict | Detail |
|---|---|---|
| **G-T2a** — `A1a.Claim` proved `sorry`-free | **PASS** | `KSUM.A1a.holds`, **unconditional** (no `QueryModel` argument). Mathematics: `KsumAudit.KFloor.core_reduction` = `prop:core-even` + `lem:core-odd` in one statement, covering both `m = k−2` and `m = k−1`. Both of `Claim`'s unused hypotheses (`2 ≤ κ`, `2 ≤ n`) are *not* consumed, so the proved identity is strictly stronger than `Claim` demands. |
| **G-T2b** — `A1c.Claim` proved `sorry`-free | **FAIL-BY-CLAIM-DEFECT** | The Claim is unprovable as frozen: it is the all-pairs-of-targets form, while `lem:transl-cover` is coset-local. Cited: **R-A1-3** of `ksum/artifacts/ksum_composition_layer_review_20260730.md`, plus my independent derivation and the in-range machine-checked obstruction `KSUM.A1c.not_reachable_k3_q21`. The faithful content IS proved: `Q_kSum_translate_le`, `Q_window_cover`, `Q_le_of_coprime`, `window_even_length`, `window_odd_length`, `exists_shift_into_window`. Per the advisory, the Claim was neither proved nor reshaped. |
| **G-T2c** — `prop:rosmanis`(1) proved; which rendering? | **PASS (partial scope), ORBIT-PROPER** | The load-bearing half — *"`D₀` is never a single orbit"*, i.e. the count is `≥ 2`, in both manuscript branches — is proved **in the orbit-proper sense**: the `S_N × C(σ)` action is defined, shown to preserve `D₀` (`isNegative_act`), and the separating invariant is **proved invariant** (`valueCount_act`), so `not_single_orbit` is a statement about genuine orbits, not about values of an unjustified invariant. **The exact bijection `orbits ↔ {(f,λ)}` and the count formula `Σ_f p_{≤m}(N−f)` are NOT formalized** — declared, not omitted. |
| **G-T2d** — non-vacuity witness for every new theorem | **PASS** | 6 witnesses in `T2KFloor` (`witness_q0_three`, `witness_coreUnit`, `witness_even_pos/neg`, `witness_odd_pos/neg` — each of the last four a `decide`d Boolean VALUE, positive and negative, at the smallest legal instance `k=3, κ=2, q=19`), 6 in `RosmanisBarrier` (`existence_fails_q3`, `swapped_string_q3`, `uniqueness_fails_q5`, `q5_cycle_type`, `witness_two_cycles_q5`, `witness_one_cycle_q3`), 2 in `A1c` (`not_reachable_k3_q21`, `k3_q21_in_range`). |
| **G-T2e** — `#print axioms` clean | **PASS** | 162 declarations printed in the full-project transcript, **0 outside `{propext, Classical.choice, Quot.sound}`** (several are proper subsets, which is cleaner still). 50 of them are T2-relevant. See `logs_ksum_lean_T2_20260730/print_axioms.txt`. Zero `sorry`, zero `axiom`, zero `native_decide`, zero build warnings. |

**Build:** `lake build` in `ksum/proof-dag/lean` → `Build completed successfully (3011 jobs)`,
`BUILD_RESULT: exit=0` (was 3009 before this run; +2 modules).

---

## 2. ENGLISH STATEMENTS, WRITTEN BEFORE FORMALIZING (rule 7c, anchoring ban)

These were written from the manuscript's *statements* — not from its proofs, and not from the
existing Lean — and then formalized. Quantifier order is as written here.

1. **`lem:core`.** *Fix `k ≥ 3` and `K ≥ 2`, put `U = kK+1`, and let `t ≥ (k−2)U`. Then each of the
   `k−2` core coordinates is at least `U`; the sum over any nonempty subset of the core lies in the
   integer interval `[U, t]`; and that sum equals `t` exactly when the subset is the whole core.*
2. **`prop:core-even`.** *Fix `k ≥ 3`, `K ≥ 2`, `q ≥ (k−1)(kK+1)`, and a target `t` with
   `(k−2)U ≤ t ≤ q−U`. Build the string from the `k−2` frozen core coordinates and the `2m` live
   coordinates. Then for EVERY live word `(f,g) ∈ {1,…,K}^{2m}`, `k`-Sum at `t` on the resulting
   `N = (k−2)+2m` coordinates equals `Claw_{m→K}(f,g)`.*
3. **`lem:core-odd`.** *Same, but with the strictly smaller ceiling `t ≤ q − 2(k−1)K − 2` and one
   extra "parked" coordinate of value `v = t + (k−1)K + 1`, giving `N = (k−2)+2m+1`; the identity
   is unchanged.*
4. **`lem:transl-cover`.** *(identity)* *For every `a`, `k`-Sum at `t` on `x` equals `k`-Sum at
   `t + ka` on `x + a·1`; hence the two query complexities agree up to absolute constants.*
   *(i)* *If `q ≥ (k−1)(kK+2)` then `W_even` contains at least `k ≥ gcd(k,q)` consecutive residues.*
   *(ii)* *If `q ≥ (k²−2)K + 2k−1` then so does `W_odd`.*
   *(covering)* *A window of at least `gcd(k,q)` consecutive residues meets every coset `t + kZ_q`;
   no coprimality hypothesis is used.*
5. **`prop:rosmanis`(1).** *Fix `(G,t)` with `σ(x) = t−x ≠ id` and `q ≥ 3`, let `τ` be the number of
   fixed points of `σ` and `m = (q−τ)/2`. For every `N ≥ 2`, the `S_N × C(σ)`-orbits on the negative
   set `D₀` are in bijection with pairs `(f, λ)`, `0 ≤ f ≤ min(τ,N)`, `λ ⊢ N−f` into at most `m`
   parts; the number of orbits is `Σ_f p_{≤m}(N−f)`, which is `≥ 2`; in particular `D₀` is never a
   single orbit.*
6. **`prop:rosmanis`(2).** *Regularity fails in two precise ways: existence fails at `q = 3`, `τ = 1`,
   `N = 2` (transposing the two positions of `(a,b)`, `a` the fixed point, is matched by no
   `ρ ∈ C(σ)`); uniqueness fails whenever `m ≥ 2` (for `N = 2`, `y = (a,a)` is fixed by the identity
   and by the side-flip of any other `2`-cycle). Consequently `C[D₀]` contains the trivial
   representation with multiplicity equal to the number of orbits, hence `≥ 2`, whereas the ED
   pattern contains it exactly once.*
7. **`prop:rosmanis`(3).** *If `τ = 0`, the positive-side building blocks — inputs whose collision is
   a repeated value — are empty, because `x_i = x_j = a` is a hit iff `a` is a fixed point.*

---

## 3. LaTeX label ↔ Lean name map, with fidelity verdicts

| LaTeX label | Lean name | File | Verdict |
|---|---|---|---|
| `lem:core` | `KsumAudit.KFloor.core_wellformed`, `KsumAudit.KFloor.sum_coreIdx` | `T2KFloor` | **NARROWER** — proved at the base target `t₀ = (k−2)U` only, where the last core entry `t−(k−3)U` collapses to `U`, not for every `t ≥ (k−2)U`. |
| `prop:core-even` | `KsumAudit.KFloor.core_reduction` (`m = k−2` branch) | `T2KFloor` | **NARROWER** — same restriction: the target is the left endpoint of `W_even`, not an arbitrary window target. Everything else (all `q`, all `k ≥ 3`, all `n`, all live words, both directions of the identity) is as stated. |
| `lem:core-odd` | `KsumAudit.KFloor.core_reduction` (`m = k−1` branch) | `T2KFloor` | **NARROWER**, same reason. The parked coordinate is present and load-bearing: `witness_odd_neg` is exactly the clause the two DEAD `sec:branch-ledger` variants failed. |
| `lem:transl-cover`, identity | `KSUM.A1c.kSum_translate` | `A1c` | **FAITHFUL** — proved for an arbitrary finite abelian group, hence at every parity of `q`, with no invertibility of `k`. |
| `lem:transl-cover`, `Θ` (query half) | `KSUM.A1c.Q_kSum_translate_le` | `A1c` | **FAITHFUL, sharpened** — the manuscript's "absolute constants" are pinned to the explicit `2`, from `sec:prelim` fact (ii) in the single direction the paper uses. |
| `lem:transl-cover`(i) | `KsumAudit.KFloor.window_even_length` | `T2KFloor` | **FAITHFUL** — `q ≥ (k−1)(kK+2) ⇒ |W_even| ≥ k`, stated subtraction-free. The bound is exactly tight in the formalization. |
| `lem:transl-cover`(ii) | `KsumAudit.KFloor.window_odd_length` | `T2KFloor` | **FAITHFUL** — `q ≥ (k²−2)K+2k−1 ⇒ |W_odd| ≥ k`, exactly tight. |
| `lem:transl-cover`, covering | `KsumAudit.KFloor.exists_shift_into_window` | `T2KFloor` | **FAITHFUL** — and it machine-confirms finding **F-R2**: the proof runs off the window LENGTH via Bézout, and carries **no** `Nat.Coprime k q` hypothesis. |
| `prop:rosmanis`(1), characterization of `D₀` | `KsumAudit.Rosmanis.isNegative_iff` (+ the bridge `isNegative_iff_twoSum_false`) | `RosmanisBarrier` | **FAITHFUL** — clauses (a) and (b) verbatim, and `D₀` is identified with `{x : 2Sum_{Z_q,t,N}(x) = 0}` rather than being redefined. |
| `prop:rosmanis`(1), count `≥ 2` | `two_orbits_of_two_cycles`, `two_orbits_of_one_cycle`, `not_single_orbit`, `twoSum_not_single_orbit` | `RosmanisBarrier` | **ORBIT-PROPER but NARROWER in scope** — the conclusion "`≥ 2` orbits / never a single orbit" is proved in both manuscript branches; the *bijection* and the *formula* `Σ_f p_{≤m}(N−f)` are NOT formalized. |
| `prop:rosmanis`(2), witnesses | `existence_fails_q3`, `uniqueness_fails_q5` (+ `q5_cycle_type`, `swapped_string_q3`) | `RosmanisBarrier` | **FAITHFUL** for the two finite witnesses. `existence_fails_q3` is *stronger* than the paper's argument: it needs no injectivity of `ρ` — commuting with `σ` alone forces `ρ(0) = 0`. |
| `prop:rosmanis`(2), representation sentence | — | — | **NOT FORMALIZED.** "In a permutation module `C[X]` the multiplicity of the trivial equals the number of orbits" was not attempted; Mathlib `v4.31` does not make it cheap at the level of `C[D₀]` for a `Sym × Centralizer` action, and the commission scoped it to "only if cheap". |
| `prop:rosmanis`(3) | `KsumAudit.Rosmanis.positive_blocks_empty` | `RosmanisBarrier` | **FAITHFUL**. |
| `C(σ) ≅ (C₂ ≀ S_m) × S_τ` | — | — | **NOT FORMALIZED.** `Centralizer` is the centralizer *as defined*; no proof uses the wreath-product identification, so nothing here depends on it. |
| `prop:embed` | — | — | **NOT FORMALIZED** — outside this run's budget (see §6). |
| `lem:embed-allt` | gcd half: `KSUM.A2.coprime_k_q` (reorg pass, pre-existing); translation half: `KSUM.A1c.Q_le_of_coprime` | `A2` / `A1c` | **FAITHFUL in two pieces**, neither authored by this run's `A2` side. |

---

## 4. Deliverable 3 — the `KSUM.A1b` check

`KSUM.A1b.Claim` **was already proved** before this run, by wiring to tier T1: `KSUM.A1b.holds :=
fun n _κ _q hq y => KsumAudit.twoSum_encode_cyc hq n y`, which is `lem:encode`'s identity part.
The proof is unconditional (no `QueryModel` argument) and the node's `lean:` block already reads
`state: "proved"`. **No gap; no edit needed; `KSUM/A1b.lean` was left byte-identical.** Recorded
here because the commission asked for the check, not because anything changed.

Consequence worth flagging: with `A1a` now proved as well, **two of `KSUM.A1.composition`'s three
leaf hypotheses are unconditional theorems**. Finding **F-R8** of the reorg pass (non-vacuity of
that composition is not machine-checked) therefore narrows to a single remaining source —
`A1c.Claim` — which §5 shows is itself defective.

---

## 5. G-T2b in detail: why `KSUM.A1c.Claim` cannot be proved

`Claim` (frozen, unchanged):

```
∃ C > 0, ∀ k N q, 3 ≤ k → 2k²+2k−5 ≤ q → ∀ t₀ t, Q(kSum_{Z_q,t₀,N}) ≤ C · Q(kSum_{Z_q,t,N})
```

**My own derivation, reached before the lead advisory arrived.** `lem:transl-cover` relates a target
only to the other targets of its own coset `t + kZ_q`; the window family is what guarantees that
coset contains a usable target. When `gcd(k,q) = g > 1` the cosets are proper subsets of `Z_q`, and
the manuscript compares nothing across them. The symmetries this development actually has are
(i) translation `t ↦ t + k·a` and (ii) the effect on the target of a per-coordinate *affine*
relabeling, `t ↦ u·t` for a unit `u` (from `sec:prelim` fact (ii)). At `k = 3, q = 21` — which
**does** satisfy `Claim`'s range hypothesis, `q₀(3) = 19 ≤ 21` — these generate two orbits on
targets, `{t : 3 ∣ t}` and `{t : 3 ∤ t}`, because a unit is never `≡ 0 (mod 3)` while `3a` always is.
Machine-checked as

```lean
theorem not_reachable_k3_q21 : ∀ u v a : ZMod 21, u * v = 1 → u * 1 + 3 * a ≠ 0 := by decide
theorem k3_q21_in_range      : 2 * 3 ^ 2 + 2 * 3 - 5 ≤ 21 := by decide
```

so no chain of `lem:transl-cover` steps and fact-(ii) relabelings compares `t₀ = 0` with `t = 1`.
**`Claim` is therefore not derivable from the `QueryModel` interface.**

**Cited derivation (lead advisory).** Finding R-A1-3 of
`ksum/artifacts/ksum_composition_layer_review_20260730.md`: at `k = 3, q = 3`, `kSum_{Z_3,0,N}` is
constant for `N ≥ 7` (every value class of size `≥ 3` sums to `0`) while `kSum_{Z_3,1,N}` is not, so
with `constQ` no constant `C` works.

**The discrepancy, reported not resolved (STEP 0 rule).** `q = 3` fails `Claim`'s own hypothesis
`19 ≤ q` at `k = 3`. So R-A1-3 falsifies the *prose* claim and the pre-window rendering, but not the
Lean `Claim` as literally written; my `q = 21` obstruction is the in-range one, and it establishes
non-derivability rather than outright falsity. **Turning "not derivable" into "false" would require
exhibiting a `QueryModel` that separates the two target orbits while satisfying `restrict`,
`relabel`, `freeze`, `constQ`, `abi`, `tani` — not attempted here.** The already-on-disk finding
F-R8 anticipated exactly this ("that instance is outside `A1c`'s window `q₀(3) = 19 ≤ q`, but close
enough that no cheap witness exists").

**What was proved instead, so the repair has its Lean side ready:**

- `Q_kSum_translate_le` — coset-local target transfer at the explicit constant `2`;
- `Q_window_cover` — *for every `t` there EXISTS a base-window target `s ∈ [t₀, t₀+k)` with
  `Q(kSum_s) ≤ 2·Q(kSum_t)`* — the faithful covering statement, and the shape a repaired `A1c`
  should carry;
- `Q_le_of_coprime` — `Claim`'s conclusion, with constant `2`, under `gcd(k,q) = 1`. This also
  explains why the same over-strong rendering is harmless on the `A2` branch: there `gcd(k,q)=1` is
  **forced** by the construction (`KSUM.A2.coprime_k_q`).

Per the advisory I did **not** reshape `Claim`; `claim_hash` is untouched and the node's `lean.state`
stays `stated`, now with a `defect:` field recording why.

---

## 6. Resisted / not attempted, with reasons

| Item | Status | Reason |
|---|---|---|
| `prop:core-even` / `lem:core-odd` at **every** window target | **not attempted** | `A1a.Claim` is existential in `t₀`, so one target discharges it in full. Generalizing needs the core vector to depend on `t` (last entry `t−(k−3)U` instead of `U`) and one more `Finset` split; the arithmetic was worked out and is straightforward, but it was traded for deliverables 4–5. **This is the gap that makes `Q_window_cover` currently decorative rather than load-bearing**, and it is half of the A1a/A1c repair the lead will direct. |
| `prop:rosmanis`(1) bijection + `Σ_f p_{≤m}(N−f)` | **not attempted** | Needs a partitions-into-`≤ m`-parts API and an orbit-quotient cardinality argument. The manuscript's *use* of part (1) is only `≥ 2`, which is proved. |
| `prop:rosmanis`(2) representation sentence | **not attempted** | Scoped by the commission to "only if Mathlib makes it cheap". It does not: it needs `C[X]`-invariants for a product-group permutation module. |
| `C(σ) ≅ (C₂ ≀ S_m) × S_τ` | **not attempted** | Not used by any proof here. |
| `prop:embed` | **not attempted** | The balanced-base-`ω` and balanced-base-`(2k+1)` digit arguments are a second `core_reduction`-sized development. `lem:embed-allt`'s gcd half is already machine-checked from the reorg pass. |
| `EmbedData` witness (`demoEmbed`, review finding R-A2-3) | **not attempted** | Flagged OPTIONAL by the advisory and outside my file ownership (`KSUM/Support/Embed.lean`). Left to the lead; the reviewer's suggested instance is `k=3, n=1, R=2, P=12, Mv=24, cP=3`, `enc` into `ZMod 325`. |

Nothing was reshaped to make it compile. Every statement above is either proved as written or listed
here as not attempted.

---

## 7. The rosmanis-node F-T1 check (deliverable 6 — report, do not create)

**Searched:** `ksum/proof-dag/NODE_INDEX.md` and every file under
`ksum/proof-dag/nodes/`.

**Result — F-T1 pattern, three more nodeless manuscript statements:**

- **`prop:rosmanis` has NO DAG node.** The only node files mentioning it are `KSUM.LEAN.yaml`,
  `KSUM.LEAN.T2.rosmanis-kfloor.yaml` and `KSUM.LEAN.statement-fidelity.yaml` — i.e. the Lean-audit
  nodes that name it as *scope*, never as a claim of their own. There is no `NODE_INDEX.md` row for
  it. This is exactly the F-T1 pattern found by T3 for `lem:factorial-filtration` and
  `prop:joint-lp`: a load-bearing manuscript proposition (it is what `sec:branch-ledger` cites as
  "the structural reason the regular-representation premise fails", killing a whole DAG leaf) whose
  only home is prose. **Registering it is a rule-8a decision for the lead; I did not create it.**
- **`lem:core`, `prop:core-even`, `lem:core-odd`** are covered by `KSUM.A1a` (its Claim names both
  propositions) — no gap.
- **`lem:transl-cover`** is covered by `KSUM.A1c` — no gap, but see §5: the node's Claim is not a
  faithful rendering of it.
- **`prop:embed` / `lem:embed-allt`** are covered by `KSUM.A2a` / `KSUM.A2` — no gap.
- Count reconciliation, checked at closeout: `NODE_INDEX.md` reads "Nodes: 141", 141 node files
  exist, and the validator reports 141 — consistent. (Mid-run the index still said 140; the lead's
  concurrent application of the composition-layer review registered `KSUM.G11` and recounted.)

---

## 8. Build command, result, and evidence

```
cd ksum/proof-dag/lean
lake build
→ Build completed successfully (3011 jobs)
→ BUILD_RESULT: exit=0
```

- Full transcript: `ksum/artifacts/logs_ksum_lean_T2_20260730/build.log` (212 lines, ends with the
  `BUILD_RESULT` line).
- `#print axioms` manifest: `ksum/artifacts/logs_ksum_lean_T2_20260730/print_axioms.txt` — **162
  declarations, 0 outside `{propext, Classical.choice, Quot.sound}`**, of which **50** are the
  tier-T2 declarations added or changed by this run.
- SHA ledger: `ksum/artifacts/logs_ksum_lean_T2_20260730/SHA256SUMS.txt`, in the LF/RAW dual-row
  convention of the T3 ledger (LF rows hash the bytes with CRLF normalized to LF; RAW rows hash the
  bytes exactly as they sit on disk).
- Hygiene greps: `sorry` 0, `axiom` 0, `native_decide` 0, `implemented_by` 0, build warnings 0
  across both libraries.

**New/changed Lean sources:**

| File | Change |
|---|---|
| `KsumAudit/T2KFloor.lean` | NEW — `lem:core`, `prop:core-even` + `lem:core-odd` (`core_reduction`), the `lem:transl-cover` window arithmetic and coset covering, 6 witnesses. |
| `KsumAudit/RosmanisBarrier.lean` | NEW — `prop:rosmanis` parts (1) (`≥ 2`, orbit-proper), (2) witnesses, (3), plus the `2Sum` bridge. |
| `KSUM/A1a.lean` | `stated → proved`: added `holds`; header records the base-target narrowing. `Claim` byte-identical, `claim_hash` unchanged. |
| `KSUM/A1c.lean` | Added `Q_kSum_translate_le`, `Q_window_cover`, `Q_le_of_coprime`, `not_reachable_k3_q21`, `k3_q21_in_range`, and the CLAIM DEFECT box. `Claim` byte-identical, `claim_hash` unchanged. |
| `KSUM/Trust.lean` | Census section (c) corrected (two proved leaves; the `A1c` defect), new section (e) with the T2 label↔name table, and `#print axioms` for all 50 new declarations. |
| `KsumAudit.lean` | Root import list + header entry for the two new modules. |

---

## 9. Standing failure-mode list (rule 7e) — how each was addressed

- **Dropped/extra normalization factors.** Every constant is explicit: the transfer constant is `2`
  (one application of fact (ii)), never an unnamed `Θ`.
- **Type/dimension mismatches.** The kernel discharges these; the one place it bites is
  `core_reduction`'s statement, where the frozen block has length `m` and the live block `2n`, and
  `Fin.append` forces `2n + m` everywhere.
- **Undefined terms of art.** `D₀`, `C(σ)`, "orbit", "negative", "window", "core", "parked" all have
  Lean definitions in the same file, and `IsNegative` is *proved* equal to the paper's `2Sum = 0`.
- **Quantifier drift — the F-R13 trap (dominant risk for this tier).** `core_reduction` carries the
  manuscript's window `(k²−2)κ + 2k−1 ≤ q` verbatim, never the `k = 2` range `2κ+1 ≤ q`; and it is a
  *hypothesis* of the theorem I proved, so the direction is safe (a stronger hypothesis would have
  been caught by the proof failing, not by it succeeding). `witness_q0_three` machine-checks that at
  `k=3, κ=2` the window threshold is exactly `q₀(3) = 19`, closing the loop on F-R13's by-product.
- **Hypotheses smuggled into definitions.** `coreVec`, `baseTarget`, `coreUnit`, `parkedVal`,
  `signedVal`, `IsNegative`, `act` are all total and hypothesis-free; every constraint lives in a
  theorem's binders.
- **Numerics validating values while the derivation is broken.** The four `core_reduction` witnesses
  are `decide`d *through the theorem* (`rw [core_reduction …, twoSum_encode_cyc …]; decide`), so
  they exercise the proved statement, not an independent re-implementation. That is the
  value-vs-formula distinction (7f) resolved in the "formula" direction, deliberately: they are
  non-vacuity checks, not corroboration.
- **Orbit vs invariant-class conflation (the tier-specific item).** Addressed head-on: the action is
  defined, `valueCount` is *proved* invariant, so `not_single_orbit` quantifies over the actual
  group. Where the rendering is narrower — the count formula — it is declared in the module's scope
  box, in `Trust.lean` §(e), and in §3 above.

---

## 10. Status written

`KSUM.LEAN.T2.rosmanis-kfloor`: **OPEN → NUMERICAL · `pending-review: KSUM.LEAN.statement-fidelity`**
(proposer tier; a green build is a run — `DAG_PROTOCOL.md` §2 and §7.1). No other node's epistemic
status was touched. `KSUM.A1a` / `KSUM.A1b` / `KSUM.A1c` remain **PROVED** from their own
2026-07-18/19 reviews; only their `lean:` mechanization fields moved.
