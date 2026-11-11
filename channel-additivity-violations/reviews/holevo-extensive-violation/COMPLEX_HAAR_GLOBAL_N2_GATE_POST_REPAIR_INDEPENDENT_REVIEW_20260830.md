# Post-repair independent adversarial review of the complex-Haar global n=2 gate and base cases

**Date:** 2026-08-30  
**Reviewer:** OpenAI Codex review agent  
**Reviewed nodes:** `HEXT.complex-haar-global-n2-output-dual-gate` and
`HEXT.same-tuple-two-leg-scalar-base-cases`  
**Boundary node:** `HEXT.same-tuple-two-leg-scalar-strong-norm`  
**Review status:** completed and immutable; any later correction must be a new review object

## Independence and repository discipline

I performed this post-repair audit in a separately commissioned review context. I did not
participate in the proposer derivation or in applying the repairs, did not receive private
proposer reasoning, did not contact the proposer, and used no subagent. I reconstructed the
output-duality identity, finite-net step, bosonic hierarchy dimension substitution, and every
listed scalar base case independently.

The canonical YAML nodes, proposer artifacts, protocols, earlier review, and external theorem
interfaces were read-only. This report is the only durable repository file created by this
re-review. I did not promote either node, edit a canonical claim, regenerate a view, stage, commit,
or push.

## Executive verdict

**Finding CHG2-PRR-VERDICT-OUTPUT-DUAL — PASS; the current output-dual claim merits `PROVED`.**

The norm duality is exact, the repaired dimensions `m^4` and `m^4-1` are correct, and a finite
coefficient net upgrades pointwise convergence in probability when the free-model estimate has a
uniform positive slack. This is a proved conditional reduction. It neither proves the missing
same-tuple convergence premise nor establishes the global physical `n=2` result by itself.

This verdict is bound to exact claim hash
`sha256:b91aeedc542797eda56f8895c548ebe33bd68121ed1bf2626506650d15e10bb3`.

**Finding CHG2-PRR-VERDICT-BASE-CASES — PASS; the current base-case claim merits `PROVED`.**

Every class in the node follows from an exact deterministic identity or from exactly the event
stated in the claim. The low coefficient-Schmidt-rank conclusion is simultaneous over all eligible
vectors on the single event `B_U<=2+delta`. The Bell and normalized-flip bounds are deterministic.
No proved row reaches dense full-rank coefficients, the normalized symmetric/antisymmetric
projectors, or arbitrary Hermitian coefficients.

This verdict is bound to exact claim hash
`sha256:29a7d833912a8c7e0ca140b1a8d2383dbc37fa6d8cb4b33a7f381546d74c11ef`.

**Finding CHG2-PRR-VERDICT-REPAIR — PASS.**

The repaired hierarchy scale is `O(d^2/k)`, not `O(d^4/k)`, for the available fully bosonic
extension hierarchy. Consequently the generic sufficient extension level is of order
`m^3 d^2`. The qualitative conclusion remains only a method obstruction: generic hierarchy
convergence supplies no fixed level uniform in `d`; it does not prove failure of a special
low-level certificate on these random instances.

No fatal or patch-required mathematical defect remains in the reviewed claims. Finding
CHG2-PRR-10 records four wording-only clarifications.

## 1. Immutable inputs and claim binding

| object | SHA-256 |
|---|---|
| `DAG_PROTOCOL.md` | `d8775b511431e6e9dc7a5be6200af80bd612e7e7d5f5ff10bb14ef748791a095` |
| `FILE_PROTOCOL.md` | `d9d6fb57a26fef3b70fc05bda74a29101d83a43df60e06eaeb345e76980fc595` |
| `proof-dag/nodes/HEXT.complex-haar-global-n2-output-dual-gate.yaml` | `16a0780b2b9ab6bf30ca5b04ac6d3e4b18b1e858822ecb5cedae0033826277da` |
| `proof-dag/nodes/HEXT.same-tuple-two-leg-scalar-base-cases.yaml` | `4aa8e11144f919df81fd4ef092658a55f8e94f1fc38c42b7197ce5ad316fa74c` |
| `proof-dag/nodes/HEXT.same-tuple-two-leg-scalar-strong-norm.yaml` | `c87176309c9f6d1031db80bb586c2ee5759ae2920c7db304f8ca669b5167c423` |
| `artifacts/COMPLEX_HAAR_GLOBAL_N2_CONCENTRATION_GATE_20260830.md` | `5c0dac3fa5f39db7e43ae24bb35b83f3c70ca99c4e9d1a841200d53b26c359ce` |
| `artifacts/SAME_TUPLE_TWO_LEG_SCALAR_BASE_CASES_20260830.md` | `836eae645a2ad15dd3676865b3896d1280ed66542a3622f6f7b246d936364198` |
| earlier immutable independent review | `edeeca7578912a624412900f0e9fcb19e858532a12d8c74a62e0441994dc6223` |

The repository-normalized exact claim hashes are:

| node | exact claim hash |
|---|---|
| `HEXT.complex-haar-global-n2-output-dual-gate` | `sha256:b91aeedc542797eda56f8895c548ebe33bd68121ed1bf2626506650d15e10bb3` |
| `HEXT.same-tuple-two-leg-scalar-base-cases` | `sha256:29a7d833912a8c7e0ca140b1a8d2383dbc37fa6d8cb4b33a7f381546d74c11ef` |
| boundary node `HEXT.same-tuple-two-leg-scalar-strong-norm` | `sha256:f782bd3d6ea6f158cba4d91f13389f53df317690647918098d3da8a69e374647` |

The claim hashes are `sha256(claim.strip())` after YAML folding and CRLF normalization. Findings
CHG2-PRR-02 and CHG2-PRR-03 review the first exact claim. Findings CHG2-PRR-04 through
CHG2-PRR-09 review the second. This report becomes stale for promotion purposes if the
corresponding claim changes.

The repaired hierarchy interface was checked against Christandl--König--Mitchison--Renner,
*One-and-a-half quantum de Finetti theorems*, arXiv:quant-ph/0602130v4, especially the Bose
symmetric error scale `2 k h/n` after renaming their local dimension to `h`. Only the order and
dimension substitution are used here.

## 2. Independent smoke test

As a non-evidentiary algebra check, I used only the Python standard library and the explicit
`(m,d)=(3,3)` tuple consisting of the identity, cyclic shift, and Fourier unitary. I constructed
`C^*`, `M_U`, and both sides of the relevant identities independently. The largest entrywise
residuals were:

| identity | maximum residual |
|---|---:|
| simple tensor, equation (19) | `1.39e-16` |
| fully diagonal, equation (13) | `1.14e-16` |
| one-leg diagonal, equation (16) | `1.57e-16` |
| rank-one factorization, equation (25) | `2.84e-17` |
| canonical Bell specialization | `5.55e-17` |
| normalized flip, equation (39) | `2.78e-17` |
| Hermiticity of `R_U` | `2.78e-17` |

The proof verdicts below are algebraic and do not rely on this smoke test.

## 3. Findings

### Finding CHG2-PRR-01 — PASS: the bosonic hierarchy repair has the correct `d^2/k` scale

**Stable source locators:** global-gate artifact Section 8, equations (30)--(32), especially the
paragraph following equation (32); repaired-node event
`independent-review-repair-applied`.

The lifted one-particle space is the two-copy physical input, so its complex dimension is

\[
 h=\dim(\mathbb C^d\otimes\mathbb C^d)=d^2.
\]

The exact cone is generated by Hartree powers
`|psi><psi| tensor |psi><psi|`. A valid outer hierarchy can therefore demand a fully bosonic
`k`-particle extension on `(C^h)^{tensor k}`. The Bose-symmetric finite de Finetti theorem gives,
for a fixed two-particle marginal, trace-norm error `O(h/k)`. Substituting `h=d^2` yields

\[
 O(h/k)=O(d^2/k).
\]

Since `||Q_U||_infinity<=1`, the same trace-norm error controls the objective. Resolving an
available margin `s=Theta(m^-3)` therefore requires `k` at least on the order of `m^3 d^2` up to
universal constants. The older ordinary permutation-invariant estimate `O(h^2/k)=O(d^4/k)` is
still a valid weaker route, and the artifact now labels it non-sharp.

**Verdict:** the quantitative repair is correct. It proves a generic hierarchy-cost obstruction,
not an instance-specific failure theorem.

### Finding CHG2-PRR-02 — PASS: exact output duality

**Stable source locators:** global-gate artifact Section 9, equations (33)--(35); output-dual node
claim, lines 5--11.  
**Reviewed claim hash:**
`sha256:b91aeedc542797eda56f8895c548ebe33bd68121ed1bf2626506650d15e10bb3`.

For the channel `N=C tensor C` and any density operator `rho`, `N(rho)` is Hermitian and positive.
Hilbert--Schmidt duality, followed by the adjoint relation, gives

\[
 \sup_{\rho\in\mathcal D}\|N(\rho)\|_2
 =\sup_{\substack{Y=Y^*\\\|Y\|_2=1}}
   \lambda_{\max}(N^*(Y)).
\]

The coefficient sphere is invariant under `Y -> -Y`. Thus the outer supremum contains both the
largest and the negative smallest eigenvalue of every `N^*(Y)`, and

\[
 \sup_Y\lambda_{\max}(N^*(Y))
 =\sup_Y\|N^*(Y)\|_\infty.
\]

The maximum over all density operators equals the maximum over pure inputs: alternatively this
follows directly from convexity of the norm. Squaring the `A/m` norm threshold gives the physical
purity threshold `A^2/m^2`. No minimax interchange, replica relaxation, or positivity enlargement
is hidden.

**Verdict:** exact and suitable for `PROVED` as a reduction.

### Finding CHG2-PRR-03 — PASS: repaired dimension and finite coefficient net

**Stable source locators:** global-gate artifact Section 9, equations (34)--(37); output-dual node
claim, lines 8--11.  
**Reviewed claim hash:**
`sha256:b91aeedc542797eda56f8895c548ebe33bd68121ed1bf2626506650d15e10bb3`.

Hermitian matrices in `M_(m^2)` form a real vector space of dimension `(m^2)^2=m^4`; its
Hilbert--Schmidt unit sphere has intrinsic dimension `m^4-1`. The repaired node now distinguishes
these correctly.

Because `N^*` is unital and positive, it contracts the operator norm on Hermitian inputs. Hence

\[
 \|N^*(Y-Y')\|_\infty
 \le \|Y-Y'\|_\infty
 \le \|Y-Y'\|_2.
\]

For fixed `m`, choose a finite Hilbert--Schmidt net whose radius is smaller than the assumed
uniform free-model slack. Pointwise convergence in probability at each of its finitely many
points, a finite union bound, and the displayed Lipschitz inequality yield the uniform target.
The covering exponent may be taken as `m^4`, despite the sphere's intrinsic dimension being
`m^4-1`; both are independent of `d`.

**Verdict:** the repaired net claim is exact, conditional only on the separately OPEN same-tuple
convergence premise and positive uniform slack.

### Finding CHG2-PRR-04 — PASS: extension of the one-leg event to all complex coefficients

**Stable source locators:** base-case artifact Section 2, equations (4)--(7); base-case node claim,
lines 6--9.  
**Reviewed claim hash:**
`sha256:29a7d833912a8c7e0ca140b1a8d2383dbc37fa6d8cb4b33a7f381546d74c11ef`.

Write `X=alpha I/sqrt(m)+X_0`, with `Tr X_0=0`. The two coefficient components are orthogonal in
Hilbert--Schmidt norm. The scalar component has output norm `|alpha|/sqrt(m)`, while the trace-zero
event gives `sqrt((A-1)/m)||X_0||_2`. Cauchy--Schwarz in these two scalar components gives

\[
 \|C^*(X)\|_\infty
 \le \sqrt{A/m}\sqrt{|\alpha|^2+\|X_0\|_2^2}
 =\beta\|X\|_2.
\]

The decomposition is complex-linear and does not require Hermiticity.

**Verdict:** the one-leg event used by all conditional base cases has exactly the claimed scope.

### Finding CHG2-PRR-05 — PASS: matrix units, entrywise sparsity, and full diagonal coefficients

**Stable source locators:** base-case artifact Sections 3 and 4.1, equations (8)--(13); base-case
table, rows 1--3; base-case node claim, lines 7--10.  
**Reviewed claim hash:**
`sha256:29a7d833912a8c7e0ca140b1a8d2383dbc37fa6d8cb4b33a7f381546d74c11ef`.

Every matrix unit maps to `m^-2` times a unitary tensor unitary, so its norm is exactly `m^-2`.
The triangle inequality therefore gives

\[
 \|\mathcal M_U(Y)\|_\infty
 \le m^{-2}\|Y\|_{\ell_1(\mathrm{entries})}.
\]

Thus the target holds deterministically when the entrywise `l_1` norm is at most `Am`. For a
fully diagonal coefficient every unitary word is the identity, so

\[
 \mathcal M_U(Y)=m^{-2}\operatorname{Tr}(Y)I,
 \qquad |\operatorname{Tr}Y|\le m\|Y\|_2.
\]

For unit Hilbert--Schmidt norm this is at most `1/m`. These conclusions require no random event.

**Verdict:** correct, including arbitrary complex coefficients in the named subclasses.

### Finding CHG2-PRR-06 — PASS: one-leg-diagonal and simple-tensor classes

**Stable source locators:** base-case artifact Sections 4.2 and 5, equations (14)--(23);
base-case table, rows 4--5; base-case node claim, lines 7--10.  
**Reviewed claim hash:**
`sha256:29a7d833912a8c7e0ca140b1a8d2383dbc37fa6d8cb4b33a7f381546d74c11ef`.

If the coefficient is supported on `v=w`, defining
`Z_(a,b)=sum_v Y_((v,a),(v,b))` gives the exact factorization

\[
 \mathcal M_U(Y)=m^{-1}I\otimes C^*(Z),
 \qquad \|Z\|_2\le\sqrt m\|Y\|_2.
\]

On the one-leg event, a normalized coefficient therefore has norm at most
`beta/sqrt(m)=sqrt(A)/m<=A/m`. The `a=b` case is identical.

For a simple tensor the exact algebra is

\[
 \mathcal M_U(Y_1\otimes Y_2)=C^*(Y_1)\otimes C^*(Y_2).
\]

Applying the one-leg event twice gives the target because
`||Y_1 tensor Y_2||_2=||Y_1||_2||Y_2||_2`. For sums of simple tensors the unavoidable projective
norm `sum_s |t_s|` appears; the artifact correctly does not extend this proof to arbitrary `Y`.

**Verdict:** correct and exactly conditional on the stated one-leg event.

### Finding CHG2-PRR-07 — PASS: rank-one factorization, sparsity, and coefficient-Schmidt threshold

**Stable source locators:** base-case artifact Section 6, equations (24)--(33d); base-case table,
rows 6--7 and 10; base-case node claim, lines 9--12.  
**Reviewed claim hash:**
`sha256:29a7d833912a8c7e0ca140b1a8d2383dbc37fa6d8cb4b33a7f381546d74c11ef`.

For a unit vector `z`, direct expansion gives the positive factorization

\[
 \mathcal M_U(|z\rangle\langle z|)=m^{-2}T_z^*T_z,
 \qquad
 T_z=\sum_{v,a}\overline{z_{v,a}}U_v\otimes U_a.
\]

If `z` has support size `s`, then `||T_z||<=||z||_1<=sqrt(s)`, proving the target for
`s<=Am` deterministically.

If the coefficient matrix of `z` has rank `r`, take a singular-value decomposition with
`sum_j s_j^2=1`. On the single event

\[
 B_U:=\sup_{\|x\|_2=1}\left\|\sum_vx_vU_v\right\|_\infty\le2+\delta,
\]

the two factors in each Schmidt term give

\[
 \|T_z\|_\infty
 \le B_U^2\sum_js_j
 \le(2+\delta)^2\sqrt r.
\]

Consequently

\[
 \|\mathcal M_U(|z\rangle\langle z|)\|_\infty
 \le \frac{(2+\delta)^4r}{m^2}\le\frac A m
\]

when `r<=Am/(2+delta)^4`. Because `B_U` is uniform in the coefficient vector, the conclusion is
simultaneous over every eligible `z`; no two-leg rank-`r` net is used.

The artifact's universal rank-one bound `(2+delta)^2/m` follows independently from operator
Cauchy--Schwarz, but it is correctly marked non-target-tight and is absent from the node claim.

**Verdict:** the fourth power, rank threshold, and simultaneous quantifier are all correct.

### Finding CHG2-PRR-08 — PASS: canonical Bell and normalized flip coefficients

**Stable source locators:** base-case artifact Section 7, equations (34)--(42); base-case table,
rows 8--9 and 11; base-case node claim, lines 12--13.  
**Reviewed claim hash:**
`sha256:29a7d833912a8c7e0ca140b1a8d2383dbc37fa6d8cb4b33a7f381546d74c11ef`.

The canonical Bell vector has exactly `m` nonzero coefficient coordinates, so its rank-one
factor obeys `||T_Omega||<=sqrt(m)` and its output norm is at most `1/m` deterministically. This
does not extend to an arbitrary maximally entangled coefficient, because Kraus labels lack a full
`U(m)` mixing symmetry.

For the flip, `||F_m||_2=m` and direct substitution gives

\[
 \mathcal M_U(F_m/m)=R_U/m,
 \qquad
 R_U=m^{-2}\sum_{v,a}U_v^*U_a\otimes U_a^*U_v.
\]

The summands are unitary, so `||R_U||<=1`; pairing `(v,a)` with `(a,v)` also makes `R_U`
Hermitian. Hence the normalized flip is safe deterministically. The normalized symmetric and
antisymmetric projectors involve `I plus-or-minus R_U` with a different normalization and are
correctly left open at the target constant.

**Verdict:** both node-level deterministic claims and their symmetry-sector boundaries are exact.

### Finding CHG2-PRR-09 — PASS: conclusion scope and the OPEN boundary are preserved

**Stable source locators:** global-gate artifact Section 10; base-case artifact Sections 8--10;
base-case node caveats, lines 16--27; boundary-node claim and caveats.  
**Reviewed claim hash:**
`sha256:29a7d833912a8c7e0ca140b1a8d2383dbc37fa6d8cb4b33a7f381546d74c11ef`.

The base-case node proves target bounds only on its listed strict coefficient subclasses. It does
not establish same-tuple strong-norm convergence even for all rank-one coefficients, much less all
Hermitian coefficients. The boundary node remains properly `OPEN`, and neither reviewed node
implies `n>=3`, arbitrary matrix amplification, or all-copy regularization.

**Verdict:** no over-propagation or quantifier inflation was found.

### Finding CHG2-PRR-10 — WORDING ONLY: four nonblocking clarity defects

**Stable source locators:** base-case artifact Section 3 immediately before equation (8);
base-case node claim, lines 7--13; output-dual node claim, lines 6--8.

1. The phrase “Equation (8) gives the exact spectrum” should say “exact operator identity.” The
   equation determines the norm exactly but does not list the tuple-dependent eigenvalues. The
   subsequent norm conclusion is correct.
2. The base-case claim puts the fully diagonal and entrywise-`l_1` classes under the one-leg-event
   umbrella, even though those classes, as well as sparse rank-one coefficients, are
   deterministic. This is a logically valid underclaim, but the final phrase “Independently of
   randomness” mentioning only Bell and flip can obscure the stronger deterministic scope.
3. For its high-probability interpretation, the base-case node should explicitly say “for every
   fixed `delta>0`, with `m` fixed before `d->infinity`.” The artifact states these quantifiers in
   Section 6.2. The node's algebraic implication on the event is correct as written.
4. For complete self-containment, the output-dual node's shorthand `sup_rho` could specify that
   `rho` ranges over density operators on the two-copy input. The artifact states this as
   `rho in D`, and the intended global target is unambiguous in context.

**Severity:** presentation only. None changes a bound, premise, conclusion, claim hash verdict, or
recommended evidence level.

## 4. Promotion recommendations

- `HEXT.complex-haar-global-n2-output-dual-gate` merits `PROVED` for the exact reduction stated at
  claim hash `sha256:b91aeedc542797eda56f8895c548ebe33bd68121ed1bf2626506650d15e10bb3`.
  Its assessment must continue to say that the same-tuple premise is OPEN and that global `n=2`
  itself is not thereby proved.
- `HEXT.same-tuple-two-leg-scalar-base-cases` merits `PROVED` for the strict classes and conditional
  events stated at claim hash
  `sha256:29a7d833912a8c7e0ca140b1a8d2383dbc37fa6d8cb4b33a7f381546d74c11ef`.
  Promotion must not delete its exclusions or imply the general boundary node.
- `HEXT.same-tuple-two-leg-scalar-strong-norm` remains `OPEN` at exact claim hash
  `sha256:f782bd3d6ea6f158cba4d91f13389f53df317690647918098d3da8a69e374647`.

I make no canonical promotion in this review.

## 5. Limitations

This review does not prove or refute the same-tuple two-leg strong-norm lemma, re-review the
Collins--Youn free-model constant, or infer the physical global `n=2` theorem. It does not cover
`n>=3`, a growing completely bounded amplification, or regularized all-copy entropy. The
one-leg-event probability theorem is not needed for the base-case claim's conditional algebra;
only its use as the named high-probability source of `B_U<=2+delta` was checked at the stated fixed
`m`, fixed positive `delta`, `d->infinity` quantifier. The numerical smoke test checks identities,
not asymptotic probability or optimal constants.

