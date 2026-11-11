# Independent review of the classical value, equality cases, and small shift

Date: 2026-09-07.
Reviewer: `/root/orbit_d3_envelope`, a separate Codex review agent using the
inherited model. The exact model version is not independently verified; this
is a same-model-family review with author-independent role separation for
the three results reviewed here, **not a fresh-context or cross-model review**.
The reviewer did not write, edit, or advise on the C1, C5, or C6 author proofs
or their checkers. Earlier in this task the reviewer authored the separate
D3 envelope computation; that result and its checker are not dependencies
or evidence for any finding in this report. Awareness of that related result
and the shared conversation are limitations on independence and are disclosed
rather than described as fresh-context independence.

## Scope and inspected materials

This review covers the exact current claims `GROTHORB.root-classical`,
`GROTHORB.root-classical-equality`, and `GROTHORB.root-small-shift`, and the
route implications `support-equality` and `discrete-gap`. It covers the full
root set with both antipodes, every integer r>=3, signed bilinear maxima,
all equality cases for the unshifted matrix, their unquotiented ordered-pair
count, and the stated closed small-shift interval. It does not review the D3
envelope, whole-interval linear conjecture, vector optima, physical dimension,
or novelty. The general proofs below do not use a small-r extrapolation.

The reviewer read the three canonical YAML files in full; the artifacts
`root-classical-value-20260907.md` (RC-1--RC-5),
`root-classical-equality-20260907.md` (RE-1--RE-7), and
`root-small-shift-proof-20260907.md` (S1--S4); both associated classical
checkers and their author run records; the current registration document;
the generated node index and graph; and both repository protocols. Complete
file hashes, exact command outputs, and exact statement hashes are frozen in
`grothendieck-group-orbit/artifacts/root-classical-review-rerun-20260907.txt`,
R1--R5. R5 records a concurrent append of unrelated C8/C9/C10 registrations;
the reviewed statements and mathematical inputs were unchanged at closeout.
In particular, the reviewed author proof hashes are:

| Artifact | SHA-256 |
|---|---|
| `root-classical-value-20260907.md` | `8ea014aa65b2af33bf5c15182eadec95d629d0970f8f816081b4497b6b6c3259` |
| `root-classical-equality-20260907.md` | `f0600088adda036abb502afaf59dcaf6202b70b9cdac7814d696cf072c80343e` |
| `root-small-shift-proof-20260907.md` | `137c49deea6f5a6f34259cb89b060ea198b7d4fe734c34ee52f4a1674df1d9b4` |

Statement hashes below were computed from parsed YAML with PyYAML 6.0.3,
using SHA-256 of UTF-8 `claim.strip()` or `implication.strip()`; they are
not hashes of a paraphrase or of the whole YAML file. Whole-file hashes
identify the input snapshot separately. Assessments and links may subsequently
change without changing the reviewed statement; changed statement text
requires a new applicable review binding.

## F1: GROTHORB.root-classical — PASS

Reviewed claim hash:
`sha256:5894fbd5f0998222db98bbe3cbef23b0a723716a30125952c2db60e748375fca`.

Exact claim:

> For every integer r>=3, let W contain all roots +/-e_i +/-e_j with i<j, n=2r(r-1), and A_r=WW^T/[4(r-1)]. Then the classical Bell value max_{s,t in {+1,-1}^n} s^T A_r t equals 2r(2r-1)/3.

I independently reconstructed the upper bound. Let c=4(r-1), z_s=W^T s,
and M=max_s ||z_s||. Cauchy--Schwarz gives z_s dot z_t<=M^2 and a maximal
diagonal pair realizes M^2, so beta_cl(A)=M^2/c. This depends only on the
positive Gram representation and is applied only to the unshifted matrix.

The identity ||z||=max_{||x||=1} x dot z reduces M to the root support
function. The sign set is finite and the sphere compact, justifying both
maxima and their interchange. Four signed roots over a pair of coordinates
contribute 2(|x_i+x_j|+|x_i-x_j|)=4 max(|x_i|,|x_j|); the factor four
correctly includes antipodal duplication. If a_i are sorted decreasing
absolute coordinates of a unit x, summing unordered pairs gives
h(x)=4 sum_i(r-i)a_i. Ties cause no double-counting problem: the pair in
positions i<j contributes a_i regardless of equality. With rho=(r-1,...,0),
Cauchy--Schwarz gives h(x)<=4||rho||, and x=rho/||rho|| attains it.
Thus M^2=16 sum_{k=0}^{r-1}k^2.

The stated explicit sign witness chooses s_(i,j,alpha,beta)=alpha. For each
fixed pair i<j, summing s_w w over its four roots gives 4e_i, hence W^T s=4rho.
The roots have no zero inner product with rho because its absolute
coordinates are distinct. The resulting diagonal objective equals the upper
bound, namely 16||rho||^2/[4(r-1)]=2r(2r-1)/3. This verifies existence,
normalization, and the bound for every integer r>=3 without a root-system
classification theorem or other unresolved premise.

I also inspected and reran `check_root_classical_value.py`. Its r=3,...,12
witness checks and exhaustive 4096-vector r=3 bilinear maximum passed (R1).
It correctly optimizes Alice separately for each Bob vector and uses exact
integers/Fraction. These runs check normalization and implementation; the
all-r verdict rests on the argument above. No defect requiring repair was
found. This node is route-free, so there is no separate route finding.

## F2R: GROTHORB.root-classical-equality/support-equality — PASS

Reviewed implication hash:
`sha256:81878c54dfe7e3b4aec018401e7be9c89d943429321013f5501611711ce02464`.

Exact implication:

> Equality in the sorted-coordinate support bound fixes the signed-sum direction to a signed permutation of rho, whose root inner products are nonzero; equality in the PSD bilinear bound identifies both signs.

The only listed unresolved premise is the base-value claim reviewed in F1.
To check the implication, let Q=||rho||^2 and L=4 sqrt(Q)>0. For any sign
vector u, its diagonal objective and the base maximum imply ||W^T u||<=L.
If (s,t) attains the maximum, z_s dot z_t=L^2. Equality in the norm product
bound forces both norms to equal L, and the positive Cauchy--Schwarz equality
forces z_s=z_t=z. This does **not** by itself imply s=t because W^T can
have a kernel; the author explicitly supplies the missing strictness step.

Set x=z/L. Both s and t yield x dot z_u=L. Their signed sums are bounded
above termwise by h(x), while the sorted-coordinate support bound is
h(x)=4 rho dot a<=L. Therefore all bounds are equalities. Euclidean
Cauchy--Schwarz with unit ||a|| and nonzero rho gives precisely
a=rho/sqrt(Q), including a single zero coordinate and distinct absolute
coordinates. Hence x=g rho/sqrt(Q), with g a signed coordinate permutation.
Any root orthogonal to x would require equal absolute values at two distinct
coordinates, which is impossible. Every support coefficient is thus nonzero.
The sum of nonnegative deficits |w dot x|-u_w(w dot x) is zero for u=s and
u=t; each deficit must vanish. Consequently both sign vectors equal
sign(w dot g rho), and in particular s=t. This handles every possible
maximizer and rules out kernel-related sign ambiguities at the maximum.

The converse and counting steps needed for the full parent claim are also
present in the assembled route proof RE-5--RE-6. A signed coordinate
permutation preserves the full root set, so changing variables in the root
sum proves W^T s(g rho)=4g rho from the explicit identity at rho. Such a pair
attains the base maximum. Applying W^T shows that equal sign patterns would
give equal orbit vectors, proving injectivity of the direction-to-pattern
map rather than assuming it. Distinct absolute coordinate values have r!
placements and the r-1 nonzero entries have 2^(r-1) sign choices. Only the
zero-coordinate sign is redundant; the stabilizer has exactly two elements.
The route therefore supplies the converse and the exact count as well as
the necessity argument highlighted in its implication text.

The supporting base claim has passed F1, and the remaining facts are proved
inside the route artifact. There is no reliance on the D3 result, an unlisted
equality hypothesis, or a global injectivity assumption for W^T. The
implication proves the currently stated full target.

## F2: GROTHORB.root-classical-equality — PASS

Reviewed claim hash:
`sha256:d6fbde6d93fc9c2ba39009177571a2b05dd268f94b21da4250d82c8fdc13ba3a`.

Exact claim:

> For every r>=3 and the full D_r root projection A_r=WW^T/[4(r-1)], every pair attaining beta_cl(A_r) has s=t with s_w=sign(w dot g*rho), rho=(r-1,r-2,...,0), for a signed coordinate permutation g; conversely all such pairs attain the optimum. The number of distinct maximizing sign pairs is 2^(r-1)*r!.

The premise F1 and complete route finding F2R establish necessity,
sufficiency, and exact enumeration for every integer r>=3. The count is for
ordinary ordered pairs of full sign vectors. Simultaneous global sign change
produces a different pair and is included; no antipodal, group-action, or
Alice/Bob quotient is taken. A root involves two different coordinates, so
the sole zero coordinate of rho introduces no undefined sign. These checks
address the potential sources of a missing factor two or non-diagonal
maximizer.

I inspected and reran `check_root_classical_equality.py` with its imported
base checker frozen. For r=3,4,5 it checked every signed permutation,
respectively producing 24, 192, and 1920 orbit vectors/sign patterns, each
with group multiplicity two and exact image 4g rho. Its complete r=3 Bob
enumeration returned exactly the predicted 24 vectors; every maximizing
Bob vector had all nonzero Alice coefficients and unique Alice=Bob (R2).
Therefore the finite check does cover all bilinear equality pairs at r=3,
including possible Alice ties. The universal completeness and count are
proved by F2R, not inferred from those ranks. No defect requiring repair was
found.

## F3R: GROTHORB.root-small-shift/discrete-gap — PASS

Reviewed implication hash:
`sha256:ff5cd598382d45f215c5a4f16c8ed50ab0b964215afeb6e6e9684b171107945c`.

Exact implication:

> All maximizing unshifted pairs are diagonal and every unshifted score lies in (1/(r-1))Z, so off-diagonal pairs lose at least 1/(r-1). Bounding the shift advantage by 2n*lambda preserves diagonal optimality throughout the stated interval.

The listed premises are exactly the base-value and equality claims checked
in F1 and F2. I independently checked the lattice without a spectral or
small-r assumption. Each coordinate of W^T s sums 4(r-1) signs and is
therefore even; the same is true of W^T t. Their dot product is divisible
by four. Dividing by 4(r-1) puts every unshifted score in
(1/(r-1))Z. The maximum C=2r(2r-1)/3 belongs to this lattice because it is
an attained score; independently C(r-1)=2r(r-1)(2r-1)/3 is integral by the
three residue classes of r modulo 3. This use of a lattice depends on exact
parity, not floating-point separation.

The equality premise rules out s!=t at score C, so every such pair has
s^T A t<=C-1/(r-1). For a fixed diagonal maximizing pair u, shifting gives
C-n lambda. An arbitrary diagonal pair cannot exceed that. For s!=t the
advantage relative to that diagonal witness is at most

```
-1/(r-1) + lambda*(n-s dot t)
 <= -1/(r-1) + 2n*lambda.
```

Here lambda>=0 and s dot t>=-n justify the direction of the inequality.
It is nonpositive for lambda<=1/[2n(r-1)]. Thus every pair is bounded by
the diagonal witness on the whole claimed real interval. The right
endpoint is included by a non-strict inequality. The phrase "preserves
diagonal optimality" means that a diagonal witness remains optimal, not
that all shifted optimizers must remain diagonal; extra ties are permitted.

The route has all needed premises, and both have passed this review. It
does not use the stronger orbit count except insofar as the full equality
premise must be assembled; that full premise has also passed. The route is
a sufficient-interval argument and makes no unsupported maximality claim.

## F3: GROTHORB.root-small-shift — PASS

Reviewed claim hash:
`sha256:9a872e7354e9445bc8dd2722bd106fc849de9b3b7649eedb9159a607194fd688`.

Exact claim:

> For every r>=3, n=2r(r-1), and A_r the full D_r root projection, beta_cl(A_r-lambda I)=2r(2r-1)/3-n*lambda for every real lambda satisfying 0<=lambda<=1/[2n(r-1)].

The reviewed premises F1/F2 and implication F3R prove the exact equality
with an explicit attaining diagonal family for all integer r>=3 and every
real lambda in the stated closed interval. Substituting n=2r(r-1) gives
the equivalent endpoint 1/[4r(r-1)^2], and r=3 gives 1/48 as stated in
the author artifact. Both lambda=0 and the right endpoint were checked in
the algebra. No continuity extrapolation from rational test points is
needed. No claim beyond this interval, no complete shifted equality
classification, and no D3-specific result enters this finding.

No defect requiring repair was found. No additional solver run is required
for this general elementary proof; the reviewer replays of the supporting
classical witnesses and equality checker are recorded in R1/R2 and do not
replace the general argument.

## Review verdict and limitations

F1, F2R, F2, F3R, and F3 all pass for their exact bound statements and
the frozen assembled inputs. This is a mathematical author-independent
review within one model family and a shared task context, with the
non-fresh-context limitation stated above. It is not a proof-assistant
formalization, cross-model verification, or novelty review. The reviewer
changed no node, assessment, route, or author artifact; applying the review
to research-state promotion remains a separate protocol update by the parent.
