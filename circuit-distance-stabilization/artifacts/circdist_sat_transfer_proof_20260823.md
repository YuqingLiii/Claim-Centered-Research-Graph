# CIRCDIST.sat.transfer — the finite-state / min-plus transfer theorem

**Node:** `CIRCDIST.sat.transfer` (frontier task-001) · **Date:** 2026-08-23 · **Role:** Opus 5
executor, proposer. **Box:** one session, stop-loss binding. No sub-agents. No Lean. No proof-DAG
object touched. No existing file modified; this is the session's single new artifact.

**Governing problem statement:** `research/circdist/notes/SAT_RESCOPE_20260822.md`, task 1 of the
2026-08-22 re-scope ("给出 `d_R(M)` 的有限状态 / min-plus transfer 表示"). **Frozen base
definitions:** `research/circdist/notes/CIRCDIST_PROBLEMS.md` 公共定义, as written out in full in
`artifacts/circdist_sat_window_theorem_20260822.md` §1.

**Epistemic ceiling, binding on every line.** Nothing here is labelled PROVED or `CERTIFIED*`.
Every mathematical statement is **CONJECTURED** and carries a *derivation status* line; every
computation is **NUMERICAL** with its code inline (§11) and its search scope stated. This document
has had no independent review, and this session cannot grant one. All prior artifacts are treated
as **data in files**, not as certification.

**Relation to the sibling nodes.** This document discharges the **transfer** arm only. It does not
compute `(d_∞, R_stab)` for the instance families of `CIRCDIST.sat.instances`. It is deliberately
**not** circular with `CIRCDIST.sat.window`: §7's theorem is proved without using any part of the
window theorem, and §9 then *re-derives* the window theorem's parts (i)–(iii) from the transfer
representation as an independent cross-check.

---

## 0. Hash chain

```text
inputs consulted (data, not certification; none modified)
  artifacts/circdist_sat_recon_20260820.md
    bde5d9e2fd686936305255ba7cd5ed7398930981130e4f5b8a21f798d5c063e9
  artifacts/circdist_sat_window_theorem_20260822.md
    487acf030bc4385ab367e5c7b27a0e2015bae4055f16ba61100ea85866d37e1b
  artifacts/circdist_sat_window_amendment1_20260822.md
    295e1635cc7a27c6ca43d88e7a9303c5bbfac96aeaecb1d2fee1a5cad4ac9799
  artifacts/circdist_sat_window_review_20260822.md
    219a756e9e366d74cd6d4b13ff91bdb8394ed35f5c922d3f864b176fcf697226
  artifacts/circdist_lift_nonint_proof_20260820.md
    42d6c138c1ea19127db76ab4f22d2a64c1d1e1e96adf76af975076b529a71f4c
  research/circdist/notes/SAT_RESCOPE_20260822.md
    6c8ec4362f728713f9934d5f0b8041195f66434ebe283a69e67147b3c7009d7f
  research/circdist/proof-dag/nodes/CIRCDIST.sat.transfer.yaml
    bb3f84645219f5d01226b92850feba66b151489e79b8309d63390a6b2a520a94

verification program of §11 (written this session, reproduced verbatim in §11.4)
  transfer.py
    1d3b8754b72d9dc77a8c16ecfab1c8b81f9dcfd5dd0a9abb2baf1b1a26e64c68
```

The window-theorem digest `487acf03…` is the one that document's amendment and review bind
themselves to; §3 of this document *derives* the clause S3′ that the amendment adopts, so nothing
below depends on that adoption being correct.

---

## 1. Statement of the theorem

Fix a CSS code `Q = [[n,k,d]]`, `k ≥ 1`, with X-check set `𝒜`, Z-check set `ℬ`, check matrices
`H_X ∈ F₂^{𝒜×n}`, `H_Z ∈ F₂^{ℬ×n}`, `S_X := rowspace H_X`, `S_Z := rowspace H_Z`. Fix a **legal,
measurement-consistent** single-round single-ancilla schedule `M` (Definitions 2.3–2.5), of any
depth `T ≥ 1`, interleaved or not, graph-like or not, with `𝒜, ℬ` the given (possibly **dependent**)
generating sets. Let `C_R^Z(M)`, `C_R^X(M)` be the two memory experiments with ideal initialisation
and ideal terminal transversal readout, and `d_R^σ(M)` their circuit distances (Definition 2.11).

Work in the min-plus semiring `(𝕊, ⊙, ⊕) := (ℤ_{≥0} ∪ {+∞}, +, min)`, with matrix product
`(AB)[i,j] = min_h (A[i,h] + A[h,j])` written `A ⊙ B`, and `A^{⊙R}` the `R`-fold product.

> ### THEOREM T (min-plus transfer representation). CONJECTURED.
>
> **(a) State space.** Put `Σ^Z := F₂^n / S_X`, a finite abelian group of order `2^{r_Z}` with
> `r_Z := n − rank H_X`. Then `H_Z` and every logical functional `λ^{(j)} = ⟨·, χ_{Z_L^{(j)}}⟩`
> descend to `Σ^Z`, and the class of the accumulated residual data-`X` error is a **sufficient
> statistic** for the whole future of the undetectability constraint and of the terminal logical
> condition. **No measurement memory and no logical bookkeeping beyond this class is needed**
> (Lemma 6.4); the corresponding statement for a detector window `w > 2` is false and is out of
> scope (Remark 6.6).
>
> **(b) Fault dictionary.** For `[δ] ∈ Σ^Z` and `μ ∈ F₂^ℬ` let
> ```
>      w_M([δ], μ) := min{ |S| : S a one-round X-sector fault configuration
>                               with [E(S)] = [δ] and u(S) = μ } .
> ```
> `w_M` is well defined (Definition 5.2), **round-independent** (Lemma 5.3), and **finite everywhere**,
> with `w_M([δ],μ) ≤ min_{δ'∈[δ]} |δ'| + |μ|` (Lemma 5.5). Every elementary fault is a weighted
> transition and every weighted transition is realised by a fault configuration of exactly that
> weight (Lemma 5.6).
>
> **(c) Transfer system.** Define, over `𝕊`, indices ranging over `Σ^Z`,
> ```
>      A[σ, σ'] := w_M( σ' − σ , H_Z σ )                      (transfer matrix)
>      u[σ]     := 0 if σ = [0],                    else +∞   (ideal initialisation)
>      v[σ]     := 0 if H_Z σ = 0 and σ ≠ [0],      else +∞   (ideal terminal readout + logical)
> ```
> All entries of `A` are finite; `v` is finite on exactly `2^k − 1` states. Then **for every
> `R ≥ 1`**
> ```
>      d_R^Z(M)  =  u ⊙ A^{⊙R} ⊙ v  =  min over σ_0,…,σ_R of  u[σ_0] + Σ_{r=0}^{R−1} A[σ_r,σ_{r+1}] + v[σ_R] .
> ```
> When `k = 1` the right-hand side is the single matrix entry `(A^{⊙R})[[0], [X_L]]`.
>
> **(d) Both sectors.** The mirror system `(u^X, A^X, v^X)` on `Σ^X := F₂^n / S_Z`,
> `A^X[σ,σ'] = w_M^X(σ'−σ, H_X σ)`, computes `d_R^X(M)`. On the disjoint union
> `Σ := Σ^Z ⊔ Σ^X` with the block-diagonal `A := A^Z ⊕ A^X` and the concatenated `u := (u^Z,u^X)`,
> `v := (v^Z,v^X)`, one single min-plus system computes
> ```
>      d_R(M) = min( d_R^Z(M), d_R^X(M) ) = u ⊙ A^{⊙R} ⊙ v      for every R ≥ 1 .
> ```
>
> **(e) Spectrum and consequences.** `A[σ,σ'] = 0` **iff** `σ = σ'` and `H_Z σ = 0`. Hence the
> min-plus eigenvalue of `A` is `0`, its critical graph consists of exactly `2^k` self-loops
> (`2^k + 2^k` for the assembled two-sector system), and its cyclicity is `1`. Consequently
> `A^{⊙R}` is eventually **constant**, not merely eventually periodic; and, directly from the
> transfer representation and with no appeal to tropical transient theory,
> `d_{R+1} ≤ d_R`, `d_R ≤ d`, `d_R = d_d` for `R ≥ d`, and `R_stab ≤ d_∞ ≤ d` (§9).

**Derivation status by part.** **(a) complete** (§4, §6); **(b) complete** (§5); **(c) complete**
(§7); **(d) complete** (§8); **(e) complete** (§9) — each *relative to* the model of §2 and the
imported clauses tabulated in §2.6, and each subject to the residual sub-claims of §12. The `d = 3`
implementation of `artifacts/circdist_sat_recon_20260820.md` §7 is **not used** anywhere in the
derivation; §11 is a fresh, independent corroboration written for this session.

**Two definitions in the recon are corrected here, not merely restated.**

* The recon's Claim 3.4 says the critical graph is "a set of `2^{2k}` self-loops". The correct
  count is `2^k` per sector: the zero-cost self-loops sit at `{σ : H_Z σ = 0} = ker H_Z / S_X`,
  which has dimension `n − rank H_Z − rank H_X = k`. (The recon's own `d = 3`, `k = 1` run reports
  `2`, i.e. `2^k`, so the exponent is a slip in the text, not in the code.)
* The recon's Definition 3.2 lists "unreachable states" as an object to be identified. Under the
  frozen fault model **there are none**: Lemma 5.5 makes every entry of `A` finite, so the
  transition graph is complete and every state is reachable in one step from every other. The
  honest replacement is the *pruned* state set of Remark 5.7, which is a statement about optimal
  paths, not about reachability.

---

## 2. The model, and what is imported

§2 restates the frozen model so that every quantifier below has an explicit range. Definitions
2.1–2.11 are the window theorem's Definitions 1.1–1.12 verbatim in content; the numbering is local.
§2.6 tabulates precisely which of its lemmas are imported rather than re-derived.

### 2.1 Code

**Definition 2.1.** `Q = [[n,k,d]]` is given by `𝒜, ℬ` with supports in `[n]`, subject to
`|supp(a) ∩ supp(b)| ≡ 0 (mod 2)` for all `a ∈ 𝒜, b ∈ ℬ` — equivalently `H_X H_Z^⊤ = 0` **(CSS)**.
Fix logical representatives `X_L^{(1..k)}, Z_L^{(1..k)}`, and put
`d_X := min{|v| : v ∈ ker H_Z ∖ S_X}`, `d_Z := min{|v| : v ∈ ker H_X ∖ S_Z}`, `d = min(d_X,d_Z)`.

**Standing fact 2.2.** `ker H_Z = S_X ⊕ span{χ_{X_L^{(j)}}}` and `ker H_X = S_Z ⊕ span{χ_{Z_L^{(j)}}}`,
each quotient of dimension `k = n − rank H_X − rank H_Z`; and for `v ∈ ker H_Z`, `v ∉ S_X` **iff**
`|v ∩ supp(Z_L^{(j)})|` is odd for some `j`. *Standard CSS symplectic duality; status: complete.*

**Scope clause T0.** `k ≥ 1`. `𝒜` and `ℬ` are the **given generating sets**, not required
independent: `leftker(H_X) ≠ 0` is explicitly in scope (this is the case §3 must handle and the
case the toric and bivariate-bicycle families exhibit).

### 2.2 Schedule

**Definition 2.3 (one round).** Each check `g` owns one ancilla `anc(g)`. Per round: every
`anc(a)`, `a ∈ 𝒜`, is prepared in `|+⟩`, is the **control** of exactly one CNOT onto each
`q ∈ supp(a)`, and is measured in `X`; every `anc(b)`, `b ∈ ℬ`, is prepared in `|0⟩`, is the
**target** of exactly one CNOT from each `q ∈ supp(b)`, and is measured in `Z`. No flags, no cat
states, no repeated CNOTs, no change of generating set.

**Definition 2.4 (legality).** `M` assigns a time step in `{0,…,T−1}` to every CNOT (`t(a→q)`,
`t(q→b)`); it is **legal** if at every step each physical qubit is in at most one two-qubit gate.

**Definition 2.5 (measurement consistency, (MC)).** With
`c_{ab}(M) := #{q ∈ supp(a) ∩ supp(b) : t(q→b) < t(a→q)} mod 2`, `M` is measurement-consistent iff
`c_{ab} = 0` for all `(a,b)`. Writing `c'_{ab} := #{q : t(a→q) < t(q→b)}`, (CSS) gives
`c_{ab} + c'_{ab} ≡ 0`, hence `c'_{ab} = c_{ab}`, so **(MC) is mirror-symmetric** and selects the
same schedule class in both sectors. *Status: complete; this is the window amendment's Repair 3,
re-derived here in one line because §3 consumes both `c` and `c'`.*

**Scope clause T1.** Every statement below quantifies over **all** `(Q,M)` with `Q` CSS, `k ≥ 1`,
and `M` legal **and** measurement-consistent in the class of Definitions 2.3–2.4 — any depth,
interleaved or not, any check weights, graph-like or not, generating sets dependent or not.

### 2.3 Rounds and records

**Definition 2.6.** `C_R^Z(M)`: ideal initialisation in `|0⟩^{⊗n}`; `R` **verbatim repetitions** of
the round; ideal transversal `Z` readout of all `n` data qubits. Rounds are indexed
`r ∈ {0,…,R−1}`. `C_R^X(M)` is the mirror (`|+⟩^{⊗n}`, ideal `X` readout). Records: `m_{g,r}` for
each check `g` and round `r`; readout bits `ρ_q`, `q ∈ [n]`. Boundary conventions
`m_{b,−1} := 0` and `m_{b,R} := ⊕_{q∈supp(b)} ρ_q`.

**Scope clause T2 (round-translation covariance).** The elementary fault locations of round `r` are
in effect-preserving bijection with those of round `r'`, for all `r,r'` and all `R`, and the
location sets of distinct rounds are **disjoint**. This holds for the verbatim layout of Definition
2.6 and fails for cross-round idle-layer compression, which is out of scope.

**Definition 2.7 (detector set; Z-memory).** `D_{b,r} := m_{b,r} + m_{b,r−1}` for `b ∈ ℬ`,
`r ∈ {0,…,R}` — **the full interval, no detector missing at either temporal end**; and
`D_{a,r} := m_{a,r} + m_{a,r−1}` for `a ∈ 𝒜`, `r ∈ {1,…,R−1}` (the round-0 `X`-outcome is uniformly
random, so `D_{a,0}` does not exist). Observables `λ^{(j)} := ⊕_{q ∈ supp(Z_L^{(j)})} ρ_q`.

### 2.4 Faults

**Definition 2.8 (locations and configurations).** The **locations** of round `r` are: each CNOT of
that round (carrying any of the 15 non-identity two-qubit Paulis immediately after it); each
(qubit, time step) at which that qubit is not in a two-qubit gate, plus each ancilla immediately
after preparation (carrying any of the 3 non-identity single-qubit Paulis); and each recorded
outcome of that round (carrying a classical flip). A **fault configuration** `F` assigns to each
location an element of the group attached to it, with `|F| := #{locations assigned a non-identity
element}`. An **elementary fault** is a configuration of weight `1`. Data initialisation and the
terminal readout are ideal and carry no locations. Propagation is `F₂`-symplectic,
`CNOT(c,t) : x_t ← x_t + x_c`, `z_c ← z_c + z_t`; ancilla Pauli frames are zeroed after each
round's measurement.

**Lemma 2.9 (collision handling — one location, one Pauli).** The record-flip vector and observable
flip of a configuration are `F₂`-linear in the assignments. Consequently, for any target effect `e`,
```
      min{ |S| : S a multiset of elementary faults with total effect e }
    = min{ |F| : F a fault configuration with effect e } .
```
*Derivation.* `≤` is trivial (a configuration is such a multiset). For `≥`, take a minimising
multiset `S`; if two of its members share a location `ℓ`, replace them by the single element of
`ℓ`'s group equal to their product. By linearity the effect is unchanged; the weight drops by `1`
if the product is non-identity and by `2` if it is the identity. Iterating terminates and yields a
configuration of weight `≤ |S|`. ∎ *Status: complete. This is the lemma that makes "weight" additive
under the union of per-round pieces, because Definition 2.8's location set is **partitioned by
round** (T2): distinct rounds cannot collide, so `|⊔_r S_r| = Σ_r |S_r|` exactly, while within a
round the collision-permissive minimum already equals the collision-free one.*

### 2.5 Circuit distance

**Definition 2.10.** `F` is **undetectable** in `C_R^σ(M)` if it flips no detector of Definition
2.7, and **logical** if it flips some `λ^{(j)}`.

**Definition 2.11.** `d_R^σ(M) := min{|F| : F undetectable and logical in C_R^σ(M)}`;
`d_R(M) := min(d_R^Z, d_R^X)`; `d_∞(M) := lim_R d_R(M)`;
`R_stab(M) := min{R_0 : d_R = d_∞ ∀ R ≥ R_0}`.

**Scope clause T3.** The identification of 公共定义's `d_circ(C(M))` with `min(d_R^Z, d_R^X)` is an
inherited convention (the window theorem's **W-G1**), not a result of this document. Every
statement of §3–§7 and §9 is proved **per sector**; §8 assembles.

### 2.6 What is imported, and what is proved here

| item | source | here |
|---|---|---|
| model, Definitions 2.1–2.11 | window theorem §1 | restated, not re-derived |
| (MC) ⟺ deterministic detectors | window theorem Standing fact 1.6 | used; the `c = c'` half re-derived in 2.5 and again in 3.3 |
| sector decoupling | window theorem CONJECTURED 2.1 | **re-derived** (Lemma 3.1), because §3 needs it against a *larger* detector set than Definition 2.7 |
| round transparency, round-independence | window theorem 2.3, 2.4 | **re-derived** (Lemmas 5.3, 5.4) |
| time-locality column form `(∂)` | window theorem 2.5 | re-derived as Lemma 6.1 |
| criterion (W) | window theorem 2.8 | **re-derived** (Lemma 6.2), in the state notation |
| zero-voltage singletons `f_q` | window theorem 2.11 | **re-derived** (Lemma 5.5) |
| detector-span clause **S3′** | window review §1.3, adopted by window amendment §1.2 | **derived** here (§3), in a sharper form: an *equality* of spans on the Z-side, with the observable/detector split given a canonical definition |
| monotonicity, contiguity, window | window theorem §3–§5 | **not used**; independently re-derived in §9 as a cross-check |
| the `d = 3` min-plus implementation | recon §7 | **not used** |

---

## 3. The detector convention: which parities are detectors, and the dependent-check subtlety

This section closes, with derivations, the question the window theorem left as its "cheapest
remaining formal hole" (W-G3) and its review answered with clause S3′. It is placed **before** the
transfer construction because Theorem T computes a distance against a specific detector set, and
the theorem is worth nothing if that set is the wrong one.

Throughout §3 we work in `C_R^Z(M)`. Write a record parity as a triple of coefficient vectors
`(α, β, γ)`: `α ∈ F₂^{𝒜×R}` on the `m_{a,r}`, `β ∈ F₂^{ℬ×R}` on the `m_{b,r}`, `γ ∈ F₂^n` on the
readout bits `ρ_q`.

### 3.1 Sector decoupling

**CONJECTURED 3.1 (sector decoupling).** Split each Pauli fault into its `x`-part and `z`-part, and
assign each classical record flip to the sector of the record it flips (`m_{b,·}` → X-sector,
`m_{a,·}` → Z-sector). For any configuration `F`, let `F^X` keep the `x`-parts and the `m_{b,·}`
flips and delete the rest. Then:

1. every `m_{b,r}`, every readout bit `ρ_q`, and hence every `λ^{(j)}` and every `D_{b,r}` is
   flipped by `F` exactly as by `F^X`;
2. every `m_{a,r}` — hence *every parity whatsoever of X-check records* — is flipped by `F^X` by
   `0`;
3. `F^X` is a legitimate configuration with `|F^X| ≤ |F|`.

*Derivation.* Propagation is `F₂`-linear and type-preserving: `x`-components travel control→target
and `z`-components target→control, never mixing. `m_{b,r}` is a `Z`-basis measurement of `anc(b)`,
flipped only by the `x`-component present on `anc(b)` at measurement time (plus its own classical
flip); the terminal `Z`-basis readout of a data qubit is flipped only by that qubit's
`x`-component. `m_{a,r}` is an `X`-basis measurement of `anc(a)`, flipped only by `z`-components
(plus its own classical flip). `F^X` retains all `x`-components and all `m_{b,·}` flips of `F`,
giving (1); it has no `z`-component and no `m_{a,·}` flip, giving (2). For (3): at every location
Definition 2.8 makes all 15 (resp. 3) non-identity Paulis available, so the `x`-part of an assigned
Pauli is either the identity (the location is freed) or itself an available assignment; deletions
only lower the weight. ∎ *Status: complete.*

### 3.2 The deterministic-parity space splits by Pauli type

**Definition 3.2.** `V` := the space of record parities that are **deterministic** in the
fault-free `C_R^Z(M)`, i.e. whose back-propagated Pauli lies in the stabiliser group of the input
state `|0⟩^{⊗n}_{data} ⊗ (⊗_r |0⟩_{anc(b)} |+⟩_{anc(a)})`, namely
`G_0 := ⟨ Z_q (q ∈ [n]),  Z_{anc(b,r)},  X_{anc(a,r)} ⟩`. Write `V_Z` for the deterministic parities
with `α = 0` and `V_X` for those with `β = 0, γ = 0`.

**CONJECTURED 3.3 (type splitting and closed forms).**
```
      V = V_Z ⊕ V_X ,
      V_Z = { (β,γ) : γ ∈ ker H_X } ,           dim V_Z = |ℬ| R + n − rank H_X ,
      V_X = { α : Σ_r H_X^⊤ α_{·,r} = 0 } ,     dim V_X = |𝒜| R − rank H_X .
```

*Derivation.* Every `m_{b,r}` and every `ρ_q` back-propagates a `Z`-type Pauli, every `m_{a,r}` an
`X`-type one, and CNOT conjugation preserves Pauli type. So the back-propagated Pauli of a general
parity is `X(ξ) Z(ζ)` with `ξ` coming from `α` alone and `ζ` from `(β,γ)` alone, on disjoint
symplectic coordinates. `G_0` is generated by pure-type elements, and membership of `X(ξ)Z(ζ)` in
it is the conjunction of two independent coordinate conditions —
```
      ξ|_{data} = 0 ,  ξ|_{anc(b,·)} = 0        and        ζ|_{anc(a,·)} = 0
```
(`ζ|_{data}` and `ζ|_{anc(b,·)}` are unconstrained because every `Z_q` and every `Z_{anc(b,r)}` lies
in `G_0`; `ξ|_{anc(a,·)}` is unconstrained because every `X_{anc(a,r)}` does). Hence `V = V_Z ⊕ V_X`.

*Z-half.* Back-propagate `Z_{anc(b,r)}` from the end of round `r`. Each gate `q→b` has `anc(b)` as
target, and `CNOT Z_t CNOT = Z_c Z_t`, so the Pauli picks up `Z_q` for every `q ∈ supp(b)`: the data
vector gains `χ_{supp(b)}`. Continuing backwards inside round `r`, each gate `a→q` with `q` a target
already carrying `Z_q` contributes `Z_{anc(a,r)}` once, with total exponent
`#{q ∈ supp(a) ∩ supp(b) : t(a→q) < t(q→b)} = c'_{ab} = c_{ab} ≡ 0` by **(MC)** and Definition 2.5.
So no `X`-ancilla component is produced inside round `r`. Set
`ζ^{(r)} := γ + Σ_{r' ≥ r} H_Z^⊤ β_{·,r'}` (the data `Z`-vector at the start of round `r`; the
recursion `ζ^{(r)} = ζ^{(r+1)} + H_Z^⊤β_{·,r}` is what the previous sentence computes). Passing
`ζ^{(r+1)}` backwards through round `r`: gates `q→b'` have `q` as control and `CNOT Z_c CNOT = Z_c`,
contributing nothing; gates `a→q` have `q` as target and contribute `Z_{anc(a,r)}` with exponent
`|supp(a) ∩ ζ^{(r+1)}| = (H_X ζ^{(r+1)})_a`. By **(CSS)**, `H_X H_Z^⊤ = 0`, so
`H_X ζ^{(r+1)} = H_X γ` for every `r`. The condition `ζ|_{anc(a,·)} = 0` is therefore the single
condition `H_X γ = 0`, and `β` is unconstrained. The `ξ` conditions are vacuous (`ξ = 0`).

*X-half.* Back-propagate `X_{anc(a,r)}`. Each gate `a→q` has `anc(a)` as control and
`CNOT X_c CNOT = X_c X_t`, so the data vector gains `χ_{supp(a)}`. Inside round `r`, gates `q→b`
with `q` a control contribute `X_{anc(b,r)}` with exponent
`#{q ∈ supp(a)∩supp(b) : t(q→b) < t(a→q)} = c_{ab} ≡ 0` by **(MC)**. Set
`ξ^{(r)} := Σ_{r' ≥ r} H_X^⊤ α_{·,r'} ∈ S_X`. Passing backwards through an earlier round: gates
`a'→q` have `q` as target and `CNOT X_t CNOT = X_t`, contributing nothing; gates `q→b` contribute
`X_{anc(b,r')}` with exponent `(H_Z ξ^{(r'+1)})_b = 0`, since `ξ ∈ S_X ⊆ ker H_Z` by **(CSS)**. So
`ξ|_{anc(b,·)} = 0` automatically, and the only surviving condition is `ξ|_{data} = ξ^{(0)} = 0`,
i.e. `Σ_r H_X^⊤ α_{·,r} = 0`. The map `α ↦ H_X^⊤ Σ_r α_{·,r}` has image `S_X`, of dimension
`rank H_X`, giving the stated dimension. ∎
*Status: complete. Note where the hypotheses are spent: **(MC)** kills the intra-round cross terms
in both halves, **(CSS)** kills the inter-round cross terms in both halves. Both are needed; neither
substitutes for the other.*

**NUMERICAL 3.4.** Both closed forms, and the splitting `dim V = dim V_Z + dim V_X`, verified
exactly by back-propagation on 18 instances (3 codes × 2 schedules × `R ∈ {1,2,3}`), including a
code with a **dependent** X-generating set: 18/18, `0` disagreements (§11.3). The same closed forms
reproduce, value for value, all 18 rows of the independently computed table in
`artifacts/circdist_sat_window_amendment1_20260822.md` §4.

### 3.3 Detectors versus observables: a canonical split

Definition 2.10 measures `d_R` against a *chosen* set of parities called detectors. That choice is
not innocent: if `𝒟` is any complement of `span{λ^{(j)}}` in `V`, then replacing `𝒟` by
`𝒟' := {P + λ^{(1)}·c(P)}` changes which fault sets count as undetectable-and-logical, and can
change `d_R`. So `d_circ` is a function of `(circuit, fault model, detector/observable split)`, and
the split must be pinned down before Theorem T can be said to compute anything. The window
theorem's S3 ("enlarging the detector set can only decrease `d_circ`") is exactly the sentence its
review struck, for exactly this reason.

**Definition 3.5 (canonical detector space).** Consider the family of experiments
`C_R^Z(M; s)`, `s ∈ F₂^k`, differing only in the prepared logical basis state
`|s⟩_L := X_L^s |0⟩^{⊗n}`. A deterministic parity `P ∈ V` is a **detector** if its value is the same
in every member of the family, and an **observable direction** otherwise. Write `𝒟` for the space of
detectors.

This is the canonical split: detectors are exactly the parities a decoder may consult without
consulting the logical information, and `d_R` computed against `𝒟` is by construction independent of
which logical basis state was prepared.

**CONJECTURED 3.6.** In the notation of 3.3,
```
      𝒟 = 𝒟_Z ⊕ 𝒟_X ,      𝒟_Z = { (β,γ) : γ ∈ S_Z } ,      𝒟_X = V_X ,
      V_Z = 𝒟_Z ⊕ span{λ^{(1)},…,λ^{(k)}} ,      dim 𝒟_Z = |ℬ| R + rank H_Z .
```
Moreover
```
      𝒟_Z = span{ D_{b,r} : b ∈ ℬ, r ∈ {0,…,R} }          (EQUALITY, not containment),
      span{ D_{a,r} : a ∈ 𝒜, r ∈ {1,…,R−1} } ⊆ 𝒟_X ,       with codimension  dim leftker(H_X).
```

*Derivation.* The value of `P` on input `|s⟩_L` differs from its value on `|0⟩^{⊗n}` by the
commutation phase of the back-propagated Pauli with `X_L^s`, i.e. by
`Σ_j s_j ⟨ζ^{(0)}, χ_{X_L^{(j)}}⟩` for the `Z`-part (the `X`-part has `ξ^{(0)} = 0` by 3.3, so it
contributes nothing). Since `⟨χ_{supp(b)}, χ_{X_L^{(j)}}⟩ = 0` (checks commute with logicals) and
`ζ^{(0)} = γ + Σ_r H_Z^⊤β_{·,r}`, the condition is `⟨γ, χ_{X_L^{(j)}}⟩ = 0` for all `j`. Combined
with `γ ∈ ker H_X` from 3.3 and Standing fact 2.2 (`ker H_X = S_Z ⊕ span{χ_{Z_L^{(j)}}}`, with
`⟨χ_{Z_L^{(i)}}, χ_{X_L^{(j)}}⟩ = δ_{ij}`), this says exactly `γ ∈ S_Z`. Hence `𝒟_Z` as displayed,
`𝒟_X = V_X`, and `V_Z = 𝒟_Z ⊕ span{λ}` with the `λ^{(j)}` supplying the `k` missing directions.

*The Z-side equality.* Each `D_{b,r}` lies in `𝒟_Z`: for `r < R` it has `γ = 0 ∈ S_Z`; for `r = R`
it has `γ = χ_{supp(b)} ∈ S_Z`. Conversely the detectors `D_{b,r}`, `r ∈ {0,…,R−1}`, are
triangular in `β` (`D_{b,0} = m_{b,0}`, `D_{b,r} = m_{b,r} + m_{b,r−1}`), so their span contains
every `(β, 0)`; and the `D_{b,R}` contribute `γ`-parts spanning `{χ_{supp(b)}} = S_Z`. Dimensions
match: `|ℬ|R + rank H_Z`.

*The X-side codimension.* `span{D_{a,r} : r ∈ {1,…,R−1}} = F₂^𝒜 ⊗ Even(F₂^R)` has dimension
`|𝒜|(R−1)`, while `𝒟_X = V_X = {α : Σ_r α_{·,r} ∈ leftker H_X}` has dimension `|𝒜|R − rank H_X`;
the difference is `|𝒜| − rank H_X = dim leftker(H_X)`. The missing directions are represented by
`α_{·,0} = t ∈ leftker(H_X)∖0`, `α_{·,r} = 0` otherwise — i.e. by the parities `⊕_{a ∈ T} m_{a,0}`,
which are deterministic although each `m_{a,0}` is individually uniform. ∎ *Status: complete.*

> **This is clause S3′, derived rather than asserted, and sharper than the form the window
> amendment adopts.** The review's S3′ says the `D_{b,r}` are "maximal modulo the observables";
> 3.6 says they are *exactly* the canonical Z-side detector space `𝒟_Z`, with the observable
> directions canonically identified rather than chosen. The review's precision note — that
> `rank(D) = dim V − k` fails when `leftker(H_X) ≠ 0` — is here a corollary: the shortfall is
> `dim leftker(H_X)` and it sits entirely on the X-side.

**CONJECTURED 3.7 (the detector-set convention does not matter for `d_R^Z`).** `d_R^Z(M)` computed
against the canonical `𝒟` of Definition 3.5 equals `d_R^Z(M)` computed against the Definition-2.7
detector set.

*Derivation.* Definition 2.7's set is contained in `𝒟` (by 3.6), so a fault undetectable against `𝒟`
is undetectable against Definition 2.7's set, giving `d^{2.7} ≤ d^{𝒟}`. Conversely let `F` attain
`d^{2.7}` and put `F^X` as in 3.1. By 3.1(1) it flips the same `D_{b,r}` (none) and the same
observables (some), and by 3.6 those `D_{b,r}` span all of `𝒟_Z`, so `F^X` annihilates `𝒟_Z`; by
3.1(2) it flips no X-check record at all, so it annihilates `𝒟_X` — **including the redundancy
directions `⊕_{a∈T} m_{a,0}` that Definition 2.7 omits**. Hence `F^X` is undetectable against `𝒟`
and logical, with `|F^X| ≤ |F|`, so `d^{𝒟} ≤ d^{2.7}`. ∎ *Status: complete.*

**NUMERICAL 3.8.** In the 18 instances of 3.4: every Definition-2.7 detector lies in `𝒟`
(18/18); every `λ^{(j)}` lies in `V` but **not** in `𝒟` (18/18); `𝒟_Z = span{D_{b,r}}` exactly
(18/18); `𝒟_X = V_X` with `dim V_X − rank{D_{a,r}} = dim leftker(H_X)` (18/18, the value being `1`
for the dependent-generator code and `0` otherwise). §11.3.

> **Danger spot addressed: S3′ span subtleties with dependent checks.** The redundancy parities that
> a dependent generating set creates are *real* extra detectors, they are invisible to Definition
> 2.7, and they exist already at round 0 where the individual `m_{a,0}` are random. They do not
> affect `d_R^Z` — but the reason is 3.1(2) plus the *equality* in 3.6, not the struck sentence
> "enlarging the detector set can only decrease `d_circ`". Note also the asymmetry and why it is not
> a defect: on the **Z** side there is no analogous hole, because the round-0 absolute detector
> `D_{b,0}` puts every Z-side redundancy parity `⊕_{b∈T} m_{b,r} = ⊕_{b∈T} Σ_{r'≤r} D_{b,r'}` into
> the Definition-2.7 span automatically.

From here to §9, "fault" means an **X-sector** elementary fault (Lemma 3.1) and "detector" means a
Z-check detector `D_{b,r}`, `r ∈ {0,…,R}`; by 3.7 nothing is lost.

---

## 4. The state space

**Definition 4.1.** `Σ := Σ^Z := F₂^n / S_X`, with `[·]` the quotient map, `|Σ| = 2^{r_Z}`,
`r_Z = n − rank H_X`. `Σ` is written additively; `−σ = σ`.

**CONJECTURED 4.2 (the quotient is legitimate).** `H_Z` and each `λ^{(j)}` descend to `Σ`:
if `E + E' ∈ S_X` then `H_Z E = H_Z E'` and `|E ∩ supp(Z_L^{(j)})| ≡ |E' ∩ supp(Z_L^{(j)})|`.

*Derivation.* `H_Z H_X^⊤ = 0` gives the first; `|supp(a) ∩ supp(Z_L^{(j)})| ≡ 0` (an X-stabiliser
commutes with a logical `Z`) gives the second. ∎ *Status: complete.*

**CONJECTURED 4.3 (terminal classes).** `{σ ∈ Σ : H_Z σ = 0} = ker H_Z / S_X` has order `2^k`, and
its non-zero elements — exactly `2^k − 1` of them — are precisely the classes of terminal residuals
that are undetectable **and** logical. For `k = 1` there is exactly one, `[X_L]`.

*Derivation.* `dim(ker H_Z / S_X) = n − rank H_Z − rank H_X = k` (Standing fact 2.2). Given
`E ∈ ker H_Z`, `E ∉ S_X` iff some `λ^{(j)}(E) = 1`, again by 2.2. ∎ *Status: complete.*

**Remark 4.4 (what `Σ` is *not*).** `Σ` is a **sufficient** statistic (Lemma 6.4), not a proved
**minimal** one. The Nerode-minimal state space of the language of undetectable logicals is a
quotient of `Σ`, and this document does not compute it; see sub-claim **T-G2** (§12). Nothing in
Theorem T requires minimality: a non-minimal but correct state space gives the same
`u ⊙ A^{⊙R} ⊙ v`.

---

## 5. One-round data and the fault dictionary

**Definition 5.1.** For a one-round X-sector configuration `S` (all faults of `S` in one round):
```
      E(S) ∈ F₂^n     the residual data-X error at the end of that round,
      u(S) ∈ F₂^ℬ     the vector of flips that S induces in that round's own records m_{b,·},
```
both computed with a **zero** incoming data frame; and `λ^{(j)}(E) := |E ∩ supp(Z_L^{(j)})| mod 2`.
Both are `F₂`-linear in `S` (Lemma 2.9).

**Definition 5.2 (fault dictionary).** For `[δ] ∈ Σ`, `μ ∈ F₂^ℬ`,
```
      w_M([δ], μ) := min{ |S| : S a one-round X-sector configuration, [E(S)] = [δ], u(S) = μ } .
```
Well defined on classes by construction, and independent of the collision convention by Lemma 2.9.

**CONJECTURED 5.3 (round-independence).** `E`, `u`, `λ` and hence `w_M` do not depend on which round
`r ∈ {0,…,R−1}` the configuration sits in, nor on `R`.

*Derivation.* By T2 the rounds are verbatim repetitions with fault-location sets in
effect-preserving bijection; by Definition 2.8 every ancilla enters each round with a zero Pauli
frame, so a fault's propagation inside its own round sees the identical gate sequence with the
identical initial ancilla frame in every round. ∎ *Status: complete; this is where T2 is consumed.*

**CONJECTURED 5.4 (round transparency).** A data `X`-error `E` present at the start of a round is
unchanged at the end of that round, and its only effect on that round's records is to flip `m_{b,·}`
by `H_Z E`.

*Derivation.* By Definition 2.3 a data qubit is the **target** only of gates `a→q` and the
**control** only of gates `q→b`. An `x` on data qubit `q` is therefore never overwritten (targets
receive, controls keep) and propagates to `anc(b)` exactly once for each `b ∋ q`, flipping `m_{b,·}`
by `[q ∈ supp(b)]`. Summing over `q ∈ E` gives `(H_Z E)_b`. The `X`-ancillas are never targets and
carry zero incoming frame, so nothing flows back onto the data. ∎ *Status: complete. This is the
lemma the entire node rests on, and it is exactly where a schedule outside Definition 2.3 (flags,
cat states, repeated CNOTs, un-reset ancillas) breaks the analysis.*

**CONJECTURED 5.5 (finiteness, with an explicit bound).**
`w_M([δ], μ) ≤ min_{δ' ∈ [δ]} |δ'| + |μ| < ∞` for every `([δ], μ)`. In particular **every entry of
`A` is finite** and no state is unreachable.

*Derivation.* Two families of weight-1 faults.
*(i) Zero-voltage singletons.* For each data qubit `q` let `t*` be the last time step at which `q`
lies in a two-qubit gate (unique by legality). If that gate is `q→b`, take the two-qubit fault
`X⊗I` immediately after it; if it is `a→q`, take `I⊗X`. Either way the residual is `{q}`, and since
every gate `q→b'` has `t(q→b') ≤ t*` and has already executed, no `anc(b')` is reached: `u = 0`. If
`q` lies in no gate, take a single-qubit `X` at any of the `T ≥ 1` idle steps of `q`. So
`E = e_q`, `u = 0`.
*(ii) Pure record flips.* For each `b`, the classical flip of `m_{b,r}` has `E = 0`, `u = e_b`.
(Equivalently, and without using the classical-flip location: `anc(b)` is a target only, so an `X`
on `anc(b)` immediately after its last CNOT flips `m_{b,·}` and reaches no data qubit.)
Distinct data qubits have distinct `t*`-gates (every CNOT joins one data qubit to one ancilla), and
the record flips sit at distinct locations, so the union of `|δ'|` singletons and `|μ|` record flips
is a configuration of weight `|δ'| + |μ|`, or less after Lemma 2.9 merges a collision. ∎
*Status: complete. Scope note: finiteness consumes the availability of (i) and (ii); a fault model
lacking both two-qubit faults and classical record flips could produce `+∞` entries, and Theorem T
would still hold with `min ∅ = +∞`.*

**CONJECTURED 5.6 (the dictionary is exactly a transition weight).** For any one-round
configuration `S` in round `r` and any class `σ` of the incoming accumulated residual:
(i) `S` contributes weight `|S| ≥ w_M([E(S)], u(S))`; and (ii) for every pair `([δ], μ)` there is a
configuration `S` in round `r` with `[E(S)] = [δ]`, `u(S) = μ` and `|S| = w_M([δ], μ)`.
*Derivation.* (i) is the definition, (ii) is attainment of a minimum over a non-empty finite set
(non-empty by 5.5). Round-placement is immaterial by 5.3. ∎ *Status: complete.*

**Remark 5.7 (the shape of `A`, and pruning).** `A[σ,σ'] = w_M(σ'−σ, H_Z σ)` depends on the ordered
pair only through the *difference* `σ'−σ` and the *source syndrome* `H_Z σ`: `A` is a
**Toeplitz matrix over the group `Σ`, twisted by the source syndrome**. It is therefore determined
by `|Σ| · 2^{rank H_Z}` numbers rather than `|Σ|²`, and the system is literally a
one-letter tropical automaton on a group-labelled graph — which is the precise sense in which the
spacetime code here is a terminated time-invariant convolutional code with an **affine** (coset)
terminal condition, the identification the recon's route R5 flags as P5.1/P5.2. Since 5.5 makes
every state reachable, the meaningful reduction is not "delete unreachable states" but
**pruning to the optimal-path support**
`Σ_useful := { σ : (u ⊙ A^{⊙*})[σ] + (A^{⊙*} ⊙ v)[σ] ≤ d }`, everything outside which can be
deleted without changing any `d_R`.

---

## 6. The undetectability recursion, and where `u` and `v` come from

Fix `R ≥ 1` and an X-sector configuration `F` in `C_R^Z(M)`. Write `S_r` for its restriction to
round `r` (a one-round configuration; `F = ⊔_r S_r` and `|F| = Σ_r |S_r|` exactly, by T2 and Lemma
2.9). Define the **boundary states**
```
      σ_0 := [0] ,      σ_{r+1} := σ_r + [E(S_r)]      (r = 0,…,R−1),
```
so `σ_r` is the class of the accumulated residual data error present throughout round `r`, and
`σ_R` is the class of the terminal residual `E_tot(F) = Σ_r E(S_r)`.

**CONJECTURED 6.1 (time locality).** A fault `f` in round `r` flips exactly the detectors
`[u(f)]_r + [u(f) + H_Z E(f)]_{r+1}` and the observables by `λ(E(f))`.

*Derivation.* `m_{b,r}` is flipped by `u_b(f)`; for `r' > r` the data carries `E(f)` throughout
round `r'`, so by 5.4 `m_{b,r'}` is flipped by `(H_Z E(f))_b`, and the virtual `m_{b,R}` likewise
because the ideal readout sees `E(f)`. Substituting into `D_{b,r} = m_{b,r} + m_{b,r−1}` gives the
claim, the terms cancelling for `r' ≥ r+2`. The convention `m_{b,−1} = 0` makes `r = 0` an instance
of the same formula, and `r+1 ≤ R` is always a legitimate detector index. ∎ *Status: complete; both
temporal boundaries are consumed here.*

**CONJECTURED 6.2 (criterion (W), in state form).** `F` is undetectable in `C_R^Z(M)` **iff**
```
      u(S_r) = H_Z σ_r    for every r ∈ {0,…,R−1} ,     and     H_Z σ_R = 0 .          (W)
```

*Derivation.* By 5.4 and 6.1 the record `m_{b,r}` is flipped by `(H_Z σ_r)_b + u_b(S_r)` for
`r ≤ R−1`, and the virtual `m_{b,R}` by `(H_Z σ_R)_b`. So
`D_{b,r} = [(H_Z σ_r) + u(S_r)]_b + [(H_Z σ_{r−1}) + u(S_{r−1})]_b` for `1 ≤ r ≤ R−1`,
`D_{b,0} = [(H_Z σ_0) + u(S_0)]_b = u_b(S_0)`, and
`D_{b,R} = (H_Z σ_R)_b + [(H_Z σ_{R−1}) + u(S_{R−1})]_b`. All detectors vanish iff the sequence
`r ↦ H_Z σ_r + u(S_r)` is constant on `{0,…,R−1}` **and** agrees with `H_Z σ_R` at the right end,
while the `r = 0` instance pins the constant to `0` because `σ_0 = [0]`. That is (W). ∎
*Status: complete. This is the window theorem's Lemma 2.8 re-derived in state notation; the two
statements are the same, with `c_b(r−1) = (H_Z σ_r)_b` and `U_b(r) = u_b(S_r)`.*

**CONJECTURED 6.3 (the observable).** `F` is logical iff `σ_R ∉ {[0]}`, given `H_Z σ_R = 0`.
*Derivation.* The ideal readout is flipped by `E_tot(F)` (5.4), so `F` flips `λ^{(j)}` iff
`λ^{(j)}(E_tot) = 1`; by Standing fact 2.2 with `E_tot ∈ ker H_Z`, some `λ^{(j)}(E_tot) = 1` iff
`E_tot ∉ S_X` iff `σ_R ≠ [0]`. ∎ *Status: complete.*

**CONJECTURED 6.4 (sufficiency of the state).** In (W) and 6.3, the incoming accumulated residual
enters **only** through its class `σ_r ∈ Σ`, and the round-`r` constraint depends on nothing else.
*Derivation.* The constraint at round `r` is `u(S_r) = H_Z σ_r`, and `H_Z` descends to `Σ` (4.2);
the terminal condition is `H_Z σ_R = 0` and `σ_R ≠ [0]`, both functions of `σ_R` (4.2, 4.3); and the
state update `σ_{r+1} = σ_r + [E(S_r)]` is group translation. ∎ *Status: complete. This is Theorem
T(a).*

> **Derivation of the boundary vectors.** (W) has exactly two boundary instances, and each supplies
> exactly one of `u`, `v`.
>
> * **`r = 0`.** `D_{b,0} = m_{b,0}` is an **absolute** detector — it exists because `|0⟩^{⊗n}` is a
>   `+1` eigenstate of every `Z_{supp(b)}` — and it forces `u(S_0) = 0`. Equivalently: the state
>   before round `0` is `[0]` with certainty. That is `u[σ] = 0` iff `σ = [0]`, and the round-0
>   constraint is then *already* encoded in `A[[0], σ_1] = w_M(σ_1, H_Z[0]) = w_M(σ_1, 0)`. Nothing
>   further is needed.
> * **`r = R`.** The terminal ideal readout supplies `D_{b,R}`, which closes the recursion with
>   `H_Z σ_R = 0`; combined with 6.3 this is `v[σ] = 0` iff `H_Z σ = 0` and `σ ≠ [0]`.
>
> **Remark 6.5 (what each boundary buys, quantitatively).** Drop the round-0 detector (noisy or
> unknown initialisation). Then (W) becomes `u(S_r) = H_Z σ_r + κ` for an unconstrained constant
> `κ ∈ F₂^ℬ`, and the correct object is no longer a single `(u,A,v)` but the family
> `A_κ[σ,σ'] := w_M(σ'−σ, H_Z σ + κ)` with `d_R = min_κ ( u ⊙ A_κ^{⊙R} ⊙ v )` — equivalently a
> state space `Σ × F₂^ℬ` in which `κ` is carried as a constant component. Drop the terminal detector
> instead and `v` loses its first clause, becoming `v[σ] = 0` iff `σ ≠ [0]`, which is a *different*
> and generally smaller quantity. **Both boundaries are load-bearing, in different places**, and
> this is the precise form of the round-0/terminal asymmetry.
>
> **Remark 6.6 (detector window `w > 2`).** If detectors spanned `w` consecutive rounds, (W) would
> couple `u(S_r)` to the previous `w−2` rounds' record flips, and Theorem T(a) would be **false** as
> stated: the state would have to be enlarged to `Σ × (F₂^ℬ)^{w−2}`. Definition 2.7 fixes `w = 2`,
> which is exactly why no measurement memory appears in `Σ`. The recon's §3.7 sketch of the `w > 2`
> case is consistent with this and is out of scope here.

---

## 7. Theorem T(c): the two directions

> **CONJECTURED 7.1.** For every `(Q,M)` in the scope of T0–T3 and every `R ≥ 1`,
> `d_R^Z(M) = u ⊙ A^{⊙R} ⊙ v`.

*Derivation.*

**(≥) Projection.** Let `F` be undetectable and logical in `C_R^Z(M)` with `|F| = d_R^Z(M)`. By
Lemma 3.1 replace `F` by `F^X`, which is undetectable (against Definition 2.7's set, and by 3.7
against the canonical `𝒟`), logical, and of weight `≤ |F|`; minimality forces `|F^X| = |F|`, so we
may assume `F` is X-sector. Split `F = ⊔_{r} S_r` by round — legitimate and weight-exact because
Definition 2.8's location set is partitioned by round (T2) and Lemma 2.9 applies within each round.
Form the boundary states `σ_0 = [0], …, σ_R`. By Lemma 6.2, `u(S_r) = H_Z σ_r` for every
`r ≤ R−1` and `H_Z σ_R = 0`; by Lemma 6.3, `σ_R ≠ [0]`. Hence for each `r`,
```
      |S_r| ≥ w_M( [E(S_r)] , u(S_r) ) = w_M( σ_{r+1} − σ_r , H_Z σ_r ) = A[σ_r, σ_{r+1}]
```
by Definition 5.2 and 5.6(i), and `u[σ_0] = 0`, `v[σ_R] = 0`. Therefore
```
      d_R^Z(M) = |F| = Σ_r |S_r| ≥ u[σ_0] + Σ_r A[σ_r,σ_{r+1}] + v[σ_R] ≥ u ⊙ A^{⊙R} ⊙ v .
```

**(≤) Lifting.** Let `(σ_0,…,σ_R)` attain `u ⊙ A^{⊙R} ⊙ v` with finite value `W` (finite by 5.5 and
4.3: a finite-cost path exists since `k ≥ 1`). Finiteness of `u[σ_0]` gives `σ_0 = [0]`; finiteness
of `v[σ_R]` gives `H_Z σ_R = 0` and `σ_R ≠ [0]`. For each `r ∈ {0,…,R−1}` invoke 5.6(ii) to choose a
one-round configuration `S_r`, placed in round `r`, with
```
      [E(S_r)] = σ_{r+1} − σ_r ,     u(S_r) = H_Z σ_r ,     |S_r| = A[σ_r, σ_{r+1}] .
```
**This is the step that needs the state to be a sufficient statistic:** the required record-flip
vector `H_Z σ_r` is a function of the *class* `σ_r` alone (4.2), so it can be fixed before the actual
representative `Σ_{r'<r} E(S_{r'})` is known. Set `F := ⊔_r S_r`, a legitimate configuration of
weight `Σ_r |S_r| = W` because the rounds' location sets are disjoint (T2).

By induction the class of the accumulated residual before round `r` is exactly `σ_r`: true at
`r = 0`, and `[Σ_{r'≤r} E(S_{r'})] = σ_r + (σ_{r+1} − σ_r) = σ_{r+1}`. Hence `F`'s boundary states
are the chosen `σ_r`, and (W) holds by construction — `u(S_r) = H_Z σ_r` for `r ≤ R−1` and
`H_Z σ_R = 0` — so `F` is undetectable by 6.2; and `σ_R ≠ [0]` makes it logical by 6.3. Therefore
`d_R^Z(M) ≤ |F| = W = u ⊙ A^{⊙R} ⊙ v`.

Both inequalities give equality. ∎ *Derivation status: complete, relative to §2's model and §3, §5,
§6.*

**Remark 7.2 (`k = 1`).** By 4.3 the only state with `v` finite is `[X_L]`, so
`d_R^Z = (A^{⊙R})[[0],[X_L]]` — the recon's Claim 3.3 second sentence, now with the count `2^k − 1`
behind it.

**Remark 7.3 (what the two directions each consume).** Projection consumes sector decoupling (3.1),
the round partition of locations (T2), and (W)'s two boundary instances. Lifting consumes, in
addition, attainment (5.6(ii)) and — critically — that the *constraint* at round `r` is a function
of the class rather than of the representative (6.4). If `H_Z` did not descend to `Σ`, the lifting
direction would fail even though the projection direction would still hold, and the theorem would
degrade to an inequality. That asymmetry is the reason `Σ` must be a quotient by `S_X` and not by
anything larger.

---

## 8. Theorem T(d): both CSS sectors

**CONJECTURED 8.1.** The mirror of Definitions 2.6–2.11 under `𝒜 ↔ ℬ`, `X ↔ Z`, control ↔ target
carries every statement of §3–§7 to `C_R^X(M)`, giving `Σ^X = F₂^n / S_Z`,
`A^X[σ,σ'] = w_M^X(σ'−σ, H_X σ)`, `u^X[σ] = 0` iff `σ = [0]`, and `v^X[σ] = 0` iff `H_X σ = 0` and `σ ≠ [0]`, and
`d_R^X(M) = u^X ⊙ (A^X)^{⊙R} ⊙ v^X`. The mirror is compatible with scope clause T1 because (MC) is
mirror-symmetric (Definition 2.5: `c'_{ab} = c_{ab}` by (CSS)).

*Derivation.* The mirror is an isomorphism of the entire structure: it exchanges the roles of the
two ancilla families and of the two Pauli types, and Definitions 2.1–2.11 are stated symmetrically
under it once 2.5's asymmetric phrasing is seen to select the same class. No step of §3–§7 uses any
property that distinguishes the sectors beyond the labelling. ∎ *Status: complete; the (MC)
symmetry is the window amendment's Repair 3, which §2.5 re-derives.*

**CONJECTURED 8.2 (one system for both sectors).** On `Σ := Σ^Z ⊔ Σ^X` (disjoint union) put
`A := A^Z ⊕ A^X` (block diagonal, cross blocks `+∞`), `u := (u^Z, u^X)`, `v := (v^Z, v^X)`. Then
`u ⊙ A^{⊙R} ⊙ v = min(d_R^Z, d_R^X) = d_R(M)` for every `R ≥ 1`.
*Derivation.* Every finite-cost path stays inside one block, so the min-plus scalar is the minimum
of the two block scalars. ∎ *Status: complete, relative to the inherited aggregation convention T3
(= window sub-claim W-G1).*

> **Danger spot addressed: sector coupling, X faults triggering Z detectors via hooks.** A hook —
> one fault on `anc(a)` spreading `X` to several data qubits, some of which subsequently feed
> `anc(b)` inside the same round — is *not* a sector-coupling phenomenon: it is a single X-sector
> fault with `|E(f)| > 1` and possibly `u(f) ≠ 0`, and the dictionary records exactly that pair.
> Genuine sector coupling would be an `X`-type fault flipping an X-check record or a `Z`-type fault
> flipping a Z-check record, and Lemma 3.1 shows neither happens: `m_{b,r}` is a `Z`-basis
> measurement, flipped only by `x`-components; `m_{a,r}` is an `X`-basis measurement, flipped only
> by `z`-components; the terminal `Z` readout, only by `x`-components. A `Y` fault contributes to
> both sectors, and 3.1(3) is what lets the minimum be taken sector-purely without loss. The two
> sectors are therefore genuinely two independent min-plus systems, and `d_R` is their minimum
> rather than anything coupled — but note that this is a statement about *this* fault model and
> *this* observable set, and it is the place where a non-CSS gate or a `Y`-type ancilla measurement
> would break the block-diagonal structure of 8.2.

---

## 9. Theorem T(e): spectrum, and the window theorem re-derived from the algebra

Everything in §9 is proved **from `(u,A,v)`**, without using `artifacts/circdist_sat_window_theorem_20260822.md`.
Its purpose is twofold: to record the corollaries that come for free, and to give the window
theorem's three parts a second, algebraically independent derivation.

**CONJECTURED 9.1 (zero-cost transitions).** `A[σ,σ'] = 0` **iff** `σ = σ'` and `H_Z σ = 0`.
*Derivation.* `w_M([δ],μ) = 0` iff the empty configuration qualifies, i.e. `[δ] = [0]` and `μ = 0`;
and `μ = H_Z σ`. ∎ *Status: complete.*

**Corollary 9.2 (spectrum).** All entries of `A` are finite (5.5), so `A` is irreducible; all
weights are `≥ 0` and `A` has a zero-weight loop at `[0]`, so the min-plus eigenvalue is
`λ_⊙(A) = 0`; the critical graph is exactly the set of `2^k` self-loops at `{σ : H_Z σ = 0}` (4.3),
whose cyclicity is `1`. By the cyclicity theorem (ASSUMPTION A1 below), `A^{⊙(R+1)} = A^{⊙R}` for
all `R` beyond some transient — `A^{⊙R}` is eventually **constant**, not merely eventually periodic.
*The recon's "`2^{2k}` self-loops" is corrected to `2^k`.*

**Corollary 9.3 (ceiling, `d_R ≤ d`).** For every `R ≥ 1`, `d_R^Z(M) ≤ d_X` and hence
`d_R(M) ≤ d`.
*Derivation.* Take `w ∈ ker H_Z ∖ S_X` with `|w| = d_X` (non-empty by T0 and 2.2) and put
`σ := [w] ≠ [0]`, `H_Z σ = 0`. By 5.5, `A[[0], σ] ≤ w_M(σ, 0) ≤ |w| = d_X`; by 9.1,
`A[σ,σ] = 0`. The path `[0] → σ → σ → … → σ` of length `R` has cost `≤ d_X` and `v[σ] = 0`. Mirror
for `d_R^X ≤ d_Z`. ∎ *Status: complete; this is the window theorem's 2.11+2.12 in transfer form.*

**Corollary 9.4 (monotonicity — window part (i)).** `d_{R+1}(M) ≤ d_R(M)` for every `R ≥ 1`.
*Derivation.* `v[σ] < ∞` implies `H_Z σ = 0` implies `A[σ,σ] = 0` (9.1). So
`(A ⊙ v)[σ] ≤ A[σ,σ] + v[σ] = v[σ]`, i.e. `A ⊙ v ≤ v` entrywise; multiplying on the left by
`u ⊙ A^{⊙R}` (min-plus multiplication is monotone) gives `d_{R+1} ≤ d_R`. Same in each block. ∎
*Status: complete. Physically this is "append a fault-free round"; algebraically it is a
zero-cost self-loop at a terminal state, and the round-`R` **detector meaning shift** of the window
theorem's §3.1 — `D_{b,R}` compares the ideal readout to `m_{b,R−1}` in `C_R`, but two genuine
measurements in `C_{R+1}` — is invisible here precisely because round transparency (5.4) is already
built into `A`.*

**Corollary 9.5 (path compression — window part (ii)).** Every zero-cost step of a path is a
self-loop (9.1) and may be **deleted**, yielding a path of length one shorter, the same endpoints
and the same cost. Hence, if `d_R(M) = W`, an optimal `R`-path has at most `W` steps of positive
cost, so there is `R' ≤ min(R, W)` with `d_{R'}(M) ≤ W = d_R(M)`; with 9.4 this forces
`d_{R'} = d_R`. *Status: complete. This is the transfer-language form of contiguity: "no fault-free
round strictly inside a minimum-weight witness" becomes "no zero-cost step inside an optimal
path", and the deletion is literally matrix-power truncation.*

**Corollary 9.6 (window part (iii)).** `(d_R)_{R≥1}` is non-increasing in `[1,d]`, hence eventually
constant with `d_∞ = min_R d_R`; `d_R = d_d` for every `R ≥ d`, so `d_∞ = d_d`; and
`R_stab ≤ d_∞ ≤ d`.
*Derivation.* The first clause is 9.4 + 9.3. For `R ≥ d`: by 9.5 there is `R' ≤ min(R, d_R) ≤ d`
with `d_{R'} = d_R`; monotonicity gives `d_d ≤ d_{R'} = d_R ≤ d_d` (the last by 9.4 since `R ≥ d`),
so `d_R = d_d`. For `R_stab`: put `R := R_stab`, so `d_R = d_∞`; by 9.5 there is `R' ≤ min(R, d_∞)`
with `d_{R'} = d_∞`, and minimality of `R_stab` forces `R' ≥ R_stab = R`, hence `R = R' ≤ d_∞`. ∎
*Status: complete.*

> **Consistency check, stated as such.** Corollaries 9.4–9.6 reproduce parts (i), (ii)-in-effect and
> (iii) of `artifacts/circdist_sat_window_theorem_20260822.md`, including `d_∞ = d_d` and
> `R_stab ≤ d_∞ ≤ d`, from a construction that shares with it only the model of §2 and the two
> lemmas 5.4 and 6.2. **This is corroboration, not certification:** both derivations are mine-side
> and neither is independently reviewed, and a shared error in the model of §2 or in round
> transparency would survive both. What it does rule out is an error confined to one of the two
> argument styles.

**ASSUMPTIONS used in §9, with their load-bearing status.**

**A1 — cyclicity theorem for min-plus matrix powers.** For irreducible `A` there exist `T ≥ 0` and
`γ ≥ 1` with `A^{⊙(t+γ)} = λ^{⊙γ} ⊙ A^{⊙t}` for `t ≥ T`, `λ` the eigenvalue and `γ` the cyclicity
of the critical graph. *Source:* Cohen–Dubois–Quadrat–Viot, INRIA RR-191 (1983) / IEEE TAC
30(3):210–220 (1985); textbook form Baccelli–Cohen–Olsder–Quadrat, *Synchronization and Linearity*
(Wiley 1992), **Definition 3.111 + Theorem 3.112** — **not** Theorem 3.109, despite that number
circulating widely; refinement Butkovič, *Max-linear Systems* (Springer 2010), Thm 8.3.6
(Nachtigall, `T_c(A) ≤ n²`). *Load-bearing for:* the phrase "eventually constant" in 9.2 **only**.
Corollaries 9.3–9.6 do not use it: 9.5 gives the scalar transient `≤ d` directly, which is
incomparably better than `n² = 4^{r_Z}`. *Bibliographic status: inherited from
`artifacts/circdist_sat_recon_20260820.md` §6 A1, which reports it as checked in that session; not
re-fetched here, and not load-bearing.*

**A2 — no transient bound in the dimension alone.** Nowak–Charron-Bost, arXiv:1405.3458, Thm 5.4:
no upper bound on the transient in terms of the matrix dimension alone exists in general.
*Load-bearing for:* the claim that 9.5's window is a genuine gain over generic tropical theory —
generic theory cannot deliver an `r_Z`-free bound; 9.5 can, because `λ_⊙ = 0` exactly and weights
are integers capped at `d`. *Status: inherited, as A1.*

**A3 — the one-letter boundary.** For powers of a **single** matrix the tropical theory is
decidable and polynomial (Gaubert, INRIA RR-2162 (1994); Molnárová–Pribiš, DAM 103:167–175 (2000),
`O(n³)` period); equality of tropical rational series over **two or more** letters is undecidable
(Krob, IJAC 4(3):405–426 (1994)). *Load-bearing for:* the scope statement that Theorem T's
automaton is a **one-letter** automaton because the rounds are verbatim repetitions (T2). Any
generalisation to non-identical rounds (alternating schedules, drifting layouts) crosses the Krob
boundary and loses the generic decidability guarantee, and this should be recorded on the node.
*Status: inherited, as A1.*

---

## 10. The four known danger spots, itemised

| danger | where it is handled | one-line resolution |
|---|---|---|
| **sector coupling** (X faults triggering Z detectors via hooks) | Lemma 3.1; §8 box | Hooks are ordinary X-sector faults with `|E(f)| > 1`; genuine cross-sector triggering is impossible because `m_{b,·}` is a `Z`-measurement and `m_{a,·}` an `X`-measurement, and `Y` faults are handled by weight-non-increasing projection to the X-part. |
| **round-0 / terminal detector meaning shift** (round transparency) | 5.4, 6.1, 6.2, Remark 6.5, Cor. 9.4 | The round-0 detector is absolute (`m_{b,−1} = 0`) and pins the recursion's constant to `0`, giving `u = 1_{[0]}`; the terminal detector is the ideal readout, giving `v`'s syndrome clause. The `C_R`-vs-`C_{R+1}` change of meaning at index `R` is neutralised by round transparency, which is already inside `A`. Each boundary is load-bearing in a *different* place, and Remark 6.5 states exactly what each one buys. |
| **collision handling** (one location, one Pauli) | Lemma 2.9; §7 both directions | Weight is measured on configurations, not multisets; the two agree because faults at a shared location merge into one at strictly lower weight. Across rounds no collision is possible (T2), so `|F| = Σ_r |S_r|` **exactly** — which is what makes the weight additive and hence min-plus the right semiring. |
| **S3′ span subtleties with dependent checks** | §3.2–§3.3, esp. 3.6, 3.7 | Dependent `𝒜` creates real detectors (`⊕_{a∈T} m_{a,0}`) invisible to Definition 2.7, and they exist at round 0 where the individual records are random. `d_R^Z` is unaffected — because the Definition-2.7 Z-detectors span `𝒟_Z` **exactly** and the projected witness `F^X` flips no X-record whatsoever. The Z-side has no analogous hole because the round-0 absolute detector absorbs every Z-side redundancy parity. |

---

## 11. NUMERICAL corroboration

**Nothing in §11 is used by any derivation in §3–§9.** These are independent checks that the
theorem's conclusions hold where they can be tested exhaustively. The `d = 3` implementation of
`artifacts/circdist_sat_recon_20260820.md` §7 was **not** read, imported or run; the program of
§11.4 was written for this session from the definitions of §2.

**Scope, stated.**
* Codes: Steane `[[7,1,3]]` (Hamming checks `{3456, 1256, 0246}`); rotated surface `[[9,1,3]]`
  (`𝒜 = {12, 0134, 4578, 67}`, `ℬ = {03, 1245, 3467, 58}`, `Z_L = {0,1,2}`, `X_L = {0,3,6}`); and
  **`steane+redX`**, Steane with `𝒜` enlarged by the sum of its three X-checks (`{0,1,3,6}`) — in
  scope of T0, dependent by construction, `dim leftker(H_X) = 1`. The Steane Z-memory is **not
  graph-like**, so the hypergraph case is exercised.
* Schedules: two non-interleaved (Z-block-first, X-block-first, one CNOT per time step, `T = 24`
  resp. `T = 28`) and two **interleaved** depth-4 rotated-surface schedules obtained by enumerating
  all `24 × 24` corner-order pairs and keeping those that are legal **and** (MC) — `16` of `576`
  survive, and the two used are `(NW,NE,SW,SE)/(NW,NE,SW,SE)` and `(SW,NW,SE,NE)/(SW,NW,SE,NE)`,
  which give *different* `d_R` per sector and so exercise hook misalignment.
* Both CSS sectors for every schedule, via the mirror of 8.1 run through the identical code path.
* `R ∈ {1,2,3}`; exhaustive minimum-weight search to weight `4` (all instances resolve at `≤ 3`,
  so the searches are exhaustive at the reported minimum).
* **Not covered:** `d ≥ 5`, genuine qLDPC instances, `k > 1`, `R > 3`, and any claim about
  `R_stab ≥ 2`. This is a check of the *representation*, not a delivery of
  `CIRCDIST.sat.instances`.

### 11.1 Ground truth versus transfer

The two arms share only the circuit layout.

* **Ground truth.** Direct multi-round simulation of `C_R^σ(M)` with an explicit `F₂` symplectic
  frame over all `n + |𝒜| + |ℬ|` qubits per round, with **all 15** two-qubit Paulis, **all 3**
  single-qubit Paulis at idle and preparation locations, and classical flips of **both** record
  types; detectors are the full Definition-2.7 set (`D_{b,r}` for `r ∈ {0,…,R}` **and** `D_{a,r}`
  for `r ∈ {1,…,R−1}`), and the observable is `λ`. Single-fault columns are deduplicated and the
  minimum-weight undetectable logical is found by meet-in-the-middle over columns (valid at the
  reported minimum by Lemma 2.9, as argued in the program's header).
* **Transfer.** `Σ = F₂^n/S_X` enumerated by coset minima; the one-round X-sector columns `(δ,μ)`
  obtained by simulating **one** round; `w_M` by exact BFS over all `2^{n+|ℬ|}` targets;
  `A[σ,σ'] = min_{g ∈ S_X} w(σ+σ'+g, H_Z σ)`; `u`, `v` as in Theorem T; `u ⊙ A^{⊙R} ⊙ v` by
  min-plus vector iteration.

**NUMERICAL 11.1.** **16 / 16** (schedule, sector) instances agree with the ground truth at every
`R ∈ {1,2,3}` — `48 / 48` values, `0` disagreements. In every instance `A` has **all entries
finite** and **exactly `2` zero-cost self-loops** (`= 2^k` with `k = 1`), as Corollary 9.2 predicts.

### 11.2 Parity spaces and the detector convention

**NUMERICAL 11.2.** On 18 instances (3 codes × 2 schedules × `R ∈ {1,2,3}`), computed exactly by
back-propagation with no sampling: `dim V_Z = |ℬ|R + n − rank H_X` (18/18);
`dim V_X = |𝒜|R − rank H_X` (18/18); `V = V_Z ⊕ V_X` (18/18); `dim 𝒟_Z = |ℬ|R + rank H_Z` and
`𝒟_Z = span{D_{b,r}}` **exactly** (18/18); `rank{D_{b,r}} + 1 = dim V_Z` when `k = 1`, i.e. `λ` is
deterministic but is **not** a detector (18/18); every Definition-2.7 detector lies in `𝒟` (18/18);
`𝒟_X = V_X` with `dim V_X − rank{D_{a,r}} = dim leftker(H_X)`, the value being `1` exactly on the
dependent-generator code (18/18).

### 11.3 Output, verbatim

```text
interleaved depth-4 surface schedules, legal AND (MC): 16 of 576
  e.g. (('NW', 'NE', 'SW', 'SE'), ('NW', 'NE', 'SW', 'SE')) | (('SW', 'NW', 'SE', 'NE'), ('SW', 'NW', 'SE', 'NE'))

instance                       sec MC   brute d_R        transfer d_R     match
steane713/blkZ                 Z   yes  [2, 2, 2]        [2, 2, 2]        OK
steane713/blkZ                 X   yes  [2, 2, 2]        [2, 2, 2]        OK
steane713/blkX                 Z   yes  [2, 2, 2]        [2, 2, 2]        OK
steane713/blkX                 X   yes  [2, 2, 2]        [2, 2, 2]        OK
surface913/blkZ                Z   yes  [3, 3, 3]        [3, 3, 3]        OK
surface913/blkZ                X   yes  [2, 2, 2]        [2, 2, 2]        OK
surface913/blkX                Z   yes  [3, 3, 3]        [3, 3, 3]        OK
surface913/blkX                X   yes  [2, 2, 2]        [2, 2, 2]        OK
steane+redX/blkZ               Z   yes  [2, 2, 2]        [2, 2, 2]        OK
steane+redX/blkZ               X   yes  [2, 2, 2]        [2, 2, 2]        OK
steane+redX/blkX               Z   yes  [2, 2, 2]        [2, 2, 2]        OK
steane+redX/blkX               X   yes  [2, 2, 2]        [2, 2, 2]        OK
surface913/ilv0                Z   yes  [3, 3, 3]        [3, 3, 3]        OK
surface913/ilv0                X   yes  [2, 2, 2]        [2, 2, 2]        OK
surface913/ilv1                Z   yes  [2, 2, 2]        [2, 2, 2]        OK
surface913/ilv1                X   yes  [3, 3, 3]        [3, 3, 3]        OK

transfer arm structure:
  steane713/blkZ/Z                   |Sigma|=16   zero-cost self-loops=2   all A entries finite=True
  steane713/blkZ/X                   |Sigma|=16   zero-cost self-loops=2   all A entries finite=True
  steane713/blkX/Z                   |Sigma|=16   zero-cost self-loops=2   all A entries finite=True
  steane713/blkX/X                   |Sigma|=16   zero-cost self-loops=2   all A entries finite=True
  surface913/blkZ/Z                  |Sigma|=32   zero-cost self-loops=2   all A entries finite=True
  surface913/blkZ/X                  |Sigma|=32   zero-cost self-loops=2   all A entries finite=True
  surface913/blkX/Z                  |Sigma|=32   zero-cost self-loops=2   all A entries finite=True
  surface913/blkX/X                  |Sigma|=32   zero-cost self-loops=2   all A entries finite=True
  steane+redX/blkZ/Z                 |Sigma|=16   zero-cost self-loops=2   all A entries finite=True
  steane+redX/blkZ/X                 |Sigma|=16   zero-cost self-loops=2   all A entries finite=True
  steane+redX/blkX/Z                 |Sigma|=16   zero-cost self-loops=2   all A entries finite=True
  steane+redX/blkX/X                 |Sigma|=16   zero-cost self-loops=2   all A entries finite=True
  surface913/ilv0/Z                  |Sigma|=32   zero-cost self-loops=2   all A entries finite=True
  surface913/ilv0/X                  |Sigma|=32   zero-cost self-loops=2   all A entries finite=True
  surface913/ilv1/Z                  |Sigma|=32   zero-cost self-loops=2   all A entries finite=True
  surface913/ilv1/X                  |Sigma|=32   zero-cost self-loops=2   all A entries finite=True

parity-space dimensions (Z-memory), closed forms vs computed:
code           sched R   dimV dimVZ   fVZ dimDZ   fDZ  rkDb dimVX   fVX dimDX  rkDa   lk all
steane713      blkZ  1      7     7     7     6     6     6     0     0     0     0    0 True
steane713      blkZ  2     13    10    10     9     9     9     3     3     3     3    0 True
steane713      blkZ  3     19    13    13    12    12    12     6     6     6     6    0 True
steane713      blkX  1      7     7     7     6     6     6     0     0     0     0    0 True
steane713      blkX  2     13    10    10     9     9     9     3     3     3     3    0 True
steane713      blkX  3     19    13    13    12    12    12     6     6     6     6    0 True
surface913     blkZ  1      9     9     9     8     8     8     0     0     0     0    0 True
surface913     blkZ  2     17    13    13    12    12    12     4     4     4     4    0 True
surface913     blkZ  3     25    17    17    16    16    16     8     8     8     8    0 True
surface913     blkX  1      9     9     9     8     8     8     0     0     0     0    0 True
surface913     blkX  2     17    13    13    12    12    12     4     4     4     4    0 True
surface913     blkX  3     25    17    17    16    16    16     8     8     8     8    0 True
steane+redX    blkZ  1      8     7     7     6     6     6     1     1     1     0    1 True
steane+redX    blkZ  2     15    10    10     9     9     9     5     5     5     4    1 True
steane+redX    blkZ  3     22    13    13    12    12    12     9     9     9     8    1 True
steane+redX    blkX  1      8     7     7     6     6     6     1     1     1     0    1 True
steane+redX    blkX  2     15    10    10     9     9     9     5     5     5     4    1 True
steane+redX    blkX  3     22    13    13    12    12    12     9     9     9     8    1 True

ALL transfer==brute : True
ALL parity formulas : True
elapsed 5.1s
```

### 11.4 The program, verbatim

```python
"""CIRCDIST.sat.transfer -- exact corroboration of the min-plus transfer theorem.

Ground truth is DIRECT multi-round simulation of C_R^sigma(M) with an explicit F_2
symplectic frame and the full Definition-1.9 detector set (both check types, both
temporal boundaries).  The transfer arm builds Sigma = F_2^n/rowspace(H_X), the
one-round dictionary w_M(delta,mu) by exact BFS, A[s,s'] = w_M(s'-s, H_Z s),
u = indicator([0]), v = indicator(H_Z s = 0 and s != 0), and computes
u (min-plus) A^R v.  The two arms share no code path beyond the circuit layout.

No stim, no external library, no sampling.
"""
import itertools, sys, time
from collections import deque

# ---------------------------------------------------------------- codes
STEANE = [[3,4,5,6],[1,2,5,6],[0,2,4,6]]
SURF_X = [[1,2],[0,1,3,4],[4,5,7,8],[6,7]]
SURF_Z = [[0,3],[1,2,4,5],[3,4,6,7],[5,8]]
CODES = {
 'steane713'   : dict(n=7, A=[list(x) for x in STEANE], B=[list(x) for x in STEANE],
                      ZL=[0,1,2], XL=[0,1,2]),
 'surface913'  : dict(n=9, A=[list(x) for x in SURF_X], B=[list(x) for x in SURF_Z],
                      ZL=[0,1,2], XL=[0,3,6]),
 'steane+redX' : dict(n=7, A=[list(x) for x in STEANE]+[[0,1,3,6]],
                      B=[list(x) for x in STEANE], ZL=[0,1,2], XL=[0,1,2]),
}

def rank2(vs):
    basis = []
    for v in vs:
        for b in basis: v = min(v, v ^ b)
        if v: basis.append(v); basis.sort(reverse=True)
    return len(basis)

def mask(sup):
    m = 0
    for q in sup: m |= 1 << q
    return m

# ---------------------------------------------------------------- schedules
def sched_blocks(A, B, order):
    """non-interleaved, one CNOT per time step; order 'Z' = all q->b first."""
    zb = [('qb', j, q) for j in range(len(B)) for q in B[j]]
    xb = [('aq', i, q) for i in range(len(A)) for q in A[i]]
    ops = zb + xb if order == 'Z' else xb + zb
    return [[op] for op in ops]                      # one op per time step

CORNERS = ['NW','NE','SW','SE']
SURF_SLOT_X = {0:{'SW':1,'SE':2}, 1:{'NW':0,'NE':1,'SW':3,'SE':4},
               2:{'NW':4,'NE':5,'SW':7,'SE':8}, 3:{'NW':6,'NE':7}}
SURF_SLOT_Z = {0:{'NE':0,'SE':3}, 1:{'NW':1,'NE':2,'SW':4,'SE':5},
               2:{'NW':3,'NE':4,'SW':6,'SE':7}, 3:{'NW':5,'SW':8}}

def sched_corners(piX, piZ):
    """interleaved rotated-surface schedule, depth 4: check g acts on slot pi^-1(t) at step t."""
    steps = [[] for _ in range(4)]
    for i, slots in SURF_SLOT_X.items():
        for t, c in enumerate(piX):
            if c in slots: steps[t].append(('aq', i, slots[c]))
    for j, slots in SURF_SLOT_Z.items():
        for t, c in enumerate(piZ):
            if c in slots: steps[t].append(('qb', j, slots[c]))
    return steps

# ---------------------------------------------------------------- instance
class Inst:
    def __init__(self, n, A, B, ZL, steps, name, XL=None):
        self.n, self.A, self.B, self.ZL, self.steps, self.name = n, A, B, ZL, steps, name
        self.XL = XL or []
        self.na, self.nb = len(A), len(B)
        self.Q = n + self.na + self.nb
        self.T = len(steps)
        # legality
        for t, ops in enumerate(steps):
            used = []
            for (k, idx, q) in ops:
                c, tt = (self.ancA(idx), q) if k == 'aq' else (q, self.ancB(idx))
                used += [c, tt]
            assert len(used) == len(set(used)), 'illegal schedule at step %d' % t
        # times
        self.tA, self.tB = {}, {}
        for t, ops in enumerate(steps):
            for (k, idx, q) in ops:
                (self.tA if k == 'aq' else self.tB)[(idx, q)] = t
        # (CSS) and (MC)
        for i in range(self.na):
            for j in range(self.nb):
                assert len(set(A[i]) & set(B[j])) % 2 == 0, 'CSS violated'
        self.mc = all(sum(1 for q in set(A[i]) & set(B[j])
                          if self.tB[(j,q)] < self.tA[(i,q)]) % 2 == 0
                      for i in range(self.na) for j in range(self.nb))
    def ancA(self, i): return self.n + i
    def ancB(self, j): return self.n + self.na + j

# ---------------------------------------------------------------- simulation
def run_round(I, xf, zf, rf):
    """one round; rf maps location-key -> pauli.  Returns (xf,zf) on data and record flips."""
    for key, val in rf.items():
        if key[0] == 'prep':
            q = key[1]; xf ^= val[0] << q; zf ^= val[1] << q
    for t in range(I.T):
        for (k, idx, q) in I.steps[t]:
            c, tt = (I.ancA(idx), q) if k == 'aq' else (q, I.ancB(idx))
            if (xf >> c) & 1: xf ^= 1 << tt
            if (zf >> tt) & 1: zf ^= 1 << c
        for key, val in rf.items():
            if key[0] == 'cnot' and key[1] == t:
                c, tt = key[2]
                xf ^= (val[0] << c) | (val[2] << tt)
                zf ^= (val[1] << c) | (val[3] << tt)
            elif key[0] == 'idle' and key[1] == t:
                q = key[2]; xf ^= val[0] << q; zf ^= val[1] << q
    mb = [(xf >> I.ancB(j)) & 1 for j in range(I.nb)]
    ma = [(zf >> I.ancA(i)) & 1 for i in range(I.na)]
    for key in rf:
        if key[0] == 'mflipB': mb[key[1]] ^= 1
        if key[0] == 'mflipA': ma[key[1]] ^= 1
    m = (1 << I.n) - 1
    return xf & m, zf & m, mb, ma

def column(I, R, r_f, rf):
    """detector vector + observable bit of the single fault rf placed in round r_f."""
    xf = zf = 0; recB = []; recA = []
    for r in range(R):
        xf, zf, mb, ma = run_round(I, xf, zf, rf if r == r_f else {})
        recB.append(mb); recA.append(ma)
    ro = [(xf >> q) & 1 for q in range(I.n)]
    bits = []
    for j in range(I.nb):
        for r in range(R + 1):
            if r == 0:   bits.append(recB[0][j])
            elif r < R:  bits.append(recB[r][j] ^ recB[r-1][j])
            else:        bits.append((sum(ro[q] for q in I.B[j]) % 2) ^ recB[R-1][j])
    for i in range(I.na):
        for r in range(1, R): bits.append(recA[r][i] ^ recA[r-1][i])
    obs = sum(ro[q] for q in I.ZL) % 2
    v = 0
    for b in bits: v = (v << 1) | b
    return (v << 1) | obs, len(bits)

P2 = [(a,b,c,d) for a in (0,1) for b in (0,1) for c in (0,1) for d in (0,1)][1:]
P1 = [(1,0),(0,1),(1,1)]

def faults(I, xsector):
    out = []
    for t in range(I.T):
        used = set()
        for (k, idx, q) in I.steps[t]:
            c, tt = (I.ancA(idx), q) if k == 'aq' else (q, I.ancB(idx))
            used |= {c, tt}
            ps = [(1,0,0,0),(0,0,1,0),(1,0,1,0)] if xsector else P2
            for p in ps: out.append(({('cnot', t, (c, tt)): p}, ))
        for q in range(I.Q):
            if q not in used:
                ps = [(1,0)] if xsector else P1
                for p in ps: out.append(({('idle', t, q): p}, ))
    for q in range(I.n, I.Q):
        ps = [(1,0)] if xsector else P1
        for p in ps: out.append(({('prep', q): p}, ))
    for j in range(I.nb): out.append(({('mflipB', j): 1}, ))
    if not xsector:
        for i in range(I.na): out.append(({('mflipA', i): 1}, ))
    return [f[0] for f in out]

# ---------------------------------------------------------------- brute force d_R
def brute_dR(I, R, cap=4):
    fl = faults(I, xsector=False)
    cols = set()
    for r in range(R):
        for rf in fl:
            c, _ = column(I, R, r, rf)
            if c: cols.add(c)
    cols = sorted(cols)
    target = 1                                    # zero detectors, observable flipped
    best = {0: 0}
    for c in cols:
        if c not in best or best[c] > 1: best[c] = 1
    lvl2 = dict(best)
    for i, a in enumerate(cols):
        for b in cols[i+1:]:
            s = a ^ b
            if s and (s not in lvl2 or lvl2[s] > 2): lvl2[s] = 2
    ans = cap + 1
    for s, w in lvl2.items():
        o = lvl2.get(s ^ target)
        if o is not None and w + o < ans: ans = w + o
    return ans if ans <= cap else None, len(cols)

# ---------------------------------------------------------------- transfer arm
def transfer(I, Rmax):
    n, nb = I.n, I.nb
    fl = faults(I, xsector=True)
    cols = set()
    for rf in fl:
        xf, zf, mb, ma = run_round(I, 0, 0, rf)
        mu = 0
        for j in range(nb): mu |= mb[j] << j
        c = xf | (mu << n)
        if c: cols.add(c)
    cols = sorted(cols)
    size = 1 << (n + nb)
    dist = [-1] * size; dist[0] = 0; dq = deque([0])
    while dq:
        s = dq.popleft()
        for c in cols:
            t = s ^ c
            if dist[t] < 0: dist[t] = dist[s] + 1; dq.append(t)
    SXrows = [mask(a) for a in I.A]
    SX = {0}
    for rrow in SXrows: SX |= {s ^ rrow for s in SX}
    SX = sorted(SX)
    canon = {}
    for E in range(1 << n):
        if E not in canon:
            cl = min(E ^ s for s in SX)
            for s in SX: canon[E ^ s] = cl
    Sig = sorted(set(canon.values()))
    idx = {s: i for i, s in enumerate(Sig)}
    def HZ(E):
        v = 0
        for j, b in enumerate(I.B):
            if bin(E & mask(b)).count('1') % 2: v |= 1 << j
        return v
    INF = float('inf')
    Amat = [[INF] * len(Sig) for _ in Sig]
    for s in Sig:
        mu = HZ(s)
        for sp in Sig:
            best = INF
            for g in SX:
                d = dist[(s ^ sp ^ g) | (mu << n)]
                if d >= 0 and d < best: best = d
            Amat[idx[s]][idx[sp]] = best
    zself = [s for s in Sig if Amat[idx[s]][idx[s]] == 0]
    allfinite = all(Amat[i][j] < INF for i in range(len(Sig)) for j in range(len(Sig)))
    vvec = [0 if (HZ(s) == 0 and s != 0) else INF for s in Sig]
    vec = [0 if s == 0 else INF for s in Sig]
    out = []
    for R in range(1, Rmax + 1):
        nv = [INF] * len(Sig)
        for i in range(len(Sig)):
            if vec[i] == INF: continue
            for j in range(len(Sig)):
                t = vec[i] + Amat[i][j]
                if t < nv[j]: nv[j] = t
        vec = nv
        out.append(min(vec[i] + vvec[i] for i in range(len(Sig))))
    return out, len(Sig), len(zself), allfinite, len(cols)

# ---------------------------------------------------------------- parity spaces
def parity_spaces(I, R):
    """dim of deterministic-parity spaces, by exact back-propagation."""
    n, na, nb, T = I.n, I.na, I.nb, I.T
    gates = []
    for r in range(R):
        for t in range(T):
            for (k, idx, q) in I.steps[t]:
                if k == 'aq': gates.append((n + r*(na+nb) + idx, q, 'aq'))
                else:         gates.append((q, n + r*(na+nb) + na + idx, 'qb'))
    NQ = n + R*(na+nb)
    recs = []
    for r in range(R):
        for i in range(na): recs.append(('a', i, r))
        for j in range(nb): recs.append(('b', j, r))
    for q in range(n): recs.append(('ro', q))
    SXb = [mask(a) for a in I.A]; SZb = [mask(b) for b in I.B]
    rkHX, rkHZ = rank2(SXb), rank2(SZb)
    XLm = mask(I.XL)
    obstruct_V, obstruct_D = [], []
    for key in recs:
        if key[0] == 'a':   x, z = 1 << (n + key[2]*(na+nb) + key[1]), 0
        elif key[0] == 'b': x, z = 0, 1 << (n + key[2]*(na+nb) + na + key[1])
        else:               x, z = 0, 1 << key[1]
        for (c, t, _) in reversed(gates):
            if (x >> c) & 1: x ^= 1 << t
            if (z >> t) & 1: z ^= 1 << c
        dm = (1 << n) - 1
        xd, zd, xa, za = x & dm, z & dm, x >> n, z >> n
        # obstruction coordinates: |0>-input -> xd, x on ancB, z on ancA must vanish
        bad = 0; bit = 0
        for q in range(n): bad |= ((xd >> q) & 1) << bit; bit += 1
        for r in range(R):
            for i in range(na): bad |= ((za >> (r*(na+nb)+i)) & 1) << bit; bit += 1
            for j in range(nb): bad |= ((xa >> (r*(na+nb)+na+j)) & 1) << bit; bit += 1
        obstruct_V.append(bad)
        # canonical DETECTOR: additionally, value independent of the logical basis input
        # |s>_L = X_L^s |0>^n, i.e. the back-propagated Z-part commutes with every X_L
        bad2 = bad | ((bin(zd & XLm).count('1') % 2) << bit)
        obstruct_D.append(bad2)
    L = len(recs)
    Zr = [i for i, k in enumerate(recs) if k[0] in ('b', 'ro')]
    Xr = [i for i, k in enumerate(recs) if k[0] == 'a']
    dimVZ = len(Zr) - rank2([obstruct_V[i] for i in Zr])
    dimVX = len(Xr) - rank2([obstruct_V[i] for i in Xr])
    dimV  = L - rank2(obstruct_V)
    dimDZ = len(Zr) - rank2([obstruct_D[i] for i in Zr])
    dimDX = len(Xr) - rank2([obstruct_D[i] for i in Xr])
    ri = {k: i for i, k in enumerate(recs)}
    def vec(ks):
        v = 0
        for k in ks: v ^= 1 << ri[k]
        return v
    Db = []
    for j in range(nb):
        for r in range(R + 1):
            if r == 0:  Db.append(vec([('b', j, 0)]))
            elif r < R: Db.append(vec([('b', j, r), ('b', j, r-1)]))
            else:       Db.append(vec([('ro', q) for q in I.B[j]] + [('b', j, R-1)]))
    Da  = [vec([('a', i, r), ('a', i, r-1)]) for i in range(na) for r in range(1, R)]
    lam = vec([('ro', q) for q in I.ZL])
    def obs(c, table):
        v = 0
        for i in range(L):
            if (c >> i) & 1: v ^= table[i]
        return v
    detOK = all(obs(c, obstruct_D) == 0 for c in Db + Da)      # Def-1.9 detectors are canonical
    lamV  = obs(lam, obstruct_V) == 0                          # lambda deterministic
    lamD  = obs(lam, obstruct_D) == 0                          # ... but NOT a canonical detector
    return dict(dimV=dimV, dimVZ=dimVZ, dimVX=dimVX, dimDZ=dimDZ, dimDX=dimDX,
                rkDb=rank2(Db), rkDbl=rank2(Db + [lam]), rkDa=rank2(Da),
                fVZ=nb*R + n - rkHX, fDZ=nb*R + rkHZ, fVX=na*R - rkHX,
                leftker=na - rkHX, splits=(dimV == dimVZ + dimVX),
                detOK=detOK, lamV=lamV, lamD=lamD)

# ---------------------------------------------------------------- driver
def mirror(code):
    return dict(n=code['n'], A=code['B'], B=code['A'], ZL=code['XL'], XL=code['ZL'])

def build(codename, schedname, sector):
    c = CODES[codename]
    cc = c if sector == 'Z' else mirror(c)
    if schedname.startswith('blk'):
        steps = sched_blocks(cc['A'], cc['B'], schedname[3])
    else:
        piX, piZ = SCHEDS[schedname]
        if sector == 'X': piX, piZ = piZ, piX
        steps = sched_corners(piX, piZ) if sector == 'Z' else sched_corners_mirror(piX, piZ)
    return Inst(cc['n'], cc['A'], cc['B'], cc['ZL'], steps,
                '%s/%s/%s' % (codename, schedname, sector), XL=cc['XL'])

def sched_corners_mirror(piX, piZ):
    """same physical CNOTs, roles swapped: A<->B."""
    steps = [[] for _ in range(4)]
    for i, slots in SURF_SLOT_Z.items():
        for t, cn in enumerate(piX):
            if cn in slots: steps[t].append(('aq', i, slots[cn]))
    for j, slots in SURF_SLOT_X.items():
        for t, cn in enumerate(piZ):
            if cn in slots: steps[t].append(('qb', j, slots[cn]))
    return steps

# find legal + MC interleaved surface schedules
SCHEDS = {}
def find_interleaved():
    good = []
    for piX in itertools.permutations(CORNERS):
        for piZ in itertools.permutations(CORNERS):
            try:
                I = Inst(9, SURF_X, SURF_Z, [0,1,2], sched_corners(piX, piZ), 'probe')
            except AssertionError:
                continue
            if I.mc: good.append((piX, piZ))
    return good

if __name__ == '__main__':
    t0 = time.time()
    good = find_interleaved()
    print('interleaved depth-4 surface schedules, legal AND (MC): %d of 576' % len(good))
    print('  e.g. %s | %s' % (good[0], good[len(good)//2] if len(good) > 1 else '-'))
    SCHEDS['ilv0'] = good[0]
    SCHEDS['ilv1'] = good[len(good)//2]
    RMAX = 3
    jobs = []
    for cn in ('steane713', 'surface913', 'steane+redX'):
        for sn in ('blkZ', 'blkX'):
            jobs.append((cn, sn))
    jobs += [('surface913', 'ilv0'), ('surface913', 'ilv1')]
    print()
    print('%-30s %-3s %-4s %-16s %-16s %s' % ('instance', 'sec', 'MC', 'brute d_R', 'transfer d_R', 'match'))
    allok = True
    stats = []
    for (cn, sn) in jobs:
        for sec in ('Z', 'X'):
            I = build(cn, sn, sec)
            assert I.mc
            tr, nsig, nzs, fin, ncols = transfer(I, RMAX)
            br = []
            for R in range(1, RMAX + 1):
                d, nc = brute_dR(I, R)
                br.append(d)
            ok = (br == tr)
            allok &= ok
            stats.append((I.name, nsig, nzs, fin, tr))
            print('%-30s %-3s %-4s %-16s %-16s %s'
                  % ('%s/%s' % (cn, sn), sec, 'yes', str(br), str(tr), 'OK' if ok else 'MISMATCH'))
    print()
    print('transfer arm structure:')
    for (nm, nsig, nzs, fin, tr) in stats:
        print('  %-34s |Sigma|=%-4d zero-cost self-loops=%-3d all A entries finite=%s'
              % (nm, nsig, nzs, fin))
    print()
    print('parity-space dimensions (Z-memory), closed forms vs computed:')
    hdr = ('code','sched','R','dimV','dimVZ','fVZ','dimDZ','fDZ','rkDb',
           'dimVX','fVX','dimDX','rkDa','lk','all')
    fmt = '%-14s %-5s %-2s %5s %5s %5s %5s %5s %5s %5s %5s %5s %5s %4s %s'
    print(fmt % hdr)
    pok = True
    for cn in ('steane713', 'surface913', 'steane+redX'):
        for sn in ('blkZ', 'blkX'):
            for R in (1, 2, 3):
                I = build(cn, sn, 'Z')
                d = parity_spaces(I, R)
                ok = (d['dimVZ'] == d['fVZ'] and d['dimDZ'] == d['fDZ']
                      and d['dimVX'] == d['fVX'] and d['rkDb'] == d['dimDZ']
                      and d['rkDbl'] == d['dimVZ'] and d['splits']
                      and d['dimDX'] == d['dimVX']
                      and d['dimVX'] - d['rkDa'] == d['leftker']
                      and d['detOK'] and d['lamV'] and not d['lamD'])
                pok &= ok
                print(fmt % (cn, sn, R, d['dimV'], d['dimVZ'], d['fVZ'], d['dimDZ'],
                             d['fDZ'], d['rkDb'], d['dimVX'], d['fVX'], d['dimDX'],
                             d['rkDa'], d['leftker'], ok))
    print()
    print('ALL transfer==brute : %s' % allok)
    print('ALL parity formulas : %s' % pok)
    print('elapsed %.1fs' % (time.time() - t0))
```

### 11.5 Reproduction, and the limitation this check inherits

Python 3.9.6, no external library, no `stim`, no sampling; single process, ~5 s wall clock. The
program is reproduced above in full and its SHA-256 is in §0; it was written to this session's
scratchpad and is preserved here because the scratchpad is not part of the repository. Declared
OS-level background processes started by this session: **none** (the `drive10`/`drive7` + `kissat`
workers running on this machine belong to another work item and were not touched, inspected or
signalled).

**Inherited limitation, stated plainly.** The two arms are independent in their *algorithms* — one
simulates `R` rounds and searches over multi-round fault sets against the full detector set, the
other builds a `2^{r_Z}`-state min-plus system from a single round — but they share their *model
design*: the same gate layout, the same fault-location taxonomy, the same detector definitions, the
same frozen conventions. A systematic modelling error (e.g. against `stim`'s conventions) would
survive both. §11 therefore corroborates the *derivation* of §5–§7 and not the model of §2. The
one thing to re-derive before trusting any of §11 is Lemma 5.4 (round transparency): every number
above inherits its correctness through the simulator's propagation rule, and it is the cheapest
thing to get subtly wrong.

---

## 12. Residual gaps, as precise sub-claims

Each is written so it can become its own DAG node. **T-G3 is the one this session considers the
sharpest**, because it is the only one that could change the *value* of `d_R` rather than the
*generality* of the statement.

**T-G1 (inherited model clauses).**
> The model of §2 — Definition 2.8's fault taxonomy, scope clause T2 (verbatim round repetition,
> disjoint per-round location sets, ancilla frames zeroed each round), and scope clause T3
> (`d_circ(C(M)) = min(d_R^Z, d_R^X)`, the window theorem's **W-G1**) — is the frozen model of
> 公共定义.

Not re-derived here; imported. T2 is immediate for the layout of Definition 2.6 and **false** for
cross-round idle-layer compression, which is therefore outside the scope (this is the window
theorem's **W-G2**, inherited verbatim). T3 is definitional: everything in §3–§7 and §9 is proved
per sector and survives any aggregation that is monotone in each argument.

**T-G2 (minimality of the state space).** OPEN.
> Is `Σ = F₂^n/S_X` the **Nerode-minimal** state space for the language
> `{(σ_0,…,σ_R) : path of finite cost from [0] to a terminal class}` with its min-plus weights? If
> not, what is the minimal quotient, and does it have a closed form in terms of `(H_X, H_Z, M)`?

Theorem T asserts sufficiency (6.4), never minimality. A minimal quotient would identify states
`σ, σ'` with equal *future cost profiles*; since `v` separates `[0]` from the other zero-syndrome
classes and `A[σ,·]` depends on `σ` both by translation and through `H_Z σ`, no obvious lumping
exists, but none is excluded either. Settling this changes no value of `d_R`; it changes the size of
the object one must build for `CIRCDIST.sat.instances` at `d ≥ 5`, where `|Σ| = 2^{n − rank H_X}`
is the binding cost.

**T-G3 (the detector/observable split is a definitional choice, and Definition 3.5 is new here).**
> `d_circ` is a function of `(circuit, fault model, choice of detector space `𝒟` complementary to
> the designated observables)`, and different complements give different values. Definition 3.5
> fixes `𝒟` canonically as "the deterministic parities whose value is independent of which logical
> basis state was prepared", and Proposition 3.6 shows the frozen Definition-2.7 Z-detectors span
> exactly the Z-half of that `𝒟`.

**Why this is a gap and not a result:** Definition 3.5 is introduced in *this* document. If a
reviewer prefers a different canonical split — for instance one defined by a family of *code-state*
inputs rather than logical-basis inputs, which is a genuinely different family because
`|0⟩^{⊗n}` is not a code state and makes the round-0 X-check outcomes random — then `𝒟_X` changes
and, in principle, so could `d_R`. Three things reduce the risk and should be recorded with the
sub-claim: (a) whatever `𝒟` is chosen, if it contains the Definition-2.7 set and is contained in
`V`, then Proposition 3.7's argument goes through verbatim, because `F^X` annihilates *all* of
`V_X` and all of `𝒟_Z`; (b) the split is forced on the Z-side by 3.6's dimension count; (c) it is
confirmed numerically on 18 instances including a dependent generating set (11.2). **What is not
established is that Definition 3.5 is the split the frozen 公共定义 intends.** This is precisely the
hole the window theorem labelled W-G3 and its review answered with S3′; §3 answers it more sharply,
but the answer rests on a definition a reviewer must ratify.

**T-G4 (computability of `A`).** Not a gap in Theorem T, but a statement the node's claim
("explicitly constructible") should carry honestly.
> `A` is computed exactly by BFS/Dijkstra over `F₂^n × F₂^ℬ` from the one-round fault columns, or
> by a weight-capped search over subsets of one round's `L` locations of size `≤ d`, in
> `O(L^d · poly)`. Both are **exponential** in the code parameters; no polynomial algorithm is
> claimed, and the general "minimum weight of a coset with a prescribed syndrome side-condition"
> problem is of syndrome-decoding shape.

Explicitly **not** asserted here: NP-hardness. The recon's A7 flags Vardy (1997) and
Kapshikar–Kundu as *unverified* and distinct from the decoding results; conflating them is a
referee-catchable error and is avoided.

**T-G5 (scope of finiteness).** Lemma 5.5 consumes the availability of two weight-1 mechanisms
(terminal single-qubit `X` on a data qubit; a pure record flip). A fault model lacking **both**
would make some `A` entries `+∞`; Theorem T survives with `min ∅ = +∞`, but Corollary 9.2's
irreducibility and the "no unreachable states" claim would not.

**Epistemic residual (not a mathematical gap).** Every statement here is CONJECTURED with a
derivation status; none has been independently reviewed. Rule 6 requires an independent
claim-level review before `CIRCDIST.sat.transfer` may carry a completion level. In particular §9's
agreement with `CIRCDIST.sat.window` is a consistency check between two unreviewed documents by the
same side, and must not be read as mutual certification.

---

## 13. One paragraph for the assembly node

For every legal, measurement-consistent, single-round single-ancilla CSS schedule `M` — any depth,
interleaved or not, dependent generating sets allowed, both CSS sectors, under the frozen ideal
temporal boundaries — the circuit distance of the `R`-round memory experiment is exactly a min-plus
matrix element. Per sector, the state is the class of the accumulated residual data error modulo the
opposite stabiliser group, `Σ = F₂^n/S_X`, and nothing else: the undetectability constraint at each
round demands that the round's own record flips equal the syndrome of the incoming state, which is a
function of the class alone, and the terminal logical condition is likewise a function of the final
class alone. Every elementary fault is a weighted transition through the one-round dictionary
`w_M([δ],μ)`, every transition is realised at exactly its weight, and per-round weights add exactly
because fault locations are partitioned by round — so the transfer matrix `A[σ,σ'] = w_M(σ'−σ,H_Zσ)`
is a genuine matrix and `d_R = u ⊙ A^{⊙R} ⊙ v` with `u` the indicator of `[0]` (forced by the
absolute round-0 detector) and `v` the indicator of the `2^k − 1` non-trivial zero-syndrome classes
(forced by the ideal terminal readout). Both boundary vectors are derived from the two boundary
instances of the undetectability recursion, not assumed. The zero-cost transitions are exactly the
`2^k` self-loops at zero-syndrome states, so the min-plus eigenvalue is `0`, the cyclicity is `1`,
and `A^{⊙R}` is eventually constant; deleting zero-cost self-loops from an optimal path re-derives,
from the algebra alone, monotonicity, `d_∞ = d_d`, and `R_stab ≤ d_∞ ≤ d`, in agreement with the
window theorem. What this document does **not** settle: whether `Σ` is minimal, whether the
canonical detector/observable split introduced in §3 is the one 公共定义 intends, and any instance
value at `d ≥ 5`.
