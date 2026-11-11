# WHGAP R5b — independent rule-7 review of P6b-V1 and the paper's necessity section (2026-07-29)

Reviewer: fresh Opus instance, no authorship of any reviewed work, no desired outcome given.
Commission: `channel-capacity/werner-holevo-gap/notes/WHGAP_REVIEW_COMMISSION_R5_20260729.md`, §R5b.
Interpreter for every run: `C:<home>/cpython3119/python.exe` (sympy 1.13.1, mpmath 1.3.0,
numpy 1.26.4, scipy 1.14.1).

**VERDICT: (A) — license granted, with 8 minors and no MAJOR.** Exact licensing wording in §8.

---

## 0. PRE-ACTION REPORT (research/PRETASK_RELOAD_PROMPT.md, executed from disk first)

Files read from disk, completely, in the prescribed order, before any math or code:
`research/DAG_PROTOCOL.md`; `research/RESEARCH_STRUCTURE_PROTOCOL.md`;
`channel-capacity/werner-holevo-gap/README.md`;
`channel-capacity/werner-holevo-gap/notes/WERNER-HOLEVO-GAP_PROOF_DAG.md`;
`channel-capacity/werner-holevo-gap/proof-dag/NODE_INDEX.md`;
`.../proof-dag/nodes/WHGAP.order-boundary.md` and its parent `.../nodes/WHGAP.goal.md`
(this LEAF has no children).

- **Target node and status as read from disk:** `WHGAP.order-boundary` (alias P6), kind LEAF,
  role proof, **status NUMERICAL** with `status_source` "P6 execution 2026-07-29; interval-certified
  grid violations and bounded-search boundary bracket; pending-review", `disposition: null`,
  parents `["WHGAP.goal"]`, children `[]`. "Adversarial reviews: None yet." NODE_INDEX row and the
  DAG Mermaid/outline agree (NUMERICAL, pending-review). No status drift found.
- **My ROLE:** reviewer. **Independence statement:** I did not author the paper, the P6b execution,
  the witness, or any script under review; I was given no desired outcome; the two licensing options
  were presented to me as alternatives.
- **Highest status my evidence could license (§2 ladder):** my completed, archived, rule-7-compliant
  review opens the **PROVED** tier for the reviewed mathematics. Per rule 2/§2, **the status write
  itself is not mine to make** — I am the independent checker whose report the decision layer cites;
  and per the commission's binding single-writer deviation I edit no node file, no `NODE_INDEX.md`
  and no DAG doc. I write only this report, my script, and my logs.
- **Gates and deliverables (one line each):** (1) audit Lemma `lem:re-to-bkm`'s exact statement,
  hypotheses and second-order expansion; (2) rebuild the witness computation in my own script with
  my own basis order and my own complement assembly; (3) audit the conclusion `x ≥ 1/2` necessary,
  and the phase Corollary given frozen P2/P4; (4) audit the finite-ε strict-violation family for an
  explicit ε(x) > 0; (5) audit the λ_5/2 bookkeeping and the spin-2 claim; independent-path
  requirement: verify the RE→BKM Hessian claim by finite differences on toy examples at ≥ 2
  parameter points; deliverable: this report at
  `artifacts/whgap_r5b_review_20260729.md` plus a verdict from the R5b menu.
- **Conflicts between commission text and the disk protocols:** two, both recorded, neither
  resolved silently by me:
  1. **Single-writer deviation.** The commission forbids the node/index/DAG updates that
     `RESEARCH_STRUCTURE_PROTOCOL.md` §6 and `DAG_PROTOCOL.md` §5 would otherwise require of me in
     this session. The commission states the deviation is commissioned per protocol and that the
     decision layer performs the atomic updates citing this artifact immediately after the batch. I
     comply with the commission and flag it here; the atomic-update obligation therefore sits with
     the decision layer, not with me.
  2. **Shared log directory / SHA manifest.** The commission asks each R5 agent to end with
     `artifacts/logs_whgap_r5_20260729/SHA256SUMS.txt`. That file was already present and owned by
     the concurrent R5a agent when I finished. Overwriting it would have destroyed another agent's
     provenance — exactly the corruption the single-writer deviation exists to prevent. I therefore
     wrote **`SHA256SUMS_r5b.txt`** (LF endings, verified with `sha256sum -c`) covering only my own
     files. Flagged, not silently resolved.
  Additionally, one **wording** discrepancy in the commission's own licensing menu (not a protocol
  conflict) is recorded in §8: menu (A) reads "necessary for `⪰_cBKM`, **hence** for `⪰_cRE`", which
  inverts the implication (cBKM is the *stronger* order). The paper does it correctly; I license the
  logically correct direction and say so explicitly.

---

## 1. Type audit (rule 7a) — every object in the reviewed claims

| Object | Type / dimension | Notes |
|---|---|---|
| `Λ_x` | `M_3(C) → M_3(C)`, CPTP, unital, self-adjoint w.r.t. HS | sector scalars `1`, `1−3x/2` (sym traceless, 5-dim), `1−x/2` (antisym, 3-dim) — my gate A6 |
| `Λ_x^c` | `M_3(C) → M_4(C)`, CPTP, **padded** (4-dim environment) | built as `Tr(K_a Y K_b^†)`; not the 3-dim minimal complement — my gates A3, A4 |
| `K_0 … K_3` | `3×3`, **real** | `K_0 = √(1−x)·1`, `K_{μ+1} = √(x/2)·A_μ`; realness proved (gate A0) so `K^† = K^T` is sound (failure mode 4) |
| `ρ_ε` | `3×3` state, faithful iff `0 < ε < 1/2`, spectrum `{1−2ε, ε, ε}` | 0-based labels: the two `ε` directions are `|1⟩,|2⟩` |
| `X` | `3×3` Hermitian, **traceless**, symmetric, `‖X‖_HS = 1` | an *observable/tangent direction*, not a state; spin-2 |
| `Λ_x(ρ_ε)` | `3×3` ≻ 0, diagonal, spectrum `{a_ε, b_ε, b_ε}`, `b_ε = x/2+(1−3x/2)ε` | degenerate pair carries `X` — my gate B3 |
| `Λ_x^c(ρ_ε)` | `4×4`, diagonal, spectrum `{1−x, xε, e_ε, e_ε}`, `e_ε = (x/2)(1−ε)` | **faithful iff ε > 0**; the `xε` eigenvalue is the only one that dies at ε = 0 and it is *not* touched by `Λ^c(X)` — my gates B4, B5 |
| `Λ_x(X)` | `3×3` = `(1−3x/2)X`, traceless | gate B1 |
| `Λ_x^c(X)` | `4×4` = `0 ⊕ (−x/2)X`, traceless | `a(X) = 0` kills the cross block — gate B2 |
| `g_θ(·)` | quadratic form on Hermitian matrices; **requires θ faithful** | receiver: form on `M_3`; environment: form on `M_4` — different domains, must not be conflated |
| `Δ_J(τ)` | superoperator-valued: `M_3(C) → L(M_3(C))`; Choi `27×27` | `L_{M(τ)} − J^†∘L_{N(τ)}∘J`; `J: M_3 → M_4` (16×9 matrix), `J^†` is its HS adjoint (9×16) — my block F |
| `λ_5, λ_3` | scalars, multiplicities 5 and 3 in a 27-dim space | `λ_5 = 4(1−x)(2x−1)/x`, `λ_3 = 16(1−x)(3x−1)/(9x)` |

The one type-level defect found is **m1** below: Lemma 5.1's conclusion names `g_{N(ρ)}` and
`g_{M(ρ)}` while its hypotheses require only the *input* `ρ` to be faithful. `g_θ` is defined in the
same lemma only for faithful `θ`, so the displayed conclusion is ill-typed for channels that map a
faithful input to a rank-deficient output. In the application both outputs are faithful for `ε > 0`
(verified), so nothing downstream fails.

## 2. Standing failure modes (rule 7e / commission §2) — item by item

1. **`.H` on real-symbolic matrices leaving `conjugate(√(1−x))`.** Screened, and I *hit it* in my
   first draft. Structurally eliminated: my Kraus operators are built from **positive real symbols**
   `s = √(1−x)`, `t = √(x/2)`; gate **A0** proves every Kraus entry is real, which is what makes
   `K^† = K^T` sound; `s²→1−x`, `t²→x/2` are substituted only at the end. The authored script
   `whgap_p6b_v1_witness.py` uses the same defence (`ALPHA`, `BETA` positive) and documents it —
   correctly.
   *Second-order trap found in my own tooling and recorded here:* substituting `s**4 → (1−x)**2`
   *before* `s**2` makes sympy match `s**2` as `(s**4)**(1/2)` and emit `Abs(x−1)`, silently
   poisoning every downstream identity. Single-pass `s**2/t**2` substitution is correct (verified on
   `s²,s³,s⁴,s⁶,st,s³t`).
2. **WindowsApps store python.** Not used; the pinned interpreter throughout.
3. **Complement convention drift (3-dim vs padded 4-dim; sign of the `a(Y)` block; the `k` factor).**
   Screened by gate **A3**: all 16 entries of my Kraus-built `Λ^c(Y)` against the paper's `eq:comp`
   on a *generic complex* `Y`, including the cross-block signs (`+β a(Y)^T` top row, `−β a(Y)` first
   column) and `β = st = √(x(1−x)/2)` (gate A2b). Padded-vs-minimal is tracked explicitly in §1.
4. **Transpose vs conjugate transpose.** See item 1; realness proved before any `.T` is used.
5. **`sorted()` on symbolic eigenvalues.** Avoided: eigenvalues are handled via `eigenvects` with
   symbolic degeneracy tests, never sorted; only *numeric* eigenvalues are sorted.
6. **CRLF in SHA manifests.** My manifest is LF (`file` reports plain "ASCII text") and
   `sha256sum -c` passes.
7. **Eigenvalue bookkeeping at degeneracies / near-zero gaps.** This is the *centre* of this witness
   and was screened hardest: both BKM forms are evaluated entirely inside **degenerate** blocks
   (`c(a,a) = 1/a`), which I confirmed symbolically (B3, B4) and, independently, by a finite-difference
   check on a deliberately **degenerate-spectrum** toy (`θ = diag(1/2,1/4,1/4)`, gate E toy3). The
   only near-zero eigenvalue in the problem (`xε → 0`) is *not* in the support of `Λ^c(X)`, so no
   divided difference ever divides by a vanishing gap — this is why the ε→0 limit is finite on both
   sides, and it is exactly what the 0-based index convention buys (see m3).
8. **`ε log ε` bookkeeping / kernel-cluster remainders.** **Not applicable to R5b.** No `ε log ε`
   expansion appears anywhere in the necessity chain: `g_B(ε)` and `g_E(ε)` are rational in `(x,ε)`
   and finite at `ε = 0`. (That machinery belongs to the N1' lemma, R5d scope.) Screened and
   dismissed with reason, not waved.
9. **Anchoring.** See §3.

## 3. Anchoring discipline (rule 7c) — what was independent, and one honest coincidence flag

Order of work, strictly: (i) protocol chain + node files; (ii) paper §5 — *the object of review*,
necessarily read; (iii) **my own hand derivation and my own script, written and run to exit 0**;
(iv) only then `artifacts/whgap_p6b_necessity_20260729.md`, `tools/whgap_p6b_v1_witness.py`,
`tools/whgap_p6b_v1_bridge.py`, and the P6b logs.

**Coincidence flag, as rule 7c requires.** I read the paper's *displayed values* for `g_B`, `g_E`
and the gap before deriving them, because they are the claims under review; my agreement with those
three displays therefore corroborates rather than independently discovers them. What is genuinely
mine and was produced with no sight of the authored scripts: my own channel/complement assembly from
Kraus in **two different basis orders**; the BKM form by **two independent routes** (divided
differences *and* the integral representation `∫₀^∞ Tr[Z(θ+u)^{-1}Z(θ+u)^{-1}]du`, agreeing to
`<1e-45` relative); the **factorization** `x·b_ε − 2u²(1−ε) = 2(1−x)[(2x−1) + (1−3x/2)ε]`; the
**explicit threshold** `ε_c(x) = 2(1−2x)/(2−3x)` (which appears nowhere in the paper); the
finite-difference verification of the RE→BKM Hessian claim at seven configurations; and an
independent from-scratch rebuild of the `27×27` defect Choi matrix and its spectrum.

My script: **`tools/whgap_r5b_indep_necessity.py`** (sha256
`8fd22bb86d0cf7984acc88d37d784ab45402f3b28ff636a36fc179eab1b56a94`).
Log `artifacts/logs_whgap_r5_20260729/r5b_indep.log`, machine record
`.../r5b_indep.json`, manifest `.../SHA256SUMS_r5b.txt`.
**Result: 57 gates, 0 failures, exit 0.**

**Independence note on the reviewed layer.** `artifacts/whgap_p6b_necessity_20260729.md` discloses
honestly that the commissioned executor died three times and that the **decision layer** — i.e. the
proposer of the witness — executed P6b V1 itself. The P6b layer is therefore *proposer-authored*
verification. The independence rule 6 requires for this node is carried by **this review's own
script**, not by P6b. I record that explicitly so the eventual status write cannot lean on P6b for
independence.

## 4. Claim-by-claim findings

### Claim 1 — Lemma 5.1 (`lem:re-to-bkm`): cRE forces BKM domination

**Statement audited as displayed.** Hypothesis: `M, N` channels with common input, `ρ` a faithful
input state, `N ⪰_cRE M` "even merely with trivial reference". Conclusion: for every traceless
Hermitian `X`, `g_{N(ρ)}(N(X)) ≥ g_{M(ρ)}(M(X))`. Proof: `(ρ+tX, ρ)` is an admissible pair by
faithfulness; the second-order expansion
`D(Φ(ρ)+tΦ(X) ‖ Φ(ρ)) = (t²/2) g_{Φ(ρ)}(Φ(X)) + O(t³)` holds for any channel `Φ`; compare `t²`
coefficients.

Checks I performed:

- **Hypothesis sufficiency.** Trivial reference is `dim R = 1`, which is inside "every finite
  reference" in the paper's own definition of the order (§4, lines 406–409), so the weakest possible
  hypothesis is being used — correct, and it makes the theorem stronger. `Tr X = 0` is exactly what
  makes `ρ+tX` a state and kills the first-order term (`d/dt D(θ+tZ‖θ)|₀ = Tr Z = 0`, since `Φ` is
  trace preserving); `Φ(X)` traceless verified (gates A4, A4b, B1, B2).
- **The `1/2` and the identification of the Hessian with the BKM form.** Verified two ways.
  Analytically I derived the divided difference from the integral representation:
  `∫₀^∞ (a+u)^{-1}(b+u)^{-1} du = (log a − log b)/(a−b)`, and `= 1/a` at `a=b`, so
  `g_θ(Z) = Σ_ij |Z_ij|² c(λ_i,λ_j)` **is** the Kubo–Mori metric — my `bkm_integral_num` route agrees
  with the divided-difference route to `<1e-45` relative at three `(x,ε)` points (gate B8).
  Numerically I checked the expansion itself by finite differences (gates **E**), at **seven**
  configurations, all with the correct remainder *shape*:

  | configuration | `g_θ(Z)` (independent) | best rel. err. | remainder |
  |---|---|---|---|
  | toy1 `2×2` nondegenerate, complex `Z` | 0.2276698429513284 | 6.2e-9 | `O(t)` |
  | toy2 `3×3` **non-diagonal** nondegenerate, complex `Z` | 0.2480717401465826 | 7.0e-10 | `O(t)` |
  | toy3 `3×3` **degenerate** `diag(1/2,1/4,1/4)` | 0.1188629436111989 | 1.2e-8 | `O(t)` |
  | witness receiver, `x=2/5, ε=1/50` | 0.7692307692307692 | 3.1e-15 | `O(t²)` |
  | witness environment, `x=2/5, ε=1/50` | 0.2040816326530612 | 8.7e-16 | `O(t²)` |
  | witness receiver, `x=9/20, ε=1/200` | 0.4660783232211803 | 1.7e-15 | `O(t²)` |
  | witness environment, `x=9/20, ε=1/200` | 0.2261306532663316 | 8.4e-16 | `O(t²)` |

  The pass criterion is the decay law, not a single small number: `rel_err/t` is constant to
  4 significant figures on the toys (`O(t³)` term present) and drops by exactly `10×` per decade on
  the witness cases (the cubic term vanishes there by symmetry, so the remainder is `O(t⁴)`). This
  is a genuine confirmation of the expansion's *shape*, not just of one value.
- **Failure mode of the lemma as stated.** `g_θ` is defined in the lemma only for faithful `θ`, but
  no hypothesis forces `M(ρ)` or `N(ρ)` faithful. A channel can map a faithful input to a
  rank-deficient output, in which case `g_{M(ρ)}` is undefined and
  `D(M(ρ)+tM(X)‖M(ρ))` can be `+∞` for every `t ≠ 0`, so the expansion fails. → **minor m1**.
  In the application both outputs *are* faithful for `ε>0` (gates A5, B5), so the theorem is safe.
- **"Comparing `t²` coefficients"** is loose phrasing for: divide the inequality by `t² > 0` and let
  `t → 0`. Correct as intended; no defect.

**Verdict on claim 1: correct as applied; statement needs the output-faithfulness hypothesis (m1)
and a citation for the expansion (m5).** FORMULA-level for the divided-difference/integral identity;
VALUE-level (7 configurations) for the expansion itself.

### Claim 2 — the witness computation

Rebuilt from the frozen §1 conventions in my own script, in **two basis orders**: the paper's
(`heavy = 0`, degenerate pair `{1,2}`) and a permuted one (`heavy = 1`, pair `{0,2}` — an `O(3)`
permutation of the first, so covariance demands identical forms). Both give, **symbolically in
`(x,ε)`**:

```
Λ_x(X)   = (1 − 3x/2) X                                        [B1]
a(X)     = 0,  Λ_x^c(X) = 0 ⊕ (−x/2)X                          [B2]
Λ_x(ρ_ε) = diag(a_ε, b_ε, b_ε),  b_ε = x/2 + (1−3x/2)ε         [B3]
Λ_x^c(ρ_ε) = diag(1−x, xε, e_ε, e_ε),  e_ε = (x/2)(1−ε)        [B4,B5]
g_B = (1 − 3x/2)² / b_ε          g_E = x / (2(1 − ε))          [B6,B7]
```

All four displays of Theorem 5.2 reproduce **exactly**, in both basis orders, as identities in
`(x,ε)` — FORMULA level, not sampled. Cross-checked at VALUE level by the integral representation at
`(x,ε) ∈ {(2/5,1/20), (9/20,1/100), (3/5,1/50)}` to `<1e-45` relative (B8).

Post-hoc comparison with the authored `v1_witness.json`: the recorded
`g_B = (3x−2)²/(2(x+2ε−3εx))` is algebraically identical to my `(1−3x/2)²/b_ε` (numerator
`(2−3x)² = 4(1−3x/2)²`, denominator `= 4b_ε`); `g_E = −x/(2ε−2) = x/(2(1−ε))`; environment
eigenvalues `[1−x, εx, x(1−ε)/2, x(1−ε)/2]` identical to mine. **No discrepancy.**

Two structural observations worth recording, both load-bearing:

- The *only* eigenvalue that vanishes as `ε → 0` is the environment's `xε`, and `Λ^c(X)` has **no
  support on it**. That is precisely why `g_E(ε)` stays finite (`→ x/2`) and the `ε→0` limit needs no
  regularization. Verified (B4, B5, C2, C4).
- Both BKM forms live entirely inside degenerate blocks, so only the `c(a,a) = 1/a` branch is used —
  no log divided difference enters at all. This is what makes the whole computation four lines.

**Verdict on claim 2: fully confirmed at FORMULA level, in two independent basis orders.**

### Claim 3 — the conclusion `x ≥ 1/2` necessary, and the phase Corollary

- **Gap identity (FORMULA, gate C1):** `x/2 − (2/x)(1−3x/2)² = 2(1−x)(2x−1)/x`, derived by hand
  (`(2/x)[x²/4 − (1−3x/2)²] = −2(2x−1)(x−1)/x`) and confirmed symbolically.
- **Limits (C2, C4):** `g_E → x/2` and `g_B → 2(1−3x/2)²/x` as `ε→0⁺`; both sides continuous at
  `ε = 0`, so the argument is a limit of *valid* inequalities — **no interchange of limits is
  involved**, and the ε→0 route alone is a complete proof, independent of the finite-ε family.
- **Sign (C3):** `2(1−x)(2x−1)/x` is `< 0` exactly on `(0,1/2)`, `= 0` at `1/2`, `> 0` on `(1/2,1)`.
- **Logical direction.** The paper proves `¬(Λ^c ⪰_cRE Λ)` for `x < 1/2`, i.e. `x ≥ 1/2` is
  necessary for the **weaker** order `⪰_cRE`, hence *a fortiori* for the **stronger** `⪰_cBKM`. The
  paper's Corollary proof also gives the direct route (cBKM ⟹ trivial-reference BKM domination ⟹
  contradiction). Both are sound. (The commission menu's "hence" runs the other way; see §8.)
- **Corollary 5.3 (`cor:phase`).** The cycle closes: `x ≥ 1/2 ⟹` certificate
  (`thm:spectrum` + `lem:x1`, frozen P2/P4 scope); certificate `⟹ cBKM ⟹ cRE` (`thm:zw` +
  the BGSW bridge); `cRE ⟹ x ≥ 1/2` (`thm:necessity`). I checked the non-obvious payoff and confirm
  it: because the necessity argument is about the *order*, it upgrades Proposition `prop:unique`
  from "no member of the five-parameter covariant **ansatz** certifies below `1/2`" to "**no**
  signed-lift CP-defect certificate whatsoever exists below `1/2`". That is a real strengthening and
  it is correctly used in §6 (lines 583–586). `x = 1` sits in the `≥ 1/2` half so the necessity leg
  is vacuous there; the corollary's `x=1` parenthetical (minimal self-complementary representation)
  is a *faithfulness* caveat for `thm:zw`, not an order caveat — the orders themselves are invariant
  under isometric environment embeddings, so no ambiguity arises. `(0,1]` is exactly partitioned by
  the two cases: no regime is left untested.
- **Consistency with the frozen certified terrain (D5, E-control).** The same witness produces **no**
  violation at `x ∈ {1/2, 11/20, 4/7, 3/4}` for any tested `ε`, and at `x ∈ {11/20, 3/4}` the direct
  relative entropies satisfy `D_env > D_rec`. A witness that "violated" on proved-zero terrain would
  have been a decisive falsifier; it does not.

**Verdict on claim 3: confirmed. `x ≥ 1/2` is necessary for `⪰_cRE` (and hence `⪰_cBKM`);
Corollary 5.3 follows given frozen P2/P4.**

### Claim 4 — the finite-ε strict-violation family

I derived the exact condition myself before reading the authored script. Since `x/2 + (1−3x/2)ε > 0`
and `1−ε > 0`, `g_E ≥ g_B` is equivalent to the **linear** condition
`x·b_ε − 2(1−3x/2)²(1−ε) ≥ 0`, and that expression factors as

```
x b_ε − 2u²(1−ε) = 2(1−x)[ (2x−1) + (1−3x/2) ε ],      u := 1 − 3x/2
```

whose `ε`-coefficient `2(1−x)(1−3x/2)` is **strictly positive** on `(0,1/2)` (gate D2). Hence the
violation set is exactly the interval

```
0 < ε < ε_c(x) = 2(1−2x)/(2−3x)              [D1, D3]
```

`ε_c(x) > 0` exactly on `(0,1/2)` and `ε_c → 0` as `x → 1/2⁻`. Taking `ε = ε_c(x)/2` I verified in
**exact rational arithmetic** at 11 rational `x < 1/2` (`1/100, 1/20, 13/100, 39/100, 79/200, 2/5,
199/400, 399/800, 499/1000, 4999/10000, 7999/16000` — including the P6 bracket endpoint) that
`g_E < g_B` strictly, that `0 < ε < 1/2` so `ρ_ε` is faithful, and that **both** outputs are
positive definite (gate D4). So the commissioned claim — "for each rational `x < 1/2` there is an
explicit `ε(x) > 0` with strict BKM violation at faithful `ρ_ε`" — holds, and in fact holds at
FORMULA level for **all real** `x ∈ (0,1/2)`, not merely rational ones.

Post-hoc: the authored script reaches the same place by the same algebra and additionally records the
symbolic strictness certificate `gap(ε_c/2) = −(1−2x)(2−3x)/(1−x) < 0` on `(0,1/2)`, which I
re-derived by hand and confirm. Its `eps_c = 2(2x−1)/(3x−2)` is my `ε_c`, and its `eps_star` is my
`ε_c/2`. Its gap closed form `(x−1)(ε(3x−2)−4x+2)/((ε−1)(ε(3x−2)−x))` is algebraically identical to
mine. **No discrepancy.** This layer is *stronger* than the paper, which states no threshold at all
(→ **minor m2**).

**Verdict on claim 4: confirmed at FORMULA level over the whole interval, plus 11 exact rational
instances.**

### Claim 5 — the `λ_5/2` bookkeeping and the spin-2 remark

- `2(1−x)(2x−1)/x = λ_5(x)/2` with `λ_5 = 4(1−x)(2x−1)/x` — FORMULA, gate F2 (trivial arithmetic,
  confirmed).
- `X` is symmetric traceless, hence in the 5-dimensional spin-2 sector; `mult(λ_5) = 5` matches
  (gate F3, and A6 which confirms `Λ_x` acts on that sector by `1−3x/2`).
- **I did not take `λ_5` on trust.** I rebuilt the `27×27` defect Choi matrix from scratch — my own
  `J_x` assembly at the forced point `(p,d) = (1/3, 2(1−x)/3)`, my own vectorization
  `E_kl ↔ e_k⊗e_l`, my own HS adjoint `J^† = J_mat^†`, my own `Δ_J(E_ij) = Λ(E_ij)⊗1 − J^†(Λ^c(E_ij)⊗1)J`
  — and at `x = 2/5` **and** `x = 3/5` (c ≥ 2, one on each side of the boundary) confirmed:
  Hermitian, all entries rational, the exact annihilator `C(C−λ_5)(C−λ_3) = 0`, both trace identities
  `Tr C = 5λ_5+3λ_3` and `Tr C² = 5λ_5²+3λ_3²` (which together pin the multiplicities uniquely), and
  — by a genuinely different route — 40-digit numeric eigenvalues giving exactly `0^19, λ_5^5, λ_3^3`
  (`λ_5 = −6/5 < 0` at `x=2/5`; `λ_5 = 8/15 > 0`, `λ_3 = 128/135` at `x=3/5`). Gate F1. This
  independently corroborates the frozen `thm:spectrum` as well.
- **What is *not* established** is the remark's causal language. The verified content is an equality
  of two scalar functions of `x` (contingent on `‖X‖_HS = 1`, which the paper does not state) plus
  the observation that both objects live in the spin-2 sector. "It **is** the local
  information-geometric obstruction" and "the certificate boundary, the order boundary, and the local
  BKM obstruction **coincide**" are interpretation beyond that — no sector-level derivation
  identifying the defect Choi's spin-2 block *with* the BKM gap form is given. → **minor m6**.

**Verdict on claim 5: the arithmetic and the spin-2 placement are confirmed (FORMULA for the
identity; VALUE at two rational `x` for `λ_5` and its multiplicity); the remark's causal reading is
unverified interpretation.**

## 5. Value-vs-formula statement (rule 7f)

| Claim | Established as | What remains unverified |
|---|---|---|
| `Λ_x`, `Λ_x^c` assembly, `eq:comp`, sector scalars | **FORMULA**, symbolic in `x`, generic complex `Y`, all 9/16 entries | — |
| `Λ(X) = (1−3x/2)X`, `Λ^c(X) = 0 ⊕ (−x/2)X`, spectra of `Λ(ρ_ε)`, `Λ^c(ρ_ε)` | **FORMULA** in `(x,ε)`, two basis orders | — |
| `g_B = (1−3x/2)²/b_ε`, `g_E = x/(2(1−ε))` | **FORMULA** in `(x,ε)`, two basis orders, two BKM routes | — |
| gap identity `= 2(1−x)(2x−1)/x`, its sign, the `ε→0` limits | **FORMULA** in `x` | — |
| violation set `= (0, ε_c(x))`, `ε_c = 2(1−2x)/(2−3x)` | **FORMULA** in `x`; + 11 exact rational instances | — |
| `c(a,b) = ∫₀^∞(a+u)^{-1}(b+u)^{-1}du` (BKM = Kubo–Mori) | **FORMULA** (symbolic) + `<1e-45` numeric agreement | — |
| `D(θ+tZ‖θ) = (t²/2)g_θ(Z) + O(t³)` (Lemma 5.1's engine) | **VALUE**, 7 configurations, correct remainder decay law | the general lemma is **not** proved here and is uncited in the paper (m5); it is a standard result, verified but granted |
| `λ_5 = 4(1−x)(2x−1)/x` with multiplicity 5 | **VALUE** at `x = 2/5, 3/5` (exact annihilator + traces + numeric spectrum) | the closed-form charpoly as an identity in `x` is frozen P2 scope, not re-derived symbolically here |
| Corollary 5.3's `x ≥ 1/2 ⟹` certificate leg | **frozen** (P2/P4, R2/R3-reviewed) | not re-reviewed; used only within its reviewed scope (7d) |
| Remark 5.4's structural interpretation | **not established** (numerical/algebraic coincidence only) | a sector-level derivation (m6) |

**Frozen-input scope used (7d).** Only: P2/P4 reviewed results (signed-lift region `[1/2,1)`,
`Q = P = 0` on `[1/2,1]`) and P3 reviewed results (`Q > 0` on `(0,x_1)`), plus commission §1
conventions. I relied on P3 only as a consistency cross-check, never as a premise. Everything else
in the repo was treated as carrying only its node status; in particular I did **not** treat the
pending-review P6 numerics, the P9b datum, or the CONJECTURED `x_D = 2/5` as established. My λ_5
check does not lean on the frozen `thm:spectrum` — it rebuilds it.

## 6. Findings

**MAJOR: none.** No link of the necessity chain fails. Every displayed identity of §5 reproduced
exactly in an independent construction, the logic is sound, the claim discipline is correct (the
paper does **not** claim anything about `Q` below `1/2`, and explicitly leaves it open at lines
586–590), and the result is consistent with the frozen certified terrain.

**Minors** (m1–m7 in scope; m8 adjacent, reported because it is cheap and the paper is a deliverable):

- **m1 — Lemma 5.1 is missing a hypothesis (must-fix; ill-typed as displayed).** Add "with `M(ρ)`
  and `N(ρ)` faithful" (or "with both output states faithful"). As written the conclusion names
  `g_{N(ρ)}, g_{M(ρ)}`, which the lemma defines only for faithful arguments; for a channel mapping a
  faithful input to a rank-deficient output, `D(M(ρ)+tM(X)‖M(ρ)) ≡ +∞` and the expansion fails.
  Correspondingly, Theorem 5.2 should display the **full** environment spectrum
  `Λ_x^c(ρ_ε) = diag(1−x, xε, (x/2)(1−ε), (x/2)(1−ε))`, not only `e_ε`: the entry `xε` is exactly
  what makes the environment output faithful for `ε>0`, i.e. what licenses the lemma, and it is also
  what fails at `ε=0` — so it belongs in the proof, not off-stage.
- **m2 — "any fixed small `ε>0` already gives a strict violation" is unquantified and
  non-uniform in `x`.** The exact condition is `ε < ε_c(x) = 2(1−2x)/(2−3x)`, and `ε_c → 0` as
  `x → 1/2⁻`; a *single* fixed `ε` is **not** uniformly valid — e.g. `ε = 1/10` witnesses violation
  only for `x < (2−2ε)/(4−3ε) = 0.4865…`. The sentence is true on the intended reading ("for each
  `x`, all sufficiently small `ε`") but invites the false uniform reading. Recommend displaying
  `ε_c(x)`, or `ε = ε_c/2` with the one-line certificate
  `gap(ε_c/2) = −(1−2x)(2−3x)/(1−x) < 0` on `(0,1/2)`. This is already verified in the P6b layer and
  costs the paper two lines; it also removes any residual limit-interchange question by exhibiting a
  finite-`ε` violation explicitly. (The `ε→0` route is complete on its own, which is why this is a
  minor.)
- **m3 — the witness is index-convention-fragile; make the convention local.** The proof works only
  because `X` couples the **degenerate** pair of `ρ_ε`, which requires the 0-based reading of
  `X = (|1⟩⟨2|+|2⟩⟨1|)/√2` against `ρ_ε = diag(1−2ε,ε,ε)`. Under a 1-based reading, `X` couples
  `a_ε` and `b_ε`, `g_B` becomes a log divided difference, and `g_E` **diverges** as `ε→0` (the
  environment pair is then `{xε, (x/2)(1−ε)}`) — no violation is obtained at all. The convention is
  declared globally ("Indices run over `{0,1,2}`", Notation), so the statement is correct; but
  Theorem 5.2 should say "`X` couples the two degenerate eigendirections of `ρ_ε`". The authored
  script independently flags the same sensitivity, and its flag is correct.
- **m4 — `⪰_cBKM` is never defined, and `⪰_cRE` only implicitly.** Corollary 5.3's proof leans on
  "cBKM ⟹ the trivial-reference BKM domination used there", and the corollary asserts a cBKM
  equivalence, but the paper defines neither order. `⪰_cRE` is defined only inside a proof (§4,
  lines 406–409). Rule-7g resolvability: promote both to numbered definitions in §2, or cite the
  precise definition in ZW/HRSF22/BGSW. (Under the standard definition the parenthetical is
  immediate, so this is expository — but as printed the reader cannot check it.)
- **m5 — the second-order RE expansion is used with no citation, and §7 overclaims about it.**
  Lemma 5.1's proof says "the standard second-order expansion of Umegaki relative entropy gives …"
  with no reference. It is standard and I verified it at seven configurations, but a referee will ask
  for a citation (Kubo–Mori/BKM metric as the Hessian of relative entropy; monotone-metrics
  literature). Relatedly, §7's blanket claim that "every displayed identity in
  Sections 3–5 is finite and checkable by hand or by a few lines of computer algebra" does **not**
  cover this analytic limit statement; §7 should exempt it (or, better, cite it).
- **m6 — Remark 5.4's causal language outruns what is verified.** Verified: the two scalar functions
  agree exactly, and both objects sit in the spin-2 sector. Not verified: that the BKM gap *is* the
  defect Choi's spin-2 branch. Also, "equals exactly `λ_5(x)/2`" is normalization-dependent — it
  requires `‖X‖_HS = 1`, which is never stated. Recommend stating the normalization and either
  softening the causal phrasing or supplying the sector-level derivation.
- **m7 — precision hygiene in the reviewed verification layer.**
  `tools/whgap_p6b_v1_witness.py`'s numeric integral cross-check sets `mp.mp.dps = 40` but feeds the
  integrand through `float(...)` and `sp.matrix2numpy(..., dtype=float)`, so its inputs are double
  precision; the 25-digit output strings and the reported `~1e-16 / 1e-17` relative errors sit at the
  double floor rather than at 40 digits. The check is still decisive at VALUE level, so this is
  cosmetic, but the reported precision is overstated. (Same trap in my own first draft; after fixing
  it my equivalent check reaches `<1e-45`.) `whgap_p6b_v1_bridge.py` is clean on this point.
- **m8 — adjacent (outside §5, reported for the record): the abstract and the §6 phase table
  overclaim antidegradability.** The abstract says "antidegradability, which holds exactly for
  `x ≥ 4/7`", and the §6 table asserts "`Λ_x` antidegradable: **no**" on `[1/2,4/7)`. But §1
  (lines 155–158) and §6 (lines 596–599) both state that `4/7` is only *numerically* tight to
  `10^{-6}` and that non-antidegradability throughout the window is **open**; the node record has P1
  at CERTIFIED\* with narrow scope and "exact boundary GAP". Reconcile — the two-threshold phase
  diagram should carry the numerical caveat wherever it asserts the `4/7` edge or the "no" on
  `[1/2,4/7)`.

## 7. What the reviewed layer got right (recorded so it is not re-litigated)

The paper's §5 is short and correct, and the P6b V1 layer is a genuinely good verification: it uses
positive-symbol Kraus prefactors to defeat the `conjugate(√(1−x))` trap and documents why; it derives
the divided differences from the integral representation rather than assuming them; it reports the
1-based convention sensitivity unprompted; it supplies a *symbolic* strictness certificate over the
whole interval `(0,1/2)` rather than a grid of samples; it includes calibration anchors at and above
`1/2` where the gap must be positive; and `v1_bridge.py` tests the second-order expansion with
**generic non-diagonal** `σ` (3 seeds × 2 `x` × both channels, `a t²+b t³+c t⁴` fit, 10-digit match)
while stating honestly that the general lemma is prose and not verified there. Provenance is intact:
`sha256sum -c artifacts/logs_whgap_p6b_20260729/SHA256SUMS.txt` passes on all 13 entries, and
`v1_witness.json` / `v1_bridge.json` both record `status: PASS`. The paper compiles clean
(`main.log` has no errors; §5 is Lemma 5.1 / Theorem 5.2 / Corollary 5.3 / Remark 5.4 on pp. 7–8, and
`main.pdf` is newer than `main.tex`).

## 8. Verdict — R5b licensing menu, option (A)

**(A) LICENSE.** Stated in the logically correct direction (the commission menu's "necessary for
`⪰_cBKM`, hence for `⪰_cRE`" inverts the implication, since `⪰_cBKM` is the stronger order; the
paper itself has it right, and I license the paper's version):

> **Theorem (necessity) — PROVED.** For every `x ∈ (0, 1/2)` the domination `Λ_x^c ⪰_cRE Λ_x` fails,
> already with trivial reference; hence so does the stronger `Λ_x^c ⪰_cBKM Λ_x`. Equivalently,
> `x ≥ 1/2` is **necessary** for `Λ_x^c ⪰_cRE Λ_x` and for `Λ_x^c ⪰_cBKM Λ_x`. Written proof in
> paper §5; exact-verification layer (P6b V1) PASS; **independently re-derived in this review** in a
> reviewer-authored script with its own basis order, its own complement assembly, two independent
> BKM routes, and a from-scratch finite-difference verification of the second-order engine
> (57 gates, 0 failures).
>
> **Corollary (exact phase classification) — PROVED given frozen P2/P4.** On this family, for
> `x ∈ (0,1]` (with `x=1` in the minimal self-complementary representation),
> `Λ_x^c ⪰_cBKM Λ_x ⟺ Λ_x^c ⪰_cRE Λ_x ⟺ ∃` signed-lift CP-defect certificate for
> `(Λ_x, Λ_x^c) ⟺ x ∈ [1/2,1]`. In particular the necessity theorem upgrades
> Proposition `prop:unique` from "no member of the covariant five-parameter ansatz" to "**no**
> signed-lift CP-defect certificate whatsoever" below `x = 1/2`.
>
> **Scope limits attached to this licensing.** (i) The second-order relative-entropy expansion that
> drives Lemma 5.1 is granted as a standard result: verified here at VALUE level at seven
> configurations with the correct remainder decay law, but not proved and, in the paper, not cited
> (m5). (ii) Lemma 5.1 as *displayed* omits the output-faithfulness hypothesis and is ill-typed
> without it (m1); the licensing covers the lemma **as applied**, where both outputs are faithful for
> `ε>0` and this is verified. (iii) `λ_5 = 4(1−x)(2x−1)/x` with multiplicity 5 is confirmed here at
> VALUE level at `x = 2/5` and `x = 3/5` by an independent rebuild of the `27×27` defect Choi; its
> closed-form charpoly as an identity in `x` remains frozen P2 scope. (iv) Remark 5.4's *structural*
> reading (that the BKM gap **is** the defect Choi's spin-2 branch) is **not** licensed — only the
> exact numerical identity `gap = λ_5/2` at `‖X‖_HS = 1` and the shared spin-2 placement (m6).
> (v) Nothing here licenses any claim about `Q(Λ_x)` for `x < 1/2`; the paper correctly leaves that
> open. (vi) The independence required by rule 6 is carried by **this** review, not by the P6b layer,
> which was executed by the proposer (disclosed in the P6b artifact).
>
> The eight minors m1–m8 are recommendations for paper v4 and do **not** gate this licensing; m1
> (missing hypothesis) and m2 (unquantified `ε`) should be treated as must-fix before submission.

## 9. Provenance

| File | Role | SHA-256 |
|---|---|---|
| `tools/whgap_r5b_indep_necessity.py` | reviewer's independent script, 57 gates, exit 0 | `8fd22bb86d0cf7984acc88d37d784ab45402f3b28ff636a36fc179eab1b56a94` |
| `artifacts/logs_whgap_r5_20260729/r5b_indep.json` | machine record of all 57 gates | `236cccba3210ec8b0293d5ee8e410ce0331a79da1debdaa784b9f7f142ee0cbb` |
| `artifacts/logs_whgap_r5_20260729/r5b_indep.log` | console log | `b17dc038d571e18033747a496d8cc78b73a1d9f2883db72636502e081dfdbc2c` |
| `artifacts/logs_whgap_r5_20260729/SHA256SUMS_r5b.txt` | LF manifest, `sha256sum -c` passes | — |

Command: `C:<home>/cpython3119/python.exe tools/whgap_r5b_indep_necessity.py artifacts/logs_whgap_r5_20260729/r5b_indep.json`
→ `57 gates, 0 failures`, exit 0.

Reviewed inputs (read, unmodified; hashes verified against the frozen P6b manifest):
`channel-capacity/werner-holevo-gap/paper/main.tex` §5 (lines 473–565) plus §2 (160–223), §4
(384–471), §6 (567–613), §7 (615–631) for context;
`channel-capacity/werner-holevo-gap/proof-dag/nodes/WHGAP.order-boundary.md` (Evidence entry
2026-07-29 late); `artifacts/whgap_p6b_necessity_20260729.md` §V1;
`tools/whgap_p6b_v1_witness.py`; `tools/whgap_p6b_v1_bridge.py`;
`artifacts/logs_whgap_p6b_20260729/{v1_witness.json, v1_bridge.json, SHA256SUMS.txt}`.
Nothing under `artifacts/logs_whgap_p6b_20260729/` was re-run or rewritten (re-running
`whgap_p6b_v1_witness.py` would have overwritten a frozen log).

This report is immutable. Per the commission's binding single-writer deviation, no node file,
`NODE_INDEX.md`, or DAG document was edited by me; the atomic node/index/DAG update citing this
artifact is the decision layer's obligation.

