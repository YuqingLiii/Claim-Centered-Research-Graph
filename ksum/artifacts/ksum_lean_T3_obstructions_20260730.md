# k-Sum tier T3 — Lean audit of the obstruction / negative-result group

**Date:** 2026-07-30 · **Role:** executor · **Target node:** `KSUM.LEAN.T3.obstruction-theorems`
**Sources:** [`ksum/lean/KsumAudit/Obstructions*.lean`](../ksum/lean/KsumAudit/)
**Evidence:** [`ksum/artifacts/logs_ksum_lean_T3_20260730/`](logs_ksum_lean_T3_20260730/)
(`build.log`, `print_axioms.txt`, `SHA256SUMS.txt`)

---

## HEADLINE — the four NARROWER verdicts (G-T3c), read this first

The commission says a NARROWER verdict is the most important possible outcome of the audit.
There are **four**, and it matters a great deal that **none of them is quantifier drift in the
manuscript**. All four are *formalization-coverage* gaps — but exactly one of them sits on an
**obstruction**, and that one is the finding a reviewer should weigh hardest.

| LaTeX target | Node | Why NARROWER | Direction of the risk |
|---|---|---|---|
| `thm:orientation-obstruction` **clause (b)** | `KSUM.B4b.L2.ORIENT` | Lean takes the paper's displayed bound (51) as a **hypothesis** and derives `corr ≤ 1/2` from it. The analytic step that *produces* (51) — the endpoint-phase generating-polynomial evaluation and the triangle-inequality norm lower bound — is unformalized (§6.4). Clause (a) (`2^{-r(m-1)}`) IS proved outright. | **This is an obstruction — a universally quantified impossibility.** So here "narrower" means the Lean tier does **not** confirm the paper's clause (b); it confirms only that (51) ⇒ `≤ 1/2`. **Escalate this one.** |
| `thm:pair-tensor` | `KSUM.B4b.L2.M1` | Lean proves annihilation of **falling-factorial occupancy rows** of order `< q-1`, and the measure lives on the **labeled pair-state space**, not on `ℤ_q^N`. The paper's conclusion is about **query polynomials** and an `S_N × C(σ)`-invariant measure on `ℤ_q^N`. The bridge is `lem:factorial-filtration`, which is NOT formalized (§6.1). | EXISTENCE claim, so "narrower" means the audit delivers **less** than the paper asserts. Not evidence against the paper. |
| `thm:tilted-log-band` | `KSUM.B4b.L2.L2P3` | No theorem in the module is the LaTeX theorem. Only the Weierstrass inequality and the closing numeric chain `2/(1+C·S) ≥ 437/581 > 3/4` are proved, **with `C ≤ 25/19` and `S ≤ 29/23` as hypotheses**. The divided-difference band on `T_m = {0,1,5,…,5^{m-1}}` — the actual content — is unformalized (§6.3). | Same direction: existence claim, audit under-delivers. |
| `lem:band-multiplication` | `KSUM.B4b.L2.BANDMULT` | Clauses (b) and (c) are now FAITHFUL **at the paper's own `m`-quantifier** (this run's `band_add_fin`; the draft had only `m = 2, 3`). Clause (a) `ν ≠ 0` and clause (d) common-value-group invariance are unformalized, and the hypergeometric reduction "`S_N`-average of the orbit-lifted product = convolution" is taken as the **definition** of `ν` (§6.2). | Positive/tool claim: audit under-delivers. |

**No WIDER-in-a-dangerous-direction and no DIVERGENT verdict was found.** In particular the two
obstruction theorems whose *class boundary* is the whole point — `thm:product-obstruction` (M2)
and `thm:block-obstruction` (T4/VBUD) — are FAITHFUL, and the product one is checked at a
strictly **wider** class than the paper's (§4.2), which is the safe direction for an
impossibility statement. Both (G2) and (G3) of `prop:transfer-facts` were NARROWER **as drafted**
(a substituted hypothesis in each) and were repaired to FAITHFUL by this run — see F-T3 and F-T8,
which are the two places the draft had quietly weakened a paper hypothesis.

---

## 0. PRE-ACTION REPORT (per `research/PRETASK_RELOAD_PROMPT.md`)

**Files read from disk, completely, before any math, code, or edit**, in order:
`research/PRETASK_RELOAD_PROMPT.md`; `DAG_PROTOCOL.md` (whole file; §1, §2, §3, §7 in
detail); `research/RESEARCH_STRUCTURE_PROTOCOL.md` (§4 item 7 in detail); `ksum/README.md`;
the header block and the Lean outline block of `ksum/notes/KSUM_PROOF_DAG.md`;
`ksum/proof-dag/NODE_INDEX.md`; the target node
`ksum/proof-dag/nodes/KSUM.LEAN.T3.obstruction-theorems.yaml`; its parent
`ksum/proof-dag/nodes/KSUM.LEAN.yaml`; the ten related obstruction nodes
`KSUM.B4b.L2.{M1,L2P3,BANDMULT,M2,T4,VBUD,ORIENT,G1,G2,G3}` plus
`KSUM.B4b.L2.ALT.nonproduct.profile-lattice-core`; the reorg report
`ksum/artifacts/ksum_lean_reorg_20260730.md`; `ksum/paper/ksum_small_alphabet.tex`
§`sec:proof-search` (lines 671–1150); and all eight draft `Obstructions*.lean` modules plus
`KsumAudit.lean`, `lakefile.lean` and `KSUM/Trust.lean`.

- **Target node and status as read from disk:** `KSUM.LEAN.T3.obstruction-theorems` — **OPEN**
  (`status_source: rule8a-registration-2026-07-30`), LEAF, role `tool`, parent `KSUM.LEAN` (OPEN),
  no children, eleven `related` obstruction/tool nodes.
- **Role:** executor.
- **Highest status the planned evidence could license (§2 of the DAG protocol):** **NUMERICAL with
  a `pending-review:` marker**, writable by the proposer citing the run. A `lake build` is a run
  (command + log + SHA-256); `DAG_PROTOCOL.md` §7.1 states that a Lean attribute never promotes a
  node by itself, and `KSUM.LEAN`'s scope clause 3 repeats it. A completion tier requires
  `KSUM.LEAN.statement-fidelity` to complete first (rule 6 + rule 7). **No obstruction node's
  status may be changed by this run at all** — the audit is confirmatory and can only demote, and
  a demotion would itself need an independent review.
- **Gates, one line each.** G-T3a: resolve the LaTeX-label ↔ node-id mapping from disk and table
  it. G-T3b: per-theorem `sorry`-free build. G-T3c: per-theorem fidelity verdict
  FAITHFUL/NARROWER/WIDER/AMBIGUOUS-IN-SOURCE, derived by rendering the Lean back into English
  BEFORE reading the LaTeX. G-T3d: a compiling, non-vacuous witness example per theorem.
  G-T3e: `#print axioms` = the three standard axioms only, every theorem.
- **Deliverables, one line each.** Audited/completed Lean under
  `ksum/lean/KsumAudit/`; this artifact plus log and `SHA256SUMS.txt` under
  `ksum/artifacts/logs_ksum_lean_T3_20260730/`; node updates at ceiling NUMERICAL·pending-review;
  `KSUM/Trust.lean` census flipped; `NODE_INDEX.md` T3 Lean column, the `LeanT3` Mermaid label and
  class, the nested-outline entry, and the DAG header's "Most recent change" synced; both
  validators exit 0.

### Conflicts between the commission text and the disk — **two, reported, not silently resolved**

1. **`git diff --check` vs the no-git instruction.** `RESEARCH_STRUCTURE_PROTOCOL.md` §9 lists
   `git diff --check` among the required closeout checks; this commission forbids running any
   `git` command. **No `git` command was run.** The two non-git validators were run and both
   exit 0. (The same conflict was reported by the T1 executor and again by the reorg executor on
   2026-07-30; it recurs and is recorded again rather than treated as settled.)
2. **Where the draft modules live.** The node's 2026-07-30 work record says the eight
   `Obstructions*.lean` modules are under `ksum/lean/KsumAudit/`. On disk they are under
   **`ksum/lean/KsumAudit/`** — the node text predates the same-day §7.2 move
   and was not updated by the reorg pass. Disk wins; the node's Work record is corrected by this
   run's entry rather than by editing the historical line. A related residue: the ADOPTED tier-T1
   module `KsumAudit/Defs.lean` still cites the pre-move path `ksum/lean/README.md` in
   its docstring. **That file was deliberately NOT edited** — it is byte-identical to the archived
   T1 ledger and belongs to `KSUM.LEAN.T1.k2-main-line`, not to this tier. Reported as F-T13.

---

## 1. Gate G-T3a — the LaTeX-label ↔ node-id mapping, resolved FROM DISK

Resolved by reading each node file's `## Claim` and matching it to the LaTeX statement; not
guessed from label names. Every row below is justified by a verbatim phrase that occurs in **both**
the node Claim and the LaTeX.

| LaTeX label | line | Node id (from `NODE_INDEX.md`) | Node status | Matching evidence used to resolve it |
|---|---|---|---|---|
| `thm:pair-tensor` | 830 | `KSUM.B4b.L2.M1` | PROVED | node: "exact-total pair tensor has exact `l1=1` … annihilates every query polynomial of degree below `q-1`; cancellation holds separately on every exact-total pair-size slice before mixing" ≡ the theorem text |
| `thm:tilted-log-band` | 866 | `KSUM.B4b.L2.L2P3` | PROVED | node: "pure high degree at least `2(1+floor(log_5((q-1)/2)))` … correlation at least `437/581>3/4`" ≡ (41) + the displayed degree |
| `lem:band-multiplication` | 944 | `KSUM.B4b.L2.BANDMULT` | PROVED | node: "annihilation bands add, so blocks with bands `d_j` yield annihilation below `sum_j d_j`" ≡ the lemma |
| `thm:product-obstruction` | 983 | `KSUM.B4b.L2.M2` | PROVED | node lists **the same five numbered class conditions verbatim** and the value `2^(1-(q-1)/2)` |
| `thm:block-obstruction` (48)–(49) | 1021 | `KSUM.B4b.L2.T4` | PROVED | node: "fixed-allocation, unaveraged absolute-value sign-bit composition … exact correlation identity is `-2 Psi(-1^m) product_j rho_j`" ≡ (49); `rho<=4/5` |
| `thm:block-obstruction` (50) | 1021 | `KSUM.B4b.L2.VBUD` | PROVED | node: "`sum_j r_j<=(q-1)/2` … `m*r0<=(q-1)/2`" ≡ (50) verbatim |
| `thm:orientation-obstruction` | 1063 | `KSUM.B4b.L2.ORIENT` | PROVED | node: "cross-block true-NO coherence costs exactly `2^{-r(m-1)}` and the normalized correlation is at most `1/2`" ≡ clauses (a),(b) |
| `prop:transfer-facts` (G1) | 1111 | `KSUM.B4b.L2.G1` | PROVED | node: "`Q_j -> Q_j O` and `B -> O^T B O` leave the ambient operator unchanged" ≡ (53) |
| `prop:transfer-facts` (G2) | 1111 | `KSUM.B4b.L2.G2` | PROVED | node: "`R_G v=R_G R_H v=0` for a nontrivial H-satellite" ≡ (G2) verbatim |
| `prop:transfer-facts` (G3) | 1111 | `KSUM.B4b.L2.G3` | PROVED | node: "`mu_A=Reynolds(diag A)/tr A` … degree-zero factorial moment exactly one" ≡ (54) |
| `lem:factorial-filtration` | 754 | **NO NODE** | — | exhaustive grep of `ksum/proof-dag/nodes/` finds the string only inside the T3 node's own scope table |
| `prop:joint-lp` | 781 | **NO NODE** | — | same |

**G-T3a: PASS.** Nine LaTeX targets → ten nodes (one LaTeX theorem, `thm:block-obstruction`, spans
two nodes; one LaTeX proposition, `prop:transfer-facts`, spans three). **Two of the nine targets
have no canonical node at all.** That is itself a finding (F-T1) and is why they can be reported as
gaps without demoting anything: there is no node whose status could be affected.

The β1 identities on `KSUM.B4b.L2.ALT.nonproduct.profile-lattice-core` were read as commissioned.
**C3 was NOT formalized**, as the node and the commission require: the node records it as "a finite
observation, not a cap theorem — `D_crit/sqrt(N)` wobbles in `0.75-1.0`", capped at NUMERICAL by
the 2026-07-23 review. C1/C2/C4 are PROVED-scoped but are *identities about the β1 ansatz*, not
statements of §`sec:proof-search`; C2 ("activating `Theta(q)` pairs by a product pays EXACTLY M2's
`2^{1-(q-1)/2}`") is the *same* statement as `thm:product-obstruction`, and is therefore already
covered by `product_obstruction_q`/`product_obstruction_mixture_q` (§4.2). Nothing else from that
node was formalized, and its status is untouched.

---

## 2. The adopt-or-rewrite audit (this run's addition #1)

Method, per the commission and rule 7c (anchoring ban): for each module, every theorem statement
was extracted and **rendered back into English from the Lean type alone**, written down, and only
then compared with the LaTeX. The English renderings are §4; this section is the per-module
verdict.

**Result: ADOPT 44 / REPAIR 0 / REJECT 0**, plus **14 theorems ADDED** to close gaps the audit
found (44 draft + 14 new = the 58 declarations in the axiom manifest). No draft statement had to be
rewritten. The draft's own module docstrings were unusually honest about scope — every "NOT
formalized" list I checked was accurate; the two places it went wrong (F-T3, F-T8) are both
*hypothesis substitutions* asserted in a docstring rather than proved, and both are now proved.

| Module | Draft decls printed | Verdict | What the audit changed |
|---|---|---|---|
| `ObstructionsCore` | (defs + 6 lemmas) | **ADOPT** | Definitional check only (§3). Fixed a stale path (`ksum/lean/README.md` → `ksum/lean/README.md`); added `set_option linter.unusedSectionVars false` to clear 3 warnings. No statement touched. |
| `ObstructionsPairTensor` | 9 | **ADOPT** | Statements faithful to the module's declared scope; the scope itself is NARROWER than the LaTeX (headline). Removed an unused hypothesis (`exists_light_pair`'s `1 ≤ r` — F-T10) and cleared 3 warnings. No statement touched. |
| `ObstructionsProduct` | 5 | **ADOPT** | **+2 theorems**: `product_obstruction_mixture_normalized`, `product_obstruction_mixture_q`. The draft proved clause 5 only in *ratio* form, so equation (47)'s **value** for mixtures was not machine-checked (F-T4). +1 witness. |
| `ObstructionsBlock` | 8 | **ADOPT** | **+2 theorems**: `block_obstruction_two_blocks` (clause (iii) assembled onto the composed measure, F-T5), `value_budget_q` (equation (50) written with the paper's own `(q-1)/2`, F-T6 — no draft theorem mentioned `q` at all). +3 witnesses incl. the first non-vacuity witness for the correlation identity (F-T7). Cleared 4 warnings. |
| `ObstructionsOrientation` | 6 | **ADOPT** | Faithful for clause (a); clause (b) NARROWER as declared (headline). Nothing added — the missing step is analytic, not arithmetic (§6.4). |
| `ObstructionsBandMult` | 5 | **ADOPT** | **+1 theorem**: `band_add_fin`, the **general `m`** statement (F-T2). The draft had `m = 2` and `m = 3` and its docstring called the general case "the evident induction"; the LaTeX and the node Claim both quantify over `m`, so the draft was NARROWER than both. +1 witness at `m = 5`. Cleared 2 warnings. |
| `ObstructionsTiltedBand` | 4 | **ADOPT** | Explicitly partial and correctly self-described. Nothing added (§6.3). |
| `ObstructionsTransfer` | 7 | **ADOPT** | **+9 theorems**: `psd_eq_zero_of_trace_eq_zero`, `psd_trace_pos_of_ne_zero`, `transfer_G3_nonzero` (G3 at the paper's own "every NONZERO PSD `A`", F-T3), `transfer_G3_pure_high_degree_zero`; `reynolds_smul_eq`, `reynolds_eq_zero_of_mem_augment`, `mem_augment_of_reynolds_eq_zero`, `reynolds_eq_zero_iff_mem_augment`, `transfer_G2_satellite` (with the new definition `augment`: G2's satellite hypothesis turned into a proved characterization, F-T8). +3 witnesses incl. the first witness for G2 (F-T7). Cleared 5 warnings. |
| **total** | **44** | **ADOPT 44 / REPAIR 0 / REJECT 0** | **+14 theorems, +8 witnesses, −16 warnings** |

Only after this audit was any new content written on top of the draft.

---

## 3. Definitional check on the substrate (`ObstructionsCore`)

A wrong definition makes every theorem about the wrong object while every gate still passes, so the
substrate is checked separately, against the paper's own text.

| Lean | Paper | Verdict |
|---|---|---|
| `l1 μ = ∑ x, |μ x|` | "unit-`ℓ¹`", "‖μ‖₁ = 1" | matches |
| `total μ = ∑ x, μ x` | "total mass zero" | matches |
| `signF no x = if no x then -1 else 1` | `F = 2·twoSum − 1 ∈ {−1,+1}`; `F = +1` iff YES (eq. 36) | matches: `F = −1` exactly on NO |
| `corr no μ = ∑ x, μ x * signF no x` | `⟨μ, F_{N,q,t}⟩` | matches |
| `ffRow α n = ∏_a (n a)_{α a}` | `∏_{a∈ℤ_q}(n_a(x))_{\underline{α_a}}` (eq. 38) | matches, with `Nat.descFactorial` = falling factorial |
| `rowOrder α = ∑_a α a` | `|α|` (eq. 38) | matches |
| `PureHighDegree S occ μ d` | "pure high degree at least `d`" = annihilates every query polynomial of degree `< d`, **which `lem:factorial-filtration` identifies with every falling-factorial row of order `< d`** | matches **modulo the unformalized filtration lemma**; the Lean definition is the falling-factorial side of that equivalence, which is the side the obstruction proofs use |
| `corr_of_total_zero : total μ = 0 → corr no μ = −2·(NO mass)` | "Its total mass is zero, so orienting the NO mass negatively gives correlation `2·2^{-r}`" | matches; this is the identity every obstruction proof runs on |

One honest caveat, recorded rather than smoothed: `PureHighDegree` is **defined** as the
falling-factorial condition. The paper *proves* that this is equivalent to the query-degree
condition (`lem:factorial-filtration`). Since that lemma is not formalized (§6.1), every T3
statement about "pure high degree" is a statement about falling-factorial rows, and the reader must
supply the filtration lemma to read it as a statement about query polynomials. This is the single
most load-bearing sentence in the audit and is repeated on the node.

---

## 4. Gate G-T3c — English renderings (written from the Lean, before re-reading the LaTeX) and verdicts

### 4.1 `thm:pair-tensor` → `KSUM.B4b.L2.M1` — **NARROWER**

*Rendered back from `pair_tensor`:* for every `q` and `N` with `q` odd, `q ≥ 3` and `N ≥ q`, there
is a finite nonempty set `T` of vectors `s : Fin ((q−1)/2) → ℕ` and a probability weighting `w` on
`T` such that every `s ∈ T` has all coordinates `≥ 2` and sums to `N−1`, the resulting signed
weighting of (slice, local-state) pairs has `ℓ¹` norm exactly `1`, and for every fixed-point order
`αf` and every family of local orders `α` with `αf + ∑_c (α_c¹ + α_c²) < q−1`, the pairing against
the corresponding falling-factorial row is `0`.

*LaTeX:* "there is an `S_N × C(σ)`-invariant signed measure `μ` on `ℤ_q^N` such that `‖μ‖₁ = 1` and
`μ` annihilates every **query polynomial** of degree below `q−1`. The cancellation holds on each
labeled exact pair-total slice before those slices are mixed."

*Diff.* (i) configuration space: labeled slice/local-state space, not `ℤ_q^N` — the uniform lift of
an occupancy weight to its `S_N` string orbit is not formalized, so `S_N`-invariance and the
pushforward `ℓ¹` identity are absent; (ii) "query polynomial" → "falling-factorial row" (needs
§6.1); (iii) `C(σ)`-invariance IS proved (`prodKappa_endpoint_swap`, `prodKappa_perm`) but is not a
conjunct of `pair_tensor`; (iv) `t ∈ ℤ_q` does not appear — correctly, since the paper's proof uses
`t` only through `r = (q−1)/2`. **NARROWER.** The last slice-wise clause of the LaTeX
(`slice_annihilation`) is FAITHFUL on its own.

Supporting statements, all FAITHFUL: `kappa_l1`, `kappa_total`, `kappa_moment_fst/snd`,
`kappa_annihilates` (both parities of `s`, every `s`), `prodKappa_l1`, `prodKappa_moment`,
`admissible_nonempty` (the paper's `N−1 ≥ 2r`), `mixture_l1_and_annihilation`.

### 4.2 `thm:product-obstruction` → `KSUM.B4b.L2.M2` — **FAITHFUL (and WIDER in the safe direction)**

*Rendered back from `product_obstruction_q`:* let `ι` be a finite index type with
`|ι| = (q−1)/2` and `q ≥ 5`; let each `c ∈ ι` carry an arbitrary finite local state type `Ω c` with
an arbitrary decidable "axis" predicate; let `f c : Ω c → ℚ` be nonpositive on the axis, nonnegative
off it, of total mass zero and not identically zero; let the global NO predicate be exactly the
all-axis event. Then if the product measure has `ℓ¹` norm `1`, `|⟨μ,F⟩| = 2^{1−(q−1)/2} ≤ 1/2`.
`product_obstruction_mixture_q` says the same for an arbitrary nonnegative mixture of such products.

*LaTeX:* the five-condition class, "after unit-`ℓ¹` normalization and global sign orientation, every
measure in this class has `⟨μ,F⟩ = 2^{1−r} = 2^{1−(q−1)/2} ≤ 1/2`."

*Diff.* Condition-by-condition: (1) → the explicit `hNO : no x ↔ ∀ c, axis c (x c)`, so the
"fixed-point occupancy at most one" premise is visible as exactly what it buys and nothing more;
(2) → `f` is a total family plus `IsLocalFactor.nonzero`; (3) → the three sign/mass fields; (4)
→ `Ω`, `axis` arbitrary — strictly wider than "occupancy pairs on an exact-total slice", so the
obstruction is proved for **more** measures than the paper's class; (5) → the mixture theorems.
Sign: Lean states `|⟨μ,F⟩|`, the paper states `⟨μ,F⟩` "after global sign orientation" — the same
content. `Odd q` is **not** assumed in Lean (only `5 ≤ q`), another harmless widening.
**FAITHFUL.** Since an obstruction is a `∀`-statement, widening is the safe direction and is
recorded as such.

### 4.3 `thm:block-obstruction` (48)–(49) → `KSUM.B4b.L2.T4` — **FAITHFUL**

*Rendered back from `block_obstruction_corr` / `block_obstruction_bound`:* for a finite family of
blocks, inner measures `μ_j` with `∑_y |μ_j y| = 1`, `∑_y μ_j y = 0` and positive mass only on YES
inputs, and an outer `Ψ` on sign vectors with `∑_s |Ψ s| = 1`, `∑_s Ψ s = 0`, the measure
`ζ(x) = 2^m Ψ(sgn μ_1(x_1),…)·∏_j |μ_j(x_j)|` satisfies
`⟨ζ, OR⟩ = −2 Ψ(all-negative) ∏_j ρ_j`, where `ρ_j` is the `|μ_j|`-conditional NO probability given
`S_j = −1`, and `|⟨ζ,OR⟩| ≤ ∏_j ρ_j`. Here `OR = −1` exactly when *every block input is NO*.

*LaTeX:* equations (48)–(49) verbatim.

*Diff.* None on the identity or the bound. One **rule-7g resolution** the draft made and I confirm
(F-T9): "`OR_m` is `+1` unless every **block label** is `−1`" is ambiguous in isolation — "label"
could be the sign bit `S_j` or the YES/NO label of `x_j`. The proof disambiguates it ("If any
`S_j=+1`, the block is certainly YES … Conditional on `S=(−1,…,−1)`, block independence makes the
global NO probability `∏_j ρ_j`"): `OR_m` is the ±1 indicator of the **composed problem**. That is
what `hnoG` encodes. **FAITHFUL**, with the ambiguity named rather than papered over.

The band clause `block_obstruction_band` is FAITHFUL with one explicit structural choice worth
recording (F-T11): the query row is taken to be a **product of per-block rows** with per-block
orders. That is exactly the structure of a query row on a fixed-allocation composed input, and the
paper's own proof presupposes it ("a block of local factorial order below `d`"), but the paper does
not state it as a hypothesis and Lean does. `OuterPureHighDegree Ψ D` ("annihilates every function
depending on fewer than `D` sign coordinates") is equivalent to "`Ψ` has pure high degree `D`" for
multilinear sign polynomials, so no strength is lost there.

Clause (iii) is now a single theorem on the composed measure (`block_obstruction_two_blocks`):
`ρ_j ≤ 4/5` for two blocks ⇒ `|⟨ζ,OR⟩| ≤ 16/25 < 2/3`. The step `ρ ≤ 4/5` itself
(`rho_le_four_fifths`) is FAITHFUL as the paper's arithmetic (`2/(1+5/4+1/4)`), but it is stated
about an abstract layer-weight vector, **not** about the tilted inner of §6.3 — the link
"the phase-3 inner has these layer ratios" is part of the unformalized `thm:tilted-log-band` and is
named as such.

### 4.4 `thm:block-obstruction` (50) → `KSUM.B4b.L2.VBUD` — **FAITHFUL**

*Rendered back from `value_budget` / `value_budget_equal` / `value_budget_q`:* if each block `j`
receives a set `B j` of complete complementary value pairs, all `B j` inside a common finite pool
and pairwise disjoint, then `∑_j |B j| ≤ |pool|`; with `|B j| = r₀` for all `j`,
`m·r₀ ≤ |pool|`; and if `r₀ ≥ 1`, `m ≤ |pool|`. With `|pool| = (q−1)/2` these are literally (50)
and the sentence the paper draws from it.

*Diff.* None. The "cannot produce the required `√N` growth" conclusion is rendered as the honest
formal fact that the block count is bounded by a quantity **in which `N` does not occur**; the
paper's phrasing is an informal consequence of exactly that. **FAITHFUL.** (Before this run no
theorem in the module mentioned `q`, so the instantiation `|pool| = (q−1)/2` was left to the
reader — F-T6.)

### 4.5 `thm:orientation-obstruction` → `KSUM.B4b.L2.ORIENT` — clause (a) **FAITHFUL**, clause (b) **NARROWER**

*Rendered back from `orientation_coherence_factor`:* for `r` pairs each carrying `m` independent
uniform binary endpoint orientations and `m ≥ 1`, the fraction of orientation patterns in which all
`m` blocks agree on **every** pair is exactly `2^{−r(m−1)}`. That is clause (a). **FAITHFUL**
(and proved for `m ≥ 1`, wider than the paper's `m ≥ 2`).

*Rendered back from `orientation_obstruction_half`:* for `r ≥ 2`, `m ≥ 2` and any `c ≥ 0`, if either
`c ≤ 2^{r+1−m(r+1)}` or `c² ≤ 2^{2(r+1−m(r+1))+rm}`, then `c ≤ 1/2`. The two disjuncts are the
even-`s` case (`|A_s| = 1`) and the odd-`s` case (`|A_s| ≥ 2^{−1/2}`, squared so no half-integer
exponent leaves `ℚ`) of the paper's displayed bound (51); the even case gives `≤ 1/8`, matching the
paper.

*LaTeX clause (b):* "the normalized correlation is at most `1/2`", derived from (51), which is
itself derived from an endpoint-phase norm lower bound.

*Diff.* Lean **assumes** (51) and concludes `≤ 1/2`; it does not prove (51). **NARROWER** — and,
because this is an obstruction, this is the verdict an independent reviewer should weigh most.
What is missing is precisely §6.4.

### 4.6 `prop:transfer-facts` (G1) → `KSUM.B4b.L2.G1` — **FAITHFUL (termwise, hence stronger)**

*Rendered back from `gauge_term`:* for any real matrices `Q`, `B` and any `O` with `O Oᵀ = 1`,
`(QO)(OᵀBO)(QO)ᵀ = QBQᵀ`. `gauge_sum` sums this over a frame index, which is (53) as displayed.
**FAITHFUL**, and termwise is strictly stronger than the summed form. The prose consequence
("a Gelfand–Tsetlin or Jucys–Murphy chain … by itself does not remove this residual gauge") is not
a displayed claim; instead a `2×2` witness shows the gauge is a **genuine** freedom
(`OᵀBO ≠ B` while the lifted terms are equal), which is the operative content of "terminal labels
do not specify multiplicity coordinates". The GT/JM sentence itself remains prose — declared, not
formalized (§6.5).

### 4.7 `prop:transfer-facts` (G2) → `KSUM.B4b.L2.G2` — **FAITHFUL after this run's repair**

*Rendered back from the draft's `transfer_G2`:* for a finite group `G`, a linear action on a
`ℚ`-module, and any nonempty subset `H ⊆ G`, **if the `H`-Reynolds average of `v` is zero** then the
`G`-Reynolds average of `v` is zero and equals `R_G R_H v`.

*LaTeX:* "if `v` lies in a nontrivial `H`-satellite, then `R_G v = R_G R_H v = 0`."

*Diff (as drafted):* the paper's hypothesis is "lies in a nontrivial satellite"; Lean's is
`R_H v = 0`. The draft docstring asserted these coincide ("which is what … gives, since the Reynolds
projection is the orthogonal projection onto the trivial isotypic component") — an assertion, not a
proof, i.e. a hypothesis substitution. **This run closes it**: `reynolds_eq_zero_iff_mem_augment`
proves, for a multiplicatively closed nonempty `H`, that `R_H v = 0` **⟺** `v` lies in the
augmentation submodule `⟨ρ h w − w : h ∈ H⟩`, and `transfer_G2_satellite` states (G2) with the
augmentation hypothesis. In characteristic zero the augmentation submodule *is* the sum of the
nontrivial `H`-isotypic components (Maschke), so the only remaining step is that standard
dictionary, which is now the *only* thing carried in prose. Verdict after repair: **FAITHFUL**,
with the residual dictionary named. Non-vacuity is witnessed by the sign representation of `S₂` on
`ℚ`, where the augmentation submodule contains the nonzero vector `−2`.

### 4.8 `prop:transfer-facts` (G3) → `KSUM.B4b.L2.G3` — **FAITHFUL after this run's repair**

*Rendered back from the draft's `transfer_G3`:* for a real matrix `A` that is positive semidefinite
**and has nonzero trace**, the function `x ↦ R_G(diag A)(x)/tr A` is pointwise nonnegative, sums to
`1`, is `G`-invariant, and has nonzero degree-zero moment.

*LaTeX:* "For every **nonzero** positive semidefinite operator `A` … `μ_A` is a nonnegative
invariant probability measure. Its degree-zero factorial moment is one, so its pure high degree is
zero."

*Diff (as drafted):* `A ≠ 0` replaced by `tr A ≠ 0`, with the draft docstring declaring the
implication unproved. **This run closes it**: `psd_eq_zero_of_trace_eq_zero` proves that a PSD real
matrix of zero trace is zero (nonnegative diagonal summing to zero ⇒ zero diagonal; then testing the
quadratic form on `e_i + t e_j` for all real `t` forces every off-diagonal entry to vanish), hence
`psd_trace_pos_of_ne_zero`, hence `transfer_G3_nonzero` at the paper's own quantifier. The clause
"so its pure high degree is zero" is now its own theorem
(`transfer_G3_pure_high_degree_zero`): for any occupancy labelling and any `d ≥ 1`, `μ_A` fails to
annihilate all rows of order `< d`. Verdict after repair: **FAITHFUL**.

### 4.9 `lem:band-multiplication` → `KSUM.B4b.L2.BANDMULT` — **NARROWER** overall; clauses (b),(c) FAITHFUL after this run's repair

*Rendered back from `band_add_fin`:* for every `m`, every family of finite block index types
`I : Fin m → Type`, every family of occupancy maps and signed measures, and every family of orders
`d : Fin m → ℕ`, if block `i` annihilates every falling-factorial row of order `< d i`, then the
convolution — configuration space `∀ i, I i`, occupancy the coordinatewise sum, measure the product
— annihilates every falling-factorial row of order `< ∑_i d i`.

*LaTeX clause (b):* "`ν` … annihilates every falling-factorial row below `∑_j d_j`."

*Diff.* None, at the paper's own quantifier. `descFactorial_add` is the falling-factorial
Vandermonde behind (45). `band_preserved_by_scaling` is clause (c) ("normalizing by its actual `ℓ¹`
norm is therefore legal and preserves this band") for an arbitrary constant. **FAITHFUL for
(b),(c).** Clause (a) (`ν ≠ 0`, via the integral-domain argument on the generating polynomials) and
clause (d) (common-value-group invariance) are **not formalized**, and the hypergeometric reduction
"`S_N`-average of the orbit-lifted product = convolution" is **taken as the definition of `ν`**,
exactly as the paper's own displayed computation (45) does — declared, §6.2. Before this run the
module had only `m = 2` and `m = 3`, which was NARROWER than both the LaTeX and the node Claim
(F-T2); that is now closed.

### 4.10 `thm:tilted-log-band` → `KSUM.B4b.L2.L2P3` — **NARROWER**

*Rendered back:* `one_sub_sum_le_prod_one_sub` — for a finite family in `[0,1]`,
`1 − ∑ x_i ≤ ∏ (1 − x_i)`. `tilt_corr_lower_bound` — for `0 ≤ C ≤ 25/19` and `0 ≤ S ≤ 29/23`,
`2/(1+CS) ≥ 437/581`. `tilt_gap` — `437/581 − 3/4 = 5/2324` and `3/4 < 437/581`.

*LaTeX:* an existence claim with `‖μ‖₁ = 1`, `⟨μ,F⟩ ≥ 437/581 > 3/4`, and annihilation of every
query polynomial of degree `< 2(1+⌊log₅((q−1)/2)⌋)`.

*Diff.* No theorem in the module is the LaTeX theorem; the module says so itself. The bounds
`C_h ≤ 25/19` and `∑_j A_j ≤ 29/23` are hypotheses, not conclusions. **NARROWER.** §6.3 says
exactly what is missing.

---

## 5. Gates

### G-T3b — per-theorem `sorry`-free build — **PASS**

`lake build` from `ksum/proof-dag/lean`: **`Build completed successfully (3009 jobs)`,
`BUILD_RESULT: exit=0`**, Lean `v4.31.0`, Lake `5.0.0-src+68218e8`, Mathlib pinned `v4.31.0`.
Full transcript: `logs_ksum_lean_T3_20260730/build.log`.

`grep` over `KsumAudit/Obstructions*.lean` for `sorry`, `axiom `, `native_decide`,
`implemented_by`: **one hit, inside a docstring** (`ObstructionsCore.lean:17`, the house-rules
sentence). Zero code hits. `sorryAx` is absent from the entire build transcript.

**Build warnings: 0** (the reorg pass recorded 16, all in these modules; every one is now fixed —
deprecated `push_neg` → `not_forall`/`not_exists`, unused simp arguments, unused section variables,
one unused binder name).

| Module | printed decls | build | warnings |
|---|---|---|---|
| `ObstructionsCore` | (definitions + 6 lemmas) | green | 0 |
| `ObstructionsPairTensor` | 9 | green | 0 |
| `ObstructionsProduct` | 7 | green | 0 |
| `ObstructionsBlock` | 10 | green | 0 |
| `ObstructionsOrientation` | 6 | green | 0 |
| `ObstructionsBandMult` | 6 | green | 0 |
| `ObstructionsTiltedBand` | 4 | green | 0 |
| `ObstructionsTransfer` | 16 | green | 0 |
| **total** | **58** | **green** | **0** |

### G-T3c — fidelity — **PASS (reported, not auto-escalated)**

Verdicts are given per **(LaTeX target, node)** pair, because two LaTeX statements split across
several nodes (`thm:block-obstruction` → T4 + VBUD; `prop:transfer-facts` → G1 + G2 + G3). Ten
pairs are formalized; two labels are formalized not at all (§6.1, §6.7) and have no node.

**FAITHFUL 6 · NARROWER 4 · WIDER 0 · AMBIGUOUS-IN-SOURCE 1 (orthogonal, on a term of art).**

| LaTeX target | Node | Verdict |
|---|---|---|
| `thm:product-obstruction` | `M2` | FAITHFUL (class strictly wider than the paper's — safe direction) |
| `thm:block-obstruction` (48)–(49) | `T4` | FAITHFUL |
| `thm:block-obstruction` (50) | `VBUD` | FAITHFUL |
| `prop:transfer-facts` (G1) | `G1` | FAITHFUL (termwise ⇒ stronger than the displayed summed form) |
| `prop:transfer-facts` (G2) | `G2` | FAITHFUL **after this run's repair** (drafted NARROWER: substituted hypothesis, F-T8) |
| `prop:transfer-facts` (G3) | `G3` | FAITHFUL **after this run's repair** (drafted NARROWER: substituted hypothesis, F-T3) |
| `thm:orientation-obstruction` | `ORIENT` | **NARROWER** — clause (a) FAITHFUL, clause (b) conditional on (51) |
| `thm:pair-tensor` | `M1` | **NARROWER** |
| `thm:tilted-log-band` | `L2P3` | **NARROWER** |
| `lem:band-multiplication` | `BANDMULT` | **NARROWER** — clauses (b),(c) FAITHFUL at the paper's `m`-quantifier; (a),(d) absent |
| `lem:factorial-filtration` | *(no node)* | not formalized (§6.1) |
| `prop:joint-lp` | *(no node)* | not formalized (§6.7) |
| — term of art: `OR_m`'s "block label" | `T4` | **AMBIGUOUS-IN-SOURCE**, resolved from the proof (F-T9) |

### G-T3d — witness example per theorem, compiling, non-vacuous — **PASS**

Every module now carries witnesses; the two gaps the draft had are closed.

| Module | witnesses | non-vacuity actually demonstrated |
|---|---|---|
| PairTensor | 5 | `admissible` nonempty at `(q,N) = (3,3)`; tensor `ℓ¹ = 1` at `r = 1, 3`; `κ` really has norm 1 and mass 0; a concrete `q = 5` slice cancellation at row order `3 < 4` |
| Product | 2 | `q = 5`, `r = 2`, local factor `(−1/2,+1/2)`: **all** hypotheses of `product_obstruction_q` discharged by computation and the value is exactly `1/2 = 2^{1−2}`; and the same through the mixture theorem |
| Block | 5 | `ρ_j = 1` for the two witness blocks; **new**: an explicit unit-`ℓ¹` zero-total `Ψ` giving `⟨ζ,OR⟩ = −1` exactly (the draft had NO witness for the correlation identity — F-T7); `4/5·4/5 = 16/25`; the disjointness budget; the `q = 5` budget |
| Orientation | 3 | smallest covered instance `q = 5, m = 2`: coherence factor `2^{-2} = 1/4`; `|coherent 2| = 2`; even-`s` bound exactly `1/8` |
| BandMult | 3 | a block with band exactly `1` (order-one moment `−1 ≠ 0`, so the hypothesis is not vacuous); two such blocks give band `2`; **new**: five such blocks give band `5` through `band_add_fin` |
| TiltedBand | 2 | both bounds attained: `2/(1+(25/19)(29/23)) = 437/581` exactly; Weierstrass at `x = (1/4,1/4)` |
| Transfer | 5 | G1: the gauge is a GENUINE freedom (`OᵀBO ≠ B` yet lifted terms equal); G3: identity matrix PSD with nonzero trace, and (new) with positive trace at the paper's quantifier; **new** G2: sign representation of `S₂` on `ℚ`, augmentation submodule contains the nonzero vector `−2`, which Reynolds kills (the draft had NO witness for G2 — F-T7) |

### G-T3e — `#print axioms` — **PASS**

58 declarations printed; **the only axioms appearing anywhere are `propext`, `Classical.choice`,
`Quot.sound`**. No declaration depends on anything else; `sorryAx` and `Lean.ofReduceBool` are
absent. Manifest: `logs_ksum_lean_T3_20260730/print_axioms.txt`. This tier carries **no
`QueryModel` and no interface hypothesis of any kind** — grep confirms `QueryModel` does not occur
in any `Obstructions*` module — so every theorem here is **unconditional**, exactly as the node
predicted.

---

## 6. Named gaps — what resisted, precisely

A named gap is the deliverable when a step resists; none of these was worked around, and no
statement was reshaped to make something compile.

**6.1 `lem:factorial-filtration` (line 754) — NOT formalized. The most consequential gap.**
The lemma says: for `S_N`-invariant `μ`, `μ` annihilates every query polynomial of degree `< d`
**iff** every falling-factorial occupancy moment of order `< d` vanishes. The direction the
obstruction theorems need is `⇐`. Formalizing it requires two pieces Mathlib does not package:
(i) the count of value-respecting injections — for `x : Fin N → A` and a set `S` of query positions
with prescribed values, the number of injections `φ : S ↪ Fin N` with `x_{φ(i)} = a_i` is
`∏_a (n_a(x))_{α_a}`; the natural route is `Fintype.card_embedding_eq` on each value fibre plus an
equivalence between value-respecting injections and families of per-fibre embeddings; and (ii) the
`S_N`-averaging step — the average over `π ∈ S_N` of a one-hot monomial at `x` equals that injection
count divided by `(N)_m`, which needs a count of permutations extending a given partial injection.
Neither is hard mathematics; both are a multi-hour standalone development, and this is why
`thm:pair-tensor` and `thm:tilted-log-band` cannot be lifted from occupancy statements to
query-degree statements inside this tier. **It also has no DAG node** (F-T1).

**6.2 `lem:band-multiplication` clauses (a) and (d), and the hypergeometric reduction.**
(a) `ν ≠ 0` is the paper's integral-domain argument on the finite generating polynomials; it needs a
polynomial-ring embedding of occupancy measures and a monomial order, not developed here.
(d) common-value-group invariance of the normalized average is not stated. The reduction
"`S_N`-average of the orbit-lifted product has occupancy pushforward equal to the convolution" is
**taken as the definition of `ν`**, which is exactly what the paper's displayed computation (45)
does, but it means the Lean `ν` is the convolution by fiat rather than by proof.

**6.3 `thm:tilted-log-band` — the construction.** Missing: the divided-difference coefficients
`λ_k = (∏_{u∈T_m, u≠k}(k−u))^{-1}` on `T_m = {0,1,5,…,5^{m−1}}` and their annihilation of every
polynomial of degree `< m`; the ratio computation (44)
`|λ_{5^j}|/|λ_0| = A_j C_{m−1−j}` with `A_0 = 1, A_1 = 1/4, A_2 = 1/96` and later ratios `≤ 1/24`;
the transfer from the activity-layer functional to the falling-factorial band (`deg p < 2m` ⇒
activity degree `< m`); and the `ℓ¹`/invariance bookkeeping. The blocking step is the
divided-difference identity: `∑_{k∈T} p(k)/∏_{u≠k}(k−u)` is the leading coefficient of the
interpolant, hence `0` for `deg p < |T|−1`; Mathlib has `Lagrange.interpolate` but no divided
differences and no coefficient-extraction lemma for it, so this is a real development.
*(The two numeric hypotheses `C_h ≤ 25/19` and `∑_j A_j ≤ 29/23` are separable and provable — split
off `d = 1` and bound the geometric tail `∑_{d≥2} 5^{-d} = 1/20`; `∑_{j≥2} A_j ≤ (1/96)(24/23)`.
They were left undone deliberately: they would not change the NARROWER verdict, since the band is
what is missing.)*

**6.4 `thm:orientation-obstruction` clause (b) — the norm lower bound producing (51).**
Missing: evaluate the occupancy generating polynomial on endpoint phases `(e^{iθ}, e^{−iθ})`; on one
pair the axis value is `A_s = cos(sθ)` and the interior value is `1` (even `s`) or `cos θ` (odd `s`);
choose `θ = π/s` (even) or `π/(s+1)` (odd) to force `I_s = −A_s` with `|A_s| = 1` resp.
`|A_s| ≥ 2^{−1/2}`; then the one-block Fourier modulus is `ρ|A_s|^r`, convolution raises it to the
`m`-th power, and the triangle inequality lower-bounds the post-average `ℓ¹` norm by
`ρ^m |A_s|^{rm}`. This needs the full tilted construction (§6.3) **plus** complex-exponential
machinery on the generating polynomial. It is the one gap that leaves an **obstruction** clause
unconfirmed.

**6.5 `prop:transfer-facts` (G1) — the GT/Jucys–Murphy sentence.** "A Gelfand–Tsetlin or
Jucys–Murphy chain acting through the symmetric-group algebra resolves the `U_λ` factor and acts as
the identity on `M_λ`" is prose in the paper, not a displayed identity, and is not formalized. The
displayed identity (53) is proved termwise and the `2×2` witness shows the residual gauge is
genuine, which is the operative consequence.

**6.6 `prop:transfer-facts` (G2) — the isotypic dictionary.** After this run's repair the only
unformalized step is "a nontrivial `H`-isotypic component is contained in the augmentation
submodule", i.e. Maschke's decomposition in characteristic zero. Mathlib has Maschke
(`Mathlib/RepresentationTheory/Maschke.lean`) but not the isotypic-projection identification in the
form needed; the augmentation characterization proved here is the operative content.

**6.7 `prop:joint-lp` (line 781) — NOT formalized, and the reason is structural.**
The proposition asserts **exact LP optima** — a table of rational optimal values at each degree, for
two different bases, on three instances — and defines "LP-certified degree" as the largest degree
whose optimum strictly exceeds `2/3`. Certifying an optimum needs **both** a primal feasible witness
**and** a dual certificate, per (instance, degree, basis); the manuscript prints only the optimal
values and delegates reconstruction to the ancillary script
`ksum/paper/ancillary/ksum_l2rr_exact_review.py`. So there is nothing in the manuscript to
transcribe: a Lean proof would have to (i) define the `S_N × S_q` occupancy classes and the
`S_N × C(σ)` joint-histogram classes of eq. (35) for `(3,3,0)`, `(4,3,0)`, `(5,4,1)`, (ii) exhibit a
primal witness reaching each printed optimum, and (iii) exhibit a matching dual certificate to prove
optimality — none of which exists in text form on disk. Formalizing only the primal half would
prove `≥`, not the equalities the proposition states, and formalizing only the arithmetic
`1 > 2/3, 2/3 ≯ 2/3, …` would be a reshaped statement, which the commission correctly forbids.
**Like `lem:factorial-filtration`, this label has no DAG node** (F-T1), so nothing is demoted by
leaving it open. *Recording it as an audit observation: this is the only §`sec:proof-search`
statement whose proof is delegated wholesale to an ancillary program.*

---

## 7. Findings

| # | finding |
|---|---|
| **F-T1** | **Two of the nine in-scope LaTeX targets have no canonical DAG node**: `lem:factorial-filtration` and `prop:joint-lp`. Verified by exhaustive grep over `ksum/proof-dag/nodes/` — the strings occur only inside the T3 node's own scope table. Consequence: the DAG does not currently record the status of the lemma that makes every "pure high degree" statement in §`sec:proof-search` a statement about **query** degree. Registering them is a rule-8a matter for the lead, not for this executor. |
| **F-T2** | `lem:band-multiplication` was formalized only at `m = 2` and `m = 3`, with the docstring calling the general case "the evident induction". The LaTeX and the node Claim both quantify over `m`. **CLOSED by `band_add_fin`** (induction on `m` via `Fin.consEquiv`, at full generality in the alphabet, block index types, occupancies, measures and orders). |
| **F-T3** | (G3) was stated with `tr A ≠ 0` where the paper says "every **nonzero** PSD `A`", with the implication declared unproved. **CLOSED**: `psd_eq_zero_of_trace_eq_zero` + `transfer_G3_nonzero`. |
| **F-T4** | `thm:product-obstruction` clause 5 (mixtures) was proved only in *ratio* form, so the class **value** `2^{1−r}` — the actual content of eq. (47) for mixtures — was not machine-checked. **CLOSED**: `product_obstruction_mixture_normalized`, `product_obstruction_mixture_q`. |
| **F-T5** | Clause (iii) of `thm:block-obstruction` existed only as three disconnected facts (the correlation bound, the `ρ ≤ 4/5` arithmetic, and `16/25 < 2/3`). **CLOSED**: `block_obstruction_two_blocks` states it on the composed measure. |
| **F-T6** | No theorem in the value-budget section mentioned `q`; equation (50)'s right-hand side `(q−1)/2` was left for the reader to instantiate. **CLOSED**: `value_budget_q`. |
| **F-T7** | **Two G-T3d holes in the draft**: no non-vacuity witness for `block_obstruction_corr` (the correlation identity — the central claim of node T4) and none at all for `transfer_G2`. Both **CLOSED** (explicit `Ψ` giving `⟨ζ,OR⟩ = −1`; sign representation of `S₂` with a nonzero augmentation vector). |
| **F-T8** | (G2) substituted `R_H v = 0` for the paper's "`v` lies in a nontrivial `H`-satellite" and *asserted* the equivalence in a docstring. This is exactly the hypothesis-substitution failure mode rule 7 exists for. **CLOSED** by proving the characterization `R_H v = 0 ↔ v ∈ augment ρ H` (both directions, the `⇐` needing only multiplicative closure of `H`, the `⇒` needing nothing at all). |
| **F-T9** | **Rule 7g, resolved from the source, not invented.** `OR_m`'s "block label" is ambiguous in the statement (sign bit `S_j` or YES/NO label of `x_j`?). The proof disambiguates it. Verdict **AMBIGUOUS-IN-SOURCE**; a sentence in the manuscript would remove it. Recommended manuscript repair. |
| **F-T10** | `exists_light_pair`'s hypothesis `1 ≤ r` is not needed (at `r = 0` the order hypothesis is already contradictory). Harmless, but it is a hypothesis carried without being used, and the audit removes such things rather than leaving them to be mistaken for content. |
| **F-T11** | `block_obstruction_band` renders the query row as a **product of per-block rows**. That is the correct structure for a fixed-allocation composed input and the paper's own proof presupposes it, but the paper does not state it as a hypothesis while Lean must. Not a defect; recorded so the fidelity reviewer sees where the Lean statement is more explicit than the prose. |
| **F-T12** | Three of the four NARROWER verdicts point at the same two missing developments: the **filtration lemma** (§6.1) and the **tilted construction** (§6.3, and through it §6.4). Neither is deep mathematics; both are substantial Lean engineering. If the lead wants T3 to reach FAITHFUL across the board, those two are the whole remaining cost, and the second one also closes the only unconfirmed *obstruction* clause. |
| **F-T13** | Stale path in an ADOPTED tier-T1 file: `KsumAudit/Defs.lean:12` still cites `ksum/lean/README.md`, which is now a forwarding stub. **Deliberately not edited** — that file is byte-identical to the archived T1 SHA ledger and belongs to `KSUM.LEAN.T1.k2-main-line`. Flagged for whoever next touches T1. (The same stale path in `ObstructionsCore.lean` — this tier's file — was fixed.) |
| **F-T14** | Build hygiene: the reorg pass recorded 16 warnings, "all theirs". All 16 are now gone and the whole project builds warning-free. Two were deprecated `push_neg`; the rest were unused simp arguments, unused section variables, and one unused binder. Cosmetic, but a warning-free baseline is what makes the next real warning visible. |

---

## 8. What this run did NOT do (scope discipline)

- **No `QueryModel` anywhere in this tier.** Verified by grep: the string does not occur in any
  `Obstructions*` module. No statement needed it; had one seemed to, the commission's instruction
  was to stop and report, and that did not arise.
- **No obstruction node's status was changed.** All ten stay PROVED, exactly as read from disk.
  The audit is confirmatory and can only demote; it found nothing warranting a demotion, and a
  demotion would in any case require an independent review.
- **C3 of `profile-lattice-core` was NOT formalized** as a theorem, per the node and the commission.
- **No `KSUM/` node modules were created.** The §7.3 node-module namespace is reserved for
  node-mirrored modules; T3's ten obstruction nodes may get them later via the statement-fidelity
  pass. This run's content stays under `KsumAudit/`, which mirrors PAPER theorems.
- **No `git` command was run.**
- **`NODE_INDEX.md`**: only the `LeanT3` row's Lean column was touched.

---

## 9. Validators

```
python tools/proof_dag_check.py --problem ksum   → exit 0
python tools/literature_check.py                 → exit 0
```

(`git diff --check` not run — see the reported conflict in §0.)

---

**T3 RESULT: adopt/repair/reject 44/0/0 (+14 added) | 7/9 LaTeX targets formalized (10/12
label↔node pairs) | fidelity: FAITHFUL 6, NARROWER 4, WIDER 0, AMBIGUOUS-IN-SOURCE 1 | NARROWER:
thm:orientation-obstruction clause (b) [obstruction — escalate], thm:pair-tensor,
thm:tilted-log-band, lem:band-multiplication clauses (a),(d) | axioms clean: Y (58/58, three
standard only) | node status: NUMERICAL · pending-review: KSUM.LEAN.statement-fidelity |
validators: 0, 0**
