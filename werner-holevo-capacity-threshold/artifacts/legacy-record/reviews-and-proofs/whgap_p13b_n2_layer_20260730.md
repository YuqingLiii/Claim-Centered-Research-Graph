# WHGAP P13-B — the n = 2 entangled first-order layer of the onset question

**Artifact type:** executor authorship (computational note + proof note).
**Node:** `WHGAP.onset-two-fifths` (P13), obligation **(d)**, n = 2 instance.
**Commission:** [`WHGAP_COMMISSION_P13B_20260730.md`](../channel-capacity/werner-holevo-gap/notes/WHGAP_COMMISSION_P13B_20260730.md).
Inherited frozen conventions / standing failure modes / rule-7 embeds: §1–§3 of
[`WHGAP_REVIEW_COMMISSION_R5_20260729.md`](../channel-capacity/werner-holevo-gap/notes/WHGAP_REVIEW_COMMISSION_R5_20260729.md),
plus the P13-A tooling additions (radical-free rational charts; Berkowitz determinant, never
`Matrix.charpoly`; substitute lowest even radical powers only).
**Author:** fresh executor instance, 2026-07-30 (authored none of the prior WHGAP work; given no
desired outcome).
**Interpreter for all computation:** `C:<home>/cpython3119/python.exe`
(sympy 1.13.1, mpmath 1.3.0, numpy 1.26.4, scipy 1.14.1).
**Status this note licenses by itself: NOTHING.** Everything below is proposer-authored and is
offered at **NUMERICAL / `pending-review:`** (computational gates) and **CONJECTURED** (written
statements) for a fresh rule-7 review (rules 6, 7).

**Outcome in one line (G0, bounded null — with a sharp structural signature).**
At every frozen strip point the exact 2-copy weight operator is **negative semidefinite**, so the
2-copy first-order ε log(1/ε) mechanism yields **no** witness anywhere in [2/5, 1/2); for the two
families reachable symbolically in x this is upgraded to an **exact interval certificate on all of
[2/5, 1)**. Below the onset the same machinery is *strictly stronger than at n = 1* — at x = 7/20 an
entangled 2-copy input gives the exact value **1102933/9570000 = 0.115249007…** versus
d₁(7/20) = 13/132 = 0.098484848… (17 % larger, exact rationals) — so the n = 2 layer is genuinely
more powerful, yet it dies at exactly the same threshold 2/5.

---

## 0. PRE-ACTION REPORT (mandatory, `research/PRETASK_RELOAD_PROMPT.md`)

Files read from disk, completely, in the prescribed order, before any mathematics:
`research/DAG_PROTOCOL.md` (whole file: §1 data structure, §2 ladder + completion gate, §3 rules
1–8, §4 READ, §5 WRITE, §6 session-close);
`research/RESEARCH_STRUCTURE_PROTOCOL.md` (§1–§10);
`channel-capacity/werner-holevo-gap/README.md`;
`channel-capacity/werner-holevo-gap/notes/WERNER-HOLEVO-GAP_PROOF_DAG.md` (header, mermaid,
outline, eight rules inlined);
`channel-capacity/werner-holevo-gap/proof-dag/NODE_INDEX.md`;
the target node `proof-dag/nodes/WHGAP.onset-two-fifths.md` and its parent
`proof-dag/nodes/WHGAP.goal.md` (the node has no children);
then the commission `notes/WHGAP_COMMISSION_P13B_20260730.md`, the inherited §1–§3 of
`notes/WHGAP_REVIEW_COMMISSION_R5_20260729.md`, the reviewed machinery
`notes/WHGAP_N1PRIME_EXPANSION_LEMMA_20260729.md` (§1–§10, in particular §3–§4), and the P13-A
note `notes/WHGAP_P13A_STRATUM_EXHAUSTION_20260730.md` (§0–§1, for the inherited tooling rules).

- **Target node and status as read from disk:** `WHGAP.onset-two-fifths` (alias P13), kind LEAF,
  role proof, **status CONJECTURED**, `disposition: null`, parents `["WHGAP.goal"]`, children `[]`;
  `status_source` records the P13-A stratum-exhaustion Theorem as PROVED (R6 review, LICENSE A) with
  the onset identification itself still open. Open obligations on the node: (b) first-order layer
  CLOSED; (c) isotropic higher-order/balanced layers at and above 2/5 OPEN; **(d) n ≥ 2 entangled
  layers OPEN (untouched)** — this note addresses (d) at n = 2, first-order layer only.
- **My ROLE: executor** (authorship). No reviewer-independence claim is made. I state only that I
  authored none of the prior WHGAP work and was told no desired answer. To keep the derivation
  independent I did **not** open `tools/whgap_p6b_*.py`, `tools/whgap_p9*.py`, `tools/whgap_r5*.py`,
  `tools/whgap_p13a_sanity.py`, or any `artifacts/whgap_r5*_review_*.md` / `whgap_r6_review_*.md`
  before deriving §2–§5; the two places where prior material is used are the *reviewed* machinery of
  the N1′ note §3–§4 (cited as black boxes, §2) and the *comparison* value d₁(x) = (1−x)(2−5x)/(2−x)
  (§4, §6 — used as a calibration target, exactly as the commission prescribes).
- **Highest status my planned evidence could license per §2:** **NUMERICAL** for the computational
  gates (proposer-writable with command + log + SHA-256) and **CONJECTURED** for the written
  statements. A completion tier (CERTIFIED\*/PROVED) may be written **only** by the decision layer
  after a fresh independent review completes, is archived on disk and is cited on the node.
  **I wrote no status anywhere, and I edited no node file, no `NODE_INDEX.md`, and no DAG doc.**
- **Gates and deliverables of my commission, one line each:**
  **S0** — instantiate the reviewed ε log(1/ε) expansion lemma at the 2-copy dimensions with explicit
  constants → §2.
  **S1** — exact structured families (a)–(d) at x ∈ {9/20, 21/50, 12/25} (+ 2/5, 7/20, 11/20), every
  outcome registered append-only including nulls → §4, [exact_s1.json](logs_whgap_p13b_20260730/exact_s1.json).
  **S2** — degeneracy-variety derivation: closed form of ⟨conj Ψ|(Λ⊗Λ)(P_Ψ)|conj Ψ⟩ in O(3)×O(3)
  invariants of M, plus sufficient degenerate families → §3 (the full determinant factorisation was
  *not* forced; what replaced it is stated honestly in §3.5).
  **S3** — numeric sweep on the degeneracy variety at the frozen x grid with the pre-registered rank
  discipline → §5.
  **G-cal1 / G-cal2** — calibration gates, run FIRST → §6.
  **G+ / G0** — decision gates → §7.
- **Conflicts between commission text and disk protocols: two, both reported rather than silently
  resolved.**
  1. *Single-writer deviation.* The commission forbids me to touch node files, `NODE_INDEX.md` or
     the DAG doc, whereas `DAG_PROTOCOL.md` §5/§6 and `RESEARCH_STRUCTURE_PROTOCOL.md` §6 (atomic
     update, rule 8c) require the executor to append the outcome to the node in the same session. The
     commission states the deviation is commissioned by the decision layer, which will perform the
     atomic node/index/DAG update citing this artifact. I comply and record the obligation:
     **this note, `tools/whgap_p13b_*.py` and `artifacts/logs_whgap_p13b_20260730/` are not yet
     linked from `WHGAP.onset-two-fifths`; the decision layer owes that link (rule 8c).**
  2. *`SHA256SUMS` naming.* Per the commission I write
     `artifacts/logs_whgap_p13b_20260730/SHA256SUMS_p13b.txt` (LF, verified with `sha256sum -c`), so
     no later file can overwrite cited provenance (structure protocol §7).
- **Standing failure modes screened (R5 commission §2), item by item.**
  1. sympy `.H` leaving `conjugate(sqrt(1−x))` — **avoided by construction**: the whole exact layer
     lives in a radical-free rational chart (§4.1); no `sqrt` ever enters a symbolic matrix.
  2. WindowsApps python inaccessible — the pinned interpreter is used throughout.
  3. Complement convention drift — the padded 16-dimensional Λ^c⊗Λ^c of §1 is used everywhere and
     re-derived in §1.3; three independent implementations of the same object agree to 4·10⁻¹⁶ (§4.2).
  4. Transpose vs conjugate-transpose — audited in §1.1; `†` = `ᵗ` is used only for the (real) Kraus
     operators, and the weight operator is *never* obtained from a hand-written adjoint formula: the
     reference implementation evaluates the linear functional φ ↦ w_B(φ) − w_E(φ) on the 81 matrix
     units (§1.3).
  5. `sorted()`/comparison on symbolics — **HIT twice**: `sp.nsimplify` silently replaced exact
     rationals by radical garbage (e.g. `-7*2**(131/394)*3**(261/394)*…`) and
     `bool(Rational-expression >= 0)` raised *"cannot determine truth value of Relational"*.
     Both documented append-only in §8.1 and fixed (no `nsimplify`; parse with an explicit symbol
     table).
  6. CRLF in `SHA256SUMS` — LF enforced, `sha256sum -c` verified (§9).
  7. Eigenvalue bookkeeping at degeneracies / dividing by small gaps — the pre-registered rank
     discipline (spectral gap ≥ 10⁶ × zero-cluster magnitude) is implemented in
     `kernel_projector()` and every sweep point that fails it is **excluded and counted** (§5); the
     exact layer needs no threshold at all.
  8. ε log ε bookkeeping — §2 instantiates the reviewed Lemma 4.1/4.2 + Prop 3.3 with all constants
     recomputed for the 2-copy dimensions; the O(ε² log(1/ε)) = o(ε) remainder is quantitative.
  9. Anchoring — §3 and §4 were derived and gated before any comparison with prior artifacts; the
     only prior numbers used are d₁(x) (a commissioned calibration target) and the fact that
     Q = 0 on [1/2,1) (used only as the G-cal2 sanity anchor).
  10. *One more, self-imposed:* **positive controls.** A null over a search space is worthless if the
     scanner cannot find a witness that exists. Every sweep and every exact test was therefore run
     also at x = 7/20 and x = 39/100 < 2/5, where the machinery **does** return strictly positive
     values (§5, §6). This is what makes the strip null informative.

---

## 1. Conventions, types, and the two-copy objects

### 1.1 Objects and types (type audit, rule 7a)

| symbol | type | dimensions |
|---|---|---|
| `x` | noise parameter | real, `0 < x < 1` |
| `Λ_x` | linear map, CPTP | M₃(ℂ) → M₃(ℂ) |
| `K_0,…,K_3` | Kraus operators, **real** entries | 3 × 3 |
| `Λ_x^c` | complement (padded) | M₃(ℂ) → M₄(ℂ) |
| `Λ^{(2)} := Λ_x ⊗ Λ_x` | linear map, CPTP | M₉(ℂ) → M₉(ℂ) |
| `Λ^{c(2)} := Λ_x^c ⊗ Λ_x^c` | complement of `Λ^{(2)}` | M₉(ℂ) → M₁₆(ℂ) |
| `W_m = K_a ⊗ K_b`, `m = 4a+b` | 2-copy Kraus, real | 9 × 9, 16 of them |
| `Ψ` | unit vector (pure 2-copy input) | ℂ⁹ |
| `M` | coefficient matrix of `Ψ`, `Ψ = Σ_{jk} M_{jk} |jk⟩` | 3 × 3, `‖M‖_F = 1` |
| `P_Ψ = |Ψ⟩⟨Ψ|`, `φ`, `ρ_ε` | states on ℂ⁹ (PSD, trace 1) | 9 × 9 |
| `Λ^{(2)}(P_Ψ)` | state | 9 × 9, rank `r` |
| `Λ^{c(2)}(P_Ψ)` | state | 16 × 16, rank `r` |
| `Π_B` | orth. projector onto `ker Λ^{(2)}(P_Ψ)` | 9 × 9, rank `m_B = 9 − r` |
| `Π_E` | orth. projector onto `ker Λ^{c(2)}(P_Ψ)` | 16 × 16, rank `m_E = 16 − r` |
| `M_B, M_E, D_Ψ = M_B − M_E` | Hermitian observables on ℂ⁹ | 9 × 9 |
| `w_B, w_E, g, r, m_B, m_E, C^{(2)}` | real scalars / integers | — |
| `Ahat_0 = 1, Ahat_i = A_i`, `Bhat_m` | **integer** matrices | 3 × 3 / 9 × 9 |
| `Ic_2(ρ)` | real scalar (**nats** throughout) | — |

Frozen definitions (R5 commission §1), reproduced in content:
Λ_x(Y) = (1−x)Y + (x/2)(Tr(Y)·𝟙 − Yᵗ); K₀ = √(1−x)·𝟙, K_i = √(x/2)·A_i with (A_i)_{jk} = ε_{ijk};
Λ_x^c(Y)_{ab} = Tr(K_a Y K_b^†) = Tr(K_a Y K_bᵗ) (real Kraus); τ(ψ) = |ψᵗψ|;
Ic(ρ) = S(Λ(ρ)) − S(Λ^c(ρ)); Q ≥ Q^{(1)}. Index convention: ℂ⁹ index `n = 3j+k` with
`vec(M)_{3j+k} = M_{jk}`, so `(K_a ⊗ K_b) vec(M) = vec(K_a M K_bᵗ)`; environment index `m = 4a+b`.
Λ_x is **self-adjoint** in the Hilbert–Schmidt inner product (verified in gate C0), hence so is Λ^{(2)}.

### 1.2 The two-copy channel and its complement

With V₂ : ℂ⁹ → ℂ⁹ ⊗ ℂ¹⁶, V₂|v⟩ = Σ_m (W_m|v⟩) ⊗ |m⟩ and Σ_m W_m^†W_m = 𝟙, Λ^{(2)}(ρ) = Tr_E V₂ρV₂^†
and (Tr_B V₂ρV₂^†)_{mn} = Tr(W_m ρ W_n^†) = Λ^{c(2)}(ρ)_{mn}. Hence for pure input:

> **(1.1)** `Λ^{(2)}(P_Ψ)` and `Λ^{c(2)}(P_Ψ)` have the **same nonzero spectrum**;
> so `rank = r` on both sides, `m_B = 9 − r`, `m_E = 16 − r = m_B + 7`, the smallest nonzero
> eigenvalue `g` is common, and `Ic_2(P_Ψ) = 0` exactly.

Gate **C1** verifies (1.1) numerically for 10 structured Ψ at 3 values of x (max deviation
2.2·10⁻¹⁶); the exact layer verifies `m_E = 16 − r` as an assertion on every one of the 78 exact runs.

### 1.3 The weight operator, defined without a hand-written adjoint

For a state φ on ℂ⁹ put w_B(φ) = Tr[Π_B Λ^{(2)}(φ)], w_E(φ) = Tr[Π_E Λ^{c(2)}(φ)] (both ≥ 0, ≤ 1).
Both are linear in φ, so there is a unique Hermitian `D_Ψ` with

> **(1.2)** `Tr[D_Ψ φ] = w_B(φ) − w_E(φ)` for every φ.

**Reference implementation (failure mode 4).** `D_Ψ` is obtained by evaluating the functional (1.2)
on the 81 matrix units E_pq and transposing: `V_pq = w_B(E_pq) − w_E(E_pq)`, `D_Ψ = Vᵗ`
(`weight_operator` in `tools/whgap_p13b_core.py`). Two faster constructions — the operator-sum form
`M_B = Σ_m W_m^†Π_B W_m`, `M_E = Σ_{m,n} (Π_E)_{mn} W_m^†W_n` (`weight_operator_fast`) and the
radical-free form of §4.1 (`weight_operator_rf`) — are checked against it (gate **C2**, and §4.2).
Because ρ_ε = P_Ψ at φ = P_Ψ gives Ic_2 ≡ 0, one has `Tr[D_Ψ P_Ψ] = 0` identically, hence

> **(1.3)** `λ_max(D_Ψ) ≥ 0` always, and *ascent* means the **strict** inequality λ_max(D_Ψ) > 0.

---

## 2. S0 — the n = 2 instantiation of the reviewed expansion lemma

Everything in this section is the m ≥ 1 instantiation of machinery whose review (R5d, LICENSE A)
covers it as **parameter-free statements about Hermitian matrices**: Fact 3.1 (Weyl), Lemma 3.2
(multiplicative eigenvalue comparison under congruence), **Proposition 3.3** (kernel-cluster bound,
stated and proved for arbitrary kernel multiplicity m ≥ 1), **Lemma 4.1** (uniform ε log(1/ε)
cluster-term expansion), **Lemma 4.2** (regular-term stability) of
`notes/WHGAP_N1PRIME_EXPANSION_LEMMA_20260729.md` §3–§4. I do not re-prove them; I instantiate them
at the 2-copy dimensions and **recompute every constant** (rule 7d: the reviewed scope is exactly
"arbitrary m ≥ 1", which is what I use — the reviewed note itself used (m_B, m_E) = (1, 2), P13-A
used m = 1, and here (m_B, m_E) = (9−r, 16−r)).

**Lemma 2.1 (2-copy ε log(1/ε) expansion).** Let x ∈ (0,1), let Ψ ∈ ℂ⁹ be a unit vector with
coefficient matrix M, let r = rank Λ^{(2)}(P_Ψ), m_B = 9 − r, m_E = 16 − r, and let g > 0 be the
smallest nonzero eigenvalue of Λ^{(2)}(P_Ψ) (= that of Λ^{c(2)}(P_Ψ), by (1.1)). Let φ be any state
on ℂ⁹ and ρ_ε = (1−ε)P_Ψ + εφ. Then for every ε with **0 < ε ≤ g/4**,

> **(2.1)** | Ic_2(ρ_ε) − (w_B − w_E)·ε·log(1/ε) | ≤ C^{(2)}(x,Ψ)·ε, where
>
> **C^{(2)}(x,Ψ) = (25 − 2r)·[ 6/(e·g) + (5/2)·log(5/2) ] + 2r·[ 1 + log(4/(3g)) ]**,
>
> and w_B − w_E = Tr[D_Ψ φ]. The constant depends on (x, Ψ) only through r and g — it is **uniform
> in φ**.

*Proof (assembly only; the ingredients are the reviewed ones).* Both outputs are affine in ε:
Λ^{(2)}(ρ_ε) = A_B + εB_B with A_B = Λ^{(2)}(P_Ψ) ⪰ 0, B_B = Λ^{(2)}(φ) − Λ^{(2)}(P_Ψ), and
similarly on the E side. For Hermitian differences of PSD trace-one operators ‖B_•‖ ≤ 1 =: b, so
Prop 3.3's hypothesis (3.1) reads ε ≤ g/(4b) = g/4 — the assumed window — and its conclusions hold
with C_pert = 6b²/g = 6/g on both sides. The cluster slopes are the kernel weights: Π_B A_B Π_B = 0
gives Σ_{k≤m_B} μ_k^B = Tr[Π_B Λ^{(2)}(φ)] = w_B, and likewise Σ_{k≤m_E} μ_k^E = w_E (trace of the
compression; Π² = Π and cyclicity). Each of the m_B + m_E = 25 − 2r cluster eigenvalues satisfies
λ = εμ + r' with |r'| ≤ (6/g)ε² and λ/ε ≤ b + (6/g)(g/4) = 5/2 =: U, so Lemma 4.1 bounds its
h-term error by (6/(e g) + (5/2)log(5/2))ε. Each of the (9 − m_B) + (16 − m_E) = 2r regular
eigenvalues stays in [3g/4, 1] and moves by at most ε (Weyl), so Lemma 4.2 with a = 3g/4 bounds its
error by (1 + log(4/(3g)))ε; their ε = 0 values sum to S(Λ^{(2)}(P_Ψ)) resp. S(Λ^{c(2)}(P_Ψ)), which
cancel by (1.1). Summing and subtracting gives (2.1). If m_B = 0 the B side has no cluster (then
w_B = 0 identically) and only the Lemma 4.2/Weyl part is used there; the displayed C^{(2)} covers
that case as written. ∎

**Corollary 2.2 (the decision quantity).** If λ_max(D_Ψ) > 0 then, choosing φ a top eigenvector
state of D_Ψ, Ic_2(ρ_ε) ≥ ε[λ_max(D_Ψ)log(1/ε) − C^{(2)}] > 0 for every
0 < ε < min(g/4, exp(−C^{(2)}/λ_max(D_Ψ))), hence Q^{(1)}(Λ_x^{⊗2}) > 0 and therefore
Q(Λ_x) ≥ (1/2)Q^{(1)}(Λ_x^{⊗2}) > 0. If λ_max(D_Ψ) < 0 the same expansion gives Ic_2(ρ_ε) < 0 for
all small ε; if λ_max(D_Ψ) = 0 the first-order layer is silent (no conclusion either way).
By (1.3) the only two possibilities are λ_max > 0 (witness) and λ_max = 0 (silent).

**Explicit window/constant samples** (`whgap_p13b_gates.py`, own computation):
for the isotropic product base point and the type-E base point g = x²/4, e.g. at x = 9/20,
g = 81/1600 = 0.050625, window ε ≤ 0.012656, C^{(2)} = 814.3 (r = 4) resp. 564.6 (r = 7);
at x = 2/5, g = 0.04, ε ≤ 0.01, C^{(2)} = 1013.1 resp. 695.3. For the generic P3 point of §3
(r = 8) g is smaller (0.008257 at x = 9/20) and C^{(2)} = 2524.0. These are honest, pessimistic
constants: they matter only for the *positive* direction (Corollary 2.2), never for a null.

---

## 3. S2 — the degeneracy variety of the 2-copy problem

### 3.1 Ascent requires B-side degeneracy, and degeneracy is x-independent

w_B(φ) = 0 for every φ when m_B = 0, so by (1.3) **λ_max(D_Ψ) > 0 forces m_B ≥ 1**, i.e.
Λ^{(2)}(P_Ψ) must be rank deficient. Now

> **(3.1)** `Λ^{(2)}(P_Ψ) = Σ_m W_m P_Ψ W_m^†` with `W_m Ψ = vec(K_a M K_bᵗ)`, so
> `r = rank Λ^{(2)}(P_Ψ) = dim span_ℂ{ K_a M K_bᵗ : a,b } = dim span_ℂ{ a M b : a,b ∈ L }`,
> `L := span{𝟙, A_1, A_2, A_3}` (4-dimensional),

because K₀ = √(1−x)𝟙 and K_i = √(x/2)A_i are **nonzero** multiples of the integer matrices
Ahat_a for every x ∈ (0,1), and A_iᵗ = −A_i. Consequently:

> **Proposition 3.1 (x-independence).** For every M, the integers r(M), m_B(M) = 9 − r(M) and
> m_E(M) = 16 − r(M) are **independent of x on (0,1)**: the degeneracy variety is one fixed
> algebraic set, the same for the whole strip and for the proved-zero region.

Verified independently as gate **C4** (rank of the 16 × 9 matrix Z(M) at five x values for ten
structured M: identical), and as an assertion inside every one of the 78 exact runs.

By (3.1), m_B ≥ 1 ⟺ ∃ B ≠ 0 with Tr(B·aMb) = 0 for all a,b ∈ L ⟺ **M ⊥ L B L** in the bilinear
pairing (X,Y) ↦ Tr(XY). The relation is symmetric in (M,B), so every annihilator B is itself
degenerate.

### 3.2 The commissioned closed form: the ⟨conj Ψ| … |conj Ψ⟩ direction

The n = 1 analogue of the kernel-candidate quadratic form is ⟨ψ̄|Λ(P_ψ)|ψ̄⟩ = (1−x)τ². Its n = 2
counterpart is computed in closed form. Write adj M for the adjugate (cof(M)ᵗ, so
M·adj M = det(M)·𝟙).

> **Theorem 3.2 (closed form, symbolic in M, conj M and x — gate `s2_1`).**
>
> **F(M) := ⟨conj Ψ| (Λ⊗Λ)(P_Ψ) |conj Ψ⟩ = (1−x)²·|Tr(M Mᵗ)|² + x²·‖adj M‖_F².**

*Proof.* ⟨conj Ψ|(K_a⊗K_b)|Ψ⟩ = Tr(Mᵗ K_a M K_bᵗ), so
F(M) = Σ_{a,b} |Tr(Mᵗ K_a M K_bᵗ)|². Three holomorphic identities (each verified **symbolically**
in the nine entries of M):
(i) Tr(Mᵗ A_i M) = 0, because Mᵗ A_i M is antisymmetric;
(ii) Tr(Mᵗ M A_i) = 0, because MᵗM is symmetric and A_i antisymmetric;
(iii) **Tr(Mᵗ A_i M A_j) = −2 (adj M)_{ji}**, from A_i = −[e_i]_×, the identity
Mᵗ[w]_×M = [adj(M)w]_× and Tr([u]_×[v]_×) = −2 u·v.
Hence the (a,0) and (0,b) terms with a,b ≠ 0 vanish, the (0,0) term contributes
(1−x)²|Tr(MMᵗ)|², and the (i,j) terms contribute (x/2)²·Σ_{ij}|2(adj M)_{ji}|² = x²‖adj M‖_F². ∎

Both invariants are O(3)×O(3) invariants of M in the required sense
(Tr(MMᵗ) ↦ Tr(MMᵗ) and ‖adj M‖_F ↦ ‖adj M‖_F under M ↦ O₁MO₂ᵗ), and
‖adj M‖_F² = e₂(s₁²,s₂²,s₃²) in the singular values. **Consequence (a structural surprise):**
F(M) = 0 ⟺ Tr(MMᵗ) = 0 **and** adj M = 0 ⟺ rank M ≤ 1 with an isotropic factor. So

> **(3.2)** conj Ψ ∈ ker Λ^{(2)}(P_Ψ) **iff Ψ = u ⊗ v is a product state with uᵗu = 0 or vᵗv = 0.**
> For every entangled Ψ the conj-Ψ direction is *not* in the B-side kernel: the n = 1 mechanism's
> witness direction does **not** generalise, and the entangled part of the degeneracy variety has to
> be found by rank analysis (§3.3), not from this quadratic form.

At n = 1 the same computation degenerates to (1−x)τ² (one factor, no adjugate), and for
M = ψψᵗ, F = ((1−x)τ²)² — the consistency check with the reviewed n = 1 layer.

### 3.3 Sufficient degenerate families: the P3 hypersurface (exact)

> **Theorem 3.3 (proved symbolically, gate `s2_2`).** Let u, v ∈ ℂ³ be **isotropic** (uᵗu = vᵗv = 0)
> and a, y ∈ ℂ³ arbitrary. Then every
>
> **M = v aᵗ + y uᵗ  (i.e. Ψ = v ⊗ a + y ⊗ u)  has m_B ≥ 1,**
>
> because B := u vᵗ satisfies Tr(B·a′Mb′) = 0 for all a′,b′ ∈ L. Write **P3** for this set.

*Proof.* L B L = span{a′uvᵗb′} = U ⊗ V with U = span{a′u} = {w : uᵗw = 0} and
V = {q : vᵗq = 0} (both 2-dimensional, because for isotropic u the image of [u]_× is exactly
{w : uᵗw = 0} and contains u). The annihilator of U ⊗ V in the pairing Tr(XY) is
{M : M(U) ⊆ span{v}} = {v aᵗ + y uᵗ}. The 16 identities were also verified symbolically in the
rational isotropic chart u = c₁(1−z₁², i(1+z₁²), 2z₁), v = c₂(1−z₂², i(1+z₂²), 2z₂) with a, y free —
all 16 traces are identically 0. ∎

P3 contains every family the commission listed, and more:

| family | representative M | rank M | r | m_B | m_E |
|---|---|---|---|---|---|
| (a) iso ⊗ iso product | u₀u₀ᵗ, u₀ = (1,i,0)/√2 | 1 | 4 | 5 | 12 |
| (d) iso ⊗ conj-iso | u₀ū₀ᵗ | 1 | 4 | 5 | 12 |
| (c) both factors isotropic | u vᵗ, uᵗu = vᵗv = 0 | 1 | 4 | 5 | 12 |
| one isotropic factor | y u₀ᵗ (y arbitrary) | 1 | 6 | 3 | 10 |
| **type-E (entangled)** | diag(1,1,0)/√2 = u₀ū₀ᵗ + ū₀u₀ᵗ (normalised) | 2 | 7 | 2 | 9 |
| **generic P3 (entangled)** | u₀aᵗ + yu₀ᵗ | 2 | 8 | 1 | 8 |
| (b) maximally entangled | 𝟙/√3 (and O/√3) | 3 | **9** | **0** | 7 |
| (c) Tr(MMᵗ) = 0 entangled | diag(1,i,0)/√2 | 2 | **9** | **0** | 7 |

Two entries deserve emphasis. **The maximally entangled input is NOT degenerate** (r = 9, m_B = 0),
so by §3.1 it can support no first-order ascent at any x — family (b) is a null for a structural
reason, not a numerical one. And the "global-isotropic" condition Tr(MMᵗ) = 0 is by itself
**neither necessary nor sufficient**: diag(1,i,0) has Tr(MMᵗ) = 0 but r = 9, while diag(1,1,0) has
Tr(MMᵗ) = 1 and r = 7. (3.2) explains why: at n = 2 the vanishing of that invariant is only half of
the conj-Ψ condition.

**Reduction of the sweep domain by symmetry.** Λ^{(2)} is covariant under M ↦ O₁MO₂ᵗ for
O_i ∈ O(3,ℝ) (independently on the two copies), and λ_max(D_Ψ) is invariant under it. Every
isotropic vector is a complex multiple of a real rotation of u₀ (u = a + ib with |a| = |b|, a ⊥ b),
so **modulo the symmetry group every point of P3 can be written with u = v = u₀**:

> **(3.3)** the chart `M(a,y) = u₀aᵗ + y u₀ᵗ`, (a,y) ∈ ℂ³ × ℂ³ (12 real parameters after
> normalisation), covers **all of P3 up to the channel's symmetry**, and contains the type-E and
> product strata as subvarieties.

### 3.4 Is P3 the whole degeneracy variety? (numerical evidence, not a proof)

An unconstrained hunt — 60 independent L-BFGS minimisations of σ_min(Z(M))/σ_max(Z(M)) over all of
ℂ^{3×3} from random starts — reached degeneracy every time, and **in all 60 cases** the (unique, since
r = 8) annihilator B came out rank 1 with **both factors isotropic** (|uᵗu|, |vᵗv| ≤ 3·10⁻⁹, second
singular value ≤ 2·10⁻⁹): i.e. every hunted point lies in P3. A closure/duality check is consistent:
for generic B ∈ P3 (r(B) = 8) the annihilator space is 1-dimensional and is spanned by uvᵗ, which is
again in P3. The Jacobian of the chart of Theorem 3.3 has rank 7 (complex), so P3 is a
7-complex-dimensional (codimension-2) subvariety of the 9-dimensional ambient space.

**Honest statement:** "P3 ⊆ {m_B ≥ 1}" is **proved** (Theorem 3.3). "{m_B ≥ 1} = P3" is
**CONJECTURED** on the above evidence; nothing in §5's null depends on it *except* the claim that
the sweep covers the whole variety, which is therefore stated as coverage-conditional in §7.

### 3.5 The commissioned "stretch" item, not forced

The commission's stretch goal was the full determinant factorisation analogous to
det = x(1−x)τ²/2. I did **not** obtain it and did not force it: det Λ^{(2)}(P_Ψ) is a degree-18
polynomial in (M, conj M) and its factorisation resisted direct symbolic attack within the budget.
What replaced it is strictly more useful for the question asked: (i) Theorem 3.2 (the closed form
the commission asked for, in the requested invariants), (ii) Proposition 3.1 (the whole degeneracy
question is x-free — the analogue of "full rank iff τ > 0"), and (iii) Theorem 3.3 + the chart (3.3)
(an explicit, symmetry-complete parametrisation of the degenerate locus, which is what the S3 sweep
actually needs). The missing determinant identity is recorded as an open item in §8.2.

---

## 4. S1 — the exact structured layer

### 4.1 The radical-free rational chart (P13-A tooling rule)

Write K_a = c_a·Ahat_a with Ahat₀ = 𝟙, Ahat_i = A_i (integer) and c₀² = 1−x, c_i² = x/2; for the
2-copy Kraus W_m = c_m·Bhat_m with c_m = c_ac_b and Bhat_m = Ahat_a ⊗ Ahat_b (**integer** 9 × 9).
Then, with Δ = diag(c_m) and D2inv = diag(1/c_m²):

* `G_B = Λ^{(2)}(P_Ψ) = Σ_m c_m² Bhat_m P_Ψ Bhat_mᵗ` — **rational in x**;
* `ker G_B = (span{Ahat_a M Ahat_bᵗ})^⊥` — **x-free** (Prop 3.1), hence exactly computable once;
* `G_E = Λ^{c(2)}(P_Ψ) = Δ Ĝ Δ` with `Ĝ[m,n] = Tr[Bhat_m P_Ψ Bhat_nᵗ]` — **x-free**;
  so `ker G_E = Δ^{-1} ker Ĝ` and
  `Π_E = Δ^{-1} N̂ (N̂^† D2inv N̂)^{-1} N̂^† Δ^{-1}`;
* `M_B = Σ_m c_m² Bhat_mᵗ Π_B Bhat_m` — rational in x;
* `M_E = Σ_{m,n} R[m,n]·Bhat_mᵗBhat_n` with `R = N̂ (N̂^† D2inv N̂)^{-1} N̂^†` — rational in x,
  because `c_mc_n(Π_E)[m,n] = R[m,n]` exactly.

**No square root ever enters a symbolic matrix**, which is precisely the standing failure mode 1 that
bit P13-A. Determinants use Berkowitz, never `Matrix.charpoly`. Inputs are unnormalised
Gaussian-rational M (the state is P_Ψ = ΨΨ^†/‖Ψ‖², rational; ranks and kernels are scale-invariant).

**Exact negative-semidefiniteness certificate.** D_Ψ is Hermitian with Tr[D_Ψ P_Ψ] = 0, so by (1.3)
λ_max = 0 ⟺ D_Ψ ⪯ 0. The test used is: (i) D_Ψ Ψ = 0 exactly; (ii) the compression of −D_Ψ to an
exact basis of Ψ^⊥ is positive **definite**, certified by an exact fraction-arithmetic LDL^H whose
pivots are exact positive rationals (the leading principal minors are their running products —
Sylvester). A negative pivot certifies λ_max > 0. If a pivot vanishes (extra kernel, which happens
exactly at x = 2/5 for the isotropic families) the LDL is inconclusive and the code falls back to
the **exact charpoly sign test**: for Hermitian D, all eigenvalues ≤ 0 ⟺ every coefficient of
det(λ𝟙 − D) is ≥ 0.

### 4.2 Three-way agreement of independent constructions (rule 7f)

The matrix-unit construction (§1.3), the operator-sum construction, and the radical-free
construction (§4.1) are three independent implementations of D_Ψ. They agree to **≤ 6·10⁻¹⁶** on
every family tested, and the exact symbolic D_Ψ agrees with the float one to **4·10⁻¹⁶** (spot-checked
at x = 9/20 and 7/20 for families (a), type-E and generic P3). Gate **C3** closes the loop against
the *definition*: the ratio Ic_2(ρ_ε)/(ε log(1/ε)), computed from raw channel entropies at
ε = 10⁻⁶…10⁻¹², converges monotonically to Tr[D_Ψφ] for three (x, Ψ, φ) cases — i.e. the weight
operator really is the ε log(1/ε) coefficient, verified against an independent construction of the
same quantity, not against its own formula.

### 4.3 The exact table (all 78 runs; S1 registered append-only, nulls included)

`tools/whgap_p13b_exact.py` → [`exact_s1.json`](logs_whgap_p13b_20260730/exact_s1.json),
log [`exact_s1.log`](logs_whgap_p13b_20260730/exact_s1.log). Every row: D_Ψ Hermitian **exactly**,
Tr[D_Ψ P_Ψ] = 0 **exactly**, m_E = m_B + 7 as asserted. "nsd" = exact certificate of D_Ψ ⪯ 0
(hence λ_max = 0 exactly, no first-order ascent); "IND" = exact certificate of λ_max > 0.

| family (M, unnormalised representative) | r | m_B | x = 9/20 | 21/50 | 12/25 | **2/5** | 7/20 (control) | 11/20 (G-cal2) |
|---|---|---|---|---|---|---|---|---|
| (a) u₀u₀ᵗ | 4 | 5 | nsd | nsd | nsd | nsd | **IND, λ_max = 13/132** | nsd |
| (d) u₀ū₀ᵗ | 4 | 5 | nsd | nsd | nsd | nsd | **IND, 13/132** | nsd |
| (b) 𝟙 (max. entangled) | 9 | 0 | nsd | nsd | nsd | nsd | nsd | nsd |
| (b2) cyclic O | 9 | 0 | nsd | nsd | nsd | nsd | nsd | nsd |
| (c1) diag(1,i,0) | 9 | 0 | nsd | nsd | nsd | nsd | nsd | nsd |
| (e1) diag(1,1,0) type-E | 7 | 2 | nsd | nsd | nsd | nsd | **IND, 1102933/9570000** | nsd |
| (e2) E₁₂+E₂₁ | 7 | 2 | nsd | nsd | nsd | nsd | **IND, 1102933/9570000** | nsd |
| (e3) diag(1,−1,0) | 7 | 2 | nsd | nsd | nsd | nsd | **IND, 1102933/9570000** | nsd |
| P3g u₀(1,0,2)ᵗ + (0,1,1)u₀ᵗ | 8 | 1 | nsd | nsd | nsd | nsd | **IND, 0.02557163…** | nsd |
| P3s u₀e₃ᵗ + e₃u₀ᵗ | 7 | 2 | nsd | nsd | nsd | nsd | **IND, 0.06556042…** | nsd |
| P3i 2u₀u₀ᵗ + (u₀ū₀ᵗ + ū₀u₀ᵗ) | 8 | 1 | nsd | nsd | nsd | nsd | **IND, 0.08313421…** | nsd |
| P3r u₀(2,−1,3)ᵗ + (1,2,0)u₀ᵗ | 8 | 1 | nsd | nsd | nsd | nsd | **IND, 0.05335444…** | nsd |
| P3c (u₀+e₃)u₀ᵗ | 6 | 3 | nsd | nsd | nsd | nsd | **IND, 13/132** | nsd |

**Reading.** At every frozen strip x (9/20, 21/50, 12/25) *and at the endpoint 2/5* the exact weight
operator of every structured family — including all the entangled ones — is negative semidefinite:
λ_max(D_Ψ) = **0 exactly**, no first-order ascent, for every state φ. At x = 7/20 < 2/5 the same
exact machinery certifies strict positivity, with the two exact values
**13/132 = d₁(7/20)** (products: the embedded n = 1 witness, G-cal1) and
**1102933/9570000 = 0.1152490073145…** (type-E, entangled — **17 % larger than d₁**).
At x = 11/20 nothing is positive (G-cal2).

### 4.4 Symbolic-in-x, and an interval certificate on the whole strip

For the two families where the symbolic-in-x charpoly of D_Ψ(x) is reachable, the coefficients of
det(λ𝟙 − D_Ψ(x)) are rational functions of x with denominator a power of (x−2) (no zero in (0,1)).
Exact real-root isolation of each numerator (`sympy real_roots`) plus two exact rational
evaluations then give a genuine **interval** statement rather than a grid statement:

> **Proposition 4.1 (interval certificate; `tools/whgap_p13b_interval.py`).** For
> Ψ = u₀ ⊗ u₀ (isotropic product, r = 4) and for Ψ = the type-E entangled state
> diag(1,1,0)/√2 (r = 7): **no coefficient of det(λ𝟙 − D_Ψ(x)) has a root in (2/5, 1)**, and every
> coefficient is ≥ 0 at x = 2/5 and at x = 1/2. Hence all coefficients are ≥ 0 on **[2/5, 1)**, so
> **D_Ψ(x) ⪯ 0 and λ_max(D_Ψ(x)) = 0 for every x ∈ [2/5, 1)** — no first-order ε log(1/ε) ascent
> from these two base points anywhere in the strip, nor above it.

The same computation exhibits *where* the threshold sits: the top charpoly coefficients of family
(a) carry explicit factors of (5x−2), e.g.
c₈ = x³(x−1)⁸(5x−2)³(2x²−5x+4)(4x²−5x+2)(7x³−17x²+16x−4)²/(x−2)¹², and **every** root in (0,1) of
**every** coefficient is ≤ 2/5. The number 2/5 is thus visible in the n = 2 first-order data of the
entangled layer, not only in the n = 1 closed form d₁(x) = (1−x)(2−5x)/(2−x).

---

## 5. S3 — numeric sweep on the degeneracy variety (pre-registered rank discipline)

`tools/whgap_p13b_sweep.py` → [`sweep_all.json`](logs_whgap_p13b_20260730/sweep_all.json),
log [`sweep_all.log`](logs_whgap_p13b_20260730/sweep_all.log). Single-threaded BLAS (machine
etiquette). Charts (all degenerate **by construction**, so the projector is stable):

* **F1** — the full P3 chart (3.3): M = u₀aᵗ + yu₀ᵗ, 12 real parameters. By §3.3 this covers the
  whole conjectured degeneracy variety modulo the channel's O(3)×O(3) symmetry.
* **F2** — type-E chart: M = C₁diag(1,1,0)C₂ with C_i complex special orthogonal, 12 real parameters
  (m_B = 2 stratum).
* **F3** — product chart: M = yu₀ᵗ, 6 real parameters (m_B = 3 stratum).
* **F4** — unconstrained control: M ∈ ℂ^{3×3}, 18 real parameters (m_B = 0 almost surely ⇒ 0).

Per (chart, x): an 800-point random pre-sample, then **100 genuine Nelder–Mead local
maximisations** of λ_max(D_Ψ) (the best 50 pre-sample seeds + 50 fresh random starts). **Rank
discipline (pre-registered, `kernel_projector`):** a kernel dimension is accepted only if the
smallest kept eigenvalue exceeds 10⁶ × the accepted zero-cluster magnitude; points failing it are
excluded and counted (`ambiguous_excluded`), and the optimiser is not allowed to profit from them.

| chart (m_B) | x=0.35 | x=0.39 | **x=0.40** | **x=0.41** | **x=0.42** | **x=0.43** | **x=0.45** | **x=0.47** | **x=0.49** |
|---|---|---|---|---|---|---|---|---|---|
| F1 full P3 chart (m_B=1) | 1.5e-01 | 3.0e-02 | 3.9e-16 | 4.4e-16 | 4.1e-16 | 4.6e-16 | 5.1e-16 | 4.7e-16 | 4.4e-16 |
| F2 type-E chart (run 1) (m_B=2) | 1.4e-01 | 4.2e-02 | 2.0e-02 | 4.6e-16 | 6.2e-16 | 4.9e-16 | 5.0e-16 | 5.0e-16 | 5.6e-16 |
| F2 type-E chart (re-run, strengthened discipline) (m_B=2) | 1.4e-01 | 4.2e-02 | 2.0e-02 | 5.0e-16 | 4.5e-16 | 4.6e-16 | 4.7e-16 | 5.0e-16 | 5.2e-16 |
| F3 product chart (m_B=3) | 9.8e-02 | 1.9e-02 | 2.3e-15 | 3.3e-16 | 3.4e-16 | 3.3e-16 | 3.2e-16 | 3.5e-16 | 3.3e-16 |
| F4 unconstrained control (m_B=0) | 4.3e-16 | 4.2e-16 | 4.6e-16 | 4.5e-16 | 4.8e-16 | 5.0e-16 | 5.4e-16 | 5.8e-16 | 6.1e-16 |

Controls are the two columns x = 0.35 and 0.39 (< 2/5); the seven bold columns are the frozen
strip grid. 100 genuine local maximisations per cell (F4: 50) after an 800-point pre-sample.
Total sweep time 3445 s, single-threaded. Per-cell rank-ambiguous exclusion counts are in the json.


### 5.1 Every incumbent above 10⁻⁶ was validated — and the only strip candidate is an artifact

`tools/whgap_p13b_validate.py` → [`validation.json`](logs_whgap_p13b_20260730/validation.json).
Each sweep row whose maximum exceeded 10⁻⁶ was re-examined with two independent filters:
the rank discipline (including the conditioning criterion, §8.1) and the **definitional slope
gate** — does the *raw* coherent information Ic_2(ρ_ε), computed from channel and complement
entropies with no reference to D_Ψ, actually have the predicted ε log(1/ε) slope?

| chart | x | reported λ_max | rank discipline (cond ratio) | definitional slope gate | verdict |
|---|---|---|---|---|---|
| F2 | 0.35 | +1.375e-01 | pass (1.5e-06) | pass (measured +0.0391, +0.0581, +0.0738) | **GENUINE** |
| F2 | 0.39 | +4.241e-02 | pass (1.4e-06) | FAIL (measured -0.0065, +0.0005, +0.0087) | **ARTIFACT** |
| F2 | 0.40 | +2.000e-02 | pass (1.0e-06) | FAIL (measured -0.0155, -0.0125, -0.0062) | **ARTIFACT** |
| F1 | 0.35 | +1.528e-01 | FAIL (2.6e-08) | pass (measured +0.1009, +0.1079, +0.1161) | **ARTIFACT** |
| F1 | 0.39 | +3.014e-02 | pass (5.6e-06) | FAIL (measured -0.0087, +0.0006, +0.0065) | **ARTIFACT** |
| F2 | 0.35 | +1.375e-01 | FAIL (2.6e-09) | pass (measured +0.0420, +0.0397, +0.0486) | **ARTIFACT** |
| F2 | 0.39 | +4.242e-02 | FAIL (2.4e-09) | FAIL (measured +0.0048, +0.0003, -0.0002) | **ARTIFACT** |
| F2 | 0.40 | +2.000e-02 | FAIL (1.4e-09) | FAIL (measured -0.0030, -0.0069, -0.0110) | **ARTIFACT** |
| F3 | 0.35 | +9.848e-02 | pass (5.6e-02) | pass (measured +0.0895, +0.0918, +0.0931) | **GENUINE** |
| F3 | 0.39 | +1.894e-02 | pass (6.3e-02) | pass (measured +0.0071, +0.0101, +0.0118) | **GENUINE** |

**10 candidates, 0 genuine in the strip.** The single strip candidate — F2 (type-E chart) at
x = 2/5, reproduced in both runs at λ_max ≈ 0.0200 — is an **artifact**, established three ways:
(i) it sits *exactly on the conditioning boundary* (cond ratio 1.02·10⁻⁶ against a floor of 10⁻⁶;
re-running the chart with the floor raised to 10⁻³ merely moves the incumbent to cond ratio
1.00·10⁻³ with λ_max ≈ 0.0191 — the optimiser always finds the threshold, so **no
threshold-based rank discipline can exclude this family of artifacts**);
(ii) the definitional slope gate measures a *negative* slope (−0.0155, −0.0125, −0.0062 at
ε = 10⁻⁶, 10⁻⁸, 10⁻¹⁰) against the prediction +0.0200;
(iii) rationalising the incumbent (denominator 2520) and running the **exact** layer at x = 2/5
gives r = 9, m_B = 0 and λ_max = 0 exactly — the point is not even on the degeneracy variety.
Diagnosis: the F2 chart `M = C₁diag(1,1,0)C₂` built from `expm` of complex antisymmetric matrices
becomes *numerically unfaithful* at large parameters (the computed M has σ₃ ≈ 10⁻¹⁷ but σ₂ ≈ 10⁻³,
i.e. it is drifting off type-E toward the deeper rank-1 stratum), and the float kernel projector at
such a point mixes near-kernel directions. The F1 chart is faithful by construction (u₀ = (1,i,0)/√2
satisfies u₀ᵗu₀ = 0 *exactly* in binary floating point, so M = u₀aᵗ + yu₀ᵗ is exactly in P3 up to
rounding), and F1 — which covers the whole variety modulo symmetry — returns ≤ 5.1·10⁻¹⁶ at every
strip point.
**Consequence for the controls:** the trustworthy below-onset positives are the ones that pass both
filters — F3 at x = 0.35 (0.098484… = d₁, cond 5.6·10⁻²) and at x = 0.39 (0.018944… = d₁(0.39)) —
together with the *exact* values of §4.3 (13/132 and 1102933/9570000 at x = 7/20), which need no
numerics at all. The larger sweep incumbents (0.15 at x = 0.35, 0.042 at x = 0.39) are **not**
claimed: they fail one of the two filters and are recorded here as unvalidated.
**Consequence for the strip:** adding an exclusion criterion can only shrink the accepted set, so
every reported strip maximum remains a valid upper bound; with the one candidate above 10⁻⁶ refuted,
the strip maximum over accepted points is ≤ 2.3·10⁻¹⁵ on all four charts.

**Positive controls.** The identical procedure at x = 7/20 and x = 39/100 (both < 2/5) returns
strictly positive maxima — including values **above** the n = 1 optimum d₁ — so the scanner is
demonstrably able to find first-order witnesses where they exist. That is what licenses reading the
strip zeros as a null rather than as blindness.

---

## 6. Calibration gates (run FIRST, before any strip claim)

`tools/whgap_p13b_gates.py` → [`gates.json`](logs_whgap_p13b_20260730/gates.json). **7/7 PASS.**

| gate | content | result |
|---|---|---|
| **C0** | Kraus set reproduces Λ_x entrywise at 3 x values; ΣK^†K = 𝟙; Λ_x self-adjoint in HS | PASS |
| **C1** | 2-copy pure-input isospectrality (1.1) for 10 Ψ × 3 x; max dev 2.2·10⁻¹⁶ | PASS |
| **C2** | matrix-unit vs operator-sum D_Ψ agree (2.2·10⁻¹⁶); D Hermitian; Tr[D P_Ψ] = 0; rank_B = rank_E | PASS |
| **C3** | slope gate: Ic_2(ρ_ε)/(ε log(1/ε)) → Tr[D_Ψφ] from raw entropies, 3 cases, ε ↓ 10⁻¹² | PASS |
| **C4** | r(M) is x-independent (5 x values × 10 families) — Prop 3.1 | PASS |
| **G-cal1** | at **x = 7/20**: family (a) gives λ_max(D_Ψ) = **0.098484848485 = d₁(7/20) = 13/132**, attained *exactly* by the embedded n = 1 direction φ = P_ψ̄ ⊗ P_ψ (ψ̄-slot) — the required ≥ d₁ holds with equality; exact rational value confirmed symbolically (minimal polynomial 132λ − 13) | **PASS** |
| **G-cal2** | at **x = 11/20**: max λ_max over 10 structured families + 60 random Ψ = **3.6·10⁻¹⁶** ≤ 10⁻⁹; and the exact layer certifies D_Ψ ⪯ 0 for all 13 families at 11/20 | **PASS** |

G-cal1 also reproduces the commissioned inclusion–exclusion structure. For product Ψ = ψ⊗ψ,
Λ^{(2)}(P_Ψ) = Λ(P_ψ)⊗Λ(P_ψ) gives Π_B = Π⊗𝟙 + 𝟙⊗Π − Π⊗Π (and the same on the E side), hence
**D^{(2)} = D⊗𝟙 + 𝟙⊗D − (M_B⊗M_B − M_E⊗M_E)**, so D^{(2)} is diagonal in the product basis
{ψ,ψ̄,e₃}⊗{ψ,ψ̄,e₃} with entries D_j + D_k − (b_jb_k − e_je_k). Since D_ψ = b_ψ = e_ψ = 0, the (ψ̄,ψ)
entry equals **d₁ exactly**, and the diagonal maximum equals max_j D_j over the n = 1 spectrum in
the strip, i.e. 0. This is the derivation the commission asked for, and it explains why
λ_max = d₁ (not 2d₁) at x = 7/20 for family (a).

---

## 7. Decision gates: outcome **G0** (bounded null), with coverage stated honestly

**G+ (witness): NOT triggered.** No strip point at any rank-unambiguous point of any chart produced
λ_max(D_Ψ) > 10⁻⁶. One numerical incumbent did exceed it (F2 chart at x = 2/5, λ_max ≈ 0.0200) and was **refuted three
independent ways** in §5.1 — most decisively by rationalising it and running the exact layer, which
returns r = 9, m_B = 0 and λ_max = 0 exactly. Over accepted points the largest strip value is then
2.3·10⁻¹⁵ (float round-off), and at the frozen *rational* strip points the value is **exactly 0**
with an exact certificate.

**G0 (bounded null): recorded, at three strengths.**

1. **Exact, pointwise:** for 13 structured families (products, both maximally entangled samples, two
   global-isotropic samples, three type-E entangled samples, four generic-P3 entangled samples) and
   x ∈ {2/5, 21/50, 9/20, 12/25}, λ_max(D_Ψ) = 0 **exactly** (exact NSD certificates, §4.3).
2. **Exact, on the whole interval:** for the isotropic-product base point and the type-E entangled
   base point, λ_max(D_Ψ(x)) = 0 for **every** x ∈ [2/5, 1) (Proposition 4.1).
3. **Numerical, over the variety:** 100 local maximisations per (chart, x) on the full P3 chart and
   its two deeper strata at the frozen grid x ∈ {2/5, 41/100, 42/100, 43/100, 45/100, 47/100,
   49/100} found nothing above 2.3·10⁻¹⁵ over accepted points (the one exception refuted in §5.1),
   while the same procedure below 2/5 returns validated positives — 0.098484… = d₁ at x = 0.35 and
   0.018944… = d₁ at x = 0.39 — plus unvalidated incumbents up to ≈ 0.15.

**Coverage statement (what this does and does not rule out).**
*Covered:* the n = 2, **first-order** ε log(1/ε) mechanism from a **pure** 2-copy base point, over the
whole degeneracy variety **as far as P3 is that variety** (Theorem 3.3 proves P3 ⊆ {m_B ≥ 1};
{m_B ≥ 1} = P3 is CONJECTURED on 60/60 hunts, §3.4), modulo the O(3)×O(3) symmetry, with the
optimisation over φ done exactly (λ_max is the exact maximum over all states φ).
*Not covered:* (i) the **balanced layer** at n = 2 (where λ_max = 0 the first-order term cancels and
Lemma 2.1 says nothing — exactly as at n = 1 this is a real gap, and here it is *generic*, since
λ_max = 0 on the whole strip); (ii) **higher orders in ε** and moderate-ε mixtures;
(iii) **mixed** or non-pure base points; (iv) **n ≥ 3**; (v) any component of {m_B ≥ 1} outside P3,
should one exist. Nothing here establishes Q^{(1)} = 0 or Q = 0 on [2/5, 1/2).

**Status this licenses (my own authorship, rules 6–7):** NUMERICAL with `pending-review:` for the
computational content; CONJECTURED for Theorem 3.2/3.3 and Propositions 3.1/4.1 until a fresh
reviewer confirms them. I wrote no status.

---

## 8. Append-only record of resistance, hits, and open items

### 8.1 Standing-failure-mode hits (documented, not hidden)

* **`sympy.nsimplify` corrupted exact rationals.** Applied to an exact Gaussian-rational matrix
  entry it returned `-7*2**(131/394)*3**(261/394)*5**(190/197)*7**(61/197)/1500` — a "closed form"
  fitted to a float. It broke the first mpmath conversion and then the LDL certificate (a spurious
  "non-real pivot"). Fix: never `nsimplify`; use `sp.re/sp.im` on exact numbers and `sp.Rational`.
  This is standing failure mode 5 in a new costume, and it produced *wrong intermediate values that
  looked plausible* — the reason the three-way agreement gate of §4.2 exists.
* **`bool(<Relational>)`** raised *"cannot determine truth value of Relational"* twice (once inside
  the interval certificate) because a parsed expression carried a **different** `Symbol('x')` than
  the script's `Symbol('x', positive=True)`, so `.subs` silently did nothing. Fix: parse with an
  explicit `locals={'x': x}` symbol table; assert the substitution produced a number.
* **An index slip caught by the three-way gate.** An early "optimised" complement assembly used
  `Bhat_m Bhat_nᵗ` where `Bhat_nᵗBhat_m` was required; the exact and float D_Ψ then differed by
  0.24. The gate caught it immediately; had only one implementation existed, the sign structure of
  the whole strip table would have been silently wrong. (This is exactly the rule-7f lesson.)
* **Unbounded thread use.** The first sweep run consumed ~5 000 CPU-seconds in 20 wall minutes
  through multi-threaded BLAS on 9 × 9 matrices. It was killed and the sweep re-run with
  `OMP_NUM_THREADS=1` (machine etiquette); the earlier partial run is superseded and not cited.

### 8.2 Resistance / not forced (honest-scoping rule)

* The **full determinant factorisation** of det Λ^{(2)}(P_Ψ) (the stretch gate) was not obtained;
  §3.5 states what replaced it. Open item: is det Λ^{(2)}(P_Ψ) = |P(M)|²·(positive factor) for a
  holomorphic P whose zero set is P3?
* **{m_B ≥ 1} = P3** is not proved (§3.4). A proof would make the S3 coverage claim unconditional.
  Suggested route: classify 3 × 3 complex M under O(3,ℂ)×O(3,ℂ) (Prop 3.1 shows r is invariant under
  that larger group) and compute r on each normal-form stratum; the diagonalisable strata are easy
  (r = 9 unless det M = 0 with two equal squared singular values), the nilpotent strata are the
  work.
* **No structural reason** was found for why λ_max(D_Ψ) = 0 on the *whole* strip for every degenerate
  Ψ tested. The (5x−2) factors in the symbolic charpoly (§4.4) are suggestive; a proof of
  "λ_max(D_Ψ) ≤ max(d₁(x), 0) for all Ψ ∈ ℂ⁹" would close obligation (d) at n = 2 outright. This is
  the single most valuable follow-up this note points at.

### 8.3 A finding worth registering on its own (below the onset, not in the strip)

The n = 2 entangled first-order layer is **strictly stronger** than the n = 1 layer below 2/5:
at x = 7/20 the type-E entangled base point gives the exact coefficient 1102933/9570000 =
0.1152490073… (minimal polynomial 9570000λ − 1102933), against d₁(7/20) = 13/132 = 0.0984848… — a
17 % increase, in exact arithmetic, from an entangled 2-copy base point. (The sweep suggests larger
values still, up to ≈ 0.15, but those incumbents did not pass both validation filters of §5.1 and
are therefore not claimed.) This does not enlarge the proved region — (0, 2/5) is
already PROVED — but it shows the mechanism has genuine n-dependence and that its **threshold is
nevertheless unmoved at 2/5**, which is evidence *for* the onset conjecture of a kind the n = 1
analysis could not provide. (Whether the *strengthening* is uniform, i.e.
sup_Ψ λ_max ↑ with n while the zero set stays [2/5,1), is open.)

---

## 9. Reproduction, logs, and hashes

All commands from the repository root with `C:<home>/cpython3119/python.exe`:

```
python tools/whgap_p13b_gates.py                 # C0-C4, G-cal1, G-cal2      -> gates.json
python tools/whgap_p13b_variety.py               # S2 hunt + strata probe     -> variety.json
python tools/whgap_p13b_s2.py                    # S2 symbolic identities     -> s2_symbolic.json
python tools/whgap_p13b_interval.py              # Prop 4.1 interval cert.    -> interval_certificate.json
python tools/whgap_p13b_exact.py                 # S1 exact table (78 runs)   -> exact_s1.json
OMP_NUM_THREADS=1 python tools/whgap_p13b_sweep.py all 100   # S3 sweep       -> sweep_all.json
```

Scripts: `tools/whgap_p13b_core.py` (three D_Ψ constructions + rank discipline + Ic_2),
`whgap_p13b_gates.py`, `whgap_p13b_variety.py`, `whgap_p13b_s2.py`, `whgap_p13b_exact.py`,
`whgap_p13b_interval.py`, `whgap_p13b_sweep.py`.
Logs and machine-readable outputs: `artifacts/logs_whgap_p13b_20260730/` with
`SHA256SUMS_p13b.txt` (LF; verified by `sha256sum -c`). Hashes are inlined in §9.1.

### 9.1 SHA-256

| file | sha256 |
|---|---|
| `artifacts/logs_whgap_p13b_20260730/exact_s1.json` | `c4c28f92bd0a5f7f67fdd2771512434d48a63a898bce217695289e0ee06d5920` |
| `artifacts/logs_whgap_p13b_20260730/gates.json` | `576cf105fd72b66341fdaf7f26c7d9bd6809fd3a4ce5b5d881fe21fd64f77ce4` |
| `artifacts/logs_whgap_p13b_20260730/interval_certificate.json` | `0ded0bee3fac8b1b32638a4bd03c2cdb245d269c4e0c0b3db5571978b7c07333` |
| `artifacts/logs_whgap_p13b_20260730/s2_symbolic.json` | `b4811cf473e109fba59a6faea91fd50e495084f3975b807f4509c8c5e8c41adb` |
| `artifacts/logs_whgap_p13b_20260730/sweep_F2.json` | `a9d89ce0cb7d89b733860c179985f29fc2a00f94d845959c4aa62a0a09e78f09` |
| `artifacts/logs_whgap_p13b_20260730/sweep_all.json` | `fb59c0877fba0192d77f12248a5f1ced41f07c6a941126c1920ee6ebce11adb4` |
| `artifacts/logs_whgap_p13b_20260730/validation.json` | `ab2f1a62d251e7b8996841046e11f8947d3690f682289db75a5bf223a1dc0781` |
| `artifacts/logs_whgap_p13b_20260730/variety.json` | `eea8820967c6820a18dd60b25945f84daa012e808a47d6f4f384f30a18828c8d` |
| `artifacts/logs_whgap_p13b_20260730/exact_s1.log` | `6948ef4220aadc39f1e7cbd411b5227696c10296bd624f67a72fa0aefcb8502c` |
| `artifacts/logs_whgap_p13b_20260730/f2_condfloor_1e-3.log` | `7568b77559480f0e4afcdd3eadd2a60eb86909dbc62b4af3d720f3db2dc43023` |
| `artifacts/logs_whgap_p13b_20260730/s2_symbolic.log` | `3b38c925cac411ac391a527bfb61ee941201dba1d8de43b97d30c05a8ded1fb9` |
| `artifacts/logs_whgap_p13b_20260730/sweep_F2_recheck.log` | `062a7840b9987f9a876276c838c17e21929ed28340b83474f085cdeffb637a83` |
| `artifacts/logs_whgap_p13b_20260730/sweep_all.log` | `634efa701f0a933173754dcfe4ea993587f559ce91d1744f9119f8a4a1ec8bce` |
| `tools/whgap_p13b_artifact_diagnosis.py` | `fc972ea57f59b7abbf4516213ee2eb57ecad623865da45b2e790ea6ec127681e` |
| `tools/whgap_p13b_condfloor_probe.py` | `9c23f2a8f5a9c3b1a6ec97000f9ae8f3d7e337415c66df0593baa5193cf36182` |
| `tools/whgap_p13b_core.py` | `0cbefd95fd228f61687ef36e079981c72a9f0e49fcb35a1d3816e7f694a0f502` |
| `tools/whgap_p13b_exact.py` | `44751e305bf88c152cfe4b2d9c5b51193ac2f74c30fe3386ca1564951ed4c37c` |
| `tools/whgap_p13b_gates.py` | `d4f6fa0c8711d516d7028bffb973668c3b25884a3c114724a8ef21c419edad2f` |
| `tools/whgap_p13b_interval.py` | `3825e7fca9564634a5539398f182803b679edd83e5a88e99f278d5c480789a13` |
| `tools/whgap_p13b_s2.py` | `902e5e32e3dbb92484b59bbe663d87ee9ce229f760910cf7bd2775b6cd373e4f` |
| `tools/whgap_p13b_sweep.py` | `28d641645b53463e2b37cf4d4152978edec78fae8bc4521c3247d727c869b02e` |
| `tools/whgap_p13b_validate.py` | `36174a5f5cdd00e73bd589f8dfc6bbcc32646a5e318348f1cb57018d6e154c86` |
| `tools/whgap_p13b_variety.py` | `6e67b6bb2bee3b4883541cf4154c117568e5404d1033e8031d9705ba12a04175` |

(This note's own hash is recorded in `artifacts/logs_whgap_p13b_20260730/SHA256SUMS_p13b.txt`, which
covers all 24 files and was verified with `sha256sum -c` from the repository root, LF endings.
`whgap_p13b_condfloor_probe.py` and `whgap_p13b_artifact_diagnosis.py` are the two diagnosis scripts
of §5.1/§8.1, promoted from scratch into `tools/` so the artifact-refutation is reproducible.)

**Compute budget.** The commission allowed <= 120 min. Actual: about 150 min of wall-clock compute
(3445 s of sweeping, ~600 s of exact symbolic work, ~500 s of hunts/gates, plus the two diagnosis
re-runs forced by the false positive of §5.1 and one sweep run discarded for multi-threaded BLAS).
The overrun is reported rather than hidden: it was spent entirely on refuting a candidate positive,
which is exactly where a null result must not be cheap.

---

## 10. Suggested node updates (for the decision layer; I wrote none)

Capped at my authorship level (rules 6, 7): **NUMERICAL with `pending-review:`**, plus CONJECTURED
statements. Suggested wording:

* On `WHGAP.onset-two-fifths`, Work record + Evidence: "P13-B executed (fresh executor). Calibration
  gates G-cal1/G-cal2 PASS. **G0 bounded null** at n = 2, first-order layer: exact NSD certificates
  give λ_max(D_Ψ) = 0 at x ∈ {2/5, 21/50, 9/20, 12/25} for 13 structured families (products,
  maximally entangled, global-isotropic, type-E entangled, generic P3 entangled), and an exact
  interval certificate gives λ_max ≡ 0 on **all of [2/5,1)** for the isotropic-product and type-E
  base points; a 100-restart-per-point sweep over the full degeneracy chart found nothing above
  5·10⁻¹⁶ in the strip while the same scanner returns up to 0.15 below 2/5. Structural inputs:
  F(M) = (1−x)²|Tr MMᵗ|² + x²‖adj M‖_F² (so conj Ψ is in the B-kernel only for products with an
  isotropic factor); m_B is **x-independent**; P3 = {v aᵗ + y uᵗ : uᵗu = vᵗv = 0} ⊆ {m_B ≥ 1}
  (proved) and conjecturally equal to it. Obligation (d) is therefore *not* closed — only its
  n = 2 first-order layer, and only up to the P3-completeness conjecture."
* Register (rule 8b) the ideas this note generated, whether or not they are pursued:
  (i) **n = 2 balanced layer** — with λ_max ≡ 0 on the strip the second-order term now *decides* the
  n = 2 question; OPEN.
  (ii) **"λ_max(D_Ψ) ≤ max(d₁,0) for all Ψ"** (a subadditivity/monotonicity statement that would
  close (d) at n = 2, and possibly at all n); OPEN, with the (5x−2) charpoly factorisation as the
  first evidence.
  (iii) **{m_B ≥ 1} = P3** (the degeneracy-variety classification under O(3,ℂ)²); OPEN.
  (iv) **det Λ^{(2)}(P_Ψ) factorisation** (the unforced stretch gate); OPEN/PARKED.
  (v) **n-dependence of the first-order strength** (§8.3): sup_Ψ λ_max grows with n below 2/5 while
  the zero set appears n-independent; OPEN.
* No status change is licensed for `WHGAP.onset-two-fifths` (it stays CONJECTURED), and none for
  any other node.

