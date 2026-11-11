# WHGAP — the N1′ isotropic ε log(1/ε) expansion lemma, and Q(Λ_x) > 0 on (0, 2/5)

**Artifact type:** executor authorship (proof note). **Node:** `WHGAP.no-ascent-hierarchy` (P9).
**Commission:** `notes/WHGAP_REVIEW_COMMISSION_R5_20260729.md`, section **E-N1**.
**Author:** fresh executor instance, 2026-07-29 (did not author any prior WHGAP work).
**Interpreter for all computation:** `C:<home>/cpython3119/python.exe`
(sympy 1.13.1, mpmath 1.3.0, numpy 1.26.4).
**Status this note licenses by itself: NOTHING.** Everything below is proposer-authored and is
offered at **CONJECTURED / pending-review** for the R5d fresh review (rule 6).

---

## 0. PRE-ACTION REPORT (mandatory, `research/PRETASK_RELOAD_PROMPT.md`)

Files read from disk, in the prescribed order, before any mathematics:
`research/DAG_PROTOCOL.md` (whole file: §2 ladder, §3 rules 1–8, §4–§6 protocols);
`research/RESEARCH_STRUCTURE_PROTOCOL.md` (§4 placement, §5 naming, §6 atomic update, §7
move/archive, §9 closeout, §10 root-level field folders);
`channel-capacity/werner-holevo-gap/README.md`;
`channel-capacity/werner-holevo-gap/notes/WERNER-HOLEVO-GAP_PROOF_DAG.md` (DAG + inlined rules);
`channel-capacity/werner-holevo-gap/proof-dag/NODE_INDEX.md`;
`channel-capacity/werner-holevo-gap/proof-dag/nodes/WHGAP.no-ascent-hierarchy.md` (target) and its
parent `WHGAP.goal.md` (the node has no children);
then the commission `notes/WHGAP_REVIEW_COMMISSION_R5_20260729.md`.

- **Target node and status as read from disk:** `WHGAP.no-ascent-hierarchy` — **CONJECTURED**,
  `status_source: "decision-layer derivation 2026-07-29 (first-order closed form derived in-node;
  pending review)"`, with a `pending-review:` marker on the P9/P9b executor findings and
  *"Adversarial reviews: None yet."*
- **My ROLE:** **executor** (authorship). I am not a reviewer and make no independence claim of the
  reviewer kind; I state instead that I did not author any earlier WHGAP work and was given no
  desired outcome. To keep this note's derivation genuinely independent I **did not open**
  `tools/whgap_p6b_v2_fable.py`, `tools/whgap_p6b_v2_isotropic.py`, `tools/whgap_r5c_*.py`,
  `artifacts/whgap_p6b_necessity_20260729.md`, or the R5a/R5b/R5c review reports. Everything here is
  built from the §1 frozen conventions (Kraus operators) alone; the only quantities I compare
  against a previously displayed closed form are in §11 (corroboration, explicitly not a
  dependency).
- **Highest status my planned evidence could license per §2:** **NUMERICAL** for the computational
  gates (proposer-writable, with command + log + SHA-256), and **CONJECTURED** for the written
  Lemma/Theorem. A completion tier (CERTIFIED\*/PROVED) can be written **only** by the decision
  layer after the fresh R5d review completes and is cited on the node (rule 6, rule 7). I write no
  status anywhere.
- **Gates and deliverables of my commission, one line each:**
  (i) this note, containing the isotropic ε log(1/ε) expansion **Lemma** with every remainder
  explicit and a self-proved degenerate-perturbation bound (no folklore citation);
  (ii) the **Theorem** Q(Λ_x) > 0 for all x ∈ (0, 2/5) via the witness φ = P_ψ̄;
  (iii) the **exact B-side diagonalization**;
  (iv) a **numerical sanity table** produced by my own `tools/whgap_n1p_sanity.py`, logged under
  `artifacts/logs_whgap_r5_20260729/`;
  (v) an honest corollary landscape and status suggestions capped at CONJECTURED/pending-review.
- **Conflicts between commission text and disk protocols:** **two, both benign; reported, not
  silently resolved.**
  1. *Single-writer deviation.* The commission forbids me to touch node files, `NODE_INDEX.md`, or
     the DAG doc, whereas `DAG_PROTOCOL.md` §5/§6 and `RESEARCH_STRUCTURE_PROTOCOL.md` §6 (atomic
     update, rule 8c) require the executor to append the outcome to the node in the same session.
     The commission states the deviation is commissioned by the decision layer, which will perform
     the atomic node/index/DAG update citing this artifact immediately after the batch. I comply
     with the commission and record the obligation here: **this note and its logs are not yet
     linked from `WHGAP.no-ascent-hierarchy`; the decision layer owes that link (rule 8c).**
  2. *`SHA256SUMS.txt` name collision.* The commission asks for `SHA256SUMS.txt` in
     `artifacts/logs_whgap_r5_20260729/`. That file already exists (written by the R5a agent), and
     the R5b/R5c agents used `SHA256SUMS_r5b.txt` / `SHA256SUMS_r5c.txt`. Overwriting R5a's file
     would destroy cited provenance (§7: never overwrite cited history), so I follow the
     established per-role pattern and write **`SHA256SUMS_n1p.txt`** (LF endings). Hashes are also
     inlined in §12 of this note.
- **Standing failure modes screened (commission §2):** 1 (sympy `.H`/`conjugate(sqrt(1−x))`) —
  screened and *hit*, see §12; 2 (pinned interpreter) — used throughout; 3 (complement convention
  drift) — the padded 4-dimensional complement of §1 is used everywhere and re-derived in §1.3;
  4 (transpose vs conjugate-transpose) — audited in §1.1; 5 (`sorted()` on symbolic eigenvalues) —
  avoided, sorting by `str`; 6 (CRLF in SHA256SUMS) — LF enforced; 7 (eigenvalue bookkeeping at
  degeneracies) — this is the whole content of §3–§4, and the divided-difference/gap issue is
  handled by an explicit spectral-gap threshold; 8 (ε log ε bookkeeping) — Lemma 4.1 is exactly
  this, with 0 log 0 = 0 and O(ε² log(1/ε)) = o(ε) made quantitative; 9 (anchoring) — I derived
  everything before looking at any prior closed form, and never opened the prior scripts (above).

---

## 1. Conventions, types, and the base point

### 1.1 Objects and types (type audit, rule 7a)

| symbol | type | dimensions |
|---|---|---|
| `Y` | complex matrix (argument of the channel) | 3 × 3 |
| `Λ_x` | linear map, CPTP | M₃(ℂ) → M₃(ℂ) |
| `K_0,…,K_3` | Kraus operators, **real** entries | 3 × 3 each |
| `Λ_x^c` | linear map, CPTP (padded complement) | M₃(ℂ) → M₄(ℂ) |
| `ψ, ψ̄, e₃` | unit vectors (pure states, kets) | ℂ³ |
| `P = \|ψ⟩⟨ψ\|`, `φ`, `ρ_ε` | states (PSD, trace 1) | 3 × 3 |
| `Λ(ρ_ε)` | state | 3 × 3 |
| `Λ^c(ρ_ε)` | state | 4 × 4 (rank ≤ 3) |
| `Π_E` | orthogonal projector onto ker Λ^c(P) | 4 × 4, rank 2 |
| `w_B, w_E, d₁, c₁, C(x)` | real scalars | — |
| `Ic(ρ)` | real scalar (nats unless stated) | — |

Frozen definitions (commission §1), reproduced verbatim in content:

- **Channel.** For x ∈ (0,1),
  Λ_x(Y) = (1−x) Y + (x/2)·(Tr(Y)·𝟙 − Yᵗ) on qutrits.
- **Kraus.** K₀ = √(1−x)·𝟙 and K_{i} = √(x/2)·A_{i} for i = 1,2,3, where (A_i)_{jk} = ε_{ijk}
  (Levi-Civita). *Index note:* the commission writes μ = 0,1,2; I write i = 1,2,3 for the Kraus
  label and j,k = 1,2,3 for matrix indices, so that ψ = (e₁ + i e₂)/√2 and e₃ use the same
  1-based labels. This is a pure relabelling of the same operator set. It is harmless for every
  statement below because the environment index enters only through the Gram matrix
  Λ^c(Y)_{ab} = Tr(K_a Y K_b^†), and relabelling the Kraus operators conjugates Λ^c by a
  permutation matrix, leaving all spectra (hence all entropies) invariant.
- **Complement (padded, 4-dimensional).** Λ_x^c(Y)_{ab} = Tr(K_a Y K_b^†), a,b ∈ {0,1,2,3}.
  Because the K_a are **real**, K_a^† = K_aᵗ; the identification of `†` with `ᵗ` is used only for
  these real matrices and never for the (complex) states. This is standing failure mode 4 and is
  the only place `†` = `ᵗ` is invoked.
- **Isotropy.** τ(ψ) = |ψᵗψ|; the isotropic stratum is τ = 0; canonical representative
  ψ = (e₁ + i e₂)/√2 with ψ̄ = (e₁ − i e₂)/√2.
- **Coherent information.** Ic(ρ) = S(Λ(ρ)) − S(Λ^c(ρ)), S(σ) = −Tr σ log σ, and
  Q(Λ) ≥ Q^{(1)}(Λ) = max_ρ Ic(ρ) (Lloyd–Shor–Devetak; the only external input used, and it is
  used only in the last line of §8). **All logarithms below are natural**; every statement is a
  sign statement or is homogeneous of degree 1 in log, hence base-independent (bits = nats/log 2).

Verification of the Kraus data (script gate **G1**, symbolic):
Σ_a K_a Y K_a^† = (1−x) Y + (x/2)(Tr(Y)𝟙 − Yᵗ) as an identity in the nine entries of Y, and
Σ_a K_a^† K_a = (t² + 2s²)𝟙 = 𝟙 for t² = 1−x, s² = x/2. (Both from
Σ_i ε_{ijk}ε_{ilm} = δ_{jl}δ_{km} − δ_{jm}δ_{kl}.)

### 1.2 The isotropic base point

Let ψ be **any** unit vector with ψᵗψ = 0 (τ(ψ) = 0). Two elementary consequences:

1. ⟨ψ|ψ̄⟩ = Σ_j \overline{ψ_j} ψ̄_j = \overline{ψᵗψ} = 0, so ψ ⊥ ψ̄. Choose a unit e with
   {ψ, ψ̄, e} orthonormal.
2. Pᵗ = P_ψ̄ for P = |ψ⟩⟨ψ| (true for every ψ: (Pᵗ)_{jk} = ψ_k \overline{ψ_j} = (P_ψ̄)_{jk}).

Hence 𝟙 − Pᵗ = 𝟙 − P_ψ̄ = P + P_e and

> **(1.1)** Λ(P) = (1−x)P + (x/2)(𝟙 − P_ψ̄) = **(1 − x/2)·P + (x/2)·P_e**,
> so spec Λ(P) = {1 − x/2, x/2, 0} with **ker Λ(P) = span{ψ̄}** (one-dimensional).

For x ∈ (0,1) the two nonzero eigenvalues are distinct and the smallest **nonzero** eigenvalue is

> **(1.2)** g := min(x/2, 1 − x/2) = **x/2**  (since x < 1).

### 1.3 The complement at the base point, and Ic(P) = 0

Let V : ℂ³ → ℂ³ ⊗ ℂ⁴, V|v⟩ = Σ_a (K_a|v⟩) ⊗ |a⟩. Σ_a K_a^†K_a = 𝟙 makes V an isometry, and
Λ(ρ) = Tr_E(VρV^†), while
(Tr_B VρV^†)_{ab} = Σ_j (K_a ρ K_b^†)_{jj} = Tr(K_a ρ K_b^†) = Λ^c(ρ)_{ab}. So Λ^c is the
complementary channel in the §1 convention, and for a **pure** input P the two outputs
Λ(P), Λ^c(P) are the two reductions of the pure state V|ψ⟩; by the Schmidt decomposition they have
the **same nonzero spectrum**. With (1.1):

> **(1.3)** spec Λ^c(P) = {1 − x/2, x/2, 0, 0}; **dim ker Λ^c(P) = 2**; the smallest nonzero
> eigenvalue is again g = x/2; and **Ic(P) = S(Λ(P)) − S(Λ^c(P)) = 0** exactly
> (0 log 0 = 0 for the padding zeros).

Both statements in (1.3) are re-verified symbolically for the canonical ψ in gate **G3**
(`spec Λ^c(P_ψ) = {(1−x/2, 1), (0, 2), (x/2, 1)}`, and S(Λ(P)) − S(Λ^c(P)) simplifies to 0).

**Both sides now have kernels** — this is the structural reason an ε log(1/ε) *competition* is
possible on the isotropic stratum, whereas on the real stratum the E side always wins.

---

## 2. What is to be proved

Fix x ∈ (0,1) and an isotropic ψ. For a state φ on ℂ³ put ρ_ε = (1−ε)P + εφ, and define the two
**kernel weights**

> **(2.1)** w_B(ψ,φ) := ⟨ψ̄| Λ(φ) |ψ̄⟩,  w_E(ψ,φ) := Tr[ Π_E(ψ) Λ^c(φ) ],
> Π_E(ψ) = orthogonal projector onto ker Λ^c(P_ψ) (rank 2 by (1.3)).

Both are ≥ 0 (compressions of PSD operators) and ≤ 1.

**Lemma 5.1 (to be proved).** Ic(ρ_ε) = (w_B − w_E)·ε·log(1/ε) + R(ε) with an explicit bound
|R(ε)| ≤ C(x)·ε for all 0 < ε ≤ x/8, C(x) explicit and **independent of φ and of ψ**.

**Theorem 8.1 (to be proved).** For every x ∈ (0, 2/5), Q(Λ_x) ≥ Q^{(1)}(Λ_x) > 0.

§3 and §4 are the two self-contained technical ingredients; §5 assembles the Lemma; §7 computes the
witness exactly; §8 is the Theorem.

---

## 3. A self-contained degenerate-perturbation bound

Nothing in this section is quoted from the literature except the Courant–Fischer variational
principle, which is proved in one line where used. Throughout, eigenvalues of a Hermitian matrix
M ∈ M_d are listed **increasingly**: λ₁(M) ≤ … ≤ λ_d(M), and

> **(CF)** λ_k(M) = min_{dim W = k} max_{0 ≠ w ∈ W} ⟨w, M w⟩ / ⟨w, w⟩.

**Fact 3.1 (Weyl).** |λ_k(M) − λ_k(M′)| ≤ ‖M − M′‖ for Hermitian M, M′ (‖·‖ = operator norm).
*Proof.* For every unit w, ⟨w,Mw⟩ ≤ ⟨w,M′w⟩ + ‖M−M′‖; take max over w ∈ W then min over
k-dimensional W in (CF), and symmetrize. ∎

**Lemma 3.2 (multiplicative eigenvalue comparison under congruence).** Let M ∈ M_d be Hermitian and
L ∈ M_d invertible, N := L M L^†, and σ_min, σ_max the extreme singular values of L. Then for each
k there is θ_k ∈ [σ_min², σ_max²] with

> λ_k(N) = θ_k · λ_k(M).

*Proof.* Substituting v = L^{-†}w in (CF) (a bijection of k-dimensional subspaces V ↦ L^†V) and
using ⟨v, Nv⟩ = w^†L^{-1}·L M L^†·L^{-†}w = ⟨w, Mw⟩ and ⟨v,v⟩ = ‖L^{-†}w‖²,

  λ_k(N) = min_{dim W = k} max_{0≠w∈W} ⟨w,Mw⟩ / ‖L^{-†}w‖² = min_W max_w θ(w)·R(w),

where R(w) = ⟨w,Mw⟩/‖w‖² and θ(w) = ‖w‖²/‖L^{-†}w‖². The singular values of L^{-†} are the
reciprocals of those of L, so θ(w) ∈ [σ_min², σ_max²] for every w ≠ 0.

*Upper bound.* Let W\* attain λ_k(M) in (CF), so R(w) ≤ λ_k(M) for all w ∈ W\*.
If λ_k(M) ≥ 0: for w with R(w) ≥ 0, θR ≤ σ_max²R ≤ σ_max²λ_k(M); for w with R(w) < 0,
θR < 0 ≤ σ_max²λ_k(M). Hence λ_k(N) ≤ σ_max²λ_k(M).
If λ_k(M) < 0: every R(w) ≤ λ_k(M) < 0, so θR ≤ σ_min²R ≤ σ_min²λ_k(M), giving
λ_k(N) ≤ σ_min²λ_k(M).

*Lower bound.* Apply the upper bound to the pair (N, L^{-1}), using M = L^{-1}N(L^{-1})^†,
σ_max(L^{-1}) = 1/σ_min(L), σ_min(L^{-1}) = 1/σ_max(L): if λ_k(N) ≥ 0 then
λ_k(M) ≤ λ_k(N)/σ_min², i.e. λ_k(N) ≥ σ_min²λ_k(M); if λ_k(N) < 0 then λ_k(M) ≤ λ_k(N)/σ_max²,
i.e. λ_k(N) ≥ σ_max²λ_k(M).

*Assembling the four cases.* If λ_k(M) > 0 the upper bound forces λ_k(N) ≤ σ_max²λ_k(M), and
λ_k(N) < 0 is impossible (it would force λ_k(N) ≥ σ_max²λ_k(M) > 0), so λ_k(N) ≥ σ_min²λ_k(M) and
θ_k := λ_k(N)/λ_k(M) ∈ [σ_min², σ_max²]. If λ_k(M) < 0, the upper bound gives
λ_k(N) ≤ σ_min²λ_k(M) < 0 and then the lower bound gives λ_k(N) ≥ σ_max²λ_k(M); dividing by the
negative λ_k(M) again puts θ_k in the interval. If λ_k(M) = 0 both bounds force λ_k(N) = 0 and any
θ_k serves. ∎

**Proposition 3.3 (kernel-cluster bound).** Let A ∈ M_d be Hermitian with A ⪰ 0, K := ker A of
dimension m ≥ 1, and let g > 0 be the **smallest nonzero** eigenvalue of A. Let B ∈ M_d be
Hermitian with ‖B‖ ≤ b, and let μ₁ ≤ … ≤ μ_m be the eigenvalues of the compression
Π_K B Π_K restricted to K. Then for every ε with

> **(3.1)** 0 ≤ ε ≤ g/(4b),

the matrix M := A + εB satisfies

1. λ_k(M) ∈ [−εb, εb] for 1 ≤ k ≤ m, and λ_j(M) ≥ g − εb ≥ 3g/4 for j > m — i.e. the *m smallest*
   eigenvalues form the kernel cluster and are separated from the rest;
2. **|λ_k(M) − ε μ_k| ≤ (40/9)·ε²b²/g ≤ 6·ε²b²/g for 1 ≤ k ≤ m.**

*Proof.* Write ℂ^d = K ⊕ K^⊥ and, in that splitting,
M = [[εB₁₁, εB₁₂],[εB₂₁, A₂₂ + εB₂₂]], where B₁₁ = Π_K BΠ_K|_K etc., and A₂₂ = A|_{K^⊥} ⪰ g·𝟙 by
the definition of g. (There is no A₁₁ or A₁₂ block because K = ker A and A is Hermitian, so A
leaves K and K^⊥ invariant.)

**(1)** Using W = K in (CF), λ_m(M) ≤ max_{unit w ∈ K}⟨w, (A+εB)w⟩ = max_{unit w∈K} ε⟨w,Bw⟩ ≤ εb;
and λ₁(M) ≥ λ₁(A) − εb = −εb by Fact 3.1. Also λ_{m+1}(M) ≥ λ_{m+1}(A) − εb = g − εb ≥ 3g/4 by
Fact 3.1 and (3.1). Since εb ≤ g/4 < 3g/4, the ordering is as claimed.

**(2)** By (3.1), A₂₂ + εB₂₂ ⪰ (g − εb)𝟙 ⪰ (3g/4)𝟙 ≻ 0, so it is invertible with
‖(A₂₂+εB₂₂)^{-1}‖ ≤ 1/(g−εb) ≤ 4/(3g). Put

  L := [[𝟙, −εB₁₂(A₂₂+εB₂₂)^{-1}],[0, 𝟙]] = 𝟙 + E, E := [[0, −εB₁₂(A₂₂+εB₂₂)^{-1}],[0,0]].

L is unit upper triangular, hence invertible, and a direct multiplication gives the **exact** block
diagonalization

  N := L M L^† = [[S, 0],[0, A₂₂ + εB₂₂]],  S := εB₁₁ − ε²B₁₂(A₂₂+εB₂₂)^{-1}B₂₁.

*Step (a): S is close to εB₁₁.* ‖S − εB₁₁‖ ≤ ε²b²/(g − εb) ≤ (4/3)·ε²b²/g. With Fact 3.1,

  **(3.2)** |λ_k(S) − ε μ_k| ≤ (4/3)·ε²b²/g  (1 ≤ k ≤ m),

because the eigenvalues of εB₁₁ are exactly εμ_k.

*Step (b): the m smallest eigenvalues of N are those of S.* From (3.2) and (3.1),
‖S‖ ≤ εb + (4/3)ε²b²/g ≤ εb + (4/3)(g/4)(εb)/g = (4/3)εb ≤ g/3, while
λ_min(A₂₂+εB₂₂) ≥ 3g/4 > g/3. Hence λ_k(N) = λ_k(S) for k ≤ m.

*Step (c): N is a small congruence away from M.* ‖E‖ ≤ εb/(g−εb) ≤ (4/3)(εb/g) =: u, and by (3.1)
u ≤ 1/3. From LL^† = 𝟙 + E + E^† + EE^† we get σ_max(L)² = ‖LL^†‖ ≤ 1 + 2u + u² and
σ_min(L)² = λ_min(LL^†) ≥ 1 − 2u − u², so with η := 2u + u² ≤ u(2 + 1/3) = (7/3)u = (28/9)(εb/g),
Lemma 3.2 gives θ_k ∈ [1−η, 1+η] and therefore, using |λ_k(M)| ≤ εb from part (1),

  **(3.3)** |λ_k(N) − λ_k(M)| = |θ_k − 1|·|λ_k(M)| ≤ η·εb ≤ (28/9)·ε²b²/g  (k ≤ m).

Combining (3.2), step (b) and (3.3): |λ_k(M) − εμ_k| ≤ (4/3 + 28/9)ε²b²/g = (40/9)ε²b²/g. ∎

**Remark 3.4 (why the multiplicative step is necessary).** A naive bound ‖M − N‖ ≤ ‖E‖(2‖M‖+…)
is only O(ε), which would destroy the ε² accuracy: the congruence error is *proportional to the
eigenvalue it perturbs*, and the cluster eigenvalues are themselves O(ε). Lemma 3.2 is what
converts an O(ε) similarity defect into an O(ε²) eigenvalue defect. This is exactly the
"degenerate-perturbation" content and is the reason the commission asked for it to be proved
rather than cited.

**Remark 3.5 (no spectral gap is divided by inside the cluster).** Proposition 3.3 never divides by
differences of the μ_k, and never assumes the cluster slopes are distinct. This matters here because
the two E-side cluster slopes can coincide: for the witness φ = P_ψ̄ of §7 they are 4x(1−x)/(2−x)
and x/2, which are equal at x = 6/7 (from 8(1−x) = 2−x), and for general φ the coincidence set is
nonempty. Standard non-degenerate first-order perturbation theory divides by μ_j − μ_k and would be
inapplicable there; standing failure mode 7 (dividing by near-zero spectral gaps) is thereby avoided
by construction. The only gap used anywhere is g, the distance from the cluster to the *rest* of the
spectrum, and it is bounded below by x/2 uniformly in φ.

---

## 4. Uniform ε log(1/ε) entropy bookkeeping

Write h(u) := −u log u for u ≥ 0, with h(0) := 0 (continuous extension). h is concave, h(1) = 0,
h′(u) = −(1 + log u), h″(u) = −1/u.

**Lemma 4.1 (uniform cluster-term expansion).** Let λ ≥ 0, μ ≥ 0, ε ∈ (0,1], and suppose
λ = εμ + r with |r| ≤ Cε² and λ/ε ≤ U. Then

> **(4.1)** | h(λ) − εμ·log(1/ε) | ≤ (C/e + κ(U))·ε,  κ(U) := max(1/e, U log U).

*Proof.* If λ = 0 both terms are handled by 0 log 0 = 0 and the claim reads |εμ log(1/ε)| ≤ …,
which follows from εμ = |r| ≤ Cε² and ε log(1/ε) ≤ 1/e; assume λ > 0. From
log λ = log ε + log(λ/ε),

  h(λ) = −λ log λ = λ·log(1/ε) − λ·log(λ/ε),

hence h(λ) − εμ log(1/ε) = r·log(1/ε) − ε·( (λ/ε)·log(λ/ε) ).
Now |r log(1/ε)| ≤ Cε²log(1/ε) ≤ (C/e)·ε because max_{0<ε≤1} ε log(1/ε) = 1/e; and
|(λ/ε)log(λ/ε)| ≤ κ(U) because |u log u| ≤ max(1/e, U log U) on [0, U]. ∎

**Lemma 4.1 is the "ε log ε bookkeeping" of standing failure mode 8, made uniform:** the bound is
*independent of μ*, so no case split between μ = 0 and μ > 0 and no lower bound on μ is needed.
(A naive expansion −λ log λ ≈ εμ log(1/ε) − εμ log μ fails uniformly as μ ↓ 0 because log μ blows
up; the point of writing the second term as ε·(λ/ε)log(λ/ε) is that u log u stays bounded at u = 0.)

**Lemma 4.2 (regular-term stability).** Let 0 < a ≤ λ, λ′ ≤ 1 with |λ − λ′| ≤ δ. Then
|h(λ) − h(λ′)| ≤ (1 + log(1/a))·δ.
*Proof.* |h′(u)| = |1 + log u| ≤ max(1, log(1/a) − 1) ≤ 1 + log(1/a) on [a, 1]; apply the mean
value theorem. ∎

---

## 5. The expansion Lemma

**Lemma 5.1 (isotropic ε log(1/ε) expansion).** Let x ∈ (0,1), let ψ ∈ ℂ³ be any unit vector with
τ(ψ) = |ψᵗψ| = 0, P = |ψ⟩⟨ψ|, and let φ be **any** state on ℂ³. Put ρ_ε = (1−ε)P + εφ and let
w_B, w_E be as in (2.1). Then for every ε with 0 < ε ≤ x/8,

> **(5.1)** | Ic(ρ_ε) − (w_B − w_E)·ε·log(1/ε) | ≤ C(x)·ε,
>
> C(x) := 3·[ 12/(e·x) + (5/2)·log(5/2) ] + 4·[ 1 + log(8/(3x)) ] ≤ **14/x + 11 + 4·log(3/x)**.

In particular Ic(ρ_ε) = (w_B − w_E)·ε·log(1/ε) + O(ε) as ε → 0⁺, with the O(ε) constant explicit
in x and **uniform in φ and in ψ**.

*Proof.* Both outputs are affine in ε:

  Λ(ρ_ε) = A_B + ε B_B, A_B := Λ(P), B_B := Λ(φ) − Λ(P);
  Λ^c(ρ_ε) = A_E + ε B_E, A_E := Λ^c(P), B_E := Λ^c(φ) − Λ^c(P).

**Norms and gaps.** A_B, A_E ⪰ 0 with spectra (1.1), (1.3): kernel dimensions m_B = 1, m_E = 2 and
smallest nonzero eigenvalues g_B = g_E = g = x/2 by (1.2). For Hermitian differences of PSD
trace-one operators, λ_max(X − Y) ≤ λ_max(X) ≤ 1 and λ_min(X−Y) ≥ −λ_max(Y) ≥ −1, so

  **(5.2)** ‖B_B‖ ≤ 1, ‖B_E‖ ≤ 1; take b := 1.

Then the hypothesis (3.1) reads ε ≤ g/(4b) = x/8, which is exactly the assumed range, and
Proposition 3.3 applies on both sides with C_pert := 6b²/g = 12/x.

**Cluster slopes are the kernel weights.** On the B side the compression of B_B to
K_B = span{ψ̄} is the scalar ⟨ψ̄|(Λ(φ) − Λ(P))|ψ̄⟩ = ⟨ψ̄|Λ(φ)|ψ̄⟩ = w_B, because Λ(P)|ψ̄⟩ = 0 by
(1.1). So m_B = 1 and μ^B₁ = w_B. On the E side, Π_E A_E Π_E = 0 (as Π_E projects onto ker A_E),
so the compression of B_E to K_E is Π_E Λ^c(φ) Π_E, whose two eigenvalues μ^E₁, μ^E₂ ≥ 0 satisfy

  **(5.3)** μ^E₁ + μ^E₂ = Tr[Π_E Λ^c(φ) Π_E] = Tr[Π_E Λ^c(φ)] = w_E.

(The trace identity uses Π_E² = Π_E and cyclicity; it is re-verified numerically in gate **G6** for
24 random φ, to 40+ digits.)

**Cluster terms.** By Proposition 3.3(2), every cluster eigenvalue satisfies λ = εμ + r with
|r| ≤ C_pert ε², and λ ≥ 0 (both Λ(ρ_ε) and Λ^c(ρ_ε) are states), and
λ/ε ≤ μ + C_pert·ε ≤ b + C_pert·(x/8) = 1 + 3/2 = 5/2 =: U. Lemma 4.1 gives, per cluster
eigenvalue,

  **(5.4)** |h(λ) − εμ log(1/ε)| ≤ ( 12/(e x) + (5/2)log(5/2) )·ε.

There are m_B + m_E = 1 + 2 = 3 cluster eigenvalues in total.

**Regular terms.** By Proposition 3.3(1) the remaining eigenvalues satisfy λ_j(ε) ≥ g − εb ≥
3g/4 = 3x/8 and λ_j(ε) ≤ 1 (trace-one PSD), and |λ_j(ε) − λ_j(0)| ≤ εb = ε by Fact 3.1, where the
λ_j(0), j > m, are exactly the **nonzero** eigenvalues of A_B resp. A_E. Lemma 4.2 with a = 3x/8
gives, per regular eigenvalue,

  **(5.5)** |h(λ_j(ε)) − h(λ_j(0))| ≤ (1 + log(8/(3x)))·ε,

and there are (3 − 1) + (4 − 2) = 4 regular eigenvalues in total. Moreover
Σ_{j>m_B} h(λ_j(0)) = S(Λ(P)) and Σ_{j>m_E} h(λ_j(0)) = S(Λ^c(P)) because the kernel eigenvalues
contribute h(0) = 0.

**Assembly.** Summing (5.4) over the three cluster eigenvalues and (5.5) over the four regular ones,

  S(Λ(ρ_ε))  = S(Λ(P))  + w_B·ε log(1/ε) + R_B,
  S(Λ^c(ρ_ε)) = S(Λ^c(P)) + w_E·ε log(1/ε) + R_E,

where, by (5.3), the cluster slopes add up to w_B on the B side and to w_E on the E side, and
|R_B| + |R_E| ≤ 3(12/(ex) + (5/2)log(5/2))ε + 4(1 + log(8/(3x)))ε = C(x)·ε. Subtracting and using
S(Λ(P)) = S(Λ^c(P)) from (1.3) gives (5.1). The final numerical simplification uses
12/e ≤ 4.415, (5/2)log(5/2) ≤ 2.291 and log(8/(3x)) ≤ log(3/x):
C(x) ≤ 13.25/x + 6.88 + 4 + 4 log(3/x) ≤ 14/x + 11 + 4 log(3/x). ∎

**Remark 5.2 (what is uniform in what).** The constant C(x) depends on x only. It does not depend
on φ (only ‖Λ^{(c)}(φ)‖ ≤ 1 was used, i.e. that φ is a state) nor on which isotropic ψ was chosen
(only (1.1)–(1.3) were used, and those hold for *every* isotropic ψ). **Consequently this note
never needs the O(3)-orbit-transitivity statement** (R5c claim 4(iii)): the Lemma is proved
pointwise on the stratum, not transported from a representative. If φ is required only to be PSD
with Tr φ ≤ 1 the same proof applies verbatim.

**Corollary 5.3 (the (N1′-a) necessity layer).** If Q^{(1)}(Λ_x) = 0 then for every isotropic ψ and
every state φ, w_B(ψ,φ) ≤ w_E(ψ,φ).
*Proof.* If w_B > w_E, then by (5.1) Ic(ρ_ε) ≥ (w_B−w_E)ε log(1/ε) − C(x)ε > 0 as soon as
ε ≤ x/8 and log(1/ε) > C(x)/(w_B−w_E); such ε exist, so Q^{(1)} ≥ Ic(ρ_ε) > 0. ∎

This is the inequality family the node calls **(N1′-a)**; Lemma 5.1 supplies the asymptotic
statement that the node previously carried as an unproved display. It is stated here as a
consequence of the Lemma, at the same (unreviewed) status as the Lemma.

---

## 6. Numerical remark on the empty balanced layer

Corollary 5.3 is a *first-order* necessary condition; when w_B = w_E the ε log(1/ε) term cancels and
(5.1) says nothing (the balanced layer (N1′-b)). No claim about the balanced layer is made in this
note. I note only, for the reviewer's orientation and without asserting it, that the earlier
P9b/P6b finding (an isotropic weight operator that is negative semidefinite with kernel exactly
span{ψ} at x = 9/20) would make the balanced layer *trivial* at that x, and that my own §11
corroboration reproduces that operator's diagonal. Nothing in §5, §7 or §8 depends on this.

---

## 7. The witness φ = P_ψ̄: everything is exact

Take the canonical isotropic ψ = (e₁ + i e₂)/√2, ψ̄ = (e₁ − i e₂)/√2, e = e₃, and

> **φ := P_ψ̄ = |ψ̄⟩⟨ψ̄|**,  ρ_ε = (1−ε)P_ψ + ε P_ψ̄.

### 7.1 The B side is exactly diagonal

Λ has real coefficients, so Λ(Ȳ) = \overline{Λ(Y)}; applying (1.1) to the (also isotropic) ψ̄,

> **(7.1)** Λ(P_ψ̄) = (1 − x/2) P_ψ̄ + (x/2) P_{e₃}, hence
> **Λ(ρ_ε) = (1−ε)(1−x/2)·P_ψ + ε(1−x/2)·P_ψ̄ + (x/2)·P_{e₃}**,
> i.e. in the orthonormal basis (ψ, ψ̄, e₃),
> **Λ(ρ_ε) = diag( (1−ε)(1 − x/2), ε(1 − x/2), x/2 )** — exactly, for all ε ∈ [0,1].

Verified symbolically in (x, ε) as gate **G2** (`U^H Λ(ρ_ε) U == diag((1−ε)(1−x/2), ε(1−x/2), x/2)`,
with U = [ψ ψ̄ e₃] checked unitary). In particular

> **(7.2)** w_B = ⟨ψ̄|Λ(P_ψ̄)|ψ̄⟩ = **1 − x/2**.

### 7.2 The E side splits into two 2 × 2 blocks

Write s := √(x/2), t := √(1−x), st = √(x(1−x)/2). With (A_i)_{jk} = ε_{ijk} one has A_i v = v × e_i,
so for ψ = (e₁ + i e₂)/√2:

  A₁ψ = ψ × e₁ = −(i/√2) e₃,  A₂ψ = ψ × e₂ = (1/√2) e₃,  A₃ψ = ψ × e₃ = i ψ.

Hence with u_a := K_aψ: u₀ = tψ, u₁ = −i(√x/2)e₃, u₂ = (√x/2)e₃, u₃ = i sψ, and
Λ^c(P_ψ)_{ab} = ⟨u_b, u_a⟩. Since ψ ⊥ e₃, the Gram matrix is **block diagonal** with respect to the
index split {0,3} ⊔ {1,2}. Because the K_a are real, Λ^c(Ȳ) = \overline{Λ^c(Y)}, so
Λ^c(P_ψ̄) = \overline{Λ^c(P_ψ)}; the two blocks are conjugated, and therefore, exactly,

> **(7.3)** Λ^c(ρ_ε) = A(ε) ⊕ B(ε) in the split {0,3} ⊔ {1,2}, with
> A(ε) = [[ 1−x, −i·st·(1−2ε) ], [ i·st·(1−2ε), x/2 ]],
> B(ε) = (x/4)·[[ 1, −i(1−2ε) ], [ i(1−2ε), 1 ]].

Verified symbolically in (x, ε) as gate **G3**, including the vanishing of all eight cross-block
entries. Consequences, exactly:

> **(7.4)** Tr A(ε) = 1 − x/2 =: T (independent of ε), det A(ε) = 2x(1−x)·ε(1−ε) =: D;
> spec A(ε) = { (T ± √(T² − 4D))/2 }, and since A(ε) is Hermitian, T² − 4D ≥ 0 automatically;
> **spec B(ε) = { (x/2)(1−ε), (x/2)·ε }.**

At ε = 0: det A(0) = 0 and spec = {0, 1−x/2}; spec B(0) = {0, x/2} — reproducing (1.3) and
exhibiting the 2-dimensional kernel as one direction in each block.

### 7.3 The two kernel weights, computed from the definitions

Because the two nonzero eigenvalues of Λ^c(P_ψ) are 1 − x/2 and x/2, the spectral projector onto
its kernel is the Lagrange polynomial

> **(7.5)** Π_E = (Λ^c(P_ψ) − (1−x/2)𝟙)·(Λ^c(P_ψ) − (x/2)𝟙) / ( (1−x/2)·(x/2) ),

which is verified symbolically in x to be Hermitian, idempotent, of trace 2, and to annihilate
Λ^c(P_ψ) (gate **G4**). Evaluating (2.1) with (7.5) gives, symbolically in x,

> **(7.6)** w_B = 1 − x/2,  w_E = 4x(1−x)/(2−x) + x/2 = x(10 − 9x)/(2(2−x)),
>
> **(7.7)** d₁(x) := w_B − w_E = ( (2−x)² − x(10−9x) ) / (2(2−x)) = (10x² − 14x + 4)/(2(2−x))
> = **(1−x)(2−5x)/(2−x)**.

Two independent cross-checks of (7.6), both in gate **G4**:

* the ε → 0 slope of the small eigenvalue of block A, computed from the exact formula (7.4) as
  λ_−(ε) = 2D/(T + √(T²−4D)) (the form that is manifestly regular at ε = 0), equals
  **μ_A := 4x(1−x)/(2−x)**; the small eigenvalue of block B is exactly (x/2)·ε, slope
  **μ_B := x/2**; and μ_A + μ_B equals w_E of (7.6) — i.e. the definition-based Π_E computation and
  the exact two-block diagonalization agree as **formulas in x**;
* d₁(x) factors as (1−x)(2−5x)/(2−x), whose only roots in (0,1) are x = 2/5 (and x = 1 at the
  endpoint), so for x ∈ (0,1):

> **(7.8)** d₁(x) > 0 ⟺ x < 2/5;  d₁(2/5) = 0;  d₁(x) < 0 for x ∈ (2/5, 1).

**Independence statement (rule 7c/7f in spirit).** (7.6)–(7.7) were derived here from the Kraus
operators and the definitions (2.1) only, symbolically in x — a **formula-level** verification, not
a value check at sample points — before consulting any previously recorded closed form. The
agreement with the R5c-scope closed form is reported separately in §11 as corroboration.

---

## 8. Theorem: Q(Λ_x) > 0 for every x ∈ (0, 2/5)

**Theorem 8.1.** For every x ∈ (0, 2/5), Q(Λ_x) ≥ Q^{(1)}(Λ_x) ≥ Ic(ρ_ε) > 0 for every ε with

> **(8.1)** 0 < ε < ε₁(x) := min( x/8, exp( −C(x)/d₁(x) ) ),

where ρ_ε = (1−ε)P_ψ + εP_ψ̄ with ψ = (e₁ + i e₂)/√2, d₁(x) = (1−x)(2−5x)/(2−x) and
C(x) = 14/x + 11 + 4 log(3/x) as in Lemma 5.1. In particular Q(Λ_x) > 0 on (0, 2/5).

*Proof.* ψ is isotropic (ψᵗψ = (1 + i²)/2 = 0) and φ = P_ψ̄ is a state, so Lemma 5.1 applies:
for 0 < ε ≤ x/8,

  Ic(ρ_ε) ≥ (w_B − w_E)·ε·log(1/ε) − C(x)·ε = ε·[ d₁(x)·log(1/ε) − C(x) ],

using w_B − w_E = d₁(x) from (7.7). For x < 2/5 we have d₁(x) > 0 by (7.8), so the bracket is
positive exactly when log(1/ε) > C(x)/d₁(x), i.e. ε < exp(−C(x)/d₁(x)). Both conditions hold on
(8.1), so Ic(ρ_ε) > 0. Finally Q^{(1)} = max_ρ Ic(ρ) ≥ Ic(ρ_ε) and Q ≥ Q^{(1)} by the
Lloyd–Shor–Devetak theorem. ∎

**Dependence audit (as required by the commission).** Theorem 8.1 uses: §1 (conventions + Kraus),
(1.1)–(1.3) (base point), Lemma 5.1 (with its self-contained ingredients §3, §4), the value
w_B − w_E = d₁(x) established in §7.3 **by my own symbolic derivation from the definitions**, and
LSD for the last inequality. It does **not** use: the R5c-scope closed form of the full weight
operator D (§11 is corroboration only), the O(3)-orbit-transitivity claim (Remark 5.2), the
maximality of φ = P_ψ̄ among all φ, the balanced layer (N1′-b), or any P6/P6b/P9/P9b result.
The two frozen results P2/P4 (Q = P = 0 on [1/2,1)) and P3 (Q > 0 on (0, x₁)) are used **only** in
the discussion of §10 and nowhere in the proof.

**Sanity of the explicit threshold.** At x = 1/5: C = 91.8322008044…, d₁ = 4/9, so
ε₁ = e^{−206.62…} = 1.8408116…×10⁻⁹⁰. Gate **G8** evaluates Ic(ρ_ε) at ε = ε₁/2 at 400-digit
precision by two independent routes (direct Kraus assembly + numerical Hermitian eigensolver; and
the closed forms (7.1)/(7.4)) obtaining 8.4911578111…×10⁻⁸⁹ > 0 from both, agreeing to > 50
digits. The threshold (8.1) is of course wildly pessimistic (§9 shows the true crossover at
x = 1/5 is above ε = 1), but it is *explicit and verified*.

---

## 9. Sharp two-term expansion for the witness (used only to interpret the numerics)

This section is **not needed for Theorem 8.1**. It is included because it explains the sanity table
quantitatively, and because it converts §10's honesty statement into a computation.

**Proposition 9.1.** With the data of §7 (φ = P_ψ̄), set β := 1 − x/2, a := 2x(1−x),
μ_A := a/β = 4x(1−x)/(2−x), and

> **(9.1)** c₁(x) := (1 − x) − μ_A·( 1 + log(β/μ_A) ),  β/μ_A = (2−x)²/(8x(1−x)).

Then there is ε₂(x) > 0 and an explicit C₂(x) with

> **(9.2)** | Ic(ρ_ε) − d₁(x)·ε·log(1/ε) − c₁(x)·ε | ≤ C₂(x)·ε²·log(e/ε) for 0 < ε ≤ ε₂(x),
>
> ε₂(x) := min( 1/2, β²/(8a), 1/(2J) ),
> C₂(x) := 2 + 3μ_A²/β + μ_A·J·( 6 + |log μ_A| ), J := 1 + 8a/β² = 1 + 64x(1−x)/(2−x)².

*Proof.* All four eigenvalue families are exact ((7.1), (7.4)); expand each h-term.

**(i) B side.** The three eigenvalues are (1−ε)β, εβ, x/2.
The map ε ↦ h((1−ε)β) is smooth on [0,1/2] with second derivative −β/(1−ε), so Taylor with
Lagrange remainder gives h((1−ε)β) = h(β) + ε(β log β + β) + R₁, |R₁| ≤ βε²/(2(1−ε)) ≤ βε² ≤ ε².
Exactly, h(εβ) = εβ log(1/ε) − εβ log β. And h(x/2) is constant. Summing,
S(Λ(ρ_ε)) = S(Λ(P)) + βε log(1/ε) + βε + R₁ (the two ±εβ log β cancel), with |R₁| ≤ ε².

**(ii) E side, block B.** Eigenvalues (x/2)(1−ε) and (x/2)ε: identical structure with β → x/2,
contributing h(x/2) + (x/2)ε log(1/ε) + (x/2)ε + R₂, |R₂| ≤ (x/2)ε² ≤ ε².

**(iii) E side, block A.** λ_+ + λ_- = β and λ_+λ_- = D = aε(1−ε), with
λ_- = 2D/(β + √(β²−4D)). For ε ≤ ε₂ we have 4D ≤ 4aε ≤ β²/2, so with q := 4D/β² ∈ [0,1/2] and
1 − q/2 − q² ≤ √(1−q) ≤ 1 − q/2:

  λ_-/(μ_A ε) = 2(1−ε)/(1 + √(1−q)) = 1 + δ.

Indeed 1 + √(1−q) ≤ 2 − q/2 gives 1 + δ ≥ (1−ε)/(1 − q/4) ≥ 1 − ε, and
1 + √(1−q) ≥ 2 − q/2 − q² gives 1 + δ ≤ 1/(1 − (q/4 + q²/2)) ≤ 1 + q/2 + q² ≤ 1 + q (using
1/(1−u) ≤ 1 + 2u for u ≤ 1/2 and q² ≤ q/2). Hence, with q ≤ 4aε/β²,

  **|δ| ≤ ε + 2q ≤ ε·(1 + 8a/β²) = J·ε ≤ 1/2**  for ε ≤ ε₂.

Then:
* h(λ_+) = h(β − λ_-) = h(β) + (1 + log β)·μ_Aε + R₃′ + R₃, where R₃′ = (1+log β)μ_Aεδ collects the
  δ-correction of the linear term, |R₃′| ≤ (1 + log 2)·μ_A J ε² ≤ 1.7·μ_A J ε² (β ∈ (1/2,1]), and
  |R₃| ≤ λ_-²/(2(β−λ_-)) ≤ λ_-²/β ≤ 3μ_A²ε²/β (using λ_- ≤ (3/2)μ_Aε and λ_- ≤ β/2, the latter
  from ε ≤ β²/(8a));
* h(λ_-) = λ_- log(1/λ_-) = εμ_A(1+δ)·[ log(1/ε) − log μ_A − log(1+δ) ]
  = εμ_A log(1/ε) − εμ_A log μ_A + R₄, with
  |R₄| ≤ εμ_A( |δ|log(1/ε) + |δ||log μ_A| + (1+|δ|)|log(1+δ)| ) ≤ εμ_A·J·ε·( log(1/ε) + |log μ_A| + 3 ),
  using |log(1+δ)| ≤ 2|δ| for |δ| ≤ 1/2.

**(iv) Assembly.** The ε log(1/ε) coefficients are β on the B side and μ_A + x/2 on the E side; by
(7.2), (7.6) these are w_B and w_E, and their difference is d₁ — consistent with Lemma 5.1. The
ε-linear coefficients are β on the B side and (1 + log β)μ_A − μ_A log μ_A + x/2 on the E side,
whose difference is (β − x/2) − μ_A(1 + log(β/μ_A)) = (1−x) − μ_A(1 + log(β/μ_A)) = c₁(x). Summing
the remainders and using ε² ≤ ε²log(e/ε) and ε²log(1/ε) ≤ ε²log(e/ε):

  |R₁| + |R₂| + |R₃′| + |R₃| + |R₄| ≤ ε²·log(e/ε)·[ 2 + 3μ_A²/β + μ_A·J·(1.7 + 3 + |log μ_A| + 1) ]
  ≤ C₂(x)·ε²·log(e/ε),

with C₂ as displayed (the "+1" absorbs the log(1/ε) factor of R₄ into log(e/ε)). ∎

Note c₁(x) < 0 on a neighbourhood of 2/5 (numerically c₁(2/5) = −0.1726092435, c₁(0.395) =
−0.1681785575, c₁(9/20) = −0.2122444432, while c₁(1/5) = +0.1142352882). Since the crossover of
d₁ε log(1/ε) + c₁ε happens at

> **(9.3)** ε\* = exp( c₁(x)/d₁(x) ) when d₁ > 0,

and d₁(x) → 0 as x ↑ 2/5 with c₁ → −0.1726…, the true crossover ε\* collapses **doubly
exponentially** as x approaches the onset: ε\*(1/5) = 1.293 (i.e. no constraint), but
ε\*(0.395) = 1.7759×10⁻⁸ and ε\*(0.399) ≈ e^{−0.1725/0.001879} ≈ 10⁻⁴⁰. **This is the single most
important practical consequence of this note**: near the candidate onset, any numerical search for
a positive coherent information along this family must go to extreme ε (and precision), and a
search stopping at ε = 10⁻⁵ will report the wrong sign.

---

## 10. Corollary landscape — stated honestly

1. **Proved here (subject to review):** Q(Λ_x) > 0 for **all x ∈ (0, 2/5)**, by a one-line witness
   (φ = P_ψ̄ against the isotropic pure state ψ) plus Lemma 5.1. Since 2/5 > x₁ = 0.390910232076…,
   this **subsumes** the frozen P3 result "Q > 0 on (0, x₁)" and also subsumes P3's exact
   rank-two witness point x = 783/2000 = 0.3915 (which lies in (x₁, 2/5)) — a consistency check
   with the frozen inputs, not a use of them.
2. **Nothing is claimed on [2/5, 1/2).** At x = 2/5 exactly, d₁ = 0 and the mechanism gives *no*
   information (numerically Ic(ρ_ε) = c₁(2/5)·ε + o(ε) < 0 down to ε = 10⁻²⁰, i.e. this witness
   family is strictly *unhelpful* at the endpoint, so 2/5 is not covered even in the limit).
   Combined with the frozen P2/P4 theorem (Q = P = 0 on [1/2, 1)), the undetermined strip after
   this note is exactly **[2/5, 1/2)**.
3. **"x_D = 2/5 is the exact onset" remains a CONJECTURE about where THIS mechanism ends**, not a
   theorem about Q. To upgrade 2/5 to an onset one would need, at least: (a) that no other state φ
   beats P_ψ̄, i.e. max_φ (w_B − w_E) = max(d₁, 0) — this is the R5c-scope closed-form/optimality
   claim, which is under review and is **not** used or asserted here; (b) that no *non*-isotropic
   ψ (τ ≠ 0) supports an ascent for x ∈ [2/5, 1/2); (c) that the balanced layer (N1′-b) and all
   higher-order terms give nothing; and (d) the same at every blocklength n ≥ 2 (superactivation
   directions). Each is open.
4. **Direction of the necessity statement.** Corollary 5.3 is the honest reading of the node's
   (N1′-a): Q^{(1)} = 0 forces w_B ≤ w_E for all isotropic ψ and all φ. Its contrapositive is what
   Theorem 8.1 exploits. Neither statement says anything about the converse
   ("w_B ≤ w_E everywhere ⟹ Q^{(1)} = 0"), which is false in general as an implication and is
   *not* claimed.
5. **Interaction with the paper.** If R5d licenses this note, the paper's Q > 0 section can be
   shortened dramatically: the whole interval (0, 2/5) comes from one witness state and one
   expansion lemma, replacing the P3 interval-arithmetic package (which would remain as the source
   of the sharper *numerical* onset picture x_H, x₁ and of the two-letter probe). That is a
   decision-layer call, not mine.

---

## 11. Corroboration against the R5c-scope closed form (explicitly not a dependency)

The node records (under review in R5c) a weight operator D = M_B − M_E that is diagonal in
(e₃, ψ̄, ψ) with d₀ = −x(1−x)/(2−x), d₁ = (1−x)(2−5x)/(2−x), d₂ = 0. Evaluating **my own**
definition-based functional φ ↦ w_B(φ) − w_E(φ) (i.e. (2.1) with Π_E from (7.5)) at the three
projectors gives, symbolically in x (gate **G7**):

| φ | my w_B − w_E | recorded value | agree |
|---|---|---|---|
| P_{e₃} | −x(1−x)/(2−x) | d₀ = −x(1−x)/(2−x) | yes |
| P_ψ̄ | (1−x)(2−5x)/(2−x) | d₁ = (1−x)(2−5x)/(2−x) | yes |
| P_ψ | 0 | d₂ = 0 | yes |

and at x = 9/20 the triple is (−99/620, −11/124, 0), matching the P9b datum
`diag(−99/620, −11/124, 0)` on the node. This is a **formula-level** agreement (identity in x, not
a value check), obtained without reading the prior scripts or reports. It corroborates the R5c
package but is not used by Lemma 5.1 or Theorem 8.1: those need only the single value
w_B(P_ψ̄) − w_E(P_ψ̄), derived in §7.3. As commissioned, the R5c closed form is cited here as an
**input under review**; its verdict does not affect the validity of §5 or §8, only the *optimality*
discussion in §10 item 3(a).

---

## 12. Numerical sanity table and gate log

Script: **`tools/whgap_n1p_sanity.py`** (mine; 75 boolean gates, **all PASS**).
Command: `C:<home>/cpython3119/python.exe tools/whgap_n1p_sanity.py`
Logs: `artifacts/logs_whgap_r5_20260729/n1p_sanity.json`, `…/n1p_sanity.log`.
Precision: mpmath `mp.dps = 60` throughout, raised to 400 for gate G8's certificate point.

### 12.1 The commissioned table (φ = P_ψ̄; Ic in **nats**)

`Ic` is computed **numerically from the Kraus operators only** (assemble ρ_ε, apply Λ and Λ^c,
Hermitian eigensolver, −Σλ log λ); "prediction" is d₁·ε·log(1/ε) + c₁·ε from (7.7) and (9.1).
`ε = 10⁻³, 10⁻⁴, 10⁻⁵` are the commissioned values; the smaller ones were added to exhibit the
crossover of §9.

| x | ε | Ic(ρ_ε) [nats] | two-term prediction | sign |
|---|---|---|---|---|
| 1/5 | 1e-3 | 0.003185705707 | 0.003184348746 | + |
| 1/5 | 1e-4 | 4.207905017e-4 | 4.207719898e-4 | + |
| 1/5 | 1e-5 | 5.231114514e-5 | 5.231091050e-5 | + |
| 1/5 | 1e-8 | 8.301204546e-8 | 8.301204508e-8 | + |
| 1/5 | 1e-12 | 1.239468912e-11 | 1.239468912e-11 | + |
| 1/5 | 1e-20 | 2.058165834e-19 | 2.058165834e-19 | + |
| 79/200 = 0.395 | 1e-3 | −1.020554925e-4 | −1.030821098e-4 | **−** |
| 79/200 = 0.395 | 1e-4 | −8.124540181e-6 | −8.138329388e-6 | **−** |
| 79/200 = 0.395 | 1e-5 | −5.966715449e-7 | −5.968447797e-7 | **−** |
| 79/200 = 0.395 | 1e-8 | +5.411997684e-11 | +5.411969753e-11 | **+** |
| 79/200 = 0.395 | 1e-9 | +2.711078881e-11 | +2.711078566e-11 | + |
| 79/200 = 0.395 | 1e-12 | +9.220723339e-14 | +9.220723338e-14 | + |
| 79/200 = 0.395 | 1e-20 | +2.657977606e-21 | +2.657977606e-21 | + |
| 2/5 | 1e-3 | −1.716034443e-4 | −1.726092435e-4 | − |
| 2/5 | 1e-5 | −1.725922923e-6 | −1.726092435e-6 | − |
| 2/5 | 1e-20 | −1.726092435e-21 | −1.726092435e-21 | − |
| 9/20 | 1e-3 | −8.242421565e-4 | −8.250291857e-4 | − |
| 9/20 | 1e-4 | −1.029186305e-4 | −1.029290767e-4 | − |
| 9/20 | 1e-5 | −1.233539316e-5 | −1.233552347e-5 | − |
| 9/20 | 1e-12 | −2.663383413e-12 | −2.663383413e-12 | − |
| 9/20 | 1e-20 | −4.297476060e-20 | −4.297476060e-20 | − |

(The full 28-row table, including all ε ∈ {1e-3, 1e-4, 1e-5, 1e-8, 1e-9, 1e-12, 1e-20} at all four
x values, is in `n1p_sanity.json`, gate `G5.table`, with S_B and S_E printed separately.)

**Honest reading of the table — the commission's expected sign pattern is not what happens at the
commissioned ε.** The commission anticipated (+, +, − or ≈0) at x = (1/5, 0.395, 9/20) for
ε ∈ {10⁻³,10⁻⁵}. What is observed: **x = 1/5 is (+) as expected; x = 9/20 is (−) as expected; but
x = 0.395 is (−) at all three commissioned ε and only turns (+) at ε ≲ 1.8×10⁻⁸.** This is not a
contradiction with Theorem 8.1 — it is exactly (9.3): at x = 0.395 the positive term
d₁ε log(1/ε) = 0.00942·ε·log(1/ε) only overtakes the negative term c₁ε = −0.1682·ε when
log(1/ε) > 17.85. The predicted crossover ε\* = 1.7759×10⁻⁸ brackets the observed flip between
ε = 10⁻⁵ (−) and ε = 10⁻⁸ (+). The table therefore **confirms** the analysis in a stronger sense
than the anticipated pattern would have.

**Slope check against d₁.** The residual |Ic − (d₁ε log(1/ε) + c₁ε)| divided by ε falls by a factor
≈ 10 for each factor 10 in ε at every x tested (e.g. at x = 1/5: 1.357e-3, 1.851e-4, 2.346e-5,
3.832e-8, 5.813e-12, 9.775e-20 for ε = 1e-3 … 1e-20; gate `G5.remainder_quality`, monotone
decreasing at all four x). That is the O(ε²log(1/ε)) remainder of Proposition 9.1 — i.e. the
numerics test the **two-term** expansion, hence a fortiori the ε log(1/ε) slope d₁.

### 12.2 Gate summary

| gate | content | result |
|---|---|---|
| G1 | Kraus set reproduces Λ_x entrywise (symbolic in 9 entries of Y); Σ K_a^†K_a = 𝟙; τ(ψ)=0; ⟨ψ\|ψ̄⟩=0; Pᵗ = P_ψ̄ | PASS |
| G2 | (ψ,ψ̄,e₃) orthonormal; **Λ(ρ_ε) = diag((1−ε)(1−x/2), ε(1−x/2), x/2)** exactly, symbolic in (x,ε); spec Λ(P) = {1−x/2, x/2, 0} | PASS |
| G3 | Λ^c(ρ_ε) block diagonal (8 cross entries vanish); blocks equal (7.3); Tr A = 1−x/2; det A = 2x(1−x)ε(1−ε); spec B = {xε/2, x(1−ε)/2}; spec Λ^c(P) = {1−x/2, x/2, 0, 0}; S(Λ(P)) = S(Λ^c(P)) | PASS |
| G4 | Π_E of (7.5) Hermitian/idempotent/trace 2/annihilating; w_B = 1−x/2; w_E = 4x(1−x)/(2−x) + x/2; **w_B − w_E = (1−x)(2−5x)/(2−x)**; exact-block slopes agree with w_E; d₁ roots = {2/5, 1} | PASS |
| G5 | 28-row Ic table + prediction + residual monotonicity + sign summary | PASS |
| G6 | Proposition 3.3 stress: 24 instances (x ∈ {1/5, 9/20}, 6 random complex φ each, ε ∈ {1e-3,1e-5}); \|λ_k − εμ_k\| ≤ 6ε²b²/g in all; worst dev/bound = 2.30e-2; Tr[Π_EΛ^c(φ)] = Σμ_k to 40+ digits in all | PASS |
| G7 | corroboration of the recorded weight-operator diagonal (§11) | PASS |
| G8 | \|Ic − d₁ε log(1/ε)\| ≤ C(x)·ε at all 16 tested (x,ε) with ε ≤ x/8; certificate point at x = 1/5, ε = ε₁/2 = 9.204058e-91 gives Ic = 8.4911578111e-89 > 0 by two independent routes agreeing to >50 digits (dps 400) | PASS |

**Failure mode 1 was hit and fixed, and the reviewer should note it.** Declaring only
`x = Symbol('x', positive=True)` leaves sympy unable to decide `1 − x > 0` and `2 − x > 0`, so three
checks initially failed spuriously: `conjugate(sqrt(1−x))` survived in `Π_E − Π_E^†`, and
`sqrt((x−2)²)` printed as `Abs(x−2)` in the block-A slope. Fixes, both recorded in the script:
(a) all Kraus algebra is carried in **real positive symbols** s, t with s² = x/2, t² = 1−x, so no
`.H` ever meets a symbolic square root; (b) zero-testing of the remaining expressions uses the
manifestly-positive chart **x = 1/(1+y), y > 0** (helper `zero_expr`), which supplies sympy the
missing facts. A third initially-failing check (`2D/(T+√(T²−4D)) = (T−√(T²−4D))/2`) was replaced by
the equivalent polynomial identity (T−√)(T+√) = 4D plus the positivity T + √(T²−4D) ≥ T > 0.
This is a *tooling* fix, not a mathematical change; nothing in §3–§9 depends on the chart.

### 12.3 Provenance hashes (SHA-256)

```
0ae9238490a4d6b2cc8da45c83918db409b74afe13b04df7b7a6148b98f4832e  tools/whgap_n1p_sanity.py
7feb6bf45fb1f1e5c2c23f8d0ee17a511f22bbcda1a12f58f7958f45317958e5  artifacts/logs_whgap_r5_20260729/n1p_sanity.json
8f4e856e0384536f81ff30015b1a0c456d65a55dc85a0f8342ad59258a372467  artifacts/logs_whgap_r5_20260729/n1p_sanity.log
```

Also archived as `artifacts/logs_whgap_r5_20260729/SHA256SUMS_n1p.txt` (LF line endings; see the
PRE-ACTION REPORT for why the name is suffixed).

---

## 13. Status suggestions for the decision layer and for R5d (capped, per the commission)

I write no status. My suggestions, all at **CONJECTURED / pending-review** until a fresh rule-7
review completes (rule 6):

1. **Lemma 5.1 + Corollary 5.3 + Theorem 8.1** — suggested tier if R5d licenses: the Lemma and the
   Theorem are candidates for PROVED (they are self-contained: §3, §4 prove their own perturbation
   and entropy bounds, and §7.3 derives the one numerical input the Theorem needs). Until then:
   **CONJECTURED with `pending-review:`** on `WHGAP.no-ascent-hierarchy`.
2. **The computational package** (`tools/whgap_n1p_sanity.py` + the two logs, 75 gates PASS) is
   proposer-writable evidence at **NUMERICAL** with a `pending-review:` marker, citing the command,
   log paths and the SHA-256 values of §12.3.
3. **Do not** let this note move `WHGAP.qpositive-onset` (P3): if Theorem 8.1 survives review it
   *subsumes* P3's interval, but P3's own status is a separate, already-reviewed record; the
   subsumption is a decision-layer bookkeeping matter.
4. **A new node is owed** (rule 8b) for the object this note isolates but does not settle:
   *"the isotropic first-order mechanism terminates exactly at x_D = 2/5"* — i.e. the conjunction
   of items 3(a)–(d) of §10. It should be registered OPEN/CONJECTURED with the four named
   obligations, so that "2/5" is never read off this note as an onset. The decision layer owns that
   write (single-writer deviation).
5. **Suggested R5d attention points**, in decreasing order of how much I would distrust myself:
   (i) Lemma 3.2's four-case assembly and the claim that the congruence error is *multiplicative*
   (Remark 3.4) — if that step is wrong, the ε² accuracy collapses to ε and Lemma 5.1 fails;
   (ii) the counting of cluster vs regular eigenvalues in the assembly of Lemma 5.1 (3 and 4
   respectively) and the claim Σ cluster slopes = w_E, which uses Π_E A_E Π_E = 0;
   (iii) whether ‖B‖ ≤ 1 in (5.2) is right (it uses that both Λ^{(c)}(φ) and Λ^{(c)}(P) are PSD
   with trace 1 — note Λ^c(P) has trace 1 as a 4×4 matrix, and the padding zeros are harmless);
   (iv) Lemma 4.1's uniformity in μ (the whole reason no case split is needed);
   (v) my symbolic Π_E via the Lagrange polynomial (7.5) — an independent construction of the
   kernel projector (e.g. explicit kernel vectors k_A ∝ (i·st, 1−x), k_B ∝ (1, −i)/√2 in the two
   blocks) should reproduce w_E = 4x(1−x)/(2−x) + x/2;
   (vi) the arithmetic of (7.7): (2−x)² − x(10−9x) = 4 − 14x + 10x² = 2(5x² − 7x + 2) =
   2(1−x)(2−5x), so d₁ = 2(1−x)(2−5x)/(2(2−x)) = (1−x)(2−5x)/(2−x) — worth re-checking by hand at
   two rational x (x = 1/5 gives d₁ = 4/9; x = 9/20 gives d₁ = −11/124).

