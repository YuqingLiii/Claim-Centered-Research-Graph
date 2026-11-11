# R13 — independent §7.10 review of the WHGAP LEAN-3 batch (WP-F / WP-E / WP-D)

**Reviewer:** fresh Opus 5 instance, 2026-08-01. **Role:** reviewer.
**Independence statement:** I did not author any part of the LEAN-3 batch, I was given no
desired outcome, and the licensing menu was presented to me as alternatives.
**Commission:** `channel-capacity/werner-holevo-gap/notes/WHGAP_COMMISSION_LEAN3_20260801.md`
(R13 paragraph) + the rule-7 embeds of
`notes/WHGAP_REVIEW_COMMISSION_R5_20260729.md` §§1–3.
**Reviewed inputs (frozen):** commits `b0cd426` (WP-F), `989bb63` (WP-E), `1d976f5` (WP-D);
`artifacts/whgap_lean3_20260801.md`; `WHGAP/Support/SelfComplement.lean`,
`WHGAP/Support/Channel.lean`, the LEAN-3 diffs to `WHGAP/Support/DefectChoi.lean`,
`WHGAP/private-boundary.lean`, `WHGAP/order-boundary.lean`, `WHGAP/Trust.lean`,
`proof-dag/lean/README.md`, `WHGAP.lean`; `proof-dag/nodes/WHGAP.goal.md`.

---

## VERDICT

**(B) FINDINGS — 2 MAJOR + 10 minor.**

**Neither MAJOR is a soundness defect.** Everything the batch *proves* is correct: I rebuilt
the tree from scratch (exit 0), re-derived every LEAN-3 statement in my own construction
before reading the executors' notes (rule 7c), and all 37 of my independent gates PASS,
including a from-scratch Kraus rebuild of the 27×27 defect Choi matched entry-by-entry
against `Cmat` at four rational `x`. Both MAJORs are **over-claims in the honesty layer** —
the one thing this review exists to gate — and both are one-paragraph repairs.

> **Conditional license.** Once MAJOR-1 and MAJOR-2 are corrected as prescribed below,
> licensing statement (A) — *"the LEAN-3 batch is a faithful extension; the substitutions are
> sound; the degradation is honest; the trust boundary is accurately displayed"* — is fully
> supported by this review, with the qualification that the trust-boundary display should also
> absorb minors m1, m2 and m5.

Evidence tier of the batch remains **NUMERICAL** (a green build is a run, DAG protocol §2 /
§7.1); this review is the completion gate for the decision layer to act on, not a status write
by me.

---

## PRE-ACTION REPORT

* Target node **`WHGAP.goal`**, status as read from disk: **OPEN**
  (`channel-capacity/werner-holevo-gap/proof-dag/nodes/WHGAP.goal.md:7`; composition
  `status: OPEN`, `rel: ["P13 (the strip) is CONJECTURED, not resolved", "x = 1 endpoint tier
  per P4"]`).
* Role: **reviewer**; independence statement above.
* Highest status my evidence could license per §2: a completed rule-6/rule-7 review **opens**
  the completion tier for the decision layer to write, citing this artifact; I write no node
  status myself (single-writer deviation, commissioned).
* Gates/deliverables, one line each: (1) reproduce the clean build + `#print axioms` +
  forbidden scan + freeze-check + `lean_dag_check`; (2) special audits WP-F / WP-E / WP-D per
  the commission's items 2(a)–(c); (3) trust-boundary accuracy after the batch (§7.9/§7.10.6);
  (4) vacuity/satisfiability (§7.10.5); (5) own-script numerical/symbolic spot checks.
* Conflict between my commission text and the disk protocols: **none.**

---

## 1. Reproduction gates (§7.10.1–2)

| gate | what I ran | result |
|---|---|---|
| clean rebuild | deleted `.lake/build/lib/lean/WHGAP*` then `lake build` in `proof-dag/lean` | **exit 0**, `[3201/3202]` jobs — `artifacts/logs_whgap_lean3_20260801/r13_build.log` |
| `#print axioms` | from my own build transcript, all `Trust.lean` rows | **203/203** declarations; 200 on `[propext, Classical.choice, Quot.sound]`, 3 on strict subsets; **0 non-standard, 0 `sorryAx`** — `r13_print_axioms.txt` |
| forbidden constructs | my own 13-pattern scan of `proof-dag/lean/WHGAP/` | **0 in code**; every `sorry`/`native_decide`/`implemented_by` hit is prose in a docstring. `decide` occurs only in the eight pre-existing WP-A integer certificates (kernel-checked, permitted); **no `native_decide` anywhere** — `r13_forbidden_scan.txt` |
| frozen Claims | `tools/whgap_lean_freeze_claims.py --check` | **8/8 ok**, exit 0 — no Claim text or hash moved in LEAN-3 |
| §7.6 anti-drift | `tools/lean_dag_check.py --problem werner-holevo-gap` | exit 0 — **0 FAIL**, 2 WARN, 1 INFO, byte-identical to the R12/LEAN-2 baseline (the two documented scoped-input exceptions on P4/P6) |
| structure / literature | `tools/proof_dag_check.py --problem werner-holevo-gap`, `tools/literature_check.py` | exit 0 / exit 0 (only the registered `WHGAP/Model.lean` orphan WARNING, M7-F2) |
| SHA ledger | recomputed every row under the declared LF convention | 26 distinct files; **the last (most recent) row matches the current file for 25 of 26**. The one exception is `nodes/WHGAP.goal.md` — see minor m8. Earlier rows for files later edited by a subsequent work package mismatch **by design** (append-only per-package ledger). |
| import graph | read all `import` lines | node-module imports unchanged = the propagating skeleton; LEAN-3 added only `Support` imports (`private-boundary → Support.Channel`, `Trust → Support.{Channel,SelfComplement}`). Consistent with §7.6 check 6, and `lean_dag_check` agrees. |

`WHGAP/SelfTest.lean` is byte-identical to its pre-LEAN-3 version (`git diff` empty) — the
executors' single-writer note that it was deliberately not extended is accurate.

**Axiom-census coverage note (not a finding).** 30 public auxiliary lemmas (casts `toR_*`,
`mapR_*`, the `Support.Basic` denominator lemmas, `Channel.leg*_val`/`dl_cast`,
`SelfComplement.A_zero/one/two`) are not individually listed in `Trust.lean`. Every one of
them is in the dependency closure of a listed theorem, so a `sorryAx` in any of them would
surface in the listed theorem's axiom line; combined with the clean forbidden scan the census
is transitively complete.

---

## 2. Method: my own derivations came first (rule 7c, anchoring ban)

Before opening `artifacts/whgap_lean3_20260801.md` or any of the executors' check scripts
(`whgap_lean3_wpd_check.py`, `whgap_lean3_wpe_charpoly.py`, `whgap_lean2_wpa_codegen.py` —
none of which I read at any point), I read the manuscript
(`paper/main.tex`: `eq:kraus`, `eq:comp`, `eq:Jintro`, `eq:defect`, `eq:master`,
`eq:charpoly`, `lem:x1`, `thm:necessity`, `eq:epsc`, `lem:holevo`, `thm:private`) and the
Lean statements, and wrote **`tools/whgap_r13_defect_check.py`** — an independent exact-sympy
rebuild. Where my construction unavoidably coincides with the executors' (the substitution
`x = 2/(9q²+2)`), I deliberately used a *different* reduction instead: I kept `x` symbolic and
reduced modulo the chart ideal by `q² ↦ 2(1−x)/(9x)`, then required both the `q⁰` and the `q¹`
coefficient to vanish. **Reported coincidence (7c):** my `Jdag` was obtained by
differentiating `⟨Z, J(Y)⟩` in the entries of `Y`, i.e. by a route independent of the
hand-written Lean formula; Lean's `Jdag_adjoint` pins its `Jdag` uniquely to the same object,
so the two agree by construction and not by copying.

**All 37 gates PASS** (`r13_defect_check.log`). The load-bearing ones:

| gate | content | 7f: value or formula |
|---|---|---|
| R1a–c | `A_μᵀ = −A_μ`; `½Tr(A_μ X A_νᵀ) = ½(δ_{μν}Tr X − (Xᵀ)_{μν}) = (Λ₁(X))_{μν}` | **FORMULA**, symbolic in a general `3×3` `X` |
| R2a–e | `g = f − s²`, `g(0)=0`, `g' = log(1+s) − log(1−s) − 2s`, `h(0)=0`, `h' = 2s²/(1−s²) ≥ 0`; series `f = s² + s⁴/6 + s⁶/15 + …` | **FORMULA** (derivatives symbolic), plus 5 sample values |
| R3a–d | `x b_ε − 2(1−3x/2)²(1−ε) = 2(1−x)[(2x−1) + (1−3x/2)ε]`; bracket vanishes exactly at `ε = ε_c(x)`; `g_E < g_B` inside the window; the `ε=0` gap identity | **FORMULA** + 3 `(x,ε)` values |
| R4 | **own Kraus-built defect Choi = Appendix A `Cmat`, all 729 entries**, at `x ∈ {3/10, 26/51, 1/2, 4/7}` | **VALUES** at 4 exact rational `x` (729 entries each) |
| R4b | `Σ_a K_a X K_aᵀ = eq:family` and `Tr(K_a X K_bᵀ) = eq:comp`, symbolic `X`, at the same 4 `x` | **FORMULA** in `X` |
| R5 | **the nine general-`(τ,Y)` entry identities** `Δ_J(τ)(Y) = Σ_k c_k(x) W_k(τ,Y)`, 18 free entries each side | **FORMULA**, symbolic in `x`, `q`, `τ`, `Y` |
| R6 | the fifteen `word_k(E_ij,E_rs)[b,b'] = pat_k` identities on a 25-point index grid | **VALUES** (25 index pairs × 15 words) |
| R7/R7b | `charpoly = z¹⁹(z−λ₅)⁵(z−λ₃)³` at 4 rational `x`, by **Berkowitz on the 27×27 matrix**, computed **twice**: once from my Kraus-built Choi, once from the Appendix A table — **neither through the `F/G` (Weinstein–Aronszajn) factorization nor through any similarity** | **VALUES** at 4 exact rational `x` |
| R7c/d | `charpoly(C_{1/2}) = z²⁴(z − 8/9)³` and `rank C_{1/2} = 3` (own computation) | **VALUES** |
| R8a–c | `Λ_x(ρ_ε + θX) = outB(α,b,u)` and `Λ^c_x(ρ_ε + θX) = outE(1−x, xε, e, −v)` for **every** `β`, both signs of `θ` | **FORMULA**, symbolic in `x, ε, θ, r, β` |
| R8d | `ρ_ε ± tX ⪰ 0` at the frozen point `ε = t = ε_c/2`, three `x` | **VALUES** (see m5) |
| R9 | `s=√(x/2)`, `t=√(1−x)`, `q=t/(3s)` ⟹ `9xq² = 2(1−x)` **and** `st = (3x/2)q`, four `x` | **VALUES** |

I also ran an out-of-tree Lean probe (`r13_probe.log`, `lake env lean`, nothing added to the
tree) printing the **elaborated signatures** of every LEAN-3 declaration and discharging four
satisfiability theorems (§4 below). All four probe theorems compile on the three standard
axioms.

**7a — type audit of the new objects.** `A : Fin 3 → Matrix (Fin 3) (Fin 3) R` (Levi-Civita,
input×input); `K s t : Fin 4 → Matrix (Fin 3) (Fin 3) R` (**four** Kraus operators, padded
environment); `LamK/Lam : Matrix (Fin 3) (Fin 3) → Matrix (Fin 3) (Fin 3)`;
`LamCK/LamC : Matrix (Fin 3) (Fin 3) → Matrix (Fin 4) (Fin 4)` (3-dim input → **4**-dim padded
environment, matching `eq:comp`); `Jlift : Matrix (Fin 3) (Fin 3) → Matrix (Fin 4) (Fin 4)`
(receiver `L(ℂ³_B)` → environment `L(ℂ⁴_E)`, the direction `J : L(H_B) → L(H_E)` of `thm:zw`);
`Jdag` the reverse; `Defect x q : (τ Y : Matrix (Fin 3) (Fin 3)) → Matrix (Fin 3) (Fin 3)` — a
*bilinear* map, i.e. the superoperator-valued map `τ ↦ Δ_J(τ)` in uncurried form;
`choiOf : (bilinear) → Matrix (Fin 27) (Fin 27)` with row `(i,b,b') = 9i+3b+b'` and column
`(j,r,s)`. I re-derived the Choi convention independently from `eq:defect`: vectorizing a
superoperator `Ψ` on `L(ℂ³)` row-major gives `Ψ̂_{(b,b'),(r,s)} = Ψ(E_{rs})_{b,b'}`, so
`C = Σ_{ij}|i⟩⟨j|_A ⊗ Ψ̂(E_{ij})` has exactly the row/column roles `choiOf` uses and the paper's
"input leg first". **The row/column-leg orientation flagged by the WP-D executor as the place a
silent error could hide is correct**, and my 729-entry agreement at four `x` is the check.
`SelfComplement.LamCmin : Matrix (Fin 3) (Fin 3) ℝ → Matrix (Fin 3) (Fin 3) ℝ` — the two
`Fin 3`s are the **input** index of `X` and the **environment** index `μ,ν` of the *minimal*
(3-dim) representation; identifying them is the content of self-complementarity, not an
accident, and the module's SCOPE block says the minimality itself is not formalized. Correct.

**7e — standing failure modes screened.** (1) sympy `.H` on real symbolics: avoided, `.T`
throughout, and the reality of the Kraus set is what makes it sound (checked). (2) pinned
interpreter `C:<home>/cpython3119/python.exe` used for everything. (3) complement
convention drift 3-dim vs padded 4-dim, sign of the `a(Y)` block, the `k` factor: checked
entrywise against `eq:comp` — `LamCgen`'s cross block is `+β a(X)` above the diagonal and
`−β a(X)` below, and its lower-right block is `c(Tr X·δ − Xᵀ)`, both as displayed. (4)
transpose vs conjugate-transpose in the HS adjoint: `Jdag_adjoint` is stated for the real
bilinear pairing `Σ_{ab} Z_{ab} W_{ab} = Tr(ZᵀW)`, which for real matrices *is* the HS pairing;
the complex case is exactly residual (b) and is not claimed (see MAJOR-1). (5) no symbolic
sorting used. (6) SHA ledger written LF, verified under that convention. (7) degeneracy
bookkeeping: `charpoly_Cmat` is *stated* at the coincidence points and I checked `x = 1/2`
explicitly. (8) `ε log ε` bookkeeping: not in scope for LEAN-3. (9) anchoring: see above.

---

## 3. Special audit (a) — WP-F

**`f_ge_sq` — re-derived independently, then checked as a Lean argument.** I derived the
two-level argument in sympy before reading Step 1b: with `g(s) = f(s) − s²`, `g(0) = 0` and
`g'(s) = log(1+s) − log(1−s) − 2s`; that function vanishes at 0 and has derivative
`1/(1+s) + 1/(1−s) − 2 = 2s²/(1−s²) ≥ 0` on `(0,1)` (gates R2a–c, all symbolic). The Lean
realization is sound:

* the shared private helper `nonneg_of_deriv_nonneg` uses `monotoneOn_of_deriv_nonneg` on
  `convex_Ico 0 1`; `interior_Ico` gives `Ioo 0 1`, so `hnn` is required exactly on the open
  interval while continuity is required on `[0,1)` — the `HasDerivAt` hypothesis is supplied
  on `(-1,1)`, which covers the two-sided requirement at the endpoint `0`;
* both `HasDerivAt` witnesses go through `HasDerivAt.congr_deriv`, so the *stated* `g'` must be
  proved equal to the derivative Lean actually computes. **The commissioned check that this
  side goal was non-trivial passes:** in `log_diff_ge_two_mul` the build reports the later
  `first`-alternatives as "never executed" (private-boundary.lean:248–250), i.e. the goal was
  closed by the genuine rewrite `neg_div`/`sub_neg_eq_add` turning `1/(1+y) − (−1/(1−y)) − 2`
  into the stated `1/(1+y) + 1/(1−y) − 2`; in `f_ge_sq` the product-rule derivative
  `log(1+y) + 1 − log(1−y) − 1 − 2y` likewise had to be normalized to `log(1+y) − log(1−y) − 2y`.
  A mis-stated `g'` could not have survived either goal.

**`Delta_lower_bound` is genuinely unconditional.** Elaborated signature (my own probe, not
the source comments):
`∀ {x : ℝ}, 0 < x → x < 1/2 → (1 - 2*x)^3 / (2*(1-x)*(2-3*x)) ≤ Support.Delta x`.
I also *applied* it out-of-tree at `x = 3/10` with two `norm_num` arguments and nothing else
(`r13_delta_lb_unconditional`, axioms clean). No `hsq`, no residual scalar hypothesis anywhere
in P14's analytic core.

**Trust census removal is append-only in substance.** The `hsq` row was deleted from the
census table, but its verbatim text is reproduced in a new dated
"Append-only census removals" subsection that states the removal is *by discharge*, names the
discharging theorem, and records that no other declaration consumed `hsq` (I confirmed by
grep: `hsq` appears nowhere else in the tree). The module's own append-only deviation record
carries the same entry plus the two rejected elementary routes. This satisfies rule 4 /
§7 append-only.

**SelfComplement vs paper `lem:x1`, symbol by symbol.**

| paper `lem:x1` | Lean | verdict |
|---|---|---|
| `Λ₁(X) = ½(Tr(X)𝟙 − Xᵀ)` | `LamOne X = (1/2) • (X.trace • 1 - Xᵀ)` | identical |
| Kraus `A_μ/√2`, 3-dim environment | `A0/A1/A2` = `ε_{μjk}` (I re-derived all 27 entries), `√2`'s multiplied into the single `½` | identical; the `½` is exactly `(1/√2)²` |
| `(Λ₁^{c,min}(X))_{μν} = ½Tr(A_μ X A_ν†)` | `LamCmin X μ ν = (1/2) * (A μ * X * (A ν)ᵀ).trace` | identical (`A_μ` real ⟹ `† = ᵀ`, and the module says so) |
| `= ½(δ_{μν}Tr X − (Xᵀ)_{μν})` | `lamCmin_apply` | identical |
| `= (Λ₁(X))_{μν}` | `lamCmin_eq_lamOne` | identical |
| "`J = id` … identically vanishing defect" | `defect_identity_zero` | identical |
| "Theorem `thm:zw` applies and gives `P(Λ₁) = Q(Λ₁) = 0`" | **not formalized** | correctly declared out of scope in the module's SCOPE block and README item 8 |

I re-derived the identity by hand as well: `Tr(A_μ X A_νᵀ) = −Tr(A_μ X A_ν) = −Σ_{jl}X_{jl}(δ_{jν}δ_{μl} − δ_{jl}δ_{μν}) = δ_{μν}Tr X − X_{νμ}`, using `Σ_i ε_{ijμ}ε_{iνl} = δ_{jν}δ_{μl} − δ_{jl}δ_{μν}`. Agrees.
The quantification is over **all** real `X` and all `μ,ν` — no sampling. Real-only is stated
and justified (real-linearity in the entries); the complex extension is explicitly not claimed.

**WP-F item 3.** `gB = (1−3x/2)²/b_ε` and `gE = x/(2(1−ε))` match `thm:necessity`'s two
displayed values symbol for symbol; `gE_lt_gB` is proved *from* `strict_violation_window`
(itself from `threshold_factorization`), i.e. wired, not duplicated, as commissioned. The
inequality direction is the right one: `g_E < g_B` is the failure of the domination
`g_E ≥ g_B` that `cRE`/`cBKM` would force. The module correctly states that `gB`/`gE` are
*definitions* — the collapse of the BKM form to them is not formalized.

---

## 4. Special audit (b) — WP-E

**The Weinstein–Aronszajn route is sound and the exponent is derived, not asserted.**
Mathlib's signature, printed by my own probe:

    Matrix.charpoly_mul_comm_of_le (A : Matrix m n R) (B : Matrix n m R) :
      Fintype.card n ≤ Fintype.card m →
        (A * B).charpoly = X ^ (Fintype.card m - Fintype.card n) * (B * A).charpoly

With `A = Fmat x : Matrix Idx (Fin 5 ⊕ Fin 3) ℝ` and `B = Gmat`, the exponent is
`Fintype.card Idx − Fintype.card (Fin 5 ⊕ Fin 3) = 27 − 8`, **produced by Mathlib and reduced
to 19 by `norm_num`**; the executor supplies only the `card` inequality. Confirmed: the `19` is
`27 − 8`.

**`G F_x` really follows from only the four small certificates.** I derived it myself first:
`(G F_x)_{(inl k),(inl k')} = Σ_I V₅_{Ik}(λ₅/12)W₅_{Ik'} = (λ₅/12)(V₅ᵀW₅)_{kk'} = λ₅δ`, and the
other three blocks likewise from `V₅ᵀV₃ = 0`, `V₃ᵀW₅ = 0`, `V₃ᵀV₃ = 16·𝟙`. Reading the Lean
proof afterwards: `Gmat_mul_Fmat` consists of exactly four `col_contract` applications, one per
certificate, and **uses nothing else** — no 27×27 product, no `decide` beyond WP-A's. The
orientation the executor flagged (`Gmat` carries `V₅`, `Fmat` carries `W₅`) is the one fixed by
`V₅ᵀW₅ = 12·𝟙`; swapping them would give `W₅ᵀV₅ = 12·𝟙` as well but `W₅ᵀW₅ ≠ 0`-type blocks
would break — and in any case my independent charpoly computation (below) does not go through
this factorization at all, so it is an unconditional cross-check.
`Fmat_mul_Gmat` uses `Cmat_eq` + `A5_eq`/`A3_eq` (the pre-existing `R5_factor`/`R3_factor`),
which is the forward direction and was already R12-reviewed.

**Cross-check of the charpoly identity at ≥ 3 rational `x`, by my own computation, not through
either factorization.** I computed `det(z𝟙 − C)` by sympy's Berkowitz algorithm on the full
27×27 matrix, for **two independent constructions** of `C` — (i) my Kraus-rebuilt defect Choi,
(ii) the Appendix A table — at `x = 3/10, 26/51, 1/2, 4/7`. All eight computations give
exactly `z¹⁹(z − λ₅(x))⁵(z − λ₃(x))³`:

    x = 3/10 : z^19 (15z + 56)^5 (135z + 56)^3 / 1868347265625
    x = 26/51: z^19 (663z − 50)^5 (221z − 200)^3 / 1382752534188934925523
    x = 1/2  : z^24 (9z − 8)^3 / 729
    x = 4/7  : z^19 (7z − 3)^5 (21z − 20)^3 / 155649627

**`charpoly_half` and the paper's claim at `x = 1/2`.** The polynomial `X²⁴(X − 8/9)³` matches
the paper's eigenvalue data at `x = 1/2` exactly (`λ₅ = 0`, `λ₃ = 8/9` with multiplicity 3).
It does **not**, by itself, give the paper's *rank* claim — see **MAJOR-2**.

**`x = 0` junk-convention caveat: stated.** Both the theorem docstring and the report say that
at `x = 0` both sides degenerate to `X²⁷` because `a/0 = 0`, that the point carries no
mathematical content, and that `charpoly_Cmat_of_ne_zero` is the loaded branch. I confirmed the
`x = 0` branch does no work elsewhere (grep: `Cmat_zero`, `lam5_zero`, `lam3_zero` are used
only inside `charpoly_Cmat`).

**Route substitution: sound, reported, and strictly stronger.** The frozen route (kernel basis
`K`, `S = [W₅|V₃|K]`, one expensive `S⁻¹S = 𝟙` product, similarity invariance) needed `x ≠ 0`;
the executed route needs nothing, avoids the expensive step entirely, and covers the
coincidence points. It was disclosed in the report, in the module docstring, and in the node
work record. `multiplicity_unique`'s docstring was correctly re-scoped rather than deleted.

---

## 5. Special audit (c) — WP-D (the heart)

**Chart logic.** `9xq² = 2(1−x)` is exactly `q = ±(1/3)√(2(1−x)/x)` (gate R9, four `x`);
`x = 2/(9q²+2)` is an equivalent form and the substitution is sound because `9q²+2 > 0`
always, so no division by zero and no case split is hidden. The hypothesis also *forces*
`0 < x ≤ 1` (for `x ≤ 0` or `x > 1` it has no real solution), so no junk `x` is silently
covered. The sign ambiguity in `q` is harmless: the defect depends on `q` only through
`d = 2βq = 3xq²`, which is even; and `(s,t) → (−s,t)` flips `q` and `β` together, so the
negative branch is the same physical lift written with a sign-flipped Kraus set.

**Nine entry identities: I verified all nine, not five.** Gate R5 checks
`Δ_J(τ)(Y) = Σ_{k=1}^{15} c_k(x)W_k(τ,Y)` entry by entry with `τ` and `Y` fully symbolic
(18 free symbols) and `x` symbolic, reducing modulo the chart ideal by `q² ↦ 2(1−x)/(9x)` and
requiring both the `q⁰` and the `q¹` remainder coefficients to vanish. All nine vanish
identically. My `c_k(x)` were transcribed from the paper's Appendix A "forced value" column,
independently of `DefectChoi.cco`; they agree.

**`choi_defect_eq_Cmat` quantifies over the chart correctly.** Elaborated signature:
`∀ {x q : ℝ}, 9*x*q^2 = 2*(1-x) → choiOf (Defect x q) = DefectChoi.Cmat x`. The hypothesis is
neither vacuous (§6 below) nor overly narrow (it admits both `q` branches and every
`x ∈ (0,1]`), and it is not overly *wide* either — it is exactly the condition under which
`β := 3xq/2` equals `s t`.

**`outB_eq`/`outE_eq` vs paper §7.** Verified symbolically (gates R8a–c) in `x, ε, θ, r, β`:
`Λ_x(ρ_ε + θX) = outB(α, b, u)` with `α = 1−x−(2−3x)ε` (which is `Tr`-complementary to
`b = x/2 + (1−3x/2)ε`, matching `thm:necessity`'s `b_ε` and `lem:holevo`'s `b`), and
`Λ^c_x(ρ_ε + θX) = outE(1−x, xε, e, −v)` with `e = (x/2)(1−ε)`, `v = θx/(2r)` — matching
`thm:necessity`'s displayed `Λ^c_x(ρ_ε) = diag(1−x, xε, e, e)` and `lem:holevo`'s
`Λ^c_x(X) = 0 ⊕ (−x/2)X` in the same frame order. **The "for every `β`" claim is correct and
for the stated reason:** `ρ_ε ± θX` is symmetric, so `a(ρ_ε ± θX) = 0` and the entire first
row/column of `eq:comp` collapses independently of `β` (my gate keeps `β` free). To read
`outE_eq` as a statement about the *complement* one composes it with `LamCK_eq` at
`β = s t`; both halves exist in the tree.

**The honest degradation is genuine — with one exception.** Residual (b) is open: no
`specB_charpoly`/`specE_charpoly` exists anywhere in the tree (grep), nothing was renamed to
look closed, `Trust.lean`'s 2026-08-01 status block reads "**STILL OPEN — unchanged**", the
README item 11 says so, and the report says so. **The exception is `Channel.lean`'s own scope
block, which says the opposite — MAJOR-1.**

---

## 6. Vacuity and satisfiability (§7.10.5)

Established *inside Lean*, out-of-tree (`r13_probe.log`, all four on the three standard
axioms):

* `r13_chart_inhabited_and_bridge_applies : ∀ x, 0 < x → x < 1 → ∃ q, 9xq² = 2(1−x) ∧
  choiOf (Defect x q) = Cmat x` — built from `exists_chart` + `chart_q` + the bridge, so
  **`exists_chart` is actually used to discharge the bridge's hypothesis**, for every physical
  `x`;
* `r13_bridge_at_two_thirds` — the bridge at the explicit rational chart point
  `(x,q) = (2/3, 1/3)` (note `q(1/2) = √2/3` is irrational, so `x = 1/2` is not a rational
  chart point);
* `r13_delta_lb_unconditional` — `Delta_lower_bound` applied with only `0 < x < 1/2`;
* `r13_gE_lt_gB_at` — `gE_lt_gB` instantiated at `(x,ε) = (3/10, 1/10)`, inside the window.

Hypothesis review of every new declaration: `f_ge_sq` `[0,1)`; `Delta_lower_bound` `(0,1/2)`;
`lamCmin_*`, `A_transpose`, `defect_identity_zero`, `Jdag_adjoint`, `charpoly_Cmat`,
`Gmat_mul_Fmat` — none; `epsC_lt_one`, `b_pos_of`, `gE_lt_gB` — inhabited window;
`charpoly_Cmat_of_ne_zero`, `Fmat_mul_Gmat` — `x ≠ 0`; `LamK_eq`, `LamCK_eq`, `LamK_tp` —
`s² = x/2`, `t² = 1−x`, inhabited over `ℝ` for `x ∈ [0,1]`; `chart_*`, `defect_eq`,
`choi_defect_eq_Cmat` — the chart, inhabited; `outB_eq`/`outE_eq` — `r ≠ 0` (vestigial, m10);
`word_choi` — `1 ≤ k ≤ 15`. **No contradictory, empty, or weakened-conclusion hypothesis
anywhere.** No conclusion was weakened relative to LEAN-2: `Delta_lower_bound` gained
strength, everything else is new.

---

## 7. Trust-boundary accuracy after the batch (§7.9 / §7.10.6)

What remains **outside** Lean after LEAN-3, enumerated by me from the sources:

1. **The three interface fields** `lsd_devetak`, `zw_hrsf_zero`, `q_pos_of_ic_pos` — the
   LSD/Devetak regularization, the Zhu–Wang signed-lift criterion + HRSF22 tensorization, and
   LSD achievability. *Displayed:* `Interface.lean`, `Trust.lean` "Interface", README items 1
   and 7. ✔
2. **`hach`** — the achievability reading of `IcScalar` (the §6 witness's coherent
   information). *Displayed:* Trust row, README item 11. ✔ (mislabelled "§4 entropy assembly",
   m6)
3. **`hdev`** — Devetak's formula for `P^{(1)}` applied to the one ensemble. *Displayed*, but
   its residual content is now stated as "Devetak's formula **alone**", which omits the
   state-validity of the ensemble members (m5).
4. **`hbridge`** (retained general bridge), **`hexp`** (general expansion lemma),
   **`hHolds`/`hFails`** (P6), **`h13`/`hS`** (the goal's P13 dependence). *Displayed.* ✔
5. **Residual (b)** — the §6 complex `specB`/`specE` identification, plus the "same charpoly ⟹
   same `vnEntropy`" passage for complex Hermitian matrices. *Displayed correctly in
   `Trust.lean`, README item 11 and the report; **displayed as CLOSED in `Channel.lean` —
   MAJOR-1**.*
6. **Complete positivity, the Stinespring dilation, "LamCK is *the* complementary channel",
   every capacity, every blocklength, and any coding theorem.** *Displayed:* README item 1
   (amended), Channel.lean honesty item 1, Trust's two "scope facts". ✔
7. **The paper's own proof of `eq:charpoly`** (SO(3) spin reduction, `eq:pencil`, the Gram
   factors `4/25`, `1/3`) — the Lean proof reaches the polynomial by an unrelated road.
   *Displayed:* README item 9, report item 24. ✔ (An important and correctly stated
   limitation: a defect in the manuscript's *narrative* would not be caught.)
8. **`lem:x1`'s capacity conclusion and the minimality of the Stinespring representation.**
   *Displayed:* SelfComplement SCOPE block, README item 8. ✔
9. **The §5 BKM collapse** (that `gB`/`gE` are the BKM forms). *Displayed:* order-boundary
   fidelity note, report item 21. ✔
10. **Residual (c)** is now CLOSED, but four documents still say it is open (m1).
11. **The transcription of `eq:Jintro` into `Jlift`** is a definition, not a checked fact
    (the Kraus set, by contrast, is pinned by `LamK_eq`/`LamCK_eq`). *Displayed* as
    "the signed lift `J` is checked here only as the linear map of `eq:Jintro`". ✔

Both §7.9 verbatim scope clauses are present in the README, and the "a green build is a run …
caps at NUMERICAL" clause is present. The tier declaration (T1+T2+minimal T3) is accurate.

---

## MAJOR findings

### MAJOR-1 — `Channel.lean`'s scope block presents residual (b) as CLOSED and names two theorems that do not exist

`WHGAP/Support/Channel.lean`, "Honesty note (§7.9 scope)", item 4 (lines 71–75):

> "The eigen-data glue for the §6 witness **is closed** only at **characteristic-polynomial**
> level (`specB_charpoly`, `specE_charpoly`): the passage 'same charpoly ⟹ same `vnEntropy`'
> is proved in `WHGAP.Support.Entropy` for **real symmetric** matrices only, and the §6 outputs
> here are genuinely **complex** Hermitian. See the scope paragraph on `specE_charpoly`."

`grep -rn "specB_charpoly\|specE_charpoly"` over the whole tree returns **only these two
docstring lines**. The declarations were never written — WP-D's item 3 did not land, exactly as
`Trust.lean` ("(b) **STILL OPEN — unchanged**"), README item 11 and the report all correctly
state. The referenced "scope paragraph on `specE_charpoly`" also does not exist.

Consequence: the §7.9 scope block of the very module the batch added is the one place where the
display is **stronger** than the content, and it over-claims precisely the item the batch
otherwise degraded honestly. A reader of `Channel.lean` alone concludes that the §6 complex
spectra are machine-checked at charpoly level. This is text left over from the un-landed item
(see also m3: the module still imports `Support.IcScalar` and uses nothing from it).

**Not a soundness defect** — nothing proved depends on it, and `choi_defect_eq_Cmat` /
`outB_eq` / `outE_eq` are unaffected.

**Prescribed repair:** rewrite item 4 to say that the §6 witness's complex `specB`/`specE`
identification was **not reached in Lean** (exact-sympy gates D9a–D9e of
`tools/whgap_lean3_wpd_check.py` only), that residual (b) of `Trust.lean` therefore stands, and
that *even at charpoly level* the further passage "same charpoly ⟹ same `vnEntropy`" would
remain missing for complex Hermitian matrices. Remove the two phantom declaration names and the
dangling cross-reference; drop the unused `IcScalar` import or state what it serves.

### MAJOR-2 — "`charpoly_half` … i.e. `rank C_{1/2} = 3`" is an invalid inference; no rank statement exists in Lean

The gloss appears in four places:

* `WHGAP/Support/DefectChoi.lean:57` — "it covers `x = 1/2` (`charpoly_half`: `X²⁴(X − 8/9)³`,
  **i.e. the paper's `rank C = 3`**)";
* `WHGAP/Support/DefectChoi.lean:808–810` (the `charpoly_half` docstring) — "the
  characteristic polynomial is `X²⁴(X − 8/9)³` — **i.e. `rank C_{1/2} = 3`**, which is exactly
  the paper's claim";
* `proof-dag/nodes/WHGAP.goal.md`, LEAN-3 WP-E work record — "**`charpoly_half` gives
  `X²⁴(X−8/9)³` at `x = 1/2`, the paper's rank `C = 3` at the physically decisive point**";
* `artifacts/whgap_lean3_20260801.md`, WP-E table — "the paper's `rank C_{1/2} = 3`".

A characteristic polynomial does **not** determine rank: `X²⁴(X − 8/9)³` is equally the
charpoly of a matrix with a nontrivial nilpotent part at `0`, whose rank can be anything from
3 to 26. Paper Theorem 3.3(2)'s rank claim therefore is **not** machine-checked by
`charpoly_half`, and `grep -rn "rank"` finds no rank statement anywhere in the development.

The mathematical fact is nevertheless true — I verified `rank C_{1/2} = 3` in my own
computation (gate R7d) — and it is *three lines* from lemmas already in the file: at `x = 1/2`,
`lam5 = 0`, so `Cmat_eq` gives `C = (λ₃/16)A₃`, and `A3_sq : A₃² = 16A₃` gives `C² = λ₃C`,
i.e. `C(C − λ₃) = 0`; a squarefree annihilating polynomial forces diagonalizability, hence
`rank = 3`. So this is an over-claim about **what the build checks**, not an error about the
matrix.

**Prescribed repair:** either (i) replace "i.e. `rank C = 3`" by "i.e. the eigenvalue multiset
`{0²⁴, (8/9)³}` — the paper's rank-3 claim then follows from diagonalizability, which is
*not* formalized", in all four places; or (ii) add the three-line `rank_Cmat_half` lemma via
`C(C − λ₃) = 0` and keep the wording. (i) is enough; (ii) is better.

---

## Minor findings

**m1 — four documents still say residual (c) is outside Lean, after WP-D closed it.**
(i) README item 3 — "What remains outside Lean is exactly two things … (i) that the explicit
matrices `outB`/`outE` really are `Λ_x(ρ_ε ± tX)` … established in exact sympy … **not** in
Lean" (contradicted by the same README's item 11); (ii) the same README's "What it does mean"
paragraph — "the identification of `outB`/`outE` with the channel outputs remains outside Lean
(item 3(i) above)"; (iii) `private-boundary.lean`'s module header, "What is left, and only what
is left: **(i) the identification step** … established outside Lean"; (iv) the
`Claim_of_devetak` docstring — "What remains outside Lean is (i) the identification of
`outB`/`outE` …". `Trust.lean`'s census table row has the same stale text but is explicitly
corrected by its own appended 2026-08-01 block, so it is the least misleading of the five.
All are **under**-claims (the mirror image of MAJOR-1) and none can mislead anyone into
trusting something unproved — but they make the module's own header contradict the section
WP-D added 440 lines below it.

**m2 — node `lean:` metadata not refreshed for LEAN-3 on the nodes whose Lean content
changed.** `WHGAP.private-boundary`'s `lean.rel` still lists *"`Delta_lower_bound` additionally
rel `hsq` — a FORMALIZATION gap only"* (discharged by WP-F) and the `outB`/`outE`
identification as "outside Lean" (closed by WP-D); `WHGAP.order-boundary`'s block still points
at `logs_whgap_lean_20260730/`, is `synced: 2026-07-30`, and does not mention the new
`gB`/`gE`/`gE_lt_gB` layer; `WHGAP.goal`, `WHGAP.private-boundary`,
`WHGAP.signed-lift-extension` and `WHGAP.no-ascent-hierarchy` all still carry
`build: artifacts/logs_whgap_lean2_20260731/` and `synced: 2026-07-31`. Under the
single-writer deviation this is decision-layer work, not the executors'; `lean_dag_check`
cannot catch it (its `rel`-text checks are textually undecidable, M7-F3). Rule 8c wants the
outcome recorded on **its** node: LEAN-3 is recorded only on `WHGAP.goal`.

**m3 — dead import.** `WHGAP/Support/Channel.lean:2` imports `WHGAP.Support.IcScalar` and uses
no declaration from it (the module references `IcScalar` only in prose). It is a leftover of
the un-landed item 3, same origin as MAJOR-1.

**m4 — README numbering.** "What a green build here does NOT establish" runs 1–9, then 11, 12:
item 10 is missing. WP-D's item was appended as 11 without renumbering.

**m5 — `hdev`'s residual content is under-described.** `Trust.lean`'s 2026-08-01 block says
"what `hdev` still carries is Devetak's formula **alone**". It also carries the *validity of
the ensemble*: that `ρ_ε ± tX` are states (PSD, trace one) and that `|t| ≤ √2 ε` as `eq:ens`
requires. Nothing in Lean checks positivity of the inputs (`outB_trace`/`outE_trace` check
trace-one of the two *averages* only), and the constraint `|t| ≤ √2 ε` is nowhere represented.
The obligation is discharged in the manuscript and is true at the frozen point — my gate R8d
verifies `ρ_ε ± tX ⪰ 0` at `ε = t = ε_c/2` for three `x` — but the enumeration should name it
rather than say "alone". (Pre-existing in kind; LEAN-3 is where the enumeration became
complete-sounding.)

**m6 — "§4 entropy assembly (`hach`)".** README item 11 and the report call `hach` "the §4
entropy assembly". `hach` is the achievability reading of the **§6** `IcScalar` (P9/P3); the
paper's **§4** assembly is inside the `zw_hrsf_zero` interface (P4). The commission text
carries the same conflation, so this is inherited, not invented.

**m7 — work-record hygiene on `WHGAP.goal.md`.** Two near-duplicate WP-D entries dated
2026-08-01 ("LANDED (partially) …" and "LANDED (3 of 4 items …)") describe the same landing;
and the node now has two `## Work record` sections and two `## Adversarial reviews` sections
(the second pair pre-dates LEAN-3). §3 of the structure protocol wants one of each.

**m8 — the SHA ledger pins a live co-edited file.** `SHA256SUMS.txt`'s last row for
`channel-capacity/werner-holevo-gap/proof-dag/nodes/WHGAP.goal.md` no longer matches the file
(the decision layer appended to the node after the executor hashed it); 25 of 26 last-rows
verify. Hashing a node file in a *run* ledger is self-defeating — either drop that row or
re-hash at closeout.

**m9 — new linter noise.** The batch introduces ~20 build warnings: unused `simp` arguments and
unused auto-included section variables throughout `Channel.lean`, `'ring' tactic does nothing`
and `this tactic is never executed` at `SelfComplement.lean:116`, and never-executed
`first`-alternatives in `private-boundary.lean:248–250, 285–288`. All cosmetic; the last of
these is in fact *useful* evidence (it is how I confirmed the `congr_deriv` side goals were
non-trivial), but the rest should be cleaned.

**m10 — vestigial hypothesis.** `outB_eq`/`outE_eq` carry `hr0 : r ≠ 0`, which is not a genuine
side condition: under Lean's junk convention `Xwit 0 = 0` and `u x θ 0 = v x θ 0 = 0`, so the
identity still holds. I machine-checked the `r = 0` instance out-of-tree (`r13_probe.log`,
second probe, exit 0). Harmless, but it advertises a non-degeneracy requirement that does not
exist.

---

## What this review did NOT establish

* I did not re-verify the LEAN-1 / LEAN-2 content beyond what LEAN-3 touches; R11 and R12 are
  the reviews of record for those, and I relied on them only for provenance, not for any
  statement I license here (7d).
* I did not verify the executors' own scripts (`whgap_lean3_wpd_check.py`,
  `whgap_lean3_wpe_charpoly.py`) — I never read them; my agreement with their conclusions
  comes from an independent construction, which corroborates the *claims*, not their scripts.
* Per 7f: gates R1–R3, R4b, R5, R8 verify **formulas** (symbolic identities); gates R4, R6, R7,
  R9 verify **values** at exact rational points. The 729-entry Choi bridge is verified as
  values at four `x` plus the nine underlying entry identities as a formula — together these
  are stronger than either alone, but the composition `choiOf ∘ Defect = Cmat` as a formula in
  `x` is checked in Lean, not by me.
* Nothing here bears on complete positivity, the Zhu–Wang criterion, any capacity, the P13
  strip, or the OPEN status of `WHGAP.goal`.

---

## Provenance

* Reviewer script: `tools/whgap_r13_defect_check.py` (exact sympy, no floats), 37/37 gates PASS.
* Logs (all under `artifacts/logs_whgap_lean3_20260801/`, prefix `r13_`):
  `r13_build.log` (own clean rebuild, exit 0), `r13_print_axioms.txt` (203 declarations),
  `r13_forbidden_scan.txt`, `r13_gates.txt` (freeze / `lean_dag_check` / `proof_dag_check` /
  `literature_check`), `r13_defect_check.log`, `r13_probe.log` (elaborated signatures +
  satisfiability probes).
* Interpreter: `C:<home>/cpython3119/python.exe` (sympy 1.13.1). Toolchain
  `leanprover/lean4:v4.31.0`, Mathlib `v4.31.0`.
* Single-writer deviation observed: I wrote only this report, `tools/whgap_r13_*.py`, and
  `r13_`-prefixed logs; SHA ledger rows appended additively. No node file, `NODE_INDEX.md`, or
  DAG document was edited by me.

