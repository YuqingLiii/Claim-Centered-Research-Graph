# WHGAP commission P13-B — the n = 2 entangled first-order layer (frozen 2026-07-30)

Commissioner: decision layer (Fable 5). Node (rule 8a): `WHGAP.onset-two-fifths` (P13),
obligation (d), n = 2 instance. ONE executor (fresh Opus instance). The paired rule-7
review is DEFERRED until the outcome is known (a bounded null stays NUMERICAL with
`pending-review:`; a positive witness triggers an immediate exact-verification + review
follow-up commission). Interpreter: `C:<home>/cpython3119/python.exe`. Scripts
`tools/whgap_p13b_*.py`; logs `artifacts/logs_whgap_p13b_20260730/` (create;
SHA256SUMS_p13b.txt, LF).

**Mandatory first step:** `research/PRETASK_RELOAD_PROMPT.md` with {PROBLEM_DIR} =
`channel-capacity/werner-holevo-gap`, {NODE_ID} = `WHGAP.onset-two-fifths`, ROLE =
executor; PRE-ACTION REPORT at the top of your artifact.

**Inherited frozen material:** conventions / standing failure modes / rule-7 embeds =
§1–§3 of [WHGAP_REVIEW_COMMISSION_R5_20260729.md](WHGAP_REVIEW_COMMISSION_R5_20260729.md);
plus the P13-A additions (radical-free rational charts; Berkowitz det instead of
Matrix.charpoly; substitute lowest even radical powers only). Single-writer deviation
binding (no node/index/DAG edits).

**Reviewed inputs you may rely on (7d):** the E-N1 machinery
(`WHGAP_N1PRIME_EXPANSION_LEMMA_20260729.md` §3–§4 — Prop 3.3 holds for ARBITRARY kernel
multiplicity m ≥ 1, R5d-confirmed in scope), the P13-A stratum-exhaustion note (+ R6),
the R5c closed form (n = 1 weight operator), P2/P4, P3+R5d (Q > 0 on (0, 2/5)).

## Question

For x in the strip [2/5, 1/2): does an ENTANGLED 2-copy pure input Psi on (C^3)^{x2}
support a first-order eps-log(1/eps) ascent of the 2-copy coherent information? A
certified YES at any strip x proves Q^(1)(Lambda_x^{x2}) > 0, hence Q(Lambda_x) > 0
there — shrinking the open strip. A bounded NO is structured n=2 evidence for the onset
conjecture.

## Setup (frozen)

Identify Psi on C^3 ⊗ C^3 with its 3x3 coefficient matrix M (Psi = sum_jk M_jk |jk>,
||M||_F = 1). The 2-copy channel is Lambda_x ⊗ Lambda_x with complement
Lambda_x^c ⊗ Lambda_x^c (16-dim padded environment, product Kraus K_a ⊗ K_b). For
rho_eps = (1-eps) P_Psi + eps phi:
- w_B(Psi,phi) = Tr[Pi_B (Lambda⊗Lambda)(phi)], Pi_B = orthogonal projector onto
  ker (Lambda⊗Lambda)(P_Psi) (dim m_B = 9 - r);
- w_E(Psi,phi) = Tr[Pi_E (Lambda^c⊗Lambda^c)(phi)], Pi_E = projector onto
  ker (Lambda^c⊗Lambda^c)(P_Psi) (dim m_E = 16 - r);
- r = common rank (isospectral nonzero spectra: pure global input), Ic_2(P_Psi) = 0.
- Weight operator D_Psi = M_B - M_E on C^9 with M_B = (Lambda⊗Lambda)†(Pi_B),
  M_E = sum_{ab,cd} (K_a⊗K_b)† (Pi_E)_{ab,cd} (K_c⊗K_d);
  first-order coefficient = Tr[D_Psi phi]; ascent iff lambda_max(D_Psi) > 0.
- The expansion Ic_2(rho_eps) = (w_B - w_E) eps log(1/eps) + O(eps) is the m ≥ 1
  instantiation of the reviewed machinery — STATE it with the explicit constants for the
  2-copy dimensions (gate S0); do not re-prove the reviewed ingredients, cite them.

## Stages and gates

**S0 (lemma instantiation).** Write the n = 2 expansion statement with explicit window
(eps <= g/4, g = smallest nonzero output eigenvalue) and remainder constant, citing the
reviewed Prop 3.3 / Lemmas 4.1–4.2 at multiplicities (m_B, m_E). One page, exact.

**S1 (exact structured layer, sympy).** Compute D_Psi (or at least lambda_max(D_Psi))
EXACTLY for the pre-registered families at x in {9/20, 21/50, 12/25} (and symbolically in
x where feasible):
 (a) product iso⊗iso: Psi = psi_0 ⊗ psi_0, psi_0 = (e1 + i e2)/sqrt2. Derive the
     product-kernel inclusion-exclusion Pi_B = Pi⊗1 + 1⊗Pi - Pi⊗Pi and the resulting
     D^(2) = D⊗1 + 1⊗D - (M_B⊗M_B - M_E⊗M_E) from first principles; verify
     lambda_max(D^(2)) = max over the 9 product-basis diagonal entries and record its
     sign on [2/5, 1/2) (expected <= 0 — verify, do not assume);
 (b) maximally entangled: M = 1/sqrt3 (and M = O/sqrt3 samples, O in SO(3));
 (c) global-isotropic entangled: families with Tr(M M^T) = 0 — at least
     M = (E_11 + i E_22)-type rank-2, M = (u v^T with u^T u = v^T v = 0), and a
     2-parameter interpolation between (a) and one of these;
 (d) iso ⊗ conj-iso: psi_0 ⊗ conj(psi_0).
 For each: exact ranks (r, m_B, m_E), lambda_max(D_Psi) exact or 50-digit certified.
 REGISTER every family outcome append-only, including nulls.

**S2 (degeneracy structure).** For generic Psi, (Lambda⊗Lambda)(P_Psi) is expected full
rank (then w_B = 0 and no ascent — the scan must live on the degeneracy variety).
Derive: the closed form of <conj(Psi)|(Lambda⊗Lambda)(P_Psi)|conj(Psi)> as a polynomial
in x and the O(3)xO(3)-invariants of M (candidates: Tr(M M^T), det M, Tr(M M^dag) = 1,
sigma-values) — the n = 1 analog was (1-x) tau^2. From it (and/or direct rank analysis)
give at least SUFFICIENT closed-form families with m_B >= 1 beyond S1's list. Stretch
(do not force): the full determinant factorization analog of det = x(1-x)tau^2/2.

**S3 (numeric sweep on the degenerate variety).** At x grid
{2/5, 41/100, 42/100, 43/100, 45/100, 47/100, 49/100}: maximize lambda_max(D_Psi) over
the S1/S2 degenerate families (their parameters) with >= 100 restarts per (x, family),
float64 + mpmath refinement of incumbents. Rank discipline (pre-registered): kernel
dimensions accepted ONLY when the spectral gap between the accepted-zero cluster and the
smallest kept eigenvalue exceeds 1e6 x the zero-cluster magnitude; otherwise the point is
recorded as rank-ambiguous and excluded (append-only list).

**Calibration gates (run FIRST, before any strip claim):**
- G-cal1 (must PASS): at x = 7/20 < 2/5 the machinery must certify
  lambda_max(D_Psi) >= d_1(7/20) = (1-x)(2-5x)/(2-x) > 0 via family (a)'s
  (psibar tensor slot) — the known n = 1 witness embedded at n = 2.
- G-cal2 (hard sanity, must PASS): at x = 11/20 > 1/2 NO family and no sweep point may
  yield lambda_max > 1e-9 (Q = 0 is PROVED there; a positive is a scanner defect, stop
  and diagnose).

**Decision gates:**
- G+ (witness): if any strip x yields lambda_max(D_Psi) > 1e-6 at a rank-unambiguous
  point: rationalize (Psi, top eigenvector phi-direction), re-verify EXACTLY (sympy
  ranks + exact or 80-digit directed evaluation of Tr[D phi]), and report immediately —
  cap NUMERICAL, pending-review; the decision layer will commission exact verification +
  review (this would prove Q > 0 at that x).
- G0 (bounded null): all strip points <= 0 within tolerance across all families and
  sweeps: record as NUMERICAL bounded-null evidence, pending-review, with the explicit
  coverage statement (families searched, restarts, rank-ambiguous exclusions).

**Budget:** <= 120 min compute. Honest-scoping rule as in P13-A: document resistance
append-only, do not force. Deliverable artifact:
`artifacts/whgap_p13b_n2_layer_20260730.md` + scripts + logs + SHA256SUMS_p13b.txt.
Return {status: DONE|BLOCKED, outcome: WITNESS|NULL|MIXED, summary, artifact_path,
best_strip_value}.

