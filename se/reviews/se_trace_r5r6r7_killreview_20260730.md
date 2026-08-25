# SE trace routes r5 / r6 / r7 — KILL REVIEW (fresh independent adjudication)

**Date:** 2026-07-30 · **Reviewer:** Opus 4.8 subagent (rule 2/6 FRESH reviewer)
**Scope:** the recorded but never-reviewed kills on
`SE.denom.Phi.legal.trace.r5`, `.r6`, `.r7` (standing debt since SE DAG entry (49)).
**Reviewer run artifacts:** `se/artifacts/logs_se_trace_r5r6r7_killreview_20260730/`
(`se_r5r6r7_independent.py`, `run_r5_r6_gates.py`, `run_r7_commutator.py`,
`run_r5_r6_gates.log`, `run_r7_commutator.log`, `scope_scaling.log`, `SHA256SUMS.txt`).
**Immutable.** Append-only history; corrections go in a new dated artifact.

---

## PRE-ACTION REPORT

- **Target nodes and status as read from disk (2026-07-30):**
  - `SE.denom.Phi.legal.trace.r5` — **OPEN / PARKED** (`se/proof-dag/nodes/SE.denom.Phi.legal.trace.r5.yaml:7,9`)
  - `SE.denom.Phi.legal.trace.r6` — **OPEN / PARKED** (`…/SE.denom.Phi.legal.trace.r6.yaml:7,9`)
  - `SE.denom.Phi.legal.trace.r7` — **OPEN / PARKED** (`…/SE.denom.Phi.legal.trace.r7.yaml:7,9`)
  - Parent `SE.denom.Phi.legal.trace` — **OPEN**, OR node, fourteen children; the r5/r6/r7 rows of
    its `composition:` map each read `status: OPEN`, `rel: ["kill recorded …, independent review
    still owed"]` (`…/SE.denom.Phi.legal.trace.yaml:79-96`). `NODE_INDEX.md:68-70` agrees.
- **ROLE:** independent REVIEWER.
  **Independence statement:** I did not author any of the reviewed work. None of
  `se_mphys_20260719.md`, `se_mphys2_20260719.md`, `se_frames3_20260719.md`, nor anything under
  `se/artifacts/logs_se_mphys_20260719/`, `logs_se_mphys2_20260719/`, `logs_se_frames3_20260719/` is
  mine, and I did not open any proposer script. **I was given no wanted outcome:** my commission
  states explicitly that a kill which does NOT survive review is as valuable as one that does.
- **Highest status my evidence could license (§2 ladder):** **REFUTED** on each of r5/r6/r7 whose
  kill I confirm — writable by the independent checker (the decision layer) citing this review, per
  rule 6. Nothing higher, and nothing at all on the parent: a confirmed route kill is an OR-child
  refutation, which under §1 kills that route only.
  **I wrote no status anywhere.** This artifact is my only new file besides its run-log sibling
  (rule 1 requires command+log+SHA for every number I report); no DAG or node file was touched.
- **Commission gates / deliverables (one line each):** (1) locate the recorded kill per route;
  (2) re-derive or re-compute the killing fact independently in exact arithmetic, no
  `Fraction(float)`; (3) rule-7a type audit of every displayed operator identity in the kill;
  (4) rule-7f value-vs-formula statement; (5) rule-7g quantifier scope — does the kill refute the
  route AS REGISTERED; (6) per-route verdict KILL-CONFIRMED / KILL-INSUFFICIENT / KILL-WRONG with a
  DEAD/PARKED recommendation; (7) frozen-scope guard: a confirmed kill refutes only that route,
  never the trace target, T6, or SE; (8) this artifact.
- **Conflict between commission text and disk protocols:** **none on rules.** One conflict between a
  *node's own citation* and the disk is reported as finding **F-1** (r7 cites
  `se_mphys_20260719.md` §5 for a discussion that is not in §5).

---

## HEADLINE VERDICT

| route | registered claim (verbatim, node `## Claim`) | verdict | disposition recommended |
|---|---|---|---|
| **r5** | reversed Hölder `Tr(A_γD_h) ≤ ‖A_γ‖·Tr(D_h)` with `Tr(D_h)` replaced by `T` | **KILL-CONFIRMED** | **REFUTED / DEAD** |
| **r6** | h-averaging (R4b H3): the h-AVERAGED trace bounds are *strictly easier* than per-h | **KILL-CONFIRMED** | **REFUTED / DEAD** (scoped — see §3.4) |
| **r7** | compose-late / output-side-only: apply (R.32) before strict compression and move `P_ξ` last | **KILL-CONFIRMED**, subject to two mandatory record repairs (F-1, F-2) | **REFUTED / PARKED** (NOT DEAD — §4.5) |

None of the three kills is wrong. Two record defects and one over-kill risk were found; all are
bookkeeping, not mathematics. **No route verdict is reversed, and TRACE's computed status does not
move**: with r5/r6/r7 REFUTED, the OR is still `max` over `t3` (OPEN) and `t6` (OPEN) ⇒ **OPEN**.

---

## 1. Method — one independent reconstruction, thirty-odd exact cross-checks

### 1.1 What I built, and why it is independent (rule 7c)

I did **not** rerun the proposer scripts and did not read them. I rebuilt every object from the
*definitions* printed in the notes — `se_frames1_20260719.md` Definition 2.1 (admissible strict
sector); `se_frames3_20260719.md` (F3.9)–(F3.21) (literal cosets `D_{I,J}`, `Π_D`, `τ_{I,J}`,
branch projectors `Q_γ`, `P_comp`); `se_mphys_20260719.md` (1.1)–(1.2) (`L_h`, `S_{h,γ}`) — inside a
concrete permutation model that the proposer did not use:

- `V_λ` is realized as the **λ-isotypic subspace of a concrete permutation module of `S_q`**
  (multiplicity one in every case used), extracted by the character projector
  `P_λ = (f^λ/q!) Σ_g χ^λ(g) ρ(g)` with `χ^λ` computed by my own Murnaghan–Nakayama recursion
  (validated by `Σ_g χ^μ(g)² = |S_n|` for all `μ ⊢ 4` and for `(6,2)`, `(6,1,1)` on `S_8`).
  Ambients: `C^q` for `λ=(q-1,1)`; `C[2-subsets of [8]]` (dim 28) for `λ=(6,2)`;
  `C[ordered pairs of [8]]` (dim 56) for `λ=(6,1,1)`.
- Every group element acts by a permutation matrix, so `Π_D`, `Q_γ`, `P_comp`, `P_ξ` are exact
  **rational** matrices in the ambient orthonormal basis; there is no float anywhere and no
  `Fraction(float)` (the defect the R3b review caught in a neighbouring artifact).
- `P_ξ` is built as the `H = S_{A°} × S_B` isotypic projector for `V_κ ⊠ V_ν`; `Q_z` as the
  `S_{[q]\{1\}}`-isotypic projector for `τ_z = (q-j, θ-z)`; `Q_0 = P_λ - Q_z`.
- The fibre `Ran Π_{D_s} ∩ V_λ` is one-dimensional in every gate used (`f^θ = 1`), but the raw
  spanning vectors I extract have **unequal** norms `t_s`. Instead of introducing irrational
  normalizations I use the exact similarity `Δ G Δ ~ Δ² G` with `Δ² = diag(1/t_s)` rational, so all
  reported spectra and traces are exact rationals in the honest orthonormal fibre basis.

**Anchoring flag (7c).** My values coincide with the proposer's on every quantity I recomputed.
I flag the coincidence as required: it is agreement between two *different construction paths*
(character projectors in permutation modules + a `Δ²` similarity, versus the proposer's reduced
orthonormal fibre coordinates), not a reproduction of the proposer's derivation. I read the claims
and the object definitions — unavoidable, since verification requires the same objects — but no
proposer code and no proposer derivation of the killing numbers.

### 1.2 Type audit (rule 7a) — every operator in the three kills

Reproduced and **verified by rank**, not asserted:

| object | domain → codomain | dimension | verified |
|---|---|---|---|
| `C = P_ξ V_λ` (strict carrier) | — | `dc = f^κ f^ν · c` | `rank(P_ξ P_λ)` = `2,6,3,6,1` at the five `j=2` gates = `d·c` with `c=1`; `1,2,2,3` at the four `j=1` gates |
| `X_h = ⊕_{s∈D_{a,b}} Ran Π_{D_{h,s}}` | — | `N_{a,b} f^θ` | `rank(Π_D P_λ) = f^θ = 1`, `N_{a,b} = 3,6,3,6,3` |
| `O = Ran P_comp` | — | `R = f^{λ/(n)}` | `rank(P_comp P_λ) = 6` at all five `j=2` gates |
| `L_h : C → X_h` | `dc` columns | `(N_{a,b}f^θ) × dc` | `D_h = L_hL_h^*` is `6×6` PSD on `X_h` |
| `S_{h,γ} : X_h → O` | — | `R × (N_{a,b}f^θ)` | `A_γ = S^*S` is `6×6` PSD on `X_h` |
| `A_γ`, `D_h` | `X_h → X_h` | same space | `Tr(A_γD_h)` is well typed |
| strictness `Q_0P_ξ = P_ξ`, `Q_zP_ξ = 0` (F3.15) | — | — | **True in all five `j=2` gates** (independent check) |

`c` sits in the **domain** of `L_h` only; it is never appended to `S_{h,γ}` or to a branch of
`V_λ`. The reversed-Hölder inequality `Tr(A_γD_h) ≤ ‖A_γ‖ Tr(D_h)` is correctly typed (both
operators live on `X_h`) and is **true**; the kill therefore has to attack the *substitution*
`Tr(D_h) → T`, and it does. No mistyped display was found in any of the three kills.

### 1.3 Independent reproduction ledger (all exact rationals)

`run_r5_r6_gates.log` — five admissible strict sectors at `n=4, q=8, j=2`:

| gate `(θ;a,b)` | `B_θ(q)` | `T` | `m=C(j,a)` | `Tr D_h` | `‖L_h‖²` | `(T-a)` | `(T-b)` | `‖A_0‖` | `‖A_0+(δ_z+1)A_z‖` | joint trace | carrier `‖L^*X_hL‖/B²` |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `((2);0,2)` | 7/5 | 3 | 1 | 7/5 | 7/10 | 196/125 | 49/750 | 28/25 | 7/5 | 49/25 | 1/2 |
| `((2);1,1)` | 7/5 | 6 | **2** | 21/5 | 7/5 | 1862/375 | 427/1500 | **56/25** | 14/5 | 1001/150 | **17/12** |
| `((1,1);0,2)` | 4/3 | 3 | 1 | 2 | 4/3 | 16/7 | 1/21 | 4/3 | 4/3 | 8/3 | 1 |
| `((1,1);1,1)` | 4/3 | 6 | **2** | 4 | 4/3 | 256/63 | 1/21 | **8/3** | 8/3 | 40/9 | **2** |
| `((1,1);2,0)` | 4/3 | 3 | 1 | 4/3 | 4/3 | 16/9 | 0 | 4/3 | 4/3 | 16/9 | 1 |

Every one of these matches the recorded ledger: `se_mphys_20260719.md` §4 (both tables and the
`(0.1)` display), `se_mphys2_20260719.md` §2.4/§4, and — as a bonus — the **already-reviewed r1
killer ratios `17/12` and `2`** (`se_frames3b_review_20260719.md` §0), which my construction
reproduces without ever seeing R3b. `δ_z` was derived independently as the **axial distance of the
two removable corners of `λ`** (frames1 §1.1) and comes out `5` for `θ=(2)` and `7` for `θ=(1,1)`,
which is what makes the `14/5`, `8/3`, `1001/150`, `40/9` entries land exactly.
`B_θ(q) = \binom qj f^θ/f^λ` was recomputed from hook lengths (`f^{(6,2)}=20`, `f^{(6,1,1)}=21`).

Admissibility was checked item-by-item against **Definition 2.1**: both hostile sectors satisfy all
six conditions (`q=2n`; `θ,α,β` partitions; `λ=(6,2)`/`(6,1,1)`, `κ=(2,1)`, `ν=(3,1)` partitions;
long child `q-j-1 = 5 ≥ θ₁`; stable removal `n-1-a = 2 ≥ θ₁` and `n-b = 3 ≥ θ₁`;
`c = c^θ_{αβ} = 1 > 0`). Definition 2.1 states verbatim that the **tame** range `n ≥ 3j` is *not*
part of admissibility. The trace target as frozen on the parent node quantifies over "every
admissible strict sector", so **the counterexample sectors are inside the target's quantifier.**
This was the single largest scope risk in the whole review and it is clean.

---

## 2. r5 — reversed Hölder with `Tr(D_h) → T`

### 2.1 The recorded kill

Node: *"fails at the hostile rows by exactly 8/7 and 3/2 after the T replacement — it inherits the
coherent-fold operator failure (`se_mphys2_20260719.md` §0/§1 (1.5))"*. The source displays
`(2.12)`: `(336/25)/(294/25) = 8/7` and `16/(32/3) = 3/2`.

### 2.2 Independent recomputation

The route, spelled out, produces the bound `Tr(A_0D_h) ≤ ‖A_0‖·Tr(D_h) ≤ ‖A_0‖·T` and needs
`‖A_0‖·T ≤ B_θ(q)²T`, i.e. **`‖A_0‖ ≤ B_θ(q)²`**. My construction gives, exactly:

- `(4,8,2,θ=(2); a=b=1)`: `‖A_0‖ = 56/25`, `B_θ² = 49/25`, ratio **`8/7`**;
  route bound `‖A_0‖T = 336/25` versus cap `294/25`.
- `(4,8,2,θ=(1,1); a=b=1)`: `‖A_0‖ = 8/3`, `B_θ² = 16/9`, ratio **`3/2`**;
  route bound `16` versus cap `32/3`.

Both recorded rationals reproduce **exactly**, from an independent construction.

### 2.3 Mechanism, independently confirmed

The failure is not an artifact of one sector. At the three gates with `m = C(j,a) = 1`
(`(a,b) ∈ {(0,j),(j,0)}`) the ratio is `4/7` and `3/4`; at the two gates with `m = 2` it is exactly
`2 × 4/7 = 8/7` and `2 × 3/4 = 3/2`. That is the fold identity `S S^* = m \tilde S\tilde S^*`
(H4 / (5.2)) verified as a *consequence* of my independent numbers rather than assumed. Since
`max_{0<a<j} C(j,a)` is `2, 3, 6, 10, 20, 35, 70` for `j = 2,…,8` (`scope_scaling.log`), the deficit
is **unbounded in `j`**, not a near-miss.

### 2.4 Scope (rule 7g) — what is and is not killed

- The inequality `Tr(A_γD_h) ≤ ‖A_γ‖Tr(D_h)` is **true** and is not refuted.
- `(T-a)`/`(T-b)` **pass** at both hostile gates (`1862/375 < 294/25`, `256/63 < 32/3`). The kill is
  of the route, not of the target — exactly as the source says.
- The *un-substituted* variant `‖A_0‖·Tr(D_h)` is not a rescue: `1176/125 < 294/25` at the first
  hostile gate, but at the second it is `(8/3)·4 = 32/3 = ` the cap **exactly** — zero margin — and
  it would in any case need `Tr(D_h) ≤ T`, which is itself only NUMERICAL
  (`se_mphys_20260719.md` §7 claim table: "R1 (6.6) is not a proof for `L_h`").
- The route survives only on the `m = 1` faces `a ∈ {0, j}`. That is **not** the registered route
  (which is the uniform replacement) and must not be used to revive it; I record it as a local
  observation only.
- Entry (45)'s companion caution ("lossy variants cannot rescue the uniform constant; fibre loss
  `f^θ/f^αf^β` super-constant in the taper") is independently corroborated: on the admissible family
  `θ=(k,k)`, `α=β=(k)` (`c^θ_{αβ}=1`, admissible for `n ≥ 2k+1`) the loss is the Catalan number
  `1,2,5,14,42,132,429,1430,…` (`scope_scaling.log`). I did not re-verify the "in the taper"
  asymptotic statement itself, which belongs to entry (45), not to this kill.

### 2.5 Verdict

**KILL-CONFIRMED.** Licenses **REFUTED**, reason: *"the route's own output `‖A_0‖·T` exceeds the
target cap `B_θ(q)²T` by exactly `8/7` and `3/2` at the admissible strict sectors
`(4,8,2,(2);1,1)` and `(4,8,2,(1,1);1,1)`; the mechanism is the coherent fold `m = C(j,a)`, whose
deficit is unbounded in `j`."*
**Disposition: DEAD.** No repair exists for the registered uniform route; the node states no revive
condition and the `m = 1` faces are a different statement.

---

## 3. r6 — h-averaging (R4b's H3)

### 3.1 The recorded kill

Node: *"matching covariance makes every relevant trace INDEPENDENT of h, so the average EQUALS the
per-h value — zero gain (`se_mphys2_20260719.md` §0 item 3)."*

### 3.2 Independent re-derivation (analytic, mine, before computing)

Let `r_h ∈ S_B` be the matching relabelling, `r_h(\bar i) = \overline{h(i)}`. Then:

1. `D_{h,s} = r_h(D_{0,s})` for every `s = (I,J)` (because `r_h` fixes `A` pointwise), hence
   `Π_{D_{h,s}} = ρ(r_h)Π_{D_{0,s}}ρ(r_h)^{-1}` and the fibre bases satisfy
   `u_{h,s} = ρ(r_h)u_{0,s}`.
2. `τ_{h,s} = τ_{0,s} r_h^{-1}` is a legitimate extension of the fixed-set map for `D_{h,s}`
   (it sends `\overline{h(i)} ↦ \bar i ↦ i`, fixes `I`, fixes `1`), and `Π_D` absorbs the ambiguity
   in the extension, so nothing depends on the choice.
3. `r_h ∈ H = S_{A°}×S_B`, so `ρ(r_h)` **commutes with `P_ξ`**; `r_h` fixes the query point `1`, so
   `ρ(r_h)` **commutes with every `Q_γ`**; and `r_h ∈ S_B` so it commutes with `P_comp`.

Therefore, in the transported fibre bases, `S_{h,γ} = S_{0,γ}` **identically** and
`L_h = L_0 ρ_C(r_h)^{-1}` with `ρ_C(r_h)` unitary on `C`. Hence `A_γ(h) = A_γ(0)` and
`D_h = L_hL_h^* = L_0ρρ^*L_0^* = D_0`. Every trace `Tr(A_γD_h)`, every `‖B_{h,γ}‖_{HS}²`, and
`Tr(D_h)` are **exactly independent of `h`**; the `n!`-average equals the common value, which is
also the maximum. Improvement factor exactly `1`. This is stronger than the source's own argument
(which only observes `‖B_{h,γ}‖²_{HS}` is `h`-independent via the unitary right factor (4.2)).

### 3.3 Independent recomputation

`run_r5_r6_gates.log`: at each of the five admissible sectors I formed `L_h`, `S_{h,γ}`, `A_γ`,
`D_h` **separately for all `n! = 24` matchings `h ∈ S_4`** and collected the triples
`(T\text{-}a, T\text{-}b, Tr D_h)`. Result in every sector: **exactly one distinct triple over 24
matchings** (120 independent evaluations, zero variance). Values as in §1.3.

### 3.4 Scope (rule 7g) — the over-kill hazard, and how to word the REFUTED

The node's claim has two clauses. Clause (i), *"the h-averaged bounds are strictly easier"*, is
**false** — that is the kill. Clause (ii), *"averaged versions suffice for the assembly"*, is
**TRUE and load-bearing** (`se_mphys2` §4: the assembly uses `G_R = (1/n!)Σ_h …`; the source itself
records "H3 is sufficient for the assembly"). A bare `REFUTED` on r6 must therefore be written with
a reason that refutes only clause (i), or a later reader will conclude the averaged statement is
false and discard a correct reduction. This is the one place where I would push back on wording.

The second sentence of the source's item 3 — *"Twirling gives `G_R = I_d ⊗ M_ξ` but Schur structure
supplies no upper bound on `Tr M_ξ`"* — is an absence-of-evidence remark, not a refutation. It is
not needed: the exact equality alone kills clause (i). I did not verify it and it should not be
cited as part of the kill.

### 3.5 Verdict

**KILL-CONFIRMED** (re-derived analytically *and* re-computed exactly, 5 sectors × 24 matchings).
Licenses **REFUTED**, reason: *"zero gain — matching covariance makes `A_γ` and `D_h` exactly
`h`-independent, so the `n!`-average equals the per-h value; the 'strictly easier' premise is false.
This refutes the averaging-over-h route only; the sufficiency of the averaged statement for the
assembly is CONFIRMED and retained."*
**Disposition: DEAD** — the equality is exact and now analytically derived, so there is no repair of
the h-average. This does **not** touch `t4`'s L-average, which is a different node and stays where
it is.

---

## 4. r7 — compose-late / output-side-only

### 4.1 Sub-kill (A): `[P_ξ, Π_D] ≠ 0` — independently recomputed

Cited as `se_frames3_20260719.md` (F3.43), "in each of the four exact physical gates at
`(n,q,j)=(3,6,1),(4,8,1)`". `run_r7_commutator.log`, my construction, `λ = (q-1,1)` in `C^q`:

| gate `(n,q,j)`; `(a,b)` | `κ`, `ν` | `dc` | physical `D` | `[P_ξ,Π_D] = 0`? | `‖[P_ξ,Π_D]‖_F²` |
|---|---|---|---|---|---|
| `(3,6,1); (1,0)` | `(1,1)`,`(3)` | 1 | `{2}`, `{3}` | **No** | `12/25` each |
| `(3,6,1); (0,1)` | `(2)`,`(2,1)` | 2 | `{5}`, `{6}` | **No** | `8/25` each |
| `(4,8,1); (1,0)` | `(2,1)`,`(4)` | 2 | `{2},{3},{4}` | **No** | `160/441` each |
| `(4,8,1); (0,1)` | `(3)`,`(3,1)` | 3 | `{6},{7},{8}` | **No** | `12/49` each |

Confirmed at **all four gates and at every physical `D` in each gate** (10 index sets), with exact
rational Frobenius norms. The `dc` column `1, 2, 2, 3` independently reproduces
`se_frames3_20260719.md` §6.1. The conclusion drawn — *"the strict compression cannot simply be
moved to the last step"* — is exactly what non-commutation licenses, no more.

### 4.2 Sub-kill (B): the output-side-only variant

Node text: *"the output-side variant hits the ambient-versus-carrier trace mismatch (the `V_λ`-level
trace counts ambient directions, not the `T` source columns) (`se_mphys_20260719.md` §5
discussion)."*

**F-1 (record defect — mis-citation).** `se_mphys_20260719.md` §5 is *"Conditional chain through the
assembly constant"* and contains no ambient-versus-carrier discussion. The content actually lives in
(a) `se_frames3_20260719.md` §4, the paragraph immediately after (F3.43) — *"the resulting trace
counts ambient/carrier directions… does not justify replacing that count by the `T` source columns
in (F3.38)"*; (b) `se_mphys_20260719.md` **§6** ¶1 and its Rule-7(e) item 4
("ambient versus carrier"), plus §1 ¶3 on `U_h` (`T` source columns) versus `L_h` (`dc` carrier
columns); (c) `se_mphys2_20260719.md` §2.3. Rule 1 ("cite or it didn't happen") is not satisfied by
the citation as written; it must be repaired before a REFUTED write.

**F-2 (missing dependency).** As stated, (B) is an **absence-of-bridge** argument, not a refutation:
"the `V_λ`-level identity does not by itself give the `T`-column count" is a gap. What closes it is
that the bridge it names — the physical `T`-column factorization (F3.39)–(F3.41),
`B_{h,γ} = K_{h,γ}U_h^*` with `K_0^*K_0 + Σ_z(δ_z+1)K_z^*K_z ⪯ B_θ(q)²I_T` — is **separately
REFUTED / DEAD with a completed independent review**: node `SE.denom.Phi.legal.trace.r1`
(`…/trace.r1.md:7-9,29,45`), killed by the exact carrier-level ratios `17/12` and `2`, review
`se/artifacts/se_frames3b_review_20260719.md` §0 (Z1 and Z2 both CONFIRMED). **I reproduced those two
ratios independently** (§1.3, last column: `17/12` at `(4,8,2,(2);1,1)` and `2` at
`(4,8,2,(1,1);1,1)`), from my own construction, without opening R3b. So (B) is closed — but only via
r1, which the r7 node does not cite. The REFUTED write must add that dependency, otherwise r7's
record does not stand on its own.

### 4.3 Type audit of the (B) argument (7a)

The mismatch is real and correctly typed at the source. `E_{out,γ}` in (F3.35) has domain
`Q_γV_λ`, of dimension `f^{τ_γ}` — **not** `f^{τ_γ}·c`; the reviewed raw map `U_h` has `T`
source columns with `T = \binom{n-1}{a}\binom{n-1-a}{b}f^αf^β`; `L_h` has `dc` carrier columns.
At my hostile gates these are genuinely different counts (`T = 6` versus `dc = 6` coincidentally
equal there, but `T = 3` versus `dc = 2` at `((2);0,2)` and `T = 3` versus `dc = 1` at
`((1,1);2,0)`), so no `T ↔ dc` identification is available even at `c=1`. The quantitative loss
`f^θ/(f^αf^β)` is unbounded (Catalan family, §2.4).

### 4.4 Scope (rule 7g)

`[P_ξ,Π_D] ≠ 0` refutes **a specific rearrangement** (moving the strict compression to the last
step), not the existence of *any* output-side-first argument. The node already words its revive
condition correctly — *"only if a commutation-free reformulation appears"* — and that condition is
non-vacuous. The kill also does **not** touch `Q_γP_ξ`: strictness (F3.15) `Q_0P_ξ = P_ξ`,
`Q_zP_ξ = 0` holds exactly in all five of my `j=2` gates, so the branch projectors *do* commute
past `P_ξ` in the required sense; only `Π_D` obstructs.

### 4.5 Verdict

**KILL-CONFIRMED**, conditional on the two record repairs F-1 (citation) and F-2 (explicit r1
dependency). Sub-kill (A) is confirmed outright by independent exact computation; sub-kill (B) is
confirmed as a *dependent* kill resting on the already-reviewed r1 refutation, whose killer ratios I
also reproduced independently.

Licenses **REFUTED**, reason: *"the compose-late order is blocked by `[P_ξ,Π_D] ≠ 0`, exact at all
four `j=1` physical gates and every physical `D` therein; the output-side-only variant needs the
`T`-column factorization (F3.40)–(F3.41), which is REFUTED/DEAD on `SE.denom.Phi.legal.trace.r1`."*

**Disposition: PARKED, not DEAD.** I explicitly recommend **against** the node's own stated
expectation ("Reviewed kill ⟹ REFUTED/DEAD"). Under §1/rule 3, `DEAD = no repair`; r7 carries a
stated, non-vacuous revive condition (a commutation-free reformulation), and the kill refutes two
concrete orderings rather than the class. Marking it DEAD would be an over-kill of exactly the kind
rule 3 was written to prevent.

---

## 5. Rule-7 accounting

- **7a — type audit.** §1.2 and §4.3: every operator in the three kills typed as a function of all
  parameters (`n,q,j,θ,a,b,α,β,c`), with `dc`, `N_{a,b}f^θ`, `R`, `T` each verified by **rank**, not
  asserted. `c` occurs only in the domain of `L_h`. No mistyped display found.
- **7b — regime-complete identity gates.** All my gates are at **identity/matrix level** (full
  `6×6` Grams and their exact spectra, plus `28×28`/`56×56` ambient projector identities), not
  trace-only. **`c ≥ 2` is UNTESTED** here, as it is project-wide (`G-C2-TRACE`). *For a kill this is
  not a defect*: refuting a universal route needs one admissible counterexample, and `c=1` sectors
  are admissible. It would be a defect for any *proof*, and I claim none. I state this explicitly so
  the label is not silently inherited: **the three REFUTED writes are `c=1`-witnessed and that is
  sufficient; nothing about `c ≥ 2` is established or needed.**
- **7c — anchoring ban.** Independent model and independent character machinery; no proposer script
  or derivation read. Coincidence of values flagged in §1.1 as required.
- **7d — no frozen-input immunity.** I re-opened rather than granted: `B_θ(q) = \binom qj f^θ/f^λ`
  recomputed from hook lengths; admissibility re-checked item-by-item against Definition 2.1 for
  every sector I used; `δ_z` re-derived from the axial-distance definition instead of being taken
  from the notes; the strictness identities (F3.15) re-verified rather than assumed.
- **7e — standing failure modes.** Checked: dropped/extra normalization (the `Δ²` similarity exists
  precisely to avoid a hidden fibre rescaling; `B_θ` and `T` recomputed); type/dimension mismatch
  (§1.2); undefined terms of art (§7g below); colored-orbit sum silently replaced by a full central
  sum (my `Π_D` is the literal pointwise-stabilizer average over the actual `D_{I,J}`, and the
  physical index set `D_{a,b}` is enumerated literally, `N_{a,b} = mN` verified as `3,6,3,6,3`);
  numerics validating a value while a printed derivation is broken (addressed in 7f); sum-versus-
  maximum (all my `j=2` gates have a single tail branch `z`, so I neither used nor tested a
  multi-tail sum-to-maximum step — **declared untested**); `Fraction(float)` (none — no float is
  constructed anywhere in my scripts).
- **7f — value-versus-formula.** My code exercises an **independent construction** of the same
  objects, not the proposer's printed formulas or code path. Consequently: what I have established
  is that the **killing values are correct** (`8/7`, `3/2`, per-h ≡ average, `[P_ξ,Π_D] ≠ 0`, and
  incidentally `17/12`, `2`). I have **not** audited the proposer's scripts or their internal
  derivations, and this review does not certify them. For a kill, value-level correctness is exactly
  what is load-bearing, so the gap is immaterial — but it must not be read as a certification of
  `logs_se_mphys*` / `logs_se_frames3*` as software.
- **7g — quantifier hygiene.** Terms resolved to on-disk definitions: *admissible strict sector* →
  `se_frames1_20260719.md` Definition 2.1 (checked item-by-item; **tame `n ≥ 3j` is explicitly not
  part of it**, so my `n=4, j=2` counterexamples are inside the target's quantifier); *axial
  distance* → frames1 §1.1; *long/tail branch*, `δ_min`, *strict carrier*, *completion*, `T`,
  `B_θ(q)` → frames1/frames3 as cited. Per-route scope conclusions in §2.4, §3.4, §4.4.

---

## 6. Findings (record defects; none reverses a verdict)

| id | severity | finding |
|---|---|---|
| **F-1** | MAJOR (record) | r7 cites `se_mphys_20260719.md` §5 for the ambient-versus-carrier discussion; §5 is the conditional assembly chain and contains no such discussion. Correct locators: `se_frames3_20260719.md` §4 (paragraph after (F3.43)); `se_mphys_20260719.md` §6 ¶1 and §1 ¶3; `se_mphys2_20260719.md` §2.3. **Must be repaired before the REFUTED write** (rule 1). |
| **F-2** | MAJOR (record) | r7's output-side sub-kill is, as written, a gap statement. It closes only through `SE.denom.Phi.legal.trace.r1` (REFUTED/DEAD, reviewed). The r7 node does not cite r1. **The dependency must be added** or r7's record does not stand alone. |
| **F-3** | MODERATE | r6's node claim bundles a **false** clause ("strictly easier") with a **true, load-bearing** clause ("averaged versions suffice for the assembly"). A bare REFUTED will be misread. Reason string must scope the refutation to the first clause (wording in §3.5). |
| **F-4** | MODERATE | r7's node predicts "Reviewed kill ⟹ REFUTED/**DEAD**". I recommend **PARKED**: a non-vacuous revive condition is stated on the node itself, and the kill refutes two concrete orderings, not the class (rule 3, do not over-kill). |
| **F-5** | MINOR | r5's node says the route "inherits the coherent-fold operator failure". Confirmed and now quantified: the ratio is exactly `m = C(j,a)` times the unfolded ratio (`4/7 → 8/7`, `3/4 → 3/2`), and `max_{0<a<j}C(j,a)` grows without bound. Suggest recording the mechanism, since it is what makes DEAD (rather than PARKED) correct. |
| **F-6** | MINOR (informational) | The second sentence of `se_mphys2` §0 item 3 ("Schur structure supplies no upper bound on `Tr M_ξ`") is absence-of-evidence, not a refutation. It is not needed for r6's kill and should not be cited as part of it. |

---

## 7. Frozen scope guard — what these three confirmations do NOT establish

Stated explicitly, per commission:

1. **The trace target is untouched.** `(T-a)` and `(T-b)` **pass** at every gate I computed,
   including both hostile ones. Nothing here bears on the entry-(76) refutation of the *universal
   raw* T-a endpoint, which rests on different (`c=2`, `n=18,19`) evidence I did not examine.
2. **T6 is untouched.** I computed nothing about `J = ω²rawT_a + rawT_b = d Tr(M_ξ)` or the PSD
   target `M_ξ ⪯ (15/4)B_θ(q)²ω I_c`.
3. **TRACE does not move.** OR-status `= max_B min(status(B), status(route B→A))`; with
   r5/r6/r7 REFUTED the maximum is still carried by `t3` (OPEN) and `t6` (OPEN) ⇒ **TRACE stays
   OPEN**, and every ancestor is unchanged. The three writes are bookkeeping-only for propagation;
   their value is that the OR's dead branches stop being re-proposable.
4. **SE / the root proposition is untouched**, and nothing here says anything about `research/ksum`
   or `channel-capacity` (out of scope, not opened).
5. **`c ≥ 2` remains untested** everywhere in this review, by design (see 7b).
6. **The remaining unreviewed kills — r2, r3, r4 — are out of my scope** and remain OPEN/PARKED with
   their reviews still owed.

## 8. Recommended DAG writes (for the decision layer; I wrote none)

| node | write | reason string (short form) | disposition |
|---|---|---|---|
| `SE.denom.Phi.legal.trace.r5` | `OPEN → REFUTED` | route output `‖A_0‖·T` exceeds `B_θ²T` by exactly `8/7` and `3/2` at admissible strict `(4,8,2,(2);1,1)`, `(4,8,2,(1,1);1,1)`; mechanism = coherent fold `m=C(j,a)`, deficit unbounded in `j` | **DEAD** |
| `SE.denom.Phi.legal.trace.r6` | `OPEN → REFUTED` | zero gain: covariance makes `A_γ`, `D_h` exactly `h`-independent, so the `n!`-average equals the per-h value; refutes the "strictly easier" premise only — averaged-suffices is CONFIRMED and retained | **DEAD** |
| `SE.denom.Phi.legal.trace.r7` | `OPEN → REFUTED` | compose-late blocked by `[P_ξ,Π_D] ≠ 0` (exact, four `j=1` gates, all physical `D`); output-side-only needs (F3.40)–(F3.41), REFUTED/DEAD on `trace.r1` | **PARKED** (revive: a commutation-free reformulation) |

Each write must cite **this artifact** and repair F-1/F-2 on r7 and F-3 on r6. The parent
`SE.denom.Phi.legal.trace` composition rows for r5/r6/r7 move `OPEN → REFUTED` with
`rel: ["reviewed kill"]`, matching the existing r1 row; the parent's own status is **recomputed
OPEN**, unchanged. `NODE_INDEX.md:68-70` must be synchronized in the same diff.

## 9. Reproduction

Python: `<machine-local-path-redacted>` (3.10.18; sympy 1.14.0 used only for
exact eigenvalues of rational matrices). All arithmetic is `fractions.Fraction` / integer; no float
is constructed anywhere, hence no `Fraction(float)` hazard.

```
cd se/artifacts/logs_se_trace_r5r6r7_killreview_20260730
python run_r7_commutator.py     > run_r7_commutator.log     # r7, four j=1 gates
python run_r5_r6_gates.py       > run_r5_r6_gates.log       # r5 + r6, five j=2 gates x 24 matchings
```

`SHA256SUMS.txt` in that directory records SHA-256 of all three scripts and all three logs.
No DAG, node, index, or paper file was edited by this review.
