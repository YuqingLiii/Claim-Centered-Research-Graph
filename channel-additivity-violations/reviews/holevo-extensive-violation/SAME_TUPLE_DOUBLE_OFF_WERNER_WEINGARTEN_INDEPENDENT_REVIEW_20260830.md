# Independent review: positive double-off neighborhoods and finite-d Werner Weingarten tails

Date: 2026-08-30

Reviewer: OpenAI Codex, fresh independent review context
`/root/weyl_majorization_audit`.

Review status: complete. This is an immutable project-level review record. It does not edit or
promote any canonical YAML node.

## Independence declaration

I did not author the six claims, either proposer artifact, or the Collins--Matsumoto source. I did
not participate in the proposer-side derivations. I reconstructed the displayed identities and
inequalities from the definitions, checked the current folded YAML claim strings independently,
inspected the relevant pages of the local primary PDF, and used fresh smoke tests only as
cross-checks. The smoke tests are not used in place of the analytic arguments.

I read `DAG_PROTOCOL.md` and `FILE_PROTOCOL.md` before issuing this verdict. Their SHA-256 digests
at review time were respectively
`d8775b511431e6e9dc7a5be6200af80bd612e7e7d5f5ff10bb14ef748791a095` and
`d9d6fb57a26fef3b70fc05bda74a29101d83a43df60e06eaeb345e76980fc595`.

## Executive verdict

All six amended nodes pass and are safe to promote to `PROVED` at the exact hashes recorded below.
The diagonal-core claim now correctly restricts its trace-greater-than-`A` examples to `m>A`.
Both Weingarten assumptions now locate the exact series on PDF p. 8 and the coefficient bounds on
PDF p. 9, with the mechanical `PDF-1.4` anchor.

One nonfatal bibliographic wording defect remains in the prose artifact: Sections 3 and 11
attribute the exact expansion to Theorems 3.1--3.2 alone, although Theorem 2.7 is the direct source
of that expansion. The amended canonical node metadata is correct, the primary source fully
supports both claims, and this wording issue does not block their promotion.

Nothing in either Weingarten result proves the growing-order minimal positive-genus contraction-
skeleton bound. `HEXT.same-tuple-werner-centered-bound` must remain unresolved.

## 1. Immutable inputs and hashes

The following SHA-256 values are raw file hashes computed during this review.

| Input | SHA-256 |
|---|---|
| `artifacts/SAME_TUPLE_POSITIVE_DOUBLE_OFF_NEIGHBORHOODS_20260830.md` | `dabbbe5eb4c614dddd2b45d6c77fe0a19969bf0c89844f305d66c5840695eb11` |
| `artifacts/WERNER_FINITE_D_WEINGARTEN_REMAINDER_GATE_20260830.md` | `d1a3d33f569084331967720c132a037e82824ca825ed8ec754e3f8e8387dd2a7` |
| `artifacts/primary-sources/collins-matsumoto-1701.04493.pdf` | `42becfc0db3534ade549855727aa759fe8531b95c49d99851a56f53515f2d172` |
| `nodes/HEXT.same-tuple-double-off-projective-interface.yaml` | `e7878d51ee6f9970fd444a9379ce69aa5a15d0f345d20f8cb11ebd49e304234f` |
| `nodes/HEXT.same-tuple-positive-rook-plus-double-off-direction.yaml` | `3ca7b755d66607e21718c0bf67f4b49304309f4174ef477137560ed861a0c037` |
| `nodes/HEXT.same-tuple-positive-diagonal-core-projective-neighborhood.yaml` | `ff88a14411f8140102e847685a6d91da668cf731c86f9dbad6908f164e8b39d7` |
| `nodes/HEXT.same-tuple-double-off-projective-frobenius-obstruction.yaml` | `1305abb96f158d77fa96e7cf9ca4fd03e6bd4a4ed6725f18e8dcbe92cf1fb314` |
| `nodes/HEXT.werner-monotone-weingarten-tail-summability.yaml` | `74b3515e0b5bf5579038c7d3b350e88d75d6f79440ccc46b983c577ab32c9e1b` |
| `nodes/HEXT.werner-uniform-cn-per-genus-obstruction.yaml` | `edcc3fd8f70ddadecc8a81f40b331452a0b7b968c7c3d69a18535135619d713c` |
| reviewed rook-support premise node | `4aef5abd6e186528d76d440f1f3d79f2ca24faffe44726b37c8661d7ace86c12` |
| prior rook/collision independent review | `324010420582732a0c4496d75ccd3b31f810bcb661891ca257e7a17a40bacde2` |
| current centered-bound frontier node | `aa4aae9e6fab25ab1af754ac5bb9baf128c0b05d121482be1e1929b0b6e1077e` |

The node paths in the table are under `holevo-extensive-violation/proof-dag/`; artifact and review
paths are under `holevo-extensive-violation/`.

### Exact current claim hashes and disposition

The claim hashes are `sha256(claim.strip())` after YAML folding and CRLF normalization.

| Node | Exact current claim hash | Review disposition |
|---|---|---|
| `HEXT.same-tuple-double-off-projective-interface` | `sha256:7e150bfef0b4882e9c2858ce3dcf2523558be9a7122d7b08f5568cdb365ca403` | PASS; safe for `PROVED` |
| `HEXT.same-tuple-positive-rook-plus-double-off-direction` | `sha256:d25db65f677c5e7732801360cbbe4def6fc525b17b80d18092a71fd818044d54` | PASS; safe for `PROVED` |
| `HEXT.same-tuple-positive-diagonal-core-projective-neighborhood` | `sha256:de69a5d63c775d4273ffcf8e784f61c1cf9a39d0f68d1666c6b76312bddffefc` | PASS; safe for `PROVED` |
| `HEXT.same-tuple-double-off-projective-frobenius-obstruction` | `sha256:4b03893e83c6661ce45095e33d496b17d30461c397ad0d9be83e786b2eb6458c` | PASS; safe for `PROVED` |
| `HEXT.werner-monotone-weingarten-tail-summability` | `sha256:e47cd4541145cc59fcd04cf217f738d0ceb6c126508210d4c169af7fc0c8c0e4` | PASS; safe for `PROVED` |
| `HEXT.werner-uniform-cn-per-genus-obstruction` | `sha256:1499b208141da056c999303931ca974eeeb0cbe1466a69ee3342e74aba7a2e2c` | PASS; safe for `PROVED` |

## 2. Fresh cross-checks

I ran a fresh read-only Python/Numpy smoke test with seed `20260830` using `m=5,d=4`. It gave:

- `||M_U(X tensor Z)-C^*(X) tensor C^*(Z)||_F = 4.85e-15` for random complex
  zero-diagonal factors;
- for the explicit rank-two family at `A=2.8`,
  `||E_0||_F=1`, `pi_X(E_0)/||E_0||_F=1.414213562373095`, minimum eigenvalue
  `0.1949902507`, Hilbert--Schmidt norm `1`, and trace `4.9997500187>A`;
- `(2A-1)+(A-1)^2=7.84=A^2` numerically;
- at `p=4,g=3`, all `3^3=27` explicit paired level-four backtrack paths returned to the
  identity and obeyed the monotonicity order;
- for one test degree profile `(4,3,1)` and total excess `g=3`, the composition sum was
  `0.6023` times the multinomial upper bound; and
- for `N=27,d=10^6`, `theta=6.9427e-6` and `theta/(1-theta)=6.9428e-6`.

These tests checked indexing, tensor-leg normalization, the Schmidt ratio, the explicit
backtracking injection, and the geometric-tail arithmetic. The findings below are analytic.

## 3. Findings

### Finding STDW-IR-01 -- PASS: the double-off projective interface has the stated exact constant

**Applies to:** `HEXT.same-tuple-double-off-projective-interface`, exact claim hash
`sha256:7e150bfef0b4882e9c2858ce3dcf2523558be9a7122d7b08f5568cdb365ca403`.

`Delta_1` and `Delta_2` are commuting Hilbert--Schmidt orthogonal projections. Hence

\[
 \Pi_X=(I-\Delta_1)(I-\Delta_2)=I-\Pi_R
\]

is the orthogonal projection onto the tensor product of the two zero-diagonal matrix spaces. Every
`E` in this range therefore has projective decompositions

\[
 E=\sum_j X_j\otimes Z_j,
 \qquad \operatorname{diag}X_j=\operatorname{diag}Z_j=0.
\]

For a simple tensor, direct substitution into the four-index definition gives the exact identity

\[
 \mathcal M_U(X\otimes Z)=C^*(X)\otimes C^*(Z).
\]

Zero diagonal implies zero trace, and the stipulated event applies to complex matrices, so it can
be applied separately to both factors even when a projective decomposition is not Hermitian term
by term. With
`alpha^2=(A-1)/m`, tensor-norm multiplicativity and the triangle inequality give

\[
 \|\mathcal M_U(E)\|_\infty
 \le {A-1\over m}\sum_j\|X_j\|_F\|Z_j\|_F.
\]

Taking the infimum proves exactly the current claim. No positivity, Hermiticity, probabilistic
conclusion, or Frobenius replacement is silently introduced. This node is safe for `PROVED`.

### Finding STDW-IR-02 -- PASS: the rook-core plus one double-off direction closes at exactly `A/m`

**Applies to:** `HEXT.same-tuple-positive-rook-plus-double-off-direction`, exact claim hash
`sha256:d25db65f677c5e7732801360cbbe4def6fc525b17b80d18092a71fd818044d54`.

Let `s=||Y_R||_F` and `e=||E||_F`. Orthogonality of the rook and double-off sectors gives
`s^2+e^2=1`. The already reviewed positive rook theorem is homogeneous and yields

\[
 \|\mathcal M_U(Y_R)\|_\infty\le {\sqrt{2A-1}\over m}s.
\]

For the single simple tensor, `pi_X(E)=||E||_F=e`, so Finding STDW-IR-01 gives the second term
`(A-1)e/m`. Therefore

\[
 \|\mathcal M_U(Y_R+E)\|_\infty
 \le {\sqrt{2A-1}\,s+(A-1)e\over m}
 \le {\sqrt{(2A-1)+(A-1)^2}\over m}={A\over m}.
\]

Separate positivity of `Y_R` is load-bearing because the rook projection is not positive. Total
positivity is the condition placing the sum in the positive coefficient class. There is indeed no
additional bound on `e`: the proof uses the full unit-circle budget `s^2+e^2=1`. The stated
operator-norm neighborhood `Y_R >= rho I`, `||E||_infinity<=rho` is also sufficient by the
Loewner inequality `E>=-||E||_infinity I`. This node is safe for `PROVED` with its existing scope
caveats.

### Finding STDW-IR-03 -- PASS: diagonal-core threshold and amended trace scope are exact

**Applies to:** `HEXT.same-tuple-positive-diagonal-core-projective-neighborhood`, exact current
claim hash
`sha256:de69a5d63c775d4273ffcf8e784f61c1cf9a39d0f68d1666c6b76312bddffefc`.

For a positive fully diagonal `D`,

\[
 \mathcal M_U(D)={\operatorname{Tr}D\over m^2}I,
 \qquad \operatorname{Tr}D\le m\|D\|_F.
\]

With `s=||D||_F`, `e=||E||_F`, the diagonal and double-off sectors are orthogonal, so
`s^2+e^2=1`. Finding STDW-IR-01 proves

\[
 \|\mathcal M_U(D+E)\|_\infty
 \le {s+(A-1)\pi_X(E)\over m}.
\]

If `pi_X(E)<=kappa_A e` and
`kappa_A^2=(A+1)/(A-1)`, then

\[
 s+(A-1)\pi_X(E)
 \le \sqrt{1+(A-1)^2\kappa_A^2}\sqrt{s^2+e^2}=A.
\]

Thus the target inequality and projective/Frobenius threshold are correct.

For orthonormal zero-diagonal Hermitian families,

\[
 E_0={1\over\sqrt r}\sum_{j=1}^rX_j\otimes Z_j
\]

has Schmidt singular values all equal to `1/sqrt(r)`, hence Frobenius norm one and projective norm
`sqrt(r)`. The dimension `m(m-1)` of the zero-diagonal space gives the stated rank limit, and the
identity Schmidt direction is orthogonal to all `X_j,Z_j`, so
`(I+tE_0)/sqrt(m^2+t^2)` has coefficient Schmidt rank exactly `r+1`. It is positive definite for
sufficiently small nonzero `t`.

The remaining trace is

\[
 \operatorname{Tr}Y_t={m^2\over\sqrt{m^2+t^2}}\longrightarrow m.
\]

Therefore trace greater than `A` is available precisely when `m>A` (with sufficiently small
nonzero `t`). The amended canonical claim now states that necessary qualifier and its caveat
correctly notes that only the explicit trace example, not the conditional neighborhood
inequality, uses `m>A`. The target theorem, rank range, positivity, and trace scope all pass. This
amended node is safe for `PROVED`.

### Finding STDW-IR-04 -- PASS: the projective/Frobenius obstruction is exact and route-scoped

**Applies to:** `HEXT.same-tuple-double-off-projective-frobenius-obstruction`, exact claim hash
`sha256:4b03893e83c6661ce45095e33d496b17d30461c397ad0d9be83e786b2eb6458c`.

Under the Hilbert tensor identification, the projective norm is the nuclear norm of the associated
coefficient operator. If its Schmidt singular values are `sigma_j`, then

\[
 \pi_X(E)=\sum_j\sigma_j,
 \qquad \|E\|_F=(\sum_j\sigma_j^2)^{1/2}.
\]

For `r` equal nonzero singular values the ratio is exactly `sqrt(r)`. Since either zero-diagonal
factor space has complex dimension `m(m-1)`, ranks through `m(m-1)` occur and the ratio can reach
`sqrt(m(m-1))=Theta(m)`. Thus no dimension-free projective-to-Frobenius comparison covers the
whole double-off unit sphere. The node correctly limits its conclusion to the projective triangle
route and makes no assertion against cancellation or against the original same-tuple target. It is
safe for `PROVED`.

### Finding STDW-IR-05 -- PASS: amended primary-source locators match the theorem chain

**Applies to:** both Weingarten nodes and Sections 3 and 11 of
`WERNER_FINITE_D_WEINGARTEN_REMAINDER_GATE_20260830.md`.

I inspected the complete relevant local-PDF pages. The precise source chain is:

- PDF p. 6, Lemma 2.5: path expansion in the Weingarten graph;
- PDF p. 8, Theorem 2.7: the exact parity-refined series
  `(-1)^|pi| d^(p+|pi|) Wg_d(pi)=sum_(g>=0) #P(pi,|pi|+2g)d^(-2g)`;
- PDF pp. 8--9, Lemma 2.8: identification with monotone transposition factorizations;
- PDF p. 9, Theorem 3.1: for every `g>=0`,
  `(p-1)^g P_0(pi)<=P_g(pi)<=(6p^(7/2))^g P_0(pi)`; and
- PDF p. 9, Theorem 3.2: the normalized summed bound when
  `d>sqrt(6)p^(7/4)`.

This exactly supports the monotone path coefficient bound and, together with Theorem 2.7, the
series used by the artifact. The theorem symbols, exponent `7/2`, and dimension threshold
`sqrt(6)p^(7/4)` all match.

The amended node assumptions now say `Exact expansion on PDF p. 8 and path bounds on PDF p. 9;
file anchor PDF-1.4`, which is accurate and mechanically locatable. The prose artifact still says
in Sections 3 and 11 that Theorems 3.1--3.2 supply the exact expansion; strictly, Theorem 2.7 is
the direct source and Theorems 3.1--3.2 supply the coefficient and summed estimates. This is a
nonfatal bibliographic wording defect in the artifact. It does not affect the derivation, the
amended canonical assumptions, or the promotion verdict.

### Finding STDW-IR-06 -- PASS: the multi-label tail is a uniform geometric correction

**Applies to:** `HEXT.werner-monotone-weingarten-tail-summability`, exact claim hash
`sha256:e47cd4541145cc59fcd04cf217f738d0ceb6c126508210d4c169af7fc0c8c0e4`.

In the two trace factors there are `2N` unstarred and `2N` starred unitary factors. For every
nonzero balanced term, the common per-label degree `p_v` therefore obeys

\[
 \sum_vp_v=2N,
 \qquad p_v\le2N.
\]

For a fixed edge sequence and fixed permutation pair `(sigma_v,tau_v)` for every label, the
Kronecker index equalities and loop count are fixed. Increasing a monotone excess `g_v` changes
only the Weingarten coefficient, contributes `d^(-2g_v)`, and does not change its sign. Writing
`a_v=6p_v^(7/2)`, Theorem 3.1 gives, at total excess `g`,

\[
 \sum_{\sum_vg_v=g}\prod_vP_{g_v}(\pi_v)
 \le (\prod_vP_0(\pi_v))
      \sum_{\sum_vg_v=g}\prod_va_v^{g_v}
 \le (\prod_vP_0(\pi_v))(\sum_va_v)^g.
\]

The final inequality follows from the multinomial coefficients, all at least one. Since
`x -> x^(7/2)` is superadditive on nonnegative inputs,

\[
 \sum_va_v\le6(\sum_vp_v)^{7/2}=6(2N)^{7/2}.
\]

After restoring `d^(-2g)`, summation over `g>=1` gives exactly

\[
 {\theta_{N,d}\over1-\theta_{N,d}},
 \qquad \theta_{N,d}={6(2N)^{7/2}\over d^2},
\]

whenever `theta<1`. This condition is stronger than every individual convergence condition in
the relevant regime. For every fixed `c`, the bound is uniform over integers
`N<=c log d` and is
`O((log d)^(7/2)/d^2)=o(1)`.

The claim is deliberately skeletonwise: it does not bound the sum of minimal-path skeleton
weights. With the amended source locator verified in Finding STDW-IR-05, this node is safe for
`PROVED` at its current claim hash.

### Finding STDW-IR-07 -- PASS: repeated labels refute the literal `C^N`-per-excess target

**Applies to:** `HEXT.werner-uniform-cn-per-genus-obstruction`, exact claim hash
`sha256:1499b208141da056c999303931ca974eeeb0cbe1466a69ee3342e74aba7a2e2c`.

For `pi=id_p`, each chosen `i in {1,...,p-1}` gives the directed two-solid-step excursion

\[
 id_p\longrightarrow(i,p)\longrightarrow id_p.
\]

Concatenating `g` excursions leaves all larger transposition entries equal to `p`, hence satisfies
the weak monotonicity rule, and gives `(p-1)^g` distinct paths before dashed deletion. This
independently realizes the lower bound needed by the node.

For the repeated Werner edge sequence `(1,2)^N`, both trace words are
`(U_1^*U_2)^N`. Each of labels 1 and 2 has balanced degree `N`; choosing an identity Weingarten
permutation for one label and the minimal path for the other realizes a coefficient containing
`(N-1)^g`. For `N>=3`, this exceeds any prescribed `C^N` once `g` is large enough. The displayed
formula `g>N log C/log(N-1)` in the artifact assumes `C>1`; `0<C<=1` is even easier. This omitted
domain in the explanatory formula does not alter the exact node claim.

Every such term retains `d^(-2g)`, and the complete repeated-word integral is small:
`U_1^*U_2` is Haar and `E|Tr(H^N)|^2=min(N,d)`, hence equals `N` for `N<=d`. Thus the node
correctly scopes the obstruction to an absolute coefficientwise proof route and makes no adverse
moment or probability inference. With the amended source locator verified in Finding STDW-IR-05,
this node is safe for `PROVED` at its current claim hash.

### Finding STDW-IR-08 -- UNRESOLVED: the centered-spectrum claim still lacks minimal-skeleton control

**Applies to:** the scope boundary of both Weingarten nodes and current
`HEXT.same-tuple-werner-centered-bound`.

The tail lemma controls only additional monotone backtracking above a fixed permutation skeleton.
Minimal monotone paths can already have positive topological genus because their Kronecker loop
count can be deficient. The earlier exponential cyclic-collision count controls the fixed-order
annular/free-reduction support, not the absolute mass of these nonplanar minimal skeletons.

Consequently none of the audited results proves a bound on `E Tr(S_U^N)` uniformly through
`N=c_m log d`, a high-probability extreme-norm estimate, or a generic Haar counterexample. A bound
of the proposed form `C_0^N N^(alpha h)` per handle remains a sufficient but unproved next lemma.
The centered-spectrum node must stay `CONJECTURED`.

## 4. Promotion recommendations

Safe to promote at the current exact claim hashes:

1. `HEXT.same-tuple-double-off-projective-interface`, using Finding STDW-IR-01;
2. `HEXT.same-tuple-positive-rook-plus-double-off-direction`, using Finding STDW-IR-02;
3. `HEXT.same-tuple-positive-diagonal-core-projective-neighborhood`, using amended-claim Finding
   STDW-IR-03;
4. `HEXT.same-tuple-double-off-projective-frobenius-obstruction`, using Finding STDW-IR-04;
5. `HEXT.werner-monotone-weingarten-tail-summability`, using Findings STDW-IR-05--06; and
6. `HEXT.werner-uniform-cn-per-genus-obstruction`, using Findings STDW-IR-05 and STDW-IR-07.

The remaining artifact-only attribution wording noted in Finding STDW-IR-05 is worth correcting
in a future prose repair but does not block any of these six promotions.

Do not promote `HEXT.same-tuple-werner-centered-bound` on this evidence.

## 5. Limitations

- I verified the Collins--Matsumoto statements and their match to the local use; I did not
  independently reprove the published path-count theorem from first principles.
- The one-leg trace-zero event is a premise of the double-off results. I reviewed the deductions on
  that event, not a probability proof that the event holds.
- I did not enumerate all finite-dimensional contraction skeletons. Their uncontrolled
  minimal-path positive-genus mass is precisely the remaining gate.
- The numerical checks are smoke tests and do not enlarge any theorem's dimension, positivity,
  rank, or probability scope.
