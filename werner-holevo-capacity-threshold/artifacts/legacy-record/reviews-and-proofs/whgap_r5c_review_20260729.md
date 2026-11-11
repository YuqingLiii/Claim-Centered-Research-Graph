# WHGAP R5c — independent review of P6b-V2 (isotropic weight operator) + the P9b digestion

**Reviewer:** fresh Opus instance, 2026-07-29 (night). **Commission:**
`channel-capacity/werner-holevo-gap/notes/WHGAP_REVIEW_COMMISSION_R5_20260729.md`, section
"R5c — review of P6b-V2 + P9b digestion". **Node:** `WHGAP.no-ascent-hierarchy`.
**Interpreter for every run:** `C:<home>/cpython3119/python.exe`
(sympy 1.13.1, mpmath 1.3.0). This artifact is immutable.

---

## 0. PRE-ACTION REPORT (per `research/PRETASK_RELOAD_PROMPT.md`)

Files read from disk before any mathematics, in order: `research/DAG_PROTOCOL.md` (whole file:
§1 data structure, §2 ladder, §3 rules 1–8, §4–§6 protocols and session-close checklist);
`research/RESEARCH_STRUCTURE_PROTOCOL.md` (§1–§10); `channel-capacity/werner-holevo-gap/README.md`;
`channel-capacity/werner-holevo-gap/notes/WERNER-HOLEVO-GAP_PROOF_DAG.md` (header, inlined eight
rules, Mermaid, outline); `channel-capacity/werner-holevo-gap/proof-dag/NODE_INDEX.md`; the target
node `proof-dag/nodes/WHGAP.no-ascent-hierarchy.md`; its parent `nodes/WHGAP.goal.md`. The node has
no children (LEAF).

- **Target node / status as read from disk:** `WHGAP.no-ascent-hierarchy` (alias P9), kind LEAF,
  role proof, **status CONJECTURED**, `status_source: "decision-layer derivation 2026-07-29
  (first-order closed form derived in-node; pending review)"`, disposition null, parent
  `WHGAP.goal` (OPEN), `Adversarial reviews: None yet`. Index row agrees (line 61 of
  `NODE_INDEX.md`): `P9 | WHGAP.no-ascent-hierarchy | LEAF | proof | CONJECTURED`.
- **My ROLE:** reviewer. **Independence statement:** I did not author any of the reviewed
  work (neither the P6b-V2 scripts, nor the P9b execution, nor the node's digestion sections),
  I was given no desired outcome, and the commission presented its licensing menu as
  alternatives. I performed my own derivation before reading any author derivation
  (see §1 for the one unavoidable anchoring exposure and how it was handled).
- **Highest status my planned evidence could license (per §2 ladder):** a completed, archived,
  rule-7-compliant independent review opens the **PROVED** tier for the algebraic
  closed-form claims (claims 1–2) and for the digestion claims 4(i)–(iii) that are pure algebra
  /group theory; the *writer* of any status is the decision layer citing this artifact
  (rule 2/6: I neither stamp nor write node statuses). Nothing here licenses anything about the
  ε log ε expansion lemma or about Q(Λ_x) > 0 — those are R5d/E-N1 scope and remain untouched.
- **Gates and deliverables of my commission, one line each:**
  (i) derive the isotropic weight operator D by my OWN construction (w_B, w_E as linear
  functionals on a Hermitian basis; derive the duality myself; do not start from the author's
  M_B/M_E); (ii) prove or c ≥ 3-rational-point-verify d_0 = −x(1−x)/(2−x),
  d_1 = (1−x)(2−5x)/(2−x), d_2 = 0; (iii) adjudicate the supersession of
  `tools/whgap_p6b_v2_isotropic.py`; (iv) verify the P9b digestion claims, including the
  load-bearing O(3)-orbit-transitivity + covariance-transport claim 4(iii), so far only asserted;
  (v) deliver `artifacts/whgap_r5c_review_20260729.md` with a verdict from the R5c menu.
- **Conflicts between commission text and disk protocols:** **one, and it is itself
  commissioned.** The commission's binding "single-writer deviation" forbids me from editing node
  files / `NODE_INDEX.md` / the DAG doc, which otherwise conflicts with the atomic-update
  obligations (structure protocol §6.3, DAG protocol §5.1, PRETASK obligation 2). The commission
  states the deviation is authorized by the commissioner and that the decision layer performs the
  atomic node/index/DAG updates citing this artifact immediately after the batch; I therefore
  wrote only this report, my own scripts under `tools/`, and my own logs under
  `artifacts/logs_whgap_r5_20260729/`. **This report is not linked from the node by me**; that
  obligation transfers to the decision layer and is flagged here so it cannot be lost.
  Secondary, procedural: the commission asks each agent to end with `SHA256SUMS.txt` in the shared
  log directory, but R5a already wrote `SHA256SUMS.txt` and R5b wrote `SHA256SUMS_r5b.txt` there;
  to avoid the exact concurrent-write corruption the single-writer rule exists to prevent, I wrote
  **`SHA256SUMS_r5c.txt`** (LF, verified with `sha256sum -c`). No other conflict; no protocol rule
  was relaxed. No status was written by me anywhere.

---

## 1. Method, and the anchoring disclosure (7c)

**Anchoring ban compliance.** I built the entire construction myself before opening any author
file: `tools/whgap_r5c_weight_operator.py` (symbolic), `tools/whgap_r5c_numeric_gates.py`
(60-digit mpmath, disjoint route), and a by-hand closed-form proof (§3). Only afterwards did I read
`artifacts/whgap_p6b_necessity_20260729.md`, `tools/whgap_p6b_v2_fable.py`,
`tools/whgap_p6b_v2_isotropic.py`, `artifacts/logs_whgap_p6b_20260729/v2_isotropic.json` and the
P9b JSON.

**Unavoidable exposure, declared:** the commission text itself displays the three target values
(d_0, d_1, d_2) and the definitional shapes of M_B/M_E. I could not un-see them. Mitigations
actually carried out: (a) I derived the duality **Tr[M_E φ] = Tr[Π_E Λ^c(φ)]** from scratch
(§2) rather than reading it; (b) my primary route never uses M_B/M_E at all — it reconstructs D
from the nine values of the functional φ ↦ w_B(φ) − w_E(φ) on an orthonormal Hermitian basis, and
the M_B − M_E form appears only in gate G8b as a cross-check; (c) my Π_E is built two ways, one of
them (numeric route) from a Hermitian eigendecomposition that has no analytic input at all;
(d) I use my own coordinate conventions (Kraus amplitudes a = √(1−x), b = √(x/2) as independent
positive symbols) which differ from both author scripts; (e) I re-derived the closed forms by hand
in a projector algebra (§3) that neither author script uses, obtaining the same result by a
different mechanism (the 4κ coefficient arises from iA_2 = P_ψ̄ − P_ψ). **Notational coincidence
flag (required by 7c):** my final closed forms coincide with the author's displayed ones; the
derivations do not coincide — the author's route is nullspace + Gram–Schmidt + symbolic
`simplify`, mine is an exact projector-algebra identity plus an independent functional
reconstruction.

**Parameterization choice, and why (standing failure mode 1).** My first symbolic attempt used
`x = Symbol('x', positive=True)` directly and immediately reproduced failure mode 1: sympy left
`conjugate(sqrt(2-x))`/`conjugate(sqrt(1-x))` unresolved and four gates failed spuriously (log
`r5c_weight_operator.log` first revision; retained in the discussion here rather than as a
separate artifact). I therefore reparameterized with **a = √(1−x) > 0, b = √(x/2) > 0** and
K_0 = a·1, K_{μ+1} = b·A_μ, constraint a² + 2b² = 1 (gate G1d). Every object is then
polynomial/rational in (a, b), **every conjugation resolves exactly with no hand-stripping**, and
the map back to x is applied only after all conjugations. This is a strictly stronger discipline
than the author's `realify` helper (see minor m1).

---

## 2. Type audit (7a) — every object in the reviewed claims

| Object | Type | Dimension / notes |
|---|---|---|
| x | real parameter | frozen domain x ∈ (0,1); a = √(1−x), b = √(x/2) both > 0 there |
| Λ_x | superoperator M_3(C) → M_3(C) | CPTP; Λ(Y) = (1−x)Y + (x/2)(Tr Y·1 − Y^T); trace preservation needs a²+2b² = 1 (G1d) |
| Λ_x^† | superoperator M_3 → M_3 | **equals Λ_x** — verified on all 81 basis pairs (G8a), so "M_B = Λ†(P_ψ̄) = Λ(P_ψ̄)" is typed correctly |
| K_0 … K_3 | matrices in M_3(R) | real ⟹ K^† = K^T; A_μ = (ε_{μjk}) real antisymmetric; the four are linearly independent |
| Λ_x^c | superoperator M_3(C) → M_4(C) | padded 4-dim; (a,b) entry Tr(K_a Y K_b^†); trace-preserving (G1e); Λ^c(ρ) has rank 4 for generic full-rank ρ (the 4th dimension is **not** a spurious padding zero) |
| ψ | unit vector in C^3 | isotropic: τ(ψ) = \|ψ^Tψ\| = 0; canonical ψ = (e_1+ie_2)/√2 = (1,i,0)/√2 (0-indexed) |
| ψ̄, e_3 | unit vectors in C^3 / R^3 | (e_3, ψ̄, ψ) is an orthonormal **basis of C^3** — U†U = 1 verified (G4d); ψ ⊥ ψ̄ is exactly isotropy |
| P_ψ, P_ψ̄, P_{e_3} | rank-1 orthogonal projectors on C^3 | 3×3; P_ψ^T = P_ψ̄ |
| Π_E | orthogonal projector on **C^4** | Π_E = Π_E† = Π_E², Tr Π_E = 2, Π_E Λ^c(P_ψ) = 0 (G3b,c) — rank exactly 2 for every x ∈ (0,1) |
| w_B, w_E | real-linear functionals on the Hermitian part of M_3 | w_B(φ) = ⟨ψ̄\|Λ(φ)\|ψ̄⟩ (scalar); w_E(φ) = Tr[Π_E Λ^c(φ)] (scalar); both real on Hermitian φ (G4b) |
| M_B, M_E, D | Hermitian operators on C^3 (3×3) | entries rational in x; D = M_B − M_E; **not** superoperators |
| d_0, d_1, d_2 | real scalars, functions of x | eigenvalues of D in the ordered basis (e_3, ψ̄, ψ) |

Two type-level points that the reviewed text does not state but which the claims silently need,
and which I verified: (i) the **E-side index transport is by a real orthogonal 4×4
V = 1 ⊕ det(O)·O**, not by an arbitrary unitary and not by 1 ⊕ O (the det factor is required on
the det = −1 branch) — G6c; (ii) w_E is a trace over a genuinely 2-dimensional kernel: since the
four Kraus operators are linearly independent and ρ_ε is faithful for ε > 0, rank Λ^c(ρ_ε) = 4,
so both kernel eigenvalues move to order ε and the full 2-dim Π_E is the correct weight
(this is what makes the definition in claim 1 the right object).

---

## 3. My own derivation of D (independent path, exact, by hand; machine-confirmed)

**Duality, derived here, not read.** For Hermitian φ,
w_B(φ) = Tr[P_ψ̄ Λ(φ)] = Tr[Λ^†(P_ψ̄) φ], and Λ^† = Λ because
Tr[M φ^T] = Σ_{ij} M_{ij} φ_{ij} = Tr[M^T φ]. For the environment,
Tr[Π_E Λ^c(φ)] = Σ_{a,b} (Π_E)_{ab} (Λ^c(φ))_{ba} = Σ_{a,b} (Π_E)_{ab} Tr(K_b φ K_a^†)
= Tr[(Σ_{a,b} (Π_E)_{ab} K_a^† K_b) φ], hence **M_E = Σ_{ab} (Π_E)_{ab} K_a^T K_b** (real Kraus).
M_E is Hermitian because Π_E is.

**Base point.** With ψ isotropic, P_ψ^T = P_ψ̄ and 1 = P_ψ + P_ψ̄ + P_{e_3}, so
Λ(P_ψ) = (1−x)P_ψ + (x/2)(1 − P_ψ̄) = **(1−x/2)P_ψ + (x/2)P_{e_3}** — spectrum {1−x/2, x/2, 0},
kernel exactly span{ψ̄}. Likewise M_B = Λ(P_ψ̄) = (1−x/2)P_ψ̄ + (x/2)P_{e_3}, i.e.
diag(x/2, 1−x/2, 0) in (e_3, ψ̄, ψ).

**Environment kernel, computed from the Kraus images.** v_a := K_a ψ. Using A_μψ = ψ × e_μ:
v_0 = aψ, v_1 = −i(b/√2)e_3, v_2 = (b/√2)e_3, v_3 = i b ψ. So span{v_a} = span{ψ, e_3}
(⟹ rank Λ^c(P_ψ) = 2, spectrum {1−x/2, x/2, 0, 0} with the ψ-block weight a²+b² = 1−x/2 and the
e_3-block weight b²/2 + b²/2 = x/2 — **isospectral** with Λ(P_ψ), so Ic(P_ψ) = 0 exactly).
Since Λ^c(P_ψ)_{ab} = ⟨v_b, v_a⟩ is a Gram matrix, its kernel is the **conjugate** of the space of
linear dependencies (this is exactly where standing failure mode 4 bites, and where the superseded
script went wrong — §6). The two dependencies are (b)v_0 + (i a)v_3·(−1)… explicitly, the kernel of
the Gram matrix is spanned by

  u^(1) = (b, 0, 0, −i a),  u^(2) = (0, 1, −i, 0),   ⟨u^(1), u^(2)⟩ = 0,
  ‖u^(1)‖² = a² + b² = 1 − x/2,  ‖u^(2)‖² = 2,

and Π_E = u^(1)u^(1)†/(1−x/2) + u^(2)u^(2)†/2 (verified: Π_E² = Π_E = Π_E†, Tr = 2,
Π_E Λ^c(P_ψ) = 0, and equal to sympy's own nullspace projector — G3a–d).

**Projector algebra.** With A_2 = E_01 − E_10 one has the three identities
iA_2 = P_ψ̄ − P_ψ, E_00+E_11 = P_ψ + P_ψ̄, −A_2² = E_00 + E_11, and (for the second kernel
direction) A_0A_1 = E_10, A_1A_0 = E_01, −A_0² = E_11+E_22, −A_1² = E_22+E_00. Then

- from u^(1) (the K_0 ↔ K_3 mixing direction):
  M_E^{(1)} = (a²b²/(a²+b²))·[1 + 2iA_2 + (E_00+E_11)] = **κ (4P_ψ̄ + P_{e_3})**,
  κ := a²b²/(a²+b²) = x(1−x)/(2−x);
- from u^(2) (the two e_3-block directions):
  M_E^{(2)} = (x/2)[½(P_ψ+P_ψ̄) + P_{e_3} + ½ iA_2] = **(x/2)(P_ψ̄ + P_{e_3})**.

Note both P_ψ coefficients cancel — that is the mechanism behind d_2 = 0, and it is a genuine
cancellation, not an assumption. Hence

  **D = M_B − M_E = (1 − x − 4κ) P_ψ̄ − κ P_{e_3}**,  κ = x(1−x)/(2−x),

which is **exactly diagonal** in (e_3, ψ̄, ψ) with

  **d_0 = −κ = −x(1−x)/(2−x),  d_1 = 1 − x − 4κ = (1−x)(2−5x)/(2−x),  d_2 = 0.**

(1 − x − 4κ = (1−x)[1 − 4x/(2−x)] = (1−x)(2−5x)/(2−x).) Signs on (0,1): (1−x) > 0 and (2−x) > 0,
so d_0 < 0 strictly, and sign(d_1) = sign(2−5x) ⟹ **d_1 > 0 ⟺ x < 2/5**, d_1 = 0 exactly at
x = 2/5, d_1 < 0 on (2/5, 1). Largest eigenvalue of D = max(d_1, 0) since d_2 = 0 and d_0 < 0.

**Orbit transitivity (claim 4(iii)), proved here.** Write ψ = u + iv with u, v ∈ R^3. Then
‖ψ‖ = 1 and ψ^Tψ = 0 ⟺ ‖u‖² = ‖v‖² = 1/2 and u·v = 0, i.e. {√2u, √2v} is an orthonormal pair.
Put O := [√2u, √2v, 2(u×v)]. Its columns are orthonormal and the third is the cross product of the
first two, so O ∈ **SO(3)** and O ψ_0 = (√2u + i√2v)/√2 = ψ for ψ_0 = (e_1+ie_2)/√2. Hence SO(3)
alone acts **transitively** on the isotropic stratum {ψ : ‖ψ‖ = 1, ψ^Tψ = 0}; the stabilizer of
ψ_0 is trivial (Rψ_0 = ψ_0 with R real forces Re_1 = e_1, Re_2 = e_2, hence R = 1), so the stratum
is a single free SO(3)-orbit of real dimension 3 = 5 − 2, matching the constraint count. Global
phases need no separate U(1): e^{−iθ}ψ_0 = R_θ ψ_0 for the rotation R_θ about e_3, and in any case
D depends on ψ only through P_ψ and P_ψ̄ = P_ψ^T.

**Covariance transport (claim 4(iii)), proved here.** For O ∈ O(3): Λ(OYO^T) = OΛ(Y)O^T (real
coefficients, Tr and transpose both O-equivariant). From ε_{ijk}O_{ai}O_{bj}O_{ck} = det(O)ε_{abc}
one gets O^T A_μ O = det(O)·Σ_c O_{μc} A_c, hence **O^T K_i O = Σ_j V_{ij} K_j with
V = 1 ⊕ det(O)·O real orthogonal**, and therefore Λ^c(OYO^T) = V Λ^c(Y) V^T. Consequently
ker Λ^c(P_{Oψ}) = V·ker Λ^c(P_ψ), Π_E(Oψ) = V Π_E(ψ) V^T, and, since conj(Oψ) = O ψ̄,
w_B(Oψ, φ) = w_B(ψ, O^TφO) and w_E(Oψ, φ) = w_E(ψ, O^TφO). Hence
Tr[D_{Oψ} φ] = Tr[D_ψ O^TφO] = Tr[O D_ψ O^T φ] for all φ, i.e.

  **D_{Oψ} = O D_ψ O^T** — orthogonal (in particular unitary) equivalence, same spectrum,
  with the diagonalizing triple transported to (O e_3, O ψ̄, O ψ).

**One representative therefore suffices, unconditionally** — no continuity or chart-coverage
argument is needed (contrast the P9b stereographic chart, whose omitted point was covered "by
continuity"; see minor m5).

---

## 4. Gate table (own scripts; all runs logged with hashes)

`tools/whgap_r5c_weight_operator.py` — symbolic, exact, in (a,b) → mapped to x.

| Gate | Content | Result |
|---|---|---|
| G1a–b | 9 Hermitian directions, Tr[G_jG_k] = δ_jk, all Hermitian | PASS |
| G1c | Σ_i K_i G K_i^T = a²G + b²(Tr G·1 − G^T) on all 9 directions | PASS (formula) |
| G1d–e | Tr Λ(Y) = (a²+2b²)Tr Y with a²+2b² = 1; Tr Λ^c(G) = Tr G | PASS |
| G1f–g | τ(ψ) = 0, ‖ψ‖ = 1, ψ ⊥ ψ̄ | PASS |
| G2a–c | Λ(P_ψ) = (1−x/2)P_ψ + (x/2)P_{e_3}; spec {1−x/2, x/2, 0}; ker = span{ψ̄}, 1-dim | PASS (formula) |
| G2d–f | spec Λ^c(P_ψ) = {1−x/2, x/2, 0, 0} (0 with multiplicity 2), rank 2, isospectral with the B side | PASS (formula) |
| G3a–c | orthogonal kernel Gram diag(1−x/2, 2); Π_E = Π_E² = Π_E†, Tr = 2, Π_EΛ^c(P_ψ) = 0 | PASS |
| G3d | my analytic kernel basis ≡ sympy's nullspace projector, symbolically | PASS |
| G4a–c | D from the 9 functional values is Hermitian; the values are real; **Tr[D G] = w_B(G) − w_E(G) for all 9 directions symbolically** (⟹ for every Hermitian φ by real-linearity) | PASS (formula) |
| G4d–e | (e_3, ψ̄, ψ) orthonormal; **D exactly diagonal** (all off-diagonals identically 0) | PASS (formula) |
| G4f–h | **d_0 = −x(1−x)/(2−x), d_1 = (1−x)(2−5x)/(2−x), d_2 = 0** | PASS (formula, symbolic in x) |
| G4i | D = (1−x−4κ)P_ψ̄ − κP_{e_3} (my projector form) | PASS (formula) |
| G5a | 6 exact rational x (1/5, 2/5, 9/20, 499/1000, 1/2, 3/4): reconstructed diagonal = closed forms | PASS (values, c = 6 ≥ 3) |
| G5b | **x = 9/20 ⟹ diag(−99/620, −11/124, 0)** = the P9b datum | PASS (value) |
| G5c–e | d_1 numerator roots {2/5, 1}; d_0 < 0 on (0,1); d_1 ≤ 0 on [2/5,1) | PASS |
| G6a | constructive SO(3)-transitivity on 3 explicit isotropic ψ (det = +1, Oψ_0 = ψ) | PASS |
| G6b–c | 4 test O (2 with det = +1, 2 with det = −1): O^TK_iO = ΣV_{ij}K_j with V = 1⊕det(O)O orthogonal; Λ- and Λ^c-covariance on all 9 directions | PASS (formula) |
| G6d | symbolic transport D_{Oψ} = O D_ψ O^T rebuilt from its own Π_E | **sympy-uncertified** — see below |
| G7a–e | at x = 9/20: eigs {−99/620, −11/124, 0}, D ⪯ 0, ker D = span{ψ}; −D ⪰ 0; balance at P_ψ; 15 probe states off span{ψ} strictly negative; mixtures strictly negative | PASS |
| G8a–c | Λ^† = Λ on all 81 pairs; **functional-reconstructed D ≡ M_B − M_E**; M_B, M_E both diagonal (M_B = diag(x/2, 1−x/2, 0)) | PASS |
| G8d | 1 − x = d_1 + 4κ — the identity that explains the superseded value | PASS |

`tools/whgap_r5c_numeric_gates.py` — mpmath, **mp.dps = 60**, Π_E from a numeric Hermitian
eigendecomposition (no analytic kernel input anywhere).

| Gate | Content | Result |
|---|---|---|
| N1 | rank Λ^c(P_ψ) = 2 with nonzero eigenvalues {1−x/2, x/2}, Tr Π_E = 2, at 6 rational x | PASS (< 1e−45) |
| N2 | numerically reconstructed D reproduces d_0, d_1, d_2 = 0 and is diagonal in (e_3, ψ̄, ψ); worst error 2.3e−61, worst off-diagonal 2.8e−62 | PASS (values, 6 points) |
| N3 | Tr[D φ] = w_B(φ) − w_E(φ) for 8 random full-rank complex states at each of 6 x (48 checks); worst 1.2e−61 | PASS |
| N4 | 10 random isotropic ψ (τ < 1e−60): D_ψ built from its OWN numeric Π_E equals O D_{ψ_0} O^T (≤ 1.9e−61) and spec D_ψ = {d_0, d_1, 0} (≤ 3.3e−61) | PASS |
| N5 | coherence only: Ic(ρ_ε)/(ε log₂(1/ε)) → d_1 with the correct sign at x = 1/5 (d_1 = +0.4444; ratios 0.4569 → 0.4494 for ε = 1e−4 … 1e−10) and x = 9/20 (d_1 = −0.08871; ratios −0.1117 → −0.0979) | PASS (corroboration) |

**On G6d.** The symbolic transport residual did not reduce to 0 entrywise under sympy — 5 of 9
entries were certified 0 and 4 were left as unnormalized nested radicals (Gram–Schmidt on a
generically rotated 4-dim kernel produces sqrt-of-degree-18-polynomial towers). I therefore
localized it in `tools/whgap_r5c_transport_diag.py`: the residual is a rational function of (a,b)
that must vanish identically, and it **vanishes exactly at 4 independent (a,b) points (3 rational
plus the x = 9/20 radical point) for all four rotations, both det branches**
(`r5c_transport_diag.log`), while the numeric gate N4 gives 1e−61 agreement at 10 random isotropic
ψ. Together with the analytic proof in §3 (which needs only the symbolically-verified covariance
identities G6c) the transport claim is established; the G6d "FAIL" flag in
`r5c_weight_operator.log` is a computer-algebra normalization artifact, **not** a mathematical
failure, and is disclosed here rather than suppressed.

---

## 5. Claim-by-claim verdict, with value-vs-formula statements (7f)

**Claim 1 (definitions and duality) — CONFIRMED as a FORMULA (symbolic in x).**
w_B(ψ,φ) = ⟨ψ̄|Λ(φ)|ψ̄⟩ with ker Λ(P_ψ) = span{ψ̄} exactly (G2c); w_E(ψ,φ) = Tr[Π_EΛ^c(φ)] with
Π_E the orthogonal projector onto the **2-dimensional** ker Λ^c(P_ψ) (G2d–e, G3b–c);
M_B = Λ†(P_ψ̄) with Λ† = Λ verified (G8a); M_E = Σ_{ab}(Π_E)_{ab}K_a^TK_b **re-derived
independently** (§2, §3); and w_B − w_E = Tr[Dφ] verified symbolically on a complete Hermitian
basis (G4c), hence for every Hermitian φ, hence for every state. My primary route did not use
M_B/M_E; their agreement with the functional reconstruction is gate G8b.

**Claim 2 (closed forms, diagonality, sign rule, spectra) — CONFIRMED as a FORMULA (symbolic),
and additionally at c = 6 rational points and 60-digit numerics.**
D is exactly diagonal in (e_3, ψ̄, ψ) (all off-diagonals identically zero, G4e); d_0 = −x(1−x)/(2−x),
d_1 = (1−x)(2−5x)/(2−x), d_2 = 0 (G4f–h, hand proof §3, N2); sign rule d_1 > 0 ⟺ x < 2/5 with the
only sign change at x = 2/5 (G5c); spec Λ(P_ψ) = {1−x/2, x/2, 0} and spec Λ^c(P_ψ) =
{1−x/2, x/2, 0, 0} (G2b, G2d). The auxiliary statement max_φ(w_B − w_E) = max(d_1, 0) is immediate
from d_2 = 0, d_0 < 0 and is confirmed. **What remains unverified in claim 2:** nothing within its
own scope. Explicitly out of scope here: whether (w_B − w_E) is the ε log(1/ε) coefficient of
Ic(ρ_ε) — the expansion lemma is E-N1/R5d work; N5 only corroborates the sign convention
numerically and is labelled as corroboration.

**Claim 3 (supersession) — CORRECTLY ADJUDICATED; and I localize the defect exactly.** See §6.

**Claim 4(i) — CONFIRMED (value at x = 9/20, and as a formula on (2/5,1)).** At x = 9/20,
D = diag(−99/620, −11/124, 0) ⪯ 0 with ker D = span{ψ} exactly (G5b, G7a). Since
w_B(φ) − w_E(φ) = Tr[Dφ] for every state φ, "D ⪯ 0" **is** precisely the (N1′-a) inequality
w_B ≤ w_E for all φ at that x, with an exact rational certificate. As a formula, D ⪯ 0 holds
exactly on x ∈ [2/5, 1) (d_0 < 0 always, d_1 ≤ 0 ⟺ x ≥ 2/5), with the kernel 1-dimensional on
(2/5,1) and 2-dimensional at x = 2/5.

**Claim 4(ii) — CONFIRMED (and I supply the general argument).** For D ⪯ 0 and φ ⪰ 0,
Tr[Dφ] = 0 ⟺ Tr[(−D)^{1/2}φ(−D)^{1/2}] = 0 ⟺ (−D)^{1/2}φ^{1/2} = 0 ⟺ supp φ ⊆ ker D. At x = 9/20
ker D = span{ψ}, so the only balanced state is φ = P_ψ, for which ρ_ε = P_ψ identically — the
balanced layer is empty of nontrivial directions (G7a–e; 15 explicit probe states off span{ψ} all
give Tr[Dφ] < 0, and mixtures with P_ψ̄ reach balance only at the endpoint). **Scope caution
(minor m4):** this emptiness is a property of x ∈ (2/5, 1); at x = 2/5 the kernel is
span{ψ, ψ̄} and at x < 2/5 D is indefinite, so the balanced set is then a nontrivial face/hypersurface.
The reviewed text says "empty **there**", which is correct, but the statement must not be
generalized in the write-up.

**Claim 4(iii) (the load-bearing, previously only asserted claim) — CONFIRMED, with my own proof
(§3) plus symbolic and 60-digit numeric verification (G6a–c, G6d/diag, N4).** Two corrections of
detail, neither affecting the conclusion: (a) **SO(3) alone** is transitive on the isotropic
stratum — the U(1) factor named in the claim is redundant (D depends on ψ only through P_ψ);
(b) the transport is by O ∈ O(3) on the input side **and by V = 1 ⊕ det(O)·O on the environment
index** — the det(O) sign is required for reflections and should be stated in any write-up.
"One representative suffices" is therefore true unconditionally.

**Claim 5 (consistency) — CONFIRMED.** d_1 ≤ 0 on [2/5, 1) (G5e), so no first-order isotropic
ascent exists anywhere in the region where Q = 0 is PROVED ([1/2,1), frozen input P2/P4) — the
necessary coherence check passes; and the x = 9/20 datum matches the closed form exactly (G5b).
I note for the record that this is a **consistency** check, not evidence for the onset value: the
closed form would have to fail on [1/2,1) to be refuted here, and it does not.

---

## 6. Supersession adjudication (claim 3) — verdict and exact defect localization

**Verdict: the supersession is correct. `tools/whgap_p6b_v2_isotropic.py`'s d_1 = 1 − x is
genuinely wrong; the replacement's closed forms are right.** My grounds are stronger and more
specific than the artifact's, and are unconditional:

1. **The superseded Π_E is not the projector onto ker Λ^c(P_ψ) at all**, and the script's *own*
   gates say so: `projector_checks.annihilates_environment_output = false` and
   `analytic_basis_in_kernel = false` in `logs_whgap_p6b_20260729/v2_isotropic.json`. An operator
   that fails the defining property cannot define w_E; no appeal to the (unreviewed) expansion
   lemma is needed to reject its output.
2. **Root cause, localized (new in this review; `tools/whgap_r5c_supersession_diag.py`,
   `r5c_supersession_diag.log`).** That script works at ψ′ = (0, 1, −i)/√2 = (u + iv)/√2 with
   u = e_2, **v = −e_3**, so **u × v = −e_1**. It nevertheless passes `w_third = (1,0,0) = +e_1`
   and records `"third_is_u_cross_v": true`, which is **false**. Its analytic environment-kernel
   vector k_2 = (1, −iκ·third), κ = √(2(1−x)/x), therefore carries the wrong sign: I verified at
   x ∈ {1/5, 9/20, 3/4} that k_1 = (0, √2 ψ̄) **is** in ker Λ^c(P_ψ′), that
   k_2 with +e_1 **is not**, and that k_2 with u × v = −e_1 **is**. (Structurally this is standing
   failure mode 4: the kernel of the Gram matrix Λ^c(P_ψ)_{ab} = ⟨v_b, v_a⟩ is the *conjugate* of
   the dependency space, so the sign/conjugation of the K_0-mixing direction is exactly the place
   an error lands.)
3. **Exact reproduction and repair.** Using the script's own convention (third = +e_1) I reproduce
   its published numbers exactly at x = 9/20: diag(−99/620, **11/20**, **−99/155**) — i.e.
   d_1 = 1 − x = 11/20 and d_2 = 4d_0 ≠ 0, matching `v2_isotropic.json` entry for entry. Flipping
   **only** that sign (third = u × v) restores diag(−99/620, −11/124, 0). Nothing else in that
   script had to change: its M_B, its M_E assembly Σ_{ab}(Π_E)_{ab}K_a^†K_b, and its basis are
   all correct.
4. **The correct closed form also holds at the superseded script's own ψ′** (three rational x:
   (−4/45, 4/9, 0) at 1/5; (−99/620, −11/124, 0) at 9/20; (−3/20, −7/20, 0) at 3/4) — consistent
   with the transport claim 4(iii), since ψ′ is another point of the same SO(3)-orbit.
5. **Identity behind the wrong value:** 1 − x = d_1 + 4κ (G8d). A Π_E missing the whole
   K_0 ↔ K_3 mixing contribution 4κP_ψ̄ yields exactly d_1 = 1 − x — I verified that the
   hypothetical rank-1 Π_E (only the e_3-block direction) gives diag(0, 1−x, 0) (G8e). The
   superseded script's error is a *rotated* version of this: it retains a second direction, but
   the wrong one, which also drives d_2 off zero.

**On the arbitration reasoning as written (minor m2).** The artifact/node justify the supersession
by (i) "d_1 = 1−x > 0 would place a first-order ascent at proved-zero x ≥ 1/2 — impossible given
the expansion lemma pattern" and (ii) agreement of the replacement with the earlier P9b datum.
(i) is *conditional* on the very expansion lemma that is still unreviewed, and (ii) is agreement
between two unreviewed computations; neither is a proof that the superseded object is wrong.
The conclusion is nonetheless correct, and items 1–3 above give the unconditional reason.
Recommendation to the decision layer: record item 1 (its own Π_E fails Π_EΛ^c(P_ψ) = 0) and
item 2 (the `third` sign) as the reason on the node's append-only history, so the retired script's
defect is not re-litigated.

**One further finding about a retired-but-on-disk audit (minor m3).** The superseded script also
contains an audit *of P9b*: `p9b_pi_e_audit.raw_sum_equals_true_projector = false`, insinuating
that P9b's Π_E (a sum of normalized rank-one projectors over sympy's raw nullspace basis) is not
the orthogonal projector. That audit compares P9b's projector against the **defective** pi_e and
is therefore void; its own neighbouring field records `raw_basis_mutually_orthogonal: true`, which
already implies the sum *is* the orthogonal projector. My independent computation confirms P9b's
value diag(−99/620, −11/124, 0) is correct. The false doubt should be explicitly annulled where
the append-only history cites `v2_isotropic.json`.

---

## 7. Standing failure-mode screen (7e; §2 of the commission, item by item)

1. **`.H`/unresolved conjugates on real-symbolic matrices.** Screened, and it bit my own first
   attempt. Resolved structurally by the (a,b)-parameterization: no conjugate is ever stripped by
   hand in my scripts. I audited the authors' stripping: `whgap_p6b_v2_fable.py::realify` removes
   `conjugate(u)` for **any** I-free u, which is unsound in general (e.g. `conjugate(sqrt(x−2))`
   would be stripped although sqrt(x−2) is imaginary for x < 2) and is sound **here** only because
   every stripped radical (√(1−x), √(x/2), √(1−x/2), positive numerics) is a positive real on
   x ∈ (0,1). Because my conjugate-free route reproduces the same D symbolically, the stripping
   did **not** corrupt the reviewed result. Recorded as minor m1.
2. **WindowsApps store python.** Not used; every run in this review is the pinned
   `C:<home>/cpython3119/python.exe` (recorded in both JSONs).
3. **Complement convention drift.** Screened: padded 4×4 throughout, Λ^c(Y)_{ab} = Tr(K_aYK_b^†),
   trace-preserving (G1e), Kraus normalization K_0 = √(1−x)1, K_{μ+1} = √(x/2)A_μ verified against
   the closed-form channel on all 9 Hermitian directions (G1c). No k-factor or a(Y)-block sign
   enters my construction.
4. **Transpose vs conjugate-transpose.** Screened explicitly: K real ⟹ K^† = K^T verified as a
   property, not assumed; the duality derivation keeps K_a^† and only then substitutes K_a^T; and
   the Gram-kernel-vs-dependency-space conjugation is exactly the defect I localized in §6.
5. **`sorted()` on symbolic eigenvalues.** Screened: all spectra are sorted as strings after
   mapping to x, never as symbolic comparisons.
6. **CRLF in SHA256SUMS.** Screened: `SHA256SUMS_r5c.txt` written with LF (file(1) reports "ASCII
   text", no CRLF) and verified with `sha256sum -c` (12/12 OK).
7. **Degeneracy / near-zero-gap bookkeeping.** Screened: my verification is exact/symbolic, so no
   interval enclosures or spectral-gap divisions occur. Degeneracies noted: at x = 1/2,
   d_0 = d_1 = −1/6; at x = 2/5, ker D becomes 2-dimensional; rank Λ^c(P_ψ) = 2 holds on all of
   (0,1) but the x/2 eigenvalue closes onto the kernel as x → 0⁺ (irrelevant for fixed x > 0,
   relevant to any future uniform-in-x perturbation statement — flagged for R5d).
8. **ε log ε bookkeeping.** Out of R5c scope by construction; I did not certify any expansion.
   N5 is labelled corroboration of the sign convention only. I do record the structural fact that
   makes claim 1 the right object: rank Λ^c(ρ_ε) = 4 for faithful ρ_ε (the four Kraus operators
   are linearly independent), so both kernel eigenvalues are O(ε) and the full 2-dim Π_E trace is
   the correct leading weight.
9. **Anchoring.** Screened; see §1 including the declared unavoidable exposure and the
   coincidence flag.

**Quantifier hygiene (7g).** Terms of art in the reviewed claims resolve as follows: "isotropic"
= τ(ψ) = |ψ^Tψ| = 0 (commission §1); "weight operator" = the unique Hermitian D with
Tr[Dφ] = w_B(φ) − w_E(φ) for all Hermitian φ (existence/uniqueness by the orthonormal-basis
reconstruction, G4c); "balanced layer" = {states φ : Tr[Dφ] = 0} (node's N1′-b);
"(N1′-a)" = ∀ isotropic ψ, ∀ states φ: w_B ≤ w_E (node). "First-order isotropic ascent" is
defined only *through* the unreviewed expansion lemma — within R5c it can be read purely as
"max_φ(w_B − w_E) > 0", and I verified only that reading. **Frozen-input scope (7d):** I relied on
P2/P4 (Q = P = 0 on [1/2,1)) solely for the consistency check of claim 5, and on nothing else;
I did not treat any pending-review claim as established, and in particular the ε log ε expansion,
the "candidate exact onset x_D = 2/5", and "Q > 0 on (0,2/5)" are **not** reviewed here.

---

## 8. Findings

**MAJOR: none.**

**Minors (none of them affects the claims licensed below):**

- **m1 — unsound-in-general conjugate stripping in the accepted script.**
  `tools/whgap_p6b_v2_fable.py::realify` (and its ancestor in the superseded script) strips
  `conjugate(u)` for every I-free u. Sound only under x ∈ (0,1); it should carry that hypothesis
  in-code and must not be reused as a general utility. My conjugate-free route confirms the
  reviewed result is uncontaminated.
- **m2 — the written supersession rationale is conditional.** It leans on the unreviewed expansion
  lemma and on agreement with another unreviewed datum. The unconditional reason (the superseded
  Π_E fails Π_EΛ^c(P_ψ) = 0; root cause = the `third` = +e_1 vs u × v = −e_1 sign) should replace
  it on the node.
- **m3 — a void audit is on disk.** `logs_whgap_p6b_20260729/v2_isotropic.json`'s
  `p9b_pi_e_audit.raw_sum_equals_true_projector: false` compares P9b's projector to the defective
  one and should be explicitly annulled; P9b's Π_E and its datum are correct (verified here).
- **m4 — scope of "the balanced layer is empty".** True at x = 9/20 and, as a formula, on
  x ∈ (2/5, 1); at x = 2/5 ker D = span{ψ, ψ̄} and for x < 2/5 D is indefinite. Any write-up must
  carry the range.
- **m5 — two wording corrections in claim 4(iii)/the node.** "SO(3)×U(1)" → SO(3) suffices
  (stabilizer trivial; D depends only on P_ψ); "transports D_ψ unitarily" → orthogonally, with the
  environment index transported by V = 1 ⊕ det(O)·O (the det factor is needed for reflections).
  Also: the P9b stereographic chart's omitted point was covered "by continuity"; the transitivity
  proof in §3 removes that hand-wave and should be cited in its place.
- **m6 — reproducibility note on my own run.** Gate G6d in `r5c_weight_operator.log` is flagged
  FAIL for computer-algebra reasons only (unnormalized nested radicals); it is resolved by
  `r5c_transport_diag.log` (exact vanishing at 4 independent (a,b) points × 4 rotations) and by
  numeric gate N4. The script exits 1 for that reason; the mathematics is not in doubt. Disclosed
  so no later reader mistakes the exit code for a substantive failure.

---

## 9. Verdict (7g — exactly one licensing statement from the R5c menu)

**(A) LICENSE.** *The isotropic weight operator closed form (claims 1–2) is PROVED as an algebraic
identity* — here symbolically in x (not merely at points), by my own independent construction
(functional reconstruction on a complete Hermitian basis, plus an exact projector-algebra hand
proof, plus a 60-digit numeric route whose Π_E comes from a Hermitian eigendecomposition), and
additionally confirmed at c = 6 rational x including 9/20 and 499/1000; *the supersession
(claim 3) is correctly adjudicated* — with the defect now localized unconditionally to the
`third` = +e_1 vs u × v = −e_1 sign error that puts the superseded Π_E off the kernel; *and the
digestion claims 4(i), (ii), (iii) hold*, with 4(iii) now carrying a proof (SO(3)-transitivity on
the isotropic stratum + covariance transport D_{Oψ} = O D_ψ O^T with V = 1 ⊕ det(O)·O) rather than
an assertion. Claim 5's consistency check also holds.

**Scope of this license, stated explicitly:** it covers the algebra of D at the isotropic stratum
and the group-theoretic reduction to one representative. It does **not** cover the ε log ε
expansion lemma, the identification of w_B − w_E as the Ic(ρ_ε) leading coefficient, the candidate
onset x_D = 2/5, or Q(Λ_x) > 0 on (0, 2/5) — all of which remain with E-N1/R5d. The minors above
are wording/hygiene items for the decision layer and do not qualify the licensed claims.

**Rule-2/6 note:** I write no status anywhere. Per the single-writer deviation, the decision layer
must link this artifact from `WHGAP.no-ascent-hierarchy` (Adversarial reviews + Evidence) in the
same session it is read (rule 8c), and only then apply any status write.

---

## 10. Provenance

Scripts (all new, all mine, under `tools/`):
`whgap_r5c_weight_operator.py`, `whgap_r5c_numeric_gates.py`, `whgap_r5c_transport_diag.py`,
`whgap_r5c_supersession_diag.py`.
Logs and machine JSON: `artifacts/logs_whgap_r5_20260729/r5c_weight_operator.{log,json}`,
`r5c_numeric_gates.{log,json}`, `r5c_transport_diag.{log,json}`,
`r5c_supersession_diag.{log,json}`.
Hash manifest: `artifacts/logs_whgap_r5_20260729/SHA256SUMS_r5c.txt` (LF; `sha256sum -c` 12/12 OK).

Reviewed inputs, as frozen by the commission: `artifacts/whgap_p6b_necessity_20260729.md` §V2;
`tools/whgap_p6b_v2_fable.py` (read only); `tools/whgap_p6b_v2_isotropic.py` (superseded) and
`artifacts/logs_whgap_p6b_20260729/v2_isotropic.{log,json}`;
`artifacts/logs_whgap_p9b_20260729/g0_repaired_derivation.json`; the node's "Decision-layer
digestion of P9b" and "P6b-V2 outcome" sections. Frozen inputs relied upon: P2/P4 (Q = P = 0 on
[1/2,1)) for claim 5 only.

Script SHA-256:
```
ea1925513964ff67579545749a2fa51923e5bffae10a2024643ebfd823cefcfe  tools/whgap_r5c_weight_operator.py
e029b0a6c31a98f2e53b64ed75191c4c235fb49062bc263508d952d57b06a013  tools/whgap_r5c_numeric_gates.py
f4959b0809f71c538c9f17419452b855993771855ab519b2119be14de0414a38  tools/whgap_r5c_transport_diag.py
01775c164cee1fbd67feb2794cc12e3b6e74c739a41ef6aa75641ee8b3c734f6  tools/whgap_r5c_supersession_diag.py
```
Each hash is the version of the script that produced the corresponding log in this manifest (the
transport diagnostic was trimmed to suppress an oversized debug print and then re-run; only the
re-run version is hashed and logged).

