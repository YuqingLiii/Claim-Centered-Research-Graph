# R5a — independent review of P6 (cBKM order-boundary scan)

Reviewer: fresh Opus instance, ROLE = reviewer. Date: 2026-07-29.
Commission: `channel-capacity/werner-holevo-gap/notes/WHGAP_REVIEW_COMMISSION_R5_20260729.md`,
section "R5a". Node: `WHGAP.order-boundary` (P6).
Interpreter for every run: `C:<home>/cpython3119/python.exe`
(mpmath 1.3.0, numpy 1.26.4). Logs: `artifacts/logs_whgap_r5_20260729/`.

---

## PRE-ACTION REPORT (per `research/PRETASK_RELOAD_PROMPT.md`)

Files read from disk before any work: `research/PRETASK_RELOAD_PROMPT.md`,
`research/DAG_PROTOCOL.md` (whole file), `research/RESEARCH_STRUCTURE_PROTOCOL.md`,
`channel-capacity/werner-holevo-gap/README.md`,
`channel-capacity/werner-holevo-gap/proof-dag/NODE_INDEX.md`,
`channel-capacity/werner-holevo-gap/proof-dag/nodes/WHGAP.order-boundary.md`,
parent `nodes/WHGAP.goal.md` (P6 is a LEAF; no children),
the R5 commission, and the frozen reviewed inputs
(`artifacts/whgap_p6_relaxation_20260729.md`,
`artifacts/logs_whgap_p6_20260729/e1_certificates.json` + `e1_scan.json`,
`tools/whgap_p6_common.py`, `tools/whgap_p6_e1_scan.py`, `tools/whgap_p6_e1_certify.py`).

- **Target node and status as read from disk:** `WHGAP.order-boundary` (alias P6), kind LEAF,
  role proof, `status: NUMERICAL`, `status_source` = "P6 execution 2026-07-29; interval-certified
  grid violations and bounded-search boundary bracket; pending-review". Adversarial reviews:
  "None yet". Open obligation on the node: exactly this review.
- **ROLE:** reviewer. **Independence statement:** I did not author any part of P6, P6b, the P6
  scripts, or the node text; I was given no desired outcome; the commission's licensing menu was
  presented to me as alternatives.
- **Highest status my evidence could license (§2 ladder):** a completed rule-7 review by a fresh
  instance opens the completion tier; on a favourable verdict the *decision layer* (not I) could
  write CERTIFIED\* (single review, partial scope) on this node citing this artifact. My own
  computations, being reviewer-authored, license nothing above NUMERICAL by themselves. Because
  my verdict is FINDINGS, no completion-tier status is opened by this review.
- **Commission gates/deliverables (one line each):** (1) methodology audit of the cBKM test
  statistic, conditioning floor, restart taxonomy, and directed-interval certification route;
  (2) independent recomputation, own code and own c(a,b), of ≥ 2 rational witnesses including
  x = 499/1000, at ≥ 60 digits, with a self-computed margin; (3) own short no-violation search at
  x = 11/20 (≤ 10 min); (4) audit of the boundary-claim discipline; ≤ 45 min compute; report to
  `artifacts/whgap_r5a_review_20260729.md`; verdict from the R5a menu.
- **Single-writer deviation:** acknowledged and obeyed — I edited no node file, no `NODE_INDEX.md`,
  no DAG doc. I wrote only this report, three scripts under `tools/`, and logs under
  `artifacts/logs_whgap_r5_20260729/` (with `SHA256SUMS.txt`, LF endings).
- **Conflicts between commission text and disk protocols:** one, reported not resolved — the
  commission's licensing option (A) contains a factual scope assertion ("bisection points down to
  7999/16000 (directed-interval Rayleigh-quotient witnesses)") that the frozen disk evidence
  contradicts (see MAJOR-1). Because rule 1 (cite or it didn't happen) and rule 6 forbid writing a
  status text unsupported by disk, I cannot sign (A) as written; I return FINDINGS and supply a
  repaired scope sentence for the decision layer.

Compute used: ~3 minutes of CPU across four runs (27 s + 38 s + 71 s + 19 s + 4 s), far inside
the 45-minute budget. Wall clock inside budget.

---

## 1. What I did, and in what order (7c — anchoring ban)

I built my own implementation first, from the commission's section-1 conventions only, before
reading any P6 number other than the frozen *inputs* (the rational σ and Z records, which the
commission instructs me to load):

- `tools/whgap_r5a_recheck.py` — own Levi-Civita, own Kraus family, complement built **directly
  from the definition** Λ^c(Y)_{ab} = Tr(K_a Y K_b^†) (I did not use the author's hand-written
  closed form), own divided difference c(a,b), own BKM form as the eigenbasis sum, plus a second
  structurally different implementation of the same form via the resolvent integral
  g_θ(Y) = ∫₀^∞ Tr[Y(θ+t)^{-1}Y(θ+t)^{-1}]dt. Part B assembles the difference form as a 9×9 real
  symmetric Gram matrix on **my own** Hermitian basis (diagonal units + symmetric/antisymmetric
  off-diagonal pairs), i.e. an assembly route independent of the author's row-major
  `kron` superoperators.
- `tools/whgap_r5a_floor_probe.py` — double-precision vs 60/120-digit arbitration of apparent
  small violations at x ≥ 1/2.
- `tools/whgap_r5a_embed_check.py` — reference-dimension embedding test at x = 499/1000.

Only after those ran did I compare with `e1_certificates.json` / `e1_scan.json`. Notational
coincidence flag (7c): my eigenbasis-sum formula necessarily coincides with the author's
c(a,b) definition because the commission freezes it; my *route* (no superoperator matrices, no
Γ matrix, no interval library) does not.

## 2. Type audit (7a)

| object | type / dimension | notes |
|---|---|---|
| x | rational scalar in (0,1) | exact `Fraction`, converted to `mpf` at working dps |
| σ_RA | (3d_R)×(3d_R) PSD, trace 1 — a **state** | must be *faithful*: λ_min > 0 |
| Z | (3d_R)×(3d_R) Hermitian — a **tangent direction**, not a state, no trace constraint | scale-free (Rayleigh quotient) |
| Λ_x | superoperator 3×3 → 3×3 | real matrix in HS coordinates |
| Λ_x^c | superoperator 3×3 → **4×4** (padded, 4 Kraus) | real matrix in HS coordinates |
| id_R⊗Λ_x | (3d_R)² → (3d_R)² | `S_M`, shape (3d_R)²×(3d_R)² |
| id_R⊗Λ_x^c | (3d_R)² → (4d_R)² | `S_N`, shape (4d_R)²×(3d_R)² |
| Γ_θ^{-1} | superoperator on (dim θ)²; θ = Λ(σ) is 3d_R-square, θ = Λ^c(σ) is 4d_R-square | positive definite iff θ faithful |
| T_N − T_M = S_N†G_N S_N − S_M†G_M S_M | Hermitian **9d_R²×9d_R²** on the input HS space | matches the node's "9 d_R²-dimensional" claim ✓ |

Adjoint convention (failure mode §2.4): the code uses `.conj().T` for the HS adjoint. Here every
superoperator matrix is **real** in the row-major basis (Λ has real coefficients; the complement's
entries Tr(K_a E_{ij} K_b^T) are real because the Kraus are real), so `.conj().T` = `.T` and no
transpose-vs-conjugate-transpose drift is possible. I verified realness implicitly by rebuilding
the complement from Kraus in mpmath and matching the closed form to 10^-242 (below).

Sign/direction audit: cBKM domination of Λ by Λ^c at (σ, Z) is
g_{Λ^c(σ)}(Λ^c(Z)) − g_{Λ(σ)}(Λ(Z)) ≥ 0. A **negative** Rayleigh quotient is therefore a
violation, and since λ_min(T_N − T_M) ≤ Rayleigh quotient, a single negative value is a valid
one-sided certificate. The logic direction is correct in the scripts and in the artifact: one
witness suffices for a violation; "no violation" is a search statement only. Also correct: a
violation at d_R = 1 already violates the *complete* order (complete ⇒ d_R = 1 instance).

## 3. Methodology audit (task 1)

**Sound, and confirmed by my own derivations:**

1. *Minimizing over the full complex operator space* (the scanner diagonalizes the difference on
   all 2·(3d_R)² real dimensions instead of the (3d_R)² Hermitian ones) is **legitimate**: writing
   Z = H + iK with H, K Hermitian, the cross terms i⟨H,TK⟩ − i⟨K,TH⟩ cancel because T is
   HS-self-adjoint and maps Hermitian to Hermitian, so min over complex = min over Hermitian.
   Consequence worth recording: every eigenvalue is then doubly degenerate and the returned
   eigenvector is Hermitian only up to a global phase, which is exactly why the Hermitization step
   inside `certify()` is load-bearing, not cosmetic.
2. *The certifier's hand-written complement closed form* (`complement_mp`: (1−x)Tr Y; off-diagonal
   ±√(x(1−x)/2)(Y_{jk}−Y_{kj}); lower block (x/2)(Tr Y·I − Y^T)) is **not** the definition it claims
   to implement, so I re-derived it: with Σ_j ε_{jkμ}ε_{jνl} = δ_{kν}δ_{μl} − δ_{kl}δ_{μν} one gets
   Tr(A_μ Y A_ν) = Y_{νμ} − δ_{μν}Tr Y, hence the lower block is exactly (x/2)(Tr Y·I − Y^T), and
   the (0,μ+1) entry is +√(x(1−x)/2)(Y_{jk}−Y_{kj}) with (jk) the μ-complement, the (μ+1,0) entry
   its negative. The closed form is correct (failure mode §2.3 screened: convention, padding, sign
   and the k-factor all check out). Numerically, my Kraus-built complement matches the closed-form
   lower block to ≤ 4.7·10^-243 at x = 7/20, 12/25, 499/1000 (three independent parameter values,
   7b satisfied).
3. *Interval branch logic at degeneracies* is sound in principle: c(a,b) = ∫₀¹ dt/(ta+(1−t)b) lies
   between 1/max(a,b) and 1/min(a,b), so the reciprocal-endpoint bound used when the eigenvalue
   intervals overlap is valid and avoids the division-by-zero failure (§2.7). Eigenvalue padding
   4·residual is a valid Weyl-type enclosure.
4. *Restart taxonomy* is as documented (1 maximally mixed + 30 P3 + 50 near-pure + 29 product +
   40 random = 150, asserted in code) and the conditioning guard is the 0.999/0.001 identity mix on
   product/random starts plus the `factor_to_state(floor=1e-4)` inside the descent. The near-pure
   and P3 categories are **exempt** from the 10^-3 floor (they use ε ∈ [10^-3,10^-2] and
   [10^-4,10^-2]); the decisive 12/25 and 499/1000 witnesses come from that exempt class. For
   those witnesses this is harmless because the values were re-evaluated at high precision — but it
   is why the *no-violation* side needs the noise analysis in minor m1.
5. *Frozen-input integrity:* all 33 files hashed in `artifacts/logs_whgap_p6_20260729/SHA256SUMS.txt`
   verify (after stripping CR — see m5), so I reviewed the same bytes P6 produced.

**Not sound as advertised:** items MAJOR-1, MAJOR-2, MAJOR-3 and minors m1–m4, m8 below.

## 4. Independent recomputation of the certified witnesses (task 2)

Own code, own c(a,b), **exact rationals** from `e1_certificates.json` (Hermitized exactly with
`Fraction` arithmetic — real part symmetrized, imaginary part antisymmetrized — σ normalized by its
exact trace, Z normalized by its Frobenius norm), evaluated at dps 60, 120 and 240, plus the
independent resolvent-integral route at dps 40. Three of the eight witnesses, including the
commission-mandated x = 499/1000:

| x | my Rayleigh quotient (identical at 60/120/240 digits) | resolvent-integral route (dps 40) | P6 `directed_interval_upper` |
|---|---|---|---|
| 7/20 | −706.833715334567143521655023068 | −706.83371533456714352 | −706.8337153347308908189… |
| 12/25 | −8.62221737775022837955915220849 | −8.6222173777502283796 | −8.622217377750481748567… |
| 499/1000 | −0.0188215524727134784846527562491 | −0.018821552472713478485 | −0.018821552472713018063… |

Diagnostics I computed for each: eigen-residuals ‖θv − λv‖ ≤ 2.4·10^-241 and ‖Q†Q − I‖ at the same
order (so the eigenbasis sums are exact to working precision); both output states faithful
(min spectra 6.1·10^-5 at 7/20 … 1.97·10^-4 at 499/1000, all four N-eigenvalues positive, so
Γ^{-1} is defined); spread across the three precisions **exactly 0** in all printed digits.

**Own margin.** The value is stable to ≥ 25 significant digits across a 4× precision change and
agrees with a structurally different implementation (resolvent integral) to all 20 digits it prints.
The dominant uncertainty is not arithmetic but input representation: perturbing the input entries at
relative 10^-16 moves the value by ~2·10^-13 relative (this is exactly the P6-vs-mine gap in the
table). Taking a generous 10^-9 absolute error budget, the certified negativity margins are
7.1·10^2, 8.6 and 1.9·10^-2 respectively — i.e. **strict negativity confirmed at all three points,
with ≥ 7 orders of margin at the tightest point (499/1000)**. Verified for the *exact rational*
data, which is strictly stronger than what P6 actually certified (MAJOR-2).

## 5. Own no-violation search at x = 11/20 (task 3), and its arbitration

My own search (9×9 Gram assembly on my own Hermitian basis, d_R = 1, 260 random starts across five
classes — Haar, near-pure, rank-2-plus-floor, isotropic (e₁+ie₂)/√2, and the diag(1−2ε,ε,ε)
family — plus 400 local Hermitian refinement steps):

| x | min over starts | after refinement | class attaining it |
|---|---|---|---|
| 11/20 | −1.55·10^-9 | −7.14·10^-9 | isotropic (ε ≈ 10^-7) |
| 1/2 | −4.01·10^-10 | −3.24·10^-9 | isotropic |
| 499/1000 (positive control) | −3.38·10^-2 | −3.44·10^-2 | near-pure |

So my bounded search at 11/20 *does* dip below the preregistered −10^-9 floor. I arbitrated this
at high precision rather than reporting it as a violation: re-evaluating the very same states in
mpmath (own 9×9 Gram in mpmath, `mp.eigsy`) gives

| x | double precision | dps 60 | dps 120 |
|---|---|---|---|
| 11/20 (seed 20260729) | −3.87·10^-9 | +5.4·10^-54 | −6.7·10^-115 |
| 1/2 (seed 777001) | −3.73·10^-9 | −6.3·10^-55 | +3.0·10^-115 |
| 11/20 (seed 424242) | −5.28·10^-9 | −5.9·10^-55 | −7.8·10^-115 |

i.e. the true minimum at those states is **exactly zero**, and the double-precision negatives are
roundoff. **Task-3 conclusion: no genuine violation exists at x = 11/20 (consistent with the frozen
P2/P4 result), but the −10^-9 tolerance does not survive a search that is allowed to visit
σ_min ≈ 10^-7.** The structural reason, which I derived and then checked at four x values
(7/20, 9/20, 1/2, 11/20): the direction **Z ∝ σ is always an exact zero mode**, because
g_θ(θ) = Σ_i λ_i²·(1/λ_i) = Tr θ = 1 on both sides. Hence λ_min(T_N − T_M) ≤ 0 identically, and at
x ≥ 1/2 it equals 0 exactly; every "no-violation" number in the E1 table at x ≥ 1/2 is a
measurement of roundoff around a guaranteed zero, whose size is set by the conditioning of the
states the search is permitted to visit.

## 6. Boundary-claim discipline audit (task 4)

Correct in the artifact: the explicit "the upper/no-violation side is bounded-search evidence, not
a theorem"; "No interpolation beyond the displayed bisection bracket is claimed"; the node's
`NUMERICAL` + `pending-review:` cap; the D2 and S3 sections' self-limiting language ("randomized
stress test … not an independent proof").

Incorrect or overstated: MAJOR-1 (the bracket's lower endpoint is *not* certified), MAJOR-3
("G0a passes numerically by a large margin at every reference dimension"), m1 (the evidential value
of the no-violation side), m4 (writing x_B ∈ [·,·] presumes a unique boundary, i.e. monotonicity
in x, which is nowhere established).

## 7. Standing failure modes (§2), item by item (7e)

1. sympy `.H` on real-symbolic matrices — n/a here (no sympy in the reviewed scan/certify path);
   screened.
2. WindowsApps interpreter — n/a; I used the pinned `C:<home>/cpython3119/python.exe` for
   every run.
3. Complement convention drift (3 vs padded 4, sign of a(Y), k factor) — **screened and cleared**
   by independent Kraus-vs-closed-form derivation and numerical match (§3.2).
4. Transpose vs conjugate transpose in HS adjoints — screened; superoperator matrices are real here
   so the two coincide (§2 type audit).
5. `sorted()` on symbolic eigenvalues — n/a (numerical path).
6. CRLF in SHA256SUMS — **violated by P6**, see m5.
7. Divided differences at degeneracies / enclosures dividing by near-zero gaps — screened; branch
   logic sound (§3.3), but the eigenvector padding is asserted rather than proved (m3).
8. ε log ε bookkeeping — n/a to P6 (no entropy expansion in scope; that is R5b/R5d territory).
9. Anchoring — screened: own implementation and own numbers first, comparison last (§1).

## 8. Value-vs-formula statement (7f)

- **Values verified** (specific points): the three Rayleigh quotients of §4 (exact rational inputs,
  60/120/240 digits, two implementations); the high-precision arbitration of three searched states
  at x = 11/20 and 1/2 (§5); the embedded d_R = 2, 3 values at x = 499/1000 (§9 MAJOR-3).
- **Formulas verified** (identities, derived by me and then checked at ≥ 2–4 parameter values, 7b):
  Λ^c from Kraus ≡ the closed form used by the certifier; the exact zero mode g_θ(θ) = Tr θ;
  the tensor factorization g_{ρ⊗θ}(P_r⊗Y) = p^{-1}g_θ(Y) (relative error 0 at d_R = 2 and 3);
  min over complex Z = min over Hermitian Z.
- **Not verified / out of scope:** the formal soundness of the author's interval machinery as
  *interval arithmetic* (m3) — I replaced it with precision-doubling plus residuals rather than
  auditing it as a proof; the d_R = 2, 3 no-violation statements at x ≥ 1/2 (I searched d_R = 1
  only); the actual value of x_B (nothing here locates it); everything about the P6b necessity
  theorem and the paper's §5 (frozen out of R5a; R5b's scope). I relied on the permitted frozen
  inputs only: P2/P4 (cBKM/signed-lift holds on [1/2,1), Q = P = 0) and P3 (Q > 0 on (0,x₁)).

## 9. Findings

### MAJOR-1 — the bracket's lower endpoint is *not* a certified violation; the licensing sentence and the artifact both overstate certification scope

`e1_certificates.json` contains exactly **eight** certificates, at x = 7/20, 2/5, 21/50, 11/25,
23/50, 12/25, 49/100, 499/1000, all d_R = 1. The four bisection points are recorded in a *separate*
`bisection` block, produced by `scan_pair(..., steps=1)` in **double precision** with the
classification rule `minimum_eigenvalue < -1e-9`:
999/2000 → −4.08·10^-3, 1999/4000 → −1.96·10^-3, 3999/8000 → −4.36·10^-4,
7999/16000 → −8.02·10^-5. None of them passed through `certify()`; there is no interval, no
rational witness, and no high-precision evaluation for any of them.

Consequently the artifact's sentence "Only the lower endpoint is a certified violation"
(`whgap_p6_relaxation_20260729.md`, S2 section) is **false** — the lower endpoint 7999/16000 is
precisely the one bracket point that is *not* certified — and the commission's licensing option (A)
inherits the error: "certified at the displayed rational grid points **and bisection points down to
7999/16000 (directed-interval Rayleigh-quotient witnesses)**". Writing (A) verbatim onto the node
would put an unsupported certification claim on disk (rule 1). Repair is easy and costs nothing
mathematically: certify the four bisection points with the existing `certify()` path (their
magnitudes, ≥ 8·10^-5, are ~4 orders above the noise band quantified in m1, so they will almost
certainly certify), or restrict the licensed scope to the eight d_R = 1 grid points and label the
bisection classifications as double-precision search.

### MAJOR-2 — the recorded 80-digit directed intervals do not enclose the value of the rational data recorded next to them

`certify()` reads the rational record through `core.matrix_from_rational_record`, which does
`float(Fraction(v))`, then `mp_matrix` does `mp.mpf(str(v.real))`; Hermitization and normalization
happen in numpy double as well. The object actually enclosed is therefore a float64/decimal
perturbation of the stored rational, at relative distance ~10^-16, while the reported enclosure has
width ~5.6·10^-70. My exact-rational evaluation (§4) differs from the recorded interval in the
**13th significant digit**:

- x = 7/20: exact-rational value −706.833715334567143521655023068 vs recorded interval
  [−706.83371533473089081892297…, −706.83371533473089081892297…] — gap 1.64·10^-10, i.e. ~10^60
  interval widths outside.
- x = 12/25: mine −8.62221737775022837955915 vs recorded −8.622217377750481748567 (gap 2.5·10^-13).
- x = 499/1000: mine −0.01882155247271347848465 vs recorded −0.018821552472713018063 (gap 4.6·10^-13).

So (i) every digit beyond ~13 in the artifact's "certified Rayleigh-quotient upper bounds" table is
spurious, and (ii) a reader who recomputes from the JSON's own rational data lands outside the
stated interval. The artifact's description ("witnesses were rationalized … and re-evaluated at
110 mpmath digits and 80 directed interval digits") asserts the rationalized objects were the ones
evaluated; they were not. **The conclusion survives** — I certify strict negativity for the exact
rationals at three points, including the tightest (499/1000, margin 1.9·10^-2 against a ≤10^-9
error budget) — but the certificate's *semantics* and its advertised precision must be corrected
(feed `mp.mpf(num)/den` from the `Fraction`s, Hermitize and normalize inside mpmath, and truncate
the reported digits to what the input representation supports).

### MAJOR-3 — the d_R ≥ 2 searches are demonstrably inadequate; the claim "G0a passes … at every reference dimension" is not supported at the strip edge

I proved (and verified numerically) the factorization: for σ_RA = ρ_R ⊗ σ_A and Z = P_r ⊗ Z_A with
P_r a rank-one spectral projector of ρ_R of eigenvalue p,
g_{ρ_R⊗θ}(P_r⊗Y) = p^{-1} g_θ(Y), hence any d_R = 1 violation embeds with the value multiplied by
1/p; with ρ_R = I/d_R, min_{d_R} ≤ d_R · min_{d_R=1}. Instantiating the recorded 499/1000 witness
(`tools/whgap_r5a_embed_check.py`, dps 60, relative error 0 against the prediction):

| d_R | embedded value (mine, explicit witness) | P6 E1 scan reported minimum |
|---|---|---|
| 1 | −1.8822·10^-2 | −1.8822·10^-2 ✓ |
| 2 | **−3.7643·10^-2** | −1.03·10^-12 |
| 3 | **−5.6465·10^-2** | −1.73·10^-10 |

The d_R = 2 and d_R = 3 searches at 499/1000 therefore miss a *trivially constructible* witness by
ten orders of magnitude (root cause visible in `whgap_p6_e1_scan.py`: `effective_steps` = 2 for
d_R = 2 and **0** for d_R = 3, with warm starts carried only from the previous x at the same d_R,
itself already under-optimized — 49/100 shows the same defect, −0.573 found where ≤ −5.43 is
embeddable). Consequences: (a) the artifact's "G0a passes numerically by a large margin at every
reference dimension" is unsupported near the edge; (b) the d_R = 2, 3 columns of the E1 table carry
no evidential weight where they report near-zero values and should not be read as the order's
reference-dimension behaviour; (c) nothing in the *licensed* conclusion depends on them, since the
certificates and the bisection are d_R = 1 — but any future claim about reference dimension must
re-run the multi-reference search with the embedding as a floor test.

### minors

- **m1 (evidential value of the no-violation side).** The difference form has an *exact* zero mode
  Z ∝ σ for every x and σ (§5), so at x ≥ 1/2 the true minimum is 0 and the scan measures roundoff.
  My search reaches −3.9·10^-9 … −7.1·10^-9 at x = 11/20 on states whose true value is 0 to
  50+ digits; P6's own worst clean-side number is −6.85·10^-10, only a factor 1.5 inside the
  preregistered floor. G0b's PASS is thus a property of the conditioning guard (which bars the
  states that produce larger roundoff), not a separation of scales; the effective resolution of the
  no-violation side is ~10^-7, not 10^-9. Recommendation: state the resolution explicitly, or
  re-evaluate the best few states per point at 60 digits (cheap — my probe cost 71 s for three
  states) so the no-violation side becomes a high-precision statement.
- **m2 (recorded objects are not the certified objects).** The stored `rational_witness` is not
  exactly Hermitian (exact departure 4.9·10^-16 at 7/20, 2.8·10^-15 at 12/25, **4.0·10^-12** at
  499/1000) and the stored `rational_sigma` has trace ≠ 1 (relative 3·10^-16). Harmless because
  `certify()` Hermitizes/normalizes, but the JSON should record the *post*-Hermitization,
  post-normalization rationals that were actually evaluated. Compounds MAJOR-2.
- **m3 (semi-rigorous enclosure).** `vec_pad = 8·residual/gap` and the entry-radius bound in
  `interval_bkm` are asserted with a one-line comment ("Weyl … residual/gap controls eigenvectors");
  no Davis–Kahan-type statement is cited or proved, `gap` is the global minimum positive gap
  (conservative, good) and the entry radius double-counts (also conservative), so the construction
  is plausible-with-slack rather than a verified interval computation. Given the 10^13 margins this
  is not decision-relevant, and my independent recomputation supplies the negativity conclusion by
  a different route (precision doubling + residual bounds).
- **m4 (quantifier hygiene, 7g).** "x_B ∈ [7999/16000, 1/2]" and the phrase "the order boundary"
  presuppose that the violation set is an interval, i.e. monotonicity of violation in x. Nothing in
  P6 establishes that. Preferred wording: "violations found at … ; none found at 1/2, 11/20", plus
  an explicit note that no monotonicity in x is claimed. (Also cosmetic: "down to 7999/16000"
  inverts the direction — the bisection ran *upward* from 499/1000.)
- **m5 (standing failure mode §2.6 violated by P6).** `artifacts/logs_whgap_p6_20260729/SHA256SUMS.txt`
  has CRLF line terminators, so `sha256sum -c` fails on every line ("No such file or directory").
  After `tr -d '\r'`, **all 33 hashes verify** — the frozen inputs are intact, but the provenance
  file as written does not check.
- **m6 (no defect; recorded for the record).** The certifier's complement is a hand-written closed
  form, not the Kraus definition; I derived the identity independently and confirmed agreement
  (≤ 4.7·10^-243) at three x values. This closes failure mode §2.3 for the reviewed path.
- **m7 (no defect; recorded).** Diagonalizing on the full complex operator space is equivalent to
  the Hermitian-direction problem (proof in §3.1); it makes every eigenvalue doubly degenerate, so
  the recorded eigenvector is Hermitian only up to phase and the Hermitization in `certify()` is
  load-bearing.
- **m8 (missing guard).** `certify()` asserts faithfulness of σ but never of the *outputs* Λ(σ),
  Λ^c(σ), which is what Γ^{-1} actually requires; a non-faithful output would silently poison
  c(a,b). I verified faithfulness at the three points I recomputed (min N-eigenvalue 6.1·10^-5 …
  1.97·10^-4). Add the assertion.

## 10. Verdict

**FINDINGS** (menu option B). I cannot sign option (A) as written: its scope sentence asserts
directed-interval certification for the four bisection points, which the disk contradicts
(MAJOR-1), and the displayed enclosures do not enclose the recorded rational objects (MAJOR-2).
None of the three MAJORs overturns the substantive result, and I independently reproduce strict
negativity at three witnesses including x = 499/1000.

For the decision layer's convenience, the scope statement I *would* endorse on the present
evidence — as a **repaired** (A), still at CERTIFIED\* tier and subject to the decision layer's own
adjudication of my MAJORs — is:

> cBKM-order violation is independently confirmed at the eight displayed rational d_R = 1 grid
> points 7/20 … 499/1000: P6's directed-interval bounds are semi-rigorous and are stated to
> spurious precision (R5a MAJOR-2), but R5a's independent exact-rational recomputation at
> 60/120/240 digits confirms strict negativity at 7/20, 12/25 and 499/1000 with margins ≥ 10^7
> times any plausible error, by two structurally independent implementations of the BKM form. The
> four bisection points (999/2000 … 7999/16000) are **double-precision search classifications
> only** (magnitudes 8·10^-5 … 4·10^-3, ~4 orders above the measured noise band) — NUMERICAL, not
> certified. The no-violation side at x ≥ 1/2 is bounded-search evidence whose effective resolution
> is ~10^-7, not the preregistered 10^-9, because the difference form has an exact zero mode Z ∝ σ
> and the observed roundoff on ill-conditioned states reaches 5·10^-9 (R5a §5); R5a's own
> high-precision arbitration finds the true minimum at x = 11/20 and x = 1/2 to be exactly 0,
> consistent with frozen P2/P4. The d_R ≥ 2 columns of the E1 table are not evidence (R5a MAJOR-3).
> No monotonicity in x, and hence no unique "boundary" x_B, is established by P6.

Requirements to reach an unstarred claim on this node: (i) re-run `certify()` with exact rational
inputs inside mpmath and truncate reported digits; (ii) certify the bisection points or relabel
them; (iii) re-run the d_R = 2, 3 searches with the embedding floor test; (iv) high-precision
re-evaluation of the no-violation side; (v) the separate exact necessity route (P6b/paper §5) —
out of this review's scope, R5b.

## 11. Provenance

Scripts (reviewer-authored): `tools/whgap_r5a_recheck.py`, `tools/whgap_r5a_floor_probe.py`,
`tools/whgap_r5a_embed_check.py`.
Logs and machine records: `artifacts/logs_whgap_r5_20260729/r5a_recheck.json` + `.log`,
`r5a_floor_probe.json` + `.log`, `r5a_embed_check.json` + `.log`, `r5a_zero_mode_check.log`,
`p6_sha256_verify.log`, and `SHA256SUMS.txt` (LF endings) covering all of the above plus this
report. Reproduce with
`C:<home>/cpython3119/python.exe tools/whgap_r5a_recheck.py` (27 s),
`… tools/whgap_r5a_floor_probe.py` (71 s),
`… tools/whgap_r5a_embed_check.py` (19 s).
Per the commission's single-writer deviation I made no edit to any node file, `NODE_INDEX.md`, or
the DAG doc; the decision layer performs those updates citing this artifact.

