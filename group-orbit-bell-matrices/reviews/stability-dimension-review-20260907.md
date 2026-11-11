# Independent review of spectral stability and the vector-dimension gap

Date: 2026-09-07.

Reviewer: Codex / GPT-6, independent delegated agent
`/root/orbit_stability_audit`.

Independence: the primary research agent authored the candidate proof. This
reviewer received a separate delegated review context, independently derived
the inequalities from the displayed definitions, inspected the source and
replayed the checker. The reviewer did not author or modify the target claims,
proof, checker, or node assessments. This is an independent agent review using
the same model family, not an external human review or a formal proof.

Review root: `/private/tmp/grothorb-exploration-20260907-hLCZqw`.
Only this report was created by the reviewer. No YAML file was edited. This is
an immutable review record; a subsequent correction requires a separate report.

## Materials and statement binding

The two exact statements below are the YAML-loaded `claim` strings, including
their folded whitespace. Their digests were computed by importing
`tools/proof_dag_schema.py:claim_hash`, which strips leading/trailing whitespace
and normalizes CRLF before SHA-256. File digests below bind the inspected
artifact bytes separately from these statement digests.

Primary inspected files and SHA-256 digests:

| Repository-relative path | SHA-256 |
| --- | --- |
| `DAG_PROTOCOL.md` | `d8775b511431e6e9dc7a5be6200af80bd612e7e7d5f5ff10bb14ef748791a095` |
| `FILE_PROTOCOL.md` | `6a2ea1af9bd14a4eaa8d158e304aee5e82cf907497addb17c2771782a4e6a329` |
| `tools/proof_dag_schema.py` | `38772ab9c2847461cf1410e2943681a7c74248669292709e7477153efb54aa2e` |
| `grothendieck-group-orbit/proof-dag/nodes/GROTHORB.near-saturation.yaml` | `773933b7615e89819388195c15f8b6552da84df65f06ec3d573d7fc8b99db98f` |
| `grothendieck-group-orbit/proof-dag/nodes/GROTHORB.robust-dimension-gap.yaml` | `971f5c84917f2d9c9a9e76886df63238cafac21b496b2bb2bb323bad61204e76` |
| `grothendieck-group-orbit/artifacts/spectral-stability-dimension-gap-20260907.md` | `9d865834263273d673c5a4da0c5006c598a0622050a1571b98dc05b83d1d5fdf` |
| `grothendieck-group-orbit/tools/check_spectral_stability.py` | `d0dc91fc79ac18802c1003b3635e7b323c707e470c31e2f0d9edafa59c666888` |
| `grothendieck-group-orbit/artifacts/spectral-stability-exact-check-20260907.md` | `2e94306f2e4509434b4a76d219c227f09f03ecc3ee96a0a5d1338afefdb21872` |

The reviewer also inspected the following context to resolve the definitions
of equivariance, paired bases, vector value, weight normalization, and the P3
example. No verdict on their entire contents is implied:

| Repository-relative path | SHA-256 |
| --- | --- |
| `grothendieck-group-orbit/artifacts/balanced-rank-theorem-draft-20260829.md` | `c6b7bd87193b34ad6e5c05d20971fba2722ba202c3e87e2bd6717a951d5dfef4` |
| `grothendieck-group-orbit/artifacts/complete-extremizer-classification-20260829.md` | `44ac28ada792471f5ff014f763a94da16929ac2f6d99df01b2a056f52a47cd99` |
| `grothendieck-group-orbit/artifacts/balance-rigidity-20260907.md` | `b88ffdd3b086a557912ec42bc37e53d6ec94ab3054d7a4a770f7207f06077cdf` |
| `grothendieck-group-orbit/proof-dag/nodes/GROTHORB.invariant-projector.yaml` | `4289e66365c4abad929aa7022e6adf78c39ec28471dd55f10ef674c51c86ceeb` |
| `grothendieck-group-orbit/proof-dag/nodes/GROTHORB.spectral-upper.yaml` | `5c0a1dbe5a72aad04ce240bd067d77a672a52eae634784d18ccdc634f55aeb97` |
| `grothendieck-group-orbit/proof-dag/nodes/GROTHORB.balanced-criterion.yaml` | `8e58e2d6e861b7b8c23143fd66ed6f69b53b4aab8cea0be81b9339a44281a91d` |
| `grothendieck-group-orbit/README.md` | `f1076c47f43cb893514f941e3ed45dfe96a2e107f95111a2c868813a14e19b14` |

## Finding ST-AUD-1: GROTHORB.near-saturation

Object: node claim `GROTHORB.near-saturation`; direct mathematical proof in
ST1-ST2 of the spectral-stability artifact.

Exact reviewed statement:

```text
Let A be nonzero and real, sigma its top singular value, and tau<sigma the operator norm on the orthogonal complement of its top right singular space (zero if the complement is zero). For unit-row strategies X,Y with objective at least (1-epsilon)sigma sqrt(mn), 0<=epsilon<=1, and normalized x=X/sqrt(m), y=Y/sqrt(n), the squared Frobenius mass of y outside the top right singular space is at most (2epsilon-epsilon^2)/(1-(tau/sigma)^2), and ||x-Ay/sigma||_F^2 <= 2epsilon.
```

Reviewed hash:
`sha256:25645acde7aad5ca01d5957f0f2bac55e747f573b45c40fb8ba9c09cd29ee1e4`.

Verdict: **PASS** for the exact statement in the real unit-row matrix model.

Independent verification:

1. Write `A` as an `m by n` real matrix, and give `X,Y` a common strategy
   width. The objective is `<X,AY>_F`. Unit rows give
   `||x||_F=||y||_F=1`; therefore the normalized objective is
   `q=<x,By>_F`, for `B=A/sigma`. Nonzero `A` gives `sigma>0`, and
   `t=tau/sigma` lies in `[0,1)`.
2. With `P` the full top right singular projector, the invariant orthogonal
   splitting for `B^T B` gives
   `||By||_F^2 <= ||Py||_F^2+t^2||(I-P)y||_F^2`.
   This is valid column by column and then after summing; no square-matrix
   assumption is used. Substituting `||y||_F^2=1` gives
   `||By||_F^2 <= 1-(1-t^2)||(I-P)y||_F^2`.
3. Cauchy--Schwarz gives `q<=||By||_F`. The hypothesis
   `q>=1-epsilon>=0` licenses squaring the lower bound. Hence
   `(1-epsilon)^2 <= 1-(1-t^2)||(I-P)y||_F^2`.
   Division by the strictly positive denominator gives the first claimed
   bound with exactly `2epsilon-epsilon^2`.
4. Expanding the Frobenius square gives
   `||x-By||_F^2=1+||By||_F^2-2q<=2-2q<=2epsilon`.
   The second bound uses `||By||_F<=1` and has the claimed constant.

Boundary checks: at `epsilon=0` the conclusions force exact top-space
concentration and alignment. At `epsilon=1`, the first bound is at least
one, and the alignment bound follows from `q>=0`. The concentration proof
must not be extended to `epsilon>1` by the same squaring step. If the top
right space is all of `R^n`, its complement and outside mass are zero;
the convention `tau=0` is consistent. Nonzero nullspaces, rectangular
matrices, and arbitrary top multiplicity are covered by the same splitting.

Scope: no equivariance, balanced projectors, or attainability of the spectral
upper bound is assumed or needed. This proves concentration and alignment.
It does not prove distance to a feasible exact optimal strategy, a stability
modulus for a chosen Gram matrix, or physical self-testing.

## Finding ST-AUD-2: GROTHORB.robust-dimension-gap

Object: node claim `GROTHORB.robust-dimension-gap`; direct mathematical proof
in ST1 and ST3-ST5 of the spectral-stability artifact, with the transitivity
step independently checked below.

Exact reviewed statement:

```text
Let A be a nonzero real m by n transitive equivariant matrix with top singular value sigma of multiplicity r>=2, paired bases U,V, and largest remaining singular value tau<sigma (zero if there is none). Suppose L(K)=(diag(UKU^T),diag(VKV^T)) is injective on Sym_r, and set s=min_{||K||_F=1}||L(K)||_2>0 and delta=1-tau/sigma. Then every real unit-vector strategy of dimension d<r has value at most (1-delta*s^2/(16*r^2))*sigma*sqrt(m*n).
```

Reviewed hash:
`sha256:5a80145414508268c490c4a89c775e6da0506f121f755a4e0242b3a225cf791e`.

Verdict: **PASS** for the exact statement, using the project's explicit
conventions: transitive permutation actions on both the row and column sets,
`P_g A Q_g^T=A`, and paired orthonormal top bases satisfying
`AV=sigma U` and `A^T U=sigma V`.

Independent verification:

1. Equivariance implies that `AA^T` commutes with every `P_g` and `A^T A`
   with every `Q_g`. Their top spectral projectors therefore commute too.
   Transitivity permutes their diagonal entries, so each diagonal is
   constant; the rank `r` trace fixes the constants to `r/m` and `r/n`.
   Consequently `L(I_r/r)=((1/m)1_m,(1/n)1_n)`. This step does not
   require a classification theorem or an unproved representation-theory
   assumption.
2. For `C=[[0,B],[B^T,0]]`, the `+1` eigenspace is exactly the columns of
   `W=[U;V]/sqrt(2)`. Paired orthonormality gives `W^T W=I_r` and
   `CW=W`. For a rectangular matrix, the remaining eigenvalues are
   `+a/sigma,-a/sigma` for remaining nonzero singular values `a`, the
   `-1` eigenspace paired with the top singular space, and any nullspace
   zeros. Every one is at most `tau/sigma`. This is an upper spectral
   bound, not an absolute-value bound: the `-1` eigenvalue causes no
   difficulty.
3. Set `Z=[x;y]/sqrt(2)`. Then `||Z||_F=1` and
   `<Z,CZ>_F=q`. Put `T=W^T Z`, `Z0=WT`, `E=Z-Z0`, and
   `eta=||E||_F`. The orthogonal decomposition gives
   `q<=||Z0||_F^2+(tau/sigma)||E||_F^2=1-delta eta^2`.
   Thus `eta^2<=(1-q)/delta`. This holds for every strategy, including
   negative `q`; the robust-dimension proof does not silently import the
   nonnegative-score hypothesis from ST-AUD-1.
4. Let `M=[x;y]=sqrt(2)Z`, `M0=[UT;VT]=sqrt(2)Z0`, and
   `H=TT^T`. The two diagonal row-norm vectors of `MM^T` are
   `((1/m)1_m,(1/n)1_n)`, while those of `M0M0^T` are `L(H)`.
   For arbitrary equal-shape row matrices `F,G`, rowwise factorization,
   Cauchy--Schwarz, and the triangle inequality prove
   `||diag(FF^T-GG^T)||_2 <= ||F-G||_F (||F||_F+||G||_F)`.
   Here `||M||_F=sqrt(2)`, `||M0||_F<=sqrt(2)`, and
   `||M-M0||_F=sqrt(2)eta`. Hence
   `||L(H-I_r/r)||_2<=4eta`, with no missing `sqrt(2)` factor.
5. Compactness of the Frobenius unit sphere and injectivity of `L` imply
   `s>0`. Homogeneity gives `s||K||_F<=||L(K)||_2` for every
   symmetric `K`, including `K=0`. Consequently
   `||H-I_r/r||_F<=4eta/s`.
6. Since `T` has only `d<r` columns, `H` has a unit null vector `v`.
   Therefore `||H-I_r/r||_F>=||(H-I_r/r)v||_2=1/r`.
   Combining with the preceding bounds yields
   `1-q>=delta s^2/(16r^2)`. Multiplication by the positive scale
   `sigma sqrt(mn)` proves exactly the claimed value bound.

Boundary and normalization checks: if no smaller positive singular value
exists, `tau=0` gives `delta=1`; all extra dilation eigenvalues are zero or
negative, including the case of a full top right singular space. The proof
remains valid. The dilation weight has `Tr(H)=||T||_F^2<=1`, with scalar
comparison weight `I_r/r`. At exact saturation, the weight in the earlier
unnormalized equality classification is `nH`; confusing these conventions
would change the bound, but the present derivation does not do so. Changing
paired bases by a common orthogonal matrix conjugates `K` orthogonally, so
the Frobenius singular constant `s` is independent of that choice.

Scope: `d` is the common ambient real vector dimension of the correlation
strategy. The conclusion alone does not establish a minimum complex local
Hilbert-space dimension, a dimension estimate in a different physical model,
robust self-testing, or an optimal quantitative gap. No claim of sharpness is
needed for the constant `16r^2`.

## Supplementary finding ST-AUD-3: P3 conditioning and finite replay

Object: the P3 conditioning calculation in
`artifacts/spectral-stability-exact-check-20260907.md` and the finite checker.
This supplementary finding is not a third universal node claim.

Verdict: **PASS** for the exact P3 constant and the reported finite checks.

For the displayed basis of `1_3^perp`, the Frobenius-orthonormal symmetric
basis is `E0=I/sqrt(2)`, `E1=diag(1,-1)/sqrt(2)`, and
`E2=[[0,1],[1,0]]/sqrt(2)`. Each side of `L(Ej)` has the following
three entries, and the full vector repeats the same entries twice:

```text
L(E0), one side: (sqrt(2)/3, sqrt(2)/3, sqrt(2)/3)
L(E1), one side: (1/(3sqrt(2)), 1/(3sqrt(2)), -2/(3sqrt(2)))
L(E2), one side: (1/sqrt(6), -1/sqrt(6), 0)
```

The columns are pairwise orthogonal, with full squared lengths
`4/3,2/3,2/3`. Thus `L^*L` has precisely those three eigenvalues and
`s^2=2/3`. The stated threshold is
`1-(2/3)/(16*2^2)=95/96`. This calculation is independent of the finite
strategy enumeration and respects the Frobenius normalization of off-diagonal
coordinates.

The reviewer reran the unmodified checker from the review root with Python
3.9.6 (standard-library `fractions` and `itertools`):

```text
python3 grothendieck-group-orbit/tools/check_spectral_stability.py

P3 signs: nonnegative_pairs=46, best_relative_score=8/9, dimension_gap_threshold=95/96, PASS
P3 rational planar strategies: nonnegative_pairs=2440, best_relative_score=8/9, PASS
diag(2,1) imbalanced strategies: nonnegative_pairs=128, best_relative_score=3/4, PASS
1x4 rectangular strategies: nonnegative_pairs=584, best_relative_score=1, PASS
All checks use exact Fraction arithmetic. This finite run is not a universal proof.
```

Exit status was zero. The checker updates the best score before omitting
negative-score cases from the ST2 inequalities; that omission agrees with the
declared `epsilon=1-q` range. It enumerates all scalar sign strategies for
P3, but only the four listed rational unit vectors for the planar examples.
It does not enumerate all real planar strategies, verify arbitrary inputs to
`check`, or mechanize the universal dilation argument. The scalar optimum
`8/9` is also independently consistent with
`max_x x^T P3 y=||P3 y||_1`: a constant sign vector gives zero, and a
nonconstant three-coordinate sign vector gives `8/3`, normalized by three.
The matrix P3 itself has singular values `1,1,0`; the distinct number `2/3`
is the least squared singular value of its balance map `L`, not of P3.

## Overall verdict and limitations

Both universal mathematical claims pass the independent adversarial review at
their exact statement hashes above. The proof was checked algebraically; the
finite run is corroboration and is not the basis for universal quantification.
The review found no mathematical repair necessary within the stated real
vector scope. It does not certify other project claims, the full DAG's
protocol compliance, a formalization, or any novelty or priority statement.

The target nodes were `OPEN` at inspection. This report does not promote them.
Any promotion must separately attach the applicable finding and exact reviewed
hash, link the proof and run evidence, preserve events, and complete the
repository's required state validation. File hashes above describe the
inspected snapshot; changing a claim invalidates that claim's statement-bound
verdict until it is reviewed again.
