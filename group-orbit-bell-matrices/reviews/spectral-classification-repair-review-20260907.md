# Independent review of spectral-classification scope repairs

Date: 2026-09-07. This is a separate follow-up review after the original
spectral/classification report was finalized; it does not rewrite that report.

Reviewer: Codex GPT-6, delegated reviewer `/root/orbit_existing_audit`.
The reviewer independently found the two original wording defects and did
not author or edit the proof artifacts or repaired node statements. The
coordinating agent applied the repairs and requested a fresh check of their
exact text and the assembled classification argument. Independence is from
the authoring agent; this is same-model-family review, not external human or
different-model review. No webpage ChatGPT session was used.

Reviewed root:

```text
/private/tmp/grothorb-exploration-20260907-hLCZqw
```

The reviewer previously read the local `DAG_PROTOCOL.md` and
`FILE_PROTOCOL.md` in full, both 2026-08-29 proof artifacts in full, and all
load-bearing spectral/classification nodes. In this follow-up, the repaired
equality/transitive nodes, their route sources, the unchanged classification
claim and spectrahedral route, and
`artifacts/spectral-classification-scope-repair-20260907.md` were inspected.
The source addendum was checked after SC1 explicitly restricted its
normalized-basis construction to nonzero transitive equivariant matrices.
All project-relative paths below are under `grothendieck-group-orbit/`.

Scope: exact completion of the two repaired claims, the balanced-top-space
route against its repaired target, and the full assembled all-extremizer
classification through the spectrahedral route. The retired commutant route,
quantum realization, R/C/H theorem, wreath products, later exploration
theorems, and literature priority are excluded. Row and column counts are
positive integers. This report is immutable and makes no node edits or
automatic assessment changes.

## Exact statement binding

The normalized hashes below were computed with
`tools/proof_dag_schema.py::claim_hash` on the YAML-decoded exact `claim` or
`implication`: replace CRLF with LF, strip outer whitespace, and hash UTF-8
bytes with SHA-256. Internal whitespace is preserved.

| Finding | Exact target | Reviewed hash | Verdict |
| --- | --- | --- | --- |
| F1 | repaired `GROTHORB.equality-characterization.claim` | `sha256:57801178adf2f68edec4a8eeb6fb5fe319462b63eb7d2addbe98028ec314143c` | PASS |
| F2 | repaired `GROTHORB.transitive-optimum.claim` | `sha256:3595380193737509977c85f3b2806810291bba8218e68de229adb35cb6230ab5` | PASS |
| F2R | `GROTHORB.transitive-optimum.routes.balanced-top-space.implication` | `sha256:84d6b925e3477ddd0553add534f2c36b1cceb556ef6b55da52f156802c4ac6c8` | PASS against the repaired target |
| F3 | `GROTHORB.extremizer-classification.claim` | `sha256:5cbc9e0d89f69f0929510b7592b1480185c5efcf320a3b619d3da4f41c5d02e3` | PASS, including assembled mathematical support |
| F3R | `GROTHORB.extremizer-classification.routes.spectrahedral-classification.implication` | `sha256:d82439273a03af85a1bbb295a4a27d5e45f493c3b1ec1f10c2caeb73035bf547` | PASS, including assembled mathematical support |

The unchanged supporting premise claims were independently checked in
`reviews/spectral-classification-review-20260907.md`:

| Premise | Original finding | Reviewed claim hash |
| --- | --- | --- |
| `GROTHORB.spectral-upper` | F1, PASS | `sha256:5eb3c78d20d4431b223f760c4edbe64239e63fc50894feb6e0ec20a8e98adea1` |
| `GROTHORB.balanced-criterion` | F2, PASS | `sha256:69783511b8a93069122c7b208ea7a31478b0e03d2e8a2e3075f5c3b044b69a5b` |
| `GROTHORB.invariant-projector` | F3, PASS | `sha256:bc24d83480c8b4750c42f0f7e8c52e5e4727bde1ee53323843606c5ba870e1e5` |

## F1 — Repaired equality characterization: PASS

The final sentence now reads:

> Whenever such strategies exist, the minimum real vector dimension among them is the minimum rank of a feasible H.

This explicitly supplies the missing existence condition. The preceding
iff remains unrestricted over nonzero matrices: an attaining strategy exists
exactly when the balance constraints have a feasible PSD weight. If neither
exists, no minimum is asserted. In particular `A=diag(2,1)` is correctly
handled: its paired top bases are `(1,0)^T`, the balance equations are
infeasible, and the dimension clause does not apply.

The full proof was checked, not just the replacement sentence. Equality in
the operator/Frobenius bound puts every column of `Y` in the whole top right
singular space, even for repeated top singular values. Equality in the
positive Cauchy--Schwarz bound gives
`X=(sqrt(m/n)/sigma) A Y`. Hence `Y=VT` and `X=sqrt(m/n)UT`. The unit-row
constraints become exactly the two displayed diagonal equations for
`H=TT^T`; conversely those equations imply `Tr(H)=n` and an objective
`sigma sqrt(mn)` for every factorization. With a nonempty feasible set,
the attained ranks form a nonempty subset of `{1,...,r}`. Its smallest
rank exists, and a real factor with width equal to that rank realizes it.
No minimum over an empty set or unmentioned infinity convention remains.

The repair closes the original report's F4 failure for the new exact hash.
The original FAIL remains a valid record about the former statement.

## F2 — Repaired transitive optimum: PASS

The repaired claim keeps the optimum-value equality for all matrices and
explicitly states the two cases: normalized rows of paired top singular
bases attain it for `A!=0`; every feasible vector strategy is optimal for
`A=0`. This matches the actual proof, including rectangular zero matrices.

For nonzero `A`, equivariance implies commutation of `AA^T` and `A^T A`
with the respective permutation actions. Their full top spectral projectors
therefore commute as well. The positive singular value gives a common
multiplicity `r>=1`; transitivity and projector trace give diagonals `r/m`
and `r/n`. Thus `X=sqrt(m/r)U` and `Y=sqrt(n/r)V` are unit-row strategies
with objective `sigma sqrt(mn)`. The universal upper bound matches this
value. These arguments check both the positive multiplicity and rectangular
normalization, without assuming irreducibility or a simple singular value.

For `A=0`, every summand in the objective is zero and both sides of the
value formula vanish. Feasible unit vectors exist in dimension one. No
paired-full-space construction is now required, so the different full
left/right zero-space dimensions when `m!=n` cause no undefined expression.

The repair closes the original report's F5 failure for the new exact hash.
It does not claim that the former unconditional basis wording was correct.

## F2R — Balanced-top-space route against repaired target: PASS

The implication string is unchanged. Its nonzero case supplies the
normalized-basis construction from the three reviewed premises; its zero
case supplies zero value and optimality of every feasible strategy. These
are now exactly the two conclusions written in the parent claim. The prior
target mismatch is removed, and the full route obligation passes against
the repaired target hash above.

This change in verdict reflects the changed parent target, not a claim that
the old review misread the route. The old F5R explicitly accepted the
piecewise implication text while rejecting its use to establish the older
unqualified parent. The current report binds both the same route hash and
the repaired parent hash, making that difference explicit.

## F3 — All-extremizer classification, fully assembled: PASS

For every nonzero transitive equivariant matrix in the claim, F2 provides
spectral saturation and the scalar feasible weight `H_0=(n/r)I_r`. Therefore
the repaired F1 existence condition is met. Every optimum attains the
spectral upper bound and is one of the equality strategies parameterized by
the complete balance spectrahedron; every feasible weight gives an optimum.
The minimum-rank formula follows with a nonempty feasible set.

The ambient-orthogonal quotient was checked independently. The full labeled
Gram matrix of the two vector families is `B H B^T`, where `B` stacks
`sqrt(m/n)U` and `V`. Its Bob block uniquely recovers the weight by
`H=V^T(YY^T)V`. Equal weights give equal full Gram matrices, hence isometric
vector spans and a common ambient orthogonal map after zero padding.
Different weights cannot give the same full labeled Gram data. A common
paired-basis change `U,V -> UR,VR` sends `H -> R^T H R` and preserves the
classification and rank minimum.

This classifies all vector extremizers; it does not restrict to invariant
weights. The original `I_3/S_3` noninvariant example remains part of the
valid obstruction to the retired commutant-only route. Averaging may change
the labeled Gram data and is unnecessary here.

The entire required mathematical chain now passes: universal upper bound,
balanced construction, invariant-projector lemma, repaired transitive
assembly, repaired general equality classification, and this full
spectrahedral classification. The previous assembly caveat arising from
the two overly broad premise statements is closed for the repaired hashes.

## F3R — Spectrahedral-classification route, fully assembled: PASS

The route has the repaired transitive-optimum and equality-characterization
nodes as premises. F2/F2R and F1 above check those exact statements and
their load-bearing arguments. The nonzero transitive target guarantees
nonemptiness, turns all optimization extrema into equality cases, and then
applies the verified Gram equivalence and minimum-rank result. Thus the
implication proves the exact current parent claim with all required
mathematical inputs checked. It passes as an assembled route, not merely as
an implication conditional on unresolved mathematical wording.

Attaching the appropriate finding to each node/route and changing assessments
are separate protocol operations for the coordinating agent. This report
provides review evidence and does not silently promote any node.

## Provenance and limits

Raw SHA-256 digests of the repaired snapshot and supporting immutable review:

```text
sha256:8a995b4802bf0a9bcf6f39740aa71fe45036ceb25497b1158ffa07f7b0f5934a  grothendieck-group-orbit/proof-dag/nodes/GROTHORB.equality-characterization.yaml
sha256:6b68ba76b57cc7c5cbbd5621c939903706adcb4d3f68e25245706aa4ed1f8a60  grothendieck-group-orbit/proof-dag/nodes/GROTHORB.transitive-optimum.yaml
sha256:dbfac4fb3080c02bd86acb5146f9a28aa778feff20da64b7ee60db2c02cefae2  grothendieck-group-orbit/proof-dag/nodes/GROTHORB.extremizer-classification.yaml
sha256:56483aabd923e86edb66d7670c51f1617f7365162eb7d856b5ca2009658bf50e  grothendieck-group-orbit/artifacts/spectral-classification-scope-repair-20260907.md
sha256:7e21414c47cf8deab81b494ff31ba74fecbb02177c0b1fbc7f9abd2a9ec66941  grothendieck-group-orbit/reviews/spectral-classification-review-20260907.md
```

All five exact targets in this follow-up pass. The two original FAIL findings
and their original hashes are preserved. This follow-up makes no novelty,
source-priority, physical-dimension, or formal-verification claim. Hashes
identify the reviewed text; the proofs and boundary checks above supply the
mathematical review. No canonical node or historical proof artifact was
modified by this reviewer.
