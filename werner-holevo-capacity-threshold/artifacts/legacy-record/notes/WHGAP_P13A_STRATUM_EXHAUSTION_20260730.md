# WHGAP P13-A — stratum exhaustion of the first-order mechanism at every anisotropic (τ ≠ 0) pure base point

**Artifact type:** executor authorship (proof note). **Node:** `WHGAP.onset-two-fifths` (P13),
obligations (b) and the first-order part of (c).
**Commission:** [`WHGAP_COMMISSION_P13A_20260730.md`](WHGAP_COMMISSION_P13A_20260730.md), section
**E-P13A**; inherited frozen conventions / standing failure modes / rule-7 embeds are §1–§3 of
[`WHGAP_REVIEW_COMMISSION_R5_20260729.md`](WHGAP_REVIEW_COMMISSION_R5_20260729.md).
**Author:** fresh executor instance, 2026-07-30 (authored none of the prior WHGAP work; given no
desired outcome).
**Interpreter for all computation:** `C:<home>/cpython3119/python.exe`
(sympy 1.13.1, mpmath 1.3.0, numpy 1.26.4).
**Status this note licenses by itself: NOTHING.** Everything below is proposer-authored and is
offered at **CONJECTURED / pending-review** for the paired fresh R6 review (rule 6).

**One-line result.** For every x ∈ (0,1) and every pure ψ with τ(ψ) > 0 the E-side kernel is
one-dimensional and its kernel weight is *exactly* w_E = (x/2)(1 − ⟨ψ|φ|ψ⟩), so
Ic(ρ_ε) = −w_E·ε·log(1/ε) + O(ε) with w_E ≥ 0, and **w_E = 0 only for φ = P_ψ**: the exceptional
set of the commission's G3 is **EMPTY**, G4 is vacuous, and no anisotropic pure base point supports
a first-order ε log(1/ε) ascent at any x.

---

## 0. PRE-ACTION REPORT (mandatory, `research/PRETASK_RELOAD_PROMPT.md`)

Files read from disk, completely, in the prescribed order, before any mathematics:
`research/DAG_PROTOCOL.md` (whole file: §1 data structure, §2 ladder, §3 rules 1–8, §4 READ,
§5 WRITE, §6 session-close);
`research/RESEARCH_STRUCTURE_PROTOCOL.md` (§1–§10, incl. §4 placement, §5 naming, §6 atomic update,
§7 move/archive, §9 closeout, §10 root-level field folders);
`channel-capacity/werner-holevo-gap/README.md`;
`channel-capacity/werner-holevo-gap/notes/WERNER-HOLEVO-GAP_PROOF_DAG.md` (DAG, mermaid, outline,
eight rules inlined);
`channel-capacity/werner-holevo-gap/proof-dag/NODE_INDEX.md`;
the target node `proof-dag/nodes/WHGAP.onset-two-fifths.md` and its parent
`proof-dag/nodes/WHGAP.goal.md` (the node has no children);
then the commission `notes/WHGAP_COMMISSION_P13A_20260730.md`, the inherited §1–§3 of
`notes/WHGAP_REVIEW_COMMISSION_R5_20260729.md`, and the reviewed input
`notes/WHGAP_N1PRIME_EXPANSION_LEMMA_20260729.md` (whole file).

- **Target node and status as read from disk:** `WHGAP.onset-two-fifths` (alias P13), kind LEAF,
  role proof, **status CONJECTURED**, `disposition: null`, parents `["WHGAP.goal"]`, children `[]`,
  `status_source: "registered 2026-07-30 per rule 8b …"`; `Adversarial reviews: None yet.`; the
  node's open obligations are (b) non-isotropic strata, (c) balanced/higher-order layers at and
  above 2/5, (d) every blocklength n ≥ 2. This note addresses **(b)** and the **first-order part of
  (c)** only.
- **My ROLE: executor** (authorship). No reviewer-independence claim is made or implied; I state
  only that I authored none of the prior WHGAP work and was told no desired answer. To keep the
  derivation independent I did **not** open `tools/whgap_p6b_v2_*.py`, `tools/whgap_p9*_*.py`,
  `tools/whgap_r5c_*.py`, `tools/whgap_r5d_*.py`, or `artifacts/whgap_r5{a,b,c,d}_review_*.md`
  **before** deriving §3–§6 from the frozen Kraus operators; the two places where I consulted prior
  material are §7 (the τ→0 crosscheck against the reviewed isotropic values, which is a
  *comparison*, not an input) and §1.4 (the R5c transport statement, re-derived here and only then
  compared to `artifacts/whgap_r5c_review_20260729.md` lines 188–191).
- **Highest status my planned evidence could license per §2:** **NUMERICAL** for the computational
  gates (proposer-writable, with command + log + SHA-256) and **CONJECTURED** for the written
  Theorem. A completion tier (CERTIFIED\*/PROVED) may be written **only** by the decision layer
  after the fresh R6 review completes, is archived on disk and is cited on the node (rules 6, 7).
  **I write no status anywhere and I edited no node file, no `NODE_INDEX.md`, and no DAG doc.**
- **Gates and deliverables of my commission, one line each:**
  **G0** — SO(3)×U(1) normal form ψ_α = cos α e₁ + i sin α e₂, α ∈ [0, π/4], τ = cos 2α, plus the
  covariant transport of the whole first-order problem → §2.
  **G1** — exact 2×2-block identities Tr = 1 − x/2, **det = x(1−x)τ²/2**, complement eigenvalue
  x/2, full-rank criterion, closed spectrum {x/2, μ₊, μ₋} → §3 (re-derived from scratch; the
  commission's pre-derivation is *confirmed* and additionally repaired at the τ = 1 edge, §3.4).
  **G2** — Ic(ρ_ε) = −w_E ε log(1/ε) + O(ε) for τ > 0 with an explicit remainder uniform in φ → §5.
  **G3** — exact characterization of the exceptional set {(x,α) : dim ker K(k) ≥ 2, τ > 0} → §6:
  **it is empty**.
  **G4** — the linear layer on exceptions → §8: **vacuous**, with the trivial direction φ = P_ψ
  handled exactly (Ic ≡ 0 along it, not merely to first order).
  **G5** — sanity script `tools/whgap_p13a_sanity.py` covering (i)–(iv) → §9 (56 gates, all PASS),
  plus one non-commissioned add-on (v) that fixes the theorem's scope.
- **Conflicts between commission text and disk protocols:** **three, all reported rather than
  silently resolved.**
  1. *Single-writer deviation.* The commission forbids me to touch node files, `NODE_INDEX.md` or
     the DAG doc, whereas `DAG_PROTOCOL.md` §5/§6 and `RESEARCH_STRUCTURE_PROTOCOL.md` §6 (atomic
     update, rule 8c) require the executor to append the outcome to the node in the same session.
     The commission states the deviation is commissioned by the decision layer, which will perform
     the atomic node/index/DAG update citing this artifact. I comply and record the obligation:
     **this note, `tools/whgap_p13a_sanity.py` and `artifacts/logs_whgap_p13a_20260730/` are not
     yet linked from `WHGAP.onset-two-fifths`; the decision layer owes that link (rule 8c).**
  2. *`SHA256SUMS` naming.* The commission asks for per-role `SHA256SUMS_*.txt`; I write
     `artifacts/logs_whgap_p13a_20260730/SHA256SUMS_p13a.txt` (LF endings, verified with
     `sha256sum -c`) so a later R6 file cannot overwrite cited provenance (§7).
  3. *A substantive scope conflict in G1's phrasing, reported per the reload instruction.* The
     commission says "in span{ψ, ψ̄} the 2×2 block of Λ_x(P_ψ) has trace = 1 − x/2 and
     det = x(1−x)τ²/2". At **τ = 1** (real ψ up to phase) span{ψ, ψ̄} is **one**-dimensional, so
     there is no 2×2 block and the sentence is ill-typed at that edge. The identities and the
     closed spectrum are nevertheless correct there in the corrected formulation of §3
     (characteristic-polynomial form), which I use. Everything the commission asks for in the
     τ > 0 *interior* is confirmed exactly as stated. This is a typing repair, not a
     mathematical disagreement.
- **Standing failure modes screened (R5 commission §2), item by item.**
  1. sympy `.H` leaving `conjugate(sqrt(1−x))` — **screened and HIT**; see §9.1: the first run
     failed the Hermiticity gate for exactly this reason and the fix was to move the whole E-side
     symbolic layer into a *radical-free rational chart*. Documented append-only.
  2. WindowsApps python inaccessible — the pinned interpreter is used throughout.
  3. Complement convention drift — the padded 4-dimensional Λ^c of §1.2 is used everywhere and
     re-derived in §1.3; the Kraus set is re-verified against Λ_x entrywise (gate `G5i.c0`).
  4. Transpose vs conjugate-transpose — audited in §1.1; `†` is identified with `ᵗ` only for the
     (real) Kraus operators and nowhere else.
  5. `sorted()`/comparison on symbolics — **HIT**: `Matrix.charpoly()` raises
     "cannot determine truth value of Relational" on these entries; replaced by
     `det(λ1 − M)` with Berkowitz (helper `charpoly_expr`).
  6. CRLF in SHA256SUMS — LF enforced and `sha256sum -c` verified.
  7. Eigenvalue bookkeeping at degeneracies / dividing by small gaps — §5 never divides by a
     difference of cluster slopes (the cluster is one-dimensional); the only gap used is
     g = μ₋(x,τ), bounded below explicitly in (3.6).
  8. ε log ε bookkeeping — Lemma 4.1 of the reviewed note is used verbatim with 0 log 0 = 0 and an
     O(ε²log(1/ε)) = o(ε) remainder made quantitative in (5.6).
  9. Anchoring — §3–§6 were derived and gated before any comparison with prior artifacts; the two
     comparisons made are flagged as comparisons in §1.4 and §7.

---

## 1. Conventions, types, and the two reviewed inputs

### 1.1 Objects and types (type audit, rule 7a)

| symbol | type | dimensions |
|---|---|---|
| `Y` | complex matrix (channel argument) | 3 × 3 |
| `Λ_x` | linear map, CPTP | M₃(ℂ) → M₃(ℂ) |
| `K_0,…,K_3` | Kraus operators, **real entries** | 3 × 3 each |
| `Λ_x^c` | linear map, CPTP (padded complement) | M₃(ℂ) → M₄(ℂ) |
| `ψ, ψ̄, e_j` | unit vectors (kets) | ℂ³ |
| `P = P_ψ = \|ψ⟩⟨ψ\|`, `φ`, `ρ_ε` | states (PSD, trace 1) | 3 × 3 |
| `Λ(ρ_ε)` | state | 3 × 3 |
| `Λ^c(ρ_ε)` | state | 4 × 4 (rank ≤ 3) |
| `k = k(ψ)` | unit vector spanning ker Λ^c(P_ψ) | ℂ⁴ |
| `K(k) = Σ_a k̄_a K_a` | **single** matrix (not a channel) | 3 × 3 |
| `[w]_×` | cross-product matrix, `[w]_× v = w × v` | 3 × 3, complex-bilinear in `w` |
| `μ_±, x/2, g, w_E, C(x,τ), τ, α` | real scalars | — |
| `V = 1 ⊕ det(O)·O` | real orthogonal environment transport | 4 × 4 |
| `Ic(ρ)` | real scalar (**nats** throughout) | — |

Frozen definitions (R5 commission §1), reproduced in content:

- **Channel.** Λ_x(Y) = (1−x)·Y + (x/2)·(Tr(Y)·𝟙 − Yᵗ) on qutrits, x ∈ (0,1).
- **Kraus.** K₀ = t·𝟙 with t := √(1−x), and K_i = σ·A_i for i = 1,2,3 with σ := √(x/2),
  (A_i)_{jk} = ε_{ijk}. *Index note:* the commission labels the antisymmetric generators
  μ = 0,1,2; I label them i = 1,2,3 so that matrix indices and Kraus indices share the 1-based
  convention. This is a permutation of the environment index, which conjugates Λ^c by a permutation
  matrix and therefore changes no spectrum, no entropy and no kernel dimension.
- **Complement (padded, 4-dimensional).** Λ_x^c(Y)_{ab} = Tr(K_a Y K_b^†), a,b ∈ {0,1,2,3}. The
  K_a are real, so K_a^† = K_aᵗ; this is the **only** place `†` = `ᵗ` is used (failure mode 4).
- **Isotropy.** τ(ψ) := |ψᵗψ| ∈ [0,1] for unit ψ (Cauchy–Schwarz); the isotropic stratum is τ = 0;
  this note works on the **anisotropic strata τ > 0**.
- **Coherent information.** Ic(ρ) = S(Λ(ρ)) − S(Λ^c(ρ)), S(σ) = −Tr σ log σ, and
  Q(Λ) ≥ Q^{(1)}(Λ) = max_ρ Ic(ρ) (Lloyd–Shor–Devetak; used nowhere in this note's proofs — this
  note produces *no* positivity claim).

Verified independently in gate `G5i.c0`/`G5i.c1`: Σ_a K_a Y K_a^† = Λ_x(Y) as an identity in the
nine entries of Y, and Σ_a K_a^† K_a = 𝟙.

Two elementary facts about A_i used constantly:

> **(1.1)** A_i v = v × e_i for every v ∈ ℂ³, hence **Σ_i w_i A_i = −[w]_×** for every w ∈ ℂ³.

(Direct from (A_i)_{jk} = ε_{ijk}; verified symbolically in `G5i.f2`.)

### 1.2 Reviewed inputs used, and the exact scope in which they are used (rule 7d)

1. **The perturbation/entropy machinery of
   [`WHGAP_N1PRIME_EXPANSION_LEMMA_20260729.md`](WHGAP_N1PRIME_EXPANSION_LEMMA_20260729.md) §3–§4**,
   reviewed under R5d with LICENSE A: **Fact 3.1** (Weyl), **Lemma 3.2** (multiplicative eigenvalue
   comparison under congruence), **Proposition 3.3** (kernel-cluster bound), **Lemma 4.1** (uniform
   ε log(1/ε) cluster-term expansion), **Lemma 4.2** (regular-term stability). These are used as
   black boxes with their stated hypotheses, at exactly the granularity their review covered: they
   are *parameter-free statements about Hermitian matrices* (A ⪰ 0 with kernel of dimension m and
   spectral gap g, a bounded Hermitian perturbation B), and I instantiate them at m = **1** on the
   E side and at m = 0 (no cluster at all, only Lemma 4.2 + Weyl) on the B side. The reviewed note
   instantiated the same propositions at m_B = 1, m_E = 2; the propositions themselves are stated
   and proved for arbitrary m ≥ 1, so my m = 1 instantiation is inside the reviewed scope. Every
   remainder constant is recomputed here from scratch for my instantiation — I do **not** reuse the
   reviewed note's C(x).
2. **The R5c-reviewed isotropic closed form** d₁(x) = (1−x)(2−5x)/(2−x), the isotropic slope
   decomposition w_E^{iso} = μ_A + x/2 with μ_A = 4x(1−x)/(2−x), and the SO(3) orbit transport
   V = 1 ⊕ det(O)·O. Used **only** in §1.4 (transport, which I re-derive independently) and §7
   (the τ → 0 crosscheck, a comparison), and in §10 when combining with the isotropic layer to
   state the corollary. **No step of §2–§8 depends on it.**

Frozen results P2/P4 (Q = P = 0 on [1/2,1)) and P3 + R5d (Q > 0 on (0, 2/5)) are used only in the
discussion of §10.

### 1.3 Λ^c is the complementary channel, and Ic vanishes at every pure state

Let V_iso : ℂ³ → ℂ³ ⊗ ℂ⁴, V_iso|v⟩ = Σ_a (K_a|v⟩) ⊗ |a⟩. Σ_a K_a^†K_a = 𝟙 makes V_iso an isometry,
Λ(ρ) = Tr_E(V_iso ρ V_iso^†), and
(Tr_B V_iso ρ V_iso^†)_{ab} = Σ_j (K_a ρ K_b^†)_{jj} = Λ^c(ρ)_{ab}. Hence:

> **(1.2)** For every **pure** input P, Λ(P) and Λ^c(P) are the two marginals of the pure state
> V_iso|ψ⟩; by the Schmidt decomposition they have the **same nonzero spectrum**, so
> **rank Λ^c(P) = rank Λ(P)** and **Ic(P) = 0 exactly** (0 log 0 = 0 for the padding zeros).

Gate `G5i.c5` re-verifies (1.2) at the level of characteristic polynomials, symbolically over the
whole parameter space.

### 1.4 The covariant transport of the entire first-order problem (G0, second half)

**Lemma 1.1 (transport).** For every O ∈ O(3):
Λ_x(O Y Oᵗ) = O Λ_x(Y) Oᵗ, and Λ_x^c(O Y Oᵗ) = V Λ_x^c(Y) Vᵗ with the **real orthogonal**
V := 1 ⊕ det(O)·O acting on the environment index.

*Proof.* Λ_x has real coefficients and both Y ↦ Tr(Y)𝟙 and Y ↦ Yᵗ are O(3)-equivariant
((OYOᵗ)ᵗ = OYᵗOᵗ), giving the first identity. For the second, from
ε_{abc}O_{ia}O_{jb}O_{kc} = det(O)·ε_{ijk} one gets, contracting with O_{νμ} and using
orthogonality,

> **(1.3)** Oᵗ A_i O = det(O)·Σ_j O_{ij} A_j.

Put K'_a := Oᵗ K_a O. Then K'_0 = K_0 and K'_i = det(O) Σ_j O_{ij} K_j, i.e. K'_a = Σ_b V_{ab} K_b
with V = 1 ⊕ det(O)·O real orthogonal. Since K_a O = O K'_a,
Λ^c(OYOᵗ)_{ab} = Tr(K_a O Y Oᵗ K_b^ᵗ) = Tr(K'_a Y K'_b{}^ᵗ) = (V Λ^c(Y) Vᵗ)_{ab}. ∎

**Corollary 1.2 (the whole first-order problem is transported).** For O ∈ O(3), a global phase
e^{iθ}, a pure ψ and a state φ:
τ(e^{iθ}Oψ) = τ(ψ);  spec Λ(P_{Oψ}) = spec Λ(P_ψ);  spec Λ^c(P_{Oψ}) = spec Λ^c(P_ψ);
ker Λ^c(P_{Oψ}) = V·ker Λ^c(P_ψ);  and, with ρ_ε(ψ,φ) := (1−ε)P_ψ + εφ,

> **(1.4)** Ic(ρ_ε(Oψ, OφOᵗ)) = Ic(ρ_ε(ψ, φ)) for every ε,
> and w_E(Oψ, OφOᵗ) = w_E(ψ, φ) (with w_E defined in (4.1)).

*Proof.* τ(e^{iθ}Oψ) = |ψᵗOᵗOψ| = |ψᵗψ|. P_{Oψ} = O P_ψ Oᵗ (O real). Then Λ(ρ_ε(Oψ,OφOᵗ)) =
O Λ(ρ_ε(ψ,φ)) Oᵗ and Λ^c(ρ_ε(Oψ,OφOᵗ)) = V Λ^c(ρ_ε(ψ,φ)) Vᵗ by Lemma 1.1 and linearity; a unitary
(here: orthogonal) conjugation changes no spectrum, hence no entropy, hence not Ic. Global phases
leave P_ψ and hence everything invariant. ∎

Gate `G5i.g1` verifies (1.3) symbolically at four test O, two with det = +1 and two with
det = −1 (the reflections are the cases where the det factor is load-bearing). This re-derivation
agrees with the R5c review's transport statement
(`artifacts/whgap_r5c_review_20260729.md` lines 188–191); I derived (1.3) before reading it and
report the agreement as a *coincidence of independent derivations*, as rule 7c requires.

---

## 2. G0 — the SO(3) × U(1) normal form

**Proposition 2.1 (normal form).** Let ψ ∈ ℂ³ be a unit vector. Then there exist θ ∈ ℝ, O ∈ SO(3)
and α ∈ [0, π/4] with

> **(2.1)** e^{iθ} O ψ = ψ_α := cos α · e₁ + i sin α · e₂,   and   τ(ψ) = cos 2α.

Conversely τ(ψ_α) = cos 2α, so α ↦ τ is a bijection [0, π/4] → [0,1], and **τ(ψ) > 0 ⟺ α < π/4**.

*Proof.* Write ψ = a + i b with a, b ∈ ℝ³. Then ψᵗψ = (a·a − b·b) + 2i (a·b), and a global phase
acts on it by ψᵗψ ↦ e^{2iθ}ψᵗψ. Choose θ so that e^{2iθ}ψᵗψ ≥ 0 is real and nonnegative (possible:
any complex number is e^{-2iθ}·|·| for a suitable θ); after this rotation, still writing ψ = a + ib,

> **(2.2)** a·b = 0  and  a·a − b·b = τ ≥ 0,  while  a·a + b·b = ‖ψ‖² = 1,

so a·a = (1+τ)/2 and b·b = (1−τ)/2. (τ ≤ 1 by (2.2), consistent with Cauchy–Schwarz.)
*Case τ < 1.* Then a ≠ 0 ≠ b and a ⊥ b, so (â, b̂, â × b̂) with â = a/‖a‖ is a **right-handed**
orthonormal basis of ℝ³; the real matrix O sending it to (e₁, e₂, e₃) has det O = +1, i.e.
O ∈ SO(3), and O a = ‖a‖ e₁, O b = ‖b‖ e₂. Setting cos α := ‖a‖ = √((1+τ)/2) and
sin α := ‖b‖ = √((1−τ)/2) — both ≥ 0, and cos α ≥ sin α ⟺ τ ≥ 0, so α ∈ [0, π/4] — gives
Oψ = ψ_α with cos 2α = cos²α − sin²α = τ.
*Case τ = 1.* Then b = 0 and ψ = a is a real unit vector; any O ∈ SO(3) with O a = e₁ works, and
α = 0, τ = cos 0 = 1. ∎

Gates `G5i.a3`, `G5i.a4` verify τ(ψ_α) = cos 2α symbolically (via the rational parameterization
u = tan α, τ = (1−u²)/(1+u²)).

**By Corollary 1.2 it therefore suffices, for every statement about spectra, kernels, w_E and
Ic(ρ_ε), to work at ψ = ψ_α.** Two independent uses are made of this below, and it is worth being
explicit about which:

* §3 and §6 are in fact proved **for arbitrary ψ, without invoking the normal form** — the normal
  form is then used only to *express the answer in the commissioned (x, α) coordinates* and to run
  the (x, α) grid scan of G5(iv). (Gates `G5i.f1`–`G5i.f8` are the general-ψ versions.)
* §5's remainder bound is proved pointwise on the stratum (it uses only the spectrum of Λ(P_ψ),
  which §3 gives for arbitrary ψ), so it too needs no transport. **Consequently nothing in this
  note load-bears the orbit-transitivity statement**; Lemma 1.1 is included because the commission
  asks for the transport to be stated, and because it is what makes the (x, α) parameterization a
  complete description rather than a slice.

---

## 3. G1 — the exact spectrum of Λ_x(P_ψ) on every stratum

Throughout, for a unit ψ set P := P_ψ = |ψ⟩⟨ψ| and Q := P^ᵗ. The first observation is that Q is
again a rank-one projector:

> **(3.1)** (Pᵗ)_{jk} = ψ_k ψ̄_j = (P_ψ̄)_{jk}, i.e. **Pᵗ = P_ψ̄**, and
> ⟨ψ|ψ̄⟩ = Σ_j ψ̄_j ψ̄_j = conj(ψᵗψ), so **|⟨ψ|ψ̄⟩| = τ** and **Tr(P Q) = τ²**.

(Gate `G5i.a6`, `G5i.f8`.) Since Tr P = 1,

> **(3.2)** Λ_x(P) = (1−x)P + (x/2)(𝟙 − Pᵗ) = **(x/2)·𝟙 + (1−x)·P − (x/2)·Q**.

### 3.1 The 2 × 2 block (the commissioned route)

Let S := span{ψ, ψ̄}. Both P and Q map ℂ³ into S and annihilate S^⊥, and 𝟙 preserves S and S^⊥, so
**Λ_x(P) is block diagonal with respect to S ⊕ S^⊥** and acts as the scalar x/2 on S^⊥. In the
normal form, ψ_α and ψ̄_α both lie in W := span{e₁, e₂} and S = W whenever 0 < τ < 1; gate
`G5i.b1`/`G5i.b2` verifies the block structure and Λ(P)_{33} = x/2 symbolically. Assume
0 < τ < 1 for this subsection, so dim S = 2.

**Lemma 3.1 (block trace and determinant).** With a := x/2, p := 1−x, q := −x/2, on the
two-dimensional space S,

> **(3.3)** Tr(Λ_x(P)|_S) = 2a + p + q = **1 − x/2**,
> **(3.4)** det(Λ_x(P)|_S) = a² + a(p+q) + pq(1 − τ²) = **x(1−x)τ²/2**.

*Proof.* M := Λ_x(P)|_S = a·𝟙_S + p·P + q·Q with P, Q rank-one projectors on the 2-dimensional S.
The trace is immediate: Tr𝟙_S = 2, Tr P = Tr Q = 1. For the determinant use
det M = ((Tr M)² − Tr(M²))/2 (valid on a 2-dimensional space). Expanding
M² = a²𝟙 + p²P + q²Q + 2apP + 2aqQ + pq(PQ + QP) and using P² = P, Q² = Q,
Tr(PQ) = Tr(QP) = τ² (by (3.1)),

  Tr(M²) = 2a² + p² + q² + 2a(p+q) + 2pq τ²,  (Tr M)² = 4a² + p² + q² + 2pq + 4a(p+q),

so det M = (2a² + 2a(p+q) + 2pq(1−τ²))/2 = a² + a(p+q) + pq(1−τ²). Substituting a = x/2, p = 1−x,
q = −x/2: a² + a(p+q) = (x/2)(x/2 + 1 − 3x/2) = x(1−x)/2 and pq = −x(1−x)/2, hence
det M = (x(1−x)/2)·(1 − (1−τ²)) = x(1−x)τ²/2. ∎

*Sanity of the algebra.* Dropping the middle term a(p+q) (an easy slip) would give
x²/4 − x(1−x)/2, which at τ = 0 is nonzero and therefore contradicts the reviewed isotropic
spectrum {1−x/2, x/2, 0}. The τ = 0 specialization of (3.4) is 0, which is the required
consistency check with the reviewed input, and the τ = 1 specialization is x(1−x)/2, matching the
directly computable spectrum {1−x, x/2, x/2} of Λ_x(P_{e₁}).

### 3.2 The closed spectrum (valid on all strata, including τ = 1)

**Proposition 3.2 (exact spectrum).** For every x ∈ (0,1) and every unit ψ ∈ ℂ³, with
T := 1 − x/2 and D := x(1−x)τ(ψ)²/2,

> **(3.5)** det(λ𝟙 − Λ_x(P_ψ)) = (λ − x/2)·(λ² − T λ + D),
> hence **spec Λ_x(P_ψ) = { x/2, μ₊, μ₋ }**, μ_± = ½( T ± √(T² − 4D) ),
> and T² − 4D = (1−x/2)² − 2x(1−x)τ² ≥ (1 − 3x/2)² ≥ 0, so μ_± are real.
> Moreover **μ₋ ≤ x/2 ≤ μ₊**, μ₊ ≥ T/2 > 0, and
> **Λ_x(P_ψ) is full rank ⟺ D > 0 ⟺ τ(ψ) > 0.**

*Proof.* By (3.2), Λ_x(P) = a𝟙 + pP + qQ with the data of Lemma 3.1. On S^⊥ (dimension 3 − dim S)
it acts as a = x/2; on S it acts as the matrix M of Lemma 3.1. If dim S = 2 the characteristic
polynomial is (λ − a)·(λ² − Tr M·λ + det M), which is (3.5) by (3.3)–(3.4). If dim S = 1 (i.e.
τ = 1, ψ = e^{iθ}·real, P = Q) then Λ_x(P) = (1−x)P + (x/2)(𝟙 − P) has spectrum {1−x, x/2, x/2},
while at τ = 1 the quadratic λ² − Tλ + D = λ² − (1−x/2)λ + x(1−x)/2 factors as
(λ − (1−x))(λ − x/2) — so (3.5) holds there too. (Both branches, and the discriminant identity at
τ = 1, are gated symbolically: `G5i.b5`, `G5i.b7`, and the general-ψ version `G5i.f7`, which
verifies (3.5) for an **arbitrary** unit ψ with no normal form and no case split.)

For the discriminant: τ² ≤ 1 gives T² − 4D ≥ (1−x/2)² − 2x(1−x) = 1 − 3x + 9x²/4 = (1 − 3x/2)².
For the ordering, evaluate the quadratic at λ = x/2:

  (x/2)² − T(x/2) + D = (x/2)[x/2 − 1 + x/2 + (1−x)τ²] = (x/2)(1−x)(τ² − 1) ≤ 0,

so x/2 lies between the two roots (gate `G5i.b8`). Finally μ₊μ₋ = D and μ₊ + μ₋ = T > 0 with
μ₊ ≥ T/2 > 0, so μ₋ = D/μ₊ > 0 ⟺ D > 0 ⟺ τ > 0 (gates `G5i.b9`, `G5i.b10`). ∎

### 3.3 The spectral gap actually used later

Combining Proposition 3.2 with (1.2):

> **(3.6)** For τ > 0 the **smallest nonzero** eigenvalue of both Λ_x(P_ψ) and Λ_x^c(P_ψ) is
> **g = g(x,τ) := μ₋ = D/μ₊ = x(1−x)τ² / (T + √(T² − 4D))**, and since μ₊ ≤ T,
> **g ≥ x(1−x)τ² / (2 − x) > 0.**
> Also **dim ker Λ_x(P_ψ) = 0 and dim ker Λ_x^c(P_ψ) = 1** for τ > 0.

The right-hand form of g in (3.6) is the one manifestly regular at τ = 0 and is what the numerics
use (failure mode 7: no cancellation of large numbers). The kernel dimensions follow from
Proposition 3.2 (three nonzero eigenvalues) and rank Λ^c(P) = rank Λ(P) = 3 with Λ^c(P) of size 4.

### 3.4 What the commission's G1 pre-derivation got right, and the one repair

Confirmed exactly, by my own derivation: trace = 1 − x/2; **det = x(1−x)τ²/2**; the orthogonal
complement carries x/2; full rank ⟺ τ > 0; closed spectrum {x/2, μ₊, μ₋}. The single repair is
the typing one already reported in §0: the phrase "the 2×2 block in span{ψ, ψ̄}" is ill-typed at
τ = 1 where that span is one-dimensional; Proposition 3.2 is stated in characteristic-polynomial
form so that it covers τ ∈ (0,1] uniformly.

---

## 4. The kernel weight w_E, in three equivalent forms

For τ > 0 fix a **unit** k = k(ψ) spanning ker Λ_x^c(P_ψ) (unique up to phase by (3.6)), and define

> **(4.1)** w_E(ψ, φ) := ⟨k| Λ_x^c(φ) |k⟩   for a state φ.

w_E ≥ 0 (a compression of a PSD operator) and w_E ≤ 1. Two rewritings are immediate:

**Lemma 4.1 (Kraus contraction form).** With **K(k) := Σ_a k̄_a K_a** (a single 3 × 3 matrix),

> **(4.2)** w_E(ψ,φ) = Tr[ K(k) φ K(k)^† ] = **Tr[ φ · K(k)^† K(k) ]**,
> and hence, for a state φ, **w_E = 0 ⟺ supp φ ⊆ ker K(k).**

*Proof.* ⟨k|Λ^c(φ)|k⟩ = Σ_{ab} k̄_a k_b Tr(K_a φ K_b^†) = Tr[(Σ_a k̄_a K_a) φ (Σ_b k̄_b K_b)^†],
and Tr[KφK^†] = Tr[φ K^†K] by cyclicity. For the second claim, K^†K ⪰ 0 and φ ⪰ 0, so
Tr[φ K^†K] = 0 ⟺ (K^†K)^{1/2}φ^{1/2} = 0 ⟺ supp φ ⊆ ker(K^†K) = ker K. ∎

(Gate `G5i.e3`.)

**Lemma 4.2 (the kernel vector, in closed form, for arbitrary ψ).** Let ψ be a unit vector with
τ(ψ) > 0. Then

> **(4.3)** **k(ψ) = (0, ψ̄₁, ψ̄₂, ψ̄₃) ∈ ℂ ⊕ ℂ³** is a unit vector spanning ker Λ_x^c(P_ψ);
> in the normal form, k(ψ_α) = (0, cos α, −i sin α, 0).
> In particular the identity-Kraus component of the kernel vector **vanishes**: k₀ = 0.

*Proof.* Write u_a := K_a ψ, so that Λ^c(P)_{ab} = Tr(K_a P K_b^†) = ⟨u_b|u_a⟩ is the Gram matrix
of (u_0,…,u_3) (in this index order). For k ∈ ℂ⁴ put v := Σ_b k̄_b u_b = K(k)ψ. Then
(Λ^c(P) k)_a = Σ_b ⟨u_b|u_a⟩ k_b = ⟨v|u_a⟩. Hence

> **(4.4)** Λ^c(P)k = 0 ⟺ ⟨v|u_a⟩ = 0 for all a ⟹ ⟨v|v⟩ = Σ_b k̄_b⟨v|u_b⟩ = 0 ⟹ **K(k)ψ = 0**,

and conversely K(k)ψ = 0 gives v = 0 hence Λ^c(P)k = 0. So **ker Λ^c(P_ψ) = {k : K(k)ψ = 0}**.
Now let m := k̄, i.e. m_a = k̄_a, and use (1.1):

  K(k)ψ = Σ_a m_a K_a ψ = m₀ t ψ + σ Σ_i m_i (ψ × e_i) = m₀ t ψ + σ (ψ × m⃗),  m⃗ := (m₁,m₂,m₃).

Apply the (complex-bilinear) form ψᵗ(·). Since ψᵗ(ψ × m⃗) = det[ψ, ψ, m⃗] = 0, we get
m₀ t (ψᵗψ) = 0; as t > 0 and |ψᵗψ| = τ > 0 this forces **m₀ = 0**. Then ψ × m⃗ = 0, and
ker[ψ]_× = span{ψ} for ψ ≠ 0 (Lemma 6.1(iii) below), so m⃗ = λψ for some λ ∈ ℂ. Thus
m = λ(0, ψ) and k = m̄ = λ̄(0, ψ̄); with ‖ψ̄‖ = 1 the choice λ = 1 gives a unit vector. ∎

(Gates `G5i.c6`, `G5i.c7` in the normal form; `G5i.f1` for arbitrary complex ψ. Note that (4.4)
also re-proves dim ker Λ^c(P_ψ) = 1 for τ > 0, independently of the rank count of §3.3 —
two independent routes to the same kernel dimension.)

**Proposition 4.3 (the closed form of the weight).** For every unit ψ with τ(ψ) > 0 and every
Hermitian φ,

> **(4.5)** **K(k(ψ)) = −σ·[ψ]_×**   (purely skew — no identity part, because k₀ = 0),
> **(4.6)** **K(k)^† K(k) = (x/2)·(𝟙 − P_ψ)**,
> **(4.7)** **w_E(ψ,φ) = (x/2)·( Tr φ − ⟨ψ|φ|ψ⟩ )**, so for a **state** φ:
> **w_E = (x/2)·(1 − ⟨ψ|φ|ψ⟩) ∈ [0, x/2]**.

*Proof.* (4.5): K(k) = Σ_a k̄_a K_a = Σ_i ψ_i K_i = σ Σ_i ψ_i A_i = −σ[ψ]_× by (1.1) and k₀ = 0.
(4.6): [w]_× is antisymmetric, [w]_×^ᵗ = −[w]_×, and its entries are linear in w, so
[ψ]_×^† = conj([ψ]_×)^ᵗ = [ψ̄]_×^ᵗ = −[ψ̄]_×. Hence K^† = (−σ[ψ]_×)^† = σ[ψ̄]_× and
K^†K = σ[ψ̄]_×·(−σ[ψ]_×) = −σ²·[ψ̄]_×[ψ]_×. For any v,
[ψ̄]_×[ψ]_× v = ψ̄ × (ψ × v) = ψ(ψ̄·v) − v(ψ̄·ψ) = (ψψ^† − ‖ψ‖²𝟙)v, hence
K^†K = σ²(‖ψ‖²𝟙 − P_ψ) = (x/2)(𝟙 − P_ψ) for unit ψ.
(4.7) is (4.2) with (4.6). Finally 0 ≤ ⟨ψ|φ|ψ⟩ ≤ 1 for a state φ, giving the range. ∎

Gates: `G5i.d1`, `G5i.d3` (normal form), `G5i.f2`, `G5i.f3` (arbitrary ψ), `G5i.e1`, `G5i.e2`
(the functional identity (4.7) against a **general Hermitian φ** with nine free real parameters —
a formula-level, not value-level, verification), and `G5ii.b` (numeric, with k taken from an
independent Hermitian eigensolver rather than from (4.3)).

**Remark 4.4 (why w_E is x-linear and α-independent).** (4.7) is strikingly simple: the whole
α-dependence of the E-side kernel weight is carried by the *direction* ψ inside ⟨ψ|φ|ψ⟩, and the
prefactor is exactly σ² = x/2 — the identity-Kraus weight 1−x never appears, precisely because
k₀ = 0. This is the structural reason the exceptional set turns out empty (§6).

---

## 5. G2 — the leading-coefficient expansion at every anisotropic pure base point

**Theorem 5.1 (anisotropic ε log(1/ε) expansion).** Let x ∈ (0,1), let ψ ∈ ℂ³ be a unit vector with
**τ(ψ) > 0**, P = P_ψ, let φ be **any** state on ℂ³, and put ρ_ε = (1−ε)P + εφ. Let
g = g(x,τ) = μ₋ be the gap of (3.6) and w_E = w_E(ψ,φ) = (x/2)(1 − ⟨ψ|φ|ψ⟩) of (4.7). Then for
every ε with **0 < ε ≤ g/4**,

> **(5.1)** | Ic(ρ_ε) + w_E·ε·log(1/ε) | ≤ **C(x,τ)·ε**, with
> **C(x,τ) := 6/(e·g) + (5/2)·log(5/2) + 3·(1 + log(2/g)) + 3·(1 + log(4/(3g)))**
> ≤ **3/g + 9 + 6·log(2/g)**.

In particular **Ic(ρ_ε) = −w_E·ε·log(1/ε) + O(ε)** as ε → 0⁺ with w_E ≥ 0, and the O(ε) constant is
explicit in (x, τ) and **uniform in φ**.

*Proof.* Both outputs are affine in ε:

  Λ(ρ_ε) = A_B + ε B_B,  A_B := Λ(P), B_B := Λ(φ) − Λ(P);
  Λ^c(ρ_ε) = A_E + ε B_E, A_E := Λ^c(P), B_E := Λ^c(φ) − Λ^c(P).

**Norms.** For Hermitian differences of PSD trace-one operators,
λ_max(X − Y) ≤ λ_max(X) ≤ 1 and λ_min(X − Y) ≥ −λ_max(Y) ≥ −1, so

> **(5.2)** ‖B_B‖ ≤ 1 and ‖B_E‖ ≤ 1; take b := 1.

(Λ^c(P) and Λ^c(φ) are 4 × 4 PSD of trace 1; the padding zeros are harmless.)

**B side: no cluster at all.** By Proposition 3.2, τ > 0 gives spec A_B ⊂ [g, 1] with **no zero
eigenvalue**. By Weyl (Fact 3.1 of the reviewed note) each eigenvalue of Λ(ρ_ε) satisfies
|λ_j(ε) − λ_j(0)| ≤ εb = ε, so λ_j(ε) ∈ [g − ε, 1] ⊆ [3g/4, 1] for ε ≤ g/4. Lemma 4.2 of the
reviewed note (regular-term stability) with a = 3g/4 gives, per eigenvalue,
|h(λ_j(ε)) − h(λ_j(0))| ≤ (1 + log(4/(3g)))·ε, and there are **3** of them. Hence

> **(5.3)** | S(Λ(ρ_ε)) − S(Λ(P)) | ≤ 3·(1 + log(4/(3g)))·ε.

*(Bookkeeping note. The displayed C(x,τ) carries the two regular-term blocks as
3(1+log(2/g)) [B side] + 3(1+log(4/(3g))) [E side], whereas the proof just gave the sharper
3(1+log(4/(3g))) on the B side as well. Since 4/(3g) < 2/g the displayed C is therefore a **valid,
deliberately slack** bound, and it is the expression the script evaluates. Keeping the two blocks
separate makes C manifestly the sum of four independently justified pieces: B-regular, E-cluster,
E-regular, and the ε² correction inside the cluster term.)*

**E side: a one-dimensional kernel cluster.** A_E ⪰ 0 with K_E := ker A_E of dimension
**m_E = 1** and smallest nonzero eigenvalue g, by (3.6). Since Π_E := |k⟩⟨k| projects onto ker A_E,
Π_E A_E Π_E = 0, and the compression of B_E to K_E is the **scalar**

> **(5.4)** μ^E := ⟨k| B_E |k⟩ = ⟨k| Λ^c(φ) |k⟩ − ⟨k| Λ^c(P) |k⟩ = **w_E**.

Proposition 3.3 of the reviewed note (kernel-cluster bound), applied with A = A_E, B = B_E, b = 1,
m = 1 and this g, is valid for ε ≤ g/(4b) = g/4 and gives: the smallest eigenvalue λ₁(ε) of
Λ^c(ρ_ε) satisfies

> **(5.5)** |λ₁(ε) − ε·w_E| ≤ (40/9)·ε²/g ≤ 6·ε²/g,

while the other three eigenvalues satisfy λ_j(ε) ≥ g − ε ≥ 3g/4. For the cluster term, λ₁(ε) ≥ 0
(Λ^c(ρ_ε) is a state) and λ₁(ε)/ε ≤ w_E + 6ε/g ≤ 1 + 6/4 = 5/2 =: U, so Lemma 4.1 of the reviewed
note (with C = 6/g and κ(U) = max(1/e, U log U) = (5/2)log(5/2)) gives

> **(5.6)** | h(λ₁(ε)) − ε·w_E·log(1/ε) | ≤ ( 6/(e g) + (5/2)·log(5/2) )·ε.

For the three regular E-side eigenvalues, Lemma 4.2 of the reviewed note with a = 3g/4 and
δ = ε gives (1 + log(4/(3g)))·ε each; and Σ_{j≥2} h(λ_j(0)) = S(Λ^c(P)) because the kernel
eigenvalue contributes h(0) = 0. Hence

> **(5.7)** | S(Λ^c(ρ_ε)) − S(Λ^c(P)) − w_E·ε·log(1/ε) |
> ≤ ( 6/(e g) + (5/2)log(5/2) )·ε + 3·(1 + log(4/(3g)))·ε.

**Assembly.** Subtract (5.7) from (5.3) and use **S(Λ(P)) = S(Λ^c(P))** from (1.2):

  | Ic(ρ_ε) − ( 0 − w_E·ε·log(1/ε) ) | ≤ 3(1+log(4/(3g)))ε + (6/(eg) + (5/2)log(5/2))ε
  + 3(1+log(4/(3g)))ε ≤ C(x,τ)·ε,

using 4/(3g) < 2/g for the last step. The simplification uses 6/e ≤ 2.208 < 3 and
(5/2)log(5/2) ≤ 2.291, 3 + 3 = 6, 2.291 + 6 ≤ 9 (with log(4/3) ≤ log 2 absorbed):
C ≤ 3/g + 9 + 6 log(2/g). ∎

**Corollary 5.2 (no first-order ascent off the isotropic stratum; strict decrease).** Let
x ∈ (0,1) and τ(ψ) > 0.
(i) The coefficient of ε log(1/ε) in Ic(ρ_ε) is **−w_E ≤ 0** for every state φ: no anisotropic pure
base point supports a first-order ε log(1/ε) ascent, at any x.
(ii) If **φ ≠ P_ψ** then w_E > 0 strictly and

> **(5.8)** **Ic(ρ_ε) < 0 for every 0 < ε < min( g/4, exp(−C(x,τ)/w_E) ).**

(iii) If φ = P_ψ then ρ_ε = P for all ε and **Ic(ρ_ε) = 0 identically** (by (1.2)).

*Proof.* (i) is (5.1) with w_E ≥ 0. (ii): by (4.7), w_E = 0 ⟺ ⟨ψ|φ|ψ⟩ = 1 ⟺ φ = P_ψ for a state
φ (equality in ⟨ψ|φ|ψ⟩ ≤ Tr φ = 1 forces supp φ ⊆ span{ψ}); so φ ≠ P_ψ gives w_E > 0, and (5.1)
gives Ic(ρ_ε) ≤ ε·(C(x,τ) − w_E·log(1/ε)) < 0 exactly when log(1/ε) > C/w_E. (iii) is immediate. ∎

**Remark 5.3 (what is uniform in what — and what is NOT).** C(x,τ) depends on (x, τ) only, not on
φ and not on which ψ with that τ was chosen (only (3.6) was used, and it holds for every ψ with
that τ). It **degenerates as τ ↓ 0**: g ≍ x(1−x)τ²/(2−x), so C ≍ 3(2−x)/(x(1−x)τ²) blows up like
τ^{−2} and the admissible window ε ≤ g/4 collapses like τ². This is not a defect of the proof — it
is the correct behaviour, and §7 shows it is exactly what reconciles Corollary 5.2 with the
reviewed isotropic ascent at τ = 0.

**Remark 5.4 (the one-dimensional cluster is what changes).** Structurally, the difference from the
isotropic case is not the size of any constant but a **kernel-dimension count**: at τ > 0 the B
side has *no* kernel (Proposition 3.2) and the E side has a *one*-dimensional one, so the
ε log(1/ε) coefficient is w_B − w_E with **w_B ≡ 0**. At τ = 0 the B side acquires a kernel
(spanned by ψ̄) and the E-side kernel becomes two-dimensional, and the competition
w_B − w_E = d₁(x) becomes possible. The anisotropic strata cannot compete at first order because
they have nothing on the B side to compete with.

---

## 6. G3 — the exceptional set is EMPTY

By Lemma 4.1 the states φ that kill the ε log(1/ε) term are exactly those with
supp φ ⊆ ker K(k). By (4.4), K(k)ψ = 0 always, so span{ψ} ⊆ ker K(k) and φ = P_ψ is always such a
state (the trivial, flat direction of Corollary 5.2(iii)). The commission's exceptional set is

> **(6.1)** E := { (x, α) : x ∈ (0,1), α ∈ [0, π/4), dim ker K(k(ψ_α)) ≥ 2 }
> = { (x, α) : rank K(k) ≤ 1 }.

**Lemma 6.1 (rank and kernel of a complex cross-product matrix).** Let w ∈ ℂ³, w ≠ 0, and
S := [w]_×. Then, with the complex-bilinear w·w := wᵗw:
(i) S² = w wᵗ − (w·w)𝟙 and S³ = −(w·w)·S, so the characteristic roots of S are
**0, ±i√(w·w)**;
(ii) **rank S = 2**, whether or not w·w = 0;
(iii) **ker S = span{w}**.

*Proof.* (i) [w]_×[w]_× v = w × (w × v) = w(w·v) − v(w·w), which is the displayed S²; multiplying by
S and using S w = w × w = 0 gives S³ = −(w·w)S. For the characteristic polynomial
λ³ − c₁λ² + c₂λ − c₃ of the 3 × 3 matrix S: c₁ = Tr S = 0 (S is antisymmetric);
Tr S² = Tr(w wᵗ) − 3(w·w) = (w·w) − 3(w·w) = −2(w·w), so c₂ = (c₁² − Tr S²)/2 = **(w·w)**; and
c₃ = det S = 0 because S w = 0 with w ≠ 0. Hence det(λ𝟙 − S) = **λ³ + (w·w)λ**, whose roots are
0 and ±i√(w·w).
(ii) If w·w ≠ 0, the three roots 0, ±i√(w·w) are distinct, S is diagonalizable, and the
0-eigenspace is one-dimensional, so rank S = 2. If w·w = 0 then S³ = 0 while
S² = w wᵗ ≠ 0 (because w ≠ 0), so S is nilpotent of index exactly 3, i.e. a single Jordan block
J₃, and again rank S = 2.
(iii) rank S = 2 and Sw = 0 with w ≠ 0 give ker S = span{w}. ∎

(Gates `G5i.d5`, `G5i.f4`, `G5i.f5`, `G5i.f6`; the char-poly gate `G5i.d5` verifies
det(λ𝟙 − K(k)) = λ³ + (xτ/2)λ symbolically, i.e. **ψ·ψ = τ** in the normal form.)

**Theorem 6.2 (exact characterization of the exceptional set: it is empty).** For every x ∈ (0,1)
and every unit ψ with τ(ψ) > 0:

> **(6.2)** **rank K(k(ψ)) = 2 and ker K(k(ψ)) = span{ψ}, exactly.**
> Consequently, for a state φ: **w_E(ψ,φ) = 0 ⟺ φ = P_ψ**, and
> **E = ∅.**

*Proof.* By (4.5), K(k) = −σ[ψ]_× with σ = √(x/2) > 0 and ψ ≠ 0. Lemma 6.1(ii),(iii) gives
rank = 2 and kernel span{ψ}. The φ statement is Lemma 4.1 plus supp φ ⊆ span{ψ} ⟺ φ = P_ψ for a
state. Since dim ker K(k) = 1 < 2 at every (x, α) with α < π/4, the set (6.1) is empty. ∎

Three independent confirmations, all in §9:
* symbolically, spec K(k)^†K(k) = {0, x/2, x/2} over the whole parameter space (gate `G5i.d4`) —
  the singular values of K(k) are √(x/2), √(x/2), 0, so the rank is 2 with a *clean* gap and the
  conclusion is not a numerical near-degeneracy;
* symbolically for **arbitrary** complex ψ (gate `G5i.f3`);
* numerically, the commissioned 20 × 20 (x, α) grid scan (gate `G5iv.a`): rank 2 at **all 400**
  points, smallest K^†K eigenvalue ≤ 6.7e-52, second-smallest ≥ 0.0238.

**Remark 6.3 (the a·𝟙 + skew(w) analysis the commission anticipated).** The commission suggested
analysing K(k) through the form a𝟙 + skew(w) with characteristic roots a, a ± i√(w·w). The answer
is that **a = 0 identically**, because the kernel vector has k₀ = 0 (Lemma 4.2) and the identity
Kraus operator is the only source of an a𝟙 part. The complex bilinear form is w·w = ψᵗψ = τ (the
isotropy invariant itself), so the char roots are 0, ±i√(xτ/2). The "mind complex bilinear w.w"
warning is real but does **not** create an exception here: rank [w]_× = 2 for w ≠ 0 *both* when
w·w ≠ 0 (diagonalizable, simple kernel) and when w·w = 0 (nilpotent J₃) — Lemma 6.1(ii). Had the
rank dropped in the isotropic-bilinear case w·w = 0 there would have been an exceptional stratum
accumulating at τ = 0; there is not.

---

## 7. The τ → 0 boundary: why this does NOT contradict the isotropic ascent

Corollary 5.2 says that at every τ > 0, small-ε perturbations of P_ψ strictly *decrease* Ic below
0 unless φ = P_ψ. The reviewed isotropic layer says that at τ = 0 and x < 2/5 they *increase* it.
Both are true, and the reconciliation is a **kernel-dimension jump**, not a discontinuity of any
formula. Precisely (all four items gated in §9, G5(iii)):

1. **The E-side kernel dimension jumps** from 1 (τ > 0, (3.6)) to 2 (τ = 0, reviewed (1.3) of the
   N1′ note), and the **B-side** kernel dimension jumps from 0 to 1. The τ = 0 problem is therefore
   *not* the τ → 0 limit of the τ > 0 problem, and Theorem 5.1 must not be evaluated at τ = 0.
2. **Where the missing isotropic slope goes.** The reviewed isotropic weight at the witness
   φ = P_ψ̄ is w_E^{iso} = μ_A + x/2 with μ_A = 4x(1−x)/(2−x) (block-A slope) and x/2 (block-B
   slope). My τ > 0 formula at the same φ gives, by (4.7) and |⟨ψ|ψ̄⟩|² = τ²,

   > **(7.1)** w_E(ψ_α, P_ψ̄) = (x/2)(1 − τ²) **→ x/2** as τ ↓ 0,

   i.e. it converges to the **block-B** slope only. The block-A slope μ_A is carried by the
   eigenvalue μ₋(x,τ), which for τ > 0 is a **nonzero (regular)** eigenvalue and only joins the
   kernel cluster at τ = 0. Quantitatively, from (3.6),

   > **(7.2)** μ₋(x,τ)/τ² → x(1−x)/(2−x) = **μ_A/4** as τ ↓ 0.

   (Verified at x ∈ {9/20, 1/5} and τ ∈ {1e-1, 1e-2, 1e-3, 1e-5}: gate `G5iii.c`; e.g. at
   x = 9/20, μ₋/τ² = 0.1596774523 at τ = 1e-3 against μ_A/4 = 0.1596774194.)
3. **The window collapses at the same rate.** Theorem 5.1 holds only for ε ≤ g/4 ≍ x(1−x)τ²/(4(2−x)),
   which at x = 9/20, τ = 1e-3 is already 3.99e-8, and at τ = 1e-5 is 3.99e-12 (gate `G5iii` table).
   So the anisotropic no-ascent statement retreats to smaller and smaller ε as the stratum
   approaches the isotropic one, and it never covers the isotropic witness.
4. **Consequently no uniform-in-τ statement is claimed or implied**, and in particular *nothing*
   here says that Ic ≤ 0 in a τ-uniform neighbourhood of the pure states. See §10 item 3.

---

## 8. G4 — the linear layer on exceptions: vacuous

Since E = ∅ (Theorem 6.2), the commission's G4 branch "if E is nonempty" is not entered. The
commission's own vacuity statement is what applies, and it is exactly correct:

> The kernel-avoiding set is { φ state : supp φ ⊆ ker K(k) } = { φ : supp φ = span{ψ} } = **{P_ψ}**,
> and along that direction ρ_ε = P for all ε, so **Ic(ρ_ε) = 0 identically** (not merely to first
> order) by (1.2). Every other state φ has w_E > 0 **strictly**, so the ε log(1/ε) term is present
> with a negative coefficient and (5.8) already settles the sign. **No balanced or ε-linear layer
> computation is needed at τ ≠ 0 for the Theorem as stated.**

For completeness: the ε-linear coefficient
c₁ = −Tr[Λ(φ) log Λ(P)] + Tr[Λ^c(φ) log Λ^c(P)] that the commission would have asked for on
exceptional strata is not even well defined here without care (log Λ^c(P) is singular at τ > 0,
the kernel being one-dimensional) — but this is moot: on the only kernel-avoiding direction the
whole family is constant.

---

## 9. G5 — the sanity script, and the failure modes it caught

Script: **`tools/whgap_p13a_sanity.py`** (mine; **56 boolean gates, all PASS**).
Command: `C:<home>/cpython3119/python.exe tools/whgap_p13a_sanity.py`
Logs: `artifacts/logs_whgap_p13a_20260730/p13a_sanity.json`, `…/p13a_sanity.log`.
Runtime 41 s. Precision: mpmath `mp.dps = 80` for the expansion gates, 60/50/40 for the crosscheck,
grid and probe gates, and **adaptive dps up to 1384** for the certificate points.

### 9.1 Two standing failure modes were hit, and the reviewer should note both

* **Failure mode 1 (sympy `.H` / `conjugate(sqrt(1−x))`), HIT.** Declaring only
  `x = Symbol('x', positive=True)` and then substituting `{t**2: 1-x, sg**2: x/2}` into the
  complement is *unsound in sympy*: the complement's off-block entries carry the **odd** monomial
  `t·sg`, and sympy rewrites `t` as `sqrt(1-x)` there, after which `conjugate(sqrt(1-x))` survives
  (sympy cannot decide 1 − x > 0) and the Hermiticity gate failed. This is precisely the documented
  radical-power-substitution trap. **Fix, recorded append-only in the script:** move the entire
  E-side symbolic layer into a *radical-free rational chart* of the conic t² + 2σ² = 1,

  > **(9.1)** t = (1−2v²)/(1+2v²), σ = 2v/(1+2v²), so **x = 8v²/(1+2v²)²**, v ∈ (0, 1/√2),

  together with u = tan α, τ = (1−u²)/(1+u²). x = 4w/(1+w)² with w = 2v² is strictly increasing on
  w ∈ (0,1), so (9.1) sweeps **all** of x ∈ (0,1) bijectively; every expression in §4–§6 is then a
  rational function of (u, v) with rational coefficients and conjugation is entrywise-safe. Gate
  `G5i.c_chart_valid` verifies t² + 2σ² = 1 and prints x(v). This is a *tooling* change: no
  mathematical step of §3–§8 depends on the chart.
* **Failure mode 5 (comparison of symbolics), HIT.** `sympy.Matrix.charpoly()` raises
  `TypeError: cannot determine truth value of Relational` inside `_sort_factors` on these entries.
  Replaced throughout by the helper `charpoly_expr(M, λ) = expand(det(λ𝟙 − M, method='berkowitz'))`.

Screened and not hit: 2 (pinned interpreter used), 3 (complement convention re-derived, `G5i.c0`),
4 (`†` = `ᵗ` only for real Kraus, `G5i.c1`), 6 (LF `SHA256SUMS_p13a.txt`, `sha256sum -c` OK),
7 (no division by cluster-slope differences anywhere; the one-dimensional cluster makes this
structural), 8 (Lemma 4.1 of the reviewed note used with its uniform bound), 9 (anchoring: §3–§6
derived and gated before any comparison; the comparisons are flagged in §1.4 and §7).

### 9.2 G5(i) — symbolic gates (37 gates)

| gate group | content | result |
|---|---|---|
| `G5i.a*` | normal form: P = \|ψ⟩⟨ψ\|, P² = P, ψᵗψ = (1−u²)/(1+u²) = cos 2α, ⟨ψ\|ψ̄⟩ = τ, normalization | PASS |
| `G5i.b*` | **Λ(P) block diagonal; Λ(P)₃₃ = x/2; Tr(2×2) = 1 − x/2; det(2×2) = x(1−x)τ²/2**; charpoly factorization (3.5); μ_± are the roots; discriminant at τ = 1 equals (1−3x/2)²; q(x/2) = (x/2)(1−x)(τ²−1) ≤ 0; det Λ(P) = (x/2)·x(1−x)τ²/2; μ₊μ₋ = D | PASS |
| `G5i.c*` | rational chart valid; Kraus reproduce Λ_x on all 9 entries; Σ K_a^ᵗK_a = 𝟙; every Λ^c(P) entry rational; Λ^c(P) Hermitian, trace 1; **charpoly Λ^c(P) = λ(λ−x/2)(λ²−Tλ+D)** (isospectrality + ker dim 1); Λ^c(P)k = 0 for k = (0, ψ̄); ‖k‖ = 1 | PASS |
| `G5i.d*` | **K(k) = −σ[ψ]_×**; K(k)ψ = 0; **K^†K = (x/2)(𝟙−P)**; spec K^†K = {0, x/2, x/2}; **charpoly K(k) = λ³ + (xτ/2)λ** | PASS |
| `G5i.e*` | **w_E = (x/2)(Tr φ − ⟨ψ\|φ\|ψ⟩)** against a general Hermitian φ (9 free real parameters); the state specialization; w_E = Tr[φ K^†K] | PASS |
| `G5i.f*` | the same load-bearing identities for an **arbitrary** complex ψ (no normal form): kernel vector, K(k) skew form, K^†K, charpoly (3.5), Tr(PPᵗ) = τ², and Lemma 6.1(i)–(iii) | PASS |
| `G5i.g1` | transport (1.3) at four test O, det = +1, +1, −1, −1 | PASS |

Value-vs-formula (rule 7f): all of G5(i) is **formula-level** — identities in the symbols
(u, v) resp. arbitrary complex ψ and arbitrary Hermitian φ, i.e. in x, α and φ simultaneously — not
value checks at sample points.

### 9.3 G5(ii) — numeric spot-check of Theorem 5.1

At the three commissioned points, three random states φ each (seeded `Random(20260730)`),
ε ∈ {1e-4, 1e-6} as commissioned plus {1e-8, 1e-12, 1e-20} to exhibit the asymptotics.
Ic is computed **from the Kraus operators only** (assemble ρ_ε, apply Λ and Λ^c, Hermitian
eigensolver, −Σλ log λ), never from any formula of this note. Sample rows (φ#0 at each point;
the full 45-row table is `p13a_sanity.json`, `meta.G5ii_table`; Ic in nats):

| x | α | τ | g = μ₋ | C(x,τ) | ε | w_E | Ic(ρ_ε) | −w_E ε log(1/ε) | (Ic − pred)/ε |
|---|---|---|---|---|---|---|---|---|---|
| 9/20 | π/8 | 0.70711 | 0.0903784 | 50.078 | 1e-4 | 0.13473206 | −1.2414392e-4 | −1.2409281e-4 | −5.1112e-4 |
| 9/20 | π/8 | 0.70711 | 0.0903784 | 50.078 | 1e-6 | 0.13473206 | −1.8619016e-6 | −1.8613922e-6 | −5.0944e-4 |
| 9/20 | π/8 | 0.70711 | 0.0903784 | 50.078 | 1e-20 | 0.13473206 | −6.2051501e-20 | −6.2046405e-20 | −5.0952e-4 |
| 9/20 | π/6 | 0.5 | 0.0422193 | 82.504 | 1e-4 | 0.17694299 | −1.5408367e-4 | −1.6297052e-4 | +8.8869e-2 |
| 9/20 | π/6 | 0.5 | 0.0422193 | 82.504 | 1e-20 | 0.17694299 | −8.0596189e-20 | −8.1485260e-20 | +8.8907e-2 |
| 1/5 | π/8 | 0.70711 | 0.0468871 | 76.670 | 1e-4 | 0.03946536 | **+1.6334692e-5** | −3.6348944e-5 | +5.2684e-1 |
| 1/5 | π/8 | 0.70711 | 0.0468871 | 76.670 | 1e-6 | 0.03946536 | −1.8340822e-8 | −5.4523416e-7 | +5.2689e-1 |
| 1/5 | π/8 | 0.70711 | 0.0468871 | 76.670 | 1e-20 | 0.03946536 | −1.2905533e-20 | −1.8174472e-20 | +5.2689e-1 |

Gate verdicts:

* `G5ii.a` — dim ker Λ^c(P_ψ) = 1 at all three points (λ₁/λ₀ ≥ 1.6e+80) and the eigensolver's
  kernel vector equals (0, ψ̄) up to phase to ≤ 1.3e-81. **Independent construction** of k, not a
  re-evaluation of (4.3).
* `G5ii.b` — w_E from ⟨k|Λ^c(φ)|k⟩ with the *numeric* k agrees with (4.7) to < 1e-50 at all nine
  (point, φ) pairs.
* `G5ii.c` — the two-point log-slope of Ic(ρ_ε)/ε between ε = 1e-12 and 1e-20 equals **−w_E** with
  relative error ≤ 1.7e-12 at all nine pairs. *This is the actual test of the leading coefficient*:
  the residual column above shows that (Ic − pred)/ε converges to a finite constant, i.e.
  Ic/ε = −w_E log(1/ε) + c + o(1), which is the content of Theorem 5.1 sharpened by one order.
* `G5ii.d` — the rigorous bound |Ic + w_E ε log(1/ε)| ≤ C(x,τ)·ε holds at every tested
  ε ≤ g/4 (all 45 rows are inside the window). *Honest note:* at these ε the bound is far from
  tight (C ≈ 50–83 while log(1/ε) ≤ 46), so `G5ii.d` alone does not force the sign.
* `G5ii.e` — **certificate points** where the bound *does* force the sign: at
  ε = min(g/4, exp(−1.2·C/w_E)) < exp(−C/w_E), with adaptive precision:

| x | α | dps | ε | w_E | C | Ic(ρ_ε) | −w_E ε log(1/ε) | Ic < 0 | bound |
|---|---|---|---|---|---|---|---|---|---|
| 9/20 | π/8 | 691 | 1.6533619e-197 | 0.132626661 | 50.078 | −9.9369398871e-196 | −9.9357124475e-196 | yes | holds |
| 9/20 | π/6 | 933 | 3.6048569e-294 | 0.146526091 | 82.504 | −3.5671901224e-292 | −3.5689675761e-292 | yes | holds |
| 1/5 | π/8 | 1384 | 2.4036598e-474 | 0.084364561 | 76.670 | −2.1834924817e-472 | −2.2114542724e-472 | yes | holds |

### 9.4 G5(iii) — the τ → 0 crosscheck

As commissioned, the τ = 0 setup is **not** used for the isotropic stratum. What is checked is the
correspondence of §7: `G5iii.a` (w_E(τ>0, φ = P_ψ̄) = (x/2)(1−τ²) → x/2, the isotropic **block-B**
slope), `G5iii.b` (the closed form μ₋(x,τ) reproduces the numeric second-smallest Λ^c(P)
eigenvalue), `G5iii.c` (μ₋/τ² → x(1−x)/(2−x) = μ_A/4, so the isotropic block-A slope μ_A belongs
to an eigenvalue that is *nonzero* at τ > 0). Table in `meta.G5iii_table`, at
x ∈ {9/20, 1/5}, τ ∈ {1e-1, 1e-2, 1e-3, 1e-5}.

### 9.5 G5(iv) — the exceptional-set scan

20 × 20 grid, x ∈ {1/21,…,20/21}, α ∈ {(π/4)·i/21, i = 1..20} (400 points, all τ > 0). Results:
rank histogram of K(k) = **{2: 400}**; max |smallest eigenvalue of K^†K| = 6.68e-52; min
second-smallest eigenvalue of K^†K = 0.0238 (a clean gap, so the rank verdict is not a
near-degeneracy); max deviation of K^†K from (x/2)(𝟙 − P_ψ) = 4.83e-50; max deviation of the
numeric kernel vector from (0, ψ̄) up to phase = 3.61e-49; min second-smallest eigenvalue of
Λ^c(P) across the grid = 1.30e-4 (so dim ker Λ^c(P) = 1 throughout). Gates `G5iv.a`–`G5iv.d`.

### 9.6 G5(v) — a NON-COMMISSIONED add-on that fixes the theorem's scope

The (x, α, ε) = (1/5, π/8, 1e-4) row above is **positive**: Ic = +1.63e-5 > 0 from an anisotropic
pure base point. That is not a contradiction (Theorem 5.1 is a small-ε statement, and at x = 1/5
the crossover is at ε ≈ exp(−0.5269/0.03947) ≈ 1.6e-6, matching the sign flip between 1e-4 and
1e-6), but it does mean the theorem must **not** be read as "τ ≠ 0 base points are useless". To
record this honestly I added a bounded probe (`G5v`): for x ∈ {1/5, 9/20, 49/100}, α over 8 values
in (0, π/4], 8 states φ each (three anisotropic projectors, four random, plus P_ψ̄), ε over 12
values in [1e-6, 0.9]. Maxima found: **x = 1/5 → max Ic = +0.3093534** (at τ = 0.98079, ε = 0.9);
**x = 9/20 → 0.0**; **x = 49/100 → 0.0**. This is a *bounded search*; it licenses nothing (compare
P3's much larger S1 scans already on disk) and is reported only to fix the scope of §5.

### 9.7 Provenance hashes (SHA-256)

```
e8fcace922ad534c5c813bb479905f24792b69add18aee5393c24e2496cbc269  tools/whgap_p13a_sanity.py
767ebac8416aea985d91026b3181efcfcf8c2d68b596aee9b9d97b09fd5a68fa  artifacts/logs_whgap_p13a_20260730/p13a_sanity.json
0e318d9f8538f52a38f0cb867c2f60141305e9e50fc5d005a1ebe59b01cc0be3  artifacts/logs_whgap_p13a_20260730/p13a_sanity.log
```

Archived as `artifacts/logs_whgap_p13a_20260730/SHA256SUMS_p13a.txt` (LF endings; verified with
`sha256sum -c`, three OK).

---

## 10. What is and is not established — stated as precisely as I can

**Established here (subject to R6 review), for every x ∈ (0,1):**

1. **Proposition 3.2 (exact spectrum on every stratum)** — spec Λ_x(P_ψ) = {x/2, μ₊, μ₋} with
   μ_± the roots of λ² − (1−x/2)λ + x(1−x)τ²/2; full rank ⟺ τ > 0; μ₋ ≤ x/2 ≤ μ₊; and
   spec Λ_x^c(P_ψ) is the same set plus one 0.
2. **Lemma 4.2 + Proposition 4.3 (the E-side kernel data in closed form)** —
   ker Λ_x^c(P_ψ) = span{(0, ψ̄)}, K(k) = −σ[ψ]_×, K^†K = (x/2)(𝟙 − P_ψ), and
   **w_E = (x/2)(1 − ⟨ψ|φ|ψ⟩)**.
3. **Theorem 5.1 (the commissioned expansion)** — for τ > 0,
   Ic(ρ_ε) = −w_E ε log(1/ε) + R(ε) with |R(ε)| ≤ C(x,τ)ε on 0 < ε ≤ g/4, C explicit and uniform
   in φ; and hence **Corollary 5.2**: the ε log(1/ε) coefficient is ≤ 0 always, is < 0 for every
   φ ≠ P_ψ, and Ic(ρ_ε) < 0 outright for ε < min(g/4, exp(−C/w_E)).
4. **Theorem 6.2 (G3, the commissioned exceptional set)** — **E = ∅**: dim ker K(k) = 1 exactly, at
   every (x, α) with τ > 0. Hence **G4 is vacuous** (§8).

**The combination with the reviewed isotropic layer, stated with its exact scope.** Define the
*n = 1 pure-base first-order mechanism* as: a pure base point P_ψ, a state φ, and the family
ρ_ε = (1−ε)P_ψ + εφ, judged by the sign of the coefficient of ε log(1/ε) in Ic(ρ_ε) as ε → 0⁺.
Then, granting the R5c/R5d-reviewed isotropic results (max over φ of that coefficient equals
max(d₁(x), 0) with d₁ = (1−x)(2−5x)/(2−x)) and the above:

> **(10.1)** the coefficient is > 0 for **some** (ψ, φ) ⟺ **x < 2/5**, and every such witness has
> **τ(ψ) = 0**. Equivalently: at n = 1 the pure-base first-order mechanism yields
> positive-capacity witnesses **exactly** for x < 2/5, and only on the isotropic stratum.

This is the statement the commission's target Theorem asks for, and it is the one I claim (at
CONJECTURED/pending-review). **It is a statement about a mechanism, not about Q.** In particular:

5. **NOT established: Q^{(1)}(Λ_x) = 0 on [2/5, 1/2).** Theorem 5.1 is a *local, small-ε* statement
   at *pure* base points. Three gaps remain even at n = 1:
   (a) **finite mixing** — §9.6 exhibits Ic > 0 from a τ > 0 base point at moderate ε (at x = 1/5),
   so the small-ε sign says nothing at ε = O(1); every ρ is (1−ε)P + εφ for suitable *large* ε;
   (b) **non-uniformity in τ** — the window ε ≤ g/4 collapses like τ² (Remark 5.3, §7), so there is
   **no** τ-uniform neighbourhood of the pure states on which Ic ≤ 0 is proved, and no compactness
   argument can be run from Theorem 5.1 as stated;
   (c) **higher-order layers on the isotropic stratum at and above 2/5** — obligation (c) of the
   node is only *partly* addressed here: I settle the first-order layer off the isotropic stratum
   and note that at τ ≠ 0 the balanced layer is empty (the only balanced φ is P_ψ, along which Ic
   ≡ 0); the balanced/higher-order layers **on** the isotropic stratum at x ∈ [2/5, 1/2) are
   untouched by this note.
6. **NOT addressed: obligation (d)**, every blocklength n ≥ 2 (entangled base points; the
   superactivation directions). Nothing here restricts n ≥ 2 in any way — the entire argument is
   about a qutrit input.
7. **A closing-the-gap remark on where the difficulty now sits.** Remark 5.4 identifies the
   mechanism-level reason 2/5 appears at all: at τ > 0 the B side is *full rank*, so w_B ≡ 0 and
   the E side wins by default; the competition needs a B-side kernel, which exists only at τ = 0.
   If x_D = 2/5 is to become a theorem, the remaining work is therefore **not** further stratum
   analysis at first order (that is now complete, modulo review) but (a)/(b) above — a global,
   non-perturbative argument on [2/5, 1/2) — plus (c) and (d).

---

## 11. Status suggestions for the decision layer and for R6 (capped, per the commission)

I write no status. Suggestions, all at **CONJECTURED / pending-review** until the fresh R6 review
completes and is cited (rules 6, 7):

1. **Propositions 3.2, 4.3, Lemma 4.2, Theorem 5.1, Corollary 5.2, Theorem 6.2 (E = ∅)** — if R6
   licenses, these are candidates for PROVED: they are self-contained modulo the R5d-reviewed
   §3–§4 machinery of the N1′ note, whose use is scoped in §1.2. Until then: **CONJECTURED with
   `pending-review:`** on `WHGAP.onset-two-fifths`.
2. **The combined mechanism statement (10.1)** — candidate for PROVED *conditional on* the R5c/R5d
   isotropic inputs (which carry LICENSE A), i.e. unconditional if those verdicts stand. This is
   the statement that would close node obligation **(b)** and the **first-order part of (c)**.
   Obligations (c)-at-and-above-2/5 (isotropic higher-order layers) and (d) (n ≥ 2) remain OPEN,
   and item 5 of §10 must be carried into any status text so that (10.1) is never read as
   Q^{(1)} = 0 on the strip.
3. **The computational package** (`tools/whgap_p13a_sanity.py` + two logs, 56 gates PASS) is
   proposer-writable evidence at **NUMERICAL** with a `pending-review:` marker, citing the command,
   the log paths and the §9.7 hashes.
4. **Two new nodes are owed (rule 8b)**, for objects this note isolates but does not settle:
   (i) *"the small-ε no-ascent statement upgrades to a τ-uniform neighbourhood of the pure states"*
   — the missing (b) of §10 item 5, which is what a compactness route to Q^{(1)} = 0 on the strip
   would need; and (ii) *"finite-mixing (non-perturbative) exhaustion on [2/5, 1/2)"* — the
   missing (a). Both should be registered OPEN. The decision layer owns those writes
   (single-writer deviation).
5. **Suggested R6 attention points**, in decreasing order of how much I would distrust myself:
   (i) **Lemma 3.1's determinant** — the a(p+q) term is exactly the term an algebraic slip drops,
   and dropping it still produces a plausible-looking answer; R6 is asked (and the commission
   already asks) to redo this by a *different* route — e.g. the full 3 × 3 characteristic
   polynomial, or the eigenvalue product det Λ(P) = (x/2)·det(2×2), or an explicit orthonormal
   basis of span{ψ, ψ̄}. My own second route is gate `G5i.f7` (arbitrary-ψ charpoly).
   (ii) **Lemma 4.2's step "ψᵗ(ψ × m⃗) = 0 forces m₀ = 0"** — it uses the *complex-bilinear* form,
   not the inner product, and the conclusion is exactly where τ > 0 enters. If this step is wrong
   the whole kernel identification is wrong. Please re-derive with your own parameterization of k
   (the commission asks for this explicitly).
   (iii) **Lemma 6.1(ii) in the nilpotent case w·w = 0** — the claim rank[w]_× = 2 *also* when
   w·w = 0 is what makes E empty rather than "empty except on a τ → 0 accumulation". Check
   S² = w wᵗ ≠ 0 carefully.
   (iv) **The instantiation of Proposition 3.3 of the N1′ note at m = 1** and my recomputation of
   the four pieces of C(x,τ) (I did **not** reuse the reviewed note's constant); in particular the
   claim λ₁(ε)/ε ≤ 5/2, which uses ε ≤ g/4 and b = 1.
   (v) **The identification g = μ₋** as the smallest *nonzero* eigenvalue of both sides — via
   μ₋ ≤ x/2 ≤ μ₊, which rests on the sign of q(x/2) = (x/2)(1−x)(τ²−1).
   (vi) **The scope statements of §10 item 5** — I would like these adversarially attacked: if any
   of (a), (b), (c-isotropic), (d) is in fact closed by something already on disk, say so; and if
   my (10.1) overstates what the mechanism-level combination gives, say that instead.
   (vii) **The rational chart (9.1)** — confirm it really sweeps all of x ∈ (0,1) (so that the
   symbolic gates are formula-level over the full parameter range, not on a subregion), and that
   no gate silently depends on v < 1/√2 in a way that excludes part of (0,1).

