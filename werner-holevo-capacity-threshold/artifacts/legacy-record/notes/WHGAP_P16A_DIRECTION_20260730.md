# WHGAP P16-A (Track B) — is a direction-restricted order even usable?

Node: `WHGAP.direction-restricted-order` (P16). Executor note, 2026-07-30.
Commission: [WHGAP_COMMISSION_P15A_P16A_20260730.md](WHGAP_COMMISSION_P15A_P16A_20260730.md), Track B.

---

## PRE-ACTION REPORT (mandatory, `research/PRETASK_RELOAD_PROMPT.md` executed first)

Files read from disk before any work, in the prescribed order: `research/DAG_PROTOCOL.md`;
`research/RESEARCH_STRUCTURE_PROTOCOL.md`; `channel-capacity/werner-holevo-gap/README.md`;
`channel-capacity/werner-holevo-gap/proof-dag/NODE_INDEX.md`;
`proof-dag/nodes/WHGAP.direction-restricted-order.md` (target), its parent
`proof-dag/nodes/WHGAP.goal.md`, and the related nodes
`proof-dag/nodes/WHGAP.restricted-order.md` (P12, the parent programme) and
`proof-dag/nodes/WHGAP.pure-anchor-order.md` (P15, the sibling candidate); §§1–3 of
`notes/WHGAP_REVIEW_COMMISSION_R5_20260729.md` (frozen conventions, standing failure modes,
rule-7 embeds); the R8 MAJOR-1 section of `artifacts/whgap_r8_review_20260730.md`.
(The problem DAG doc `notes/WERNER-HOLEVO-GAP_PROOF_DAG.md` is the whole-graph view; the
node files + NODE_INDEX carry the same graph and were used as the authority here.)

- **Target node and status as read from disk:** `WHGAP.direction-restricted-order` (alias P16),
  kind LEAF, role proof, **status OPEN**, disposition `null`
  (`channel-capacity/werner-holevo-gap/proof-dag/nodes/WHGAP.direction-restricted-order.md`,
  front matter line `status: OPEN`; NODE_INDEX row `P16 | ... | OPEN`). Work record: "node
  registered … No commission". Open obligation: *"Settle design question 1 (is the restriction
  stable under references and tensoring?). If NO, this node closes as DEAD with that reason …"*
- **ROLE: executor.** I am a fresh instance; I did not author any prior WHGAP work, and the
  decision-layer prediction in my commission ("the class dies at B2") was given to me as
  explicitly untrusted input, to be derived independently or refuted.
- **Highest status my planned evidence could license (§2 ladder):** **NUMERICAL** with a
  `pending-review:` marker, written by the decision layer citing this note plus the run logs
  (command + log path + script SHA-256). Nothing here licenses a completion tier: rule 2 forbids
  an author from killing a branch to REFUTED, and rule 6 requires a COMPLETED, archived,
  rule-7-compliant independent review (R10) before REFUTED/DEAD may be written on this node.
  My B4 output is therefore a **recommendation**, not a status write.
- **Gates and deliverables (one line each):**
  - B1 — write down ≥ 2 precise candidate definitions of a direction-restricted domination.
  - B2 — decide, for each, whether the pairs the coherent-information step consumes lie in the
    class: decompose `ψ_RA − ψ_R ⊗ ρ_A` under the O(3) action on A and compute the spin-2
    isotypic component for ≥ 20 random and ≥ 3 structured purifications, plus n-copy versions.
  - B3 — stability under references and under tensoring, for B2 survivors only.
  - B4 — verdict: DEAD with reason, or a precise surviving formulation + feasibility-probe needs.
  - Deliverable: this note; scripts `tools/whgap_p16a_*.py`; logs
    `artifacts/logs_whgap_p16a_20260730/` with a per-role `SHA256SUMS_p16a.txt` (LF).
- **Conflicts between commission text and disk protocols:**
  1. **Reconciled tension (not a conflict).** The commission's B2/B4 wording says to "record it
     [the definition] with that reason [DEAD]". Per DAG rule 2/6 an executor may not write
     REFUTED/DEAD. The commission's own "Cap" line resolves this ("Cap NUMERICAL/CONJECTURED with
     `pending-review:` for R10"), and I follow the disk: the verdict below is authored as a
     recommendation at NUMERICAL/CONJECTURED tier.
  2. **Commissioned protocol deviation, noted as required.** The single-writer binding forbids me
     from editing node files, `NODE_INDEX.md`, or the DAG doc; DAG §5 / rule 8c would otherwise
     require me to append the outcome to the node in this session. The deviation is explicitly
     commissioned (R5 commission, "Single-writer deviation (binding)") and the decision layer
     performs the atomic node/index/DAG update citing this note. **This note is therefore an
     orphaned artifact until that update lands** — flagging it so it cannot be forgotten.
  3. Otherwise none.

---

## 0. Conventions and calibration (own implementation, before reading any prior numbers)

Frozen conventions (R5 §1): `Λ_x(Y) = (1−x)Y + (x/2)(Tr(Y)·1 − Y^T)` on qutrits;
`K_0 = √(1−x)·1`, `K_{μ+1} = √(x/2)·A_μ` with `(A_μ)_{jk} = ε_{μjk}`; padded 4-dimensional
complement `Λ^c_x(Y)_{ab} = Tr(K_a Y K_b^T)`; BKM form
`g_θ(Z) = Σ_ij |⟨i|Z|j⟩|² c(λ_i,λ_j)`, `c(a,b) = (log a − log b)/(a−b)`, `c(a,a) = 1/a`.

**Types (7a).** `Y, Z, θ`: 3×3 complex (states / traceless Hermitian directions) on the channel
input `A`; `Λ_x(Y)`: 3×3; `Λ^c_x(Y)`: **4×4** (padded); with a reference `R` of dimension `d_R`
the objects are `d_R·3 × d_R·3` on the input and B side and `d_R·4 × d_R·4` on the E side, and
the lifted maps are `id_R ⊗ Λ`, `id_R ⊗ Λ^c` applied blockwise. `P_2` below is a superoperator
on `B(A)` (9 complex dimensions), **not** a matrix on `A`. The cBKM defect
`q_θ(Z) := g_{Λ^c_R(θ)}(Λ^c_R(Z)) − g_{Λ_R(θ)}(Λ_R(Z))` is a real **quadratic form** in `Z`,
a number, not an operator.

**G-cal (calibration gate, run FIRST, before reading the paper's values).** With my own BKM code
and my own complement assembly, at the R5b witness anchor `ρ_ε = diag(1−2ε, ε, ε)` and direction
`X = (E₂₃+E₃₂)/√2` (1-based indices; the pair of ε-degenerate levels):

| x | q(ε=10⁻²) | 10⁻³ | 10⁻⁴ | 10⁻⁵ | analytic limit 2(1−x)(2x−1)/x |
|---|---|---|---|---|---|
| 0.20 | −4.478429 | −4.765838 | −4.796562 | −4.799656 | **−4.800000** |
| 0.40 | −0.582294 | −0.598203 | −0.599820 | −0.599982 | **−0.600000** |
| 0.45 | −0.235487 | −0.243542 | −0.244354 | −0.244435 | **−0.244444** |
| 0.49 | −0.036091 | −0.041078 | −0.041577 | −0.041627 | **−0.041633** |
| 0.50 | +0.005001 | +0.000500 | +0.000050 | +0.000005 | **0** |
| 0.55 | +0.167118 | +0.163982 | +0.163671 | +0.163640 | **+0.163636** |
| 0.70 | +0.346382 | +0.343206 | +0.342892 | +0.342861 | **+0.342857** |

and my computed `g_B`, `g_E` match the closed forms `(1−3x/2)²/b_ε` (with `b_ε = x/2 + (1−3x/2)ε`)
and `x/(2(1−ε))` to `≤ 3.3e−16`. The sign flip is exactly at `x = 1/2`. **G-cal PASS** — my
independent stack reproduces the reviewed necessity witness (R5b, PROVED input) without having
been fitted to it. Log `b0_calibration.json`.

**Own isotypic projectors (7c).** The covariance group is `O(3)` acting on `B(A)` by
`M ↦ O M O^T` (this is the action for which `Λ_x` is covariant — verified, max error 8.9e−16).
`−I` acts trivially, so the action factors through `SO(3)` and the O(3)- and SO(3)-isotypic
decompositions coincide. `B(A) ≅ spin 0 ⊕ spin 1 ⊕ spin 2` with complex dimensions 1, 3, 5.
I built the spin-2 projector **two independent ways**:
- closed form `P_2(M) = (M + M^T)/2 − (Tr M/3)·1`;
- Casimir route: the infinitesimal action is `M ↦ [J_a, M]` with `J_a = i L_a` the spin-1
  generators, so `Ĉ = Σ_a ad_{J_a}²` has eigenvalue `J(J+1)`; the spin-2 isotypic projector is
  the spectral projector of `Ĉ` at eigenvalue 6.
Agreement: `1.2e−15`; observed Casimir spectrum `{0, 2, 6}` with multiplicities `(1, 3, 5)`;
`P_0+P_1+P_2 = 1` to `7.4e−16`; `P_2` Hermitian and idempotent to `4.2e−16`; equivariance
`P_2(OMO^T) = O P_2(M) O^T` to `1.4e−15` for both `det O = ±1`.
`P_2` preserves Hermiticity and is an **orthogonal** projection in Hilbert–Schmidt inner product.

With a reference `R` (no group action on `R`), `B(R ⊗ A) = B(R) ⊗ B(A)` and the spin-2 isotypic
projector is `Π_2 := id_{B(R)} ⊗ P_2`, i.e. `P_2` applied to each `R`-block.

**Independent confirmation of R5b claim 5.** `P_2 X = X` exactly: the necessity witness direction
is *purely* spin-2 (fraction `1.000000` for both the `(1,2)` and the `(2,3)` placement). So a
restriction that excludes spin-2 directions does exclude the witness — the premise that makes
this node conceivable is correct.

---

## 1. B1 — four precise candidate definitions

Throughout, `𝒮_2(R) := ran(Π_2)` is the spin-2 isotypic subspace of `B(R ⊗ A)`, and directions
`Z` are traceless Hermitian (differences of states).

**D1 (pair class; finite / relative-entropy form).**
`𝒟_1 := { (ρ, σ) states on R ⊗ A, any finite-dimensional R : Π_2(ρ − σ) = 0 }`.
`Λ` satisfies D1-restricted domination iff
`D(Λ^c_R(ρ) ‖ Λ^c_R(σ)) ≥ D(Λ_R(ρ) ‖ Λ_R(σ))` for every `(ρ,σ) ∈ 𝒟_1`.
*Statement about **state PAIRS**.* Its complete (reference-assisted) version is the definition as
written, quantified over all `R`; the trivial-reference version is `R = ℂ`.

**D2 (cone field; infinitesimal / BKM form).**
Admissible tangent cone at every base point `θ`:
`𝒞(θ) := { Z = Z†, Tr Z = 0, Π_2 Z = 0 }` (here a base-point-independent linear subspace, i.e. a
constant cone field). `Λ` satisfies D2 iff `q_θ(Z) ≥ 0` for all faithful `θ` and all `Z ∈ 𝒞(θ)`.
*Statement about a **cone field of directions**.*

> **Lemma 0 (D1 ⟺ D2).** With `h(t) = D(σ + tZ ‖ σ)` one has `h(0) = h′(0) = 0` and
> `h″(t) = g_{σ+tZ}(Z)`, so `D(ρ‖σ) = ∫₀¹ (1−t) g_{σ+t(ρ−σ)}(ρ−σ) dt`. Every point of the
> segment `σ + t(ρ−σ) = (1−t)σ + tρ` is a state and the direction along the segment is the
> *constant* `Z = ρ − σ`, which lies in `𝒞` precisely when `(ρ,σ) ∈ 𝒟_1`. Hence D2 ⟹ D1.
> Conversely `t ↓ 0` in `D(σ+tZ‖σ) = (t²/2) g_σ(Z) + O(t³)` gives D1 ⟹ D2 at faithful `σ`.
> (Both directions applied on the B and E sides simultaneously.) So D1 and D2 are the same
> condition in two languages; I keep both because the node's design question 1 is posed about the
> cone-field reading.

**D3 (exclude ONLY the purely-spin-2 directions).** `q_θ(Z) ≥ 0` for every faithful `θ` and every
traceless Hermitian `Z` with `Π_2 Z ≠ Z`. *Cone field.* This is the weakest possible reading of
"excludes the spin-2 breaking directions".

**D4 (quantitative cone; exclude an OPEN cone around the spin-2 subspace).** Fix `η ∈ (0,1]`.
`q_θ(Z) ≥ 0` for every faithful `θ` and every `Z` with `‖Π_2 Z‖²_HS ≤ (1−η)‖Z‖²_HS`.
*Cone field.* D2 is the case `η = 1`; D4 with `η < 1` is strictly stronger than D2.

> **Lemma 1 (why D3 is not a restriction at all — and a design constraint on ALL such classes).**
> For fixed `θ`, `Z ↦ q_θ(Z)` is a real quadratic form, hence continuous. If the admissible set
> `𝒜` is **dense** in the traceless Hermitian space, then `q_θ ≥ 0` on `𝒜` implies `q_θ ≥ 0`
> everywhere. The complement of the proper linear subspace `𝒮_2` is dense, so **D3 is EQUIVALENT
> to unrestricted cBKM**, which is PROVED false for every `x < 1/2` (R5b necessity theorem,
> frozen input). **D3 is dead, for a reason that generalises: any usable direction restriction
> must exclude a set with non-empty interior — an OPEN cone.** D1/D2 (exclude a codimension-5·d_R²
> subspace's complement, i.e. admit only a thin subspace) and D4 (admit a closed cone whose
> complement is open) both satisfy this; "exclude the breaking directions" naively read does not.

---

## 2. B2 — do the coherent-information pairs lie in the class?

The pairs the CI step consumes are `(ψ_{RA}, ψ_R ⊗ ρ_A)`, because
`I(R;B)_ψ = D( Λ_R(ψ_{RA}) ‖ Λ_R(ψ_R ⊗ ρ_A) )` and likewise on the E side, and
`I_c(ρ_A) = ½[I(R;B) − I(R;E)]` (the identity R8 §2.12 verified independently).

### 2.1 Theorem B2 (exact; not merely "generically")

> **Theorem.** Let `ψ_{RA}` be pure with Schmidt decomposition `ψ = Σ_j √p_j |j⟩_R |u_j⟩_A`, and
> let `σ_A` be **any** state on `A` (not only the marginal `ρ_A`). Then
>
>   `‖Π_2( ψ_{RA} − ψ_R ⊗ σ_A )‖²_HS`
>     `= Σ_{j≠k} p_j p_k (1 + |u_j^T u_k|²)/2  +  Σ_j p_j² ‖P_2(|u_j⟩⟨u_j| − σ_A)‖²_HS`
>     `≥ (1 − Tr ρ_A²)/2 > 0`  whenever `ψ` is entangled.
>
> **Proof.** Write `Δ = Σ_{jk} |j⟩⟨k|_R ⊗ M_{jk}`; `{|j⟩⟨k|}` is HS-orthonormal in `B(R)`, so
> `‖Π_2Δ‖² = Σ_{jk} ‖P_2 M_{jk}‖²`. In the Schmidt basis `ψ_R = Σ_j p_j |j⟩⟨j|` is diagonal, so
> `ψ_R ⊗ σ_A` is `R`-block-diagonal and for `j ≠ k` the block is **unchanged by the anchor**:
> `M_{jk} = √(p_j p_k) |u_j⟩⟨u_k|`. For such a block `Tr M_{jk} = ⟨u_k|u_j⟩ = 0`, and with
> `M = u_j u_k^†`, `M^T = ū_k ū_j^†`, one gets
> `‖P_2 M‖² = ¼(‖M‖² + ‖M^T‖² + 2 Re Tr(M† M^T)) = ¼(2 + 2|u_j^T u_k|²) = (1+|s_{jk}|²)/2`
> with `s_{jk} = u_j^T u_k`. Summing, `Σ_{j≠k} p_j p_k (1+|s_{jk}|²)/2 ≥ Σ_{j≠k} p_j p_k /2
> = (1 − Σ_j p_j²)/2 = (1 − Tr ρ_A²)/2`. The diagonal blocks contribute the non-negative second
> sum. ∎

Consequences, in the exact logical form:
1. **No entangled purification pair is in `𝒟_1`, and no CI direction is in `𝒞(θ)`** — for *any*
   product anchor, so the freedom `σ_A ≠ ρ_A` in the CI step (which exists, since
   `D(ψ_{RB}‖ψ_R⊗ω_B) = I(R;B) + D(ρ_B‖ω_B)`) does **not** rescue the class.
2. The excluded content is exactly the *entanglement* of the pair: the bound is `(1−Tr ρ_A²)/2`,
   which vanishes iff `ψ` is a product state — precisely the case in which the CI step is empty
   (`I(R;B) = I(R;E) = 0`, `I_c` from a pure input `= 0`).
3. Therefore **D1/D2-restricted domination cannot imply `Q ≤ 0`**: the restriction removes every
   pair the coherent-information argument consumes. This is a *vacuity* statement about the route,
   not a claim that the restricted condition is false. (§3 shows it is *also* false on most of the
   strip.)

**The decision-layer prediction is CONFIRMED, and sharpened**: not "generically nonzero" but
"nonzero for every entangled purification, with an explicit anchor-independent lower bound".

### 2.2 Numerical verification (own code, own projectors)

`tools/whgap_p16a_spin2.py` → `b2_spin2.json`. 24 Haar-random purifications (`d_R = 3`) + 4
structured (maximally entangled; isotropic-Schmidt `τ = 0` rank-2; real Schmidt rank-3; real
rank-2) + 6 arbitrary non-marginal anchors `σ_A ≠ ρ_A`:

- the theorem's lower bound holds in **34/34** cases (`bound_ok: true` throughout);
- minimum spin-2 norm² over all cases `= 0.1224`; **no case is near zero**;
- spin-2 **fraction** `‖Π_2Δ‖²/‖Δ‖²` ranges over `[0.576, 0.716]`;
- exact analytic cross-check: maximally entangled `ψ` gives `‖Π_2Δ‖² = 5/9`, `‖Δ‖² = 8/9`,
  fraction `5/8` — computed by hand from the theorem and reproduced to `1e−15`.

`n = 2` (two channel copies, `d_A = 9`, `d_R = 9`): 12 Haar purifications + 4 tensorised CI pairs
(products of two `n = 1` purifications). Two conventions for "spin-2" at `n = 2`, both tested with
Casimir-built projectors: **(a) per-copy** (`O_1 ⊗ O_2` independent; spin-2 in copy 1) and
**(b) diagonal** (a single `O` acting on both copies; total spin 2). Minimum over all 16 samples:
`0.346` (per-copy) and `0.226` (diagonal) — **nonzero everywhere**, fractions `0.35–0.60`.

**B2 verdict: D1 and D2 are DEAD** (recommended; reason = Theorem B2). **D3 is DEAD** by Lemma 1.
**D4 survives B2** — the CI directions have spin-2 fraction `≤ 0.72` (`n=1`) and `≤ 0.60` (`n=2`)
while the necessity witness has fraction exactly `1`, so a cone with `η ≳ 0.3` excludes the
witness and retains every sampled CI direction. D4 therefore goes to B3.

---

## 3. Additional finding (not commissioned): the restriction is also FALSE on most of the strip

Vacuity (§2) already kills D1/D2 as a Q = 0 mechanism. Independently, I measured whether the
restricted condition even *holds*, by minimising the Rayleigh quotient of `q_θ` over the
spin-2-free subspace. `tools/whgap_p16a_cone.py`, `tools/whgap_p16a_witness.py`;
logs `b2_cone.json`, `b2_scan.json`, `b2_refassisted.json`, `b2_witness.json`,
`b2_witness_strip.json`.

- **Falsification anchor (binding per the node).** At `x = 0.2 ∈ (0, 2/5)` where `Q > 0` is
  PROVED, the spin-2-free restricted condition **fails** hard (`min q/‖Z‖² = −3.14` at
  `ρ_{0.1}`, `−5.07` at `ρ_{0.01}`, `−3.50` at random faithful anchors). Required for viability;
  satisfied. It also fails at `x = 0.1, 0.3, 0.35, 0.38, 0.39, 0.40` (trivial reference).
- **Inside the strip it fails too, with high-precision witnesses.** Using a **chart-aware**
  rationalisation (the direction is rationalised in a *rational basis of the spin-2-free
  subspace* — 15 exact basis elements for `d_R = 2`, verified Hermitian, traceless and exactly
  spin-2-free; the unconstrained base point is rationalised entrywise, Hermitised exactly,
  trace-normalised and checked faithful), evaluated at **60 dps** with mpmath:

  | x | base point | min eig θ | spin-2 residual of Z | `q/‖Z‖²` (60 dps) |
  |---|---|---|---|---|
  | 0.42 | faithful, `d_R = 2`, non-product | 2.583e−2 | 9.6e−17 (float readout of an exact 0) | **−0.2748977983804598939** |
  | 0.45 | faithful, `d_R = 2`, non-product | 3.955e−3 | 4.8e−17 | **−0.0280809901650730336** |

  So the **complete** (reference-assisted) D1/D2 condition is false at `x = 0.42` and `x = 0.45`.
- **Bounded search finds no violation at `x ∈ {0.46, 0.47, 0.48, 0.49}`** (150 random faithful
  `d_R = 2` base points each; minima `+4.3e−3, +2.6e−2, +3.8e−2, +5.0e−2`) — NUMERICAL only, and
  R8 m1's warning applies: a non-negative bounded minimum is not a proof of non-negativity.
  Reading: the spin-2-free restriction buys ground only from `1/2` down to roughly `0.455`; it
  does **not** reach `2/5`.
- **D4 inherits all of this.** `{Z : ‖Π_2Z‖² ≤ (1−η)‖Z‖²} ⊇ {Z : Π_2Z = 0}`, so D4-restricted
  domination *implies* D2-restricted domination; the `x = 0.42` and `x = 0.45` witnesses are
  spin-2-free, hence admissible for every `η`, hence **D4 also fails at 0.42 and 0.45** for every
  `η ∈ (0,1]`. Direct cone minimisation confirms it (`x = 0.45`, `ρ_{0.1}`: cone `f = 0.9` gives
  `−0.121`). Even a cone that keeps the CI pairs cannot cover the strip.
- **Where the breaking directions live (independent re-confirmation, with a caveat).** The
  minimiser of `q_θ` over *all* directions has spin-2 fraction `1.000` at every `ρ_ε` anchor for
  `x ∈ {0.4, 0.45, 0.49, 0.55}` and `0.84–0.99` at random faithful anchors in the strip — R5b
  claim 5's "the breaking direction is spin-2" is a **strip** phenomenon and I reproduce it. But
  at `x = 0.2` the minimiser has fraction `0.000–0.24`: below `2/5` the breaking directions are
  *not* spin-2. That asymmetry is exactly why the restriction can separate `(0,2/5)` from part of
  the strip — and exactly why it cannot be used, since it also separates out the CI pairs.

---

## 4. B3 — stability under references and under tensoring (run for the B2 survivor D4, and for D1/D2)

**(i) Attaching a reference: STABLE.** `Π_2` is defined uniformly as `id_{B(R)} ⊗ P_2`, so if
`Π_2^{(R)} Z = 0` then `Π_2^{(R⊗R′)}(Z ⊗ ω) = 0` for every operator `ω` on `R′`; likewise the D4
cone condition is preserved because `‖Π_2(Z⊗ω)‖² = ‖Π_2 Z‖²‖ω‖²`. The complete version of the
class is well defined. (This is the *only* part of design question 1 that comes out positive.)

**(ii) Tensoring: NOT STABLE, in either covariance convention.**

- **Diagonal action** (one `O` on both copies — the convention under which `Λ_x^{⊗2}` is covariant
  as a channel with a single `O(3)` symmetry): "spin-2-free" means each factor lies in
  `spin 0 ⊕ spin 1`, but `1 ⊗ 1 = 0 ⊕ 1 ⊕ 2` contains spin 2. Measured with my Casimir projector
  on `A⊗A`: for spin-2-free `Z_1, Z_2`, the **total-spin-2 fraction of `Z_1 ⊗ Z_2`** was
  `0.17, 0.33, 0.64, 0.55, 0.50, 0.26, 0.41, 0.27` over 8 samples — never zero.
- **Per-copy action** (`O_1 ⊗ O_2`): the class of admissible **pairs** is not closed under tensor
  products, because
  `ρ_1⊗ρ_2 − σ_1⊗σ_2 = (ρ_1−σ_1)⊗ρ_2 + σ_1⊗(ρ_2−σ_2)`
  and the copy-2 spin-2 part of `ρ_2` is generically nonzero. Measured for tensor products of two
  admissible (spin-2-free-difference) pairs: copy-1 spin-2 fraction of the product difference
  `0.11–0.19`, diagonal-spin-2 fraction `0.18–0.28` over 8 samples — never zero.

**Answer to the node's design question 1: NO.** The restriction survives references but not
tensoring, in either convention; the hybrid tensorisation induction cannot even be *stated* for
this class, because the tensor of two admissible pairs is not admissible. Per the node's own
Open-obligations text ("If NO, this node closes as DEAD with that reason"), this is a second,
structurally independent kill, and it applies to D1, D2 and D4 alike.

---

## 5. B4 — verdict

**Recommendation: `WHGAP.direction-restricted-order` (P16) is DEAD** — for the class of
restrictions defined by the **O(3)-isotypic type of the difference / tangent direction**, which is
the class the node registers. Three logically independent reasons, any one sufficient:

1. **Vacuity w.r.t. the coherent-information step (B2, a theorem).** Excluding spin-2 excludes
   *every* entangled purification pair, for *every* product anchor, with the anchor-independent
   bound `‖Π_2(ψ_{RA} − ψ_R⊗σ_A)‖² ≥ (1 − Tr ρ_A²)/2`. The class cannot imply `Q = 0`.
   Applies to D1, D2 (and to D3 vacuously).
2. **Falsity on the strip (§3, 60-dps witnesses).** The restricted condition — in its complete
   reference-assisted form — is false at `x = 0.42` and `x = 0.45`, with exactly spin-2-free
   directions at faithful base points. Applies to D1, D2 **and D4** (whose admissible set contains
   the spin-2-free subspace), and to D3 via Lemma 1 (D3 ≡ unrestricted cBKM, PROVED false below
   1/2). At best the restriction reaches down to `≈ 0.455` (bounded search), never to `2/5`.
3. **Failure of tensor stability (B3).** Not closed under tensoring in either the diagonal or the
   per-copy covariance convention; the induction the capacity proof needs cannot be started.

**What this does NOT establish.** (a) It is not a statement that "no direction-restricted order
can work" in an unrestricted sense — only that restrictions defined through the spin-2 isotypic
component of the difference are dead. A restriction by a *different* geometric feature (one that
is not a linear-isotypic condition on `ρ−σ`, e.g. a condition coupling the direction to the base
point, or a restriction on the anchor rather than the direction) is untouched by this note; but
Lemma 1 constrains every candidate to exclude an **open** cone, and §3 shows any excluded cone
must be large enough to swallow spin-2-free violating directions at `x = 0.42, 0.45`.
(b) The bounded searches at `x ∈ {0.46,…,0.49}` are NUMERICAL, not proofs of non-negativity.
(c) Nothing here bears on `WHGAP.pure-anchor-order` (P15), which remains the surviving candidate.

**Consequence for the parent programme.** With P16 dead, the P12-A no-go map becomes **exhaustive
for the classes considered so far** (row-(d)-quantifier classes; `α ≥ 1` Rényi; less noisy; cRE;
cBKM; signed lifts; anchored less-noisy; and now direction/isotypic-restricted classes), leaving
`WHGAP.pure-anchor-order` (P15) as the only registered survivor of the restricted-order
programme, alongside `WHGAP.order-converse` (P11) and genuine `I_c`-additivity technology.

**Status cap (rule 6).** Everything above is executor-authored. Recommended tier for the decision
layer pending R10: **NUMERICAL with `pending-review:`** for §§0, 2.2, 3, 4 (runs with
command + log + SHA-256); Theorem B2 and Lemmas 0/1 are proofs written by me and therefore
**CONJECTURED / pending-review** until R10 completes. No completion-tier status (REFUTED/DEAD) may
be written on P16 on the strength of this note alone.

---

## 6. Screening against the standing failure-mode list (R5 §2), and rule-7 self-report

| # | Failure mode | How screened |
|---|---|---|
| 1 | sympy `.H` leaving `conjugate(√(1−x))` | no symbolic `.H` used; the exact layer uses `Fraction` and mpmath only |
| 2 | WindowsApps python inaccessible | all runs on the pinned `C:<home>/cpython3119/python.exe` |
| 3 | complement convention drift (3 vs padded 4-dim, sign, k) | complement built from the frozen Kraus set and cross-checked by G-cal against R5b's closed forms to 3e−16 |
| 4 | transpose vs conjugate-transpose in HS adjoints | Kraus are real; `Λ^c(Y)_{ab} = Tr(K_a Y K_b^T)` used verbatim; Hermiticity of every output checked implicitly by `eigh`/`eighe` |
| 5 | `sorted()` on symbolic eigenvalues | no symbolic eigenvalues taken |
| 6 | CRLF in SHA256SUMS | written with `newline="\n"`, verified with `sha256sum -c` |
| 7 | eigenvalue bookkeeping at degeneracies / near-zero gaps | `c(a,a)=1/a` branch at gap `< 1e−12` (float) / `1e−40` (60 dps); kernel–kernel entries of the E-side base given a large `c`, which can only *suppress* violations, never create them; violations re-verified at 60 dps |
| 8 | ε log ε bookkeeping | not used here (no entropy expansion in this track) |
| 9 | anchoring | G-cal, the isotypic projectors and Theorem B2 were derived and run **before** reading any prior numeric value; the two projector constructions are mutually independent; R5b's closed forms were compared only afterwards |
| — | **new (commission)**: `nsimplify` on exact rationals | never used; rationalisation is `Fraction`-based |
| — | **new (commission)**: `Symbol('x')` needs a reality assumption | no free symbols used |
| — | **new (commission)**: ambient rationalisation VOID on a positive-codimension set | the spin-2-free constraint is positive-codimension; directions are rationalised **inside a rational basis of that subspace** (15 exact elements, residual exactly 0 in exact arithmetic), never in the ambient Hermitian space |

- **(7b) c ≥ 2 gates:** every claim is exercised at ≥ 2 values of `x` (G-cal at 7; the strip
  witnesses at 0.42 and 0.45; the falsification anchor at 6 values below 2/5) and, for B2, at
  ≥ 2 values of `d_R`, ≥ 2 anchor types (`σ_A = ρ_A` and `σ_A ≠ ρ_A`) and both `n = 1, 2`.
- **(7f) value vs formula:** Theorem B2, Lemma 0 and Lemma 1 are **formula/identity** statements
  (Theorem B2 is proved in closed form and *then* corroborated at 34 points by an independent
  construction — the numerics corroborate, they do not establish the derivation). §0's G-cal is a
  **value** check at 7 x-values × 4 ε. §3's negative results are **values** at two `x` (60 dps,
  exact inputs); §3's non-negative results are **bounded searches**, i.e. values with no
  quantifier. §4 is a **structural** (representation-theoretic) statement corroborated at 8+8
  samples; the `1 ⊗ 1 ⊃ 2` argument is the proof.
- **(7g) terms of art:** "spin-2 component" = the `J = 2` isotypic component of `B(A)` under
  `M ↦ OMO^T`, `O ∈ O(3)`, equivalently `ran(P_2)` with `P_2(M) = (M+M^T)/2 − (Tr M/3)1`;
  "CI pairs" = `(ψ_{RA}, ψ_R ⊗ ρ_A)`; "admissible" = in the cone/pair class of the definition
  under discussion; "complete" = quantified over all finite-dimensional references.

---

## 7. Reproduction

```
C:<home>/cpython3119/python.exe tools/whgap_p16a_spin2.py      # B2 + B3, -> b2_spin2.json
C:<home>/cpython3119/python.exe tools/whgap_p16a_cone.py       # cone/subspace minima -> b2_cone.json
C:<home>/cpython3119/python.exe tools/whgap_p16a_witness.py    # 60-dps exact-input witness -> b2_witness.json
```
plus the two inline scans recorded as `b0_calibration.json`, `b2_scan.json`,
`b2_refassisted.json`, `b2_witness_strip.json` (commands echoed in
`artifacts/logs_whgap_p16a_20260730/COMMANDS.txt`).
Checksums: `artifacts/logs_whgap_p16a_20260730/SHA256SUMS_p16a.txt` (LF), covering the three
scripts and every log file.

