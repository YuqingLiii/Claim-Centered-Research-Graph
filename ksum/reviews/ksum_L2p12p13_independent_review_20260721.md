# Independent Rule-7 review of k-Sum L2 Phases 12 and 13

Date: 2026-07-21  
Reviewed node: `KSUM.B4b.L2.ALT.multipair.variable-pair-totals`  
Reviewer role: fresh independent reviewer; no proposer mathematics or code authored  
Scope: the Phase-12 orbit-moment formula and three scoped obstruction assertions, and the
Phase-13 `N=8,q=5,m=K=2` exact finite discriminator  

## Verdict and status ceiling

**Mixed PASS/PARTIAL.** The finite Phase-13 core is independently reproduced exactly, and the
Phase-12 printed orbit-moment formula agrees entry by entry with a separately derived group-action
construction on the entire finite gate.  The affine-product correlation obstruction is also
verified in its stated conditional scope.  The displayed single-alternant residual and the
Bun--Thaler dichotomy are not sufficiently defined in the proposer memo to pass a Rule-7 type or
quantifier audit; they remain plausible, narrowly scoped proposer claims, not completion-tier
results.

The reviewed canonical node must remain **OPEN**.  Its claim asks for an asymptotic nonseparable
signed kernel with constant correlation and high-`C_t` mass; neither Phase 12 nor Phase 13 constructs
one or rules out the full class.

Status ceilings by subclaim:

- The fully specified finite lemma in this report (`N=8,q=5,m=K=2`, moments of degree `<D`) is
  eligible for **PROVED** if it is registered verbatim as its own proof node and this completed
  review is cited.  This review supplies a fresh derivation, exact commands, logs, script hashes,
  primal witnesses, and a dual certificate.
- The general Phase-12 moment formula is proved combinatorially after the rigorous restatement
  below, but the original memo omits the allowed `q`/fixed-point range and has no identity gate for
  `K<m` or `rho>=3`.  As a general separate node it should be capped at **CERTIFIED\*** until those
  regimes are gated and the statement adopts the explicit domain below.  Its `m=K=2` specialization
  is covered by the finite PROVED recommendation.
- The order-`R` tensor affine-difference correlation calculation is correct conditional on the
  assumed legal box and YES/NO pattern.  The memo does not exhibit or type the box-to-histogram map,
  so no claim that such a box exists in every required regime is certified.
- The printed single-alternant and Bun--Thaler obstruction statements are at most
  **CONJECTURED** as written.  Their variables and lift maps are missing, so Rule 7a/7g fail.
- The specific proposer claims “18-term polynomial,” the orbit-list SHA, and the `1/896` perturbation
  are not independently certified: the polynomial/list/serialization/perturbation was not archived.
  The existential dual-certificate claim is nevertheless verified by a different explicit
  17-term certificate.

No DAG, node, index, handoff, or status file was edited by this reviewer.

## Anchoring-ban record (Rule 7c)

The review proceeded in two deliberately separated stages.

1. I read only the canonical node's one-sentence claim, current status, and short experimental
   assertions.  Before opening either proposer artifact, I independently defined the orbit domain,
   derived the group-averaged falling-factorial moments, enumerated the 24 orbits, constructed all
   moment matrices, and solved the exact primal and dual problems.  The frozen derivation is
   [`pre_proposer_derivation.md`](logs_ksum_L2p12p13_review_20260721/pre_proposer_derivation.md).
2. Only after freezing and running that construction did I open the Phase-12/13 memos.  I then wrote
   a second implementation that directly evaluates the proposer's displayed injection formula and
   compared it with the first construction.

The notation `A_{a,b}`, `F_gamma`, `m`, and `rho` below overlaps the proposer because those symbols
were adopted only in the post-disclosure comparison.  The pre-disclosure construction instead used
canonical four-cell vectors and the independent `W_2` group action.  This coincidence is therefore
identified rather than presented as an independent notational invention.

## From-scratch construction and type audit (Rule 7a)

### General displayed moment formula

The following is the typed version of the formula that was actually reviewed.

- Parameters: integers `N>=0`, `m>=0`, and `0<=K<=min(m,N)`.  Here `m` is the number of two-cycles
  of the complementary-value involution.  A claim in terms of `q` must separately state the parity
  and number of fixed symbols; the Phase-12 memo does not.
- Split domain:
  `Omega_N={(r,u) in Z_{>=0}^2: r<=u, 1<=r+u<=N}`.
- Histogram domain:
  `X_{N,m,K}={H in Z_{>=0}^{Omega_N}: sum H=K,
  sum_(r,u)(r+u)H_{r,u}=N}`.  Thus a histogram is an integer vector of dimension
  `|Omega_N|`, subject to two affine constraints; it is not itself a probability distribution.
- Add the unused-slot coordinate `Hbar_{0,0}=m-K`, giving exactly `m` split instances.
- A query pattern is a list
  `alpha=((a_1,b_1),...,(a_rho,b_rho)) in (Z_{>=0}^2)^rho` on `rho` distinct
  complementary pair labels.  Its total degree is `d=sum_j(a_j+b_j)`.  The displayed rational
  formula is defined for `rho<=m` and `d<=N`.  Empty products define the `rho=d=0` case.
- The within-pair orientation average is the scalar map
  `A_{a,b}:Z_{>=0}^2 -> Q`,
  `A_{a,b}(r,u)=((r)_a(u)_b+(r)_b(u)_a)/2`.
- An injection `iota:[rho]->[m]` selects an ordered list of distinct slots.  The orbit moment is

  `F_alpha:X_{N,m,K}->Q`,

  `F_alpha(H)=1/((N)_d(m)_rho) sum_(iota injective)
              product_j A_{a_j,b_j}(r_{iota(j)},u_{iota(j)})`.

  The denominator is nonzero precisely in the stated range.  Query patterns with `d>N` or
  `rho>m` are impossible/zero but cannot be evaluated by this fraction without a separate
  convention.

This identity follows by averaging a fixed multilinear query first over `S_N` positions, producing
`(N)_d^{-1}` times falling factorials, then over assignments of the `m` complementary pair labels,
producing `(m)_rho^{-1}`, and finally over the two orientations of every selected pair, producing
`A`.  Grouping repeated slot types gives products `(Hbar_tau)_{nu_tau}`.  Their total falling-factorial
degree is `sum nu_tau=rho`, so `deg_H F<=rho`; in slot occupancies the degree is at most `d`.

If the distinguished fixed symbol has support count zero, a query using it contributes
`(0)_{gamma_h}`.  This is 1 for `gamma_h=0` and 0 otherwise.  The symbol `h`, the number of fixed
symbols, and the parameter range where there is exactly one such symbol must be defined in any
general claim; they are not defined in the Phase-12 memo.  In the Phase-13 gate, adding the omitted
fixed-symbol query rows merely adds zero rows and changes neither rank nor nullspace.

The earliest pair-detecting gate has `rho=1,(a,b)=(1,1)`.  Since
`A_{1,1}(r,u)=ru`, the formula gives exactly
`F_(1,1)(H)=C_t(H)/(m(N)_2)`.  Its domain is `N>=2,m>=1`; outside it the displayed division is
undefined.

### Finite operator and LP types

For `N=8,q=5,m=K=2`, every orbit is a canonical vector
`x=(x_1,x_2,x_3,x_4) in Z_{>=0}^4` with total eight and both pair totals positive, modulo
`W_2=(S_2)^2 semidirect S_2`.  The orbit set `X` has dimension 24 as a finite indexing set.

Let `Q_D` be the `W_2`-orbits of four-cell nonnegative query multiplicities with total degree `<D`.
The unnormalised integer matrix used independently is

`M_D in Z^{|Q_D| x 24}`,

`M_D[alpha,x]=sum_(beta in W_2 alpha, distinct) product_i (x_i)_{beta_i}`.

Its rows differ from the rational `F_alpha` rows by the nonzero factor
`|W_2 alpha|(N)_{|alpha|}`.  Hence the two matrices have the same row space and kernel.  The exact
comparison script also evaluates the printed `F` directly rather than relying only on this scaling
argument.

The signed witness has type `w in Q^24`; moment annihilation is the identity
`M_D w=0 in Q^{|Q_D|}`.  The target is `s in {+1,-1}^24`, with `s_x=+1` iff
`C_t(x)=x_1x_2+x_3x_4>0`.  The primal is
`max <s,w>` subject to `M_Dw=0` and `||w||_1<=1`.  A dual polynomial-value vector has type
`p=M_D^T y in Q^24`; `||s-p||_infinity<=epsilon` is a global upper certificate
`<s,w><=epsilon` for every feasible `w`.

## Regime-complete finite gates (Rule 7b)

The exact finite tests cover:

- all 24 legal orbits, including YES and NO, diagonal and non-diagonal splits, equal and unequal
  pair totals, and nontrivial pair-exchange stabilizers;
- query patterns using zero, one, and two complementary pair types (`rho=0,1,2`), every degree
  appearing below the stated cutoff, and both orientation-stabilized and generic query orbits;
- `D=2` as the positive control, `D=8` as the nontrivial nullspace regime, and `D=9` as the
  full-rank negative control;
- the identity `M_Dw=0`, not only traces or aggregate moments;
- all preregistered tail thresholds `T=4,6,8`, with the actual absolute tail rather than a split-LP
  surrogate;
- direct formula-value identities on all `63*24=1512` entries for `D=8` and all
  `92*24=2208` entries for `D=9`.

Not covered by a numerical identity gate are `K<m` (unused complementary-pair slots), `rho>=3`,
more than one fixed symbol, even-`q` complement structure, or asymptotic `D=Theta(sqrt(N))`.  The
general combinatorial derivation includes unused slots algebraically, but Rule 7b still requires
these missing qualitative regimes to be named.  Consequently the general formula is capped as
described in the verdict, and no asymptotic conclusion is licensed.

## Exact Phase-13 reproduction

Independent enumeration gives exactly 24 legal orbits.  With degree interpreted, as the memo says,
as **strictly less than** `D`:

| `D` | rows | rank | nullity |
|---:|---:|---:|---:|
| 2 | 2 | 1 | 23 |
| 8 | 63 | 20 | 4 |
| 9 | 92 | 24 | 0 |

At `D=2`, `-1/2` on any NO orbit and `+1/2` on any YES orbit annihilates the constant and fixed-total
linear rows, has unit `l1`, and has sign correlation 1.

At `D=8`, exact extreme-ray enumeration gives a unit-`l1` annihilator with sign correlation `1/32`.
One exact optimal witness that also satisfies every tail gate is:

| orbit | `C_t` | weight |
|---|---:|---:|
| `(0,2;0,6)` | 0 | `-1/64` |
| `(0,2;1,5)` | 5 | `3/32` |
| `(0,2;2,4)` | 8 | `-15/64` |
| `(0,2;3,3)` | 9 | `5/32` |
| `(0,6;1,1)` | 1 | `1/64` |
| `(1,1;1,5)` | 6 | `-3/32` |
| `(1,1;2,4)` | 9 | `15/64` |
| `(1,1;3,3)` | 10 | `-5/32` |

It has zero mass, unit `l1`, and exact absolute tail masses

- `31/32` on `C_t>=4`,
- `7/8` on `C_t>=6`,
- `25/32` on `C_t>=8`.

All exceed the preregistered `1/4` threshold.  An exact rational LP independently produces
`p in rowspace(M_8)` with `||s-p||_infinity=1/32`.  Therefore no feasible witness, tail-constrained
or otherwise, can exceed `1/32`; the displayed primal attains it.  The complete 17 nonzero
coefficients of this independently found degree-at-most-seven certificate and every residual are in
[`emit_exact_dual_certificate.log`](logs_ksum_L2p12p13_review_20260721/emit_exact_dual_certificate.log).
The YES-indicator correlation is half the sign correlation, namely `1/64`; the memo's convention is
confirmed to be the `{+1,-1}` sign convention because its `D=2` positive control is 1.

At `D=9`, degree eight enters and the 24 columns have full rank, so the only annihilator is zero.
Deleting the `(1,1)` row leaves ranks 20 and 24 at `D=8,9`, respectively, confirming its redundancy.

The proposer memo's “18-term” certificate is not printed, so this review verifies existence and the
optimal value using a different 17-term row-basis certificate; it does not verify that unpublished
representation.  Likewise, the claimed orbit-list hash has no serialization rule or archived list,
and the `1/896` perturbation does not identify the modified orbit, old/new label, witness, or norm.
Those three provenance-specific assertions remain unverified.

## Phase-12 obstruction audit

### Affine Moebius/simplex differences: scoped PASS

For a legal binary box with `R` independent directions, the order-`R` tensor first difference has
`2^R` coefficients of equal absolute value.  Unit-`l1` normalization makes each magnitude `2^{-R}`.
If exactly one corner is NO and all others YES, zero total mass makes sign correlation twice the
absolute weight of that NO corner, hence exactly `2^(1-R)`.  This independently matches the memo.

This proves only the conditional calculation.  “Legal affine box,” the map from box coordinates to
histograms, and the range in which one-NO/all-other-YES holds are not supplied.  It does not obstruct
arbitrary nonseparable signed kernels.

### Single alternant: qualitative support, printed identity unauditable

For a single rectangular alternant in two side counts, the mixed second difference of
`C_t(r,u)=ru` is `(r-r')(u-u')`, nonzero for a nondegenerate rectangle.  Thus a generic lone
alternant indeed fails the degree-two moment gate.  However, the memo's stronger printed residual
`-V(s) sum_i r_i^2` has no definitions for `s`, `r_i`, the number/range of indices, the sign
convention for `V`, or the map from an alternant row to a legal histogram.  Its domain, codomain,
and dimensions therefore cannot be audited.  Linear combinations of alternants can also cancel
individual mixed differences, exactly as the memo's scope caveat acknowledges.

### Bun--Thaler lift: conditional arithmetic only, lift identity unauditable

Under the natural reconstruction in which `k` balanced pairs carry common total occupancy `M/k`,
legality requires positive integers with `2k` dividing `M`; then each pair contributes
`(M/(2k))^2` and the total is indeed `M^2/(4k)`.  Polynomial moment annihilation in `k` alone does
not automatically annihilate `1/k`.  Reparametrizing by a fixed per-pair total `s` instead gives
`C_t=ks^2/4`, polynomial in `k` when the required parity/integrality holds.

That verifies the scalar arithmetic only.  The memo never defines the inner/outer signed measures,
their domains, the pushforward/lift operator, its mass-preservation identity, the meaning of
“both kill constants,” or the correlation functional after lifting.  Consequently the asserted
zero-correlation identity has no well-typed displayed map to check and cannot pass Rule 7a, 7b, or
7g.  The result remains restricted to the unnamed literal lift and cannot rule out corrected
invalid-parameter/shared-boundary constructions.

## No frozen-input immunity (Rule 7d)

No prior review was treated as frozen.  The variable-total histogram parametrization, position and
alphabet orbit averages, normalization factors, target-pair statistic, all ranks, both LP sides,
and every tail constraint were reopened and derived independently for their present use.  The
Phase-11 asymptotic endpoint/support claims were not used to establish the finite lemma and are not
endorsed here.  General `q` parity/fixed-point structure was explicitly reopened and found missing
from the Phase-12 statement.

## Standing failure-mode audit (Rules 7e and 7f)

- **Dropped/extra normalization:** `(N)_d`, `(m)_rho`, and the `1/2` orientation average were derived
  independently.  A post-disclosure implementation of the printed formula matched the independent
  orbit-sum construction exactly on 3,720 entries.  The independent integer rows differ only by a
  nonzero row factor, which is sufficient for rank/kernel statements but is not silently equated
  to the normalized probability value.
- **Type/dimension mismatch:** all finite maps and matrix dimensions are stated above.  The
  alternant and lift claims fail this check because their maps are absent.
- **Undefined ranges/terms:** `h`, the `q` range, “nonfixed,” “legal affine box,” `V(s)`, `r_i`,
  “literal `(M,k)` parametrization,” “mass-preserving lift,” “inner/outer,” “kill constants,” and
  “local dual error” are unresolved in the proposer artifacts.  The rigorous finite restatement
  avoids them or defines them.
- **Orbit/full-central confusion:** the independent construction averages `S_N` positions through
  falling factorials and the full `q=5` complement-preserving symbol action through `W_2`.
  Fixed-symbol query rows are zero on this support.  No colored-orbit sum was substituted for a
  full central sum in the finite gate.
- **Numerics versus printed derivation:** the first script constructs the operator independently
  from the group action; it corroborates the same values but, by itself, would not verify the printed
  formula.  The second script separately implements the printed injection formula and compares every
  value.  Thus the finite displayed formula is checked both as an independent construction and as a
  printed formula.  The grouped-histogram degree statement is checked analytically.  The unpublished
  18-term polynomial and perturbation experiment are not checked.
- **Hardcoded-output risk:** ranks, witnesses, LP optima, formula comparisons, and certificates are
  computed from enumerated matrices by exact SymPy arithmetic.  The scripts do not print hardcoded
  rank/optimum literals.  The explicit certificate is recomputed and its row-space identity checked.

## Quantifier hygiene (Rule 7g)

The finite conclusion is universally quantified over all 24 explicitly defined orbit classes and
all query orbit rows of degree `<D` for `D in {2,8,9}`.  Tail means
`sum_{x:C_t(x)>=T}|w_x|`, and correlation means `<s,w>` for the explicitly defined sign target.
“Degree `<D`” is strict; using `<=D` would shift the rank statement and is not interchangeable.

The general formula is valid on the explicit `(N,m,K,rho,d)` domain above.  No conclusion is made
for an unspecified relation between `q` and `m`, even `q`, extra fixed points, `d>N`, `rho>m`, or an
asymptotic cutoff.  The undefined Phase-12 terms listed in the standing audit prevent completion-tier
use of those obstruction statements.

## Commands, environment, and immutable provenance

Environment: Python 3.12.9; SymPy 1.14.0.

Commands run from the repository root:

```powershell
python artifacts\logs_ksum_L2p12p13_review_20260721\independent_orbit_lp_review.py |
  Tee-Object -FilePath artifacts\logs_ksum_L2p12p13_review_20260721\independent_orbit_lp_review.log

python artifacts\logs_ksum_L2p12p13_review_20260721\printed_formula_and_tail_gate_check.py |
  Tee-Object -FilePath artifacts\logs_ksum_L2p12p13_review_20260721\printed_formula_and_tail_gate_check.log

python artifacts\logs_ksum_L2p12p13_review_20260721\emit_exact_dual_certificate.py |
  Tee-Object -FilePath artifacts\logs_ksum_L2p12p13_review_20260721\emit_exact_dual_certificate.log
```

SHA-256:

| file | SHA-256 |
|---|---|
| `independent_orbit_lp_review.py` | `9ffda791dcb43ffda95aff4d54821037351f58f17f8ea8f65233b60f8c3f7157` |
| `independent_orbit_lp_review.log` | `b5fa912de8fa7d5f4632977c4a46c17e02d1cd25253f9ea979f23df58ceab837` |
| `pre_proposer_derivation.md` | `c9c3da1f8bf5ebb4959e10038243c4d6e3750ba50c91d03c78e0156b1cc149ab` |
| `printed_formula_and_tail_gate_check.py` | `5877ea55bf47d89782d46020d789e5d5713d4e1155ff7741f3d41fc0882749ed` |
| `printed_formula_and_tail_gate_check.log` | `f4858c1bcba5fc1ac55612b7e3eb5d0fd14df1782e5de8de85845e9fa40494a3` |
| `emit_exact_dual_certificate.py` | `4e0a9d82d46f67ed2f7745d765b2acfe28e8a4c3b89b06406055efeea4ec353f` |
| `emit_exact_dual_certificate.log` | `c724bdf5f19cc716ac0aa6145a08ae58fafd9b6d47e6709a8613ec82de1c16fd` |

