# Phase 27 fresh Rule-7 review: two-orientation shared-NO cascade (`q=5`)

Reviewer: fresh independent instance `/root/phase27_shared_no_rule7_review`  
Target node: `KSUM.B4b.L2.ALT.two-orientation-shared-no-cascade`  
Review opened: `2026-07-21T20:55:38-04:00`  

## Pre-anchor derivation (sealed before proposer materials were read)

### Reading boundary and independence declaration

Before this section was written, I read only:

1. `DAG_PROTOCOL.md` in full;
2. lines 1--41 and 70--76 of the target node (frontmatter, Claim, Role, Current status,
   Dependencies, and Open obligations); and
3. the Claim/Role/Current-status header of `KSUM.B4b.L2.yaml` only to identify the ambient target as a
   multisymmetric joint-histogram dual.

I did **not** read the target node's Work record, Evidence, Adversarial reviews, or Status history; I
did not read the Phase-27 proposer artifact; and I did not inspect any proposer checker or log. The
notation and construction below were fixed before those sources were unsealed. The very short node
claim does not specify endpoint coefficients, so this section derives the construction class and the
identities that any positive candidate must satisfy; it does not guess undocumented numerical
coefficients.

### Independent model and orbit-row algebra

Write the five colors as

\[
  \{0,a,\bar a,b,\bar b\},
\]

where `0` is the self-complementary color and the other four colors form two unordered complementary
pairs. Let

\[
  \mathcal H_N=\{h\in\mathbb Z_{\ge0}^{5}:\sum_c h_c=N\}.
\]

The predicate-preserving color group is the wreath action
`G=(C_2)^2\rtimes S_2` on the two complementary pairs, fixing `0`. The ambient position symmetry has
already been quotiented by passing to histograms. For an exponent vector
`alpha in Z_{>=0}^5`, with `|alpha|=t`, define the full central orbit row

\[
 R_\alpha(h)=\sum_{g\in G}\prod_{c}(h_{g c})_{\alpha_c},
 \qquad (u)_r=u(u-1)\cdots(u-r+1).
 \tag{PA.1}
\]

An orbit-normalized average differs from (PA.1) only by a fixed positive row factor and hence has the
same kernel. Here `R_alpha : H_N -> Z` is a scalar-valued function; the associated evaluation map on
a signed measure `psi in R^{H_N}` is `psi |-> sum_h psi(h)R_alpha(h) in R`. Every factor is defined
for nonnegative integral occupancies. Rows with `alpha_0>0` vanish on the slice used below.

The raw `rho<=2` description is naturally exhaustive at `q=5`: after removing the fixed zero color,
there are exactly two complementary-pair blocks, so a colored raw monomial can involve `rho=0,1,2`
active pair blocks and no third block. Passing from colored rows to the full central rows means taking
the complete `G`-orbit sum (PA.1), not selecting one colored representative. This exhaustiveness must
be checked against the proposer's precise definition of `rho`; it is a pre-registered hostile gate,
not an assumed frozen input.

For integers `1<=x<=N-1`, use canonical representatives

\[
 H_x=(0;x,0;N-x,0),\quad
 Y_x=(0;x-1,1;N-x,0),\quad
 \widetilde Y_x=(0;x,0;N-x-1,1).
 \tag{PA.2}
\]

They lie in `H_N`. `H_x` is NO when both occupied colors are selected from different complementary
pairs; `Y_x` is YES exactly when `x>=2`; and `tilde Y_x` is YES exactly when `N-x>=2`. The group swaps
the two pairs, hence

\[
 [H_x]=[H_{N-x}],\qquad [\widetilde Y_x]=[Y_{N-x}].
 \tag{PA.3}
\]

Thus the two oriented jumps `Y_x-H_x` and `Y_{N-x}-H_{N-x}` have exactly the same unordered NO orbit.
For odd `N=2M+1`, the reflection has no fixed integer `x`; in the shifted collision variable

\[
 z=x-1,\qquad z^*=(N-x)-1=N-2-z=2M-1-z.
 \tag{PA.4}
\]

This is the off-by-one-sensitive form: reflection is about `(N-2)/2=M-1/2`, not about `M`.

Put `Delta_alpha(x)=R_alpha(Y_x)-R_alpha(H_x)`. Since `Y_1` and `H_1` are in the same NO orbit,
`Delta_alpha(1)=0`. Expanding falling factorials shows that for `|alpha|=t`, `Delta_alpha(x)` is a
polynomial of degree at most `t-1`: a term that changes must use the newly opened cell, whose
occupancy is one and whose positive exponent consumes one unit of query degree. Therefore

\[
 \Delta_\alpha(x)=z\,p_\alpha(z),\qquad \deg p_\alpha\le t-2.
 \tag{PA.5}
\]

For all query degrees `t<D`, this gives `deg p_alpha<=D-3`. Conversely, choosing a raw row that hits
the singleton once and its mate `j+1` times gives a nonzero triangular falling-factorial basis in
degrees `j=0,...,D-3`. Subject to the promised raw/full-row audit, the restricted difference-row
span is therefore exactly

\[
 \{z p(z):p\in\mathbb R[z],\ \deg p\le D-3\}.
 \tag{PA.6}
\]

This establishes the important offset: annihilating moments through degree `D-2` in the unshifted
`Delta` polynomial (equivalently degree `D-3` after division by `z`) kills query degree strictly less
than `D`; it does not by itself kill degree `D`.

### Independent barycentric kernel and shared-NO bookkeeping

Choose `m=D-1` distinct nonzero integer nodes `z_1,...,z_m` in the legal range
`1<=z_j<=N-3`, put `x_j=z_j+1`, and define

\[
 P(u)=\prod_{k=1}^{m}(u-z_k),\qquad
 \lambda_j={1\over P'(z_j)},\qquad w_j={\lambda_j\over z_j}.
 \tag{PA.7}
\]

The support conditions make every denominator nonzero. The standard partial-fraction identity is

\[
 \sum_{j=1}^{m}\lambda_j p(z_j)=0
 \quad(\deg p\le m-2=D-3),
 \qquad
 \sum_j {\lambda_j\over z_j}=-{1\over P(0)}\ne0.
 \tag{PA.8}

Consequently the signed orbit measure

\[
 T=\sum_j w_j\bigl(\delta_{[Y_{x_j}]}-\delta_{[H_{x_j}]}\bigr)
 \tag{PA.9}

annihilates every row of query degree `<D` by (PA.5)--(PA.8), but has nonzero YES-vs-NO
correlation. Its type is `T in R^Omega`, where `Omega=H_N/G`; `delta_[h]` is the standard basis vector
of that finite-dimensional space, and each row is a functional in `(R^Omega)^*`.

If both a node `z` and its reflected node `z*=N-2-z` occur, their NO basis vector is the same. Thus,
after collecting unordered orbits, the exact formulas are

\[
 \|T\|_1=\sum_{\text{YES orbits }y}|T(y)|+
             \sum_{\text{NO orbits }h}|T(h)|,
 \quad
 T([H_x])=-(w(x)+w(z^*)),
 \quad
 \langle T,f\rangle=2\sum_jw_j,
 \tag{PA.10}

where `f=+1` on YES and `f=-1` on NO. Formula (PA.10), rather than an oriented-edge norm, is where
shared-NO cancellation can change both the normalized correlation and the tail fraction.

The claim mentions a quadratic boundary bridge. Independently, the safe abstract form is a second
row-kernel `B in R^Omega`, supported on legal boundary orbits, satisfying the same identities
`<B,R_alpha>=0` for `|alpha|<D`, and then `Psi=B+cT`. If `supp(B)` and `supp(T)` are disjoint as orbit
sets, then and only then

\[
 \|B+cT\|_1=\|B\|_1+|c|\|T\|_1.
 \tag{PA.11}

If only their oriented presentations are disjoint but they share an unordered NO orbit, (PA.11) can
fail. The adjective "quadratic" is not a definition; the proposer must print its coefficients,
support, admissible range, and the polynomial identity it uses.

For `Y_x`, the number of complementary cross-pairs in the opened pair is `x-1=z`; hence the natural
tail gate `C_t>=N/4` is exactly `z>=N/4` on this slice. A claimed constant tail fraction must be
computed after orbit collection and `l1` normalization.

### Quantifiers and pre-registered regime-complete gates

The all-large-odd statement must have the form: there is an explicit absolute `N_0` such that for
every odd `N>=N_0`, with

\[
 D=\lfloor\sqrt{N/512}\rfloor+2,
 \tag{PA.12}
\]

all printed support nodes are distinct, nonzero, integral, and legal; all YES nodes really have both
members of a complementary pair occupied; the bridge/tail support claim holds after quotienting by
`G`; every degree-`<D` full central row is annihilated; `||Psi||_1=1`; the stated correlation exceeds
`2/3`; and the stated constant `l1` mass lies on `C_t>=N/4`. Equation (PA.12) gives
`D-2=floor(sqrt(N/512))`, so `D=Theta(sqrt N)` with leading constant `1/sqrt(512)` and additive two.

Before seeing proposer choices, I pre-register identity/matrix-residual gates for these qualitatively
different regimes:

* the smallest odd `N` allowed by every printed inequality, including the first values at which `D`
  changes (`D=3,4,5,...`);
* odd `N` immediately below and above each floor/split/reflection crossover;
* a middle feasible case with `D=7` but **not only** `N=20003`;
* at least two larger `D` values;
* raw rows at `rho=0,1,2`, including rows whose colored support uses one pair, both pairs, and the zero
  color, plus their complete central orbit sums;
* query degrees `0,1,2,D-2,D-1` (where feasible), checking exact rational row residuals, not merely
  objective values;
* every bridge piece alone, the tail kernel alone, and their sum, with separately generated orbit
  tables and direct orbit collection;
* reflection endpoints and neighbors to expose `M`/half-integer and `z` off-by-one errors;
* exact support-intersection, legality, correlation-factor-two, `l1`, and `C_t=N/4` boundary tests.

If any claimed all-large regime cannot be tested, the verdict must name it and cannot license PROVED.
The finite point `N=20003,D=7` is useful but cannot alone represent the floor transitions, minimal
legality range, large-`D` scaling, or all odd `N`.

### Standing failure-mode checklist fixed before unsealing

The post-anchor audit will separately check: dropped/extra orbit and normalization factors;
domain/codomain or dimension mismatches; undefined `admissible`, `strict`, `active range`, `taper`, or
similar terms and missing stability ranges; colored raw sums substituted for full central orbit sums;
and code that validates independently constructed values while the printed formula is malformed.
No earlier result is frozen for a new operator-level, `q=5`, all-large-odd-`N` use unless its cited
review demonstrably covered that exact scope under Rule 7(a)--(c).

## Post-anchor comparison and verdict

The pre-anchor section was sealed on disk before I opened the proposer artifact, target Work
record/Evidence, proposer checker, or proposer JSON. I then read those sources and re-opened the
load-bearing Phase-25 row reduction because it had no cited Rule-7(a)--(c) review for the present
operator-level, all-large-odd-`N`, full-`q=5` use.

### Comparison with the independently derived construction

The constructions agree structurally but **not notationally**. My pre-anchor `x` was the occupied
count in `H_x`, and my `z=x-1` was the opened-pair collision count; the proposer instead uses
`x=s-1`, `M=N-2`, `d=2x-M`, and `z=d^2`. My `M=(N-1)/2` was an integer midpoint parameter. Thus the
shared letters `x`, `M`, and `z` are a natural but potentially dangerous coincidence, not copied
notation. Translating to one system gives

\[
 x_{\rm prop}=s-1=C_t(H_+^{(s)}),\quad
 x_{\rm prop}'=N-s-1=(N-2)-x_{\rm prop},\quad
 d=2s-N,\quad z=d^2.
\]

This translation confirms the proposer's off-by-one formulas (27.7), (27.8), and (27.12).

My pre-anchor barycentric kernel was the unreduced one-orientation kernel. The proposer takes the
antisymmetric combination of the two reflected orientations first; odd falling-factorial
differences become `d Q(d^2)`, halving the moment rank. That is a genuine refinement of, and is
compatible with, the independently derived orbit-row algebra.

### Independent reconstruction of the full row span

Let `A_D={alpha in Z_{>=0}^5: |alpha|<D}`. A full central row is the complete eight-term
`G=(C_2)^2\rtimes S_2` sum in (PA.1). On every Phase-27 atom `h_0=0`, so rows with `alpha_0>0`
vanish identically. For `alpha_0=0`, restriction of `alpha` to the four nonzero colors consists of
zero, one, or two active complementary-pair patterns. Symmetrizing within each pair and then
between the two pairs gives exactly:

* the constant row (`rho=0`);
* one unordered pair pattern (`rho=1`); or
* an unordered pair of unordered pair patterns (`rho=2`).

These are exactly the three cases generated by the proposer's imported `row_patterns`. Stabilizers
can multiply a row by a positive row-dependent constant, but do not change its kernel. There is no
possible `rho=3` at `q=5,K=2`, because there are only two complementary-pair blocks. Thus raw
`rho<=2` exhausts the restriction of the **full** central `q=5` orbit-row span; zero-color rows are
the additional trivial-zero branch. The proposer checker does not explicitly enumerate that
zero-color branch, but its omission is harmless on this support. My checker enumerates it.

Independently of Phase 25, a changed-pair factorial kernel

\[
 A_{a,b}(1,s-1)-A_{a,b}(0,s)
\]

is a polynomial in `s` of degree at most `a+b-1` and vanishes at `s=1`, since the two pair
histograms are then related by the within-pair swap. It is therefore `(s-1)` times a polynomial of
degree at most `a+b-2`. Multiplication by the untouched-pair kernel raises degree by exactly its
query order. Hence every full row of total falling-factorial/query degree `<D` restricts to

\[
 (s-1)R(s-2),\qquad \deg R\le D-3.
\]

Conversely, the rows with one singleton hit and increasing hits on its mate give a triangular
falling-factorial basis through degree `D-3`. Therefore the annihilation map is exactly

\[
 (V_{N,D}\lambda)_k=\sum_s\lambda_s(s-1)_k=0,
 \qquad k=1,\ldots,m=D-2.
\]

This proves, rather than freezes, the load-bearing equivalence (27.9).

For antisymmetric reflected weights, this becomes

\[
 \sum_j b_j\{(x_j)_k-(M-x_j)_k\}=0.
\]

The brace is an antisymmetric degree-`k` polynomial under `d=2x-M -> -d`, so it is uniquely
`d Q_k(d^2)` with `deg Q_k<=floor((k-1)/2)`. With `r=ceil(m/2)`, all `k=1,...,m` are covered by
`deg Q<=r-1`. The `r+1` distinct nodes and `b_j=1/(d_j product_{ell!=j}(z_j-z_ell))` therefore
annihilate the complete system. This verifies the printed reflection/barycentric derivation, not
merely a numerically equal independently constructed value.

### Rule 7(a): per-display type and dimension audit

Use these typed spaces throughout:

* `H_N={h in Z_{>=0}^5: sum h=N}` and `Omega_N=H_N/G`; set `L(N)=|Omega_N|`.
* `E_N=R^{Omega_N}` has dimension `L(N)`; signed orbit measures, `J_s`, `K_raw`, `B`, `K`, and `W`
  all lie in `E_N`. A basis vector `delta_[h]` is well defined only after orbit canonicalization.
* `A_D={alpha in Z_{>=0}^5:|alpha|<D}` has size `binom(D+4,5)`. The unsimplified full row operator
  `F_<D:E_N -> R^{A_D}` is a `binom(D+4,5) by L(N)` matrix. Quotienting duplicate exponent orbits
  only deletes proportional rows.
* For a chosen orientation support `S subset {2,...,N-2}`, the synthesis map
  `J_S:R^S -> E_N`, `lambda |-> sum_s lambda_s J_s`, has dimensions `L(N) by |S|`.
* `V_{N,D}:R^S -> R^m`, `m=D-2`, is the `m by |S|` falling-factorial moment map above.
* For the tail support, `r=ceil(m/2)`, the evaluation map
  `Z:R^{r+1}->R^r`, `nu |-> (sum_j nu_j z_j^ell)_{ell=0}^{r-1}`, is `r by (r+1)`.
  For the bridge, the analogous map is `m by (m+1)`.
* `1,f in E_N^*`, where `1` is total mass and `f([h])=+1` on YES and `-1` on NO. The `l1` norm,
  tail seminorm, and correlation numerator are scalar maps `E_N->R_{>=0}`, `E_N->R_{>=0}`,
  and `E_N->R`, respectively.

Every numbered proposer display was checked as follows.

| display | domain/codomain and well-definedness | result |
|:--|:--|:--|
| (27.1) | Five scalar assertions about one `W in E_N`; `F_<D W` is in `R^{A_D}`. “Annihilation degree” resolves to falling-factorial row degree `<D`. | PASS after normalization. |
| (27.2) | For `2<=s<=N-2`, both histograms are in `H_N`; `J_s=delta_[H+]-delta_[H-] in E_N`. `C_t=s-1` on YES. | PASS. |
| (27.3) | Equality is in `Omega_N`, not literal equality of ordered four-tuples. Pair exchange sends one representative to the other. | PASS with this required typing. |
| (27.4) | `R^2 -> E_N`, `(a,b)` mapped to three orbit basis vectors. | PASS; the NO coordinates coincide. |
| (27.5) | Two scalar maps of (27.4). It assumes the two YES orbits are distinct; this holds on all used supports. | PASS. |
| (27.6) | An element of `E_N`; both coefficients and basis vectors are defined. | PASS. |
| (27.7)--(27.8) | Integer maps `s -> x=s-1`, `N -> M=N-2`, and involution `x -> M-x`; no fixed point for odd `N` because `M` is odd. | PASS; no off-by-one error. |
| (27.9) | The identity `V_{N,D}lambda=0 in R^m`, with `m=D-2`; each `(s-1)_k` is scalar. | PASS; independently re-derived. |
| (27.10)--(27.11) | Injection `R^{r+1}->R^S` followed by `V_{N,D}`; `F_k:Z->Z` and each sum is scalar. | PASS. |
| (27.12)--(27.13) | `x,M,d,z in Z`; `Q_k in Q[z]` and `d Q_k(z)` is scalar. Division by `d` is used only later, where `d_j!=0`. | PASS. |
| (27.14) | Integer rank parameter `r=ceil(m/2)`; polynomial target space has dimension `r`. | PASS for even and odd `m`. |
| (27.15)--(27.16) | Maps `{0,...,r}->Z` producing `x_j,d_j,z_j`. | PASS for every odd `N>=513`; nodes are legal, nonzero, and distinct. |
| (27.17)--(27.18) | `nu,b in Q^{r+1}` and `Z nu=0 in Q^r`. Denominators require nonzero `d_j` and distinct `z_j`. | PASS under the just-proved range. |
| (27.19) | `K_raw in E_N`; after orbit collection it has `2(r+1)` distinct YES coordinates. | PASS for odd `N>=513`. |
| (27.20) | Three scalar functionals on `K_raw`; positivity uses at least one nonzero barycentric weight. | PASS. |
| (27.21)--(27.22) | `m,D in Z` and a scalar inequality. With `m=floor(sqrt(N/512))`, `64m^2<=N/8`. | PASS. |
| (27.23)--(27.24) | `{0,...,m}->Z` bridge support and a vector `lambda in Q^{m+1}`. All factorial denominators and `1+64j^2` are positive. | PASS. |
| (27.25)--(27.26) | Scalar ratio with positive denominator. The alternating magnitudes decrease; `pi^2<10` gives the printed strict bound. | PASS. |
| (27.27) | Affine combination in `E_N`. | PASS. |
| (27.28) | Scalars plus `F_<D W=0 in R^{A_D}`. Additivity of `l1` uses disjoint **orbit** supports, not merely oriented supports. | PASS after direct orbit intersection testing and analytic `C_t` separation. |
| (27.29) | Scalar normalized correlation. The factor two is already included in `rho_B`; `K` has zero numerator. | PASS. |
| (27.30)--(27.31) | A finite parameter tuple and scalar checker outputs. | Formula values PASS, but the tuple is not on the claimed `D(N)` schedule; see D1 below. |

No map changes domain silently, and every displayed vector identity is well typed after interpreting
histogram equalities in the orbit quotient. This completes the required per-display audit rather
than relying on scalar outputs alone.

### Norm, correlation, tail, and all-large legality

For `N` odd and at least `513`, put `m=floor(sqrt(N/512))>=1` and `r=ceil(m/2)`. Then

\[
 2(\lfloor N/3\rfloor+r)<N-2,
\]

so all `d_j<0`; hence they are nonzero and the strictly increasing `x_j` give distinct `d_j^2`.
Also `x_j` and `N-2-x_j` lie in `[N/4,3N/4]`. For the bridge,

\[
 C_t=1+64j^2\le1+64m^2\le1+N/8<N/4.
\]

Thus every atom is legal, the two components are disjoint after the unordered orbit quotient, and
their `l1` norms add. `K` contains no NO coordinate after merging, has unit tail norm and zero label
numerator. The normalized bridge has

\[
 \rho_B>{6048\over6565},
\]

so `W=(3/4)B+(1/4)K` has unit norm, exact tail `1/4`, and correlation
`>4536/6565>2/3`. This supplies an explicit stability range; the proposer's phrase “inconsequential
bounded adjustment for very small N” is not used.

The cutoff is exactly

\[
 D=\lfloor\sqrt{N/512}\rfloor+2,
\]

and the moment map has `m=D-2` rows. Falling-factorial total order is the one-hot query-polynomial
degree, so `F_<D W=0` means annihilation of every query-polynomial row of degree `<D`, including
degree `D-1`; it does not include degree `D`. In the standard quantum polynomial conversion a
`T`-query acceptance polynomial has degree at most `2T`, so the resulting quantum query lower-bound
scale is `D/2=Theta(sqrt N)`. The artifact's `D` is a row/query-polynomial cutoff, not a literal
number of quantum queries.

### Rule 7(b): regime-complete independent identity gates

I wrote `ksum/tools/ksum_l2p27_shared_no_rule7_independent.py` without importing the author row generator
or arithmetic path. It enumerates every five-color exponent vector `alpha` with `|alpha|<D`, sums
the full eight-element color group directly, evaluates the **printed** bridge and tail coefficient
formulas with `Fraction`, independently canonicalizes orbit atoms, and then checks the printed
norm/correlation/tail formulas.

The exact gate matrix covered:

| regime | `(N,D)` gates | result |
|:--|:--|:--|
| pre-first transition / smallest certified range | `(511,2)`, `(513,3)` | all residuals zero; all scalar gates PASS |
| even/odd `m` and floor transitions | `(2047,3)`, `(2049,4)`, `(4607,4)`, `(4609,5)`, `(8191,5)`, `(8193,6)` | PASS |
| formula schedule at `D=7` | `(12801,7)` | PASS |
| proposer finite point and corrected schedule | `(20003,7)`, `(20003,8)` | both PASS; only `D=8` matches the printed schedule |
| larger even/odd rank | `(32769,10)`, `(51201,12)` | PASS |

At every gate, degree slices `0,...,D-1` and `rho=0,1,2` had exact residual zero. Zero-color rows,
one-pair colored rows, two-pair colored rows, and their full central orbit sums were all included.
Every gate also returned: legal histograms, nonzero `d`, distinct `z`, zero surviving shared NO
atoms, bridge/tail orbit-support disjointness, bridge below `N/4`, tail kernel at or above `N/4`,
total mass zero, `l1=1`, tail `1/4`, and correlation `>2/3`.

No qualitative regime in the fixed-`q=5`, odd-`N>=513`, exact-`D(N)` claim remains untested:
`m=0` was additionally exercised below the certified range, both parities of `m` and `r`, floor
crossovers, endpoint row degrees, all possible `rho`, and larger `D` were covered. The analytic
argument covers the infinite tail of odd `N`.

### Findings and failure-mode diversity

**D1 (MINOR, provenance/coverage):** the sole proposer self-check `(N,D)=(20003,7)` does not use the
artifact's displayed schedule. At `N=20003`,
`floor(sqrt(N/512))+2=8`. Therefore (27.30)--(27.31) is not representative of the claimed parameter
at that `N`. The independent `(20003,8)` gate passes, so this is not a counterexample to the formula.

**D2 (MINOR, quantifier wording):** “sufficiently large,” “inconsequential bounded adjustment,” and
“by inspection” did not print a stability threshold. The audit above resolves the claim without an
adjustment for every odd `N>=513`. A future proposer-facing revision should state that range.

**D3 (MINOR, checker-description precision):** the author checker uses a basis of nonzero-pair
patterns, not literal five-color exponent enumeration. That basis is complete after restriction to
`h_0=0`, and missing zero-color rows vanish identically. Thus the calculation is valid, but the
phrase “every raw `rho<=2` orbit row” should state this restriction and the orbit-normalization
convention.

Standing hostile checks found no mathematical failure:

* **normalizations:** full group sums can differ from the pair-kernel basis by fixed row factors;
  none affect zero residuals. The label factor two and both component normalizations are correct.
* **types/dimensions:** audited display by display above; no mismatch remains.
* **terms/ranges:** `C_t`, degree cutoff, reflection, and correlation are resolved here. No
  `admissible`, `strict`, `active range`, or `taper` term is used load-bearingly.
* **colored versus central sums:** independent full `G` enumeration confirms the complete central
  restriction, including the trivial zero-color branch.
* **values versus formula:** the author code evaluates its printed coefficient formulas through a
  pre-existing reduced row generator. The independent code also evaluates the printed coefficients,
  but against a separately constructed full-color orbit operator. This checks the printed formulas;
  agreement of values alone was not used to validate the prose derivation, which was separately
  reconstructed above.
* **support collisions:** bridge/tail disjointness is true after unordered orbit merging, so `l1`
  adds linearly. The tail threshold is exactly `C_t>=N/4`, not a rounded substitute.

No new escape direction was discovered, so none is named or tested.

### Rule 7(c)--(g) completion ledger

* **7(c), anchoring ban — SATISFIED.** The timestamped pre-anchor derivation was written before any
  proposer proof/checker/log was read. Notational coincidences and differences are disclosed above.
* **7(d), no frozen-input immunity — SATISFIED.** The Phase-25 equivalence was re-opened and proved
  for the full operator-level `q=5`, degree-`<D`, all-large-odd-`N` use. Nothing new was accepted on
  a prior value-only citation.
* **7(e), failure-mode diversity — SATISFIED.** All five standing modes and the commission's hostile
  support/reflection/correlation/threshold checks are reported explicitly.
* **7(f), value/formula decoupling — SATISFIED.** The exact scope of both code paths is stated; the
  prose derivation has an independent analytic check.
* **7(g), quantifier hygiene — SATISFIED.** The review fixes `q=5`, `K=2`, odd `N>=513`, exact
  `D(N)`, `m`, `r`, `h=64`, mixture constants, orbit degree, label, norm, and tail threshold. The
  polynomial/quantum-query factor of two is explicit.

Together with the type and regime sections, **all Rule 7(a)--(g) requirements are satisfied**.

### Command, logs, and SHA-256 provenance

Independent command:

```text
python ksum/tools/ksum_l2p27_shared_no_rule7_independent.py \
  --output ksum/artifacts/logs_ksum_L2p27_shared_no_rule7_review_20260721/independent.json
```

Exact output: `ksum/artifacts/logs_ksum_L2p27_shared_no_rule7_review_20260721/independent.json`.

```text
00C4D24A31FD45230C2E7C75F2C81210A1D94786E3EA635B32F075B1518C56A1
  ksum/tools/ksum_l2p27_shared_no_rule7_independent.py
8B28FDD1D2FC150D258253C34CA0D1915CC261114F9337AB7EF34199F669F8FC
  ksum/artifacts/logs_ksum_L2p27_shared_no_rule7_review_20260721/independent.json
```

The author's cited SHA-256 values also match the files read:

```text
7D40BB5D97BCC5C59220FFCC7B9E3F0B4A3FC4658B06D6D601472BF41048DDA5
  ksum/tools/ksum_l2p27_shared_no_check.py
48BBAC269099C8C0426C79612989349326CD130D429FABE82B357D98300E789E
  ksum/artifacts/logs_ksum_L2p27_shared_no_20260721/run.json
```

## Verdict

**MINOR.** The construction is mathematically valid for fixed `q=5`, `K=2`, every odd `N>=513`,
and `D=floor(sqrt(N/512))+2`: it annihilates the full central orbit-row span of query-polynomial
degree `<D`, has total mass zero and unit `l1`, correlation greater than `2/3`, and exactly `1/4`
absolute mass at `C_t>=N/4`. The minor findings are the off-schedule proposer gate and imprecise
stability/checker wording; independent formula-level gates close the mathematical coverage.

This completed review satisfies Rule 7(a)--(g) and **permits the main agent to promote the scoped
node claim to PROVED**, citing this report and its independent run provenance. It does not prove a
`q=N` endpoint, an endpoint-uniform construction, or a literal quantum-query cutoff of `D` rather
than the standard `D/2` conversion. I do not modify the DAG or node status in this review.
