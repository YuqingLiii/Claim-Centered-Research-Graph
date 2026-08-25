# Fresh hostile Rule-7 review — finite `s=6` six-operator occurrence algebra

Date: 2026-07-22  
Reviewer: fresh independent instance; did not author the candidate mathematics or code  
Controlling canonical node:
`KSUM.B4b.L3.ALT.hidden-frequency-mask.critical-endpoint.ALT.induced-packet-occurrence-pencil-classification`  
Reviewed artifact:
`ksum/artifacts/ksum_L3_uniform_occurrence_algebra_candidate_falsifier_20260722.md`

## 1. Formal verdict

**PASS / STRICTLY SCOPED PASS.**

No mathematical or provenance defect was found in the submitted finite `s=6` claim.  This review
independently verifies, over `Q`, the complete occurrence-only six-operator object at

\[
 (s,a,d,r,m)=(6,36,25,6,900),\qquad \theta=(893,6,1).
\]

The exact licensed result is:

1. the full and block-stabilizer James quotients have dimensions `30` and `105`, their stacked
   maps have shapes/ranks `60 x 30 / 27` and `186 x 105 / 90`, and their kernels have dimensions
   `3` and `15`;
2. the complete standard occurrence multiplicity is therefore `C_6=15-3=12`, with no favorable
   copy selected or omitted;
3. the marked quotient has dimension `199`, and the three relative-JM corner projectors resolve
   all twelve source columns exactly;
4. all six `12 x 12` rational forms are exactly PSD, with ranks

   \[
   (T1,TV_{35},M1,MV_{35},B1,BV_{35})=(12,12,8,12,10,12);
   \]

5. the three same-corner commutators vanish, while every one of the twelve different-corner
   commutators has exact rank `6`;
6. the common commutant has dimension `2`; the center has two primitive rational idempotents of
   ranks `1` and `11`; exact bicommutant and word-closure dimensions both equal `122`; and

   \[
   \boxed{\mathcal A_6\cong M_1(\mathbb Q)\oplus M_{11}(\mathbb Q)};
   \]

7. both simple blocks are split over `Q`, not merely after a field extension.

The submitted package therefore supplies a finite operator-algebra counterexample to the old
registered `Q^3 direct-sum M_8(Q)` candidate, in addition to the already reviewed formula-level
counterexample `C_6=12 != 11`.

This PASS does **not** complete the controlling node.  That node asks for complete physical
NO/YES, left/right, marked-status, path, and transfer pencils.  This review licenses no `s=7`
operator algebra, no replacement all-`s` operator-algebra law, no alphabet or Pieri assembly, no
physical transfer or feasibility statement, no attenuation, no numerator or denominator bound,
no query bound, and no exponent improvement.  The canonical node remains **OPEN**.  Per
commission, this reviewer made no canonical/shared DAG edit.

## 2. Blind chronology and immutable evidence

Before opening, grepping, hashing, or executing the target artifact, target checksum, target
scripts, target outputs, or mutable canonical `s=6` numbers, the reviewer read the two shared
protocols in full and used only the already reviewed `s=4`, `s=5`, and uniform multiplicity
packages.  The hostile baseline was then sealed at

`ksum/artifacts/ksum_L3_uniform_occurrence_algebra_candidate_falsifier_rule7_hostile_blind_baseline_20260722.md`,
SHA-256
`39A0A682585991217B74AD948A84B0DE43244F32A6D77FAD337F3164FA174258`.

The sealed baseline preregistered the types, the `105 -> 186` and `30 -> 60` James gates, kernel
dimensions `15/3`, `C_6=12`, every six-form/commutant/center/bicommutant/splitness gate, the
`s=4/s=5` regressions, and the strict `s=7` firewall without choosing an algebra answer.

The first complete regression exposed one reviewer-side transcription error in that sealed prose:
the reviewed `s=4` `M,eta=1` form has rank `2`, not `4`.  The baseline remains byte-immutable, and
a pre-target erratum was archived at

`ksum/artifacts/ksum_L3_uniform_occurrence_algebra_candidate_falsifier_rule7_hostile_blind_baseline_precomparison_erratum_20260722.md`,
SHA-256
`C2DF90CDC888CCB7B85844B5F4E071433AA83DE08433897372CD7B81412A1928`.

The independent source itself produced the correct rank two before target access; all other `s=4`
and all `s=5` regression gates passed.  This was a baseline transcription error, not a proposer
defect and not an `s=6` answer-directed repair.

The final pre-comparison independent evidence was sealed as follows:

| independent evidence | SHA-256 |
|---|---|
| self-contained exact reducer `ksum/artifacts/ksum_L3_s6_occurrence_rule7_independent_exact_20260722.py` | `B79C24DA1708D7A08B09D1B469D1FA6842992366E7F63BCAC31AFE016E1C6DE3` |
| full blind JSON | `473A520EC29174E74D8253254275F3A83D8B0A85E4D2B7091595E68F3155088A` |
| blind summary JSON | `F56C17F9D7FD4C87A5B9CC9234B8DAABE639B99C3DA9D74DA1F7BA931768CDE0` |
| blind stdout | `D20017B428C1EE15CA7BA157FF110DE37C84D50468D7A41CBE39D211E7AF7FA8` |

The reducer imports no project reducer and reads no proposer package.  It independently implements
compact integer-partition orbit catalogues, James maps, full-to-distinguished embedding, marked
refinement, the literal relative transposition sum, all six rational forms, exact rational
centralizers and bicommutants, CRT central idempotents, and a modular word-span lower bound.

Only after the script and outputs had been hashed did the reviewer open the target checksum first.
The checksum package has SHA-256
`C6388548058B2FD3B34F4BCB9948294C4C385A6CF980C45F4FCB2D768CE3E3FF`,
and all eleven listed target files rehash exactly.

## 3. Independent finite reconstruction

### 3.1 Source, quotient, and multiplicity dimensions

Put

\[
 H=S_{25}^{36},\qquad K=H\rtimes S_{36},\qquad
 K_0=H\rtimes S_{35},\qquad U_\theta=(S^\theta)^H.
\]

The independent compact orbit catalogue produces:

| quotient | source dimension | James targets | stack rank | kernel dimension |
|---|---:|---|---:|---:|
| full `K` | 30 | `1,2,4,7,12,19,15` | 27 | 3 |
| block stabilizer `K_0` | 105 | `2,5,11,21,38,64,45` | 90 | 15 |

Here the first six targets are the keep maps and the last is the merge map.  Every matrix is
integer, every nullspace residual is zero, and the full quotient embeds into the distinguished
quotient with rank `30`.  Because

\[
 \operatorname{Ind}_{S_{35}}^{S_{36}}\mathbf1
 \cong \mathbf1\oplus V_{36},
\]

the complete multiplicity space

\[
 Z_6=\operatorname{Hom}_{S_{36}}(V_{36},U_\theta)
\]

has dimension `15-3=12`.  The selected isotypic carrier has dimension `35*12=420`.

An independent low-tail SSYT count gives

\[
 \dim U_\theta=111{,}861{,}360,
\]

and the three marked-child invariant dimensions are

\[
 (111{,}861{,}360,\ 16{,}313{,}115,\ 3{,}838{,}380).
\]

The exact hook dimensions are

\[
 f^\theta=551{,}887{,}031{,}663{,}585{,}280,
\]

\[
 (f^{\kappa_T},f^{\kappa_M},f^{\kappa_B})=
 (547{,}589{,}748{,}534{,}481{,}952,
 3{,}581{,}073{,}780{,}074{,}336,
 716{,}209{,}349{,}028{,}992),
\]

and the three children sum exactly to `f^theta`.

### 3.2 Marked JM, forms, and normalization

Fix one point `x` in block zero.  The marked quotient is `Q^199`, with exact diagonal positive
orbit Gram.  The relative operator

\[
 J_x=\sum_{y\ne x}(x\ y):\mathbb Q^{199}\longrightarrow\mathbb Q^{199}
\]

is self-adjoint in that Gram.  The three contents and Lagrange denominators are

\[
 (c_T,c_M,c_B)=(892,4,-2),\qquad
 (D_T,D_M,D_B)=(793872,-5328,5364).
\]

The three polynomial images are eigenimages on all twelve embedded source columns, are mutually
orthogonal, and sum to the complete source.  No global projector identity on unrelated marked
permutation summands is used.

Under `S_35`,

\[
 V_{36}\downarrow S_{35}\cong\mathbf1\oplus V_{35},
 \qquad \dim V_{35}=34.
\]

Thus each raw matrix `H_(kappa,eta)` is a rational symmetric bilinear form on the same
twelve-dimensional `Z_6`.  The independent construction checks, entry by entry,

\[
 H^\mathbf1_\kappa+34H^{V_{35}}_\kappa
 =35{f^\kappa\over f^\theta}G
\]

for all three corners and both resolutions

\[
 \sum_\kappa H^\mathbf1_\kappa=G,
 \qquad
 \sum_\kappa H^{V_{35}}_\kappa=G.
\]

Independent rational LDL certificates establish exact PSD and ranks

| corner | `eta=1` | `eta=V_35` |
|---|---:|---:|
| `T` | 12 | 12 |
| `M` | 8 | 12 |
| `B` | 10 | 12 |

No floating eigenvalue or tolerance makes a decision.

### 3.3 Commutators, center, bicommutant, words, and splitting

The bilinear forms are not multiplied as operators.  Every algebra calculation uses

\[
 A_{\kappa,\eta}=G^{-1}H^\eta_\kappa
 \in\operatorname{End}_{\mathbb Q}(Z_6),
 \qquad A^TG=GA.
\]

All three same-corner eta pairs commute.  Each different-corner pair has exact rank-six
commutator.  The six-generator common-centralizer system has `144` unknowns, rank `142`, and
nullity `2`; its exact basis is commutative.

The exact rational bicommutant has dimension `122`.  A separate modular word closure at the good
prime `2147483647` reaches the same dimension.  Modular independence of integer-rescaled words is
a characteristic-zero lower bound, while the rational bicommutant is an exact upper bound, so the
word algebra equals the bicommutant over `Q`.

The independent checker constructs the primitive rational central idempotents by a squarefree
center generator and CRT.  They are idempotent, orthogonal, sum to `I_12`, are `G`-self-adjoint,
commute with all six generators, and have ranks `1` and `11`.  On these blocks the restricted
algebra dimensions are `1` and `121`, while the restricted commutants are both one-dimensional.
Therefore the blocks are the full rational matrix algebras themselves; there is no division-
algebra or field-extension obstruction:

\[
 \mathcal A_6=M_1(\mathbb Q)\oplus M_{11}(\mathbb Q).
\]

This is stronger than recognizing two clusters over `R` or `C`.

## 4. Exact post-seal comparison

The post-seal checker

`ksum/artifacts/logs_ksum_L3_s6_occurrence_rule7_review_20260722/postseal_compare.py`,
SHA-256
`AE11CCD7D467D07E6A79975EC40D3908BC5B621AA748EE8649EA7BF215C65CDB`,

imports no proposer or reducer code.  It reads the two exact JSON certificates and returns
`ALL_POSTSEAL_S6_RULE7_COMPARISON_GATES_PASS`.  Its output has SHA-256
`B3C9E819467370877E27D30E4D67CD66D32486711954A6D13DDD2A97CAA860DA`.

The independent and proposer gauges are not assumed equal.  The checker solves the exact
simultaneous-intertwiner equations for `T:1` and `M:1`; the solution space has dimension `2` and
contains an invertible rational matrix `X`.  It then verifies

\[
 X A_i^{\rm blind}=A_i^{\rm target}X
\]

for all six generators.  The metric twist

\[
 G_{\rm blind}^{-1}X^TG_{\rm target}X
\]

commutes with all six blind generators, as required for two invariant positive forms on the same
semisimple representation.

The checker transfers both blind central idempotents through `X`.  In target coordinates they
remain rational, `G_target`-self-adjoint, idempotent, mutually orthogonal, central for all six
operators, sum to `I_12`, and have ranks `1,11`.  Thus the comparison is exact simultaneous
conjugacy plus matrix-level central-block verification, not agreement of a list of scalar ranks.

Every proposer form additionally receives an independent rational LDL PSD certificate; both eta
resolutions, all three trace identities, `G`-self-adjointness, all fifteen commutators, and all
central-projector identities pass.

A fresh proposer rerun reproduces the archived `s=6` JSON semantically exactly after deleting only
the nondeterministic timing field.  Fresh `s=4` and `s=5` outputs likewise agree after deleting
only timings; the fresh `s=7` source output is byte-identical to the archived output.  The fresh
`s=6` JSON has SHA-256
`516AD5FE5C86ED0F54E74854418D6A6CF7E6B53E85C38B86A8B9A5FC3D06866E`.

## 5. Rule 7(a): per-display type and dimension audit

All parameters below are characteristic-zero parameters; for the finite operator claim,
`s=6,a=36,d=25,r=6,m=900,c=dim Z_6=12`.

| Target display or identity | Domain, codomain, and dimension audit | Result |
|---|---|---|
| (1.1), old candidate | `C_s` is an integer and `A_s` is interpreted as a unital `Q`-subalgebra of `End_Q(Z_s)`.  At `s=6` the intended natural carrier has proposed rank `3+8=11`, whereas `dim Z_6=12`. | Typed under the natural-module reading; old conjunction false. |
| (1.2), multiplicity formula | Equality of integers for legal `s>=4`: `dim_Q Hom_K(V_a,S^theta)=sum_(k=0)^(s-2)p(k)`. | Already reviewed uniformly and re-audited here. |
| (1.3), finite algebra | Isomorphism of unital associative `Q`-algebras inside `End_Q(Z_6)=M_12(Q)`.  The two natural blocks have ranks `1+11=12`. | Exact. |
| family parameter display | `a,d,r,m` are positive integers and `theta=(m-r-1,r,1)` is a partition of `m`; `m>=2r+1`. | Exact for all legal `s>=4`. |
| `H,W,W_0,U_theta` | `H<=S_m`; `W=H semidirect S_a<=S_m`; `W_0=H semidirect S_(a-1)<=W`; `U_theta=(S^theta)^H` is a `Q[S_a]`-module. | Block permutations normalize `H`; well defined. |
| induced-module identity | Isomorphism of `Q[S_a]`-modules `Ind_(S_(a-1))^(S_a)1 = 1 direct-sum V_a`; dimensions `a=1+(a-1)`. | Exact. |
| (2.1) | Equality of integer multiplicities/fixed-space dimensions inside the same `S^theta`; at `s=6`, `12=15-3`. | Exact. |
| (2.2) | Equality in the homogeneous degree-`m` symmetric-function/character ring.  Each `h_mu` is the character of the degree-`m` Young permutation module `M^mu`. | Four surviving determinant terms have signs `+,-,-,+`. |
| (2.3)--(2.6) | Scalar orbit-count and fixed-dimension identities.  Every two- or three-row composition sums to `m`; no map between unequal carriers is asserted. | Exact in the explicit low-tail range. |
| (2.7)--(2.9) | Equalities of integers involving ordinary partition numbers. | Exact; `C_6=12`, old value `11`. |
| James keep maps | `M^(m-r-1,r,1)^G -> M^(m-v-1,v,1)^G`, `0<=v<r`, for `G=K_0` or `K`.  Reduced shapes are the table in Section 3.1. | All integer coefficients and residuals exact. |
| James merge map | `M^(m-r-1,r,1)^G -> M^(m-r-1,r+1)^G`; reduced shapes `105->45` and `30->15`. | Exact. |
| full-to-distinguished embedding | `Q^30 -> Q^105`, sending each full orbit sum to its exact block-zero orbit fibers. | Rank 30; Gram weights partition exactly. |
| multiplicity embedding | `B:Z_6=Q^12 -> Q^105`, then marked refinement `Q^105 -> Q^199`. | Complete twelve-column source; both Gram identities exact. |
| relative `J_x` | Endomorphism `Q^199 -> Q^199` induced by the literal sum of `899` transpositions. | Exact and marked-Gram self-adjoint. |
| corner polynomials | Endomorphisms of `Q^199`, asserted as branch projectors only after composition with `B:Q^12->Q^199`. | Contents distinct; denominators nonzero; all source residuals zero. |
| eta restriction | `V_36 downarrow S_35 = 1 direct-sum V_35`, dimensions `35=1+34`; after tensoring with `Z_6`, eta sectors have dimensions `12` and `408`. | Exact. |
| six `H` forms | Elements of `Bil_Q(Z_6)`, hence rational symmetric `12 x 12` matrices. | Exact PSD/ranks. |
| eta trace identity | Equality in `Bil_Q(Z_6)`: both sides are `12 x 12`; factors `35` and `34` are separately accounted for. | Three full matrix residuals zero. |
| `A=G^-1H` | Endomorphism of `Z_6`, `Q^12->Q^12`; `G` is nonsingular and `A^TG=GA`. | Exact. |
| commutators | Endomorphisms `Z_6->Z_6`.  There are three same-corner and twelve different-corner unordered pairs. | Exact ranks `0` and `6`. |
| common commutant | Kernel in `End_Q(Z_6)` of a rational system on `12^2=144` unknowns. | System rank 142, kernel dimension 2. |
| bicommutant | Common commutant of the two-dimensional rational commutant inside `End_Q(Z_6)`. | Dimension 122. |
| modular word certificate | Reduction of rational `12 x 12` generators at a prime not dividing any denominator; independent reduced words give a lower bound on the characteristic-zero word dimension. | Hits rational upper bound 122. |
| central separator/projectors | The commutant is commutative, hence lies in its bicommutant; after `A=A''`, its rational self-adjoint separator is central.  Lagrange/CRT projectors are endomorphisms of `Q^12`. | Ranks 1 and 11; exact identities pass. |
| `s=7` source check | James maps only on quotient sources `Q^45` and `Q^165`, with kernels 4 and 23; `Z_7` has dimension 19. | No `s=7` marked operator or algebra is constructed. |

The normalizer issue is explicit: only permutations of the thirty-six equal blocks act on
`U_theta`; after marking a point in block zero, the remaining block group `S_35` normalizes the
marked base group.  No `f^theta`-dimensional Specht carrier is mistaken for the twelve-dimensional
multiplicity factor.

## 6. Rule 7(b): regime-complete identity gates

The new target is the genuinely matrix-valued `c=12` regime.  The review exercises, exactly:

- all twelve source columns, not a trace or selected copy;
- all three removable corners and both eta sectors of dimensions `1` and `34`;
- all six rational forms, six LDL PSD certificates, and all six ranks;
- both three-corner resolutions and all three eta trace identities as `12 x 12` residuals;
- all fifteen pairwise commutators;
- the complete 144-variable common commutant;
- primitive central idempotents, rational block ranks, restricted algebra/commutant dimensions;
- the rational bicommutant and an independent word-span lower bound; and
- exact simultaneous conjugacy between the blind and proposer families.

The same independent source reproduces the reviewed `c=4` and `c=7` regimes, including their
different rank and block patterns.  The already reviewed dense `c=1` toy remains frozen only for
the literal tabloid/marked-transposition mechanism.  The new `c=12` identities are reopened in
full, so no multiplicity, corner, eta, or algebra branch is tested only at aggregate level.

## 7. Rules 7(c)--(g) and hostile failure modes

### 7(c), anchoring ban

Satisfied by the immutable hostile baseline, pre-target erratum, pre-comparison script/output
hashes, and the chronology in Section 2.  The target filename was visible in a repository status
listing, but no target contents or target values were read before both seals.  The blind algebra
answer was not extrapolated from `s=4` or `s=5`; it changes both the commutator rank and central
decomposition patterns.

### 7(d), no frozen-input immunity

The reviewed `s=4`/`s=5` packages are used only for regression values and the already reviewed
orbit/James/JM mechanism.  The reviewed uniform formula is used only for source multiplicity.
Every `s=6,c=12` source, form, matrix identity, centralizer, center, bicommutant, word, and
splitness conclusion is independently rebuilt.  No earlier finite algebra pattern is load
bearing.

### 7(e), standing and target-specific failure modes

- **Dropped/extra normalization:** the factors `900`, `36`, `35`, `34`, `25`, full point orbit,
  `dim eta`, hook ratios, orbit sizes, and Gram raising are separated; both resolutions and all
  trace identities pass.
- **Type/dimension mismatch:** Section 5 audits every displayed operator identity on the complete
  twelve-dimensional multiplicity factor.
- **Undefined ranges:** `legal` for the uniform multiplicity formula means
  `s>=4,a=s^2,d=4s+1`; the finite algebra claim means only `s=6`.  No stability threshold is used.
- **Colored orbit substituted for a full central sum:** the orbit bases are exact invariant-space
  bases, while the eta formula comes from the full point sum.  No block-color surrogate replaces
  the `900`-point central sum.
- **Values hiding a broken derivation:** exact construction agreement is separated from the
  per-display formula/type audit.  The baseline's own rank transcription error was exposed rather
  than hidden by favorable output.
- **Wrong inner product/raw-form multiplication:** all adjoints use the exact orbit Gram, and all
  products use `G^-1H`, never raw `H`.
- **Favorable-copy selection:** the full-invariant subspace now has dimension `3`; all three
  directions are removed before retaining the complete twelve-dimensional complement.
- **Rank-only algebra classification:** commutant, center idempotents, restricted blocks,
  bicommutant, and word closure are all checked in addition to commutator ranks.
- **Floating spectral classification:** no floating eigenvalue or tolerance is decisive.
- **Complex versus rational splitting:** both rational central factors and the full rational block
  dimensions are checked; real/complex clustering is not substituted for `Q`-splitness.
- **Bad modular characteristic:** the target and blind word certificates use different good
  primes; denominator invertibility is checked, and the rational bicommutant supplies the upper
  bound.
- **Finite-to-uniform inference:** the finite `1+11` decomposition is not interpolated.
- **`s=7` leakage:** only source quotient/multiplicity data are computed; no six forms or algebra
  are built or inferred.

### 7(f), value versus formula

Four evidence layers are distinct.

1. The proposer rerun executes the submitted formulas and reproduces every deterministic field;
   only wall-clock timing changes.
2. The pre-target blind reducer constructs the same mathematical object without importing or
   reading proposer code.  It uses a separately written expanded-pair orbit catalogue, a different
   exact nullspace path, all-six centralizer equations, explicit rational CRT idempotents, and a
   different modular prime.
3. The post-seal checker proves exact simultaneous rational conjugacy of all six operators and
   transfers the complete central projector system, which is stronger than matching scalar
   invariants.
4. Sections 3 and 5 directly audit the printed James, JM, eta, Gram, centralizer, modular-word, and
   rational-splitting derivations.  Matching matrices alone would not repair an ill-typed formula.

Thus the independent construction verifies the finite values, while the human audit separately
verifies the printed route.

### 7(g), quantifier hygiene

In this review:

- `finite s=6 target` means only `(s,a,d,r)=(6,36,25,6)`;
- `corner` means exactly `T=(892,6,1)`, `M=(893,5,1)`, or `B=(893,6)`;
- `V_35` means the 34-dimensional standard `S_35` module;
- `same corner` means the three eta pairs, and `different corner` means the other twelve pairs;
- `occurrence algebra` means the unital `Q`-algebra generated by the six rational
  `G^-1H` endomorphisms on this one `Z_6`;
- `split over Q` means the rational algebra itself is the displayed product of full rational
  matrix algebras; and
- `s=7 check` means only the source James quotient and `C_7=19`.

No undefined `admissible`, `active`, `strict`, `taper`, or replacement stable range enters the
positive verdict.

## 8. Banked result, stopping point, and future direction

The finite `s=6` occurrence table, rank-six different-corner commutators, rational `1+11` central
decomposition, exact word/bicommutant equality, and `M_1(Q) direct-sum M_11(Q)` classification may
now be treated as reviewed input.  Together with the already reviewed formula, they decisively
kill the old registered joint quadratic/algebra candidate.

The source-only value `C_7=19` is a consistency gate and nothing more.  This review expressly
withholds an `s=7` occurrence algebra and every uniform operator-algebra theorem.

As a future direction only, the most promising exact certificate to generalize is the
two-generator centralizer system after removing the rational invariant line: one would seek a
partition-indexed support/connectivity argument forcing every solution of
`XT_s=T_sX, XM_s=M_sX` on the complement to be scalar.  That could certify all-`s`
irreducibility of a proposed complement if proved uniformly; the present finite ranks do not prove
it.
