# WHGAP R8 — fresh independent review of the P12-A private-boundary note

Reviewer: fresh Opus instance, 2026-07-30. Reviewed artifact:
`channel-capacity/werner-holevo-gap/notes/WHGAP_P12A_PRIVATE_BOUNDARY_20260730.md`.
Commission: `channel-capacity/werner-holevo-gap/notes/WHGAP_COMMISSION_P12A_20260730.md` (§R8).
Node: `WHGAP.restricted-order` (P12). Immutable once written.

**VERDICT: FINDINGS — 3 MAJOR, 9 minor.** Licensing menu option (A) is *not* taken, for the
three reasons in §4. The mathematical core (Theorem 3.5 on the open family) is independently
confirmed at every step and is licensable in the restated form given in §5.

---

## 0. PRE-ACTION REPORT (`research/PRETASK_RELOAD_PROMPT.md`)

Files read from disk, in order, before any mathematics: `research/DAG_PROTOCOL.md` (whole);
`research/RESEARCH_STRUCTURE_PROTOCOL.md`; `channel-capacity/werner-holevo-gap/README.md`;
`channel-capacity/werner-holevo-gap/proof-dag/NODE_INDEX.md`;
`proof-dag/nodes/WHGAP.restricted-order.md` (target) and
`proof-dag/nodes/WHGAP.zero-capacity-application.md` (P4, the frozen input);
`notes/WHGAP_REVIEW_COMMISSION_R5_20260729.md` §1–§3 (frozen conventions, standing failure
modes, rule-7 embeds); `notes/WHGAP_DESIGN_MEMO_P12_20260730.md`; the reviewed note.

- **Target node and status as read from disk:** `WHGAP.restricted-order` (P12), `kind: LEAF`,
  `role: proof`, **status `OPEN`**, disposition null, parent `WHGAP.goal`; related
  `WHGAP.order-boundary` (PROVED), `WHGAP.relaxed-lift` (CONJECTURED), `WHGAP.order-converse`
  (OPEN), `WHGAP.more-capable-route` (OPEN/PARKED).
- **My ROLE: reviewer.** Independence statement: I did not author the reviewed note, any of the
  `whgap_p12a_*` scripts, the design memo, the commission, or any prior WHGAP work, and I was
  given no desired outcome — the menu was presented to me as alternatives.
- **Highest status my evidence could license (§2 ladder):** a completed rule-7 review by a fresh
  instance opens the **PROVED** tier for the reviewed claims that pass; the *decision layer* (not
  I) writes any status, citing this report. I write no node/index/DAG edit (single-writer
  deviation, binding).
- **Gates and deliverables, one line each:** own-route re-derivation of the closed forms (own
  Kraus/complement assembly, own entropies); line-by-line audit of S1a's limit argument and
  S1b's explicit threshold; own-script reproduction of G-cal and G-ind at ≥ 2 points each;
  audit of the P⁽¹⁾-superadditivity step and the Devetak-formula citation; audit of S2 and of
  the S3 no-go map for over-claim, especially Q-leakage on [2/5,1/2) and the exact scope of the
  no-go; report at `artifacts/whgap_r8_review_20260730.md` with exactly one menu option or
  FINDINGS.
- **Conflicts between commission text and disk protocols:** **one, and it is load-bearing.** The
  commission's frozen-input list grants "P2/P4 (P = Q = 0 on **[1/2,1]**)". The disk
  (`WHGAP.zero-capacity-application.md`, header `status: PROVED`, Claim block lines 21–27 and
  Current status lines 39–46) records **PROVED on [1/2,1)** and the **closed-interval corollary
  at CERTIFIED\*** with a cite-only RK24 endpoint. Per the reload prompt the disk wins and I
  report rather than resolve: see MAJOR 2. No other conflict on rules.

---

## 1. What I did (anchoring ban, 7c)

I derived everything below from the frozen conventions of R5 §1 **before** comparing to the
note's or the memo's values. My Kraus set is built from a Levi-Civita tensor I construct in the
script; the channel is `sum_a K_a Y K_a^dag`; the complement is the padded 4×4
`[Tr(K_a Y K_b^dag)]_{ab}`; output spectra come from sympy/mpmath eigenvalue routines, never from
a displayed formula; Holevo quantities are assembled as `S(avg) − mean S(components)` from those
spectra. The reviewed values are read in only in a final `NOTE-COMPARE` block that runs last
(`tools/whgap_r8_symbolic.py`), and the G-ind path (`delta_direct` in
`tools/whgap_r8_numgates.py`) never touches `b, u, e, v, f` at all.

**Notational coincidence disclosure (7c):** my independently derived quantities coincide
notationally with the note's `b, u, e, v` because both are forced by the frozen conventions —
`b` is literally the (1,1) entry of `Λ_x(ρ_ε)` and `u, v` the off-diagonal entries of the two
degenerate blocks. The coincidence is structural, not evidence of independence by itself; the
independence claim rests on the `delta_direct` route and the matrix-power Rényi route, which
share no code path with the note.

Five scripts, **60 gates, 0 unresolved failures**; seven gate failures occurred and were all
resolved (five sympy log-combination artifacts, two defects in *my own* code) — logged
append-only in §6.

| script | log |
|---|---|
| `tools/whgap_r8_symbolic.py` | `artifacts/logs_whgap_r8_20260730/r8_symbolic.log`, `r8_symbolic.json` |
| `tools/whgap_r8_symbolic2.py` | `artifacts/logs_whgap_r8_20260730/r8_symbolic2.log` |
| `tools/whgap_r8_numgates.py` | `artifacts/logs_whgap_r8_20260730/r8_numgates.log`, `r8_numgates.json` |
| `tools/whgap_r8_s2s3.py` | `artifacts/logs_whgap_r8_20260730/r8_s2s3.log`, `r8_s2s3.json` |
| `tools/whgap_r8_b2probe.py` | `artifacts/logs_whgap_r8_20260730/r8_b2probe.log`, `r8_b2probe.json` |
| `tools/whgap_r8_closeout.py` | `artifacts/logs_whgap_r8_20260730/r8_closeout.log` |
| `tools/whgap_r8_lit.py` | `artifacts/logs_whgap_r8_20260730/r8_lit.log`, `r8_lit_zw.log` |

Interpreter `C:<home>/cpython3119/python.exe` throughout; hashes in
`artifacts/logs_whgap_r8_20260730/SHA256SUMS_R8.txt` (LF, `sha256sum -c` verified).
The executor's own `SHA256SUMS_E-P12A.txt` verifies **15/15 OK** from the repo root.

### Type audit (7a)

| object | type | note |
|---|---|---|
| `Λ_x` | superoperator on 3×3 complex matrices | `Λ_x(Y) = (1−x)Y + (x/2)(Tr(Y)1 − Yᵀ)` |
| `K_0` | 3×3, `√(1−x)·1` | real |
| `K_{μ+1}` | 3×3, `√(x/2)·A_μ`, `(A_μ)_{jk} = ε_{μjk}` | real, antisymmetric |
| `Λ_x^c` | 3×3 → **4×4** (padded) | `Λ^c(Y)_{ab} = Tr(K_a Y K_b†)`; `K† = Kᵀ` justified only after checking `A_μ` integer and `√(1−x), √(x/2)` real on `x ∈ (0,1)` |
| `ρ_ε, X` | 3×3 Hermitian; `X` real symmetric traceless, `‖X‖_HS = 1` | gate T3 |
| `χ_B, χ_E, Δ` | scalars in **nats** | gates H1*/H2* |
| ensemble `E(ε,t)` | two-point c-q object, weights ½/½ | average `ρ̄ = ρ_ε` |
| `w_B, w_E` (§7 reviewer addendum) | scalars, `Tr[Π_ker(·) Λ^{(c)}(φ)]` | 3×3 vs 4×4 kernels distinguished |

Kraus completeness `Σ_a K_aᵀK_a = 1` verified symbolically (T1); the Kraus channel equals the
frozen superoperator form on a **generic symbolic 3×3** (T2) — not on a sample.

---

## 2. Claim-by-claim verdicts

Every entry states VALUE vs FORMULA (7f) and the multiplicity of the check (7b).

### 2.1 S1a — Theorem 2.1 (less noisy ⟺ RE domination). **PASS (FORMULA, analytic).**

I re-derived both directions before reading the note's proof.

- (⟸) is the identity `χ({p_u,τ_u}) = Σ_u p_u D(τ_u‖τ̄)` plus termwise domination; admissibility
  `supp ρ_u ⊆ supp ρ̄` follows from `ρ̄ ⪰ p_u ρ_u`. Correct.
- (⟹) the three ingredients are each sound and each is genuinely needed:
  - **(i)** `σ_p ⪰ (1−p)σ` and operator monotonicity of `log` give
    `D(ω‖σ_p) ≤ D(ω‖σ) − log(1−p)` (2.2). The step is legitimate **because** admissibility
    forces `supp σ_p = supp σ` and `supp Φ(σ_p) = supp Φ(σ)`; the note supplies exactly that
    (`supp ρ ⊆ supp σ ⟹ σ ⪰ cρ ⟹ Φ(σ) ⪰ cΦ(ρ)`). Checked.
  - **(ii)** joint lower semicontinuity of Umegaki relative entropy. Standard; correctly used
    only on the M-side to bound the liminf from below.
  - **(iii)** `D(τ‖τ+pΔ) = O(p²)`. The note's justification is telegraphic
    ("the derivative of log at a point commuting with itself is the ordinary difference
    quotient") but the integral-representation statement it then gives is the correct argument:
    `Dlog_τ(Δ) = ∫_0^∞ (s+τ)^{-1}Δ(s+τ)^{-1} ds`, hence
    `d/dp Tr[τ log(τ+pΔ)]|_0 = Tr[Δ ∫_0^∞ τ(s+τ)^{-2}ds] = Tr[Δ] = 0` (the integral is the
    support projector of `τ`, and `Tr Δ = 0` on that support). I verified this derivation
    independently. Real-analyticity near `p = 0` holds since `τ + pΔ ≻ 0` on `supp τ`.
  - The limsup/liminf bookkeeping is correct: `limsup LHS ≤ D(N(ρ)‖N(σ))` and
    `liminf RHS ≥ D(M(ρ)‖M(σ))`, and `LHS_p ≥ RHS_p` for every `p` closes it.
- **Literature check reproduced independently.** HRSF22 (local PDF
  `hirche-rouze-stilckfranca-2022-contraction-partial-orders/arxiv_2011.05949.pdf`): my own
  extraction finds on **p. 8** the equivalence (2.10)⟺(2.11) in exactly the note's form, and on
  **p. 9** the sentence the note quotes. The note's claim "this is literature, not new" is
  correct, and its independence disclosure is appropriate. Also confirmed from the same PDF:
  **Prop. 3.3** (p. 12) `N ⪰^c_{m.c.} N^c ⟺ N ⪰_{m.c.} N^c` — cited correctly — and eq. **(3.4)**
  `I(A⟩B) = I(X:B) − I(X:E)` (see minor m5).

*Scope:* the note correctly notes Theorem 2.1 is used only interpretively (§7) and that
Theorem 3.5 does not depend on it. I confirm the dependency structure: §3 is self-contained.

### 2.2 S1b — closed forms. **PASS (FORMULA, symbolic in (x,ε,t); plus VALUE at 11 points).**

Derived by my own route:

- `Λ(X) = (1−3x/2)X`; `Λ(ρ_ε) = diag(1−2b, b, b)` with `b = x/2 + (1−3x/2)ε` — gate B1, symbolic.
- `[Λ(ρ_ε), Λ(X)] = 0` — gate B2, symbolic.
- `spec Λ(ρ_ε ± tX) = {1−2b, b±u}`, `u = t(1−3x/2)/√2` — gates B3/B4, symbolic **eigenvalue
  computation** (not a substitution check).
- On the E side I derived `Tr(A_μ X A_νᵀ) = δ_{μν}Tr X − X_{νμ}` by hand and confirmed
  symbolically: the **a-block vanishes** (`Tr(X A_μ) = 0` for `X` symmetric, `A_μ`
  antisymmetric) and `Λ^c(X) = 0 ⊕ (−x/2)X` — gate E2. `Λ^c(ρ_ε) = diag(1−x, xε, e, e)`,
  `e = (x/2)(1−ε)` — gate E1. `spec Λ^c(ρ_ε ± tX) = {1−x, xε, e±v}`, `v = tx/(2√2)` — gate E4.
- `χ_B = b f(u/b)`, `χ_E = e f(v/e)`: the α and (1−x, xε) eigenvalues cancel identically. Closed
  symbolically with positive free symbols (`h(w,y) = w f(y/w)`; gates H0*/H1*/H2*) and
  numerically at **5 (x,ε,t)** to residual `< 1.5e-61` at 60 dps.
- `g_B − g_E = (1−x)[(1−2x) − (1−3x/2)ε]/(b(1−ε))`, sign change exactly at
  `ε_c(x) = 2(1−2x)/(2−3x)` — gates G3/G4, symbolic. Confirms the paper §5 / R5b input.

The note's `b, u, e, v` agree with mine identically (gates NC-b/u/e/v). **The memo's values are
correct; the note's re-derivation is faithful.**

**Memo sign defect independently confirmed.** Gate G5 (symbolic limit):
`lim_{ε→0}(u²/b − v²/e) = t²(1−x)(1−2x)/x`. The memo's `(2x−1)` is wrong; the note's §3.6
correction is right, and my check confirms the diagnosis that the memo transcribed the paper's
oppositely oriented display. Correctly reported rather than silently repaired.

### 2.3 Theorem 3.2 (explicit threshold). **PASS (FORMULA), audited step by step.**

I re-derived each step. All five hold, with the side conditions actually available:

1. `χ_B ≥ u²/b` needs `|u/b| ≤ 1`, supplied by positivity of `Λ(ρ_ε ± tX)`. ✔
2. `s_E² = ε²/(2(1−ε)²) ≤ 1/2` needs `ε ≤ 1/2`; and `ε ≤ ε_c(x)/2 = (1−2x)/(2−3x) ≤ 1/2 ⟺ x ≥ 0`.
   ✔ Then `1 − s_E² ≥ 1/2` and `f(s) ≤ s² + s⁴/(6(1−s²))` gives
   `χ_E ≤ v²/e + ε⁴x/(24(1−ε)³)`; I verified `v⁴/e³ = t⁴x/(8(1−ε)³)`. ✔
3. `g_B − g_E ≥ 1−2x`: numerator bracket `≥ (1−2x)/2` from `ε ≤ ε_c/2`, denominator
   `b(1−ε) ≤ (1−x)/2` from `b ≤ (1−x)/2`. ✔
4. `ε < 2(1−2x)` from `2−3x > 1/2` on `(0,1/2)`; `(1−ε)³ ≥ 1/8`. ✔
5. bracket `1/2 − 4x(1−2x)/3 ≥ 1/3` since `max_{(0,1/2)} 4x(1−2x) = 1/2` at `x = 1/4`. ✔

Series facts (3.1) verified: `f(s) = Σ_{k≥1} s^{2k}/(k(2k−1))` to `s¹⁰` (gate S1) and
`f'(s) = log((1+s)/(1−s))` on `0 < s < 1` (gate S2*); `k(2k−1) ≥ 6` for `k ≥ 2` gives the upper
bracket. **The threshold argument is correct as written.**

### 2.4 §3.4b — Lemma 3.2b and the exact value (3.5). **PASS (FORMULA + VALUE at 5 x).**

This is the note's own strengthening over the memo and it is the sharpest thing in the note.
Verified symbolically: `s_B = s_E ⟺ (1−2x) = (2−3x)ε` (gate K0, by solving, not by substitution);
at `ε = t = ε_c/2`, `b = (1−x)/2` (K1), `b−e = (1−2x)(1−x)/(2−3x)` (K2),
`s* = (1−2x)/(√2(1−x))` on **both** sides (K3), hence

> **Δ(x, ε_c/2, ε_c/2) = [(1−2x)(1−x)/(2−3x)] · f((1−2x)/(√2(1−x))) > 0 on (0,1/2)**,

confirmed at 60 dps at `x ∈ {2/5, 21/50, 9/20, 12/25, 499/1000}` with residual `< 8e-62`
(gate K4*), and `(3.6) = (1−2x)³/(2(1−x)(2−3x))` verified as `(b−e)s*²` (K5) and as `≥ (3.4)` (K6).
Positivity needs only `b > e = ε(1−x) > 0` and `f > 0`; **no series bound at all.** Correct, and
the note is right that Theorem 3.2 must nevertheless be retained, because S3 row (d) needs
arbitrarily small ε where `s_B ≠ s_E`.

### 2.5 §3.5 — superadditivity and the Devetak citation. **PASS (FORMULA; citation verified).**

Lemma 3.3's proof is correct: the `n`-fold product ensemble has average `(N(ρ̄))^{⊗n}`, both
entropy terms split by additivity, so `χ = nχ` on each side; `(N^{⊗n})^c = (N^c)^{⊗n}` up to a
tensor-factor permutation unitary of the environment, which no entropy sees. Hence
`P⁽¹⁾(N^{⊗n}) ≥ n P⁽¹⁾(N)`.

Citation audited against the local PDF myself (`zhu-wang-2026-quantum-incapacity/
arxiv_2607.24693.pdf`, p. 4): ZW **(2.6)** is Devetak's
`P⁽¹⁾(N) := sup_{ensembles}[I(U;B)_ω − I(U;E)_ω]` and **(2.7)** is
`P(N) = lim_n (1/n)P⁽¹⁾(N^{⊗n}) = sup_{n≥1} (1/n)P⁽¹⁾(N^{⊗n})`, with the text "the existence of
the limit follows from superadditivity and finite dimensionality" and the attribution
"[Dev05]". **The note's citation is accurate and the `sup` form makes `P ≥ P⁽¹⁾` immediate**;
Lemma 3.3 is the independent proof of what the `sup` form presupposes, so the step is not
circular.

### 2.6 S0 literature. **PASS — reproduced independently.**

(1) confirmed above. (2) my own sweep: `private` occurs in **RK24** only on pp. 22–24 and in
**RK25** only on p. 14, in every case inside a bibliography entry title — no private-capacity
statement about `Λ_x` in either body. ZW treats **only `x = 1/2`** ("We consider the `x = 1/2`
member of the noisy Werner–Holevo family", p. 2). **The note's novelty claim relative to the
local library is correct.** (3) HHHO context paragraph is properly fenced as context.

### 2.7 G-cal (HARD). **PASS — reproduced with my own script, 600 pairs per x.**

Fully independent matrix route (`delta_direct`): 30 ε-values × 20 t-values, `t ∈ (0, √2 ε]`.

| x | pairs | my max Δ | argmax (ε,t) | note's max Δ |
|---|---|---|---|---|
| 11/20 | 600 | **−1.100910527e-07** | (0.0161290, 0.00114049) | −3.994963487e-08 |
| 3/5 | 600 | **−1.767449183e-07** | (0.0161290, 0.00114049) | −6.436745879e-08 |

Δ ≤ 0 everywhere on my grid at both x (grids differ, so the maxima differ; both are negative and
both are attained at the smallest ε on the grid, consistent with `Δ → 0⁻` as `ε → 0`). Also
Δ ≤ 0 at `x ∈ {1/2, 4/5, 19/20}` on 9 further admissible `(ε,t)`.

**Proposition 5.1 audited and confirmed.** `∂h/∂w = log(1 − y²/w²) ≤ 0` and
`∂h/∂y = log((w+y)/(w−y)) ≥ 0` (closed at 50 dps by finite differences at 4 points after
sympy declined the log combination — see §6 R-1); `b − e = ε(1−x) ≥ 0` and
`v² − u² = (t²/2)(1−x)(2x−1) ≥ 0 ⟺ x ≥ 1/2`, both symbolic (M3, M4). I additionally verified the
**full inequality chain** `|u| ≤ v ≤ e ≤ b` at 12 `(x,ε,t)` with `x ≥ 1/2` (`v ≤ e ⟺ ε ≤ 1/2`,
which admissibility supplies), so
`Δ = h(b,|u|) − h(e,|u|) + h(e,|u|) − h(e,v) ≤ 0`. **The symbolic G-cal on all of [1/2,1] is
sound and is stronger than the commission required.** *Value-vs-formula:* Prop. 5.1 is FORMULA;
the 600-pair scans are VALUE at two x.

### 2.8 G-ind. **PASS — 6 triples, ≥ 55 digits, my own construction.**

| (x, ε, t) | my Δ (independent matrices → eigenvalues → entropies) | agreement w/ closed form | note's Δ |
|---|---|---|---|
| (9/20, 1/20, 1/25) | 1.6084218405614e-04 | 56.9 digits | 1.60842184056e-04 |
| (1/5, 3/10, 1/5) | 2.9296494190842e-02 | 59.4 digits | 2.92964941908e-02 |
| (49/100, 1/200, 1/300) | 2.1588752626246e-07 | 55.2 digits | 2.15887526262e-07 |
| (11/20, 1/10, 1/8) | −1.5726479332833e-03 | 58.1 digits | −1.57264793328e-03 |
| (12/25, 1/50, 1/60) | 1.0322775524547e-05 | 55.9 digits | 1.03227755245e-05 |
| (2/5, 1/4, 1/4) | 8.4122613705773e-03 | 59.7 digits | 8.41226137058e-03 (§4) |

**Every digit the note prints in §5.2 and §4 is reproduced.**

### 2.9 S1c exact certificates. **PASS — reproduced in ℚ, no `nsimplify` anywhere.**

All six rows reproduce exactly, including the `s_B² = s_E²` coincidence and the exact `LB`:

| x | ε = t | s_B² = s_E² | LB (exact) | conditions |
|---|---|---|---|---|
| 2/5 | 1/4 | 1/18 | 53/6480 | all OK |
| 21/50 | 8/37 | 32/841 | 105856/22559825 | all OK |
| 9/20 | 2/13 | 2/121 | 239/173030 | all OK |
| 12/25 | 1/14 | 1/338 | 6/54925 | all OK |
| 49/100 | 2/53 | 2/2601 | 15557/1054575450 | all OK |
| 499/1000 | 2/503 | 2/251001 | 1505507/94879507504500 | all OK |

Checked exactly: `LB ∈ ℚ`, `LB > 0`, `1 − 2ε ≥ 0`, `s_B² ≤ 1`, `s_E² ≤ 1/2`, `ε²(1−2x)/3 ≤ LB`,
and `LB ≤ Δ` at 60 dps. The note's claim that positivity rests on exact rational arithmetic plus
the *proved* series bounds (3.1) is accurate.

### 2.10 G-cont / S1d. **PASS (VALUE).**

My own optimizer over an `ε_c`-scaled box: Δ_max = 2.4134e-01, 1.99926e-02, 3.32410e-03,
2.60509e-04, 3.50664e-05, 3.76068e-08, 3.78777e-11 at `x = 1/5, 2/5, 9/20, 12/25, 49/100,
499/1000, 4999/10000`; ratios to `(1−2x)³` = 1.117, 2.499, 3.324, 4.070, 4.383, 4.701, 4.735 —
matching the note's table to grid resolution and confirming `Δ_max → 0` with the `4.74(1−2x)³`
scaling. I confirm the note's asymptotic statements: the exact witness (3.5) behaves as
`2(1−2x)³` (factor 2.37 below optimal) and (3.4) as `(4/3)(1−2x)³`.

### 2.11 S2 — the purity-knob hierarchy. **PASS (Props 6.1/6.2 FORMULA; separation VALUE at 3 x).**

- **Prop. 6.1** re-derived independently (Stinespring `V|ψ⟩ = Σ_a |a⟩_E ⊗ K_a|ψ⟩_B`; pure input ⟹
  `V|ψ⟩` pure on BE ⟹ marginals isospectral) and verified numerically: `χ_B − χ_E = I_c(ρ̄)` at
  **18 random two-point pure ensembles** (residual `≤ 1.7e-40`) and `S(Λψ) = S(Λ^cψ)` at
  **36 pure states** (residual `≤ 2.1e-40`), at 40 dps with complex states.
- `sup` over pure ensembles `= max_ρ I_c(ρ) = Q⁽¹⁾`: correct, both inclusions.
- **Prop. 6.2** is ZW (2.6) verbatim (verified, §2.5). **Cor. 6.3** follows.
- **Separation reproduced:** at `x = 9/20` my 6 random pure ensembles give `χ_B − χ_E ∈
  [−0.0668, −0.0406]`, at `12/25` `[−0.0905, −0.0666]`, both `< 0`, while the S1b mixed ensemble
  gives `+1.402480e-03` and `+1.099444e-04`. Control `x = 1/5`: pure ensembles `[+0.0590, +0.2281]`,
  all positive. **The predicted regime separation is confirmed.**
- **No Q-leakage:** the note's §6 scope note explicitly states the pure-ensemble table is not a
  claim that `Q⁽¹⁾ ≤ 0` on the strip. I checked §6 and §8 line by line — the discipline holds.

### 2.12 S3 — the no-go map.

Verified **independently and confirmed**:

- **Row (d)** — the load-bearing row. Trace distance of `ρ_ε ± tX` to `|0⟩⟨0|` is exactly `2ε`
  (eigenvalues of the difference are `−2ε, ε ± t/√2`; trace norm `4ε` when `|t| ≤ √2 ε`).
  Δ > 0 at `ε/ε_c ∈ {1/2, 1/10, 1/1000, 1/10⁶}` and `x ∈ {9/20, 49/100}` — 8/8, with distances
  matching `2ε` to 30 digits. **Row (d) as stated in the table is correct**, and its hypothesis
  ("*all* pairs within trace distance δ of a pure state") is the right one — see MAJOR 1.
- **Row (a6), Prop. 7.1** — I re-derived `D_α(Λ(ρ_ε+tX)‖Λ(ρ_ε)) = (α−1)^{-1}log(1 + b F_α(u/b))`
  using `α_eig + 2b = 1`, and the E-side analogue using `(1−x) + xε + 2e = 1`; both correct, as
  is `F_α(s) = α(α−1)s² + O(s⁴)`. I then recomputed `D_α` **from matrix powers of the actual
  outputs** (own eigendecomposition of each matrix separately; no spectrum formula, no assumed
  eigenvalue pairing) at 40 cases: domination **fails** at every `α ∈ {1.25,1.5,2,3,5}` and both
  t-scales for `x ∈ {1/5, 9/20, 49/100}`, and **holds** at the control `x = 11/20`. This is a
  stronger check than the note's (see minor m3).
- **Row (c)** — I verified the underlying identity myself: for a purification `ψ_RA`,
  `I(R;B) − I(R;E) = 2 I_c(ρ_A)` at **9 random purifications across 3 x**, residual `≤ 1.3e-40`
  (own 3⊗3⊗4 tripartite construction, own marginals). Hence class (c) domination ⟺ `Q⁽¹⁾ = 0`.
  The HRSF22 Prop. 3.3 citation is accurate (§2.1).
- **Row (b2)** — see MAJOR 3, minors m1/m2, and §3 below. The reported violations reproduce.
- Rows a1–a4, b1: correct, and each is an immediate consequence of Theorem 3.5 plus the
  containment of the witness pair (I checked each containment argument).

---

## 3. Reviewer addendum: what row (b2) actually is (new, and it corroborates the note)

The note leaves 𝒫_b2 = `{(P_ψ, σ)}` as an unstructured numerical question. I derived its
first-order content and verified it:

> **Lemma (reviewer).** For `σ_s = (1−s)P_χ + sφ`,
> `G(χ, σ_s) := D(Λ^c(P_χ)‖Λ^c(σ_s)) − D(Λ(P_χ)‖Λ(σ_s)) = s·(w_E − w_B)(χ,φ) + o(s)`,
> where `w_B = Tr[Π_{ker Λ(P_χ)} Λ(φ)]` and `w_E = Tr[Π_{ker Λ^c(P_χ)} Λ^c(φ)]`.

(The derivative of `D(ω‖ω+sΔ)` at `s = 0` is `−Tr[Π_{supp ω}Δ] = Tr[(1−Π_{supp ω})Λ(φ)]` when ω
is rank-deficient — the same integral-representation computation as in §2.1(iii).) Verified
numerically at 6 `(x,φ)`:

| x | φ | w_B − w_E | G/s at s = 1e-6 | predicted |
|---|---|---|---|---|
| 1/5 | P_χ̄ | +0.44444444 | −0.44444182 | −0.44444444 |
| 1/5 | 1/3 | +0.11851852 | −0.11851808 | −0.11851852 |
| 2/5 | P_χ̄ | 0.00000000 | +0.00000189 | 0.00000000 |
| 2/5 | 1/3 | −0.05000000 | +0.05000061 | +0.05000000 |
| 9/20 | P_χ̄ | −0.08870968 | +0.08871113 | +0.08870968 |
| 9/20 | 1/3 | −0.08279570 | +0.08279623 | +0.08279570 |

`w_B − w_E` is **exactly the P13 weight operator** `Tr[Dφ]` (R5c/P13-A, `d_1 = (1−x)(2−5x)/(2−x)`,
positive iff `x < 2/5`; identically `−w_E < 0` off the isotropic stratum by P13-A). So:

- 𝒫_b2 is **violated at first order exactly where the P13 first-order `I_c`-ascent mechanism
  lives**, i.e. only on the isotropic stratum and only for `x < 2/5`. That is an *independent,
  review-tier explanation* of why the note's bounded search finds violations at `x ≤ 2/5` and
  none at `9/20, 49/100` — the note's numerical null on the strip is corroborated by a reviewed
  first-order theorem, not merely by an optimizer.
- The `x = 2/5` violation the note reports is therefore **non-perturbative** (`w_B − w_E ≤ 0`
  everywhere at `x = 2/5`). I reproduced it with an independent parameterization and optimizer
  and re-evaluated the minimizer at **50 dps**: `G = −0.122420884139` (note: `−1.2234614805e-01`).
  I checked it is **not** a support-threshold artifact: at the minimizer `min spec Λ(σ) = 2.95e-02`,
  i.e. nowhere near singular. **The note's new datum is real.** (By contrast the `x = 1/5` value
  `−11.67` *is* driven by `min spec Λ(σ) = 1.5e-12` and carries no magnitude information — only
  the sign is meaningful there.)

This addendum bears directly on MAJOR 3: at first order the two conditions coincide, so the
note's assertion that 𝒫_b2 is *strictly* stronger than `Q⁽¹⁾ = 0` has no evidence behind it.

---

## 4. FINDINGS

### MAJOR 1 — the §8 headline no-go statement has a broken quantifier (over-claim)

§8 (the boxed "Correct statement of what is established") reads:

> "Every order class defined by relative-entropy (or α ≥ 1 Rényi) domination that contains **a
> pair of MIXED states within arbitrarily small trace distance of a pure state** … is FALSE for
> Λ_x at every x ∈ (0,1/2), unconditionally".

That hypothesis is too weak for the conclusion. What the S1b witness kills is any class
containing the **specific** pairs `w(x,ε) = (ρ_ε + εX, ρ_ε)` for arbitrarily small ε. Row (d) of
the §7 table states this correctly ("any class containing **all** pairs of states within trace
distance δ of a pure state"); §8 drops the "all" and thereby declares FALSE a family of classes
the witness never touches.

This is not hypothetical. The P12 node itself proposes exactly such a class
(`WHGAP.restricted-order.md`, "Current status", third bullet): *"the P6 witness family shows
WHICH (ρ, X) pairs break full cBKM below 1/2 (spin-2 directions at near-pure REAL-stratum
anchors); a viable restricted order must EXCLUDE those pairs while keeping the purification
pairs."* A direction-restricted class of that kind contains mixed pairs arbitrarily close to a
pure state (so §8 as written kills it) but does **not** contain the witness, whose `X` lies in
the spin-2 sector (R5b claim 5). Nothing in this note bears on it.

**Consequence:** the S3 no-go map does **not** hold at the scope stated in §8, and menu option
(A)'s clause "the S3 no-go map holds at the stated scope" cannot be licensed as written.
**Fix:** restore the row-(d) quantifier in §8 ("contains all pairs within trace distance δ of a
pure state, for some δ > 0"), and add direction-restricted classes as an explicitly
**undecided** row of the table (they are the node's own live candidate).

### MAJOR 2 — the closed-interval statement `{x : P = 0} = [1/2,1]` overruns the disk scope of P4

Theorem 3.5 and §8 assert `{x ∈ (0,1] : P(Λ_x) = 0} = [1/2,1]` **exactly**, citing "P4 (frozen
input: P = Q = 0 on [1/2,1])". The disk says otherwise
(`channel-capacity/werner-holevo-gap/proof-dag/nodes/WHGAP.zero-capacity-application.md`):

- header `status: PROVED`; Claim: "**[PROVED …]** The **[1/2,1] Corollary sits at CERTIFIED\***
  (RK24 endpoint cite-only)";
- Current status: "**Theorem:** … for every x in **[1/2, 1)** … **Corollary at CERTIFIED\*:**
  {x : Q(Λ_x)=0} ⊇ [1/2, 1], with the x=1 endpoint resting on cite-only RK24."

Rule 7d requires a frozen citation to name the scope of the review it leans on; this one does
not, and the resulting displayed theorem promotes a CERTIFIED\* endpoint into a PROVED equality.
The commission's own frozen-input list repeats the same slip, so this is inherited rather than
invented — but the reload protocol makes the disk authoritative and requires me to report it.

**What is fully supported:** `{x ∈ (0,1) : P(Λ_x) = 0} = [1/2,1)` **exactly**, at PROVED tier.
The closed interval remains at CERTIFIED\* until the RK24 endpoint is discharged locally (an
already-registered optional upgrade on the P4 node; note that the archived external review on
that node argues the endpoint independently of RK24 — that argument, if adopted, would remove
this finding, but it is recorded there at external-review tier, not PROVED).

### MAJOR 3 — "𝒫_b2 is strictly stronger than Q⁽¹⁾ = 0" is asserted, not established

§7.2 and §7.3(B) state: *"a violation of 𝒫_b2 does **not** imply Q⁽¹⁾ > 0 (𝒫_b2 is **strictly
stronger** than Q⁽¹⁾ = 0), so the x = 2/5 datum says nothing about Q at 2/5."* The parenthetical
is load-bearing — if 𝒫_b2 were *equivalent* to `Q⁽¹⁾ = 0`, the reproduced `x = 2/5` violation
would be a `Q⁽¹⁾(Λ_{2/5}) > 0` statement, i.e. precisely the kind of Q-claim the commission's
scoping clause forbids being made *implicitly*. The note's only support for strictness is that
one particular route to the converse (the two-point ensemble of §2) is unavailable, which
establishes nothing. §7.2's "So 𝒫_b2 sits **between** more capable and less noisy" and §8's "is
dead at and below 2/5" inherit the same defect (the "dead **at** 2/5" clause additionally rests
on an optimizer result, i.e. NUMERICAL, whereas "below 2/5" rests on a PROVED input).

My §3 addendum sharpens the concern rather than resolving it: at first order the 𝒫_b2-violation
condition and the `Q⁽¹⁾`-ascent condition are *literally the same* function `w_B − w_E`, so no
separation is in evidence; the only witnessed gap is the non-perturbative `x = 2/5` datum, which
is evidence *for* strictness but is a single numerical point.

**Fix (conservative and sufficient):** replace with "the converse implication
(`Q⁽¹⁾ = 0 ⟹ 𝒫_b2`) is not established, hence a violation of 𝒫_b2 carries no Q-consequence";
downgrade "sits between" to "implies `Q⁽¹⁾ = 0`; whether the implication is strict is open"; and
mark "dead at 2/5" as NUMERICAL.

### minors

- **m1 (§7.3 B table).** The reported minima `+1.31e-04` (9/20), `+8.03e-06` (49/100),
  `+1.35e-04` (11/20 control) are optimizer stalls, not margins. My run (20 restarts, independent
  parameterization) drives them to `+8.10e-12`, `+1.78e-11`, `+1.43e-11` — i.e. to the degenerate
  corner `σ → P_ψ` where `G → 0⁺`. The note's honest-reading paragraph says this in prose, but
  the table invites the opposite reading. Recommend replacing the numbers with "no negative value
  found; `inf G = 0`, approached at `σ → P_ψ`".
- **m2 (§7.3 A).** The text says `ε = ε_c(x)/2` for the Rényi probes and then reports a control
  at `x = 11/20` — but `ε_c(11/20) = −4/7 < 0`, so that recipe is inadmissible there (`ρ_ε` would
  have negative eigenvalues). The script substitutes `ε = 1/10` correctly
  (`tools/whgap_p12a_s3probe.py:43`); the note never says so. Documentation only. (I walked into
  this exact trap in my own first run — see §6 R-3.)
- **m3 (§7.3 A, 7f).** The Rényi table is computed from the *closed-form* expression
  `D_α = log1p(w F_α(s))/(α−1)` (`s3probe.py:52–56`), i.e. it exercises the proved formula, not an
  independent construction — the note's own value-vs-formula discipline is not stated for this
  table. My matrix-power recomputation (40 cases) supplies the missing independent leg.
- **m4 (§3.6).** The memo-defect diagnosis is correct and independently confirmed (gate G5), but
  the note could state plainly that the memo transcribed the paper's `(5.3)` in the opposite
  orientation, which is what makes the error benign.
- **m5 (§6).** Prop. 6.1 is presented as an own derivation; it is also literature — HRSF22
  eq. (3.4), p. 12 of the local PDF, attributed there to Wilde Thm 13.6.1. Novelty is not
  claimed, but S0's "is it new?" discipline was applied only to the private-capacity theorem.
- **m6 (§4 / script).** `whgap_p12a_gates.py:216` casts the exact rational `LB` to float64 before
  the mpmath comparison `LB ≤ Δ`. Harmless at the ~1e-4 relative margins in play, but it means
  "exact rational arithmetic" covers `LB > 0` (exact) and not `LB ≤ Δ` (60-dps float). The note's
  §4 text is already correctly worded; this is a script-hygiene note only.
- **m7 (§7 table row a5).** "DEAD below 1/2 **iff** it implies a1" is a conditional cell inside a
  column headed "verdict below 1/2"; it should be read as UNDECIDED. `WHGAP.relaxed-lift` is
  CONJECTURED on disk, consistent.
- **m8 (§3.4b).** `s* ∈ (0, 1/√2]` should be `(0, 1/√2)` on the open family `x ∈ (0,1/2)`; the
  endpoint is attained only in the `x → 0` limit. Cosmetic.
- **m9 (commission compliance).** The commission asked S3 to record "on what grounds: false
  conclusion vs unprovable". Every DEAD verdict in the note is of a single type — the class's
  *domination hypothesis* is FALSE for `Λ_x` — established either directly by the witness (rows
  a1–a4, a6, b1, d) or by contradiction with PROVED `Q > 0` (rows b2, c on `(0,2/5)`). The
  content is recoverable but the distinction is not tabulated; recommend an added column, which
  would also make the `[2/5,1/2)` cells read UNDECIDED rather than blank.

### Screened and NOT found (7e — standing failure-mode list, item by item)

1. `.H` on real-symbolic matrices — the note uses `.T` throughout and justifies it from real
   Kraus; I re-verified the Kraus entries are real on `x ∈ (0,1)`. Clean.
2. WindowsApps interpreter — pinned interpreter used by both of us. Clean.
3. Complement convention drift — I built the padded 4×4 independently; the a-block vanishing and
   the untouched `(1−x), xε` entries reproduce. Clean.
4. Transpose vs conjugate-transpose — **this is where both of us slipped** (executor's R-1,
   my R-2); both defects were caught by gates and repaired. The final note is clean.
5. `sorted()` on symbolic eigenvalues — the note compares eigenvalue *sets*; I did the same and
   additionally avoided assumed eigenvalue pairing in the Rényi recomputation. Clean.
6. CRLF in SHA256SUMS — executor's file verifies 15/15 from the repo root; mine is LF.
7. Degeneracy bookkeeping — both perturbations sit inside exactly degenerate scalar blocks
   (`b·I₂`, `e·I₂`), so commutation is exact and no divided-difference issue arises. Confirmed
   symbolically (gates B2, E3). Clean.
8. `ε log ε` bookkeeping — not applicable to §3 (finite-ε rational statement). Correctly claimed.
9. Anchoring — the note's MEMO-CHECK block runs last and its G-ind route is formula-free;
   my own derivation preceded any comparison, and I disclose the structural notational
   coincidence in §1. Clean.

**Not over-claimed anywhere I could find:** no statement about `Q` on `[2/5,1/2)` leaks into any
theorem, corollary, table verdict, or summary sentence. §6's scope note and §8's binding
scoping paragraph are correct and sufficient. The one *implicit* Q-adjacent exposure is
MAJOR 3, and it errs in the conservative direction.

---

## 5. What I would license if the findings are addressed

Had the three MAJORs not been present, the following would be licensable at PROVED tier on the
strength of this review (stated here so the decision layer can act on the corrected note without
a second full review cycle):

1. **`P⁽¹⁾(Λ_x) ≥ Δ(x, ε_c/2, ε_c/2) = [(1−2x)(1−x)/(2−3x)]·f((1−2x)/(√2(1−x))) ≥
   (1−2x)³/(2(1−x)(2−3x)) > 0` for every `x ∈ (0,1/2)`, hence `P(Λ_x) > 0` there** — every step
   independently re-derived (own Kraus/complement/entropies), symbolically where possible and at
   60 dps at 11 parameter points; exact rational certificates at 6 x reproduced in ℚ.
   Theorem 3.2 (threshold form, needed for row (d)) and Lemma 3.2b/(3.5) (exact form) both hold.
2. **`{x ∈ (0,1) : P(Λ_x) = 0} = [1/2,1)` exactly**, with `[1/2,1]` at CERTIFIED\* pending the
   RK24 endpoint (MAJOR 2 is exactly the difference between this and what the note wrote).
3. **The purity-knob hierarchy (S2)** — Prop. 6.1, Prop. 6.2 (= ZW (2.6)), Cor. 6.3 — verified;
   the pure/mixed regime separation reproduced at 3 x.
4. **Theorem 2.1** (less noisy ⟺ RE domination) — verified; also HRSF22 Prop. 2.3, so not new.
5. **Prop. 5.1** (`Δ ≤ 0` on all of `[1/2,1]`, symbolically) and **Prop. 7.1** (α ≥ 1 Rényi
   orders fail below 1/2) — verified, the latter by an independent matrix-power route.
6. **S3 rows a1–a4, a6, b1, c, d** at the *row-(d)* scope — verified.

The surviving frontier as I read it after this review: (i) direction-restricted classes (the
node's own spin-2-excluding candidate) — **undecided, and wrongly declared dead by §8**;
(ii) `𝒫_b2` on `[2/5,1/2)` — undecided, with its first-order layer now explained by P13;
(iii) `WHGAP.order-converse` (P11); (iv) genuine `I_c`-additivity technology
(`WHGAP.more-capable-route`). The note's proposal to register `𝒫_b2` as a new node under rule 8b
is well taken; I would add a second node for the direction-restricted class.

---

## 6. Reviewer resistance log (append-only)

- **R-1.** Five gates in `whgap_r8_symbolic.py` (H1, H2, K4, M1, S2) failed on the first run.
  Diagnosis: sympy will not combine `log(a) + log(b) → log(ab)` for symbols without positivity
  assumptions, so the entropy-to-`f` identities and the two `h`-derivatives were unprovable as
  written. Repaired in `whgap_r8_symbolic2.py` by re-establishing each with **positive free
  symbols** and `expand_log(..., force=True)`, plus a 60-dps numerical leg at 5 points; `M1`/`M2`
  closed in `whgap_r8_closeout.py` by 50-dps finite differences at 4 points. Not a defect of the
  reviewed note.
- **R-2.** `S2a` and `S3c` failed on the first numerical run (residuals ~1e-1). Diagnosis: **my
  own** `vN()` projected each output onto its real part before calling `mp.eigsy`, which is wrong
  for the complex Hermitian outputs of random complex pure states — standing failure mode 4, the
  same class of slip the executor logged as R-1. Repaired by using `mp.eighe` on the properly
  Hermitized matrix (`whgap_r8_s2s3.py`); residuals then `≤ 2e-40`. Not a defect of the note.
- **R-3.** The Rényi block crashed with a complex-ordering error. Diagnosis: **my own** — at the
  control `x = 11/20` I used `ε = ε_c(x)/2`, which is *negative* there, so `ρ_ε` was not a state.
  Repaired by using `ε = 1/10` at `x ≥ 1/2`. This is what surfaced minor m2: the note's text does
  not record which ε its own control used.
- **R-4.** My first `S1c` reproduction used `sp.nsimplify(..., rational=True)` on an
  already-rational expression, violating the frozen tooling rule. Re-done in
  `whgap_r8_closeout.py` with pure `sp.Rational` arithmetic and an `isinstance(LB, sp.Rational)`
  assertion; all six rows unchanged.
- No resistance on the note's main theorem: every claim in §2, §3 and §5 of the note passed my
  independent route, most of them first time.

## 7. Provenance

Commands (cwd = repo root, interpreter `C:<home>/cpython3119/python.exe`):

```
python tools/whgap_r8_symbolic.py    > artifacts/logs_whgap_r8_20260730/r8_symbolic.log
python tools/whgap_r8_symbolic2.py   > artifacts/logs_whgap_r8_20260730/r8_symbolic2.log
python -u tools/whgap_r8_numgates.py > artifacts/logs_whgap_r8_20260730/r8_numgates.log
python -u tools/whgap_r8_s2s3.py     > artifacts/logs_whgap_r8_20260730/r8_s2s3.log
python -u tools/whgap_r8_b2probe.py  > artifacts/logs_whgap_r8_20260730/r8_b2probe.log
python -u tools/whgap_r8_closeout.py > artifacts/logs_whgap_r8_20260730/r8_closeout.log
python -u tools/whgap_r8_lit.py      > artifacts/logs_whgap_r8_20260730/r8_lit.log
```

SHA-256 of reviewer scripts and logs: `artifacts/logs_whgap_r8_20260730/SHA256SUMS_R8.txt`
(LF; `sha256sum -c` verified). Executor's `SHA256SUMS_E-P12A.txt`: **15/15 OK**.

I wrote no node file, no `NODE_INDEX.md` entry and no DAG edit (single-writer deviation). No
status is applied by me; the decision layer applies licensing citing this report.

