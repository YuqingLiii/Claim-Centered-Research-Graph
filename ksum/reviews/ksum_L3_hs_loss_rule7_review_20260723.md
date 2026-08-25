# Rule-7 independent review — G1 Hilbert–Schmidt loss quantification (KSUM.B4b.L3 HS-query-energy-law)

**Reviewer:** fresh Opus 4.8 instance; did NOT author the G1 work product; not told the wanted verdict.
**Date:** 2026-07-23
**Target node:** `KSUM.B4b.L3.ALT.hidden-frequency-mask.critical-endpoint.ALT.hs-query-energy-law`
**Work product under review:** `ksum/artifacts/ksum_L3_hs_loss_quantification_20260723.md` +
`ksum_L3_hs_loss_quantification_20260723_compute.py` + `logs_.../run.log` + `.sha256` ledger.
**This review writes NO node status and edits NO existing file.** Per the commission, a *confirming*
review may later license REFUTED/DEAD on the node; a *refuting* one would block it. I report the
mathematics.

---

## 0. Provenance checks (mandatory)

- **SHA-256 ledger vs disk:** MATCH for all three files
  (`.md` `032910cf…`, `.py` `061469941e…`, `run.log` `bc9e1eb1…`). Recomputed with `sha256sum`.
- **Script reproduces its log:** `diff <(python …compute.py) run.log` → **byte-for-byte identical**.
- **Script is a genuine computation, not printed literals (rule 1):** `hook_dim()` implements the
  hook-length formula and is exercised; the disk values are compared to it at runtime
  (`match=True`). No hardcoded dimension is emitted as a "result".

## 1. Anchoring discipline followed (7c)

Sequence actually executed: (1) read `DAG_PROTOCOL.md`, the target node, `KSUM.B4b.retarget.yaml`,
and the `literal-marked-query-polar-norm-interface` node; (2) opened the G1 artifact only for its
scope + frozen-inputs table (F1–F14) + type definitions, **not** its derivation; (3) derived the
conversion inequality, the Schur/isotypic energy identity, the carrier-multiplicity loss floor, the
`Δ_i` equivariance typing, the hook dimensions (two independent methods), and the budget values
**myself**; (4) only then read §(c)–(g) and compared. Where my derivation coincided with the
proposer's (the Schur energy identity, the `op ≥ HS/√rank` direction) it is genuine independent
agreement, not reproduction — my hook-dimension route (determinant formula) is *algebraically
distinct* from the proposer's hook-length product, and both agree.

## 2. My independent derivation (before reading §c)

Adversary bound (F12): `Adv± = max_Γ ‖Γ‖_op / max_i ‖Γ∘Δ_i‖_op`; want numerator large, denominator ≤1.

**(a) Conversion inequality.** For any matrix `M` of rank `r`: `‖M‖_op ≤ ‖M‖_HS ≤ √r·‖M‖_op`, i.e.
`‖M‖_op ≥ ‖M‖_HS/√r`, equality iff flat spectrum. Verified on 20 000 random matrices
(worst `(HS/√r)/op = 1.0000 ≤ 1`), flat case tight.

**(b) Equivariant energy identity (Schur).** With `G = S_n^L×S_n^R×S_q`, an equivariant `Γ`
decomposes as `Γ = ⊕_ρ I_{f^λ f^μ f^ν} ⊗ Γ_ρ`, `ρ=(λ,μ,ν)`. Then `‖Γ‖_op = max_ρ‖Γ_ρ‖_op`,
`‖Γ‖²_HS = Σ_ρ (f^λ f^μ f^ν)‖Γ_ρ‖²_HS`, `rank Γ = Σ_ρ (f^λ f^μ f^ν)·rank(Γ_ρ)`. (Because for
`A = I_D⊗B`, `tr A*A = D·tr B*B`.) I derived this before reading §(b); it matches the artifact.

**(c) Carrier-multiplicity loss floor — the real mechanism.** For *any* spectrum,
`‖Γ‖²_HS ≥ f^{ρ*}·‖Γ_{ρ*}‖²_HS ≥ f^{ρ*}·‖Γ‖²_op` where `ρ*` achieves the op-norm. Hence
`‖Γ‖_HS/‖Γ‖_op ≥ √(f^{ρ*})`. This is a genuine **lower bound on the HS/op ratio driven purely by
the Schur carrier multiplicity** — it does *not* require flatness (flatness only makes it tight).
So a route that certifies the numerator through `‖Γ‖_HS` and needs `‖Γ‖_op` loses `≥ √(carrier)`.

**(d) `Δ_i` typing, derived from its definition** `(Δ_i)_{x,y}=1[x_i≠y_i]`:
- Alphabet `g∈S_q`: `(Δ_i)_{g·x,g·y}=1[g(x_i)≠g(y_i)]=1[x_i≠y_i]` ⇒ `Δ_i` commutes with `S_q` ⇒ the
  `ν`-block index is preserved (`f^ν` common to numerator and every masked query).
- Position `π∈S_n^L`: `(Δ_i)_{π·x,π·y}=(Δ_{π^{-1}i})_{x,y}` ⇒ `Δ_i` is fixed only by `Stab(i)=S_{n-1}`
  ⇒ a left query branches `λ→λ⁻⊢n−1`; `f^λ` is **not** preserved. Same for the right side/`μ`.
This is exactly D2, confirmed from first principles.

**(e) Floor and budget.** `L=√rank ≥ √(f^{λ*}f^{μ*}f^{ν*})`; grant the (favourable) `f^ν`
cancellation ⇒ `≥ √(f^{λ*}f^{μ*})`; most-favourable block (one nontrivial position side, minimal)
⇒ `≥ √(n−1)`. With `n−1=Θ(q^{3/2})` this is `Θ(q^{3/4})`. Budget `q^{1/12}=64^{1/12}=1.4142`.
Margin ≈ 12× at the finite point, growing asymptotically.

## 3. Regime-complete identity gates (7b)

Scripts (mine): `ksum_L3_hs_loss_rule7_review_20260723_hookdims.py`
(SHA-256 `b44f7e62…`, log `3d94105b…`) and `…_detcheck.py`
(SHA-256 `af18cc42…`, log `2b012c03…`); command `python <script>`.

- **Hook dimensions, TWO independent methods** (hook-length product AND Frobenius/Aitken
  determinant with exact fractions), plus textbook anchors `f^(3,2)=5, f^(4,2)=9, …`:
  `f^(283,4,1)=62,660,742,144` ✔, `f^(62,2)=1952` ✔, `f^(61,3)=39,648` ✔,
  `f^(61,2,1)=79,360` ✔, `f^(287,1)=287` ✔. **All EXACT, both methods.**
- **`a=16,q=64` evaluations recomputed:** reviewed carrier `√f^(283,4,1)=250 321.3 = q^{2.989}` ✔;
  most-favourable `√287 = 16.9411 = q^{0.6804}`.
- **Second parameter point (7b, growth law):** holding the finite constant `c=n/q^{3/2}=0.5625`,
  at `q=64/256/1024` the exponent of `√(n−1)` is `0.680/0.698/0.709` → **converges to 3/4 from
  below**, and the reviewed-carrier exponent rises `2.99/3.18/3.30`. Confirms the asymptotic
  `α=3/4` (one side) / higher (reviewed), and that finite-`q` exponents are *below* `3/4`.
- **Sign-representation Kostka gate** (for §5, D4): multiplicity of `S^{(1^n)}` in permutation
  module `M^μ` is `0` unless `μ=(1^n)`. Verified for `n=5` across all `μ`.

## 4. Type audit (7a) — verdict PASS on the displayed identities

| Displayed object | domain → codomain, dims (all parameters) | well-typed? |
|---|---|---|
| `Γ` | `ℂ[X_0]→ℂ[X_1]`, `dim X_t=|G|/|K_t|`, `G=S_n^L×S_n^R×S_q` | yes |
| `Γ=⊕_ρ I_{f^λf^μf^ν}⊗Γ_ρ` | carrier `f^λf^μf^ν`, mult `Γ_ρ: M_0(ρ)→M_1(ρ)` | yes (Schur) |
| `‖Γ‖_op=max_ρ‖Γ_ρ‖_op` | carrier norm-invisible | yes |
| `‖Γ‖²_HS=Σ_ρ f^λf^μf^ν‖Γ_ρ‖²_HS` | `tr I_{D_ρ}=D_ρ` | yes |
| `Δ_i` (Hadamard mask) | `{0,1}^{X_1×X_0}`, `S_q`-fixed, `Stab(i)=S_{n-1}` | yes |
| `‖Γ∘Δ_i‖²_HS=Σ_τ f^{λ⁻}f^μf^ν‖·‖²_HS`, `τ=(λ⁻,μ,ν)` | left query `λ→λ⁻⊢n−1` | yes |

Every displayed map is well defined and the dimensions carry the correct carrier weights.
**Multiplicity > 1 check:** the `f^ν` *cancellation* between numerator and mask is **granted, not
proven**, and at multiplicity > 1 need not hold cleanly (the `ν`-block multiplicity operators on
numerator and mask differ). This does **not** damage the verdict because granting cancellation only
*shrinks* `L`; the kill survives the most-favourable grant. (It would be a genuine gap if the goal
were to prove the route *works*.)

## 5. Per-claim verdicts, scopes, value-vs-formula (7f)

**D1 — conversion direction/normalization, `L=√rank`. → PASS.**
Scope: the algebraic direction of the HS↔op conversion as used in eq. (★). *Established by my own
derivation* (§2a,c), not the proposer's code. The artifact applies `op ≥ HS/√rank` to the
**numerator** and the free `op ≤ HS` to the **denominator** (eq. (★), §c.1) — the correct
directions; normalization `D_ρ=f^λf^μf^ν` is right. Note the commission's phrase "adversary-
*denominator* role" is loose: the `√rank` loss actually sits on the **numerator**; the artifact's
placement is nonetheless correct. `L=√rank` is the honest loss of an energy-only route (§2c gives
the matching carrier-multiplicity floor, so it is a real lower bound, not merely a flat-spectrum
worst case).

**D2 — `Δ_i` alphabet-equivariant / position-localizing; carriers survive. → PASS.**
Scope: the equivariance/branching typing and which carriers cancel. *Established by my own
computation from the definition of `Δ_i`* (§2d). Alphabet `f^ν` common; position `f^λ→f^{λ⁻}` broken.
Full type audit in §4. Caveat carried from §4: the `f^ν` cancellation is a favourable grant.

**D3 — floor `f^λ,f^μ ≥ n−1=Θ(q^{3/2})`; `a=16,q=64` hook values. → PASS (hook identities exact;
one MINOR display defect).**
Scope: the hook-dimension identities and the numeric floor. *Established by two independent
constructions of mine* (hook-length + determinant), which also agree with the proposer's formula.
`f^(283,4,1)=62,660,742,144` and parents `1952/39648/79360` are **exact and double-verified**;
reviewed-carrier `L≈2.5e5=q^{2.99}` ✔. **MINOR defect:** the claim writes the most-favourable value
as "`≈16.9 = q^{0.667}`", which is internally inconsistent — `√287=16.94=q^{0.680}`, whereas
`q^{0.667}=16.00`. Root cause: `compute.py:86` uses `isqrt(287)=16` (integer floor) instead of
`√287`. The error is *conservative* for a kill (it understates `L`) and cosmetic; the floor claim
`f^λ ≥ n−1` and the verdict are unaffected. Recommended fix: `math.sqrt`, relabel `q^{0.680}`.

**D4 — position-trivial adversaries capped at `Θ(N^{1/3})`, so the loss is "unavoidable". → MINOR.**
Scope: the F10 cap and its use to force non-trivial position content. The cap value `2√a=Θ(N^{1/3})`
is correctly cited (F10, frozen) and correctly scaled (`√a=√Θ(N^{2/3})=Θ(N^{1/3})`, far below the
`N^{11/18}` baseline); the trivial-case logic is valid. **Gap:** "unavoidable" and "any adequate
adversary occupies a block with nontrivial position content, `f^{λ*}≥n−1`" require ruling out **all**
1-dimensional position carriers, but F10 as cited rules out only the **trivial** rep `(n)`. The
**sign** rep `(1^n)` is also 1-dimensional and nontrivial and is *not* addressed on disk; a query
does not raise its dimension either. I verified the standard repair the artifact omitted: by Young's
rule the sign irrep occurs in a permutation module `M^μ` only when `μ=(1^n)` (Kostka gate, §3), so
it is absent whenever any two positions are interchangeable — hence the minimal nontrivial irrep
*that actually appears* is `(n−1,1)`, dim `n−1`. The conclusion therefore holds, but via an argument
the artifact does not make; §(g).2 only partially concedes this. Value-level use of frozen F10; I did
not re-derive F10 itself.

**D5 — OUT-OF-BUDGET, `α≥3/4` (`≥2` pure energy) vs `1/12`; secondary findings. → PASS.**
Scope: the budget comparison, the growth exponents, and the direction of the two on-disk gaps.
*Established by my own budget/exponent arithmetic* (§2e, §3). Quantifier structure (7g): for **all**
equivariant adversaries reaching `‖Γ‖=Ω(N^{2/3})` (which forces non-linear position content, §5·D4),
the energy-route certified loss is `L=√rank ≥ √(n−1)=Θ(q^{3/4})`, uniformly in `N` along
`q=Θ(N^{2/3})`; "one broken side" = the most-favourable (smallest-`L`) block, so `α≥3/4` is a valid
universal floor. `α≥2` for the crude no-cancellation reading `√(f^λf^μf^ν)_min=√(q^{3/2}·q^{3/2}·q)`.
Every reading ≫ `q^{1/12}=1.41`. **Direction of the gaps (checked as instructed):** F4 literal `1` >
suppressed `1/2`; F5 literal `‖Δ(B)‖²=1/2` > compressed `‖B−E(B)‖²=1/4` — in both, the literal object
is the *larger*-normed one, so replacing compressed by literal **adds** loss. Sign/direction of "the
gaps can only ADD loss" is **correct**. Secondary "literal HS identity absent from disk" is
corroborated by F6 (literal defect BLOCKED) and honestly flagged as not changing the outcome.

## 6. Frozen-input immunity (7d) and standing failure modes (7e)

- **7d.** F3 (hook dims) and F1 (energy identity) are *re-derived independently here*, not leaned on.
  F10 (position cap) is used at value level; I re-opened the aspect its citation does **not** cover —
  1-dimensional-but-nontrivial (sign) position content — and found it repairable (§5·D4). F4/F5 are
  `d=2` toys: they rigorously fix the *sign* of the two gaps (used correctly); the artifact's further
  remark that the gaps *scale* with carrier dimension (l.181–182) is an extrapolation beyond the toy
  and is **not** independently verified — but it is **not load-bearing** (the `√rank` position loss
  alone is out of budget). The 2026-07-22 compressed-model chain is thus used only for the gap
  *direction*, which its content supports.
- **7e standing list.** Dropped/extra normalizations: none (carrier weight `D_ρ` correct). Type
  mismatches: none in the displayed identities. Undefined terms / missing ranges: "flat-spectrum
  conversion" is a mild misnomer — the operative bound is a carrier-multiplicity floor that holds
  regardless of flatness (noted); "position-trivial" silently means the *trivial* rep only, not all
  1-dim content (the D4 gap). Colored-orbit vs full-central sums: the energy identity sums over the
  full central label set `ρ=(λ,μ,ν)` (F7), not a colored sub-sum — OK. Numerics-mask-broken-
  derivation: the derivation is analytic and independently reproduced; the only numeric slip
  (`isqrt`) is cosmetic and conservative.

## 7. Overall verdict

**CONFIRMING — PASS with two MINOR repairs.** The review meets the rule-7 standard (7a type audit,
7b regime-complete double-method identity gates + a second parameter point, 7c anchoring, 7d frozen
re-opening, 7e failure-mode sweep, 7f value-vs-formula per claim, 7g quantifier hygiene). The G1
**OUT-OF-BUDGET** verdict for the Hilbert–Schmidt-energy route is **mathematically supported**: the
`√rank` loss is a genuine carrier-multiplicity lower bound (not a worst-case artefact), the hook
dimensions are exact, the `Δ_i` equivariance/branching typing is correct, and the floor
`L≥√(n−1)=Θ(q^{3/4})` exceeds the `q^{1/12}` budget by ≈12× at the finite point and by a growing
exponent gap asymptotically. The kill is correctly **scoped to this route** (energy-only): the
sibling operator-norm/polar route is explicitly preserved, so this respects rule 3 (no over-kill) and
supports REFUTED/DEAD **on this node** rather than a universal obstruction.

Per-claim: **D1 PASS · D2 PASS · D3 PASS (one MINOR display defect) · D4 MINOR · D5 PASS.**

Required repairs (do not threaten the verdict; should be recorded on the node before REFUTED/DEAD):
1. Replace `isqrt` by `math.sqrt`; relabel the most-favourable finite value `16.94 = q^{0.680}`
   (not `q^{0.667}`).
2. Close the `f^λ=1` case honestly: state the Young's-rule fact (sign rep `S^{(1^n)}` absent from any
   permutation module with an interchangeable pair) so that "position-trivial ⇒ capped" upgrades to
   "*every* 1-dimensional position carrier is trivial-or-absent", rather than leaning on F10's
   trivial-rep cap alone.

## 8. Reproducibility of this review

- `ksum/artifacts/ksum_L3_hs_loss_rule7_review_20260723_hookdims.py` — SHA-256 `b44f7e62a726786bbcdad4981606952d87d6ccef735f790f3691497d88426782`; log `logs_ksum_L3_hs_loss_rule7_review_20260723/hookdims.log` (`3d94105b9fe1d9bd99a647eeba8adebfa52b116421b9640d20d75d0850ab2e3c`).
- `ksum/artifacts/ksum_L3_hs_loss_rule7_review_20260723_detcheck.py` — SHA-256 `af18cc420094559e8c48af1b7aef61a918e2786da7c3dce9cae3db7d047e6ed8`; log `logs_.../detcheck.log` (`2b012c035b0a05a83dd3883df97591932dd5375f71c16770cb0ef63c9689d757`).
- Command: `python <script>` (Python 3.12; exact big-int + `fractions`; determinant method uses no external libs).
- Proposer artifacts verified against ledger `ksum_L3_hs_loss_quantification_20260723.sha256` (all MATCH); `compute.py` reproduces `run.log` byte-for-byte.
