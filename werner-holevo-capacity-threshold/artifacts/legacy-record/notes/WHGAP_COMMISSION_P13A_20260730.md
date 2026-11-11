# WHGAP commission P13-A — stratum exhaustion of the first-order mechanism (frozen 2026-07-30)

Commissioner: decision layer (Fable 5). Node (rule 8a): `WHGAP.onset-two-fifths` (P13),
obligations (b) and the first-order part of (c). Executor + paired fresh reviewer (R6),
one Opus instance each. Interpreter: `C:<home>/cpython3119/python.exe`. Scripts
`tools/whgap_p13a_*.py` / `tools/whgap_r6_*.py`; logs
`artifacts/logs_whgap_p13a_20260730/` (create; per-role `SHA256SUMS_*.txt`, LF).

**Mandatory first step (both agents):** `research/PRETASK_RELOAD_PROMPT.md` with
{PROBLEM_DIR} = `channel-capacity/werner-holevo-gap`, {NODE_ID} = `WHGAP.onset-two-fifths`,
ROLE as assigned; PRE-ACTION REPORT at the top of your note/report.

**Inherited frozen material:** conventions, standing failure modes, and rule-7 embeds are
§1–§3 of [WHGAP_REVIEW_COMMISSION_R5_20260729.md](WHGAP_REVIEW_COMMISSION_R5_20260729.md)
verbatim (they bind this commission too). Single-writer deviation likewise binding: no
node/index/DAG edits by agents; the decision layer applies outcomes.

**Reviewed inputs you may rely on (7d):** the R5-reviewed package — the expansion-lemma
machinery of `WHGAP_N1PRIME_EXPANSION_LEMMA_20260729.md` (Lemma 5.1, §3–§4 perturbation
bounds; R5d LICENSE A), the R5c closed form (D diagonal with d_1 = (1-x)(2-5x)/(2-x) and
the SO(3) transport), P2/P4 (Q = P = 0 on [1/2,1)), P3+R5d (Q > 0 on (0, 2/5)).
Everything else carries only its node status.

## Target statement (to be proved, refined, or honestly scoped)

**Theorem (stratum exhaustion, n = 1).** For every x in (0,1) and every pure qutrit state
psi with isotropy tau(psi) = |psi^T psi| > 0, and every state phi, the perturbation
rho_eps = (1-eps) P_psi + eps phi satisfies
Ic(rho_eps) = -w_E(psi,phi) * eps log(1/eps) + O(eps) with w_E >= 0.
Consequently NO tau != 0 pure base point supports a first-order eps-log-eps ascent at any
x; combined with the R5c closed form on the isotropic stratum, the n = 1 pure-base
first-order mechanism yields positive-capacity witnesses EXACTLY for x < 2/5.

## E-P13A — executor tasks (deliverable: proof note
`WHGAP_P13A_STRATUM_EXHAUSTION_20260730.md` in this notes/ directory)

**G0 (normal form).** Prove: every pure psi is equivalent under SO(3) x U(1) (global
phase) to psi_alpha = cos(alpha) e1 + i sin(alpha) e2, alpha in [0, pi/4], with
tau = cos(2 alpha). Route: psi = a + ib, phase-rotate to a.b = 0, SO(3)-align. State the
covariant transport of the whole first-order problem (cite the R5c transport
V = 1 (+) det(O) O — it applies verbatim at every stratum).

**G1 (Claim A: B-side rank).** Prove, exactly: in span{psi, psi_bar} the 2x2 block of
Lambda_x(P_psi) has
trace = 1 - x/2 and **det = x(1-x) tau^2 / 2**,
and the orthogonal complement carries eigenvalue x/2. Hence Lambda_x(P_psi) is full rank
iff tau > 0 (decision-layer pre-derivation — re-derive it, do not trust it). Record the
resulting exact spectrum {x/2, mu_+(x,tau), mu_-(x,tau)} in closed form.

**G2 (Claim B: leading coefficient).** For tau > 0: rank Lambda^c(P_psi) = 3 by
isospectrality (pure input), so ker Lambda^c(P_psi) = span{k(psi)}, dim 1. Assemble, with
the reviewed §3–§4 machinery (full-rank side analytic; E-side one-dimensional kernel
cluster), the expansion Ic(rho_eps) = -w_E eps log(1/eps) + O(eps), w_E =
<k|Lambda^c(phi)|k> >= 0, with an explicit remainder constant uniform in phi (state and
prove your bound; you may adapt the note's Prop 3.3 / Lemma 4.1 with citation — they are
reviewed inputs).

**G3 (Claim C: the kernel-avoiding set).** Derive w_E = Tr[phi K(k)^dagger K(k)] with
K(k) = sum_a conj(k_a) K_a (a single 3x3 matrix: sqrt(1-x) conj(k_0) 1 +
sqrt(x/2) sum_mu conj(k_{mu+1}) A_mu). Then w_E = 0 iff supp phi subseteq ker K(k).
K(k) psi = 0 always. CHARACTERIZE EXACTLY, in closed form over (x, alpha) with
tau > 0, when dim ker K(k) >= 2 (equivalently rank K(k) <= 1): compute k(alpha, x)
explicitly from the 4x4 Lambda^c(P_{psi_alpha}), form K(k), and analyze via 2x2 minors /
the structure a*1 + skew(w) (char roots a, a +- i sqrt(w.w) — mind complex bilinear w.w).
Deliverable: the exact exceptional set E = {(x, alpha) : dim ker K(k) >= 2, tau > 0}
(possibly empty).

**G4 (the linear layer on exceptions).** If E is empty: G4 is vacuous — state so, and the
Theorem holds with kernel-avoiding set {phi : supp phi = span{psi}} = {P_psi} (trivial
ascent direction; Ic identically 0 along it to first order — note the balanced/linear
layer at tau != 0 then needs NO further work for the Theorem as stated, since every
phi != P_psi has w_E > 0 strictly). If E is nonempty: for each exceptional stratum
compute the eps-linear coefficient c_1 = -Tr[Lambda(phi) log Lambda(P)] +
Tr[Lambda^c(phi) log Lambda^c(P)] on the kernel-avoiding phi and settle its sign on
[2/5, 1/2), or scope honestly what remains.

**G5 (sanity script `tools/whgap_p13a_sanity.py`).** (i) symbolic verification of G1's
det/trace identities and the closed spectrum; (ii) numeric spot-check of G2 at
(x, alpha) in {(9/20, pi/8), (9/20, pi/6), (1/5, pi/8)}: direct Ic(rho_eps) for 3 random
phi at eps in {1e-4, 1e-6} against -w_E eps log(1/eps); (iii) continuity crosscheck at the
tau -> 0 boundary against the R5c isotropic data (the tau = 0 limit of your G2 setup must
NOT be used for the isotropic stratum — different kernel dimensions; check instead that
your w_E formula at small tau approaches the isotropic w_E of the reviewed note §7.3
where it should); (iv) exceptional-set scan: numeric rank of K(k) on a (x, alpha) grid
(20 x 20) to corroborate G3's exact answer.

**Cap:** authorship licenses nothing — end at CONJECTURED/pending-review suggestions for
R6. Honest-scoping rule: if any gate resists inside ~90 min of compute, deliver the
partial result with the failure documented append-only; do not force.

## R6 — paired fresh review (report `artifacts/whgap_r6_review_20260730.md`)

Full rule-7 review of the E-P13A note: re-derive G0 normal form, G1 determinant (own
route — e.g. eigenvalue product or direct 3x3 det, not the executor's 2x2 block), G2
assembly and remainder, G3 kernel characterization INDEPENDENTLY (own parameterization of
k), G4 exception handling; reproduce G5 (ii) and (iv) with your own script at >= 2
parameter points each. c >= 2 identity gates; anchoring ban; value-vs-formula statements.

**Licensing menu:**
- (A) "The stratum-exhaustion Theorem is PROVED [state the exact scope incl. the
  exceptional set as characterized]; combined with the R5c closed form, at n = 1 the
  pure-base first-order mechanism yields ascent exactly on the isotropic stratum with
  x < 2/5 — P13 obligations (b) and first-order (c) are CLOSED."
- (B) FINDINGS (itemized MAJOR/minor).

## Batch deliverable format

Executor returns {status: DONE|BLOCKED, summary, note_path, exceptional_set}; reviewer
returns {verdict: LICENSE_A|FINDINGS, summary, majors[], minors[], report_path}. The
decision layer applies outcomes to `WHGAP.onset-two-fifths` (and cross-links), runs
validators, commits locally.

