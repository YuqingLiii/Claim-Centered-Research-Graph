# Independent hostile review — KSUM.B4b.L2 phase 4

Date: 2026-07-19  
Reviewer: fresh independent reviewer; authored none of the target work; no wanted verdict  
Network: not used  
Commits: none  
Scope: phase-4 absolute-value composition, conditional-correctness and value-budget obstructions,
finite formulas, preregistration, caps/G11, and DAG synchronization

## Pre-action report

Before opening the phase-4 derivation, I reloaded the research-structure protocol, the proof-DAG
protocol including newly binding rule 7, the node index, the complete `KSUM.B4b.L2` node and parent
`KSUM.B4b`, and the completed phase-2 and phase-3 reviews. I then derived the two proposed
consequences independently from the reviewed phase-3 kernel and recorded that derivation in
[ANCHORING_DERIVATION.txt](logs_ksum_L2p4r_20260719/ANCHORING_DERIVATION.txt). Only after that file
was written did I inspect the phase-4 report, proposer scripts, predictions, outputs, and manifest.

The worktree was already heavily dirty, including all phase-4 files and unrelated SE work. I
preserved those changes and made no commit. No network was used.

Fresh review evidence, importing neither proposer script nor proposer JSON:

- [exact review driver](../tools/ksum_l2p4r_exact_review.py);
- [exact rational/coefficient output](logs_ksum_L2p4r_20260719/exact_review.json);
- [commands](logs_ksum_L2p4r_20260719/COMMANDS.txt) and
  [SHA-256 manifest](logs_ksum_L2p4r_20260719/SHA256SUMS.txt).

## Ruling

**T1 is PROVED only for the fixed-allocation, unaveraged absolute-value sign-bit composition (and
for any later averaging known to preserve its `l1` norm). The report's broader use of T1 after
symmetry averaging and renormalization is not proved. T2 is PROVED for the precisely defined
whole-`sigma`-pair/value-disjoint allocation class. The preregistered BLOCKED outcome remains
accurate for that selected mechanism because T2 alone prevents the required `sqrt(N)` growth at
fixed `q`. The route leaf remains CONJECTURED; B4b, B4, and the root remain OPEN.**

The review finds one **MAJOR** scope/normalization defect and two **MINOR** presentation/provenance
defects. It does not license the unqualified statement that every symmetry-completed standard
composition has correlation at most `product_j rho_j`.

## Rule-7 execution log

### 7a — type audit of every phase-4 display: EXECUTED

Here is the common typed model used to audit every display. For odd `q`,
`sigma: Z_q -> Z_q`, `sigma(a)=t-a`, is an involution with fixed point `f=t/2` and
`r=(q-1)/2` nonfixed two-cycles. Block indices are `j in [m]`; complementary-pair indices are
`c in [r]`; string-position indices are `i in [N]`. A whole-pair allocation is a family of
pair-index sets `A_j subseteq [r]`, pairwise disjoint, with `r_j=|A_j|`. It induces a disjoint
coordinate embedding from block occupancy spaces

`Omega_j={n^(j) in N_0^(2r_j): sum n^(j)=N_j}`

into the global occupancy slice

`Omega_{N,q}={n in N_0^q: sum_a n_a=N, n_f=0}`,

where `N=sum_j N_j`. Thus pair coordinates, block coordinates, and string positions are different
index types. A uniform orbit lift maps a signed occupancy measure on `Omega_{N,q}` to a signed
measure on `[q]^N`; the reviewed falling-factorial map sends a query monomial of position degree
`a` to a constant multiple of an occupancy row indexed by `alpha in N_0^q`, `|alpha|=a`.

Every displayed formula was checked as follows:

| Display(s) | Domain/codomain and dimension audit | Result |
|---|---|---|
| `k_0=0,k_1=1,k_2=5,...,k_h=5^(h-1)` and signs `(-1)^(h-i)` | The nodes are distinct integers in `[0,r_j]`; the barycentric functional is a signed measure on these `h+1` activity layers. The sign formula follows from the `h` ordered denominator factors. | PASS. |
| `P=|mu|`, `S=sgn(mu)`, `P[S=±]=1/2` | `mu` is a real signed measure on a finite block domain `X_j`, with `||mu||_1=1` and total zero; `P` is a probability measure. Strictly, `S:X_j^*-> {±1}` is defined only on `X_j^*=supp(mu)`. | PASS after the support restriction; the report omits it (D11). |
| `rho=<mu,g>=Pr[g=NO|S=-1]` | `g:X_j^*->{±1}` uses YES=`+1`, NO=`-1`. The conditional is under `P=|mu|`, conditioned on the event `{S=-1}`, equivalently on the two-atom sigma-algebra `sigma(S)`. Since `P(S=-1)=1/2`, it is well defined. | PASS; the exact conditioning sigma-algebra is supplied here. |
| Weight ratios and `rho<=2/(1+5/4+1/4)=4/5` | Ratios are dimensionless rational numbers for phase-3 support size at least three (`r_j>=5`). The bound does not cover the endpoint support `{0,1}`, where `rho=1`. | PASS and tight at `{0,1,5}`. |
| `m r0 <= r=(q-1)/2` | `m` is a block count; `r0` is pairs per equal block; `r` is the number of global complementary pairs. More generally `sum_j r_j<=r`. These are pair-index counts, not position counts. | PASS within whole-pair allocation. |
| `zeta(x_1,...,x_m)=2^m Psi(S_1,...,S_m) product_j |mu_j(x_j)|` | `mu_j in R^{X_j}`, `P_j=|mu_j|`, `S_j:X_j^*->{±1}`, and `Psi in R^{{±1}^m}`. The formula defines `zeta in R^{product_j X_j^*}`. Via the disjoint value-coordinate embedding it becomes a global occupancy/string measure. | PASS after restricting to the product support; as printed, `sgn(0)` makes the map ill typed (D11). |
| `||zeta||_1=1` and `sum zeta=0` | Under `tensor_j P_j`, the sign vector is uniform on the `2^m` sign cells. Hence the norm is `sum_s |Psi(s)|=1` and the total is `sum_s Psi(s)=0`. | PASS for the unaveraged product measure. |
| Pure high degree `dD` | A block factorial row has local orders `a_j`; if `a_j<d`, its conditional expectation is constant on `S_j`. If `sum a_j<dD`, fewer than `D` block indices can be sign-dependent, giving a multilinear sign polynomial of degree `<D`, annihilated by `Psi`. | PASS. Block index and local occupancy degree are not confused. |
| `-2 Psi(-1,...,-1) product_j rho_j` | The product probability space is `tensor_j P_j`; conditioning is on the full sign sigma-algebra `sigma(S_1,...,S_m)`. Given all signs negative, the block events are conditionally independent and global NO has probability `product rho_j`; any positive sign makes OR deterministically YES. The result is a real scalar. | PASS for unaveraged `zeta`. |
| `<= product_j rho_j` | For `||Psi||_1=1` and total zero, each atom has absolute mass at most `1/2`; after choosing orientation, the absolute correlation is at most the product. | PASS before renormalized symmetry averaging; FAIL as an automatically inherited bound afterward (D10). |
| `(4/5)^2=16/25<2/3` | Scalar exact inequality; it applies when at least two blocks each have `r_j>=5`. Other blocks with `rho<=1` do not improve the product. | PASS in the fixed-allocation class. |
| Finite table: bands `2,4`, rows `6,56`, support `12,16` | At `(N,q,m)=(10,5,2)`, global occupancy dimension is `q=5`, with `n_0=0`; the row counts are `sum_{a<2} C(a+4,4)=6` and `sum_{a<4} C(a+4,4)=56`. The two active outer sign cells plus the all-negative cell give 12 patterns; parity gives all 16. | PASS by fresh reconstruction. |
| Conditional band `Omega(sqrt(m)(1+log((q-1)/(2m))))` | This is a lower-bound degree expression conditional on an outer degree `Omega(sqrt(m))`, with `1<=m<=(q-1)/2`; it is not an algorithmic upper bound and not an achieved witness. | PASS with that qualifier. |
| At `q=N`, `sqrt(m)(1+log(N/m))=sqrt(N)sqrt(y)(1+log(1/y))` | `y=m/N` is dimensionless and lies in `(0,1/2]` up to endpoint constants. The last factor is bounded, so the expression is `O(sqrt(N))`. | PASS as asymptotic cap arithmetic. |

The group-average map is
`A_G:R^{[q]^N}->R^{[q]^N}`, `A_G nu=|G|^{-1} sum_{g in G} g.nu`, for
`G=S_N x C(sigma)`. It preserves total mass, annihilation, and correlation with invariant `F`, but
only guarantees `||A_G nu||_1<=||nu||_1`. This map is well defined; the report's subsequent use of
its normalization is the source of D10, not a type failure of the map itself.

### 7b — identity-level gates in every regime: EXECUTED

The fresh script reconstructs the correlation from the three block atoms
`(S,g)=(+,YES),(-,NO),(-,YES)` with polynomial probabilities
`1/2,rho_j/2,(1-rho_j)/2`. For each `m=1,2,3`, it checks the identity against a full basis of the
zero-total outer-measure space: respectively 1, 3, and 7 point-difference basis elements. Thus the
check is an identity in the independent variables `rho_1,...,rho_m`, not a value at one pattern.
The exact inequality follows from `2|Psi(-1^m)|<=||Psi||_1=1` at each `m`.

The script also reconstructs occupancy gates at `m=2` and `m=3`. Results are:

| case | outer | band | rows | support | `l1` | correlation |
|---|---|---:|---:|---:|---:|---:|
| `(10,5,0,2)` | correlated order 1 | 2 | 6 | 12 | 1 | 1 |
| `(10,5,0,2)` | parity | 4 | 56 | 16 | 1 | `1/2` |
| `(15,7,0,3)` | correlated order 1 | 2 | 8 | 32 | 1 | 1 |
| `(15,7,0,3)` | parity | 6 | 792 | 64 | 1 | `1/4` |

The `m=2` printed values are therefore independently reconstructed, and `m=3` exercises the
multi-block identity beyond the commissioned point. The logarithmic-inner branch is exercised
symbolically for arbitrary `rho_j` and separately by exact barycentric values, including the tight
`rho=4/5` case; the small occupancy gates intentionally use the degenerate `rho=1` endpoint.

### 7c — anchoring ban: EXECUTED

Before reading phase 4 I derived:

1. For support `T_n={0,1,5,...,5^(n-1)}`, conditional negative-sign correctness equals the dual
   correlation. For `n>=2`, the `K=1` and `K=5` absolute-weight ratios alone contribute at least
   `5/4+1/4`, so `rho<=4/5`. This is **proved and tight** at `n=2`, not merely observed. For `n=1`,
   `rho=1`, so the qualifier “logarithmic block” must mean `r_j>=5`/`n>=2`.
2. Whole-pair allocation forces `sum_j r_j<=(q-1)/2`, hence `m r0<=(q-1)/2` for equal blocks.
   Therefore `m` cannot grow with `N` at fixed `q`.

These match the phase-4 fixed-allocation derivation. The fresh notation independently coincides on
`rho`, `m`, and `r0` only because those symbols are already part of the claim; the derivation and
support restriction were recorded before the report was opened.

### 7d — frozen inputs only within reviewed scope: EXECUTED

M1/M2 and L2P3 were treated as PROVED only in their reviewed scopes. The new use of L2P3's complete
sign support and the uniform `4/5` bound was reopened. The proof above establishes the bound from
the barycentric weights; no phase-3 status was used as immunity. The fresh script gives exact values
`1,4/5,16/21,992/1315,...`, confirming both the endpoint exception and strict decrease after the
tight case.

### 7e — standing failure-mode list: EXECUTED

- Type/dimension mismatch: found the off-support `sgn(0)` and under-specified block/occupancy lift
  (D11); no numerical dimension mismatch survives the repaired types.
- Quantifier tops and caps: swept `q=5` and `q=N`; checked the `r_j=1` endpoint and the first
  logarithmic `r_j=5` endpoint separately.
- Family boundary: hardened “standard absolute-value OR block composition” to the displayed
  unaveraged product/sign-bit formula. The renormalized invariant average is not covered without a
  norm-preservation theorem (D10).
- Charge direction: `dD` is a lower-bound annihilation band; Johnson/B4a are upper caps. No reversal
  remains.
- Tautology: the proposer verifier reads proposer weights and claimed values from JSON; it rechecks
  values but does not reconstruct the printed formula (D12). The fresh driver reconstructs it.
- Threshold: `16/25<2/3` is exact and respects the strict `>2/3` direct error-`1/3` convention.
- Preregistration: all six manifest hashes match. Filesystem ordering is predictions
  (`22:03:19Z`), scripts (`22:05:45Z`, `22:05:50Z`), outputs (`22:06:01Z`, `22:06:02Z`), manifest
  (`22:07:33Z`), then report (`22:09:57Z`). The transcript corroborates that the prediction was
  registered before construction. This proves the available on-disk ordering, not off-record
  knowledge. `BLOCKED` remains correct under the frozen definition because T2 is a precise
  obstruction to the selected whole-pair mechanism even after D10 limits T1.

### 7f — value versus formula: EXECUTED

For `(N,q,t,m)=(10,5,0,2)`, I verified the **printed formulas by independent reconstruction**, not
by rerunning proposer code. The fresh driver constructs both inner and outer measures, composes
them, recomputes all 6/56 factorial rows, norm, support, activity layers, and correlation in exact
`Fraction` arithmetic. It imports neither proposer module nor proposer JSON. Commands, output, and
SHA are linked above. The proposer `ksum_l2p4_exact_verify.py`, by contrast, validates values parsed
from the proposer JSON and therefore is a value-level checker, not an independent formula
reconstruction.

### 7g — every term resolves: EXECUTED

- **Conditional correctness:** resolved to
  `P_j(g_j=NO | S_j=-1)` under `P_j=|mu_j|`, conditioned on `sigma(S_j)`.
- **Whole sigma-pair allocation:** resolved to pairwise-disjoint sets `A_j` of complete nonfixed
  two-cycles of `sigma`, with a block allowed to use both endpoints of its assigned cycles and no
  other values.
- **Absolute-value block composition:** resolved to the displayed density
  `2^m Psi(S) product_j |mu_j|` on the product support; it is a hard formula-defined class.
- **Value-disjoint soundness:** resolved operationally in “Cross-block soundness”: pairwise-disjoint
  whole-pair allocations imply that a complementary hit cannot use two blocks. The phrase is not
  separately labeled as a definition, but its necessary and sufficient mechanism is explicit.

## Target verdicts

### T1 — correlation-product obstruction

**PROVED component, with a mandatory class boundary.** For the unaveraged product-support measure
defined by the L2P4 formula, the exact identity

`<zeta,OR_m>=-2 Psi(-1^m) product_j rho_j`

holds for every `m>=1`, and `|<zeta,OR_m>|<=product_j rho_j`. The phase-3 logarithmic inner has the
tight bound `rho<=4/5`; consequently any fixed allocation containing two such blocks has
correlation at most `16/25<2/3`. The fresh identity gates cover `m=1,2,3` and a basis of every
zero-total outer at each such `m`.

This PROVED component does **not** include arbitrary group averaging followed by `l1`
renormalization. That extension remains OPEN unless norm preservation or an equivalent
post-average product bound is proved.

### T2 — value-budget obstruction

**PROVED component for whole-pair/value-disjoint allocation.** Pair-disjointness gives
`sum_j r_j<=(q-1)/2`; equal blocks give `m r0<=(q-1)/2`. At fixed `q`, both the number of blocks and
every phase-3 block band are bounded independently of `N`, so no composition on these finitely many
block sign bits can produce the canonical `sqrt(N)` growth. This is not a theorem about schemes
that reuse complementary values and suppress cross-block hits by another exact mechanism.

### T3 — BLOCKED classification, obligation, caps, and G11

**PASS with the T1 scope correction.** The selected preregistered mechanism includes whole-pair
allocation, so T2 independently satisfies the frozen BLOCKED definition. This blocks a mechanism,
not the L2 route. The updated obligation must bypass the whole-pair budget and either avoid the
fixed-allocation product loss, improve the inner to aggregate error `O(1)`, use more than sign bits,
or prove that symmetry cancellation/renormalization itself yields a legal high-correlation witness.
It must still engage the untouched `sqrt(N)` side.

Cap sweep: at `q=5`, `m<=2` and the conditional band is `O(1)`, while the canonical target grows as
`Theta(sqrt(N))`. At the opposite endpoint `q=N` (on the odd subsequence), the conditional expression
is `O(sqrt(N))`, below the Johnson `N^(2/3)` cap and B4a's
`N^(3/4+epsilon)` endpoint. The same bounds cover the intervening range. No exponent consequence is
drawn from `(10,5,0,2)` or `(15,7,0,3)`; G11 passes.

### T4 — node, views, index, and header

**PASS after synchronization in this review change.** The canonical L2 leaf stays CONJECTURED; its
phase-4 pending-review marker is removed only for the now-reviewed components. The parent and all
ancestors retain their computed OPEN statuses. The node, parent, index note, Mermaid label, nested
outline, ledger, prover prompt, and “Most recent change” header now state the T1 boundary, T2 proof,
and unchanged cap-scale obligation consistently.

## Defects and severity

### D10 — product bound lost under possible norm-reducing symmetry average (MAJOR)

The report correctly says a group average can decrease `l1`, and that normalization can increase
positive correlation. It then uses the pre-average upper bound `product rho_j` as though it also
bounded the normalized invariant measure. If `bar(zeta)=A_G zeta`, then

`<bar(zeta),F>=<zeta,F>` but `||bar(zeta)||_1<=1`,

so the normalized correlation is `<zeta,F>/||bar(zeta)||_1`, potentially larger than the product.
No norm-preservation or post-average lower bound on `||bar(zeta)||_1` is proved. This is a MAJOR
scope gap in T1 as an obstruction to the final invariant class. It does not overturn T2 or the
selected-mechanism BLOCKED outcome.

### D11 — support and index types under-specified (MINOR)

`sgn(mu_j(x_j))` is not `{±1}`-valued where `mu_j=0`, and `x_j` is overloaded between block inputs
and string positions. Restricting to `supp(mu_j)` and separating block, pair, and position indices
repairs the candidate lemma without changing any value.

### D12 — “independent reconstruction” overstates proposer verifier scope (MINOR)

The proposer verifier reads the constructed weights and expected scalar values from proposer JSON.
It independently recomputes moment rows and labels, but it does not reconstruct the formula that
produced those weights. This is value-level verification. The fresh review script supplies the
missing formula-level reconstruction.

## What I did not check

- I did not prove norm preservation for the full `S_N x C(sigma)` average or determine whether its
  cancellations can rescue correlation; this is the live D10 escape.
- I did not construct the canonical cap-scale witness, an `eta>1/6` exponent result, or any
  `sqrt(N)`-engaging replacement.
- I did not enumerate all `5^10` or `7^15` strings. The fresh finite gates are complete occupancy
  falling-factorial checks, with the already reviewed orbit-lift/query-degree map used in scope.
- I did not construct or import a general `Omega(sqrt(m))` OR dual.
- I did not review even-`q` cycle types, reused-value mechanisms, additional targets, or a full
  symmetry-averaged finite instance.
- I did not re-review M1/M2/L2P3 outside the precise uses named above, rerun optimizer extraction,
  use the network, or make a git commit.
