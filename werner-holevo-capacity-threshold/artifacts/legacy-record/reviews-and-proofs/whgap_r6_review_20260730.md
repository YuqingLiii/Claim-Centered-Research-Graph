# WHGAP R6 — fresh independent review of the P13-A stratum-exhaustion note

**Reviewed artifact:** [`channel-capacity/werner-holevo-gap/notes/WHGAP_P13A_STRATUM_EXHAUSTION_20260730.md`](../channel-capacity/werner-holevo-gap/notes/WHGAP_P13A_STRATUM_EXHAUSTION_20260730.md)
(executor authorship, 2026-07-30) plus its computational package
`tools/whgap_p13a_sanity.py` and `artifacts/logs_whgap_p13a_20260730/`.
**Commission:** [`WHGAP_COMMISSION_P13A_20260730.md`](../channel-capacity/werner-holevo-gap/notes/WHGAP_COMMISSION_P13A_20260730.md) §R6;
inherited frozen conventions / standing failure modes / rule-7 embeds are §1–§3 of
[`WHGAP_REVIEW_COMMISSION_R5_20260729.md`](../channel-capacity/werner-holevo-gap/notes/WHGAP_REVIEW_COMMISSION_R5_20260729.md).
**Node:** `WHGAP.onset-two-fifths` (P13). **Reviewer:** fresh Opus instance, 2026-07-30.
**Interpreter:** `C:<home>/cpython3119/python.exe` (sympy 1.13.1, mpmath 1.3.0).
**Reviewer scripts:** `tools/whgap_r6_symbolic.py` (38/38 gates PASS),
`tools/whgap_r6_numeric.py` (21/21 gates PASS).
**Reviewer logs:** `artifacts/logs_whgap_p13a_20260730/r6_symbolic.{json,log}`,
`…/r6_numeric.{json,log}`, hashes in `…/SHA256SUMS_r6.txt` (LF; `sha256sum -c` = 6 × OK).

**VERDICT: LICENSE A**, at the exact scope written in §9 below, with **0 MAJOR** and **5 minor**
items. Every load-bearing claim of the note (G0–G4) was re-derived by a route different from the
executor's and independently confirmed; the two commissioned reproductions (G5(ii), G5(iv)) were
reproduced with my own code, my own seeds and my own grid at more than the required number of
parameter points.

---

## 0. PRE-ACTION REPORT (mandatory, `research/PRETASK_RELOAD_PROMPT.md`)

Files read from disk, completely, in the prescribed order, before any mathematics:
`research/DAG_PROTOCOL.md` (whole file: §1 data structure, §2 ladder + completion gate, §3 rules
1–8, §4 READ, §5 WRITE, §6 session-close); `research/RESEARCH_STRUCTURE_PROTOCOL.md` (§1–§10);
`channel-capacity/werner-holevo-gap/README.md`;
`channel-capacity/werner-holevo-gap/notes/WERNER-HOLEVO-GAP_PROOF_DAG.md` (header, eight inlined
rules, mermaid, outline); `channel-capacity/werner-holevo-gap/proof-dag/NODE_INDEX.md`; the target
node `proof-dag/nodes/WHGAP.onset-two-fifths.md` and its parent `proof-dag/nodes/WHGAP.goal.md`
(the node has no children); then the commission `notes/WHGAP_COMMISSION_P13A_20260730.md`, §1–§3 of
`notes/WHGAP_REVIEW_COMMISSION_R5_20260729.md`, the reviewed note, and the frozen input
`notes/WHGAP_N1PRIME_EXPANSION_LEMMA_20260729.md` §3–§5, §7.3 (Fact 3.1, Lemma 3.2,
Proposition 3.3, Lemmas 4.1/4.2, the isotropic weights).

- **Target node and status as read from disk:** `WHGAP.onset-two-fifths` (alias P13), kind LEAF,
  role proof, **status CONJECTURED**, `disposition: null`, parents `["WHGAP.goal"]`, children `[]`,
  `Adversarial reviews: None yet.` Open obligations on the node: (b) non-isotropic strata,
  (c) balanced/higher-order layers at and above 2/5, (d) every blocklength n ≥ 2.
- **My ROLE: reviewer. Independence statement:** I authored none of the reviewed work — not the
  note, not `tools/whgap_p13a_sanity.py`, not any prior WHGAP artifact — and I was given **no
  desired outcome**; the commission's menu presents (A) and (B) as alternatives and I was told to
  pick whichever the evidence supports.
- **Highest status my evidence could license per §2:** a completed rule-7 review by a fresh
  independent instance opens the **PROVED** tier for the reviewed statements, at the scope this
  report states, and the writer is the decision layer (single-writer deviation), citing this
  artifact. I write **no status** and I edited **no** node file, `NODE_INDEX.md`, or DAG doc.
- **Gates and deliverables of my commission, one line each:** re-derive the **G0** normal form;
  re-derive the **G1** determinant **by my own route** (direct 3×3 determinant / eigenvalue
  product, not the executor's 2×2 block reduction); audit the **G2** assembly and remainder line by
  line; characterise the **G3** kernel independently **with my own parameterisation of k**; audit
  the **G4** exception handling; reproduce **G5(ii)** and **G5(iv)** with my own script at ≥ 2
  parameter points each; c ≥ 2 identity gates, anchoring ban, value-vs-formula statements
  throughout; write `artifacts/whgap_r6_review_20260730.md` and pick from the R6 menu.
- **Conflicts between commission text and disk protocols: two, reported not silently resolved.**
  1. *Single-writer deviation.* The commission forbids agents to touch node files, `NODE_INDEX.md`
     or the DAG doc, while `DAG_PROTOCOL.md` §5/§6 and rule 8c require the outcome to be appended
     to the node in the same session. The commission states the deviation is commissioned by the
     decision layer, which will perform the atomic update citing this artifact. I comply and record
     the obligation: **this report and `artifacts/logs_whgap_p13a_20260730/r6_*` are not yet linked
     from `WHGAP.onset-two-fifths`; the decision layer owes that link (rule 8c), together with the
     executor's note, script and logs, which are likewise still unlinked.**
  2. *Licensing-statement scope.* Menu item (A) ends "P13 obligations (b) and first-order (c) are
     CLOSED". Node obligation (b) as written on disk reads "no tau ≠ 0 pure psi supports **any**
     ascent for x in [2/5, 1/2)". The note proves the **first-order (ε log(1/ε)) layer only**, and
     both the note (§9.6) and my own probe exhibit Ic > 0 at moderate ε from τ > 0 pure base points
     (at x = 1/5). I therefore license (A) with obligation (b) marked **closed at the first-order
     layer**, not in its literal "any ascent" reading — see §9 and minor **m1**.

---

## 1. Anchoring discipline (7c) — stated honestly

The dispatch required me to open the reviewed note as part of the mandatory reload, so I cannot
claim to have read the claim without the proof. What I did instead, and what the reader should
weigh:

* Every derivation in §§3–7 below was carried out **in my own script, in my own coordinates**,
  before I opened `tools/whgap_p13a_sanity.py` at all. I opened the executor's script only after my
  own 38 + 21 gates had passed, and then only to audit provenance (that its `Ic` is built from the
  Kraus operators, and that the note's tables match its JSON).
* My routes are deliberately **different**, as the commission requires:
  - **G1** — a direct 3 × 3 characteristic polynomial of `Λ_x(ψψ†)` for an **arbitrary**
    (unnormalised, 6 free real parameters) complex ψ, in a homogeneous chart with no normal form
    and no `span{ψ, ψ̄}` block reduction, plus an independent determinant (eigenvalue-product) gate.
  - **G3** — the kernel **found** by sympy `nullspace()` on the 4 × 4 `Λ^c(ψψ†)` at three
    independent generic exact ψ, and separately pinned by an exact rank count from the charpoly; the
    rank of `K(k)` established twice: by the 2 × 2 minors (`σ²ψ_j²`, no case split at all) and by
    the exact spectrum of `K†K`.
  - **G5** — my own seed (`Random(6060606)`), my own ε ladder, my own 16 × 16 grid at
    `x = a/17, α = (π/4)·b/17`, disjoint from the executor's 20 × 20 grid at denominators 21.
* Where my derivation coincides notationally with the executor's, I say so (§3, §5): the
  coincidences are of *results*, reached by different computations.
* I did **not** re-run `tools/whgap_p13a_sanity.py`. Reproducing an author's script is not
  verification (standing failure mode 9).

---

## 2. Type audit (7a)

Every displayed object in the reviewed claims, with domain/codomain/dimension as a function of all
parameters. All of it checks out; the note's own §1.1 table is correct and complete.

| object | type | dimension | parameter dependence |
|---|---|---|---|
| `Λ_x` | CPTP map | M₃(ℂ) → M₃(ℂ) | x ∈ (0,1) |
| `Λ_x^c` | CPTP map, **padded** | M₃(ℂ) → M₄(ℂ) | x; output rank ≤ 3 always |
| `K_0 = t·1, K_i = σA_i` | real 3 × 3 matrices | 4 of them | t = √(1−x), σ = √(x/2) |
| `ψ` | unit ket | ℂ³ | τ(ψ) = \|ψᵗψ\| ∈ [0,1] |
| `P = P_ψ`, `φ`, `ρ_ε` | states | 3 × 3, PSD, trace 1 | — |
| `Λ(ρ_ε)` / `Λ^c(ρ_ε)` | states | 3 × 3 / 4 × 4 | affine in ε |
| `k(ψ)` | unit vector spanning ker Λ^c(P) | **ℂ⁴** (not ℂ³) | defined only where dim ker = 1, i.e. τ > 0 |
| `K(k) = Σ_a k̄_a K_a` | a **single matrix**, not a channel | 3 × 3 | linear in k̄ |
| `Π_E = \|k⟩⟨k\|` | projector | 4 × 4, rank **1** (rank 2 at τ = 0) | the dimension jump is the whole point |
| `w_E`, `g`, `C(x,τ)`, `μ_±` | real scalars | — | `C` depends on (x,τ) only, **not** on φ |
| `V = 1 ⊕ det(O)·O` | real orthogonal | 4 × 4 | O ∈ O(3) |
| `Ic` | real scalar | — | **nats** throughout (note and both scripts) |

Three type-level points I checked specifically, because they are where this kind of argument breaks:

1. **`†` = `ᵗ` is used only for the real Kraus operators** (note §1.1, failure mode 4). I verified
   `Σ_a K_a Y K_aᵀ = Λ_x(Y)` on all nine entries of a symbolic Y and `Σ_a K_aᵀK_a = 1`
   (`A0.kraus_reproduce_Lambda`, `A0.kraus_TP`), and separately rebuilt both marginals from the
   Stinespring isometry `M[j,a] = (K_aψ)_j`, `Λ(P) = MM†`, `Λ^c(P)_{ab} = ⟨K_bψ|K_aψ⟩`, agreeing
   with the frozen definitions to < 1e-45 at 6 random pure states and 2 values of x
   (`B0.stinespring_conventions`) — failure mode 3 screened by construction, not by inspection.
2. **`k ∈ ℂ⁴` while `K(k) ∈ M₃`**: the index a runs over the environment, and the note's
   `k₀ = 0` conclusion is what removes the identity-Kraus part from `K(k)`. Confirmed symbolically.
3. **The commission's own G1 phrasing is ill-typed at τ = 1**, exactly as the note reports in its
   §0 conflict 3: `span{ψ, ψ̄}` is one-dimensional when ψ is real up to phase, so "the 2 × 2 block"
   does not exist there. The note's repair — stating Proposition 3.2 in characteristic-polynomial
   form — is correct and uniform on τ ∈ (0,1]; my own route never needs the case split at all
   (`A1.charpoly_direct_arbitrary_psi` holds for **every** complex ψ, including ψ real and ψ
   isotropic).

---

## 3. G0 — the normal form and the transport (note §2, §1.4): **CONFIRMED**

Proposition 2.1 is correct. The proof is the standard one and I reproduce it: with ψ = a + ib,
ψᵗψ = (a·a − b·b) + 2i(a·b) (gate `A6.z_real_parts`), a global phase acts by
ψᵗψ ↦ e^{2iθ}ψᵗψ (`A6.phase_action_on_z`), so θ can be chosen to make ψᵗψ = τ ≥ 0, i.e. a ⊥ b and
a·a − b·b = τ with a·a + b·b = 1. For τ < 1 both a, b ≠ 0 and (â, b̂, â × b̂) is **right-handed**,
so the aligning O is in SO(3) — the note is right to make the handedness explicit, since an O(3)
element with det = −1 would not preserve the E-side transport form. τ = 1 is the degenerate branch
and is handled. τ(ψ_α) = cos 2α and ‖ψ_α‖ = 1 verified symbolically (`A6.normal_form_*`).

Lemma 1.1 (transport) is correct. I re-derived `OᵀA_iO = det(O)·Σ_j O_{ij}A_j` and verified it at
four test O — two with det = +1 (a symbolic rotation about z, one about x) and **two with
det = −1** (the reflection diag(1,1,−1) and the transposition swap₁₂), which is where the det
factor is load-bearing (`A5.transport_*`). I additionally verified the map-level statements
`Λ_x(OYOᵀ) = OΛ_x(Y)Oᵀ` and `Λ^c(OYOᵀ) = VΛ^c(Y)Vᵀ` with `V = 1 ⊕ det(O)O` **at the reflection**,
symbolically in a general Y, plus `VVᵀ = 1` (`A5.LambdaC_transport_reflection`, `A5.V_orthogonal`).

**Reviewer note (a strength of the note, worth preserving in any write-up):** the note's §2 is
explicit that **nothing in §3–§6 load-bears the transport** — §3, §5 and §6 are proved for
arbitrary ψ and the normal form is used only to express the answer in (x, α) coordinates. My own
gates are all arbitrary-ψ, which corroborates that claim structurally: I never used Proposition 2.1
to prove anything.

---

## 4. G1 — the exact spectrum (note §3): **CONFIRMED by my own route, with the same values**

My route: no block reduction. For an arbitrary unnormalised complex ψ (6 free real symbols), with
N = ⟨ψ|ψ⟩ and z = ψᵗψ, the **direct 3 × 3 Berkowitz characteristic polynomial** of
`Λ_x(ψψ†)` factors exactly as

> det(λ1 − Λ_x(ψψ†)) = (λ − Nx/2)·(λ² − N(1 − x/2)λ + x(1−x)|z|²/2)   (gate `A1.charpoly_direct_arbitrary_psi`)

which, dividing by N (i.e. for unit ψ, |z| = τ), is precisely the commissioned
**trace = 1 − x/2, det = x(1−x)τ²/2**, third eigenvalue **x/2**. I checked the determinant a second
time on its own (`A1.det_eigenvalue_product`: det Λ_x(ψψ†) = (Nx/2)·x(1−x)|z|²/2) and the trace via
trace preservation (`A1.trace_TP`).

This is the item the note itself flagged as the one where an algebraic slip is most plausible
(§11(i): "the a(p+q) term is exactly the term an algebraic slip drops"). **It does not drop:** my
computation never forms a(p+q) at all, and lands on the same determinant. The two τ-specialisations
the note offers as sanity anchors are also correct: τ = 0 ⟹ det = 0 (consistent with the reviewed
isotropic spectrum {1−x/2, x/2, 0}) and τ = 1 ⟹ det = x(1−x)/2 with spectrum {1−x, x/2, x/2}.

Everything downstream in §3 checks:

* discriminant: T² − 4D is affine and decreasing in τ² and equals (1 − 3x/2)² at τ² = 1, hence
  ≥ 0 on τ² ∈ [0,1] — so μ_± are real for **every** stratum (`A1.discriminant_identity`);
* ordering: the quadratic at λ = x/2 equals (x/2)(1−x)(τ² − 1) ≤ 0, so **μ₋ ≤ x/2 ≤ μ₊**
  (`A1.root_ordering`); with μ₊ + μ₋ = T > 0 this gives μ₋ > 0 ⟺ D > 0 ⟺ τ > 0, i.e. the
  commissioned full-rank criterion;
* the numerically stable form and the gap bound used later:
  μ₋ = 2D/(T + √(T²−4D)) and **g = μ₋ ≥ D/T = x(1−x)τ²/(2−x)** (`A1.mu_minus_stable_form`,
  `A1.gap_lower_bound`). *(The note's (3.6) states exactly this; I initially mis-set my own gate to
  2D/T and it failed — the error was mine, the note's constant is the correct one.)*
* the E side: det(λ1 − Λ^c(ψψ†)) = λ · [the 3 × 3 charpoly] symbolically for arbitrary ψ
  (`A2.charpoly_LcP`), which simultaneously gives isospectrality, Ic(P) = 0, **rank Λ^c(P) = 3** and
  **dim ker Λ^c(P) = 1** for τ > 0 — the note's §3.3. Numerically, Ic(P_ψ) = 0 to < 1e-40 at 6
  random pure inputs (`B0.Ic_zero_at_pure`), and the numeric second-smallest eigenvalue of Λ^c(P)
  matches μ₋ to relative 1e-60 at all three commissioned points (`B.gap_closed_form[...]`).

**Value-vs-formula (7f):** all of §4 is **formula-level** — identities in x and in an arbitrary
complex ψ, symbolically, not value checks at sample points.

---

## 5. G3 — the kernel and the exceptional set (note §4, §6): **CONFIRMED, E = ∅**

I did not start from the note's guess `k = (0, ψ̄)`. My route:

1. **Found** the kernel: sympy `nullspace()` of the 4 × 4 `Λ^c(ψψ†)` at three independent generic
   exact ψ — (1, 2i, 1/3), (2/5 + i, −1/2, 3 − 2i), (1, 1 + i, 2 − i/7) — returned in each case a
   **one-dimensional** space, proportional to (0, conj ψ) (`A2.kernel_found_by_nullspace`).
2. **Pinned** it for all ψ: `Λ^c(ψψ†)·(0, conj ψ) = 0` symbolically for arbitrary complex ψ
   (`A2.k_annihilates`) together with the exact rank-3 count of item §4 ⟹ the kernel is
   *exactly* span{(0, ψ̄)} whenever τ > 0. (Note that (0, ψ̄) lies in the kernel at **every** τ,
   including τ = 0; what τ > 0 buys is that there is nothing else.)
3. Consequently `K(k) = Σ_a k̄_aK_a = σ Σ_i ψ_iA_i = −σ[ψ]_×` (`A3.Kk_is_minus_sigma_cross`), purely
   skew with **no identity part** because k₀ = 0, and `K(k)ψ = 0` identically (`A3.Kk_kills_psi`).
4. **Rank, twice, by routes that do not depend on each other:**
   - the three principal 2 × 2 minors of K(k) are σ²ψ₃², σ²ψ₂², σ²ψ₁² (`A3.minor_route_rank_two`).
     They cannot all vanish for ψ ≠ 0, so **rank K(k) ≥ 2 for every nonzero ψ, with no case split
     whatever** — this is a strictly cleaner argument than the note's Lemma 6.1(ii), which splits on
     w·w ≠ 0 (diagonalisable) versus w·w = 0 (Jordan J₃);
   - `K†K = (x/2)(N·1 − ψψ†)` with characteristic polynomial λ(λ − (x/2)N)² symbolically
     (`A3.KdagK_closed_form`, `A3.KdagK_spectrum`): exactly **one** zero eigenvalue, so
     rank K(k) = 2 and **dim ker K(k) = 1 < 2** at every (x, ψ) with ψ ≠ 0.
5. The note's Lemma 6.1 is nonetheless correct as stated, and I checked its delicate branch
   explicitly: `[w]_×² = wwᵗ − (w·w)1` symbolically (`A3.S_squared`), and for the isotropic-bilinear
   witness w = (1, i, 0) — where w·w = 0 — `[w]_×` is nilpotent of index exactly 3 with
   `[w]_×² = wwᵗ ≠ 0` and **rank 2** (`A3.nilpotent_case_rank`). This is the note's §11(iii)
   attention point and it survives: the rank does **not** drop on the complex-isotropic locus, so
   there is no exceptional stratum accumulating at τ → 0.
6. Hence `w_E = Tr[φ K†K] = (x/2)(Tr φ − ⟨ψ|φ|ψ⟩)`, verified against a **general Hermitian φ with
   nine free real parameters** and arbitrary ψ (`A4.wE_closed_form_general_hermitian`,
   `A4.wE_equals_Tr_phi_KdK`) — formula level in x, ψ and φ simultaneously. For a state,
   w_E = (x/2)(1 − ⟨ψ|φ|ψ⟩) ∈ [0, x/2], and **w_E = 0 ⟺ ⟨ψ|φ|ψ⟩ = 1 ⟺ φ = P_ψ**.

**Conclusion: the commissioned exceptional set E = {(x,α) : dim ker K(k) ≥ 2, τ > 0} is EMPTY**, and
the kernel-avoiding set of states is exactly {P_ψ}. Numerically, on my own 16 × 16 grid (256 points,
all τ > 0, denominators coprime to the executor's): rank histogram **{2 : 256}**, largest
"zero" eigenvalue of K†K = 5.7e-42, smallest nonzero = 0.0294 (a clean gap, so the rank verdict is
not a near-degeneracy), max deviation of K†K from (x/2)(1 − P) = 2.3e-41, and the smallest nonzero
eigenvalue of Λ^c(P) over the grid = 2.4e-4 > 0 so dim ker Λ^c(P) = 1 throughout
(`Biv.*`). At the three commissioned points the eigensolver's kernel vector equals (0, ψ̄) up to
phase to < 1e-61, i.e. the closed form (4.3) is confirmed by an **independent construction**
(`B.kernel_vector_matches[...]`).

---

## 6. G2 — the expansion and its remainder (note §5): **CONFIRMED line by line**

The commission asked for a line-by-line audit of the assembly. I checked each step against the
frozen §3–§4 machinery of the N1′ note (R5d LICENSE A), whose statements I read from disk.

| step | claim | audit |
|---|---|---|
| affinity | Λ(ρ_ε) = A_B + εB_B, Λ^c(ρ_ε) = A_E + εB_E | exact, both maps linear ✔ |
| (5.2) | ‖B_B‖, ‖B_E‖ ≤ 1, so b = 1 | for PSD trace-1 X, Y: X − Y ⪯ X ⪯ 1 and X − Y ⪰ −Y ⪰ −1 ✔; numerically ‖B_E‖ ≤ 0.31 at my test points, well inside ✔ |
| B side | spec A_B ⊂ [g, 1], **no** kernel (τ > 0); Weyl ⟹ λ_j(ε) ∈ [3g/4, 1] for ε ≤ g/4 | Fact 3.1 applies with ‖εB_B‖ ≤ ε; upper end λ_j(ε) ≤ 1 automatic (eigenvalue of a state) ✔ |
| (5.3) | \|S(Λ(ρ_ε)) − S(Λ(P))\| ≤ 3(1 + log(4/3g))ε | Lemma 4.2 with a = 3g/4, δ = ε, three eigenvalues ✔ |
| (5.4) | cluster slope μ^E = ⟨k\|B_E\|k⟩ = w_E | ⟨k\|Λ^c(P)\|k⟩ = 0 since k ∈ ker ✔ |
| (5.5) | \|λ₁(ε) − εw_E\| ≤ (40/9)ε²/g ≤ 6ε²/g | Proposition 3.3 is stated and proved in the reviewed note for **arbitrary m ≥ 1**, so the m = 1 instantiation is inside the R5d-reviewed scope (7d) ✔; hypothesis ε ≤ g/(4b) = g/4 matches ✔; I verified the *conclusion* numerically at 3 points × 2 φ × 3 ε (`Bvii.prop33_instantiation`) ✔ |
| U ≤ 5/2 | λ₁(ε)/ε ≤ w_E + 6ε/g ≤ 1 + 3/2 | uses ε ≤ g/4 and w_E ≤ 1 ✔ (numerically λ₁/ε ≤ 0.12 at my points) |
| (5.6) | \|h(λ₁) − εw_E log(1/ε)\| ≤ (6/(eg) + (5/2)log(5/2))ε | Lemma 4.1 with C = 6/g, κ(U) = max(1/e, U log U) = (5/2)log(5/2) ✔ (μ-independent, so no case split at w_E = 0) |
| E regular | 3 eigenvalues ≥ g − ε ≥ 3g/4, each (1 + log(4/3g))ε; Σ_{j≥2}h(λ_j(0)) = S(Λ^c(P)) since h(0) = 0 | ✔ |
| assembly | subtract, use S(Λ(P)) = S(Λ^c(P)) from isospectrality | ✔ — this is where the B-side and E-side base entropies cancel exactly, and it is the reason the leading term is **−w_E**, not w_B − w_E |
| displayed C | 6/(eg) + (5/2)log(5/2) + 3(1+log(2/g)) + 3(1+log(4/3g)) | **slacker** than what the proof gives on the B side (4/(3g) < 2/g), hence a valid upper bound; the note flags this itself. Arithmetic of the simplification C ≤ 3/g + 9 + 6log(2/g) checks (6/e ≤ 2.21, (5/2)log(5/2) ≤ 2.30, 2.30 + 6 ≤ 9) ✔ |

**Uniformity claims (7g).** C(x,τ) depends on (x, τ) only — not on φ, and not on which ψ of that τ —
because only the gap (3.6) enters; the window ε ≤ g/4 likewise. The *φ-dependent* window in
Corollary 5.2(ii), ε < min(g/4, exp(−C/w_E)), is correctly **not** claimed uniform. Remark 5.3's
degeneration C ≍ τ^{−2} as τ ↓ 0 is correct (g ≍ x(1−x)τ²/(2−x)) and the note draws the right
consequence: **no τ-uniform statement is available**, so no compactness argument can be run.

**Numerical reproduction of G5(ii) (my own code, seed, ε ladder), at all three commissioned points
(≥ 2 required), 3 φ each, ε ∈ {1e-4, 1e-6, 1e-12, 1e-20}:**

* w_E computed from the **eigensolver's** kernel vector equals the closed form to < 1e-45 at all
  9 (point, φ) pairs (`Bii.wE_closed_form_numeric`);
* the rigorous bound |Ic + w_E ε log(1/ε)| ≤ C(x,τ)ε holds at every tested ε inside the window
  (`Bii.remainder_bound`);
* **the leading coefficient itself**: the two-point log-slope of Ic/ε between ε = 1e-12 and 1e-20
  equals **−w_E** to relative error ≤ 1.0e-12, 9/9 pairs (`Bii.leading_coefficient_slope`). This is
  the sharp test — the remainder bound alone is far too slack at these ε to force the sign, exactly
  as the note honestly says in its `G5ii.d` note;
* **certificate points** where the bound *does* force the sign, adaptive precision: at
  (9/20, π/8), ε = 7.27e-123 (dps 202): Ic = −4.3633e-121 < 0, bound holds; at (1/5, π/8),
  ε = 6.599e-812 (dps 891): Ic = −6.0263e-810 < 0, bound holds (`Bii.certificate_points`).
  These are my own φ and my own ε, not the executor's rows.

My independently computed gaps and constants agree with the note's table to all printed digits:
g = 0.0903783919 / 0.0468871126 / 0.0422193171 and C = 50.07833 / 76.669693 / 82.503681 at
(9/20, π/8) / (1/5, π/8) / (9/20, π/6).

**Corollary 5.2 is correct:** (i) the ε log(1/ε) coefficient is −w_E ≤ 0 for every state φ at every
τ > 0 and every x; (ii) φ ≠ P_ψ ⟹ w_E > 0 strictly ⟹ Ic(ρ_ε) < 0 for ε < min(g/4, exp(−C/w_E));
(iii) φ = P_ψ ⟹ ρ_ε ≡ P and Ic ≡ 0 exactly.

---

## 7. G4 and the τ → 0 reconciliation (note §7, §8): **CONFIRMED**

**G4 is vacuous and correctly handled.** With E = ∅ the kernel-avoiding set of *states* is
{φ : supp φ ⊆ span{ψ}} = {P_ψ}, along which ρ_ε = P for all ε and Ic ≡ 0 **identically** — not
merely to first order. So no balanced/ε-linear layer computation is needed at τ ≠ 0, and the note's
observation that c₁ would not even be well defined there (log Λ^c(P) singular, one-dimensional
kernel) is right and moot. Nothing is swept under the rug here.

**The τ → 0 story is correct and is the part a careless reader would most likely mis-handle.** The
τ > 0 result (Ic strictly decreasing at small ε) and the reviewed isotropic ascent at τ = 0,
x < 2/5 coexist because of a **kernel-dimension jump**, not a discontinuous formula: at τ > 0 the B
side is full rank (w_B ≡ 0) and the E-side kernel is 1-dimensional; at τ = 0 the B side acquires a
kernel and the E-side kernel becomes 2-dimensional. I verified the quantitative form of this:
μ₋(x,τ)/τ² → x(1−x)/(2−x) = μ_A/4 (`Biii.tau_to_zero`; e.g. at x = 9/20, τ = 1e-3:
0.159677452 against 0.159677419), i.e. the isotropic **block-A** slope sits on an eigenvalue that is
*nonzero* at τ > 0 and only joins the cluster at τ = 0, while
w_E(ψ_α, P_ψ̄) = (x/2)(1 − τ²) → x/2 recovers the **block-B** slope only (verified symbolically,
`A4.wE_at_Ppsibar`). The admissible window ε ≤ g/4 collapses like τ² at the same rate, so
Theorem 5.1 never reaches the isotropic witness. No contradiction, and the note claims none.

**Corroboration of the frozen isotropic input** (not a re-review; R5c/R5d carry LICENSE A). With my
own implementation at τ = 0 I confirm dim ker Λ^c(P) = 2 and w_B − w_E = d₁ = (1−x)(2−5x)/(2−x) at
φ = P_ψ̄, = d₀ = −x(1−x)/(2−x) at φ = P_{e₃}, = 0 at φ = P_ψ, to < 1e-35, at x ∈ {1/5, 2/5, 9/20};
and 40 random φ per x never beat max(d₁, 0) (`Bvi.isotropic_corroboration`). So the note's quotation
of the isotropic layer in (10.1) — max over φ of the mechanism coefficient equals max(d₁, 0), > 0
iff x < 2/5 — is faithful.

---

## 8. The scope statements of §10 — adversarially attacked, and they hold

The note's §11(vi) explicitly asks the reviewer to attack §10 item 5. I did, from both sides.

* **(a) finite mixing.** The note is right that the small-ε result says nothing at ε = O(1), and it
  is right to flag it. I reproduced the phenomenon independently: at (x, α) = (1/5, π/8) with my own
  random φ, **Ic(ρ_ε) > 0 at ε = 1e-4** (+2.06e-5, +5.35e-5, +3.02e-5 for my three φ), flipping
  negative by ε = 1e-6 and converging to the −w_E ε log(1/ε) law thereafter. The reviewed
  Theorem 5.1 is therefore genuinely a small-ε statement, and any reading of it as "τ ≠ 0 base
  points are useless" would be **false**. The note says exactly this; I confirm it is not an
  overcautious hedge but a real limitation.
* **(b) non-uniformity in τ.** Confirmed above: C ≍ τ^{−2}, window ≍ τ². No compactness route.
* **(c) isotropic higher-order layers at and above 2/5.** Untouched by this note, correctly stated.
  (For the record, the balanced layer *on* the isotropic stratum is empty for x ∈ (2/5, 1) as well,
  since then d₁ < 0, d₀ < 0, d₂ = 0 make D ⪯ 0 with kernel span{ψ} — this follows from the frozen
  R5c closed form and I verified the numbers; the note does not need it and does not claim it.)
* **(d) n ≥ 2.** Untouched, correctly stated. Nothing in the argument restricts blocklength.
* I checked whether anything already on disk closes (a)–(d): it does not. P3's S1 scans are
  bounded searches (and R5a re-scoped the P6 numerical record); P10's distillation probes are
  bounded nulls; P9/P9b stopped at their gates. The strip [2/5, 1/2) remains genuinely open.

Bounded search of my own, reported as such and licensing nothing: over τ > 0 base points only
(α ∈ {(π/4)b/8, b = 1..8}, 7 φ each including P_ψ̄, ε ∈ {1e-6 … 0.9}), the maximum Ic found was
+0.323 at x = 1/5 (τ = 0.195, ε = 0.9) and **negative** at x = 9/20 (−1.44e-7) and x = 49/100
(−1.61e-7).

---

## 9. Verdict

**LICENSE A**, at the following exact scope, which is what I certify and what any status write
should quote:

> **Theorem (stratum exhaustion at every anisotropic pure base point) — PROVED.** For every
> x ∈ (0,1) and every unit ψ ∈ ℂ³ with τ(ψ) = |ψᵗψ| > 0: Λ_x(P_ψ) is full rank with spectrum
> {x/2, μ₊, μ₋}, μ_± the roots of λ² − (1 − x/2)λ + x(1−x)τ²/2; Λ_x^c(P_ψ) has the same spectrum
> plus one zero, so **dim ker Λ_x^c(P_ψ) = 1**, spanned by k = (0, ψ̄); K(k) = −√(x/2)·[ψ]_× has
> **rank exactly 2** with ker K(k) = span{ψ}, so the commissioned exceptional set
> **E = {(x,α) : dim ker K(k) ≥ 2, τ > 0} is EMPTY** and G4 is vacuous; and for every state φ and
> every 0 < ε ≤ g/4 with g = μ₋,
> **| Ic((1−ε)P_ψ + εφ) + w_E·ε·log(1/ε) | ≤ C(x,τ)·ε**, with
> **w_E = (x/2)(1 − ⟨ψ|φ|ψ⟩) ≥ 0** and C(x,τ) explicit and **uniform in φ**. Consequently no
> anisotropic pure base point supports a first-order ε log(1/ε) ascent at any x; the only state
> with w_E = 0 is φ = P_ψ, along which Ic ≡ 0 exactly; and every φ ≠ P_ψ gives Ic < 0 outright for
> ε < min(g/4, exp(−C/w_E)).
>
> **Combined statement (10.1) — PROVED, granting the R5c/R5d-reviewed isotropic layer (both
> LICENSE A, hence unconditional).** Define the *n = 1 pure-base first-order mechanism* as the sign
> of the coefficient of ε log(1/ε) in Ic((1−ε)P_ψ + εφ). That coefficient is > 0 for **some**
> (ψ, φ) **⟺ x < 2/5**, and every such witness has **τ(ψ) = 0**. Equivalently: at n = 1 the
> pure-base first-order mechanism yields positive-capacity witnesses **exactly** on the isotropic
> stratum with x < 2/5.
>
> **Scope of the P13 obligations.** Node obligation **(b) is CLOSED at the first-order layer** —
> no τ ≠ 0 pure base point yields an ε log(1/ε) ascent, at any x — and **not** in its literal "any
> ascent" reading: Ic > 0 at moderate ε from τ ≠ 0 pure base points is exhibited (independently, by
> both the author and this reviewer) at x = 1/5, and nothing here excludes it on [2/5, 1/2). The
> **first-order part of obligation (c) off the isotropic stratum is CLOSED** (the balanced set at
> τ ≠ 0 is {P_ψ}, along which Ic ≡ 0). Obligation (c) **on** the isotropic stratum at and above 2/5,
> and obligation (d) (n ≥ 2), are untouched. **Nothing here establishes Q^{(1)} = 0 or Q = 0
> anywhere on [2/5, 1/2); x_D = 2/5 remains a conjecture about where this mechanism ends.**

**Value-vs-formula statement (7f), overall.** My symbolic layer (38 gates) verifies **FORMULAS** —
identities in x, in an arbitrary complex ψ, and in an arbitrary 9-parameter Hermitian φ — not values
at sample points. My numeric layer (21 gates) verifies **VALUES** at 3 (x, α) points × 3 φ × 4 ε,
two certificate points, a 256-point (x, α) grid, an 8-point τ ladder and a 3-x isotropic ladder, and
in every case the numeric object (Ic, the kernel vector, the gap, w_E) is built by an **independent
construction** (Kraus operators + Hermitian eigensolver + Stinespring cross-check), then compared to
the note's formulas. Independent-construction agreement corroborates the claims; the *printed
derivations* of G1, G3, G2's assembly and G4 were verified separately and symbolically, above.

**MAJOR findings: none.**

**Minor findings (none blocks the licence):**

* **m1 (scope of the licensing text, decision-layer action).** Menu (A)'s phrase "P13 obligations
  (b) and first-order (c) are CLOSED" overstates obligation (b) as it is written on the node ("no
  tau ≠ 0 pure psi supports **any** ascent"). Any status write must say **first-order layer**; the
  §9 wording above is the corrected form. (The note itself is not at fault — its §10 item 5 states
  the limitation clearly.)
* **m2 (probe hygiene).** The non-commissioned G5(v) probe sweeps α over (0, π/4], which **includes
  α = π/4, i.e. τ = 0** — outside the stratum this note is about. Per the log
  (`meta.G5v_moderate_eps`), the reported maxima at x = 9/20 and x = 49/100 ("0.0") are attained
  exactly at `at_tau: 0.0`, so they are not evidence about the τ > 0 stratum. My τ > 0-only probe
  found maxima −1.44e-7 (9/20) and −1.61e-7 (49/100). Cosmetic — the probe licenses nothing — but
  the §9.6 sentence should exclude the isotropic endpoint or name it.
* **m3 (gate bookkeeping).** Of the 56 gates in `p13a_sanity.json`, one (`G5v.probe_completed`) is a
  completion flag rather than a mathematical assertion, so "56 boolean gates, all PASS" is 55
  assertions plus one marker. All 56 are recorded PASS in the log and the note's tables match the
  JSON row-for-row (I verified the G5(ii) rows, the three certificate rows, the G5(iii) table and
  the G5(iv) statistics against `meta`).
* **m4 (normal-form-only prose).** Remark 6.3's "w·w = ψᵗψ = τ" and "char roots 0, ±i√(xτ/2)" hold
  **in the normal form**; for general ψ, ψᵗψ is a complex number of modulus τ and the charpoly is
  λ³ + (x/2)(ψᵗψ)λ (my gate `A3.skew_charpoly`). The note's gate line qualifies this; the remark's
  prose does not. No mathematical consequence.
* **m5 (deliberate slack, verified).** The displayed C(x,τ) carries 3(1 + log(2/g)) on the B side
  where the proof yields the sharper 3(1 + log(4/(3g))). It is therefore a valid but non-tight
  bound; the note flags this. Since C enters Corollary 5.2(ii) only through exp(−C/w_E), the slack
  costs nothing but window size. No action needed.

**Rule-7 self-audit.** (7a) per-display type audit: §2. (7b) c ≥ 2 identity gates: every algebraic
identity is verified **fully symbolically** in x, ψ and φ (stated per gate), and every numeric claim
at ≥ 3 parameter points; both qualitatively distinct regimes of the kernel-dimension count (τ > 0
one-dimensional cluster; τ = 0 two-dimensional) are exercised at the identity level, as is the
delicate w·w = 0 branch. (7c) anchoring: §1, with the honest caveat that the reload made me read
the note first; all derivations are own-route and own-code. (7d) frozen inputs: I relied only on the
R5d-reviewed §3–§4 machinery of the N1′ note (used at m = 1, inside its stated m ≥ 1 scope), the
R5c-reviewed isotropic closed form (corroborated, not re-reviewed), and P2/P4/P3 as background —
none of which carries the τ > 0 analysis this note contributes. (7e) standing failure modes: §10
below. (7f) value-vs-formula: stated above and per gate. (7g) every term of art used in the licence
resolves in the note or in this report.

---

## 10. Standing failure modes (R5 commission §2), screened item by item

1. **sympy `.H` / `conjugate(sqrt(1−x))` — SCREENED AND HIT BY ME TOO.** My first symbolic run
   substituted `{t**2: 1−x, sg**2: x/2}` into the complement, and sympy silently rewrote the *odd*
   monomial `t·σ` in the (0,i) entries as `√2·√x·√(1−x)`, after which `.H` produced
   `conjugate(sqrt(1−x))` and my Hermiticity gate failed. This **independently reproduces the
   executor's §9.1 report** of the same trap on the same matrix entries. My fix differs from theirs
   (they moved to a rational chart; I made `strip()` refuse to substitute unless the expression is
   *proved* even in both radical symbols, and kept Λ^c in the (t, σ) chart), and both are sound:
   the trap is a tooling artefact, no mathematical step depends on the chart.
2. **WindowsApps python** — not used; the pinned interpreter throughout.
3. **Complement convention drift** — screened by an independent Stinespring reconstruction
   (`B0.stinespring_conventions`), not by inspection. My first draft of that gate had an extra
   transpose and failed; the failure was mine and the frozen convention is the correct one.
4. **Transpose vs conjugate-transpose** — `†` = `ᵗ` used only for the real Kraus operators, and the
   Kraus set was verified to reproduce Λ_x entrywise before any use.
5. **`sorted()` / comparison on symbolics** — avoided by using `det(λ1 − M, berkowitz)` instead of
   `charpoly()`; I hit no TypeError, consistent with the executor's report of the same workaround.
6. **CRLF in SHA256SUMS** — `SHA256SUMS_r6.txt` written with LF and verified with
   `sha256sum -c` (6 files, all OK).
7. **Degeneracy / dividing by small gaps** — nothing in the τ > 0 analysis divides by cluster-slope
   differences (the cluster is one-dimensional, so the question does not arise); the only gap used
   is g = μ₋, and I used the cancellation-free form 2D/(T + √(T²−4D)) numerically.
8. **ε log ε bookkeeping** — Lemma 4.1 of the reviewed note is μ-independent and handles
   0 log 0 = 0; the O(ε²log(1/ε)) = o(ε) step is made quantitative in (5.6) and I re-checked the
   constants.
9. **Anchoring** — §1.

---

## 11. Provenance

```
whgap_r6_symbolic.py   38/38 gates PASS   3.3 s
whgap_r6_numeric.py    21/21 gates PASS   6.6 s
C:<home>/cpython3119/python.exe  (Python 3.11.9, sympy 1.13.1, mpmath 1.3.0)
```

Commands (from the repository root):

```
C:<home>/cpython3119/python.exe -u tools/whgap_r6_symbolic.py artifacts/logs_whgap_p13a_20260730/r6_symbolic.json > artifacts/logs_whgap_p13a_20260730/r6_symbolic.log
C:<home>/cpython3119/python.exe -u tools/whgap_r6_numeric.py  artifacts/logs_whgap_p13a_20260730/r6_numeric.json  > artifacts/logs_whgap_p13a_20260730/r6_numeric.log
```

SHA-256 (also archived as `artifacts/logs_whgap_p13a_20260730/SHA256SUMS_r6.txt`, LF endings,
`sha256sum -c` = 6 × OK):

```
9c5fe9327acaeec0b325ef5d467ab63c542d8165342577274305e35e23b76b84  tools/whgap_r6_symbolic.py
be26fbb9e4f940c92d0e9912cf3441b46d2d85395c718c24c688abe08ad533a2  tools/whgap_r6_numeric.py
3483f1b8cc29ece5655ceae14d6615388071ad9e6c338723109e3c437e0d90ba  artifacts/logs_whgap_p13a_20260730/r6_symbolic.json
733d54d294f8af508d1bb3df0014593770095dbbeb9317e751951e6f161676c0  artifacts/logs_whgap_p13a_20260730/r6_symbolic.log
17a64879cfb714d243dd32822884c6715bb90bc95f08cfeb3990d66575f44ed1  artifacts/logs_whgap_p13a_20260730/r6_numeric.json
2294f08cfb5f3c0a108115d6555e870ee08d2984a2920ea51d56e0816b558541  artifacts/logs_whgap_p13a_20260730/r6_numeric.log

(the reviewed package's own hashes in the note's §9.7 were re-verified against disk and match:
 e8fcace922ad534c5c813bb479905f24792b69add18aee5393c24e2496cbc269  tools/whgap_p13a_sanity.py
 767ebac8416aea985d91026b3181efcfcf8c2d68b596aee9b9d97b09fd5a68fa  artifacts/logs_whgap_p13a_20260730/p13a_sanity.json
 0e318d9f8538f52a38f0cb867c2f60141305e9e50fc5d005a1ebe59b01cc0be3  artifacts/logs_whgap_p13a_20260730/p13a_sanity.log)
```

This report is immutable. The decision layer owes the rule-8c node links for both the reviewed
package and this review.

