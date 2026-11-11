# Independent review: same-tuple high-Schmidt spectral-flat extensions

Date: 2026-08-30

Reviewer: OpenAI Codex, fresh independent review context
`/root/weyl_majorization_audit`.

Review status: complete. This immutable project-level report does not edit or promote any
canonical YAML node.

## Independence declaration

I did not author the artifact or any of the four proposer-side claims. I reconstructed the
Stinespring map, realignment ranks, flip spectra, normalization and norm constants independently.
I also ran fresh finite-dimensional smoke tests, but the verdicts below rest on the analytic
arguments rather than those tests.

I read `DAG_PROTOCOL.md` and `FILE_PROTOCOL.md` before review. Their SHA-256 digests were
`d8775b511431e6e9dc7a5be6200af80bd612e7e7d5f5ff10bb14ef748791a095` and
`d9d6fb57a26fef3b70fc05bda74a29101d83a43df60e06eaeb345e76980fc595`.

## Executive verdict

All four current claims pass and are safe to promote to `PROVED` at the exact hashes recorded
below. The CP normalization is exact; the complement projector has spectral rank `m^2-1` and
maximal operator-Schmidt rank `m^2`; the `q`-family has the stated positivity, normalization,
operator-Schmidt rank and amplitude bound; and the Haagerup--Kadison statement is correctly scoped
to an unrefined proof route.

There is one nonfatal artifact-only wording issue. Section 3.2 says the complement projector has
trace greater than `A` in the intended parameter range. This is not true uniformly for all
`m>=2, eta>=0`; it requires

`A < sqrt(m^2-1)`, equivalently
`(1+eta)^2 < (m/9)(sqrt(m^2-1)-1)`.

The project regime of very large `m` and sufficiently small `eta` satisfies that condition, and
the complement-projector node does not include any trace assertion. The issue therefore does not
block its promotion. The `q`-family's separate trace statement is correctly qualified by `m>A`
and sufficiently small nonzero `q`.

## 1. Immutable inputs and exact hashes

Raw SHA-256 file hashes at review time:

| Input | SHA-256 |
|---|---|
| `artifacts/SAME_TUPLE_HIGH_SCHMIDT_SPECTRAL_FLAT_EXTENSION_20260830.md` | `ce2c8c876f29ffd8bd03fca72cb233a5679fd2a2a48e02a8ccb55f56245bca1a` |
| `nodes/HEXT.same-tuple-positive-spectral-flat-base-case.yaml` | `695b873f7ba66a4c9a860cc49580b9c20f3853691007872512182a1cd2045172` |
| `nodes/HEXT.same-tuple-maximal-schmidt-complement-projector.yaml` | `53bd1a8c0ae0244f544af5357e8c39d068877fb7bd4b071746b80c015f9eef90` |
| `nodes/HEXT.same-tuple-positive-maximal-schmidt-double-off-neighborhood.yaml` | `d01b2dc5d1165111071867b5312a8fa3356815299da55accbfdc7b92ec2569ba` |
| `nodes/HEXT.same-tuple-high-schmidt-kadison-haagerup-obstruction.yaml` | `b8903a067d27fa7a05c7277682c06cf4bd855901d4a22f641b7356fc116af516` |

Node paths in this table are under `holevo-extensive-violation/proof-dag/`; the artifact path is
under `holevo-extensive-violation/`.

The exact folded claim hashes are:

| Node | Exact current claim hash | Verdict |
|---|---|---|
| `HEXT.same-tuple-positive-spectral-flat-base-case` | `sha256:f00f5c8a230c705544b0b5e04382b9c0ea6e9a4b8a57c3ef041c74cf3c98fd9e` | PASS; safe for `PROVED` |
| `HEXT.same-tuple-maximal-schmidt-complement-projector` | `sha256:eddd21711e6c99128e861a89c5079863d2801334dea5f5b45ff801b20c015de7` | PASS; safe for `PROVED` |
| `HEXT.same-tuple-positive-maximal-schmidt-double-off-neighborhood` | `sha256:4ca2ed5626897e8321f20db4ccc4af753cbbf6de03da211f1f0bcffd18ef8800` | PASS; safe for `PROVED` |
| `HEXT.same-tuple-high-schmidt-kadison-haagerup-obstruction` | `sha256:a457d528ff40e5f77764cb47ed0d8840bfcf2f51b75c699f5df400bb9f57d127` | PASS; safe for `PROVED` |

Claim hashes are `sha256(claim.strip())` after YAML folding and CRLF normalization.

## 2. Fresh smoke tests

A fresh Numpy test with seed `20260830` checked `m=2,3,5` and random unitary tuples:

- the Stinespring residual `||V^*V-I||_F` was below `7.2e-16`;
- the normalized complement projector had Hilbert--Schmidt norm one, spectral ranks
  `3,8,24`, and realignment ranks `4,9,25` respectively;
- at the worst target parameter `eta=0`,
  `A/m-1/sqrt(m^2-1)` was positive in every tested dimension;
- an exhaustive grid over `m=2,...,7`, `eta in {0,0.25,3}`, both amplitude endpoints and an
  interior `q` verified positivity, the target operator-norm comparison, and realignment rank
  `1+m(m-1)` for every nonzero `q`;
- for the normalized off-diagonal flip at `m=2,3,7,20`, the flat Kadison bound was
  `sqrt(m(m-1))/m`, tending to one, whereas using the exact scaled-unitary images before Kadison
  gave `sqrt(m(m-1))/m^2`, of order `1/m`; and
- the complement-projector trace comparison was explicitly seen to fail at small `m` or large
  `eta`, confirming the need for the artifact-only qualifier recorded above.

## 3. Findings

### Finding HSSF-IR-01 -- PASS: Stinespring normalization and UCP contraction are exact

**Applies to:** `HEXT.same-tuple-positive-spectral-flat-base-case`, exact claim hash
`sha256:f00f5c8a230c705544b0b5e04382b9c0ea6e9a4b8a57c3ef041c74cf3c98fd9e`.

For

`V xi = m^(-1/2) sum_v |v> tensor U_v xi`,

one has

`V^*V = m^(-1) sum_v U_v^*U_v = I`.

Direct multiplication gives

`V^*(X tensor I)V = m^(-1) sum_(v,w) X_(v,w) U_v^*U_w = C^*(X)`.

Thus `C^*` is unital completely positive, with exactly the normalization used in the four-index
definition. Its tensor square is unital completely positive even though the same tuple is reused
on both tensor legs. For Hermitian `H`, applying order preservation to
`-||H|| I <= H <= ||H|| I` yields

`||M_U(H)||_infinity <= ||H||_infinity`.

For positive `Y` with `||Y||_F=1`, the condition `||Y||_infinity<=A/m` is equivalent to

`r_infinity(Y)=||Y||_F^2/||Y||_infinity^2 >= m^2/A^2`.

Consequently the target follows deterministically for every unitary tuple. No independence between
tensor legs, randomness, entry support, or operator-Schmidt-rank bound is used. The exact current
claim passes.

### Finding HSSF-IR-02 -- PASS: projection ranks and the low-rank-hole threshold are correct

**Applies to:** the projection consequences in Sections 3.1--3.2 and the scope of the first two
nodes.

If `P` is an orthogonal projection of rank `r`, then `P/sqrt(r)` is positive,
Hilbert--Schmidt normalized and has operator norm `1/sqrt(r)`. Finding HSSF-IR-01 proves the target
whenever

`r >= m^2/A^2`.

For `P=I-H` with `rank(H)=k`, this is exactly

`k <= m^2(1-1/A^2)`.

Writing `A=1+c/m`, `c=9(1+eta)^2`, gives

`m^2(1-1/A^2) = 2cm-3c^2+O(c^3/m)`.

Hence the artifact's `18(1+eta)^2 m + O((1+eta)^4)` statement is correct only in its explicitly
stated fixed-`eta`, large-`m` sense; it is not a uniform expansion in arbitrary growing `eta`.
Neither atomic claim uses such a uniform asymptotic.

### Finding HSSF-IR-03 -- PASS: the complement projector has maximal realignment rank

**Applies to:** `HEXT.same-tuple-maximal-schmidt-complement-projector`, exact claim hash
`sha256:eddd21711e6c99128e861a89c5079863d2801334dea5f5b45ff801b20c015de7`.

Let `Q=I-|Omega><Omega|`. It is an orthogonal projection of spectral rank `m^2-1`, so
`Q/sqrt(m^2-1)` is positive and Hilbert--Schmidt normalized. Under coefficient realignment,
`I_m tensor I_m` becomes `u u^*`, where `u=vec(I_m)` and `||u||^2=m`, while

`|Omega><Omega| = m^(-1) sum_(v,w) E_(v,w) tensor E_(v,w)`

becomes `I_(m^2)/m`. Thus the realigned matrix of `Q` is

`u u^* - I_(m^2)/m`.

It has eigenvalue `m-1/m` along `u` and `-1/m` on the `m^2-1` dimensional orthogonal complement.
For every `m>=2` it is invertible, so the operator-Schmidt rank is exactly the maximal value
`m^2`.

The UCP contraction gives output norm at most `1/sqrt(m^2-1)`. It remains to check the least
favorable `eta=0`. The artifact uses the valid chain

`A >= 1+1/m >= m/sqrt(m^2-1)` for every `m>=2`,

which is equivalent to `1/sqrt(m^2-1)<=A/m`. Larger `eta` only increases `A`. Thus the exact node
claim is uniform for all `m>=2, eta>=0` and passes.

The coefficient trace equals `sqrt(m^2-1)`. This exceeds `A` only under the inequality stated in
the executive verdict, not for all node parameters. Because trace is absent from the exact node
claim, this artifact-only wording issue is nonblocking.

### Finding HSSF-IR-04 -- PASS: the off-diagonal flip norms and ranks are exact

**Applies to:** `HEXT.same-tuple-positive-maximal-schmidt-double-off-neighborhood`, exact claim
hash `sha256:4ca2ed5626897e8321f20db4ccc4af753cbbf6de03da211f1f0bcffd18ef8800`.

The operator

`E_x = sum_(v!=w) E_(v,w) tensor E_(w,v)`

annihilates every diagonal vector `|v,v>` and swaps `|v,w>` with `|w,v>` on each unordered
off-diagonal pair. Its spectrum is therefore `0` on an `m`-dimensional space and `+1,-1` on each
two-dimensional pair. Hence

`||E_x||_infinity=1`, `||E_x||_F^2=m(m-1)`.

The displayed matrix-unit factors form two orthonormal families. All Schmidt singular values are
one, so

`OSR(E_x)=m(m-1)`, `pi_X(E_x)=m(m-1)`, and
`pi_X(E_x)/||E_x||_F=sqrt(m(m-1))`.

The identity Schmidt direction lies in the diagonal matrix-unit subspaces, orthogonal to every
off-diagonal direction. Therefore realignment of `I+qE_x` has rank
`1+m(m-1)` whenever `q!=0`. No cancellation is possible. These assertions hold for all `m>=2`;
the formulas remain harmless at `m=1` as well.

### Finding HSSF-IR-05 -- PASS: the q-family positivity, normalization and target interval close

**Applies to:** the same node and exact claim hash as Finding HSSF-IR-04.

The numerator `I+qE_x` has eigenvalues `1` on the diagonal sector and `1+q,1-q` on each
off-diagonal pair. It is positive semidefinite exactly for `|q|<=1` and positive definite exactly
for `|q|<1`. Orthogonality to the identity gives

`||I+qE_x||_F^2 = m^2+q^2m(m-1)`,

so the denominator in `Y_q` is exact. The coefficient operator norm is

`||Y_q||_infinity = (1+|q|)/sqrt(m^2+q^2m(m-1)) <= (1+|q|)/m`.

Thus `|q|<=A-1`, together with the positivity restriction, proves the claimed interval
`|q|<=min(1,A-1)` for every `m>=2, eta>=0`. This is a sufficient interval, not an assertion that
the target fails immediately outside it.

Direct substitution also verifies

`M_U(E_x)=R_U-I/m` and
`M_U(Y_q)=[I+q(R_U-I/m)]/sqrt(m^2+q^2m(m-1))`.

The family has full coefficient spectral rank for `|q|<1`. Its trace is
`m^2/sqrt(m^2+q^2m(m-1))`, which tends to `m` as `q` tends to zero. Therefore the artifact's
trace-greater-than-`A` sentence is correctly restricted to `m>A` and sufficiently small nonzero
`q`. The exact node claim passes without enlargement to constant amplitude.

### Finding HSSF-IR-06 -- PASS: Haagerup followed only by Kadison retains the nuclear sum

**Applies to:** `HEXT.same-tuple-high-schmidt-kadison-haagerup-obstruction`, exact claim hash
`sha256:a457d528ff40e5f77764cb47ed0d8840bfcf2f51b75c699f5df400bb9f57d127`.

For a Schmidt expansion with nonnegative singular values `s_j`, the operator Cauchy--Schwarz or
Haagerup inequality applied to `sqrt(s_j)C^*(X_j)` and `sqrt(s_j)C^*(Z_j)` gives exactly the two
weighted square functions in the artifact. Unital complete positivity implies the correctly
oriented Kadison inequalities

`C^*(X_j)C^*(X_j)^* <= C^*(X_jX_j^*)`,

and similarly `C^*(Z_j)^*C^*(Z_j) <= C^*(Z_j^*Z_j)`.

If both coefficient square functions are flat, Hilbert--Schmidt normalization of the Schmidt
vectors forces their scalar value to be `(sum_j s_j)/m`. Unitality then makes the product bound

`||M_U(E)||_infinity <= (sum_j s_j)/m`.

For an equal-Schmidt-rank `r` Hilbert--Schmidt unit direction, `s_j=1/sqrt(r)` and the nuclear sum
is `sqrt(r)`. At `r=Theta(m^2)` the displayed bound is `Theta(1)`, not the target scale
`Theta(1/m)`.

This does not say every use of Haagerup fails. For the off-diagonal matrix-unit family, retaining
the exact fact `C^*(E_(v,w))=U_v^*U_w/m` before Kadison improves each square function by a factor
`m`, and the structured target can succeed. The node accurately obstructs only the unrefined
Haagerup-followed-by-Kadison route and is safe for `PROVED`.

### Finding HSSF-IR-07 -- SCOPE PASS: the general high-Schmidt positive cone remains open

The spectral-flat theorem is a sufficient coefficient-operator-norm condition. The explicit
double-off family is confined to `|q|<=min(1,A-1)`. Neither result controls arbitrary positive
high-operator-Schmidt-rank coefficients, large coefficient operator norm, or the constant-
amplitude repeated-tuple Werner direction. The obstruction finding rules out only one relaxation
route. The artifact and all four nodes preserve these boundaries.

## 4. Promotion recommendations

Promote all four current nodes to `PROVED`, binding:

1. `HEXT.same-tuple-positive-spectral-flat-base-case` to Finding HSSF-IR-01;
2. `HEXT.same-tuple-maximal-schmidt-complement-projector` to Findings HSSF-IR-02--03;
3. `HEXT.same-tuple-positive-maximal-schmidt-double-off-neighborhood` to Findings
   HSSF-IR-04--05; and
4. `HEXT.same-tuple-high-schmidt-kadison-haagerup-obstruction` to Finding HSSF-IR-06.

The review links must use the exact claim hashes in Section 1. Do not infer or promote the general
same-tuple strong-norm node from these base cases.

## 5. Limitations

- I reviewed deterministic consequences for the four precise coefficient classes and the stated
  proof-route obstruction; I did not prove the general same-tuple theorem.
- The numerical runs were finite-dimensional indexing checks, not evidence for a wider claim.
- The artifact's fixed-`eta` asymptotic and intended-parameter trace prose must not be read as
  uniform statements in arbitrarily growing `eta`.

