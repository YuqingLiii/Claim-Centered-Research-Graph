# WHGAP R7 — independent rule-7 review of the P13-B package (n = 2 first-order layer)

**Artifact type:** independent adversarial review (immutable).
**Commission:** [`WHGAP_REVIEW_COMMISSION_R7_20260730.md`](../channel-capacity/werner-holevo-gap/notes/WHGAP_REVIEW_COMMISSION_R7_20260730.md).
**Reviewed inputs (frozen):** `artifacts/whgap_p13b_n2_layer_20260730.md`; commission
[`WHGAP_COMMISSION_P13B_20260730.md`](../channel-capacity/werner-holevo-gap/notes/WHGAP_COMMISSION_P13B_20260730.md);
logs/JSON under `artifacts/logs_whgap_p13b_20260730/` (SHA256SUMS_p13b.txt verified, see §0.5).
**Inherited:** §1–§3 of
[`WHGAP_REVIEW_COMMISSION_R5_20260729.md`](../channel-capacity/werner-holevo-gap/notes/WHGAP_REVIEW_COMMISSION_R5_20260729.md)
+ the P13-A/P13-B tooling notes (radical-free charts; Berkowitz determinant; `nsimplify` ban).
**Reviewer:** fresh Opus instance, 2026-07-30. Authored none of the reviewed work; given no
desired outcome. Interpreter `C:<home>/cpython3119/python.exe` (sympy 1.13.1, mpmath 1.3.0,
numpy 1.26.4, scipy 1.14.1).

## VERDICT — **FINDINGS** (2 MAJOR, 6 minor)

The **exact mathematics of the package is confirmed in full** by an independent construction:
claims 1, 2, 3, 4 and the two exact calibration values (claims 5, 6) reproduce exactly, and my own
runs even *strengthen* the interval certificate. The two MAJORs are **not** arithmetic errors —
they are an inverted comparison and an overstated coverage claim, both of which have already been
copied verbatim into `WHGAP.onset-two-fifths`, `NODE_INDEX.md` and the DAG header, and one of which
(MAJOR 1) is contradicted by exact numbers I computed from the package's own machinery.

Licensing menu option (A) **cannot be taken as written**, because its final clause ("the n = 2
first-order layer yields no witness in [2/5, 1/2) within the searched families") is fine but the
package's headline reading of claim 6 is false and its coverage statement is not honest about the
m_B ≥ 2 strata. §7 below gives the exact wording that WOULD be licensed after repair.

---

## 0. PRE-ACTION REPORT (mandatory, `research/PRETASK_RELOAD_PROMPT.md`)

**0.1 Files read from disk, completely, in the prescribed order, before any mathematics:**
`research/DAG_PROTOCOL.md` (whole file: §1 data structure, §2 ladder + completion gate, §3 rules
1–8, §4 READ, §5 WRITE, §6 session-close); `research/RESEARCH_STRUCTURE_PROTOCOL.md` (§1–§10);
`channel-capacity/werner-holevo-gap/README.md`;
`channel-capacity/werner-holevo-gap/notes/WERNER-HOLEVO-GAP_PROOF_DAG.md` (header, mermaid,
outline, eight rules inlined); `channel-capacity/werner-holevo-gap/proof-dag/NODE_INDEX.md`;
the target node `proof-dag/nodes/WHGAP.onset-two-fifths.md` (no children; parent `WHGAP.goal`
read via the DAG doc's goal entry and outline). Then the R7 commission, the inherited §1–§3 of
the R5 commission, the P13-B commission, the reviewed artifact, and — for the S0 instantiation
audit only — §3–§4 of `notes/WHGAP_N1PRIME_EXPANSION_LEMMA_20260729.md`.

**0.2 Target node and status as read from disk:** `WHGAP.onset-two-fifths` (alias P13), kind LEAF,
role proof, **status CONJECTURED**, `disposition: null`, parents `["WHGAP.goal"]`, children `[]`.
`status_source` records the P13-A stratum-exhaustion Theorem as PROVED (R6, LICENSE A) with the
onset identification itself open. Open obligation (d) carries "n = 2 FIRST-ORDER layer: bounded
null executed (P13-B, `pending-review:`) … Review debt: P13-B rule-7 review (R7) owed before any
completion-tier interpretation." That review debt is what this artifact discharges.

**0.3 My ROLE: reviewer.** Independence statement: I did not author any part of the P13-B package,
any P13-A/R5/R6 material, or any WHGAP node, and I was given no desired outcome — the commission's
menu presents (A) and (B) as alternatives. To honour the anchoring ban (7c) I wrote every one of my
scripts from the frozen definitions of R5 §1 **before opening any `tools/whgap_p13b_*.py`**; I have
still not read those scripts (see §0.4 for the one deliberate exception: two frozen JSON files
needed to audit claim 5).

**0.4 Highest status my evidence could license per §2:** a completed independent review at rule-7
quality opens the completion tier (CERTIFIED\*/PROVED/REFUTED) for the reviewed statements, but the
**status write itself is the decision layer's** (proposer cites the review artifact). I wrote no
status, and I edited **no node file, no `NODE_INDEX.md`, and no DAG doc** (single-writer deviation,
§0.6). My own new evidence (§4.6, §5.4) is reviewer-authored and caps at NUMERICAL/observation for
anything it proposes.

**0.5 Gates and deliverables of my commission, one line each.**
- Verify `SHA256SUMS_p13b.txt` before relying on any frozen input → **DONE, 24/24 files OK**
  (`sha256sum -c` from the repository root; every line `OK`, including the artifact itself).
- Claim 1 (S2 identity): own derivation → §2.
- Claim 2 (m_B x-independence): audit + ≥ 2 exact Ψ of different rank → §3.
- Claim 3 (exact strip nulls): own exact D_Ψ at ≥ 4 (family, x) pairs incl. a type-E and an r = 8
  point → §4 (I did **6** strip pairs + 7 further exact runs).
- Claim 4 (interval certificate): own symbolic-in-x charpoly for ONE base point → §5 (I did
  **both**).
- Claim 5 (calibrations + false-positive refutation): exact re-test + logic audit → §6.
- Claim 6 (below-onset enhancement): exact re-verification + over-claim audit → §4.4, §4.6.
- Claim 7 (variety-conjecture hygiene + coverage honesty) → §3.3, §5.4, §6.3.
- Pick exactly one licensing-menu option or FINDINGS → **FINDINGS**, §7.

**0.6 Conflicts between commission text and disk protocols: one, reported not resolved.**
The R7 commission binds the single-writer deviation (no node/index/DAG edits), whereas
`DAG_PROTOCOL.md` §5/§6 and `RESEARCH_STRUCTURE_PROTOCOL.md` §6 (atomic update, rule 8c) require
the outcome to be appended to the node in the same session. The deviation is commissioned by the
decision layer, which owes the atomic node/index/DAG update citing this report. I comply and record
the obligation: **this report and `tools/whgap_r7_*.py` are not yet linked from
`WHGAP.onset-two-fifths`.** No other conflict; in particular the node's own text already carries
the `pending-review:` marker required by rule 6, so nothing on disk over-claims today.

**0.7 Standing failure modes screened (R5 §2), item by item.**
1. `.H` on real-symbolic matrices → avoided: my exact layer is radical-free and every conjugate is
   applied to explicit Gaussian rationals. **One related trap HIT and diagnosed** (minor m5): in my
   symbolic-in-x run `Symbol("x")` without a reality assumption leaves `conjugate(x)` unresolved, so
   the Hermiticity gate returns False spuriously; the rational-x runs (which do resolve it) give
   `D_hermitian = True` in all 13 cases, and the charpoly coefficients come out real rational
   functions, which settles it.
2. WindowsApps python → the pinned interpreter is used throughout.
3. Complement convention drift → §1.2: I derived the padded 16-dim complement and the adjoint
   `(Λ^c)^†(Z) = Σ_{ab} Z_{ab} K_a^T K_b` myself; my D_Ψ then reproduces the executor's exact values,
   so conventions coincide.
4. Transpose vs conjugate-transpose → audited; my M_B is obtained TWICE (operator-sum via
   self-adjointness, and by applying the **channel formula** `Y ↦ (1−x)Y + (x/2)(Tr Y·1 − Y^T)`
   index-wise on each tensor factor, which never mentions Kraus). The two agree exactly in all 13
   runs.
5. `sorted()`/`bool(Relational)` on symbolics → avoided by clearing denominators to integers before
   any comparison; `nsimplify` never used.
6. CRLF in SHA sums → my `SHA256SUMS_r7.txt` is written LF and verified with `sha256sum -c`.
7. Degeneracy bookkeeping / small gaps → my exact layer needs no threshold; where I do use floats
   (§6) I report the **whole spectrum** rather than a pass/fail flag.
8. ε log ε bookkeeping → §1.3 audits the S0 instantiation constants against the R5d-reviewed
   Prop 3.3 / Lemmas 4.1–4.2 and reproduces them to the digit.
9. Anchoring → §0.3. My independent path differs from the executor's in the E-side projector
   construction (range route vs kernel route, §1.2), in the charpoly route (Newton identities on a
   denominator-cleared integer matrix vs Berkowitz on rationals) and in the B-side operator
   (channel formula vs Kraus). Where notation coincides it is because the objects are forced; I flag
   that explicitly in §1.2.

---

## 1. Type audit and independent construction (rule 7a)

### 1.1 Types of every object in the reviewed claims

| symbol | type | dimension | checked |
|---|---|---|---|
| `x` | real parameter, `0 < x < 1` | — | strip values used are exact rationals |
| `Λ_x` | CPTP, self-adjoint in HS | M₃(ℂ)→M₃(ℂ) | self-adjointness re-derived (§1.2) |
| `K_0…K_3` | Kraus, **real** entries | 3×3 | `K_0 = c_0·1`, `K_i = c_i·A_i`, `(A_i)_{jk}=ε_{ijk}` |
| `Λ^{c}_x` | complement, padded | M₃(ℂ)→M₄(ℂ) | `Λ^c(Y)_{ab}=Tr(K_aYK_b^T)` |
| `W_m = K_a⊗K_b`, `m=(a,b)` | 2-copy Kraus, real | 9×9, 16 of them | `Bhat_m = Ahat_a⊗Ahat_b` integer |
| `Ψ ↔ M` | unit vector ↔ coefficient matrix | ℂ⁹ ↔ 3×3, `‖M‖_F=1` | `Ψ_{3j+k}=M_{jk}`, `W_mΨ = vec(K_aMK_b^T)` |
| `Λ^{(2)}(P_Ψ)` / `Λ^{c(2)}(P_Ψ)` | states, equal nonzero spectrum | 9×9 / 16×16, rank r | `m_B=9−r`, `m_E=16−r` verified in all 13 runs |
| `Π_B, Π_E` | orthogonal projectors | rank m_B / m_E | built two independent ways (§1.2) |
| `M_B, M_E, D_Ψ = M_B−M_E` | Hermitian **observables** on ℂ⁹ | 9×9 | Hermiticity exact in all 13 runs |
| `Ic_2` | real scalar, **nats** | — | my slope tests use nats consistently |

Two type facts are load-bearing and both hold: `M_E ⪰ 0` (because `w_E(φ)=Tr[Π_EΛ^{c(2)}(φ)] ≥ 0`
for every state), and `Tr[D_ΨP_Ψ]=0`, hence `λ_max(D_Ψ) ≥ 0` always and "ascent" means the strict
inequality. Consequence used below: **whenever m_B = 0 one has D_Ψ = −M_E ⪯ 0 for a purely
structural reason** — those table rows carry no information (see MAJOR 2).

### 1.2 My construction of D_Ψ, derived before reading any executor script

`Λ` is HS-self-adjoint: `⟨Z,Λ(Y)⟩ = ⟨Λ(Z),Y⟩` with the same formula (the transpose part is
self-adjoint because `Tr(Z^†Y^T) = Tr(Z̄Y)`), so `M_B = (Λ^{(2)})^†(Π_B) = Σ_m c_m² Bhat_m^T Π_B Bhat_m`
and equally `M_B = (Λ⊗Λ)(Π_B)`; I compute **both** and compare (gate passes in all 13 runs).
For the environment I derived `⟨Z,Λ^c(Y)⟩ = Tr[(Σ_{ab} conj(Z_{ab})K_b^TK_a)Y]`, i.e.
`(Λ^c)^†(Z) = Σ_{ab}Z_{ab}K_a^TK_b`, so `M_E = Σ_{mn}(Π_E)_{mn}W_m^TW_n = Σ_{mn}R_{mn}Bhat_m^TBhat_n`
with `R := ΔΠ_EΔ`, `Δ = diag(c_m)`.

**Radical-free `R` by the RANGE route (differs from the executor's kernel route).** With
`Ghat_{mn} := Tr[Bhat_mP_ΨBhat_n^T]` (x-free) one has `G_E = ΔGhatΔ`, hence
`range(G_E) = Δ·range(Ghat)`; with `S` a rational column basis of `range(Ghat)`,
`R = D2 − D2·S(S^†D2S)^{-1}S^†D2` where `D2 = diag(c_m²)` is rational in x. **No square root ever
enters a symbolic matrix.** The executor instead used a kernel basis of `Ghat`; the two formulas
must agree, and my exact values reproduce the executor's table entry for entry, which is the
strongest available cross-check. *Notational-coincidence flag (7c):* the objects `Π_B, Π_E, M_B, M_E`
are forced by the definitions, so my names coincide with the executor's; the constructions do not.

**Exact certificate.** For Hermitian `D`, `D ⪯ 0` ⟺ every coefficient of `det(λ1−D)` is ≥ 0 (write
`λ_i = −μ_i ≥ 0`: `Π(λ+μ_i)` has nonnegative coefficients; conversely a monic polynomial with
nonnegative coefficients is positive for λ > 0, and `D` Hermitian has real spectrum). I clear
denominators first — `N := L·D` Gaussian-integer, `spec(N) = L·spec(D)` — and compute the charpoly
by **Newton's identities from `Tr(N^k)`**, i.e. in integer arithmetic only. (The symbolic-λ Berkowitz
determinant on 14-digit Gaussian rationals did not finish in 10 min for the r = 8 point; this is a
tooling note worth adding to the P13-A/B list.)

### 1.3 S0 / Lemma 2.1 (not itself a numbered claim, audited anyway)

The instantiation is correct and the constants are exactly reproducible from the R5d-reviewed
ingredients: cluster count `m_B+m_E = 25−2r`, regular count `2r`; `b = ‖B_•‖ ≤ 1` for a difference
of states, so `(3.1)` reads `ε ≤ g/4` and `C_pert = 6/g`; `λ/ε ≤ 1 + (6/g)(g/4) = 5/2 = U`;
`κ(5/2) = (5/2)log(5/2)`; Lemma 4.2 with `a = 3g/4` gives `1 + log(4/(3g))`. Recomputing
`C^{(2)}` myself: x = 9/20, g = x²/4 = 81/1600 → **814.3 (r = 4)** and **564.5 (r = 7)**; x = 2/5,
g = 0.04 → **1013.1 (r = 4)** and **695.3 (r = 7)**. These match §2's printed samples (564.6 is a
rounding difference). Corollary 2.2's "λ_max < 0" branch is vacuous by §1.1, and its statement that
the constants "matter only for the positive direction, never for a null" is correct: a null here is
the *exact* statement `λ_max = 0`, which is remainder-free.

---

## 2. Claim 1 — the S2 identity. **CONFIRMED (FORMULA level)**

Script `tools/whgap_r7_s2.py`, log `r7_s2.log`, JSON `r7_s2.json`.

I re-derived the identity from scratch. Since `⟨conj Ψ|v⟩ = Σ_n Ψ_n v_n`,

    ⟨conj Ψ|(K_a⊗K_b)|Ψ⟩ = Tr(M^T K_a M K_b^T),   F(M) = Σ_{a,b} |Tr(M^T K_a M K_b^T)|².

Because `F` is a sum of squared moduli of *holomorphic* functions of `M`, I verified it as a
**polynomial identity in 18 independent symbols** (`m_{jk}` and `n_{jk}` standing for
`conj(m_{jk})`) with **symbolic x** — not at sample points:

- `Tr(M^T A_i M A_j) = −2·adj(M)_{ji}` — symbolic, all 9 (i, j): **PASS**
  (route: `A_i = −[e_i]_×`, `M^T[w]_×M = [adj(M)w]_×`, `Tr([u]_×[v]_×) = −2u·v`; sympy's `adjugate`
  independently checked against `M·adj M = det(M)·1`).
- `Tr(M^T A_i M) = 0` and `Tr(M^T M A_i) = 0` — symbolic: **PASS** (antisymmetry / symmetry).
- the (a,0) and (0,b) blocks vanish; the (0,0) block is `Tr(MM^T)`: **PASS**.
- **`Σ_{a,b} c_a²c_b² T_{ab}(M)T_{ab}(N) ≡ (1−x)²Tr(MM^T)Tr(NN^T) + x²Σ_{ij}adj(M)_{ji}adj(N)_{ji}`** —
  identically zero difference in 18 symbols and x: **PASS**.

Independent value-level closure against the **channel formula** (not the Kraus set): I implemented
`Λ⊗Λ` by index action of `Y ↦ (1−x)Y + (x/2)(Tr Y·1 − Y^T)` on each factor, checked it against the
Kraus assembly (max deviation 1.1·10⁻¹⁶), and compared `⟨conj Ψ|(Λ⊗Λ)(P_Ψ)|conj Ψ⟩` with the closed
form at 4 rational x × 3 random complex M (one of them det = 0): **max error 8.3·10⁻¹⁷**.

Consequence (3.2) also confirmed: `x ∈ (0,1)` makes both coefficients strictly positive, so
`F = 0 ⟺ Tr(MM^T) = 0 and adj M = 0 ⟺ M = uv^T` with `u^Tu = 0` or `v^Tv = 0`; and the n = 1
degeneration `F = ((1−x)τ²)²` for `M = ψψ^T` is correct. **Value-vs-formula (7f): FORMULA verified
symbolically; the executor's own numeric spot-checks were not needed and were not used.**

---

## 3. Claim 2 — m_B is x-independent. **CONFIRMED (derivation + values)**

**Derivation audit.** `Λ^{(2)}(P_Ψ) = Σ_m |W_mΨ⟩⟨W_mΨ|`, so its range is `span{W_mΨ}` and
`r = dim span_ℂ{K_aMK_b^T} = dim span_ℂ{Ahat_a M Ahat_b^T}` because each `c_ac_b ≠ 0` on `(0,1)` and
rescaling spanning vectors by nonzero scalars does not change a span. Hence `r`, `m_B = 9−r` and
(via the pure-input isospectrality) `m_E = 16−r` are x-free, and
`ker Λ^{(2)}(P_Ψ) = (span{Ahat_aMAhat_b^T})^⊥`. The argument is correct and complete as printed.

**Values (own code).** `tools/whgap_r7_checks.py D` (`r7_checks_D.log`): for 5 families of ranks
r = 4, 6, 7, 8, 9 I computed `rank G_B` and `rank Ghat` at **six** rational x
(1/10, 7/20, 2/5, 9/20, 11/20, 9/10) and the x-free `rank U(M)`: all three agree at every point,
for every family. In addition, all **13** exact runs of §4 carry two gates: the kernel of `G_B`
computed by direct nullspace at that x has the same dimension as the x-free route
**and the two orthogonal projectors are exactly equal** (`PiB_two_routes_equal: true`), and
`rank Ghat = r` throughout.

**3.3 P3 hygiene (part of claim 7).** Theorem 3.3's `P3 ⊆ {m_B ≥ 1}` is a correct closed-form
sufficient condition (annihilator `B = uv^T`; `L·B·L = U⊗V` with `U = {w : u^Tw = 0}`,
`V = {q : v^Tq = 0}`; annihilator of `U⊗V` in `Tr(XY)` is `{va^T + yu^T}`), and the chart reduction
`u = v = u_0` modulo `O(3,ℝ)×O(3,ℝ)` is valid (every isotropic `u = a + ib` with `|a| = |b|`,
`a ⊥ b` is a complex multiple of a real rotation of `u_0`; the two rotations act independently on
`u` and `v`; the scalars absorb into `a`, `y`). My own **unconstrained** hunt
(`tools/whgap_r7_variety.py`, 30 L-BFGS minimisations of `σ_9(U)/σ_1(U)` over all of ℂ^{3×3}):
**30/30 converged to degeneracy and 30/30 annihilators came out rank one with both factors
isotropic** (`|u^Tu|, |v^Tv| ≤ 1.3·10⁻⁸`) — an independent corroboration of the executor's 60/60.
`{m_B ≥ 1} = P3` remains **CONJECTURED**, correctly labelled as such on the artifact and the node.

---

## 4. Claim 3 (+ the exact calibration values of claims 5, 6). **CONFIRMED**

Script `tools/whgap_r7_exact.py` → `r7_exact.json`, `r7_exact.log`. Every row is my own exact
construction (§1.2), with seven per-row gates: kernel dims agree, projectors agree,
`M_B` self-adjoint-route = channel-formula-route, `D` Hermitian, `Tr[DP_Ψ] = 0`, `DΨ = 0`, charpoly
coefficients real. **All gates PASS in all 13 runs.**

| family (unnormalised M) | x | r | m_B | m_E | my exact verdict |
|---|---|---|---|---|---|
| iso-product `u₀u₀^T` | 9/20 | 4 | 5 | 12 | **NSD exactly**, λ_max = 0 |
| **type-E `diag(1,1,0)`** | 21/50 | 7 | 2 | 9 | **NSD exactly**, λ_max = 0 |
| **P3g `u₀(1,0,2)^T+(0,1,1)u₀^T` (r = 8)** | 12/25 | 8 | 1 | 8 | **NSD exactly**, λ_max = 0 |
| **type-E** | **2/5** | 7 | 2 | 9 | **NSD exactly**, λ_max = 0 |
| **P3g (r = 8)** | **2/5** | 8 | 1 | 8 | **NSD exactly**, λ_max = 0 |
| P3s `u₀e₃^T+e₃u₀^T` | 9/20 | 7 | 2 | 9 | **NSD exactly**, λ_max = 0 |
| iso-product | 7/20 | 4 | 5 | 12 | λ_max = **13/132** exactly |
| **type-E** | 7/20 | 7 | 2 | 9 | λ_max = **1102933/9570000** exactly |
| type-E `E₁₂+E₂₁` | 7/20 | 7 | 2 | 9 | λ_max = **1102933/9570000** exactly |
| P3c `(u₀+e₃)u₀^T` | 7/20 | 6 | 3 | 10 | λ_max = **13/132** exactly |
| max-entangled `1` | 9/20 | 9 | 0 | 7 | NSD (structural: `D = −M_E`) |
| `diag(1,i,0)` | 9/20 | 9 | 0 | 7 | NSD (structural) |
| iso-product | 11/20 | 4 | 5 | 12 | **NSD exactly** (G-cal2 anchor) |

So the commission's requirement is met with margin: **6 strip pairs** (four of them at the
prescribed rational strip x, two at the endpoint 2/5), **including a type-E point and an r = 8
point**, all NSD by exact certificate; plus the two exact calibration values.

**4.4 Claim 5 (G-cal1) and claim 6 (the exact value): both exact, both reproduced.**
`d₁(7/20) = (1−x)(2−5x)/(2−x)|_{7/20} = (13/20)(1/4)/(33/20) = 13/132` — value equals formula.
My independent construction returns `λ_max = 13/132` for the isotropic-product family (and for
P3c), and `λ_max = 1102933/9570000` for type-E (and for `E₁₂+E₂₁`). The inclusion–exclusion behind
G-cal1 is correct as printed: `ker(A⊗A) = K⊗ℂ³ + ℂ³⊗K` gives `Π^{(2)} = Π⊗1 + 1⊗Π − Π⊗Π`, and since
`Λ^†(1) = 1` and `(Λ^c)^†(1_4) = 1_3`, `D^{(2)} = D⊗1 + 1⊗D − (M_B⊗M_B − M_E⊗M_E)`; the `(ψ̄,ψ)`
entry is `d₁` (not `2d₁`) because `D_ψ = b_ψ = e_ψ = 0`. I additionally verified that the
isotropic-product family gives `λ_max = d₁(x)` **exactly at six different x** (13/132, 31/810,
369/12920, 7969/322600, 61/3220, 0 at 2/5) — i.e. the embedded n = 1 witness is exactly recovered
as a formula in x, not only at 7/20.

**4.5 Independent VALUE-vs-FORMULA closure against the definition (7f).**
`tools/whgap_r7_checks.py A` (`r7_checks_A.json`): with my own 60-digit mpmath entropies —
B side from the **channel formula**, E side from the Kraus set, `φ` = top eigenprojector of my
exact `D_Ψ` — the ratio `Ic_2(ρ_ε)/(ε log(1/ε))` converges to the exact λ_max:

| base point | ε = 1e-8 | 1e-12 | 1e-16 | 1e-20 | exact λ_max |
|---|---|---|---|---|---|
| iso-product, 7/20 | 0.0945632 | 0.0958704 | 0.0965240 | 0.0969162 | **13/132 = 0.0984848** |
| type-E, 7/20 | 0.1087407 | 0.1109101 | 0.1119949 | 0.1126457 | **1102933/9570000 = 0.1152490** |

The residual is the expected `O(1/log(1/ε))` correction. So the exact λ_max really is the
`ε log(1/ε)` coefficient of the **raw** coherent information — established against an independent
construction of the same quantity, not against the package's own formula.

### 4.6 MAJOR 1 — claim 6's headline reading is wrong in both halves

The *number* `1102933/9570000` is right. The sentence built on it is not. Two independent defects,
both from my own exact computations (`tools/whgap_r7_threshold.py` → `r7_threshold.json`):

**(a) Per channel use the n = 2 layer is strictly WEAKER, not "17 % stronger".** The capacity-level
quantity is `Q ≥ (1/n)Q^{(1)}(Λ^{⊗n})`, and Corollary 2.2 itself uses
`Q(Λ_x) ≥ ½Q^{(1)}(Λ_x^{⊗2})`. So the comparable coefficients are
`λ_max^{(2)}/2 = 0.0576245` against `d₁(7/20) = 0.0984848` — a ratio of **0.585**, i.e. the 2-copy
entangled first-order mechanism delivers **41 % LESS** coherent information per channel use than the
n = 1 witness. Equivalently the 2-copy coefficient is strictly **subadditive**:
`0.1152490 < 2·d₁ = 0.1969697`. "Strictly stronger", "genuinely more powerful" and "beats n = 1 by
~17 %" therefore invert the only normalisation that has capacity meaning.

**(b) The type-E point does NOT "die at exactly the same threshold 2/5" — it dies earlier.** Its
exact first-order threshold is the unique root in (0,1) of `19x⁴ − 21x³ − 14x² + 28x − 8`:

> **x\*_E = 0.391297769484659129686047092319…  <  2/5**   (2/5 − x\*_E = 8.702·10⁻³)

(This is the largest root in (0,1) of any charpoly coefficient of the type-E `D_Ψ(x)`; my interval
certificate shows no coefficient has a root in (2/5,1), so the switch-on point is that root.) Exact
λ_max values on the way down confirm it and show the "17 %" advantage is a one-point artefact that
**reverses** as the threshold is approached:

| x | 7/20 = 0.350 | 19/50 = 0.380 | 77/200 = 0.385 | 387/1000 | 39/100 = 0.390 | 2/5 |
|---|---|---|---|---|---|---|
| type-E λ_max | **0.1152490** | 0.0313400 | 0.0174471 | 0.0118998 | 0.0035902 | 0 |
| `d₁(x)` (n = 1) | 0.0984848 | 0.0382716 | 0.0285604 | 0.0247024 | 0.0189441 | 0 |
| type-E > n = 1 (unnormalised)? | yes | **no** | **no** | **no** | **no** | — |
| type-E > n = 1 per use? | **no** | no | no | no | no | — |

**(c) Consequently "the 2/5 threshold reappears at n = 2" is not independent blocklength evidence.**
The only base point whose threshold is exactly 2/5 is the isotropic **product** family (a) — and its
`λ_max ≡ d₁(x)` identically (§4.4), i.e. it *is* the n = 1 witness embedded by
`Π^{(2)} = Π⊗1+1⊗Π−Π⊗Π`. The `(5x−2)` charpoly factors that §4.4 offers as the structural signature
belong to that product family; I verified that for the **type-E entangled** base point **no
numerator is divisible by `5x−2`**, and every coefficient is *strictly* positive at x = 2/5 except
the constant term. So the artifact's sentence "The number 2/5 is thus visible in the n = 2
first-order data of the **entangled** layer" is unsupported: in the entangled data the visible
number is `x*_E ≈ 0.3913`, and 2/5 is visible only through the product (n = 1) stratum.

**What survives.** The *null* is untouched and in fact reinforced: the entangled base points die
*earlier* than 2/5, so `sup_Ψ` of the per-Ψ threshold is attained by the product family at exactly
2/5, and the numerical sweep found nothing above it. The honest headline is "the n = 2 first-order
layer does not extend the mechanism past 2/5; the sup is attained by the embedded n = 1 witness, and
the genuinely entangled base points examined switch on strictly below 2/5", not "n = 2 is stronger
but dies at the same place".

**Propagation to repair (decision layer):** the artifact's one-line outcome (§ header), §8.3, the
node's Evidence bullet "below-onset enhancement (noteworthy)", `NODE_INDEX.md` lines 82–84, and the
DAG header's "beats n=1 by ~17% yet dies at the same 2/5 (blocklength-robustness evidence)".

---

## 5. Claim 4 — the interval certificate. **CONFIRMED for BOTH base points (FORMULA in x)**

Script `tools/whgap_r7_interval.py` → `r7_interval_isoprod.json`, `r7_interval_typeE.json`.
The commission asked for one base point; because the B-side kernel and the E-side range are x-free
(§1.2, claim 2) my `D_Ψ(x)` is rational in x with **no branch or case analysis**, so I did both.

**Logic I applied (and which the artifact's Prop 4.1 states correctly):** write
`det(λ1−D(x)) = Σ_k c_k(x)λ^k`. If (i) no denominator of any `c_k` vanishes on `[2/5,1)`, (ii) no
numerator has a root in the OPEN interval `(2/5,1)`, and (iii) every `c_k ≥ 0` at probe points of the
interval and at the left end, then each `c_k` is continuous and of constant sign there, so `D(x) ⪯ 0`
and (with `Tr[DP_Ψ] = 0`) `λ_max(D_Ψ(x)) = 0` for every `x ∈ [2/5,1)`.

| | isotropic product (r = 4) | type-E (r = 7) |
|---|---|---|
| denominators | powers of `(x−2)` only — no root in `[2/5,1)` | powers of `(x−2)` only — no root in `[2/5,1)` |
| numerator roots in `(2/5,1)` | **none** (all 10 coefficients) | **none** (all 10 coefficients) |
| all `c_k ≥ 0` at x = 2/5, 9/20, 1/2, 3/4, 99/100 | **yes** | **yes** |
| largest numerator root in (0,1) | **exactly 2/5** | **x\*_E = 0.3912978…** |
| `(5x−2)` divides numerators | yes, for `λ¹, λ², λ³` (multiplicities 3, 2, 1) | **no coefficient** |
| verdict | `λ_max ≡ 0` on `[2/5,1)` | `λ_max ≡ 0` on `[2/5,1)` (and in fact on `[x*_E,1)`) |

I also reproduce the executor's displayed `c₈` structure: my `λ¹` coefficient has denominator
`(x−2)¹²` and real roots in (0,1) consisting of `2/5` (×3) and the real root of
`7x³−17x²+16x−4 ≈ 0.3785` (×2), which is exactly
`x³(x−1)⁸(5x−2)³(2x²−5x+4)(4x²−5x+2)(7x³−17x²+16x−4)²/(x−2)¹²` up to the two root-free quadratics.
**Value-vs-formula (7f): FORMULA in x, verified symbolically, for both base points.** Claim 4 is
fully independently established (and, for type-E, strengthened to `[x*_E, 1)`).

**5.4 An observation that repairs part of the coverage gap (reviewer-authored, minor m4).**
The artifact names the n = 2 **balanced layer** as its main uncovered item and calls it "*generic*,
since λ_max = 0 on the whole strip". That characterisation is wrong in the conservative direction.
Balance means `Tr[D_Ψφ] = 0` with `D_Ψ ⪯ 0`, which forces `supp φ ⊆ ker D_Ψ`. I computed
`dim ker D_Ψ` exactly (`r7_kerD.json`):

| base point / x | 2/5 | 9/20 | 12/25 |
|---|---|---|---|
| isotropic product | **4** | **1** | **1** |
| type-E | **1** | **1** | — |
| P3g (r = 8) | — | **1** | — |
| P3s (r = 7) | — | **1** | — |

So at every strip point tested **except** the isotropic product exactly at x = 2/5, `ker D_Ψ =
span{Ψ}`, the only balanced state is `φ = P_Ψ`, and `ρ_ε ≡ P_Ψ` gives `Ic_2 ≡ 0`: the n = 2 balanced
layer is **empty**, exactly as the P9b datum emptied it at n = 1. This is a genuinely useful
narrowing of obligation (d) and belongs on the node; it is reviewer-authored evidence and licenses
nothing above NUMERICAL by itself.

---

## 6. Claim 5 — calibrations and the false-positive refutation. **CONFIRMED, with one leg void**

**6.1 G-cal1 / G-cal2.** G-cal1 is exact and reproduced (§4.4). For G-cal2 I re-verified the exact
NSD certificate at x = 11/20 for the isotropic-product family only (one of the executor's 13); the
remaining 12 exact rows and the 60 random Ψ at 11/20 are **not** independently re-run here — stated
as a scope limit, not a defect. My own strip probe (§6.4) is the substantive corroboration.

**6.2 The x = 2/5 F2 incumbent: the refutation holds, and I reproduced its decisive leg.**
I read the executor's float incumbent from the frozen `sweep_F2.json` and analysed it with my own
code (`tools/whgap_r7_checks.py E` → `r7_checks_EF.json`):

- **Singular values of M:** `(0.9999973, 2.33198·10⁻³, 6.895·10⁻¹⁷)` — numerically rank 2 but with
  `σ₂/σ₁ = 2.3·10⁻³`, i.e. drifting hard toward the rank-1 stratum. The executor's diagnosis is
  right.
- **Spectrum of `G_B` at that point** (this is the quantitative core): two machine zeros
  `(−6.8·10⁻¹⁷, −1.2·10⁻¹⁷)`, then **three eigenvalues at `6.53·10⁻⁷, 8.70·10⁻⁷, 8.71·10⁻⁷`**, then
  `4.00·10⁻², 1.600·10⁻¹, 1.600·10⁻¹, 6.400·10⁻¹`. The choice `m_B = 2` therefore *retains three
  eigenvalues of size 10⁻⁶* — these are the near-kernel of the nearby `m_B = 5` stratum, not genuine
  nonzero eigenvalues of a type-E point. My threshold sweep shows the discontinuity directly:
  relative floor `10⁻³…10⁻⁵` gives `m_B = 5` and `λ_max = 6.93·10⁻⁶`; floor `10⁻⁶…10⁻¹¹` gives
  `m_B = 2` and `λ_max = 1.99986·10⁻²`.
- **My own definitional slope measurement at that exact float point** (60 dps, raw entropies):
  ratios `−0.0154887, −0.0124720, −0.0061758` at `ε = 10⁻⁶, 10⁻⁸, 10⁻¹⁰` against the predicted
  `+0.0199986`. This matches the executor's `−0.0155, −0.0125, −0.0062` and is the decisive
  refutation: **independently confirmed**.

**6.3 Leg (iii) of the three-way refutation is non-evidential (minor m2).** "Rationalising the
incumbent (denominator 2520) and running the exact layer at x = 2/5 gives r = 9, m_B = 0 and
λ_max = 0" proves nothing about the point: rationalising in ambient ℂ^{3×3} leaves *every*
positive-codimension variety, so the same test would "refute" a genuine witness found anywhere on
the degeneracy variety. (The P13-B commission's own G+ protocol — "rationalize (Psi, top
eigenvector), re-verify EXACTLY" — inherits the flaw; a **chart-aware** rationalisation, e.g.
rational `a, y` in `M = u₀a^T + yu₀^T`, is what preserves `m_B ≥ 1` exactly. Worth fixing in future
commissions.) Legs (i) and (ii) are sound and suffice.

**6.4 My own independent strip probe.** `tools/whgap_r7_checks.py F` — 400 random points per x on
the F1 chart `M = u₀a^T + yu₀^T` with my own float pipeline (relative floor 10⁻⁶):

| x | 0.35 | 0.39 | **0.40** | **0.42** | **0.45** | **0.49** |
|---|---|---|---|---|---|---|
| best λ_max | 0.1333243 | 0.0181183 | 2.9e-16 | 2.3e-16 | 2.9e-16 | 2.7e-16 |

Below 2/5 the scanner returns strict positives (positive control passes); at and above 2/5 nothing
above 3·10⁻¹⁶. This corroborates the S3 strip null on the generic (m_B = 1) stratum with an
implementation that shares no code with the executor's.

---

## 7. MAJOR 2 — the coverage statement overstates what was searched

The bounded null is real, but §7's coverage statement is not honest about one stratum, and the
"13 structured families" head-count is inflated. Three concrete points:

**(a) The `m_B ≥ 2` strata are not numerically covered.** `λ_max(D_Ψ)` is **discontinuous** across
strata — `Π_B` jumps with `m_B`, so as `M` approaches a deeper stratum `Π_B(M)` converges to a
*proper subprojector* of `Π_B(M_0)` (§6.2 exhibits the jump numerically: same point, two floors, two
different `λ_max`). Therefore random/local search inside the **F1** chart, which is generic
`m_B = 1`, never probes `m_B ≥ 2`, and §5.1's repair — "F1, *which covers the whole variety modulo
symmetry*, returns ≤ 5.1·10⁻¹⁶" — does not repair the F2 failure. F1 covers P3 **as a set** mod
symmetry (that part is correct, §3.3); it does not cover P3's strata as a *search space*.
The `m_B = 2` stratum modulo the real `O(3)×O(3)` symmetry is **positive-dimensional** (the F2 chart
itself carries 12 real parameters via complex special-orthogonal `C₁, C₂`, and `r` is invariant under
`O(3,ℂ)²` while `λ_max` is invariant only under the real subgroup), and the only chart for it was
self-diagnosed as *numerically unfaithful*. Exact coverage of `m_B = 2` is at **two isolated orbits**
only: type-E `diag(1,1,0)` and P3s `u₀e₃^T+e₃u₀^T`, which I verified are **inequivalent** (the
normalised `O(3)×O(3)` invariant `Tr(MM^T)/‖M‖_F²` is 1 for type-E and 0 for P3s). The §7 "not
covered" list must name this; the suggested node wording "a 100-restart-per-point sweep over the
full degeneracy chart" must not stand.

**(b) The "13 structured families" collapse to about 7 orbits, three of which carry no
information.** `tools/whgap_r7_checks.py C` (`r7_checks_C.log`): I exhibited explicit **real
orthogonal** `(O₁, O₂)` with `O₁MO₂^T = scalar · M'` for
(a) `u₀u₀^T` → (d) `u₀ū₀^T`; (a) → (c) `uv^T` with both factors isotropic;
(e1) `diag(1,1,0)` → (e3) `diag(1,−1,0)`; (e3) → (e2) `E₁₂+E₂₁`; (b) `1` → (b2) cyclic `O` —
and verified the exact covariance identity `D_{(O₁⊗O₂)Ψ} = (O₁⊗O₂)D_Ψ(O₁⊗O₂)^T` symbolically at
x = 9/20 for a nontrivial rotation pair. So those rows have **identical** λ_max by symmetry, not by
independent computation (which is also why (a), (d), (c) all print 13/132 and (e1), (e2), (e3) all
print 1102933/9570000 — my table §4 reproduces the same coincidences). Moreover the three `m_B = 0`
rows (max-entangled ×2, `diag(1,i,0)`) are NSD for the structural reason `D = −M_E ⪯ 0` (§1.1); the
artifact says this for family (b) in §3.3 but still counts them among the 13 in §7's null.

**(c) A wording non-sequitur (minor m3).** "adding an exclusion criterion can only shrink the
accepted set, so every reported strip maximum remains a valid upper bound" — a valid upper bound
*over the accepted set* only; excluded points are not bounded by it. The following clause ("the
strip maximum over accepted points is ≤ 2.3·10⁻¹⁵") is the honest version and should replace it.

---

## 8. Minors

- **m1 — undefined term of art (rule 7g).** "cond ratio" / "conditioning criterion" is never
  defined in the artifact. §5 defines only the pre-registered gap discipline ("smallest kept
  eigenvalue exceeds 10⁶ × the accepted zero-cluster magnitude"), which the x = 2/5 F2 incumbent
  passes by **ten orders of magnitude** (my computation: zero-cluster/smallest-kept = 1.04·10⁻¹⁰).
  The quantity actually reported in `validation.json` and used in §5.1 leg (i) is
  (smallest kept eigenvalue)/(largest eigenvalue): `6.52537·10⁻⁷ / 6.399966·10⁻¹ = 1.0196·10⁻⁶`,
  exactly the printed `cond_ratio_B`. A reader applying the criterion as stated in §5 cannot
  reproduce leg (i). §5.1's pointer "(including the conditioning criterion, §8.1)" does not resolve
  either — §8.1 contains no such definition.
- **m2 — non-evidential refutation leg**: §6.3 above.
- **m3 — upper-bound non-sequitur**: §7(c) above.
- **m4 — "balanced layer is generic" is wrong (conservative direction)**: §5.4 above; the balanced
  set is `{P_Ψ}` at every strip point tested except the isotropic product exactly at 2/5, where
  `dim ker D_Ψ = 4`.
- **m5 — "type-E" is overloaded and a shared sympy trap.** "type-E" names both a single point
  (`diag(1,1,0)/√2`, whose exact certificates are what exist) and the 12-parameter F2 chart
  `{C₁diag(1,1,0)C₂}`; the two must not be conflated in the coverage claim. Separately: in a
  symbolic-in-x run, `sp.Symbol("x")` without a reality assumption leaves `conjugate(x)` unresolved
  and makes a Hermiticity gate fail spuriously (I hit this; the rational-x runs settle it). Also
  worth adding to the P13-A/B tooling list: on a denominator-cleared **integer** matrix, charpoly by
  **Newton identities from `Tr(N^k)`** finishes in ~1 s where symbolic-λ Berkowitz did not finish in
  10 min for the r = 8 point.
- **m6 — commission cap breached (honestly disclosed).** 150 min actual against the ≤ 120 min cap;
  the artifact reports this and explains it (the false-positive refutation). No concealment; recorded
  so the decision layer can decide whether the cap or the honesty rule governs.

---

## 9. What I did NOT verify (scope limits, stated per 7d/7f)

1. The **reviewed ingredients** of Lemma 2.1 (N1' Prop 3.3, Lemmas 4.1–4.2) — frozen at R5d scope
   "arbitrary kernel multiplicity `m ≥ 1`", which is exactly the use made here. I audited the
   *instantiation* and reproduced every constant (§1.3); I did not re-prove the lemmas.
2. The **full S3 sweep**: I did not re-run the 3445 s Nelder–Mead campaign, nor the F2/F3/F4 charts.
   My corroboration is 400 random F1 points per x (§6.4) plus the exact layer.
3. The float λ_max values at 7/20 for P3g/P3s/P3i/P3r, and 12 of the 13 exact rows at x = 11/20
   (G-cal2), remain executor-only.
4. The exact interval certificate covers the two named base points (I did both symbolically); no
   claim is made about other orbits beyond the pointwise exact rows of §4.
5. `{m_B ≥ 1} = P3` — corroborated 30/30 by my own hunt, still CONJECTURED. Nothing in claims 3–6
   depends on it; the S3 coverage does.

---

## 10. Licensing statement I would sign after repair (for the decision layer)

Not a menu selection — the verdict is **FINDINGS**. If MAJOR 1 and MAJOR 2 are repaired in the
artifact/node text (the numbers need no change), the evidence I gathered supports exactly this:

> The P13-B **exact** package is CERTIFIED\* at the following scopes, independently re-derived in
> review R7: (1) the S2 identity
> `⟨conj Ψ|(Λ⊗Λ)(P_Ψ)|conj Ψ⟩ = (1−x)²|Tr(MM^T)|² + x²‖adj M‖_F²` — **PROVED** as a symbolic
> identity in the 9 entries of M and in x, together with `Tr(M^TA_iMA_j) = −2 adj(M)_{ji}`, and its
> corollary that `conj Ψ` lies in the B-kernel exactly for rank-one M with an isotropic factor;
> (2) x-independence of `r, m_B, m_E` on (0,1), with `ker Λ^{(2)}(P_Ψ) = (span{Ahat_aMAhat_b^T})^⊥`
> — **PROVED**; (3) exact `λ_max(D_Ψ) = 0` at the 13 tabulated (family, x) rows, of which ~7 are
> distinct `O(3)×O(3)` orbits and 3 are structurally trivial (`m_B = 0`) — **PROVED at those
> orbits**; (4) `λ_max(D_Ψ(x)) ≡ 0` on `[2/5,1)` for the isotropic-product base point and on
> `[x*_E, 1)` with `x*_E = 0.391297769484659…` for the type-E base point — **PROVED** (symbolic in
> x, exact root isolation); (5) G-cal1 `= 13/132 = d₁(7/20)` exactly, with the isotropic-product
> family satisfying `λ_max ≡ d₁(x)` identically, and the x = 2/5 F2 false positive correctly refuted
> by the conditioning and definitional-slope legs (the rationalisation leg is void); (6) the exact
> type-E value `1102933/9570000` — **PROVED**, with the framing corrected: per channel use it is
> `0.0576 < d₁ = 0.0985` (the 2-copy coefficient is strictly subadditive), and the type-E point's
> own threshold is `x*_E < 2/5`, so the 2/5 threshold at n = 2 is attained by the **embedded n = 1
> product witness**, not by an entangled base point.
> The S3 sweep + calibrations are a sound **NUMERICAL** bounded null on the generic `m_B = 1`
> stratum and the product stratum, with the `m_B = 2` strata covered only at two isolated exact
> orbits (their chart F2 being numerically unfaithful) and with `{m_B ≥ 1} = P3` explicitly
> CONJECTURED. Nothing here establishes `Q^{(1)} = 0` or `Q = 0` on `[2/5, 1/2)`; the node stays
> **CONJECTURED**.

Reviewer-authored follow-ups worth registering as nodes (rule 8b; I registered none):
(i) the n = 2 **balanced layer looks EMPTY** on the open strip (`dim ker D_Ψ = 1` at every strip
point tested) — this is the artifact's own "main uncovered item" and it may already be closed;
(ii) a **faithful chart for the `m_B = 2` stratum** (exact rational parametrisation instead of
`expm` of complex antisymmetric matrices), which is the one real hole in the S3 coverage;
(iii) the per-Ψ threshold function `x*(Ψ)` and the conjecture `sup_Ψ x*(Ψ) = 2/5`, of which
`x*(product) = 2/5` and `x*(type-E) = 0.3912978…` are the first two exact values.

---

## 11. Reproduction, logs, hashes

All commands from the repository root with `C:<home>/cpython3119/python.exe`
(`PYTHONPATH=tools`):

```
python tools/whgap_r7_s2.py                       # claim 1  -> r7_s2.json
python tools/whgap_r7_exact.py                    # claims 2,3,5,6 (13 exact runs) -> r7_exact.json
python tools/whgap_r7_interval.py isoprod         # claim 4  -> r7_interval_isoprod.json
python tools/whgap_r7_interval.py typeE           # claim 4  -> r7_interval_typeE.json
python tools/whgap_r7_checks.py A                 # 7f slope gates + per-use audit -> r7_checks_A.json
python tools/whgap_r7_checks.py C                 # orbit collapse + covariance    -> r7_checks_C.json
python tools/whgap_r7_checks.py D                 # x-independence values          -> r7_checks_D.json
python tools/whgap_r7_checks.py E F               # false-positive audit + F1 probe -> r7_checks_EF.json
python tools/whgap_r7_variety.py                  # claim 7 corroboration -> r7_variety.json
python tools/whgap_r7_threshold.py                # MAJOR 1(b) -> r7_threshold.json
```

Reviewer scripts: `tools/whgap_r7_s2.py`, `whgap_r7_exact.py`, `whgap_r7_interval.py`,
`whgap_r7_checks.py`, `whgap_r7_variety.py`, `whgap_r7_threshold.py`.
Reviewer logs/JSON: `artifacts/logs_whgap_p13b_20260730/r7_*.json|log` (+ `r7_kerD.json` from the
inline `dim ker D_Ψ` run of §5.4, and `r7_diag_p3g.log` from the timing diagnosis of the r = 8 point).
Provenance notes, so nothing in the hash list is unexplained: `r7_checks_all.json` is a consolidated
**no-argument** run of `whgap_r7_checks.py` (all parts A–F) whose every section is **byte-identical**
to the corresponding per-part file (checked, all 7 sections `identical`); `r7_interval.log` is the
pre-rename output of the isotropic-product interval run and is **byte-identical** to
`r7_interval_isoprod.log` (`cmp` clean). Both are kept rather than deleted, and neither is relied on
above.
Hashes: `artifacts/logs_whgap_p13b_20260730/SHA256SUMS_r7.txt` (LF; verified with `sha256sum -c`
from the repository root). The reviewed package's own `SHA256SUMS_p13b.txt` was verified **before**
any frozen input was used: 24/24 `OK`.

**Compute:** about 55 min wall clock, single-process sympy/mpmath. One methodological cost is
recorded append-only: my first exact runner used a symbolic-λ Berkowitz determinant and stalled on
the r = 8 point (>10 min); it was replaced by the Newton-identity route on a denominator-cleared
integer matrix (~1 s), and the replacement was regression-checked against the two known values
13/132 and 1102933/9570000 before any new row was computed.

