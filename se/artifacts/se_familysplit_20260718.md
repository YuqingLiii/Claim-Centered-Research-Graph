# FAMILY-SPLIT DECLARATION

**Date:** 2026-07-18  
**Scope:** Set Equality at \(q=2n\).  
**Verdict:** **PROVED for the family identification and its legal \(\Delta_1\)-diamond decomposition.** This note does **not** prove the open legal \(\Phi\)-channel bound or the open legal cross-\(k\) assembly.

## 1. Objects and declaration

Fix an integer \(n\ge 1\), put \(q:=2n\), and let

\[
H:=\mathbb C^q=H_0\oplus H_1,\qquad
H_0:=\operatorname{span}\{e_0\},\qquad
H_1:=e_0^\perp .
\]

Here \(e_0\) is the normalized constant vector, and \(\Pi_0,\Pi_1\) are the orthogonal projectors onto \(H_0,H_1\). For \(m\ge0\) and \(d\in\mathbb Z\), let \(\bar H_d^{(m)}\subseteq H^{\otimes m}\) be BR's exact-weight-\(d\) position-\(S_m\) subspace whose irreducibles have exactly \(d\) boxes below the first row, and let \(\bar\Pi_d^{(m)}\) be its orthogonal projector. We use \(\bar\Pi_d^{(m)}=0\) when \(d<0\) or \(d>m\). These are BR's spaces and projectors (<code>se/artifacts/references/BR_1310.5185v4_collision.tex:600-609</code>).

Let \(A:=\{1,\ldots,n\}\), \(B:=\{n+1,\ldots,2n\}\), and let \(M_{\rm se}\) be the set of bipartite perfect matchings between \(A\) and \(B\); hence \(|M_{\rm se}|=n!\). BR's ambient level operator is

\[
W_{{\rm se},k}:H^{\otimes2n}\longrightarrow
\mathbb C^{M_{\rm se}}\otimes H^{\otimes n}.
\]

It is a stack of matching blocks: its \(\mu\)-block is

\[
|M_{\rm se}|^{-1/2}W_k^\mu=(n!)^{-1/2}W_k^\mu .
\tag{1.1}
\]

Thus \(1/\sqrt{|M_{\rm se}|}\) is already part of BR's \(W_{{\rm se},k}\); it is not another factor to insert after legal restriction (<code>se/artifacts/references/BR_1310.5185v4_collision.tex:522-532</code>).

**Declaration.** For every \(k\ge0\), the witness projector is

\[
\boxed{
P_k:=\bar\Pi_{{\rm se},k}
:=\sum_{\ell=0}^{k}
\bar\Pi_{k-\ell}^{(n)}\otimes\bar\Pi_{\ell}^{(n)} .}
\tag{1.2}
\]

The summands are orthogonal because different \(\ell\)'s have different exact weights in at least one tensor factor. This is exactly BR's \(S_n\times S_n\) Set-Equality family: BR defines \(\bar\Pi_{{\rm se},k}\) as the orthogonal projector onto that sum of subspaces (<code>se/artifacts/references/BR_1310.5185v4_collision.tex:607-611</code>). The witness handoff assigns the same family to \(P_k\) (<code>se/notes/SE_HANDOFF_CONTINUE_PROOF.md:28-33</code>).

Define

\[
\bar W_{{\rm se},k}:=W_{{\rm se},k}P_k .
\tag{1.3}
\]

This is BR's definition \(\bar W_{\mathsf{qp},k}=W_{\mathsf{qp},k}\bar\Pi_{\mathsf{qp},k}\), specialized to \(\mathsf{qp}={\rm se}\), rather than a new family (<code>se/artifacts/references/BR_1310.5185v4_collision.tex:603-611</code>).

Put

\[
K:=\lfloor n^{1/3}\rfloor,\qquad
\alpha_k:=(K-k)_+
=\begin{cases}K-k,&0\le k<K,\\0,&k\ge K,\end{cases}
\]

and set \(\alpha_k:=0\) also for \(k<0\). Then

\[
\boxed{
\widetilde\Gamma_n
:=\sum_{k\ge0}\alpha_kW_{{\rm se},k}\bar\Pi_{{\rm se},k}
=\sum_{k\ge0}\alpha_k\bar W_{{\rm se},k}.}
\tag{1.4}
\]

Equation (1.4) is BR's equation <code>eqn:decomposition</code>, \(\widetilde\Gamma_{\mathsf{qp}}=\sum_k\alpha_k\bar W_{\mathsf{qp},k}\), where \(\mathsf{qp}\) is BR's problem label, specialized here to Set Equality (<code>se/artifacts/references/BR_1310.5185v4_collision.tex:502-508</code>). The witness uses the displayed integer taper; the operator decomposition itself is linear in any scalar sequence \((\alpha_k)\).

### Normalization and legal restriction

Let

\[
\begin{aligned}
Y_n&:=\{(f,g):f,g:[n]\to[q]\text{ injective and }
\operatorname{im}f=\operatorname{im}g\},\\
N_n&:=\{(f,g):f,g:[n]\to[q]\text{ injective and }
\operatorname{im}f\cap\operatorname{im}g=\varnothing\}
\end{aligned}
\]

be the legal Set-Equality YES rows and NO columns. At \(q=2n\), both have size \(q!\) (<code>se/notes/SE_BRIDGE_COMMISSION_PROMPT.md:70-77</code>). Permuting positions within the two \(n\)-position halves preserves injectivity and disjointness, so \(\mathbb C[N_n]\) is \(S_n\times S_n\)-invariant. Therefore the position-isotypic projector (1.2) restricts to the same \(P_k\) on legal columns; this is the family assignment recorded at <code>se/notes/SE_HANDOFF_CONTINUE_PROOF.md:30-33</code>, not a second legal-only projector.

Let \(J_Y,J_N\) be the normalized coordinate restrictions from BR's ambient row and column spaces to those legal spaces, and define

\[
\mathcal R(T):=J_YTJ_N^* .
\tag{1.5}
\]

This is the common legal-channel convention used by the proved \(X/Y\) bounds (<code>se/artifacts/se_bridge2_pin_20260718.md:45-63</code>). Write \(W_{{\rm se},k}^{\rm leg}\) for the unnormalized closed-form legal kernel obtained from the \(k\)-th BR matching kernel. In the witness coordinates, the transferred level atom is

\[
\mathcal R(\bar W_{{\rm se},k})
=\frac1{q!}\,W_{{\rm se},k}^{\rm leg}P_k .
\tag{1.6}
\]

There are two distinct normalization facts:

1. every ambient matching block already carries \(1/\sqrt{|M_{\rm se}|}=1/\sqrt{n!}\), by (1.1);
2. the legal witness has one \(k\)-independent outside factor \(1/q!\), because at \(q=2n\)

   \[
   n!(q)_n=q!,\qquad (q)_{2n}=q!,
   \]

   where \((q)_r:=q(q-1)\cdots(q-r+1)\).

The second fact and its \(k\)-independence are recorded with the witness at <code>se/notes/SE_HANDOFF_CONTINUE_PROOF.md:28-37</code>; the first is BR's block normalization at <code>se/artifacts/references/BR_1310.5185v4_collision.tex:526-532</code>. They are not two copies of the same scalar and must not be multiplied into \(W_{{\rm se},k}\) twice.

By linearity of \(\mathcal R\), (1.4)--(1.6) give

\[
\boxed{
\Gamma_n
=\mathcal R(\widetilde\Gamma_n)
=\frac1{q!}\sum_{k=0}^{K-1}(K-k)
W_{{\rm se},k}^{\rm leg}P_k .}
\tag{1.7}
\]

Thus the stated witness is the legal restriction, in the stated common normalization, of BR's own Set-Equality decomposition. The primed projectors below do not replace \(P_k\); they occur only inside BR's decomposition of the already-defined atom \(\bar W_{{\rm se},k}=W_{{\rm se},k}P_k\).

## 2. IDENT-1 and IDENT-2

For \(m\ge1\), define BR's projector error

\[
\Phi_d^{(m)}
:=\bar\Pi_d^{(m)}
-\Pi_0\otimes\bar\Pi_d^{(m-1)}
-\Pi_1\otimes\bar\Pi_{d-1}^{(m-1)} .
\tag{2.1}
\]

This is BR's <code>eqn:error</code> (<code>se/artifacts/references/BR_1310.5185v4_collision.tex:616-623</code>). With position \(1\) in the first \(n\)-position half singled out, define operators on the remaining \(2n-1\) input legs by

\[
\bar\Pi'_{{\rm se},k}
:=\sum_{\ell=0}^{k}
\bar\Pi_{k-\ell}^{(n-1)}\otimes\bar\Pi_{\ell}^{(n)},
\qquad
\Phi_{{\rm se},k}
:=\sum_{\ell=0}^{k-1}
\Phi_{k-\ell}^{(n)}\otimes\bar\Pi_{\ell}^{(n)} .
\tag{2.2}
\]

These are BR's definitions (<code>se/artifacts/references/BR_1310.5185v4_collision.tex:632-646</code>). We set \(\bar\Pi'_{{\rm se},-1}:=0\). An empty sum is zero, so BR's upper limit \(k-1\) gives \(\Phi_{{\rm se},0}=0\) (<code>se/artifacts/references/BR_1310.5185v4_collision.tex:639-640</code>).

### IDENT-1

\[
\boxed{
\bar\Pi_{{\rm se},k}
=\Pi_0\otimes\bar\Pi'_{{\rm se},k}
+\Pi_1\otimes\bar\Pi'_{{\rm se},k-1}
+\Phi_{{\rm se},k}.}
\tag{2.3}
\]

This is BR's displayed <code>eqn:PiQkDecomposition</code> (<code>se/artifacts/references/BR_1310.5185v4_collision.tex:645-651</code>). It follows by substituting (2.1) into the first \(S_n\)-factor of each summand in (1.2) and collecting the \(\Pi_0\), \(\Pi_1\), and error terms; the apparent \(\ell=k\) error term vanishes because the \(d=0\) instance of (2.1) has \(\Phi_0^{(n)}=0\). It is pure projector algebra and holds for every alphabet dimension \(q\) for which the spaces are defined, hence at \(q=2n\). It uses neither legal restriction nor a commutant assertion.

To state IDENT-2, let \(e_0^*\) denote the adjoint covector of \(e_0\), and define

\[
\Psi_0:=\Pi_0\otimes e_0^*=e_0^*\otimes\Pi_0,
\qquad
\Psi_1:=\Pi_1\otimes e_0^*+e_0^*\otimes\Pi_1 .
\]

For a matching \(\mu\), order its first edge so its first endpoint is query position \(1\), and put

\[
S_r^\mu:=
\sum_{\substack{c\in\{0,1\}^{\{2,\ldots,n\}}\\|c|=r}}
\Psi_{c_2}\otimes\cdots\otimes\Psi_{c_n}.
\]

BR's block components are

\[
X_k^\mu=\Psi_0\otimes S_k^\mu,\qquad
Y_k^\mu=(e_0^*\otimes\Pi_1)\otimes S_{k-1}^\mu,\qquad
Z_k^\mu=(\Pi_1\otimes e_0^*)\otimes S_{k-1}^\mu,
\tag{2.4}
\]

with an empty sum interpreted as zero. These are BR's formulas, including the placement of query position \(1\) at the first endpoint of the first matching edge (<code>se/artifacts/references/BR_1310.5185v4_collision.tex:483-489,544-553</code>). Let \(X_{{\rm se},k},Y_{{\rm se},k},Z_{{\rm se},k}\) be the corresponding stacks of \(|M_{\rm se}|^{-1/2}\)-scaled matching blocks. Then

\[
W_{{\rm se},k}
=X_{{\rm se},k}+Y_{{\rm se},k}+Z_{{\rm se},k}
\tag{2.5}
\]

(<code>se/artifacts/references/BR_1310.5185v4_collision.tex:554-558</code>). Define the barred channels

\[
\begin{aligned}
\bar X_{{\rm se},k}
&:=X_{{\rm se},k}
(\Pi_0\otimes\bar\Pi'_{{\rm se},k}),\\
\bar Y_{{\rm se},k}
&:=Y_{{\rm se},k}
(\Pi_0\otimes\bar\Pi'_{{\rm se},k}),\\
\bar Z_{{\rm se},k}
&:=Z_{{\rm se},k}
(\Pi_1\otimes\bar\Pi'_{{\rm se},k-1}).
\end{aligned}
\tag{2.6}
\]

These are BR's channel definitions (<code>se/artifacts/references/BR_1310.5185v4_collision.tex:653-657</code>).

### IDENT-2

Multiplying IDENT-1 on the left by \(W_{{\rm se},k}\) and using (2.5)--(2.6) gives

\[
\boxed{
\bar W_{{\rm se},k}
=W_{{\rm se},k}\bar\Pi_{{\rm se},k}
=\bar X_{{\rm se},k}
+\bar Y_{{\rm se},k}
+\bar Z_{{\rm se},k}
+W_{{\rm se},k}\Phi_{{\rm se},k}.}
\tag{2.7}
\]

This is BR's displayed identity (<code>se/artifacts/references/BR_1310.5185v4_collision.tex:659-663</code>). Like IDENT-1, it holds before legal restriction and for every alphabet dimension \(q\); \(q=2n\) is only the witness specialization.

The finite computations are corroboration, not a premise. For \((n,k)=(3,1),(3,2),(4,1),(4,2)\), the log reports IDENT-1/2 residuals on lines 15, 30, 43, and 58 of <code>se/artifacts/logs_se_py_reverify_20260717/ybar_norms_fresh.log</code>; IDENT-3 is exactly zero on those rows. **Numerical correction:** the four requested rows are bounded by \(3.4\times10^{-15}\), not \(1.4\times10^{-15}\): the \((4,2)\) row reports <code>IDENT1=3.373e-15</code> and <code>IDENT2max=3.162e-15</code> (<code>se/artifacts/logs_se_py_reverify_20260717/ybar_norms_fresh.log:58</code>). The DAG's \(1.4\times10^{-15}\) summary (<code>se/notes/SE_PROOF_DAG.md:38-40,437-440</code>) is stale. No numerical residual is used to prove (2.3) or (2.7).

## 3. The witness's \(\Delta_1\) decomposition

For matrices with a row symbol and a column symbol at query position \(i\), define

\[
\Delta_i[u,v]:=\mathbf1\{u_i\ne v_i\},
\]

where \(\mathbf1\{\cdot\}\) is the indicator, and let \(\circ\) denote entrywise (Hadamard) product. BR's actual diamond requirement is:

> “\(\Delta_i\circ B=\Delta_i\circ A\).”

Thus \(B\) is a permissible representative of \(\Delta_i\diamond A\) precisely when it agrees with \(A\) on every entry with unequal queried symbols (<code>se/artifacts/references/BR_1310.5185v4_collision.tex:202-210</code>). Diamond representatives are not unique, and the construction is linear (<code>se/artifacts/references/BR_1310.5185v4_collision.tex:221-225</code>).

BR assigns

\[
\bar X_{{\rm se},k}\mapsto\bar X_{{\rm se},k},\quad
\bar Y_{{\rm se},k}\mapsto\bar Y_{{\rm se},k},\quad
W_{{\rm se},k}\Phi_{{\rm se},k}
\mapsto W_{{\rm se},k}\Phi_{{\rm se},k},\quad
\bar Z_{{\rm se},k}\mapsto-\bar X_{{\rm se},k-1}.
\tag{3.1}
\]

This is the assignment at <code>se/artifacts/references/BR_1310.5185v4_collision.tex:665-672</code>. We now check, rather than merely relay, that it satisfies the quoted requirement.

The first three arrows are valid because any matrix may be chosen as its own diamond representative. For the fourth arrow, let \(I\) be the identity operator on the queried copy of \(H\). Then

\[
\Pi_1=I-\Pi_0,\qquad
\Delta_1\circ I=0,\qquad
\Longrightarrow\qquad
\Delta_1\circ\Pi_1=-\Delta_1\circ\Pi_0.
\tag{3.2}
\]

This is BR's one-coordinate relation \(\Pi_1\mapsto-\Pi_0\) (<code>se/artifacts/references/BR_1310.5185v4_collision.tex:356-369</code>). In each matching block, (2.4) shows that \(Z_k^\mu\) and \(X_{k-1}^\mu\) have the same \(e_0^*\) factor on the partner of position \(1\) and the same tail \(S_{k-1}^\mu\); their only queried-coordinate difference is \(\Pi_1\) versus \(\Pi_0\). The right projector on the nonquery legs is also the same \(\bar\Pi'_{{\rm se},k-1}\) in the two barred operators by (2.6), and BR places the primed projector on the remaining \(2n-1\) legs (<code>se/artifacts/references/BR_1310.5185v4_collision.tex:645-646</code>). Finally, the two stacked blocks carry the same \(|M_{\rm se}|^{-1/2}\) factor. Multiplying (3.2) by these common partner, tail, and stack factors proves entrywise that

\[
\Delta_1\circ\bar Z_{{\rm se},k}
=\Delta_1\circ(-\bar X_{{\rm se},k-1}).
\tag{3.3}
\]

At \(k=0\), \(S_{-1}^\mu\) and \(Z_0^\mu\) are zero; set \(\bar X_{{\rm se},-1}:=0\). Thus (3.3) includes the boundary. This verifies all four arrows in (3.1) against the definition in <code>sec:adv</code> and supplies the check summarized by BR at <code>se/artifacts/references/BR_1310.5185v4_collision.tex:673</code>.

Apply (3.1) linearly to IDENT-2 and then to (1.4). Reindexing the two \(X\)-sums, with \(\alpha_k=0\) outside \(0\le k<K\), gives the valid ambient representative

\[
\boxed{
\Delta_1\diamond\widetilde\Gamma_n
:=
\sum_{k\ge0}(\alpha_{k-1}-\alpha_k)\bar X_{{\rm se},k-1}
+\sum_{k\ge0}\alpha_k\bar Y_{{\rm se},k}
+\sum_{k\ge0}\alpha_kW_{{\rm se},k}\Phi_{{\rm se},k}.}
\tag{3.4}
\]

This is precisely BR's assembled image (<code>se/artifacts/references/BR_1310.5185v4_collision.tex:673-676</code>). The symbol \(:=\) chooses a diamond representative; it does not assert uniqueness.

### Restriction to the legal submatrix

Let \(P_Y,P_N\) denote unnormalized coordinate deletion to legal rows and columns. If ambient \(A,B\) satisfy \(\Delta_1\circ B=\Delta_1\circ A\), then every retained legal pair \((y,x)\) with \(y_1\ne x_1\) is also an ambient unequal-symbol pair. Therefore \(B[y,x]=A[y,x]\) on every entry selected by the legal mask, and

\[
\Delta_1^{\rm leg}\circ(P_YBP_N^*)
=P_Y(\Delta_1\circ B)P_N^*
=P_Y(\Delta_1\circ A)P_N^*
=\Delta_1^{\rm leg}\circ(P_YAP_N^*).
\tag{3.5}
\]

The normalized restrictions \(J_Y,J_N\) differ from \(P_Y,P_N\) only by uniform scalar factors, so the same equality holds with \(\mathcal R\). The diamond requirement is entrywise on pairs of inputs, and deleting illegal rows and columns cannot invalidate it. This is the same submatrix mechanism BR uses for query masks (<code>se/artifacts/references/BR_1310.5185v4_collision.tex:338-340</code>), here applied to the diamond equality.

Combining (1.7), (3.4), and (3.5), the legal witness has the following valid chosen representative:

\[
\boxed{
\Delta_1^{\rm leg}\diamond\Gamma_n
:=
\mathcal R\!\left(
\sum_{k\ge0}(\alpha_{k-1}-\alpha_k)\bar X_{{\rm se},k-1}
+\sum_{k\ge0}\alpha_k\bar Y_{{\rm se},k}
+\sum_{k\ge0}\alpha_kW_{{\rm se},k}\Phi_{{\rm se},k}
\right).}
\tag{3.6}
\]

Writing \(\|\cdot\|\) for operator norm, BR's adversary estimate gives

\[
\|\Delta_1^{\rm leg}\circ\Gamma_n\|
\le2\|\Delta_1^{\rm leg}\diamond\Gamma_n\|,
\tag{3.7}
\]

by BR's factor-two diamond estimate (<code>se/artifacts/references/BR_1310.5185v4_collision.tex:211-219</code>). Consequently the witness denominator is controlled by the **legal** operators

\[
\mathcal R(\bar X_{{\rm se},k}),\qquad
\mathcal R(\bar Y_{{\rm se},k}),\qquad
\mathcal R(W_{{\rm se},k}\Phi_{{\rm se},k}),
\tag{3.8}
\]

together with the way their different \(k\)-levels combine in (3.6). This identifies the witness's operators; it does not replace the still-needed legal cross-\(k\) norm argument by a triangle inequality or by BR's ambient orthogonality claim.

## 4. What remains, and what does not

For a partition \(\theta\vdash k\), let \(f^\theta\) denote the dimension of the complex Specht module of shape \(\theta\), and define

\[
\rho_{n,k}:=\max_{\theta\vdash k}
\frac{(2n)^k f^\theta}{k!\,f^{(2n-k,\theta)}} .
\tag{4.1}
\]

This is the matched-degree scalar used by both proved legal bounds (<code>se/artifacts/se_bridge2_pin_20260718.md:74-83</code>).

1. **The legal \(X\)-channel norm is proved.** For \(0\le k\le n\),

   \[
   \|\mathcal R(\bar X_{{\rm se},k})\|\le\rho_{n,k},
   \]

   where \(\rho_{n,k}\) is the maximum matched-degree scalar defined in the cited note. This is Corollary 5.1 at <code>se/artifacts/se_bridge2_pin_20260718.md:334-353</code>; the independent review confirms the X line at <code>se/artifacts/se_bridge2_pin_review_20260718.md:34-38</code>.

2. **The legal \(Y\)-channel norm is proved.** In the witness range \(0\le k<K\),

   \[
   \|\mathcal R(\bar Y_{{\rm se},k})\|
   \le\rho_{n,k}\sqrt2\sqrt{k/n}.
   \]

   This is Corollary 5.2 at <code>se/artifacts/se_bridge2_pin_20260718.md:355-380</code>; the review confirms it at <code>se/artifacts/se_bridge2_pin_review_20260718.md:34-39</code>. Because (1.2)--(2.7) identify these as channels of the witness atom itself, those proved bounds apply to the witness decomposition (3.6).

3. **The legal \(\Phi\)-channel norm is open.** The ambient \(W_{{\rm se},k}\Phi_{{\rm se},k}\) bound is proved, but its legal transfer has unresolved diagonal and off-diagonal children (<code>se/notes/SE_PROOF_DAG.md:458-480</code>). Nothing here promotes \(\|\mathcal R(W_{{\rm se},k}\Phi_{{\rm se},k})\|\) to proved.

4. **Legal cross-\(k\) combination is open.** BR says the different-\(k\) channel operators are mutually orthogonal in the ambient construction (<code>se/artifacts/references/BR_1310.5185v4_collision.tex:688-695</code>). That statement is not imported after legal restriction. The DAG records conflicting legal claims and requires separate adjudication, including the two-sided disjointness needed for parity grouping (<code>se/notes/SE_PROOF_DAG.md:449-456</code>). Thus this note does not claim that the norm of either sum in (3.6) is the maximum of its summand norms.

5. **End-commutativity (Q1) is not needed here.** Put \(G:=((S_n\times S_n)\rtimes\mathbb Z_2)\times S_q\), the full symmetry group named by the DAG. Q1 asks whether \(\operatorname{End}_G(\mathbb C[Y_n])\) is commutative (<code>se/notes/SE_PROOF_DAG.md:443-447</code>). Equations (1.2), (2.3), and (2.7) are identities of explicitly defined orthogonal projectors and operators; (3.3) is an entrywise query-mask identity; and (3.5) is deletion of entries. None requires multiplicity-freeness, simultaneous scalarization, or a commutant assertion. Q1 may matter to a different spectral organization, but it is not a hypothesis of this declaration.

The DAG described the open family-split content as declaring \(P_k=\bar\Pi_{{\rm se},k}\), using IDENT-1/2, and pushing the witness's masked matrix through the split (<code>se/notes/SE_PROOF_DAG.md:430-442,537-540</code>). Sections 1--3 do exactly that. The remaining \(\Phi\) and cross-\(k\) nodes are logically separate.

## 5. Status table

| step | verdict | sources |
|---|---|---|
| Declare \(P_k=\bar\Pi_{{\rm se},k}\), BR's \(S_n\times S_n\) family | **PROVED** | <code>se/artifacts/references/BR_1310.5185v4_collision.tex:603-611</code>; <code>se/notes/SE_HANDOFF_CONTINUE_PROOF.md:28-33</code> |
| BR decomposition \(\widetilde\Gamma_n=\sum_k\alpha_k\bar W_{{\rm se},k}\) | **PROVED** | <code>se/artifacts/references/BR_1310.5185v4_collision.tex:502-508,603-611</code> |
| \(1/\sqrt{|M_{\rm se}|}\) inside each BR block and \(1/q!\) outside the legal witness | **PROVED** | <code>se/artifacts/references/BR_1310.5185v4_collision.tex:526-532</code>; <code>se/notes/SE_HANDOFF_CONTINUE_PROOF.md:28-37</code> |
| IDENT-1 | **PROVED** | <code>se/artifacts/references/BR_1310.5185v4_collision.tex:616-650</code> |
| IDENT-2 and BR channel definitions | **PROVED** | <code>se/artifacts/references/BR_1310.5185v4_collision.tex:653-663</code> |
| IDENT numerical checks | **CORROBORATION ONLY**; maximum on the four requested rows is \(3.373\times10^{-15}\) | <code>se/artifacts/logs_se_py_reverify_20260717/ybar_norms_fresh.log:15,30,43,58</code> |
| Diamond requirement located and quoted | **DEFINED / QUOTED** | <code>se/artifacts/references/BR_1310.5185v4_collision.tex:202-210,221-225</code> |
| \(\bar Z_k\mapsto-\bar X_{k-1}\), including \(k=0\) | **PROVED** | <code>se/artifacts/references/BR_1310.5185v4_collision.tex:356-369,544-553,653-673</code>; equations (3.2)--(3.3) |
| Ambient assembled \(\Delta_1\)-diamond image | **PROVED** | <code>se/artifacts/references/BR_1310.5185v4_collision.tex:673-676</code>; equation (3.4) |
| Diamond assignment survives legal row/column deletion | **PROVED** | definition at <code>se/artifacts/references/BR_1310.5185v4_collision.tex:202-210</code>; submatrix observation at <code>se/artifacts/references/BR_1310.5185v4_collision.tex:338-340</code>; equation (3.5) |
| Witness legal channels are \(\mathcal R(\bar X_k),\mathcal R(\bar Y_k),\mathcal R(W_k\Phi_k)\) | **PROVED** | equations (1.7), (2.7), and (3.6); <code>se/artifacts/references/BR_1310.5185v4_collision.tex:659-676</code> |
| Legal \(X\)-channel bound | **PROVED** | <code>se/artifacts/se_bridge2_pin_20260718.md:334-353</code>; review <code>se/artifacts/se_bridge2_pin_review_20260718.md:34-38</code> |
| Legal \(Y\)-channel bound | **PROVED** | <code>se/artifacts/se_bridge2_pin_20260718.md:355-380</code>; review <code>se/artifacts/se_bridge2_pin_review_20260718.md:34-39</code> |
| Legal \(\Phi\)-channel bound | **OPEN** | <code>se/notes/SE_PROOF_DAG.md:458-480</code> |
| Legal cross-\(k\) combination / orthogonality | **OPEN; not claimed** | ambient-only <code>se/artifacts/references/BR_1310.5185v4_collision.tex:688-695</code>; legal node <code>se/notes/SE_PROOF_DAG.md:449-456</code> |
| End-commutativity Q1 as a premise | **NOT NEEDED** | Q1 at <code>se/notes/SE_PROOF_DAG.md:443-447</code>; direct algebra in Sections 1--3 |

**Final status.** <code>SE.denom.familysplit.ident</code> is discharged: the witness atom is BR's \(\bar W_{{\rm se},k}=W_{{\rm se},k}\bar\Pi_{{\rm se},k}\), and BR's primed family is only the internal projector split producing the \(X,Y,Z,\Phi\) channels. The chosen BR diamond representative restricts entrywise to the legal witness, so all proved **legal** channel bounds apply to these witness operators. The full denominator remains open exactly at the separately recorded legal \(\Phi\) and legal cross-\(k\) nodes.
