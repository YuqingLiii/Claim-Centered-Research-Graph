# Independent balance-rigidity and root-frame review

Date: 2026-09-07.

Reviewer: Codex GPT-6, delegated reviewer `/root/orbit_existing_audit`.
The reviewer did not author the balance-rigidity or root-frame proof, checker,
or node statements and made no edits to those inputs. Their author was a
separate delegated agent. This is independent argument review within the
same model family, not a different-model or human review. No webpage ChatGPT
review was used. The reviewer separately audited the pre-existing
spectral/classification chain and its two scope repairs.

Reviewed root:

```text
/private/tmp/grothorb-exploration-20260907-hLCZqw
```

The reviewer read the local `DAG_PROTOCOL.md` and `FILE_PROTOCOL.md` in full;
`artifacts/balance-rigidity-20260907.md` BR-1 through BR-7 and
`artifacts/root-frame-dimension-20260907.md` RF-1 through RF-5 in full;
the two node YAML files including routes and premises; the entire exact
checker and its saved run; and the repaired equality/transitive statements
and existing classification dossier. Project-relative paths in this report
are under `grothendieck-group-orbit/` unless otherwise specified.

Scope is the two exact node claims and their named route implications,
including all-vector versus invariant-vector scope and real vector dimension.
No literature priority, new Grothendieck ratio, fewest-settings bound,
complex quantum-dimension optimum, near-saturation theorem, or robustness
constant was checked or inferred. This report is immutable; later statement
changes require a new hash-bound review. The reviewer did not alter canonical
nodes or assign their assessment levels.

## Reviewed statements and verdicts

Hashes were computed from exact decoded YAML strings with
`tools/proof_dag_schema.py::claim_hash`, using CRLF-to-LF normalization and
outer whitespace stripping before UTF-8 SHA-256. Internal whitespace is not
collapsed. Each target below is an exact node `claim` or route `implication`.

| Finding | Target | Reviewed hash | Verdict |
| --- | --- | --- | --- |
| F1 | `GROTHORB.balance-rigidity.claim` | `sha256:1048c444851e7ad620c1db6724fe83c562a70ecd600d8888d934dbce233dd683` | PASS |
| F1R | `GROTHORB.balance-rigidity.routes.balance-kernel.implication` | `sha256:e08ddabcea9e8dfb69f8f8415efe19300b54fb0b43e4ea90a1ea9fdf7a72aa54` | PASS |
| F2 | `GROTHORB.root-frame-dimension.claim` | `sha256:3316ba45bb7756dce199b39bebcaf076988cca760076c096021ce1d078024450` | PASS |
| F2R | `GROTHORB.root-frame-dimension.routes.root-frame-rigidity.implication` | `sha256:418e4456ef9aabcf3e17e6c09dd12e7e05f5a52f638ec19aaba4ba380506215d` | PASS |

## F1 — Balance-kernel uniqueness and rank reduction: PASS

Let `c=n/r>0`, and use the dossier's exact balance constraints
`diag(UHU^T)=(n/m)1_m` and `diag(VHV^T)=1_n`. The hypotheses are nonzero
and transitive equivariant, so the complete paired top spaces have equal
positive width `r`; their full projectors have constant diagonals `r/m`
and `r/n`. Therefore `H_0=cI_r` is positive definite and satisfies both
constraints, also for rectangular matrices. This checks the scaling of
`H`, which here has trace `n`, not trace one.

Subtracting those affine equations gives exactly
`S(A)=(H_0+ker L) intersect PSD`. Injectivity of `L` forces the single weight
`H_0`. If `K` is any nonzero symmetric element of `ker L`, then for
`0<epsilon<c/||K||_op` both `cI_r+epsilon K` and `cI_r-epsilon K` are
positive definite and feasible. They are distinct, which proves the other
direction of the uniqueness equivalence. Positivity here is interiority in
the PSD cone; full-dimensional interiority of the affine feasible set is
neither true in general nor used.

For the rank reduction, summing `diag(VKV^T)=0` gives
`Tr(K)=Tr(K V^T V)=0`. A nonzero real symmetric traceless matrix has both
positive and negative eigenvalues, so `lambda_min(K)<0`. With
`t_*=-c/lambda_min(K)>0`, the eigenvalues of `H_*=cI_r+t_*K` are
`c(1-lambda_i(K)/lambda_min(K))`. Since division by the negative minimum
reverses the inequality, each is nonnegative and at least one is zero.
Thus `H_*` is feasible and has rank at most `r-1`. It cannot be zero:
the balance constraints give `Tr(H_*)=n>0`.

This also checks the small-dimension boundary. For `r=1`, trace zero forces
`K=0`, so the noninjective branch never applies; no zero-dimensional
unit-vector strategy is claimed. For any noninjective case `r>=2`, the
constructed rank is between one and `r-1`.

The reviewed full equality classification says that all optimal strategies
are factorizations `H=TT^T` of the feasible set, with
`Y=VT` and `X=sqrt(m/n)UT`. The least possible real vector dimension for a
fixed weight is its rank. In the unique case `H_0` has rank `r`, giving
a lower bound `r` on every optimum and an attained width-`r` factorization.
In the noninjective case the endpoint weight gives an optimum in dimension
at most `r-1`. No claim that this endpoint has minimum feasible rank is made;
the identity example shows that another feasible weight may have smaller
rank. The argument applies to all extremizers without averaging. Averaging
does not preserve rank and would not justify this conclusion.

For an orthogonal change of paired bases, the kernel and feasible weights
transform by simultaneous orthogonal congruence. Injectivity, weight ranks,
and all conclusions are therefore independent of basis choice.

## F1R — Balance-kernel implication and assembly: PASS

The route names `GROTHORB.extremizer-classification` as its premise. Its
reviewed claim hash is
`sha256:5cbc9e0d89f69f0929510b7592b1480185c5efcf320a3b619d3da4f41c5d02e3`.
The route's strictly positive scalar weight is justified directly in BR-1
from the exact nonzero/transitive hypotheses, with the invariant-projector
argument written out, rather than being an extra unresolved assumption.
BR-2 and BR-3 supply both uniqueness directions and the explicit boundary
weight. The classification premise then gives exactly the dimension
conclusions in the target. There is no hidden assertion that a numerical
optimizer finds an extreme point.

The upstream equality and transitive statement repairs were inspected at
hashes `sha256:57801178adf2f68edec4a8eeb6fb5fe319462b63eb7d2addbe98028ec314143c`
and `sha256:3595380193737509977c85f3b2806810291bba8218e68de229adb35cb6230ab5`.
They explicitly qualify empty-set minima and zero-matrix constructions.
Here `H_0` proves nonemptiness and `A!=0` is assumed, so neither prior defect
can reappear. The assembled mathematical implication passes. Formal DAG
completion still requires the relevant upstream reviews to be attached and
their nodes assessed; this report itself makes no automatic level changes.

## F2 — Transitive root-frame family: PASS

For each `r>=3`, every unordered pair `i<j` contributes four distinct
vectors `+/-e_i +/-e_j`. Distinct supports or distinct sign choices give
distinct rows, so `n=4 binom(r,2)=2r(r-1)` is correct. On one support,
summing the four row outer products gives
`4 e_i e_i^T+4 e_j e_j^T`; mixed terms cancel. Each coordinate occurs in
`r-1` supports, hence `W^T W=4(r-1)I_r`.

Consequently `U=W/[2 sqrt(r-1)]` has orthonormal columns, and
`A=WW^T/[4(r-1)]=UU^T` is a nonzero symmetric orthogonal projection with
rank exactly `r` and top singular value one of multiplicity `r`. Since
`U=V`, these are properly paired full top singular bases. Its entries are
rational. No numerical multiplicity decision is needed.

The signed-coordinate-permutation group acts transitively on the root set:
a coordinate permutation chooses the support and independent sign changes
choose both signs. On the root labels this becomes an ordinary permutation
matrix `P_g`, containing only zeros and ones. With the declared convention
`P_g e_w=e_(g w)`, its row action is
`(P_g W)_w=(g^-1 w)^T=w^T g`, so `P_g W=Wg`. Orthogonality of `g` then
gives `P_g A P_g^T=A`. This verifies the direction of the inverse and the
transpose, as well as simultaneous transitivity on both axes; a signed
matrix on the original `r` coordinates has not been incorrectly substituted
for an allowed permutation on the `n` measurement labels.

To check balance-map injectivity, `diag(UKU^T)=0` is equivalent to
`w^T K w=0` on every root. For `e_i+e_j` and `e_i-e_j` these equations
give `K_ij=0` and `K_ii+K_jj=0`. For each `i`, the existence of two other
distinct indices `j,k` gives
`2K_ii=(K_ii+K_jj)+(K_ii+K_kk)-(K_jj+K_kk)=0`. Thus `K=0`, including
all diagonal entries. The stated `r>=3` hypothesis is necessary for this
particular deduction; for `r=2`, `diag(1,-1)` lies in the kernel, and that
case is explicitly excluded. The first diagonal component alone is
injective, so the full paired map is injective.

Transitive optimality gives value `n`, also directly attained by
`X=Y=W/sqrt(2)`: every row has norm one and lies in the projection's range.
Its squared Frobenius norm is `n`, so its value is `n`. The scalar balance
weight is `H_0=(n/r)I_r=2(r-1)I_r`; inserting it into `U H_0 U^T`
gives `WW^T/2`, whose diagonal is one. F1 gives uniqueness and a lower
bound `r` for every optimum. The displayed strategy has span `r`, proving
the exact minimum dimension. In particular, the unique balance weight
classifies all optimal labeled Gram data, not merely invariant optima.

## F2R — Root-frame-rigidity implication and assembly: PASS

The route lists `GROTHORB.balance-rigidity` and
`GROTHORB.transitive-optimum`. F1/F1R review the former exact statement and
implication above; the repaired latter statement has hash
`sha256:3595380193737509977c85f3b2806810291bba8218e68de229adb35cb6230ab5`.
The two direct algebraic steps in RF-1 and RF-3 establish the claimed
tightness and spanning/injectivity. RF-2 establishes the symmetry needed to
apply the listed transitive premise, so the short route implication is
supported by its full proof even though it abbreviates that check.
Combining these exact inputs gives the target projection, symmetry,
optimum, uniqueness, and minimum-dimension conclusions. No unregistered
dimension-minimality hypothesis is required.

## F3 — Exact finite checks: reproduced within their finite scope

The reviewer read the full checker and saved record and independently ran:

```text
python3 -B grothendieck-group-orbit/tools/check_balance_rigidity.py
```

This fresh review run on 2026-09-07 used Python 3.9.6, exited zero, and
reported `all assertions passed`. The code uses `fractions.Fraction` for
matrix arithmetic and rational elimination; its inspected assertions do not
depend on a floating-point rank tolerance. These were supporting checks of
the finite examples, not the source of the universal proofs in F1 and F2.

| Example | Settings `n` | Top rank | Balance-map rank | Kernel dimension | Checked strategy rank | Objective |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `I_3-J_3/3` | 3 | 2 | 3 | 0 | 2 | 3 |
| `I_3` | 3 | 3 | 3 | 3 | 1, with endpoint rank 2 | 3 |
| root frame `r=3` | 12 | 3 | 6 | 0 | 3 | 12 |
| root frame `r=4` | 24 | 4 | 10 | 0 | 4 | 24 |
| root frame `r=5` | 40 | 5 | 15 | 0 | 5 | 40 |

The root checks verify a transitive orbit of size `n` under the generating
permutations, invariance under each generator, projection and exact rank,
quadratic-form coefficient-map rank, and the explicit unit-diagonal Gram
matrix attaining `n`. The saved author's run gives the same mathematical
results. The reviewer additionally checked the two elementary examples
symbolically: the simplex coefficient determinant is `-16`, and the
identity endpoint has a displayed rank-two Gram factor while the all-ones
matrix has a rank-one factor. The theorem does not depend on extrapolating
these examples to arbitrary `r`.

## Provenance and limitations

Raw SHA-256 values at inspection time:

```text
sha256:b88ffdd3b086a557912ec42bc37e53d6ec94ab3054d7a4a770f7207f06077cdf  grothendieck-group-orbit/artifacts/balance-rigidity-20260907.md
sha256:e0d1bd4f36d796eb7577534262be2662bcdfb55501d8504644f548e64be4811d  grothendieck-group-orbit/artifacts/root-frame-dimension-20260907.md
sha256:a4fe9043d6047fd2dad10fe85367d6ed135ca767d7dfe3c50a618078c96fb5a9  grothendieck-group-orbit/artifacts/balance-rigidity-exact-check-20260907.txt
sha256:fadcd7cedfe89ba4eddf22de3653a6a0206344086303c3d30cc146412bc7a9d9  grothendieck-group-orbit/tools/check_balance_rigidity.py
sha256:c945a3281b3183b1caa7322fa9558a73cf0749a770bb17078252f6856d30707c  grothendieck-group-orbit/proof-dag/nodes/GROTHORB.balance-rigidity.yaml
sha256:2ef9e79c9565fa5d2296b94cf43dc0e591c6c7bc7b390970f0d86fc3a0a6cc66  grothendieck-group-orbit/proof-dag/nodes/GROTHORB.root-frame-dimension.yaml
```

All four exact mathematical targets pass. The reports establish real-vector
statements under the written nonzero, transitive, and `r>=3` hypotheses.
They do not establish novelty, a complex quantum-dimension minimum, or
minimality of the quadratic number of settings. No solver labels or numerical
rank decisions were used to certify a universal theorem. No adverse evidence
or prior failed statement was removed, and no node was edited by this reviewer.
