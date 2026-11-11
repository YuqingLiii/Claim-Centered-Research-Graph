# Independent review of WHGAP.antideg-boundary (2026-07-28)

## Review identity, scope, and outcome

I am a fresh reviewer. I did not author the reviewed work and was given no
desired outcome. I read the frozen conventions, then wrote and ran my own
channel, Choi, exact-calibration, and symmetric-extension implementations
before opening the proposer scripts, artifact tables, or logs.

**Overall verdict: MAJOR on the proposer's SDP formulation and reported
`t*(x)`/solver-sign bracket; PASS on C1-C5; MINOR on the printed C6 proof
linkage; PASS, with numerical-only caveats, on the narrower qualitative
finding "4/7 numerically tight."**

The major issue is concrete. The frozen criterion permits every
swap-*invariant* extension on
`A tensor B1 tensor B2`, dimension 27:

`(I_A tensor S_12) eta (I_A tensor S_12) = eta`.

Such an operator has an 18-dimensional `+1` swap block and a 9-dimensional
`-1` swap block. The proposer instead sets `eta = V rho V.T`, where
`V: R^18 -> R^27` spans only `A tensor Sym^2(B)`. This silently sets the
entire 9-dimensional antisymmetric block to zero and tests a stronger
bosonic-extension problem, not the frozen conjugation-invariant problem.
For example, the proposer reports
`t*(1/2) = -6.944444443839e-4`; two independent formulations of the
frozen problem give
`t*(1/2) = -4.62962962963e-4` (approximately `-1/2160`).

All reviewed proposer hashes match its archived
[`SHA256SUMS.txt`](logs_whgap_20260728/SHA256SUMS.txt). Reproduction was
performed with proposer code imported unchanged and all writes redirected to
[`logs_whgap_review_20260728/proposer_reproduction/`](logs_whgap_review_20260728/proposer_reproduction/).

## 7c and 7f - anchoring and value/formula decoupling

The independent implementation is
[`whgap_independent_review.py`](logs_whgap_review_20260728/whgap_independent_review.py).
It uses lexicographic indices
`(a,b) -> 3a+b` and `(a,b1,b2) -> 9a+3b1+b2`. Its SDP independently
parameterizes both swap sectors by real symmetric blocks of sizes 18 and 9.
The unreduced cross-check
[`whgap_full_sdp_crosscheck.py`](logs_whgap_review_20260728/whgap_full_sdp_crosscheck.py)
uses a full real-symmetric 27-by-27 variable and the explicit swap equality.
The two formulations agree.

The channel, normalized Choi formula, and lexicographic basis names
necessarily coincide with the frozen specification and partly coincide
notationally with the proposer. That coincidence is flagged; the code and
numbers were fixed before the proposer files were opened. The swap-sector
formulation does **not** coincide with the proposer: it retains the omitted
9-dimensional block.

Thus:

- the reviewer's values are **verification by independent construction**;
- the redirected run is **reproduction of proposer behavior**;
- reproduction confirms what the proposer program printed but does not repair
  its formula;
- independent-construction agreement corroborates C1-C6 and the qualitative
  boundary value, but it does not validate the proposer's restricted SDP or
  its displayed `t*(x)` table.

## 7a - per-display type and basis audit

Here `H_A = H_B = C^3`, `H_E = C^4`, and `x` is a scalar in `[0,1]`.
`L(H)` denotes the operator space on `H`.

| Displayed identity or construction | Domain, codomain, and dimensions | Audit |
|---|---|---|
| `Lambda_x(X)=(1-x)X+(x/2)(Tr(X)I-X^T)` | `L(C^3) -> L(C^3)`, 9-dimensional operator spaces; every summand is 3-by-3 | PASS. Exact basis check; scalar factors agree. |
| `A_mu(j,k)=epsilon_(mu j k)` and `K_0=sqrt(1-x)I`, `K_(mu+1)=sqrt(x/2)A_mu` | each `A_mu,K_a: C^3 -> C^3`; four 3-by-3 Kraus maps | PASS. `sum A_mu X A_mu^dag=Tr(X)I-X^T` on all nine `E_ij`; `sum A_mu^dag A_mu=2I`. |
| `Lambda_x^c(X)_(ab)=Tr(K_a X K_b^dag)` | `L(C^3) -> L(C^4)`, 9 to 16 operator dimensions; indices `a,b=0,...,3` | PASS. Constituents multiply as 3-by-3 matrices and output a 4-by-4 matrix. |
| `omega_x=(id tensor Lambda_x)(Phi)` | `omega_x in L(C^3 tensor C^3)`, 9-by-9; `Phi=|Phi><Phi|`, `|Phi|=1` | PASS. The construction uses exactly `1/3`, and the same normalized `omega_x` is imposed as the SDP marginal. Exact formula: `omega_x=(1-x)Phi+(x/6)(I-F)`. |
| `T_A` | `L(H_A tensor H_B) -> L(H_A tensor H_B)`, 9-by-9 to 9-by-9 | PASS. The implementation sends entry `(a,b; a',b')` to `(a',b; a,b')`; it is `T_A`, not `T_B`. |
| `a(Y)` and `J(Y)` | `a: L(C^3)->C^3`; `J: L(C^3)->L(C^4)`, represented by a 16-by-9 Hilbert-Schmidt matrix | PASS. All four blocks in `J(Y)` have compatible sizes `1`, `1x3`, `3x1`, `3x3`; `J^dag: L(C^4)->L(C^3)`. |
| `J^dag o Lambda^c = Lambda` | `L(C^3)->L(C^4)->L(C^3)` | PASS on all nine matrix units. |
| `L_theta(Y)=theta Y` and `Delta(tau)=L_Lambda(tau)-J^dag L_Lambda^c(tau) J` | `L_theta in L(L(H))`: 9-by-9 for `H=C^3`, 16-by-16 for `H=C^4`; `Delta(tau)` is a 9-by-9 superoperator | PASS. The commission omitted the definition of `L_theta`; Eq. (3.15) of the cited local Zhu-Wang PDF resolves it as left multiplication. |
| `G_mu|i>` and `(2/9) sum G_mu tau G_mu^dag` | `G_mu: C^3 -> C^3 tensor C^3`, matrices 9-by-3; RHS is 9-by-9 and has the same type as `Delta(tau)` | PASS on all nine `tau=E_ij`; Gram matrix is exactly `4I_3`. |
| `Phi`, `P^-`, `P_st`, and `W` | all in `L(C^3 tensor C^3)`, 9-by-9 | PASS. The three projectors have ranks 1, 3, and 5. |
| `H=(W_AB1 tensor I_B2 + S_12(W_AB1 tensor I_B2)S_12)/2` | `H in L(C^3 tensor C^3 tensor C^3)`, 27-by-27 | PASS independently. `S_12=I_A tensor S_B1B2` maps `(a,b1,b2)` to `(a,b2,b1)` in the same lexicographic ordering. Exact congruence elimination gives 24 positive pivots and an exact 3-dimensional zero residual. |
| Frozen extension constraints | `eta in L(A tensor B1 tensor B2)`, 27-by-27; `S_12:27->27`; `Tr_B2 eta in L(A tensor B1)`, 9-by-9 | PASS in the reviewer implementations. The partial trace is `sum_b2 eta[(a,b1,b2),(a',b1',b2)]`, exactly the ordering used to build `eta` and `omega_x`. |
| Proposer `eta=V rho V.T` | `V: R^18 -> R^27`, `rho` 18-by-18, `eta` 27-by-27 | **MAJOR.** Well typed, but only the `+1` swap sector is represented. Swap conjugation requires block diagonal `18+9`, not support solely in the 18-dimensional sector. |
| Proposer exact affine projection | 27-by-27 rational candidate; residual and marginal 9-by-9; `residual_A` 3-by-3 | PASS as a typed failed attempt. The code verifies its projected marginal and swap equality exactly, then finds an exact negative Rayleigh form; it does not assert exact PSD. |
| Proposer dual extraction | 81 scalar equality duals | MINOR/INCOMPLETE by design. It does not assemble or verify the full exact dual cone constraint, and correctly claims no certificate. |

The restriction to real symmetric SDP variables is legitimate for this
real-valued marginal and constraints: averaging any complex Hermitian feasible
point with its entrywise conjugate preserves positivity, the swap equality,
and the marginal.

## 7d - six calibration ground truths

These results come from the independent exact construction, not from rerunning
the proposer. Raw exact output is in
[`whgap_independent_results.json`](logs_whgap_review_20260728/whgap_independent_results.json).

| Claim | Verdict | Independent result |
|---|---|---|
| C1 Kraus action and CPTP identities | PASS | Both identities hold exactly on all nine matrix units. |
| C2 `Lambda(I)=I` and `Lambda^c(I)=diag(3/2,1/2,1/2,1/2)` | PASS | Exact equality. |
| C3 `spec(omega^(T_A))` | PASS | `{1/4:5, 0:1, -1/12:3}` exactly. General spectrum is `(1-2x)/3` (multiplicity 1), `(2-x)/6` (5), `(3x-2)/6` (3). |
| C4 lift identity and non-PSD `J(E_00)` | PASS | Lift holds on all nine matrix units; `J(E_00)=diag(1,-1,2,2)/3`. |
| C5 defect factorization and `G` Gram matrix | PASS | Exact full-basis equality; Gram matrix `4I_3`. |
| C6 witness value and `H >= 0` | PASS for the mathematical claims; MINOR for proposer proof linkage | Witness value is exactly `(4sqrt(3)-7)/10<0`. Independent exact congruence proves `H>=0`, rank 24. The proposer checks the stated spin blocks but does not construct/check the orthogonal recoupling that links its directly built `H` to those blocks; the local paper supplies that link. |

The Choi eigenvalue multiplicities were handled at the identity level:
`spec(omega_x)={1-x (x1), x/3 (x3), 0 (x5)}` and the partial-transpose
projector formula above was verified symbolically, not inferred from an
aggregate solver output.

## 7b - endpoint and regime-complete numerical gates

The frozen full SDP objective is necessarily at the solver floor on every
feasible point: `omega_x` has a five-dimensional kernel, and a strictly
positive 27-by-27 `eta` would have a strictly positive marginal. Therefore
`t*(x)<=0` for all `0<x<1`, with equality throughout the feasible region.
Raw sign bisection is intrinsically ill conditioned.

The review used both the 18+9 swap-block formulation and a full 27-by-27
formulation. Clean SCS results agree; CLARABEL is an alternate solver but
returned `optimal_inaccurate` at several ill-conditioned points, so those
statuses were not laundered into evidence.

| Regime | x | Correct full-SDP `t*(x)` | Clean status / interpretation |
|---|---:|---:|---|
| mandated endpoint | 0.500000000000 | `-4.629629629e-4` | `optimal`; infeasible |
| left interior | 0.520000000000 | `-2.432432432e-4` | `optimal`; infeasible |
| left interior | 0.550000000000 | `-4.310343562e-5` | `optimal`; infeasible |
| left interior | 0.570000000000 | `-1.942351685e-7` | `optimal`; negative but inside the commission's broad `[-1e-6,-1e-9)` tolerance gap |
| left interior | `4/7-1e-4` | `-9.480600651e-10` | `optimal`; full objective is already at its resolution floor |
| mandated endpoint | `4/7` | `4.272122775e-11` (block), `3.530415519e-11` (full) | `optimal`; feasible at `1e-9` tolerance |
| right interior | `4/7+1e-4` | `-8.326418565e-10` | `optimal`; feasible at `1e-9` tolerance |
| right interior | 0.600000000000 | `-4.124840677e-10` (block), `8.371891554e-12` (full) | `optimal`; feasible at `1e-9` tolerance |
| right interior | 0.750000000000 | `5.190332976e-11` | `optimal`; feasible at `1e-9` tolerance |
| right interior | 1.000000000000 | `-2.093759689e-13` | `optimal`; feasible at `1e-9` tolerance |

To obtain a meaningful boundary check, the review also used the support forced
by positivity: for `0<x<1`,
`supp(omega_x)=span{Phi, Alt^2(C^3)}` (dimension 4), so every PSD extension
is supported in `supp(omega_x) tensor B2` (dimension 12). The resulting
support minimum-eigenvalue margin is strongly negative below `4/7`
(`-1/6` at `1/2`, `-0.05` at `0.55`, `-0.003333...` at `0.57`,
`-0.000233333...` at `4/7-1e-4`) and at the numerical floor at and above
`4/7`.

Using clean `optimal` status, `t_support<-1e-8` on the infeasible side, and
`t_support>=-1e-9` on the feasible side, the reviewer's own operational
bracket is

`[0.5714285629136222, 0.5714285714285714]`,

width `8.514949190e-9`, with midpoint

`x*_review = 0.5714285671710968`.

The midpoint is `4.257474595e-9` below `4/7`. This is a tolerance bracket,
not an exact primal/dual certificate. The full log is
[`whgap_support_margin_tolerance.log`](logs_whgap_review_20260728/whgap_support_margin_tolerance.log).
The preserved raw-sign attempt demonstrates why raw signs are not a valid
oracle in the feasible face.

Endpoint verdicts: **PASS for infeasible/feasible classifications; MAJOR for
the proposer's displayed `t*` values because they solve the wrong restricted
SDP.**

Boundary verdicts:

- qualitative "`4/7` numerically tight": **PASS with CERTIFIED*-level
  caveats**, independently corroborated;
- proposer bracket
  `[0.571428384100,0.571428392615]`: **MAJOR** as a boundary bracket. It
  excludes `4/7`, uses raw signs around `1e-12`, and comes from the restricted
  18-dimensional SDP;
- exact equality `x*=4/7`: **GAP**. No exact infeasibility certificate below
  `4/7` and no exact boundary proof were produced.

## 7e - standing failure modes

- **Dropped/extra normalization:** checked; no error. Choi normalization
  `1/3` is consistent between construction and marginal constraint.
- **Type/dimension mismatch:** **found** at the semantic level: the proposer
  substitutes the 18-dimensional bosonic sector for the full `18+9`
  swap-invariant operator space.
- **Undefined terms and stability ranges:** see 7g; boundary and general
  tolerance semantics are not fully resolved.
- **Partial object for full object:** **found**; this is the principal MAJOR
  defect.
- **Values while derivation is broken:** separated. The independent full
  construction corroborates the qualitative value but not the proposer
  formula or table. C6 is independently proved despite the script's omitted
  recoupling check.
- **Sign/transpose drift:** none found. The review verified `T_A`, not `T_B`,
  and verified the direction/action of `S_12`.
- **Solver-status laundering:** proposer archived only `optimal` SCS
  statuses, but many tighter warm-start solves report zero iterations and do
  not make floor-level signs reliable. The review rejected all
  `optimal_inaccurate` CLARABEL results as gates.
- **Rounding asserted exact:** none found. The proposer explicitly records
  that the rational affine projection is not PSD and that the dual candidate
  is not an exact certificate.

## 7g - quantifier hygiene

| Term | Resolution |
|---|---|
| `antidegradable` | The reviewed documents provide the symmetric-extension equivalence but do not separately define the degrading-map term. The criterion is sufficient for this numerical scope. |
| `boundary` | Not explicitly quantified in the artifact or node (for example as `inf{x: Lambda_x is antidegradable}`), and the bisection assumes a single monotone transition without proving monotonicity. The review uses that infimum as an operational definition only. This prevents an exact/full-quantifier verdict. |
| `tight` | Resolved by pre-registered G2 as distance at most `1e-6` from `4/7`. Under that numerical definition, the independent result passes. It does not mean exact equality. |
| `certificate` | The feasible-side exact certificate is adequately specified as rational affine feasibility plus exact PSD. The dual certificate conditions are not fully displayed or checked; no dual certificate is claimed. |
| `feasible at tolerance` | Endpoint semantics are explicit (`t>=-1e-9` high, `t<-1e-6` low), but bisection changes to the raw test `t>=0`. This convention drift is material because every feasible full-SDP point has true optimum zero. |
| `exact` | Exact C1-C6 means symbolic identities/PSD. No exact boundary, primal extension, or dual witness is established, and the artifact correctly disclaims them. |

## Exactness/certificate claims

- The six calibration identities are exact and independently verified.
- The proposer exact affine projection fails exact PSD by an exact negative
  Rayleigh form; reproduction confirms that result.
- The proposer dual rationalization is not an exact dual-feasibility
  certificate; reproduction confirms the disclaimer.
- The denominator-200 output `4/7` is only a rational candidate and lies
  outside the proposer solver-sign bracket; the artifact correctly says so.
- The expression logged under `quadratic_surd_candidate` is transcendental,
  not a quadratic surd, and is explicitly rejected in the artifact.
- No exact antidegradability-boundary claim passes.

## Untested or unresolved regimes

These limitations cap any surviving licensing at `CERTIFIED*`:

1. no exact rational primal extension at `x=4/7` or above;
2. no exact dual infeasibility witness for any `x<4/7`;
3. no analytic proof of a unique/monotone antidegradability boundary over all
   `x in [0,1]`;
4. no clean alternate-solver boundary run (CLARABEL was
   `optimal_inaccurate` at several ill-conditioned points);
5. no second independent exact-algebra stack beyond SymPy 1.13.1;
6. no numerical complex-Hermitian run, although conjugation averaging proves
   the real restriction is without loss here;
7. the RK24 analytic `x>=4/7` theorem was cited but not independently
   re-reviewed from a local paper in this commission;
8. exact primal/dual certificate branches remain unsuccessful, rather than
   silently promoted from rounded data.

## Licensing statement

**This review does not open the completion gate for the full node claim
"compute the exact antidegradability boundary `x*` via the frozen
symmetric-extension characterization and decide whether `x*<4/7`," at tier
`CERTIFIED*` (and therefore not at `PROVED`), with scope the exact boundary,
the proposer's displayed `t*(x)` table, and its solver-sign bracket.**

The reasons are the proposer's omitted 9-dimensional swap sector, undefined
boundary/monotonicity quantifiers, and absence of exact primal/dual
certificates.

**This review does open a narrowly scoped completion gate at tier
`CERTIFIED*` for the statement "`4/7` is numerically tight under the
pre-registered `1e-6` meaning," with scope limited to the independently tested
full swap-invariant endpoint/interior regimes and the operational review
bracket
`[0.5714285629136222,0.5714285714285714]`.** It does not license exact
equality, the proposer formula, or a `PROVED` status. Status application, if
any, belongs to the separate decision layer; this review writes no node
status.

## Review artifacts

- Independent exact and 18+9 block implementation:
  [`whgap_independent_review.py`](logs_whgap_review_20260728/whgap_independent_review.py)
- Full 27-by-27 cross-check:
  [`whgap_full_sdp_crosscheck.py`](logs_whgap_review_20260728/whgap_full_sdp_crosscheck.py)
- Support-margin boundary check:
  [`whgap_support_margin.py`](logs_whgap_review_20260728/whgap_support_margin.py)
- Redirected proposer reproduction:
  [`whgap_proposer_reproduction.py`](logs_whgap_review_20260728/whgap_proposer_reproduction.py)
- Review manifest:
  [`SHA256SUMS.txt`](logs_whgap_review_20260728/SHA256SUMS.txt)


