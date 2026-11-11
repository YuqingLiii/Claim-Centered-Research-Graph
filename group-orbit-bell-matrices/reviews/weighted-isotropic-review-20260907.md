# Independent correctness review of the weighted isotropic vector optimum

Date: 2026-09-07. Reviewer: Codex agent `/root/orbit_root_prior_art`.
Reviewed root: `/private/tmp/grothorb-classical-20260907-R0Shtu`.

Verdict: **PASS** for the exact current claim in F1. The weighted upper
bound is valid for arbitrary strategy dimension, and the stated strategy
attains it. No mathematical repair is required within the registered
domain. Novelty and literature positioning are outside this review.

## Independence and materials

The reviewer did not author or advise on C11's statement, proof, or
checker. Its author was a separate agent and had completed the materials
before this review. The reviewer previously performed literature and D3
reviews in this task, so this is author/reviewer role separation in the
same model family and shared context, not a fresh-context or cross-model
review. No prior weighted-C11 proof work by this reviewer is reused as
independent evidence. A separate literature agent is not counted as a
correctness reviewer here.

The complete current YAML, complete proof WI-1--WI-5, checker source,
and author run record were read. The current YAML explicitly states that
`r,m,n` are positive integers; the review binds this version, including
that domain clarification. The repository protocols had been read fully.
The reviewer checked the general algebra and the numerical checker
separately, then replayed the latter with assertions enabled.

All paths in this table are relative to `grothendieck-group-orbit/`.

| Frozen input | SHA-256 |
|---|---|
| `proof-dag/nodes/GROTHORB.weighted-isotropic-optimum.yaml` | `615926411bcc94dff2297ad72e7bdb1043365b0f23fa7f8b36e8ebb9484c310c` |
| `artifacts/weighted-isotropic-optimum-20260907.md` | `3a727e8513dd2dba75464bca7c7fac3507673e65e31d927598d30cd5f7e0bb9a` |
| `tools/check_weighted_isotropic_optimum.py` | `df6837dc09a88dfe4287eecb234635fa04f6beeaa41474b0b0f94fcdb8b3aa24` |
| `artifacts/weighted-isotropic-exact-check-20260907.txt` | `2fb48e403e0f54b646647965fd446f6ebb5380a47e9354a545386eba8e9b8775` |

Fresh execution and statement extraction are recorded in
[weighted-isotropic-review-rerun-20260907.txt](../artifacts/weighted-isotropic-review-rerun-20260907.txt),
SHA-256 `36c9d5c6982414e1757a1b7da6141d2b05dbd7244b8455305dc372d94b100e34`.
Its WI-R1 run exited 0. All four input digests were checked again before
closeout and remained unchanged.

## F1. GROTHORB.weighted-isotropic-optimum — PASS

Target: the route-free node claim.

`reviewed_hash: sha256:efc68dff78220733c250b60537c17019339c6229129c7cd7235e033a06f83490`

Exact parsed `claim.strip()` reviewed:

> Let r,m,n be positive integers, a_1,...,a_m and b_1,...,b_n unit vectors in R^r, and u_i,v_j positive real weights. Write S=sum_i u_i and T=sum_j v_j. If sum_i u_i a_i a_i^T=(S/r)I_r and sum_j v_j b_j b_j^T=(T/r)I_r, then the real vector Bell optimum of M_ij=u_i v_j (a_i dot b_j) is S*T/r, attained by the strategy x_i=a_i,y_j=b_j.

The reviewed interpretation of the vector optimum is the one stated in
WI-1: unit `x_i,y_j` in a common real space, with the supremum over every
positive finite strategy dimension. Finite setting counts also make
arbitrary real Hilbert-space strategies equivalent to this interpretation,
because their span has dimension at most `m+n`. This is a vector-value
statement, not a minimum physical dimension or self-testing statement.

**Domain and weighted normalization.** Positive weights and nonempty
sides imply `S,T>0`, while `r>0` makes all denominators defined.
Isotropy makes both weighted frame matrices have rank r, so the required
isometries can exist only when `m,n>=r`; this is a consequence, not an
extra unregistered hypothesis. Repeated frame vectors and unequal side
counts cause no issue.

Let A and B have rows `sqrt(u_i)a_i^T` and `sqrt(v_j)b_j^T` as in WI-2.
The claimed identities `A^T A=(S/r)I` and `B^T B=(T/r)I` are exactly
the hypotheses. Thus `P=sqrt(r/S)A` and `Q=sqrt(r/T)B` have orthonormal
columns. The rectangular map `PQ^T` is a contraction and has norm exactly
one: for any unit e in `R^r`, the unit vector Qe is sent to Pe. Therefore
`K=AB^T=(sqrt(ST)/r)PQ^T` has norm `sqrt(ST)/r`. No square-matrix or
transitivity assumption is used at this step.

For arbitrary strategy dimension d, the weighted row matrices
`X~=diag(sqrt(u))X`, `Y~=diag(sqrt(v))Y` have dimensions `m by d` and
`n by d`, with squared Frobenius norms S and T. Entrywise expansion of
`tr(X~^T K Y~)` places a square root of u and v in K, and another square
root in each corresponding strategy row. The coefficient is consequently
`u_i v_j(a_i dot b_j)`, exactly M, rather than its square-root-weighted
variant. Frobenius Cauchy--Schwarz and the columnwise operator-norm
inequality give `sqrt(S)*(sqrt(ST)/r)*sqrt(T)=ST/r`. The argument holds
for every d and does not constrain strategies to dimension r.

As an independent algebraic check of the weight factors, the reviewer
rewrote the score as the Frobenius inner product of

```text
F_x = sum_i u_i x_i a_i^T,   F_y = sum_j v_j y_j b_j^T.
```

These are both `d by r`. Since `F_x=X~^T A` and `F_y=Y~^T B`,
their Frobenius norms are at most `S/sqrt(r)` and `T/sqrt(r)`.
Their inner product therefore has the same upper bound `ST/r` without
forming the rectangular cross matrix K. This confirms the normalization
and absence of a hidden `m,n`, or strategy-dimension factor.

**Attainment and scalar edge case.** The candidate strategy is admissible
in dimension r because the given frame vectors are unit. Its value is
`sum_ij u_i v_j(a_i dot b_j)^2`. Expanding the trace of the two moment
matrices gives `tr((S/r)I*(T/r)I)=ST/r`; the trace contributes r,
so the denominator is r rather than r squared. This proves attainment
as well as an upper bound on the supremum. At `r=1`, all frame vectors
are signs, isotropy is automatic, and the same construction gives ST.
No part of the isometry proof or trace calculation requires `r>1`.

**PSD upper certificate.** In WI-4, the off-diagonal blocks are `-M`
and `-M^T`, and the diagonal blocks are `(T/r)D_u` and `(S/r)D_v`.
The quadratic cross term is therefore `-2p^TMq`. With
`p~=D_u^(1/2)p` and `q~=D_v^(1/2)q`, its absolute value is bounded
using K exactly as claimed. The quadratic form is bounded below by
`(sqrt(T)||p~||-sqrt(S)||q~||)^2/r`, which is nonnegative for all p,q.
This proves L is PSD without invoking SDP duality or a missing external
theorem. Applying L to every coordinate of a vector strategy yields
diagonal contribution `2ST/r` and cross contribution `-2 score`.
The factors of two therefore give the same upper bound as WI-2.
The reviewer also checked directly that L annihilates the stacked
columns of the given frame strategy, by the two isotropy identities;
the certificate is consistent with attainment.

**Checker inspection and replay.** The checker verifies its two rational
examples with exact `Fraction` arithmetic, including positivity, unit
norms, every entry of both moment matrices, the candidate score, and the
diagonal objective. Its PSD test is valid congruence elimination: a
positive pivot yields its Schur complement; a zero pivot is accepted only
when the entire remaining row and column vanish. The in-place updates do
not alter the pivot column until the trailing-block update is complete.
No floating-point comparison, numerical tolerance, or solver claim is
used. The fresh replay gives 18 for the scalar rectangular example and
12 for the rank-two rectangular example, with nonnegative exact pivots
and respectively one and two zero pivots. The interpreter optimization
flag was 0, so assertions executed.

These examples check normalization and finite certificates. The universal
claim is justified by the general algebra above and WI-2--WI-3, not by
extrapolating from those two cases. The direct proof has no unresolved
project premise or route implication requiring a separate finding.

## Closeout

The `reviewed_hash` is SHA-256 of UTF-8 after `yaml.safe_load` and
`claim.strip()`, not a file digest. PyYAML 6.0.3 was used only for this
extraction; mathematical execution used the Python standard library.
The positive-domain version quoted in F1 is the exact statement passed.
No scope narrowing, claim rewrite, or author-file edit was made.

Same-model, shared-context, interpreter, and non-formal-proof limitations
remain. The proof's correctness does not establish originality; literature
positioning remains a separate task. This report and its reviewer rerun
record are frozen on completion, and node promotion/integration is left
to the coordinator.
