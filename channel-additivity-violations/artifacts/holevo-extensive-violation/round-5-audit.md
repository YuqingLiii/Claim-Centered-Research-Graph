# Round 5 audit — fixed-partner global entropy and hierarchical amplification

Date: 2026-08-29

Source report: `round-5-fixed-partner-global-entropy-raw.md`

## Bottom line

The round's final verdict, **OPEN**, is correct. It did not prove or refute the fixed-partner
statement

`D_n(Xi)=Smin(Xi)+Smin(Phi_n)-Smin(Xi tensor Phi_n) -> 0`

for every fixed finite-dimensional channel `Xi`.

The useful advance is a cleaner separation of two gates:

1. the fixed-partner/free-compression entropy equality, which conditionally yields a
   finite-dimensional von-Neumann-MOE gap unbounded in absolute size; and
2. a genuinely quantitative growing-level rate condition, additionally needed to make the gap
   extensive in the full input/output/environment qubit cost.

The report's uses of **PROVED** are not proof-DAG completion stamps. Primary-source theorems and
new proposer-side deductions remain subject to the repository's independent rule-6/rule-7 review
before any local node can be promoted to a completion tier.

## Claim-by-claim audit

### 1. CFN gives a deterministic limiting defect — supported

CFN Theorem 8.1 states that, for every fixed finite-dimensional `Xi`, the entire output set of
`Xi tensor Psi_n` converges to a deterministic convex body as in their Theorem 3.9. Its proof
obtains condition `C_l` for every fixed matrix level. CFN Proposition 4.2 then transfers such
output-set convergence to minimum output entropy by continuity. Combining this with the BCN
single-channel limit gives, for fixed `Xi`,

`D_n(Xi) -> d_{k,t}(Xi)` almost surely,

where the limit is deterministic and nonnegative. Consequently a fixed-partner counterexample,
if one exists, has an eventual constant defect rather than a subsequence-only pathology.

This is a reduction, not an evaluation of the constant. CFN explicitly says that its general
tensor-product limiting body is difficult to analyse, even for a fixed identity partner.

Primary source: Collins--Fukuda--Nechita, arXiv:1311.7571, Theorem 8.1 and Proposition 4.2.

### 2. The universal `-log min(dim U,dim W)` bound — verified

Gour--Wallach Proposition 2 states exactly

`E(U tensor W) >= E(U)+E(W)-log min(dim U,dim W)`.

For fixed `U` this bounds the defect by `log dim U`, but does not make it vanish. The report's
four-party entropy inequality is weak monotonicity, hence equivalent to strong subadditivity; its
use here is sound. This bound therefore explains why elementary marginal-entropy arguments stop
at a fixed constant.

Primary source: Gour--Wallach, arXiv:0704.0251, Proposition 2.

### 3. FCEA-1/FCEA-2 — a valid reformulation, still the missing theorem

For a compact limiting output body `K`, the Gibbs variational formula gives

`min_{rho in K} S(rho) = inf_H [log Tr 2^H - h_K(H)]`.

Since product inputs already give the opposite entropy inequality, equality of the minimum with
the additive value is equivalent to the pointwise support-function bound labelled FCEA-2 in the
report. This removes the random and subsequence quantifiers, but does not prove the inequality.

The report found neither a primary theorem establishing FCEA-2 nor a fixed `Xi` violating it.
Accordingly `ADDGAP.fixed-partner-global-entropy` remains OPEN.

### 4. Fixed-dimension uniformization — proposer derivation appears correct

For fixed input/output dimensions `(p,q)`, the channel set `CPTP(p,q)` is compact. Audenaert
continuity applied after a diamond-norm perturbation of `Xi` gives a modulus for `D_Phi(Xi)` that
is independent of the random environment dimension and of the realization of `Phi`. A finite-net
argument therefore upgrades pointwise convergence in probability to uniform convergence in
probability over all `Xi` of those fixed dimensions. The almost-sure version follows on a
countable dense set and the same modulus.

This step is useful for a random history in the hierarchy, but it does not provide a rate uniform
in dimensions that grow with the level.

### 5. Conditional hierarchy — absolute-unbounded conclusion is sound in outline

Assume the fixed-partner gate for one BCN family and a uniform positive matched
`Phi_n`/`conjugate(Phi_n)` von-Neumann-MOE defect. Fixed-dimension uniformization lets one choose a
deterministic auxiliary dimension at each level that works uniformly over every possible earlier
history of that level's fixed dimensions. Summable failure probabilities leave positive
probability that every level succeeds. Complex conjugation supplies the second-side estimate
without another independent event. The exact bookkeeping is

`Delta(L_J,bar(L_J)) >= sum_{j<=J} (g_j-2 ell_j)`.

Thus a fixed positive `g_j` and sufficiently small per-level leakage produce `Omega(J)` gap. This
is a conditional existence proof of finite-dimensional instances with unbounded absolute MOE gap.

Two qualifications remain:

- the premise is precisely the still-open FCEA/fixed-partner lemma for the same random family;
- conversion to a same-channel Holevo gap also uses the separate pair-to-self/Fukuda--Weyl
  reductions, which are not currently independently certified in this DAG.

### 6. The claimed HP-style extensive implication fails — important correction accepted

The auxiliary dimensions `n_j` needed at successive levels may grow arbitrarily fast. The gap
bound is only `Omega(J)`, whereas the natural full channel size contains

`sum_{j<=J} log n_j + O(J)`.

Pointwise fixed-partner convergence supplies no bound on this sum. Therefore it does not by
itself imply a gap linear in the complete input/output/environment qubit cost. A second node is
required, formalized as `ADDGAP.growing-level-rate`.

The exact extensive bookkeeping target is

`sum_{j<=J}(g_j-2 ell_j) >= c sum_{j<=J} c_j - O(1)`,

where `c_j` is the qubit cost added by layer `j`.

## Resulting DAG decisions

- Keep `ADDGAP.fixed-partner-global-entropy` OPEN.
- Keep `ADDGAP.hierarchical-strong-additivity` OPEN.
- Register `ADDGAP.growing-level-rate` OPEN before any quantitative proof attempt.
- Correct the parent blueprint: fixed-partner additivity alone targets absolute-unbounded gap;
  fixed-partner additivity plus the growing-level rate gate targets full-size extensive gap.
- Do not treat the report's cited reductions as locally certified until independent review is
  archived under the DAG protocol.

## Remaining mathematical questions

1. Is FCEA-2 true for a BCN parameter pair with a positive `p=1` matched conjugate defect?
2. If true, can its convergence be made quantitative when the partner matrix level grows?
3. If false, can one exhibit a fixed finite-dimensional `Xi` with a positive limiting defect?
4. Can a different bounded-cost layer family make the extensive bookkeeping inequality hold?


