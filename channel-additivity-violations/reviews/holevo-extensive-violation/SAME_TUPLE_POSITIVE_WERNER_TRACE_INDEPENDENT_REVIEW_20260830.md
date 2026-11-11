# Independent adversarial review of positive-coefficient extensions and the Werner trace-method gate

**Date:** 2026-08-30  
**Reviewer:** OpenAI Codex review agent  
**Reviewed nodes:**
`HEXT.same-tuple-positive-partial-trace-contraction`,
`HEXT.same-tuple-near-diagonal-positive-base-case`,
`HEXT.same-tuple-gram-safe-spectral-nuclear-base-case`,
`HEXT.same-tuple-positive-summation-obstruction`, and
`HEXT.werner-modulus-square-majorant-obstruction`  
**Re-audited boundary node:** `HEXT.same-tuple-werner-centered-bound`  
**Review status:** completed and immutable; any later correction requires a new review object

## Independence and repository discipline

I performed this audit in a separately commissioned review context. I did not participate in the
proposer derivations or node registration, did not receive private proposer reasoning, did not
contact the proposer, and used no subagent. I reconstructed the two positive partial-trace Loewner
inequalities, their conjugation conventions, every trace/nuclear threshold, the cross-term
polarization, the exact forward/reversal trace formula, and the singleton-label majorant count
independently.

The canonical YAML, proposer artifacts, protocols, earlier reviews, and external source interface
were read-only. This report is the only durable repository file created by the audit. I did not
promote a node, edit a canonical claim, regenerate a view, stage, commit, or push.

## Executive verdict

All five newly registered claims merit `PROVED` at the exact hashes in Section 1, with their
present strict scopes:

1. the positive partial-trace contraction is an exact deterministic Loewner theorem;
2. the near-diagonal positive class is exact on the stated uniform one-leg event, with a separate
   deterministic entrywise condition;
3. the Gram-safe spectral nuclear class follows from the exact cross-term factorization and does
   not extend to general rank two;
4. the positive summation obstruction proves a route loss, not failure of the positive target;
5. the modulus-square majorant obstruction is exact in the intended `m>=3`, growing-moment
   regime, but applies only to `Q_(2k)`, not to the reversal-correlated moment.

The updated evidence and frontier of `HEXT.same-tuple-werner-centered-bound` are correctly scoped.
That node remains mathematically unresolved and should stay `CONJECTURED`. The new artifact gives
an exact trace formula, a safe return-sector estimate, a failed positive majorant, and a precise
missing logarithmic-degree lemma; it does not prove the centered high-probability claim.

No fatal or patch-required defect was found. Finding STPW-IR-08 records two domain/quantifier
clarifications that should remain visible when the majorant obstruction is promoted.

## 1. Immutable inputs and exact claim hashes

| object | SHA-256 |
|---|---|
| `DAG_PROTOCOL.md` | `d8775b511431e6e9dc7a5be6200af80bd612e7e7d5f5ff10bb14ef748791a095` |
| `FILE_PROTOCOL.md` | `d9d6fb57a26fef3b70fc05bda74a29101d83a43df60e06eaeb345e76980fc595` |
| `nodes/HEXT.same-tuple-positive-partial-trace-contraction.yaml` | `a7d36aae8242ec63bd2b69c67f655baf2f727e41ab0080be785a71fba45f0cda` |
| `nodes/HEXT.same-tuple-near-diagonal-positive-base-case.yaml` | `ba02bc93c63af81ed81eaacd8b1b0728021e3865dfcd6e1a76e14e128432fc1c` |
| `nodes/HEXT.same-tuple-gram-safe-spectral-nuclear-base-case.yaml` | `b1967e27abb921f280a9c54b3943ab90b2706cfe4a0ea6e5b3560f5252c16e2f` |
| `nodes/HEXT.same-tuple-positive-summation-obstruction.yaml` | `2817c38c6b01d35cbb121cea27a771d4059e322191ef5e5455e1057fed762a9c` |
| `nodes/HEXT.werner-modulus-square-majorant-obstruction.yaml` | `ff49a412aa2f11ff6b96b313f1df3f76577d561ac03a1a896e58584aecd3ec81` |
| updated `nodes/HEXT.same-tuple-werner-centered-bound.yaml` | `9efa2b658ebd427f8fcf8bc77fbc2d2573ca1e96e44b0769c54b7faffa6bd1e1` |
| `artifacts/SAME_TUPLE_POSITIVE_POLARIZED_GRAM_EXTENSION_20260830.md` | `57dbc9903072ea99cb6aef499845b19c6ec41c7044e68480614533627a1a3c35` |
| `artifacts/WERNER_CENTERED_GROWING_TRACE_METHOD_GATE_20260830.md` | `6f0d52b4d48433c9f16d8ded4440469268b336df3af8f23f4a8b798ac15752ce` |
| inherited rank-one Gram artifact | `752777b6d5b3a8d13ebc7c328980108232dbb050bb411c52bde97573b732f655` |
| earlier Gram/Werner independent review | `6c2651600430e3455a963def1c0884a29e6a935e777c4ac5bd6657e1e81df088` |

The repository-normalized exact claim hashes are:

| node | exact claim hash | recommendation |
|---|---|---|
| `HEXT.same-tuple-positive-partial-trace-contraction` | `sha256:69e84f82cbdadc4bb50f3a1ab0685fd426c1111e667cf1c964ce7875db838ce2` | `PROVED` |
| `HEXT.same-tuple-near-diagonal-positive-base-case` | `sha256:29f5f6d931fb0fd4bfcb8c1df28694b52113b11890f292af8d6006a1a4764d24` | `PROVED` |
| `HEXT.same-tuple-gram-safe-spectral-nuclear-base-case` | `sha256:a90703a03ad639b56e2eff9358fab2b6dd7711512f139d666851ef7ec108d100` | `PROVED` |
| `HEXT.same-tuple-positive-summation-obstruction` | `sha256:1e6dd0ab31a8d6127c5f4b06bf3a74b7090f7723b5adc862fca785660d07acf2` | `PROVED` |
| `HEXT.werner-modulus-square-majorant-obstruction` | `sha256:c6227c81050e97f42becbf354a9835efa570ea80558817bf5e18106f19cc20b0` | `PROVED` in its intended growing-order scope |
| `HEXT.same-tuple-werner-centered-bound` | `sha256:c221c71b9f3cb3294d7c9c7d979cf1a154042ea4ec013f95d3fc7955c2c38da5` | unresolved; no promotion |

The hashes are `sha256(claim.strip())` after YAML folding and CRLF normalization. A finding is
stale for promotion if its reviewed claim changes.

The fixed-word fluctuation interface was checked against Mingo--Sniady--Speicher,
[*Second Order Freeness and Fluctuations of Random Matrices: II. Unitary Random Matrices*](https://arxiv.org/abs/math/0405258).
Only its fixed-word/fixed-degree scope is used. No logarithmic-degree uniformity is imported.

## 2. Independent smoke tests

As a non-evidentiary algebra check, I used only the Python standard library and the explicit
`(m,d)=(3,3)` tuple consisting of the identity, cyclic shift, and Fourier unitary.

For a random positive rank-two coefficient, the independent spectral construction of `M_U(Y)`
agreed with the direct coefficient formula to `5.56e-17`. Two hundred random quadratic-form
checks of `M_U(Y)`, `I tensor C^*(Tr_1Y)-M_U(Y)`, and
`C^*(Tr_2Y) tensor I-M_U(Y)` were all nonnegative. The cross-term identity
`M_U(|z><w|)=m^-2 T_z^*T_w` had residual `3.20e-17`, and both partial traces of the explicit dense
rank-two family agreed with `(s_1+s_2)I/m` to `1.67e-16`.

For the Werner trace artifact, direct expansion at orders two and four gave reversal-formula
residuals `1.11e-16` and `2.78e-17`. At order two `Q_2` agreed with the exact moment; at order four
it differed by `6.58e-2`, confirming that reversal cannot be replaced by a square. Brute-force
enumeration for `(m,n)=(3,4)` found exactly 16 singleton-label sequences, matching
`(m-1)^n(m-2)^(n-1)`.

The proof verdicts below are exact and do not rely on these smoke tests.

## 3. Findings

### Finding STPW-IR-01 — PASS: exact positive partial-trace Loewner contraction

**Stable source locators:** positive-extension artifact Section 2, equations (4)--(13);
positive-partial-trace node claim.  
**Reviewed claim hash:**
`sha256:69e84f82cbdadc4bb50f3a1ab0685fd426c1111e667cf1c964ce7875db838ce2`.

Let

\[
 Y=\sum_k\lambda_k|z_k\rangle\langle z_k|,
 \qquad \lambda_k\ge0.
\]

With
`B_(v,k)=sqrt(lambda_k) sum_a overline((z_k)_(v,a))U_a` and
`T_k=sum_v U_v tensor B_(v,k)`, the exact rank-one factorization gives

\[
 \mathcal M_U(Y)=m^{-2}\sum_kT_k^*T_k\succeq0.
\]

Block Cauchy--Schwarz has the correct Loewner direction:

\[
 T_k^*T_k\preceq m I\otimes\sum_vB_{v,k}^*B_{v,k}.
\]

For the convention

\[
 (\operatorname{Tr}_1Y)_{a,b}=\sum_vY_{(v,a),(v,b)},
\]

the summed square function is exactly `m C^*(Tr_1Y)`. Therefore

\[
 0\preceq\mathcal M_U(Y)\preceq I\otimes C^*(\operatorname{Tr}_1Y).
\]

Grouping by the second coefficient index gives

\[
 0\preceq\mathcal M_U(Y)\preceq C^*(\operatorname{Tr}_2Y)\otimes I.
\]

For rank-one `Y`, the first partial trace is
`overline(Z^*Z)` and the second is `ZZ^*`; the conjugation thus matches the earlier Gram lemma.
Order monotonicity for positive operators yields the minimum of the two one-leg norms.

**Verdict:** exact deterministic claim; merits `PROVED`. It is an upper contraction and need not
be tight for arbitrary positive `Y`.

### Finding STPW-IR-02 — PASS: near-diagonal positive thresholds and dense rank-two scope

**Stable source locators:** positive-extension artifact Section 3, equations (14)--(25);
near-diagonal-positive node claim.  
**Reviewed claim hash:**
`sha256:29f5f6d931fb0fd4bfcb8c1df28694b52113b11890f292af8d6006a1a4764d24`.

For either positive coefficient partial trace `R` or `L`, the trace is
`tau=TrY`, its diagonal part maps to `tau I/m`, and its off-diagonal part is trace zero. On the
uniform event

\[
 \|C^*(X_0)\|_\infty\le\alpha\|X_0\|_F,
 \qquad \alpha=\sqrt{(A-1)/m},
\]

Finding STPW-IR-01 gives

\[
 \|\mathcal M_U(Y)\|_\infty
 \le\frac\tau m+\alpha
 \min\{\|\operatorname{Off}R\|_F,\|\operatorname{Off}L\|_F\}.
\]

The target follows exactly when the displayed off-diagonal norm is at most

\[
 \frac{A-\tau}{m\alpha}
 =\frac{A-\tau}{\sqrt{m(A-1)}},
\]

with the load-bearing condition `tau<=A`. The deterministic word triangle inequality similarly
gives the condition

\[
 \tau+\min\{\|\operatorname{Off}R\|_{\ell_1},
             \|\operatorname{Off}L\|_{\ell_1}\}\le A.
\]

For the dense rank-two family with eigenvalues
`s_1=1/sqrt(1+epsilon^2)` and `s_2=epsilon/sqrt(1+epsilon^2)`, both partial traces are
`(s_1+s_2)I/m`. Hence it is safe precisely in the stated near-pure window
`(1+epsilon)/sqrt(1+epsilon^2)<=A`. This is an explicit dense rank-two subclass, not a uniform
rank-two result.

**Verdict:** exact conditional/deterministic claim; merits `PROVED`.

### Finding STPW-IR-03 — PASS: cross-term factorization and the spectral nuclear window

**Stable source locators:** positive-extension artifact Section 4, equations (26)--(32);
Gram-safe spectral-nuclear node claim.  
**Reviewed claim hash:**
`sha256:a90703a03ad639b56e2eff9358fab2b6dd7711512f139d666851ef7ec108d100`.

For arbitrary unit coefficient vectors `z,w`, direct expansion gives

\[
 \mathcal M_U(|z\rangle\langle w|)=m^{-2}T_z^*T_w.
\]

Using the reviewed rank-one certificate `g_U` on each factor,

\[
 \|\mathcal M_U(|z\rangle\langle w|)\|_\infty
 \le\sqrt{g_U(z)g_U(w)}.
\]

This is an exact two-factor estimate and introduces no four-term polarization constant. For a
singular-value decomposition

\[
 Y=\sum_ks_k|z_k\rangle\langle w_k|,
\]

the triangle inequality gives

\[
 \|\mathcal M_U(Y)\|_\infty
 \le\sum_ks_k\sqrt{g_U(z_k)g_U(w_k)}.
\]

If every left and right singular vector has either a diagonal left Gram or a diagonal
conjugated-right Gram, then every `g_U` is at most `1/m`. The bound becomes
`||Y||_1/m`, where `||Y||_1` is the singular-value nuclear norm of the full coefficient matrix.
Thus `||Y||_2=1` and `||Y||_1<=A` imply the target deterministically.

This norm is neither the entrywise `l_1` norm nor the operator-Schmidt projective norm. The dense
positive rank-two family is included only when its second eigenvalue is small enough that its
spectral trace/nuclear norm is at most `A`.

**Verdict:** exact deterministic claim; merits `PROVED` without extension to general rank two.

### Finding STPW-IR-04 — PASS: positive summation incurs the stated `sqrt(r)` route loss

**Stable source locators:** positive-extension artifact Sections 5--7, equations (33)--(38);
positive-summation-obstruction node claim.  
**Reviewed claim hash:**
`sha256:1e6dd0ab31a8d6127c5f4b06bf3a74b7090f7723b5adc862fca785660d07acf2`.

If every normalized eigenvector of a positive coefficient has a target-sharp rank-one bound
`1/m`, positivity plus spectral norm summation gives only

\[
 \|\mathcal M_U(Y)\|_\infty\le\frac{\operatorname{Tr}Y}{m}.
\]

An equal-weight positive rank-`r` coefficient on the Hilbert--Schmidt unit sphere has eigenvalues
`1/sqrt(r)` and trace `sqrt(r)`. Already for `r=2`, the resulting route bound is
`sqrt(2)/m`, whereas `A/m` tends to `1/m` in the project regime.

Coefficient eigenvector orthogonality cannot be substituted for output-support orthogonality:
distinct coordinate projectors all map to the same positive operator `I/m^2`. The block
partial-trace contraction also exposes only a trace factor and can lose a full factor `m` on a
fully diagonal positive coefficient. Operator-Schmidt triangle summation has the analogous
projective nuclear factor.

**Verdict:** the scoped summation/Cauchy route obstruction merits `PROVED`. It does not refute a
uniform positive rank-two target using additional output cancellation or geometry.

### Finding STPW-IR-05 — PASS: exact forward/block-reversal moment and safe return sector

**Stable source locators:** Werner trace artifact Sections 2--3, equations (6)--(24); updated
centered-bound evidence and frontier.

For `S_U=m^-2 sum_e A_e tensor A_e^*`, direct multiplication gives

\[
 \operatorname{Tr}(S_U^n)
 =m^{-2n}\sum_{\mathbf e}
 \operatorname{Tr}(A_{e_1}\cdots A_{e_n})
 \overline{\operatorname{Tr}(A_{e_n}\cdots A_{e_1})}.
\]

The reversal comes from
`Tr(A_(e_1)^*...A_(e_n)^*)=overline(Tr(A_(e_n)...A_(e_1)))`. At `n=2`, cyclicity makes the two
words equivalent; for `n>=4`, cyclicity does not reverse an arbitrary product.

Grouping by reduced forward and reverse free-group words gives the exact two-word kernel in
artifact equation (13). A one-word return count is not the full moment.

For the forward return sector,

\[
 T_m=\sum_{v\ne a}\lambda(g_v^{-1}g_a)=X_m^*X_m-mI.
\]

The standard free-group norm `||X_m||=2sqrt(m-1)` yields
`||T_m||<=3m-4`; the weaker length-two Haagerup bound would give the same target-scale
conclusion. Forward or reverse returns therefore contribute in absolute value at most

\[
 2d^2\left(\frac{3m-4}{m^2}\right)^n.
\]

At the Werner threshold this has ratio base
`1/(sqrt(2m)(1+eta))(1+o_m(1))`, so logarithmic moment order suppresses the return sector. This is
safe partial progress only; it does not control nonreturn reduction-plus-reversal collisions.

**Verdict:** the updated centered-bound node correctly records this as evidence/frontier
refinement without promotion.

### Finding STPW-IR-06 — PASS: modulus-square majorization and exact singleton-label floor

**Stable source locators:** Werner trace artifact Section 4, equations (25)--(33);
modulus-square-majorant node claim.  
**Reviewed claim hash:**
`sha256:c6227c81050e97f42becbf354a9835efa570ea80558817bf5e18106f19cc20b0`.

For even `n`, `Tr(S_U^n)>=0`. Cauchy--Schwarz and the bijection that reverses edge blocks give the
pointwise majorization

\[
 \operatorname{Tr}(S_U^n)\le Q_n(U),
 \qquad
 Q_n=m^{-2n}\sum_{\mathbf e}|\operatorname{Tr}W_U(\mathbf e)|^2.
\]

For the explicit singleton-label family, fix the first edge tail to label `1` and forbid label
`1` from the other `2n-1` vertex slots. There are exactly

\[
 (m-1)[(m-1)(m-2)]^{n-1}
 =(m-1)^n(m-2)^{n-1}
\]

such sequences. Conditional on the other Haar matrices, the forward word is `U_1^*V`, so its
squared trace has expectation one. Since every term of `Q_n` is nonnegative, for `m>=3`,

\[
 \mathbb E Q_n\ge\frac{q_m^n}{m-2},
 \qquad q_m=\frac{(m-1)(m-2)}{m^2}.
\]

At `n=2k`, the candidate Markov upper bound therefore has the lower floor

\[
 h_W^{-2k}\mathbb E Q_{2k}
 \ge\frac1{m-2}\left(\frac{q_m}{h_W}\right)^{2k}
 =\frac{m^{k-1}}{[18(1+\eta)^2]^k}(1+o_m(1)).
\]

For the intended very large `m` and every relevant growing order (in particular `k>=2`), this
candidate upper bound already exceeds one and worsens with `k`. Thus the ordinary
positive-majorant-plus-Markov route is quantitatively vacuous.

**Verdict:** exact route obstruction; merits `PROVED` in its stated intended large-`m` scope.

### Finding STPW-IR-07 — PASS: majorant and original moment quantifiers remain separated

**Stable source locators:** Werner trace artifact Sections 4--8, especially equations (29)--(40);
majorant-node caveats; updated centered-bound caveats, evidence, and frontier.  
**Reviewed centered claim hash:**
`sha256:c221c71b9f3cb3294d7c9c7d979cf1a154042ea4ec013f95d3fc7955c2c38da5`.

The singleton lower floor is a lower bound on `E Q_(2k)`. For order at least four, it is not a
lower bound on `E Tr(S_U^(2k))`: the exact moment retains the signed forward/block-reversal
cross-correlation. Only at order two does cyclicity make `Q_2` equal the exact trace moment.

Fixed-order second-order freeness identifies leading nonreturn contributions only after first
fixing the two finite words and the moment order, then sending `d` to infinity. It supplies no
uniform error for `k=c log d`. Conversely, naive absolute Weingarten enumeration has factorial
diagram growth and also does not furnish the missing logarithmic-degree estimate.

The new frontier asks for an exponential joint reduction-plus-reversal collision count and a
growing-degree Weingarten bound that retains this correlation. No such proof is present. The
centered node's fixed-`m`, fixed-`eta`, `d->infinity` caveat is now explicit, and the majorant node
is linked only as non-load-bearing method-boundary evidence.

**Verdict:** `HEXT.same-tuple-werner-centered-bound` remains unresolved at its unchanged exact
claim hash. The update is correct and does not justify promotion.

### Finding STPW-IR-08 — WORDING ONLY: domain and growing-order qualifiers

**Stable source locators:** modulus-square-majorant node claim; Werner trace artifact equations
(26)--(31).

1. The singleton formula uses `1/(m-2)` and is proved for `m>=3`. The node says “intended
   large-`m` regime,” which supplies the operative domain, but stating `m>=3` explicitly would make
   the finite formula self-contained.
2. The singleton floor by itself forces the displayed Markov candidate above one for the relevant
   `k>=2`/growing orders in the intended large-`m` regime. It should not be read as a floor-above-one
   assertion for every possible `k`, nor as any statement about the exact reversal-correlated
   moment. The node's final scope sentence correctly preserves the latter distinction.

These are clarity improvements only; the exact obstruction in its intended regime is unchanged.

## 4. Promotion recommendations

The following findings provide exact review bindings:

- positive partial-trace contraction: Finding STPW-IR-01, reviewed hash
  `sha256:69e84f82cbdadc4bb50f3a1ab0685fd426c1111e667cf1c964ce7875db838ce2`;
- near-diagonal positive base case: Finding STPW-IR-02, reviewed hash
  `sha256:29f5f6d931fb0fd4bfcb8c1df28694b52113b11890f292af8d6006a1a4764d24`;
- Gram-safe spectral nuclear base case: Finding STPW-IR-03, reviewed hash
  `sha256:a90703a03ad639b56e2eff9358fab2b6dd7711512f139d666851ef7ec108d100`;
- positive summation obstruction: Finding STPW-IR-04, reviewed hash
  `sha256:1e6dd0ab31a8d6127c5f4b06bf3a74b7090f7723b5adc862fca785660d07acf2`;
- Werner modulus-square majorant obstruction: Finding STPW-IR-06, reviewed hash
  `sha256:c6227c81050e97f42becbf354a9835efa570ea80558817bf5e18106f19cc20b0`.

Do not promote `HEXT.same-tuple-werner-centered-bound`; Finding STPW-IR-07 rebinds its unresolved
claim hash
`sha256:c221c71b9f3cb3294d7c9c7d979cf1a154042ea4ec013f95d3fc7955c2c38da5`.

I make no canonical level change in this review.

## 5. Limitations

This review does not prove the centered reversal-moment lemma, establish a growing-order
second-order-freeness theorem, control positive-genus Weingarten sums through logarithmic degree,
or prove the general same-tuple strong-norm claim. It does not extend the positive results to
uniform positive rank two, arbitrary positive coefficients, arbitrary Hermitian coefficients, or
`n>=3`. The numerical checks test finite algebra and counting only, not asymptotic probability or
optimal constants.

