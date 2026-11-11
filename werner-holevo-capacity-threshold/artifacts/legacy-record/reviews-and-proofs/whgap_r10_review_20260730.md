# R10 — independent review of WHGAP P16-A (Track B, direction-restricted order)

Reviewed note: `channel-capacity/werner-holevo-gap/notes/WHGAP_P16A_DIRECTION_20260730.md`
Node: `WHGAP.direction-restricted-order` (P16). Commission:
`channel-capacity/werner-holevo-gap/notes/WHGAP_COMMISSION_P15A_P16A_20260730.md`, R10 section.
Reviewer artifacts: `tools/whgap_r10_{isotypic,cone,cone2,boundary,witness}.py`,
`artifacts/logs_whgap_r10_20260730/` (`SHA256SUMS_r10.txt`, LF, verified 11/11 with
`sha256sum -c`).

**VERDICT: FINDINGS — 2 MAJOR, 5 minor.**
Menu option R10-(A) cannot be licensed *as written*: the note's B2 verdict is wrong for
its own candidate D4, and one of §3's stated numerical results is false. The note's **final
B4 recommendation (P16 DEAD for the isotypic class) is nevertheless independently
confirmed and strengthened** — see §6 for the exact wording I can support.

---

## 0. PRE-ACTION REPORT

Files read from disk, in the order prescribed by `research/PRETASK_RELOAD_PROMPT.md`:
`research/DAG_PROTOCOL.md`; `research/RESEARCH_STRUCTURE_PROTOCOL.md`;
`channel-capacity/werner-holevo-gap/README.md`;
`channel-capacity/werner-holevo-gap/proof-dag/NODE_INDEX.md`;
`proof-dag/nodes/WHGAP.direction-restricted-order.md` (target) and its parent
`WHGAP.goal` / related `WHGAP.restricted-order`; §§1–3 of
`notes/WHGAP_REVIEW_COMMISSION_R5_20260729.md`; the MAJOR-1 section of
`artifacts/whgap_r8_review_20260730.md`; then the reviewed note and the executor's logs
`artifacts/logs_whgap_p16a_20260730/` and scripts `tools/whgap_p16a_*.py`.

- **Target node and status as read from disk:** `WHGAP.direction-restricted-order`
  (alias P16), kind LEAF, role proof, **status OPEN**, `disposition: null`
  (front matter `status: OPEN`; NODE_INDEX row `P16 | … | OPEN`). Open obligation:
  *"Settle design question 1 (is the restriction stable under references and tensoring?).
  If NO, this node closes as DEAD with that reason…"*.
- **ROLE: reviewer.** I am a fresh instance. I did not author the reviewed note, any
  P16-A script, or any prior WHGAP work. **I was given no desired outcome**; the
  commission's decision-layer prediction ("the class dies at B2") was handed to me as
  untrusted input, and the licensing menu was presented as alternatives.
- **Highest status my evidence could license (§2 ladder):** a COMPLETED rule-7 review is
  the gate that lets the **decision layer** write a completion tier (here **REFUTED +
  DEAD**) on P16, citing this report. I write no node status myself (rule 2; rule 6).
  My own new numerical results (the x = 0.46 certificate) are reviewer-authored and are
  themselves NUMERICAL/pending-review evidence — they do not license anything on their own
  beyond withdrawing support from the note's contrary claim.
- **Gates and deliverables (one line each):** redo the spin-2 isotypic decomposition
  independently with my own projectors, my own O(3) action convention, verified against a
  character/dimension count; audit whether each candidate definition is precise enough to
  be an order at all; audit the B2 verdict for over-claim (a DEAD verdict must name which
  definitions it covers and must not be generalised to all conceivable direction
  restrictions); audit B3; write this report; pick one menu option or FINDINGS.
- **Conflicts between commission text and disk protocols:** none on rules. Two notes:
  (i) the single-writer deviation (no node/NODE_INDEX/DAG edits) is commissioned in the R5
  commission and re-stated in my dispatch, so this report is an orphaned artifact until the
  decision layer performs the atomic node update — flagged so it cannot be forgotten;
  (ii) the commission's B2 text tells the executor to "record it with that reason [DEAD]",
  which rules 2/6 forbid an author from doing; the reviewed note reconciled this correctly
  in its own PRE-ACTION REPORT and I concur with its reading.

---

## 1. Independent rebuild — the spin-2 isotypic decomposition (7c: own path first)

I built everything from the frozen §1 conventions before comparing with any number in the
note. Log `r10_isotypic.json`.

**Own action convention.** `Λ_x(Y) = (1−x)Y + (x/2)(Tr Y·1 − Y^T)`; for real `O`,
`(O Y O^T)^T = O Y^T O^T` and `Tr` is invariant, so `Λ_x(O Y O^T) = O Λ_x(Y) O^T`. Verified
at 40 random `O` (20 with `det O = +1`, 20 with `det O = −1`), max error **1.1e−15**. Since
`O` is real, `O^T = O^†`, so the "transpose" and "adjoint" readings of the action coincide
here — there is no convention fork to get wrong, contrary to what one might fear from
standing failure mode 4.

**`B(A)` as an `O(3)`-representation.** `B(A) ≅ V ⊗ V^*` with `V = C^3` the (self-dual)
standard representation; `−I` acts trivially (verified exactly: `Rho(−I) = id`, error 0),
so the action factors through `SO(3)` and the `O(3)`- and `SO(3)`-isotypic decompositions
coincide. This confirms the note's §0 claim by my own route.

**Three independent constructions of `P_2`, not two.**
1. closed form `P_2(M) = (M+M^T)/2 − (Tr M/3)·1`;
2. Casimir `Ĉ = −Σ_μ ad_{A_μ}²` (the infinitesimal action of `M ↦ OMO^T` at `O = exp(tL)`,
   `L ∈ so(3)`, is `M ↦ [L,M]`); observed spectrum **{0, 2, 6} with multiplicities
   (1, 3, 5)** = `J(J+1)` for `J = 0,1,2`; spectral projector at 6;
3. **group averaging** `P_2 = 5·E_{O∼Haar(SO(3))}[ χ_2(O)·Rho(O) ]` with
   `χ_2(O) = 1 + 2cos φ + 2cos 2φ`, 4·10⁴ samples.

Agreement: closed form vs Casimir **1.7e−16**; closed form vs group average **1.7e−2**
(Monte-Carlo, consistent with the `O(N^{-1/2})` rate). `Tr P_0 = 1`, `Tr P_1 = 3`,
`Tr P_2 = 5`; `P_0+P_1+P_2 = id` exactly; idempotent to 1.1e−16; self-adjoint exactly;
equivariant to 1.0e−15 for both `det O = ±1`.

**Character/dimension count (commission requirement).** For a rotation by `φ`,
`χ_{B(A)}(O) = χ_V(O)² = (1+2cos φ)²`, and
`χ_0 + χ_1 + χ_2 = 1 + (1+2cos φ) + (1+2cos φ+2cos 2φ) = 3 + 4cos φ + 2cos 2φ`. The two
agree identically, and both agree with the numerically computed `Tr Rho(O)` at 30 random
rotations, max error **1.8e−15**. Dimensions `1 + 3 + 5 = 9` ✓.

**Consequences I verified for the reviewed claims.**
- The R5b necessity direction `X = (E_ij + E_ji)/√2` has spin-2 fraction **exactly 1.000**
  for all three placements `(i,j) ∈ {(1,2),(2,3),(1,3)}`. The note's "independent
  confirmation of R5b claim 5" is correct.
- `dim{Z : Z = Z†, Tr Z = 0, Π_2 Z = 0}` = **3** at `d_R = 1` and **15** at `d_R = 2`
  (the note's "15 exact basis elements"), the spin-2-free Hermitian directions on `A` being
  exactly `i·so(3)`.

**My BKM implementation, validated independently of the note.** `g_θ(Z)` computed from the
divided differences `c(λ_i,λ_j)` agrees with second-order finite differences of the
relative entropy, `(D(θ+tZ‖θ)+D(θ−tZ‖θ))/t²` at `t = 10^{-4}` (matrix logs via
`scipy.linalg.logm`), to relative error **6e−8 … 1.5e−7** at 4 random faithful `(θ,Z)` —
i.e. my BKM code computes the Hessian of the relative entropy, which is what the whole
cBKM chain means. **G-cal reproduced independently:** my table of `q` at `ρ_ε`, `X`, for
`x ∈ {0.2, 0.4, 0.45, 0.49, 0.5, 0.55, 0.7}` and `ε ∈ {10^{-2},…,10^{-5}}` agrees with the
note's §0 table to every printed digit and converges to `2(1−x)(2x−1)/x`. **§0 PASS.**

---

## 2. B1 — are the definitions precise enough to be orders?

**Verdict on B1: yes, all four are well posed; two audit remarks.**

- **D1** (pair class `Π_2(ρ−σ) = 0`, all finite-dimensional `R`) is a precise set of pairs
  plus a precise inequality. **The note never states the (easy, but load-bearing) fact that
  this makes it a preorder**: for any fixed pair class 𝒫, "`N ⪰_𝒫 M` iff
  `D(N(ρ)‖N(σ)) ≥ D(M(ρ)‖M(σ)) ∀(ρ,σ)∈𝒫`" is reflexive and transitive automatically, so
  the node's design question 1 ("is a direction-restricted class even an order?") reduces
  *entirely* to the stability questions the note does treat. Saying so would have closed
  the question cleanly. (minor m1.)
- **D2** (constant cone field `𝒞 = ker Π_2 ∩ {Z=Z†, Tr Z = 0}`) — precise. Calling a linear
  subspace a "cone field" is loose but harmless and the note flags it.
- **Lemma 0 (D1 ⟺ D2)** — I re-derived it. With `h(t) = D(σ+tZ‖σ)` and `Tr Z = 0`,
  `h′(t) = Tr[Z(log(σ+tZ) − log σ)]` and `h″(t) = g_{σ+tZ}(Z)`; Taylor with integral
  remainder gives the displayed representation. The direction along the segment is the
  constant `Z = ρ−σ`, which is in `𝒞` exactly when `(ρ,σ) ∈ 𝒟_1`. Correct. **Gap:**
  "every point of the segment is a state" is not "every point is faithful", and D2 is
  quantified over faithful `θ` only; the CI pairs are precisely the case where both members
  are rank-deficient. The implication survives (restrict to `supp σ` and use lower
  semicontinuity) but the note does not say so. (minor m2.)
- **D3 and Lemma 1** — correct and, in my judgement, the note's best structural
  observation. `{Z : Π_2 Z ≠ Z}` is the complement of a proper subspace, hence dense; `q_θ`
  is a quadratic form, hence continuous; so D3 at any fixed faithful `θ` forces `q_θ ≥ 0`
  everywhere, including at the purely-spin-2 witness `X` where R5b PROVES `q_θ(X) < 0` for
  `x < 1/2`. D3 ≡ unrestricted cBKM, dead. The derived design constraint ("any usable
  direction restriction must exclude a set with non-empty interior") is sound and is the
  kind of statement that should survive this node.
- **D4** — precise given `η`. Note the orientation: **larger `η` is more restrictive**
  (`η = 1` recovers D2); the admissible set is `{fraction ≤ 1−η}`. The note gets this
  orientation wrong once, in the sentence that carries its D4 verdict — see MAJOR 1.

---

## 3. B2 — Theorem B2 is CORRECT; the B2 *verdict* is not (MAJOR 1)

### 3.1 Theorem B2 itself: independently re-derived and confirmed

I re-derived the theorem before running anything. With `ψ = Σ_j √p_j |j⟩_R|u_j⟩_A` and
`Δ = ψ_{RA} − ψ_R ⊗ σ_A = Σ_{jk}|j⟩⟨k| ⊗ M_{jk}`, orthonormality of `{|j⟩⟨k|}` gives
`‖Π_2Δ‖² = Σ_{jk}‖P_2 M_{jk}‖²`. For `j ≠ k`, `M_{jk} = √(p_jp_k)\,u_j u_k^†` is unchanged
by the anchor and traceless, so `P_2 M = (M+M^T)/2` and
`‖P_2M‖² = ¼(‖M‖² + ‖M^T‖² + 2Re Tr(M^†M^T))`; with `Tr(M^†M^T) = |u_j^Tu_k|²` (real,
`≥ 0`) this is `p_jp_k(1+|s_{jk}|²)/2`. Summing and dropping the non-negative diagonal
blocks gives `≥ (1 − Tr ρ_A²)/2`. **The theorem is correct exactly as displayed**, including
the anchor-independence (the `σ_A` freedom only touches the diagonal blocks).

Numerics, own code: the displayed identity holds to **1.0e−15** at 40 samples with
`d_R ∈ {2,3,4}`, half with `σ_A = ρ_A` and half with a Haar-random `σ_A ≠ ρ_A`; the bound
holds in 40/40; the maximally entangled values `‖Π_2Δ‖² = 5/9`, `‖Δ‖² = 8/9`, fraction
`5/8` reproduce to 1e−15. **The note's §2.1 and its "CONFIRMED and sharpened" reading of
the decision-layer prediction are licensed for D1/D2/D3.**

### 3.2 MAJOR 1 — "D4 survives B2" is FALSE; the supremum of the spin-2 fraction over the CI pairs is 1, not 0.72

The note concludes §2.2 with:

> "**D4 survives B2** — the CI directions have spin-2 fraction `≤ 0.72` (`n=1`) and `≤ 0.60`
> (`n=2`) while the necessity witness has fraction exactly `1`, so a cone with `η ≳ 0.3`
> excludes the witness and retains every sampled CI direction. D4 therefore goes to B3."

Three defects, in increasing order of severity.

**(a) The quantifier is inverted.** With admissible set `{fraction ≤ 1−η}`, retaining a CI
direction of fraction 0.716 needs `1−η ≥ 0.716`, i.e. **`η ≤ 0.284`**, not `η ≳ 0.3`. At
`η = 0.3` the note's own worst sampled CI direction is *excluded*.

**(b) The stated range excludes the note's own data.** §2.2 reports the fraction ranging
over `[0.576, 0.716]`. That is the max over the `n1` block of `b2_spin2.json` only; the
`n1_arbitrary_anchor` block — which §2.1 consequence 1 explicitly argues *must* be in scope,
since the CI step admits `σ_A ≠ ρ_A` — contains `anchor05` at **0.8165**. The note's own
log already breaks the sentence that follows from it.

**(c) The decisive one: the supremum is 1.** Take the Schmidt data
`p = (1−δ, δ)`, `u_1 = ψ = (e_1+ie_2)/√2`, `u_2 = ψ̄`. These are orthonormal
(`⟨u_1|u_2⟩ = 0`) yet **maximally "isotropically aligned"** (`|u_1^Tu_2| = 1`). Theorem B2
then gives, as `δ → 0`,
`‖Π_2Δ‖²/‖Δ‖² → (1+|s_{12}|²)/2 = 1`. Measured (log `r10_cone2.json`, marginal anchor
`σ_A = ρ_A`, `d_R = 2`):

| δ | 0.5 | 0.3 | 0.1 | 0.03 | 10⁻² | 10⁻³ | 10⁻⁴ | 10⁻⁶ |
|---|---|---|---|---|---|---|---|---|
| spin-2 fraction | 0.6667 | 0.7042 | 0.8475 | 0.9450 | 0.9806 | 0.9980 | 0.99980 | 0.999998 |

The executor **tested exactly this family and only at `δ = 0.3`**: `b2_spin2.json` row
`S2_isotropic_schmidt_tau0`, purity 0.58 ⟹ `δ = 0.3`, fraction 0.7042 — my value to four
decimals. The near-pure corner, where the fraction runs to 1, was never sampled. (For
contrast, 3000 Haar purifications reach only 0.654: this corner is invisible to random
sampling, which is why a structured family was needed and why one data point of it is not
enough.)

**Consequences.**
1. **For every `η ∈ (0,1]`, D4 excludes CI pairs.** So D4 dies at B2 by exactly the same
   vacuity mechanism as D1/D2 — it does not "survive B2", and it should never have been
   sent to B3 on this ground.
2. The excluded corner is not incidental: `ρ_A = (1−δ)P_ψ + δP_ψ̄` with `ψ` isotropic **is
   the ε-log-ε family that carries the PROVED `Q > 0` mechanism** (R5c weight operator /
   E-N1 lemma, frozen input). A cone restriction that keeps "generic" CI pairs and throws
   away exactly this one is worse than useless: it discards the only inputs known to matter.
3. §5 reason 1 ("Applies to D1, D2 (and to D3 vacuously)") **understates its own reach**:
   corrected, the vacuity kill covers **D1, D2, D3 and D4**. This *strengthens* the DEAD
   verdict and, importantly, makes it independent of the contested §3 numerics.

Severity: MAJOR because a stated verdict on one of the note's four registered definitions is
wrong, and because the load-bearing quantifier ("every sampled CI direction") was silently
substituted for the one the claim needs ("every CI direction"). It does **not** reverse B4.

---

## 4. §3 — MAJOR 2: the "no violation at 0.46–0.49" result is false, and the search had no negative control

### 4.1 What I did

For a fixed base point `θ`, `min_Z q_θ(Z)/‖Z‖²` over a *linear subspace* is an eigenvalue
problem, not a stochastic search. I built an orthonormal basis of (a) the full traceless
Hermitian space and (b) the 15-dimensional spin-2-free subspace at `d_R = 2`, assembled the
matrices of the two BKM forms, and read the smallest eigenvalue of the difference. Every
base point is asserted faithful, and `Λ_R(θ)`, `Λ^c_R(θ)` are checked full rank, so **no
kernel regularisation is used anywhere** (log `r10_cone2.json`; the earlier
`r10_cone.json` is kept append-only but is SUPERSEDED — its base-point list contained the
rank-2 states `(1−e)P_ψ + eP_ψ̄` and its scan block must not be used).

**Value cross-check of the note's falsification anchor:** at `x = 0.2`, trivial reference,
my minimum over the spin-2-free subspace is **−3.140208** at `ρ_{0.1}` and **−5.066491** at
`ρ_{0.01}` — the note's −3.14 / −5.07, to six digits. §3's falsification anchor **PASSES**,
independently.

**Cross-check against a PROVED input:** at `x = 0.49`, trivial reference, my minimum over
*all* directions is **−0.0415772**, converging to the R5b analytic gap
`2(1−x)(2x−1)/x = −0.0416327`. My stack sees the proved unrestricted violation.

### 4.2 The refutation

Minima over the spin-2-free subspace, `d_R = 2`, faithful base points (`r10_cone2.json`):

| x | 0.40 | 0.42 | 0.45 | **0.46** | 0.47 | 0.48 | 0.49 | 0.499 | 0.55 |
|---|---|---|---|---|---|---|---|---|---|
| min `q/‖Z‖²` | −88.0 | −45.5 | −9.69 | **−2.41** | +0.0048 | +0.0062 | +0.0074 | +0.0085 | +0.0140 |

**Certificate at `x = 46/100`** (log `r10_witness.json`, `tools/whgap_r10_witness.py`),
exact on input and evaluated at `mp.mp.dps = 60`:

- base point `θ = (1 − 1/500)|φ⟩⟨φ| + (1/500)·1/6`, `|φ⟩ = (|0⟩|ψ⟩ + |1⟩|ψ̄⟩)/√2`,
  `ψ = (e_1+ie_2)/√2` — **all entries exactly rational**, `min spec θ = 3.333e−4`,
  `min spec Λ_R(θ) = 3.333e−4`, `min spec Λ^c_R(θ) = 1.533e−4` (all faithful,
  well-conditioned — this is **not** a near-singular artifact);
- direction `Z = −0.175422·σ_z ⊗ 1_3 + 0.451487·1_2 ⊗ iA_2`, an exact rational combination
  of Gaussian-integer spin-2-free basis matrices, so `Π_2 Z = 0` **exactly**
  (chart-aware rationalisation: coefficients rationalised *inside* the positive-codimension
  chart, never in the ambient Hermitian space);
- `g_B = 180.007338024844155066036`, `g_E = 177.5990485261302513971447`,
  **`q = g_E − g_B = −2.408289498713903668891301 < 0`**.

So the spin-2-free restricted cBKM condition **FAILS at `x = 0.46`**. This directly refutes
the note's

> "Bounded search finds no violation at `x ∈ {0.46, 0.47, 0.48, 0.49}` (150 random faithful
> `d_R = 2` base points each…)"

and the reading it supports,

> "the spin-2-free restriction buys ground only from `1/2` down to roughly `0.455`; it does
> not reach `2/5`"

which reappears in §5 reason 2 as "At best the restriction reaches down to `≈ 0.455`".
The correct statement from my data is: **it fails at least up to `x = 0.46`**, and the
0.47–0.499 non-negative readings remain bounded searches with no quantifier.

### 4.3 Root cause, and the missing negative control

The note's base points are all `0.85·(Wishart) + 0.15·1/6` (`tools/whgap_p16a_witness.py`
line ~205) — well-mixed states with `min spec ≥ 0.025`. The strip violations live at
*near-pure entangled* base points (my witness has `min spec θ = 3.3e−4`, and the violation
deepens as `s → 0`). The family was structurally blind to the relevant region.

This was diagnosable from the note's own log and was not diagnosed. `b2_refassisted.json`
reports the minimum over **all** directions as `−9.06e−15` at `x = 0.49` and `−4.37e−15` at
`x = 0.55` — numerically the same answer at a point where cBKM domination is PROVED to fail
and at a point where it is PROVED to hold. A statistic that cannot separate those two
regimes cannot support a "no violation" reading anywhere. Under rule 7b this is exactly the
regime-complete gate that was owed: the *unrestricted* minimum is a free negative control at
every `x < 1/2`, and it should have been required to come out negative before any restricted
non-negative result was reported.

Severity: MAJOR — a displayed numerical result is false and a derived quantitative reading
("≈ 0.455") is repeated in the verdict section. It does **not** reverse B4: the note's §3
kill of D1/D2/D4 at `x = 0.42, 0.45` stands (I reproduce far deeper violations there), and
MAJOR 1 makes reason 2 non-load-bearing anyway.

---

## 5. B3 — confirmed

- **(i) Attaching a reference: STABLE.** `Π_2 := id_{B(R)} ⊗ P_2` is uniform in `R`, and
  `‖Π_2(Z⊗ω)‖² = ‖Π_2Z‖²‖ω‖²`. Correct, and correctly identified as the only positive part
  of design question 1.
- **(ii) Tensoring: NOT STABLE.** *Diagonal action*: I built the total-spin-2 projector on
  `B(A⊗A)` from my own Casimir `−Σ_μ ad_{A_μ^{(1)}+A_μ^{(2)}}²` (spectrum `{0,2,6,12,20}`,
  spin-2 isotypic dimension 30) and measured the total-spin-2 fraction of `Z_1⊗Z_2` for
  spin-2-free `Z_i`: **0.500 – 0.666 over 12 samples, never 0**, confirming `1⊗1 ⊃ 2`. My
  distribution differs from the note's quoted `0.17–0.64` (different sampling of the
  4-dimensional spin-2-free space), but the conclusion — never zero — is the same.
  *Per-copy action*: the identity
  `ρ_1⊗ρ_2 − σ_1⊗σ_2 = (ρ_1−σ_1)⊗ρ_2 + σ_1⊗(ρ_2−σ_2)` and
  `Π_2^{(1)}(σ_1⊗Δ_2) = (P_2σ_1)⊗Δ_2 ≠ 0` is correct as written.
- The answer to the node's design question 1 is therefore **NO**, as the note says.

---

## 6. B4 — what I can and cannot license

**I confirm the recommendation `WHGAP.direction-restricted-order` (P16) = DEAD**, for the
class of restrictions defined by the `O(3)`-isotypic type of the difference / tangent
direction — i.e. **for the definitions D1, D2, D3 and D4 as written in the note, and only
for those**. Wording I can support (corrected against the note's §5):

1. **Vacuity w.r.t. the coherent-information step — now covering all four definitions.**
   Theorem B2 (independently re-derived, exact) excludes every entangled purification pair
   from D1/D2/D3 for every product anchor, with the anchor-independent bound
   `‖Π_2(ψ_{RA} − ψ_R⊗σ_A)‖² ≥ (1 − Tr ρ_A²)/2`. **And D4 too:** the spin-2 fraction of the
   CI difference tends to 1 along the near-pure isotropic Schmidt family, so for every
   `η ∈ (0,1]` a D4 cone excludes CI pairs — including exactly the family that carries the
   PROVED `Q > 0` mechanism. (MAJOR 1; this is the correction, and it makes reason 1 alone
   sufficient.)
2. **Falsity below 1/2** — the restricted condition, in its complete reference-assisted
   form, is false at `x = 0.42` and `x = 0.45` (note's witnesses; I reproduce much deeper
   minima) **and at `x = 0.46`** (my exact-input 60-dps certificate). The note's "only down
   to ≈ 0.455" must be struck (MAJOR 2). No claim of non-negativity anywhere in
   `[0.47, 1/2)` is supported by anything better than a bounded search.
3. **Failure of tensor stability** — confirmed in both covariance conventions; the
   induction cannot be started. This answers the node's own design question 1 with NO, which
   is the condition the node itself set for closing DEAD.

**What must NOT be written.** The note's §5 "What this does NOT establish" is accurate and
adequately guarded, and I endorse it verbatim as the scope limit: this is **not** a
statement that no direction-restricted order can work. Any restriction not expressible as a
linear isotypic condition on `ρ−σ` (a base-point-coupled cone field, a restriction on the
anchor rather than the direction, a non-`O(3)`-isotypic geometric feature) is **untouched**.
Lemma 1's design constraint (a usable restriction must exclude an open cone) is the only
thing that carries over to those. The DEAD write must name D1–D4 explicitly.

**Consequence for P12** — the note's claim that the P12-A no-go map "becomes exhaustive for
the classes considered so far" is acceptable only with that scope attached; it is a
statement about a finite tabulated list, not a theorem.

---

## 7. Findings

### MAJOR

**MAJOR 1 — the B2 verdict for D4 is false ("D4 survives B2"; §2.2, propagated to §4 and
§5 reason 1's scope).** The supremum of the spin-2 fraction over the coherent-information
pairs is **1**, not 0.72: along `p = (1−δ, δ)`, `u_1 = (e_1+ie_2)/√2`, `u_2 = ū_1`
(orthonormal, `|u_1^Tu_2| = 1`) the fraction is `1 − 2δ + O(δ²)` → measured 0.999998 at
`δ = 10⁻⁶`, versus the note's single sample of this family at `δ = 0.3` (fraction 0.7042).
Hence **every** `η ∈ (0,1]` excludes CI pairs and D4 dies at B2 with D1/D2/D3. Two
subsidiary errors in the same sentence: the cone quantifier is inverted (`η ≳ 0.3` should
be `η ≤ 0.284` even on the note's own numbers), and the stated range `[0.576, 0.716]`
omits the note's own `n1_arbitrary_anchor` value 0.8165. *Effect on the verdict:
strengthens it — reason 1 becomes sufficient on its own.*
Fix: replace §2.2's last paragraph with "D1, D2, D3 and D4 all die at B2", and extend §5
reason 1 to D4.

**MAJOR 2 — §3's "bounded search finds no violation at `x ∈ {0.46,…,0.49}`" is false at
`x = 0.46`, and the derived reading "buys ground only down to ≈ 0.455" (repeated in §5
reason 2) must be withdrawn.** Exact-input 60-dps certificate at `x = 46/100`, faithful
well-conditioned rational base point, exactly spin-2-free rational direction:
`q = −2.408289498713903668891301` (`artifacts/logs_whgap_r10_20260730/r10_witness.json`).
Root cause: all of the note's base points are `0.85·Wishart + 0.15·1/6` (`min spec ≥ 0.025`),
structurally blind to the near-pure entangled region where strip violations live. The
diagnostic was already in the note's own log — `b2_refassisted.json` returns the same null
minimum over *all* directions at `x = 0.49` (where cBKM domination PROVABLY fails) and at
`x = 0.55` (where it PROVABLY holds) — and the free negative control (unrestricted minimum
must be `< 0` for every `x < 1/2`) was not run (rule 7b).

### minor

- **m1 — the "is it an order at all" question is answered only implicitly.** For any fixed
  pair class, restricted domination is automatically a preorder on channels; stating this
  reduces the node's design question 1 to the stability questions §4 treats. (§1 of the
  note.)
- **m2 — Lemma 0's faithfulness step.** "Every point of the segment is a state" does not
  give faithfulness, and D2 quantifies over faithful `θ`; the CI pairs are exactly the
  rank-deficient case. The implication survives by restricting to `supp σ`, but the note
  should say so.
- **m3 — §2.1 consequence 3 over-states the logic.** "D1/D2-restricted domination cannot
  imply `Q ≤ 0`" is a claim about implication; what is established (and what the next
  sentence correctly says) is that the CI *route* is unavailable. Since §3 argues the
  condition is also false, the implication claim is literally vacuous. Prefer "the
  coherent-information route through this class is vacuous".
- **m4 — reproducibility of the §3 witnesses.** `b2_witness.json` / `b2_witness_strip.json`
  record only the resulting numbers, not the rational base point and direction, so the
  load-bearing `x = 0.42` and `x = 0.45` certificates cannot be re-checked from the archive
  without re-running a randomised search. Compare the R5a-reviewed practice
  (`e1_certificates.json` stores the rational state and eigendirection). My own certificate
  archives its full data for this reason.
- **m5 — the `n = 2` fractions inherit MAJOR 1.** §2.2's `n = 2` minima (0.346 per-copy /
  0.226 diagonal over 16 samples) are subject to the same sampling gap; nothing in the note
  bounds the `n = 2` fraction away from 1, and the `n = 1` result already suffices to kill
  the route.

### Screened, no finding

Standing failure-mode list (R5 §2) — 1 (no symbolic `.H`; my exact layer is `Fraction` +
mpmath); 2 (pinned interpreter throughout); 3 (complement convention: rebuilt from the
frozen Kraus set, cross-checked by Kraus completeness, `Tr Λ^c(Y) = Tr Y`, and G-cal against
R5b's closed forms); 4 (real Kraus, `Λ^c(Y)_{ab} = Tr(K_aYK_b^T)` verbatim; types audited
in §1); 5 (no symbolic eigenvalues); 6 (`SHA256SUMS_r10.txt` written LF, `sha256sum -c`
11/11 OK; the note's own `SHA256SUMS_p16a.txt` also verifies 13/13 OK); 7 (degeneracy branch
at relative gap `1e−11` float / `1e−40` at 60 dps; **all** base points asserted faithful and
both lifted outputs asserted full rank, so no kernel regularisation enters any reported
number — this is where my first pass `r10_cone.json` went wrong and was superseded); 8 (no
`ε log ε` expansion used); 9 (anchoring: projectors, Theorem B2, the character count and
the BKM finite-difference validation were derived and run before any of the note's numbers
were compared). Commission additions: no `nsimplify` anywhere; no free `Symbol`; ambient
rationalisation avoided — the direction is rationalised inside a Gaussian-integer basis of
the positive-codimension spin-2-free chart, verified `Π_2 Z = 0` exactly.

**(7f) value vs formula.** Theorem B2, Lemma 0, Lemma 1 and the `1⊗1 ⊃ 2` argument are
**formula/identity** claims: I re-derived each by hand and then corroborated numerically
(the numerics corroborate, they do not establish the derivations). §1's isotypic package is
a **structural** claim verified three independent ways plus a character identity. G-cal, the
x = 0.2 anchor and the x = 0.46 certificate are **values** at specific points (the last one
exact-on-input at 60 dps). The `x ∈ [0.47, 1/2)` non-negative readings — mine and the
note's — are bounded searches: **values with no quantifier**, and neither licenses a
non-negativity statement.

**(7g) terms of art.** "spin-2 component" = the `J = 2` isotypic component of `B(A)` under
`M ↦ OMO^T`, `O ∈ O(3)`, equivalently `ran P_2`, `P_2(M) = (M+M^T)/2 − (Tr M/3)1` — resolved
three ways in §1; "CI pairs" = `(ψ_{RA}, ψ_R⊗σ_A)` with `σ_A` a state on `A`; "admissible" =
in the pair/cone class of the definition under discussion; "complete" = quantified over all
finite-dimensional references; "faithful" = strictly positive definite, asserted in code.

---

## 8. Reproduction

```
C:<home>/cpython3119/python.exe tools/whgap_r10_isotypic.py   # -> r10_isotypic.json
C:<home>/cpython3119/python.exe tools/whgap_r10_cone.py       # -> r10_cone.json  (SUPERSEDED)
C:<home>/cpython3119/python.exe tools/whgap_r10_cone2.py      # -> r10_cone2.json
C:<home>/cpython3119/python.exe tools/whgap_r10_boundary.py   # -> r10_boundary.json
C:<home>/cpython3119/python.exe tools/whgap_r10_witness.py    # -> r10_witness.json
bash -c "cd artifacts/logs_whgap_r10_20260730 && sha256sum -c SHA256SUMS_r10.txt"
```
Inline snippets (BKM finite-difference validation; the `x = 0.2` anchor spot-check) are
recorded verbatim in `artifacts/logs_whgap_r10_20260730/COMMANDS.txt`.

