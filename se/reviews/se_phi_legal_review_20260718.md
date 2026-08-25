# Independent mathematical review of `se_phi_legal_20260718.md`

**Date:** 2026-07-18  
**Role:** rule-6 gate; independent adversarial review  
**Scope:** `se/artifacts/se_phi_legal_20260718.md` (the **note**) and every load-bearing cited source, including the post-note independent computation `se/artifacts/se_phi_legal_n3_result_20260718.md`.

## Executive finding

The note's central mathematics is supported in its stated in-spec range \(1\le k<K=\lfloor n^{1/3}\rfloor\): the literal BR \(\Phi\) carrier has no external leg-1 \(\Pi_0/\Pi_1\), the available position argument gives defect only \(\ge k-1\), legal NO restriction leaves candidate alphabet defects \(\{k-1,k\}\) (only \(1\) at \(k=1\)), and the two outer one-defect restriction bounds multiply to \((k-1)r_{\rm top}\), not \(\sqrt{k-1}r_{\rm top}\). The per-level bound (5.1)--(5.4) and, conditional on a cross-\(k\) maximum, the coefficient and exponent in (5.12) are **CONFIRMED**.

This is not a clean pass as written. Required status/citation corrections are:

1. The note's citation `SE_PROOF_DAG.md:460-467` for the open cross-\(k\) node is wrong; those lines concern `familysplit`. The supporting lines are `SE_PROOF_DAG.md:475-482`. The second citation, `:505-509`, does support the conditional framing.
2. The post-note \((n,q,k)=(3,6,2)\) witness proves that defect \(k-1\) is nonzero for **some** parameters. Thus a general structural-vanishing rescue is **REFUTED**, not OPEN. It does not refute an in-spec-only vanishing theorem, and it does not refute the weaker \(O(1)\) two-sided improvement.
3. Several status-table rows need scope/wording fixes: BR's subgroup-defect statement is cited under the hypothesis \(j<m/3\); “have the subgroup types” proves support containment, not occurrence of every listed type; and the matched/one-defect “block factors” are upper-bound factors for the actual \(T_k\) blocks, not equalities for those block norms.

No numerical inconsistency was found.

## Per-step verdict table

| Step | Verdict | One-line reason | Note lines |
|---|---|---|---:|
| Probability-\(L^2\) spaces and \(J_N=R_q\), \(J_Y=\mathbf1_M\otimes R_n\) | **CONFIRMED** | The pin note states the same normalized maps and points to the underlying normalization/factorization proofs. | 30-71 |
| BR leg convention and absence of an external leg-1 projector | **CONFIRMED** | BR (632-641) defines \(\Phi_{\rm se,k}=\sum_{\ell<k}\Phi_{k-\ell}^{(n)}\otimes\bar\Pi_\ell^{(n)}\); BR (607-611) puts the first factor on positions \([1..n]\). No external \(\Pi_0\) or \(\Pi_1\) occurs. | 90-104 |
| \(K'\)-type carrier support (2.2)-(2.3) | **CONFIRMED** | Under BR's `lem:newMain` hypothesis, \(\Phi_{k-\ell}^{(n)}\) has subgroup defect \(k-\ell-1\), while \(\bar\Pi_\ell^{(n)}\) has defect \(\ell\). | 106-130 |
| Normality/coimage inclusion (2.4) | **CONFIRMED** | Each \(\Phi_j^{(n)}\) is normal (indeed self-adjoint from its displayed definition); orthogonal second-half \(\ell\)-supports make the sum block diagonal and normal, and \(\operatorname{im}(AB)\subseteq\operatorname{im}A\). | 132-140 |
| Transfer of subgroup support to \(\operatorname{im}T_k\) | **CONFIRMED** | A \(K'\)-equivariant map pairs every nonzero right-singular \(K'\)-module with an isomorphic left-singular module; this proves containment in the same type list, not occurrence of every listed type. | 140 |
| Two-fold LR derivation (2.5)-(2.7) | **CONFIRMED** | Induction first from \(S_{n-1}\times S_n\), then with \(S_1\), gives \(\nu_1\le1+\sigma_1+\sigma'_1\), hence position defect \(\ge k-1\). | 142-169 |
| Two-point support (2.7a) | **CONFIRMED** | BR's exact-weight corollary gives full-position defect \(\le k\); integrality plus (2.7) gives precisely the allowed set \(\{k-1,k\}\). This is support containment, not nonvanishing of both levels. | 171-178 |
| Exact input/output weight (2.8) | **CONFIRMED** | Every \(\Phi\)-summand has total weight \((k-\ell)+\ell=k\), and BR (525-531) puts both coimage and image of \(W_k^\mu\) in weight \(k\). | 180-187 |
| Peter-Weyl pinning and two-level survival (3.2)-(3.3) | **CONFIRMED** | On legal NO permutations only equal alphabet/full-position shapes occur; defects \(<k-1\) are therefore killed, while weight \(k\) forces alphabet defect \(\le k\). | 189-213 |
| Endpoint \(k=1\), equation (3.4) | **CONFIRMED** | Exact weight one is a direct sum of copies of \(H_1\cong S^{(q-1,1)}\), so defect zero is absent and defect one is the only possible type. | 215-220 |
| Alphabet equivariance and block decomposition (3.5) | **CONFIRMED** | \(\Psi_0,\Psi_1\), the position projectors, \(\Phi\), and legal restriction intertwine alphabet actions; distinct legal alphabet isotypes are orthogonal on both sides, so the norm costs a maximum. | 222-237 |
| Matched defect-\(k\) factor (4.4)-(4.5) | **CONFIRMED** | Full-permutation equality on NO and the completion bound on YES each contribute \(\sqrt{r_{\rm top}}\); their product is \(r_{\rm top}\). | 267-285 |
| Full-permutation scalar formula (4.3) | **CONFIRMED** | The character calculation in the one-defect source gives the stated scalar for arbitrary exact degree \(d\). | 257-265 |
| Equality condition (4.7)-(4.8) | **CONFIRMED** | For \(j=k-1\), \(q-j=2n-k+1>k-1\ge\theta_1\) in the note's range, so the extra skew box is incomparable and the ratio is exactly \(j\). | 289-304 |
| NO-side equality (4.9) | **CONFIRMED** | At \(m=q\), the legal \(\lambda\)-block Gram scalar is exactly \(r_k(\lambda)\); the ratio calculation gives \((k-1)r_{\rm top}(q,k-1,\theta)\). | 304-310 |
| YES-side one-defect bound (4.10) | **CONFIRMED** | Completion to a full permutation gives the uniform squared-norm bound for every position isotype and multiplicity vector; the matching-register identity does not change the norm. | 312-318 |
| Two-sided factor (4.11) | **CONFIRMED** | Both squared outer norms are bounded by \((k-1)r_{\rm top}\); taking square roots on both sides and multiplying restores the full factor \((k-1)r_{\rm top}\). | 320-326 |
| Hook formula/envelope (4.12)-(4.15) | **CONFIRMED** | The hook product is exact; \(\log(q^j/(q)_j)\) and the column product give (4.13), and the \(q=2n,j\le K,n\ge8\) arithmetic yields \(E_{2n}(j)\le n^{-1/3}\). | 328-362 |
| Per-level channel bound (5.1)-(5.5) | **CONFIRMED** | Maximizing the two orthogonal defect families yields exactly the stated \(F_k\); for \(k\ge3\), the one-defect term is \((k-1)(1+O(n^{-1/3}))\). | 364-398 |
| Ambient bound (5.6) | **CONFIRMED** | The cited audits correctly repair BR's printed reciprocal error at BR:1307 and combine the two \(\Phi\) restrictions by Cauchy--Schwarz with the \(\sqrt3\) \(W\)-bound. | 400-406 |
| Cross-\(k\) maximum assumption | **GAP** | It is honestly labeled OPEN/assumed, but the first DAG line citation is wrong; the actual open-node discussion is at DAG 475-482. | 408-420 |
| Quadratic maximization and (5.12) | **CONFIRMED** | \((K-k)(k-1)\) peaks at \((K+1)/2\); with \(K\sim n^{1/3}\) and the ambient \(n^{-1/2}\), the result is \((\sqrt6/4+o(1))n^{1/6}\). | 422-455 |
| Claim that this is a route envelope, not an operator lower bound | **CONFIRMED** | The note repeatedly conditions on the unproved maximum and explicitly limits the \(\Theta\)-claim to its analytic envelope. | 21-26, 414-455 |
| Rescue 1(a): general structural vanishing of defect \(k-1\) | **REFUTED** | The independent \((3,6,2)\) computation has a nonzero defect-one block of norm \(0.3\). | 461-466, 489-503 |
| Rescue 1(b): uniform \(O(1)\) two-sided improvement | **GAP** | The witness is below the crude bound and says nothing against a stronger correlated/special-site estimate; no such theorem is proved. | 461-470 |
| Status table as written | **GAP** | Its main theorem rows are right, but it conflates “some/all” nonvanishing, omits the `lem:newMain` range qualifier, and uses equality-sounding wording for support and upper factors. | 505-524 |


## Citation audit

| Citation and claim made from it | PASS/FAIL | Audit |
|---|---|---|
| BR 353-375: \(e\)-basis, \(H_0/H_1\), exact weight | **PASS** | The cited lines state exactly these conventions. |
| BR 483-490, 525-531: \(\Psi_0,\Psi_1,W_k^\mu\), exact input/output weight | **PASS** | Definitions and weight support match the note. |
| BR 600-611: \(\bar\Pi_d^{(m)}\), exact position grade, two-half convention | **PASS** | The cited lines define exact grade and assign the SE tensor factors to the two halves. |
| BR 616-629: \(\Phi_j^{(m)}\), normality, weight, subgroup defect \(j-1\) | **PASS (range-qualified)** | Normality/weight are stated at 623; the exact subgroup defect is the second conclusion of `lem:newMain`, whose statement assumes \(j<m/3\). Every use in the note is in that range, but the status row should say so. |
| BR 632-641: literal \(\Phi_{\rm se,k}\) carrier and no external leg-1 projector | **PASS** | The displayed formula contains the whole \(\Phi^{(n)}\) on the first half and no leading \(\Pi_i\). |
| BR 1361-1369: principal right-singular subgroup defects | **PASS** | It states defects \(k-\ell-1\) and \(\ell\) for a principal module. The note's all-support conclusion additionally uses (2.4) and equivariance; BR alone does not assert occurrence of all listed types. |
| `se_bridge2_pin_20260718.md` 89-127, 177-203: LR inequality and induced-span argument | **PASS** | The source proves the LR first-row bound and the same two-stage induction mechanism. |
| `se_bridge2_pin_20260718.md` 205-227: legal regular bimodule and weight-to-alphabet defect | **PASS** | These lines support equal-shape survival and defect \(\le k\). |
| `se_bridge2_pin_20260718.md` 238-300, 320-353: equivariance, restriction transport, orthogonal blocks | **PASS** | The same intertwining calculation applies to \(W_k\), and the maximum-over-isotypes conclusion is stated and proved. |
| `se_bridge2_md_inst_20260718.md` 43-59, 189-202, 219-245: matched-degree theorem and \(m=q\) equality | **PASS** | The source proves the full operator-norm inequality uniformly over position multiplicities and constructs an attaining vector at \(m=q\). |
| `se_one_defect_forgetting_bound.md` 204-268: (4.3), matched scalar, one-defect ratio/equality | **PASS** | Direct substitution independently reproduces (4.9); the condition \(q-j>\theta_1\) gives equality. |
| `se_one_defect_forgetting_bound.md` 11-41, 140-158, 270-273: YES one-defect uniformity | **PASS** | The vector-level completion argument is multiplicity-insensitive; position equivariance lets the whole space be bounded by the same scalar. |
| `se_legal_conditioning_top_gram.md` 20-49, 275-289: hook product and exponential envelope | **PASS** | The exact product and both logarithmic estimates appear in the cited ranges. |
| `se_phi_blind_lineread_codex_20260717.md` 140-162 and `se_phi_xbar_qfree_audit_20260717.md` 88-100, 138-149: explicit ambient constant | **PASS** | Together they derive the \(\sqrt2\) carrier factor, \(\sqrt3\) \(W\)-factor, and \(\sqrt6/\sqrt{n-2k+1}\). They explicitly disclose and repair BR:1307. |
| `SE_PROOF_DAG.md` 460-467: cross-\(k\) node is OPEN | **FAIL** | Those lines are about `familysplit`; the correct support is DAG 475-482. |
| `SE_PROOF_DAG.md` 505-509: conditional \(n^{1/6}\) framing | **PASS** | Those lines state the same per-level factors and explicitly condition the envelope on `SE.denom.crossk`. |
| `ybar_norms_fresh.log` line 14: \(n=3,k=1\) ambient anchor | **PASS** | The later independent numerical result repeats the ambient value \(1/\sqrt3\), providing an independent consistency check. |

## Independent re-derivation of (2.7) and (2.7a)

Fix \(\ell\in\{0,\ldots,k-1\}\). A nonzero \(K'=S_1\times S_{n-1}\times S_n\) carrier type has

\[
\mathbf1\boxtimes S^\sigma\boxtimes S^{\sigma'},\qquad
(n-1)-\sigma_1=k-\ell-1,\qquad n-\sigma'_1=\ell.
\]

If \(S^\tau\) occurs after inducing \(S^\sigma\boxtimes S^{\sigma'}\) to \(S_{2n-1}\), the LR tableau argument gives

\[
\tau_1\le\sigma_1+\sigma'_1.
\]

Inducing once more with the one-box representation gives, for every resulting \(S^\nu\) of \(S_{2n}\),

\[
\nu_1\le1+\tau_1\le1+\sigma_1+\sigma'_1.
\]

The equivariant surjection from the induced module onto the \(S_{2n}\)-span of the actual \(K'\)-module ensures that the ambient full-position constituents of the coimage are among these induced constituents. Therefore

\[
\begin{aligned}
2n-\nu_1
&\ge2n-(1+\sigma_1+\sigma'_1)\\
&=((n-1)-\sigma_1)+(n-\sigma'_1)\\
&=(k-\ell-1)+\ell=k-1.
\end{aligned}
\]

Separately, the exact-weight-\(k\) space uses only \(S_{2n}\)-irreps with first row at least \(2n-k\), so \(2n-\nu_1\le k\). Since the defect is integral,

\[
2n-\nu_1\in\{k-1,k\}.
\]

Thus (2.7a) is correctly derived. It is an allowed-support statement. The post-note witness shows the lower endpoint is genuinely attained after legal transfer in at least one algebraically valid case, but the LR argument alone did not prove that.

## Independent re-derivation of (4.9)--(4.11)

Let \(j=k-1\), \(\lambda=(q-j,\theta)\), and \(h_\theta=f^{\lambda/(q-j-1)}\). In the full-permutation scalar

\[
r_d(\lambda)=\frac1{f^\lambda}\sum_{t=0}^d
q^t(-1)^{d-t}\binom{q-t}{d-t}
\frac{f^{\lambda/(q-t)}}{t!},
\]

all terms with \(t<j\) vanish. At \(d=j\), only \(t=j\) remains, so

\[
r_j(\lambda)=\frac{q^j f^\theta}{j!f^\lambda}=r_{\rm top}(q,j,\theta).
\]

At \(d=j+1\), only \(t=j,j+1\) remain. Dividing by \(r_j\) gives

\[
\frac{r_{j+1}(\lambda)}{r_j(\lambda)}
=\frac{q}{j+1}\frac{h_\theta}{f^\theta}-(q-j).
\]

If \(q-j>\theta_1\), the additional top-row skew box is incomparable with every box of \(\theta\), hence \(h_\theta=(j+1)f^\theta\). The ratio is then

\[
q-(q-j)=j.
\]

Here \(q=2n\), \(j=k-1\), and \(q-j=2n-k+1>k-1\ge\theta_1\), so equality applies. Since \(J_N=R_q\) and the legal regular \(\lambda\)-block sees exactly the scalar \(r_k(\lambda)\),

\[
\|P_{2n,k}A_{2n,\lambda}J_N^*\|^2
=r_k(\lambda)
=(k-1)r_{\rm top}(q,k-1,\theta).
\tag{R4.9}
\]

Completion/forgetting bounds every YES position-isotypic component, including its multiplicity space, by the same full-permutation scalar. Orthogonality across position isotypes therefore gives

\[
\|J_YP_{n,k}A_{n,\lambda}\|^2
\le(k-1)r_{\rm top}(q,k-1,\theta).
\tag{R4.10}
\]

Factor the legal \(\lambda\)-block into the YES outer map, the compressed \(T_k\), and the NO outer map. The middle norm is at most \(\|T_k\|\). Each outer norm is at most

\[
\sqrt{(k-1)r_{\rm top}(q,k-1,\theta)}.
\]

Their product is therefore

\[
\|\mathcal R(T_k)|_\lambda\|
\le (k-1)r_{\rm top}(q,k-1,\theta)\,\|T_k\|.
\tag{R4.11}
\]

The note is correct: two-sided multiplication gives \(k-1\), not \(\sqrt{k-1}\). Only the NO outer scalar is proved equal to its envelope; (R4.10) and the actual restricted \(T_k\)-block need not attain it.


## Independent re-derivation of (5.12)

For \(k\ge3\), uniformly over \(k<K\),

\[
F_k=(k-1)(1+O(n^{-1/3})),\qquad
(n-2k+1)^{-1/2}=n^{-1/2}(1+O(n^{-2/3})).
\]

The polynomial part is exactly

\[
(K-k)(k-1)=\frac{(K-1)^2}{4}-\left(k-\frac{K+1}{2}\right)^2.
\]

Thus its integer maximum is \((K-1)^2/4+O(1)\), attained at one of the two integers nearest \((K+1)/2\). The \(k=1,2\) endpoints contribute only \(O(K/\sqrt n)=O(n^{-1/6})\), so they cannot dominate. Conditional on replacing the cross-\(k\) norm by a maximum,

\[
\begin{aligned}
B_n
&=\frac{\sqrt6}{\sqrt n}
\left(\frac{(K-1)^2}{4}+O(1)\right)
(1+O(n^{-1/3}))\\
&=\left(\frac{\sqrt6}{4}+o(1)\right)n^{2/3-1/2}\\
&=\left(\frac{\sqrt6}{4}+o(1)\right)n^{1/6}.
\end{aligned}
\]

The exponent \(1/6\) and coefficient \(\sqrt6/4\) are correct. The word “conditional” is used honestly throughout the note. Also, because \(F_k\ge k-1\), this particular analytic envelope (not the true operator norm) is of order \(n^{1/6}\), not merely \(O(n^{1/6})\).

## Independent numerical consistency check

The post-note computation uses probability-\(L^2\) normalization, the literal BR leg order, all six matchings with \(1/\sqrt6\) block weight, and reports projector residuals below \(10^{-12}\). Its ambient anchors are \(\|T_1\|=1/\sqrt3\) and \(\|T_2\|=1\).

At \(q=6\),

\[
r_{\rm top}(6,1,(1))=\frac65=1.2,
\quad r_{\rm top}(6,2,(2))=2,
\quad r_{\rm top}(6,2,(1,1))=\frac95=1.8.
\]

| Measured block | Measured norm | Note's applicable bound | Result |
|---|---:|---:|---|
| \(k=2\), defect 0, \((6)\) | \(0\) | Must vanish by (3.3) | **CONSISTENT** |
| \(k=2\), defect 1, \((5,1)\) | \(0.3\) | \((k-1)(6/5)\|T_2\|=1.2\) | **CONSISTENT**; strict inequality |
| \(k=2\), defect 2, \((4,2)\) | \(1.5\) | \(2\|T_2\|=2\) | **CONSISTENT** |
| \(k=2\), defect 2, \((4,1,1)\) | \(0.9\) | \((9/5)\|T_2\|=1.8\) | **CONSISTENT** |
| \(k=2\), total | \(1.5\) | \(F_2\|T_2\|=\max\{2,1.2\}=2\) | **CONSISTENT**; equals the maximum measured orthogonal block |
| \(k=1\), defect 0, \((6)\) | \(0\) | Must vanish by (3.4) | **CONSISTENT** |
| \(k=1\), defect 1, \((5,1)\) | \(0.6\) | \((6/5)(1/\sqrt3)=0.692820\ldots\) | **CONSISTENT** |

The nonzero \(0.3\) defect-one block is decisive only for nonvanishing: it refutes a theorem asserting structural vanishing for every \(n,k\). Because \((n,k)=(3,2)\) lies outside \(k<K(3)\), it does not rule out a theorem restricted to the witness range. Because \(0.3\ll1.2\), it also does not rule out an \(O(1)\) correlated two-sided improvement.

## Status-table corrections required by the gate

| Note status row | Review disposition |
|---|---|
| Leg convention | Keep **PROVED**. |
| \(\Phi_j^{(m)}\) subgroup defect exactly \(j-1\) | Keep **PROVED IN RANGE \(j<m/3\)**; normality and exact-weight support are unconditional. |
| \(\operatorname{coim}T_k\) and \(\operatorname{im}T_k\) “have” types (2.2)-(2.3) | Replace by “are supported only on types satisfying (2.2)-(2.3)”; occurrence of every candidate is not proved. |
| Full-position defect \(\ge k-1\), exact weight, Peter-Weyl pinning, two-level candidate support | Keep **PROVED**. |
| “Defect \(k-1\) is nonzero for some/all \(n,k\ge2\)” | Split: **PROVED for some / general structural vanishing REFUTED** by \((3,6,2)\); **OPEN for all or for the in-spec range**. |
| Matched and one-defect “block factors” | Keep **PROVED AS UPPER-BOUND FACTORS**. The NO outer factor in (4.9) is an equality; the actual restricted \(T_k\)-block generally is not. |
| Hook envelope, channel inequality, ambient bound | Keep **PROVED** in the stated range. |
| Cross-\(k\) maximum | Keep **OPEN / ASSUMED**, and correct the DAG citation to 475-482. |
| Conditional \((\sqrt6/4+o(1))n^{1/6}\) envelope | Keep **PROVED CONDITIONAL ON CROSS-\(k\)**. |
| Actual full legal assembly \(O(1)\) | Keep **OPEN**. |

## Gate disposition

The rule-6 review supports promotion of the **per-level legality inequality** (5.1)-(5.4) to **PROVED**, and supports (5.12) as **PROVED CONDITIONAL ON `SE.denom.crossk`**. It does not close the legal \(\Phi\) assembly. The post-note witness closes only the general-vanishing subquestion negatively; the uniform \(O(1)\) special-site/correlated improvement and the legal cross-\(k\) node remain open.

**FINAL VERDICT: CONFIRMED WITH REQUIRED CORRECTIONS — core per-level theorem PASS; conditional assembly arithmetic PASS; general structural-vanishing rescue REFUTED; \(O(1)\) tame rescue and cross-\(k\) assembly remain OPEN.**
