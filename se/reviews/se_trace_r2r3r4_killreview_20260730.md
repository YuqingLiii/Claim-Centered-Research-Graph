# Independent review of the recorded kills on SE.denom.Phi.legal.trace.r2 / r3 / r4

Date: 2026-07-30
Reviewer: fresh Opus 5 instance (Claude Code subagent), commissioned by the SE lead
Role: **reviewer** (rule 6 / rule 7 independent kill review)
Scope: the three routes r2, r3, r4 of `SE.denom.Phi.legal.trace` only

---

## PRE-ACTION REPORT

**Files read from disk before any work** (pretask reload order):
`research/PRETASK_RELOAD_PROMPT.md`, `DAG_PROTOCOL.md`,
`research/RESEARCH_STRUCTURE_PROTOCOL.md`, `se/README.md`,
`se/proof-dag/nodes/SE.denom.Phi.legal.trace.yaml` (parent, incl. the
composition map rows for r2–r4 and the append-only "Refuted routes" list),
and the three target node files
`SE.denom.Phi.legal.trace.r2.yaml`, `.r3.md`, `.r4.md`.
Evidence read: `se/artifacts/se_mphys_20260719.md`, `se/artifacts/se_mphys2_20260719.md`,
`se/artifacts/se_eta_20260719.md`, `se/artifacts/se_frames3b_20260719.md`,
`se/artifacts/se_frames1_20260719.md` (Definition 2.1, §6 eq. (6.6)),
`se/artifacts/se_frames2_review_20260719.md` ((R.1), (R.16), (R.18)–(R.19)),
`se/artifacts/se_bigate_20260719.md` (§0, §1).

**Target nodes and status as read from disk**

| node | alias | status on disk | disposition |
|---|---|---|---|
| `SE.denom.Phi.legal.trace.r2` | R2DEAD | OPEN (`status_source: adjudicated-2026-07-20`) | PARKED |
| `SE.denom.Phi.legal.trace.r3` | R3DEAD | OPEN (`status_source: adjudicated-2026-07-20`) | PARKED |
| `SE.denom.Phi.legal.trace.r4` | R4DEAD | OPEN (`status_source: adjudicated-2026-07-20`) | PARKED |

All three carry `pending-review:` markers on their kills and "None yet on the
kill (pending)" under *Adversarial reviews*. The parent OR node
`SE.denom.Phi.legal.trace` records them as
`rel: ["kill recorded, independent review still owed"]`.

**Independence statement.** I did not author any of the reviewed mathematics.
I did not write `se_mphys_20260719.md`, `se_mphys2_20260719.md`,
`se_eta_20260719.md`, `se_frames3b_20260719.md`, or any of the scripts under
`se/artifacts/logs_se_mphys_20260719/` or `se/artifacts/logs_se_eta_20260719/`, and I
did not read those scripts before building my own construction (rule 7c). I was
given **no wanted outcome**: the commission states explicitly that a kill that
does not survive review is as valuable as one that does. Two of my three
verdicts below therefore contain findings that were *not* in the record (one
gap that I had to close myself before I could confirm r2/r3, and one
strengthening of r4).

**Highest status my evidence could license (per §2 ladder).** A counterexample
or failed audit on disk, confirmed by an independent reviewer ⟹ **REFUTED**,
writable by the independent checker. My deliverable is this review artifact; the
status write plus reason plus DEAD/PARKED tag and the node/index/Mermaid
synchronization belong to whoever holds the write commission (see *Conflicts*).

**Gates and deliverables of this commission (one line each).**
1. Locate the recorded kill on each of r2/r3/r4 and quote it with its citation.
2. Re-derive or re-compute the killing fact independently, exact arithmetic, no
   `Fraction`-from-float, python `<machine-local-path-redacted>`.
3. Apply the rule-7 items in scope: 7a typing of displayed operator identities,
   7f value-vs-formula, 7g quantifier scope (route as registered vs one instance).
4. Per-route verdict KILL-CONFIRMED / KILL-INSUFFICIENT / KILL-WRONG, with a
   REFUTED reason and a DEAD/PARKED recommendation when confirmed.
5. Frozen scope guard: a confirmed kill refutes ONLY that route — never the
   trace target, T6, or SE.

**Conflicts found between the commission text and the disk protocols.**

1. **Atomic-update vs read-only.** `PRETASK_RELOAD_PROMPT.md` §"Folder and DAG
   maintenance obligations" item 2 and `RESEARCH_STRUCTURE_PROTOCOL.md` §6.3
   require the result to be appended to the node file *in the same session*
   (rule 8c). The commission declares DAG/node files READ-ONLY for me and
   permits only this artifact. **Reported, not resolved**: I made no node edit.
   The outstanding transaction is listed in §5 below so it cannot be lost.
2. **Artifact placement of run material.** `RESEARCH_STRUCTURE_PROTOCOL.md` §4
   item 5 would put my scripts/logs under `se/artifacts/logs_se_<slug>_20260730/`
   with a `SHA256SUMS.txt`. The commission directs scratch to OS temp. I obeyed
   the commission; §6 records the scratch paths, the SHA-256 of every script,
   and a complete from-scratch construction recipe so that every number below is
   reproducible without those files.
3. No other conflict. (The two python interpreters are not a conflict: the
   commission's miniconda interpreter ran all mathematics; the pretask
   closeout interpreter ran the two validators.)

---

## 1. What I built, once, and used for all three routes

Everything below is my own construction from the *definitions* quoted in the
artifacts, never from the proposer's code.

**Objects (definitions, with citations).** `A={1,…,n}`, `B={1̄,…,n̄}`, `q=2n`,
query `1∈A`, `A°=A∖{1}` (`se_frames1_20260719.md` §1.1);
`λ=(q−j,θ)`; `Π_D` = orthogonal projector onto the `S_{(A⊔B)∖D}`-invariants of
`V_λ`, rank `f^θ`; `P_comp` = average over `S_B`; `Q_γ` = the central isotypic
projectors of the query stabilizer `G=S_{(A⊔B)∖{1}}` for the Young children
`τ_0=(q−j−1,θ)` and `τ_z=(q−j,θ−z)`;
`D_{a,b}={(I,J):I,J⊆A°,|I|=a,|J|=b,I∩J=∅}`, `D_s=I∪{ī:i∈J}`, `L_s=I∪J`,
`τ_s` = the commuting swaps `ī↔i, i∈J` (`se_frames3b_20260719.md` (R3b.5)–(R3b.8));
`𝒳_h=⊕_{s∈D_{a,b}} Ran Π_{D_{h,s}}`, `dim 𝒳_h=N_{a,b}f^θ`;
`S_{h,γ}(y_s)_s=P_comp Σ_s ρ_λ(τ_{h,s})Q_γ y_s` (R3b.23).

**My realization of `V_λ`.** For `θ=(2)`: `V_{(q−2,2)} = ker d` inside the
permutation module on 2-subsets of `[q]`, `d(e_{xy})=e_x+e_y`; the orthogonal
projector is `P = I − dᵀ((q−2)I+J)^{−1}d` with
`((q−2)I+J)^{−1} = (1/(q−2))(I − J/(2q−2))`.
For `θ=(1,1)`: `V_{(6,1,1)} = ker c` inside `Λ²C⁸`, `c(e_x∧e_y)=e_x−e_y`,
`P = I − (1/8)cᵀc`. Both bases are orthonormal and the `S_q`-action is
orthogonal, so all Gram/eigenvalue statements are literal. Verified:
`P=Pᵀ=P²`, `rank P = f^λ ∈ {20,21,35,54,77}`.

**My realization of `Q_γ`.** Not by a character sum: I use the query
Jucys–Murphy element `Y = Σ_{i=2}^{q} ρ_λ((1,i))`, whose eigenvalue on the
`τ`-branch of `Res_G V_λ` is the content of the box `λ/τ`. For `λ=(q−2,2)`:
contents `q−3` (long) and `0` (tail). For `λ=(6,1,1)`: `5` and `−2`. Verified in
every gate: `Q_γ²=Q_γ=Q_γᵀ`, `Σ_γ Q_γ = P`, `rank Q_γ = f^{τ_γ}`, and
`c_0−c_z = δ_z` exactly (5 and 7 at the two `q=8` gates), which is an
independent confirmation of the axial-distance convention `δ_z=ℓ−t+r`.

**Independent recovery of the frame constant.** I do not take `B_θ(q)` on
trust. `Σ_{|D|=j} Π_D` commutes with all of `ρ_λ(S_q)`, hence is scalar; its
trace is `C(q,j)f^θ`; therefore

    B_θ(q) = C(q,j) f^θ / f^λ,     Σ_{|D|=j} Π_D = B_θ(q) I_{V_λ}.

This is `(R.1)`/`(R.16)` of `se_frames2_review_20260719.md`, re-derived here in
two lines and **verified by exact matrices** in all five `q=8` gates
(`7/5` for `θ=(2)`, `4/3` for `θ=(1,1)`).

**Independent proof of the long-branch scalar `(R.18)`** (needed by r4, and the
only place the record leans on a frozen input): if `1∈D` then
`K_D=S_{[q]∖D}≤G`, so `Π_D` commutes with the `G`-central `Q_0`, and `Q_0Π_D`
is the orthogonal projector onto `(V_{τ_0})^{K_D}`, of dimension
`f^{τ_0/(q−j)} = 0` because `τ_0` has first row `q−j−1 < q−j`. Hence
`Q_0 Π_D = 0` for every `D∋1`, so `Q_0 T_{¬1} = Q_0 Σ_{all D} Π_D = B_θ(q)Q_0`.
Verified numerically as well: `T_{¬1}` is exactly `7/5` on the long branch and
`7/30 = (7/5)/6 = B/(δ_z+1)` on the tail at `θ=(2)`, and `4/3`, `1/6 = (4/3)/8`
at `θ=(1,1)`.

**Arithmetic hygiene.** `fractions.Fraction` and `sympy.Rational` only. No float
is created anywhere in the pipeline; no `Fraction(float)` call exists. Spectra
of the fibre Grams are obtained as exact eigenvalues of the rational matrix
`G·D²` (similar to the symmetric `DGD`), so no square root is ever approximated.

---

## 2. Route r2 — frame-side operator bound on `𝒳_h`

### 2.1 The kill as recorded

Node `se/proof-dag/nodes/SE.denom.Phi.legal.trace.r2.yaml`, *Claim* and
*Current status*:

> **Killed route (frame-side operator bound on 𝒳_h):** prove (T-a)/(T-b) via
> `X_h = S₀*S₀+Σ(δ_z+1)S_z*S_z ⪯ B_θ²I_{𝒳_h}` plus `Tr(L_hL_h*) ≤ T`.
>
> **OPEN, PARKED.** Kill evidence (proposer-level, exact): `‖S₀*S₀‖ = 56/25 >
> 49/25` and `8/3 > 16/9` at the hostile gates — the coherent fold of colorings
> into one output fiber inflates operator norms (`se_mphys_20260719.md` (0.1)).

Cited evidence: `se/artifacts/se_mphys_20260719.md` (0.1), with (1.5), (1.7),
(3.1), (3.2) and the nine-gate table in §4; parent-node ledger entry
"2. Frame-side operator bound on 𝒳_h — gate-refuted (56/25>49/25; coherent
fold)".

### 2.2 My independent re-computation

Literal `S_{h,γ}` matrices built from (R3b.23) for the canonical matching,
exact spectra of `A_γ = S_{h,γ}*S_{h,γ}` and of the weighted
`X_h = A_0 + Σ_z(δ_z+1)A_z` on `𝒳_h`:

| gate `(n,q,j,θ);(a,b)` | `dim 𝒳_h` | `B_θ²` | spec `A_0` | `‖A_0‖` | `‖X_h‖` | verdict on (1.5)/(1.7) |
|---|---:|---:|---|---:|---:|---|
| `(4,8,2,(2));(1,1)` | 6 | `49/25` | `56/25`(×2), `28/25` | **`56/25`** | **`14/5`** | **fails**, `8/7` and `10/7` |
| `(4,8,2,(1,1));(1,1)` | 6 | `16/9` | `8/3`, `32/21`(×2) | **`8/3`** | **`8/3`** | **fails**, `3/2` and `3/2` |
| `(4,8,2,(2));(0,2)` | 3 | `49/25` | `28/25`(×2), `14/25` | `28/25` | `7/5` | holds (`4/7`, `5/7`) |
| `(4,8,2,(1,1));(2,0)` | 3 | `16/9` | `4/3`, `16/21`(×2) | `4/3` | `4/3` | holds (`3/4`, `3/4`) |

Both recorded killer values are reproduced **exactly and independently**:
`‖S₀*S₀‖ = 56/25 > 49/25 = B_θ(8)²` and `8/3 > 16/9`, together with the joint
values `‖X_h‖ = 14/5` and `8/3` of (3.1)–(3.2). My spectra also match
`se_mphys2_20260719.md` (3.2)/(3.4) — `λ(A_0)=(56/25,56/25,28/25)` and
`(8/3,32/21,32/21)` — which I did not read until after computing them. Auxiliary
independent agreements: `dim 𝒪 = R = 6`, `dim 𝒳_h = N_{a,b}f^θ`, and the
`η`-values `14/15, 1/15, 20/21, 1/21` of `se_eta_20260719.md` §3.

### 2.3 Rule-7 findings

**7a (type audit of the displayed identity).** `L_h : 𝒞 → 𝒳_h` is
`(N_{a,b}f^θ) × dc`; `S_{h,γ} : 𝒳_h → 𝒪` is `R × (N_{a,b}f^θ)`; therefore
`S*S` and `X_h` are `(N_{a,b}f^θ)²` endomorphisms of `𝒳_h` and the right-hand
side `B_θ²I_{𝒳_h}` is typed correctly. I confirmed the three dimensions
independently at every gate (`R=6`, `N_{a,b}f^θ ∈ {3,6}`, `dc ∈ {2,3,6}`). The
multiplicity `c` enters only through `dim 𝒞 = dc` and never through `𝒳_h` or
`S_{h,γ}` — so this identity is `c`-free and a `c=1` counterexample is a
counterexample for every `c`. **PASS.** One typography nit: the node's Claim
line uses the symbol `X_h` for the *operator* while the artifact uses `𝒳_h` for
the *space* and `X_h` for the operator; on the node the two collide.

**7f (value vs formula).** My verification exercises an **independent
construction**, not the proposer's formula: I build `Π_D`, `Q_γ`, `P_comp`,
`ρ(τ_s)` and the literal columns `P_comp ρ(τ_s)Q_γ v̂_s` and diagonalize their
Gram. As a decoupled cross-check I then confirmed the proposer's *fold formula*
`‖S_{h,γ}‖²_HS = m N η_γ` (`se_mphys2` (2.7)) against my traces:
`Tr A_0 = 28/5 = 2·3·(14/15)` and `40/7 = 2·3·(20/21)`, and at
`n=5,6,7`: `81/7`, `176/9`, `325/11` versus `m N η_0` = same. So this review
establishes **both** the value and the printed formula, and says so.

**7g (quantifier scope) — the one real defect in the record, and how I closed
it.** The route as registered proves the universally quantified premise
`X_h ⪯ B_θ²I` over *admissible strict* sectors. Both recorded killer gates are
admissible (Definition 2.1 clauses 1–6 verified by me: `q=2n`; `θ⊢j`,`α⊢β⊢`;
`λ=(6,2)`/`(6,1,1)`, `κ=(2,1)`, `ν=(3,1)` partitions; `q−j−1=5≥θ_1`;
`n−1−a=2≥θ_1`, `n−b=3≥θ_1`; `c=1>0`) — **but neither is tame**: `n=4 < 3j=6`,
and `se_frames1_20260719.md` §2 states explicitly that "tameness is not part of
admissibility because several required gates have `n<3j`". The downstream
consumer of (T-a)/(T-b) uses `n≥3j` (`se_mphys_20260719.md` (5.3)). As
*recorded*, therefore, the kill refutes the route as registered but leaves the
obvious tame-restricted variant untouched — exactly the "one instance vs the
route" hazard 7g exists to catch. **I closed this gap myself** rather than
returning KILL-INSUFFICIENT: I ran the same literal construction for the
`θ=(2)`, `j=2`, `(a,b)=(1,1)`, `α=β=(1)`, `c=1` family at `n=4,5,6,7`
(`n≥6` is tame):

| `n` | `q` | `f^λ` | `B_θ` | `B_θ²` | `dim 𝒳_h` | `‖S₀*S₀‖` | `‖X_h‖` | ratio to `B_θ²` | tame? |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| 4 | 8 | 20 | `7/5` | `49/25` | 6 | `56/25` | `14/5` | `8/7`, `10/7` | no |
| 5 | 10 | 35 | `9/7` | `81/49` | 12 | `18/7` | `18/7` | `14/9` | no |
| 6 | 12 | 54 | `11/9` | `121/81` | 20 | `22/9` | `22/9` | **`18/11`** | **yes** |
| 7 | 14 | 77 | `13/11` | `169/121` | 30 | `26/11` | `26/11` | **`22/13`** | **yes** |

The premise fails at every one of them, in-range included, with ratio exactly
`(4n−6)/(2n−1) → 2 = m = C(j,a)`, i.e. the failure margin *grows* to the full
fold factor. This is not small-shape luck and is not curable by restricting to
the tame range. **7g now PASSES**, on evidence I generated.

**Frozen scope guard.** This refutes the frame-side operator premise only. The
trace targets (T-a)/(T-b) are not touched by it: at the same hostile gates the
actual traces pass (`(1862/375)/(294/25)` and `(256/63)/(32/3)`,
`se_mphys_20260719.md` §4), which is the whole point of the trace-level
successor. Nothing here bears on T6, on TRACE, or on SE.

### 2.4 Verdict — **KILL-CONFIRMED**

Licenses **REFUTED**. Reason (for the status write): *the route's frame-side
premise `X_h ⪯ B_θ(q)²I_{𝒳_h}` is false; the `m=C(j,a)`-fold of colourings into
one output fibre multiplies the frame Gram's top eigenvalue by `m`, and the
failure is uniform in-range — exact counterexamples `56/25>49/25` and `8/3>16/9`
at the admissible `(4,8,2)` mixed gates and `22/9>121/81`, `26/11>169/121` at the
tame `(6,12,2)`, `(7,14,2)` sectors, with ratio `(4n−6)/(2n−1)→2`.*
Disposition recommendation: **DEAD**. No restriction of the sector range repairs
a premise whose failure margin increases with `n`; a weakened operator bound
carrying the explicit factor `m` would be a different claim and needs its own
node (rule 8a).

---

## 3. Route r3 — easy trace route `(1.5)+(1.6)`

### 3.1 The kill as recorded

Node `SE.denom.Phi.legal.trace.r3.yaml`:

> **Killed route (easy trace route):** (1.5) `X_h ⪯ B_θ²I` combined with (1.6)
> `Tr(L_hL_h*) ≤ T` via the reviewed U_h column count.
>
> Kill evidence: premise (1.5) is the r2 failure; and (1.6)'s reviewed count
> applies to `U_h:𝓡_{a,b}→𝒞` (T source columns), not to `L_h:𝒞→𝒳_h` — no all-c
> identification exists (`se_mphys_20260719.md` §0 item 2). … Note
> `Tr(L_hL_h*) ≤ T` itself passes all nine c=1 gates and may be independently
> provable — that SUB-claim is not dead, only this route's use of it without (1.5).

Cited evidence: `se/artifacts/se_mphys_20260719.md` §0–§1.

### 3.2 My independent re-derivation

**Leg 1 — (1.5).** Identical to §2.2 above: refuted by my own exact
counterexamples, and (my addition) refuted throughout the tame range. Since
(1.5) is a *conjunct* of this route's hypothesis, the route dies on leg 1 alone.

**Leg 2 — the `U_h`/`L_h` column count.** I read the cited source statement
directly: `se_frames1_20260719.md` (6.6) reads
`J_raw*J_raw = I_{𝓡_{a,b}}`, `U_h*U_h ⪯ I_{𝓡_{a,b}}`, `‖U_h‖²_HS ≤ T`, with the
type audit printed one line below it — "*the Hilbert–Schmidt norm is taken for
the `D_ξ × T` matrix `U_h`*", and the count argument is "each of the `T`
unprojected raw source columns has norm one". `L_h` is `(N_{a,b}f^θ) × dc` by
(R3b.22). The two maps therefore have different column counts unless `dc=T`. I
computed both, exactly and independently, over the recorded gate set:

| sector | `f^λ` | `d=f^κf^ν` | `c` | `dc` | `T=N_{a,b}f^αf^β` | `dc = T`? |
|---|---:|---:|---:|---:|---:|---|
| `(3,6,1,(1);1,(1);0,())` | 5 | 1 | 1 | 1 | 2 | **no** |
| `(4,8,1,(1);1,(1);0,())` | 7 | 2 | 1 | 2 | 3 | **no** |
| `(4,8,2,(2);0,();2,(2))` | 20 | 2 | 1 | 2 | 3 | **no** |
| `(4,8,2,(1,1);2,(1,1);0,())` | 21 | 1 | 1 | 1 | 3 | **no** |
| `(4,8,2,(2);1,(1);1,(1))` | 20 | 6 | 1 | 6 | 6 | yes |
| `(9,18,3,(2,1);2,(2);1,(1))` | 1344 | 160 | 1 | 160 | 168 | **no** |
| `(7,14,6,(3,2,1);3,(2,1);3,(2,1))` | 23296 | 560 | **2** | 1120 | 80 | **no** |

So the identification fails already at `c=1` (four of the nine mandatory gates),
and fails by a factor of 14 at the recorded `c=2` stretch point — where my
independently computed `d=f^{(3,2,1)}f^{(4,2,1)}=16·35=560`, `c=2`, `dc=1120`,
`T=80` reproduce (R3b.27) exactly. The recorded statement "no all-`c`
identification exists" is **correct, and is stronger than recorded**: no
identification exists even at `c=1` in general.

### 3.3 Rule-7 findings

**7a.** Both displayed maps are typed correctly on the node and in the sources
(`U_h : 𝓡_{a,b} → 𝒞`, `D_ξ × T`; `L_h : 𝒞 → 𝒳_h`, `(N_{a,b}f^θ) × dc`), and my
dimension table confirms every entry. **PASS.**

**7d (frozen-input scope).** The route leans on `(6.6)` of `se_frames1`, whose
own recorded status is "CONJECTURED — pending-review: the typed induced-module
construction must be matched to the eventual formal output frames; no
identity-level `c≥2` gate exists". The kill uses `(6.6)` only *negatively* (it
does not cover `L_h`), so no unreviewed input is load-bearing for the kill.
**PASS.**

**7g.** Same scope hazard as r2 for leg 1, closed the same way. Leg 2 is a type
statement with no range restriction at all, so it is scope-clean by
construction. **PASS.**

**Structural observation (not a defect in the mathematics).** As registered, r2
and r3 are not disjoint OR-children: r3's premise (1.5) *is* r2's claim. One
counterexample therefore kills both first legs simultaneously. That is legal
under the OR semantics, but a reader of the parent should know the two children
share a premise; I recommend a one-line `related:` cross-link between r2 and r3
when the statuses are written.

**Frozen scope guard.** The sub-claim `Tr(L_hL_h*) ≤ T` is **not** refuted by
anything here or in the record: it passes all nine `c=1` gates and my dimension
audit shows only that (6.6) does not *prove* it. The r3 node already states this
correctly; the status write must preserve it (rule 3: do not over-kill).

### 3.4 Verdict — **KILL-CONFIRMED**

Licenses **REFUTED**. Reason: *both legs fail — the operator premise (1.5) is
false by exact counterexample (admissible and, per this review, tame sectors
alike), and the `T`-column contraction of (6.6) is a statement about
`U_h : 𝓡_{a,b}→𝒞` (`D_ξ×T`) that cannot be transported to `L_h : 𝒞→𝒳_h`
(`(N_{a,b}f^θ)×dc`), since `dc ≠ T` already at `c=1` and `1120 ≠ 80` at the
`c=2` stretch.* Disposition recommendation: **DEAD**, with the explicit carve-out
that the sub-claim `Tr(L_hL_h*) ≤ T` stays **OPEN** (9/9 gates, no proof, no
refutation) and remains available to other routes.

---

## 4. Route r4 — Hölder FIBER budget `(2.8)/(2.9)`

### 4.1 The kill as recorded

Node `SE.denom.Phi.legal.trace.r4.yaml`:

> **Killed route (Hölder FIBER budget):** the sufficient per-fiber conditions
> (2.8)/(2.9) `η₀ ≤ B_θf^αf^β` etc.
>
> Kill evidence (proposer, exact closed forms): `η₀ = B_θf^{τ₀}/C(q−1,j)`,
> weighted sum `= B_θf^λ/C(q−1,j)` EXACTLY — and the long condition fails
> IN-RANGE at (9,18,3,(2,1);2,(2);1,(1)) by 13/8, the joint by 168/85
> (`se_eta_20260719.md`). The nine small gates passing was small-shape luck.

Cited evidence: `se/artifacts/se_eta_20260719.md` (0.1)–(0.3), §4.1–§4.2; the
conditions themselves are `se_mphys2_20260719.md` (2.8)–(2.9).

### 4.2 My independent re-derivation

**Step 1 — the fibre trace is a two-projector overlap.** `L⊆A°` gives
`S_B ≤ K_L`, hence `P_comp Π_L = Π_L`; and `S_B ≤ G`, hence `[P_comp,Q_γ]=0`.
So `η_γ = Tr(P_comp Q_γ Π_L Q_γ P_comp) = Tr(Q_γ Π_L)`. Verified literally at
`q=8`: the five-factor and two-factor traces agree exactly for every branch
(`14/15` and `14/15`; `1/15`; `20/21`; `1/21`).

**Step 2 — the closed form, with no frozen input.** `G` is transitive on the
`N=C(q−1,j)` `j`-subsets avoiding the query and `Q_γ` is `G`-central, so
`Tr(Q_0Π_L) = (1/N)Tr(Q_0T_{¬1})`; by my two-line proof in §1,
`Q_0 T_{¬1} = B_θ(q)Q_0`, hence `η₀ = B_θ(q) f^{τ₀}/N` — the recorded (0.1).

**Step 3 — the killer sector, exact.** `(n,q,j,θ;a,α;b,β) = (9,18,3,(2,1);2,(2);1,(1))`:

    Definition 2.1:  q=2n ✓;  θ=(2,1)⊢3, α=(2)⊢2, β=(1)⊢1 ✓;
                     λ=(15,2,1), κ=(6,2), ν=(8,1) partitions ✓;
                     q−j−1 = 14 ≥ θ₁ = 2 ✓;  n−1−a = 6 ≥ 2 ✓, n−b = 8 ≥ 2 ✓;
                     c = c^{(2,1)}_{(2),(1)} = 1 > 0 ✓   (my own LR enumeration)
    TAME:            n = 9 = 3j ✓  — genuinely inside the range the chain needs

    f^λ = f^{(15,2,1)} = 1344      f^{τ₀} = f^{(14,2,1)} = 1105
    N   = C(17,3)      = 680       f^θ = 2,  f^α f^β = 1
    B_θ(18) = C(18,3)·f^θ/f^λ = 816·2/1344 = 17/14
    tails: z=(1,2): τ_z=(15,1,1), δ_z=14, f=120 ;  z=(2,1): τ_z=(15,2), δ_z=16, f=119

    consistency (mine):  Tr(T_{¬1}) = N f^θ = 1360
                       = B_θ(f^{τ₀} + Σ_z f^{τ_z}/(δ_z+1)) = (17/14)(1105+8+7) = 1360 ✓
    branching:           1105 + 120 + 119 = 1344 = f^λ ✓

    η₀ = (17/14)(1105/680) = 221/112
    η_(1,2) = 1/70 ,  η_(2,1) = 1/80
    η₀ + 15η_(1,2) + 17η_(2,1) = 12/5 = B_θ f^λ/N ✓

    (2.8-long):  η₀ /(B_θ f^α f^β) = f^{τ₀}/(N f^α f^β) = 1105/680 = **13/8 > 1**
    (2.8-tail):  45/136 < 1   (passes here)
    (2.9):       f^λ/(N f^α f^β) = 1344/680 = **168/85 > 1**

Every recorded number is reproduced exactly, including the equivalence of
(2.8-long)/(2.9) to the pure dimension inequalities `f^{τ₀} ≤ Nf^αf^β` and
`f^λ ≤ Nf^αf^β` (`se_eta` (2.5)–(2.7)).

**Step 4 — the §4.2 `c=2` stretch, also reproduced.** For
`(7,14,6,(3,2,1);3,(2,1);3,(2,1))` my own LR enumeration gives
`c^{(3,2,1)}_{(2,1),(2,1)} = 2`, and `f^λ=23296`, `f^{τ₀}=12012`, `N=1716`,
`B_θ(14)=33/16`, `f^αf^β=4`, `η₀=231/16`, `η_z=(5/8,9/16,3/8)` with
`δ_z=(6,8,10)`; ratios `7/4`, `175/132`, `112/33` — all three conditions fail,
exactly as recorded. **Note the record does not say so: this sector is
NOT tame** (`n=7 < 3j=18`). It is therefore corroboration, not in-range
evidence; the in-range weight rests entirely on Step 3.

### 4.3 Rule-7 findings

**7a.** The displayed objects are `f^λ×f^λ` endomorphisms throughout
(`P_comp, Q_γ, Π_L`); `Q_γ` is central for the query stabilizer `S_{[q]∖{1}}`
and **not** for `K_L` — the artifact states this and proves `K_L ⊄ G`, and my
matrices confirm `[Π_L,Q_γ] ≠ 0` (rank-2 commutator at every `q=8` branch), so
the tempting simultaneous-invariant "dimension count" reading is correctly
excluded. The `c`-dimensional LR space never appears in `η_γ`, so the identity
is `c`-free and the `c=1` counterexample is valid for all `c`. **PASS.**

**7f.** Two genuinely decoupled paths agree: (i) my closed form from `(R.1)` +
transitivity + my own proof of `Q_0Π_D=0` for `D∋1`; (ii) literal rational
matrices at `q=8` evaluating both the five-factor trace and the two-factor
trace. This review therefore establishes the **printed formula**, not merely the
values. **PASS.**

**7g / 7b — the recorded kill is in-range, and (my addition) it is generic.**
The recorded counterexample is a single sector. I asked whether it is
representative, by exact hook-length scan of every admissible sector with
`n ≤ 24`, `j ≤ 7` (10,587 admissible sectors, of which 4,057 tame):

| condition | tame admissible sectors where it FAILS | first (smallest `n,j`) | worst ratio |
|---|---:|---|---|
| (2.8-long) | **2853 / 4057** | `n=9, j=3, θ=(2,1)`, ratio `13/8` | `185/11` at `n=24,j=7,θ=(4,1,1,1)` |
| (2.8-tail) | **480 / 4057** | `(18,36,6,(4,2);2,(2);4,(4))`, ratio `903/620` | `770/247` at `n=21,j=7` |
| (2.9) | **2865 / 4057** | `n=9, j=3, θ=(2,1)`, ratio `168/85` | `2432/123` at `n=24,j=7` |

So the fibre budget fails on roughly 70 % of the tame admissible sectors, not at
one point, and the recorded `(9,18,3,(2,1))` really is the smallest in-range
failure. Two by-products worth recording: (a) the tail half of (2.8), which
*passes* at the recorded killer, does fail in-range further out — so all three
registered conditions are in-range refuted, which the node does not yet say;
(b) my scan's first (2.8-tail) failure is `(18,36,6,(4,2);2,(2);4,(4))` at
ratio `903/620` — bit-for-bit the ratio and sector recorded for the
*independently reviewed* T1 kill
(`se/artifacts/logs_se_trace_t1_independent_20260720/`), an unplanned cross-node
consistency check of my machinery against a review I did not write.

**Frozen scope guard — checked, and the record is right.** The kill refutes the
*sufficient fibre condition* only. At the very same sector the actual trace
targets pass with wide margin: `se_bigate_20260719.md` §0–§1 records the long,
tail and weighted joint traces at `(9,18,3,(2,1);2,(2);1,(1))` using
`≈60.2 %`, `1.87 %`, `62.1 %` of their budgets (`1996/3213` for the weighted
one), and states "the R4c fiber failure by `13/8` is therefore an artifact of
the separate fiber cap, not a near miss of the physical trace target". The η
closed forms (0.1)–(0.2) are a **positive asset** (I confirm them here) and must
survive the status write.

### 4.4 Verdict — **KILL-CONFIRMED**

Licenses **REFUTED**. Reason: *the sufficient per-fibre budget is equivalent to
the pure dimension inequalities `f^{τ₀} ≤ N f^α f^β` (2.8-long) and
`f^λ ≤ N f^α f^β` (2.9) with `N=C(q−1,j)`, and both fail at the admissible TAME
`c=1` sector `(9,18,3,(2,1);2,(2);1,(1))` by `13/8` and `168/85`; the failure is
generic in-range (2853 and 2865 of 4057 tame admissible sectors with `n≤24,
j≤7`), and (2.8-tail) also fails in-range from `(18,36,6,(4,2);2,(2);4,(4))`
onward by `903/620`.* Disposition recommendation: **DEAD** for the fibre-budget
route. Carve-outs that must appear in the status write: the exact fibre-trace
closed forms `η₀ = B_θ f^{τ₀}/N`, `η_z = B_θ f^{τ_z}/(N(δ_z+1))` and
`η₀+Σ(δ_z+1)η_z = B_θ f^λ/N` are **confirmed correct** by this review and remain
a positive asset consumed elsewhere; (T-a)/(T-b) are **not** refuted at this
sector.

---

## 5. Outstanding transaction (owed to the tree, not performed by me)

Because the commission made the DAG read-only for me, the following remain open
and must be executed by the write-commissioned agent in the session that reads
this artifact (rule 8c — recording a read result may not be deferred):

1. `r2`, `r3`, `r4`: status `OPEN → REFUTED` with the reasons quoted in §2.4,
   §3.4, §4.4 and disposition `DEAD` on all three; drop the `pending-review:`
   markers; cite this artifact under *Adversarial reviews* and *Evidence*.
2. Carve-outs to preserve verbatim: `Tr(L_hL_h*) ≤ T` stays **OPEN** (r3); the
   η closed forms stay a positive asset (r4); (T-a)/(T-b), T6 and TRACE are
   untouched.
3. Parent `SE.denom.Phi.legal.trace`: change the four `rel:` strings for
   r2/r3/r4 from "kill recorded, independent review still owed" to a citation of
   this review; recompute the OR bottom-up (it stays **OPEN** — T6 and t3 are
   unaffected, and r5/r6/r7 still carry unreviewed kills).
4. Optional cleanups this review surfaced: a `related:` cross-link between r2
   and r3 (shared premise (1.5)); the `𝒳_h`/`X_h` symbol collision on r2's Claim
   line; and — new information — a note on r4 that (2.8-tail) is also in-range
   refuted, and on §4.2 of `se_eta_20260719.md` that its `c=2` stretch sector is
   **not** tame.
5. Standing debt unchanged by me: `r5`, `r6`, `r7` still have no reviewed kill.

Closeout validators run by me (read-only, from the repository root):
`python tools/proof_dag_check.py --problem se` → `Proof-DAG validation OK: 82
nodes`, exit 0; `python tools/literature_check.py` → `Literature catalogs OK: 51
papers across 5 libraries, schema v1`, exit 0.

## 6. Reproduction

Interpreter: `<machine-local-path-redacted>` (3.10.18,
sympy 1.14.0). Exact rationals only; no float anywhere in the pipeline.
Scripts were written to the session scratchpad per the commission
(`…/<private-session-id-redacted>/scratchpad/`), SHA-256 (LF-normalized
source as written):

    a7647576bdc021ebc0230169475b2ec0e5ff16db2fee195c6040a6636d2c7911  se_r2r3r4_killcheck.py
    67be66483410c7fc1923c48ebcec2e9c3d07c360ace23dabb60e04be51ba5ae6  se_r2_tame_probe.py
    cd77925f0c1222347812212156bba84b3db7d7bcf131b775007a73e4c7a311c9  scan_r4.py
    9b08312f1dc81ebc0e7c04a64116f07a062a0b831f7f5233d68f253e74d8ed25  dims_r3.py
    d8e1b5758411f4a78947979722380d9f8c9e5119e777d36194f26943822e9559  probe2.py

Since the scratchpad is transient, §1 states the construction completely: the
`ker d` / `ker c` realizations of `V_λ` with their explicit rational projectors,
`Q_γ` from the query Jucys–Murphy element with the box contents, `Π_D` and
`P_comp` as orbit-average projectors, `B_θ(q)=C(q,j)f^θ/f^λ`, and the fibre
columns `P_comp ρ(τ_s)Q_γ v̂_s` whose Gram is diagonalized as the rational
`G·D²`. Any reviewer can rebuild it from that paragraph in under an hour and
should get the same rationals; if they do not, this review is wrong and should
be overturned.

**What would overturn each verdict.** r2/r3: an error in my `V_λ` realization or
in the identification of `Q_γ` with the Young branch — testable by checking
`rank Q_0 = f^{τ_0}` and `Σ_{|D|=j}Π_D = B_θ I`, both of which I verified.
r4: a different reading of (2.8)/(2.9)'s quantifier (if the route were only ever
intended for `f^αf^β` large enough that `f^{τ₀} ≤ Nf^αf^β` holds, the route
would be alive on that sub-range — but no such restriction is registered on the
node or in `se_mphys2` §2.2, and the scan shows the failing set is the majority
of the tame range).
