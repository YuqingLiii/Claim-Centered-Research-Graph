# WHGAP R5d — fresh independent review of the N1′ expansion lemma note

**Artifact type:** independent adversarial review (immutable). **Node:** `WHGAP.no-ascent-hierarchy` (P9).
**Commission:** `channel-capacity/werner-holevo-gap/notes/WHGAP_REVIEW_COMMISSION_R5_20260729.md`, section **R5d**.
**Reviewed input (frozen, hash-verified):**
`channel-capacity/werner-holevo-gap/notes/WHGAP_N1PRIME_EXPANSION_LEMMA_20260729.md`
SHA-256 `5b8ccf95953162283ba161da3c64761df313d4dd60d5cd9050f4a52cebe80c56`.
**Reviewer:** fresh Opus instance, 2026-07-29 (night). **Interpreter:** `C:<home>/cpython3119/python.exe`
(sympy 1.13.1, mpmath 1.3.0).
**Own scripts:** `tools/whgap_r5d_indep.py` (48 gates), `tools/whgap_r5d_edge.py` (360 residual tests).
**Own logs:** `artifacts/logs_whgap_r5_20260729/r5d_indep.{json,log}`, `…/r5d_edge.{json,log}`,
hashes in `…/SHA256SUMS_r5d.txt` (LF).

---

## 0. PRE-ACTION REPORT (mandatory, `research/PRETASK_RELOAD_PROMPT.md`)

Files read from disk, completely, in the prescribed order before any mathematics:
`research/DAG_PROTOCOL.md` (whole file — §1 data structure, §2 ladder + completion gate, §3 rules 1–8,
§4 READ / §5 WRITE / §6 session-close);
`research/RESEARCH_STRUCTURE_PROTOCOL.md` (§1–§10, incl. §4 placement, §5 naming, §6 atomic update,
§7 move/archive, §9 closeout, §10 root-level field folders);
`channel-capacity/werner-holevo-gap/README.md`;
`channel-capacity/werner-holevo-gap/notes/WERNER-HOLEVO-GAP_PROOF_DAG.md` (header, eight inlined rules,
Mermaid, nested outline);
`channel-capacity/werner-holevo-gap/proof-dag/NODE_INDEX.md`;
target node `proof-dag/nodes/WHGAP.no-ascent-hierarchy.md` and its parent `nodes/WHGAP.goal.md`
(the node has no children);
then the commission `notes/WHGAP_REVIEW_COMMISSION_R5_20260729.md`, then the reviewed note.

- **Target node and its status as read from disk:** `WHGAP.no-ascent-hierarchy` (alias P9), kind LEAF,
  role proof, **status CONJECTURED**, `status_source: "decision-layer derivation 2026-07-29 (first-order
  closed form derived in-node; pending review)"`, `disposition: null`, parent `WHGAP.goal` (OPEN),
  children none. Node section *Adversarial reviews*: **"None yet."** Both P9-E1 and P9b findings on the
  node carry explicit `pending-review:` markers. `NODE_INDEX.md` row and the DAG doc's Mermaid label /
  nested outline all agree: CONJECTURED, pending-review.
- **My ROLE: reviewer. Independence statement.** I did not author the reviewed note, its script
  `tools/whgap_n1p_sanity.py`, or any prior WHGAP work (P1–P12, R1–R5c). I was given **no desired
  outcome**: the dispatch handed me the R5d licensing menu as alternatives. Anchoring discipline (7c):
  I built my own Kraus operators, my own basis order, my own kernel projector and my own numerics and
  ran them to completion **before** reading the note's script or logs; I never executed
  `tools/whgap_n1p_sanity.py` at all. I read the R5c review's verdict section only *after* my own gates
  had passed, and only to record its scope (§7 below); no internal step of my review relies on it.
- **Highest status my evidence could license per §2:** with this review completed and archived,
  **PROVED** becomes available for the Lemma and the Theorem — writable **only by the decision layer /
  an independent checker**, not by the note's author, citing this artifact (rule 6). I write no status
  anywhere (single-writer deviation, below).
- **Gates and deliverables of my commission, one line each:**
  (i) re-derive every inequality and remainder bound in the note (7a–7g);
  (ii) check the degenerate-perturbation bound proof line by line;
  (iii) verify the B-side exact diagonalization symbolically myself;
  (iv) reproduce the sanity table with my own script at ≥ 2 of the 3 x-values;
  (v) audit the Theorem's dependence structure (only the closed-form *value* of w_B − w_E may come from
  R5c scope, cleanly cited);
  (vi) write `artifacts/whgap_r5d_review_20260729.md` and pick exactly one verdict from the R5d menu.
- **Conflicts between commission text and disk protocols: two, both benign, reported not resolved.**
  1. *Single-writer deviation.* `DAG_PROTOCOL.md` §5/§6 and `RESEARCH_STRUCTURE_PROTOCOL.md` §6 (rule 8c)
     require me to append this review to the node's *Adversarial reviews* section in this session. The
     commission (§ "Single-writer deviation (binding)") forbids agents in this batch from touching node
     files, `NODE_INDEX.md`, or the DAG doc, and assigns the atomic update to the decision layer. I
     comply with the commission and record the outstanding obligation: **this report is not yet linked
     from `WHGAP.no-ascent-hierarchy`; the decision layer owes that link, plus the `Adversarial reviews`
     entry, before further work is commissioned.**
  2. *`SHA256SUMS.txt` name.* The commission asks for `SHA256SUMS.txt` in
     `artifacts/logs_whgap_r5_20260729/`; that file already exists (R5a) and §7 of the structure
     protocol forbids overwriting cited history. I follow the established per-role pattern
     (`SHA256SUMS_r5b/_r5c/_n1p`) and write **`SHA256SUMS_r5d.txt`** with LF endings.
- **Standing failure modes screened (commission §2), item by item:**
  1. *sympy `.H` / `conjugate(sqrt(1−x))`* — screened and **hit in my own script**, in a variant the note
     did not report: substituting the keys `S**4 → (x/2)**2, T**4 → (1−x)**2` makes sympy match
     `S**2 = (S**4)**(1/2)` and returns `Abs(x−1)`, silently breaking five gates. Fixed by substituting
     only `S*T`, `S**2`, `T**2` and then *asserting no free `S`,`T` survives* (`has_odd`), which is the
     soundness condition for the substitution. All symbolic algebra is carried in positive real symbols
     `S = sqrt(x/2)`, `T = sqrt(1−x)`, so no `.H` ever meets a symbolic radical; an independent exact
     route repeats every algebraic gate at **five rational x** with sympy's exact `sqrt(Rational)`,
     where conjugation resolves by itself.
  2. *WindowsApps store python* — not used; the pinned interpreter throughout.
  3. *Complement convention drift* — I rebuilt the padded 4×4 `Λ^c(Y)_{ab} = Tr(K_a Y K_b^†)` from the
     Kraus operators and verified `Σ_a K_a Y K_a^† = Λ_x(Y)` on all nine complex entries of a generic Y
     (gate R1) plus `Σ_a K_a^†K_a = 1` (R1). No 3-dim variant, no sign or k-factor alternatives were used.
  4. *Transpose vs conjugate-transpose* — gate `R1.kraus_real` verifies `K_a = conj(K_a)` entrywise, so
     `K_a^† = K_a^T` is licensed for the Kraus operators only; states are never transposed in place of
     conjugation.
  5. *`sorted()` on symbolic eigenvalues* — avoided: symbolic spectra are compared as **sets** of
     simplified expressions, or via `det(λ·1 − M)` polynomial identity, never sorted.
  6. *CRLF in SHA256SUMS* — `SHA256SUMS_r5d.txt` written with LF (verified: 0 CR bytes) and
     `sha256sum -c` passes. I also re-verified the note's `SHA256SUMS_n1p.txt`: 0 CR bytes, `-c` all OK.
  7. *Eigenvalue bookkeeping at degeneracies / dividing by small gaps* — this is the core of §3 of the
     note; I checked line by line (§3 below) that **no** difference of cluster slopes is ever divided by,
     and stress-tested the bound at kernel multiplicities m = 1, 2, 3 (gate R10).
  8. *ε log ε bookkeeping* — Lemma 4.1 checked (§4 below); `0 log 0 = 0` handled in my own `h(u)`;
     `O(ε² log(1/ε)) = o(ε)` is made quantitative and I verified the resulting bound numerically at
     four x and, in the supplementary run, at **six x × five random isotropic ψ × three random φ ×
     four ε including ε = x/8 exactly**.
  9. *Anchoring* — see the independence statement above.

---

## 1. Type audit (7a) — every object in the reviewed claims

| symbol | type | dimension / parameters | checked how |
|---|---|---|---|
| `x` | real parameter | `x ∈ (0,1)` | all statements carry the range; endpoints excluded |
| `ε` | real parameter | `ε ∈ (0, x/8]` in Lemma 5.1; `ε ∈ (0, ε₁(x))` in Thm 8.1 | hypothesis ranges cross-checked against every use |
| `Λ_x` | CPTP superoperator | `M₃(ℂ) → M₃(ℂ)` | R1: Kraus sum equals the displayed affine map on 9 generic complex entries |
| `K_0..K_3` | Kraus operators, **real** | 3×3 each, 4 of them | R1: `Σ K_a^†K_a = (T²+2S²)1 = 1`; `K_a = conj(K_a)` |
| `Λ_x^c` | CPTP superoperator | `M₃(ℂ) → M₄(ℂ)` (padded) | R2: rebuilt from `Tr(K_a Y K_b^†)`; rank 2 at pure isotropic input |
| `ψ, ψ̄, e₃` | kets | ℂ³, unit, mutually orthonormal for isotropic ψ | R2: `ψᵗψ = 0`, `⟨ψ|ψ̄⟩ = 0`, `Pᵗ = P_ψ̄` |
| `P = |ψ⟩⟨ψ|`, `φ`, `ρ_ε` | states (PSD, trace 1) | 3×3 | R9/edge: random `φ` drawn as `ZZ^†/Tr` |
| `Λ(ρ_ε)` | state | 3×3, rank 3 for ε ∈ (0,1) | R3: exact diagonal form |
| `Λ^c(ρ_ε)` | state | **4×4**, rank 4 for ε ∈ (0,1) | R4: block-diagonal `A(ε) ⊕ B(ε)` in the index split {0,3}⊔{1,2} |
| `Π_E` | orthogonal projector | 4×4, **rank 2** | R5: `Π_E = Π_E^†= Π_E²`, `Tr Π_E = 2`, `Π_E Λ^c(P_ψ) = 0`, symbolically in x |
| `A, B` (Prop 3.3) | Hermitian; `A ⪰ 0` | `d × d`, kernel dim `m ≥ 1` | R10: m ∈ {1,2,3}, d = 5 |
| `Π_K B Π_K` | Hermitian compression | acts on `K`, `m` eigenvalues `μ_k` | R10: computed as `K†BK` on an orthonormal kernel frame |
| `L` (Lemma 3.2) | invertible, unit upper triangular | `d × d` | R11: 20 random invertible L, not just triangular |
| `w_B, w_E, d₁, c₁, C(x), C₂(x)` | real scalars | functions of x only | R5/R5x/R6: formulas in x + exact values at 5 rational x |
| `Ic(ρ)` | real scalar, **nats** | — | R7: `S(Λ(ρ)) − S(Λ^c(ρ))`, my own Kraus assembly + Hermitian eigensolver |

**Dimension bookkeeping that the proof load-bears, and that I confirmed independently:**
`m_B = dim ker Λ(P) = 1` and `m_E = dim ker Λ^c(P) = 2` for **every** isotropic ψ and every x ∈ (0,1)
(R2 symbolically for the canonical ψ; `r5d_edge` for 30 random isotropic ψ at six x — the pair
(1, 2) came out every time). Hence the eigenvalue census in the assembly of Lemma 5.1 —
**3 cluster terms (1 + 2) and 4 regular terms (2 + 2)** — is exactly right, and this is the counting
the note itself flagged as its second-most-distrusted step (§13 item 5(ii)). It is correct.

**Adjoint convention.** The note invokes `K^† = K^T` only for the (real) Kraus operators and says so;
I verified the reality entrywise before using it. `Λ^†` appears nowhere in §3–§9 (the weight operator
`D = M_B − M_E` of R5c scope, which does use `Λ^†`, is confined to §11 corroboration).

---

## 2. Independent derivation FIRST (7c): what I built before reading anything of the author's

`tools/whgap_r5d_indep.py`, 48 gates, **all PASS**, deliberately divergent from the note's route:

- **Kraus/channel (R1, 4 gates).** Own Levi-Civita assembly; identity checked symbolically on a generic
  complex 3×3 `Y` (9 independent complex entries), plus trace preservation and reality.
- **Base point (R2, 6 gates).** `Λ(P) = (1−x/2)P + (x/2)P_{e₃}` symbolically; `spec Λ(P) = {1−x/2, x/2, 0}`;
  and `det(λ·1 − Λ^c(P)) = λ²(λ−(1−x/2))(λ−x/2)` **as a polynomial identity in x**, which is a stronger
  statement than the note's set-of-eigenvalues check because it also fixes the multiplicities
  (kernel dimension exactly 2).
- **B-side exact diagonalization (R3, 3 gates), in MY basis order `(e₃, ψ̄, ψ)`** — not the note's
  `(ψ, ψ̄, e₃)`:
  `U^† Λ(ρ_ε) U = diag(x/2, ε(1−x/2), (1−ε)(1−x/2))` **exactly, symbolically in (x, ε)**. This is the
  commissioned symbolic verification of the B side. It is a *formula*, not a value check, and the
  permutation relative to the note's display is the whole content of the difference.
- **E-side exact structure (R4, 6 gates).** All eight cross-block entries vanish; `Tr A(ε) = 1 − x/2`
  (ε-independent); `det A(ε) = 2x(1−x)ε(1−ε)`; `spec B(ε) = {xε/2, x(1−ε)/2}`; and both blocks match the
  note's (7.3) after substitution. Symbolic in (x, ε).
- **`Π_E` by an independent construction (R5, 9 gates).** I did **not** use the note's Lagrange
  interpolation polynomial (7.5). I computed the **nullspace** of `Λ^c(P_ψ)` in the (S,T) chart,
  orthonormalized it, and verified projector algebra symbolically. Then
  `w_E = Tr[Π_E Λ^c(P_ψ̄)] = 4x(1−x)/(2−x) + x/2` and `w_B = 1 − x/2`, hence
  **`d₁ = w_B − w_E = (1−x)(2−5x)/(2−x)` as an identity in x**, with root set `{2/5, 1}` in `(0,1]`.
  This is the note's §13 attention point (v), executed exactly as it asked, and it agrees.
  By hand, for the record: with `s² = x/2`, `t² = 1−x`, the block-A kernel ray is `(is, t)` and
  `⟨k_A|\overline{A(0)}|k_A⟩/‖k_A‖² = 4s²t²/(s²+t²) = 4x(1−x)/(2−x)`; the block-B kernel ray is `(i,1)`
  and gives `x/2`. Sum = `w_E`.
- **Exact rational route (R5x, 1 gate, c = 5).** The same nullspace construction re-run with exact
  `sqrt(Rational)` arithmetic at `x ∈ {1/5, 79/200, 2/5, 9/20, 3/4}`:
  `d₁ = 4/9, 121/12840, 0, −11/124, −7/20`, each equal to `(1−x)(2−5x)/(2−x)`. This satisfies the
  c ≥ 2 identity-gate requirement (7b) five times over at the **identity** level, on top of the
  fully symbolic gate.
- **Weight operator (R6, 4 gates), reconstructed from the 9 matrix units.** `D_{jk} := f(E_{kj})` with
  `f(φ) = w_B(φ) − w_E(φ)`; in `(e₃, ψ̄, ψ)` this is
  `diag(−x(1−x)/(2−x), (1−x)(2−5x)/(2−x), 0)` **as a formula in x**, `= diag(−99/620, −11/124, 0)` at
  `x = 9/20`. (Corroborates the note's §11 and the node's P9b datum; not needed by the Lemma.)
- **Numerics (R7–R15, 12 gates).** Own `Ic` from the Kraus operators with a Hermitian eigensolver at
  dps 60 (dps 400 for the certificate point); Lemma 5.1's bound stress-tested with **random φ**;
  Prop 3.3 stress-tested at m ∈ {1,2,3}; Lemma 3.2 (Ostrowski) stress-tested on 20 random
  (Hermitian M, invertible L) pairs; the explicit threshold, the certificate point, the crossover
  location, Prop 9.1's remainder bound, and the slope-equals-weight identity.
- **Supplementary uniformity run** `tools/whgap_r5d_edge.py`: **360** residual tests over
  `x ∈ {0.05, 0.2, 0.395, 0.45, 0.7, 0.95}` × 5 **random isotropic ψ** × 3 random φ × 4 ε values
  including `ε = x/8` **exactly** (the tight end of the hypothesis), scored against the note's
  *defining* constant `C(x) = 3[12/(ex) + (5/2)log(5/2)] + 4[1 + log(8/(3x))]` rather than the looser
  simplified one. Worst ratio `|Ic − (w_B−w_E)ε log(1/ε)| / (C(x)ε) = 0.0118`. **No violation.**

---

## 3. The degenerate-perturbation bound, checked line by line (the commission's central task)

### 3.1 Fact 3.1 (Weyl) and (CF)
`(CF)` as displayed — `λ_k(M) = min_{dim W=k} max_{0≠w∈W} ⟨w,Mw⟩/⟨w,w⟩` with eigenvalues **increasing**
— is the correct form of Courant–Fischer for that ordering. Fact 3.1's one-line proof
(`⟨w,Mw⟩ ≤ ⟨w,M′w⟩ + ‖M−M′‖`, max over W then min over W, symmetrize) is valid.

### 3.2 Lemma 3.2 (multiplicative comparison under congruence)
This is Ostrowski's theorem; the note proves it rather than citing it, as required. Every step
verified:
- the substitution `v = L^{-†}w` is a bijection of k-dimensional subspaces (`w = L^†v`); ✔
- `⟨v, Nv⟩ = ⟨w, Mw⟩` and `⟨v,v⟩ = ‖L^{-†}w‖²`; ✔
- `θ(w) = ‖w‖²/‖L^{-†}w‖² ∈ [σ_min², σ_max²]` because the singular values of `L^{-†}` are the
  reciprocals of those of `L`; ✔
- **upper bound**, both sign cases: for `λ_k(M) ≥ 0`, `θR ≤ σ_max²R ≤ σ_max²λ_k(M)` when `R ≥ 0` and
  `θR < 0 ≤ σ_max²λ_k(M)` when `R < 0` — the second case is the one a hurried proof drops, and it is
  present; for `λ_k(M) < 0` all `R(w) ≤ λ_k(M) < 0`, so `θR ≤ σ_min²R ≤ σ_min²λ_k(M)`; ✔
- **lower bound** by applying the upper bound to `(N, L^{-1})` with
  `σ_max(L^{-1}) = 1/σ_min(L)`; ✔
- **four-case assembly**, which the note itself named as its most-distrusted step (§13 item 5(i)):
  `λ_k(M) > 0` ⇒ `λ_k(N) < 0` is impossible (it would force `λ_k(N) ≥ σ_max²λ_k(M) > 0`), so both
  bounds apply with the same sign and `θ_k ∈ [σ_min², σ_max²]`; `λ_k(M) < 0` ⇒ dividing the two bounds
  by a negative number flips the inequalities into the same interval; `λ_k(M) = 0` ⇒ both bounds force
  `λ_k(N) = 0`. **All four cases are correct as written.** The assembly is the step that makes the
  bound multiplicative, and Remark 3.4's explanation of why an additive `‖M − N‖` estimate would be
  fatal (it is `O(ε)` while the cluster eigenvalues are themselves `O(ε)`) is right.
  Independent numerical corroboration: gate R11, 20 random (M, L) pairs, `θ_k` inside
  `[σ_min², σ_max²]` in every case.

### 3.3 Proposition 3.3 (kernel-cluster bound), every constant recomputed
Block form `M = [[εB₁₁, εB₁₂],[εB₂₁, A₂₂+εB₂₂]]` is right (`A` leaves `K` and `K^⊥` invariant because
`K = ker A` and `A` is Hermitian, so there is no `A₁₁` and no `A₁₂`). ✔

**Part (1).** `λ_m(M) ≤ max_{unit w∈K} ε⟨w,Bw⟩ ≤ εb` by `(CF)` with `W = K`; `λ₁(M) ≥ −εb` and
`λ_{m+1}(M) ≥ g − εb ≥ 3g/4` by Fact 3.1 with `εb ≤ g/4`. Ordering claim correct since
`εb ≤ g/4 < 3g/4`. ✔

**Part (2).** I recomputed the Schur block-diagonalization by hand:
with `G := A₂₂+εB₂₂`, `X := −εB₁₂G^{-1}`, `L = [[1,X],[0,1]]`,
`LM` has upper-right block `εB₁₂ + XG = 0` and `LML^†` has lower-left block `εB₂₁ + GX^† = 0`
(using `G^† = G` and `B₁₂^† = B₂₁`), so
`N = LML^† = S ⊕ G` with `S = εB₁₁ − ε²B₁₂G^{-1}B₂₁` — **exactly** as displayed. ✔
- step (a): `‖S − εB₁₁‖ ≤ ε²b²/(g−εb) ≤ (4/3)ε²b²/g`; Weyl gives `|λ_k(S) − εμ_k| ≤ (4/3)ε²b²/g`. ✔
  (`‖B₁₂‖ ≤ ‖B‖ ≤ b` as a compression; `‖G^{-1}‖ ≤ 1/(g−εb) ≤ 4/(3g)`.) ✔
- step (b): `‖S‖ ≤ εb + (4/3)ε²b²/g ≤ (4/3)εb ≤ g/3` (the middle step uses `εb ≤ g/4` — I checked the
  arithmetic: `(4/3)ε²b²/g = (4/3)(εb)(εb)/g ≤ (1/3)εb`), while `λ_min(G) ≥ 3g/4 > g/3`, so the m
  smallest eigenvalues of `N` are exactly those of `S`. ✔
- step (c): `u := (4/3)(εb/g) ≥ ‖E‖`, `u ≤ 1/3`; `σ_max(L)² ≤ 1+2u+u²`, `σ_min(L)² ≥ 1−2u−u² ≥ 0.222 > 0`;
  `η := 2u+u² ≤ (7/3)u = (28/9)(εb/g)`; Lemma 3.2 then gives
  `|λ_k(N) − λ_k(M)| = |θ_k−1||λ_k(M)| ≤ η·εb ≤ (28/9)ε²b²/g`, using `|λ_k(M)| ≤ εb` from part (1). ✔
- total: `(4/3 + 28/9) = 40/9 ≈ 4.444 ≤ 6`. ✔ The displayed `(40/9)` and the relaxed `6` are both
  correct, and Lemma 5.1's `C_pert := 6b²/g = 12/x` is a valid (slightly loose) instantiation.

**Remark 3.5 is correct and is load-bearing.** The proposition never divides by `μ_j − μ_k`; the only
gap used is `g`, the cluster-to-rest distance, bounded below by `x/2` uniformly in φ. The coincidence
`4x(1−x)/(2−x) = x/2 ⟺ 8(1−x) = 2−x ⟺ x = 6/7` is arithmetically right, so standard non-degenerate
perturbation theory really would be inapplicable there and the note's route really is the necessary one.

**Independent numerical corroboration (gate R10).** 24 random instances (`d = 5`, kernel multiplicities
`m ∈ {1,2,3}`, Haar-random kernel frames, random Hermitian `B` normalized to `b = 1`) × up to 3 ε values
with `ε ≤ g/(4b)`: the bound `|λ_k − εμ_k| ≤ (40/9)ε²b²/g` held in **every** case, worst
`dev/bound = 0.0915`; the part-(1) separation held in every case. **Note the coverage direction:** the
note's own gate G6 exercised the bound only at `m = 2` inside the channel problem; I exercised
`m = 1, 2, 3` on generic matrices, i.e. the hypothesis class the proposition actually claims.

---

## 4. Lemmas 4.1, 4.2 and the assembly of Lemma 5.1

**Lemma 4.1.** Algebra re-derived: `h(λ) = λ log(1/ε) − λ log(λ/ε)`, so
`h(λ) − εμ log(1/ε) = r log(1/ε) − ε·(λ/ε)log(λ/ε)`; then `|r log(1/ε)| ≤ Cε²log(1/ε) ≤ (C/e)ε` because
`max_{0<ε≤1} ε log(1/ε) = 1/e`, and `|u log u| ≤ max(1/e, U log U)` on `[0,U]` (correct for both
`U < 1`, where the max is `1/e`-bounded, and `U ≥ 1`). The `λ = 0` branch is handled correctly:
`λ = 0 ⇒ εμ = |r| ≤ Cε²`, and the claim reduces to `εμ log(1/ε) ≤ (C/e)ε`. ✔
**The uniformity claim is the real content and it is sound:** the bound does not involve `μ`, so no case
split at `μ ↓ 0` and no lower bound on `μ` is needed — precisely because the sub-leading term is written
as `ε·(λ/ε)log(λ/ε)` with `u log u` bounded at `u = 0` rather than as `−εμ log μ`. This is the note's
§13 attention point (iv); it is correct, and it is the cleanest idea in the note.

**Lemma 4.2.** `|h′(u)| = |1 + log u| ≤ 1 + log(1/a)` on `[a,1]`; mean value theorem. ✔ (Loose but valid.)

**Assembly of Lemma 5.1 — every ingredient re-checked:**
- affineness in ε of both outputs; ✔
- `(5.2) ‖B‖ ≤ 1`: for PSD trace-one `X, Y`, `λ_max(X−Y) ≤ λ_max(X) ≤ 1` and
  `λ_min(X−Y) ≥ −λ_max(Y) ≥ −1`. On the E side this uses `Tr Λ^c(P) = 1` as a 4×4 matrix, which holds
  (`Σ_a Tr(K_a P K_a^†) = Tr P = 1`) with the padding zeros harmless. This is the note's §13 attention
  point (iii); **it is right**; ✔
- hypothesis `(3.1)` becomes `ε ≤ g/(4b) = x/8`, exactly the stated range; `C_pert = 12/x`; ✔
- **cluster slopes are the kernel weights:** B side `⟨ψ̄|(Λ(φ)−Λ(P))|ψ̄⟩ = w_B` since `Λ(P)|ψ̄⟩ = 0`
  (ψ̄ is a unit vector, so the `1×1` compression *is* that number); E side `Π_E A_E Π_E = 0` so the
  compression is `Π_E Λ^c(φ) Π_E`, and `(5.3) μ^E₁ + μ^E₂ = Tr[Π_EΛ^c(φ)Π_E] = Tr[Π_E²Λ^c(φ)] = w_E`. ✔
  Independently confirmed *numerically as a limit statement*, which is the form the proof needs
  (gate R15): at `ε = 10⁻²⁵`, `λ_min(Λ(ρ_ε))/ε → w_B` and `(λ₁+λ₂)(Λ^c(ρ_ε))/ε → w_E` to 15+ digits,
  for 8 random φ at two x. This is the note's §13 attention point (ii) and it holds.
- `λ/ε ≤ μ + C_pert ε ≤ 1 + (12/x)(x/8) = 5/2 = U`; `κ(5/2) = (5/2)log(5/2) = 2.2907…`; ✔
- **census: 3 cluster + 4 regular** (see §1 above); ✔
- regular terms: `λ_j(ε) ∈ [3x/8, 1]`, `|λ_j(ε) − λ_j(0)| ≤ ε`, `a = 3g/4 = 3x/8`, and
  `Σ_{j>m} h(λ_j(0))` is `S(Λ(P))` resp. `S(Λ^c(P))` because kernel eigenvalues contribute `h(0) = 0`; ✔
- final cancellation uses `S(Λ(P)) = S(Λ^c(P))`, which is (1.3) — verified symbolically by my R2 charpoly
  gate (isospectral up to padding zeros; `Ic(P) = 0` exactly); ✔
- arithmetic of the constant: `3·12/e = 13.245`, `3·(5/2)log(5/2) = 6.872`, `4·1 = 4`,
  `4 log(8/(3x)) ≤ 4 log(3/x)` since `log(8/3) = 0.981 ≤ log 3 = 1.099`; total
  `≤ 13.25/x + 10.872 + 4log(3/x) ≤ 14/x + 11 + 4log(3/x)`. ✔ I verified the domination
  `14/x + 11 + 4log(3/x) ≥ 3[12/(ex) + (5/2)log(5/2)] + 4[1 + log(8/(3x))]` on the grid
  `x = 0.01, …, 0.99` (gate R12).

**Numerical falsification attempt on the Lemma itself.** Beyond the note's own witness-only gate, I
tested the *claimed uniformity in φ and in ψ* — the part most likely to hide an error — with random φ
and random isotropic ψ, at `ε = x/8` exactly, against the *defining* constant: 360 tests, worst ratio
0.0118, no violation. If the census were wrong, or `‖B‖ ≤ 1` were wrong, or a slope were misidentified,
this ensemble would show it as a ratio growing without bound as ε ↓ 0; it does not.

**Corollary 5.3.** Contrapositive is correctly formed: `w_B > w_E` ⇒ pick `ε ≤ x/8` with
`log(1/ε) > C(x)/(w_B−w_E)` ⇒ `Ic(ρ_ε) > 0` ⇒ `Q^{(1)} > 0`. ✔ §10 item 4 correctly refuses the
converse.

---

## 5. §7 (the witness) and §8 (the Theorem)

- `(7.1)`: ψ̄ is isotropic too (`ψ̄ᵗψ̄ = conj(ψᵗψ) = 0`), so (1.1) applies with the same third vector
  `e₃`, giving `Λ(ρ_ε) = (1−ε)(1−x/2)P_ψ + ε(1−x/2)P_ψ̄ + (x/2)P_{e₃}`. Verified symbolically in
  `(x, ε)` in my own basis order (gate R3). **This is the commissioned symbolic B-side check: PASS, at
  formula level.** ✔
- `(7.2) w_B = 1 − x/2`. ✔ (R3)
- `(7.3)`: I re-derived `A_iψ = ψ × e_i` from `(A_i)_{jk} = ε_{ijk}` and `ε_{jki} = ε_{ijk}`, then
  `u₀ = tψ, u₁ = −i(√x/2)e₃, u₂ = (√x/2)e₃, u₃ = isψ`; `ψ ⊥ e₃` forces the `{0,3}⊔{1,2}` block split;
  `Λ^c(P_ψ̄) = conj(Λ^c(P_ψ))` because the Kraus are real, so the off-diagonals acquire the factor
  `(1−2ε)`. Both blocks match the note. ✔ (R4, symbolic in (x, ε), all 8 cross entries zero)
- `(7.4)`: `Tr A = 1−x/2`; `det A = (x/2)(1−x)[1−(1−2ε)²] = 2x(1−x)ε(1−ε)`; `spec B = {(x/2)(1−ε), (x/2)ε}`. ✔
- `(7.6)/(7.7)`: `w_E = 4x(1−x)/(2−x) + x/2 = x(10−9x)/(2(2−x))`;
  `d₁ = [(2−x)² − x(10−9x)]/(2(2−x)) = (4 − 14x + 10x²)/(2(2−x)) = 2(1−x)(2−5x)/(2(2−x)) = (1−x)(2−5x)/(2−x)`.
  I re-did this factorization by hand (`(5x−2)(x−1) = 5x²−7x+2` ✔) and independently by two machine
  routes (symbolic nullspace; exact rational at five x). The note's §13 attention point (vi) hand-check
  values `d₁(1/5) = 4/9`, `d₁(9/20) = −11/124` both reproduce. ✔
- `(7.8)` sign rule: root set of the numerator in `(0,1]` is `{2/5, 1}`, `d₁ > 0 ⟺ x < 2/5`. ✔
- **Theorem 8.1.** `Ic(ρ_ε) ≥ ε[d₁ log(1/ε) − C(x)]`, positive iff `log(1/ε) > C(x)/d₁`, i.e.
  `ε < exp(−C(x)/d₁)`; intersected with `ε ≤ x/8` this is exactly `(8.1)`. `Q^{(1)} ≥ Ic(ρ_ε)` by
  definition and `Q ≥ Q^{(1)}` by LSD (the single external input, cited, standard). ✔
- **Explicit threshold and certificate.** I recomputed `C(1/5) = 91.8322008044`, `C/d₁ = 206.62245…`,
  `ε₁ = 1.84081159672×10⁻⁹⁰`, and at `ε = ε₁/2 = 9.20405798359×10⁻⁹¹`, dps 400, my own Kraus-based
  route gives `Ic = 8.4911578111035956255×10⁻⁸⁹ > 0`, matching the note's displayed
  `8.4911578111e-89`. ✔ (gate R12)
- **§9 Proposition 9.1** (not needed for the Theorem, but it is what makes the sanity table legible).
  I re-derived `c₁(x) = (1−x) − μ_A(1 + log(β/μ_A))` with `β/μ_A = (2−x)²/(8x(1−x))` from the four exact
  eigenvalue families, and checked all four displayed `c₁` values, the `q`-expansion inequalities
  (`√(1−q) ≥ 1 − q/2 − q²` on `[0,1/2]`, `1/(1−u) ≤ 1+2u` for `u ≤ 1/2`, `|log(1+δ)| ≤ 2|δ|` for
  `|δ| ≤ 1/2`), the Lagrange remainders `|R₁| ≤ βε²/(2(1−ε))`, `|R₃| ≤ λ_-²/(2(β−λ_-))`, and the
  absorption of `log(1/ε)` into `log(e/ε)`. All valid (some bounds deliberately loose, e.g. bounding
  `|1+log β| ≤ 1+log 2` where `≤ 1` is true — loose in the safe direction). Numerically:
  `|Ic − two-term| ≤ C₂(x)ε²log(e/ε)` at five x × three ε, worst ratio 0.0154. ✔ (gate R14)

---

## 6. Sanity table reproduced with MY OWN script (commissioned: ≥ 2 of 3 x-values)

Own route: assemble `ρ_ε`, apply Λ and `Λ^c` from the Kraus operators, Hermitian eigensolver,
`−Σλ log λ`, mpmath dps 60. I reproduced **all four x-values and all 21 numerically displayed table
entries** (x ∈ {1/5, 79/200, 2/5, 9/20}; ε ∈ {1e-3, 1e-4, 1e-5, 1e-8, 1e-9, 1e-12, 1e-20}) — three more
than the two required. Worst relative deviation over the 21 entries: **4.5×10⁻¹⁰**, consistent with the
note printing 10 significant digits. Selected rows (mine):

| x | ε | my Ic [nats] | note's Ic | sign |
|---|---|---|---|---|
| 1/5 | 1e-3 | 0.00318570570663 | 0.003185705707 | + |
| 1/5 | 1e-5 | 5.23111451358e-5 | 5.231114514e-5 | + |
| 1/5 | 1e-20 | 2.05816583371e-19 | 2.058165834e-19 | + |
| 79/200 | 1e-5 | −5.96671544866e-7 | −5.966715449e-7 | − |
| 79/200 | 1e-8 | +5.41199768416e-11 | +5.411997684e-11 | + |
| 2/5 | 1e-20 | −1.72609243471e-21 | −1.726092435e-21 | − |
| 9/20 | 1e-3 | −8.24242156515e-4 | −8.242421565e-4 | − |
| 9/20 | 1e-20 | −4.29747605982e-20 | −4.297476060e-20 | − |

**The note's honest reading of the sign pattern is correct and I confirm the correction it makes to the
commission's expectation.** At `x = 0.395` the sign is **negative** at all three commissioned
`ε ∈ {1e-3,1e-4,1e-5}` and turns positive only below `≈1.8×10⁻⁸`; my independently computed crossover
`ε* = exp(c₁/d₁) = 1.775878×10⁻⁸` brackets my own observed flip between `1e-5` (−) and `1e-8` (+)
(gate R13). At `x = 2/5` the sign is negative down to `ε = 1e-20`, so the witness family really is
unhelpful at the endpoint, as §10 item 2 states. The residual-quality claim also reproduces
(at `x = 1/5`, `|Ic − two-term|/ε = 1.357e-3, 1.851e-4, 2.346e-5, …`).

**Value-vs-formula (7f), per claim:**

| claim | what I verified | how |
|---|---|---|
| Kraus ⇒ Λ_x, TP | **FORMULA** (identity in x and in the 9 entries of Y) | symbolic |
| (1.1), spec Λ(P), spec Λ^c(P) with multiplicity | **FORMULA** in x | symbolic (charpoly identity) |
| (7.1) B-side exact diagonalization | **FORMULA** in (x, ε) | symbolic, own basis order |
| (7.3), (7.4) E-side blocks, Tr, det, spec B | **FORMULA** in (x, ε) | symbolic |
| Π_E projector algebra | **FORMULA** in x | symbolic, own nullspace construction |
| (7.6) w_E, (7.7) d₁, (7.8) sign rule | **FORMULA** in x, **plus VALUE at c = 5 rational x** | symbolic + exact rational |
| §11 weight operator D diagonal | **FORMULA** in x, plus VALUE at x = 9/20 | symbolic, own functional reconstruction |
| Lemma 3.2 (Ostrowski) | **PROOF** re-derived by hand; VALUES at 20 random (M,L) | hand + numeric |
| Prop 3.3 parts (1),(2), all constants | **PROOF** re-derived by hand (incl. the exact Schur identity); VALUES at m ∈ {1,2,3}, 24 instances | hand + numeric |
| Lemma 4.1, 4.2 | **PROOF** re-derived by hand | hand |
| Lemma 5.1 (assembly, census, constant) | **PROOF** re-derived by hand; VALUES at 4 x × random φ, and 360 tests at 6 x × random isotropic ψ × random φ × ε incl. ε = x/8 | hand + numeric |
| Theorem 8.1, ε₁(x), certificate point | **PROOF** re-derived; VALUE at x = 1/5, ε = ε₁/2, dps 400 | hand + numeric |
| Prop 9.1 (c₁, C₂, ε₂) | **PROOF** re-derived by hand; VALUES at 5 x × 3 ε | hand + numeric |
| sanity table | **VALUES** at 4 x × 7 ε (21 displayed entries) | own numeric route |

**What remains unverified by me.** (a) The Lloyd–Shor–Devetak inequality `Q ≥ Q^{(1)}` is granted as
literature, as is Courant–Fischer. (b) `max_φ (w_B − w_E) = max(d₁, 0)` — the *optimality* of the
witness — is **not** in scope here and is not claimed by the note; it is the R5c-scope statement.
(c) Nothing about `[2/5, 1/2)`, about non-isotropic strata (`τ ≠ 0`), about the balanced layer (N1′-b),
or about `n ≥ 2` was checked, and the note claims none of it.

---

## 7. Dependence audit of the Theorem (7d — the commissioned question)

The commission asked whether the Theorem uses *only* the closed-form **value** of `w_B − w_E` from
R5c scope, cleanly cited. **The answer is stronger than the question presumes: the Theorem uses
nothing from R5c at all.**

- `d₁ = (1−x)(2−5x)/(2−x)` is derived inside the note at §7.3 from the §1 Kraus definitions and (1.3),
  via `Π_E` built as a Lagrange polynomial in `Λ^c(P_ψ)`. That derivation is self-contained. I
  reproduced the same formula by two independent routes (own nullspace projector; own functional
  reconstruction on the matrix units) and at five rational x, and by hand. So the one numerical input
  the Theorem needs is established **within this review**, independently of R5c.
- §7.3's second bullet is in fact a *second, human-readable derivation* of `w_E`: the exact block
  spectra of (7.4) give cluster slopes `μ_A = 4x(1−x)/(2−x)` and `x/2`, and `(5.3)` (proved in §5)
  says the E-side cluster slopes sum to `w_E`. I verified this route separately (R15 numerically,
  R4/R5 symbolically). Hence (7.6) does not rest on the symbolic gate alone.
- **Remark 5.2 removes the orbit-transitivity dependency**: Lemma 5.1 is proved pointwise on the
  isotropic stratum using only (1.1)–(1.3), which hold for *every* isotropic ψ; no transport from a
  representative is needed. I confirmed the pointwise claim empirically for 30 random isotropic ψ
  (kernel dimensions `(1,2)` every time; residual bound satisfied every time). This is a real
  simplification relative to the node's N1″ framing.
- §6, §10 item 3(a) and §11 mention the R5c-scope weight operator explicitly as an **input under
  review / corroboration only**, and state that nothing in §5, §7, §8 depends on it. I checked every
  cross-reference in §5, §7, §8 and the dependence audit in §8 is accurate: the ingredients are §1,
  (1.1)–(1.3), §3, §4, §7.3 and LSD. **No hidden R5c dependency, no hidden P6/P6b/P9/P9b dependency,
  no hidden P2/P3/P4 dependency** (P2/P4 and P3 appear only in the §10 discussion, as the note says).

For the record (read only after my own gates completed, and not relied on for any step above): the R5c
review on disk (`artifacts/whgap_r5c_review_20260729.md` §9) returned **(A) LICENSE, MAJOR: none**, and
explicitly scoped itself out of the expansion lemma, the leading-coefficient identification, `x_D = 2/5`
and `Q > 0` on `(0,2/5)` — i.e. exactly the complement of what I review here, with no overlap and no
circularity.

---

## 8. Findings

**MAJOR: none.** I attempted to break the Lemma at its four self-declared weak points (Lemma 3.2's
four-case assembly, the cluster/regular census with the `Σ`-slopes identity, `‖B‖ ≤ 1`, and Lemma
4.1's uniformity in μ) and at two points the note did not flag (the `ε = x/8` boundary, and the claimed
uniformity over the isotropic stratum rather than the canonical representative). All six held.

**Minors (none affects the licensed claims):**

- **m1 — `C(x)` denotes two different functions.** Lemma 5.1 *defines*
  `C(x) := 3[12/(ex) + (5/2)log(5/2)] + 4[1 + log(8/(3x))]`, then displays the looser
  `14/x + 11 + 4log(3/x)`; §8, §12.2 (G8) and the threshold `ε₁(x)` all use the *looser* one under the
  same name. The mathematics is unaffected (a larger constant only shrinks `ε₁`, and I verified the
  domination on `x ∈ (0.01, 0.99)`), but any paper version should give the two constants different
  names, or state `C(x)` once and for all as the simplified bound.
- **m2 — §3's preamble over-claims self-containment.** "Nothing in this section is quoted from the
  literature except the Courant–Fischer variational principle, which is proved in one line where used"
  — CF is *used*, not proved, in Fact 3.1 and Lemma 3.2. Likewise §1.1 calls LSD "the only external
  input used"; CF is a second granted input. Both are entirely standard; only the self-containment
  wording needs a one-line fix ("we grant Courant–Fischer").
- **m3 — Remark 5.2's last sentence should be scoped.** "If φ is required only to be PSD with
  `Tr φ ≤ 1` the same proof applies verbatim" is true of the *entropy expansion*, but then `ρ_ε` is
  subnormalized and `Ic(ρ_ε)` is no longer a coherent information, so Corollary 5.3 and Theorem 8.1 do
  not extend. Worth one clause.
- **m4 — the primary derivation of (7.6) is a machine gate; the human-readable one is presented as a
  cross-check.** §7.3 obtains `w_E` by "evaluating (2.1) with (7.5) … symbolically in x (gate G4)", and
  relegates the exact-block-slope route to a bullet. The bullet route (exact `λ_-` slope from (7.4)
  plus `(5.3)`) is a complete written proof and should be promoted to primary, with the sympy gate as
  confirmation — otherwise a reader has to trust a script for the one number the Theorem needs. (I
  verified both, and also give the explicit kernel rays `k_A ∝ (is, t)`, `k_B ∝ (i, 1)` and the
  resulting `4s²t²/(s²+t²) + x/2` by hand in §2 above, which closes the gap for any future reader.)
- **m5 — §12.1's slope-decay wording is slightly optimistic.** "The residual … divided by ε falls by a
  factor ≈ 10 for each factor 10 in ε" — the observed consecutive-decade factors are `7.3, 7.9, …`
  (the `log(1/ε)` factor), not `≈10`. The conclusion drawn (monotone decrease consistent with
  `O(ε²log(1/ε))`) is correct and I reproduce the numbers; only the phrase overstates.
- **m6 — gate-coverage gap in the note's own verification (closed by this review).** The note's G8 tests
  the Lemma 5.1 remainder bound only for `φ = P_ψ̄` at the canonical ψ, while the Lemma claims
  uniformity in **both** φ and ψ; its G6 exercises Prop 3.3 only at kernel multiplicity `m = 2` inside
  the channel problem. I closed both: Prop 3.3 at `m ∈ {1,2,3}` on generic matrices (R10), and the
  Lemma 5.1 bound over 6 x × 5 random isotropic ψ × 3 random φ × 4 ε including `ε = x/8` exactly
  (`tools/whgap_r5d_edge.py`, worst ratio 0.0118). No violation. This is a completeness note about the
  note's gate set, not a defect in its proof.
- **m7 — bookkeeping, for the decision layer only.** The note's provenance file is
  `SHA256SUMS_n1p.txt`, not the commission's `SHA256SUMS.txt` (correctly, to avoid overwriting R5a's
  cited file — `RESEARCH_STRUCTURE_PROTOCOL.md` §7). It is LF-clean and `sha256sum -c` passes on all
  four listed files, including the note itself. Mine is `SHA256SUMS_r5d.txt`, same convention. The
  commission's single-writer deviation means **this report and both my scripts/logs are currently
  orphaned from the node**; the atomic-update obligation (rule 8c) sits with the decision layer.
- **m8 — a failure-mode-1 variant worth adding to the standing list.** In sympy, supplying
  `S**4 → (x/2)**2` as a substitution key makes `S**2` match as `(S**4)**(1/2)` and silently yields
  `Abs(x−1)`, breaking otherwise-correct symbolic gates. The safe pattern is to substitute only the
  lowest even powers (and the odd product `S*T`) and then **assert that no free radical symbol
  survives**. I hit this in my own script; recorded so the next agent does not.

---

## 9. Verdict (7g — exactly one licensing statement from the R5d menu)

**(A) LICENSE.**

*The expansion Lemma is PROVED.* Lemma 5.1 — for every `x ∈ (0,1)`, every isotropic `ψ`, every state
`φ`, and every `0 < ε ≤ x/8`,
`| Ic((1−ε)P_ψ + εφ) − (w_B − w_E)·ε·log(1/ε) | ≤ C(x)·ε` with `C(x)` explicit and independent of `φ`
and `ψ` — together with its self-contained ingredients (Fact 3.1, Lemma 3.2 = Ostrowski with a correct
four-case assembly, Proposition 3.3 with the exact Schur block-diagonalization and the constant
`40/9`, Lemmas 4.1 and 4.2), and with Corollary 5.3 (the (N1′-a) necessity layer), is correct as
written. Every inequality and every remainder constant was re-derived by hand in this review, the
perturbation bound line by line, and the B-side exact diagonalization was verified symbolically in
`(x, ε)` in an independent basis order.

*The Theorem `Q(Λ_x) ≥ Q^{(1)}(Λ_x) > 0` for all `x ∈ (0, 2/5)` is PROVED — and it is
**UNCONDITIONAL**, not conditional on R5c.* The only quantity it imports, `w_B − w_E = d₁(x) =
(1−x)(2−5x)/(2−x)`, is derived inside the note from the frozen Kraus definitions and re-derived here by
three independent routes (own nullspace projector, own functional reconstruction on the matrix units,
exact rational arithmetic at five distinct x), plus by hand. The dependence audit in the note's §8 is
accurate: no R5c, P6, P6b, P9, P9b, P2, P3 or P4 result is load-bearing; §6, §10.3(a) and §11 cite the
R5c-scope material cleanly as corroboration only. (For completeness: the R5c review on disk returned
LICENSE with no MAJOR, so the conditional and unconditional readings of the menu coincide anyway.)

**Scope of this license, stated explicitly.** It covers Lemma 5.1, Corollary 5.3, Proposition 3.3 and
its supporting lemmas, the exact witness computations of §7 (including the B-side diagonalization,
the E-side block spectra, `w_B`, `w_E`, `d₁` and the sign rule `d₁ > 0 ⟺ x < 2/5`), Theorem 8.1 with
its explicit threshold `ε₁(x)`, Proposition 9.1, and the numerical package of §12 (which I reproduced
independently). It does **NOT** cover, and the note does not claim: (i) optimality of the witness,
i.e. `max_φ (w_B − w_E) = max(d₁, 0)` — R5c scope; (ii) anything on `[2/5, 1/2)`; (iii) that
`x_D = 2/5` is the onset of `Q > 0` — as the note says in §10.3, that is a conjecture about where
*this mechanism* ends and requires four further open items; (iv) the balanced layer (N1′-b); (v) any
`n ≥ 2` layer. The undetermined strip after this note is exactly `[2/5, 1/2)` given the frozen
P2/P4 theorem.

**Recommended follow-ups for the decision layer** (mine to recommend, not to write): perform the
rule-8c atomic update linking this report, the note, and both parties' scripts/logs from
`WHGAP.no-ascent-hierarchy`; register the new node the note asks for in its §13 item 4 (*"the
isotropic first-order mechanism terminates exactly at `x_D = 2/5`"*, OPEN, with the four named
obligations) so that `2/5` is never read off this note as an onset; and note that Theorem 8.1 strictly
subsumes P3's interval `(0, x₁)` and P3's exact witness at `783/2000 = 0.3915 < 2/5` — which is a
consistency check across two independently reviewed results, and a candidate simplification for the
paper's `Q > 0` section.

---

## 10. Reproduction

```
C:<home>/cpython3119/python.exe tools/whgap_r5d_indep.py     # 48 gates, all PASS, exit 0
C:<home>/cpython3119/python.exe tools/whgap_r5d_edge.py      # 360 residual tests, PASS, exit 0
sha256sum -c artifacts/logs_whgap_r5_20260729/SHA256SUMS_r5d.txt   # all OK
sha256sum -c artifacts/logs_whgap_r5_20260729/SHA256SUMS_n1p.txt   # all OK (reviewed input frozen)
```

Logs: `artifacts/logs_whgap_r5_20260729/r5d_indep.json`, `…/r5d_indep.log`,
`…/r5d_edge.json`, `…/r5d_edge.log`. Hashes:

```
ca41b49de2ea70cab5c84f9c82eb25c13cc5b18546e54dd29528e8ea793bc5ae  tools/whgap_r5d_indep.py
f79afa5afc6ffde7d79e9bb71d8595c7a4e27adf662a785a64f10155b118fc69  tools/whgap_r5d_edge.py
8e5a6bd655fbb15c935514a5d19606a6d959e9a512229bd0dcd74f712d36a3c4  artifacts/logs_whgap_r5_20260729/r5d_indep.json
1d916e50837727b51076f3c70b2e661653eeaba620bcc19c0fce8ba74ae9ee3f  artifacts/logs_whgap_r5_20260729/r5d_indep.log
24f6fa043e85a92a995266923b14dadc1352040c788c88fcfa575ee1c93bcea3  artifacts/logs_whgap_r5_20260729/r5d_edge.json
651bb47e7a4d6e0226eac8640a1cdfc3aeba99bf24b9e6bc192e2de9a89f165a  artifacts/logs_whgap_r5_20260729/r5d_edge.log
5b8ccf95953162283ba161da3c64761df313d4dd60d5cd9050f4a52cebe80c56  channel-capacity/werner-holevo-gap/notes/WHGAP_N1PRIME_EXPANSION_LEMMA_20260729.md
```

