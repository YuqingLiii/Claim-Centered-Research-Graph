# Independent spectral-bound and extremizer-classification review

Date: 2026-09-07.

Reviewer: Codex GPT-6, independent delegated reviewer
`/root/orbit_existing_audit`. The reviewer did not author the 2026-08-29 proof
artifacts or the reviewed node statements and made no node edits. This review
was conducted in a separate delegated context from the agent coordinating the
exploration. It is a same-model-family independent argument audit, not a
different-model or external human review. No webpage ChatGPT session was used.

Scope: the eight nodes and two route implications listed below, restricted to
the real-vector spectral bound, its equality conditions, and the resulting
spectrahedral classification. The retired commutant-classification route,
R/C/H decomposition, quantum measurement realization, wreath-product results,
new exploration nodes, novelty, and literature priority were not reviewed.
The reviewer treats row and column counts as positive integers, as required
by the normalization formulas in the dossier.

This is an immutable report on the statements identified below. A repair
requires a new hash-bound review or addendum; the proposed repairs here have
not been installed or separately promoted. PASS means the specified
mathematical obligation passed the reasoning in this report. It is not an
automatic DAG promotion. FAIL means the complete exact obligation did not
pass; it does not refute correctly scoped substatements.

## Inputs and statement binding

The reviewer read `DAG_PROTOCOL.md` and `FILE_PROTOCOL.md` in full; both proof
artifacts in full; all eight node YAML files, including their assessments,
routes, and events; `grothendieck-group-orbit/proof-dag/GRAPH.mmd`; the reviews
README; and the implementation of `claim_hash` and its loader in
`tools/proof_dag_schema.py`. The generated graph was used for orientation,
not as mathematical evidence. No solver was run.

All paths in this report are relative to the reviewed temporary root:

```text
/private/tmp/grothorb-exploration-20260907-hLCZqw
```

Target hashes were computed by loading the YAML with
`proof_dag_schema.UniqueKeyLoader` and calling
`proof_dag_schema.claim_hash` on the exact decoded `claim` or `implication`.
That implementation changes CRLF to LF, strips leading/trailing whitespace,
and hashes UTF-8 bytes; it does not collapse internal whitespace. All hashes
below use that normalization. The node paths are
`grothendieck-group-orbit/proof-dag/nodes/<node-id>.yaml`.

| Finding | Exact target | Reviewed hash | Verdict |
| --- | --- | --- | --- |
| F1 | `GROTHORB.spectral-upper.claim` | `sha256:5eb3c78d20d4431b223f760c4edbe64239e63fc50894feb6e0ec20a8e98adea1` | PASS |
| F2 | `GROTHORB.balanced-criterion.claim` | `sha256:69783511b8a93069122c7b208ea7a31478b0e03d2e8a2e3075f5c3b044b69a5b` | PASS |
| F3 | `GROTHORB.invariant-projector.claim` | `sha256:bc24d83480c8b4750c42f0f7e8c52e5e4727bde1ee53323843606c5ba870e1e5` | PASS |
| F4 | `GROTHORB.equality-characterization.claim` | `sha256:b0247e9891b03886886050461c971ee8f44b8535257deeeaacea7c5da1d2184e` | FAIL: unqualified minimum when the feasible set is empty |
| F5 | `GROTHORB.transitive-optimum.claim` | `sha256:565819f106d2a2e65e242aef32d136af1f3dbf2f8c3dc2be0d042471251afef1` | FAIL: zero rectangular matrix attainment wording |
| F5R | `GROTHORB.transitive-optimum.routes.balanced-top-space.implication` | `sha256:84d6b925e3477ddd0553add534f2c36b1cceb556ef6b55da52f156802c4ac6c8` | FAIL as a route proving its exact current target; piecewise implication text itself is valid |
| F6 | `GROTHORB.extremizer-classification.claim` | `sha256:5cbc9e0d89f69f0929510b7592b1480185c5efcf320a3b619d3da4f41c5d02e3` | PASS mathematically; current DAG assembly caveat below |
| F6R | `GROTHORB.extremizer-classification.routes.spectrahedral-classification.implication` | `sha256:d82439273a03af85a1bbb295a4a27d5e45f493c3b1ec1f10c2caeb73035bf547` | PASS as a conditional implication; current DAG assembly caveat below |
| F7 | `GROTHORB.counterexample.claim` | `sha256:476117bcd924f0401966beadaab247fb8a83d20d90d8c33e4c946a141c61aa9f` | PASS |
| F8 | `GROTHORB.noninvariant-extremizer.claim` | `sha256:1bb2ea6fec7e1f1d5c420544a40a389aad09f2c72b88890235297935ed8faad6` | PASS |

These verdicts bind the decoded statements, not every unrelated sentence or
historical assessment in the files. Raw-file SHA-256 digests of the inspected
supporting material are recorded in the provenance appendix.

## F1 — Universal real-vector bound: PASS

Source inspected: balanced-rank draft, GO-T1.

For a feasible strategy with row matrices `X` and `Y`, direct expansion gives
`sum_ij A_ij <x_i,y_j> = Tr(X^T A Y) = <X,AY>_F`. The unit-row constraints
give `||X||_F=sqrt(m)` and `||Y||_F=sqrt(n)`. Frobenius Cauchy--Schwarz gives
`<X,AY>_F <= ||X||_F ||AY||_F`. Applying the operator bound to each column
of `Y` gives `||AY||_F <= ||A||_op ||Y||_F`. The desired inequality follows
for each strategy and hence for its supremum. There is no square-matrix,
rank, or nonzero assumption needed here; `A=0` gives zero on both sides.

The unrestricted vector dimension introduces no gap. There are only `m+n`
vectors, and their joint Gram matrix is PSD with unit diagonal. This fixed
finite-dimensional set is compact: every entry has magnitude at most one,
and the PSD and diagonal conditions are closed. The objective is linear in
that Gram matrix, and every such matrix has a real factorization of width at
most `m+n`. Thus an optimal strategy exists. This observation also justifies
interpreting saturation of the supremum as attainment when needed below.

## F2 — Balanced top-space construction: PASS

Source inspected: balanced-rank draft, GO-T2; classification note, GOC-T1.

For `sigma>0`, the top eigenvalue `sigma^2` of `A^T A` and `A A^T` has the
same multiplicity `r>=1`. Given an orthonormal basis `V` of the right space,
`U=AV/sigma` is an orthonormal basis of the left space and satisfies both
pairing equations. No simplicity of the top singular value is required.

The two balanced projector diagonals make
`X=sqrt(m/r) U` and `Y=sqrt(n/r) V` unit-row matrices. The trace is
`sqrt(mn)/r * Tr(U^T A V) = sigma sqrt(mn)`. All rows are nonzero before
normalization because `r/m` and `r/n` are positive. A common orthogonal
change of paired bases preserves these formulas and the attained value.

Scope limitation: this finding proves the stated sufficient condition. It
does not turn constant diagonals of the full top-space projectors into a
necessary condition for saturation. General necessity is the existence of a
possibly nonscalar feasible `H`, as analyzed in F4. GO-T5's section heading
must not be cited as a stronger necessity theorem.

## F3 — Transitive invariant-projector lemma: PASS

Source inspected: balanced-rank draft, GO-T3.

Commutation with `P_g` gives `P_g Pi P_g^T=Pi`. For a permutation taking
point `i` to point `j`, this equality identifies `Pi_ii` and `Pi_jj`.
Transitivity therefore makes the diagonal constant. Since an orthogonal
projector has eigenvalues zero and one, `Tr(Pi)=rank(Pi)=r`, so each diagonal
entry is `r/m`. The argument includes `r=0` and does not assume an
irreducible representation. Finiteness is harmless and no averaging is used.

## F4 — Equality parametrization passes; exact minimum sentence fails

Sources inspected: classification note, GOC-T1 through GOC-T3.

The equality characterization itself is correct for every nonzero real
matrix and every positive top multiplicity. To check the potentially
degenerate case without an informal equality-rule shortcut, write

```text
sigma^2 ||Y||_F^2 - ||AY||_F^2
  = sum_k y_k^T (sigma^2 I - A^T A) y_k,
```

where `y_k` are columns of `Y`. Each summand is nonnegative. Their sum
vanishes exactly when each column belongs to the kernel of
`sigma^2 I-A^T A`, including all and only the full top right singular space.
Thus `Y=VT`. Equality in Frobenius Cauchy--Schwarz is positive
proportionality because the attained value `sigma sqrt(mn)` is positive.
Norms force `X=(sqrt(m/n)/sigma) AY=sqrt(m/n) UT`. Neither vector matrix
vanishes, so this division and the equality condition are legitimate.

The two row-normalization conditions are exactly
`diag(V H V^T)=1_n` and `diag(U H U^T)=(n/m)1_m`, with `H=TT^T`.
Conversely, a feasible PSD `H` has a real factor `T`; the same formulas
give unit rows. Taking the trace of the right diagonal equation gives
`Tr(H)=n`. Substitution in the objective gives `sigma sqrt(mn)`. This
establishes both directions, including singular feasible weights.

The defect is confined to the final sentence in the exact node claim:

> the minimum real vector dimension among such strategies is the minimum rank of a feasible H.

The claim quantifies over arbitrary nonzero `A`. Such strategies and feasible
weights need not exist. For the already registered `A=diag(2,1)`, `r=1` and
`U=V=(1,0)^T`. Every scalar weight has diagonal `(h,0)`, which cannot equal
`(1,1)`. Thus the spectrahedron is empty and there is no minimum real vector
dimension or minimum feasible rank under the usual meaning of minimum.
GOC-T3 correctly supplies the phrase “Whenever it does” before discussing
strategies, but that restriction was lost in the node claim. The report does
not interpret this imprecision as refuting the equality parametrization.

Minimal repair: replace the final clause with “if the feasible set is
nonempty, the minimum real vector dimension among such strategies is the
minimum rank of a feasible H.” An alternative is to define both quantities
as `+infinity` when the feasible set is empty, but that convention must be
explicit. This is a FAIL for unconditional completion of the exact reviewed
claim, with PASS for its equality-iff part and its conditional dimension
formula. No revised statement hash is certified by this report.

When the feasible set is nonempty, `1<=rank(H)<=r` because `Tr(H)=n>0`.
The attained integer ranks form a nonempty finite set, so the minimum exists.
A width-`d` factor exists exactly for `d>=rank(H)`. Moreover the maps `U` and
`V` have full column rank, so the realized joint vector span has exactly
`rank(T)=rank(H)` dimensions. This proves the conditional formula, including
the distinction between padded ambient dimension and the actual span.

## F5 — Transitive optimum value passes; zero-case construction clause fails

Sources inspected: balanced-rank draft, GO-T4; classification note, GOC-T4;
the transitive-optimum claim and both route sources.

From `P_g A Q_g^T=A` one gets `P_g A=A Q_g` and invariance of `A A^T`
under `P_g`, and of `A^T A` under `Q_g`. For `A!=0`, their respective
top-eigenspace orthogonal projectors commute with the actions. F3 gives
diagonals `r/m` and `r/n`; F2 gives a saturating unit-vector strategy; F1
gives the matching upper bound. This proves the value and the normalized
paired-basis construction for nonzero matrices at every positive multiplicity.

For `A=0`, the value statement also holds and every feasible strategy is
optimal. The exact claim nevertheless states, without a nonzero restriction,
that the value is “attained by normalized rows of paired top left and right
singular bases.” With a rectangular zero matrix the full top left singular
space is `R^m` and the full top right singular space is `R^n`. When `m!=n`,
these spaces cannot have bases with a common column count, as required by
the dossier's definition of paired bases.

For example, take `A=0` of size `1 by 2`, with the two-element group acting
trivially on the single row and transitively on the two columns. All stated
equivariance and transitivity hypotheses hold, but the full zero-singular
spaces have dimensions one and two. A thin SVD would select only a subspace
on the larger side and would not be the defined pair of full top spaces;
an arbitrary such choice can also have a zero row, so normalization is not
an automatic repair.

Minimal repair: retain the value equality for all `A`; say that for `A!=0`
it is attained by normalized rows of paired top singular bases, while for
`A=0` every feasible strategy is optimal. The exact reviewed claim fails the
well-posed construction requirement. Its optimum-value theorem and its
nonzero construction pass. This finding does not claim a counterexample to
the optimum-value equality.

## F5R — Balanced-top-space route: exact-target mismatch

The exact route implication explicitly separates `A!=0` from `A=0`, and its
piecewise mathematical content passes the arguments in F1–F3 and F5. Its
listed nonzero proof premises are sufficient; the zero case is direct.

Nevertheless, the protocol requires a route to prove the parent claim
actually written. Its zero branch proves that every feasible strategy is
optimal, which does not supply the undefined paired-full-basis construction
asserted by the unconditional parent. Therefore the complete route obligation
to the present target receives FAIL. This is a target mismatch, not a
counterexample to the displayed piecewise implication. After the exact
parent repair in F5, the already written implication contains the needed
case split, but the repaired parent must receive its own hash-bound review.

## F6 — All-extremizer spectrahedral classification: PASS

Sources inspected: classification note, GOC-T1 through GOC-T6, limited to
the equality, spectrahedron, symmetry-action, and Gram-equivalence arguments.

The claim restricts to nonzero transitive equivariant matrices. In this
regime F5's nonzero argument gives saturation, and
`H_0=(n/r) I_r` is feasible, so the nonemptiness defect from F4 does not
arise. Every optimum is a spectral-bound equality strategy, and the verified
iff argument of F4 gives every such strategy from a feasible `H` and its
factorization. The minimum-rank argument in F4 applies because the feasible
set is now explicitly nonempty.

For the stated quotient, stack the vector matrices as `Z=B T`, where
`B` is the vertical stack of `sqrt(m/n) U` and `V`. The full labeled
row-vector Gram matrix is `Z Z^T=B H B^T`. It includes both parties'
individual Gram blocks and their cross block. Conversely,
`H=V^T (Y Y^T) V`, so different weights cannot produce the same full Gram
data in the fixed paired basis. Equal Gram matrices of finite real vector
families yield an isometry between their spans, which extends to an ambient
orthogonal map after zero padding to a common dimension. Thus each feasible
`H` gives one equivalence class under this convention, and all classes are
obtained. This is the zero-padding convention explicitly stated in GOC-T3.

For a change of paired bases `U'=UR, V'=VR`, the weight becomes
`H'=R^T H R`. Both balance equations, PSD, rank, and the associated strategy
are preserved. Top-space multiplicity and singular weights introduce no
additional quotient or missing branch.

“All extremizers” refers here to vector strategies modulo a common ambient
orthogonal change for all labeled vectors. It does not assert uniqueness of
an optimal correlation value, uniqueness of a physical realization, or
minimal complex quantum dimension. None of those stronger claims was used.

## F6R — Spectrahedral-classification route: PASS with assembly caveat

The exact route implication is valid: for nonzero transitive equivariant
matrices saturation identifies optimization extremizers with equality cases;
the verified equality conditions give the feasible weights; and full Gram
equivalence and nonemptiness give the quotient and minimum-rank conclusion.
The listed premises are the relevant interfaces for this implication.

There is a protocol-level assembly caveat. The two currently referenced
premise nodes contain the exact wording defects recorded in F4 and F5.
Although those defects lie outside the regime actually needed for this
classification, this report does not grant their current full statements
PASS. The mathematics of the classification claim and implication passes
because the required restricted results have been independently reconstructed
above. Promotion through the current DAG should wait until the premise
wording is repaired and the repaired statements receive hash-bound review,
or until an explicit independently reviewed alternative assembly is recorded.
This caveat prevents an exact-statement failure from being hidden by a
downstream positive verdict.

## F7 — Imbalanced diagonal counterexample: PASS

Source inspected: balanced-rank draft, GO-T5.

For `A=diag(2,1)`, the objective is
`2<x_1,y_1>+<x_2,y_2> <= 3`. Taking `x_i=y_i` attains three, including
in dimension one. The operator norm is two, giving spectral bound four.
The full top projector is `diag(1,0)` and is not balanced. The trivial group
provides a valid invariant, nontransitive action on two row and column
points. Hence invariance without transitivity does not force saturation.

This is an existential obstruction, as expressed by “need not.” It does
not prove that every matrix with an unbalanced full top projector fails to
saturate, or that transitivity is logically necessary for saturation. Those
stronger interpretations are outside the claim and are not licensed by
this example. The general criterion is feasibility of `H`, not merely the
scalar-projector test.

## F8 — Noninvariant extremizer: PASS

Source inspected: classification note, GOC-T5; GOC-T6 only for the boundary
between the full set and its invariant subset.

For the displayed matrix `H`, the upper `2 by 2` block has eigenvalues
`3/2` and `1/2`; the remaining eigenvalue is one. Thus `H` is positive
definite and has unit diagonal. With `A=I_3` and `U=V=I_3`, any real factor
`H=TT^T` yields `X=Y=T` with unit rows and objective three. Three is also
the universal bound, so this is an optimal vector strategy.

Conjugation by the permutation exchanging coordinates two and three sends
the nonzero off-diagonal pair `(1,2),(2,1)` to `(1,3),(3,1)`. It changes
`H`, hence `H` does not commute with this element of `S_3`. The actions on
rows and columns are transitive and leave `I_3` equivariant, so the example
meets the stated hypotheses exactly.

Group averaging preserves the feasible affine constraints and positivity,
but need not preserve the full Gram data. Here the averaged weight has every
off-diagonal entry `1/6`, whereas the original weight has entries `1/2,0,0`
on the three unordered off-diagonal positions. They are distinct labeled
Gram data; an ambient orthogonal transformation does not change Gram data.
Thus the displayed noninvariant extremizer is not equivalent to its average
under F6's ambient-orthogonal quotient. The obstruction concerns all versus
invariant extremizers and does not challenge existence of an invariant
optimal representative. No R/C/H block theorem is certified here.

## Overall verdict and limits

Six of the eight exact node claims pass their scoped mathematical review.
The two full claims failing exact completion are F4 (undefined minima when
no saturation exists) and F5 (unqualified paired-basis construction for a
rectangular zero matrix). The core equality parametrization and the optimum
value theorem pass. The spectrahedral route passes as a conditional
implication; the balanced-top-space route has a valid displayed case split
but fails to establish its exact unqualified target. Repairing and re-reviewing
the two statements is required before claiming the entire present DAG chain
has passed.

This review does not establish novelty, literature completeness, a formal
proof-assistant result, R/C/H classification, physical dimension optimality,
or any later exploration conjecture. Hash computations identify the reviewed
text; they are not mathematical verification by themselves. The source
artifacts' historical “no review yet” remarks describe their earlier status
and are not silently rewritten here. No node, event, assessment, generated
view, proof artifact, or canonical repository was modified by this reviewer.

## Provenance appendix

Raw-file SHA-256 at inspection time:

```text
sha256:d8775b511431e6e9dc7a5be6200af80bd612e7e7d5f5ff10bb14ef748791a095  DAG_PROTOCOL.md
sha256:6a2ea1af9bd14a4eaa8d158e304aee5e82cf907497addb17c2771782a4e6a329  FILE_PROTOCOL.md
sha256:38772ab9c2847461cf1410e2943681a7c74248669292709e7477153efb54aa2e  tools/proof_dag_schema.py
sha256:c6b7bd87193b34ad6e5c05d20971fba2722ba202c3e87e2bd6717a951d5dfef4  grothendieck-group-orbit/artifacts/balanced-rank-theorem-draft-20260829.md
sha256:44ac28ada792471f5ff014f763a94da16929ac2f6d99df01b2a056f52a47cd99  grothendieck-group-orbit/artifacts/complete-extremizer-classification-20260829.md
sha256:1c28ecb132e2c7793e197e0bc387884eb8b9057fbb48807436385dd455b8d71d  grothendieck-group-orbit/proof-dag/GRAPH.mmd
sha256:5c0a1dbe5a72aad04ce240bd067d77a672a52eae634784d18ccdc634f55aeb97  grothendieck-group-orbit/proof-dag/nodes/GROTHORB.spectral-upper.yaml
sha256:8e58e2d6e861b7b8c23143fd66ed6f69b53b4aab8cea0be81b9339a44281a91d  grothendieck-group-orbit/proof-dag/nodes/GROTHORB.balanced-criterion.yaml
sha256:4289e66365c4abad929aa7022e6adf78c39ec28471dd55f10ef674c51c86ceeb  grothendieck-group-orbit/proof-dag/nodes/GROTHORB.invariant-projector.yaml
sha256:ca927957dfbdcd9edaf6cb7c5ff8f4a39d39440f19603bb457f7c28c7c2378f4  grothendieck-group-orbit/proof-dag/nodes/GROTHORB.equality-characterization.yaml
sha256:07013ec94f87c06b1c300681fd713f275b48ac3574a3906dc637836fb57b93bd  grothendieck-group-orbit/proof-dag/nodes/GROTHORB.transitive-optimum.yaml
sha256:dbfac4fb3080c02bd86acb5146f9a28aa778feff20da64b7ee60db2c02cefae2  grothendieck-group-orbit/proof-dag/nodes/GROTHORB.extremizer-classification.yaml
sha256:d3d11fe5acee9acb16e9c083933191ef0f83ba338229c94cf53cf5bfbc0e5eab  grothendieck-group-orbit/proof-dag/nodes/GROTHORB.counterexample.yaml
sha256:5dfcfb37cae7fe20323e2b25dfc1d8ea90a7596eaecdff27fb864fa0f0cc983d  grothendieck-group-orbit/proof-dag/nodes/GROTHORB.noninvariant-extremizer.yaml
```
