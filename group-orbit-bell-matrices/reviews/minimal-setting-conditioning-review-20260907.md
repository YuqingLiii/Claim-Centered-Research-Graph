# Independent correctness review of the minimum-budget conditioning bound

Date: 2026-09-07. Reviewer: Codex agent `/root/orbit_root_prior_art`.
Reviewed root: `/private/tmp/grothorb-classical-20260907-R0Shtu`.

Verdict: **PASS** for the exact current C13 claim in F1. The hypotheses
force the stated ranks, and the PSD compression argument gives the
smallest-eigenvalue bound without any kernel-invariance assumption.
No mathematical repair is required within the registered domain.

## Independence, scope, and frozen inputs

The reviewer did not author or advise on the C13 claim or proof before
this review. The author supplied a completed frozen argument. Earlier
work by this reviewer concerned other claims in the same project; it
does not constitute fresh-context or cross-model independence here.
This is separate author/reviewer responsibility within the same model
family and shared task context. The reviewer makes no stronger claim of
independence.

The complete current node and the complete proof MC-1--MC-5 were read.
The repository protocols had already been read completely. The review
covers real unit frames in `R^r`, the real Frobenius space of traceless
symmetric matrices defined in MC-1, and precisely the bound stated in
the node. It does not assess novelty, sharpness, equality classification,
a condition number, experimental noise, or self-testing. No further
proposition is investigated in this review.

| Frozen input | SHA-256 |
|---|---|
| `grothendieck-group-orbit/proof-dag/nodes/GROTHORB.minimal-setting-conditioning.yaml` | `de3344283f475377661a360a229b233bf1f411a8f06632cf5b7954a01334fd23` |
| `grothendieck-group-orbit/artifacts/minimum-setting-conditioning-20260907.md` | `9e8d2c030ff30e921de56897dd238d6dabc4dcc658a5157360b72569f4e2442a` |

The proof digest agrees with the supplied frozen digest. Both input
digests were independently recomputed after the mathematical inspection
and were unchanged. The parsed statement was also read again before
closeout. No author material, node, or earlier review was edited.
The argument is analytic; no numerical test or external theorem is needed
to substitute for any step of the proof.

## F1. GROTHORB.minimal-setting-conditioning — PASS

Target: the route-free node claim.

`reviewed_hash: sha256:b2c7293343b8537e0ff7e26fe74d6ec1c6fe43fc7c6cb30e28fb4fb70309aa98`

Exact parsed `claim.strip()` reviewed:

> Let r>=2, m,n>=1 be integers. Suppose two positive weighted unit frames satisfy sum_i u_i a_i a_i^T=sum_j v_j b_j b_j^T=I_r, m+n=r(r+1)/2+1, and their combined quadratic evaluation map is injective on Sym_r. On traceless Sym_r define f_i=a_i a_i^T-I_r/r, g_j=b_j b_j^T-I_r/r and F(H)=sum_i u_i <f_i,H>_F f_i+ sum_j v_j <g_j,H>_F g_j. Then F is positive definite and lambda_min(F)<=(r-1)/max(m-1,n-1).

**Domain and positivity.** Taking the ordinary matrix trace of each
normalized moment identity gives weight sum r, because every unit-vector
outer product has trace one. Each side spans `R^r`: otherwise a nonzero
vector orthogonal to its vectors would be sent to zero by that moment
matrix, contradicting its equality to I. Thus `m,n>=r>=2`, which makes
both denominators and the kernel dimensions used later strictly positive.
Each centered matrix has trace zero, so all operators in MC.3 act on
`V={H in Sym_r:tr(H)=0}` as stated.

For H in V, the quadratic form of F is a sum of positive-weight squares.
If it vanishes, every centered evaluation vanishes individually. Since
H is traceless, those evaluations are exactly `a_i^T H a_i` and
`b_j^T H b_j`. Injectivity of the full quadratic evaluation map on
`Sym_r` therefore implies H=0. Self-adjointness and positive definiteness
of F follow on V, whose dimension is
`q=r(r+1)/2-1=m+n-2`. No uniform quantitative lower bound is claimed
by this positive-definiteness argument.

**The exact single-side ranks are forced.** For either positive weighted
sum of rank-one operators, the kernel consists precisely of vectors
orthogonal to all of that side's centered matrices. The rank consequently
equals their span dimension. Centering each normalized moment identity
gives `sum_i u_i f_i=0` and `sum_j v_j g_j=0`, with nonzero coefficient
vectors. Hence `rank(F_A)<=m-1` and `rank(F_B)<=n-1`.

The image inclusion `im(F_A+F_B) subseteq im(F_A)+im(F_B)` now yields

```text
q = rank(F) <= rank(F_A)+rank(F_B) <= (m-1)+(n-1) = q.
```

Each single-side upper bound must be attained; if either were strict,
the sum would be strict as well. Rank-nullity on V gives
`dim ker(F_A)=n-1` and `dim ker(F_B)=m-1`. This uses the exact setting
budget as well as injectivity. It does not require, or establish,
orthogonality of the two ranges, commutation of the operators, or invariance
of one side's kernel under the other side's operator.

**The traces are operator traces on the correct space.** For a unit a,
`P=aa^T` satisfies `P^2=P` and `tr(P)=1`, so
`||P-I/r||_F^2=1-2/r+r/r^2=(r-1)/r`. Each centered vector lies in V.
The rank-one operator `H -> <f,H>_F f` on V has trace `||f||_F^2`,
as follows by summing squared inner products in an orthonormal basis of V.
The weight sums r then give
`tr_V(F_A)=tr_V(F_B)=r-1`. No extra off-diagonal-coordinate factor or
trace-direction contribution is missing: the argument uses the Frobenius
inner product and an orthonormal basis of V. The ordinary r-by-r matrix
trace used to define V is kept distinct from these operator traces.

**Compression, including a non-invariant kernel.** Write
`mu=lambda_min(F)>0` and take `E=ker(F_B)`, of dimension `k=m-1`.
For an orthonormal basis vector H in E, the Rayleigh inequality gives
`mu<=<H,FH>_F=<H,F_A H>_F`. Summing over that basis gives a lower
bound `k*mu` on the trace of the compressed operator `P_E F_A|_E`.
Extending the basis to V shows that this partial diagonal sum is at most
`tr_V(F_A)`, because every omitted diagonal entry of a PSD operator is
nonnegative. Consequently `mu<=(r-1)/(m-1)`.

The compression is `P_E F_A P_E` acting on E. It is well defined even
if `F_A(E)` is not contained in E; no restriction of F_A as an invariant
operator on E is being asserted. Equivalently, compressing `F>=mu I`
gives `P_E F_A P_E>=mu P_E` because `F_B P_E=0`, and taking its trace
gives the same inequality. This verifies the potentially delicate
non-invariance point without inserting an additional hypothesis.

Interchanging A and B gives `mu<=(r-1)/(n-1)`. The numerators and
denominators are positive, so the smaller of the two upper bounds is
`(r-1)/max(m-1,n-1)`, exactly the registered bound. The proof gives an
upper bound on the least eigenvalue; it does not silently turn that into
a lower stability or perturbation guarantee.

**Boundary r=2.** The span argument gives `m,n>=2`, while the budget
is `m+n=4`, forcing `m=n=2`. Thus `q=2`, both single-side ranks and
opposite kernel dimensions are one, and both operator traces are one.
The proof gives `0<mu<=1`, with neither a zero-dimensional kernel nor
a zero denominator. As a consistency check, `tr_V(F)=2` on a
two-dimensional space also gives `lambda_min(F)<=1`. No exceptional
case, limiting argument, or domain revision is needed.

Every step follows from the stated hypotheses and elementary
finite-dimensional inner-product-space linear algebra. There is no
unresolved project premise or route implication to grade separately.
The proof applies to the entire recorded domain, and no scope narrowing
was used to reach this PASS finding.

## Closeout

The statement hash was computed as SHA-256 of
`yaml.safe_load(node_text)['claim'].strip().encode('utf-8')`. It is distinct
from the YAML file digest listed above. The report binds exactly the
statement quoted in F1 and the inspected frozen proof.

This same-model, shared-context review is not a formal proof-assistant
check or a novelty assessment. The report is frozen at completion;
canonical promotion and integration remain the coordinator's task.
No further research scope is opened, and previous frozen materials
remain unchanged.
