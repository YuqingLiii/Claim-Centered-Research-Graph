# d=4 degree-four SOS/H4 symmetry audit and exact four-block obstruction

Date: 2026-08-30

Status: author-side exact certificate, awaiting independent adversarial review.
This note does not modify the canonical DAG.  It records a new exact
restricted-SOS obstruction, an audit repair, and the next correctly oriented
block problems.

## 1. Scope and direction

Put

\[
 f(x,y)=C-x^TAy,\qquad C=2081044153087351400
\]

in the Boolean quotient by `x_i^2=y_j^2=1`.  The implication directions in
`grothendieck-d4/artifacts/d4-duality-direction-audit-20260829.md` are correct:

1. A coefficient identity
   \(f=\sum_k q_k^2\), with \(\deg q_k\leq 2\), is a primal certificate and
   proves the desired Boolean upper bound.
2. Since `f` is zero on every equality assignment, every summand in such an
   identity must vanish there.  Hence it is lossless to place all summands in
   the equality-vanishing seed module \(K\).
3. A linear functional \(L\) with \(L(q^2)\geq0\) for every \(q\in K\) and
   \(L(f)<0\) separates `f` from that SOS cone and refutes the degree-four SOS
   route.  It does not prove the upper bound.
4. Refuting a restricted family of proposed separating functionals, such as
   the archived affine families, establishes neither a primal SOS certificate
   nor infeasibility of the unrestricted dual.

The new certificate below is a separator only for two specified isotypic
blocks.  Consequently it proves a no-go for that restricted primal ansatz; it
does not settle the full twenty-block problem.

## 2. Exact isotypic primal problem

The exact decomposition in
`grothendieck-d4/artifacts/frozen-instance/d4_n1_300x300.mat.complete_K_isotypic.json`
has

\[
 K\simeq\bigoplus_{\rho=1}^{20}V_\rho\otimes\mathbb R^{m_\rho}.
\]

All twenty active blocks are of real type.  After averaging any Gram operator
over the signed H4 action, Schur's lemma gives one real PSD multiplicity
matrix \(Q_\rho\in\mathbb S_+^{m_\rho}\) per block.  In the convention in
which \(\mu_\rho\) includes the representation-dimension and normalization
factors, the exact primal problem is

\[
   Q_\rho\succeq0\quad(1\leq\rho\leq20),
   \qquad \sum_{\rho=1}^{20}\mu_\rho(Q_\rho)=f
   \quad\text{in the Boolean quotient}.                 \tag{2.1}
\]

The recovered dual pencils are the adjoints
\(M_\rho(\theta)=\mu_\rho^*(\theta)\), up to the recorded positive diagonal
congruences.  Thus (2.1), rather than dual feasibility, is the correctly
oriented PSD search for an upper-bound proof.

The multiplicity sizes and symmetric parameter counts are:

| block | \(m_\rho\) | \(m_\rho(m_\rho+1)/2\) |
|---:|---:|---:|
| 1 | 582 | 169653 |
| 2 | 465 | 108345 |
| 3 | 611 | 186966 |
| 4 | 211 | 22366 |
| 5 | 611 | 186966 |
| 6 | 822 | 338253 |
| 7 | 235 | 27730 |
| 8 | 162 | 13203 |
| 9 | 107 | 5778 |
| 10 | 397 | 79003 |
| 11 | 504 | 127260 |
| 12 (trivial) | 43 | 946 |
| 13 (Coxeter sign) | 17 | 153 |
| 14 | 107 | 5778 |
| 15 | 166 | 13861 |
| 16 | 235 | 27730 |
| 17 | 162 | 13203 |
| 18 | 504 | 127260 |
| 19 | 384 | 73920 |
| 20 | 286 | 41041 |

The full invariant Gram problem therefore has 1,569,415 real symmetric
coordinates before coefficient-map rank reduction.

## 3. The two one-dimensional seed blocks

### 3.1 Trivial block

There are 55 exact H4-invariant orbit sums of degree at most two.  Restriction
to the right equality 6-face and the swapped-left equality 6-face has exact
rank 12, leaving a canonical primitive integer kernel basis

\[
 v_{12}(z)\in\mathbb Z^{43}.
\]

Its canonical hash is

`0e2b5b533b0f78d9072997571aaeea9e79393c9e546eab58169fc008c00b92b3`.

### 3.2 Coxeter-sign block

Let \(\chi\) be the one-dimensional character that maps all four Coxeter
generators to `-1`.  Twisted signed-monomial orbit propagation gives exactly
19 nonconflicting degree-at-most-two orbit sums transforming by \(\chi\).
Their two-face restriction has exact rank 2, leaving a canonical primitive
integer kernel basis

\[
 v_{13}(z)\in\mathbb Z^{17}.
\]

The checker verifies word-parity consistency on every one of the
`14400 * 4` generator edges, verifies the stabilizer character on every
monomial-support orbit, and obtains basis hash

`459a3bc27032b2dc37e5a5891d5d795e6195ba51416fed4a6367c53f1cf94303`.

The dimensions 43 and 17 agree with the exact `complete_K_isotypic` export.
For the obstruction below it would in fact suffice that these two-face
kernels contain the corresponding components of the full equality-vanishing
module.

## 4. New exact theorem: blocks 12 and 13 cannot suffice

### D4-SOS-2BLOCK-NOGO

There is no Boolean identity

\[
 f=\sum_k q_k^2
\]

in which every degree-at-most-two summand lies in
\(K_{12}\oplus K_{13}\), the direct sum of the H4-trivial and Coxeter-sign
equality-vanishing seed blocks.

### Proof certificate

Use 1200 Boolean test points.  The first 600 are the single-coordinate flips
of the equality witness \(z_R=(a_x,b_y)\).  The next 600 are deterministic
double flips: for `a=0,...,599`, set `b=(137*a+53) mod 600`, correct the
diagonal case by replacing `b` with `b+1 mod 600`, sort the pair, and retain
each previously unseen pair.

The certificate stores integers \(n_t\) and the common positive denominator
\(10^5\).  Define

\[
 S_{12}=\sum_{t=1}^{1200}n_t v_{12}(z_t)v_{12}(z_t)^T,
 \qquad
 S_{13}=\sum_{t=1}^{1200}n_t v_{13}(z_t)v_{13}(z_t)^T.       \tag{4.1}
\]

Exact unpivoted rational \(LDL^T\) gives 43 strictly positive pivots for
\(S_{12}\) and 17 strictly positive pivots for \(S_{13}\).  Their exact
integer-matrix hashes are respectively

* `6035bfcc0908778b4ac09469cbeae85d6cabc2bb9d3b7273edade432ac6f1a9b`;
* `42a9d6ce0136b7d0287659c816ed803714448a0be6e1fef7273854c528dfcb3d`.

At the same time the exact weighted target numerator is

\[
  \sum_{t=1}^{1200}n_t f(z_t)
  =-78729040408609182032920<0.                           \tag{4.2}
\]

If a restricted SOS existed, average its PSD Gram operator over H4.  Since
the target is invariant and the two irreducibles are nonisomorphic, the
averaged Gram is block diagonal and has the form

\[
  v_{12}(z)^TQ_{12}v_{12}(z)
  +v_{13}(z)^TQ_{13}v_{13}(z),
  \qquad Q_{12}\succeq0,\ Q_{13}\succeq0.               \tag{4.3}
\]

Weighted evaluation of (4.3) on the test set equals

\[
 \operatorname{tr}(Q_{12}S_{12})+
 \operatorname{tr}(Q_{13}S_{13})\geq0,
\]

contradicting (4.2).  This proves the stated restricted no-go.  Notice that
the weights may have either sign; positivity is supplied by the two exact
weighted Gram matrices, not by pointwise positivity of the weights.

### Durable evidence

Certificate:

`tmp/grothendieck-d4-unlinked-20260830/d4-two-one-dimensional-blocks-weighted-evaluation-certificate-20260830.json`

Certificate SHA-256:

`027fb0b9cb3c7459e6b306f7c9314f6fccdee39594e20f836785de7988152fa4`

Independent reconstruction/checker:

`grothendieck-d4/tools/h4_two_onedimensional_blocks_nogo_checker.py`

Replay after installing `numpy`, `h5py`, and `sympy`:

```bash
python3 grothendieck-d4/tools/h4_two_onedimensional_blocks_nogo_checker.py \
  grothendieck-d4/artifacts/frozen-instance/d4_n1_300x300.mat \
  grothendieck-d4/artifacts/frozen-instance/d4_n1_300x300.mat.H4_level2_exact_system.json \
  tmp/grothendieck-d4-unlinked-20260830/d4-two-one-dimensional-blocks-weighted-evaluation-certificate-20260830.json
```

Expected decisive output:

```text
status = EXACT_TWO_ONE_DIMENSIONAL_BLOCKS_SOS_NO_GO_VERIFIED
trivial_positive_ldl_pivots = 43
sign_positive_ldl_pivots = 17
weighted_target_numerator = -78729040408609182032920
```

The narrower trivial-only certificate
`d4-invariant-seed-weighted-evaluation-certificate-20260830.json` is now
subsumed by D4-SOS-2BLOCK-NOGO, but remains a useful simpler regression test.

## 5. Consequence and next low-dimensional primal problem

Any full degree-four SOS certificate, if one exists, must use at least one
isotypic block outside `{12,13}`.  The two smallest remaining multiplicity
sizes are the 107-dimensional blocks 9 and 14.  Thus the next compact
symmetry-selected primal search already supported by recovered operator work
is

\[
 Q_9,Q_{14}\in\mathbb S_+^{107},\quad
 Q_{12}\in\mathbb S_+^{43},\quad
 Q_{13}\in\mathbb S_+^{17},
\]

\[
 \mu_9(Q_9)+\mu_{12}(Q_{12})+
 \mu_{13}(Q_{13})+\mu_{14}(Q_{14})=f.                  \tag{5.1}
\]

This has 12,655 symmetric Gram parameters.  It is a targeted four-block
ansatz, not a lossless reduction of (2.1).  If one wants the absolutely
smallest single-block enlargement, add either block 9 or block 14 to
`{12,13}`; that three-block problem has 6,877 symmetric parameters.  Using
both avoids an arbitrary choice between the two equal-size smallest
remaining blocks and matches the archived `{9,12,13,14}` exploratory runs.

There is a further exact, lossless reduction inside this four-block ansatz.
The target and the block set are invariant under party swap.  Averaging a
feasible Gram operator with its party-swapped conjugate preserves PSD and
the coefficient identity.  The exact party-swap replay gives the following
`(+,-)` multiplicity dimensions:

`tmp/grothendieck-d4-unlinked-20260830/session-full-sos/party-swap-K-modp/party_swap_K_modp_exact.json`

| block | (m_+) | (m_-) | parity-commuting symmetric parameters |
|---:|---:|---:|---:|
| 9 | 43 | 64 | 3026 |
| 12 | 28 | 15 | 526 |
| 13 | 11 | 6 | 87 |
| 14 | 43 | 64 | 3026 |

Consequently (5.1) is equivalent to an eight-PSD-block problem of sizes

```text
43, 64, 28, 15, 11, 6, 43, 64
```

with 6,665 real symmetric parameters, rather than 12,655.

The archived files under
`tmp/grothendieck-d4-unlinked-20260830/session-full-sos/` are only unconstrained
linear-span or numerical search diagnostics.  Their residuals and floating
block spectra are not PSD coefficient certificates and must not be promoted
to a proof or obstruction.

### D4-SOS-4BLOCK-LINEAR-NOGO

The eight-parity-block problem is now decided exactly, and the obstruction is
stronger than PSD infeasibility.  Let

\[
 \Phi:\bigoplus_{(\rho,\epsilon)}
 \mathbb S^{m_{\rho,\epsilon}}\longrightarrow
 \mathbb R[x,y]_{\leq4}/(x_i^2-1,y_j^2-1)
\]

be the coefficient map for the eight parity blocks above.  Then

\[
 \operatorname{rank}\Phi=6665,\qquad \ker\Phi=0,
 \qquad f\notin\operatorname{im}\Phi.                 \tag{5.2}
\]

In particular, there is no Boolean degree-four SOS supported on blocks
`{9,12,13,14}`.

The exact certificate evaluates all 6,665 symmetric Gram-product columns and
the target on 8,000 deterministic Boolean points: the 600 single flips of the
equality witness followed by 7,400 SHAKE-generated four-flip points.  Over
`GF(24001)` the product matrix has rank 6,665 and the target-augmented matrix
has rank 6,666.  A certified 6,666-square augmented minor has determinant

```text
5172 mod 24001
```

and exact matrix hash

```text
ea67e7d6be507d8a54384dcdbaf7e92485221abe2917a2a1a0a8a680a0dca9a7
```

A nonzero modular minor is a nonzero minor of the characteristic-zero map
over `Q(sqrt(5),i)` because all recorded denominators are invertible modulo
24001.  Thus (5.2) is a characteristic-zero conclusion, not merely evidence
from sampled real arithmetic.  Party-swap averaging is lossless, so the
parity restriction does not weaken the no-go within the four selected H4
blocks.  The exact equality-face rank-12 dual kernel is already incorporated
by the canonical `K` restriction; despite those twelve codomain relations,
the 6,665-dimensional Gram-domain map is injective.

Durable evidence:

* theorem manifest:
  `grothendieck-d4/artifacts/certificates/d4-four-block-party-parity-linear-nogo-certificate-20260830.json`;
* augmented-minor rows:
  `grothendieck-d4/artifacts/certificates/d4-four-block-party-parity-augmented-minor-20260830.json`;
* independent exact replay:
  `grothendieck-d4/tools/h4_four_block_party_parity_nogo_checker.py`;
* recorded successful replay:
  `tmp/grothendieck-d4-unlinked-20260830/d4-four-block-party-parity-nogo-checker-output-20260830.json`.

Their SHA-256 values, in the same order, are

```text
4d3698674b61a61230caf77e09bc77438b70e82b074fa9ca7983fca1d45aa4a2
83a7a2b76e3743fde450a3dfcd58f2bf27f5486712583d7ecfa2866aacb9add0
f624433a2475002928614bdda5c06985aedf722100df760ff271e959374dfe7b
ea1d4f5f9d02c2de052444ecbafced9be1df9e8edadc21e41dd6f55718a8e4db
```

The checker reconstructs the certified H4 action, canonical K covariants,
exact party-parity bases, deterministic points, all product evaluations, and
the decisive determinant.  It replays only the prefix through the final
pivot (7,133 points).  It requires `numpy`, `h5py`, and `python-flint`.

Consequently any full degree-four SOS, if one exists, must use a block outside
`{9,12,13,14}`.  The smallest remaining multiplicities are blocks 8 and 17,
both of size 162.  Their party parities are `(84,78)`, contributing 6,651
symmetric parameters each.  The smallest next single-block enlargement is
therefore either `{8,9,12,13,14}` or `{9,12,13,14,17}`, with 13,316
party-parity Gram parameters.  Adding both gives a choice-free six-block
problem with 19,967 parameters.

### D4-SOS-TWO-MINIMAL-5BLOCK-LINEAR-NOGO

Both smallest one-block enlargements above are now decided exactly.  For

\[
 S_8=\{8,9,12,13,14\},\qquad
 S_{17}=\{9,12,13,14,17\},
\]

let \(\Phi_e\) be the party-symmetric Boolean degree-four Gram coefficient
map for \(S_e\), where \(e=8,17\).  Then

\[
 \operatorname{rank}\Phi_e=13316,\qquad \ker\Phi_e=0,
 \qquad f\notin\operatorname{im}\Phi_e.                 \tag{5.3}
\]

Thus neither minimal five-block ansatz has even an indefinite Gram solution;
a PSD Gram is impossible a fortiori.

The certificate is a two-stage exact rank decomposition over `GF(24001)`.
Retain the certified 6,666-row invertible minor
\(M=[\Phi_{9,12,13,14},f]\), whose determinant is `5172`.  Evaluate the
new block on the same rows and on the increasing complementary rows in the
first 13,317 deterministic Boolean points.  Eliminating the base rows gives
the 6,651-square Schur residual

\[
 R_e=B_{e,\mathrm{extra}}-M_{\mathrm{extra}}M^{-1}B_{e,\mathrm{base}}.
\]

For both `e=8` and `e=17`, exact finite-field elimination gives

\[
 \operatorname{rank}R_e=6184,\qquad \dim\ker R_e=467.   \tag{5.4}
\]

This explains why a naive 13,317-point determinant vanishes: those Boolean
evaluations leave 467 spurious affine directions.  Let \(N_e\) be the stored
basis of this kernel and \(X_e=M^{-1}B_{e,\mathrm{base}}\).  Apply the true
746,825-coordinate invariant Boolean coefficient map to

\[
 H_e=\Phi_e^{\mathrm{new}}N_e-[\Phi_{9,12,13,14},f]X_eN_e.
\]

Here the direct invariant contraction \(Q^TJQ\) is exactly `14400` times
the canonical K-pencil adjoint.  (The single-\(q_u^2\) Schur factor
`14400/d_rho` gains a factor \(d_\rho\) after contraction of the
representation indices with \(J^{-1}\).)  On 2,048 deterministic effective
coefficient rows, both 467-column matrices have full rank.  The extracted
467-square minors have determinants

```text
block 8:  13280 mod 24001
block 17:  7143 mod 24001
```

and matrix hashes

```text
block 8:  6fd8914532bbcb3af850cf50ae2382e353181834c0e4c631d6aeb8b13e09f626
block 17: 88d678dcd7b521851dad6684cc0b5954a387fbb322c889566959a7f95940f22d
```

Hence \(H_e\) is injective.  Any relation among the 13,317 augmented
columns first reduces, by the invertibility of \(M\), to a vector in
\(\ker R_e\), and injectivity of \(H_e\) then forces that vector to vanish.
The augmented map therefore has rank `6666+6184+467=13317`, proving (5.3).
A nonzero modular minor lifts to characteristic zero because every serialized
representation denominator is a power of two, hence invertible modulo 24001.

Durable evidence:

* theorem manifest:
  `grothendieck-d4/artifacts/certificates/d4-two-minimal-five-block-linear-nogo-certificate-20260830.json`;
* block-8 Schur and coefficient-minor records:
  `tmp/grothendieck-d4-unlinked-20260830/d4-five-block-8-schur-discovery-20260830.json`,
  `tmp/grothendieck-d4-unlinked-20260830/d4-five-block-8-kernel-coefficient-minor-20260830.json`;
* block-17 analogues:
  `tmp/grothendieck-d4-unlinked-20260830/d4-five-block-17-schur-discovery-20260830.json`,
  `tmp/grothendieck-d4-unlinked-20260830/d4-five-block-17-kernel-coefficient-minor-20260830.json`;
* deterministic heavy replays:
  `tmp/grothendieck-d4-unlinked-20260830/session-fourier-energy/five_block_schur_exact_discovery.py`,
  `tmp/grothendieck-d4-unlinked-20260830/session-fourier-energy/five_block_kernel_coefficient_minor.py`;
* certificate audit:
  `grothendieck-d4/tools/h4_two_minimal_five_block_nogo_certificate_checker.py`.

The apparent affine candidates produced after only 13,317 Boolean evaluations
are explicitly **refuted** by the full invariant coefficient map; they are not
Gram identities.  The next unresolved minimal support is therefore the
six-block set `{8,9,12,13,14,17}` with 19,967 party-parity parameters.

## 6. Exact equality-rank repair: the projected rank is 12, not 28

The full-coordinate statement remains correct: restriction of the 752,621
H4-invariant Boolean moment orbit sums to the two base equality-face orbits
has rank 28.  The old 28 columns have a nonzero 28-by-28 minor modulo 24001,
and the stabilizer Burnside bound is (14+14=28).

The post-pruning question has now been decided exactly.  Let (R_E) be the
same restriction map after retaining only the 746,825 moment coordinates
that occur in the exact `(W-D)^2` product table.  Then

\[
                       \operatorname{rank}R_E=12.       \tag{6.1}
\]

Thus the previously recorded projected-rank-28 consequence is false.

### Exact lower bound

The retained global moment IDs

```text
0, 1, 2, 3, 4, 9, 11, 17, 40, 42, 47, 49
```

give twelve Reynolds orbit sums.  On restriction rows

```text
0, 1, 3, 5, 6, 12, 57, 58, 60, 62, 63, 69
```

their exact integer determinant is

```text
-120231596497305600 != 0.
```

Hence `rank(R_E) >= 12` over characteristic zero.

### Exact upper bound and minimal dependencies

Use the 28 restriction rows selected by the old full-coordinate minor.  They
form a basis of the complete restriction row space.  Exhaustive integer
evaluation on every retained orbit representative proves that the following
sixteen rows are identically zero after projection:

```text
7, 13, 15, 19, 23, 25, 27, 30,
64, 70, 72, 76, 80, 82, 84, 87.
```

These are precisely the eight degree-3/4 Walsh directions on each equality
face.  The other twelve old basis rows are exactly the rows of the nonzero
minor above.  Therefore `rank(R_E) <= 12`, proving (6.1).

The sixteen dependencies are unusually simple and minimal: in the old
28-row basis, each displayed direction projects to the zero vector.  A
dependency basis therefore consists of the sixteen corresponding unit
vectors (support size one).  Completeness follows from the nonsingular
12-by-12 complement.

The exhaustive census is:

| bidegree | orientable coordinates | retained | pruned |
|---:|---:|---:|---:|
| (4,0) | 47157 | 45664 | 1493 |
| (3,1) | 187696 | 186291 | 1405 |
| (2,2) | 282860 | 282860 | 0 |
| (1,3) | 187696 | 186291 | 1405 |
| (0,4) | 47157 | 45664 | 1493 |

The checker uses integer group sums for the decisive vanishing test; the
finite-field determinant is used only to replay the old full-rank lower
bound.  It reconstructs the certified action and all 746,825 retained
coordinates.

Certificate:

`grothendieck-d4/artifacts/certificates/d4-effective-equality-rank-certificate-20260830.json`

Independent checker:

`grothendieck-d4/tools/h4_effective_equality_rank_checker.py`

Recorded successful output:

`grothendieck-d4/artifacts/d4-effective-equality-rank-checker-output-20260830.json`

SHA-256 values for checker, certificate, and recorded output are respectively

```text
460fb1f404a75b9b707f8780b1aac3f459a617c185cb60da515ca4cb638b9d2e
5cadfb23d7965086ac4d935977e151967c397210f37eabbe07547aca5b22c6ad
71ef2169a1895413f7d5f59c2b7811b23d08ec95b9df9332db7f460d016725c2
```

Replay:

```bash
python3 grothendieck-d4/tools/h4_effective_equality_rank_checker.py \
  grothendieck-d4/artifacts/frozen-instance/d4_n1_300x300.mat \
  grothendieck-d4/artifacts/frozen-instance/d4_n1_300x300.mat.H4_level2_exact_system.json \
  grothendieck-d4/tools/bootstrap/h4_nogap_irrep_cache.py \
  tmp/grothendieck-d4-unlinked-20260830/session-full-sos/full-spec \
  grothendieck-d4/artifacts/certificates/d4-effective-equality-rank-certificate-20260830.json
```

The corrected effective-operator consequence is

\[
 \dim\ker\mathcal A^*\geq12,
 \qquad \operatorname{rank}(\mathcal A^*)\leq746825-12=746813. \tag{6.2}
\]

The stronger bound `746797` is not pending: its equality-rank justification
is refuted by (6.1).  It would require sixteen different independent kernel
directions not supplied by projected equality restriction.

## 7. Registration recommendations

### New obstruction node

Suggested ID: `GROTHD4.degree4.blocks-12-13-nogo`

Suggested claim:

> No Boolean degree-four SOS representation of
> `2081044153087351400-x^T A y` exists whose degree-at-most-two summands all
> lie in the direct sum of the H4-trivial and Coxeter-sign
> equality-vanishing isotypic blocks.

Suggested initial assessment: `NUMERICAL`, matching the repository convention
for author-generated exact computational certificates that still await
independent adversarial review.  The assessment should say explicitly that
the arithmetic is exact and mechanically replayed.  Promote only after an
independent reviewer reconstructs the bases, test points, two Gram matrices,
and negative target sum.

Evidence:

* the two-block certificate JSON above (`kind: run`);
* `h4_two_onedimensional_blocks_nogo_checker.py` (`kind: text`);
* this note for the mathematical implication from the checked arithmetic.

### New four-block obstruction node

Suggested ID: `GROTHD4.degree4.blocks-9-12-13-14`

Suggested level: `NUMERICAL` pending an external adversarial replay, while
recording that the author-side arithmetic is exact and independently checked.

Suggested claim:

> The Boolean Bell target is outside the linear image of all party-swap
> invariant Gram matrices supported on H4 blocks 9, 12, 13, and 14.  Hence no
> degree-four SOS supported on those four blocks exists, even allowing
> indefinite Gram matrices before imposing PSD.

Evidence: the theorem manifest, augmented-minor certificate, exact checker,
and recorded replay in Section 5.

### Repair existing equality-rank node

Retain the exact rank-28 full-coordinate face-restriction claim.  Register a
separate post-pruning theorem with rank exactly 12.  Replace the effective
rank consequence by the certified `<=746813` bound and mark the inference to
`<=746797` as `REFUTED`, not merely open.

Suggested new ID: `GROTHD4.degree4.effective-equality-rank12`.

Suggested claim:

> After restriction to the 746,825 moment coordinates occurring in the
> exact `(W-D)^2` product table, the two-face equality restriction map has
> characteristic-zero rank exactly 12.  Sixteen of the old 28 row-basis
> directions project identically to zero.

## 8. What remains open

The strongest new result rules out the joint four-block ansatz
`{9,12,13,14}`.  It neither
constructs a full exact PSD Gram certificate nor constructs a separator
positive on all of `K`.  The decisive degree-four alternatives remain:

1. solve the full primal system (2.1) exactly, thereby proving the Boolean
   upper bound by degree-four SOS; or
2. find a full twenty-block functional with all
   \(M_\rho(\theta)\succeq0\) and \(\theta(f)<0\), thereby proving that this
   particular degree-four SOS route is impossible.

The smallest unresolved targeted primal enlargements add block 8 or block 17
to the refuted four-block family, as quantified at the end of Section 5.
