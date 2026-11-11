# Independent review of the PSD antipodal window and full-root assembly

Date: 2026-09-07. Reviewer: Codex agent `/root/orbit_root_prior_art`.
Reviewed root: `/private/tmp/grothorb-classical-20260907-R0Shtu`.

Verdicts: **PASS** for C15 (`GROTHORB.psd-antipodal-linear-window`,
F1), **PASS** for C16 (`GROTHORB.root-extended-shift-window`, F2), and
**PASS** for the separate `psd-duplication-window` implication (F3).
The global gap certificate and its matching signs are correct, including
singular matrices and all registered boundary cases. The dependent root
formula has the stated normalization and closed sufficient interval.
No mathematical repair is required for these statements.

## Independence, scope, and frozen inputs

The reviewer did not write the C15 or C16 statements, author proofs, or
their derivations. This agent previously worked on literature and reviewed
other claims in the same task. This is independent author/reviewer role
separation within the same model family and shared context, **not a
fresh-context or cross-model review**. Earlier awareness of root and
duplication results is disclosed, not counted as extra independence.

The complete current C15 and C16 YAML files were read, including all
claims, the route implication and its premise list, and the absence of
external assumptions. The complete author artifacts PW-1--PW-6 and
RW-1--RW-4 were read and checked. The current `GROTHORB.root-classical`
node, its complete proof RC-1--RC-5, and the exact applicable F1 in the
earlier root-classical review were also read. The protocols had already
been read completely. No unrelated finding in that earlier report is
used here.

Only the registered claims and route are reviewed. This report neither
asserts a maximal interval nor judges novelty. No new computational
experiment, checker, or unregistered proposition was introduced; the
general conclusions below rest on direct algebra, not finite tests.

| Frozen local input | SHA-256 |
|---|---|
| `grothendieck-group-orbit/proof-dag/nodes/GROTHORB.psd-antipodal-linear-window.yaml` | `8958abb99db80f8c5aa8375cb470be757aa59144aabac9de2622f37679e4bcd3` |
| `grothendieck-group-orbit/proof-dag/nodes/GROTHORB.root-extended-shift-window.yaml` | `904c12b4313e0d7ee8db0ad1f6617872d8f3c518d30fce8b1a32fb884c1dcf9a` |
| `grothendieck-group-orbit/proof-dag/nodes/GROTHORB.root-classical.yaml` | `e42746b017db8cf346795064b1f8f2ceda41ab9cef4dfde22f2e3da71b91a5f4` |
| `grothendieck-group-orbit/artifacts/psd-antipodal-linear-window-20260907.md` | `281a14deb972523865c22c196b7972c4b3f704a541e7ddfa36ec3c68e7ab22f0` |
| `grothendieck-group-orbit/artifacts/root-extended-shift-window-20260907.md` | `72c4088b302b871bee2bd46aae4ca615d6bb1cf2e1f19903cf3e77b617ef413a` |
| `grothendieck-group-orbit/artifacts/root-classical-value-20260907.md` | `8ea014aa65b2af33bf5c15182eadec95d629d0970f8f816081b4497b6b6c3259` |
| `grothendieck-group-orbit/reviews/root-classical-review-20260907.md` | `ac6200d1418254694977ed940ca56314c326621315e154e36e5b7be9f1864bc9` |

The two supplied author proof digests match. All seven input digests,
all three reviewed statement digests, and their exact quotations were
rechecked at closeout and remained unchanged. Only this new report was
written; authors' files, nodes, and earlier frozen reviews were not
modified.

## F1. GROTHORB.psd-antipodal-linear-window — PASS

Target: C15's route-free claim.

`reviewed_hash: sha256:98c4958c91dace11088aaff1ecc7b590bb982f84cc5d26c027bc8a2603beda38`

Exact parsed `claim.strip()` reviewed:

> Let C be a real symmetric PSD N by N matrix with N>=1, let D(C)=(1/2)[C,-C;-C,C], and define beta_cl(M)=max_{s,t in {+1,-1}^k} s^T M t for real square k by k matrices. For every 0<=lambda<=(1/2)min_i C_ii, beta_cl(D(C)-lambda I_{2N})=2 beta_cl(C)-2N lambda.

**PSD value and finite sign completion.** Put `d_i=C_ii` and let
`K=max_z z^T C z` over the finite N-dimensional sign set. For arbitrary
signs s,t, expansion of `(s-t)^T C(s-t)>=0` gives
`s^T Ct<=(s^T Cs+t^T Ct)/2<=K`. A maximizing diagonal pair attains K,
so `beta_cl(C)=K`. This reduction is applied only to C, not to the
possibly indefinite shifted matrix.

For any `x in [-1,1]^N`, the independent sign distribution with
`Pr(Z_i=1)=(1+x_i)/2` is well defined, including its degenerate endpoint
distributions. Its means are exactly x_i. Off-diagonal moments are
x_i x_j; diagonal moments are one. Consequently its expectation is

    E_x=x^T Cx+sum_i d_i(1-x_i^2)<=K.

The inequality follows because the distribution is a finite convex
combination of sign values each at most K. This does not assume the
existence of a sign vector exactly equal to x, substitute a sampled
estimate, or require a limit argument. The moment identity uses
independence only for distinct coordinates.

**The original bilinear score and its factors.** For arbitrary full
signs a,b, set `p=(a_+-a_-)/2`, `u=(a_++a_-)/2`, and define q,v
from b in the same order. In each coordinate exactly one of p_i,u_i
is nonzero, with value a sign; the same is true for q_i,v_i. Thus
`p_i^2+u_i^2=q_i^2+v_i^2=1`, with no coupling imposed between a and b.
The inverse formulas recover the original signs, so no competing
bilinear pairs are discarded.

The block calculation is
`a^T D(C)b=(1/2)(2p)^T C(2q)=2p^T Cq`, while
`a^T b=2(p dot q+u dot v)`. Therefore the half-score really is

    S=(1/2)a^T(D(C)-lambda I)b
      =p^T Cq-lambda(p dot q+u dot v).

For `x=(p+q)/2` and `y=(p-q)/2`, symmetry of C gives
`p^T Cq=x^T Cx-y^T Cy`. In particular the desired upper bound for S
is `K-N lambda`, not the full-score expression with an extra factor.

**Independent reconstruction of the four-term gap.** Direct subtraction
of this half-score gives

    K-N lambda-S
      =(K-E_x)+y^T Cy
        +sum_i [d_i(1-x_i^2)-lambda(1-p_i q_i-u_i v_i)].

Using the two coordinate norm identities, one obtains

    2(1-x_i^2)-(1-p_i q_i-u_i v_i)
      =1-(p_i^2+q_i^2)/2+u_i v_i
      =(u_i+v_i)^2/2.

Thus the gap is exactly

    (K-E_x)+y^T Cy
      +sum_i (d_i-2lambda)(1-x_i^2)
      +(lambda/2)||u+v||^2.

Each of these four terms is nonnegative for its stated, separate reason:
finite completion bounds E_x by K; PSD controls y; the registered
interval makes every `d_i-2lambda>=0`, with `|x_i|<=1`; and
`lambda>=0` controls the final square. There is no missing condition
on zero antipodal coordinates and no assumption that arbitrary
optimizers are fully antisymmetric. Multiplying the resulting
`S<=K-N lambda` by two yields the global upper bound over all full
sign pairs, with shift term `-2N lambda`.

**Matching and boundaries.** Choose a sign z maximizing `z^T Cz=K`
and take `a=b=(z,-z)`. Then `p=q=z`, `u=v=0`, and the full score
is `2K-2N lambda`. This matches the upper bound with the same
normalization; the certificate's gaps vanish for this pair.

No inverse, positive eigenvalue lower bound, or division by a diagonal
entry is used, so singular PSD matrices are covered. If any diagonal
entry is zero, PSD still implies all diagonals are nonnegative and
the registered interval collapses to `lambda=0`; the proof gives
`beta_cl(D(C))=2 beta_cl(C)` there without claiming positive width.
This includes `C=0`. For `N=1`, writing `C=[d]` gives `K=d` and
the claimed value `2d-2lambda` on `0<=lambda<=d/2`; the coordinate
identities and the witness `(1,-1)` still apply, also when d=0.
At the lower endpoint terms proportional to lambda disappear; at the
upper endpoint some coefficients `d_i-2lambda` may be zero. All
inequalities are non-strict, so neither endpoint is omitted.

The claim therefore follows for its entire stated domain. It has no
external or project-theorem premise, and no route finding is needed
for C15. Nothing in this finding extends the interval or characterizes
its maximality.

## F2. GROTHORB.root-extended-shift-window — PASS

Target: the full C16 parent claim, using the verified C15 result and
the existing root-classical theorem through the separately checked
route in F3.

`reviewed_hash: sha256:df62de9a7c9c2c2dd4e5512ea89a3374d63f3c3bbb6e6d41f4eff509732f05db`

Exact parsed `claim.strip()` reviewed:

> For every integer r>=3, let W have as its rows all vectors epsilon e_i+eta e_j with 1<=i<j<=r and epsilon,eta in {+1,-1}, let n=2r(r-1), and put A_r=WW^T/[4(r-1)]. Then for every 0<=lambda<=1/[2(r-1)], beta_cl(A_r-lambda I_n)=2r(2r-1)/3-n lambda.

The current `GROTHORB.root-classical` premise has exact claim hash
`sha256:5894fbd5f0998222db98bbe3cbef23b0a723716a30125952c2db60e748375fca`.
It matches the earlier independent report's F1, and its proof has the
same digest recorded there. I also checked its all-r argument directly:
the positive Gram form reduces the bilinear value to
`max_s ||W^T s||^2/[4(r-1)]`. The full signed-root support function
is `4 sum_i (r-i)a_i` for decreasing absolute unit coordinates a_i.
Cauchy--Schwarz gives `4||rho||`, attained at the normalized
`rho=(r-1,...,0)`. The root sign epsilon realizes `W^T s=4rho`,
so the classical value is `2r(2r-1)/3`. This verifies the specific
unshifted premise needed here independently of its PROVED status label
or any finite-r run.

F1 above establishes the other premise before it is used. F3 checks
the complete registered implication, with no missing premise. Thus
the two actual verified arguments, rather than the author's labels,
establish the C16 formula for every integer r>=3 and both endpoints
of its stated interval. The stale authoring-time phrases that C15
was unreviewed do not constitute evidence and are not used as such.

The explicit witness in RW-4 is also correct. The two U roots over
each pair sum to `2e_i`, hence `U^T1_N=2rho`. In the `[U;-U]`
order the full sign `(1_N,-1_N)` has `W_hat^T s=4rho`, squared norm
of s equal to `2N=n`, and shifted value
`16||rho||^2/[4(r-1)]-n lambda=2r(2r-1)/3-n lambda`.
Permuting the sign pair along with the rows of W gives the same
witness in any registered row order. This checks attainment directly;
the upper bound for every competing pair is supplied by F1, not
inferred from that witness.

## F3. GROTHORB.root-extended-shift-window / psd-duplication-window — PASS

Target: the exact registered route implication, distinct from the
parent claim.

`reviewed_hash: sha256:81735fbe09238f4c5e32f9448ef5d0e01af445de76cb04e4d7df5421e20545ca`

Exact parsed `implication.strip()` reviewed:

> Select positive D_r roots U so that W is a simultaneous row permutation of [U;-U]. The matrix C=UU^T/[2(r-1)] is PSD with diagonal 1/(r-1), and D(C) is the full root projection up to simultaneous permutation. The PSD duplication-window theorem, its zero-shift identity, and the established full-root classical value give the claimed interval and formula.

The route lists exactly `GROTHORB.psd-antipodal-linear-window` and
`GROTHORB.root-classical`. Their applicable statement hashes and
verified support are given in F1 and F2. No half-root theorem, earlier
small-shift theorem, D3 computation, or shifted equality classification
is used as an undeclared third premise.

For each pair i<j take the two U rows `e_i-e_j` and `e_i+e_j`.
There are exactly `N=2 binom(r,2)=r(r-1)` such rows. U contains
the full roots with first nonzero sign epsilon=+1; -U contains those
with epsilon=-1. These are disjoint and together contain every one
of the `n=2N` signed roots exactly once. Thus `W=P[U;-U]` for a
row permutation P. The corresponding square Gram matrix is
simultaneously permuted on its two indices. This is the precise
meaning of the route's permutation wording.

Because `r>=3`, the denominator `2(r-1)` is positive and
`C=UU^T/[2(r-1)]` is a real symmetric PSD N by N matrix. Every
U row has squared norm two, so each diagonal is exactly `1/(r-1)`.
Block multiplication gives

    [U;-U][U;-U]^T/[4(r-1)]
      =(1/2)[C,-C;-C,C]=D(C).

There is no missing factor two in the Gram coefficient or in the
number of duplicated settings. The term "projection" in the route
also agrees with this normalization: summing the four outer products
for one coordinate pair gives `4(e_i e_i^T+e_j e_j^T)`, and hence
`W^T W=4(r-1)I_r`; the normalized full Gram is idempotent. This
normalization check introduces no extra project premise.

Since P maps sign sets bijectively and `P I_n P^T=I_n`, the two
shifted classical values agree for every lambda under consideration.
C15's hypothesis becomes precisely
`0<=lambda<=min_i C_ii/2=1/[2(r-1)]`; N is positive, and no other
domain condition is needed. In particular zero belongs to this
interval. Applying the already verified C15 statement at zero gives
`2 beta_cl(C)=beta_cl(D(C))=beta_cl(A_r)`. The base root premise
therefore supplies `2 beta_cl(C)=2r(2r-1)/3` without any circular
use of the shifted parent.

Applying C15 again at the chosen lambda and substituting `2N=n`
now gives exactly

    beta_cl(A_r-lambda I_n)
      =2 beta_cl(C)-2N lambda
      =2r(2r-1)/3-n lambda.

This proves the full route implication and assembles all of the
parent's hypotheses. It does not say that antipodal duplication
preserves an arbitrary shifted problem or that the new endpoint is
maximal for any or all r.

## Closeout

Each `reviewed_hash` is SHA-256 of UTF-8 `claim.strip()` or
`implication.strip()` after parsing the current YAML, not a file digest
or paraphrase hash. F1, F2, and F3 are separate findings. The
root-classical prerequisite is linked to its applicable earlier review
and was rechecked analytically; C15 is justified by F1 before it is
used in the parent or route. No premise is accepted merely from a
status or author label.

This is a non-formalized, same-model correctness audit. It makes no
novelty, maximal-window, all-optimizer, or out-of-domain assertion, and
does not revive the earlier refuted whole-interval extrapolation.
This report is frozen on completion. Node integration is left to the
coordinator; no additional research scope is opened.
