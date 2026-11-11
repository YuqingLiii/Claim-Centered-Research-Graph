# Independent correctness review of the conditioning equality criterion

Date: 2026-09-07. Reviewer: Codex agent `/root/orbit_root_prior_art`.
Reviewed root: `/private/tmp/grothorb-classical-20260907-R0Shtu`.

Verdict: **PASS** for the exact current C14 claim in F1. Both necessity
and sufficiency hold under its full stated hypotheses. In particular,
PSD compression equality proves support orthogonality before it is used,
and the one-dimensional weighted Gram kernel forces equal Alice weights.
No mathematical repair is required.

## Independence, scope, and inspected materials

The reviewer did not author or advise on C14's statement or proof before
this review. The author provided a completed frozen artifact. This
reviewer previously reviewed C13 and other claims in the same task;
therefore the present review is author/reviewer role separation within
the same model family and shared context, **not fresh-context or
cross-model independence**. Familiarity with the preceding conditioning
bound is disclosed rather than counted as independent authoring of C14.

The complete current self-contained YAML claim and all proof sections
CE-1--CE-7 were read. The repository protocols had already been read
completely. Every prerequisite rank and trace argument is present in CE-2
and was checked again; no predecessor claim or report is silently imported
as a load-bearing premise. The mathematical scope is exactly the stated
real frames, minimum total budget, injectivity, and four-condition
equivalence. Existence of such frames, novelty, sharpness in other
domains, and physical consequences are excluded.

| Frozen input | SHA-256 |
|---|---|
| `grothendieck-group-orbit/proof-dag/nodes/GROTHORB.minimal-conditioning-equality.yaml` | `bba8fe050a57c2b658fe856ca8736c0b9b044a8df6a69d7d06b9a27ed1f8b220` |
| `grothendieck-group-orbit/artifacts/minimal-conditioning-equality-20260907.md` | `f6e1d7d3498abbfb1722bbd45bcaedc5f4ec2c0654a90f9eec86ebe613cd93e4` |

The proof digest matches the supplied frozen digest. Both input digests
were recomputed after the mathematical inspection and remained unchanged.
The previous C13 report also retained digest
`97d0573d8125a3fdf5a48986fd2a439b9ba8922652af9475bddbb97adffd36cd`.
Only this new report was written. The proof is analytic and requires no
numerical experiment or finite-example inference for its correctness.

## F1. GROTHORB.minimal-conditioning-equality — PASS

Target: the route-free node claim.

`reviewed_hash: sha256:1808e5956926e46c72702359a6273694b3c8bfbbc3389693fd67ce358b6660e1`

Exact parsed `claim.strip()` reviewed:

> Let r>=2 and m>=n>=1 be integers. Let a_i,b_j be unit vectors in R^r with positive weights u_i,v_j such that each weighted second moment is I_r, m+n=r(r+1)/2+1, and the combined map H -> ((a_i^T H a_i)_i, (b_j^T H b_j)_j) is injective on Sym_r. On traceless Sym_r put f_i=a_i a_i^T-I_r/r, g_j=b_j b_j^T-I_r/r, F_A=sum_i u_i |f_i><f_i|, F_B=sum_j v_j |g_j><g_j|, and c=(r-1)/(m-1), with the Frobenius inner product defining these operators. Then lambda_min(F_A+F_B)=c if and only if all u_i=r/m, all distinct Alice pairs satisfy (a_i^T a_k)^2=(m-r)/(r(m-1)), every cross pair satisfies (a_i^T b_j)^2=1/r, and the restriction of F_B to span{g_j} has smallest eigenvalue at least c.

**Prerequisites and denominators.** The normalized moments force each
frame to span `R^r`, so `m,n>=r>=2`. Taking their matrix traces gives
both weight sums r. Thus `c>0` and all denominators in the proof are
nonzero. The centered matrices lie in the Frobenius space
`V={H in Sym_r:tr(H)=0}`, of dimension `q=m+n-2`.

The positive weighted square expression for `<H,(F_A+F_B)H>_F`, together
with injectivity on `Sym_r`, proves positive definiteness on V. Each
single-side kernel is the orthogonal complement of its centered span,
so ranks equal span dimensions. The nonzero centered relations
`sum_i u_i f_i=0` and `sum_j v_j g_j=0` give ranks at most `m-1,n-1`.
Their sum must reach q because the combined operator has full rank q.
The exact budget forces both bounds to be equalities and
`E_A+E_B=V`, where `E_A=span{f_i}`, `E_B=span{g_j}`. This yields
`dim E_A=m-1`, `dim E_B=n-1`, and `dim ker(F_B)=m-1` without assuming
orthogonality. Finally each centered matrix has norm squared `(r-1)/r`;
weight sums r give operator traces `tr_V(F_A)=tr_V(F_B)=r-1`.

**Necessity: compression equality really forces orthogonal supports.**
Assume `lambda_min(F_A+F_B)=c`. Put `E=ker(F_B)` and `k=m-1`.
Because `F_A+F_B>=cI`, summing Rayleigh inequalities over an orthonormal
basis of E gives a compressed trace at least `kc`. The full trace of
F_A is exactly `r-1=kc`, and extending this basis to V shows that the
compressed trace is at most that full trace. Both inequalities are
equalities.

All omitted diagonal entries of F_A are nonnegative. Their zero sum
therefore makes each omitted entry zero. For any such basis vector K
of `E^perp`, the explicit identity
`<K,F_A K>_F=sum_i u_i<f_i,K>_F^2=0` and strict positivity of every
weight force every f_i to be orthogonal to K. This holds for a basis
of `E^perp`, so `E_A subseteq E`. Their independently established equal
dimensions then give `E_A=E=E_B^perp`.

This argument handles the possible non-invariance correctly: it does
not assume beforehand that F_A preserves E, and trace equality alone is
used together with PSD and the square representation to eliminate the
omitted support. Only after `E_A=E` is established is F_A restricted
as an operator on E. There it is at least `cI_E` and has trace kc;
its positive semidefinite difference from `cI_E` has zero trace, hence
is zero. Since it vanishes on `E^perp`, one gets `F_A=cP_E` globally.

Expanding the centered cross product gives
`<f_i,g_j>_F=(a_i^T b_j)^2-1/r`. The proved orthogonality yields the
third condition. On `E_B=E^perp`, F_A vanishes, so the inequality for
the combined operator is exactly `F_B|E_B>=cI_EB`, the fourth condition.
This restriction is well defined even before equality is assumed,
because F_B is self-adjoint, has range E_B, and kernel `E_B^perp`.

**Necessity: the Gram kernel forces weights and squared overlaps.**
For `L e_i=sqrt(u_i)f_i` and `s=(sqrt(u_i))`, the centered relation
gives `Ls=0` and `||s||^2=r`. Rank L is `m-1`, so its kernel is
exactly `span{s}`. This step uses rank and the existing positive weights;
equal weights have not been assumed. The Gram matrix `G=L^*L` has this
same kernel. Since `LL^*=cP_E` and `range(L)=E`,
`G^2=L^*(LL^*)L=cG`. It follows that G is c times the orthogonal
projection off s, namely `c(I-ss^T/r)`.

The i-th diagonal comparison is
`u_i(r-1)/r=c(1-u_i/r)`, hence
`u_i=cr/(r-1+c)=r/m`. The positive denominator `r-1+c` validates this
division also at `r=2`. The off-diagonal comparison, after cancelling
the nonzero factor `sqrt(u_i u_k)`, gives `<f_i,f_k>_F=-c/r`.
Thus for every `i!=k`,
`(a_i^T a_k)^2=(1-c)/r=(m-r)/(r(m-1))`. The numerator is nonnegative
since the hypotheses already imply `m>=r`. These are exactly the first
and second conditions. No Bob equal-weight condition was used or needed
for this direction.

**Sufficiency.** Keep all original frame, budget, and injectivity
hypotheses, and assume the four listed conditions. Equal Alice weights
and the stated squared overlaps make its weighted Gram entries
`G_ii=(r-1)/m`, `G_ik=-c/m` for `i!=k`, so
`G=c(I-J/m)`. The centered moment relation gives `L1=0`. For any
`Z=Lx` in E_A, `F_A Z=LGx=cLx=cZ`; F_A is zero on `E_A^perp`.
Thus `F_A=cP_EA` without any appeal to the necessity direction.

The third condition makes every centered cross inner product zero,
so E_A and E_B are orthogonal. Their sum is V by the rank facts already
proved under the common hypotheses. Hence the combined operator is
`cI_EA` in one orthogonal block and `F_B|E_B` in the other. The fourth
condition puts all eigenvalues of the second block at least c. The
first block is nonzero because `m-1>=1`, and supplies an actual eigenvalue
c. Therefore the least eigenvalue is exactly c, not merely bounded
below by c. This proves the reverse implication.

**Balanced sides and r=2.** Nothing in the proof uses a strict inequality
`m>n`. If `m=n`, the Bob restriction has dimension `m-1` and trace
`r-1=c(m-1)`, so condition four forces all its eigenvalues to equal c.
This is a consequence of that condition and the trace, not an assumed
premise, and does not alter either implication.

For `r=2`, the spanning and budget conditions force `m=n=2`, with c=1.
Both centered spans are one-dimensional. The formula gives Alice weights
one, distinct Alice squared overlap zero, cross squared overlaps 1/2,
and a nonzero one-dimensional Bob restriction with trace one. All Gram
kernel, compression, and spectral-block steps remain meaningful; no
zero-dimensional minimum eigenvalue or vanishing denominator occurs.
This verifies the edge case within the conditional equivalence without
asserting or classifying existence in any setting split.

No unproved support invariance, missing equal-weight assumption, circular
use of an equality condition, or omitted implication was found. The
node is route-free and its assembled proof contains all mathematical
inputs, so no additional route finding is required.

## Closeout

The `reviewed_hash` is SHA-256 of the UTF-8 encoding of the exact string
obtained by `yaml.safe_load(node_text)['claim'].strip()`. It is separate
from the file digests above. F1 binds the full self-contained statement
quoted in this report and the inspected frozen proof.

The review is not proof-assistant formalization, a cross-model audit,
an existence result, or a novelty assessment. This report is frozen on
completion. Author files, nodes, and earlier reports remain unchanged;
canonical integration is left to the coordinator. No further research
scope is opened.
