# Independent Rule-7 review: shared-branch Young-lattice patch kernel

Date: 2026-07-22  
Reviewed canonical node:
`KSUM.B4b.L3.ALT.hidden-frequency-mask.critical-endpoint.ALT.shared-branch-young-lattice-patch-kernel`  
Reviewed proposer artifact: comparison deliberately deferred until after Section 1 was written  
Reviewer role: fresh independent checker; this file does not edit the canonical DAG

## 0. Review protocol and anchoring order

I first read only the canonical node's front matter, Claim, Role in DAG, and Kill criteria.  I did
not read `ksum/artifacts/ksum_L3_critical_shared_branch_young_lattice_patch_audit_20260722.md` before
deriving Section 1.  I did read the general DAG protocols and reopened the earlier exact
`p=0,u=1` orbit/skeleton and parent-grid inputs for the limited physical-block use made below.
Those earlier artifacts were treated as context, not as authority for the Young-graph argument.

Section 1 is the independent construction.  Sections 2 onward will be completed only after the
proposer artifact is opened.  This ordering is the Rule-7(c) anchoring record.

## 1. Independent reconstruction before reading the proposer derivation

### 1.1 Typed Young graph and the boundary-degree lemma

Let

\[
 \mathcal Y_n=\{\lambda:\lambda\vdash n\},\qquad
 \mathcal Y_{n-1}=\{\beta:\beta\vdash n-1\},
\tag{I.1}
\]

finite sets of cardinalities `p(n)` and `p(n-1)`.  Write `beta nearrow lambda` when `lambda/beta`
is one removable corner.  For nonempty `S subseteq mathcal Y_n`, put

\[
 D(S)=\{\beta\in\mathcal Y_{n-1}:\beta\nearrow\lambda
          \text{ for some }\lambda\in S\},
 \qquad d_S(\beta)=|\{\lambda\in S:\beta\nearrow\lambda\}|.
\tag{I.2}
\]

Thus `D(S)` is a finite set and `d_S(beta)` is a nonnegative integer.  Choose the
lexicographically maximal `lambda=(lambda_1,...,lambda_t)` in `S`, with `lambda_t>0`, and delete
its last-row corner.  The resulting `beta` has `d_S(beta)<=2`:

* if `lambda_t=1`, every parent of `beta` other than `lambda` adds in a row `<t` and is
  lexicographically larger than `lambda`, hence is not in `S`;
* if `lambda_t>1`, the same excludes every parent obtained by adding above row `t`; besides
  `lambda`, the only possible non-larger parent adds a new row `t+1`.

This proves the literal combinatorial statement for every nonempty level support.  It does not
by itself prove that this boundary predecessor has nonzero physical off-equality norm: the
removed corner may belong to a selected singleton channel, and equality deletion is extra
orbital data.

### 1.2 The fixed-singleton Pieri cone

Now specialize to the exact critical subsequence

\[
 a=k^2,\quad d=k,\quad m=d+1,\quad n=am,\quad q=4a,
 \qquad p=0,\quad u=1.
\tag{I.3}
\]

All parameters are positive integers, and the asymptotic statements below require `m>2`.  Fix an
arbitrary partition `alpha vdash a` and define the position Pieri cone

\[
 \mathcal C_\alpha
 =\{\lambda\vdash n:c^\lambda_{\alpha,(n-a)}=1\}.
\tag{I.4}
\]

Here `c` is a Littlewood--Richardson coefficient and `(n-a)` is the one-row partition.  Pieri's
rule says exactly that `lambda/alpha` is a horizontal strip.  Equivalently, after padding by
zeros,

\[
 \lambda_i\ge\alpha_i\ge\lambda_{i+1}\qquad(i\ge1).
\tag{I.5}
\]

Both sides of each inequality are integers.  Summing the right inequalities gives

\[
 \sum_{i\ge2}\lambda_i\le\sum_{i\ge1}\alpha_i=a,
 \qquad
 \lambda_1\ge n-a,
 \qquad
 \lambda_2\le\alpha_1\le a.
\tag{I.6}
\]

Thus `lambda_1>lambda_2` for `m>2`, so the first-row corner is removable for every
`lambda in mathcal C_alpha`.  This is uniform in the shape and number of rows of `alpha`.

### 1.3 First-row hook-weight lower bound

For `lambda vdash n`, let `f^lambda=dim S^lambda`.  If `lambda` has `ell` nonzero rows, set

\[
 h_i=\lambda_i+\ell-i\qquad(1\le i\le\ell).
\tag{I.7}
\]

The `h_i` are strictly decreasing positive integers.  Removing the first-row corner and applying
the hook formula gives the scalar identity

\[
 p_1(\lambda):={f^{\lambda-e_1}\over f^\lambda}
 ={h_1\over n}\prod_{j=2}^{\ell}
 {h_1-h_j-1\over h_1-h_j}.
\tag{I.8}
\]

Every object in (I.8) is a scalar; this is not an operator identity.  Since
`{h_2,...,h_ell}` is a subset of `{1,...,h_2}` and all factors lie in `(0,1]`,

\[
 \prod_{j=2}^{\ell}{h_1-h_j-1\over h_1-h_j}
 \ge\prod_{t=1}^{h_2}{h_1-t-1\over h_1-t}
 ={h_1-h_2-1\over h_1-1}.
\tag{I.9}
\]

The denominator is nonzero because first-row removability gives `h_1-h_2>=2`.  Consequently

\[
 p_1(\lambda)\ge {\lambda_1-\lambda_2\over n}
 \ge {n-2a\over n}=1-{2\over m}
 \qquad(\lambda\in\mathcal C_\alpha).
\tag{I.10}
\]

The inequality directions in (I.9)--(I.10) are important: adding the omitted factors, each at
most one, makes the comparison product smaller.

### 1.4 Normalized down-incidence and its singular-value bound

Let `S subseteq mathcal C_alpha` have cardinality `s`.  Define the scalar normalized down-incidence

\[
 A_S:\mathbb C^S\longrightarrow\mathbb C^{D(S)},\qquad
 (A_S)_{\beta,\lambda}
 =\mathbf1[\beta\nearrow\lambda]
  \sqrt{{f^\beta\over f^\lambda}}.
\tag{I.11}
\]

Its matrix dimensions are `|D(S)| x s`.  The Young branching identity
`f^lambda=sum_(beta nearrow lambda) f^beta` makes each column have Euclidean norm one, but it
does not make different columns orthogonal.

The first-row predecessor map

\[
 \iota:S\longrightarrow D(S),\qquad
 \iota(\lambda)=\lambda-e_1,
\tag{I.12}
\]

is injective: equality of its outputs immediately implies equality of the parents.  Define
`D_S,E_S:C^S -> C^{D(S)}` by

\[
 (D_S)_{\beta,\lambda}
 =\mathbf1[\beta=\lambda-e_1]\sqrt{p_1(\lambda)},
 \qquad E_S=A_S-D_S.
\tag{I.13}
\]

Both matrices have dimensions `|D(S)| x s`.  The columns of `D_S` have disjoint row support, so

\[
 \sigma_{\min}(D_S)=\min_{\lambda\in S}\sqrt{p_1(\lambda)}
 \ge\sqrt{1-2/m}.
\tag{I.14}
\]

The off-pivot Frobenius calculation is exact:

\[
 \|E_S\|_F^2
 =\sum_{\lambda\in S}\bigl(1-p_1(\lambda)\bigr)
 \le {2s\over m}.
\tag{I.15}
\]

Here the Frobenius-to-operator step has the safe direction
`||E_S||_op <= ||E_S||_F`; it supplies no reverse inequality.  Weyl's elementary perturbation
bound therefore yields

\[
 \boxed{
 \sigma_{\min}(A_S)
 \ge \sqrt{1-2/m}-\sqrt{2s/m}.
 }
\tag{I.16}
\]

Equation (I.16) proves that the scalar matrix `A_S` has no kernel whenever
`s<(m-2)/2`.  In particular, for `R=Theta(m^(1/3))`, it tends to one uniformly for
`s=O(R)` and for `s=O(R^2)`.  For `s=c m` it still gives a positive asymptotic bound when
`c<1/2`; it becomes vacuous at and above the threshold `s about m/2`.  Thus saying merely
`s=Omega(m)` is too coarse: some such supports are still excluded, while the bound does not
decide macroscopic supports beyond its threshold.

There is also a triangular description: order columns by nonincreasing first part and align row
`lambda-e_1` with column `lambda`.  Every other parent of that pivot row has first part
`lambda_1-1`, so the selected square submatrix is triangular with diagonal
`sqrt(p_1(lambda))`.  This proves nonsingularity but, without (I.15), triangularity alone gives no
uniform lower singular-value bound.

### 1.5 What the scalar obstruction does and does not type-check against
the physical query

The map (I.11) is a scalar map between coefficient spaces indexed by Young shapes.  A full-group
Fourier adversary block instead has the type

\[
 I_{S^\rho}\otimes B_\rho:
 S^\rho\otimes M_0(\rho)\longrightarrow
 S^\rho\otimes M_1(\rho),
\tag{I.17}
\]

where `rho=(lambda,mu,nu)` and `B_rho:M_0(rho)->M_1(rho)`.  After restriction to a left
coordinate stabilizer, common predecessors occur as multiplicity copies, and a physical query is
the Schur map `T -> T-Phi_L(T)`, not the scalar map (I.11).  Therefore (I.16) proves a
Plancherel-weighted Young-incidence obstruction only.  It can become a physical query obstruction
only after an additional, typed identity identifies the relevant YES/NO recoupling and
off-equality block with `A_S` (or bounds it from below by `A_S`).  Dimension ratios alone do not
supply that identity.

Explicitly, for `G=S_n^(L) x S_n^(R) x S_q`, put
`F_rho=f^lambda f^mu f^nu` and `c_t(rho)=dim M_t(rho)`.  Then (I.17) is a rectangular matrix of
size `F_rho c_1(rho) x F_rho c_0(rho)`.  For a left stabilizer type
`tau=(beta,mu,nu)`, its representation carrier has dimension `f^beta f^mu f^nu`, while its exact
parent multiplicity space has dimension
`sum_(lambda:beta nearrow lambda)c_t(lambda,mu,nu)`.  Neither dimension appears in (I.11).
Finally, the full physical pinching map is an endomorphism of
`Hom(C^(X_0),C^(X_1))`, whose matrices have size `|X_1| x |X_0|`.  These types make precise why a
scalar `P_(n-1) x s` singular-value estimate cannot be substituted for a one-point orbital block.

The heavy-unselected equality estimate can be independently typed on the normalized
singleton-skeleton subspace.  For a NO skeleton `sigma_0` and a YES skeleton `sigma_1`, let their
available heavy raw-label complements be `R_0(sigma_0)` and `R_1(sigma_1)`.  On `p=0,u=1`, their
sizes are `2a` and `2a+1`.  The equality kernel is the scalar matrix

\[
 \varepsilon(\sigma_1,\sigma_0)
 ={ |R_1(\sigma_1)\cap R_0(\sigma_0)|\over(2a+1)(2a)}
 =\left\langle{\mathbf1_{R_1(\sigma_1)}\over2a+1},
                 {\mathbf1_{R_0(\sigma_0)}\over2a}\right\rangle.
\tag{I.18}
\]

It has matrix dimensions `|mathcal S_1^U| x |mathcal S_0^U|`.  The displayed inner product is in
`C^q`; its two vectors have norms `(2a+1)^(-1/2)` and `(2a)^(-1/2)`.  Hence its Schur multiplier

\[
 S_\varepsilon:
 \operatorname{Hom}(\mathbb C^{\mathcal S_0^U},
                     \mathbb C^{\mathcal S_1^U})
 \longrightarrow
 \operatorname{Hom}(\mathbb C^{\mathcal S_0^U},
                     \mathbb C^{\mathcal S_1^U}),
 \quad T\mapsto T\circ\varepsilon,
\tag{I.19}
\]

obeys

\[
 \|S_\varepsilon\|\le\delta_a:={1\over\sqrt{2a(2a+1)}},
 \qquad
 \|T\circ(1-\varepsilon)\|\ge(1-\delta_a)\|T\|.
\tag{I.20}
\]

The last inequality holds for every rectangular `T` of the type in (I.19).  Its applicability is
limited: `T` must already be a normalized heavy-unselected skeleton block on which completion
averaging gives (I.18).  It is not an estimate for selected-singleton blocks, arbitrary
multiplicity carriers, or the full physical query before compression.  In particular, (I.20)
does not provide the missing lower bound relating a general parent coefficient law to such a
heavy-unselected block.

The same comments apply independently on the right.  For a two-sided scalar table, (I.16) may be
applied to each left column support and each right row support, but this is still a statement about
the scalar down-incidence maps.  It neither preserves the outer `a^(2/3)` numerator nor controls
all physical one-point orbital blocks.

### 1.6 Pre-comparison assessment

Before opening the proposer artifact, the independently established conclusions are:

1. every nonempty finite level support has a predecessor of support degree at most two;
2. every fixed-core singleton/Pieri parent is first-row dominant as in (I.6);
3. the Plancherel-normalized down-incidence has the exact lower bound (I.16), excluding an exact
   scalar harmonic on every target-sized `O(R)` or `O(R^2)` support;
4. the bound does not decide supports at or beyond its `about m/2` threshold;
5. the equality Schur multiplier estimate (I.20) is correct only after a heavy-unselected
   skeleton compression has independently been obtained;
6. no physical off-equality adversary-norm obstruction follows from (I.16) without a new
   recoupling/operator identity.

## 2. Comparison with the proposer artifact

After completing Section 1, I read
`ksum/artifacts/ksum_L3_critical_shared_branch_young_lattice_patch_audit_20260722.md`, SHA-256
`FD7574B915FB5161D46025427167231FC6ED64123E5544875114227D57736CC7`.

The proposer and independent arguments agree on the substantive statements:

* the lexicographic last-row deletion gives lower-shadow degree at most two;
* Pieri interlacing gives `lambda_1>=n-a` and `lambda_2<=a`;
* first-row deletion is an injective triangular pivot throughout the cone;
* its exact normalized weight is at least `1-2/m`;
* a support of size `s` has the singular-value lower bound (1.1)/(I.16);
* `O(R)` and `O(R^2)` supports are excluded from scalar Young-down suppression, while the
  estimate becomes nondecisive only on a macroscopic scale near `m/2`;
* the heavy-unselected equality multiplier is `O(1/a)` only after the relevant skeleton block
  has already been formed;
* the scalar/Frobenius Young calculation is not the complete physical-query operator bound.

The independent hook-coordinate derivation (I.8)--(I.10) and the proposer's first-row hook-product
derivation (6.2)--(6.3) are different derivations of the same formula.  This is useful
corroboration rather than notational reproduction.

I found one repeated local type defect and one notation ambiguity:

1. In proposer displays (5.6), (7.2), and (7.3), `B` is introduced as an
   `|S_L| x |S_R|` matrix, while `mathscr D_n` is the full `p(n-1) x p(n)` down matrix.  The
   products are not defined as printed.  The intended and valid formulas use

   \[
    A_L=\mathscr D_n[:,S_L]:\mathbb C^{S_L}\to\mathbb C^{\mathcal Y_{n-1}},
    \qquad
    A_R=\mathscr D_n[:,S_R]:\mathbb C^{S_R}\to\mathbb C^{\mathcal Y_{n-1}},
   \tag{R.1}
   \]

   and then `A_L B` and `B A_R^*`.  Equivalently, the proposer could explicitly zero-pad `B` to
   a `p(n) x p(n)` matrix.  This is a local repair; the columnwise/rowwise Frobenius proof remains
   valid and all quantitative constants are unchanged.
2. In (6.7), the unsubscripted `||E_S||` must mean operator norm.  With that reading,
   `||E_S||_op<=||E_S||_F` has the correct direction.  The artifact never uses the invalid
   reverse direction.

No major mathematical error was found in the scoped Young-incidence result.  Crucially, the
proposer does **not** infer a physical adversary operator bound from the Frobenius inequalities;
Section 8 explicitly records the missing recoupling/operator-max step.

## 3. Rule-7(a) per-display type and dimension audit

Write `P_j=p(j)=|mathcal Y_j|`, `s=|S|`, `s_L=|S_L|`, and `s_R=|S_R|`.  Scalar and set displays
are included so that no displayed formula is silently skipped.

| Proposer display | Domain/codomain or scalar type | Dimensions and verdict |
|---|---|---|
| (1.1) | scalar lower bound for `sigma_min(mathscr D_n[:,S])` | `mathscr D_n[:,S]:C^s->C^(P_(n-1))`; correct |
| (2.1) | `D_n:C^(Y_n)->C^(Y_(n-1))` | `P_(n-1) x P_n`; each basis image is typed; correct |
| (2.2) | `mathscr D_n:C^(Y_n)->C^(Y_(n-1))` | `P_(n-1) x P_n`; positive scalar entry weights; correct |
| (2.3) | scalar dimension identity for one `lambda vdash n` | `f^lambda` and every `f^beta` are positive integers; correct |
| (2.4) | matrix identity `mathscr D_n=L D_n R` | `L:P_(n-1)xP_(n-1)`, `D_n:P_(n-1)xP_n`, `R:P_nxP_n`; correct |
| (3.1) | integer cardinality `d_S(beta)` | `S subseteq Y_n`, `beta in Y_(n-1)`; finite; correct |
| (3.2) | scalar integer inequality | boundary `beta` has degree one or two; correct |
| (3.3) | tuple membership | `lambda in Y_n`, padded length `ell`; correct |
| (3.4) | partition construction | output `beta in Y_(n-1)`; final zero omitted; correct |
| (4.1) | integer parameter identities | `a=k^2,d=k,m=d+1,n=am,q=4a`; correct and gives `p=0,u=1` |
| (4.2) | partition declaration | `theta in Y_a`; correct |
| (4.3) | scalar LR coefficient | sizes `a+(n-a)=n`; by one-row Pieri it is zero or one; correct |
| (4.4) | scalar interlacing inequalities | partitions padded by zeros; correct equivalence to horizontal strip |
| (4.5) | scalar tail/row inequalities | all quantities integers; summation proof is correct |
| (4.6) | scalar gap inequality | `n-2a=a(m-2)>0` requires `m>2`; correct |
| (4.7) | set definition | subset of `Y_n`; correct; it contains every fixed-core cone |
| (5.1) | map `beta:S->Y_(n-1)` | legal because `lambda_1>lambda_2`; injective; correct |
| (5.2) | row-index set | `R_S subseteq Y_(n-1)`, cardinality `s`; correct |
| (5.3) | alternative parent construction | `gamma in Y_n` only for an addable row `j>=2`; then `gamma_1=lambda_1-1`; correct |
| (5.4) | rank/kernel of `D_n[:,S]:C^s->C^(P_(n-1))` | matrix `P_(n-1) x s`; triangular `s x s` minor proves rank `s`; correct |
| (5.5) | proposition, not an operator identity | exact scalar Young-down kernel on the declared cone is zero; correct |
| (5.6) | intended left/right down action on a table | **ill-typed as printed** for `B in C^(s_L x s_R)`; repair to `A_LB=0` and `BA_R^*=0`, or explicitly zero-pad `B` |
| (6.1) | scalar ratio | positive scalar `f^beta/f^lambda`; correct |
| (6.2) | scalar hook-product identity | `lambda_1-1` positive hook ratios; exact and equivalent to (I.8); correct |
| (6.3) | scalar lower bounds | correct inequality direction; no normalization missing |
| (6.4) | scalar branching sum | sum over all non-first removable predecessors; equals `1-p_lambda`; correct |
| (6.5) | `T_S=P_S+E_S:C^s->C^s` | each matrix `s x s`; `T_S` is the pivot-row compression; correct |
| (6.6) | diagonal scalar entries of `P_S` | `s` entries; square-root lower bound is correct |
| (6.7) | matrix norm inequality on `E_S:C^s->C^s` | correct if first norm is `||.||_op`; Frobenius bound uses only a subset of non-first mass and is safe |
| (6.8) | vector norm inequality | `c in C^s`; full output in `C^(P_(n-1))`, pivot output in `C^s`; row compression gives first inequality; correct |
| (6.9) | scalar target inequality for vectors | both sides Euclidean norms on `C^(P_(n-1))` and `C^s`; correct |
| (6.10) | scalar necessary support-size inequality | algebraically follows from (6.8) when the bracket is positive; correct for large `m` and fixed implied constant |
| (7.1) | `B:C^(S_R)->C^(S_L)` | matrix `s_L x s_R`; correct |
| (7.2) | intended `A_LB:C^(S_R)->C^(Y_(n-1))` | **ill-typed as printed**; after (R.1), dimensions `P_(n-1) x s_R` and Frobenius inequality is correct |
| (7.3) | intended `BA_R^*:C^(Y_(n-1))->C^(S_L)` | **ill-typed as printed**; after (R.1), dimensions `s_L x P_(n-1)` and Frobenius inequality is correct |
| (8.1) | partition construction | `beta(lambda) in Y_(n-1)` and `beta/theta` has size `n-a-1`; correct because deleted first-row box lies outside `theta` |
| (8.2) | scalar Schur-multiplier bound | complement sizes `2a` and `2a+1`; correct normalized factor |
| (8.3) | compressed Schur-map inequality | typed for `A_U:C^(S_0^U)->C^(S_1^U)` and compressed mask `1-epsilon` of same matrix dimensions; correct under this explicit interpretation, not for an arbitrary full block |

No multiplicity dimension is suppressed in this table: the Young-down operators act only on
shape coefficient spaces.  A genuine Fourier block has the separate type (I.17), with arbitrary
`dim M_t(rho)`.  The proposer correctly leaves those multiplicity and recoupling dimensions
outside its conclusion.

## 4. Rule-7(b) regime-complete gates

| Regime | Independent outcome | Coverage verdict |
|---|---|---|
| exact `p=0,u=1` subsequence | all parameter, Pieri, hook, and equality-complement formulas rederived | covered |
| `m<=2` | first-row gap need not be positive | explicitly outside stable range; harmless for asymptotics |
| `s=O(R)`, `R=Theta(m^(1/3))` | (I.16) is `1-O(m^(-1/3))` | covered; no scalar suppression |
| `s=O(R^2)` | (I.16) is `1-O(m^(-1/6))` | covered; no scalar suppression |
| exact harmonic with `s<(m-2)/2` | impossible by (I.16), and in fact impossible at every size in the cone by triangularity | covered |
| target `O(R^(-1/2))` scalar suppression | necessary threshold is (6.10), asymptotic to `m/2` | covered as a necessary condition only |
| `s=c m`, fixed `c<1/2` | still excluded for large `m` | covered; the bare phrase `Omega(m)` must not be read as automatic noncoverage |
| `s` at/above the threshold near `m/2` | lower bound becomes vacuous; exact injectivity alone gives no condition number | not decided |
| left and right scalar parent sets | repaired (7.2)--(7.3) apply independently | covered in Frobenius norm only |
| full physical off-equality query | only conditional retention of an already-formed `U/U` skeleton block is proved | not decided |
| `p>0` or `u>1` | not analyzed by this artifact | not covered |
| same-parent multiplicity, non-skeleton heavy carrier, pair-dependent orbital law | not represented by `mathscr D_n` | not covered |
| outer `a^(2/3)` numerator and normalized address incidence | no composition is provided | not covered |

No numerical identity gate is needed: every covered regime follows from exact symbolic identities.
In particular, no finite spectrum is used to infer an exponent.

## 5. Rule-7(c,d) anchoring and frozen-input audit

The independent reconstruction in Section 1 was fixed on disk before the proposer derivation was
opened.  Its notation (`mathcal Y_n`, `A_S=D_S+E_S`, hook coordinates `h_i`) was chosen
independently.  The subsequent agreement with the proposer's differently presented hook-row
product is therefore not anchored reproduction.

No prior completion verdict was imported.  I reopened the following uses:

* The exact `p=0,u=1` sizes and singleton/heavy types were checked against the full orbit
  classification.  Only the complement cardinalities `2a` and `2a+1` are used here.
* The heavy equality factor was rederived from the Gram factorization (I.18), rather than frozen
  from the parent-grid conclusion.
* The nonvacuity assertion for a fixed `theta` was reopened algebraically: Pieri gives every
  `lambda/theta`; a fixed removable `theta^-` and associativity give the YES position path; the
  common alphabet path follows by taking the Cartan component `2theta`, adding `2a` first-row
  boxes on NO, and on YES adding one of the two missing corner boxes before a horizontal strip of
  size `2a+1`.  This is ancillary to the Young no-go and does not assert total multiplicity one.

The review does not import the older full-orbit classification as a full-central-sum theorem, nor
does it extend its `p=0,u=1` scope.  Any use of the current scalar result for arbitrary
multiplicity spaces or one-point orbital matrices remains reopened and unproved.

## 6. Rule-7(e,f,g) standing failure modes and quantifiers

### Normalization

The diagonal similarity (2.4), branching normalization (2.3), first-row weight (6.2), and Schur
factor (8.2) have the correct factors.  The Frobenius-to-operator comparison in (6.7) has the safe
direction.  No address-incidence normalization is used; the outer composition is explicitly
unproved.

### Type and dimension mismatches

Displays (5.6), (7.2), and (7.3) require the local restriction/zero-padding repair (R.1).
Display (8.3) must be read on the compressed skeleton spaces, not on the full answer modules.
No conjugator, subgroup normalizer, or LR multiplicity frame is asserted in the reviewed
identities.

### Undefined terms and stability ranges

For a precise reading:

* all asymptotics are as integer `k->infinity` along (4.1), hence `m=k+1`;
* `R=Theta(m^(1/3))` has constants independent of `k,a,q`;
* `s` is the number of distinct position partitions in one declared support;
* `O(R^(-1/2))` means a fixed, parameter-independent constant times that quantity;
* the first-row cone and hook bounds require `m>2`;
* “heavy-unselected block” means the normalized singleton-skeleton compression for which the
  queried coordinate is outside the `a` singleton positions and completion averaging produces
  (I.18);
* “norm-active predecessor” is not resolved by support incidence alone.  The boundary lemma
  produces a combinatorially incident predecessor, but its physical off-equality norm requires
  the extra recoupling/status analysis that remains open.

With these definitions the scalar claims are quantified.  Without the last qualification, the
top-level word “norm-active” would be an overstatement.

### Colored orbit versus full central sum

The artifact works on selected Pieri shape coefficient spaces and makes no claim that a colored
orbital sum is a full central sum.  Its exact-module paragraph is a nonzero selected-line
statement, not a claim about the complete multiplicity space.  The complete physical orbital
system is expressly outside scope.

### Value versus formula

This is a formula-level review.  No numerical program or independently constructed finite matrix
is used.  Therefore there is no value/formula decoupling issue and no numerical evidence for an
exponent.  The proposer SHA above binds the exact formulas reviewed.

### Commissioned hostile checks

1. **Lexicographic boundary:** PASS.  Last-row deletion admits only the original parent and,
   when the last part exceeds one, the possible new-row parent; every earlier-row addition is
   lexicographically larger.  Hence the bound really is two, including repeated lower parts.
2. **Pieri interlacing:** PASS.  Summing `lambda_(i+1)<=theta_i` gives tail at most `a`, hence
   `lambda_1>=n-a`; separately `lambda_2<=theta_1<=a`.
3. **Pivot direction/triangularity:** PASS.  With columns in decreasing lexicographic order, an
   off-diagonal parent of row `lambda-e_1` has first part `lambda_1-1` and lies later.  Reversing
   the order merely changes upper to lower triangular; the diagonal remains nonzero.
4. **Hook-ratio direction:** PASS.  The first-row hook factors before the telescoping tail are at
   least one, so omitting them gives a lower, not upper, bound.  The independent `h_i` proof gives
   the same direction.
5. **Frobenius/operator passage:** PASS within the scalar matrix, with the required direction
   `||E||_op<=||E||_F`.  FAIL as a hypothetical passage from (7.2)--(7.3) to the adversary
   operator maximum; the proposer explicitly does not make that passage.
6. **Equality Schur multiplier:** PASS only for the normalized heavy-unselected skeleton block.
   Its factorization vectors have norms `(2a+1)^(-1/2)` and `(2a)^(-1/2)`, giving exactly
   `1/sqrt(2a(2a+1))`.  It does not apply to selected-singleton, nontrivial heavy-carrier, or
   uncompressed full physical blocks.

## 7. Scoped verdict

**SCOPED PASS WITH LOCAL TYPE CORRECTIONS.**  The universal degree-two boundary lemma, the
singleton/Pieri first-row cone, triangular injectivity, normalized hook lower bound, and
`s`-parent singular-value estimate are correct and independently reproduced.  The repeated
dimension mismatch in (5.6), (7.2), and (7.3) is repaired by (R.1) without changing any bound.

This review does **not** license `PROVED` or `REFUTED` for the canonical construction node.  It
certifies only the scoped negative result: a target-sized scalar Young-down patch inside the
singleton/Pieri cone cannot supply the desired harmonic cancellation.  The artifact neither
constructs the requested physical kernel nor rules out a patch whose combinatorial boundary is
physically inactive through nontrivial recoupling, an `Omega(m)` macroscopic support, same-parent
multiplicity, a non-skeleton carrier, or a genuinely pair-dependent orbital law.  The canonical
node should therefore remain `OPEN` (or record this audited subroute as closed) rather than receive
a completion-tier status.
