# WHGAP LEAN-1 — DAG-mirroring Lean development, tier T1 + T2 (execution report, 2026-07-30)

Executor: one fresh Opus 5 instance (LEAN EXECUTOR role).
Commission: `channel-capacity/werner-holevo-gap/notes/WHGAP_COMMISSION_LEAN1_20260730.md`.
Governing protocols: `research/DAG_PROTOCOL.md` §7, `research/RESEARCH_STRUCTURE_PROTOCOL.md`
§4 item 7.
Project: `channel-capacity/werner-holevo-gap/proof-dag/lean/`
Run artifacts: `artifacts/logs_whgap_lean_20260730/`
**Evidence tier: NUMERICAL — `pending-review:`.  A green build is a run, not a status.**

---

## 0. PRE-ACTION REPORT (mandatory, `research/PRETASK_RELOAD_PROMPT.md`)

Files read from disk, in order, before any work: `research/DAG_PROTOCOL.md` (whole file,
including the new §7), `research/RESEARCH_STRUCTURE_PROTOCOL.md` (incl. §4 item 7 and its
2026-07-30 location amendment), `channel-capacity/werner-holevo-gap/README.md`,
`channel-capacity/werner-holevo-gap/proof-dag/NODE_INDEX.md`, and the node files
`WHGAP.goal`, `WHGAP.qpositive-onset`, `WHGAP.zero-capacity-application`,
`WHGAP.signed-lift-extension`, `WHGAP.order-boundary`, `WHGAP.no-ascent-hierarchy`,
`WHGAP.onset-two-fifths`, `WHGAP.private-boundary`.

* **Target node and status as read from disk:** `WHGAP.goal` — **OPEN**
  (`status_source: problem-scaffold-2026-07-28`; displayed as "resolved except on
  `[2/5, 1/2)`", capped by the CONJECTURED child `WHGAP.onset-two-fifths`).
  The mirrored skeleton is `G ⟸ {P3 ⟸ P9, P4 ⟸ P2, P13}` plus the root-level companion
  `P6 ⟸ P2`; `P14` is `related` to the goal and is the commissioned T2 flagship.
* **Role:** executor.
* **Highest status my planned evidence could license (§2):** **NUMERICAL**, with a
  `pending-review:` marker, and only on the strength of a real run (command + log + SHA-256).
  Writable by the proposer — i.e. by me — except that this commission carries a **single-writer
  deviation**: I may not edit node/index/DAG markdown at all, so I write **no status anywhere**.
  A completion tier (CERTIFIED\*/PROVED) would require a fresh-instance rule-6/rule-7 review
  meeting §7.10 as well, written by the decision layer, not by me.
* **Gates and deliverables (one line each):**
  * G-L1 — `lake build` exits 0, full transcript captured. → `logs_whgap_lean_20260730/lake_build.log`
  * G-L2 — zero `sorry`; `#print axioms` shows only the three standard axioms; no
    `native_decide`/`implemented_by`. → `print_axioms.log`, `grep_scan.log`
  * G-L3 — `SelfTest` compiles, all examples closed by `norm_num`/`simp`. → part of the build
  * G-L4 — import graph = DAG skeleton. → §4 below and `grep_scan.log`
  * G-L5 — statement-fidelity table, self-check tier (a separate fresh review is the gate, not
    this). → §5 below
  * Deliverables — the lake project; run artifacts per §7.7 with `SHA256SUMS.txt`; this report
    with the §7.9 scope sentences verbatim; a project README in the §7.9 language.
* **Conflicts between commission text and disk protocols:** **none.**  Two commission-internal
  arithmetic points were checked and are recorded in §6 (one is a typo the commission corrects
  in its own sentence; one is a degenerate self-test point).  The commission's single-writer
  deviation (no node/index/DAG edits) is narrower than, and consistent with, §5/§6 of the DAG
  protocol; consequently the atomic-update obligation (`RESEARCH_STRUCTURE_PROTOCOL.md` §6 step
  3 — linking this artifact from `WHGAP.goal`) is **owed by the decision layer**, and is flagged
  here as an open obligation rather than performed by me.

---

## 1. Required scope language (DAG protocol §7.9 — verbatim)

> A theorem proved against an abstract interface is exactly as strong as the results that
> interface cites, and not one notch stronger.

> `lean-checked` is an evidence attribute, never a status.

And, from `RESEARCH_STRUCTURE_PROTOCOL.md` §4 item 7, verbatim:

> a formalization is *evidence*, not a status. A green build is a run (command + log + SHA) and
> therefore caps at NUMERICAL under `DAG_PROTOCOL.md` §2; it licenses a completion tier only
> through the normal rule-6/rule-7 review gate, and it can never raise a node above what its own
> imported hypotheses allow.

**What this specific green build does NOT establish** (§7.9 requires this to be spelled out;
the same list, in full, is in the project README):

1. It does not prove that `Q`, `P`, `Qone`, `Pone` are the capacities of `Λ_x` — they are four
   opaque `ℝ → ℝ` fields.  There is no channel, Choi matrix, Kraus set, complementary channel,
   entropy, Holevo quantity or blocklength anywhere in the development.
2. It does not prove the WHGAP goal: `goal.composition` takes `«onset-two-fifths».Claim I S`
   as a hypothesis, and that node is CONJECTURED on disk.
3. It does not prove the P14 theorem `P^{(1)}(Λ_x) ≥ Δ(x)`.  It proves that the **scalar**
   `Δ(x)` is strictly positive on `(0,1/2)` and that the two Holevo arguments coincide at
   `ε = t = ε_c(x)/2`.  The bridge `Δ(x) ≤ P(Λ_x)` is an explicit hypothesis.
4. It does not check the signed-lift construction (opaque predicate), only the displayed
   forcing identities and eigenvalue sign conditions.
5. It does not check the BKM order (abstract predicate parameter; the R5b necessity theorem is
   the hypothesis `hFails`).
6. It does not validate the cited external results in `Interface.lean`.
7. It is not an independent review (§7.10).  The development caps at NUMERICAL,
   `pending-review:`.

---

## 2. What was built

One `lake` project, package `whgapDag`, toolchain `leanprover/lean4:v4.31.0`, Mathlib pinned to
tag `v4.31.0`, `.lake/packages` a junction to the machine-local prebuilt cache shared with
`research/se/lean` and `research/ksum/lean` (Mathlib was **not** re-downloaded or rebuilt).
`.lake/` is excluded by `.gitignore`.

Module name = node id **exactly** (hyphenated ids via Lean's `«guillemet»` identifiers); file
path uses the raw name.  Twelve modules, listed with what each contributes:

| module (= node id) | node | tier | content |
|---|---|---|---|
| `WHGAP.Support.Basic` | — | — | the scalars `b, e, u, v, ε_c, d₁, f, s*, Δ` + denominator sign lemmas |
| `WHGAP.Interface` | — | — | `CapacityInterface`: 4 opaque capacity functions, 2 opaque predicates, 3 cited assumption fields |
| `WHGAP.«signed-lift-extension»` | P2 | T1+T2 | `Claim`; `forcing_p`, `forcing_d`, `lam5_nonneg_iff`, `lam3_nonneg_iff`, `defect_eigenvalues_sign` |
| `WHGAP.«order-boundary»` | P6 | T1+T2 | `Claim`; `gap_identity`, `gap_neg_below_half`, `threshold_factorization`, `strict_violation_window`; `composition` |
| `WHGAP.«private-boundary»` | P14 | T1+T2 | **flagship**: `mul_log_gt`, `f_pos`, `b_at/e_at/u_at/v_at`, `argument_coincidence`, `prefactor_eq/pos`, `sStar_pos`, `sStar_lt_one`, `Delta_eq_prefactor_mul`, `Delta_closed_form_pos`, `Delta_lower_bound`, `blockA_trace_det`; `Claim`, `Claim_of_delta_le` |
| `WHGAP.«no-ascent-hierarchy»` | P9 | T1+T2 | `Claim`; `d1_at_two_fifths`, `d1_sign`, `exists_pos_of_expansion` |
| `WHGAP.«qpositive-onset»` | P3 | T1 | `Claim`; `composition` (P9 ⟹ P3) |
| `WHGAP.«zero-capacity-application»` | P4 | T1 | `Claim`; `composition` (P2 ⟹ P4), `composition_one_shot` |
| `WHGAP.«onset-two-fifths»` | P13 | stated | `Claim I S`, `conjecturedS` — **no proof, deliberately** |
| `WHGAP.goal` | G | T1 | `Claim I S`; **`composition` (P3+P4+P13 ⟹ the set equality, proved outright)**, `composition_conjectured` |
| `WHGAP.SelfTest` | — | — | 29 rational `example`s |
| `WHGAP.Trust` | — | — | sorry census, hypothesis table, `#print axioms` for all 44 top declarations |

### The two MUST-LAND items — both landed

* **P14 flagship core.**  `f_pos`, `argument_coincidence`, `Delta_closed_form_pos` are all
  proved **outright, unconditionally**, with no hypothesis beyond `0 < x < 1/2` (resp.
  `0 < s < 1`).  `Delta_closed_form_pos` bundles `0 < s*(x) < 1` with `0 < Δ(x)`.
* **Goal union assembly.**  `WHGAP.goal.composition` is a complete Lean proof of the set
  equality `{x ∈ (0,1) : Q x = 0} = [1/2,1) ∪ S` from the three tier-1 child Claims plus
  `hS : S ⊆ [2/5, 1/2)`.  No other premise is used; the proof is `Set.ext` + interval case
  analysis, exactly the node's inline assembly argument.

---

## 3. Gate results

| gate | result | evidence |
|---|---|---|
| **G-L1** `lake build` exit 0, full transcript | **PASS** | `logs_whgap_lean_20260730/lake_build.log` (WHGAP build outputs deleted first, so all twelve modules recompiled from source; final line `LAKE_EXIT=0`) |
| **G-L2a** zero `sorry` | **PASS** | `grep_scan.log`: the only occurrences of the string `sorry` are inside prose docstrings that say there is none |
| **G-L2b** `#print axioms` on every top theorem | **PASS** | `print_axioms.log`: all **44** declarations report exactly `[propext, Classical.choice, Quot.sound]` |
| **G-L2c** no `native_decide` / `implemented_by` / `axiom` | **PASS** | `grep_scan.log`: no declaration matches; only docstring mentions |
| **G-L3** SelfTest compiles, examples closed by `norm_num`/`simp` | **PASS** | built as part of G-L1; all **29** examples close by `norm_num` (28, some with definition unfolds as simp args) or `simp` (1: `f 0 = 0`) |
| **G-L4** import graph = DAG skeleton | **PASS** | §4 below |
| **G-L5** statement fidelity, self-check tier | **reported** (not a gate I can close) | §5 below |

`sorry_count = 0`.  `axioms_clean = true`.

Non-fatal build warnings (all cosmetic, none affecting a proof): three `push_neg` deprecation
notices, one `<;>`-style linter note, two "tactic does nothing" notes on defensive
`all_goals ring` lines, one unused-binder note.

---

## 4. G-L4 — import graph vs. DAG skeleton

Required by the commission and by §7.6 check 6.  The propagating skeleton on disk
(`NODE_INDEX.md`, 2026-07-30 edge normalization) is
`G ⟸ {P3 ⟸ P9, P4 ⟸ P2, P13}`, with the root-level companion `P6 ⟸ P2`.

| module | imports (node modules only) | required children | match |
|---|---|---|---|
| `WHGAP.goal` | `«qpositive-onset»`, `«zero-capacity-application»`, `«onset-two-fifths»` | P3, P4, P13 | ✅ |
| `WHGAP.«qpositive-onset»` | `«no-ascent-hierarchy»` | P9 | ✅ |
| `WHGAP.«zero-capacity-application»` | `«signed-lift-extension»` | P2 | ✅ |
| `WHGAP.«order-boundary»` | `«signed-lift-extension»` | P2 | ✅ |
| `WHGAP.«signed-lift-extension»` | (none — `Interface` only) | — (LEAF) | ✅ |
| `WHGAP.«no-ascent-hierarchy»` | (none — `Interface` only) | — (LEAF) | ✅ |
| `WHGAP.«onset-two-fifths»` | (none — `Interface` only) | — (LEAF) | ✅ |
| `WHGAP.«private-boundary»` | (none — `Interface` only) | — (LEAF, `related` to G) | ✅ |

§7.6 check 5 (OR nodes: `composition_via_*` must match children exactly) does not bite: on disk
`WHGAP.goal`'s `composition` block is a **single AND-style assembly claim** over the three
children, not one route per child, so the DAG-faithful Lean form is one `composition` taking
all three — which is what is written.  Same for P3 and P4, both `kind: AND` with one child.

---

## 5. G-L5 — statement-fidelity table (self-check tier)

For each node module: the frozen prose Claim (SHA-256 over the LF bytes of the `## Claim`
section body, blank-line-stripped, computed by `tools/whgap_lean_freeze_claims.py` and embedded
verbatim in the module docstring), the Lean `Claim`, and the correspondence with its
granularity loss stated explicitly.

| node | frozen-Claim SHA-256 | prose Claim (compressed) | Lean `Claim` | correspondence / granularity loss |
|---|---|---|---|---|
| `WHGAP.goal` | `f3a95693…9ce99` | "Determine `{x : Q(Λ_x)=0}` … close the gap `x ∈ (1/2, 4/7)`" | `{x ∈ Ioo 0 1 \| I.Q x = 0} = Ico (1/2) 1 ∪ S` | **Faithful to clause 1** in the exact form of the node's own `composition:` block. Clause 2 (the `(1/2,4/7)` gap) is a substatement of `[1/2,1) ⊆` the set and is not stated separately. The `x = 1` endpoint is **excluded** — on disk it is CERTIFIED\* via a cite-only RK24 dependency. `S` is a parameter with `hS : S ⊆ [2/5,1/2)`, so the open strip is visible in the type. `Q` is an interface field, not defined. |
| `WHGAP.qpositive-onset` | `a3f1e418…68cfa` | "Determine the small-x threshold below which `Q(Λ_x) > 0`" … PROVED bound `(0, 2/5)` | `∀ x, 0 < x → x < 2/5 → 0 < I.Q x` | Lean states exactly the node's **PROVED content** (the interval theorem). Loss: the "determine" task itself, the residual exact-onset scope, `x_1`/`x_H`, the two-letter null, the `783/2000` witness — none represented. `Q` is an interface field. |
| `WHGAP.zero-capacity-application` | `8be43283…326da` | "For every `x ∈ [1/2,1)`, `Q(Λ_x) = P(Λ_x) = 0`" (+ assembly provenance) | `∀ x, 1/2 ≤ x → x < 1 → I.Q x = 0 ∧ I.P x = 0` | **Faithful in scope** (half-open interval, both capacities). Loss: "at every blocklength" is inside the cited interface field `zw_hrsf_zero` (a separate `composition_one_shot` records the `Q^{(1)}/P^{(1)}` half); the seven R2 obligations and the HRSF22-via-ZW provenance are documentation; the closed-interval `[1/2,1]` corollary is deliberately **not** stated. |
| `WHGAP.signed-lift-extension` | `6283cddf…cf757` | "The signed-lift CP-defect certificate extends to `[1/2, x_max]`, `x_max > 1/2`, yielding `Q = P = 0` with exact rational certificates" | `∀ x, 1/2 ≤ x → x < 1 → I.SignedLiftCP x` | Lean asserts the certificate's **availability** on `[1/2,1)` — i.e. the R2-PROVED region, sharper than the prose "some `x_max > 1/2`". The `Q = P = 0` clause is by design elsewhere (P4), matching the node's own scoping. Loss: the 5-parameter covariant ansatz, uniqueness, and the three exact certificates are invisible (`SignedLiftCP` is opaque); what is checked instead is the displayed algebraic core (`forcing_p`, `forcing_d`, the two eigenvalue branches). |
| `WHGAP.order-boundary` | `db030127…c9e611` | "Determine `x_B` … **ANSWERED: `x_B = 1/2` exactly**; fails on `(0,1/2)`, holds on `[1/2,1)`; cBKM and cRE sets both `= [1/2,1)`" | `∀ x, 0 < x → x < 1 → (cBKM x ↔ 1/2 ≤ x)` | Faithful to the **answer**. Loss: `cBKM` is an abstract predicate parameter (no BKM inner product, no complete positivity, no complementary channel); the cRE coincidence is not represented; both directions enter `composition` as hypotheses (`hHolds` from ZW, `hFails` from R5b). The checked content is the scalar core: `gap_identity`, `threshold_factorization`, `strict_violation_window` at the exact threshold `ε_c(x)`. |
| `WHGAP.no-ascent-hierarchy` | `542edac6…363d37` | Operator inequality `Tr[(N^c)^{⊗n}(φ) log (N^c)^{⊗n}(ψ)] ≤ Tr[N^{⊗n}(φ) log N^{⊗n}(ψ)]` at every blocklength | `∀ x, 0 < x → x < 2/5 → ∃ c, 0 < c ∧ I.IcLB x c` | **Not the prose statement** — the operator inequality is unrepresentable here (no operators, no operator logs, no blocklength). The Lean `Claim` is the *tier-1 shadow the parent P3 actually consumes*, i.e. the R5c/R5d-licensed PROVED subset. Direction: prose ⟹ (via the first-order mechanism) this; the converse is **not** asserted. Checked outright: `d1_sign`, `d1_at_two_fifths`, and `exists_pos_of_expansion` (the `ε log(1/ε)` witness extraction; the expansion itself is the hypothesis `hexp`). |
| `WHGAP.onset-two-fifths` | `502ef4a9…f5a04` | "Conjecture: onset is exactly `x_D = 2/5`; `Q^{(1)} > 0` for `x < 2/5` (PROVED), `Q^{(1)} = 0` on `[2/5,1)` (OPEN); ideally also `Q = 0`" | `∀ x, 2/5 ≤ x → x < 1/2 → (I.Q x = 0 ↔ x ∈ S)` | The goal assembly needs only the **open half, in set form**, which is what is stated. `S` is a parameter, so the conjectured value is *not* built in (`conjecturedS := Ico (2/5) (1/2)` is recorded as a definition and asserted nowhere). Loss: the `Q^{(1)}` vs `Q` distinction (prose asserts both; Lean uses `Q`), and the PROVED half (which is P3's). **No theorem is proved in this module** — deliberately, since the node is CONJECTURED. |
| `WHGAP.private-boundary` | `415bdc11…30aa9` | `P^{(1)}(Λ_x) ≥ Δ(x) = [(1-2x)(1-x)/(2-3x)] f((1-2x)/(√2(1-x))) ≥ (1-2x)³/(2(1-x)(2-3x)) > 0` for `x < 1/2`, via the symmetric two-point ensemble at `ε = t = ε_c/2`; Corollary `{x : P = 0} = [1/2,1)` | `∀ x, 0 < x → x < 1/2 → 0 < I.P x` | The **scalar half of the prose Claim is proved outright**: `f_pos`, `argument_coincidence` (the `ε = t = ε_c/2` coincidence, Lemma 3.2b), `prefactor_eq`, `Delta_eq_prefactor_mul`, `Delta_closed_form_pos`. The **inequality `≥ Δ(x)`** — ensemble, commutations, Devetak formula — is unrepresentable and is the explicit hypothesis `hbridge` of `Claim_of_delta_le`. The `≥ (1-2x)³/…` clause is `Delta_lower_bound`, conditional on `f s ≥ s²` (see §6). The Corollary's `[1/2,1)` half is P4's. `blockA_trace_det` is a **real symmetric stand-in** for the Hermitian block: same trace and determinant, not the same matrix. |

**This table is a self-check.**  Per the commission and DAG-protocol rules 6–7 and §7.10, the
completion gate is a *separate fresh statement-fidelity review*, which must at minimum
reproduce the build, rerun `#print axioms`, re-derive each `Claim` from the node file without
reading this table first, and check for weakened inequalities, dropped quantifiers, reversed
implications and vacuity.

---

## 6. Derive-and-verify: independent checks of the commission's design, and deviations

The commission instructed that its design notes be **derived and verified, not trusted**.  Every
displayed identity was re-derived symbolically before formalization
(`logs_whgap_lean_20260730/sympy_identity_check.py` / `.log`, run under
`C:<home>/cpython3119/python.exe`), and then re-proved in Lean.  Append-only record:

1. **All eleven algebraic identities of the commission's §3/§1/§2/§4 are CORRECT as stated.**
   `gap_identity`, `threshold_factorization`, `forcing_p`, `forcing_d`, `b(x,ε_c/2) = (1-x)/2`,
   `e(x,ε_c/2) = x(1-x)/(2(2-3x))`, `u = (1-2x)/(2√2)`, `v = x(1-2x)/(2√2(2-3x))`, both ratios
   `= (1-2x)/(√2(1-x))`, `b - e = ε(1-x)`, `tr A = 1 - x/2`, `det A = 2x(1-x)ε(1-ε)`.
   No discrepancy anywhere; nothing had to be restated.
   The `s* < 1` side condition reduces to `2(1-x)² - (1-2x)² = 1 - 2x² > 0`, confirmed.
2. **`ε_c(9/20) = 4/13`** — confirmed independently (the commission's parenthetical "`1/13…`"
   is corrected inside the commission's own sentence; `4/13` is the value, and it is a
   `norm_num` example in `SelfTest`).
3. **Deviation / finding (self-test design).**  The commission's proposed self-test point
   `(x, p, d) = (2/5, 1/3, 2/5)` is **degenerate for both forcing identities**: `3p - 1 = 0` at
   `p = 1/3`, and `3d + 2x - 2 = 0` at `(x,d) = (2/5, 2/5)`.  Each identity therefore reads
   `0 = 0` there and would pass even against a mis-transcribed left-hand side — a vacuous check.
   The point is kept (it is a legitimate zero-locus check and is labelled as such) and
   **non-degenerate points were added to `SelfTest`**: `forcing_p` at `(x,p) = (1/4, 1/2)`
   (both sides `= -3/4`) and `forcing_d` at `(x,d) = (1/4, 1/3)` (both sides `= -1`), each
   checked as two separate `norm_num` examples (left-hand side and right-hand side against the
   same rational).  Two further non-degenerate points were confirmed symbolically but not added
   to `SelfTest`: `forcing_p(3/4, 2/3) = -1/3` and `forcing_d(3/4, 1/2) = -4/3`.
4. **Deviation (one item left conditional, never `sorry`).**  `Delta_lower_bound` is stated with
   the explicit hypothesis `hsq : ∀ s ∈ [0,1), s² ≤ f s`.  The inequality is true (verified
   numerically at `s = 0.1, 0.5, 0.9, 0.99`; the series is `s² + s⁴/6 + …`), but every short
   proof needs a power series or a two-level derivative-monotonicity argument, and it did not
   fit the budget.  Per the commission's instruction ("an unclosable obligation becomes an
   explicit hypothesis parameter, documented") it is a parameter of that one theorem.
   **Nothing else in the development depends on it** — in particular
   `Delta_closed_form_pos` is unconditional.
5. **Deviation (`Real.sqrt` discipline).**  As instructed, `√2` never appears inside an
   identity: `argument_coincidence` and the `u/v` lemmas carry `r` as a variable and, in fact,
   do not even need `r² = 2` (they are rational identities in `r`, which is *stronger* than the
   commissioned statement).  Only `sStar` and `Delta` mention `Real.sqrt 2`, and they are
   connected to the `r`-parameterized facts by `Real.sq_sqrt` (`Support.sqrt_two_spec`).
   Likewise `β` in `blockA_trace_det` is a variable with `hβ : β² = x(1-x)/2`.
6. **Environment finding (recorded for the next Lean executor).**  `field_simp` in this Mathlib
   silently leaves inverses uncleared when the context nonvanishing hypothesis is written
   `2 - 3*x ≠ 0` but `ring_nf` normalizes the occurrence to `2 - x*3`.  Both orientations must
   be in context.  `Support.two_sub_x_three_ne` exists solely for this, and its docstring says
   so.  Also: `Mathlib.Data.Matrix.Notation` does not exist at this pin — the `!![…]` notation
   is in `Mathlib.LinearAlgebra.Matrix.Notation`.
7. **Interface honesty.**  The interface has exactly the three commissioned assumption fields.
   Everything else that could not be proved is a theorem hypothesis, so it is visible in the
   theorem type rather than hidden in the trust boundary (§7.5).  In particular the P14 bridge,
   the P6 order steps, the P9 expansion and the P13 conjecture are *not* interface fields.

---

## 7. Artifacts

Project (committed source; `.lake/` excluded):

* `channel-capacity/werner-holevo-gap/proof-dag/lean/` — `lakefile.lean`, `lean-toolchain`,
  `lake-manifest.json`, `.gitignore`, `README.md`, `WHGAP.lean`, `WHGAP/…` (12 modules).

Run artifacts, `artifacts/logs_whgap_lean_20260730/` (§7.7; `SHA256SUMS.txt` over LF bytes):

* `lake_build.log` — the exact command, the environment header, the full transcript, and the
  true exit status on the last line.
* `print_axioms.log` — `#print axioms` for all 44 top-level declarations.
* `grep_scan.log` — the forbidden-construct scan and the full import listing.
* `sympy_identity_check.py` / `.log` — the independent symbolic re-derivation.
* `SHA256SUMS.txt`.

Tooling: `tools/whgap_lean_freeze_claims.py` (the single writer of the frozen Claim text and
its SHA-256 in each module docstring; `--check` detects drift).

---

## 8. Open obligations (for the decision layer — I am not permitted to write them)

1. **Atomic update (`RESEARCH_STRUCTURE_PROTOCOL.md` §6 step 3, rule 8c).**  This report, the
   project and the run artifacts must be linked from `WHGAP.goal` and from each mirrored node in
   the same session in which this result is read.  The single-writer deviation of the commission
   forbade me from doing it.
2. **§7.6 node metadata.**  Each mirrored node needs its `lean:` block (`module`, `file`,
   `claim`, `composition`, `state`, `rel`, `build`, `claim_hash`, `synced`) and `NODE_INDEX.md`
   needs its Lean column filled (currently every row reads `none`).  The `claim_hash` values are
   in §5 above; the `state` values are: P2 `stated`+core-proved, P6 `composition-checked`
   rel `{hHolds,hFails}`, P14 `proved` (core) / `stated` (Claim) rel `{hbridge}`, P9
   `composition-checked` rel `{hexp}`, P3 `composition-checked`, P4 `composition-checked`,
   P13 `stated`, G `composition-checked` rel `{P13, hS}`.
3. **The completion gate.**  A fresh-instance §7.10 review (reproduce build; rerun
   `#print axioms`; search `sorry`/`axiom`/`native_decide`/`implemented_by`; compare every
   `Claim` against the frozen prose independently of §5; check the top conclusion against the
   manuscript; check satisfiability/non-vacuity of the interface and of `goal.composition`;
   check README/report/node honesty).  Until then this work sits at **NUMERICAL,
   `pending-review:`**.
4. **Cheap follow-ups if a later session wants them.**  Prove `f s ≥ s²` on `[0,1)` to make
   `Delta_lower_bound` unconditional; add a satisfiability witness (a concrete
   `CapacityInterface` instance) so §7.10 check 5 has something to point at.

---

## 9. LEAN-1.1 repair (appended 2026-07-30, applying the R11 review)

Executor: a second fresh Opus 5 instance, **LEAN-1.1 REPAIR EXECUTOR** role.
Input: `artifacts/whgap_r11_lean_review_20260730.md` (verdict **(B) FINDINGS — 2 MAJOR,
15 minor**; neither MAJOR a soundness defect).
Scope: **Lean sources and run artifacts only.**  The single-writer deviation still binds — no
node file, `NODE_INDEX.md`, or DAG markdown was touched by this executor; the decision layer
had already corrected those, including the P13 `## Claim` section (see the refreeze below).
**Evidence tier is unchanged: NUMERICAL.  A green rebuild is a run, not a status.**

### 9.1 What changed, item by item

| R11 item | change | files |
|---|---|---|
| **MAJOR-1** | `blockA_trace_det` **moved** from `«private-boundary»` to `«no-ascent-hierarchy»`, statement byte-identical (same `β`-parameterized form, same proof). Cross-reference corrected from "paper Lemma 7.1" to **"paper Lemma 6.1 (`lem:exactspec`, §6)"**. Header prose adjusted on both sides: the P14 module no longer lists it among its proved core and no longer carries the real-symmetric-stand-in paragraph; the P9 module now lists it as core item 3 and carries that paragraph. Append-only deviation records added to both modules. | `WHGAP/private-boundary.lean`, `WHGAP/no-ascent-hierarchy.lean`, `WHGAP/Trust.lean` (`#print axioms` line moved), `README.md` (T2 bullet) |
| **m2** | The invalid justification "prose ⟹ (via the contrapositive first-order mechanism) this" is **replaced** by: "the Lean `Claim` is the tier-1 shadow that Theorem 8.1 of the N1-prime note *produces*, and is what P3 consumes; no implication from the prose Claim is asserted." | `WHGAP/no-ascent-hierarchy.lean` |
| **m4** | `Claim_of_delta_le` **rewired to the honest shape**: `hbridge : ∀ x ∈ (0,1/2), Δ x ≤ I.Pone x`, then `0 < I.P x` via `I.lsd_devetak`. The theorem now mirrors what `thm:private` actually proves, and `lsd_devetak` is consequently **consumed by checked content** instead of being a dead interface field. Disclosed in the module docstring and in `Trust.lean`'s hypothesis table. | `WHGAP/private-boundary.lean`, `WHGAP/Trust.lean` |
| **m5** | `lsd_devetak` citation corrected to **ZW (2.3)/(2.4) and (2.6)/(2.7)**, with the parenthetical that (2.4) is displayed in limit form so the `Qone ≤ Q` half additionally rests on superadditivity of the coherent information. | `WHGAP/Interface.lean` |
| **m10** | `lake-manifest.json` `"name"` corrected `ksumAudit` → **`whgapDag`**, matching `package whgapDag` in `lakefile.lean`. Verified by a full rebuild from a deleted `.lake/build` (lake did not rewrite it). | `lake-manifest.json` |
| **m11** | The doc comment above `prefactor_eq` no longer says `prefactor_pos`; `prefactor_pos` got its own doc comment; module header and README now both read `prefactor_eq`/`prefactor_pos`. README gained a `WHGAP/Support/Basic.lean` contents paragraph that **includes `sqrt_two_spec`**. | `WHGAP/private-boundary.lean`, `README.md` |
| **m12** | Unused hypothesis `hε0 : 0 < ε` **dropped** from `strict_violation_window` (the preferred remedy: the theorem is strictly stronger), with a docstring sentence saying the physical window is `0 < ε < ε_c(x)` but positivity of `ε` is not needed. The corresponding build warning (`order-boundary.lean:76:5`) is gone. | `WHGAP/order-boundary.lean` |
| **m13** | README sentence changed to "every scalar identity **listed below**", plus an explicit parenthetical naming displayed scalar content that is *not* checked (`eq:charpoly`, the Gram factors `4/25` and `1/3`, Appendix A's entrywise table, the `lem:holevo` collapse). | `README.md` |
| **m14** | R11's satisfiability witness now **ships in-tree** as `WHGAP/Model.lean`, imported by `WHGAP/Trust.lean` and by the root `WHGAP.lean`. Its docstring credits R11 by name and records that the file was authored out-of-tree by the reviewer as `artifacts/logs_whgap_lean_20260730/r11_audit_source.lean`. One substantive improvement over the reviewer's file: because of the m4 rewiring, the **P14 bridge is now discharged concretely** (`R11_bridge`, `R11_P14`) with a model whose `Pone` really is `Δ` on `(0,1/2)`, instead of only abstractly. Ten `#print axioms` lines were added to `Trust.lean` for the model theorems. | `WHGAP/Model.lean` (new), `WHGAP/Trust.lean`, `WHGAP.lean`, `README.md` |
| **m15** | The `hsq` deviation record now states plainly that this is a **FORMALIZATION gap, not a mathematical one**: the manuscript's `eq:fdef` series display `f(s) = Σ_{k≥1} s^{2k}/(k(2k−1))` has `s²` as its `k = 1` term, so the paper does not treat `f(s) ≥ s²` as an open step; only the Lean proof did not fit the budget. | `WHGAP/private-boundary.lean` |
| **m1** | `SHA256SUMS.txt` regenerated under **one stated convention** — see §9.3. | `artifacts/logs_whgap_lean_20260730/SHA256SUMS.txt` |
| — (mandated) | **Frozen-Claim refreeze.** The decision layer extended the P13 node's `## Claim` section with its R11-m3 reconciliation note. `tools/whgap_lean_freeze_claims.py` was re-run (placeholders restored first, so the *tool* remains the single writer of both the verbatim text and the digest): `WHGAP.onset-two-fifths` hash `502ef4a9…cefe5a04` → **`e0fa50f46c12fb8f58b7d187cda62c5a478d1c73edbc94ac7f7167c977d8c3bd`**. The other seven digests are unchanged. `--check` is clean 8/8. | `WHGAP/onset-two-fifths.lean` |

**One adjunct edit, reported rather than made silently.** Refreezing P13 would have left the
module's fidelity paragraph ("the conjecture asserts both") directly contradicting the frozen
text it quotes, which now says the opposite. That sentence was therefore aligned with the newly
frozen node text, and the change is recorded in an append-only block inside the module. No Lean
*declaration* in that module changed: `Claim` and `conjecturedS` are byte-identical.

**R11 items deliberately NOT actioned here** (out of this commission's scope, owed elsewhere):
MAJOR-2 (P9's recorded `lean.state`) and m3, m8, m9 are **node-metadata** corrections owned by
the decision layer; m6 (ingest BGSW25 into `channel-capacity/literature/`) is a literature task;
m7 (implement the §7.6 anti-drift checker) is a tooling commission of its own.

### 9.2 Rebuild evidence (from deleted build outputs)

`.lake/build` was deleted in full before the run; `.lake/packages` (the junction to the shared
prebuilt Mathlib cache) was left untouched.

| | |
|---|---|
| command | `lake build` |
| cwd | `channel-capacity/werner-holevo-gap/proof-dag/lean` |
| toolchain file | `leanprover/lean4:v4.31.0` |
| **true exit status** | **0** |
| wall time | **317 s** |
| jobs | `Build completed successfully (3052 jobs)` (3051 before; +1 = `WHGAP/Model.lean`) |
| transcript | `artifacts/logs_whgap_lean_20260730/repair_lake_build.log` |

* `#print axioms`: **54/54** declarations report exactly `[propext, Classical.choice, Quot.sound]`;
  0 lines deviate. (44 before, +10 for the `WHGAP.Model` theorems; `blockA_trace_det` is still
  printed, under its new namespace.) → `repair_print_axioms.log`
* Forbidden-construct scan over every `.lean` outside `.lake/`, 10 patterns
  (`sorry`, `sorryAx`, `axiom`, `native_decide`, `implemented_by`, `extern`, `unsafe`,
  `partial`, `opaque`, `decide`): **every hit is prose inside a docstring or a `#print axioms`
  command line.** Zero `sorry`, zero `axiom` declarations, zero `native_decide`/`implemented_by`/
  `unsafe`/`partial`. → `repair_forbidden_scan.log`
* Warnings: 11, all cosmetic (`push_neg` deprecations, one `<;>`-style note, two
  "`all_goals ring` does nothing"). The unused-binder warning R11 reported at
  `order-boundary.lean:76:5` is **gone** (m12).

### 9.3 The checksum ledger, under one convention (m1)

`SHA256SUMS.txt` was regenerated. Convention, stated in its header and followed by **every**
entry: **SHA-256 over LF-normalized bytes** (read bytes, replace every CRLF by LF, hash the
result), per DAG protocol §7.7.

Two decisions were needed to make that convention *and* a plain `sha256sum -c` both hold:

1. **Scope split by owner.** The ledger now covers the executor-side artifacts and every project
   source file; it deliberately does **not** list R11's `r11_*` artifacts or `SHA256SUMS_r11.txt`.
   Those are covered by the reviewer's own ledger, which uses a **raw-byte** convention and must
   keep verifying untouched — and listing one file twice under two conventions is exactly the
   mixing m1 objected to. One file, one convention, one owner.
2. **One byte-level normalization.** `sympy_identity_check.log` (executor evidence, listed in no
   other ledger) was stored CRLF while its recorded digest was LF-normalized — the single entry
   that failed R11's `-c` run. It was rewritten CRLF → LF. **Content unchanged, and therefore its
   LF digest is unchanged** from the 16:25 ledger (`c5a0e6c3…66d3`), which R11 independently
   confirmed by `tr -d '\r' | sha256sum`. No R11 artifact was touched.

Verification actually run, transcript in `repair_sha_verify.log` (itself not self-listed):

* `sha256sum -c artifacts/logs_whgap_lean_20260730/SHA256SUMS.txt` → **28/28 OK, exit 0**;
* `sha256sum -c artifacts/logs_whgap_lean_20260730/SHA256SUMS_r11.txt` → **11/11 OK, exit 0**
  (R11's ledger still verifies);
* `python tools/whgap_lean_freeze_claims.py --check` → **8/8 ok, exit 0**.

Residual caveat, recorded in the ledger header and **not** fixed here: the repo runs
`core.autocrlf=true` and `.gitattributes` pins `-text` for `artifacts/**` only, so after a fresh
checkout the Lean sources under `channel-capacity/` may materialize with CRLF. The convention
covers that case (normalize before hashing) but a plain `-c` would then fail on the source rows.
Extending `.gitattributes` to the Lean tree is a one-line repo-hygiene fix outside this
commission's scope; flagged for the decision layer.

### 9.4 New/updated run artifacts

All under `artifacts/logs_whgap_lean_20260730/`, append-named — **no R11 log was overwritten**:

* `repair_lake_build.log` — command, environment header, full transcript, true exit status, elapsed;
* `repair_print_axioms.log` — the 54 `#print axioms` lines plus the deviation count;
* `repair_forbidden_scan.log` — the 10-pattern forbidden-construct scan with the file inventory;
* `repair_sha_verify.log` — the three verification runs above;
* `SHA256SUMS.txt` — regenerated (28 entries, LF convention).

### 9.5 Still owed by the decision layer

R11 §9's list stands, minus what is now done in the sources: apply **MAJOR-2** (P9's
`lean.state`/`rel` and the "substituted shadow" sentence) and **m3/m8/m9** to the node metadata
and `NODE_INDEX.md`; update the `claim_hash` on `WHGAP.onset-two-fifths` to
`e0fa50f4…c977d8c3bd` and the `synced` dates; refresh the P14/P9 mechanization notes for the
`blockA_trace_det` move and the `hbridge`/`Pone` rewiring; link R11's report and this appended
section from `WHGAP.goal` and from each mirrored node; then decide the `lean:` attribute
statuses. This executor wrote no node, index, or DAG file.

