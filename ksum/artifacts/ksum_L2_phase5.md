# KSUM.B4b.L2 phase 5 — averaged shared-value positional composition

Date: 2026-07-19  
Route status: **CONJECTURED · phase-5 mathematics pending-review**  
Preregistered outcome: **BLOCKED for the repeated equal-block phase-3 shared-value composition**  
Scope: odd `q>=5`, strict correlation `>2/3`; no even-`q` or exponent claim.

## Pre-action report

Before preregistration or phase-5 experimentation, the executor reloaded the research-structure
protocol, the proof-DAG protocol including rule 7, the KSUM node index, the complete
`KSUM.B4b.L2` record and propagating ancestors, B4a, the phase-2 through phase-4 reports and
completed reviews, and all proposer/reviewer scripts supporting M1, the five-condition M2 class,
L2P3, T1, T2, and D10. The reviewed scopes were frozen exactly: M1 is slice-wise; M2 applies only
to its five-condition class; L2P3 has band `2(1+floor(log_5 r))` and correlation at least
`437/581`; T1 is only the unaveraged fixed-allocation sign-bit formula; T2 is only whole-pair
value-disjoint allocation. No network, sub-agent, or git commit was used.

The prediction and escape ledger were written before any phase-5 script or finite run:
[predictions](logs_ksum_L2p5_20260719/predictions.txt).

## Outcome

The mandatory `S_N` average is completely computable and does preserve the tensor-product
annihilation band. For `m` identical phase-3 positional blocks, each of inner band `d0`, the
averaged occupancy measure annihilates every query polynomial below `m d0`. Thus the algebraic
band really has the sought first `N`-side multiplication when `m` grows.

It is not a witness. Shared values create cross-block 2-Sum hits. They reduce the true-NO mass by
the exact factor `2^(-r(m-1))`, while symmetry cancellation does not reduce `l1` nearly enough at
the required finite gates. More generally, on the equal-pair-total subsequence a unit-torus
Fourier mode gives a post-average `l1` lower bound and forces normalized correlation at most `1/2`
for every odd `q>=5` and `m>=2`.

This is the preregistered **BLOCKED** outcome for the selected repeated equal-block shared-value
phase-3 mechanism. It is a new averaged-composition obstruction, not a refutation of all D10
escapes. Under DAG rules 6 and 7, the general moment and Fourier statements are
**CONJECTURED · pending-review**; the exact runs are NUMERICAL evidence.

## 1. Construction and escape ledger

Fix odd `q>=5`, target `t`, and `r=(q-1)/2`. Let the nonfixed cycles of
`sigma(a)=t-a` be `(a_c,b_c)`, `1<=c<=r`. Split the `N=mb` positions into `m` labeled blocks of
size `b>=2r`. Every block uses every one of the same `r` value pairs, and the fixed-point occupancy
is zero.

On each block, use the reviewed phase-3 axis/interior probabilities on balanced exact pair-total
slices, with divided-difference layer weights `W_k` supported on

```text
T={0,1,5,...,5^(h-1)},    h=1+floor(log_5 r).
```

Call the resulting block occupancy measure `mu`. Form the raw string tensor
`lambda=tensor_(j=1)^m mu`, average over `S_N`, compute the actual resulting norm `L`, and use
`bar(lambda)/L` only when `L>0`. Each block is already `C(sigma)`-invariant, so the final object is
`S_N x C(sigma)`-invariant.

The frozen escape ledger passes in its intended scope:

1. **M2 condition 5:** the signed correlated layer functional is not a sign-aligned positive
   mixture. At every finite gate, the final averaged measure has both coefficient signs inside one
   global `K` layer; at the `q=5` gates its supported global `K=r=2` layer has total signed mass
   exactly zero. Either property is impossible in M2, whose five conditions force a common
   nonzero product sign on every global `K` layer. This is a representation-independent signature.
2. **T2:** every block reuses all `r` value pairs, so the blocks are positional only and
   `sum_j r_j<=r` does not apply.
3. **T1/D10:** the construction includes the explicit norm-changing map
   `A_(S_N)(tensor_j mu_j)` and division by its actual `l1`. Moreover, global 2-Sum is not the OR of
   the within-block functions because opposite axes in different blocks form a hit. Reviewed T1
   covers neither feature.

## 2. The averaged occupancy and moment computation

Write `mu_j(n^(j))` for the signed occupancy mass of block `j`. If `x` is a global string with
occupancy `n`, then the `S_N`-averaged density is

```text
bar(lambda)(x) = nu(n) / Mult(N;n),
nu(n) = sum_(n^(1)+...+n^(m)=n) product_j mu_j(n^(j)).
```

This follows directly from the hypergeometric split. Conditional on global occupancy `n`, a random
permutation assigns occupancies `n^(j)` to the position blocks with probability

```text
H(n^(1),...,n^(m) | n)
  = product_j Mult(b_j;n^(j)) / Mult(N;n).
```

The raw block-orbit density is `product_j mu_j(n^(j))/Mult(b_j;n^(j))`; multiplying by `H` cancels
the block multinomials and gives the convolution formula. Consequently the exact D10 norm is

```text
L = ||bar(lambda)||_1 = sum_n |nu(n)|,
```

not the pre-average value one.

For a factorial row `alpha=(alpha_a)`, define

```text
M_mu(alpha) = sum_n mu(n) product_a (n_a)_(alpha_a).
```

Multivariate Vandermonde gives the mathematical heart of the phase:

```text
M_nu(alpha)
 = sum_(alpha^(1)+...+alpha^(m)=alpha)
     [ product_a Mult(alpha_a; alpha_a^(1),...,alpha_a^(m)) ]
     product_j M_(mu_j)(alpha^(j)).
```

Equivalently, average a degree-`d` raw query over `S_N`. Its queried positions split among the
blocks hypergeometrically; the factors `(b_j)_(d_j)` from the split probability cancel the same
factors in the block orbit averages, leaving precisely the displayed factorial sum divided by
`(N)_d`.

If every block annihilates orders below `d0`, a nonzero term requires
`|alpha^(j)|>=d0` for every `j`. Hence `|alpha|>=m d0`. The averaged and renormalized object
therefore annihilates all query degrees below

```text
d5(m,q) = 2m(1+floor(log_5((q-1)/2))).
```

This is a proposer proof pending independent review. The exact verifier reconstructs both the
hypergeometric density and every Vandermonde row in the finite bands.

## 3. True correlation and the cross-block loss channel

Let `W_0<0` be the phase-3 mass on the all-axis layer in one block. A global input is NO only if:

- every block uses its `K=0` layer; and
- for each of the `r` complementary pairs, all `m` blocks choose the same axis endpoint.

The second event has axis-probability `2^(1-m)` per pair. Pair-total mixing does not affect it.
Thus, after choosing the harmless global orientation,

```text
|nu(NO)| = |W_0|^m 2^(-r(m-1)),
R_raw = <bar(lambda),F> = 2 |W_0|^m 2^(-r(m-1)),
<bar(lambda)/L,F> = R_raw/L.
```

The blockwise-OR numerator would have been `2|W_0|^m`. Therefore cross-block hits are exactly the
multiplicative loss `2^(-r(m-1))`. Averaging preserves the numerator because `F` is invariant; D10
can help only if the exact norm `L` shrinks by a comparable factor.

It does not at the commissioned points. At `(10,5,2)`, `L=13/16` and normalized correlation is
`2/13`. At `(14,5,2)`, `L=31/32` and normalized correlation is `4/31`.

## 4. New averaged-composition obstruction

### Lemma L2P5-F (proposer proof; pending review)

Let every block have the same exact pair total `s>=2`, so its size is `b=rs`, and repeat this block
`m>=2` times. For every odd `q>=5`, the normalized averaged composition has correlation at most
`1/2` against true 2-Sum.

### Proof

Use the occupancy generating polynomial `hat(mu)(z)=sum_n mu(n)z^n` on the unit torus. Give every
pair the endpoint phases `(e^(i theta),e^(-i theta))`. Its axis and interior polynomials are

```text
A_s = cos(s theta),
I_s = 1                 if s is even,
I_s = cos(theta)        if s is odd.
```

If `s` is even, take `theta=pi/s`; then `I_s=-A_s` and `|A_s|=1`. If `s` is odd, take
`theta=pi/(s+1)`; again `I_s=-A_s`, while `|A_s|=cos(theta)>=2^(-1/2)` because `s>=3`.

All positive divided-difference support nodes `1,5,25,...` are odd. Since `sum_k W_k=0`,

```text
|sum_k W_k(-1)^k| = |W_0-sum_(k>0)W_k| = 2|W_0| = rho.
```

Therefore this torus point has `|hat(mu)(z)|=rho |A_s|^r`. The averaged occupancy measure is the
`m`-fold convolution, so its Fourier value is the `m`th power. The triangle inequality now gives
the missing lower bound on the actual post-average norm:

```text
L >= |hat(mu)(z)|^m = rho^m |A_s|^(rm).
```

Since `|W_0|=rho/2`, the normalized correlation is at most

```text
2^(r+1) [ 2^(-(r+1)) / |A_s|^r ]^m.
```

For even `s` this is `2^((r+1)(1-m))<=1/8`. For odd `s` it is at most
`2^(r+1-m(r/2+1))<=1/2`; the last exponent is at most `-1` for every `r,m>=2`.
This proves the scoped obstruction.

The theorem closes the D10 norm loophole for the repeated equal-total phase-3 block family without
assuming norm preservation. Because balanced totals become equal whenever `r` divides the block
size, the preregistered equal-block construction fails on an infinite required `N` subsequence.
Nonidentical blocks and deliberately unequal pair totals remain outside this theorem.

## 5. Band cap sweep

The formal band is `d5=2mh(r)`, where `h(r)=1+floor(log_5 r)`, and feasibility gives
`m<=N/(2r)=N/(q-1)`.

- At `q=5`, `r=2`, `h=1`, so the algebra permits `d5=2m` and as much as `N/2` with minimal
  blocks. This eventually exceeds the Johnson `N^(2/3)` cap. The Fourier/correlation obstruction
  is therefore necessary: the large formal band cannot coexist with the required correlation.
- At `q=N` on the odd subsequence, feasibility forces `m<=N/(N-1)<2`, hence integer `m=1`.
  There is no block amplification; the band is only `O(log N)`, below both Johnson `N^(2/3)` and
  B4a's `N^(3/4+epsilon)` endpoint.

Thus no cap-violating witness statement is recorded. The only achieved high-degree multiplication
is attached to a correlation-failing signed measure.

## 6. Exact gates

All scripts use `fractions.Fraction`. Every listed target was checked, every residual was exactly
zero, post-renormalization `l1` was exactly one, and the complete odd-`q` centralizer was checked.

| `(N,q,m)` | targets | band | rows/target | raw post-average `L` | normalized correlation | `>2/3` |
|---|---:|---:|---:|---:|---:|---|
| `(10,5,2)` | 5 | 4 | 56 | `13/16` | `2/13` | FAIL |
| `(12,5,2)` | 5 | 4 | 56 | `7/8` | `1/7` | FAIL |
| `(14,5,2)` | 5 | 4 | 56 | `31/32` | `4/31` | FAIL |
| `(12,7,2)` | 7 | 4 | 120 | `1` | `1/16` | FAIL |

The independent verifier imports no constructor. It reconstructs the formula, all hypergeometric
split cells, every factorial Vandermonde row, norm, true label, M2 escape signature, and group
action. The Fourier script checks `|sum W_k(-1)^k|=rho` exactly across all support transitions
through `r=15626` and checks the integral exponent inequalities for `2<=r<=12`, `2<=m<=8`.

| purpose | command | raw log | script SHA-256 |
|---|---|---|---|
| construct/average/check | `python ksum/tools/ksum_l2p5_averaged_composition.py --output ksum/artifacts/logs_ksum_L2p5_20260719/averaged_composition_results.json` | [log](logs_ksum_L2p5_20260719/averaged_composition.log) | `c457f6f9c32935c0791f816de720810a6407b0ce7e753d0e92e5490bc4c00a27` |
| independent reconstruction | `python ksum/tools/ksum_l2p5_exact_verify.py --input ksum/artifacts/logs_ksum_L2p5_20260719/averaged_composition_results.json` | [log](logs_ksum_L2p5_20260719/exact_verify.log) | `6fdd2178ced18c48b3e23c8b9ebc74ecac3572bf359a9d5a574328b170c4aaf1` |
| Fourier obstruction gates | `python ksum/tools/ksum_l2p5_fourier_obstruction.py` | [log](logs_ksum_L2p5_20260719/fourier_obstruction.log) | `39dc05b85452266b7cddb2dab82b2b044613b3147ba6e3d508e61b93cb953eb8` |

Full commands and hashes: [COMMANDS](logs_ksum_L2p5_20260719/COMMANDS.txt) and
[SHA-256 manifest](logs_ksum_L2p5_20260719/SHA256SUMS.txt).

## 7. Gate table, outcome, and G11

| gate | result |
|---|---|
| M2 condition-5 escape | PASS at every finite gate by mixed signs within a global `K` layer; `q=5` also has zero total signed `K=r` mass |
| not whole-pair disjoint | PASS: every positional block uses all `r` value pairs |
| D10 averaging present | PASS: exact convolution norm computed before renormalization |
| averaged moment algebra | PASS analytically at proposer tier; exact hypergeometric/Vandermonde reconstruction passes |
| first `N`-multiplying formal band | PASS algebraically: `m d0`; not a witness because correlation fails |
| strict correlation `>2/3` | FAIL at every finite gate; general equal-total bound is `<=1/2` |
| cap endpoints | PASS as a negative audit; no cap-violating witness claim recorded |
| G11 | PASS: finite values verify formulas and machinery only |

**Recorded outcome: BLOCKED for repeated equal-block phase-3 shared-value positional composition.**
This extends the map as follows: T1 blocks fixed-allocation unaveraged sign-bit composition, T2
blocks whole-pair value-disjoint amplification, and L2P5-F blocks the canonical repeated
shared-value averaged phase-3 composition on its equal-total subsequence. The broader D10 space is
not closed: unequal/nonidentical blocks or a non-phase-3 inner could evade L2P5-F.

## What was not checked

- No independent rule-7 review was performed; L2P5-F and the general `m d0` moment lemma remain
  CONJECTURED/pending-review.
- No general obstruction was proved for nonidentical blocks, deliberately unequal pair totals,
  non-product outer couplings, or inner kernels other than L2P3.
- No raw enumeration of all `5^10` strings was run. The complete occupancy filtration and the exact
  hypergeometric orbit identity were checked instead; `(14,5)` is far beyond raw enumeration.
- No canonical cap-scale witness, `eta>1/6` exponent consequence, or `sqrt(N)` lower bound was proved.
- No even-`q` target/cycle type, optimizer extraction, or network source was used.
