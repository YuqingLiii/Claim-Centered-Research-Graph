# Independent hostile review — KSUM.B4b.L2 phase 5

Date: 2026-07-19  
Reviewer: fresh independent hostile reviewer; authored none of the target work; no wanted verdict  
Network: not used  
Commits: none  
Scope: averaged occupancy/factorial band lemma, true-NO orientation loss, equal-total Fourier/l1
obstruction, finite gates, preregistration, caps/G11, classification, and DAG synchronization

## Pre-action report

Before opening the phase-5 report, scripts, or logs, I reloaded from disk the research-structure
protocol, proof-DAG protocol including every item of binding rule 7, KSUM node index, complete
`KSUM.B4b.L2` node, parent `KSUM.B4b`, and the completed phase-2, phase-3, and phase-4 reviews in
their M1/M2, L2P3, T1/T2/D10 scopes. I then independently derived the averaged factorial
convolution identity and the exact NO-side orientation-coherence cost and wrote them to
[ANCHORING_DERIVATION.txt](logs_ksum_L2p5r_20260719/ANCHORING_DERIVATION.txt). Only after that file
existed did I open the phase-5 report, proposer scripts, predictions, outputs, and manifest.

The worktree was already heavily dirty, including the target node/views, untracked phase-5 files,
and unrelated SE work. I preserved those changes and made no commit. I did not execute any phase-5
proposer script and used no network.

Fresh reviewer evidence, importing neither proposer modules nor proposer values:

- [exact occupancy/Vandermonde reviewer](../tools/ksum_l2p5r_exact_review.py) and
  [output](logs_ksum_L2p5r_20260719/exact_review.log);
- [Fourier algebra reviewer](../tools/ksum_l2p5r_fourier_review.py) and
  [output](logs_ksum_L2p5r_20260719/fourier_review.log);
- [provenance audit](logs_ksum_L2p5r_20260719/PROVENANCE_AUDIT.txt),
  [commands](logs_ksum_L2p5r_20260719/COMMANDS.txt), and reviewer SHA manifest.

## Ruling

**T1 PROVED as a general band-multiplication component. T2 PROVED only for the hard class of
identical phase-3 blocks with one common exact pair total, combined by a product tensor and then
averaged/normalized. T3 PASS: BLOCKED is correct for that selected family, not for all averaged
compositions. The L2 route remains CONJECTURED.**

The review finds one **MINOR** documentation defect: the canonical shorthand “repeated equal-total
family” did not itself enumerate every class condition. The phase-5 lemma and proof do enumerate
them, so the theorem is sound; synchronized summaries are hardened to exclude unequal totals,
nonidentical blocks, and non-product couplings explicitly.

## Rule-7 execution log

### 7a — type audit of every in-scope display: EXECUTED

Fix a finite alphabet `A=Z_q`, odd `q=2r+1`, involution `sigma(a)=t-a`, one fixed point `f`, and
`r` nonfixed two-cycles. For block `j`, let `N_j` be its number of positions and
`Omega_j={n^(j) in N_0^A: sum_a n^(j)_a=N_j}`. A block occupancy measure is a vector
`mu_j in R^{Omega_j}`. Its orbit lift lies in `R^{A^[N_j]}`. The raw tensor lies in
`R^{A^[N]}`, `N=sum_j N_j`; `A_{S_N}:R^{A^[N]}->R^{A^[N]}` is the linear group average. Its
occupancy pushforward lies in `R^{Omega_{N,q}}`, where `Omega_{N,q}` has `q` coordinates and fixed
total `N`.

| Display | Domain/codomain and dimension audit | Result |
|---|---|---|
| `T={0,1,5,...}` and `W_k` | `T subseteq {0,...,r}`; `W in R^T` is the normalized divided-difference functional. `K` here is a **single-block** interior-pair count. | PASS. |
| `bar(lambda)(x)=nu(n)/Mult(N;n)` | `x in A^[N]`, `n in Omega_{N,q}`; `nu in R^{Omega_{N,q}}`. `Mult(N;n)` is the size of the global string orbit and is positive. | PASS. |
| hypergeometric `H` | For a typed split `n=sum_j n^(j)`, `H` is a scalar probability on `prod_j Omega_j`; multiplying the block-orbit densities cancels every block multinomial. | PASS. |
| `nu(n)=sum prod_j mu_j(n^(j))` | The convolution maps `prod_j R^{Omega_j}` multilinearly to `R^{Omega_{N,q}}`; only coordinatewise-compatible splits occur. | PASS. |
| `L=sum_n |nu(n)|` | `L=||A_{S_N} lambda||_1` is a nonnegative scalar. For nonzero finite block measures it is positive because the generating-polynomial product is nonzero in an integral domain. | PASS. |
| `M_mu(alpha)` | `alpha in N_0^A`; `(n)_alpha` is a scalar row on the relevant occupancy slice, and `M_mu(alpha)` is a real scalar. | PASS. |
| multivariate Vandermonde display | Each `alpha^(j) in N_0^A`; the coordinatewise multinomial coefficient is scalar and every factor `M_(mu_j)(alpha^(j))` is defined on block `j`. | PASS. |
| `d5=2m(1+floor(log_5 r))` | This is a query-degree lower bound after the reviewed orbit filtration; `m` counts positional blocks, not pairs or query positions. | PASS. |
| NO mass and correlation displays | `W_0` is a single-block layer mass; `2^{-r(m-1)}` is a conditional orientation probability; `nu(NO)`, the numerator, and the normalized correlation are scalars. | PASS. |
| `hat(mu)(z)=sum_n mu(n)z^n` | For `z in (S^1)^q`, this is a complex scalar. Convolution becomes multiplication in `C`; `|hat(nu)(z)|<=||nu||_1` is the triangle inequality. | PASS. |
| `A_s`, `I_s` | These are local complex evaluations for one pair with exact total `s`: `A_s=cos(s theta)` and `I_s` equals `1` or `cos(theta)` according to the parity of `s`. | PASS. |
| Fourier norm/correlation bounds | Both sides are nonnegative real scalars. Cancellation of `rho^m` is legal because `rho=2|W_0|>0`. | PASS. |
| `m<=N/(2r)` and cap displays | `m` is dimensionless; `N,2r` count positions. These are feasibility/cap inequalities, not achieved lower bounds. | PASS. |

Occupancy and orientation bookkeeping is type-correct. For pair `c={a_c,b_c}`, an axis atom has
positive total entirely at one endpoint, and its orientation is that endpoint. Block activity
`K_j` counts phase-3 interior pairs inside block `j`. The finite M2 signature instead uses
`K_global(n)=#{c:n_(a_c)>0 and n_(b_c)>0}` after merging. Oppositely oriented axis blocks can
increase `K_global` even when every `K_j=0`; the proof and fresh code never identify these types.

### 7b — identity gates at `m=2` and `m=3`: EXECUTED

The fresh exact script reconstructs the block law and convolution from definitions. For every
commissioned target it checks every factorial row below the claimed band and reconstructs that row
from the complete multivariate Vandermonde split. At `m=2` it checks 56 rows/286 splits for each
`q=5` target and 120 rows/680 splits for each `q=7` target. The independent `m=3` gate
`(N,q,m,t)=(12,5,3,0)` checks 252 rows and 15,504 splits below band 6. Both regimes also check the
orientation identities: coherence is `1/4` for `m=2,r=2`, `1/8` for `m=2,r=3`, and `1/16` for
`m=3,r=2`; the `m=3` exact correlation is `1/64`.

The fresh Fourier script separately gates the outer parity identity and exponent inequalities for
`m=2,3,4`, `2<=r<=20`, including support changes at `r=5`. These finite gates corroborate the
general algebra; the general verdict comes from the proof below, not extrapolation.

### 7c — anchoring ban: EXECUTED

Before opening phase 5, I derived the coordinatewise falling-factorial Vandermonde formula and the
orientation cost `2^{-r(m-1)}` in my own typed construction. The pre-report record is linked in the
pre-action section. Its notation coincides on `m`, `r`, `alpha`, and `mu` because those symbols were
part of the claim; the derivation order and added scope exclusions are independently recorded.

### 7d — frozen inputs only within reviewed scope: EXECUTED

M1/M2, L2P3, and phase-4 T1/T2 were used only in their archived scopes. Phase 5 newly load-bears
L2P3 block factorial cancellation under convolution, its axis-orientation law after merging, and
its exact Fourier polynomial on common-total slices. I reopened and proved all three aspects here;
the phase-3 review was not treated as immunity. M2 is used only for the five-condition
representation signature, not as an obstruction to the new correlated family.

### 7e — standing failure modes: EXECUTED

- Type mismatch: block `K_j`, global `K_global`, pair index, block index, value coordinate, and
  position index were separated above. No mismatch survives.
- Top-of-range/caps: at fixed `q=5`, feasibility allows `m<=N/4` and formal band `2m<=N/2`, which
  can exceed the Johnson cap only because correlation fails. At canonical `q=N`, `m>=2` is
  infeasible since every block needs at least `q-1` positions; the only feasible `m` is one.
- Soft family boundary: T2 below is explicitly limited to identical blocks, common exact `s` on
  every pair and block, and a product tensor. Unequal totals, nonidentical blocks, and non-product
  couplings are outside the theorem.
- Charge direction: `m d0` is an annihilation lower bound; Johnson/B4a are algorithmic upper caps.
  No cap-violating witness is inferred.
- Tautology: fresh code reads neither proposer JSON nor proposer modules. The proof was checked
  analytically as well as computationally.
- Strict threshold: every finite correlation is strictly below `2/3`; T2 gives `<=1/2`, so no
  equality-at-`2/3` convention is used.
- Preregistration: all nine proposer manifest hashes match. Disk/transcript ordering places the
  frozen prediction before scripts and runs. The frozen BLOCKED definition is met by a general
  scoped obstruction, not by the four failed examples alone.

### 7f — value versus formula: EXECUTED

The exact reviewer verifies the **printed construction and identities by independent
reconstruction**: it builds the layer functional, block occupancy law, convolution, true label,
norm, all-target rational values, every band row, and every Vandermonde split. It does not rerun or
import proposer code and does not read proposer output. Thus it verifies more than the four values.
The Fourier reviewer exercises the exact outer parity formula and exponent algebra; the torus
choices and triangle-inequality step were verified line-by-line analytically. Neither code nor the
finite table alone proves the analytic theorem.

Fresh rational results:

| `(N,q,m)` | band | pre-normalization `l1` | normalized correlation |
|---|---:|---:|---:|
| `(10,5,2)` | 4 | `13/16` | `2/13` |
| `(12,5,2)` | 4 | `7/8` | `1/7` |
| `(14,5,2)` | 4 | `31/32` | `4/31` |
| `(12,7,2)` | 4 | `1` | `1/16` |

### 7g — every term resolves: EXECUTED

- **Axis orientation:** for an axis atom on `{a_c,b_c}`, the unique endpoint carrying its positive
  exact pair total.
- **Equal pair totals:** one common integer `s>=2` is used on every nonfixed pair in every block;
  equality merely within a block or equality of total block sizes is insufficient.
- **Unit-torus Fourier evaluation:** substitute `z_a in S^1` in the finite occupancy generating
  polynomial and take its complex modulus; it is not an integral or a normalized Fourier transform.
- **K-layer:** in the phase-3/Fourier proof, the set of block atoms with exactly `K` interior pairs.
  In the finite M2 signature, “global K-layer” means the separately defined `K_global` after
  occupancy merging.

## Target verdicts

### T1 — band-multiplication lemma

**PROVED component.** For arbitrary finite nonzero signed block occupancy measures `mu_j` on fixed
sizes, the `S_N`-averaged product has occupancy pushforward `nu=mu_1*...*mu_m`. Coordinatewise
falling-factorial Vandermonde gives

`M_nu(alpha)=sum_(sum beta^(j)=alpha) Mult(alpha;beta^(1),...,beta^(m)) prod_j M_(mu_j)(beta^(j))`.

If block `j` annihilates every factorial row below `d_j`, then `|alpha|<sum_j d_j` forces some
`|beta^(j)|<d_j` in every summand. Hence the average annihilates below `sum_j d_j`, or `m d0` for
equal bands. The reviewed orbit filtration turns this into query degree with no loss. Convolution
is nonzero for nonzero blocks because finite generating polynomials have no zero divisors, so
normalization is legal. This is a useful independent positive component even though T2 blocks the
selected witness family.

### T2 — orientation-coherence/Fourier obstruction

**PROVED component with a hard class boundary.** Let `q=2r+1>=5`, `m>=2`, and `s>=2`. Take the
same phase-3 block on every positional block, with fixed-point occupancy zero and exact total `s`
on every nonfixed pair; combine the blocks by the raw product tensor, average over `S_N`, and
normalize by the actual post-average `l1`. Then true NO requires all blocks to be on their all-axis
layer and, independently for each pair, all `m` uniform orientations to agree. Its exact cost is
`2^{-r(m-1)}`.

For the norm floor, set endpoint phases to `(e^{i theta},e^{-i theta})`. If `s` is even, choose
`theta=pi/s`; if `s` is odd, choose `theta=pi/(s+1)`. In both cases `I_s=-A_s`, with `|A_s|=1`
for even `s` and `|A_s|>=2^{-1/2}` for odd `s`. All positive support nodes are odd and
`sum_k W_k=0`, so `|sum_k W_k(-1)^k|=2|W_0|=rho`. Therefore
`L>=rho^m|A_s|^(rm)`. Dividing the exact numerator yields

`corr <= 2^(r+1-m(r+1)) |A_s|^(-rm)`.

This is at most `1/8` for even `s` and at most `1/2` for odd `s`; the odd exponent is
`r+1-m(r/2+1)<=-1`. The theorem does **not** cover unequal pair totals, different block kernels,
signed/non-product outer couplings, correlated orientations, or alternative inners. D10 is closed
only for the displayed hard class, not for all averaged compositions.

### T3 — classification, obligation, caps, G11, and synchronization

**PASS.** The frozen BLOCKED definition demanded a precise new obstruction, not a failed finite
example. T2 applies on an infinite admissible `N=mrs` subsequence for every fixed odd `q`, whereas
the canonical route needs a witness for every sufficiently large `N`; therefore it blocks the
selected repeated identical family. It does not refute L2. The leaf remains CONJECTURED, B4b and
its ancestors remain OPEN, and no exponent status changes.

The surviving D10 routes are exactly: nonidentical blocks, deliberately unequal pair totals,
non-product outer couplings (including correlated orientations), alternative inner kernels, or
non-composition witness shapes. Any repair must still suppress cross-block hits, retain strict
correlation `>2/3`, engage the untouched `sqrt(N)` side, and meet the capped
`c0 min{sqrt(N)q^eta,N^(2/3)}` target for every large `N`, odd `5<=q<=N`, and every target.

The cap sweep above covers `q=5` and `q=N`. G11 passes: finite degrees/norms/correlations validate
the formulas, not an exponent trend. The node, parent, index, Mermaid label, nested outline,
ledger, prover prompt, and top header are synchronized to this scoped ruling.

## Defect and severity

### D13 — “repeated equal-total” was soft in canonical shorthand (MINOR, repaired)

The theorem statement in the phase-5 report says every block has the same exact pair total and that
the block is repeated, so the proof itself has a hard class. Several canonical summaries shortened
this to “repeated equal-total,” which could be misread as allowing unequal totals across blocks or
nonidentical blocks. The synchronized text now states the three load-bearing conditions: identical
phase-3 blocks, one common exact `s` on every pair and block, and raw product outer coupling.

Severity: **MINOR**. It changes no formula, finite value, component status, or route status.

## What I did not check

- I did not prove an obstruction for unequal pair totals, nonidentical blocks, non-product outer
  couplings, alternative inners, or non-composition witnesses.
- I did not construct the canonical cap-scale witness, engage its `sqrt(N)` side, or prove any
  `eta>1/6` exponent consequence.
- I did not review even-`q` targets/cycle types or enumerate raw `q^N` strings; exact occupancy rows
  and the already reviewed orbit/query filtration were used.
- I did not prove the `1/2` bound tight or determine the exact post-average norm for all parameters.
- I did not re-review M1/M2/L2P3 or T1/T2 outside the precise new uses named in rule 7d, rerun
  optimizer extraction, execute proposer code, use the network, or make a git commit.
