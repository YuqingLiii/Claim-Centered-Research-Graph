# Independent certification review: `SE.br.cor16`

## Provenance

- **Date:** 2026-07-23.
- **Reviewer:** codex independent certification reviewer.
- **Commission:** coordination layer per lead directive.
- **Target node:** `SE.br.cor16` (`COR`), `se/proof-dag/nodes/SE.br.cor16.yaml`.
- **Claim in scope:** only the explicit, unconditional
  \[
  \operatorname{Adv}^{\pm}(\operatorname{SE}(n,2n))
  \ge \left(\frac{2}{\sqrt6}-o(1)\right)n^{1/6}
  \]
  lower bound for the frozen tapered witness.
- **Excluded:** the conditional \(n^{1/3}\) chain and T6, W9J, TRACE, GRAM,
  OMEGA, canonical-Gram, physical-transport, output-frame, sandwich, and
  omega-decay claims.

### Rule-7 compliance map

- **7a:** every load-bearing displayed operator identity is typed in the
  dedicated type table below; the table includes ambient and legal dimensions,
  central-isotype dimensions, and arbitrary LR multiplicity \(c\).
- **7b:** all actual parameter regimes are identified below.  The proof uses
  levels up to \(K-1\), not merely \(k\le1\), and it works on whole central
  isotypic blocks.  LR multiplicities \(c\ge2\) may occur as passive
  multiplicity spaces, but no occurrence-space transport identity is used.
- **7c:** Phase A is written without citations to the proposer, prior review, or
  assembly artifacts.  Phase B is separate.  Notational coincidences found
  after comparison are explicitly identified.
- **7d:** the full weak-chain dependency closure, evidence, review date, review
  scope, pre-rule-7 flags, human-review effect, and present re-verification
  disposition are tabulated.
- **7e:** every standing and project-specific failure mode is checked in its
  own table.
- **7f:** every computation is labelled either “proved-formula evaluation” or
  “independent construction”; none is used as proof.
- **7g:** the verdict ends with a self-contained quantified statement defining
  \(o(1)\), the valid \(n\)-range, \(q\), legality, all partition conditions,
  and the taper window.

---

# Phase A — derivation from the frozen definitions

No proposition, prior review, assembly note, or envelope artifact is cited in
this phase.

## A.1 Spaces, legal sets, and the typed frozen witness

Let \(n\ge1\) be an integer, \(q=2n\), and let \(M_n\) be the \(n!\) perfect
bipartite matchings between two labelled \(n\)-position halves.  Write

\[
\begin{aligned}
\mathcal A_N&=L^2([q]^{2n}),&
\dim\mathcal A_N&=q^{2n},\\
\mathcal A_Y&=\mathbb C^{M_n}\otimes L^2([q]^n),&
\dim\mathcal A_Y&=n!q^n.
\end{aligned}
\]

The legal NO set \(N_n\) consists of the bijections from the \(2n\) positions
to \([q]\), and the legal YES set \(Y_n\) consists of a matching
\(\mu\in M_n\) and an injective assignment \(z:[n]\hookrightarrow[q]\) of
values to its edges.  Hence

\[
|N_n|=(q)_{2n}=q!,\qquad
|Y_n|=n!(q)_n=q!.
\]

Put \(\mathcal L_N=L^2(N_n)\) and \(\mathcal L_Y=L^2(Y_n)\); both have
dimension \(q!\).  All these finite \(L^2\) spaces use uniform probability
measure.  Let

\[
J_N:\mathcal A_N\to\mathcal L_N,\qquad
J_Y:\mathcal A_Y\to\mathcal L_Y
\]

be probability-normalized coordinate restrictions.  For
\(T:\mathcal A_N\to\mathcal A_Y\), define the legal transfer

\[
\mathcal R(T)=J_YTJ_N^*:\mathcal L_N\to\mathcal L_Y. \tag{A.1}
\]

Let \(H=L^2([q])=H_0\oplus H_1\), with
\(\dim H_0=1\), \(\dim H_1=q-1\), and constant unit vector \(e_0\in H_0\).
For each matching \(\mu\), the maps

\[
\Psi_0=\Pi_0\otimes e_0^*,\qquad
\Psi_1=\Pi_1\otimes e_0^*+e_0^*\otimes\Pi_1
\]

have type \(H\otimes H\to H\), i.e. \(q\)-by-\(q^2\).  The level map

\[
W_k^\mu=\sum_{\substack{c\in\{0,1\}^n\\|c|=k}}
\Psi_{c_1}\otimes\cdots\otimes\Psi_{c_n}
 :H^{\otimes2n}\to H^{\otimes n}
\]

has size \(q^n\)-by-\(q^{2n}\).  Stacking its \(n!\) matching blocks with
factor \(1/\sqrt{n!}\) gives

\[
W_{{\rm se},k}:\mathcal A_N\to\mathcal A_Y,
\]

of size \(n!q^n\)-by-\(q^{2n}\).

Let \(P_k^{\rm amb}\) be the orthogonal projector on
\(\mathcal A_N=H^{\otimes n}\otimes H^{\otimes n}\) onto exact total
weight \(k\) and position-\(S_n\times S_n\) types having total first-row
defect \(k\).  The legal set is position invariant, so there is a legal
projector \(P_k^{\rm leg}:\mathcal L_N\to\mathcal L_N\) satisfying

\[
J_NP_k^{\rm amb}=P_k^{\rm leg}J_N. \tag{A.2}
\]

This distinction makes the frozen notation \(W_k^{\rm leg}P_k\) type-correct:
there \(P_k=P_k^{\rm leg}\), a \(q!\)-by-\(q!\) operator, not the
\(q^{2n}\)-by-\(q^{2n}\) ambient projector.

For \(y=(\mu,z)\in Y_n\), order the matching edges as
\((a_r,b_r)\), \(1\le r\le n\), and for \(x\in N_n\) set

\[
m_r(y,x)=\mathbf1\{x_{a_r}=z_r\text{ or }x_{b_r}=z_r\}.
\]

The frozen raw legal kernel is the \(q!\)-by-\(q!\) matrix

\[
W_k^{\rm leg}[y,x]
=e_k(qm_1(y,x)-2,\ldots,qm_n(y,x)-2). \tag{A.3}
\]

The raw matching kernel has common coefficient
\(q^{-3n/2}/\sqrt{n!}\).  The two probability-\(L^2\) restrictions
contribute

\[
\frac{q^{3n/2}}{\sqrt{(q)_n(q)_{2n}}}.
\]

Their product is

\[
\frac1{\sqrt{n!(q)_n(q)_{2n}}}=\frac1{q!}, \tag{A.4}
\]

using \(n!(q)_n=(q)_{2n}=q!\).  Thus, with the typed legal projector,

\[
\mathcal R(W_{{\rm se},k}P_k^{\rm amb})
=\frac1{q!}W_k^{\rm leg}P_k^{\rm leg}. \tag{A.5}
\]

Put

\[
K=\lfloor n^{1/3}\rfloor,\qquad
\alpha_k=(K-k)_+,
\]

and define

\[
\Gamma_n=\frac1{q!}\sum_{k=0}^{K-1}(K-k)
W_k^{\rm leg}P_k^{\rm leg}:\mathcal L_N\to\mathcal L_Y. \tag{A.6}
\]

Every term in (A.6) is a real \(q!\)-by-\(q!\) operator.

## A.2 Numerator

Let \(\mathbf1_N,\mathbf1_Y\) be the unit constant vectors.  Since
\(e_0(\cdot)=1\), (A.3) gives \(W_0^{\rm leg}=J\), the all-ones matrix.
The trivial position type lies in \(P_0^{\rm leg}\), whereas
\(P_k^{\rm leg}\mathbf1_N=0\) for \(k>0\).  Equation (A.4) then gives

\[
\Gamma_n\mathbf1_N=K\mathbf1_Y,\qquad
\|\Gamma_n\|\ge K. \tag{A.7}
\]

This is exact for every \(n\ge1\).  In particular, the \(K^2\) scale that
appears later is a denominator-envelope term, not the numerator; the numerator
used by the claim is \(K\).

## A.3 The legal diamond representative

Let

\[
\Phi_d^{(m)}
=\bar\Pi_d^{(m)}
-\Pi_0\otimes\bar\Pi_d^{(m-1)}
-\Pi_1\otimes\bar\Pi_{d-1}^{(m-1)}
\]

on \(H^{\otimes m}\), and let

\[
\Phi_{{\rm se},k}
=\sum_{\ell=0}^{k-1}\Phi_{k-\ell}^{(n)}
\otimes\bar\Pi_\ell^{(n)}
\]

on \(\mathcal A_N\).  Separating the queried matched pair yields ambient
maps

\[
\bar X_k,\bar Y_k,\bar Z_k,T_k:
\mathcal A_N\to\mathcal A_Y,\qquad
T_k=W_{{\rm se},k}\Phi_{{\rm se},k},
\]

all of size \(n!q^n\)-by-\(q^{2n}\), with

\[
W_{{\rm se},k}P_k^{\rm amb}
=\bar X_k+\bar Y_k+\bar Z_k+T_k. \tag{A.8}
\]

On the query leg,
\(\Delta_1\circ\Pi_1=-\Delta_1\circ\Pi_0\).  The partner, tail,
primed projector, and stack factors in \(\bar Z_k\) and
\(\bar X_{k-1}\) agree.  Hence
\(\bar Z_k\) may be replaced by \(-\bar X_{k-1}\) in a diamond
representative.  Legal restriction preserves the entrywise equality.  With

\[
X_k=\mathcal R(\bar X_k),\qquad
Y_k=\mathcal R(\bar Y_k),\qquad
C_k=\mathcal R(T_k),
\]

the chosen legal representative is

\[
D=\sum_{k\ge0}(\alpha_{k-1}-\alpha_k)X_{k-1}
+\sum_{k\ge0}\alpha_kY_k+\sum_{k\ge0}\alpha_kC_k
 :\mathcal L_N\to\mathcal L_Y. \tag{A.9}
\]

All sums are finite because \(\alpha_k=0\) off \(0\le k<K\).

For completeness, the factor two does not require an opaque norm theorem.
Partition rows and columns according to the queried alphabet symbol.  The
equal-symbol part of any \(B:\mathcal L_N\to\mathcal L_Y\) is an orthogonal
direct sum of diagonal symbol blocks and has norm at most \(\|B\|\).
Therefore

\[
\|\Gamma_n\circ\Delta_1\|
=\|D\circ\Delta_1\|
\le\|D\|+\|\text{equal-symbol part of }D\|
\le2\|D\|. \tag{A.10}
\]

## A.4 Central defect support; no occurrence-space transport

For \(S\in\{N,Y\}\), let \(E_d^S\) be the legal central alphabet projector
onto partitions \(\lambda\vdash q\) of defect \(q-\lambda_1=d\).

On \(\mathcal L_N=L^2(S_q)\),

\[
E_\lambda^N\mathcal L_N
\cong S^\lambda_{\rm alph}\otimes S^\lambda_{\rm pos},
\qquad
\dim E_\lambda^N\mathcal L_N=(f^\lambda)^2. \tag{A.11}
\]

On the YES side,

\[
E_\lambda^Y\mathcal L_Y
\cong S^\lambda_{\rm alph}\otimes\mathbb C^{m_Y(\lambda)},
\quad
m_Y(\lambda)=n!f^{\lambda/(q-n)}, \tag{A.12}
\]

so its dimension is \(f^\lambda n!f^{\lambda/(q-n)}\).

The primed \(X/Y\) carrier has exact weight \(k\) and all its full-position
types have defect at least \(k\).  Legal NO restriction pairs equal alphabet
and position shapes by (A.11), while exact weight \(k\) permits alphabet
defect at most \(k\).  Alphabet equivariance transports the same central
label to the YES side.  Consequently

\[
X_k=E_k^YX_kE_k^N,\qquad
Y_k=E_k^YY_kE_k^N. \tag{A.13}
\]

For \(T_k\), branching the first half to \(S_{n-1}\) gives first-half
position defect \(k-\ell-1\), while the second half has defect \(\ell\).
The LR first-row inequality
\(c^\tau_{\sigma,\sigma'}>0\Rightarrow
\tau_1\le\sigma_1+\sigma'_1\), followed by adding the singled-out box,
shows full-position defect at least \(k-1\).  Exact weight gives the upper
bound \(k\).  The map \(T_k\) and both legal restrictions are alphabet
intertwiners.  Thus

\[
C_k=C_{k\to k-1}+C_{k\to k},\qquad
C_{k\to d}=E_d^YC_kE_d^N, \tag{A.14}
\]

for \(k\ge2\); \(C_1=C_{1\to1}\) and \(C_0=0\).

The LR coefficient in the support argument may be
\(c=c^\tau_{\sigma,\sigma'}\ge2\).  The corresponding position sector has
type

\[
S^\sigma\otimes S^{\sigma'}\otimes\mathbb C^c
\quad\text{and dimension}\quad f^\sigma f^{\sigma'}c. \tag{A.15}
\]

Only the predicate \(c>0\) and the first-row inequality are used.  No map is
defined from a space of dimension \(f^\theta\) to one of dimension
\(f^\theta c\), and no fixed-\(c\) endomorphism is asserted.

## A.5 Uniform legal restriction scalars

For \(\theta\vdash d\), put

\[
\lambda(d,\theta)=(q-d,\theta),\qquad
r_{\rm top}(q,d,\theta)
=\frac{q^df^\theta}{d!f^{(q-d,\theta)}},\qquad
\rho_d=\max_{\theta\vdash d}r_{\rm top}(2n,d,\theta).
\]

Completion of an \(m\)-position injection to a permutation and forgetting
back to its first \(m\) values give a commuting square of isometries.
Peter-Weyl on the full permutation space then gives, on the whole
\(\lambda\)-isotypic component (including every multiplicity vector),

\[
\|R_mP_{m,d}A_{m,\lambda(d,\theta)}\|^2
\le r_{\rm top}(q,d,\theta), \tag{A.16}
\]

with equality for \(m=q\).

Here is the scalar calculation.  The full-permutation degree-\(s\) scalar is

\[
r_s(\lambda)=\frac1{f^\lambda}\sum_{t=0}^s
q^t(-1)^{s-t}\binom{q-t}{s-t}
\frac{f^{\lambda/(q-t)}}{t!}. \tag{A.17}
\]

For \(s=d\) and \(\lambda=(q-d,\theta)\), only \(t=d\) survives, giving
\(r_d=r_{\rm top}\).  For \(s=d+1\), if \(q-d>\theta_1\), the \(t=d\)
and \(t=d+1\) terms give

\[
r_{d+1}(\lambda)=d\,r_{\rm top}(q,d,\theta). \tag{A.18}
\]

The YES completion inequality (A.16) applies to every position isotype and
every multiplicity vector; it is not a same-copy or diagonal extraction.
Multiplying the square roots of the YES and NO outer bounds yields

\[
\begin{aligned}
\|X_d\|&\le\rho_d,\\
\|Y_d\|&\le\rho_d\sqrt{\frac{2d}{n}},\\
\|C_{d\to d}\|&\le\rho_d\|T_d\|,\\
\|C_{d+1\to d}\|&\le d\,\rho_d\|T_{d+1}\|.
\end{aligned} \tag{A.19}
\]

The second inequality uses the following direct ambient count.  In a
principal \(S_{n-1}\times S_n\) sector, antisymmetrizing fixed pairs supplies
a principal singular vector having exactly one \(H_1\) entry in each pair.
The \(Y\)-block vanishes unless the partner of query position \(1\) is one
of at most \(2d\) marked second-half positions.  Exactly \((n-1)!\) of the
\(n!\) matchings choose each partner, and each surviving matching block is
a contraction on that vector.  The stacked squared norm is therefore at
most \(2d/n\).  This argument is on the whole principal singular subspace
and is independent of any LR multiplicity.

The hook formula gives the exact product

\[
r_{\rm top}(q,d,\theta)
=\frac{q^d}{(q)_d}
\prod_{c=1}^{\theta_1}
\left(1+\frac{\theta'_c}{q-d-c+1}\right). \tag{A.20}
\]

Using \(-\log(1-x)\le x/(1-x)\) and
\(\log(1+x)\le x\),

\[
\log r_{\rm top}(q,d,\theta)
\le
\frac{d(d-1)}{2(q-d+1)}
+\frac d{q-2d+1}. \tag{A.21}
\]

For \(q=2n\) and \(0\le d\le K\), this is \(O(n^{-1/3})\), uniformly in
\(\theta\).  Thus

\[
\rho_d=1+O(n^{-1/3}) \tag{A.22}
\]

uniformly over the taper window.

## A.6 The ambient \(\Phi\) constant and the printed special-path defect

On the two orthogonal domain branches of \(\Phi_s^{(m)}\), the defining
projector difference gives respectively

\[
\frac1{\sqrt{m-2s+1}}
\quad\text{and}\quad
\frac1{\sqrt{m-2s+2}}.
\]

Cauchy-Schwarz, without assuming orthogonal output ranges, gives

\[
\|\Phi_s^{(m)}\|
\le
\sqrt{\frac1{m-2s+1}+\frac1{m-2s+2}}. \tag{A.23}
\]

The \(W\)-factor on the relevant \(k-1\)-pair fixed space is at most
\(\sqrt3\).  The only delicate local arithmetic is the special path.  If
the path has \(|P|\ge4\) vertices, the normalized input has
\(2^{(|P|-2)/2}\) equal-amplitude orthogonal terms and at most two survive.
Therefore its projected norm factor is

\[
\sqrt{\frac2{2^{(|P|-2)/2}}}
=2^{-(|P|-4)/4}, \tag{A.24}
\]

the reciprocal of the factor printed in the source line later identified
in Phase B.  The corresponding \(0\)-\(1\) row/column count contributes
\(\sqrt{2^{C-1}(|P|+2)}\), while cycles contribute the cancelling
\(2^{-C/2}\).  Squaring the remaining product gives

\[
\frac{|P|+2}{2}\,
2^{-\max(0,|P|-4)/2}\le3, \tag{A.25}
\]

with equality at \(|P|=4\).  This proves the \(\sqrt3\) constant rather
than inferring it from samples.

In the SE summand indexed by \(\ell\), take \(m=n\) and
\(s=k-\ell\le k\).  Combining (A.23) with \(\sqrt3\) yields

\[
\|T_k\|\le\frac{\sqrt6}{\sqrt{n-2k+1}},
\qquad 1\le k<K. \tag{A.26}
\]

For \(n\ge8\), \(K\le n/3\), so the stability hypothesis
\(s<n/3\) and all displayed denominators hold throughout the taper.

## A.7 Defect assembly and the constant

Blocks with different alphabet defects have orthogonal domain and range.
Writing

\[
\beta_d=\alpha_d-\alpha_{d+1},
\]

equations (A.9), (A.13), and (A.14) give the exact finite orthogonal sum

\[
D=\bigoplus_{0\le d<K}D_d,\qquad
D_d=\beta_dX_d+\alpha_dY_d
+\alpha_dC_{d\to d}+\alpha_{d+1}C_{d+1\to d}. \tag{A.27}
\]

Missing endpoint blocks are zero.  The triangle inequality inside each
fixed-\(d\) block, (A.19), and (A.26) give

\[
\begin{aligned}
\|D\|\le\max_{0\le d<K}\rho_d\Bigg[
&|\beta_d|+\sqrt2\,\alpha_d\sqrt{\frac dn}\\
&+\mathbf1_{\{d\ge1\}}
\frac{\sqrt6\,\alpha_d}{\sqrt{n-2d+1}}\\
&+\mathbf1_{\{d\ge1\}}
\frac{\sqrt6\,d\,\alpha_{d+1}}{\sqrt{n-2d-1}}
\Bigg]. \tag{A.28}
\end{aligned}
\]

For the frozen taper, \(\beta_d=1\) on \(0\le d<K\).
The first term is \(1+o(1)\).  The second is \(O(1)\), since

\[
\max_d(K-d)\sqrt{d/n}
=O(K^{3/2}/\sqrt n)=O(1).
\]

The third is \(O(K/\sqrt n)=O(n^{-1/6})\).  For the fourth,

\[
\max_{0\le d<K}d(K-d-1)
=\left\lfloor\frac{(K-1)^2}{4}\right\rfloor. \tag{A.29}
\]

Uniformly over \(d<K\),
\((n-2d-1)^{-1/2}=n^{-1/2}(1+O(n^{-2/3}))\).  Therefore

\[
\|D\|
\le\left(\frac{\sqrt6}{4}+o(1)\right)n^{1/6}+O(1). \tag{A.30}
\]

By (A.10),

\[
\|\Gamma_n\circ\Delta_1\|
\le\left(\frac{\sqrt6}{2}+o(1)\right)n^{1/6}. \tag{A.31}
\]

Within-half position permutations and the half swap preserve both legal
sets, the matching stack, the symmetric \(\Psi_0,\Psi_1\), the sum defining
\(P_k\), and the taper.  The induced row and column permutation unitaries
therefore carry the mask at any position to that at position \(1\).  Thus

\[
\max_{i\in[2n]}\|\Gamma_n\circ\Delta_i\|
=\|\Gamma_n\circ\Delta_1\|. \tag{A.32}
\]

This maximum is positive: (A.7) makes \(\Gamma_n\ne0\), and every legal
YES/NO pair differs in at least one position, so any nonzero entry of
\(\Gamma_n\) survives at least one query mask.

Finally \(K=n^{1/3}(1+O(n^{-1/3}))\).  Combining (A.7), (A.31), and
(A.32),

\[
\frac{\|\Gamma_n\|}
{\max_i\|\Gamma_n\circ\Delta_i\|}
\ge
n^{1/6}
\frac{1+O(n^{-1/3})}{\sqrt6/2+o(1)}
=\left(\frac2{\sqrt6}-o(1)\right)n^{1/6}. \tag{A.33}
\]

The arithmetic is explicitly

\[
\frac1{\sqrt6/2}=\frac2{\sqrt6}.
\]

---

# Full dependency closure (7d)

“Flag” means that the archived review predates rule 7, was affected by the
2026-07-19 human review, or did not review the exact granularity used here.
Every flagged load-bearing input is re-verified in Phase A; no flag is
carried as a caveat.

| Load-bearing input | Evidence file and lines | Archived review, date, and reviewed scope | Flag | Disposition in this review |
|---|---|---|---|---|
| Adversary ratio, mask, diamond definition | `se/artifacts/references/BR_1310.5185v4_collision.tex:170-225` | `se/artifacts/se_cor16_review_20260718.md:45-73`, 2026-07-18, feasibility and ratio direction | Pre-rule-7 | Re-derived the factor-two mask inequality in (A.10) and checked nonzero witness/positive denominator. |
| Legal sets, dimensions, common \(1/q!\) normalization | `se/artifacts/se_familysplit_20260718.md:78-127` | `se/artifacts/se_cor16_review_20260718.md:75-126`, 2026-07-18, exact count and normalization; `se/artifacts/se_human_review_20260719.md:80-82`, 2026-07-19, normalization and numerator | Pre-rule-7; family review did not itself review the exact scalar | Recomputed (A.4) and distinguished ambient from legal \(P_k\). |
| Frozen \(W_k,P_k\), channel split, signed diamond assignment | `se/artifacts/references/BR_1310.5185v4_collision.tex:483-676`; `se/artifacts/se_familysplit_20260718.md:132-329` | `se/artifacts/se_bridge2_reviews_20260718.md:55-68`, 2026-07-18, family identity and \(\bar Z_k\mapsto-\bar X_{k-1}\) | Pre-rule-7 | Re-expanded the query-leg identity and typed all maps in (A.8)-(A.9). |
| Exact numerator | `se/artifacts/se_cor16_20260718.md:47-53` | `se/artifacts/se_cor16_review_20260718.md:75-132`, 2026-07-18, numerator with correction \(S_q\to S_n\times S_n\); human review `:81-83` | Pre-rule-7 | Re-derived (A.7) directly. |
| Matched-degree completion scalar | `se/artifacts/se_bridge2_md_inst_20260718.md:43-59,61-202,208-245` | `se/artifacts/se_bridge2_reviews_20260718.md:21-29`, 2026-07-18, completion, scalar, equality, endpoint; human review `:83` | Pre-rule-7 | Re-derived the commuting completion square and (A.16)-(A.17) on whole isotypes. |
| X/Y defect pinning and two-sided support | `se/artifacts/se_bridge2_pin_20260718.md:85-236,238-308` | `se/artifacts/se_bridge2_pin_review_20260718.md:18-40`, 2026-07-18, LR, induced span, Peter-Weyl, equivariance, endpoints; human review `:84` | Pre-rule-7 | Re-derived (A.11)-(A.13), including full block dimensions and arbitrary multiplicity. |
| Ambient \(X\) and \(Y\) estimates | `se/artifacts/references/BR_1310.5185v4_collision.tex:1341-1350`; `se/artifacts/se_stage2_py_verdict.md:33-105` | `se/artifacts/se_bridge2_pin_review_20260718.md:37-39`, 2026-07-18, legal corollaries assuming ambient inputs | Pre-rule-7; human review `:91` says the ambient Schur reductions were compressed | Re-derived the principal-sector argument, stack norm, and exact \(2d/n\) partner count in A.5. |
| \(\Phi_s^{(m)}\) ambient branch estimates | `se/artifacts/references/BR_1310.5185v4_collision.tex:831-986` | `se/artifacts/se_phi_blind_lineread_codex_20260717.md:28-62,138-162`, 2026-07-17, line audit and explicit constants | Pre-rule-7 | Re-derived the two branch bounds and their Cauchy-Schwarz combination (A.23). |
| Special-path \(W\)-factor | `se/artifacts/references/BR_1310.5185v4_collision.tex:1197-1338` | `se/artifacts/se_phi_blind_lineread_codex_20260717.md:65-93,164-174,198-203`, 2026-07-17, line audit locating the reciprocal error | Pre-rule-7; human review `:91` expressly flags the claimed erratum | Independently counted survivors, repaired the printed reciprocal, and proved (A.24)-(A.25). |
| Ambient SE \(T_k=W_k\Phi_k\) reduction | `se/artifacts/references/BR_1310.5185v4_collision.tex:1361-1372`; `se/artifacts/se_phi_xbar_qfree_audit_20260717.md:89-104,134-163` | `se/artifacts/se_phi_legal_review_20260718.md:40-42`, 2026-07-18, constant/range as imported | Pre-rule-7; human review `:91` flags compression | Re-derived sector isolation by \(\ell\), stability \(k<K\le n/3\), and (A.26). |
| One-defect completion bound | `se/artifacts/se_one_defect_forgetting_bound.md:11-61,100-273` | `se/artifacts/se_phi_legal_review_20260718.md:34-39,113-173`, 2026-07-18, independent derivation and multiplicity uniformity | Pre-rule-7; human review `:91` flags completion constants | Re-derived (A.17)-(A.19), including the exact \(r_{d+1}=dr_d\) calculation. |
| Hook envelope \(\rho_d=1+o(1)\) | `se/artifacts/se_legal_conditioning_top_gram.md:20-49,275-289` | `se/artifacts/se_phi_legal_review_20260718.md:40`, 2026-07-18, exact hook product and exponential envelope | Pre-rule-7 | Re-derived (A.20)-(A.22).  The numerical node `SE.denom.assembly.envelope` is not used. |
| Legal \(\Phi\) support, diagonality, per-block bounds | `se/artifacts/se_phi_legal_20260718.md:106-237,239-406` | `se/artifacts/se_phi_legal_review_20260718.md:19-44,73-204`, 2026-07-18, support, full-permutation and YES factors, range, conditional arithmetic | Pre-rule-7 | Re-derived support and block bounds in A.4-A.6 without any strong-chain identity. |
| Cross-defect orthogonality and exact assembly | `se/artifacts/se_crossk_20260718.md:61-213,215-352` | `se/artifacts/se_crossk_review_20260718.md:22-36,38-437`, 2026-07-18, witness-range support, signed coefficients, endpoints, constant | Pre-rule-7; human review `:91` calls the weak corollary near-certifiable | Re-derived the finite orthogonal sum (A.27), endpoints, envelope (A.28), and exact maximum (A.29). |
| All-position symmetry | `se/artifacts/se_cor16_20260718.md:65-69` | `se/artifacts/se_cor16_review_20260718.md:186-214`, 2026-07-18, independent half-swap repair | Pre-rule-7; original citation incomplete | Re-derived (A.32) from the frozen maps. |
| Floor effects and final reciprocal | `se/artifacts/se_cor16_20260718.md:71`; `se/artifacts/se_crossk_20260718.md:310-352` | `se/artifacts/se_cor16_review_20260718.md:216-242`, 2026-07-18, reciprocal/floor arithmetic | Pre-rule-7 | Recomputed (A.29)-(A.33) exactly. |

The human-demoted strong inputs are absent from this table because they are
not dependencies.  In particular, the weak proof does not call
`SE.denom.Phi.legal.gram`, `SE.denom.Phi.legal.omega`,
`SE.denom.Phi.legal.trace`, T6, W9J, or any sandwich/transport identity.

---

# Type audit and regime gates (7a, 7b)

## 7a. Every displayed load-bearing operator identity

The following table audits every operator identity displayed in the
load-bearing chain.  Scalar equalities and inequalities are not operator
identities.

| Identity | Domain \(\to\) codomain | Dimensions | Well-definedness check |
|---|---|---|---|
| \(\Psi_i\) and \(W_k^\mu\) | \(H^{\otimes2}\to H\); \(\mathcal A_N\to H^{\otimes n}\) | \(q^2\to q\); \(q^{2n}\to q^n\) | \(\Pi_i:H\to H\), \(e_0^*:H\to\mathbb C\); tensor factors follow matching edges. |
| Matching stack \(W_{{\rm se},k}\) | \(\mathcal A_N\to\mathcal A_Y\) | \(q^{2n}\to n!q^n\) | Direct stack of \(n!\) identically typed blocks; \(1/\sqrt{n!}\) is scalar. |
| Ambient projector and atom | \(P_k^{\rm amb}:\mathcal A_N\to\mathcal A_N\); \(W_{{\rm se},k}P_k^{\rm amb}:\mathcal A_N\to\mathcal A_Y\) | \(q^{2n}\to q^{2n}\); \(q^{2n}\to n!q^n\) | Position and weight projectors commute; the product is on the domain side. |
| Legal transfer (A.1) | \(\mathcal L_N\to\mathcal L_Y\) | \(q!\to q!\) at \(q=2n\) | \(J_N^*:\mathcal L_N\to\mathcal A_N\), \(T:\mathcal A_N\to\mathcal A_Y\), \(J_Y:\mathcal A_Y\to\mathcal L_Y\). |
| Projector intertwining (A.2) | \(\mathcal A_N\to\mathcal L_N\) on both sides | \(q^{2n}\to q!\) | Legal set is invariant under \(S_n\times S_n\), so coordinate restriction intertwines its central projectors. |
| Normalized atom (A.5) | \(\mathcal L_N\to\mathcal L_Y\) | \(q!\to q!\) | RHS uses \(W_k^{\rm leg}:\mathcal L_N\to\mathcal L_Y\) and \(P_k^{\rm leg}:\mathcal L_N\to\mathcal L_N\), not the ambient projector. |
| Witness (A.6) | \(\mathcal L_N\to\mathcal L_Y\) | \(q!\to q!\) | Finite sum of equally typed real maps. |
| Numerator action (A.7) | \(\mathbf1_N\in\mathcal L_N\mapsto\mathbf1_Y\in\mathcal L_Y\) | \(q!\)-vectors | \(P_k^{\rm leg}\mathbf1_N=0\) for \(k>0\); the \(k=0\) map is \(J/q!\). |
| Channel identity (A.8) | \(\mathcal A_N\to\mathcal A_Y\) | \(q^{2n}\to n!q^n\) | \(\Phi_{{\rm se},k}\) and the three carrier projectors are endomorphisms of \(\mathcal A_N\); left multiplication by \(W,X,Y,Z\) gives the common codomain. |
| Legal diamond sum (A.9) | \(\mathcal L_N\to\mathcal L_Y\) | \(q!\to q!\) | Legal restriction makes every channel equally typed; reindexing uses zero extensions of \(\alpha_k\). |
| Central support (A.13)-(A.14) | \(E_d^N\mathcal L_N\to E_d^Y\mathcal L_Y\) | \((f^\lambda)^2\) on a NO \(\lambda\)-block to \(f^\lambda n!f^{\lambda/(q-n)}\) on the YES block | \(T,X,Y,J_N,J_Y\) are alphabet intertwiners; the same \(\lambda\), hence the same defect, occurs on both sides. |
| LR sector (A.15) | Position sector, before legal outer maps | \(f^\sigma f^{\sigma'}c\), \(c=c^\tau_{\sigma,\sigma'}\ge1\) | Only inclusion/support is used.  No synthesis map with domain \(f^\theta\) is composed with an \(f^\theta c\) operator. |
| Completion bound (A.16) | \(P_{m,d}A_{m,\lambda}L^2([q]^m)\to L^2(\operatorname{Inj}([m],[q]))\) | ambient \(q^m\) to legal \((q)_m\), restricted to all copies of \(S^\lambda\) | Completion and forgetting are isometries; the vector inequality holds on the entire isotypic component, including every multiplicity coordinate. |
| Defect sum (A.27) | \(\bigoplus_dE_d^N\mathcal L_N\to\bigoplus_dE_d^Y\mathcal L_Y\) | sums of the block dimensions above | Distinct \(d\) projectors are orthogonal on both sides; within one \(d\), all four summands have identical domain/codomain. |
| Half-swap covariance behind (A.32) | \(\mathcal L_N\to\mathcal L_Y\) | \(q!\to q!\) | Row and column permutation operators are unitary; half swap permutes matchings and exchanges the two terms of the symmetric \(P_k\) sum. |

## 7b. Regime-complete identity gates

1. **Level regime.**  The proof is not confined to \(k\le1\).  It covers every
   integer \(0\le k<K\).  For \(n\ge8\), \(K\ge2\),
   \(k<K\le n/3\), and every BR branching denominator is positive.  The
   endpoints \(k=0\), \(k=1\), \(d=0\), and \(d=K-1\) are explicitly handled.

2. **Partition regime.**  Every central block has
   \(\lambda=(q-d,\theta)\), \(\theta\vdash d\), with \(0\le d\le K\).
   Since \(q=2n\) and \(d\le K\le n\), \(q-d\ge d\ge\theta_1\), so this is a
   partition.  The one-defect equality additionally uses
   \(q-d>\theta_1\), which follows from \(d=k-1<K\).

3. **LR multiplicity regime.**  Coefficients \(c\ge2\) can occur in the
   induced position support.  They are not assumed away.  The support proof
   uses only \(c>0\), the completion estimate is a vector inequality on the
   full isotypic component, and every assembled projector is central in the
   alphabet action.  Thus all \(c\ge1\) copies are exercised simultaneously.
   The chain is **block-scalar/multiplicity-uniform**, not \(c=1\).

4. **Why the human \(c>1\) type break is irrelevant here.**  This chain never
   uses a formula of the form
   \(E_K[\rho_\theta(\sigma)\otimes L]E_D^*\), never defines a fixed
   multiplicity-space transport \(L\), never takes a normalized
   multiplicity trace, and never uses an output-frame Gram.  Its only
   multiplicity statements are whole-block support and whole-block norm
   inequalities, both typed above.

There is no extant parameter regime in this weak chain that lacks an identity
gate; hence rule 7b does not impose a caveat.

---

# Standing failure-mode audit (7e)

| Failure mode | Finding for this chain |
|---|---|
| Dropped/extra normalization | No failure.  The matching stack contributes exactly \(1/\sqrt{n!}\); the two legal restrictions and raw kernel give one common \(1/q!\), derived in (A.4).  No second matching factor is inserted. |
| Type/dimension mismatch | The archived shorthand \(W_k^{\rm leg}P_k\) is ambiguous if \(P_k\) is read as ambient.  This review resolves it as \(P_k^{\rm leg}\) and records (A.2).  All subsequent compositions type-check, including arbitrary \(c\). |
| Undefined “admissible” or stability range | “Admissible” is unused.  The exact ranges are \(n\ge8\), \(0\le k<K\), \(0\le d<K\), \(\theta\vdash d\), and \(k-\ell<n/3\).  The taper window is explicitly \(\alpha_k=(K-k)_+\). |
| Colored-orbit sum substituted for full central sum | Absent.  The weak proof uses full central alphabet projectors \(E_\lambda^S\) and the full-permutation scalar (A.17), not a fixed-colour orbit sum. |
| Numerics validate a value while printed derivation is broken | The BR special-path line is indeed algebraically broken: its factor is printed without the reciprocal.  Equations (A.24)-(A.25) repair the derivation analytically.  Numerics are not used to excuse the print error. |
| Missing raw colour multiplicity \(m=\binom ja\) | Not applicable: no raw coloured-orbit enumeration or normalized-colour conversion occurs anywhere in the weak chain. |
| Physical \(\omega=(1-p_0)/p_0\) confused with taper proxy \((n-j-1)/(n-j)\) | Not applicable: neither physical omega nor a taper omega proxy is used. |
| Same-index/diagonal extraction substituted for full-copy row-sum contraction | Absent.  Completion bounds apply to every vector in the full isotypic component; assembly uses central orthogonal blocks, not a same-copy extraction or trace. |

---

# Phase B — comparison and reconciliation

Phase B began only after the Phase-A derivation above was fixed.

## B.1 Proposer note and pre-rule-7 review

Comparison sources:

- `se/artifacts/se_cor16_20260718.md`;
- `se/artifacts/se_cor16_review_20260718.md`;
- `se/proof-dag/nodes/SE.denom.assembly.yaml`;
- `se/proof-dag/nodes/SE.denom.assembly.envelope.yaml`;
- `se/artifacts/se_crossk_20260718.md`;
- `se/artifacts/se_crossk_review_20260718.md`;
- `se/artifacts/se_human_review_20260719.md`.

The following points reconcile all discrepancies.

1. **Numerator group label.**  The proposer note says the higher levels contain
   no trivial \(S_q\)-representation.  Its review correctly changes this to
   the position group \(S_n\times S_n\).  Phase A uses the corrected position
   statement.

2. **Normalization provenance.**  The pre-rule-7 review observes that the BR
   all-ones argument alone gives no exact \(q=2n\) normalization.  Phase A
   derives \(1/q!\) directly from the raw coefficient and both probability
   restrictions.

3. **Projector type.**  The archived formula writes the same symbol \(P_k\)
   before and after restriction.  Read literally with ambient dimensions, the
   legal product is ill-typed.  Equation (A.2) supplies the legal
   \(q!\)-dimensional intertwining projector and makes the intended identity
   precise.  This is a notation repair, not a new analytic premise.

4. **Denominator formula.**  Phase A independently obtains exactly the four
   terms of `se_crossk` equation (6.2), including the endpoint indicators,
   coefficient \(\beta_d=1\), the lower-defect factor \(d\), and the single
   factor two.  The coincidence is flagged: the same frozen channel
   decomposition and taper force the same notation
   \(\alpha_d,\beta_d,C_{k\to d},D_d\).

5. **Where \(K^2\) occurs.**  The numerator is \(K\), agreeing with the proposer.
   The \(K^2/\sqrt n\) term is
   \(d\alpha_{d+1}/\sqrt n\) in the denominator envelope.  Any description of
   a “\(K^2\)-type numerator” is a wording error and is not used.

6. **Half-swap.**  The original note's citation proves within-half symmetry
   but not the half swap.  Its review supplies the missing derivation.  Phase A
   independently checks symmetry of \(\Psi_0,\Psi_1\), the matching stack, and
   \(P_k\), yielding (A.32).

7. **Numerical envelope node.**  `SE.denom.assembly.envelope` remains a
   finite-scan record for a different \(R_{n,k}\) comparison.  The weak proof
   does not depend on it: (A.20)-(A.22) give an analytic uniform hook envelope.

8. **Printed special-path line.**  BR source line
   `se/artifacts/references/BR_1310.5185v4_collision.tex:1307` prints the
   reciprocal in the wrong direction, exactly as the 2026-07-17 blind audit
   reports.  Phase A derives the corrected factor from the number and
   amplitudes of surviving terms and independently recovers \(\sqrt3\).

9. **Human review demotions.**  The type break at \(c>1\), output-frame Grams,
   matching-twirl, coloured-orbit identity, raw sandwich, undefined
   “admissible,” and omega-decay criticisms at
   `se/artifacts/se_human_review_20260719.md:15-76` concern the stronger chain.
   None appears in the dependency closure above.

10. **Human weak-chain reservations.**  Section nine of the human review
    (`:88-92`) identifies four remaining issues for the \(n^{1/6}\) corollary:
    completion constants, the special-path correction, compressed ambient
    \(X/Y/\Phi\) reductions, and reliance on an unavailable proof record.
    Phase A resolves them respectively in A.5, A.6, A.5-A.6, and the explicit
    derivation A.1-A.7.  The on-disk records are enumerated in the dependency
    table rather than treated as private inputs.

11. **Notational-coincidence flag required by 7c.**  The constant-vector
    numerator proof, the definitions \(\alpha_k=(K-k)_+\) and
    \(\beta_d=\alpha_d-\alpha_{d+1}\), the defect block \(C_{k\to d}\), and the
    quadratic \(d(K-d-1)\) coincide with the proposer.  These coincidences were
    found on comparison; they are natural consequences of the frozen witness
    and exact defect decomposition, not evidence imported into Phase A.

No discrepancy changes the Phase-A constant or introduces a dependency on the
out-of-scope stronger chain.

---

# Numerical and exact checks (7f)

The scratch program was written outside the repository at
`<machine-local-path-redacted>` and run with
`<machine-local-path-redacted>`.  Its SHA-256 was
`EFDD27DA7B93BD51A9981946369292914791E1667D305B9132EB38D4AA8844FB`.

## Proved-formula evaluations

These checks exercise formulas already proved in Phase A.  Agreement checks
their arithmetic and implementation, not the derivation.

1. **Normalization, exact fractions.**  For \(1\le n\le9\), the program
   verified
   \[
   \left(q^{-3n/2}/\sqrt{n!}\right)^2
   \frac{q^{3n}}{(q)_n(q)_{2n}}=\frac1{(q!)^2}.
   \]

2. **Hook/scalar identities, exact fractions.**  For
   \(n=3,4,8,27,64\), every \(\theta\vdash d\), \(0\le d\le K\), was
   enumerated.  The hook product (A.20), matched scalar from (A.17), and
   one-defect identity \(r_{d+1}=d\,r_d\) agreed exactly.  Sample maxima were
   \[
   \rho_{8,2}=16/13,\quad
   \rho_{27,3}=2916/2597,\quad
   \rho_{64,4}=1048576/968121.
   \]

3. **Taper maximum, exact integers.**  For \(1\le K\le20\), exhaustive
   maximization gave
   \[
   \max_d d(K-d-1)=\left\lfloor (K-1)^2/4\right\rfloor.
   \]

4. **Special-path arithmetic, exact fractions.**  For every even
   \(2\le|P|\le20\), the code evaluated (A.24)-(A.25).  The squared combined
   bounds were \(2,3,2,5/4,3/4,\ldots\); the maximum was exactly \(3\) at
   \(|P|=4\).

## Independent-construction checks

These checks build legal inputs and masks directly, rather than evaluate a
representation-theoretic formula.  Their agreement corroborates the finite
values but does not prove the general printed derivation.

For \(n=1,2,3\), the frozen floor gives \(K=1\), so the full witness is exactly
the normalized \(k=0\) atom.  The program independently enumerated every
legal YES word, every legal NO permutation, and every query mask.  It verified
\(|Y_n|=|N_n|=(2n)!\), constant row and column degree
\((2n)!(2n-1)/(2n)\), and hence the exact values

| \(n\) | \(|Y_n|=|N_n|\) | \(\|\Gamma_n\|\) | \(\max_i\|\Gamma_n\circ\Delta_i\|\) | ratio |
|---:|---:|---:|---:|---:|
| 1 | 2 | 1 | \(1/2\) | 2 |
| 2 | 24 | 1 | \(3/4\) | \(4/3\) |
| 3 | 720 | 1 | \(5/6\) | \(6/5\) |

The mask norm follows independently because the constructed nonnegative
bipartite matrix is regular: the constant vectors attain the degree, and
\(\|A\|\le\sqrt{\|A\|_1\|A\|_\infty}\) gives the matching upper bound.

No numerical result is load-bearing.

---

# VERDICT

**CERTIFY**

The certified statement is the following, with all quantifiers explicit.

For every integer \(n\ge1\), let \(q=2n\) exactly, let \(Y_n\) be the legal
Set-Equality YES inputs consisting of two injective \(n\)-lists with equal
images, and let \(N_n\) be the legal NO inputs consisting of two injective
\(n\)-lists with disjoint images.  Put
\(K=\lfloor n^{1/3}\rfloor\), define
\(\alpha_k=(K-k)_+\), define \(W_k^{\rm leg}\) by (A.3), and let
\(P_k^{\rm leg}\) be the legal \(S_n\times S_n\) central position projector of
total first-row defect \(k\).  Then the real \(Y_n\times N_n\) matrix

\[
\Gamma_n=\frac1{(2n)!}\sum_{0\le k<K}(K-k)
W_k^{\rm leg}P_k^{\rm leg}
\]

is defined for every \(n\ge1\).  The analytic channel proof applies for every
integer \(n\ge8\), every \(0\le k<K\), every relevant
\(\theta\vdash d\), every query position \(i\in[2n]\), and every LR
multiplicity copy \(c\ge1\), and gives

\[
\|\Gamma_n\|\ge K,\qquad
\max_{i\in[2n]}\|\Gamma_n\circ\Delta_i\|
\le\left(\frac{\sqrt6}{2}+\varepsilon_n\right)n^{1/6},
\]

for a nonnegative sequence \(\varepsilon_n\to0\) as \(n\to\infty\).
The convergence is uniform over \(i\), the full taper window
\(0\le k<K\), all relevant partitions, and all multiplicity copies.  Here
“legal” means exactly the two promised injective sets just defined; no term
“admissible” is used.

Consequently, there is a sequence \(\delta_n\to0\) such that

\[
\operatorname{Adv}^{\pm}(\operatorname{SE}(n,q=2n))
\ge
\left(\frac2{\sqrt6}-\delta_n\right)n^{1/6}.
\]

Equivalently, for every real \(\epsilon>0\) there is an integer
\(N(\epsilon)\ge8\) such that for every integer \(n\ge N(\epsilon)\),

\[
\operatorname{Adv}^{\pm}(\operatorname{SE}(n,2n))
\ge
\left(\frac2{\sqrt6}-\epsilon\right)n^{1/6}.
\]

No effective numerical value of \(N(\epsilon)\) is asserted.

---

## Amendment (2026-07-29) — post-external-review repair of A.2

**This section is an append-only amendment.  Nothing above this line was
altered; the certified statement in the VERDICT section is unchanged.**

### 0. Provenance and integrity

- **SHA-256 of this file BEFORE the amendment** (as recorded in
  `se/artifacts/se_cor16_certification_20260723.sha256`, recomputed identical
  immediately before appending):

      a045781c3e8280ec1a8ac879ea12089b47cf9e8134cc70b3698ad0ffffb76293  se/artifacts/se_cor16_certification_20260723.md

  The paired `.sha256` file is regenerated for the amended file; the hash above
  preserves the provenance of the pre-amendment bytes.
- **Trigger.**  The completed EXTERNAL cross-stack review
  `se/artifacts/se_external_review_20260729.md` (SHA-256
  `7aca72b1129fc97745e8062d1b288ea086b8f55af5caac6452c8ad09379d828f`), finding
  **T1-G1**, verdict for T1: CONFIRM-WITH-ISSUES.
- **Adjudication.**  `se/notes/SE_PROOF_DAG.md`, entry **(90)**
  (2026-07-29): all 17 review findings machine-verified before adjudication,
  none refuted; `SE.br.cor16` keeps its status because the certified STATEMENT
  is intact, with this textual repair recorded as an OPEN obligation now
  discharged by this amendment.  Repair campaign approved by the lead.
- **Authorship.**  Written by the repair executor (Claude Opus 4.8 subagent) as
  commissioned; see §5 for the review discipline that applies to it.

### 1. Identity (A.2) is REFUTED AS STATED

The display

    J_N P_k^amb = P_k^leg J_N                                     (A.2)

at lines ~115–127 above is **false as stated**, for the reason that
\(P_k^{\rm amb}=\bar\Pi_{{\rm se},k}\) is *not* an element of the position
group algebra: besides the position-type condition it contains the **exact
tensor-weight projector**, and legality (injectivity of the word) is invariant
under the position group but not under the weight grading.  Invariance of the
legal set under \(S_n\times S_n\) licenses intertwining with projectors *in
the position group algebra only*.

**The reviewer's minimal counterexample** (`se_external_review_20260729.md`,
§T1-G1, verbatim):

> **最小反例：**取 `n=1,q=2,k=0`，令 `f=δ_(1,1)`，其中 `(1,1)` 是非法 NO word。
> 合法 restriction 满足 `J_N f=0`；但 exact-weight-0 projector 将 `f` 投到非零常向量，随后 restriction 非零。
> 因此不存在认证报告所写的 `J_NP_0^{amb}=P_0^{leg}J_N`。

(Rendered: take \(n=1,q=2,k=0\) and \(f=\delta_{(1,1)}\), an illegal NO word.
The legal restriction gives \(J_Nf=0\); but the exact-weight-0 projector sends
\(f\) to a nonzero constant vector, whose restriction is nonzero.  Hence no
operator \(P_0^{\rm leg}\) can satisfy the displayed identity.)

**Coordinator's exact confirmation (entry (90)):** "A.2 counterexample
CONFIRMED EXACTLY (legal values 1/4 vs 0)".

**Executor re-verification (exact rational arithmetic, independent of the
coordinator's run).**  With \(n=1,q=2\): the legal NO words are \((1,2)\) and
\((2,1)\); \(J_Nf=(0,0)\) exactly, while
\(P_0^{\rm amb}=\Pi_0\otimes\Pi_0\) gives
\(J_NP_0^{\rm amb}f=(1/4,\,1/4)\) exactly.  A second instance at \(n=2,q=4\):
for \(f=\delta_{(1,1,1,1)}\) one has \(J_Nf=0\) while
\(J_NP_0^{\rm amb}f\) is the constant \(1/256\) on all \(24\) legal words.
Both are exact `Fraction` values, not floating point.

Consequently (A.2) also fails to *define* \(P_k^{\rm leg}\): the sentence
"the legal set is position invariant, so there is a legal projector
\(P_k^{\rm leg}\) satisfying (A.2)" asserts the existence of a solution of an
equation that has none.  The VERDICT section does not depend on that sentence:
it defines \(P_k^{\rm leg}\) **explicitly** as "the legal \(S_n\times S_n\)
central position projector of total first-row defect \(k\)" (lines ~838–850),
which is exactly the operator produced by the replacement lemma below.

### 2. Replacement: the PRODUCT-LEVEL restriction lemma

All objects below are the frozen A.1 objects above; nothing new is introduced
except names for two projectors that were already implicit.

**Notation.**  On \(\mathcal A_N=H^{\otimes n}\otimes H^{\otimes n}\):

- \(P_{{\rm wt},k}\) = the orthogonal projector onto **exact total weight**
  \(k\) (the weight half of \(P_k^{\rm amb}\));
- for \(0\le u\le m\), \(D_u^{(m)}\in Z(\mathbb C[S_m])\) = the central
  projector of the position action on \(H^{\otimes m}\) onto the position
  irreducibles \(\rho\vdash m\) of defect exactly \(u\) (defect
  \(=m-\rho_1\));
- \(Q_k^{\rm pos}=\sum_{u+v=k}D_u^{(n)}\otimes D_v^{(n)}\) = the **pure
  position central projector** of total first-row defect \(k\).  It carries no
  weight condition and lies in \(Z(\mathbb C[S_n\times S_n])\).

With \(P_{m,d}\) the exact-weight-\(d\) projector on \(H^{\otimes m}\), the
frozen BR projector is \(\bar\Pi_d^{(m)}=P_{m,d}D_d^{(m)}\) (weight projectors
commute with position permutations, so the product is an orthogonal
projector), and \(P_k^{\rm amb}=\bar\Pi_{{\rm se},k}
=\sum_{\ell=0}^k\bar\Pi_{k-\ell}^{(n)}\otimes\bar\Pi_\ell^{(n)}\).

> **Lemma A.2′ (product-level legal restriction).**  For every \(k\ge0\):
>
> 1. **(weight absorption)** \(W_{{\rm se},k}=W_{{\rm se},k}P_{{\rm wt},k}\);
> 2. **(Schur–Weyl support)** \(P_{{\rm wt},k}Q_k^{\rm pos}
>    =Q_k^{\rm pos}P_{{\rm wt},k}=P_k^{\rm amb}\), hence
>    \(W_{{\rm se},k}P_k^{\rm amb}=W_{{\rm se},k}Q_k^{\rm pos}\);
> 3. **(legal intertwining, position algebra only)**
>    \(J_NQ_k^{\rm pos}=Q_k^{\rm leg}J_N\), where \(Q_k^{\rm leg}\) is the
>    image of the same central idempotent under the position action on
>    \(\mathcal L_N\) — i.e. exactly the \(P_k^{\rm leg}\) of the VERDICT;
>
> consequently
>
> \[
> \mathcal R(W_{{\rm se},k}P_k^{\rm amb})
> =\mathcal R(W_{{\rm se},k})\,Q_k^{\rm leg}
> =\frac1{q!}W_k^{\rm leg}Q_k^{\rm leg},
> \tag{A.2′}
> \]
>
> which is the operator identity (A.5) with \(P_k^{\rm leg}=Q_k^{\rm leg}\).

**Proof.**

*(1) Weight absorption.*  Since \(e_0^*=e_0^*\Pi_0\) and \(\Pi_i\Pi_i=\Pi_i\),

\[
\Psi_0=\Pi_0\otimes e_0^*=\Psi_0(\Pi_0\otimes\Pi_0),\qquad
\Psi_1=\Pi_1\otimes e_0^*+e_0^*\otimes\Pi_1
=\Psi_1\bigl(\Pi_1\otimes\Pi_0+\Pi_0\otimes\Pi_1\bigr).
\]

So \(\Psi_0\) accepts only pair weight \(0\) and \(\Psi_1\) only pair weight
exactly \(1\).  For \(c\in\{0,1\}^n\) with \(|c|=k\), the tensor
\(\Psi_{c_1}\otimes\cdots\otimes\Psi_{c_n}\) therefore annihilates every
component of total weight \(\ne k\), for each matching \(\mu\) (the matching
only relabels which two of the \(2n\) slots each \(\Psi\) consumes; the total
weight condition is matching-independent).  Summing over \(c\) with \(|c|=k\)
and stacking the \(n!\) matching blocks gives
\(W_{{\rm se},k}=W_{{\rm se},k}P_{{\rm wt},k}\).

*(2) Schur–Weyl support: half-position defect \(\le\) half weight.*  On
\(H^{\otimes m}\) the exact-weight-\(w\) subspace is
\(\bigoplus_{|S|=w}\bigl(\bigotimes_{i\in S}H_1\bigr)\otimes
\bigl(\bigotimes_{i\notin S}H_0\bigr)\); \(S_m\) permutes the summands
transitively with stabilizer \(S_w\times S_{m-w}\), so as an \(S_m\)-module it
is \(\operatorname{Ind}_{S_w\times S_{m-w}}^{S_m}(H_1^{\otimes w}\boxtimes\1)\).
Every constituent of an induction whose second factor is the trivial
representation of \(S_{m-w}\) is obtained by adding a horizontal strip of size
\(m-w\), so every constituent \(\rho\) has \(\rho_1\ge m-w\), i.e.

\[
\operatorname{def}(\rho)=m-\rho_1\le w .
\]

Hence \(P_{m,w}D_u^{(m)}=0\) whenever \(u>w\).  Now decompose
\(P_{{\rm wt},k}=\sum_{w_A+w_B=k}P_{n,w_A}\otimes P_{n,w_B}\) and expand
\(Q_k^{\rm pos}=\sum_{u+v=k}D_u^{(n)}\otimes D_v^{(n)}\).  In the product, a
term survives only if \(u\le w_A\) and \(v\le w_B\); with \(u+v=k=w_A+w_B\)
this forces \(u=w_A\) and \(v=w_B\).  Therefore

\[
P_{{\rm wt},k}Q_k^{\rm pos}
=\sum_{w_A+w_B=k}
\bigl(P_{n,w_A}D_{w_A}^{(n)}\bigr)\otimes
\bigl(P_{n,w_B}D_{w_B}^{(n)}\bigr)
=\sum_{\ell=0}^k\bar\Pi_{k-\ell}^{(n)}\otimes\bar\Pi_\ell^{(n)}
=P_k^{\rm amb},
\]

and the two factors commute, so the same holds in the other order.  Combining
with (1) and \(P_k^{\rm amb}\le P_{{\rm wt},k}\),

\[
W_{{\rm se},k}P_k^{\rm amb}
=W_{{\rm se},k}P_{{\rm wt},k}Q_k^{\rm pos}
=W_{{\rm se},k}Q_k^{\rm pos}.
\]

*(3) Legal intertwining.*  \(N_n\subset[q]^{2n}\) is invariant under the
position action of \(S_n\times S_n\) (permuting coordinates inside either half
sends injective words to injective words).  Pointwise restriction therefore
intertwines the two position actions, \(J_N\rho_{\rm amb}(g)=\rho_{\rm
leg}(g)J_N\) for every \(g\in S_n\times S_n\); extending linearly to
\(\mathbb C[S_n\times S_n]\) and evaluating at the central idempotent that
defines \(Q_k^{\rm pos}\) gives \(J_NQ_k^{\rm pos}=Q_k^{\rm leg}J_N\), with
\(Q_k^{\rm leg}\) the legal \(S_n\times S_n\) central position projector of
total first-row defect \(k\).  **This is the step (A.2) tried to take with the
wrong operator:** the weight factor inside \(P_k^{\rm amb}\) is not in the
position group algebra, and the counterexample of §1 is exactly its failure.

*Conclusion.*  Taking adjoints in (3) gives
\(Q_k^{\rm pos}J_N^*=J_N^*Q_k^{\rm leg}\).  Hence, with
\(\mathcal R(T)=J_YTJ_N^*\),

\[
\mathcal R(W_{{\rm se},k}P_k^{\rm amb})
\overset{(2)}{=}J_YW_{{\rm se},k}Q_k^{\rm pos}J_N^*
\overset{(3)}{=}J_YW_{{\rm se},k}J_N^*\,Q_k^{\rm leg}
=\mathcal R(W_{{\rm se},k})\,Q_k^{\rm leg}
=\frac1{q!}W_k^{\rm leg}Q_k^{\rm leg},
\]

the last equality being (A.3)–(A.4) above, which compute the raw legal kernel
and the single common coefficient \(1/q!\) **with no projector inserted** and
are therefore untouched by this repair. \(\square\)

**Types (rule 7a).**  \(P_{{\rm wt},k},Q_k^{\rm pos}:\mathcal A_N\to\mathcal
A_N\) are \(q^{2n}\)-by-\(q^{2n}\); \(Q_k^{\rm leg}:\mathcal L_N\to\mathcal
L_N\) is \(q!\)-by-\(q!\) at \(q=2n\); \(W_{{\rm se},k}:\mathcal A_N\to\mathcal
A_Y\) is \(n!q^n\)-by-\(q^{2n}\); \(W_k^{\rm leg}:\mathcal L_N\to\mathcal
L_Y\) is \(q!\)-by-\(q!\).  All three displayed identities are equalities of
maps with equal domain and codomain, for every \(n\ge1\), every \(k\ge0\), and
every LR multiplicity \(c\ge1\) (no multiplicity space, transport, or
multiplicity trace occurs anywhere in this lemma).

**Numerator (A.7) is unaffected.**  \(\mathbf1_N\) spans the trivial
\(S_n\times S_n\) representation, which has defect \(0\); hence
\(Q_k^{\rm leg}\mathbf1_N=0\) for \(k>0\) and
\(Q_0^{\rm leg}\mathbf1_N=\mathbf1_N\).  With \(W_0^{\rm leg}=J\) (all-ones,
from (A.3)) this gives \(\Gamma_n\mathbf1_N=K\mathbf1_Y\) and
\(\|\Gamma_n\|\ge K\) exactly, as in (A.7).  The argument used only the pure
position projector, which is what the VERDICT already names.

### 3. Machine verification of the replacement (exact)

Coordinator's run, recorded in DAG entry (90): "the product-level repair
identities CONFIRMED (weight absorption at n=1,2; pure-position intertwining
EXACT 0.0; `Q_1^leg·1=0` EXACT 0.0 — the numerator argument survives)".

Executor's independent re-verification, exact integer/rational arithmetic
(integer matrices with tracked denominators; `fractions.Fraction` for all
reported values; no floating point anywhere), at \(n=2,q=4\) — where the
position group \(S_2\times S_2\) is nontrivial, both matchings exist, and
\(k=0,1,2\) all occur — and at \(n=1,q=2\):

| Check | Statement | Result |
|---|---|---|
| C1 | \(P_{{\rm wt},k}Q_k^{\rm pos}=Q_k^{\rm pos}P_{{\rm wt},k}=P_k^{\rm amb}\) | EXACT equality, \(k=0,1,2\) |
| C2 | \(W_{{\rm se},k}^{(\mu)}P_{{\rm wt},k}=W_{{\rm se},k}^{(\mu)}\) | EXACT, \(k=0,1,2\), both matchings \(\mu\) |
| C3 | \(W_{{\rm se},k}^{(\mu)}P_k^{\rm amb}=W_{{\rm se},k}^{(\mu)}Q_k^{\rm pos}\) | EXACT, \(k=0,1,2\), both \(\mu\) |
| C4 | \(J_NQ_k^{\rm pos}=Q_k^{\rm leg}J_N\) | EXACT (residual identically \(0\)), \(k=0,1,2\) |
| C5 | \(Q_k^{\rm leg}\mathbf1_N=0\) for \(k>0\); \(=\mathbf1_N\) for \(k=0\) | EXACT |
| C6 | (A.2) fails | \(J_Nf=0\) vs \(J_NP_0^{\rm amb}f=1/4\) at \(n=1\); \(=1/256\) at \(n=2\) |

Value-vs-formula statement (rule 7f): C1–C5 are **identity-level matrix
residual** checks on operators built from the frozen definitions
(\(\Psi_0,\Psi_1,W_k^\mu\), weight projectors, symmetric-group central
idempotents) — they exercise the printed identities themselves, not an
independent construction of the same numbers.  C6 exhibits a counterexample
value.  The checks are finite (\(n\le2\)); the *proof* in §2 is the uniform
argument, and the checks guard against a mis-stated projector or a dropped
normalization, not against a wrong induction.  The verification code was run
from the session scratchpad (the work order for this amendment permits no new
repository files); it is reproduced verbatim in
`se/artifacts/se_paperrev5_changelog_20260729.md`, Appendix V.

### 4. What this amendment supersedes, and what it does NOT touch

**SUPERSEDED BY THIS AMENDMENT** (the text remains in place above,
append-only, and must be read together with this section):

1. the display **(A.2)** at lines ~115–127, and the sentence asserting the
   existence of a legal projector satisfying it;
2. the **A.2-based derivation of (A.5)** at lines ~157–162 (the *statement*
   (A.5) survives verbatim, with \(P_k^{\rm leg}=Q_k^{\rm leg}\); only its
   justification is replaced by Lemma A.2′);
3. the **two type-table rows asserting standalone projector intertwining**:
   the 7a row "Projector intertwining (A.2)" (line ~619, whose
   well-definedness column claims that position invariance alone gives the
   intertwining) and the 7e failure-mode row "Type/dimension mismatch"
   (line ~669, in so far as it resolves the ambiguous shorthand
   \(W_k^{\rm leg}P_k\) *by recording (A.2)*).  Their corrected content:
   *the standalone ambient projector does not intertwine; after left
   multiplication by \(W_{{\rm se},k}\) the weight factor is absorbed and the
   surviving pure position projector does.*
4. §B.1 item 3 (lines ~707–711), in so far as it judges (A.2) to be "a
   notation repair, not a new analytic premise": the notation repair is real
   and still needed, but the vehicle must be Lemma A.2′, not (A.2).
5. any reading of this report as "verbatim zero-defect".  The external review's
   verdict for T1 is **CONFIRM-WITH-ISSUES**; entry (82)'s "no caveats"
   wording was already superseded in entry (90).

**EXPLICITLY UNAFFECTED:**

- the **VERDICT** statement in full, including the explicit definition of
  \(P_k^{\rm leg}\), the quantifiers (\(q=2n\) exact, \(n\ge8\) for the
  analytic proof, exact gates at \(n=1,2,3\), uniformity over \(i\), the taper
  window, all \(\theta\), all \(c\ge1\)), and the bound
  \(\operatorname{Adv}^\pm(\operatorname{SE}(n,2n))\ge(2/\sqrt6-\delta_n)n^{1/6}\);
- the witness \(\Gamma_n\) (A.6), the numerator (A.7), and **every constant**:
  \(1/q!\), \(K=\lfloor n^{1/3}\rfloor\), \(\alpha_k=(K-k)_+\), the mask factor
  \(2\), the special-path factors \(2,3,2,5/4\) with maximum \(3\),
  \(\sqrt3\), \(\|T_k\|\le\sqrt6/\sqrt{n-2k+1}\), \(\sqrt6/4\), \(\sqrt6/2\),
  \(2/\sqrt6\);
- (A.1), (A.3), (A.4), and everything from A.3 (legal diamond representative)
  onward: the diamond decomposition, the defect pinning, the LR-sector support
  argument, the completion/forgetting vector inequality, the hook envelope, the
  BR:1307 repair, the assembly, and the \(7b\)/\(7e\) findings other than the
  two rows listed above;
- the external review's own conclusion that this repair "不改变 Γ、分子、任何通道或常数"
  (does not change \(\Gamma\), the numerator, any channel, or any constant).

### 5. Status discipline (DAG_PROTOCOL rules 2, 6, 7)

- The **refutation** of (A.2) as stated is not the executor's own kill: it is
  the finding of the completed, archived, independent EXTERNAL cross-stack
  review, machine-confirmed by the coordinator before adjudication (entry (90))
  and re-verified exactly here.
- **Lemma A.2′ and its proof in §2 are executor-authored and therefore sit at
  proposer level.**  They carry exact identity-level verification at
  \(n\le2\), but no independent review of *this amendment text* exists yet.
  Per rule 6 this amendment does not by itself license any status promotion,
  and per rule 2 the executor writes none.  Entry (90) already adjudicated
  that `SE.br.cor16` keeps its existing status because the certified STATEMENT
  is intact and the VERDICT already uses the pure position projector; this
  amendment discharges the *textual* repair obligation recorded there and
  leaves an OPEN obligation: **an independent rule-7 review of Lemma A.2′**
  (type audit, \(c\ge2\) regime statement, anchoring ban, value-vs-formula) if
  any future promotion is to cite this amendment.
- No external claim of any kind is licensed by this amendment.

### 6. Cites

- `se/artifacts/se_external_review_20260729.md` §T1-G1 (refutation + the
  product-level repair prescription), §T1.1 (the confirmed main chain),
  final verdict paragraph.
- `se/notes/SE_PROOF_DAG.md` entry **(90)** (verification-before-
  adjudication record, adjudication (i), the superseded-wording notes).
- `se/proof-dag/nodes/SE.br.cor16.yaml` (the node this report
  certifies), `se/proof-dag/nodes/SE.goal.yaml` (external-review entry).
- Companion paper repair: `se/paper/se_explicit_witness.tex` REV5
  (Lemma "Product-level legal restriction"), changelog
  `se/artifacts/se_paperrev5_changelog_20260729.md`.

---

## Amendment 2 (2026-08-01) — repair of the A.4 weight-to-defect step (A.2-prime review ISSUE-1)

**This section is an append-only amendment.  Nothing above this line was
altered — neither Phase A, nor the VERDICT, nor the Amendment of 2026-07-29.
The certified statement is unchanged.**

### 0. Provenance and integrity

- **SHA-256 of this file BEFORE Amendment 2** (recomputed immediately before
  appending; identical to the value recorded in
  `se/artifacts/se_cor16_certification_20260723.sha256` after Amendment 1):

      4911ad56e1cd38398526af652e5cd9098b0eb2ea060d55ce6655263fc216fb81  se/artifacts/se_cor16_certification_20260723.md

  The pre-Amendment-1 bytes hashed
  `a045781c3e8280ec1a8ac879ea12089b47cf9e8134cc70b3698ad0ffffb76293`
  (Amendment 1 §0).  The paired `.sha256` file is regenerated for the
  twice-amended file; both earlier hashes preserve the provenance chain.
- **Trigger.**  The completed **dedicated rule-7 review of Lemma A.2′**,
  `se/artifacts/se_a2prime_review_20260801.md` (SHA-256
  `c6acb691f6f96d0d67421368628823c051d882e7f7005bc35c4d73f815b7ea4b`), by a
  fresh independent Opus 5 reviewer that did not author any SE artifact and was
  given no desired outcome.  Verdict: **CONFIRM-WITH-ISSUES** — Lemma A.2′ is
  true and correctly proved; the issues are in the amendment's *surrounding
  claims*.  This section discharges its **ISSUE-1** (§B.3 of that review).
- **Record.**  `se/proof-dag/nodes/SE.br.cor16.yaml`, work record entry
  2026-08-01 (outcome), where ISSUE-1 is registered as the obligation repaired
  here.
- **Authorship.**  Written by the repair executor as commissioned.  The status
  discipline of Amendment 1 §5 applies verbatim: this text is proposer-level,
  it writes no status, and per rule 2 / rule 6 it licenses no promotion.

### 1. The defective passage, and why it became unjustified

§A.4 above, lines ~292–296, reads verbatim:

> The primed \(X/Y\) carrier has exact weight \(k\) and all its full-position
> types have defect at least \(k\).  Legal NO restriction pairs equal alphabet
> and position shapes by (A.11), while **exact weight \(k\) permits alphabet
> defect at most \(k\)**.  Alphabet equivariance transports the same central
> label to the YES side.

The emphasised clause takes an **ambient** hypothesis — exact tensor weight
\(k\) on \(\mathcal A_N=H^{\otimes 2n}\) — and draws a **legal-side**
conclusion: a bound on the alphabet-defect support of \(X_k,Y_k\) on
\(\mathcal L_N=L^2(S_q)\).  No transport across \(J_N\) is named.  Under the
pre-Amendment-1 text the transport in force was precisely the one **(A.2)**
supplied: \(J_NP_k^{\rm amb}=P_k^{\rm leg}J_N\) moved the entire ambient
projector — *weight factor included* — across the legal restriction.
Amendment 1 refuted (A.2) for exactly that reason: a weight projector is a
value-space operator, is not an element of a group algebra preserving \(N_n\),
and does not intertwine (minimal counterexample \(n=1,q=2,k=0\): legal values
\(1/4\) versus \(0\)).

Once (A.2) is deleted, the sentence above **repeats the same ambient-weight to
legal-side move with no remaining licence in the document**.  The defect is in
the *justification*, not in the conclusion: the conclusion (A.13) is true, and
§2 below proves it.  Correspondingly, Amendment 1 §4's bullet listing
"(A.1), (A.3), (A.4), and everything from A.3 onward" as **EXPLICITLY
UNAFFECTED** was, in respect of A.4, too strong.

### 2. The repair

Notation of Amendment 1 §2 is kept and extended from the half-position group
\(S_n\times S_n\) to the **full** position group \(S_{2n}\): for
\(0\le j\le 2n\) let \(D_j^{\rm fp}\in Z(\mathbb C[S_{2n}])\) be the central
projector of the position action on \(\mathcal A_N=H^{\otimes 2n}\) onto
position irreducibles \(\rho\vdash 2n\) of defect \(2n-\rho_1=j\) exactly; put
\(D_{\le k}^{\rm fp}=\sum_{j\le k}D_j^{\rm fp}\); and let
\(D_j^{{\rm fp},{\rm leg}}\) be the image of the same central idempotent under
the position action on \(\mathcal L_N\).  \(P_{2n,k}\) is the exact-weight-\(k\)
projector on \(H^{\otimes 2n}\); \(E_d^N,E_d^Y\) are the legal central alphabet
projectors of A.4.

> **Lemma A.4′ (weight to legal alphabet defect, via the full position group).**
> Let \(\bar T:\mathcal A_N\to\mathcal A_Y\) be any ambient carrier of exact
> input weight \(k\), i.e. \(\bar T=\bar TP_{2n,k}\).  Then
>
> \[
> \mathcal R(\bar T)=\mathcal R(\bar T)\,E_{\le k}^N .
> \tag{A.13′}
> \]
>
> In particular \(X_k=X_kE_{\le k}^N\) and \(Y_k=Y_kE_{\le k}^N\); together
> with the full-position-defect \(\ge k\) statement already proved in §A.4
> (LR first-row inequality, unchanged), the only surviving legal alphabet
> defect is exactly \(k\), which is (A.13).

**Proof, in three steps.**

*(R1) Exact weight forces full-position defect \(\le k\).*  Apply the
Young/Pieri argument of Amendment 1 §2(2) at \(m=2n\) instead of \(m=n\): the
exact-weight-\(w\) subspace of \(H^{\otimes m}\) is
\(\operatorname{Ind}_{S_w\times S_{m-w}}^{S_m}(H_1^{\otimes w}\boxtimes\1)\),
whose constituents are obtained by adding a horizontal strip of size \(m-w\),
so every constituent \(\rho\) has \(\rho_1\ge m-w\), i.e.
\(\operatorname{def}(\rho)=m-\rho_1\le w\).  Hence
\(P_{2n,k}D_j^{\rm fp}=0\) for every \(j>k\), and therefore
\(\bar T=\bar TP_{2n,k}=\bar TP_{2n,k}D_{\le k}^{\rm fp}\).
Nothing in that argument used the half structure, so it runs verbatim at the
full group.

*(R2) The full position group intertwines the legal restriction.*  \(N_n\) is
the set of bijections from the \(2n\) positions to \([q]\); permuting **all**
\(2n\) coordinates preserves injectivity, so \(N_n\) is \(S_{2n}\)-invariant —
a fortiori, not merely \(S_n\times S_n\)-invariant.  Pointwise restriction
therefore intertwines the two position actions,
\(J_N\rho_{\rm amb}(g)=\rho_{\rm leg}(g)J_N\) for every \(g\in S_{2n}\);
extending linearly to \(\mathbb C[S_{2n}]\) and evaluating at the central
idempotent gives \(J_ND_j^{\rm fp}=D_j^{{\rm fp},{\rm leg}}J_N\).  Both central
projectors are **self-adjoint** — their group-algebra coefficients are real
class functions with \(c_{g^{-1}}=c_g\), and both actions are by permutation
unitaries — so taking adjoints gives
\(D_j^{\rm fp}J_N^*=J_N^*D_j^{{\rm fp},{\rm leg}}\).  Hence

\[
\mathcal R(\bar T)=J_Y\bar TD_{\le k}^{\rm fp}J_N^*
=\mathcal R(\bar T)\,D_{\le k}^{{\rm fp},{\rm leg}} .
\]

This is Amendment 1 §2(3) with \(S_n\times S_n\) replaced by \(S_{2n}\); it is
a **position-algebra step only**, and no weight projector crosses \(J_N\).
(The self-adjointness clause also supplies the review's MINOR-1, which was
left implicit in Amendment 1's conclusion paragraph.)

*(R3) On the legal side the position label IS the alphabet label.*  By (A.11),
\(\mathcal L_N=L^2(S_q)\cong\bigoplus_{\lambda\vdash q}
S^\lambda_{\rm alph}\otimes S^\lambda_{\rm pos}\): the alphabet-\(\lambda\)
isotypic and the full-position-\(\lambda\) isotypic are literally the *same*
subspace of \(\mathcal L_N\).  Consequently
\(D_d^{{\rm fp},{\rm leg}}=E_d^N\) as operators for every \(d\), so
\(D_{\le k}^{{\rm fp},{\rm leg}}=E_{\le k}^N\), and (R2) becomes (A.13′).
Alphabet equivariance of the carrier and of \(J_Y\) — unchanged from A.4 —
transports the same central label to the YES side, giving the two-sided
form. \(\square\)

The three steps are exactly the three-line repair supplied by the review
(§B.3, ISSUE-1).  The ambient-weight to legal-alphabet jump is replaced by the
chain

    ambient weight  ->  ambient full-position defect   (Schur-Weyl support, R1)
                    ->  legal full-position defect     (position-algebra intertwining, R2)
                    ->  legal alphabet defect          (Peter-Weyl pairing (A.11), R3),

in which every arrow is licensed either by an operator lying in a group algebra
that preserves \(N_n\), or by an identification internal to \(\mathcal L_N\).
No new premise, constant, or object is introduced.

**Machine verification** — the reviewer's own exact gates
(`se/artifacts/logs_se_a2prime_20260801/`: scripts, logs, `SHA256SUMS.txt`;
exact integer/`Fraction` arithmetic, no floating point):

| Gate | Statement | Result |
|---|---|---|
| G2 | \(P_{2n,k}D_j^{\rm fp}=0\) for \(j>k\) — step (R1) | EXACT, \(n=1,2\) |
| G3 | \(J_ND_j^{\rm fp}=D_j^{{\rm fp},{\rm leg}}J_N\) — step (R2) | EXACT, \(n=1,2\) |
| G4 | alphabet-defect-\(d\) projector \(=\) full-position-defect-\(d\) projector on \(\mathcal L_N\) — step (R3), the (A.11) pairing | EXACT; ranks at \(n=2\): \(1,9,13,1,0\), total \(24=q!\) |
| G5 | \(\mathcal R(W_{{\rm se},k}P_k^{\rm amb})E_d^N=0\) for every \(d>k\) — the A.4 support claim end to end | EXACT, \(n=1,2\), all \(k\le n\) |

**Value-vs-formula (rule 7f).**  G2–G5 are identity-level matrix-residual
checks on operators rebuilt from the frozen A.1 definitions in the reviewer's
own code (no code shared with this project).  They exercise the printed
identities at \(n\le2\); they do **not** replace the uniform proof above, which
is what carries all \(n\).  G4 is additionally an independent-construction
agreement: two different groups' central projectors, computed separately and
found equal.

### 3. What Amendment 2 supersedes, and what it does NOT touch

**SUPERSEDED** (the text remains in place above, append-only):

1. exactly one sentence — the justification clause at lines ~292–296,
   "Legal NO restriction pairs equal alphabet and position shapes by (A.11),
   while exact weight \(k\) permits alphabet defect at most \(k\)" — in so far
   as it is read as licensing the ambient-weight to legal-alphabet inference on
   its own.  Its corrected content is **Lemma A.4′ of §2 above**;
2. Amendment 1 §4's bullet listing "(A.1), (A.3), (A.4), and everything from
   A.3 onward" as EXPLICITLY UNAFFECTED, in the narrow respect that **A.4's
   printed justification** was affected.  A.4's *statement* was not.

**EXPLICITLY UNAFFECTED:**

- **the STATEMENT of A.4 survives verbatim**: (A.11), (A.12), the display
  (A.13) \(X_k=E_k^YX_kE_k^N,\ Y_k=E_k^YY_kE_k^N\), the \(T_k\) branching
  discussion, (A.14), (A.15), and the \(c\ge2\) remark.  Only the *reason*
  given for the alphabet-defect upper bound changes;
- **Lemma A.2′ and all of Amendment 1 §2**: the dedicated review confirms the
  lemma is true and its proof correct, having re-derived all five parts under
  the anchoring ban before reading the amendment, and it strengthens the (A.2)
  refutation (A.2 fails at *every* \(k\) with \(P_k^{\rm amb}\ne0\), not only
  at \(k=0\));
- **the VERDICT in full** — the certified statement, its quantifiers, the
  witness \(\Gamma_n\) (A.6), the numerator \(\|\Gamma_n\|\ge K\) (A.7), and
  every constant (\(1/q!\), \(K=\lfloor n^{1/3}\rfloor\), \(\sqrt3\),
  \(\sqrt6/4\), \(\sqrt6/2\), \(2/\sqrt6\)).  **The VERDICT is unaffected:**
  \(\operatorname{Adv}^{\pm}(\operatorname{SE}(n,2n))\ge(2/\sqrt6-\epsilon)
  n^{1/6}\) for all \(n\ge N(\epsilon)\) stands.  This amendment changes no
  object, no constant and no inequality; it supplies a missing justification
  for a step whose conclusion was, and remains, true;
- the frozen (A.3)–(A.4) kernel and the constant \(1/q!\): the review's
  ISSUE-2 gated that constant for the first time and found
  \(\mathcal R(W_{{\rm se},k})=(1/q!)W_k^{\rm leg}\) EXACT at \(n=1,2\) for
  every \(k\le n\).

**MINOR wording defects recorded by the review (MINOR-1…5).**  MINOR-1
(self-adjointness unstated in Amendment 1's adjoint step) is supplied in (R2)
above.  MINOR-2: "\(\mathbf1_N\) *spans* the trivial \(S_n\times S_n\)
representation" in Amendment 1 §2 should read "*lies in*" — the trivial
isotypic of \(\mathcal L_N\) has dimension \(q!/(n!)^2\) (rank \(6\) at
\(n=2\)); the conclusion \(Q_k^{\rm leg}\mathbf1_N=0\) for \(k>0\) needs only
"lies in" and is unaffected.  MINOR-3: \(P_k^{\rm amb}\)'s per-half form is
asserted in Amendment 1's Notation paragraph and only then proved as A.2′(2)
— presentation, not mathematics.  MINOR-4: Amendment 1 §3's scope sentence —
C1–C5 ran at \(n=2\) only; the review's gates now cover \(n=1\) as well, and
\(n=1\) is a degenerate regime for the lemma.  MINOR-5: Amendment 1's type
paragraph omits \(J_N,J_N^*,J_Y,\mathcal R,P_k^{\rm amb}\) and phrases
\(c\)-independence as a quantifier over \(c\) — the lemma is \(c\)-free.
None has a mathematical consequence; the review is the canonical record of all
five.

### 4. Cites

- `se/artifacts/se_a2prime_review_20260801.md` — SHA-256
  `c6acb691f6f96d0d67421368628823c051d882e7f7005bc35c4d73f815b7ea4b` —
  dedicated rule-7 review of Lemma A.2′: §B.3 **ISSUE-1** (the finding and the
  three-line repair), §B.2 gates **G2–G5**, §B.3 ISSUE-2, MINOR-1…5, VERDICT.
- `se/artifacts/logs_se_a2prime_20260801/` — the reviewer's scripts, logs and
  `SHA256SUMS.txt`.
- `se/proof-dag/nodes/SE.br.cor16.yaml` — work record 2026-08-01
  (outcome); the ISSUE-1 obligation registered there is what this amendment
  discharges.
- **Amendment (2026-07-29)** above, §§1–2 — the (A.2) refutation and Lemma
  A.2′, whose absorb-then-transport pattern is reused here at \(S_{2n}\).
- Companion paper repair: `se/paper/se_explicit_witness.tex`,
  Lemma "Defect pinning"; changelog
  `se/artifacts/se_amendment2_changelog_20260801.md`.
