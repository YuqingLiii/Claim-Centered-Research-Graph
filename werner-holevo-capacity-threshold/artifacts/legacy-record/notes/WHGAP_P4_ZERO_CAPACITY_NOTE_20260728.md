# WHGAP P4 theorem note — Q = P = 0 for the noisy Werner–Holevo family on [1/2, 1)

Node: `WHGAP.zero-capacity-application` (P4). Author: decision layer, 2026-07-28.
Status of this note: proposer write-up, **unreviewed** — it supports at most CONJECTURED with
`pending-review:` until the paired R3 review completes (DAG protocol rules 6/7).

Inputs and their provenance (frozen; nothing below re-proves them):

- **[ZW]** Zhu–Wang, arXiv:2607.24693 (local PDF in
  `channel-capacity/literature/papers/zhu-wang-2026-quantum-incapacity/`): Theorem 3.3
  (signed-lift CP-defect criterion), Lemma 3.2 (BKM-to-relative-entropy bridge, after [BGSW25]),
  Corollary 3.1 and Corollary 3.7 (information/capacity consequences), Theorem 4.3 (the x = 1/2
  instance and its proof pattern), and the hybrid tensorization they attribute to [HRSF22,
  Lemma 3.1]. These are cited generic theorems; this note checks their hypotheses, not their
  proofs.
- **[P2]** Execution artifact `artifacts/whgap_signed_lift_extension_20260728.md` and its
  R2 review `artifacts/whgap_p2_review_20260728.md` (claims 1–8 PASS; licensing statements 1–3
  open PROVED tier for the facts quoted below).
- **[RK24]** Roofeh–Karimipour, PRA 109, 052620 (2024): antidegradability of Lambda_x for
  x >= 4/7 (cited for the endpoint remark only).

Throughout, `Lambda_x(X) = (1-x) X + (x/2)(Tr(X) 1_3 - X^T)` on qutrits, with Kraus family
`K_0 = sqrt(1-x) 1_3`, `K_{mu+1} = sqrt(x/2) A_mu` (`(A_mu)_{jk} = epsilon_{mu j k}`), and
`(Lambda_x^c(X))_{ab} = Tr(K_a X K_b^dag)` on `H_E = C^4` (a, b in {0,...,3}).

---

## Theorem

**For every x in [1/2, 1) and every n >= 1,**

    P^(1)(Lambda_x^{tensor n}) = Q^(1)(Lambda_x^{tensor n}) = 0,

**and consequently P(Lambda_x) = Q(Lambda_x) = 0.**

Here Q^(1) is the optimized coherent information and P^(1) the optimized private information at
blocklength n, in the conventions of [ZW] Theorem 1.1/4.3; the capacities are their
regularizations (Lloyd–Shor–Devetak and Devetak, as cited in [ZW]).

**Corollary (gap closure).** `{x : Q(Lambda_x) = 0}` contains `[1/2, 1]`. In particular the open
interval `(1/2, 4/7)` left between [ZW] (x = 1/2) and [RK24] (x >= 4/7) is closed. (The endpoint
x = 1 is not covered by the Theorem — hypothesis (H1) fails there — but is antidegradable by
[RK24], which gives Q = P = 0 there by the standard antidegradability argument.)

---

## The certified inputs from [P2]/R2

For x in [1/2, 1) define the lift `J_x : L(H_B) -> L(H_E)` by

    J_x(Y) = [[ p Tr Y ,  q a(Y)^T ],
              [ -q a(Y), c1 Tr(Y) 1_3 + c2 Y + c3 Y^T ]]

with `a(Y) = (Y_12 - Y_21, Y_20 - Y_02, Y_01 - Y_10)^T` and

    (p, q, c1, c2, c3)
      = ( 1/3,  (1/3) sqrt(2(1-x)/x),  2(1-x)/(3x),  (7x-4)/(3x),  -2(1-x)/(3x) ).

R2-licensed facts (PROVED tier; licensing statements 1–2, claims 1–7):

- **(F1)** J_x is complex-linear (as a map on L(H_B)) with real block coefficients, hence
  adjoint preserving: `J_x(Y^dag) = J_x(Y)^dag`.
- **(F2)** Intertwining: `J_x^dag ∘ Lambda_x^c = Lambda_x` for every x in (0, 1) — the unique
  point of the equivariant residual family; at x = 1/2 it reproduces the [ZW] Eq. (4.12) lift.
- **(F3)** CP defect: the operator-valued defect
  `Delta_x(tau) = L_{Lambda_x(tau)} - J_x^dag ∘ L_{Lambda_x^c(tau)} ∘ J_x` is completely
  positive as a map `L(H_A) -> L(K_B)` exactly for x in [1/2, 1) (27x27 defect-Choi PSD; spin
  blocks `B_1 ∝ (1-x)(3x-1)`, `B_2 ∝ (1-x)(2x-1)`, rank-one; solver-free exact certificates at
  x = 26/51, 4/7, 3/4).
- **(F4)** Faithfulness data: `Lambda_x(1_3) = 1_3` and
  `Lambda_x^c(1_3) = diag(3(1-x), x, x, x)`, positive definite for 0 < x < 1. Provenance note:
  (F4) is established by P2 gate D1 and expressly passed by R2 claims 1, 6, and 9 (it is not
  literally named in R2's licensing statements 1–3); the R3 review additionally re-verified it
  by exact independent computation.

## Hypothesis check for [ZW] Theorem 3.3 (M = Lambda_x, N = Lambda_x^c)

- **(H1)** `M(1) = 1_3 ≻ 0` and `N(1) = diag(3(1-x), x, x, x) ≻ 0` for x in [1/2, 1) — by (F4).
  (Fails at x = 1: first entry 0. Hence the open right endpoint.)
- **(H2)** J_x is linear, adjoint preserving, `J_x^dag ∘ N = M` — by (F1) + (F2).
- **(H3)** `Delta_{J_x}` completely positive — by (F3).

All three hypotheses hold for every x in [1/2, 1). Theorem 3.3 gives

    Lambda_x^c  ⪰_cBKM  Lambda_x                                   (*)

and Lemma 3.2 (finite dimensions; strict faithfulness of the outputs per (H1)) upgrades (*) to

    Lambda_x^c  ⪰_cRE  Lambda_x.                                   (**)

## The seven obligations (R2 review claim 9), discharged

**(O1) CPTP and chosen complement.** `sum_a K_a^dag K_a = (1-x) 1_3 + (x/2) sum_mu A_mu^dag
A_mu = (1-x) 1_3 + (x/2)(2·1_3) = 1_3` (the Kraus identity `sum_mu A_mu^dag A_mu = 2·1_3` is
[P2] gate D1 / [ZW] Eq. (4.5)); all coefficients are real for x in [0,1], so `{K_a}` is a Kraus
family and Lambda_x is CPTP. Define the Stinespring isometry
`V_x : H_A -> H_B ⊗ H_E`, `V_x |psi> = sum_{a=0}^{3} K_a |psi> ⊗ |a>_E`; then
`V_x^dag V_x = sum_a K_a^dag K_a = 1`, `Tr_E(V_x X V_x^dag) = Lambda_x(X)`, and
`<a| Tr_B(V_x X V_x^dag) |b> = Tr(K_a X K_b^dag)`, i.e. `Tr_B(V_x · V_x^dag) = Lambda_x^c` is
exactly the displayed complement. So N is THE complement associated with V_x.

**(O2) Tensor powers.** `V_x^{⊗ n}`, composed with the canonical factor-reordering unitary
`W_n : (H_B ⊗ H_E)^{⊗ n} -> H_B^{⊗ n} ⊗ H_E^{⊗ n}`, is a Stinespring isometry for
`Lambda_x^{⊗ n}` with environment `H_E^{⊗ n}`, and
`Tr_{B^n}((W_n V_x^{⊗ n}) X (W_n V_x^{⊗ n})^dag) = (Lambda_x^c)^{⊗ n}`. Since complements are
unique up to an isometry on the environment (the standard freedom, as used in [ZW] §3),
`(Lambda_x^c)^{⊗ n}` is a complement of `Lambda_x^{⊗ n}`.

**(O3) Complete quantifier.** (**) is the COMPLETE relative-entropy order: for every finite
reference R and every admissible pair (`supp rho_{RA} ⊆ supp sigma_{RA}`),
`D((N ⊗ id_R)(rho) || (N ⊗ id_R)(sigma)) >= D((M ⊗ id_R)(rho) || (M ⊗ id_R)(sigma))`. Nothing
in our application narrows the quantifier: (H3) is complete positivity of the defect —
established at the Choi level, hence valid for every finite reference (R2 claim 4 verified the
27-dimensional Choi, which is equivalent to CP with arbitrary references by Choi's theorem, as
[ZW] Remark 3.4 spells out); Theorem 3.3 and Lemma 3.2 are stated by [ZW] at the complete
orders.

**(O4) Private-information step.** For blocklength n, reference R, and an ensemble
`{p_u, rho_u}` of inputs on `R A^n` with average `rho_bar = sum_u p_u rho_u`: discard all terms
with `p_u = 0` (they contribute nothing to either Holevo quantity); for every u with `p_u > 0`,
`p_u rho_u ⪯ rho_bar` implies `supp rho_u ⊆ supp rho_bar`, so each pair `(rho_u, rho_bar)` is
admissible. Applying (**) tensorized (O6) with reference R term by term:

    chi_B - chi_E = sum_u p_u [ D(M_n,R(rho_u) || M_n,R(rho_bar))
                              - D(N_n,R(rho_u) || N_n,R(rho_bar)) ] <= 0,

with `M_n = Lambda_x^{⊗ n}`, `N_n = (Lambda_x^c)^{⊗ n}`. Optimizing over ensembles gives
`P^(1)(Lambda_x^{⊗ n}) <= 0`; the singleton ensemble gives `P^(1) >= 0`. Hence `= 0`. This is
exactly the [ZW] Theorem 4.3 / Corollary 3.7 argument with the support condition made explicit.

**(O5) Coherent-information step.** For an input `rho` on `A^n`, purify on the Schmidt support:
take R of dimension `rank(rho)` and a purification `psi_{R A^n}`; the comparison pair used by
[ZW] Corollary 3.1 is `(psi_{R A^n}, psi_R ⊗ rho_{A^n})`, and since `psi_R` (the R-marginal of
the purification) is full rank on R by the Schmidt construction, `supp(psi) ⊆
supp(psi_R ⊗ rho)` — an admissible pair. (Any second factor of the form `sigma_R ⊗ rho` with
`sigma_R` full rank works equally; [ZW] use `psi_R`.) With (**) tensorized (O6),
`I_c(rho, Lambda_x^{⊗ n}) <= 0` for every rho; pure inputs give `I_c = 0` (output and
environment marginals of a pure bipartite state share spectra). Hence
`Q^(1)(Lambda_x^{⊗ n}) = 0`.

**(O6) Tensorization orientation.** By (**) at n = 1 and the hybrid tensorization [HRSF22,
Lemma 3.1] as quoted and applied in [ZW] §3.1 (their Eq. after Lemma 3.1, iterated
identical-pair specialization):

    (Lambda_x^c)^{⊗ n}  ⪰_cRE  Lambda_x^{⊗ n}   for every n >= 1,

which — with (O2) identifying `(Lambda_x^c)^{⊗ n}` as the complement of `Lambda_x^{⊗ n}` — is
precisely the domination used in (O4)/(O5). The capacities are then
`P(Lambda_x) = lim_n (1/n) P^(1)(Lambda_x^{⊗ n}) = 0` and
`Q(Lambda_x) = lim_n (1/n) Q^(1)(Lambda_x^{⊗ n}) = 0` by the regularization theorems cited in
[ZW] (Devetak; Lloyd–Shor–Devetak).

**(O7) Endpoint exclusion.** At x = 1, `N(1) = diag(0, 1, 1, 1)` is not faithful, so (H1) and
Lemma 3.2's faithfulness hypothesis fail; x = 1 is excluded from the Theorem (and covered
instead by [RK24] antidegradability, as noted in the Corollary).

∎

## Scope, caveats, and what this note does NOT claim

1. **Below 1/2:** nothing here addresses x < 1/2. The covariant certificate provably fails
   there (R2 licensing statement 1); whether Q > 0 immediately below 1/2 is the open node
   `WHGAP.qpositive-onset` (P3). The full averaging/WLOG lemma (non-equivariant infeasibility)
   remains unwritten — only its two ingredients are PROVED-licensed (R2 statement 3).
2. **Generic theorems:** [ZW] Theorem 3.3 / Lemma 3.2 / Corollaries 3.1, 3.7 and the [HRSF22]
   tensorization are used as published statements (hypothesis-checked here, per the R2 claim-9
   audit); they were not independently re-proved in this project, and no local copy of [HRSF22]
   has been audited (R2 flagged this as the one literature-side untested regime).
3. **Conventions:** all objects are in the frozen P2 conventions (epsilon ordering, a(Y),
   row-major HS identification); R2 verified there is no sign/transpose/Choi-leg drift between
   the frozen conventions and [ZW].
4. This note's own correctness is subject to the paired R3 review; until then the node status
   cap is CONJECTURED with `pending-review:`.

## Revision 2026-07-28 (post-R3)

The R3 review (`artifacts/whgap_p4_review_20260728.md`) completed with claims 1, 4, 5, 7, 8, 9
PASS and three MINOR wording/attribution findings, each fixed in place above (the reviewed
original wording is quoted in the R3 report):

1. (F1) said "real-linear"; corrected to complex-linear with real block coefficients (R3
   claim 3).
2. (F4) provenance made explicit: P2 gate D1 + R2 claims 1/6/9, not R2's licensing statements
   1–3 literally; R3 re-verified exactly (R3 claim 2).
3. (O5) comparison-pair attribution corrected to [ZW] Corollary 3.1's
   `(psi_{RA^n}, psi_R ⊗ rho_{A^n})`, replacing the underdefined `pi_R` phrasing (R3 claims
   6/7g).

No mathematical content changed. R3's licensing: Theorem gate OPEN at PROVED on [1/2, 1)
(HRSF22-via-ZW provenance note); Corollary gate OPEN at CERTIFIED\* on [1/2, 1] (RK24 endpoint
cite-only); the (1/2, 4/7) gap-closure substatement lies within the PROVED Theorem scope.

## Revision 2 — 2026-07-28 (post external ChatGPT-Pro review)

The external cross-vendor hostile-referee review
(`artifacts/whgap_external_review_chatgpt_20260728.md`) passed all claims and contributed a
strengthening, decision-layer verified (log
`artifacts/logs_whgap_fable_audit_20260728/fable_audit_ext.log`):

**Remark (x = 1 via the minimal complement).** At x = 1 the Kraus operator K_0 vanishes.
Dropping the zero Kraus direction yields the minimal 3-dimensional environment with complement
`Λ_{1,min}^c(X) = (1/2)(Tr X · 1 − X^T) = Λ_1(X)` — the channel is self-complementary. Taking
J = id (adjoint preserving; intertwining trivially exact; defect ≡ 0, hence CP) satisfies all
hypotheses of [ZW] Theorem 3.3 with faithful outputs `Λ_1(1) = 1 ≻ 0`. The assembly of the main
Theorem then runs verbatim, so Q(Λ_1) = P(Λ_1) = 0 by the same mechanism, and the Theorem
extends to the CLOSED interval [1/2, 1]. The O7 endpoint exclusion applies only to the padded
4-dimensional complement presentation; the Corollary no longer needs RK24 for the endpoint.
Also recorded: closed-form defect-Choi spectrum {0^19, [4(1−x)(2x−1)/x]^5,
[16(1−x)(3x−1)/(9x)]^3} (unnormalized Choi convention), and the uniqueness scope is the
five-REAL-parameter ansatz (complex Im(r) direction remains an open classification item).
This revision's claims enter the paper draft and are subject to the paper's own review cycle.

