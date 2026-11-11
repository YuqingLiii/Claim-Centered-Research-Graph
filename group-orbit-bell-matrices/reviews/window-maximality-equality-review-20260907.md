# Independent review of root-window maximality and interior ordered equality

Date: 2026-09-07. Reviewer: Codex agent `/root/orbit_root_prior_art`.
Reviewed stage: `/private/tmp/grothorb-window-next-20260907-nzQdSy`.

Verdicts: **PASS** for the C17 claim (F1), its
`height-one-competitor` route (F2), the C18 claim (F3), and its
`strict-gap-coefficients` route (F4). The explicit competitor proves
failure of the old affine value at every parameter above the root
endpoint. The strict-interior gap proves the stated classification of
all original ordered sign pairs, including for singular PSD inputs.
No mathematical repair is required for these exact statements.

## Independence, inspected inputs, and evidence boundary

The reviewer did not write, edit, or advise on the C17 or C18 author
proofs. This agent previously reviewed their C15/C16 premises and
other claims in this project, and shares the task context and model
family with the authors. This is author/reviewer role separation,
**not fresh-context, cross-model, or proof-assistant independence**.
Earlier premise reviews are reused only for their exact scoped results;
they are not claimed to be previous reviews of these new statements.

Both stage-root protocols were reread completely: `DAG_PROTOCOL.md`
(283 lines) and `FILE_PROTOCOL.md` (145 lines). The two new YAML
files, all their route and premise records, and both complete new
proofs WM-1--WM-6 and IE-1--IE-8 were read. The recursive premise
chain was checked from its current nodes and complete proofs: C16
RW-1--RW-4, C15 PW-1--PW-6, and root-classical RC-1--RC-5.
The applicable old review was read in full for C15/C16, and the
root-classical review's F1 and input declaration were read. The new
registration and the relevant generated dependency view were inspected.
There are no external assumptions in the reviewed chain.

The complete 19-file input snapshot, eight decoded statement bindings,
premise lists, actual checker output, and runtime are recorded in
`artifacts/window-maximality-equality-review-rerun-20260907.txt`,
R1--R4, with SHA-256
`a574492ab5810fa52e547360bdd5af4c0951ea02e20e693adae143b1429c110b`.
In particular, the principal new frozen inputs are:

| Input relative to `grothendieck-group-orbit/` | SHA-256 |
|---|---|
| `proof-dag/nodes/GROTHORB.root-shift-window-maximality.yaml` | `33e9a70f92c55b97a9c9d539aca64a24570864bf8368e9e868b0b104d198dd97` |
| `proof-dag/nodes/GROTHORB.psd-antipodal-interior-equality.yaml` | `2c05dd04eb30317d75281996de66bd1615aa03e532644cde8b5411c9feee604c` |
| `artifacts/root-shift-window-maximality-20260907.md` | `7f71e16495b641883a3480434b5e2235c2ac3a6ec0a6537f2c0500bf447d878d` |
| `artifacts/psd-antipodal-interior-equality-20260907.md` | `892328079a880e9eb44e8b5eede13f3cc8708239ff8859b6db385d4e692dddff` |
| `tools/check_window_followups.py` | `1c84ff3eb0f15b29a27b6896035a3d7c3f991c334aecd910d2f30384adb16ca0` |

The supplied author-proof hashes match. The reviewer reran the existing
coordinator checker with `PYTHONDONTWRITEBYTECODE=1`, Python 3.9.6,
and assertions enabled (`sys.flags.optimize=0`). It exited zero and
its exact output matched the coordinator log. All input hashes and
decoded statement bindings were checked again at closeout.

The checker uses integer/Fraction arithmetic. Its C17 branch checks
the witness coefficients and selected parameter offsets only for
`r=3,...,12`; it does not optimize outside the known window. Its C18
branch builds eight exact Gram matrices with `N=1,2,3` and exhausts
every ordered full sign pair at one parameter `lambda=d_min/4` for
each matrix. It compares the complete maximizing-pair set, not only
the value or a proposed witness. Counts are 16, 256, or 4096 ordered
pairs. These finite checks include singular examples, but do not
prove the all-r or arbitrary-C claims. The universal findings below
rest on the analytic arguments. No new experiment or unregistered
proposition was introduced.

## Premise assembly checked for both new claims

The current C15 claim hash is
`sha256:98c4958c91dace11088aaff1ecc7b590bb982f84cc5d26c027bc8a2603beda38`.
It matches `psd-antipodal-window-review-20260907.md`, F1. The current
C16 claim hash is
`sha256:df62de9a7c9c2c2dd4e5512ea89a3374d63f3c3bbb6e6d41f4eff509732f05db`,
and its `psd-duplication-window` implication hash is
`sha256:81735fbe09238f4c5e32f9448ef5d0e01af445de76cb04e4d7df5421e20545ca`.
They match F2/F3 of that same frozen report, whose digest remains
`fb1e4d331ba9c657d9cda1208cd51af6d836fd41afb79eb24ecb5e8072651c7d`.
Whole-node file hashes have changed since the old pre-promotion
snapshot, but these decoded mathematical statements have not.

The root-classical premise has claim hash
`sha256:5894fbd5f0998222db98bbe3cbef23b0a723716a30125952c2db60e748375fca`,
matching its earlier applicable F1. Its proof again reduces the Gram
bilinear maximum to the root support function. Four roots per
coordinate pair contribute `4 max(|x_i|,|x_j|)`. Sorting the absolute
unit coordinates and applying Cauchy--Schwarz gives support maximum
`4||rho||`, attained by `rho=(r-1,...,0)` after normalization.
The resulting classical value is `2r(2r-1)/3`. This is a global
argument, not a small-r inference.

The C15 proof gives `beta_cl(C)=K=max_z z^T Cz` by PSD, and uses
finite independent sign completion and the exact four-term gap
reconstructed in F3 below to prove `2K-2N lambda` throughout its
closed interval. The fully antisymmetric diagonal pair matches it.
No positive-definiteness is required. For C16, the two positive roots
per coordinate pair give `N=r(r-1)` rows of U. The full matrix is
a row permutation of `[U;-U]`, and
`C=UU^T/[2(r-1)]` has diagonal `1/(r-1)` and
`D(C)=[U;-U][U;-U]^T/[4(r-1)]`. Sign-set permutation preserves
the shifted value. C15 at zero and the root-classical premise fix
`2 beta_cl(C)=2r(2r-1)/3`; C15 at the chosen parameter then gives
C16 with `2N=n`. Thus the actual complete premise arguments and
their parameter domains have been checked, not accepted from status
labels. No old equality theorem, D3 envelope, or unlisted external
result is needed.

## F1. GROTHORB.root-shift-window-maximality — PASS

Target: the exact C17 claim.

`reviewed_hash: sha256:4a217aec965420ef7e2a71b13ee1170bcd9c9bbfa966f976c87b77e036d099ee`

Exact parsed `claim.strip()` reviewed:

> For every integer r>=3, let W have as its rows all vectors epsilon e_i+eta e_j with 1<=i<j<=r and epsilon,eta in {+1,-1}, let n=2r(r-1), and put A_r=WW^T/[4(r-1)]. Among lambda>=0, beta_cl(A_r-lambda I_n)=2r(2r-1)/3-n lambda holds if and only if lambda<=1/[2(r-1)]. In particular, for every lambda>1/[2(r-1)] there is an explicit ordered sign pair scoring 2r(2r-1)/3-n lambda+4lambda-2/(r-1), strictly above that affine value.

Write `B_r=2r(2r-1)/3` and `lambda_*=1/[2(r-1)]`. The already
checked sufficient-window premise gives the claimed equality for
every `0<=lambda<=lambda_*`, including both endpoints. It does not
by itself say anything about maximality. The additional obstruction
is correctly derived from an explicit feasible ordered pair.

On each root row `w=epsilon e_i+eta e_j`, with i<j, assign the
baseline `s^0_w=epsilon`. Summing over the four roots of each pair
gives `4e_i`, hence `W^T s^0=4rho`, in any row order. Its Gram
value is `16||rho||^2/[4(r-1)]=B_r`. Choose
`h=e_(r-1)-e_r`; for every r>=3 it and its antipode are distinct
rows and satisfy `rho dot h=1`, `||h||^2=2`.

Alice changes only the -h baseline sign from -1 to +1; Bob changes
only the h sign from +1 to -1. These are legitimate independent
full sign vectors, with both untouched and changed entries still
in `{+1,-1}`. At h and -h Alice has +1 and Bob has -1; all other
coordinates agree with the baseline. Therefore

    W^T a=W^T b=4rho-2h,       a dot b=n-4.

Equality of the projected vectors is directly computed, not deduced
from PSD equality of an indefinite shifted matrix. Expanding their
squared norm gives

    a^T A_r b
      =(16||rho||^2-16(rho dot h)+4||h||^2)/[4(r-1)]
      =B_r-2/(r-1).

The full shifted score is accordingly

    B_r-2/(r-1)-lambda(n-4)
      =B_r-n lambda+4lambda-2/(r-1).

Its difference from the proposed affine optimum is precisely
`4(lambda-lambda_*)`. It is strictly positive for every
`lambda>lambda_*`, with no upper cutoff on lambda and no need for
the competitor to be globally optimal. Since a feasible score is a
lower bound on the optimum, equality with the old affine expression
is impossible anywhere above the endpoint. This also excludes a
later return to that affine expression. Combined with the premise,
it proves both directions of the iff over exactly `lambda>=0` and
the separately stated explicit-score assertion.

At `lambda=lambda_*`, the difference is zero and the premise
includes equality, so there is no endpoint gap. For `r=3`, the
root is `e_2-e_3`, n=12, and the competitor is `9-8lambda`, with
difference `4lambda-1` from `10-12lambda`; all indices and positive
denominators remain valid. These are substitutions in the general
proof, not dependencies on the finite checker or a D3 envelope.
The row-label definition works in any row ordering; equivalently,
simultaneously permuting the Gram matrix and both signs preserves
the value and the identity shift.

No assertion that this competitor equals the optimum outside the
window, or that it enumerates every endpoint optimizer, is needed
or made. The exact new maximality statement is supported by its new
obstruction, not retroactively attributed to the older sufficient
window review.

## F2. GROTHORB.root-shift-window-maximality / height-one-competitor — PASS

Target: the exact route implication, distinct from F1.

`reviewed_hash: sha256:b4042573a3c4cdb6b54b193e6b6a3b836098bce248af12275b22d71e5dca37bd`

Exact parsed `implication.strip()` reviewed:

> The registered sufficient-window theorem proves equality up to the endpoint. In the positive-root order U, with C=UU^T/[2(r-1)] and W=[U;-U], construct a sign pair whose ternary coordinates agree with the all-positive pattern except at one height-one root, where both antisymmetric coordinates vanish and the symmetric signs are opposite. Direct evaluation must establish the claimed competing affine score and its strict improvement beyond the endpoint.

The sole listed premise is `GROTHORB.root-extended-shift-window`.
It has been checked above with its complete recursive assembly. The
author includes all calculations establishing the new competitor,
so neither a half-root theorem nor a generic duplication equality
classification is an unlisted premise of this route.

The proposed coordinate prescription is implemented literally.
With U containing `e_i-e_j,e_i+e_j` for each i<j and k the row h,
the signs have blocks

    a_+=1,        a_-=-1+2E_k,
    b_+=1-2E_k,   b_-=-1.

Their coordinates are `p=q=1-E_k`, `u=E_k`, `v=-E_k`: precisely
one antisymmetric coordinate vanishes on each side, and the two
symmetric signs there are opposite. All other coordinates retain
the fully antisymmetric positive pattern. Because `U^T1=2rho`,
one obtains `U^Tp=2rho-h`,
`p^TCp=B_r/2-1/(r-1)`, and
`p dot q+u dot v=N-2`. Direct block multiplication gives the
full score `2[p^TCq-lambda(p dot q+u dot v)]`, exactly the F1
formula, with `2N=n`. This verifies the possible factor-two trap
independently in the registered coordinates.

For arbitrary original row order use `W=P[U;-U]` and the pair
`Pa,Pb`. The identity shift and sign domains are preserved by P.
The premise handles the entire closed lower interval; the computed
positive difference handles its entire complement among
nonnegative parameters. Thus the registered implication proves the
actual parent claim, including its explicit pair, with all and only
its stated project premise.

## F3. GROTHORB.psd-antipodal-interior-equality — PASS

Target: the exact C18 claim.

`reviewed_hash: sha256:746e10d42ef48a0bfe93d2cb1d504271c4778806a582dc5ca3d18949e9e5a97d`

Exact parsed `claim.strip()` reviewed:

> Let C be a real symmetric PSD N by N matrix with N>=1 and d_min=min_i C_ii>0, and put D(C)=(1/2)[C,-C;-C,C]. For every 0<lambda<d_min/2, the ordered sign pairs (a,b) attaining beta_cl(D(C)-lambda I_{2N}) are exactly a=b=(z,-z), where z in {+1,-1}^N maximizes z^T C z.

Let `K=max_z z^TCz`. Finiteness gives a maximizing sign, and the
PSD inequality `(s-t)^TC(s-t)>=0` gives `beta_cl(C)=K`.
The strict domain is contained in C15's closed domain, so the
already checked value is `beta_cl(D(C)-lambda I)=2K-2N lambda`.
This uses PSD only for C, not for the shifted matrix.

Start with completely arbitrary, independently chosen original signs
`a=(a_+,a_-)`, `b=(b_+,b_-)`. Their antipodal coordinates obey
`p_i^2+u_i^2=q_i^2+v_i^2=1`, with each coordinate in `{-1,0,1}`.
The inverse formulas `a=(p+u,u-p)`, `b=(q+v,v-q)` retain the full
ordered domain. In particular synchronization or full antisymmetry
has not been imposed before proving necessity. For the half-score
S and `x=(p+q)/2`, `y=(p-q)/2`, direct multiplication yields

    S=p^TCq-lambda(p dot q+u dot v),
    p^TCq=x^TCx-y^TCy.

For the independent finite sign distribution with means x_i, the
expectation is `E_x=x^TCx+sum_i d_i(1-x_i^2)<=K`: off-diagonal
moments factor and diagonal moments are one. This includes
deterministic coordinates and is a finite convex combination, not
an assumption that x itself is a sign vector or a sampled estimate.

Subtracting S from `K-N lambda`, the coordinate remainder is
`d_i(1-x_i^2)-lambda(1-p_iq_i-u_iv_i)`. The identity

    2(1-x_i^2)-(1-p_iq_i-u_iv_i)=(u_i+v_i)^2/2

follows by expanding x_i and using both coordinate norm relations.
It gives the exact half-gap to the optimum

    G=(K-E_x)+y^TCy
      +sum_i (d_i-2lambda)(1-x_i^2)
      +(lambda/2)||u+v||^2.

All four parts are nonnegative: E_x is bounded by K, C is PSD,
`|x_i|<=1`, and `d_i-2lambda>=d_min-2lambda>0`, with lambda
positive. The factors agree with the full-score value because
`G=(beta_cl(B)-a^TBb)/2`.

If the original pair is optimal, G=0. Every coordinate term in
the third part must vanish, forcing `x_i^2=1`. An average of two
numbers in `[-1,1]` can equal an endpoint only when both numbers
equal that endpoint; hence `p_i=q_i=x_i` for every i. Therefore
`p=q=z` is a sign vector, and the norm relations force `u=v=0`.
The inverse formulas give the literal equality `a=b=(z,-z)`, not
merely equality of their images under C. Also y=0 and
`E_x=z^TCz`; the remaining gap becomes `K-z^TCz`, forcing z to
maximize the quadratic form.

Conversely, any maximizing z and pair `a=b=(z,-z)` give
`2z^TCz-2lambda||z||^2=2K-2N lambda`, exactly the established
optimum. Thus sufficiency covers every stated pair, and necessity
excludes every other original ordered pair. No uniqueness of z or
quotient by swapping, switching, or global sign is asserted. Global
negation is already included by replacing z with -z.

Singular PSD matrices with positive diagonal are included: the
argument never inverts C or infers `y=0` from `y^TCy=0`. It obtains
y=0 only after the strict coordinate forcing. For N=1 and C=[d],
d>0, both z signs maximize K=d, and the proof gives exactly the
two diagonal ordered pairs with full signs `(1,-1)` and `(-1,1)`
throughout `0<lambda<d/2`. No nonempty off-diagonal sum is needed.

Both endpoints and zero-minimum-diagonal inputs are excluded by
the registered domain. At the upper endpoint strict coordinate
coefficients can disappear, so this forcing proof must not be
silently used there. At zero the last coefficient vanishes; that
observation is not itself evidence that the classification fails
there, as the author correctly states. No lower-endpoint result is
promoted by this review. For `d_min=0` the registered strict range
is empty. These exclusions are kept exactly as written, without
asserting an endpoint classification or another domain extension.

## F4. GROTHORB.psd-antipodal-interior-equality / strict-gap-coefficients — PASS

Target: the exact route implication, distinct from F3.

`reviewed_hash: sha256:efc78d327385e5bb26284efe100120667da70dc7b22540909eda65ce96e8669a`

Exact parsed `implication.strip()` reviewed:

> Use the established optimum value and reconstruct the full nonnegative gap identity for arbitrary ordered signs. Strictly positive coefficients C_ii-2lambda force every averaged antisymmetric coordinate to have square one at equality; recover the full signs and check equivalence to maximizing z^T C z.

The sole listed premise is `GROTHORB.psd-antipodal-linear-window`.
Its exact claim and complete proof were checked before it was used
to identify the optimum value. The parent hypotheses imply every
one of that premise's hypotheses. No pre-existing optimizer theorem
or positive-definiteness assumption is imported.

IE-2 supplies the elementary PSD identification of K and the finite
completion; IE-3--IE-4 reconstruct the full gap on the independent
ordered sign domain. IE-5's strict coordinate forcing and inverse
coordinate map recover the actual signs; IE-6 proves the reverse
direction for every maximizing z. F3 independently checks these
steps, including the half-score factor, singular inputs, and strict
domain. Thus the route establishes exactly the stated iff with its
single registered premise. There is no circular inference from the
desired equality classification or acceptance of an author label
as proof.

## Closeout

The four `reviewed_hash` values are SHA-256 of UTF-8 decoded YAML
`claim.strip()` or `implication.strip()`, distinct from whole-file
digests. Every quotation above was checked against the current parsed
string, and the exact premise lists were checked separately. The
19-file input snapshot and the reviewer rerun digest remained
unchanged at closeout. The report did not exist when work resumed
after the progress interruption, and was newly created rather than
overwriting any previous report. Only this report and the new rerun
artifact were written.

The four findings cover the assembled proofs, not just route syntax
or successful finite checks. They are a non-formalized same-model
correctness audit, not an originality assessment. C17 proves its
registered affine-window maximality but not the full envelope above
it; C18 proves only its registered strict-interior classification.
No claim, premise, route, author proof, protocol, coordinator run,
or earlier review was edited. This report and rerun are frozen on
completion; node integration is left to the coordinator. No further
research scope is opened.
