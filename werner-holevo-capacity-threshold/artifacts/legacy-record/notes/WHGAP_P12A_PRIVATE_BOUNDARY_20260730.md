# WHGAP P12-A — the private-capacity boundary of the noisy Werner–Holevo family
### and what survives of the restricted-order programme

Executor note (authorship — licenses nothing). Frozen 2026-07-30.
Node: `WHGAP.restricted-order` (P12). Commission:
[WHGAP_COMMISSION_P12A_20260730.md](WHGAP_COMMISSION_P12A_20260730.md).
Status cap: **NUMERICAL / CONJECTURED, `pending-review:` R8**.

---

## 0. PRE-ACTION REPORT (mandatory, `research/PRETASK_RELOAD_PROMPT.md`)

Files read from disk, in order, before any mathematics:
`research/DAG_PROTOCOL.md` (whole); `research/RESEARCH_STRUCTURE_PROTOCOL.md`;
`channel-capacity/werner-holevo-gap/README.md`;
`channel-capacity/werner-holevo-gap/notes/WERNER-HOLEVO-GAP_PROOF_DAG.md` (header + rules);
`channel-capacity/werner-holevo-gap/proof-dag/NODE_INDEX.md`;
`channel-capacity/werner-holevo-gap/proof-dag/nodes/WHGAP.restricted-order.md` (target)
and the related nodes named on it; `paper/main.tex` §5 (necessity);
`notes/WHGAP_REVIEW_COMMISSION_R5_20260729.md` §1–§3 (frozen conventions, standing failure
modes, rule-7 embeds); `notes/WHGAP_DESIGN_MEMO_P12_20260730.md` (input, **not** truth).

- **Target node and status as read from disk:** `WHGAP.restricted-order` (alias P12),
  `kind: LEAF`, `role: proof`, **status `OPEN`**, disposition null, parents `WHGAP.goal`,
  related `WHGAP.order-boundary` (PROVED), `WHGAP.relaxed-lift` (CONJECTURED),
  `WHGAP.order-converse` (OPEN), `WHGAP.more-capable-route` (OPEN/PARKED). Standing open
  obligation on the node: "Decision-layer design memo … then a bounded feasibility
  commission." The memo exists; this note is that commission's executor half.
- **My ROLE:** executor (authorship). I did not author any prior WHGAP work.
- **Highest status my evidence could license (§2 ladder):** **NUMERICAL** (real runs, with
  command + log path + script SHA-256) for the numerical layers, and CONJECTURED for the
  written proofs. Written proofs of my own authorship license **nothing** above that until a
  fresh independent reviewer completes R8 (rules 2, 5, 6). Who may write a completion tier:
  the independent checker only, citing the archived R8 report.
- **Gates and deliverables (one line each):**
  - S0 literature (≤ 25 min, local library first) — done, §1.
  - S1a: prove/refute less-noisy ⟺ RE domination — proved, §2.
  - S1b: exact closed forms + explicit positivity threshold + P ≥ P⁽¹⁾ — §3.
  - S1c: exact rational certificates at six x — §4.
  - S1d: numerical Δ_max curve — §5.3.
  - **G-cal (HARD, first):** Δ ≤ 0 at x ∈ {11/20, 3/5} over ≥ 500 (ε,t) pairs — §5.1, PASS
    (and proved symbolically for the whole of x ∈ [1/2,1]).
  - G-ind: closed forms vs independent Kraus-built Holevo computation, ≥ 3 triples,
    ≥ 10 digits — §5.2, PASS (5 triples, ≥ 55 digits).
  - G-cont: Δ_max(x) → 0 as x → 1/2⁻ — §5.3, PASS.
  - S2: purity-knob hierarchy — §6. S3: restricted-order no-go map — §7.
- **Conflicts between commission text and disk protocols:** **none on rules.** The
  commission's single-writer deviation (no node/index/DAG edits by me) is itself
  commissioned in the R5 batch text and is noted here as required; consequently rule 8c
  (outcomes recorded on the node in the same session) is discharged by the decision layer
  citing this immutable note, not by me. One **substantive** conflict with the *design
  memo* (which is explicitly not disk truth) is reported in §3.6 and §8: the memo's
  displayed leading-order gap carries a sign error.

---

## 1. S0 — literature (local library first)

Local library `channel-capacity/literature/papers/` (PDF text extraction: scripts
`tools/whgap_p12a_lit.py` (keyword sweep, log `s0_lit_scan.log`),
`tools/whgap_p12a_lit_hrsf.py` (HRSF22 pp. 7–16 verbatim, log `s0_lit_hrsf.log`),
`tools/whgap_p12a_lit_rk.py` (RK24/RK25 privacy sweep, log `s0_lit_rk.log`); all quotes
below are verbatim from those logs). No external search was needed — the local copies
answer all three questions.

**(1) Is "less noisy ⟺ relative-entropy domination for all pairs" in the literature?**
**YES — HRSF22, Proposition 2.3** (local PDF `hirche-rouze-stilckfranca-2022-…/arxiv_2011.05949.pdf`,
p. 9), stated as a quantum generalization of Watanabe 2012 Proposition 4:

> Given two channels M, N with the same input, σ_A and η ≥ 0, the following are equivalent:
> (i) for all c-q states ρ_UA with marginal σ_A, η I(U:B)_{(id⊗M)ρ} ≥ I(U:B′)_{(id⊗N)ρ};
> (ii) for any state ρ_A with supp ρ_A ⊆ supp σ_A, η D(M(ρ_A)‖M(σ_A)) ≥ D(N(ρ_A)‖N(σ_A)).
> "A direct consequence is that M ⪰_l.n. N if and only if Equation (2.13) holds for η = 1."

The same page also records the version used inside the paper's closure proof (their eq.
(2.10)⟺(2.11)). **So the equivalence is literature, not new.** I nevertheless prove it
independently in §2 (anchoring ban 7c: I wrote §2 before extracting the HRSF22 page, and
my ⟹ route — the operator-monotone bound σ_p ⪰ (1−p)σ plus the vanishing first order of
D(τ‖τ+pΔ) — is not the route HRSF22 defer to Section 6).

Also relevant and used below: **HRSF22 Prop. 3.3** — for a channel and its complement,
N ⪰_{c.m.c.} N^c ⟺ N ⪰_{m.c.} N^c (complete more capable adds nothing); **HRSF22 §3.1**
— "anti-less noisy channels have P⁽¹⁾(N) = 0, however anti-regularized less noisy is
needed to ensure P(N) = 0", i.e. exactly the one-way implication we invert here.

**(2) Do RK24 / RK25 / ZW state any private-capacity result for the noisy Werner–Holevo
family?** **NO.** In RK24 (`arxiv_2310.15353.pdf`) and RK25 (`arxiv_2405.11216.pdf`) the
string "private" occurs only in the bibliographies (Devetak; Fanizza–Kianvash–Giovannetti;
Leditzky–Leung–Smith) — no private-capacity statement about Λ_x anywhere in the bodies.
ZW (`arxiv_2607.24693.pdf`) proves P(Λ) = Q(Λ) = 0 **at the single point x = 1/2** (their
Λ(X) = ½X + ¼(Tr(X)1 − Xᵀ)); its §2 gives Devetak's P⁽¹⁾ and
P(N) = lim_n (1/n)P⁽¹⁾(N^{⊗n}) = sup_n (1/n)P⁽¹⁾(N^{⊗n}) (their (2.6)–(2.7)), which is the
superadditivity statement I use in §3.5. **Conclusion: the theorem of §3 (P(Λ_x) > 0 for
every x < 1/2, hence {x : P(Λ_x) = 0} = [1/2,1] exactly) is new relative to the local
library.**

**(3) HHHO 2008 context (one paragraph).** `hhho-2008-secure-key-bound-entanglement/`
(arXiv:quant-ph/0608195) is the standard reference for secure key extractable from states
with zero distillable entanglement — the state-level ancestor of a channel with P > 0 = Q.
If the strip [2/5,1/2) turns out to have Q = 0 (which **nothing in this note establishes**),
Λ_x there would be a channel-level instance of that phenomenon. Recorded as context only;
it does not enter any gate or proof.

---

## 2. S1a — the order equivalence (PROVED here, and independently in the literature)

**Setting.** M, N channels with a common input space; "admissible pair" = states (ρ,σ) with
supp ρ ⊆ supp σ. Less noisy in the sense of Watanabe/HRSF22: N ⪰_{l.n.} M iff for every
ensemble {p_u, ρ_u} (equivalently every c-q state), χ({p_u, N(ρ_u)}) ≥ χ({p_u, M(ρ_u)}).

**Theorem 2.1.** N ⪰_{l.n.} M ⟺ D(N(ρ)‖N(σ)) ≥ D(M(ρ)‖M(σ)) for every admissible (ρ,σ).

*Proof.* (⟸) Donald's identity χ({p_u, τ_u}) = Σ_u p_u D(τ_u‖τ̄) with τ̄ = Σ_u p_u τ_u gives
χ({p_u,N(ρ_u)}) = Σ_u p_u D(N(ρ_u)‖N(ρ̄)); each pair (ρ_u, ρ̄) is admissible because
ρ̄ ⪰ p_u ρ_u, so termwise domination gives the claim.

(⟹) Fix an admissible (ρ,σ) and put σ_p := (1−p)σ + pρ for p ∈ (0,1), the average of the
two-point ensemble {p : ρ, 1−p : σ}. Applying the hypothesis to that ensemble and dividing
by p > 0,

  D(N(ρ)‖N(σ_p)) + ((1−p)/p)·D(N(σ)‖N(σ_p)) ≥ D(M(ρ)‖M(σ_p)) + ((1−p)/p)·D(M(σ)‖M(σ_p)). (2.1)

Three facts make the p → 0⁺ limit rigorous.

*(i) Upper semicontinuity along this ray.* σ_p ⪰ (1−p)σ, and log is operator monotone, so
log σ_p ⪰ log(1−p)·1 + log σ, whence for any state ω with supp ω ⊆ supp σ,
D(ω‖σ_p) ≤ D(ω‖σ) − log(1−p). Applying this to Φ ∈ {M,N} (Φ(σ_p) ⪰ (1−p)Φ(σ), and
supp Φ(ρ) ⊆ supp Φ(σ) because supp ρ ⊆ supp σ ⟹ σ ⪰ cρ for some c > 0 ⟹ Φ(σ) ⪰ cΦ(ρ)):

  D(Φ(ρ)‖Φ(σ_p)) ≤ D(Φ(ρ)‖Φ(σ)) − log(1−p).  (2.2)

*(ii) Lower semicontinuity.* Φ(σ_p) → Φ(σ), and Umegaki relative entropy is jointly lower
semicontinuous, so liminf_{p→0} D(Φ(ρ)‖Φ(σ_p)) ≥ D(Φ(ρ)‖Φ(σ)). With (2.2),
D(Φ(ρ)‖Φ(σ_p)) → D(Φ(ρ)‖Φ(σ)).

*(iii) The second term is O(p), so its prefactor (1−p)/p keeps it bounded — and in fact it
is o(1)·p^0 in the sense needed.* Write τ := Φ(σ), ω := Φ(ρ), Δ := ω − τ (traceless), so
Φ(σ_p) = τ + pΔ. On supp τ (which contains supp ω) the map p ↦ D(τ‖τ+pΔ) is real-analytic
in a neighbourhood of 0, because τ + pΔ ≻ 0 there. Its value at p = 0 is 0 and its
derivative at p = 0 is −Tr[τ · d/dp log(τ+pΔ)]|₀ = −Tr[Δ] = 0 (the derivative of log at a
point commuting with itself is the ordinary difference quotient; the standard integral
representation gives d/dp Tr[τ log(τ+pΔ)]|₀ = Tr[Δ]). Hence
D(Φ(σ)‖Φ(σ_p)) = O(p²) and ((1−p)/p)·D(Φ(σ)‖Φ(σ_p)) → 0.

Now take liminf of the left side and limsup of the right side of (2.1). Using (ii) on the
M-side first term (lower bound) and (2.2)+(iii) on the N-side (upper bound), the limit of
(2.1) is D(N(ρ)‖N(σ)) ≥ D(M(ρ)‖M(σ)). ∎

**Corollary 2.2 (what P⁽¹⁾ = 0 means).** With Devetak's formula
P⁽¹⁾(Λ) = sup_{ensembles} [χ_B − χ_E] (χ_B for Λ, χ_E for Λ^c), we have
P⁽¹⁾(Λ) = 0 ⟺ Λ^c ⪰_{l.n.} Λ ⟺ D(Λ^c(ρ)‖Λ^c(σ)) ≥ D(Λ(ρ)‖Λ(σ)) for all admissible (ρ,σ).
(Note χ_B − χ_E ≤ 0 always includes the trivial ensemble, so the sup is ≥ 0; "= 0" means
"never positive".)

*Scope note (7f).* Theorem 2.1 is a FORMULA-level statement, proved symbolically/analytically,
not verified numerically. Its only use below is interpretive (§7); the main theorem of §3
does **not** depend on it.

---

## 3. S1b — the explicit ensemble and the private-capacity theorem

Frozen conventions (R5 §1): Λ_x(Y) = (1−x)Y + (x/2)(Tr(Y)·1 − Yᵀ) on qutrits, x ∈ (0,1);
K₀ = √(1−x)·1, K_{μ+1} = √(x/2)·A_μ with (A_μ)_{jk} = ε_{μjk}; Λ^c(Y)_{ab} = Tr(K_a Y K_b†)
(4×4 padded, Kraus real so K† = Kᵀ). Indices 0-based. Logarithms are **natural** (nats).

**Type audit (7a).** ρ_ε, X, Λ(·): 3×3; Λ^c(·): 4×4; K_a: 3×3 (four of them, Σ_a K_aᵀK_a = 1,
verified symbolically, gate T2); Λ is a superoperator on 3×3 matrices, Λ^c maps 3×3 → 4×4;
the ensemble is a two-point classical-quantum object, χ is a scalar in nats. Every identity
below was verified from the Kraus operators, **not** from the displayed superoperator formula
(gate T3 checks that the two agree on a generic symbolic 3×3 matrix).

### 3.1 The ensemble and its admissibility

ρ_ε := diag(1−2ε, ε, ε), X := (|1⟩⟨2| + |2⟩⟨1|)/√2 (‖X‖_HS = 1, Xᵀ = X, Tr X = 0), and

  **E(ε,t) := { ½ : ρ_ε + tX , ½ : ρ_ε − tX },  average ρ̄ = ρ_ε.**

**Lemma 3.1.** For 0 < ε ≤ 1/2 and |t| ≤ √2 ε, both ρ_ε ± tX are states; they are faithful
iff ε < 1/2 and |t| < √2 ε.
*Proof.* Trace 1 since Tr X = 0. ρ_ε ± tX is block diagonal: the (0,0) entry is 1−2ε ≥ 0 and
the {1,2} block is εI ± tX|₁₂, whose eigenvalues are ε ± t/√2. Both ≥ 0 iff |t| ≤ √2 ε. ∎

### 3.2 The two output pictures (derived, gates B1–B7, E1–E5)

Because X is symmetric and traceless, Λ_x(X) = (1 − 3x/2)X. Because ρ_ε is real diagonal,
Λ_x(ρ_ε) = (1 − 3x/2)ρ_ε + (x/2)·1 = diag(α, b, b) with

  **b = x/2 + (1 − 3x/2)ε,  α = x/2 + (1 − 3x/2)(1 − 2ε) = 1 − 2b.**

The perturbation lives entirely in the {1,2} block, on which Λ_x(ρ_ε) is the **scalar** b·I;
hence [Λ(ρ_ε), Λ(X)] = 0 (gate B5) and

  spec Λ_x(ρ_ε ± tX) = { α, b + u, b − u },  **u = t(1 − 3x/2)/√2.**

On the environment side, direct Kraus assembly gives (gates E1, E2)

  Λ^c_x(ρ_ε) = diag(1−x, xε, e, e),  **e = (x/2)(1 − ε)**,
  Λ^c_x(X) = 0 ⊕ (−x/2)X  (the "a-block" — all entries involving K₀ — vanishes),

so again the perturbation lives in the degenerate pair, [Λ^c(ρ_ε), Λ^c(X)] = 0 (gate E3) and

  spec Λ^c_x(ρ_ε ± tX) = { 1−x, xε, e + v, e − v },  **v = t x /(2√2).**

The two components ρ_ε ± tX give the **same** spectra on both sides (u ↔ −u, v ↔ −v).

### 3.3 The closed forms

Let f(s) := (1+s)log(1+s) + (1−s)log(1−s) and h(w,y) := (w+y)log(w+y) + (w−y)log(w−y) − 2w log w,
so h(w,y) = w f(y/w) (gate F1). Then, with χ = S(average output) − mean of component
entropies, the α and (1−x), xε eigenvalues cancel identically and

  **χ_B(x,ε,t) = b·f(u/b),  χ_E(x,ε,t) = e·f(v/e),
  Δ(x,ε,t) := χ_B − χ_E = b f(u/b) − e f(v/e).**  (gates F2, F3, symbolic in (x,ε,t))

These are the memo's closed forms; **they are correct** (MEMO-CHECK block of
`artifacts/logs_whgap_p12a_20260730/s1_symbolic.log`), and they are re-derived here from the
Kraus set without reading the memo's values.

Series facts used below (gate S1, verified to s¹⁰ and proved by integrating
f′(s) = log((1+s)/(1−s))):

  f(s) = Σ_{k≥1} s^{2k}/(k(2k−1)) ⟹ **f(s) ≥ s² for |s| ≤ 1**, and since k(2k−1) ≥ 6 for k ≥ 2,
  **f(s) ≤ s² + s⁴/(6(1−s²)) for |s| < 1.**  (3.1)

### 3.4 The explicit positivity threshold

Write g_B := (1−3x/2)²/b and g_E := x/(2(1−ε)) (the BKM forms of paper §5). Exactly
(gate G1, symbolic):

  **g_B − g_E = (1−x)[(1−2x) − (1−3x/2)ε] / (b(1−ε))**, positive iff ε < ε_c(x) = 2(1−2x)/(2−3x). (3.2)

Also u²/b = (t²/2)g_B, v²/e = (t²/2)g_E, v⁴/e³ = t⁴x/(8(1−ε)³), (v/e)² = t²/(2(1−ε)²)
(gates R1–R4).

**Theorem 3.2 (explicit threshold).** Let 0 < x < 1/2 and let 0 < ε ≤ ε_c(x)/2. Put t = ε.
Then E(ε,t) is an admissible ensemble of two faithful states, and

  **Δ(x, ε, ε) ≥ (ε²/2)(g_B − g_E) − ε⁴x/(24(1−ε)³) ≥ ε²(1−2x)/3 > 0.**  (3.3)

*Proof.* Admissibility: t = ε ≤ √2 ε and ε ≤ ε_c/2 ≤ 1/2 (because
ε_c(x) = 2(1−2x)/(2−3x) ≤ 1 ⟺ 2−4x ≤ 2−3x ⟺ x ≥ 0), so Lemma 3.1 applies; ε < 1/2 for
x > 0 so both states are faithful, and so are all four output states (spectra in §3.2 are
strictly positive: b ± u > 0, e ± v > 0, 1−x > 0, xε > 0).

Step 1 (lower bound on the B side). Positivity of Λ gives |u| ≤ b, so |u/b| ≤ 1 and by (3.1)
χ_B = b f(u/b) ≥ b(u/b)² = u²/b.

Step 2 (upper bound on the E side). s_E := v/e satisfies s_E² = ε²/(2(1−ε)²) ≤ (1/4)/(2·(1/4)) = 1/2
using ε ≤ 1/2. Hence 1 − s_E² ≥ 1/2, and by (3.1)
χ_E ≤ v²/e + (v⁴/e³)/(6(1−s_E²)) ≤ v²/e + (v⁴/e³)/3 = v²/e + ε⁴x/(24(1−ε)³).

Step 3 (the quadratic part). u²/b − v²/e = (ε²/2)(g_B − g_E). Since ε ≤ ε_c/2 and
1 − 3x/2 = (2−3x)/2, we get (1−3x/2)ε ≤ (1−2x)/2, hence
(1−2x) − (1−3x/2)ε ≥ (1−2x)/2 and b = x/2 + (1−3x/2)ε ≤ x/2 + (1−2x)/2 = (1−x)/2. With
1 − ε ≤ 1, (3.2) gives **g_B − g_E ≥ (1−x)·((1−2x)/2)/((1−x)/2) = 1 − 2x.**

Step 4 (the quartic remainder). ε ≤ (1−2x)/(2−3x) < 2(1−2x) (since 2−3x > 1/2 on (0,1/2)),
so ε² < 4(1−2x)²; and 1 − ε ≥ 1/2 so (1−ε)³ ≥ 1/8, giving ε⁴x/(24(1−ε)³) ≤ ε⁴x/3
≤ ε²·(4x(1−2x)²/3).

Step 5. Combining, Δ ≥ ε²(1−2x)[1/2 − 4x(1−2x)/3]. On (0,1/2), 4x(1−2x) ≤ 4·(1/4)·(1/2) = 1/2
(maximum at x = 1/4), so the bracket is ≥ 1/2 − 1/6 = 1/3. ∎

**Closed-form admissible choice.** ε(x) = ε_c(x)/2 = (1−2x)/(2−3x), t(x) = ε(x); then
b = (1−x)/2 exactly and g_B − g_E = (1−2x)/(1−ε) exactly (gates H1, H2), and

  **Δ(x, ε_c/2, ε_c/2) ≥ (1−2x)³ / (3(2−3x)²)  nats.**  (3.4)

### 3.4b The exact value at ε = ε_c/2 (a stronger and much shorter route)

The point ε = ε_c(x)/2 is special for a reason the memo does not note:

**Lemma 3.2b.** s_B := u/b and s_E := v/e are equal **iff** ε = ε_c(x)/2 (for t ≠ 0).
*Proof.* s_B = s_E ⟺ (1−3x/2)/b = x/(2e) = 1/(1−ε) ⟺ (1−3x/2)(1−ε) = x/2 + (1−3x/2)ε
⟺ (1−2x) = (2−3x)ε. ∎ (gate K0: the numerator of s_B − s_E is
√2·t·[(3x−2)ε − 2x + 1]/…, which vanishes exactly there.)

At that point, with t = ε, gates K1–K3 give the exact values

  s* := s_B = s_E = (1−2x)/(√2(1−x)) ∈ (0, 1/√2],  b − e = ε(1−x) = (1−2x)(1−x)/(2−3x),

and therefore, since χ_B = b f(s_B) and χ_E = e f(s_E) share the **same** argument,

  **Δ(x, ε_c/2, ε_c/2) = (b − e)·f(s*) = [(1−2x)(1−x)/(2−3x)] · f((1−2x)/(√2(1−x))) > 0** (3.5)

for every x ∈ (0,1/2) (gate K4: composition of F1 + K1 + K2 + K3, plus a five-point
40-digit identity check with residual 0). **This is an exact closed form for the witness's
private information — no series bound is needed at all**: positivity follows from
b > e (gate C1: b − e = ε(1−x) > 0) and f > 0. Using only f(s) ≥ s²,

  **Δ(x, ε_c/2, ε_c/2) ≥ (1−2x)³ / (2(1−x)(2−3x))**,  (3.6)

which is sharper than (3.4) at every x (gate K6). Numerical check at x = 9/20:
(3.5) gives 1.4024799966e-03, matching the independently computed Δ of §5.2 to 60 digits;
(3.6) gives 1.3986e-03; (3.4) gives 7.8895e-04.

*Why keep Theorem 3.2 as well:* the threshold form is valid for **every** 0 < ε ≤ ε_c/2, and
S3 class (d) below needs ε arbitrarily small, where the identity s_B = s_E is unavailable.

### 3.5 From Δ to the capacity

**Lemma 3.3 (superadditivity of P⁽¹⁾ under tensor powers).** P⁽¹⁾(N^{⊗n}) ≥ n·P⁽¹⁾(N).
*Proof.* Let {p_u, ρ_u} be any ensemble for N. Its n-fold product ensemble
{Π_i p_{u_i}, ⊗_i ρ_{u_i}} has average ⊗^n ρ̄, and for a product channel the Holevo quantity
of a product ensemble is additive: χ = S(⊗^n τ̄) − Σ_{u⃗} (Π p)S(⊗ τ_{u_i}) = n·χ (both terms
split by additivity of von Neumann entropy on tensor products). This holds for the B side
with N^{⊗n} and for the E side with (N^{⊗n})^c, which equals (N^c)^{⊗n} up to a fixed
isometry of the environment (a permutation of tensor factors), hence up to nothing that
entropies see. Subtracting, the private information of the product ensemble is n(χ_B − χ_E).
Taking the sup gives the claim. ∎

**Corollary 3.4.** P(N) = sup_n (1/n)P⁽¹⁾(N^{⊗n}) ≥ P⁽¹⁾(N) (Devetak's coding theorem, with
the sup form recorded in ZW §2 (2.7); Lemma 3.3 is the superadditivity that makes limit = sup).

**Theorem 3.5 (the private-capacity boundary).**
For every x ∈ (0, 1/2), with ε_c(x) = 2(1−2x)/(2−3x),
  P(Λ_x) ≥ P⁽¹⁾(Λ_x) ≥ Δ(x, ε_c/2, ε_c/2)
   = [(1−2x)(1−x)/(2−3x)]·f((1−2x)/(√2(1−x))) ≥ (1−2x)³/(2(1−x)(2−3x)) > 0.
Together with P4 (frozen input: P = Q = 0 on [1/2,1]),

  **{ x ∈ (0,1] : P(Λ_x) = 0 } = [1/2, 1] exactly.**

*Proof.* Theorem 3.2 gives an ensemble whose private information is ≥ the stated bound, so
P⁽¹⁾ ≥ it; Corollary 3.4 lifts it to P. The complement is P4. ∎

### 3.6 Memo audit (this is an input, not truth)

Independently re-derived and **CONFIRMED**: the ensemble E(ε,t); admissibility |t| ≤ √2 ε;
the commutation on both sides; b, u, e, v exactly as displayed; χ_B = b f(u/b),
χ_E = e f(v/e); ε_c(x) = 2(1−2x)/(2−3x); f's series and the two bracketing inequalities.

**Defect found (minor, sign).** The memo's §2 displays the ε → 0 leading term as
"(t²/2)·2(1−x)(2x−1)/x". The correct value (gate G3, symbolic limit) is

  lim_{ε→0} (u²/b − v²/e) = t²(1−x)(1−2x)/x = (t²/2)·2(1−x)(1−2x)/x,

i.e. the factor is (1−2x), not (2x−1). With the memo's sign the leading term would be
**negative** for x < 1/2 and the memo's own conclusion would not follow. (The paper §5
display (5.3) is consistent: it writes the gap in the opposite orientation,
x/2 − (2/x)(1−3x/2)² = 2(1−x)(2x−1)/x, which is g_E,0 − g_B,0.) The memo's conclusion is
unaffected once the orientation is fixed. Recorded, not silently repaired.

---

## 4. S1c — exact rational certificates

Script `tools/whgap_p12a_gates.py`, block "S1c"; all arithmetic in ℚ via sympy `Rational`
(no floating point, no `nsimplify` anywhere on exact rationals). For each x the certificate
data are ε = ε_c(x)/2, t = ε, and the **exact rational** lower bound
LB(x) := (t²/2)(g_B − g_E) − t⁴x/(24(1−ε)³) of Theorem 3.2, together with the exactly
verified admissibility side conditions 1−2ε ≥ 0, s_B² ≤ 1, s_E² ≤ 1/2.

| x | ε = t = ε_c/2 | s_B² = s_E² | LB (exact rational) | LB (decimal) | Δ (60 dps, both routes) |
|---|---|---|---|---|---|
| 2/5 | 1/4 | 1/18 | 53/6480 | 8.179012345679e-03 | 0.00841226137057729861 |
| 21/50 | 8/37 | 32/841 | 105856/22559825 | 4.692234979660e-03 | 0.00480239867894950771 |
| 9/20 | 2/13 | 2/121 | 239/173030 | 1.381263364734e-03 | 0.00140247999662190317 |
| 12/25 | 1/14 | 1/338 | 6/54925 | 1.092398725535e-04 | 0.000109944360562623123 |
| 49/100 | 2/53 | 2/2601 | 15557/1054575450 | 1.475190798344e-05 | 1.48002692603943501e-05 |
| 499/1000 | 2/503 | 2/251001 | 1505507/94879507504500 | 1.586756760862e-08 | 1.58728479902253570e-08 |

(ε = (1−2x)/(2−3x) in every row; exact values also in
`artifacts/logs_whgap_p12a_20260730/p12a_gates.json`, key `S1c`. Curiously s_B² = s_E²
exactly at this choice — a consequence of b = (1−x)/2 and t = ε, not an input.)
All 24 S1c gates PASS: admissibility exact,
LB > 0 exact, LB ≤ Δ, and the coarser closed-form bound ε²(1−2x)/3 ≤ LB.
**Positivity is established by exact rational arithmetic** (the series bounds (3.1) are the
only analytic input, and they are proved, not numerical); the 60-digit mpmath values are
corroboration, not the certificate.

---

## 5. Gates

### 5.1 G-cal (HARD; run before any strip claim) — PASS

x ∈ {11/20, 3/5}, where P = 0 is PROVED (P4). Dense scan of **1000 (ε,t) pairs each**
(40 ε-values × 25 t-values, t ranging over (0, √2 ε]):

| x | pairs | max Δ | argmax (ε,t) | independent-route value at argmax |
|---|---|---|---|---|
| 11/20 | 1000 | −3.994963487e-08 | (0.0121951, 0.00068986) | −3.994963487e-08 |
| 3/5 | 1000 | −6.436745879e-08 | (0.0121951, 0.00068986) | −6.436745879e-08 |

**Δ ≤ 0 everywhere tested, at both x, on both computational routes.** In addition, G-cal is
established **symbolically for the whole region x ∈ [1/2, 1]**, which is stronger than the
commission asked:

**Proposition 5.1.** ∂h/∂w = log(1 − y²/w²) ≤ 0 and ∂h/∂y = log((w+y)/(w−y)) ≥ 0 for y ≥ 0
(gates M1, M2; h is even in y, gate M3). Moreover b − e = ε(1−x) ≥ 0 always, and
v² − u² = (t²/2)(1−x)(2x−1) ≥ 0 **iff x ≥ 1/2** (gates C1, C2). Hence for x ∈ [1/2,1]:
|u| ≤ v < e ≤ b, so Δ = h(b,|u|) − h(e,v) ≤ h(e,|u|) − h(e,v) ≤ 0 for every admissible (ε,t).
∎ (This is exactly the sign structure that fails for x < 1/2, where |u| > v.)

*Value-vs-formula (7f):* Proposition 5.1 is a FORMULA-level result proved symbolically; the
1000-pair scans are VALUE-level corroboration at two x.

### 5.2 G-ind (independence) — PASS

Independent construction: build ρ_ε ± tX, apply Λ as Σ_a K_a Y K_aᵀ, build
Λ^c(Y)_{ab} = Tr(K_a Y K_bᵀ) as a 4×4, diagonalize with mpmath `eigsy` at 60 dps, take von
Neumann entropies, form χ_B − χ_E. This never uses b, u, e, v, f or any spectrum formula.

| (x, ε, t) | Δ | agreement with closed forms |
|---|---|---|
| (9/20, 1/20, 1/25) | 1.60842184056e-04 | 57.2 digits |
| (1/5, 3/10, 1/5) | 2.92964941908e-02 | 58.9 digits |
| (49/100, 1/200, 1/300) | 2.15887526262e-07 | 55.7 digits |
| (11/20, 1/10, 1/8) | −1.57264793328e-03 | 58.2 digits |
| (12/25, 1/50, 1/60) | 1.03227755245e-05 | 56.4 digits |

Five triples (commission asked ≥ 3), ≥ 55 digits (asked ≥ 10), including one calibration
point above 1/2.

### 5.3 G-cont and S1d — PASS

Δ_max(x) maximized over the admissible box (grid scaled both absolutely and by ε_c(x), then
local refinement):

| x | Δ_max | (1−2x) | Δ_max/(1−2x)³ |
|---|---|---|---|
| 1/5 | 2.414433608e-01 | 6.000e-01 | 1.1178 |
| 2/5 | 1.99926483e-02 | 2.000e-01 | 2.4991 |
| 9/20 | 3.327198691e-03 | 1.000e-01 | 3.3272 |
| 12/25 | 2.606508953e-04 | 4.000e-02 | 4.0727 |
| 49/100 | 3.508361125e-05 | 2.000e-02 | 4.3855 |
| 499/1000 | 3.762454522e-08 | 2.000e-03 | 4.7031 |
| 4999/10000 | 3.789560557e-11 | 2.000e-04 | 4.7370 |
| 49999/100000 | 3.792289206e-14 | 2.000e-05 | 4.7404 |

Δ_max(x) → 0 as x → 1/2⁻ with the clean scaling **Δ_max ≈ 4.740·(1−2x)³**, consistent with
ε_c(x) → 0 and with the exact witness value (3.5), whose leading behaviour as x → 1/2⁻ is
2(1−2x)³ — a factor 2.37 below the numerical optimum, i.e. the choice ε = ε_c/2 is within a
constant factor of optimal but is not the optimizer. (The cruder bound (3.4) gives
(4/3)(1−2x)³.) *Resistance note:* an earlier version of the optimizer used only an
absolute ε-grid and returned spurious **negative** Δ_max at x = 4999/10000 and 49999/100000
(≈ −2e-13); the optimum sits at ε ≈ ε_c/2 ~ 2(1−2x), which that grid could not resolve.
Fixed by adding an ε_c-scaled grid; the exact certificates of §4 were never affected. Logged
append-only in §9.

---

## 6. S2 — the purity-knob hierarchy

**Proposition 6.1 (pure ensembles compute coherent information).** For any ensemble of PURE
states {p_u, ψ_u} with average ρ̄, χ_B − χ_E = I_c(ρ̄, Λ) := S(Λ(ρ̄)) − S(Λ^c(ρ̄)).
*Proof.* Let V: H_A → H_B ⊗ H_E be the Stinespring isometry, V|ψ⟩ = Σ_a |a⟩_E ⊗ K_a|ψ⟩_B.
For a pure input, V|ψ_u⟩ is pure on BE, so its two marginals Λ(ψ_u) and Λ^c(ψ_u) are
isospectral, hence S(Λ(ψ_u)) = S(Λ^c(ψ_u)). Therefore
χ_B − χ_E = [S(Λ(ρ̄)) − Σ_u p_u S(Λ(ψ_u))] − [S(Λ^c(ρ̄)) − Σ_u p_u S(Λ^c(ψ_u))]
= S(Λ(ρ̄)) − S(Λ^c(ρ̄)). ∎
Consequently **sup over pure ensembles of (χ_B − χ_E) = max_ρ I_c(ρ) = Q⁽¹⁾(Λ)**: "≤" because
each pure ensemble contributes I_c of its average; "≥" because any ρ̄ has a pure-state
decomposition (e.g. its eigen-decomposition), which is a pure ensemble with that average.

**Proposition 6.2 (all ensembles).** sup over ALL ensembles of (χ_B − χ_E) = P⁽¹⁾(Λ) —
this is Devetak's definition of the private information (ZW eq. (2.6); Devetak 2005).

**Corollary 6.3 (the knob).** Restricting the relative-entropy domination to the pair class
generated by pure ensembles yields exactly "Q⁽¹⁾ = 0" (the more-capable condition, §7c);
allowing all ensembles yields exactly "P⁽¹⁾ = 0" (less noisy, Corollary 2.2). The
ensemble-class knob therefore interpolates between the two, as the memo asserts — **but see
§7 for the one class the memo's dichotomy misses.**

**Numerical separation (script `tools/whgap_p12a_gates.py`, block S2).** At x ∈ {9/20, 12/25}
(strip) and x = 1/5 (control), 4 random two-point PURE ensembles each (12 total):
- χ_B − χ_E = I_c(ρ̄) to < 1e-12 in all 12 (float64-limited; 12/12 PASS);
- S(Λ(ψ)) = S(Λ^c(ψ)) to < 1e-12 in all 24 pure states tested;
- on the strip (x = 9/20, 12/25) **all 8 pure-ensemble values are ≤ 0**
  (range −0.0955 … −0.0428), while the S1b MIXED ensemble at the same x gives
  **+1.40248e-03 (x = 9/20)** and **+1.09944e-04 (x = 12/25)**. The two regimes separate
  exactly as predicted.
- Control x = 1/5 (< 2/5, where Q > 0 is PROVED): pure ensembles give **positive** values
  (0.0809 … 0.2295), as they must.

*Scope (7f):* Propositions 6.1/6.2 are FORMULA-level (proved / cited); the separation table
is VALUE-level at 3 x with random ensembles — it is not a claim that Q⁽¹⁾ ≤ 0 on the strip.

---

## 7. S3 — the restricted-order no-go map

Convention: an order class is specified by the set 𝒫 of pairs (ρ,σ) on which
D(Λ^c(ρ)‖Λ^c(σ)) ≥ D(Λ(ρ)‖Λ(σ)) is demanded. The **S1b witness pair** is
w(x,ε) := (ρ_ε + tX, ρ_ε) with t = ε ≤ ε_c(x)/2 — both members **mixed and faithful**, both
within trace distance 2ε of |0⟩⟨0| (verified exactly, gate S3d).

| # | class 𝒫 | (i) implies P⁽¹⁾ = 0? | (ii) contains S1b witness? | verdict below 1/2 |
|---|---|---|---|---|
| a1 | less noisy / plain RE domination (all pairs) | YES (⟺, Cor. 2.2) | YES | **DEAD on (0,1/2)** — the conclusion itself is FALSE (Thm 3.5) |
| a2 | complete less noisy (cRE) | YES (⟹ a1) | YES (trivial reference) | **DEAD on (0,1/2)** |
| a3 | cBKM | YES (⟹ cRE, ZW) | YES | **DEAD on (0,1/2)** (also P6/R5b: exactly [1/2,1)) |
| a4 | signed-lift CP-defect certificate | YES (⟹ cBKM) | YES | **DEAD on (0,1/2)** (P2/P4: region exactly [1/2,1)) |
| a5 | criterion (W) — `WHGAP.relaxed-lift` | only if its conclusion is P⁽¹⁾ = 0 / less-noisy | — | **DEAD below 1/2 iff it implies a1**; if its conclusion is only Q-type it falls in class c. Its own node is CONJECTURED; not decided here. |
| a6 | α-Rényi domination, α > 1 (Petz or sandwiched) | not needed | YES | **DEAD on (0,1/2)** — see Prop. 7.1 |
| b1 | "anchored less noisy" as written on the P12 node (σ = ψ_R ⊗ ρ_A anchors, ρ free) | YES | YES (trivial R, ρ_A = ρ_ε, so σ = ρ_ε) | **DEAD on (0,1/2)** |
| b2 | **pure-first-argument** variant (ρ = P_ψ pure, σ free) — see §7.2 | NO (only Q⁽¹⁾ = 0) | **NO** (both witness members are mixed) | **DEAD on (0,2/5)** (Q > 0 PROVED) and numerically violated at x = 2/5 itself; **SURVIVES a bounded search on [2/5,1/2)** — §7.3(B). This is the one genuinely surviving intermediate class. |
| c | marginal-matched purification pairs (σ = ψ_R ⊗ ρ_A with ρ_A = Tr_R ψ_RA) | NO — equals more capable, i.e. Q⁽¹⁾ = 0 | NO | **DEAD on (0,2/5)**; open on [2/5,1/2); complete version adds nothing (HRSF22 Prop 3.3); its tensorization IS the I_c-additivity problem (`WHGAP.more-capable-route`, PARKED) |
| d | any class containing all pairs of states within trace distance δ of a pure state, any δ > 0 | YES | YES for δ(x) as below | **DEAD on (0,1/2) for every δ > 0** |

**Class d, explicitly.** Given x ∈ (0,1/2) and δ > 0, take ε = min(δ/2, ε_c(x)/2) and t = ε.
Then Theorem 3.2 gives Δ > 0 and the two ensemble members lie within trace distance
‖ρ_ε ± tX − |0⟩⟨0|‖₁/2 = 2ε ≤ δ of the pure state |0⟩⟨0| (computed exactly: the eigenvalues of
ρ_ε ± tX − |0⟩⟨0| are −2ε and ε ± t/√2, so the trace norm is 4ε). Verified at
x ∈ {9/20, 49/100} and ε/ε_c ∈ {1/2, 1/10, 1/1000, 1/10⁶}: Δ > 0 in all 8 cases, distance
= 2ε to 30 digits. **So no positive "thickness" around the pure states can be tolerated.**

**Proposition 7.1 (Rényi orders, class a6).** On the witness pair the two outputs commute on
each side, so every Rényi divergence (Petz D_α and sandwiched D̃_α coincide on commuting
pairs, and equal the classical Rényi divergence of the spectra). With
F_α(s) := (1+s)^α + (1−s)^α − 2 and the spectra of §3.2,
D_α(Λ(ρ_ε+tX)‖Λ(ρ_ε)) = (α−1)^{-1} log(1 + b F_α(u/b)) and
D_α(Λ^c(ρ_ε+tX)‖Λ^c(ρ_ε)) = (α−1)^{-1} log(1 + e F_α(v/e)) (using α_eig + 2b = 1 and
(1−x) + xε + 2e = 1). Since F_α(s) = α(α−1)s² + O(s⁴), the small-t comparison is again
u²/b vs v²/e, i.e. exactly g_B vs g_E: for ε < ε_c(x) and t small enough the E side is
strictly smaller and the order FAILS. Numerically confirmed (script
`tools/whgap_p12a_s3probe.py`) at x ∈ {1/5, 9/20, 49/100} for α ∈ {1.25, 1.5, 2, 3, 5} and
two t-scales, with x = 11/20 as a control where the order holds. **α ≥ 1 Rényi domination
therefore buys nothing below 1/2.**

### 7.2 The class the memo's dichotomy misses (the honest weakening)

The memo's structural claim is a dichotomy: any order defined by relative-entropy domination
over an ensemble class either (a) "contains a non-pure neighbourhood and is FALSE below 1/2",
or (b) "is the pure class, which is exactly Q⁽¹⁾ = 0". **This dichotomy is not exhaustive.**

Consider 𝒫_b2 := { (P_ψ, σ) : ψ pure, σ any state } — domination with a **pure first
argument** and an arbitrary second argument. It contains pairs whose second member is far
from pure, so it is not "the pure class"; yet it does **not** contain the S1b witness pair,
whose *first* member ρ_ε + tX is mixed. Consequences:

- 𝒫_b2 ⟹ Q⁽¹⁾ = 0: apply it with σ = ρ̄ to each member of a pure ensemble and sum
  (Prop. 6.1). So it is at least as strong as more capable.
- The converse is not available: recovering 𝒫_b2 from pure-ensemble domination would need
  the two-point ensemble {p : P_ψ, 1−p : σ} of §2, whose second member is mixed. So 𝒫_b2 sits
  **between** more capable and less noisy, and the S1b theorem does not touch it.
- It is nonetheless **DEAD on (0, 2/5)**, because it implies Q⁽¹⁾ = 0 and Q > 0 there is
  PROVED (R5d, frozen input).
- On the strip [2/5, 1/2) its status is **not decided by this note**. Bounded numerical probe
  (`tools/whgap_p12a_s3probe.py`, part B): minimize
  G(ψ,σ) := D(Λ^c(P_ψ)‖Λ^c(σ)) − D(Λ(P_ψ)‖Λ(σ)) over pure ψ and full-rank σ,
  12 Nelder–Mead restarts per x; control at x = 11/20 where cRE is PROVED (so no violation
  may be found). Results in §7.3(B): violations found at x ∈ {1/5, 2/5}, **none found** at
  x ∈ {9/20, 49/100}.

This is the precise sense in which the memo's no-go is **established in the large but
weakened in the dichotomy**: everything with mixed-state thickness dies unconditionally
below 1/2 (rows a, b1, d); the exactly-pure class is Q⁽¹⁾ (row c); and there is a third,
genuinely intermediate room — pure-first-argument domination — that the memo's argument does
not reach. Whether that room is empty is exactly as hard as the strip Q question (it implies
Q⁽¹⁾ = 0), and its tensorization is unstudied.

### 7.3 Probe results (bounded numerics)

**(A) Rényi orders — 40/40 gates PASS.** At x ∈ {1/5, 9/20, 49/100} with ε = ε_c(x)/2 and
t ∈ {ε, ε/10}, the domination D_α(E-side) ≥ D_α(B-side) **fails** for every
α ∈ {1.25, 1.5, 2, 3, 5}; e.g. at x = 49/100, t = ε/10 = 1/265 the deficits run from
−1.85e-07 (α = 1.25) to −7.40e-07 (α = 5). At the control x = 11/20 the domination **holds**
for all ten (α,t) combinations (+1.26e-05 … +5.02e-03). Consistent with Prop. 7.1.

**(B) pure-first-argument class 𝒫_b2 — bounded numerical null on the strip.**
min over 12 Nelder–Mead restarts (24 real parameters: pure ψ + full-rank σ):

| x | min G found | reading |
|---|---|---|
| 1/5 | −3.4603658318e+00 | violated (expected: Q > 0 PROVED there) |
| 2/5 | −1.2234614805e-01 | violated — **new datum**, and note 2/5 is *outside* the PROVED Q > 0 interval (0,2/5) |
| 9/20 | +1.3101759442e-04 | **no violation found** |
| 49/100 | +8.0315241237e-06 | **no violation found** |
| 11/20 (control) | +1.3547370402e-04 | no violation, as required (cRE PROVED) |

*Honest reading (7f, 7g).* G(ψ,σ) → 0⁺ as σ → P_ψ, so inf G ≤ 0 trivially; the small
positive "minima" at 9/20, 49/100 and at the 11/20 **control** are the optimizer settling
near that degenerate point, **not** a positive lower bound. What the run establishes is a
**bounded search that found no violation** at the two strip points, at the same resolution
at which it did find violations of size 1e-01 … 1e+00 at x ≤ 2/5. This is NUMERICAL evidence
that 𝒫_b2 may survive on [2/5,1/2) — nothing more. In particular a violation of 𝒫_b2 does
**not** imply Q⁽¹⁾ > 0 (𝒫_b2 is strictly stronger than Q⁽¹⁾ = 0), so the x = 2/5 datum says
nothing about Q at 2/5.

---

## 8. Verdict on the design memo, and scoping honesty

**Established (independently derived here):** the closed forms χ_B = b f(u/b),
χ_E = e f(v/e) with the memo's b, u, e, v; the admissibility |t| ≤ √2 ε; the commutation on
both sides; ε_c(x) = 2(1−2x)/(2−3x); the less-noisy ⟺ RE-domination equivalence (§2 —
also HRSF22 Prop 2.3, so not new); the conclusion P(Λ_x) > 0 for every x < 1/2 and hence
**{x : P(Λ_x) = 0} = [1/2,1] exactly**; the purity-knob endpoints (§6).

**Corrected:** the memo's ε → 0 leading term has the wrong sign factor ((2x−1) instead of
(1−2x)); see §3.6. Minor, does not affect its conclusions once oriented.

**Strengthened:** the memo proposes to prove Δ > 0 by the elementary inequalities
f(s) ≥ s² and f(s) ≤ s² + s⁴/(6(1−s²)). That works (Theorem 3.2), but it is unnecessary at
the natural choice: at ε = ε_c/2 with t = ε the two f-arguments **coincide exactly**
(Lemma 3.2b), giving the closed form Δ = (b−e)f(s*) = [(1−2x)(1−x)/(2−3x)]·f((1−2x)/(√2(1−x)))
and positivity from b > e alone. This also sharpens the capacity lower bound from
(1−2x)³/(3(2−3x)²) to (1−2x)³/(2(1−x)(2−3x)).

**Weakened:** the memo's "P12 no-go" dichotomy is **not exhaustive** (§7.2). Correct
statement of what is established:

> Every order class defined by relative-entropy (or α ≥ 1 Rényi) domination that contains a
> pair of MIXED states within arbitrarily small trace distance of a pure state — in
> particular less noisy, cRE, cBKM, signed-lift certificates, and the P12 node's own
> "anchored less noisy" — is FALSE for Λ_x at every x ∈ (0,1/2), unconditionally, because
> P⁽¹⁾(Λ_x) > 0 there. The only classes that survive the S1b witness are those requiring
> **exact purity of at least one argument**: the marginal-matched purification pairs
> (= more capable = Q⁽¹⁾ = 0, whose tensorization is the coherent-information additivity
> problem) and the pure-first-argument class 𝒫_b2 (which implies Q⁽¹⁾ = 0, is dead at and below
> 2/5, and survives a bounded numerical search on [2/5,1/2)).

**Surviving frontier.** (i) `WHGAP.order-converse` (P11) — does O(3)-covariance collapse
regularized-more-capable to its complete version? (ii) genuine I_c-additivity technology
(`WHGAP.more-capable-route`, PARKED); (iii) NEW, generated by this note and offered to the
decision layer for registration under rule 8b (I may not edit nodes under the single-writer
deviation): the **pure-first-argument order 𝒫_b2** as a candidate intermediate order —
strictly between more capable and less noisy on the ensemble knob, not killed by the S1b
witness, tensorization unstudied.

**Scoping honesty (binding).** **Nothing in this note claims anything about Q on
[2/5, 1/2).** The correct reading of Theorem 3.5 on the strip is: *P(Λ_x) > 0 there;
Q(Λ_x) is unknown; if Q = 0 on part of the strip, the family exhibits P > 0 = Q.* The
S2 numerics at x = 9/20, 12/25 are values at four random pure two-point ensembles each and
establish nothing about Q⁽¹⁾. Likewise §7's verdicts are statements about ORDER CLASSES, not
about capacities on the strip.

---

## 9. Provenance, resistance log, and status

### 9.1 Scripts, logs, commands

| script | log |
|---|---|
| `tools/whgap_p12a_symbolic.py` | `artifacts/logs_whgap_p12a_20260730/s1_symbolic.log` (43 gates, 0 fail) |
| `tools/whgap_p12a_gates.py` | `artifacts/logs_whgap_p12a_20260730/s2_gates.log`, `p12a_gates.json` (85 gates, 0 fail) |
| `tools/whgap_p12a_s3probe.py` | `artifacts/logs_whgap_p12a_20260730/s3_probe.log`, `p12a_s3probe.json` (41 gates, 0 fail) |

Literature-scan scripts: `tools/whgap_p12a_lit.py`, `tools/whgap_p12a_lit_hrsf.py`,
`tools/whgap_p12a_lit_rk.py` → `s0_lit_scan.log`, `s0_lit_hrsf.log`, `s0_lit_rk.log`.

Commands (interpreter `C:<home>/cpython3119/python.exe`, cwd = repo root):
```
C:<home>/cpython3119/python.exe tools/whgap_p12a_symbolic.py    > artifacts/logs_whgap_p12a_20260730/s1_symbolic.log
C:<home>/cpython3119/python.exe tools/whgap_p12a_gates.py       > artifacts/logs_whgap_p12a_20260730/s2_gates.log
C:<home>/cpython3119/python.exe -u tools/whgap_p12a_s3probe.py  > artifacts/logs_whgap_p12a_20260730/s3_probe.log
```
All three exited 0 (zero failed gates).
SHA-256 of scripts and logs: `artifacts/logs_whgap_p12a_20260730/SHA256SUMS_E-P12A.txt`
(LF line endings; verified with `sha256sum -c` — 15/15 OK; the entry for this note itself
is the pre-closeout hash and is superseded by the regenerated file if the note is edited).

Closeout validators (pinned interpreter, standing failure mode 2):
`python tools/proof_dag_check.py --problem werner-holevo-gap` → **exit 0**
("Proof-DAG validation OK: 13 nodes"; the 13 `migration_status` warnings are pre-existing
and unrelated to this session, which edited no node file);
`python tools/literature_check.py` → **exit 0** ("Literature catalogs OK: 51 papers").

### 9.2 Standing failure modes screened (R5 §2, item by item)

1. sympy `.H` on real-symbolic matrices — **avoided**: every adjoint is `.T`, justified by
   the Kraus operators being real (checked: A_μ have integer entries, prefactors √(1−x),
   √(x/2) are real for x ∈ (0,1)).
2. WindowsApps python inaccessible — **avoided**: pinned interpreter only.
3. Complement convention drift — **screened**: Λ^c is the padded 4×4
   Λ^c(Y)_{ab} = Tr(K_a Y K_bᵀ); the a-block (index 0) is displayed explicitly and shown to
   vanish on X; the (1−x), xε entries are shown untouched by the perturbation (gate E5).
4. Transpose vs conjugate transpose — **screened**, see 1; the S2/S3 numerics use complex
   states with `Ka @ Y @ Ka.conj().T`, which for real K_a is the same operator.
5. `sorted()` on symbolic eigenvalues — **avoided**: eigenvalue sets compared as `set`s of
   simplified expressions, never sorted.
6. CRLF in SHA256SUMS — **avoided**: written with `newline="\n"`.
7. Degeneracy bookkeeping — **central and handled exactly**: both perturbations act inside a
   *degenerate scalar block* (b·I₂ and e·I₂), which is why the commutation is exact and no
   divided-difference/near-zero-gap issue arises at all.
8. ε log ε bookkeeping — **not applicable**: no ε → 0 limit is taken in any proof; the
   theorem is a finite-ε statement with rational data. (The only limits taken are in §2's
   p → 0 argument, where the O(p²) claim is proved, and in the memo cross-check G3.)
9. Anchoring — **screened**: §2, §3.2–§3.3 and §5.1 were derived and coded from the frozen
   conventions before the memo's values were compared (MEMO-CHECK block runs last in
   `whgap_p12a_symbolic.py`); the G-ind route never touches the closed forms.

### 9.3 Resistance log (append-only)

- **R-1.** First S2/S3c run: 30 gate failures. Diagnosis: (i) my S2 tolerance (1e-25) was
  below the float64 accuracy floor of the randomly generated pure states (~1e-15) — the
  quantities were correct to 1e-16; tolerance corrected to 1e-12 with the reason documented
  in the script. (ii) A genuine bug of mine in the S3c check: I had written
  ρ_A = Ψ†Ψ instead of ρ_A = ΨᵀΨ̄ for ψ_{ra} = Ψ[r,a] (conjugate-transpose slip, standing
  failure mode 4). Fixed; all 6 S3c gates then PASS to < 1e-9.
- **R-2.** First S1d/G-cont run returned spurious negative Δ_max at x = 4999/10000 and
  49999/100000 (≈ −2e-13 to −3e-13) because the (ε,t) grid was absolute while the optimum
  sits at ε ≈ ε_c(x)/2 ≈ 2(1−2x). Fixed by adding an ε_c-scaled grid; the exact §4
  certificates were never affected (they do not use the optimizer). Recorded because a
  reviewer re-running the *old* grid would see an apparent contradiction with Theorem 3.2.
- **R-3.** Gate "C2" was first written with the wrong algebraic normalization
  (v² − u² = t²(2x−1)/4); the correct identity is (t²/2)(1−x)(2x−1). My gate caught my own
  slip; the corrected identity is what Proposition 5.1 uses.
- No resistance encountered on the main theorem: every symbolic gate passed first time.

### 9.4 Status (rule 6 cap)

Everything above is **my own authorship**. Per §2 of the DAG protocol and rules 2/5/6:

- Theorems 2.1, 3.2, 3.5, Propositions 5.1, 6.1, 7.1: **CONJECTURED, `pending-review:` R8**
  (written proofs, self-checked, no independent review yet).
- The gate runs, exact certificates and probe tables: **NUMERICAL, `pending-review:` R8**
  (command + log + SHA-256 recorded in §9.1).
- I write **no** completion tier on any node; under the single-writer deviation I edit no
  node file, no `NODE_INDEX.md`, and no DAG document. The decision layer performs those
  updates citing this note and the R8 report.

