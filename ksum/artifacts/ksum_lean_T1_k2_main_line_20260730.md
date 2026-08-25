# KSUM.LEAN.T1 — Lean 4 formalization of the k=2 lower-bound main line

**Node:** [`KSUM.LEAN.T1.k2-main-line`](../ksum/proof-dag/nodes/KSUM.LEAN.T1.k2-main-line.yaml)
(registered OPEN under rule 8a, 2026-07-30).
**Parent:** [`KSUM.LEAN`](../ksum/proof-dag/nodes/KSUM.LEAN.yaml).
**Role:** executor. **Date:** 2026-07-30.
**Source audited:** `ksum/paper/ksum_small_alphabet.tex`, `sec:prelim` (lines 175–215) and
`sec:k2` (lines 217–295), plus `thm:oabarrier` (lines 643–649).

---

## 0. Pre-action report (structure protocol / `PRETASK_RELOAD_PROMPT.md`)

**Files read from disk before any work, in the mandated order:**
`research/PRETASK_RELOAD_PROMPT.md`; `DAG_PROTOCOL.md` (whole file); 
`research/RESEARCH_STRUCTURE_PROTOCOL.md` (whole file); `ksum/README.md`;
`ksum/notes/KSUM_PROOF_DAG.md` (header + the whole `Lean` mermaid/outline block);
`ksum/proof-dag/NODE_INDEX.md`; `ksum/proof-dag/nodes/KSUM.LEAN.T1.k2-main-line.yaml`;
`ksum/proof-dag/nodes/KSUM.LEAN.yaml`; `ksum/lean/README.md`;
`ksum/lean/KsumAudit/Smoke.lean`, `lakefile.lean`, `lean-toolchain`.

- **Target node and status as read from disk:** `KSUM.LEAN.T1.k2-main-line`, status **OPEN**
  (`status_source: rule8a-registration-2026-07-30`), kind LEAF, role tool, AND-child of
  `KSUM.LEAN`, related to `KSUM.A1b` and `KSUM.C0`.
- **Role:** executor (not reviewer; I authored this work and may not review it).
- **Highest status my planned evidence could license (DAG §2):** **NUMERICAL with an explicit
  `pending-review:` marker.** A green `lake build` is a run (command + log + SHA), which caps at
  NUMERICAL; completion tiers need the independent review `KSUM.LEAN.statement-fidelity`, which
  has not run. Writable by me as proposer, at that tier only.
- **Gates of the commission (one line each):**
  - **G-L2** — is `lem:encode` formalized `sorry`-free? (decisive gate)
  - **G-T1a** — does each remaining target compile `sorry`-free? (per-target table)
  - **G-T1b** — does every theorem have a non-vacuous witness example that compiles?
  - **G-T1c** — does `#print axioms` show only `propext`, `Classical.choice`, `Quot.sound`?
- **Deliverables:** Lean sources in the three owned files; this artifact; build log + SHA ledger
  under `ksum/artifacts/logs_ksum_lean_T1_20260730/`; Work-record / Evidence / Status-history entries on
  the node; status ceiling NUMERICAL · pending-review.
- **Conflicts between the commission text and the disk protocols:** **two, both procedural, both
  reported rather than resolved silently:**
  1. `RESEARCH_STRUCTURE_PROTOCOL.md` §9 lists `git diff --check` among the required closeout
     checks; the commission says *"Do NOT run any `git` command."* I followed the commission and
     ran no git command. The other two closeout validators (`tools/proof_dag_check.py`,
     `tools/literature_check.py`) are not git commands and were run — both exit 0.
  2. `DAG_PROTOCOL.md` §5.4 and structure protocol §6.5 require `NODE_INDEX.md` and the
     Mermaid/outline views to be synchronized *in the same diff* as a status change; the commission
     forbids me to edit `NODE_INDEX.md` or `KSUM_PROOF_DAG.md` and assigns that sync to the lead.
     I followed the commission. **Consequence to be closed by the lead:** `NODE_INDEX.md` row
     `LeanT1` and the `LeanT1` Mermaid label both still read `[OPEN]` while the canonical node file
     now reads `NUMERICAL · pending-review`. No graph structure changed (no nodes created, no edges
     changed), so only the status word is stale.

---

## 1. Gate results

| Gate | Result | Evidence |
|---|---|---|
| **G-L2** — `lem:encode` `sorry`-free | **PASS** | `twoSum_encode` (abstract group form) and `twoSum_encode_cyc` / `twoSum_encode_cyc_pair` (the paper's displayed `ZMod q` form) compile with no `sorry`; the query half `Q_claw_le_encode` is derived from facts (i)+(ii) alone. |
| **G-T1a** — remaining targets `sorry`-free | **PASS** (7/7 in scope) | table in §2 |
| **G-T1b** — non-vacuous witness per theorem | **PASS** | 33 `example`s, all discharged by `decide` / `norm_num` / direct application at concrete parameters; **plus** `demoModel`, a proof that `QueryModel` is inhabited, so the conditional theorems are not vacuous *as a class* |
| **G-T1c** — `#print axioms` clean | **PASS** | 29/29 top-level results depend on at most `[propext, Classical.choice, Quot.sound]`; `ED_isIndexOne` depends on none; **no `axiom` and no `sorry` anywhere in the three owned files** (verified by grep, §5) |

No gate failed. Seven audit findings are recorded in §4; none of them is an error in the paper's
mathematics, but F1, F2 and F5 are gaps in what `sec:prelim` *states* versus what the proofs *use*.

---

## 2. LaTeX label ↔ Lean name map

Files: `ksum/lean/KsumAudit/{Defs,QueryModel,MainLine}.lean`, namespace `KsumAudit`.

### Definitions (`Defs.lean`)

| LaTeX | Lean | Note |
|---|---|---|
| `\kSum_{G,t,N}` (`sec:prelim`) | `kSum G k t N` | `k`-subset formulation, verbatim |
| `\twoSum_{G,t,N}` | `twoSum G t N := kSum G 2 t N` | `twoSum_eq_decide` proves the `∃ i ≠ j` form |
| `\Claw_{n\to\kappa}` (Definition, `sec:prelim`) | `Claw n κ` | on `Fin (2n) → Fin κ`; `Claw_pairUp` gives the `(f,g)` reading |
| `E(f,g)` (`lem:encode`) | `encode n s y`, per-position map `encMap n s p` | `s : Fin κ → G` abstract; `cyc q κ a = a+1` is the paper's instance |
| `T = \{(x,x)\}`, index-1 OA (`sec:barriers`) | `twoOAProblem`, `IsIndexOne2`, `ED N q` | k=2 case of the OA framework |

### Interface (`QueryModel.lean`) — **all hypotheses, none proved**

| LaTeX | Lean field |
|---|---|
| `\Q(f)`, `sec:prelim` "Query model" | `QueryModel.Q` |
| fact (i), restriction | `QueryModel.restrict` |
| fact (ii), per-coordinate relabeling | `QueryModel.relabel` |
| *(not in the paper — finding F1)* frozen coordinate | `QueryModel.freeze` |
| *(not in the paper — finding F2)* constant function has `Q = 0` | `QueryModel.constQ` |
| `thm:abi` (Ambainis–Balodis–Iraids) | `QueryModel.abi`, constant `QueryModel.cABI` |
| `thm:tani` (Tani) | `QueryModel.tani` |
| (i)+(ii) composed — **derived, a theorem not a field** | `QueryModel.relabel_inj` |

### Theorems (`MainLine.lean`)

| LaTeX | Lean | `sorry`-free |
|---|---|---|
| `lem:encode` identity, general group | `twoSum_encode` | yes |
| `lem:encode` identity, `ZMod q` (paper display) | `twoSum_encode_cyc`, `twoSum_encode_cyc_pair` | yes |
| `lem:encode` three cases | `cyc_add_ne_zero` (cases 1+2), `cyc_injective` / `cyc_sub_eq_zero_iff` (case 3) | yes |
| `lem:encode` value sets `{1..κ} ∪ {q-κ..q-1}` | `cyc_val`, `neg_cyc_val` | yes |
| `lem:encode` query half | `Q_claw_le_encode` | yes |
| `lem:shift` identity | `twoSum_shift` | yes |
| `lem:shift` query half + existence of `c` | `Q_twoSum_shift`, `exists_half_odd` | yes |
| `lem:oddN` | `twoSum_snoc_zero`, `twoSum_encode_snoc`, `twoSum_encode_snoc_cyc`, `Q_claw_le_encode_odd` | yes |
| `thm:main-odd` | `main_odd` (Tani range), `main_odd_abi` (ABI subrange) | yes |
| `thm:main-general` | `exists_repr_set` (representative construction), `main_general` | yes |
| `cor:threshold` lower half | `threshold_large` (case 1), `threshold_small` (case 2), `threshold` (combined), `sqrt_mul_rpow_eq` | yes |
| `cor:threshold` — Tani not needed (finding F6) | `threshold_small_abi` | yes |
| `thm:oabarrier` (i) | `ED_isIndexOne`, `oabarrier_ED`, `oabarrier_ED_Q` | yes |
| `thm:oabarrier` (ii) | `oabarrier_kSum` | yes |
| `thm:k2-upper` | **OUT OF SCOPE** (an algorithm) — not attempted, per commission | n/a |
| — | `demoModel`: `QueryModel` is inhabited (non-vacuity witness) | yes |

Supporting explicit-constant arithmetic: `sqrt_div_le`, `rpow6_div_le`, `combine_bound`.

---

## 3. What the result is CONDITIONAL on

Every theorem whose statement mentions `M : QueryModel` is conditional on **exactly** the fields of
that structure, and on nothing else (this is machine-checked: `#print axioms` shows no `axiom`
dependency, and the structure has no other fields):

1. `Q` — the existence of a real-valued complexity measure on Boolean functions of length-`M`
   strings over per-position finite alphabets.
2. `restrict` — `sec:prelim` fact (i), in the product-subdomain shape actually used.
3. `relabel` — `sec:prelim` fact (ii), with the per-position bijection allowed to change the
   alphabet, exactly as the paper's item (ii) states.
4. `freeze` — **not stated in the paper** (finding F1).
5. `constQ` — **not stated in the paper** (finding F2).
6. `cABI > 0`, `abi`, `tani` — the imported bounds of [ABI21] and [Tani24]. **Lean does not verify
   these.** If ABI is wrong, every `M.Q` theorem here is wrong and the kernel is silent.

Everything with no `M` argument (`twoSum_encode`, `twoSum_snoc_zero`, `twoSum_shift`,
`exists_half_odd`, `exists_repr_set`, `oabarrier_ED`, `oabarrier_kSum`, the arithmetic lemmas) is
**unconditional finite mathematics**.

Two scope restrictions, recorded so the fidelity review can see them:
- Alphabets live in `Type 0`. Every alphabet in the paper is a finite set, so this restricts
  nothing mathematically.
- Statements over `ZMod q` carry `[NeZero q]`. This is an *instance-level* side condition, needed
  only because `Fintype (ZMod q)` requires it; it is implied by every stated hypothesis
  (`2κ+1 ≤ q`, `5 ≤ q`, `cN ≤ q`) and is therefore not a narrowing of the theorem.

---

## 4. Audit findings

**F1 (MINOR, gap between what `sec:prelim` states and what the proofs use).** `lem:oddN` extends the
encoding "by one frozen coordinate of value `0`". Fact (i) as *printed* — "if `g` is the restriction
of `f` to a subset of its domain" — does not type-check for this step: the restricted function has
input length `2n`, not `2n+1`. The step needs a third elementary principle, formalized as the field
`QueryModel.freeze`: a position whose value is frozen may be deleted. It is justified by fact (i)'s
own simulation argument ("an algorithm for `f` already solves `g` with the same queries" — the
simulator answers queries to the frozen position itself, at no query cost), so this is a
**statement gap, not a mathematical error**. Repair: one sentence in `sec:prelim`.

**F2 (MINOR, same kind).** `thm:oabarrier` concludes "In both cases `Q = 0`". That a constant
function has query complexity `0` is not among facts (i)/(ii). Formalized as `QueryModel.constQ`.
Again obviously true; again unstated.

**F3 (MINOR, harmless over-hypothesis).** `lem:encode` is stated with "Let `κ ≥ 2` and let
`q ≥ 2κ+1`". The identity `2Sum(E(f,g)) = Claw(f,g)` needs only `q ≥ 2κ+1`; `κ ≥ 2` is needed only
where the claw bound is imported. `twoSum_encode_cyc` is therefore stated without `κ ≥ 2` and is
strictly stronger than the printed lemma.

**F4 (MINOR, harmless over-hypothesis).** `thm:oabarrier`(ii) hypothesizes "`p` prime". Primality is
never used: the argument needs only `p ∣ k` and the fact that `(Z_p)^m` has exponent dividing `p`,
both of which hold for every `p ≥ 1`. `oabarrier_kSum` carries no primality hypothesis and is
strictly stronger. (Primality is of course what makes `p^m` an interesting alphabet *size*.)

**F5 (SUBSTANTIVE for a formalizer; benign for the paper).** Facts (i) and (ii) as printed **cannot
be composed** if `Q` is defined only on strings over a single alphabet. The codeword set
`E([κ]^{2n})` is a *product* of two **different** per-position value sets (`{1..κ}` on the first
half, `{q-κ..q-1}` on the second), so restricting to it lands on a position-dependent alphabet, and
fact (ii) then relabels between position-dependent alphabets. The paper's own phrasing of (ii)
("possibly different per position, and possibly changing the alphabet") anticipates this, but only
for the map, not for the type of `Q`. The formalization therefore gives `Q` a *dependent* alphabet
family `Alph : Fin M → Type`. With that, the composite step used by `lem:encode` — "an injective
per-coordinate re-encoding costs a factor `2`" — is **derived** as `QueryModel.relabel_inj`, not
assumed. This is the audit's positive result on the load-bearing lemma: **the encoding needs
nothing beyond the paper's two stated facts.**

**F6 (MINOR, over-citation — machine-checked).** `cor:threshold`, Case 2, justifies its range by
"`2 ≤ κ ≤ 2n-1` (the range of Theorem `thm:tani`)". In fact `κ < n` always holds in that case:
`q < N-1` gives `q ≤ N-2`, hence `κ = ⌊(q-1)/2⌋ ≤ (N-3)/2 < ⌊N/2⌋ = n`. So **`cor:threshold` does
not depend on `thm:tani` at all** — `thm:abi` alone suffices. Formalized as `threshold_small_abi`,
which is `threshold_small` with `M.tani` replaced by `M.abi`; its existence is the proof.
(`thm:main-odd` genuinely does need Tani in the subrange `2n-1 < q ≤ 4n-1`; that is `main_odd`
versus `main_odd_abi`.)

**F7 (MINOR, proof-route simplification).** `cor:threshold` Case 2 routes even `q` through
`thm:main-general` over `Z_q`, requiring `|Z_q[2]| = 2`. That detour is unnecessary: `lem:encode`
holds "any parity", and `κ = ⌊(q-1)/2⌋` satisfies `2κ+1 ≤ q` for **both** parities
(`= q` if `q` odd, `= q-1` if `q` even). `threshold_small` therefore uses the cyclic encoding
uniformly and never invokes `thm:main-general`. The paper's route is correct; it is just longer.
(`thm:main-general` is formalized independently, as `main_general`.)

### The `c`-dependence question (explicitly commissioned)

The commission asked to **track exactly where the `c`-dependence enters and where it does not**, the
paper claiming it arises ONLY in the case `cN ≤ q < N-1`. **The paper's claim is verified**, and in a
stronger form than the paper states it — `c` is absent from Case 1 not only in the constant but in
the *hypotheses*:

- `threshold_large` (`q ≥ N-1`): its statement contains **no `c` at all**. Its hypotheses are
  `6 ≤ N` and `N - 1 ≤ q` — both absolute. Its constant is
  `c_ABI / (4·√3·6^{1/6})`, absolute.
- `threshold_small` (`cN ≤ q < N-1`): `c` occurs in exactly two places — the constant carries the
  factor `c^{1/6}`, and the validity threshold `5 ≤ cN` is `c`-dependent (this is the paper's
  "assume `N` large enough that `cN ≥ 5`"). Both are confined to this case.
- `threshold` (combined) states the constant as `min` of the two case constants, so the split is
  visible in the statement rather than only in the prose. `min` of an absolute constant and a
  `c^{1/6}`-scaled one is the formal content of the paper's "scales as `min{1, c^{1/6}}`".

The `c`-dependent *threshold* `5 ≤ cN` is worth one sentence in the paper: `Θ_c` hides it, but in
explicit-constant form it is a hypothesis, and it belongs to Case 2 only (Case 1 needs only `N ≥ 6`,
to make `κ = n-1 ≥ 2`).

### Standing failure-mode list (rule 7e) — explicit response

- **Dropped or extra normalization factors:** none. Every factor `2` is exhibited: `relabel` costs
  `2`; `lem:encode` costs `2`; `lem:shift` costs another `2`; total `4` in `main_odd`, and the final
  constants `c_ABI/(4·√3·3^{1/6})` etc. are the product of those with `√n ≥ √N/√3` and
  `κ^{1/6} ≥ (q/3)^{1/6}`. Nothing is absorbed into an `Ω(·)`.
- **Type/dimension mismatches:** discharged by the kernel. The one real type issue found is F5.
- **Undefined terms of art / missing stability ranges:** all ranges are explicit natural-number
  inequalities. `κ ≤ 2n-1` is written `κ < 2n` because natural subtraction silently turns
  `κ ≤ 2·0-1` into `κ ≤ 0`; the two readings agree wherever `κ ≥ 2`, and the choice is documented in
  the `tani` field's docstring. Same for `q ≤ 4n-1` written `q + 1 ≤ 4n` and `q < N-1` written
  `q + 1 < N`.
- **Quantifier drift:** the explicit-constant form fixes the quantifier order — the constant is a
  fixed field of `QueryModel`, quantified *before* `N` and `q`, so no "for sufficiently large `N`"
  can creep in. Range hypotheses are stated per theorem and never widened; where I state something
  strictly stronger than the paper (F3, F4) it is flagged.
- **Hypotheses smuggled into a definition:** explicitly guarded against. `encode`/`encMap`/`cyc` are
  defined for **every** `q, κ, n` with no side conditions; `q ≥ 2κ+1` appears only as a hypothesis of
  `twoSum_encode_cyc` and friends. A reader can therefore instantiate the definition at `q < 2κ+1`
  and see the lemma fail — the statement is falsifiable, which is the point.
- **Numerics validating a value while the printed derivation is broken:** not applicable — there are
  no numerics here; the kernel checks the derivation itself. The nearest analogue is *vacuity*, and
  that is countered twice: per-theorem witness examples at concrete parameters (G-T1b), and
  `demoModel`, which proves the interface is inhabited.

---

## 5. Build

```
cd <machine-local-path-redacted>
lake build KsumAudit.MainLine
```

Output (full log: [`logs_ksum_lean_T1_20260730/build.log`](logs_ksum_lean_T1_20260730/build.log);
the three owned `.olean`s were deleted first to force a real rebuild):

```
✔ [1981/1983] Built KsumAudit.Defs (56s)
✔ [1982/1983] Built KsumAudit.QueryModel (50s)
ℹ [1983/1983] Built KsumAudit.MainLine (53s)
... 29 `#print axioms` info lines (see below) ...
Build completed successfully (1983 jobs).
BUILD_RESULT: exit=0
```

No `error`, no `warning`, no `sorry`. Verified by grep over the three owned files:

```
grep -n "sorry\|axiom" KsumAudit/Defs.lean KsumAudit/QueryModel.lean KsumAudit/MainLine.lean
  -> no matches
```

Toolchain: Lean `v4.31.0`, Mathlib `v4.31.0`, `.lake/packages` a junction to a machine-local
prebuilt package cache. SHA-256 ledger:
[`logs_ksum_lean_T1_20260730/SHA256SUMS.txt`](logs_ksum_lean_T1_20260730/SHA256SUMS.txt).

### `#print axioms` — the machine-checked citation manifest

```
'KsumAudit.twoSum_encode'            depends on axioms: [propext, Classical.choice, Quot.sound]
'KsumAudit.twoSum_encode_cyc'        depends on axioms: [propext, Classical.choice, Quot.sound]
'KsumAudit.twoSum_encode_cyc_pair'   depends on axioms: [propext, Classical.choice, Quot.sound]
'KsumAudit.twoSum_snoc_zero'         depends on axioms: [propext, Classical.choice, Quot.sound]
'KsumAudit.twoSum_encode_snoc'       depends on axioms: [propext, Classical.choice, Quot.sound]
'KsumAudit.twoSum_encode_snoc_cyc'   depends on axioms: [propext, Classical.choice, Quot.sound]
'KsumAudit.QueryModel.relabel_inj'   depends on axioms: [propext, Classical.choice, Quot.sound]
'KsumAudit.Q_claw_le_encode'         depends on axioms: [propext, Classical.choice, Quot.sound]
'KsumAudit.Q_claw_le_encode_odd'     depends on axioms: [propext, Classical.choice, Quot.sound]
'KsumAudit.Q_claw_le_twoSum_zero'    depends on axioms: [propext, Classical.choice, Quot.sound]
'KsumAudit.twoSum_shift'             depends on axioms: [propext, Classical.choice, Quot.sound]
'KsumAudit.Q_twoSum_shift'           depends on axioms: [propext, Classical.choice, Quot.sound]
'KsumAudit.exists_half_odd'          depends on axioms: [propext, Quot.sound]
'KsumAudit.combine_bound'            depends on axioms: [propext, Classical.choice, Quot.sound]
'KsumAudit.main_odd'                 depends on axioms: [propext, Classical.choice, Quot.sound]
'KsumAudit.main_odd_abi'             depends on axioms: [propext, Classical.choice, Quot.sound]
'KsumAudit.exists_repr_set'          depends on axioms: [propext, Classical.choice, Quot.sound]
'KsumAudit.main_general'             depends on axioms: [propext, Classical.choice, Quot.sound]
'KsumAudit.Q_zero_le_target'         depends on axioms: [propext, Classical.choice, Quot.sound]
'KsumAudit.threshold_large'          depends on axioms: [propext, Classical.choice, Quot.sound]
'KsumAudit.threshold_small'          depends on axioms: [propext, Classical.choice, Quot.sound]
'KsumAudit.threshold_small_abi'      depends on axioms: [propext, Classical.choice, Quot.sound]
'KsumAudit.threshold'                depends on axioms: [propext, Classical.choice, Quot.sound]
'KsumAudit.sqrt_mul_rpow_eq'         depends on axioms: [propext, Classical.choice, Quot.sound]
'KsumAudit.ED_isIndexOne'            does not depend on any axioms
'KsumAudit.oabarrier_ED'             depends on axioms: [propext, Classical.choice, Quot.sound]
'KsumAudit.oabarrier_ED_Q'           depends on axioms: [propext, Classical.choice, Quot.sound]
'KsumAudit.oabarrier_kSum'           depends on axioms: [propext, Classical.choice, Quot.sound]
'KsumAudit.demoModel'                depends on axioms: [propext, Classical.choice, Quot.sound]
```

29/29 within Lean's three standard axioms. **This is the whole point of using structure fields
instead of `axiom`s**: had the imported bounds been `axiom`s, they would appear in every line above
and the manifest would be worthless.

---

## 6. Steps that resisted, and how

Nothing in the commissioned scope had to be dropped. Two steps resisted long enough to be worth
recording, because both are audit signal rather than Lean friction:

1. **Composing facts (i) and (ii)** (finding F5). The first design used a single alphabet for `Q`.
   `lem:encode` then does not type: fact (i) lands on a position-dependent alphabet and fact (ii)
   with same-alphabet bijections cannot pick it up. Per the house rule I did **not** reshape the
   statement; I changed the *interface* to the position-dependent form the paper's own item (ii)
   describes, and then *derived* the composite as `relabel_inj`. If the interface had needed
   anything strictly stronger than facts (i)+(ii), the commission required me to stop and report;
   it did not.
2. **`lem:oddN`'s frozen coordinate** (finding F1). There is no way to make the printed fact (i)
   cover it — the input length changes. I added the field `freeze`, flagged in its own docstring
   and here, rather than silently widening `restrict`.

Deliberately **not** attempted, per the commission: `thm:k2-upper` (an algorithm). Also not
formalized, and declared so the fidelity review does not assume otherwise:
- the `O(N^{2/3})` upper half of `cor:threshold` (imported from Ambainis / Childs–Eisenberg);
- the general index-1 orthogonal-array framework of Belovs–Špalek. Only the two specific arrays
  named in `thm:oabarrier` are formalized, and `IsIndexOne2` is the `k = 2` case of the index-1
  condition. The sentence "any lower bound valid uniformly over the arrays is vacuous" is
  represented by `oabarrier_ED_Q : M.Q (ED N q) = 0` plus `oabarrier_kSum`, not by a quantification
  over all admissible array families.

---

## 7. Status this artifact licenses

**NUMERICAL — pending-review (`KSUM.LEAN.statement-fidelity`).** A green build is a run
(`DAG_PROTOCOL.md` §2, structure protocol §4(7)); the completion gate is the independent
statement-fidelity review, which has not run. Per `KSUM.LEAN` scope clause 4 this audit is
confirmatory and can only ever DEMOTE the paper's theorem nodes; it produces no new bound, and the
endpoints stay `Ω(N^{11/18}) ≤ Q ≤ O(N^{2/3})` at the critical alphabet.

Specifically **not** claimed: that `thm:abi` or `thm:tani` is correct; that the formal statements
say what the LaTeX says (that is exactly what `KSUM.LEAN.statement-fidelity` must decide); or that
`KSUM.A1b` / `KSUM.C0` are re-verified (they are already PROVED with archived reviews, and this run
found nothing that would demote them).
