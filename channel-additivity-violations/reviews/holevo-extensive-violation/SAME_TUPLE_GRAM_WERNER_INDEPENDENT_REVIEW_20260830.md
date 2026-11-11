# Independent adversarial review of the same-tuple Gram and Werner-sector nodes

**Date:** 2026-08-30  
**Reviewer:** OpenAI Codex review agent  
**Reviewed nodes:**
`HEXT.same-tuple-rank-one-gram-contraction`,
`HEXT.same-tuple-near-orthogonal-gram-base-case`,
`HEXT.same-tuple-standard-decoupling-obstruction`,
`HEXT.same-tuple-werner-spectral-reduction`,
`HEXT.same-tuple-ppm-edge-gate`,
`HEXT.same-tuple-werner-centered-bound`, and
`HEXT.quantum-expander-werner-partial-transpose-interface`  
**Review status:** completed and immutable; later corrections require a new review object

## Independence and repository discipline

I performed this audit in a separately commissioned review context. I did not participate in the
proposer derivations or node registration, did not receive private proposer reasoning, did not
contact the proposer, and used no subagent. I reconstructed the matrix Cauchy--Schwarz argument,
both coefficient-Gram contractions, the real-Werner two-dimensional optimization, both spectral
edge tests, the partial-transpose factorization, and every probability/scope boundary
independently.

The canonical YAML, proposer artifacts, protocols, boundary nodes, and external source interface
were read-only. This report is the only durable repository file created by the audit. I did not
promote a node, edit a canonical claim, regenerate a view, stage, commit, or push.

## Executive verdict

The following six current claims merit `PROVED` at the exact hashes recorded in Section 1:

1. `HEXT.same-tuple-rank-one-gram-contraction`;
2. `HEXT.same-tuple-near-orthogonal-gram-base-case` as a conditional theorem on the stated
   uniform one-leg event, plus its deterministic `l_1` subclass;
3. `HEXT.same-tuple-standard-decoupling-obstruction` with exactly its route-level scope;
4. `HEXT.same-tuple-werner-spectral-reduction`;
5. `HEXT.same-tuple-ppm-edge-gate` for the nonzero normalized projectors in the intended `m>=2`
   regime; and
6. `HEXT.quantum-expander-werner-partial-transpose-interface` as an interface obstruction, not a
   counterexample to the centered bound.

`HEXT.same-tuple-werner-centered-bound` remains **UNRESOLVED** and does not merit `PROVED` or
`CERTIFIED*`. Its current `CONJECTURED` level is defensible as a registered analytic target.
Expectation safety, fixed normalized moments, and Lipschitz concentration around an unknown
median do not prove the extreme-eigenvalue statement.

No fatal defect was found. Finding STGW-IR-10 records one nonfatal mathematical presentation
repair in the decoupling artifact and two wording/quantifier clarifications. None invalidates the
six passing node claims.

## 1. Immutable inputs and exact claim hashes

| object | SHA-256 |
|---|---|
| `DAG_PROTOCOL.md` | `d8775b511431e6e9dc7a5be6200af80bd612e7e7d5f5ff10bb14ef748791a095` |
| `FILE_PROTOCOL.md` | `d9d6fb57a26fef3b70fc05bda74a29101d83a43df60e06eaeb345e76980fc595` |
| `nodes/HEXT.same-tuple-rank-one-gram-contraction.yaml` | `b749051e81a40e0405e9abedf17595e1853f256c3a250387bec3f90e19100ff5` |
| `nodes/HEXT.same-tuple-near-orthogonal-gram-base-case.yaml` | `d8b2c248776e854b01d7e94f013ce69b3dd940f01114042d9355e1be8af6716c` |
| `nodes/HEXT.same-tuple-standard-decoupling-obstruction.yaml` | `dd8a143f2cec965e50181678ea145010588d15d694238e751d68e4e1acf24751` |
| `nodes/HEXT.same-tuple-werner-spectral-reduction.yaml` | `5256dc717f5bd76bd3b820f60f44fbd3a0333e838fe92ea978c33e9ff2436125` |
| `nodes/HEXT.same-tuple-ppm-edge-gate.yaml` | `f12486c6e3dc76c2b39ce98124ab28948a221adf1177b592581222c928738174` |
| `nodes/HEXT.same-tuple-werner-centered-bound.yaml` | `b1bf77b043f5ca0283ab197a5caf25329c8fe56677ed595141db953eb4d11973` |
| `nodes/HEXT.quantum-expander-werner-partial-transpose-interface.yaml` | `81c4124e22ecdbc796fd5221f98451c9f23bb74465ac3afb8eec5d07a10219b9` |
| `artifacts/SAME_TUPLE_RANK_ONE_GRAM_CONTRACTION_20260830.md` | `113996091e768fea4cb9e3c9e8370a2612785adcf75dca4dbd9443ab81e9bd44` |
| `artifacts/WERNER_FLIP_SECTOR_SAME_TUPLE_GATE_20260830.md` | `5a9dc94ec0f02f76065f87134244dcde4781486d112d194dbcbc8ec73de9f056` |
| inherited base-case artifact | `836eae645a2ad15dd3676865b3896d1280ed66542a3622f6f7b246d936364198` |

The repository-normalized exact claim hashes are:

| node | exact claim hash | recommendation |
|---|---|---|
| `HEXT.same-tuple-rank-one-gram-contraction` | `sha256:0f7e0fc7ba6dadd1be87364480a46a6e5ea6652d51e6df667cd11dac1723a78a` | `PROVED` |
| `HEXT.same-tuple-near-orthogonal-gram-base-case` | `sha256:f696b7476eacc99632efd2056b820b3a6cd25e010bc4360ea85dc4128dff6be9` | `PROVED` |
| `HEXT.same-tuple-standard-decoupling-obstruction` | `sha256:c927613b272448126f741a49ebe11a706a6eee9c518a47e5db24144803af5cd7` | `PROVED` |
| `HEXT.same-tuple-werner-spectral-reduction` | `sha256:241ced6a8c0a7c97de7cc172d9793bb96c032287da21ad5eb4a074dfb3004e67` | `PROVED` |
| `HEXT.same-tuple-ppm-edge-gate` | `sha256:33a54f48d45ea1dfd0e6d10b8efc1e0ec0dd820628325ce08aee77c3084472a4` | `PROVED` |
| `HEXT.same-tuple-werner-centered-bound` | `sha256:c221c71b9f3cb3294d7c9c7d979cf1a154042ea4ec013f95d3fc7955c2c38da5` | unresolved; no promotion |
| `HEXT.quantum-expander-werner-partial-transpose-interface` | `sha256:ba3f076f3eb0ebd6c4cb0c53b9115b7eeda37970a58357ebe13b6339f7ba320c` | `PROVED` |

The hashes are `sha256(claim.strip())` after YAML folding and CRLF normalization. A finding is
stale for promotion if its reviewed claim changes.

The expander context was checked against M. B. Hastings,
[*Random Unitaries Give Quantum Expanders*](https://arxiv.org/abs/0706.0556). The passing
partial-transpose finding does not rely on importing an exact Hastings constant: it grants the
optimistic `O(m^-1/2)` second-singular-value estimate and proves that this input alone still does
not cross the partial-transpose interface.

## 2. Independent algebra smoke test

As a non-evidentiary check, I used the Python standard library and the explicit `(m,d)=(3,3)`
tuple consisting of the identity, cyclic shift, and Fourier unitary. Independent constructions
gave the following maximum entrywise residuals:

| identity | residual |
|---|---:|
| rank-one positive factorization | `5.56e-17` |
| right square function `sum B_v^*B_v=m C^*(overline(Z^*Z))` | `2.23e-16` |
| left square function `sum C_a^*C_a=m C^*(ZZ^*)` | `2.26e-16` |
| both dense maximally-entangled Grams equal `I/m` | `2.22e-16` |
| `M_U(I)=I` | `6.67e-17` |
| `M_U(F_m)=R_U` | `5.55e-17` |
| Hermiticity of `R_U` | `2.78e-17` |
| `R_U^Gamma=G_U^*G_U` | `5.57e-17` |
| partial transpose of the sharp `H_0` example | `2.22e-16` |

The proof verdicts are exact and do not rely on this smoke test.

## 3. Findings

### Finding STGW-IR-01 — PASS: rank-one Gram contraction and load-bearing conjugation

**Stable source locators:** Gram artifact Section 2, equations (5)--(11); rank-one-Gram node
claim.  
**Reviewed claim hash:**
`sha256:0f7e0fc7ba6dadd1be87364480a46a6e5ea6652d51e6df667cd11dac1723a78a`.

Write

\[
 T_Z=\sum_vU_v\otimes B_v,
 \qquad B_v=\sum_a\overline{z_{v,a}}U_a.
\]

For every vector `xi`, ordinary Cauchy--Schwarz on the `m` summands gives the Loewner inequality

\[
 T_Z^*T_Z\preceq m I\otimes\sum_vB_v^*B_v.
\]

The square function is exactly

\[
 \sum_vB_v^*B_v
 =\sum_{a,b}\left(\sum_vz_{v,a}\overline{z_{v,b}}\right)U_a^*U_b
 =mC^*(\overline{Z^*Z}).
\]

The entrywise conjugation is necessary: `(Z^*Z)_(a,b)` has the conjugate order. Since
`overline(Z^*Z)=Z^T overline Z` is positive with trace one, taking norms after dividing by `m^2`
is legitimate. Exchanging the two tensor legs similarly gives `mC^*(ZZ^*)`. Therefore

\[
 \|\mathcal M_U(|z\rangle\langle z|)\|_\infty
 \le\min\{\|C^*(\overline{Z^*Z})\|_\infty,\|C^*(ZZ^*)\|_\infty\}.
\]

**Verdict:** exact deterministic theorem; merits `PROVED`.

### Finding STGW-IR-02 — PASS: diagonal Grams and all maximally entangled coefficient vectors

**Stable source locators:** Gram artifact Section 3, equations (12)--(16); rank-one-Gram node
claim.  
**Reviewed claim hash:**
`sha256:0f7e0fc7ba6dadd1be87364480a46a6e5ea6652d51e6df667cd11dac1723a78a`.

If either Gram is diagonal, its trace-one diagonal contribution maps under `C^*` to `I/m`.
Finding STGW-IR-01 then gives the output bound `1/m` for every deterministic unitary tuple. This
includes dense full-rank matrices `Z=WD` or `Z=DW` with a diagonal singular-value factor and, in
particular, every maximally entangled coefficient `Z=V/sqrt(m)`, whose two Grams both equal
`I/m`.

This conclusion uses orthogonality of coefficient rows or columns, not a false `U(m)` invariance
of Kraus labels. It does not extend to arbitrary dense full-rank `Z`.

**Verdict:** the corollaries and their scope are exact.

### Finding STGW-IR-03 — PASS: deterministic and conditional near-orthogonal Gram radii

**Stable source locators:** Gram artifact Section 4, equations (17)--(26); near-orthogonal-Gram
node claim.  
**Reviewed claim hash:**
`sha256:f696b7476eacc99632efd2056b820b3a6cd25e010bc4360ea85dc4128dff6be9`.

For either trace-one Gram `G`, its off-diagonal part has trace zero and

\[
 C^*(G)=I/m+C^*(\operatorname{Off}G).
\]

The deterministic unitary-word triangle inequality gives

\[
 \|C^*(G)\|_\infty
 \le\frac{1+\|\operatorname{Off}G\|_{\ell_1}}m,
\]

so off-diagonal entrywise `l_1` norm at most `A-1` is sufficient.

On the uniform one-leg trace-zero event, put
`alpha=sqrt((A-1)/m)`. The Gram contraction gives, simultaneously for every coefficient vector,

\[
 \|\mathcal M_U(|z\rangle\langle z|)\|_\infty
 \le\frac1m+\alpha
 \min_{\sigma\in\{L,R\}}\|\operatorname{Off}(G_\sigma)\|_F.
\]

The target follows when the minimum is at most `alpha`, because
`alpha^2=(A-1)/m`. With `A-1=9(1+eta)^2/m`, the radius is
`3(1+eta)/m` in the inherited `eta>=0` regime. No net over `z` is needed: all randomness is in
the already uniform one-leg event.

The full-Gram effective-rank check `r_eff>=m/A` and the dense non-flat Hadamard example were also
recomputed and correctly delimit, rather than refute, the route.

**Verdict:** exact conditional/deterministic claim; merits `PROVED` without implying a general
rank-one theorem.

### Finding STGW-IR-04 — PASS WITH NONFATAL ARTIFACT REPAIR: standard decoupling obstruction

**Stable source locators:** Gram artifact Section 6, equations (30)--(32), especially the prose
after equation (32); standard-decoupling node claim.  
**Reviewed claim hash:**
`sha256:c927613b272448126f741a49ebe11a706a6eee9c518a47e5db24144803af5cd7`.

Independent Steinhaus phases change the chaos to

\[
 \sum_{v,a}\overline{z_{v,a}}\epsilon_v\epsilon_aU_v\otimes U_a.
\]

Replacing the second phase by an independent `delta_a` leaves the same projective unitary matrix
on both legs: `epsilon_i U_i` and `delta_i U_i` differ only by a scalar. Their joint law is not two
independent Haar tuples. Thus phase-only decoupling cannot invoke an independent-leg strong-norm
theorem.

For any comparison strong enough actually to transfer a norm bound, a multiplicative loss
`C>1` turns `||T_ind||<=sqrt(A m)` into at best
`||T_same||<=C sqrt(A m)`, hence

\[
 \|\mathcal M_U\|\le C^2A/m>A/m.
\]

A universal constant bounded away from one cannot be absorbed by the `O(1/m)` relative slack;
the node correctly leaves open an instance-specific `1+O(1/m)` comparison with strong tails.

Equation (32) in the artifact, however, is written only as a comparison of **expected** norms.
Such a first-moment inequality does not itself imply a pointwise, high-probability, or second-moment
bound, and one cannot literally square it using equation (2). The correct presentation is: an
expectation-only comparison is already insufficient to transfer the desired high-probability
claim; even if upgraded to a transferable norm/tail comparison, its fixed factor would square to
`C^2`. This is a nonfatal repair to the artifact exposition, not a failure of the scoped node
claim.

**Verdict:** the exact route obstruction merits `PROVED`; it neither refutes the same-tuple claim
nor every conceivable decoupling method.

### Finding STGW-IR-05 — PASS: exact `P_+` and `P_-` spectral edges

**Stable source locators:** Werner artifact Section 2, equations (1)--(11); PPM-edge node claim.  
**Reviewed claim hash:**
`sha256:33a54f48d45ea1dfd0e6d10b8efc1e0ec0dd820628325ce08aee77c3084472a4`.

The adjoint of the `(v,a)` summand in `R_U` is the `(a,v)` summand, and each summand is unitary.
Thus `R_U` is Hermitian with spectrum in `[-1,1]`; both `I+R_U` and `I-R_U` are positive.
Since

\[
 \mathcal M_U(P_\pm/\sqrt{r_\pm})
 =\frac{I\pm R_U}{2\sqrt{r_\pm}},
 \qquad r_\pm=m(m\pm1)/2,
\]

the two output norms are exactly

\[
 \frac{1+\lambda_{\max}(R_U)}{2\sqrt{r_+}},
 \qquad
 \frac{1-\lambda_{\min}(R_U)}{2\sqrt{r_-}}.
\]

Multiplying the target by the normalizations gives precisely

\[
 \lambda_{\max}(R_U)\le A\sqrt{2(1+1/m)}-1
\]

and

\[
 \lambda_{\min}(R_U)\ge-[A\sqrt{2(1-1/m)}-1].
\]

At fixed `eta` these approach the upper and lower values `plus-or-minus(sqrt(2)-1)`. Passing the
two edge tests is much weaker than controlling every Werner linear combination.

**Verdict:** exact for the intended `m>=2` domain in which both normalized projectors exist;
merits `PROVED`.

### Finding STGW-IR-06 — PASS: exact real-Werner centered-spectrum equivalence

**Stable source locators:** Werner artifact Section 3, equations (12)--(21); Werner-reduction node
claim.  
**Reviewed claim hash:**
`sha256:241ced6a8c0a7c97de7cc172d9793bb96c032287da21ad5eb4a074dfb3004e67`.

For `Y=alpha I+beta F_m` with real coefficients,

\[
 \|Y\|_2^2=m^2(\alpha^2+\beta^2)+2m\alpha\beta,
 \qquad
 \mathcal M_U(Y)=\alpha I+\beta R_U.
\]

For a fixed eigenvalue `lambda` of `R_U`, inversion of the coefficient Gram matrix gives

\[
 \sup_{(\alpha,\beta)\ne0}
 \frac{|\alpha+\beta\lambda|^2}{\|Y\|_2^2}
 =\frac{1+\lambda^2-2\lambda/m}{m^2-1}.
\]

The supremum over coefficients commutes with the maximum over the finite spectrum. Comparing with
`A^2/m^2` and completing the square yields

\[
 (\lambda-1/m)^2\le(A^2-1)(1-m^{-2})
\]

for every eigenvalue, exactly equivalent to

\[
 \|R_U-I/m\|_\infty\le\sqrt{(A^2-1)(1-m^{-2})}.
\]

For `m=1` the displayed Gram inverse degenerates because `I=F_1`, but both sides of the claimed
equivalence are directly true; the intended application has `m` vastly larger than one.

**Verdict:** exact two-dimensional reduction; merits `PROVED`. It does not establish the random
centered bound.

### Finding STGW-IR-07 — UNRESOLVED: expectation, fixed moments, and concentration do not prove the centered bound

**Stable source locators:** Werner artifact Sections 4--6 and Section 9.2, equations (22)--(32)
and (43)--(44); centered-bound node claim and caveats.  
**Reviewed claim hash:**
`sha256:c221c71b9f3cb3294d7c9c7d979cf1a154042ea4ec013f95d3fc7955c2c38da5`.

For `v!=a`, `U_v^*U_a` is Haar and the first unitary moment gives

\[
 \mathbb E R_U=I/m+\frac{m-1}{md}F_d.
\]

This verifies that the matrix expectation is centered to `O(1/d)`, but convexity gives
`||E R_U||<=E||R_U||`, not the reverse.

For `S_U=R_U-I/m`, the only nonzero free-word contribution to the normalized second moment has
`x=a,y=v`, so

\[
 \lim_{d\to\infty}\mathbb E d^{-2}\operatorname{Tr}(S_U^2)
 =\frac{m-1}{m^3}.
\]

This is a bulk `Theta(1/m)` scale. A bounded number of constant-sized outlier eigenvalues is
invisible to every fixed normalized moment in dimension `d^2`.

Direct telescoping gives the correct tuple Lipschitz constant `4/sqrt(m)`. Phase-invariant Haar
concentration therefore supplies an exponent of order `m d t^2` around the **unknown median**. At
the Werner radius `t=Theta(m^-1/2)` this exponent is of order `d`, but no audited argument places
the median inside the target interval.

**Verdict:** the probabilistic centered-spectrum claim is neither proved nor refuted. Keep it
unresolved at exact claim hash
`sha256:c221c71b9f3cb3294d7c9c7d979cf1a154042ea4ec013f95d3fc7955c2c38da5`.
The fixed-`m`, fixed-`eta`, `d->infinity` order must be preserved in any future proof.

### Finding STGW-IR-08 — PASS: expander factorization and the dimension-`d` partial-transpose loss

**Stable source locators:** Werner artifact Section 7, equations (33)--(38b); expander-interface
node claim.  
**Reviewed claim hash:**
`sha256:ba3f076f3eb0ebd6c4cb0c53b9115b7eeda37970a58357ebe13b6339f7ba320c`.

With

\[
 G_U=m^{-1}\sum_vU_v\otimes\overline{U_v},
 \qquad \Pi=|\Omega_d\rangle\langle\Omega_d|,
\]

every summand fixes `Omega_d`, and direct multiplication gives the exact identity

\[
 G_U^*G_U=R_U^\Gamma.
\]

Granting the optimistic expander estimate
`||(I-Pi)G_U(I-Pi)||=O(m^-1/2)` yields

\[
 R_U^\Gamma=\Pi+H_U,
 \qquad 0\preceq H_U\preceq O(m^{-1})(I-\Pi).
\]

On returning through partial transpose,

\[
 R_U=F_d/d+H_U^\Gamma.
\]

The general operator-norm bound is `||H_U^Gamma||<=d||H_U||`. Positivity and `H_U Pi=0` do not
improve it dimension-independently: the explicit matrix

\[
 H_0=P_{\rm sym}^{(d)}-\Pi
\]

is positive, lies below `I-Pi`, and has norm one, while

\[
 H_0^\Gamma=(I+d\Pi)/2-F_d/d
\]

has norm of order `d/2`. Scaling preserves the order-`d` amplification.

**Verdict:** the standard expander gap alone does not imply the centered Werner bound. The exact
interface obstruction merits `PROVED`; an instance-specific delocalization theorem remains open.

### Finding STGW-IR-09 — PASS: deterministic counterexample and conclusion scope

**Stable source locators:** Werner artifact Sections 8--11, equations (39)--(44); both artifacts'
boundary sections.

For the all-equal deterministic tuple, `R_U=I`, and

\[
 \|\mathcal M_U(P_+/\sqrt{r_+})\|_\infty
 =m^{-1}\sqrt{2m/(m+1)}.
\]

This violates the target when `A^2<2m/(m+1)`, including the stated large-`m` regime. The tuple has
zero probability under independent Haar sampling, so it rules out an all-tuple theorem but does
not refute the centered probabilistic node. For this tuple the normalized `P_-` maps to zero.

The Gram nodes cover rank-one coefficients only. The Werner nodes cover a two-dimensional real
coefficient sector only. None proves arbitrary Hermitian coefficients, the general same-tuple
strong-norm node, global all-coefficient `n=2`, any growing completely bounded amplification, or
`n>=3`.

**Verdict:** all counterexample and non-propagation boundaries are correctly scoped.

### Finding STGW-IR-10 — NONFATAL REPAIR / WORDING: remaining defects

**Stable source locators:** Gram artifact Section 6.2 after equation (32); PPM-edge node claim;
centered-bound node claim.

1. **Nonfatal mathematical presentation repair:** an expected-norm comparison such as artifact
   equation (32) cannot be squared to obtain an output operator-norm bound. The corrected logic is
   stated in Finding STGW-IR-04. This does not invalidate the node's route obstruction.
2. **Domain wording:** the normalized antisymmetric coefficient `P_-/sqrt(r_-)` exists only for
   `m>=2`. The intended project regime satisfies this overwhelmingly, but the PPM node would be
   more self-contained with the domain stated.
3. **Probability wording:** the centered node should explicitly say that `eta` is fixed along with
   `m` before `d->infinity`. This is the artifact's intended quantifier and is required to keep the
   threshold fixed.

No other constant, conjugation, normalization, or scope defect was found.

## 4. Promotion recommendations

The following exact review bindings support promotion without changing their scopes:

- rank-one Gram contraction: Finding STGW-IR-01, reviewed hash
  `sha256:0f7e0fc7ba6dadd1be87364480a46a6e5ea6652d51e6df667cd11dac1723a78a`;
- near-orthogonal Gram base case: Finding STGW-IR-03, reviewed hash
  `sha256:f696b7476eacc99632efd2056b820b3a6cd25e010bc4360ea85dc4128dff6be9`;
- standard-decoupling obstruction: Finding STGW-IR-04, reviewed hash
  `sha256:c927613b272448126f741a49ebe11a706a6eee9c518a47e5db24144803af5cd7`;
- Werner spectral reduction: Finding STGW-IR-06, reviewed hash
  `sha256:241ced6a8c0a7c97de7cc172d9793bb96c032287da21ad5eb4a074dfb3004e67`;
- `P_+/-` edge gate: Finding STGW-IR-05, reviewed hash
  `sha256:33a54f48d45ea1dfd0e6d10b8efc1e0ec0dd820628325ce08aee77c3084472a4`;
- expander/partial-transpose interface: Finding STGW-IR-08, reviewed hash
  `sha256:ba3f076f3eb0ebd6c4cb0c53b9115b7eeda37970a58357ebe13b6339f7ba320c`.

Do not promote the centered probabilistic node. Finding STGW-IR-07 binds its unresolved current
claim hash
`sha256:c221c71b9f3cb3294d7c9c7d979cf1a154042ea4ec013f95d3fc7955c2c38da5`.

I make no canonical level change in this review.

## 5. Limitations

This review does not prove or refute the centered high-probability bound, compute growing-order
Weingarten moments, establish an instance-specific partial-transpose delocalization result, or
prove the general same-tuple strong-norm lemma. The Hastings source was used only to check that the
artifact addresses the standard quantum-expander interface; no exact external expander constant
is load-bearing. The smoke test checks algebraic identities rather than asymptotic probability or
optimal constants.

