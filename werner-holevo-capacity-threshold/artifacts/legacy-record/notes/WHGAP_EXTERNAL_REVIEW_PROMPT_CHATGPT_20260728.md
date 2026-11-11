# External cross-vendor review prompt (for ChatGPT Pro) — WHGAP core proof (2026-07-28)

Copy everything below the line into ChatGPT (best available reasoning model). It is
self-contained — no repository access needed. Paste the full reply back for archiving; it will
be recorded on the node as an external review artifact.

---

Please act as a hostile referee for the following quantum-information proof. Verify every
displayed identity yourself (by hand or your own computation), do not trust any claim, and
report: for each numbered claim, PASS or a concrete error; then an overall verdict. Be
maximally critical — finding a real flaw is the most valuable outcome.

**Setup (qutrit noisy Werner–Holevo family).** For x in (0,1) define
Lambda_x : M_3(C) -> M_3(C) by

    Lambda_x(X) = (1-x) X + (x/2) (Tr(X) I - X^T).

Kraus family: K_0 = sqrt(1-x) I, and K_{mu+1} = sqrt(x/2) A_mu for mu = 0,1,2, where
(A_mu)_{jk} = epsilon_{mu j k} (Levi-Civita, indices in {0,1,2}). Complementary channel
Lambda_x^c : M_3 -> M_4 with matrix elements (Lambda_x^c(X))_{ab} = Tr(K_a X K_b^dagger),
a,b in {0,...,3}.

**Claim 1 (structure).** sum_mu A_mu X A_mu^dagger = Tr(X) I - X^T and
sum_mu A_mu^dagger A_mu = 2I; hence sum_a K_a^dagger K_a = I (CPTP), Lambda_x(I) = I, and
Lambda_x^c(I) = diag(3(1-x), x, x, x). Lambda_x acts with eigenvalue 1 on I, (1 - 3x/2) on
symmetric traceless matrices, and (1 - x/2) on antisymmetric matrices.

**Claim 2 (lift and intertwining).** With
a(Y) = (Y_12 - Y_21, Y_20 - Y_02, Y_01 - Y_10)^T (indices 0-based), define
J_x : M_3 -> M_4 in block form

    J_x(Y) = [ [ p Tr(Y) ,  q a(Y)^T ],
               [ -q a(Y) ,  c1 Tr(Y) I + c2 Y + c3 Y^T ] ]

with p = 1/3, q = (1/3) sqrt(2(1-x)/x), c1 = 2(1-x)/(3x), c2 = (7x-4)/(3x),
c3 = -2(1-x)/(3x). Then J_x is adjoint-preserving (J(Y^dagger) = J(Y)^dagger) and satisfies
the Hilbert–Schmidt-adjoint intertwining relation

    J_x^dagger ∘ Lambda_x^c = Lambda_x.

At x = 1/2 this is exactly the lift of Zhu–Wang, arXiv:2607.24693, Eq. (4.12).

**Claim 3 (CP defect exactly on [1/2, 1)).** Define the operator-valued defect

    Delta_x(tau) = L_{Lambda_x(tau)} - J_x^dagger ∘ L_{Lambda_x^c(tau)} ∘ J_x,

where L_A(Y) = A·Y is left multiplication, so Delta_x(tau) is an operator on the 9-dimensional
Hilbert–Schmidt space M_3. Then tau -> Delta_x(tau), as a map M_3 -> L(M_3), is completely
positive (equivalently its 27x27 Choi matrix is PSD) **if and only if** 1/2 <= x < 1.
Moreover: at x = 1/2 the Choi has rank 3 and equals (2/9) sum_mu Choi(tau -> G_mu tau
G_mu^dagger) with G_mu|i> = |i>|mu> + (1/2)|mu>|i> - (1/2) delta_{mu i} sum_j |j>|j>; for
x in (1/2, 1) the rank is 8. Checkable samples: at x = 4/7 the Choi is PSD with rank 8; at
x = 49/100 it has an exact negative eigenvalue -102/1225.

**Claim 4 (uniqueness within the covariant family).** In the 5-real-parameter adjoint-
preserving ansatz above (p, q, c1, c2, c3 free), the intertwining relation imposes exactly
three independent linear conditions (one per O(3) sector), leaving a 2-parameter family; PSD
of the defect Choi then forces the parameters uniquely to the values in Claim 2.

**Claim 5 (capacity assembly).** Zhu–Wang's Theorem 3.3 (arXiv:2607.24693) states: if M, N
are finite-dimensional channels with M(I) ≻ 0 and N(I) ≻ 0, and there exists an
adjoint-preserving linear J with J^dagger ∘ N = M and Delta_J completely positive, then
N ⪰_cBKM M (complete Bogoliubov–Kubo–Mori domination). Their Lemma 3.2 (after
Belzig–Gao–Smith–Wu) upgrades this to complete relative-entropy domination N ⪰_cRE M under
output faithfulness. Hirche–Rouzé–Stilck França hybrid tensorization then yields
(Lambda_x^c)^{⊗n} ⪰_cRE (Lambda_x)^{⊗n} for every n; since (Lambda_x^c)^{⊗n} is a
complement of (Lambda_x)^{⊗n} (tensor of Stinespring isometries, up to environment
reordering), the standard Holevo-quantity and coherent-information comparisons give: the
optimized private information and optimized coherent information of Lambda_x^{⊗n} are 0 for
every n (pure inputs give I_c = 0; environment domination gives <= 0 — for the private case
discard p_u = 0 terms and use supp(rho_u) ⊆ supp(rho_bar); for the coherent case purify on
the Schmidt support and use the pair (psi_{RA^n}, psi_R ⊗ rho_{A^n})). Hence
Q(Lambda_x) = P(Lambda_x) = 0 for all x in [1/2, 1). At x = 1 the assembly fails because
Lambda_1^c(I) = diag(0,1,1,1) is not faithful.

**Questions.**
(a) Verify Claims 1–3 by direct computation. For Claim 3 verify at least x = 4/7 (PSD, rank
8) and x = 49/100 (negative eigenvalue -102/1225), and check the x = 1/2 rank-3
factorization.
(b) Verify Claim 4's counting (3 linear conditions; 2 free parameters) and, if you can, the
PSD-forcing uniqueness.
(c) Audit the logic of Claim 5 GIVEN the quoted theorem statements: any gap in support
conditions, order orientation, tensorization applicability, complement identification at
tensor powers, or the endpoint exclusions?
(d) Overall verdict: does this establish Q = P = 0 on [1/2, 1) — closing the (1/2, 4/7) gap
between Roofeh–Karimipour (antidegradability for x >= 4/7, PRA 109, 052620) and Zhu–Wang
(x = 1/2 only)? List every error, unjustified step, or needed caveat you find.

