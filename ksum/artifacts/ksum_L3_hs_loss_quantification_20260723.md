# G1 — Hilbert–Schmidt loss-exponent quantification for the literal masked query

**Date:** 2026-07-23
**Task:** G1 of the `KSUM.B4b.retarget` gate plan — quantify the HS pinching/energy loss
exponent for the literal masked query in the induced-packet critical-endpoint adversary.
**Target node (rule 8a cite):**
`KSUM.B4b.L3.ALT.hidden-frequency-mask.critical-endpoint.ALT.hs-query-energy-law`
**Candidate interface package:**
`...critical-endpoint.ALT.literal-marked-query-polar-norm-interface`

**STATUS CAP (hard constraint):** this artifact is **NUMERICAL / CONJECTURED — pending-review**.
It writes **no** completion-tier status (no PROVED / CERTIFIED\* / REFUTED). Finite evaluation is
diagnostic only and never proves an asymptotic law (G11). It edits no existing repo file and runs
no git command. All verdict language below is a proposer-tier judgement awaiting independent
Rule-7 review.

---

## (a) Scope statement and frozen-inputs list

### Scope

The `hs-query-energy-law` node proposes to bound the **operator norm** of the *literal masked
query* via an exact **Hilbert–Schmidt orthogonal-pinching/energy identity**, and hopes that
"carrier multiplicities, coefficient normalization, and numerator scale" render the resulting
operator-norm bound asymptotically sufficient
(node claim, `...hs-query-energy-law.md:19-24`). Its own kill criterion is that "the unavoidable
Hilbert–Schmidt/operator-norm dimension factor loses the required `m^(1/6)` gain on a legal
endpoint family" (`...hs-query-energy-law.md:64-68`).

G1 asks: write the exact HS inequality with all normalizations; extract the loss factor `L` (ratio
between what the HS bound certifies and the operator-norm quantity the adversary needs) symbolically
in the packet/carrier dimensions, multiplicities, `a,q,s,N`; evaluate at `a=16,q=64`; and compare
its growth exponent `alpha` to the budget threshold `1/12` of `KSUM.B4b.retarget`.

**Primary structural finding (stated up front):** the *literal* masked-query HS identity is **not on
disk** — the node is a stub with "None at the exponent level" evidence
(`...hs-query-energy-law.md:45-47`), and the two interfaces that would *define* the literal query
(polar/range typing; outer numerator) are OPEN. What **is** exactly on disk is (i) the HS
energy identity for the **alphabet-equivariant compressed effect** (sufficiency decision eq. (3.2)),
and (ii) the full **orbit-intertwiner block-norm system** (6.6)/(6.8). Between the compressed effect
and the literal query the disk records two **strict gaps** (compression gap (4.5); carrier-suppression
gap (3.4)). The loss factor `L` is therefore quantifiable only as a **lower bound**; that lower bound
is what decides the budget question, and it decides it robustly.

### Frozen inputs (every on-disk definition relied on; file:line)

| Ref | Object used | Source (file:line) |
|---|---|---|
| F1 | HS energy identity `‖C‖²_HS = Σ_ν f^ν ‖C_ν‖²_HS`, `‖C‖ = max_ν‖C_ν‖` | `ksum/artifacts/ksum_L3_critical_induced_packet_equivariant_sufficiency_decision_20260722.md:216-232` (eq. 3.2) |
| F2 | full-product-invariant norms `‖C‖=max‖c_ν‖`, `‖C‖²_HS = p·Σ_ν f^ν‖c_ν‖²_HS`, `p=dim P=(f^λ)²` | same, `:237-246` (eq. 3.3), `:79-84` (eq. 1.5) |
| F3 | carrier hook dims `f^λ=62,660,742,144` at `λ=(283,4,1)`; parents `(f^{(62,2)},f^{(61,3)},f^{(61,2,1)})=(1952,39648,79360)`; mults `m_{0,ν}=(16,48,96)`, `m_{1,ν}=(16,80,160)`; `D=19456` | same, `:79-104` (eq. 1.5–1.8) |
| F4 | carrier-suppression operator-norm loss toy (true defect norm `1` vs suppressed `1/2`) | same, `:248-259` (eq. 3.4) |
| F5 | compressed-vs-literal strict gap `‖Δ(B)‖²=1/2` vs `‖B−E(B)‖²=1/4` | same, `:290-333` (eq. 4.1–4.5) |
| F6 | decision ledger: literal defect norm **BLOCKED** (missing polar/range identity); numerator **BLOCKED** | same, `:373-386` |
| F7 | orbit-intertwiner block-norm system `‖Γ(c)‖=max_ρ‖Σ_ω c_ω B_{ρ,ω}‖`, `ρ=(λ,μ,ν)`, `λ,μ⊢n`, `ν⊢q`; carrier `S^λ⊗S^μ⊗S^ν`; mult space `M_t(ρ)=(S^λ⊗S^μ⊗S^ν)^{K_t}` | `ksum/artifacts/ksum_L3_critical_orbit_intertwiner_attempt_20260721.md:236-304` (eq. 6.1–6.8) |
| F8 | masked-query block system `‖Γ(c)∘Δ_i‖=max_τ‖…B^L_{τ,η}‖`, `τ=(λ⁻,μ,ν)`, `λ⁻⊢n−1` (left query) | same, `:285-306` (eq. 6.7–6.8) |
| F9 | orbital norm `‖A_ω‖=√(r_ω s_ω)` | same, `:178-193` (eq. 4.3–4.4) |
| F10 | position-trivial ("local two-orbital") adversary is only `Θ(N^{1/3})` | same, `:322-402` (§7, eq. 7.6–7.8) |
| F11 | scaling `a=Θ(N^{2/3})`, `m=d+1=Θ(N^{1/3})`, `N=Θ(am)`; `s`↔occurrence mult | same, `:44-50` (eq. 2.2); `ksum/artifacts/ksum_L3_hidden_frequency_critical_adversary_attempt_20260721.md:56-61` (eq. 1.6) |
| F12 | exact adversary target `‖Γ‖≥cN^{2/3}`, `max_i‖Γ∘Δ_i‖≤1`; `Δ_i`=differ-at-`i` 0/1 matrix | `ksum/artifacts/ksum_L3_hidden_frequency_critical_adversary_attempt_20260721.md:286-299` (eq. 5.1) |
| F13 | baseline `Adv±=Ω(a^{2/3}√(d+1))=Ω(√N q^{1/6})=Ω(N^{11/18})`; missing gain `m^{1/6}=N^{1/18}` | same, `:18-56` (eq. 1.1–1.7); intertwiner `:466-472` (eq. 8.7) |
| F14 | budget: net loss `L<q^{1/12}` (`~N^{1/18}` at criticality) to beat `√N q^{1/6}`; threshold `alpha=1/12` | `ksum/proof-dag/nodes/KSUM.B4b.retarget.yaml:21-35` |

`a=Θ(q)` throughout the packet (`q=4a` at the reviewed point: `q=64`, `a=16`); `s` denotes the
occurrence/heavy-multiplicity parameter of the reviewed reducers (`s`-fan-out, `C_s=Σ_{j=0}^{s-2}p(j)`),
tied to `m=d+1` (heavy frequency) at criticality.

---

## (b) Type audit of the displayed inequality

The literal general-adversary bound (F12) needs, in **operator (spectral) norm** throughout,

```
Adv±(HF_{N,q}) = max_Γ ‖Γ‖_op / max_{i∈[2n]} ‖Γ∘Δ_i‖_op ,    Γ ∈ ℝ^{X_1×X_0}.
```

Types of the constituent maps (all as functions of the parameters):

- **`Γ` (numerator).** Domain `ℂ[X_0]` (NO orbit), codomain `ℂ[X_1]` (YES orbit).
  `dim X_0=|G|/|K_0|`, `dim X_1=|G|/|K_1|`, `|X_1|/|X_0|=a²/(q−4a+1)∈{…}` (F9 context; intertwiner
  eq. 3.5). `G=S_n^{(L)}×S_n^{(R)}×S_q`, `n=⌊N/2⌋`.
- **Block form (F7).** By Schur, an equivariant `Γ=Σ_ω c_ω A_ω` decomposes as
  `Γ = ⊕_{ρ} I_{S^λ⊗S^μ⊗S^ν} ⊗ Γ_ρ`, `ρ=(λ,μ,ν)`, `λ,μ⊢n`, `ν⊢q`.
  - **carrier factor** `I_{S^λ⊗S^μ⊗S^ν}`: identity on a space of dimension `D_ρ=f^λ f^μ f^ν`.
  - **multiplicity operator** `Γ_ρ : M_0(ρ) → M_1(ρ)`, a `dim M_1(ρ) × dim M_0(ρ)` matrix,
    `dim M_t(ρ)=dim (S^λ⊗S^μ⊗S^ν)^{K_t}`.
  - Consequently `‖Γ‖_op = max_ρ ‖Γ_ρ‖_op` (carrier identity is norm-invisible), while
    `‖Γ‖²_HS = Σ_ρ D_ρ ‖Γ_ρ‖²_HS` (carrier identity contributes `tr I_{D_ρ}=D_ρ`). **This is the HS
    orthogonal-pinching/energy identity for the equivariant adversary** — the exact analogue of F1's
    `Σ_ν f^ν(…)`, now with the full three-factor carrier weight.
- **`Δ_i` (query mask).** `Δ_i∈{0,1}^{X_1×X_0}`, `(Δ_i)_{x,y}=1[x_i≠y_i]`; applied as an entrywise
  (Hadamard) product `Γ∘Δ_i` (F12). Key equivariance facts:
  - `Δ_i` **commutes with the alphabet action** `S_q` (relabelling values preserves `x_i≠y_i`), so
    `ρ(g)Δ_iρ(g)^*=Δ_i`, `g∈S_q`. ⇒ `Γ∘Δ_i` keeps the alphabet block index `ν`.
  - `Δ_i` **breaks the position action** on the queried side: a left query localises one of the `n`
    left positions, so `S_n^{(L)}→S_{n−1}^{(L)}` and the left index branches `λ→λ⁻⊢n−1` (F8, eq. 6.7).
  - Hence `‖Γ∘Δ_i‖_op = max_τ ‖(Γ∘Δ_i)_τ‖_op`, `τ=(λ⁻,μ,ν)` (left) or `(λ,μ⁻,ν)` (right);
    `‖Γ∘Δ_i‖²_HS = Σ_τ D_τ ‖(Γ∘Δ_i)_τ‖²_HS`, `D_τ=f^{λ⁻}f^μ f^ν` (left).

**Dimension bookkeeping that drives the loss.** Numerator carrier weight `D_ρ=f^λ f^μ f^ν`; masked
(left) carrier weight `D_τ=f^{λ⁻}f^μ f^ν`. Their ratio `D_ρ/D_τ=f^λ/f^{λ⁻}` is **not 1** — for the
minimal nontrivial `λ=(n−1,1)`, `f^λ/f^{λ⁻}=(n−1)/1=n−1`. The alphabet factor `f^ν` is **common** to
`Γ` and to `Γ∘Δ_i` (both sides and every query), because `Δ_i` is alphabet-equivariant. The position
factors `f^λ,f^μ` are **not common**: a left query strips `f^λ→f^{λ⁻}`, a right query strips
`f^μ→f^{μ⁻}`, and the denominator is a max over **all** `i` (both sides). This asymmetry is the entire
mechanism of the HS/operator-norm loss.

---

## (c) Derivation

### c.1 What the HS energy law can rigorously certify

Fix an equivariant candidate `Γ` (F7). The energy law computes the two HS quantities
`E_num := ‖Γ‖_HS` (a clean carrier-weighted sum, F1/F7) and a mask bound
`E_den ≥ max_i ‖Γ∘Δ_i‖_HS`. The adversary theorem requires **operator** norms. The only
generic conversions available from the energy alone are the two-sided HS/op inequalities on each
block, `‖·‖_op ≤ ‖·‖_HS ≤ √(rank)·‖·‖_op`:

```
‖Γ‖_op       ≥ ‖Γ‖_HS / √(rank Γ),          rank Γ = Σ_ρ D_ρ · rank(Γ_ρ);
‖Γ∘Δ_i‖_op   ≤ ‖Γ∘Δ_i‖_HS ≤ E_den.
```

Therefore the **rigorously certifiable** adversary lower bound obtainable from the energy law is

```
Adv± ≥ ‖Γ‖_op / max_i‖Γ∘Δ_i‖_op ≥ (1/√(rank Γ)) · (E_num / E_den)
     = (1/L) · (HS-adversary ratio),        L := √(rank Γ).                (★)
```

`E_num/E_den` is the "HS-adversary ratio" the energy law delivers; `L=√(rank Γ)` is the loss —
exactly "the ratio between what the HS bound certifies and the operator-norm quantity the adversary
bound actually needs" (task def.). This is the honest content of the energy-law route **by itself**:
it never sees spectral concentration, so it cannot beat the flat-spectrum bound `‖Γ‖_op≥‖Γ‖_HS/√rank`.

### c.2 The loss is bounded below by the signal block's non-cancelling carrier

`rank Γ = Σ_ρ D_ρ rank(Γ_ρ) ≥ D_{ρ*} rank(Γ_{ρ*}) ≥ D_{ρ*} = f^{λ*} f^{μ*} f^{ν*}`, where `ρ*` is
the block carrying the numerator norm. So the **pure energy-law** loss is

```
L = √(rank Γ) ≥ √(f^{λ*} f^{μ*} f^{ν*})          (crude reading, no cancellation).
```

A *more favourable* reading grants the extra (not-on-disk) matched-cancellation argument that would
strip the **common** alphabet factor `f^ν` (legitimate in principle because `Δ_i` is alphabet-
equivariant, so `f^ν` appears identically in `E_num` and `E_den`). Even granting it in full, the
**position** factors survive, because a query on either side strips that side's factor while the
denominator maxes over both sides:

```
L_net ≥ √(f^{λ*} f^{μ*})   ≥ √(f^{λ*})    (one broken side, minimal nontrivial λ*).
```

### c.3 The position carrier cannot be trivial (so the loss cannot vanish)

If the signal block had trivial position content (`λ*=μ*=(n)`, `f^{λ*}=f^{μ*}=1`) the position loss
would vanish — but then `Γ` is an **alphabet-only / local** adversary, and F10 proves exactly this
class is capped at `‖Γ‖=2√a=Θ(N^{1/3})` (intertwiner eq. 7.6–7.8), far below even the `N^{11/18}`
baseline, let alone `N^{2/3}`. Hence **any** adequate adversary occupies a block with nontrivial
position content, `f^{λ*}≥f^{(n−1,1)}=n−1`. The energy identity necessarily weights that block by its
full carrier dimension, so the position loss is **unavoidable** for the HS route. (The operator-norm
route — the *sibling* `polar-offdiagonal-block-law` / `literal-marked-query-polar-norm-interface` —
avoids `L` entirely by bounding operator norms directly; this is exactly why the node itself calls the
polar block "the cleaner first test", `...hs-query-energy-law.md:59-62`.)

### c.4 Two on-disk strict gaps only *add* loss

The object in c.1–c.3 is already the **compressed / equivariant** effect. The disk proves the
**literal** masked query is strictly larger-normed in two independent ways, both of which only enlarge
`L`, never shrink it:
- **compression gap (F5, eq. 4.5):** `‖Δ(B)‖²=1/2 > 1/4=‖B−E(B)‖²` — the literal query defect exceeds
  the compressed defect (needs a polar/range identity that is BLOCKED, F6);
- **carrier-suppression gap (F4, eq. 3.4):** suppressing a rank-1 position carrier of dimension `d`
  changes the true operator norm from `1` to `1/d` (shown for `d=2`) — i.e. the literal (unsuppressed)
  operator norm carries a further position-dimension factor the compressed model omits.

Both are `O(1)` only in their `d=2` toys and **scale with the carrier dimension**; at criticality the
carrier dimensions are `poly(q)` with positive degree (F3). They cannot rescue the budget.

---

## (d) Symbolic loss factor `L` and parameter-growth table

**Symbolic `L`.** With `ρ*=(λ*,μ*,ν*)` the signal block,

```
   L  =  √(rank Γ)  =  √( Σ_ρ f^λ f^μ f^ν · rank(Γ_ρ) )
      ≥  √( f^{λ*} f^{μ*} f^{ν*} · rank(Γ_{ρ*}) )                    [pure energy law]
      ≥  √( f^{λ*} f^{μ*} )                                          [grant f^ν cancellation]
      ≥  √( f^{(n−1,1)} )  =  √(n−1)  =  Θ(√n).                       [one side, minimal]
```

This is a genuine power law `L = q^alpha · (bounded)`, **not** a polylog factor.

**Parameter-growth table (each factor at `q=Θ(N^{2/3})`, so `a=Θ(q)`, `n∼N∼q^{3/2}`, `m=Θ(N^{1/3})=Θ(q^{1/2})`).**

| Parameter / factor | role in `L` | bounded or growing? | growth at criticality |
|---|---|---|---|
| `f^{ν}` (alphabet Specht, `ν⊢q`) | in `L` (crude); **cancels** if matched-argument granted | growing | `Θ(q)` (min `(q−1,1)`) up to `Θ(q³)` (three-row packet) |
| `f^{λ}, f^{μ}` (position Specht, `⊢n`) | in `L` (**does not cancel**) | growing | `≥ n−1=Θ(q^{3/2})` (min `(n−1,1)`); `∼n^{k}` for `k` off-row cells |
| `f^{λ}/f^{λ⁻}` (query branch ratio) | source of non-cancellation | growing | `≥ n−1=Θ(q^{3/2})` |
| `rank(Γ_ρ)` (occurrence/mult block) | multiplies inside `L` | growing (`≥1`) | `≤ min(m_{0,ν},m_{1,ν})=Θ(a)=Θ(q)` |
| `a` | packet/UIC scale | growing | `Θ(q)=Θ(N^{2/3})` |
| `q` | alphabet | growing | `Θ(N^{2/3})` |
| `s`, `m=d+1` | occurrence / heavy multiplicity | growing | `Θ(N^{1/3})=Θ(q^{1/2})` |
| `N` | domain | growing | `Θ(q^{3/2})` |
| `D=19456`, `p=(f^λ)²` | carrier-suppressed / full carrier | growing | finite point `1.9×10⁴` / `3.9×10²¹` |

**Dominant growth of `L`.**

```
   most favourable (net, one broken side, minimal position irrep):   L ~ q^{3/4}      (alpha=3/4)
   net, both position sides minimal:                                 L ~ q^{3/2}      (alpha=3/2)
   pure energy law, minimal irreps incl. alphabet:                   L ~ q^{2}        (alpha=2)
```

Every reading is a positive power of `q` with `alpha ≥ 3/4`.

---

## (e) Evaluation at the finite reviewed point `a=16, q=64`

Script `ksum/artifacts/ksum_L3_hs_loss_quantification_20260723_compute.py`
(SHA-256 `061469941e724ed035b7cbf30bec133241ad3483f680c64f72d5ce044684d7ed`) recomputes the on-disk
hook dimensions (all match: `f^{(283,4,1)}=62,660,742,144`; `(f^{(62,2)},f^{(61,3)},f^{(61,2,1)})=
(1952,39648,79360)`) and forms `L` in each reading. Command:

```
"<machine-local-path-redacted>" \
  ksum/artifacts/ksum_L3_hs_loss_quantification_20260723_compute.py
```

Log: `ksum/artifacts/logs_ksum_L3_hs_loss_quantification_20260723/run.log`
(SHA-256 `bc9e1eb1f9d2a91943329e5f687f1c188766000d66a94da1d35f6966c34d2201`).
Finite point: `a=16, q=64`, position `n=|λ|=288` (`λ=(283,4,1)`).

| Reading of `L` | value at `a=16,q=64` | as `q^alpha` |
|---|---|---|
| A — net, 1 side, minimal `(n−1,1)`  (most favourable) | `√287 ≈ 16.9` | `q^{0.667}` |
| A′ — net, both position sides, minimal | `287` | `q^{1.361}` |
| B — net, 1 side, reviewed `λ=(283,4,1)` | `√f^λ ≈ 2.50×10⁵` | `q^{2.989}` |
| B′ — net, both sides `p=(f^λ)²` | `f^λ = 6.27×10¹⁰` | `q^{5.978}` |
| C — pure energy law, minimal irreps incl. `f^ν` | `≈ 2.28×10³` | `q^{1.859}` |
| C′ — pure energy law, reviewed carriers incl. `f^ν` | `≈ 1.77×10¹³` | `q^{7.334}` |

Budget cell: `q^{1/12} = 64^{1/12} ≈ 1.414` is the **entire** tolerated loss (equivalently the sought
`m^{1/6}` gain). The smallest reading (A) already exceeds it by `16.9 / 1.414 ≈ 12×` at this finite
point; the exponent gap is `0.667 − 0.083 ≈ 0.58` at `n=288` and widens to `≥ 3/4 − 1/12 = 2/3`
asymptotically (`n∼q^{3/2}`).

*(Diagnostic only: the finite point `n=288 ≈ 0.56 q^{3/2}` slightly understates the asymptotic
exponent; a finite evaluation and a scaling heuristic do not constitute an asymptotic proof — G11.)*

---

## (f) Verdict

**OUT-OF-BUDGET.**

Symbolic loss: `L = √(rank Γ) ≥ √(f^{λ*} f^{μ*})`, dominant growth **`L = Θ(q^{alpha})` with
`alpha ≥ 3/4`** (most favourable, net, one broken position side); `alpha ≥ 2` for the pure energy-law
route with no cancellation granted. Budget threshold is `alpha < 1/12`. At `a=16,q=64` the most
favourable reading gives `L ≈ 16.9 = q^{0.667}`, against a total tolerated `q^{1/12} ≈ 1.41`.

**Why OUT-OF-BUDGET rather than NOT-DETERMINABLE.** The *exact value* of `alpha` is under-determined
(the literal polar/range identity and the outer numerator are OPEN, so whether `alpha=3/4` or `2` or
larger is not fixed on disk). But the *budget comparison* is determined: every quantifiable lower
bound on `L` exceeds `q^{1/12}` by a large margin, and the one mechanism that could drive `L→O(1)` —
a position-trivial adversary — is ruled out by F10 (position-trivial ⇒ `Θ(N^{1/3})`, far sub-baseline).
The two on-disk strict gaps (F4, F5) only enlarge `L`. Hence the HS-route loss cannot fit inside the
`q^{1/12}` bridge budget: this reproduces, and quantifies, the node's own kill criterion — "the
unavoidable HS/operator-norm dimension factor loses the required `m^{1/6}` gain."

**Secondary finding (recorded, not the verdict):** the literal masked-query HS pinching identity that
the node names is itself **absent** from the frozen record; only the equivariant compressed-effect
identity exists, separated from the literal query by two documented strict gaps. Anyone who wanted a
strict NOT-DETERMINABLE reading of the *node's exact object* is entitled to it — but it does not change
the budget outcome, because the loss is out of budget already at the compressed level and the gaps are
one-signed (they add loss).

Status of this verdict: **CONJECTURED / NUMERICAL — pending-review**. Proposer-tier; no completion
gate opened.

---

## (g) What would change this verdict

1. **A genuine HS→operator-norm concentration theorem.** If one proved the signal-bearing `Γ_{ρ*}`
   has an operator norm within `q^{o(1)}` of `‖Γ_{ρ*}‖_HS/√(f^{λ*}f^{μ*})` *without* re-solving the
   adversary SDP (i.e. a certified spectral-concentration bound, not a flat-spectrum estimate), the
   `√(rank)` in (★) would be replaced by something smaller. But the energy law alone provably cannot
   supply this (it sees only total energy); such a theorem is the operator-norm route, not the HS route.
2. **A construction whose signal block has bounded position content while still reaching `N^{2/3}`.**
   This would need `f^{λ*}f^{μ*}=q^{o(1)}` with `‖Γ‖=Ω(N^{2/3})`; F10 rules out the trivial case and no
   on-disk family reaches the baseline with `O(1)` position carrier. A new registered node exhibiting
   one would reopen the question.
3. **A matched-cancellation identity making even the position carrier common** to numerator and every
   masked query — impossible as stated (a query localises a position and strips `f^λ→f^{λ⁻}`), so this
   would require redefining `Δ_i` or the norm, i.e. a different theorem.
4. **A relaxed budget.** If `KSUM.B4b.retarget` were re-relaxed so the tolerated total loss were
   `q^{alpha_0}` with `alpha_0 ≥ 3/4` (net) — i.e. a numerator scale far above `√N q^{1/4}` — the HS
   route could re-enter. No such numerator is on disk.
5. **Independent Rule-7 review** correcting any of: the alphabet-equivariance of `Δ_i` (which powers
   the `f^ν` cancellation and the "position-only" loss), the hook-dimension identifications (F3,
   cross-checked exactly by the script), or the claim that the energy law cannot certify concentration.
   A correction to any of these could move `alpha`; none is presently in doubt.

---

## Reproducibility

- Script: `ksum/artifacts/ksum_L3_hs_loss_quantification_20260723_compute.py`
  SHA-256 `061469941e724ed035b7cbf30bec133241ad3483f680c64f72d5ce044684d7ed`.
- Command:
  `"<machine-local-path-redacted>" ksum/artifacts/ksum_L3_hs_loss_quantification_20260723_compute.py`
- Log: `ksum/artifacts/logs_ksum_L3_hs_loss_quantification_20260723/run.log`
  SHA-256 `bc9e1eb1f9d2a91943329e5f687f1c188766000d66a94da1d35f6966c34d2201`.
- The script computes only standard hook-length dimensions and dimension-factor arithmetic; it embeds
  no adversary optimizer and asserts no asymptotics. All exponents `alpha` in §(d),(f) are analytic
  (from the carrier structure F7/F8), not fitted to the finite point.

**Load-bearing scope lock.** This artifact quantifies the HS-route loss for the equivariant orbit-
intertwiner adversary (F7) using the on-disk energy identity (F1) and carrier dimensions (F3). It does
**not** construct any adversary, prove any operator-norm bound, compute a spectrum or numerator, or
change any node status. It caps at CONJECTURED/NUMERICAL — pending-review.
