# k-Sum Lean audit — consolidated STATEMENT-FIDELITY review (node `KSUM.LEAN.statement-fidelity`)

**Date:** 2026-07-31 · **Reviewer:** fresh Opus 5 instance, independent · **Artifact:** immutable
· **Scope:** the whole on-disk Lean development at `ksum/lean/` (libraries
`KsumAudit` and `KSUM`), tiers T1 + T2 + T3 + the DAG-mirroring composition layer + the
2026-07-30 repair batch, against `ksum/paper/ksum_small_alphabet.tex`.

---

## 0. PRE-ACTION REPORT

**Files read from disk, completely, before any math or verdict**, in the order prescribed by
`research/PRETASK_RELOAD_PROMPT.md`: that template; `DAG_PROTOCOL.md` (whole file, §1–§7
including all of §7.10); `research/RESEARCH_STRUCTURE_PROTOCOL.md`; `ksum/README.md`; the
header block of `ksum/notes/KSUM_PROOF_DAG.md`; `ksum/proof-dag/NODE_INDEX.md`;
the target node `ksum/proof-dag/nodes/KSUM.LEAN.statement-fidelity.yaml`; its parent
`ksum/proof-dag/nodes/KSUM.LEAN.yaml`; the three tier nodes `KSUM.LEAN.T{1,2,3}.*`; and
`ksum/notes/ksum_lean_campaign_state_20260730.md`.

- **Target node and status as read from disk:** `KSUM.LEAN.statement-fidelity` — **OPEN**
  (`status_source: rule8a-registration-2026-07-30`), LEAF, role `tool`, parent `KSUM.LEAN` (OPEN),
  no children, three `related` tier nodes.
- **ROLE: reviewer. Independence statement.** I did not author any part of this Lean development,
  any node file, the manuscript, or any prior artifact in this campaign. I was given **no desired
  outcome**; the commission states explicitly that a confirming and a rejecting verdict are equally
  acceptable and that a NARROWER/DIVERGENT finding is more valuable than a FAITHFUL one. I have
  written no Lean, no node, and run no `git` command.
- **Highest status my evidence could license (§2 ladder):** a **completed independent review**,
  archived and cited, opens the rule-6/rule-7 gate so that the **proposer/lead** may write
  CERTIFIED\* (or PROVED, on the tier nodes, by an independent checker). I write **no status
  myself**; per the commission the lead applies verdicts.
- **Gates / deliverables (one line each).** (1) reproduce `lake build` and report true exit + job
  count; (2) `#print axioms` census on every top theorem + grep for `sorry`/`axiom`/`native_decide`/
  `implemented_by`; (3) every `Claim`/interface field against its frozen source; (4) every top
  conclusion against its manuscript statement; (5) satisfiability/vacuity, with four mandated
  sub-checks; (6) honesty of README, node statuses, `lean:` blocks, §7.9 scope clauses; deliverable
  = this one artifact.
- **Conflicts between commission text and disk:** **two, reported not resolved.**
  1. `RESEARCH_STRUCTURE_PROTOCOL.md` §9 lists `git diff --check` among required closeout checks;
     the commission forbids `git`. **No `git` command was run** (the same recurring conflict the T1,
     reorg and T3 executors each reported).
  2. The commission says the `KSUM` library has modules "A1, A1a-A1d, A2, A2a, A2b, B2, B4, B4a,
     goal, Interface, Support/*, SelfTest, Trust" and the campaign ledger says "seventeen modules".
     On disk there are **17 `.lean` files** under `KSUM/` (12 node modules + `Interface`,
     `Support/Embed`, `Support/Freeze`, `SelfTest`, `Trust`); the `KSUM.LEAN` node work record of
     2026-07-30 says "fourteen modules covering …" in one place and "Seventeen modules" in another.
     Disk wins: 17. Cosmetic, recorded.

**Method note (7c, anchoring ban).** For every theorem ruled on below I first read the Lean source
and wrote the English rendering in §4.A / §5.A / §6.A **before opening the LaTeX**; the LaTeX was
opened only at §4.B / §5.B / §6.B, and the executors' own LaTeX↔Lean tables (`ksum_lean_T3_…`,
`ksum_lean_T2_…`) were read **last**, after my verdicts were fixed. Coincidences with the
executors' wording are flagged where they occur (§6.C).

---

## 1. DUTY 1 — BUILD REPRODUCTION

Command, run by me from `ksum/lean/`:

```
lake build
```

- **True exit status: `0`.**
- **Final line: `Build completed successfully (3011 jobs).`**
- Job count **3011**, matching the repair-batch record. Mathlib came from the machine-local
  prebuilt cache through the `.lake/packages` junction
  (`→ /c<machine-local-path-redacted>`); the two project
  libraries were **replayed** from trace-matched caches, which is itself evidence that the current
  sources hash-match what was elaborated.
- **Zero warnings, zero errors, zero `declaration uses 'sorry'`** in the transcript (grep for
  `warning|error|sorry|declaration uses` returns nothing).
- Toolchain `leanprover/lean4:v4.31.0`, Mathlib required at tag `v4.31.0` — matching
  `lean-toolchain` and `lakefile.lean`.
- **Independent SHA ledger verification.** I re-verified
  `ksum/artifacts/logs_ksum_lean_repair_20260730/SHA256SUMS.txt` against disk under both its declared
  conventions (LF-normalized and RAW): **38 rows verify exactly, 0 missing.** The 8 rows that do
  not verify are all **non-Lean** files edited *after* the repair batch by the lead's 2026-07-31 A1
  promotion (`KSUM.A1.yaml`, `NODE_INDEX.md`, `KSUM_PROOF_DAG.md`, the campaign ledger). **Every Lean
  source verifies**, so my build reproduces exactly the ledgered state.
- All five evidence directories exist with `build.log`, `SHA256SUMS.txt` and (for T2/T3/reorg/repair)
  `print_axioms.txt`; each `build.log` records `BUILD_RESULT: exit=0`. **§7.7 satisfied.**

---

## 2. DUTY 2 — AXIOM / HOLE CENSUS

### 2.1 Grep census (all `.lean` outside `.lake/`, 34 files)

| pattern | declaration-position hits | comment/docstring hits |
|---|---|---|
| `^\s*axiom\s+` | **0** | — |
| `sorry` (outside backticked prose) | **0** | 24, all of the form ``No `sorry`.`` |
| `native_decide` | **0** | 5 |
| `implemented_by` | **0** | 2 |
| `unsafe`, `opaque`, `sorryAx`, `admit` | **0** | — |
| `set_option` | 9 | 8 × `linter.unusedSectionVars false`, 1 × `maxHeartbeats 2000000` |

The single `maxHeartbeats 2000000` sits on `KsumAudit.KFloor.core_reduction_at` (a ~260-line
proof); it is a resource bound, not a soundness escape. The eight `linter.unusedSectionVars false`
are cosmetic. **No hole of any kind exists in this development.**

### 2.2 `#print axioms` manifest

`KSUM/Trust.lean` carries 89 `#print axioms` and imports `KsumAudit.MainLine`,
`KsumAudit.Obstructions` (which pulls the eight `Obstructions*` modules), `KsumAudit.T2KFloor`,
`KsumAudit.RosmanisBarrier`, `KSUM.goal`, `KSUM.B4`, `KSUM.A1`, `KSUM.SelfTest`,
`KsumAudit.Smoke`, so the tier-owned blocks land in the same transcript. I did **not** assume
completeness; I machine-extracted the printed set from my own build log and cross-checked it
against a namespace-tracking parse of all 34 sources:

- **176 declarations printed** (89 Trust + 29 MainLine + 58 Obstructions\*).
- **Distinct axiom sets observed:** `[propext, Classical.choice, Quot.sound]` ×151,
  `[propext, Quot.sound]` ×14, `[propext]` ×4, `[Quot.sound]` ×1, *"does not depend on any axioms"*
  ×6. **Nothing outside Lean's three standard axioms. 176/176 clean.**
- Source census: **329 declarations, of which 235 `theorem`/`lemma`.** 80 theorem/lemmas are not
  individually printed. I inspected the list: **all 80 are helper lemmas** (`prod_ite_forall`,
  `axis_sum_eq`, `cyc_val`, `reynolds_apply`, `occ_split`, the `demo*` lemmas, …), each a
  transitive dependency of a printed top-level result, so any bad dependency would surface in the
  printed manifest. Two printed names (`KsumAudit.KFloor.card_coreIdx`, `mem_coreIdx`) are declared
  with a leading `@[simp]` attribute and so were missed by my line-anchored parse, not absent.

**VERDICT (duty 2): CENSUS CLEAN.** No `sorry`, no `axiom`, no `native_decide`, no
`implemented_by`; 176/176 printed declarations at exactly Lean's three standard axioms; nothing
present that is unaccounted for in `Trust.lean`.

**Two minor recording defects, no soundness impact:**
- **m-1.** `KSUM/Trust.lean`'s header claims `#print axioms` "for every top-level declaration"; it
  is 176/235. The accurate phrasing is "every culminating result"; helper lemmas are covered
  transitively. (README line 75 repeats the phrase.)
- **m-2.** Three declarations that read as culminating are not in the manifest:
  `KsumAudit.Obstructions.Orientation.orientation_corr_le_half` (a named step of ORIENT clause (b)),
  `KsumAudit.Obstructions.not_pureHighDegree_succ_of_moment_zero_ne_zero`, and
  `KsumAudit.Obstructions.PairTensor.exists_light_pair`. Each is consumed by a printed theorem, so
  the census is sound; adding the three lines would make it self-evidently so.

---

## 3. DUTY 3 — FAITHFULNESS OF HYPOTHESES (the `QueryModel` interface)

Rendered from `KsumAudit/QueryModel.lean` **before** opening `sec:prelim`.

### 3.A Lean-only renderings

`QueryModel` has exactly **nine fields**: `Q`, `restrict`, `relabel`, `freeze`, `constQ`, `cABI`,
`cABI_pos`, `abi`, `tani`.

- `Q` — an arbitrary real-valued function on Boolean functions over **position-dependent** finite
  alphabets `Alph : Fin M → Type` (`Type 0`). *No* non-negativity, monotonicity or normalization is
  assumed.
- `restrict` — for every family of `Finset`s `D i`, `Q (f restricted to ∏ᵢ D i) ≤ Q f`.
- `relabel` — for every per-position **equivalence** `e i : Alph' i ≃ Alph i`,
  `Q (f ∘ e) ≤ 2 · Q f`.
- `freeze` — for every `a : Alph (Fin.last M)`,
  `Q (fun y : (∀ i : Fin M, Alph i.castSucc) => f (Fin.snoc y a)) ≤ Q f`.
- `constQ` — `f` constant ⇒ `Q f = 0`.
- `cABI : ℝ` with `0 < cABI`.
- `abi` — `∀ n κ, 2 ≤ κ → κ < n → cABI·√n·κ^{1/6} ≤ Q (Claw n κ)`.
- `tani` — `∀ n κ, 2 ≤ κ → κ < 2·n → cABI·√n·κ^{1/6} ≤ Q (Claw n κ)`.

### 3.B Diff against `sec:prelim` / `thm:abi` / `thm:tani`

| field | manuscript source | verdict | note |
|---|---|---|---|
| `Q` | `sec:prelim` "Query model" | FAITHFUL | position-dependent alphabets are what item (ii) already licenses (**finding F5**); with a single alphabet (i)+(ii) cannot compose |
| `restrict` | fact (i) | **NARROWER (safe)** | fact (i) allows *any* subdomain; Lean restricts to **product** subdomains `∏ D i`. Every use in the paper (codeword subdomain of `E`, the frozen core) is product-shaped, so nothing is lost, and assuming *less* is the safe direction |
| `relabel` | fact (ii) | **FAITHFUL** | per-position bijections, alphabet-changing, **absolute factor `2` present and exact**. The paper's `Θ` half is deliberately not a field — the paper says every transfer uses (ii) "in the single direction" |
| `freeze` | **NOT IN THE MANUSCRIPT** | **NOT-A-PAPER-CLAIM (F1)** | correctly flagged in three places (field docstring, `Interface.lean` table, `Trust.lean` (b)) |
| `constQ` | **NOT IN THE MANUSCRIPT** | **NOT-A-PAPER-CLAIM (F2)** | same, correctly flagged |
| `cABI`, `cABI_pos` | the constant hidden in `Ω(·)` | FAITHFUL (bookkeeping) | making it explicit removes the two-parameter (`n`,`κ`) ambiguity — a real strengthening |
| `abi` | `thm:abi`: "For all `2 ≤ κ < n`" | **FAITHFUL** | range matches exactly |
| `tani` | `thm:tani`: "for all `2 ≤ κ ≤ 2n−1`" | **FAITHFUL** | `κ < 2*n` over `ℕ` ≡ `κ ≤ 2n−1`; the docstring's reason for avoiding `2*n − 1` (truncated subtraction at `n = 0`) is correct |

**Three observations a reader must have:**

- **(a) `abi` is redundant given `tani`.** Both fields carry the *same* `cABI`, and
  `{2 ≤ κ < n} ⊆ {2 ≤ κ < 2n}`, so `abi` follows from `tani`. This is not an over-assumption
  (the conjunction is equivalent to "∃ c>0 such that both `Ω`-statements hold with `c`", which is
  exactly the two cited theorems, taking the min of their constants). It does mean that
  **finding F6 is a statement about which field a proof term references**, not about logical
  necessity — which is the correct reading and is how `threshold_small_abi` is presented.
- **(b) The interface asserts a threshold-free `Ω`.** `abi`/`tani` hold at *every* `(n,κ)` in
  range, with no "for sufficiently large `n`". A literal asymptotic `Ω` would give a threshold.
  For a nonconstant function in any faithful model `Q > 0`, so the threshold-free form follows by
  shrinking the constant over the finitely many small cases — standard, and the paper's "constants
  hidden in `Ω(·)` are absolute" supports it. Recorded as a **mild interface strengthening**, not a
  defect.
- **(c) F1 is real but narrower than described.** `lem:oddN` freezes a coordinate of value `0`.
  Fact (i) as printed *does* cover the domain restriction to
  `Z_q^{2n} × {0} ⊆ Z_q^{2n+1}`. What fact (i) does **not** give is the further step "a position
  whose alphabet is a singleton may be deleted", which changes the input **length**. So the
  unstated principle is exactly *singleton-coordinate deletion*, and one sentence in `sec:prelim`
  repairs it. The Lean `freeze` field bundles both steps; the finding stands, with this refinement.

**No third unstated field has appeared.** Field-by-field enumeration above is exhaustive: two
unstated facts (`freeze`, `constQ`), two cited theorems (`abi`, `tani`), two stated facts
(`restrict`, `relabel`), one definition (`Q`), one bookkeeping constant with positivity. **Item (i)
of the queued list is answered: exactly F1 and F2, both flagged, and no new one.**

### 3.C `Defs.lean` — definitional-smuggling check (7e)

Rendered from Lean alone, then diffed:

| definition | Lean | manuscript | hypothesis smuggled? |
|---|---|---|---|
| `kSum G k t N x` | `∃ S : Finset (Fin N), S.card = k ∧ ∑_{i∈S} x i = t` | `sec:prelim` display | **none** |
| `twoSum G t N` | `kSum G 2 t N` | `k=2` specialization | **none** |
| `Claw n κ y` | `∃ i j : Fin n, y (lo n i) = y (hi n j)` on `Fin (2n) → Fin κ` | Definition (Claw) | **none**; the paper's own range caveat is deferred to `thm:abi`/`thm:tani`, exactly as printed |
| `encode n s y p` | `if p < n then s (y p) else -(s (y p))` | `E(f,g) = (f(1),…,f(n), −g(1),…,−g(n))` | **none**; defined for *every* `q`, `κ`, `s` — `q ≥ 2κ+1` appears only in `lem:encode`'s hypotheses |
| `cyc q κ a` | `((a+1 : ℕ) : ZMod q)` | values `{1,…,κ}` | **none** |
| `Coll k n R g` | `∃ v, ∀ j, ∃ i, g (blockPos k n j i) = v` | `def:kcoll` | **none**; equivalent to `∃ i₁…i_k, g₁(i₁)=…=g_k(i_k)` |
| `twoOAProblem`, `IsIndexOne2`, `ED` | as printed | `sec:barriers` | **none** |
| `frozen m f c` | iterated `Fin.snoc`, last `m` coordinates fixed | `sec:k3` item (a) | **none** |

**No hypothesis of any paper theorem is hidden inside a definition.** The house rule stated at the
top of `Defs.lean` is honoured throughout.

### 3.D `SelfTest.lean` — the "wrong object" countermeasure (7e, and this node's own mandate)

Witness `example`s instantiate hypotheses; they cannot catch a mis-defined `twoSum`/`Claw`/`E`,
because a wrong definition has witnesses too. §7.3 requires decidable checks that the
**definitions** reproduce independently known values. I read all 33 `example`s in
`KSUM/SelfTest.lean` and assessed coverage rather than accepting the G-R4 PASS.

| definition | positive | negative | discriminating negative (the one that matters) |
|---|---|---|---|
| `twoSum` | `1+4=0` in `Z_5` | pair sums of `(1,1,2,2)` never `0` | **yes** — `(3,1,1,1)` at `t=1`: `3+3=1` but no two *distinct* positions sum to `1`, so a definition allowing one coordinate twice would fail |
| `kSum`, **`k = 3`** | `1+2+4≡0` in `Z_7` | `1+1+1≠0` | **yes** — `(3,4,1,1)` at `k=3`, `t=0`: the *pair* `3+4=0` must **not** count, so a definition using "some subset" rather than "size exactly `k`" would fail |
| `Claw` | `f=(0,1), g=(2,0)` share `0` | `f=(0,1), g=(2,2)` share nothing | **yes** — `(2,2,0,1)`: a repeat **inside** the first half must be `false`, so a definition comparing the wrong halves would fail |
| `cyc`/`encode` | `cyc 5 2 = {1,2}`; `encode … 0 = 1` | `encode … 1 ≠ 2` | **yes** — position 1 carries `−s 1 = 3`, so "`s` on both halves" would fail |
| `lem:encode` identity | **exhaustive** over all `2²` words at `(n,κ,q)=(1,2,5)` | `¬∀ y …` at `q = 4 < 2κ+1`, `n = 2` | **yes** — and the negative control is sharp: it needs `n ≥ 2` because the failure is a *within-half* pair, which is exactly what `lem:encode`'s case analysis says. At `n = 1` the identity survives at `q = 4`, and that is checked too |
| `blockPos`/`Coll` | value `1` in both blocks | blocks carry disjoint values | **yes** — `(1,1,0,2)`: a repeat **inside** one block must be `false` |
| `frozen` | `(1,2)+core `(4)`` sums to `0` in `Z_7` | two negatives | **yes, and this is the best check in the file** — `kSum` is permutation-invariant, so no `kSum`-valued test can detect "core prepended instead of appended". Three *position-sensitive* probes (`x 0 = 1`, `x 2 = 4`, `¬(x 0 = 4)`) plus `frozen … = kSum … (Fin.append live core)` and `Fin.append ![1,2] ![4] = ![1,2,4]` pin the order exactly |
| `KSUM.A2.coprime_k_q` arithmetic | `k=3` and `k=4` instances against the manuscript's own `P`, `M`, `q` | — | **yes** — `gcd(3, 3·25) = 3 ≠ 1` at `P = 2`, showing `k ∣ P` is load-bearing, not decoration |

**Verdict: the SelfTest genuinely pins the definitions, and it does cover `kSum` at `k = 3`, not
only `k = 2`** (three checks, including the size-exactly-`k` discriminator). Every definition
carries at least one positive and one negative case, and in six of eight rows the negative is a
*discriminating* one aimed at a specific mis-definition. **Coverage gaps, recorded:** no checks
exist for `twoOAProblem` / `IsIndexOne2` / `ED` (T1's barrier definitions), for `encMap` in
isolation, for `coreVec`/`coreVecAt`/`baseTarget` (T2 — though `KFloor.witness_coreUnit` checks
`U = 7, t₀ = 7, v = 12` at `k=3, K=2`, which covers the numerics), or for any tier-T3 definition
(`corr`, `signF`, `l1`, `ffRow`, `PureHighDegree`, `kappa`, `zeta`, `rho`, `prodMeasure`). The T3
vocabulary is where an unchecked definition would be hardest to notice, since its theorems are
stated entirely in that vocabulary; `ObstructionsCore.lean`'s own header concedes that its
adoption verdict is "a definitional one … recorded in §2 of that artifact", i.e. by prose, not by
`decide`. **Recommended: extend `SelfTest` to `signF`/`corr`/`l1` and to `kappa`/`prodKappa` at
`r = 1`, where hand-computable values exist.**

---

## 4. DUTY 4 — TIER T1: CONCLUSION FIDELITY

### 4.A Lean-only renderings (written before opening §`sec:k2`)

- `twoSum_encode_cyc` — *for every `n`, `κ`, `q` with `2κ+1 ≤ q` and every word `y` on `2n`
  letters, `2Sum` at target `0` on the encoded string equals `Claw_{n→κ}(y)`.*
- `Q_claw_le_encode` — *for `s` injective with `s a + s b ≠ 0` for all `a,b`,
  `Q(Claw_{n→κ}) ≤ 2 · Q(2Sum_{G,0,2n})`.*
- `Q_claw_le_encode_odd` — *same bound at length `2n+1`* (uses `freeze`).
- `twoSum_shift` / `Q_twoSum_shift` — *if `c+c = t'−t` then translating every coordinate by `c`
  carries `2Sum_t` to `2Sum_{t'}`; hence `Q(2Sum_t) ≤ 2·Q(2Sum_{t'})`.*
- `main_odd` — *for `q` odd, `q ≥ 5`, `q+1 ≤ 4⌊N/2⌋`, every `t`:
  `cABI/(4√3·3^{1/6})·√N·q^{1/6} ≤ Q(2Sum_{Z_q,t,N})`.*
- `main_odd_abi` — *same conclusion under the tighter `q+1 ≤ 2⌊N/2⌋`, using only `abi`.*
- `main_general` — *for finite abelian `G`, `κ = (|G| − |G[2]|)/2 ≥ 2`, `κ < 2n`, `N ∈ {2n, 2n+1}`:
  `cABI/(2√3)·√N·κ^{1/6} ≤ Q(2Sum_{G,0,N})`.*
- `threshold_large` — *`t = 0` or `q` odd, `N ≥ 6`, `N−1 ≤ q` ⇒
  `cABI/(4√3·6^{1/6})·√N·N^{1/6} ≤ Q`; **no `c` anywhere**.*
- `threshold_small` / `threshold_small_abi` — *`0 < c`, `N ≥ 6`, `5 ≤ cN ≤ q`, `q+1 < N` ⇒
  `cABI·c^{1/6}/(4√3·3^{1/6})·√N·N^{1/6} ≤ Q`; the second is the first with `tani` replaced by
  `abi`.*
- `threshold` — *the two cases assembled with the `min` of the two constants.*
- `oabarrier_ED` / `oabarrier_ED_Q` — *`q < N` ⇒ `ED N q` is identically `true`, hence `Q = 0`.*
- `oabarrier_kSum` — *`p ∣ k` and `(k−1)p^m < N` ⇒ `kSum_{(Z_p)^m, k, 0, N}` is identically `true`.*

### 4.B Diff against the LaTeX, and verdicts

| LaTeX label | Lean name | verdict | verified (7f) | notes |
|---|---|---|---|---|
| `lem:encode` (identity) | `twoSum_encode_cyc`, `twoSum_encode` | **FAITHFUL** (+ strictly stronger) | statement + proof read | omits the paper's `κ ≥ 2` (**F3**) — strengthening, safe |
| `lem:encode` (query half) | `Q_claw_le_encode` | **FAITHFUL** | statement + proof read | `Ω(·)` made explicit as the factor `2`; goes through `relabel_inj`, i.e. facts (i)+(ii) only |
| `lem:oddN` | `Q_claw_le_encode_odd` | **FAITHFUL** rel `freeze` | statement + proof read | the `freeze` dependence is visible in the type; see §3.B(c) |
| `lem:shift` (identity) | `twoSum_shift` | **FAITHFUL** | statement + proof read | |
| `lem:shift` (query) | `Q_twoSum_shift` | **NARROWER (declared)** | statement + proof read | paper states `Θ`; Lean states only `Q(2Sum_t) ≤ 2 Q(2Sum_{t'})`. Sufficient for every use; the reverse follows by `−c` and is not written |
| `thm:main-odd` | `main_odd` | **FAITHFUL** | statement + proof read | `q ≤ 4n−1` rendered `q+1 ≤ 4·(N/2)`; constant exhibited |
| `thm:main-odd` (ABI subrange) | `main_odd_abi` | **FAITHFUL** | statement + proof read | the paper's own sentence "the subrange `q ≤ 2n−1` uses `thm:abi` alone" |
| `thm:main-general` | `main_general` (+ `exists_repr_set`) | **FAITHFUL** | statement + proof read | `n` taken as a parameter with `N ∈ {2n,2n+1}` rather than `⌊N/2⌋` — equivalent |
| `cor:threshold` Case 1 | `threshold_large` | **FAITHFUL** | statement + proof read | `κ = n−1`, `abi` only, no `c` in constant **or** hypotheses — matches the paper's claim about where `c` enters |
| `cor:threshold` Case 2 | `threshold_small` | **FAITHFUL** | statement + proof read | `c` confined to `c^{1/6}` and to the validity threshold `5 ≤ cN` |
| `cor:threshold` Case 2 | `threshold_small_abi` | **FAITHFUL + AUDIT FINDING** | statement + proof read | **F6 CONFIRMED independently.** I re-derived it: `q ≤ N−2` and `κ=(q−1)/2` give `κ ≤ (N−3)/2 < ⌊N/2⌋ = n`, so `abi`'s range suffices and `cor:threshold` does **not** need `thm:tani`. Machine-checked by the theorem's existence |
| `cor:threshold` (whole) | `threshold` | **NARROWER (declared)** | statement + proof read | paper asserts `Θ_c(N^{2/3})`; Lean formalizes only the **lower** half. The matching `O(N^{2/3})` of Ambainis / Childs–Eisenberg is out of scope and said so |
| `thm:oabarrier` (i) | `ED_isIndexOne`, `oabarrier_ED`, `oabarrier_ED_Q` | **FAITHFUL** | statement + proof read | |
| `thm:oabarrier` (ii) | `oabarrier_kSum` | **NARROWER on the `Q` clause; STRONGER on hypotheses** | statement + proof read | drops "`p` prime" (**F4**) — correct, only `p ∣ k` and exponent `p` are used — and drops `k ≥ 3` (also sound: `k ∈ {0,1,2}` hold trivially). **But the paper's "In both cases `Q = 0`" is stated only for (i)**; there is no `oabarrier_kSum_Q`. One line (`M.constQ … oabarrier_kSum`) would close it |
| — | `demoModel`, `demoQ*`, `Claw_nonconst` | infra | statement + proof read | see §7.1 |
| — | `combine_bound`, `sqrt_div_le`, `rpow6_div_le`, `exists_half_odd`, `sqrt_mul_rpow_eq`, `encMap_injective`, `Q_zero_le_target`, `Q_claw_le_twoSum_zero` | infra | statement read | explicit-constant arithmetic; `sqrt_mul_rpow_eq` confirms `√N·N^{1/6} = N^{2/3}` |

**F7 also confirmed independently:** `threshold_small` handles **even** `q` with the same cyclic
encoding at `κ = ⌊(q−1)/2⌋` (the hypothesis `2κ+1 ≤ q` reads `q−1 ≤ q` there), so `cor:threshold`
Case 2's detour through `thm:main-general` is indeed unnecessary.

---

## 5. DUTY 4 — TIER T2: CONCLUSION FIDELITY

### 5.A Lean-only renderings

- `core_reduction_at` — *for `k ≥ 3`, core size `m ∈ {k−2, k−1}`, modulus `(k²−2)κ + 2k−1 ≤ q`,
  and any offset `r < k`: `kSum` at target `t₀ + r` (`t₀ = (k−2)(kκ+1)`) on the `2n + m`
  coordinates `append (encoded live block) (coreVecAt … r)` equals `2Sum` at `0` on the live
  block.*
- `core_wellformed` — *at the base target, every subset of `a ≤ k−2` core coordinates sums to
  `a·U` with `U ≤ a·U ≤ t₀`, and `a·U = t₀ ⟺ a = k−2`.*
- `sum_coreIdx` / `sum_coreIdxAt` — *the whole core sums to `t₀` / to `t₀ + r`.*
- `window_even_length` / `window_odd_length` — *the two window-length inequalities, written
  subtraction-free.*
- `exists_shift_into_window` — *for a window `[lo, lo+L)` inside `[0,q)` with `gcd(k,q) ≤ L`, every
  `t` admits a shift `a` and a window residue `s` with `t + k·a = s` in `Z_q`.* **No coprimality
  hypothesis.**
- `KSUM.A1c.kSum_translate` / `Q_kSum_translate_le` / `Q_window_cover_coset` — *the translation
  identity for arbitrary finite abelian `G`; its query transfer at the explicit factor `2`; and the
  assembled statement "every `t` is at least as hard as some window target **in its own coset**, up
  to the factor `2`".*
- Rosmanis: `isNegative_iff` (*`x` negative ⟺ each fixed-point value occurs ≤ once and each 2-cycle
  contributes only one side*), `isNegative_iff_twoSum_false` (*that set is exactly
  `{x : 2Sum = false}`*), `isNegative_act` + `valueCount_act` (*the `S_N × C(σ)` action preserves
  `D₀` and the number of distinct values is an invariant*), `not_single_orbit`,
  `two_orbits_of_two_cycles`, `two_orbits_of_one_cycle`, `twoSum_not_single_orbit`,
  `positive_blocks_empty`, `existence_fails_q3`, `uniqueness_fails_q5`.

### 5.B Diff against `app:k3` / `prop:rosmanis` / `app:embed`

| LaTeX label | Lean name | verdict | verified (7f) | notes |
|---|---|---|---|---|
| `lem:core` | `core_wellformed`, `sum_coreIdx` | **NARROWER** | statement + proof read | proved **at the base target `t = t₀` only**, where all core entries equal `U` and the paper's two sub-cases collapse. The general-`t` clause "every nonempty `A` has `∑ ∈ [U,t]`, with `= t` iff `A` is the whole core" is **not** formalized at `t ≠ t₀` |
| `lem:core` (whole-core sum) | `sum_coreIdxAt` | **FAITHFUL** | statement + proof read | at every window target — but this is one sub-clause of `lem:core`, not the lemma (see honesty item **H-7**) |
| `prop:core-even` | `core_reduction_at`, `m = k−2` | **NARROWER** | statement + proof read | three narrowings, all safe: (1) target range is the `k`-element sub-window `[t₀, t₀+k)`, not all of `W_even`; (2) the modulus hypothesis used is the **stronger** odd-case `(k²−2)κ+2k−1 ≤ q`, not `prop:core-even`'s `q ≥ (k−1)(kK+1)`; (3) the conclusion is `2Sum` at `0` on the live block rather than `Claw`, one `lem:encode` step short. (1)+(2) are exactly what the covering argument needs and no more |
| `lem:core-odd` | `core_reduction_at`, `m = k−1` | **NARROWER** | statement + proof read | same three; parked value `t + (k−1)K + 1` matches |
| `lem:transl-cover` (identity) | `KSUM.A1c.kSum_translate` | **FAITHFUL** | statement + proof read | stated for arbitrary finite abelian `G`, all parities |
| `lem:transl-cover` (query) | `KSUM.A1c.Q_kSum_translate_le` | **NARROWER (declared)** | statement + proof read | paper states `Θ`; Lean the one direction actually used, with constant `2` |
| `lem:transl-cover` (i) | `window_even_length` | **FAITHFUL** | statement + proof read | I re-derived `\|W_even\| ≥ k ⟺ q ≥ (k−1)(kK+2)` independently; agrees |
| `lem:transl-cover` (ii) | `window_odd_length` | **FAITHFUL** | statement + proof read | same for `\|W_odd\| ≥ k ⟺ q ≥ (k²−2)K+2k−1` |
| `lem:transl-cover` (covering) | `exists_shift_into_window` | **FAITHFUL** | statement + proof read | runs off the window **length** `≥ gcd(k,q)`, exactly as printed; `lo+L ≤ q` guarantees the residue is genuine |
| `lem:transl-cover` (assembled) | `KSUM.A1c.Q_window_cover_coset` | **FAITHFUL** | statement + proof read | the coset witness `s = t + k·a` is exposed — this is the R-A1-3 repair, and it is present |
| `prop:rosmanis` (1), characterization | `isNegative_iff`, `isNegative_iff_twoSum_false` | **FAITHFUL** | statement + proof read | the bridge to the paper's own object `D₀ = {2Sum = false}` is proved, which is the right thing to check |
| `prop:rosmanis` (1), count `≥ 2` | `not_single_orbit`, `two_orbits_of_{two_cycles,one_cycle}`, `twoSum_not_single_orbit` | **NARROWER** | statement + proof read | genuinely **orbit-proper** (action defined, `D₀`-preservation proved, separating invariant proved invariant), in both branches. **Not formalized:** the bijection with `(f,λ)`, the formula `Σ_f p_{≤m}(N−f)`, and "nondecreasing and unbounded in `N` once `m ≥ 2`". The module says so, in the right place |
| `prop:rosmanis` (2) | `existence_fails_q3`, `uniqueness_fails_q5` (+ `swapped_string_q3`, `q5_cycle_type`) | **NARROWER** | statement + proof read | the two finite witnesses only; the representation-theoretic sentence ("multiplicity of the trivial = number of orbits") is **not** formalized, declared |
| `prop:rosmanis` (3) | `positive_blocks_empty` | **FAITHFUL** | statement + proof read | |
| `C(σ) ≅ (C₂ ≀ S_m) × S_τ` | — | **NOT FORMALIZED** (declared) | — | `Centralizer` is the centralizer as defined; no proof uses the wreath identification |
| `prop:embed` | — | **NOT FORMALIZED** (declared) | — | outside the run's budget; consequences carried by `EmbedData` |
| `lem:embed-allt` (gcd half) | `KSUM.A2.coprime_k_q` (+ `coprime_k_succ_of_dvd`, `coprime_k_MvSucc`) | **FAITHFUL** | statement + proof read | I checked the argument line by line against the paper's own two-case proof; the Lean runs the cases through `gcd` rather than prime-by-prime and is equivalent |
| `lem:embed-allt` (translation half) | `KSUM.A2.nsmul_surjective`, `KSUM.A1c.Q_le_of_coprime` | **FAITHFUL** | statement + proof read | |

**Queued item (iii) answered.** T2's declared gaps are confirmed exactly as declared (bijection +
count formula unformalized; part (2)'s rep-theory sentence unformalized). The
**every-window-target repair is genuinely IMPLEMENTED, not merely stated**:
`core_reduction_at` carries `(hr : r < k)` and its target is literally `baseTarget k κ + r`, and
`KSUM.A1a.Claim` quantifies `∀ s, t₀ ≤ s < t₀ + k`. I re-checked the arithmetic claim that the same
modulus hypothesis suffices: `(k²−2)κ + 2k − 1 ≤ q` is the master inequality at `r = k−1`, and the
proof consumes only `r ≤ k−1`. **Confirmed.**

---

## 6. DUTY 4 — TIER T3: CONCLUSION FIDELITY

### 6.A Lean-only renderings (the ones that matter)

- `pair_tensor` — *for odd `q ≥ 3` and `N ≥ q`, with `r = (q−1)/2`, there exist a nonempty finite
  set `T` of pair-total vectors `s : Fin r → ℕ` with `s_c ≥ 2` and `∑ s_c = N−1`, and a probability
  weight `w` on `T`, such that the mixture `∑_{s∈T} w_s · ⨂_c κ_{s_c}` has `ℓ¹` norm exactly `1`
  and annihilates every **falling-factorial row** `(1)_{α_f} · ∏_c prodRow` of total order
  `< q−1`.* **No measure on `Z_q^N`, no `S_N × C(σ)` invariance, no query polynomial appears.**
- `tilt_corr_gt_three_quarters` — *if `0 ≤ C ≤ 25/19` and `0 ≤ S ≤ 29/23` then
  `2/(1+C·S) > 3/4`* — plus `one_sub_sum_le_prod_one_sub` (Weierstrass) and `tilt_gap`
  (`437/581 − 3/4 = 5/2324`).
- `band_add`, `band_add_three`, `band_add_fin` — *if each block measure annihilates every
  falling-factorial row below order `d_i`, the `m`-fold **convolution** annihilates every row below
  `∑ d_i`.* `band_preserved_by_scaling` — *rescaling preserves the band.*
- `product_obstruction_{exact,ratio,normalized,q}` and `…_mixture{,_normalized,_q}` — *on an
  abstract product state space `∀ c : ι, Ω c` with an abstract axis predicate and an abstract NO
  predicate **assumed** equal to the all-axis event, every unit-`ℓ¹` locally-balanced
  sign-separated product (and every nonnegative mixture of such) has `|corr| = 2^{1−|ι|}`, and
  `≤ 1/2` once `|ι| = (q−1)/2` with `q ≥ 5`.*
- `block_obstruction_corr` / `_bound` — *`⟨ζ, OR_m⟩ = −2·Ψ(true,…,true)·∏_j ρ_j` and
  `|⟨ζ,OR_m⟩| ≤ ∏ ρ_j`* (`true` is `sgnNeg`, i.e. `S_j = −1`; convention checked).
- `block_obstruction_band` — *if `Ψ` has outer pure high degree `D`, and the query row is a
  **product** `∏_j row_j` with per-block orders `ord j` such that each `μ_j` kills rows of order
  `< d`, and `∑_j ord j < d·D`, then `⟨ζ, ∏ row⟩ = 0`.*
- `rho_le_four_fifths` — *an arithmetic lemma: given three distinct support points with
  `w_{i1} ≥ (5/4) w_{i0}`, `w_{i5} ≥ (1/4) w_{i0}` and `∑ w = 1`, one has `2 w_{i0} ≤ 4/5`.*
- `block_obstruction_two_blocks` — *assuming `ρ_j ≤ 4/5` for both blocks, `|corr| ≤ 16/25 < 2/3`.*
- `value_budget{,_equal,_q}`, `block_count_bounded_by_q` — *disjoint pair allocations satisfy
  `∑_j r_j ≤ |pairs|`, `|J|·r₀ ≤ |pairs|`, and with `|pairs| = (q−1)/2` the three displayed forms.*
- `orientation_coherence_factor` — *for `r` pairs each carrying `m` uniform ±orientations, the
  fraction of patterns in which all `m` agree on every pair is exactly `2^{−r(m−1)}`.*
- `orientation_obstruction_half` — *given `c ≥ 0` and **either** `c ≤ 2^{r+1−m(r+1)}` **or**
  `c² ≤ 2^{2(r+1−m(r+1))+rm}`, one has `c ≤ 1/2`, for all `r ≥ 2`, `m ≥ 2`.*
- `gauge_term` / `gauge_sum` — *the matrix identity (53), **termwise** as well as summed.*
- `transfer_G2` — *`R_H v = 0` ⇒ `R_G v = 0 = R_G R_H v`*, for arbitrary finite `G` and arbitrary
  **nonempty** `H` (no subgroup structure needed). `reynolds_eq_zero_iff_mem_augment` —
  *for multiplicatively-closed nonempty `H`, `R_H v = 0 ⟺ v ∈ ⟨ρ_h w − w⟩`.*
  `transfer_G2_satellite` — the composite.
- `transfer_G3_nonzero` — *for every nonzero PSD `A`, `R_G(diag A)/tr A` is nonnegative, sums to
  `1`, is `G`-invariant, and has nonzero degree-zero moment*; `transfer_G3_pure_high_degree_zero` —
  *hence its pure high degree is `0`*; `psd_eq_zero_of_trace_eq_zero` — *PSD with zero trace is
  zero.*

### 6.B Diff and verdicts

| LaTeX label / clause | Lean name | verdict | verified (7f) | notes |
|---|---|---|---|---|
| `thm:pair-tensor` | `pair_tensor` (+ `mixture_l1_and_annihilation`, `slice_annihilation`, `admissible_nonempty`) | **NARROWER** | statement + proof read | **CONFIRMED, and I would state it more sharply than the module does.** The paper asserts an `S_N × C(σ)`-invariant signed measure **on `Z_q^N`** annihilating every **query polynomial** of degree `< q−1`. The Lean object lives on the labeled pair-occupancy space; the query-polynomial bridge is `lem:factorial-filtration`, **unformalized**; `S_N`-invariance on strings (the orbit lift) is **unformalized**; the `ℓ¹` identity is on the labeled space, not the occupancy pushforward. What *is* proved — the local kernel's norm/moments, the slice tensor, the mixture, `C(σ)`-invariance (endpoint swap + pair permutation), non-emptiness at `N ≥ q` — is faithful **to the module's declared scope** |
| `thm:tilted-log-band` | `tilt_corr_lower_bound`, `tilt_gap`, `tilt_corr_gt_three_quarters`, `one_sub_sum_le_prod_one_sub` | **NARROWER (severe)** | statement + proof read | **CONFIRMED.** The file states it itself: *"NO theorem in this file is the LaTeX theorem."* The two paper bounds `C_h ≤ 25/19` and `∑_j A_j ≤ 29/23` are **hypotheses**, and the divided-difference construction on `{0,1,5,…,5^{m−1}}`, the ratio computation (44), the activity→falling-factorial transfer, and the `ℓ¹`/invariance bookkeeping are all absent. Correctly self-described, which is why this is a NARROWER and not a DIVERGENT |
| `lem:band-multiplication` (b) | `band_add`, `band_add_three`, `band_add_fin` | **FAITHFUL at the paper's `m`-quantifier** | statement + proof read | `band_add_fin` is genuinely general in `m`; `descFactorial_add` is the Vandermonde of (45). **Caveat:** `ν` is *defined* to be the convolution; the hypergeometric reduction "`S_N`-average of the orbit-lifted product has occupancy pushforward = convolution" is not proved |
| `lem:band-multiplication` (c) | `moment_const_mul`, `band_preserved_by_scaling` | **FAITHFUL** | statement + proof read | |
| `lem:band-multiplication` (a) `ν ≠ 0` | — | **NARROWER: NOT FORMALIZED** | — | **CONFIRMED.** The paper's integral-domain argument on generating polynomials is absent. Since (c) says "normalizing by its actual `ℓ¹` norm is therefore legal", and legality rests on `ν ≠ 0`, this is the clause with the most downstream weight |
| `lem:band-multiplication` (d) common-group invariance | — | **NARROWER: NOT FORMALIZED** | — | **CONFIRMED** |
| `thm:product-obstruction` (47) | `product_obstruction_{exact,ratio,normalized,q}` | **FAITHFUL (with a modelling caveat)** | statement + proof read | the five class conditions map cleanly (2+3 → `IsLocalFactor`, 4 → arbitrary `Ω c`/`axis c`, 5 → the mixture theorems). **Caveat:** condition 1 ("fixed-point occupancy at most one, **so NO is the all-axis event**") enters as the *hypothesis* `hNO`; the Lean therefore does not verify that the paper's class over `Z_q^N` actually satisfies it. The module says so explicitly, which is why I do not downgrade |
| `thm:product-obstruction` (mixtures) | `product_obstruction_mixture{,_normalized,_q}` | **FAITHFUL** | statement + proof read | the mixture **value** (not only the ratio) is machine-checked |
| `thm:block-obstruction` (49) | `block_obstruction_corr`, `block_obstruction_bound` | **FAITHFUL** | statement + proof read | sign convention verified: `sgnNeg μ j y = decide (μ j y < 0)`, so `Ψ (fun _ => true)` **is** `Ψ(−1,…,−1)`. The `OR_m` disambiguation (F-T9) is resolved correctly to the composed problem's ±1 indicator |
| `thm:block-obstruction` (i), degree | `block_obstruction_band` | **NARROWER — NEW FINDING, I DIVERGE FROM THE T3 REPORT** | statement + proof read | The paper says *"`ζ` has pure high degree at least `dD`"*, i.e. **every** falling-factorial row of total order `< dD` is annihilated. The Lean proves it only for rows that are **products** `∏_j row_j` of per-block rows with `∑_j ord j < d·D`. A general row `∏_a (n_a)_{α_a}` on the composed input is a *linear combination* of such products (Vandermonde, which this very development proves as `descFactorial_add`), so the gap is closable by linearity — but it is **not closed in Lean**, and the T3 report grades this theorem FAITHFUL. The module header does disclose the abstraction ("the query row abstracted to a PRODUCT of per-block rows"); the report's verdict table does not carry the disclosure |
| `thm:block-obstruction` (iii), `ρ_j ≤ 4/5` | `rho_le_four_fifths`, `two_block_corr_lt_two_thirds`, `block_obstruction_two_blocks` | **NARROWER — SECOND NEW FINDING** | statement + proof read | The paper's clause is *"for a logarithmic inner from `thm:tilted-log-band` containing at least five complementary pairs, `ρ_j ≤ 4/5`"*. `rho_le_four_fifths` is a pure arithmetic lemma about three weights with two ratio hypotheses, and `block_obstruction_two_blocks` takes `hρ : ∀ j, rho μ blockNO j ≤ 4/5` as a **hypothesis**. The link from the tilted inner to `ρ_j ≤ 4/5` is therefore **not** established — consistently with `thm:tilted-log-band` itself being unformalized |
| `thm:block-obstruction` (50), value budget | `value_budget`, `value_budget_equal`, `block_count_bounded_by_q`, `value_budget_q` | **FAITHFUL** on the two displayed inequalities | statement + proof read | the concluding sentence *"Hence this whole-pair allocation cannot produce the required `√N` growth at fixed `q`"* is **not** formalized — it is the inference that makes (50) an obstruction |
| `thm:orientation-obstruction` (a) | `orientation_coherence_factor`, `orientation_counts`, `card_coherent` | **NARROWER** | statement + proof read | I confirm the T3 report's "clause (a) is proved" **only in the counting sense**: what is proved is that the coherent-orientation event among `2^{rm}` patterns has measure exactly `2^{−r(m−1)}`. That true NO *of the named construction* incurs precisely this factor is a modelling step about the tilted product tensor, and it is not in Lean. A second-order narrowing the T3 report does not record |
| `thm:orientation-obstruction` (b) | `orientation_obstruction_half`, `orientation_bound_{even,odd_sq}`, `orientation_corr_le_half` | **NARROWER** | statement + proof read | **CONFIRMED, unchanged.** `hbound` is literally the paper's displayed bound (51) in its two cases; the analytic norm lower bound that *produces* (51) (endpoint phases, `θ = π/s` or `π/(s+1)`, triangle inequality) is absent. **The kernel does not confirm this obstruction clause.** The arithmetic that *is* checked is correct and covers all `r ≥ 2, m ≥ 2` |
| `prop:transfer-facts` (G1) / (53) | `gauge_term`, `gauge_sum` | **FAITHFUL** (termwise is stronger) | statement + proof read | the prose GT/Jucys–Murphy sentence is not a displayed claim and is not formalized; a `2×2` witness shows the gauge is a genuine freedom |
| `prop:transfer-facts` (G2) | `transfer_G2`, `reynolds_eq_zero_iff_mem_augment`, `transfer_G2_satellite` | **NARROWER (dictionary granted)** | statement + proof read | The paper's hypothesis is *"`v` lies in a nontrivial `H`-satellite"*, defined at (52) as a summand with nontrivial `U_λ`. The Lean's is *`v ∈ augment ρ H = ⟨ρ_h w − w⟩`*. These coincide **by Maschke in characteristic zero**, which is **not** formalized. The 2026-07-30 repair correctly upgraded an assumed `R_H v = 0` to a proved characterization; but the remaining step is a definitional substitution, so I record NARROWER where the T3 report records FAITHFUL. Rule 7g: the term "satellite" resolves to (52) in the paper and to `augment` in Lean — two definitions, one unformalized bridge |
| `prop:transfer-facts` (G3) / (54) | `transfer_G3_nonzero`, `transfer_G3`, `transfer_G3_pure_high_degree_zero`, `psd_eq_zero_of_trace_eq_zero` | **FAITHFUL** | statement + proof read | the repair is real and correct: PSD with zero trace is zero, so the theorem now stands at the paper's own "every **nonzero** PSD `A`". Nonnegativity, unit total, `G`-invariance, and pure-high-degree-zero are all present |
| `lem:factorial-filtration` | — | **NOT FORMALIZED** (declared; node `KSUM.B4b.L2.FILT` registered 2026-07-30) | — | this is the bridge that makes `thm:pair-tensor` and `thm:tilted-log-band` statements about **query** degree; its absence is the root cause of the T3 headline NARROWER |
| `prop:joint-lp` | — | **NOT FORMALIZED** (declared; node `KSUM.B4b.L2.JOINTLP`) | — | exact LP optima delegated to an ancillary script; no dual certificates printed |

### 6.C Diff against the T3 executor's own table (read last, per 7c)

- **Agreement:** the four NARROWER verdicts the report headlines — `thm:pair-tensor`,
  `thm:tilted-log-band`, `lem:band-multiplication` (a)/(d), `thm:orientation-obstruction` (b) — are
  **each independently confirmed**, on grounds I derived from the Lean sources before reading the
  report. Coincidence of wording ("occupancy level", "the analytic step that produces (51)") is
  disclosed here as required; the substance was independently derived.
- **Divergence (three items).** I grade **NARROWER** where the report grades FAITHFUL, on:
  `thm:block-obstruction` clause (i) (product-row abstraction); `thm:block-obstruction` clause
  (iii) (`ρ_j ≤ 4/5` assumed, not derived from the tilted inner); and `prop:transfer-facts` (G2)
  (satellite ↦ augmentation submodule, Maschke granted). I also add a second-order narrowing on
  `thm:orientation-obstruction` clause **(a)**, which the report treats as fully proved.
- **Net:** the tier's NARROWER count rises from **4 labels** to **6 labels / 9 clauses**. None of
  the additions is a WIDER or DIVERGENT; every one is under-delivery, which is the safe direction
  for positive claims and — for the *obstruction* clauses (orientation (a),(b); block (i),(iii)) —
  means those obstructions are **not** machine-confirmed. The report's headline sentence *"the two
  obstruction theorems whose class boundary is the whole point … are FAITHFUL"* should be read as
  applying to `thm:product-obstruction` and to `thm:block-obstruction`'s **correlation identity
  (49)** only.

---

## 7. DUTY 5 — VACUITY AND SATISFIABILITY

### 7.1 (a) `demoModel` — is `QueryModel` inhabited **non-degenerately**?

`demoQ f = 0` if `f` is constant, else `√M · M^{1/6}` where `M` is the **input length**.

- **It is a legitimate consistency witness.** `restrict` and `relabel` hold because the length is
  unchanged and `demoQ ≤ B(M)` always; `freeze` because `B` is monotone in the length; `constQ` by
  construction; `abi`/`tani` because `Claw n κ` is nonconstant for `2 ≤ κ`, `1 ≤ n` (proved as
  `Claw_nonconst`) and `√n·κ^{1/6} ≤ √(2n)·(2n)^{1/6}` when `κ < 2n`. I verified each of the six
  field proofs.
- **Is it degenerate in a way that would signal the fields are weaker than the cited theorems?**
  **No, but with two honest qualifications.**
  (1) The field set contains lower bounds on `Q` (`abi`,`tani`) and upper bounds on `Q` of derived
  functions (`restrict`,`relabel`,`freeze`). A measure that is large on every nonconstant function
  and monotone in length satisfies both families. That the witness is *coarse* (it sees only
  constant-vs-nonconstant and the length) shows the field set is **loose**, not that any individual
  field is weaker than its cited theorem — I checked each field against `sec:prelim`/ABI/Tani in
  §3.B and found no weakening.
  (2) **The factor `2` of `relabel` is never exercised** by the witness: `demoQ(f∘e) ≤ demoQ(f)`,
  i.e. the witness satisfies `relabel` with constant `1`. So `demoModel` gives no evidence about
  whether the factor-2 slack is needed. Since every theorem consumes `relabel` in the `≤ 2·` form,
  this is harmless, but it should not be mistaken for a check on the constant.
- **The standing open obligation, stated as this node's text requires.** `demoModel` settles
  question (a) — *is the field set consistent?* — and settles **nothing** about question (b) —
  *does the true bounded-error quantum query complexity satisfy these fields?* That question is not
  settleable without formalizing the query model itself (node
  `KSUM.LEAN.ALT.full-query-model`, PARKED). **`demoModel` is not quantum query complexity and the
  module says so; every T1 / T2-transfer / A1 / A2 / B2 / B4 result is conditional on the cited
  literature and on the two unstated facts F1/F2.**
- **Sanity check that the conditional theorems have content in the witness.** `KSUM.A1.holds
  demoModel` yields `A·√N·q^{1/6} ≤ demoQ(kSum)` with `A = 1/(4√3·(2k²)^{1/6}) < 1` and `q ≤ N`;
  since `demoQ ∈ {0, N^{2/3}}`, the theorem *forces* `kSum` to be nonconstant in that regime — an
  internally consistent, non-trivial consequence. The composition is not vacuously true.

### 7.2 (b) `EmbedData` — witness search (R-A2-3)

**CONFIRMED: `KSUM.Support.EmbedData` has NO instance anywhere in the development.** I grepped
every `.lean` outside `.lake/` for `EmbedData where`, `: EmbedData :=`, `instance … EmbedData`,
`def … : EmbedData`: the only hit is the `structure EmbedData where` declaration itself.

**Consequence, which must be stated on the nodes.** `KSUM.A2a.Claim`, `KSUM.A2b.Claim`,
`KSUM.A2.Claim` and `KSUM.B2.Claim` all begin `∀ D : EmbedData, …`. If `EmbedData` were
uninhabited, **all four are vacuously true and `KSUM.A2.composition` and `KSUM.B2.composition`
carry no content whatsoever**. Nothing on disk rules this out.

**It is easy to rule out, and I checked the arithmetic.** The instance suggested in the T2 report
is valid: `k=3, n=1, R=2, P=12, Mv=24, cP=3`, giving `q = 13·25 = 325`, and
`enc p a = ((a : ℕ) : ZMod 325)` is injective at every position. Check: `3 ∣ 12` ✓;
`2(24+1) = 50 = 7² + 1` ✓; `R^{k−1} = 4 ≤ 12 = P` ✓; `P = 12 ≤ 3·4 = cP·R^{k−1}` ✓; `3 ≤ k`,
`1 ≤ n`, `2 ≤ R` ✓. **What would establish non-vacuity: adding this one `def demoEmbed :
EmbedData := …` (six lines) plus a `#print axioms` line.** Until then the A2/B2 branch of the
composition layer is *machine-checked but not machine-checked to be about anything*.

### 7.3 (c) `KSUM.B4.B4bClaim` after the restriction to odd `5 ≤ q ≤ N`

- **The `q = 2` vacuity is genuinely fixed.** I re-derived the defect: at `q = 2`, `t = 0`,
  `N ≥ 3`, pigeonhole gives `i ≠ j` with `x_i = x_j`, and `2x_i = 0` in `Z_2`, so `2Sum ≡ true` and
  `Q = 0` in any faithful model, contradicting `c·√N·2^{1/4} > 0`. Restricting to `q` odd with
  `5 ≤ q ≤ N` removes it.
- **Non-degeneracy of the new regime.** I checked that `2Sum_{Z_q,t,N}` is genuinely nonconstant
  throughout it: for `q` odd `≥ 5`, `2v = t` has a unique solution, so a constant string at any
  `v ≠ t/2` is a NO instance, and `x = (a, t−a, …)` with `2a ≠ t` is a YES instance. So no
  constant-function collapse survives.
- **Satisfiability of `B4bClaim` itself was NOT established, and this review does not establish
  it** — the bound `c·N^{1/2}q^{1/4} ≤ Q(2Sum)` *is* the open `k=2` lower bound. What is at issue
  for §7.10(5) is the weaker and decidable question: **is `KSUM.B4.composition` non-vacuous, i.e.
  are `B4a.Claim M` and `B4bClaim M` jointly satisfiable for some `M : QueryModel`?**
- **What would establish it, concretely (I verified the arithmetic).** `demoModel` does **not**
  work: at `q ≈ N` its `N^{2/3}` falls below `c·N^{1/2}q^{1/4} ≈ c·N^{3/4}`. An **alphabet-aware**
  witness does: set `Q(f) = 0` if `f` is constant, else `M^{1/2}·A^{1/4}` where `M` is the length
  and `A = max_i |Alph i|`. Then `restrict` holds (restriction shrinks `A`, keeps `M`); `relabel`
  holds with constant `1` (equivalences preserve cardinality); `freeze` holds (`M ≤ M+1`, alphabets
  unchanged); `constQ` by construction; `abi`/`tani` hold with `cABI = 1` because
  `(2n)^{1/2}κ^{1/4} ≥ n^{1/2}κ^{1/6}` for `κ ≥ 2`; `B4a.Claim` holds with `C_ε = 1`; and
  `B4bClaim` holds with `c = 1`. **Adding that model would discharge the non-vacuity of
  `KSUM.B4.composition` in one module.** Recorded as the concrete repair.

### 7.4 (d) T3 non-vacuity witnesses — sample of six (G-T3d)

I did not accept the T3 report's G-T3d PASS; I re-read the witnesses in the sources.

| theorem | witness on disk | verdict |
|---|---|---|
| `orientation_coherence_factor` | `example : (piFinset (fun _ : Fin 2 => coherent 2)).card / 2^4 = 1/4`, plus `(coherent 2).card = 2` and the even-`s` value `1/8` | **PASS** — smallest legal instance `q=5 (r=2), m=2`, both the ratio and the two card facts |
| `pair_tensor` / `slice_annihilation` | `admissible (r:=1) 3` nonempty; `∑_x \|prodKappa x\| = 1` at `r = 1` and `r = 3`; `kappa_l1 ∧ kappa_total`; a concrete `q=5, r=2` slice cancellation at order `3 < 4` | **PASS** — includes a *negative-direction* check (the kernel is nonzero with the claimed norm) |
| `band_add` / `band_add_fin` | one-block measure `wOcc/wMu` with band exactly `1` (`wNonzero : moment = −1 ≠ 0`, so the band is **tight**), two-block instance, and a five-block instance of `band_add_fin` | **PASS** — and it is the right shape: it certifies the *hypotheses* are satisfiable by a **genuinely nonzero** measure, which is the failure mode here |
| `product_obstruction_*` | witnesses present in `ObstructionsProduct` (2 examples) | **PASS** |
| `tilt_corr_*` | `2/(1 + (25/19)(29/23)) = 437/581` exactly — i.e. **the hypotheses are attained**, so the bound is tight, not vacuous | **PASS** |
| `transfer_G2` / `G3` | witnesses added by the T3 run (3 in `ObstructionsTransfer`), including the first for G2 | **PASS** |

**One gap.** `KsumAudit.KFloor.core_reduction_at`'s four witnesses (`witness_even_{pos,neg}`,
`witness_odd_{pos,neg}` at `k=3, K=2, q=19`) are all at **`r = 0`** — they instantiate
`core_reduction`, the base-target corollary, not the general-`r` theorem. The generalized target is
the whole point of the repair batch, so **a witness at `r ≥ 1` (e.g. `r = 2`, `q = 19`) is owed.**
Non-vacuity of the general statement is not in doubt (its hypotheses admit `r = 0`), but the
repair's *new content* has no witness.

**Overall vacuity verdict:** T1 non-vacuous (`demoModel`); T2/T3 unconditional and witnessed;
**A1 group non-vacuous and machine-checked so** (all three child Claims are theorems, F-R8 closed —
I confirm this, see §8); **A2/B2 non-vacuity UNVERIFIED (no `EmbedData` witness)**; **B4
composition non-vacuity UNVERIFIED (no model satisfying both sides)**.

---

## 8. QUEUED ITEMS (i)–(v), each answered explicitly

**(i) T1 findings F1–F7.** F1 (`freeze`) and F2 (`constQ`) are the only two interface fields the
paper does not state; both are flagged in the field docstrings, in `KSUM/Interface.lean`'s citation
table, in `KSUM/Trust.lean` §(b), and in `KSUM.LEAN`'s Open obligations. **No third unstated field
exists** (enumeration in §3.B). F3 (`κ ≥ 2` unused in `lem:encode`) and F4 (`p` prime unused in
`thm:oabarrier`(ii)) are confirmed and are strengthenings. F5 (position-dependent alphabets make
the composite a theorem, `relabel_inj`) is confirmed and is the right design. **F6 and F7 I
re-derived independently and both hold** (§4.B). The hidden `c`-dependence (`5 ≤ cN`) is real and
visible in `threshold_small`'s hypotheses. **Refinement on F1:** the missing principle is precisely
*singleton-coordinate deletion*, not domain restriction (§3.B(c)).

**(ii) T3's four NARROWER verdicts.** All four **confirmed** (§6.B), on independently derived
grounds. **Revised upward:** I add three more NARROWER clauses (`thm:block-obstruction` (i) and
(iii), `prop:transfer-facts` (G2)) and one second-order narrowing (`thm:orientation-obstruction`
(a)). **Are they recorded on the audited nodes rather than only in artifacts?** Partly:
`KSUM.B4b.L2.ORIENT` carries a dated partial-confirmation note ("clause (a) machine-checked; clause
(b) only as '(51) ⇒ ≤1/2'") — good. `KSUM.B4b.L2.M1` (pair-tensor), `KSUM.B4b.L2.L2P3`
(tilted-log-band) and `KSUM.B4b.L2.BANDMULT` carry the NARROWER only through the tier node and the
artifact, not as their own dated notes; and the three new narrowings I add are recorded nowhere.
**Recorded as honesty item H-8.**

**(iii) T2's declared gaps.** Confirmed exactly as declared; the every-window-target repair is
genuinely **implemented** in `core_reduction_at` and consumed by `KSUM.A1a.Claim` (§5.B).

**(iv) The repaired `A1a`/`A1c` Claim texts — first independent read.** I read both in full and
checked them against the composition-layer review §3.1's prescriptions **and** against the
manuscript lemmas.

- `KSUM.A1a.Claim` — **every-window-target quantifier PRESENT**
  (`baseTarget k κ ≤ s → s < baseTarget k κ + k`), **parked coordinate PRESENT** (`k−2 ≤ m ≤ k−1`),
  and it is **proved** by `holds` from `core_reduction_at`, unconditionally. Against
  `prop:core-even`/`lem:core-odd` it is NARROWER in the three ways listed in §5.B, all safe. Its
  window hypothesis is the manuscript's `(k²−2)κ + 2k−1 ≤ q`, **not** the looser `2κ+1 ≤ q`; the
  module's own note that quantifying over all `κ` with `2κ+1 ≤ q` would have been *stronger than
  the paper* (and would silently vacuate the composition) is correct and is the single best piece
  of self-audit in this development.
- `KSUM.A1c.Claim` — **coset membership PRESENT** (`((s:ℕ) : ZMod q) = t + k • a`), **explicit `/C`
  constant PRESENT** (`∃ C, 0 < C ∧ … Q(kSum_s) ≤ C·Q(kSum_t)`), **window bounds on `s` PRESENT**,
  and it is **proved** by `holds` with `C = 2`. Against `lem:transl-cover` this is **FAITHFUL**.
  The refuted all-pairs rendering survives, unproved and consumed by nothing, as `ClaimAllPairs`,
  beside the in-range obstruction `not_reachable_k3_q21` (which I verified is in range:
  `2·3²+2·3−5 = 19 ≤ 21`).
- **VERDICT: the two repaired Claim texts do meet the reviewer's prescriptions.** The lead's
  2026-07-31 write of `KSUM.A1 → PROVED` is therefore **substantively correct**. **Procedural
  caveat (recorded, not a mathematical objection):** that write was made *before* any independent
  instance had read the repaired texts — the license was conditional on repairs whose discharge was
  verified only by the lead. This review supplies the missing independent read, after the fact.

**(v) Claim-hash agreement (§7.6 check 3) — I hashed all 12 node/module pairs, not 4.**
Convention as declared (the `## Claim` section body, UTF-8, LF, `str.strip()`, SHA-256):

| node | computed | recorded (Lean docstring / node YAML) | |
|---|---|---|---|
| `KSUM.A1a` | `5a70591b…` | `5a70591b…` / `5a70591b…` | **OK** |
| `KSUM.A1b` | `827117dd…` | `827117dd…` / `827117dd…` | **OK** |
| `KSUM.A1c` | `ed56ed4d…` | `ed56ed4d…` / `ed56ed4d…` | **OK** |
| `KSUM.A1d` | `5306ca60…` | `5306ca60…` / `5306ca60…` | **OK** |
| `KSUM.A1` | `c9f8aa1f…` | `c9f8aa1f…` / `c9f8aa1f…` | **OK** |
| `KSUM.A2` | `7f375f3d…` | `7f375f3d…` / `7f375f3d…` | **OK** |
| `KSUM.A2a` | `4cb82063…` | `4cb82063…` / `4cb82063…` | **OK** |
| **`KSUM.A2b`** | **`e1154f27…`** | **`fe3f827d…` / `fe3f827d…`** | **MISMATCH** |
| `KSUM.B4a` | `12b8db15…` | `12b8db15…` / `12b8db15…` | **OK** |
| `KSUM.B4` | `71c30233…` | `71c30233…` / `71c30233…` | **OK** |
| `KSUM.B2` | `a25606dc…` | `a25606dc…` / `a25606dc…` | **OK** |
| `KSUM.goal` | `61adf071…` | `61adf071…` / `61adf071…` | **OK** |

Plus `KSUM.B1` (no module, but a `claim_hash` in its `lean:` block): computed `aa324409…`,
recorded `4d8818e1…` — **MISMATCH**. Both mismatches are emitted by
`tools/proof_dag_check.py` as **warnings** (exit 0), so the repeated campaign statement "validators
exit 0" is true and simultaneously conceals two live §7.6 anti-drift breaks. Details in §9.

---

## 9. DUTY 6 — HONESTY OF THE RECORD

### 9.1 What is exemplary (state this first, because the failures below are all staleness)

- **§7.9 scope clauses are present verbatim** in `ksum/lean/README.md`:
  *"A theorem proved against an abstract interface is exactly as strong as the results that
  interface cites, and not one notch stronger."* and *"`lean-checked` is an evidence attribute,
  never a status."* Both exact.
- The README's "What a green build here does **not** establish" list, `KSUM.LEAN`'s five scope
  clauses, `KSUM/Trust.lean`'s trust boundary, `KSUM/Interface.lean`'s per-field citation table,
  and the **PROSE ↔ `Claim` DIFF** section in every node module are, collectively, the strongest
  anti-overclaim apparatus I have reviewed. **I found no wording anywhere that implies the original
  theorem is verified where only a relative composition was checked.** `KSUM/B2.lean`'s named gap
  ("a green build of `composition` proves the transport, NOT that the transported bound is new")
  and `KSUM/goal.lean`'s refusal to declare a content-free modus-ponens schema are both correct
  calls that a less careful development would have got wrong.
- All three tier nodes sit at **NUMERICAL** with an explicit
  `pending-review: KSUM.LEAN.statement-fidelity` marker in `status_source` and in the body. Correct
  under §2/§7.1.
- The forwarding stub at `ksum/lean/README.md` is present and accurate.

### 9.2 Honesty defects found (all staleness or drift; none overstates what was verified)

- **H-1 (README, material).** *"It does not establish the leaf claims. `KSUM.A1a`, `KSUM.A1c`,
  `KSUM.A2a`, `KSUM.A2b`, `KSUM.B4a` are STATED as `Prop`s and used as hypotheses. `KSUM.A1b` is
  the one exception."* — **false on disk since the T2 tier and the repair batch**: `KSUM.A1a.Claim`
  and `KSUM.A1c.Claim` are **proved** (`A1a.holds`, `A1c.holds`). The error is conservative
  (understates), but a reader would draw the wrong conclusion about what the A1 group now delivers.
- **H-2 (README, material).** The `KsumAudit/` table still labels `Obstructions*.lean` as
  **"UNVERIFIED, UNADOPTED … Node `KSUM.LEAN.T3.obstruction-theorems` stays OPEN"**, and the
  Mechanization-tier paragraph says they "would be §7.8 T2 … but they are **not adopted**". T3
  landed on 2026-07-30 with ADOPT 44/0/0 and the node is NUMERICAL·pending-review.
- **H-3 (README, omission).** The two tier-T2 modules `KsumAudit/T2KFloor.lean` and
  `KsumAudit/RosmanisBarrier.lean` do not appear in the README at all — neither in the module
  table nor in the tier statement.
- **H-4 (anti-drift, §7.6 check 3).** `KSUM/A2b.lean` prints, under the heading *"FROZEN CLAIM
  (verbatim from the `## Claim` section of the node file)"*, the superseded text
  *"all wrong block-multisets excluded (balanced base-ω) + 62,140 exhaustive checks
  [PROVED + NUMERICAL]"*. The node's `## Claim` was rewritten by the 2026-07-30 composition-layer
  review application (the 62,140 checks were moved into a parenthetical) and now hashes
  `e1154f27…`, while both the Lean docstring and the node's `lean.claim_hash` record `fe3f827d…`
  with `synced: "2026-07-30"`. **The word "verbatim" is now false**, and the `synced` field asserts
  a sync that did not happen. Mathematically harmless (the Lean `Claim` still renders the PROVED
  half correctly), but this is exactly the drift the hash mechanism exists to catch.
- **H-5 (anti-drift + stale reason).** `KSUM.B1`'s `claim_hash` (`4d8818e1…`) records the
  pre-rewrite Claim (`synced: "2026-07-30"`), while the current Claim hashes `aa324409…`. Worse,
  its `lean.reason` still reads *"B1s Claim is a strategy description, not a proposition. No module
  written."* — **contradicted by its own file**, whose Claim was rewritten into a proposition on
  2026-07-30 and whose `status_source` now says the route proof "is statable and near-trivial".
- **H-6 (prose/Lean divergence, self-declared).** `KSUM.B4`'s frozen `composition.claim` states no
  `q`-range, while the mechanized `B4bClaim`/`Claim` are scoped to `q` odd with `5 ≤ q ≤ N`. The
  node's Open obligations record the owed prose repair, so this is disclosed — but until it lands,
  the frozen prose and the Lean say different things.
- **H-7 (label precision).** `KSUM/Trust.lean` §(e)'s T2 table row for `lem:core` reads
  `sum_coreIdxAt … FAITHFUL (2026-07-30: every window target)`. That is true of the *whole-core-sum*
  sub-clause only; `lem:core`'s subset-range clause remains base-target-only (§5.B). As written the
  row can be read as "`lem:core` is now FAITHFUL".
- **H-8 (findings not on the audited nodes).** The T3 NARROWER verdicts for `thm:pair-tensor`,
  `thm:tilted-log-band` and `lem:band-multiplication` live in the tier node and the artifact but
  not as dated notes on `KSUM.B4b.L2.M1` / `.L2P3` / `.BANDMULT` (contrast `ORIENT`, which does
  carry one). The three additional narrowings this review finds are recorded nowhere yet. Rule 8c
  places these on the nodes when read.
- **m-1/m-2** (§2.2): `Trust.lean`/README say `#print axioms` covers "every top-level declaration"
  (it is 176/235, sound but imprecisely described); three culminating-looking declarations are
  absent from the manifest.

**HONESTY VERDICT: FAIL — on record-accuracy, not on scope-overstatement.** Eight defects, every
one a staleness or drift defect, and every one erring in the *conservative* direction (the record
claims less than the disk delivers, or quotes a superseded text). The load-bearing question of
§7.10(6) — *does any wording imply the theorem is verified where only a relative composition was
checked?* — is answered **NO**, emphatically. The FAIL is repairable by one small documentation
batch (README items H-1/H-2/H-3, two hash re-syncs H-4/H-5, one `lean.reason` rewrite, one Trust
row, and the node notes of H-8) and impugns none of the mathematics.

---

## 10. PER-TIER ROLLUPS

**T1 — `KSUM.LEAN.T1.k2-main-line`: PASS-WITH-CAVEATS.**
The tier's Lean content faithfully renders what its node claims it renders: `lem:encode`,
`lem:oddN`, `lem:shift`, `thm:main-odd`, `thm:main-general`, `cor:threshold`, `thm:oabarrier`.
Caveats: (1) `cor:threshold`'s `Θ_c` is formalized on the **lower** side only — the matching
`O(N^{2/3})` is out of scope and declared; (2) `thm:oabarrier`(ii)'s `Q = 0` conclusion is not
stated (only the constancy); (3) the `restrict` field is narrower than fact (i) (product subdomains
— safe, and sufficient for every use); (4) `lem:shift`'s `Θ` is rendered one-sided; (5) two
interface fields (`freeze`, `constQ`) are **not in the manuscript** and are carried honestly as
fields — the tier is conditional on more than the paper admits, and says so; (6) `demoModel`
settles consistency only.

**T2 — `KSUM.LEAN.T2.rosmanis-kfloor`: PASS-WITH-CAVEATS.**
Unconditional (no `QueryModel` in either module — verified: neither imports it). Caveats:
(1) `lem:core`'s subset-range clause is base-target-only; (2) `prop:core-even`/`lem:core-odd` are
proved on the `k`-element sub-window `[t₀, t₀+k)` under the stronger odd-case modulus condition,
with the conclusion one `lem:encode` step short of `Claw` — all three safe and exactly what the
covering consumes; (3) `prop:rosmanis`(1)'s bijection and count formula are **not** formalized
(only `≥ 2`, orbit-properly); (4) `prop:rosmanis`(2)'s representation-theoretic sentence is not
formalized (only the two witnesses); (5) `C(σ) ≅ (C₂≀S_m)×S_τ` and `prop:embed` are not formalized;
(6) `core_reduction_at`'s new general-`r` content has no witness at `r ≥ 1`.

**T3 — `KSUM.LEAN.T3.obstruction-theorems`: PASS-WITH-CAVEATS.**
Unconditional. Caveats — **six labels / nine clauses NARROWER**, two more than the tier's own
report: `thm:pair-tensor` (occupancy level; no measure on `Z_q^N`, no `S_N`-invariance, no query
polynomials — the `lem:factorial-filtration` bridge is unformalized); `thm:tilted-log-band`
(**no theorem in the module is the paper theorem** — only its closing arithmetic, under the paper's
two bounds as hypotheses); `lem:band-multiplication` clauses (a) and (d) unformalized and `ν`
defined rather than derived; `thm:orientation-obstruction` clause (b) **assumes** the displayed
bound (51) and clause (a) is proved only as an orientation-counting identity; `thm:block-obstruction`
clause (i) proved only for **product** rows and clause (iii)'s `ρ_j ≤ 4/5` **assumed**;
`prop:transfer-facts` (G2) proved with "satellite" replaced by the augmentation submodule (Maschke
granted). `thm:product-obstruction`, `thm:block-obstruction` (49), `prop:transfer-facts` (G1) and
(G3), and `lem:band-multiplication` (b)/(c) are FAITHFUL. Two in-scope labels
(`lem:factorial-filtration`, `prop:joint-lp`) are unformalized, now with nodes.
**Consequence to state plainly: of the obstruction clauses, the kernel confirms
`thm:product-obstruction` and the block correlation identity; it does not confirm the orientation
obstruction, the block degree/`ρ` clauses, or the tilted-band witness.**

**KSUM composition layer: PASS-WITH-CAVEATS.**
The four composition theorems are machine-checked and their hypothesis sets match the nodes'
declared `composition` blocks (I checked gate G-R3 myself for each). `KSUM.A1.composition` +
`KSUM.A1.holds` are the substantive result: all three child Claims are theorems, so
**finding F-R8 is genuinely CLOSED, not narrowed** — I confirm this independently. Caveats:
(1) `KSUM.B4a.Claim` is **WIDER** than `thm:k2-upper` (drops the paper's `q ≥ 2`) — benign, since
`B4.Claim` only uses it at `5 ≤ q ≤ N`, but it is an interface over-assumption in a hypothesis and
should be closed; (2) `KSUM.B2.DonorClaim` types the donor bound as `L : ℕ → ℕ → ℝ` with **no `k`
argument**, so it demands one `L` uniform in `k` — a real narrowing of `B2.Claim`;
(3) `KSUM.A2.Claim`'s `Θ_k(R^{k−1})` is per-`EmbedData`-instance rather than uniform in `R`
(self-declared as the one place the Claim is weaker than the frozen prose — **confirmed**);
(4) `KSUM.A1d.Claim`'s plateau clause is nested under `q ≤ C_k·N`, whereas `thm:kfloor` states the
plateau "for every `q ≥ c_k N`" without a ceiling — NARROWER, safe; (5) the A2/B2 branch has **no
`EmbedData` witness** and the B4 sandwich has **no jointly-satisfying model** (§7.2, §7.3);
(6) `KSUM.k3.donor` and `KSUM.B4b` have no modules and enter as written-out hypotheses — a declared
§7.3 deviation; (7) `KSUM.goal` is claim-free with a reason, which is the correct §7.4 record.

---

## 11. STANDING CONDITIONALITY (stated explicitly, as this node's Open obligations require)

**`QueryModel` inhabitation by the true `Q` is OPEN and is not provable in this development.**
`KsumAudit.demoModel` proves the field set is *consistent*; it proves nothing about bounded-error
quantum query complexity, and it is not a claim to. Settling whether real `Q` satisfies these
fields requires formalizing the quantum query model itself — the deliberately-not-taken road
recorded as `KSUM.LEAN.ALT.full-query-model` (OPEN · PARKED).

Therefore:

- **Conditional on the cited literature and on the two unstated facts F1/F2:** everything in
  **tier T1**; the three interface-relative results in `KSUM/A1c.lean`
  (`Q_kSum_translate_le`, `Q_window_cover_coset`, `Q_le_of_coprime`); `KSUM.A1.composition` and
  `KSUM.A1.holds`; `KSUM.A2.composition`; `KSUM.B2.composition`; `KSUM.B4.composition`. Each is
  **exactly as strong as ABI21 + Tani24 + `sec:prelim` facts (i)/(ii) + the unstated
  coordinate-freezing and constant-function principles, and not one notch stronger.**
- **Unconditional (no `QueryModel`, no interface hypothesis of any kind — verified by import
  inspection):** all of **tier T3**; and the tier-T2 cores in `KsumAudit/T2KFloor.lean` and
  `KsumAudit/RosmanisBarrier.lean`.

---

## 12. RECOMMENDED ACTIONS FOR THE LEAD (no status is written by this review)

1. **Documentation batch** closing H-1 … H-8 and m-1/m-2. Low cost, and it is what a FAIL on
   §7.10(6) requires.
2. **Two hash re-syncs** (`KSUM.A2b`, `KSUM.B1`) plus `KSUM.B1`'s stale `lean.reason`; consider
   promoting `frozen-Claim hash drift` from *warning* to *error* in `tools/proof_dag_check.py`,
   since a warning that is routinely reported as "validators exit 0" is not a gate.
3. **Three cheap non-vacuity closures**, each a few lines: `demoEmbed : EmbedData` (§7.2); an
   alphabet-aware witness model for the B4 sandwich (§7.3); a `core_reduction_at` witness at
   `r ≥ 1` (§7.4).
4. **Record on the audited nodes** (rule 8c) the three additional T3 narrowings found here —
   `thm:block-obstruction` (i) and (iii), `prop:transfer-facts` (G2) — and the second-order
   narrowing on `thm:orientation-obstruction` (a); and close `B4a.Claim`'s dropped `q ≥ 2`.
5. **Manuscript-repair batch** already queued is unaffected and remains owed (F1 with the
   §3.B(c) refinement, F2, F5, F6, the `5 ≤ cN` sentence, F-T9, ORIENT (51), `prop:joint-lp` dual
   certificates, the `KSUM.LEAN` census table).

---

**Counting unit** for the tally below: one row per (LaTeX label or node id) × clause ruled on in
§3.B, §4.B, §5.B, §6.B and §10 — 42 FAITHFUL (6 interface + 11 T1 + 10 T2 + 8 T3 + 7 KSUM-layer),
23 NARROWER (1 + 3 + 6 + 9 + 4), 1 WIDER, 0 DIVERGENT, 12 infrastructure/not-a-paper-claim, plus 4
labels declared unformalized (`prop:embed`, `C(σ) ≅ (C₂≀S_m)×S_τ`, `lem:factorial-filtration`,
`prop:joint-lp`).

`FIDELITY RESULT: build 0/3011 | census clean | theorems: F 42 / N 23 / W 1 / D 0 / infra 12 | tier rollups: T1 PASS-WITH-CAVEATS T2 PASS-WITH-CAVEATS T3 PASS-WITH-CAVEATS KSUM-layer PASS-WITH-CAVEATS | honesty FAIL | headline: the Lean says what the paper says wherever it speaks — 42 faithful renderings, one WIDER (B4a drops q≥2), zero DIVERGENT — but it speaks about strictly less than the manuscript in 23 places, notably four T3 obstruction clauses the kernel does NOT confirm and three vacuity questions (EmbedData, the B4 sandwich, the true Q) that remain open, and the record itself carries eight staleness/drift defects including two live frozen-Claim hash breaks.`
