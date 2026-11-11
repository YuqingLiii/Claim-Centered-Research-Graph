# WHGAP R14 — independent §7.10 review of `rank_Cmat_half` (LEAN-3.2) and the LEAN-4 WP-G package

Fresh Opus 5 instance, 2026-08-01. Commission:
[`WHGAP_COMMISSION_LEAN4_R9_M6_20260801.md`](../channel-capacity/werner-holevo-gap/notes/WHGAP_COMMISSION_LEAN4_R9_M6_20260801.md),
section **R14**. NODE_ID = `WHGAP.goal`. ROLE = reviewer.

**VERDICT: (A) — LICENSE.** *"`rank_Cmat_half` and the WP-G package are licensed as
recorded; the residual display is accurate."*
**0 MAJOR, 5 minors** (all documentation/record accuracy; none changes what is proved).

---

## 0. PRE-ACTION REPORT

* **Target node and its status as read from disk:** `WHGAP.goal` — **OPEN**
  (`channel-capacity/werner-holevo-gap/proof-dag/nodes/WHGAP.goal.md:7`; the composition
  block displays `rel: P13 unresolved` as the reason).
* **Role:** reviewer. **Independence statement:** I did not author `rank_Cmat_half`,
  `Cmat_half_factor`, `V3R_Cmat_half_V3R`, any part of `Channel.lean` §8, the Trust/README
  wording, or the WP-G report; I was given no desired outcome — the commission's menu is
  (A) license / (B) findings, stated as alternatives.
* **Highest status my evidence could license (§2):** my own work here is a *review*, and a
  Lean build is a run ⇒ **NUMERICAL** as evidence. What this review can do is **open the
  rule-6/rule-7 completion gate** for the reviewed items; only the decision layer may then
  write a completion tier on the node, citing this report.
* **Gates/deliverables of my commission:** (1) re-derive the `rank_Cmat_half` factorization
  route myself and compute `rank Cmat(1/2)` with my own exact code; check the three new
  declarations against paper Thm 3.3(2) and the glosses in all four places; (2) reproduce
  the build; verify both charpoly statements against `IcScalar`'s lists symbol by symbol;
  own sympy re-derivation of both charpolys; audit the Trust/README residual wording for
  over/under-claim; (3) standard §7.10 (axioms, forbidden scan, freeze-check,
  `lean_dag_check`).
* **Conflicts between commission text and disk:** **none.** The single-writer deviation
  (no node/index/DAG markdown) is commissioned and observed: the only files I created are
  this report, `tools/whgap_r14_*.py`, and `artifacts/logs_whgap_lean4_20260801/r14_*`.
  One temporary Lean probe was compiled out of tree and removed from the project directory
  (its source is archived as `r14_scratch.lean` in the log directory).

**Anchoring ban (7c), declared:** `tools/whgap_r14_charpoly_check.py` and
`tools/whgap_r14_rank_check.py` were written and run **before** opening
`artifacts/whgap_lean4_20260801.md`, `tools/whgap_lean4_wpg_check.py`, or any of the
reviewed proofs. The charpoly script is built **only** from the frozen conventions of
[`WHGAP_REVIEW_COMMISSION_R5_20260729.md`](../channel-capacity/werner-holevo-gap/notes/WHGAP_REVIEW_COMMISSION_R5_20260729.md)
§1 (channel, Kraus set, padded complement, witness state) — not from `Channel.lean`'s
displays. The rank script uses only the **definitions** `pat`, `cco`, `V3`
(`DefectChoi.lean:104–277`), which are the objects the claim is about, and none of the
reviewed proofs. My route differs from the executor's: I carry `√(x/2)`, `√(1−x)` as free
symbols and eliminate them at the end by the ring relations `s²=x/2`, `t²=1−x`, `st=β`;
I compute charpolys as `det(X·1 − M)` rather than by block splitting.

---

## 1. Own re-derivation of the two charpolys (gates R14-A0 … A9, ALL PASS)

Script `tools/whgap_r14_charpoly_check.py`, log
`artifacts/logs_whgap_lean4_20260801/r14_charpoly_check.log`.

| gate | content | result |
|---|---|---|
| A0a–A0d | `P_ψ` rank-1 projector; `τ(ψ)=0` (isotropic); `ρ_ε` Hermitian, trace 1; `P_ψᵀ = P_ψ̄` | PASS |
| A1 | Kraus sum `Σ K_a Y K_aᵀ` **=** `(1−x)Y + (x/2)(Tr Y·1 − Yᵀ)` for a **fully generic** 3×3 `Y` (9 independent symbols) | PASS |
| A2 | `Tr Λ(ρ_ε) = Tr Λ^c(ρ_ε) = 1` | PASS |
| **A3** | `charpoly Λ(ρ_ε) = (X−(1−ε)(1−x/2))(X−ε(1−x/2))(X−x/2)`, **symbolically in (x,ε)** | PASS |
| **A4** | `charpoly Λ^c(ρ_ε) = (X²−(1−x/2)X+2x(1−x)ε(1−ε))(X−x(1−ε)/2)(X−xε/2)`, **symbolically in (x,ε)**, modulo `β² = x(1−x)/2` | PASS |
| A5 | the reduction really needs `hβ`: before using `β² = x(1−x)/2` the two sides differ ⇒ the hypothesis is **load-bearing, not decorative** | PASS |
| A6 | `λ± = [(1−x/2) ± √discE]/2` are exactly the quadratic factor's roots | PASS |
| A7 | `ε → 0`: `spec Λ(P_ψ) = {1−x/2, x/2, 0}`, `spec Λ^c(P_ψ) = {1−x/2, x/2, 0, 0}` (the known base point) | PASS |
| A8 | independent **value** gates at four distinct rational `(x,ε)`: `(9/20,1/7)`, `(1/5,1/3)`, `(49/100,1/50)`, `(3/10,2/5)` | PASS |
| A9 | `β := st` satisfies `β² = x(1−x)/2` | PASS |

My independently assembled `Λ^c(ρ_ε)` is, entry for entry, the matrix of `LamCWit_eq`:
diagonal `(1−x, x/4, x/4, x/2)`, `(0,3)`-entry `−iβ(1−2ε)`, `(1,2)`-entry `−i(x/4)(1−2ε)`,
Hermitian conjugates below. Likewise `Λ(ρ_ε)` matches `LamWit_eq` in the standard basis.
The `{0,3} ⊔ {1,2}` block structure, the two traces (`1−x/2`, `x/2`) and the two
determinants (`2x(1−x)ε(1−ε)` after `hβ`; `x²ε(1−ε)/4`) all reproduce.

**Symbol-by-symbol comparison with `IcScalar`'s lists** (`IcScalar.lean:192–196`):

* `specB x ε = [(1−ε)(1−x/2), ε(1−x/2), x/2]` — the three linear factors of `specB_charpoly`,
  identical term for term; `specB_charpoly_list` states exactly the product form.
* `specE x ε = [lamP, lamM, (x/2)(1−ε), (x/2)ε]` — `x(1−ε)/2 ≡ (x/2)(1−ε)` and
  `xε/2 ≡ (x/2)ε`; the `λ±` pair enters through `quad_eq_lamP_lamM`, whose hypotheses
  `0 ≤ x ≤ 1` are exactly what `discE ≥ 0` (SOS form
  `discE = (1−3x/2)² + 2x(1−x)(1−2ε)²`, re-derived here) requires for `Real.sqrt` to behave.
  The extra hypotheses appear **only** in the list form, never in `specE_charpoly` — the
  square-root-free level is genuinely square-root free, as claimed.

**Statement fidelity vs the frozen commission text** (§7.10 item 3): both statements are
*verbatim* the commissioned ones, with the E side kept at the quadratic factor. Nothing is
weakened: no quantifier is dropped (`specB_charpoly` has **no** hypothesis; `specE_charpoly`
has exactly `hβ`), no inequality is loosened, no implication reversed. Both are stated for
arbitrary complex `x, ε, β`, i.e. **strictly stronger** than the physical case, and the
Hermiticity lemmas for real parameters are stated separately — the executor's own note on
this is accurate.

**Non-vacuity, checked in Lean, not only in sympy** (report §5 item 5 asked for this;
`r14_scratch.lean`, compiled out of tree with `lake env lean`, exit 0):

```
example : (Lam (1/5 : ℂ) (rhoWit (1/4 : ℂ))).charpoly
        = (X - C (27/40)) * (X - C (9/40)) * (X - C (1/10))        -- three DISTINCT roots
example : (LamC (1/9 : ℂ) (2/9 : ℂ) (rhoWit (1/4 : ℂ))).charpoly
        = (X^2 - C (17/18) * X + C (1/27)) * (X - C (1/24)) * (X - C (1/72))
example : WHGAP.DefectChoi.Cmat (1/2 : ℝ) ≠ 0                       -- from rank_Cmat_half
```

The E-side instance also settles satisfiability of `hβ` by **rationals**
(`(2/9)² = (1/9)(8/9)/2`), so the hypothesis is not vacuously restrictive.

## 2. Own re-derivation of the rank route (gates R14-B0 … B9, ALL PASS)

Script `tools/whgap_r14_rank_check.py`, log `r14_rank_check.log`. `Cmat` was rebuilt from
the fifteen `pat` patterns and fifteen `cco` coefficients and evaluated exactly over ℚ.

| gate | content | result |
|---|---|---|
| B0 | `V₃ᵀV₃ = 16·1₃` (so `V₃` has full column rank 3) | PASS |
| B1 | **`Cmat(1/2) = (1/18)·V₃V₃ᵀ`, all 729 entries, exact** — the content of `Cmat_half_factor` | PASS |
| B2 | **`V₃ᵀ Cmat(1/2) V₃ = (128/9)·1₃`** — the content of `V3R_Cmat_half_V3R`; `det = (128/9)³ ≠ 0` | PASS |
| B3 | **`rank Cmat(1/2) = 3`** by my own exact rank over ℚ (no factorization used) | PASS |
| B4 | `charpoly Cmat(1/2) = X²⁴(X−8/9)³` (consistency with `charpoly_half`) | PASS |
| B5/B6 | symmetric; spectrum `{(8/9)³, 0²⁴}`, PSD | PASS |
| B7 | both legs of the sandwich hold numerically | PASS |
| B8/B9 | **regime gate (7b):** `rank Cmat(x) = 8` at `x = 4/7, 26/51, 49/100, 5/6`; `= 5` at `x = 1/3`; `= 3` only at `x = 1/2` | PASS |

**Route soundness, checked as a proof and not only as arithmetic.** The Lean proof is
`rank C ≤ rank((1/18)•V₃) ≤ card (Fin 3) = 3` (`rank_mul_le_left`, `rank_le_card_width`)
and `3 = rank((128/9)•1₃) = rank(V₃ᵀ C V₃) ≤ rank(V₃ᵀ C) ≤ rank C`
(`rank_of_isUnit` via `isUnit_smul_one_three`, then `rank_mul_le_left`/`rank_mul_le_right`),
closed by `omega`. Both directions are valid for **any** field; no diagonalizability,
no symmetry, no PSD-ness is used, and `charpoly_half` is not invoked anywhere in the proof
term. The R13 MAJOR-2 defect (charpoly ⇒ rank) is therefore genuinely repaired, and
repaired the strong way.

**Statement vs paper Thm 3.3(2).** The paper's clause reads "*rank C_x = 8 for
x ∈ (1/2,1), and rank C_{1/2} = 3*". Lean proves the **second** conjunct only; the
docstrings say "paper Theorem 3.3(2) **at the physically decisive point**", which is
accurate but does not name the unformalized first conjunct (minor m5 — I verified that
conjunct myself at three interior `x`, so it is true, merely unchecked in Lean). The
paper's factorization `C_{1/2} = (2/9)Σ_μ |vec G_μ⟩⟨vec G_μ|` is consistent with the Lean
one: `V₃`'s columns have squared norm 16, and `(1/18)·16 = 8/9`, matching the paper's three
nonzero eigenvalues `8/9`.

**The four glosses (R13 MAJOR-2) — all four checked, all correct:**
`DefectChoi.lean` module header (the corrected `charpoly_Cmat` bullet + the new
`rank_Cmat_half` bullet), `multiplicity_unique`'s scope item 2, `charpoly_half`'s docstring
scope paragraph, and `README.md` item 9. Each now says the charpoly gives the **multiset**
and `rank_Cmat_half` gives the **rank**, and each states the non-inference explicitly. A
tree-wide grep found no surviving "charpoly ⟹ rank" reading.

## 3. Build reproduction and standard §7.10 gates (reproduced, not trusted)

| gate | command | my result | executor's claim |
|---|---|---|---|
| clean rebuild | `rm -rf .lake/build/lib/lean/WHGAP*; lake build` | **exit 0**, "Build completed successfully (**3202 jobs**)" (`r14_build.log`) | exit 0, 3202 jobs — matches |
| `#print axioms` | same build | **232** declarations, **every one** on `[propext, Classical.choice, Quot.sound]` or a subset; **0 non-standard** (`r14_print_axioms.txt`) | 232 (206 + 26) — matches |
| new-declaration census | `Trust.lean` §"Support.Channel (LEAN-4 WP-G)" | **26** `#print axioms` lines covering **every** §8 declaration incl. `psiWit`…`specE_charpoly_list`; the three LEAN-3.2 rank declarations are also present (lines 249–251) | complete — matches |
| forbidden constructs | grep `sorry`/`native_decide`/`implemented_by`/`axiom` | **9 hits, all prose in docstrings; 0 code occurrences** (`r14_forbidden_scan.txt`); `decide` used only for the small integer certificates and the four `Equiv` inverse proofs — kernel `decide`, never `native_decide` | matches |
| freeze-check | `whgap_lean_freeze_claims.py --check` | **8/8 ok**, hashes unchanged (`r14_gates.txt`) | matches |
| `lean_dag_check` | `--problem werner-holevo-gap` | **0 FAIL**, 2 WARN (the two documented scoped-input exceptions on P4/P6), 1 INFO | matches |
| `proof_dag_check` / `literature_check` | — | **OK, 16 nodes**, exit 0 / exit 0 | matches |
| warnings | build log | **22**, unchanged from the LEAN-3.2 baseline | matches |
| ledger | `SHA256SUMS.txt` | **9/9 verify** under the file's declared LF-normalization convention | matches |
| file scope | `git status` | only `README.md`, `Support/Channel.lean`, `Trust.lean` modified under the Lean project; **no node file, no `NODE_INDEX.md`, no DAG doc touched**; the Channel.lean diff is the docstring plus an appended §8 (from line 455) — the R13-reviewed §1–§7 proof content is byte-unchanged | matches |

`split3`/`split4` audited by hand as permutations: `split3 : 0,1 ↦ inl 0, inl 1; 2 ↦ inr 0`;
`split4 : 0 ↦ inl 0, 3 ↦ inl 1, 1 ↦ inr 0, 2 ↦ inr 1` — exactly the `{0,3} ⊔ {1,2}` split,
and `charpoly_of_reindex_blocks` is `charpoly_reindex` + `charpoly_fromBlocks_zero₁₂`, which
assumes only that the off-diagonal blocks vanish (proved by `ext`, not assumed).

## 4. Residual-display audit (over-claim / under-claim)

The claim under audit is the three-place wording of residual (b). My finding: **accurate,
in all three places.**

* `Trust.lean` §"2026-08-01 (LEAN-4 WP-G)" — heading says "CLOSED AT CHARPOLY LEVEL", body
  says **"REDUCED, not removed"** and names the missing glue in one sentence: *"same
  characteristic polynomial ⟹ same `vnEntropy`" is not available for complex Hermitian
  matrices in this development.* I verified the underlying fact: `Support/Entropy.lean`
  builds `vnEntropy` over `ℝ` for real symmetric matrices only, and none of its lemmas
  applies to a `Matrix (Fin 3) (Fin 3) ℂ`. The earlier WP-D subsection saying "(b) STILL
  OPEN" is left intact above it (append-only), with an explicit "what HAS moved" pointer —
  no reader is left with a contradiction.
* `Channel.lean` honesty item 4 — states what is proved and what is missing, preserves the
  R13 MAJOR-1 history (the phantom declarations that once appeared there now exist), and
  correctly notes that `specE_charpoly_list` is the *only* place the square root reappears.
* `README.md` item 10 — amended with the previous text quoted verbatim, and adds the correct
  consequence: "nothing here yet turns the two charpolys into `S(Λ(ρ_ε)) − S(Λ^c(ρ_ε))`,
  and the achievability reading `hach` is untouched."

**Under-claim check.** Nowhere does the tree still say the §6 complex spectra "were not
reached in Lean" — except in `IcScalar.lean`'s own honesty note (minor m2) and in the
manuscript's Lean-status paragraph (minor m3).

**Value-vs-formula (7f).** What I established, explicitly:

1. The **statements** `specB_charpoly`, `specE_charpoly`, `Cmat_half_factor`,
   `V3R_Cmat_half_V3R`, `rank_Cmat_half` are TRUE — verified as **formulas** (symbolic in
   `(x,ε)`; the rank statements are pointwise at `x = 1/2` and exact over ℚ) by an
   **independent construction** (my Kraus rebuild from the frozen conventions; my own
   `pat`/`cco` assembly), plus value gates at ≥ 4 rational parameter points.
2. That the Lean **proofs** establish them is carried by the kernel (build reproduced,
   axioms clean, no `sorry`), not by my sympy; my sympy corroborates the statements, not
   the proof terms. Both are reported, per 7f.
3. **What the charpoly theorems do NOT buy, quantified:** my gate R14-C5 computes
   `S(Λ(ρ_ε)) − S(Λ^c(ρ_ε))` from an independent numeric diagonalization of the Kraus-built
   outputs and compares it with `IcScalar`'s list formula at `(x,ε) = (0.2,0.25)`,
   `(0.45,0.05)`, `(0.39,0.001)`: agreement to `< 1e-41`. This is exactly the step that
   remains **outside Lean**, and it is a numerical corroboration only — it does not
   discharge the complex-Hermitian entropy glue. The residual display is right to keep it
   open.

## 5. Rule-7 checklist

* **(7a) Type audit.** `Lam : R → Matrix (Fin 3) (Fin 3) R → Matrix (Fin 3) (Fin 3) R` over
  `[Field R] [CharZero R]`, instantiated at `R = ℂ` — checked that `ℂ` satisfies the
  instance and that no `ℝ`-bound definition (`Jlift`, `Jdag`, `Defect`) enters §8.
  `LamC : ℂ → ℂ → Matrix 3×3 ℂ → Matrix (Fin 4) (Fin 4) ℂ` — the **padded 4-dimensional**
  complement of the frozen convention, not the 3-dimensional one (failure mode §2.3
  screened). `rhoWit : ℂ → Matrix (Fin 3) (Fin 3) ℂ` is a *state* only for real
  `ε ∈ [0,1]`; the charpoly statements do not need that and do not claim it.
  `charpoly ∈ ℂ[X]`, monic of degree 3 resp. 4 — the two claimed products have degrees
  `1+1+1` and `2+1+1`, so no factor is lost. **Adjoint convention (failure mode §2.4):**
  `LamK`/`LamCK` use `ᵀ`, not `ᴴ`; for real Kraus scalars `s,t` (the physical case)
  `K† = Kᵀ`, and for arbitrary complex `s,t` the statements are algebraic identities about
  a different object — I checked that no claim in the tree reads the `ᵀ`-version as the
  physical complement without the real-parameter proviso (`LamCWit_isHermitian` is stated
  for real `x, ε, β`, and README item 1 keeps "`LamCK` is *the* complementary channel"
  outside Lean). `Cmat : ℝ → Matrix (Fin 27) (Fin 27) ℝ`; `V3R : Matrix (Fin 27) (Fin 3) ℝ`;
  `V3Rᵀ C V3R : Matrix (Fin 3) (Fin 3) ℝ` — the sandwich types compose.
* **(7b) Regime-complete identity gates.** Both charpolys verified **fully symbolically** in
  `(x,ε)` (E side modulo the `β` relation) *and* at four distinct rational points; the
  degeneracy regime is exercised on purpose (gate C4: at `(x,ε) = (2/5,1/4)` the B-spectrum
  collapses to 2 distinct values — the charpoly still pins the multiset); the rank statement
  is checked across six `x` covering all three qualitative regimes (generic 8, `λ₃ = 0` ⇒ 5,
  `λ₅ = 0` ⇒ 3) and at the eigenvalue-coincidence point `x = 5/6` where the rank does **not**
  drop.
* **(7c) Anchoring ban.** Declared in §0; my derivation route (free-symbol square roots,
  `det(X·1 − M)`) differs from both the executor's Lean route (block splitting +
  trace/determinant) and its sympy route. No notational coincidence to flag beyond the
  shared frozen conventions of R5 §1, which are the definition of the problem.
* **(7d) Frozen-input scope.** I relied on no pending-review claim. `Cmat`'s *definition*
  and `V3` were read from the source (they are the objects of the claim); the
  Kraus↔`LamCgen` bridge that `specE_charpoly_kraus` needs was **re-verified here
  generically** (gate C1: all 16 entries for a fully generic complex 3×3), rather than
  imported from the R13-reviewed record.
* **(7e) Standing failure modes** (R5 §2, item by item): 1 sympy `.H` on real symbols —
  avoided by carrying `s,t` as symbols and reducing by ring relations; 2 pinned interpreter
  `C:<home>/cpython3119/python.exe` used throughout; 3 complement convention — padded
  4-dim verified generically; 4 transpose vs conjugate-transpose — audited above; 5
  `sorted()`/`eigenvals` on symbolic spectra — avoided (`det(X·1 − M)`, and the one
  `eigenvals` call is on a numeric matrix); 6 CRLF — my ledger and JSON are written LF and
  the executor's ledger verifies 9/9 under its declared convention; 7 degeneracy
  bookkeeping — gate C4; 8 `ε log ε` — not in scope of these statements; 9 anchoring — §0.
* **(7f) Value vs formula.** §4.
* **(7g) Quantifier hygiene.** Every term of art in the reviewed statements resolves:
  "closed at charpoly level" (defined in the same Trust subsection), "complex-Hermitian
  entropy glue" (resolves to `Support/Entropy.lean`'s declared real-symmetric scope),
  "residual (b)" (row (b) of the Trust table), "physically decisive point" (`x = 1/2`,
  `λ₅ = 0`, fixed by `lam5_eq_zero_iff`).

## 6. Findings

**MAJOR: none.**

**Minors (documentation / record accuracy; none affects what is proved):**

* **m1 — a false statement in a script header.** `tools/whgap_lean4_wpg_check.py`'s module
  docstring (gate list, line ~41) says "*G13 … at (x,eps) = (2/5, 1/4) the three
  B-eigenvalues are pairwise distinct*". That is **false**: at `(2/5,1/4)`,
  `specB = [3/5, 1/5, 1/5]` (independently confirmed by my gate R14-C4). The **code** at
  line 266ff is correct — it records the degeneracy in a comment and uses `(1/5,1/4)` — and
  the WP-G report §3 records it honestly; only the header was left stale. Fix: sync the
  docstring line.
* **m2 — stale under-claim in `IcScalar.lean`.** Its honesty note (lines 30–46) still reads
  "*that they are the outputs of `Λ_x` and `Λ_x^c` at `ρ_ε` is the note's gates G2/G3
  (exact symbolic computation from the Kraus operators), **not Lean***". Since WP-G, the
  load-bearing half of that — that the two **lists** `specB`/`specE` are the spectra of the
  Lean-defined channel outputs — *is* a Lean theorem (`specB_charpoly_list`,
  `specE_charpoly_list`), and `IcScalar` consumes the lists, not `BOut`. The file contains
  no reference to WP-G at all (grep: zero hits for `Channel`, `specB_charpoly`, `LEAN-4`).
  Fix: one cross-reference sentence, retaining the true residue (the matrices `BOut`,
  `blockA`, `blockB` are still not proved equal to the outputs). Same class as R13 m1.
* **m3 — the manuscript's Lean-status paragraph is now stale** (`paper/main.tex:1046–1048`):
  "*the complex-spectra identification of Lemma `lem:exactspec`, the latter verified by
  computer algebra and independent review rather than in Lean*". After WP-G that
  identification **is** in Lean at characteristic-polynomial granularity; what is not in
  Lean is the passage from the two charpolys to the entropies. The paper was outside WP-G's
  declared file scope, so this is a decision-layer follow-up, not an executor defect — but
  it is the outward-facing statement and should be refined, not merely deleted.
* **m4 — an unmarked unformalized gloss.** `Channel.lean:546–547` states "`IcScalar.BOut`
  is its diagonal form in the `(ψ, ψ̄, e₃)` frame". The fact is **true** (I re-derived it:
  `Λ(ρ_ε) = (1−ε)(1−x/2)P_ψ + ε(1−x/2)P_ψ̄ + (x/2)P_{e₃}`), but it is not machine-checked
  anywhere and carries no scope marker at that spot — formally the same class as R13
  MAJOR-2, though disarmed by honesty item 4 and by report §2 a few paragraphs away. Fix:
  add "(true, not formalized)".
* **m5 — the unformalized half of Thm 3.3(2) is not named.** The glosses say "paper
  Theorem 3.3(2) at the physically decisive point"; the theorem's **first** conjunct
  (`rank C_x = 8` on `(1/2,1)`) is nowhere stated as excluded. I verified it holds at
  `x = 4/7, 26/51, 49/100` exactly, so nothing is wrong — but a reader should be told which
  conjunct is machine-checked. Fix: one clause in the `rank_Cmat_half` docstring.

**Recorded, not silent (my own):** my rank script's first design expectation — that the
eigenvalue-coincidence point `x = 5/6` (`λ₅ = λ₃`) would also drop the rank — was **wrong**
(both eigenvalues are nonzero there, so the rank stays 8). The gate was corrected with the
reasoning written into the script rather than silently edited. No bearing on the reviewed
work.

## 7. Licensing statement

Per the commission's menu, **(A)**:

> `rank_Cmat_half` and the WP-G package are licensed as recorded; the residual display is
> accurate.

Concretely, the following are licensed at the tier the decision layer may now write, citing
this report: `Cmat_half_factor`, `V3R_Cmat_half_V3R`, `rank_Cmat_half` (paper Thm 3.3(2),
second conjunct, unconditional); `Pwit_eq_outer`, `PwitBar_eq_outer`, `rhoWit_eq`,
`rhoWit_trace`, `rhoWit_isHermitian`, `LamWit_eq`, `LamCWit_eq`, `LamWit_isHermitian`,
`LamCWit_isHermitian`, `specB_charpoly`, `specE_charpoly`, `specB_charpoly_kraus`,
`specE_charpoly_kraus`, `specB_charpoly_list`, `quad_eq_lamP_lamM`, `specE_charpoly_list`
and the four plumbing lemmas. The scope of the license is **exactly** what the tree says:
residual (b) is closed at characteristic-polynomial level and only there; the
complex-Hermitian entropy glue, `hach`, and the three `CapacityInterface` fields are
untouched, and a green build remains evidence (NUMERICAL), never a status.

The five minors are documentation items; none of them is a condition on this license.

## 8. Artifacts

* Scripts: `tools/whgap_r14_charpoly_check.py`, `tools/whgap_r14_rank_check.py`,
  `tools/whgap_r14_ic_check.py`.
* Logs (`artifacts/logs_whgap_lean4_20260801/`): `r14_charpoly_check.log`,
  `r14_charpoly_gates.json`, `r14_rank_check.log`, `r14_rank_gates.json`,
  `r14_ic_check.log`, `r14_ic_gates.json`, `r14_build.log`, `r14_print_axioms.txt`,
  `r14_forbidden_scan.txt`, `r14_gates.txt`, `r14_scratch.lean`, `r14_scratch.log`,
  and `r14_SHA256SUMS.txt` (LF-normalized digests of all of the above plus the scripts).
* Interpreter: `C:<home>/cpython3119/python.exe` (sympy 1.13.1, mpmath at 50 dps);
  Lean toolchain `leanprover/lean4:v4.31.0` with the pinned Mathlib.

