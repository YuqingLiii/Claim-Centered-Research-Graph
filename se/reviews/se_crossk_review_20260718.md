# Independent mathematical review of `se_crossk_20260718.md`

**Date:** 2026-07-18  
**Role:** rule-6 gate for `SE.denom.crossk`  
**Posture:** independent adversarial re-derivation; no intended verdict assumed

## Executive finding

The load-bearing cross-level argument is correct **for the tapered witness range**. Legal \(X_k,Y_k\) are supported on alphabet defect exactly \(k\) on both sides. In the proved range \(1\le k<K=\lfloor n^{1/3}\rfloor\), legal \(C_k=\mathcal R(W_{{\rm se},k}\Phi_{{\rm se},k})\) is diagonal in the alphabet isotype and supported only on defects \(\{k-1,k\}\) (only defect 1 at \(k=1\)). Consequently:

1. distinct \(X/Y\) levels are two-sided orthogonal;
2. Phi levels at distance at least two are two-sided orthogonal;
3. more sharply, the Phi sum is an orthogonal direct sum over a **common input/output defect** \(d\), with only levels \(d,d+1\) in that block;
4. the signed diamond split gives \(X_d\) coefficient \(\beta_d=\alpha_d-\alpha_{d+1}\), not \(\alpha_d\), so the \(X\)-channel is \(O(1)\); the \(Y\)-channel is also \(O(1)\) due to its \(\sqrt{d/n}\) decay;
5. the proved one-defect Phi envelope is the only growing term: \((\sqrt6/4+o(1))n^{1/6}\) for the chosen representative, doubled to \((\sqrt6/2+o(1))n^{1/6}\) only by the factor-two diamond inequality.

I found no major grading or arithmetic error. I found two required statement corrections:

- **Phi range:** Sections 4 and 8 do not consistently say that the cited Phi support theorem is proved only in the source's range. The source says “henceforth \(1\le k<K\),” and the underlying BR support lemma is invoked in its \(k<n/3\) range. Equations (4.1)–(4.8) are proved as used by the witness, but their unrestricted wording is broader than the citations support.
- **Infinite sums:** Lemma 2.1 is exact for finite families, and for infinite families when an operator sum is actually defined (for example a bounded orthogonal direct sum). “Arbitrary scalars” alone does not define an infinite operator sum. All applications here are finite.

## Per-step verdict table

| item | verdict | finding |
|---|---|---|
| 1. Two-sided orthogonal-sum lemma | **CONFIRMED WITH MINOR QUALIFIER** | Correct for finite sums; an infinite-family convergence/definition hypothesis is missing. |
| 2. Legal \(X/Y\) cross-\(k\) | **CONFIRMED** | PIN (4.7) pins legal input and output to defect exactly \(k\); the alphabet-trivial matching register causes no leak. |
| 3a. Phi two-level support | **CONFIRMED IN RANGE** | Only defects \(\{k-1,k\}\) survive on legal NO, and equivariance transports the same alphabet isotype to legal YES. |
| 3b. Phi diagonality/regrouping | **CONFIRMED IN RANGE** | Source (3.5) has the same partition on both sides; there are no \(d\to d'\) blocks with \(d\ne d'\). |
| 3c. Distance-two orthogonality/parity | **CONFIRMED IN RANGE** | Disjoint support on both sides kills both cross products; parity costs at most two maxima. |
| 4. Signed diamond split | **CONFIRMED** | The exact assignment \(\bar Z_k\mapsto-\bar X_{k-1}\) produces the taper difference on \(X\). |
| 4b. Cancellation (5.6)/(5.7) | **WELL-POSED, OPEN** | \(X_{k-1}\) and \(L_k\) act in the same aggregate defect block. The note correctly refrains from claiming either estimate. |
| 5. Assembly (6.2) | **CONFIRMED** | Coefficients, indices, block factors, and denominators are correct. |
| 5b. \(X/Y\) remainder | **CONFIRMED \(O(1)\)** | \(X\) is weighted by \(\beta_d=1\); \(Y\) is \(\max_d(K-d)\sqrt{2d/n}=O(1)\). |
| 5c. Constants | **CONFIRMED** | \(\sqrt6/4\) is for \(D\); \(\sqrt6/2\) follows from the external factor-two diamond inequality. |
| 6. Disposition/status tables | **CONFIRMED WITH RANGE CORRECTIONS** | Historical adjudications are supported; Phi rows need an explicit proved-range qualifier. |

## 1. Two-sided orthogonal-sum lemma

Assume \(A_i=P_i^YA_iP_i^N\), with the \(P_i^Y\)'s pairwise orthogonal and the \(P_i^N\)'s pairwise orthogonal. For \(i\ne j\),

\[
A_i^*A_j=P_i^NA_i^*P_i^YP_j^YA_jP_j^N=0,
\]

and similarly

\[
A_iA_j^*=P_i^YA_iP_i^NP_j^NA_j^*P_j^Y=0.
\]

For a finite weighted sum \(A=\sum_i c_iA_i\),

\[
A^*A=\sum_i |c_i|^2A_i^*A_i.
\]

The positive summands are supported on the mutually orthogonal spaces \(\operatorname{im}P_i^N\). Hence

\[
\|A\|^2=\|A^*A\|
=\max_i|c_i|^2\|A_i^*A_i\|
=\max_i|c_i|^2\|A_i\|^2.
\]

Thus (2.2)–(2.3) are correct. Both projector families are needed for the stated two-sided row/column conclusion. The only defect is the missing finite/convergence qualifier. The witness has only finitely many nonzero levels, so the omission has no downstream effect.

## 2. Legal \(X/Y\): exact defect on both sides

PIN proves two distinct ingredients:

- exact tensor weight \(k\) allows alphabet defect at most \(k\);
- the primed carrier's full-position defect is at least \(k\), so legal-NO Peter–Weyl pairing kills alphabet defects below \(k\).

Their conjunction leaves legal-NO alphabet defect exactly \(k\). PIN then proves alphabet equivariance and

\[
\mathcal R(\bar T_{{\rm se},k})
=J_Y(\mathbf1_M\otimes W_{n,k}A_{n,=k})
 \bar T_{{\rm se},k}
 (W_{2n,k}A_{2n,=k})J_N^*,
\quad \bar T\in\{\bar X,\bar Y\}.
\]

This is genuinely two-sided. On legal YES, the alphabet group acts diagonally on the injective word and trivially on the matching register. Therefore \(\mathbf1_M\otimes A_{n,=k}\) is the output defect-\(k\) projector. The matching factor can enlarge multiplicities inside an isotype but cannot change its partition or defect. There is no matching-register leak.

After transport through legal restriction,

\[
X_k=E_k^YX_kE_k^N,\qquad
Y_k=E_k^YY_kE_k^N.
\]

For \(k\ne k'\), both \(E_k^SE_{k'}^S=0\). Hence both cross products vanish for each channel, and Lemma 2.1 gives the weighted maximum. The cited PIN review independently confirms the pin, equivariance, output transport, and identity.

## 3. Phi support, diagonality, and regrouping

### 3.1 What the source proves

For the source's range \(1\le k<K\), the Phi note proves:

1. the NO coimage has exact weight \(k\);
2. its full-position defect is at least \(k-1\) and at most \(k\);
3. legal-NO Peter–Weyl pairing therefore permits only alphabet defects \(\{k-1,k\}\);
4. at \(k=1\), exact weight one excludes defect zero, leaving only defect one;
5. \(T_k\) is an alphabet intertwiner, and legal restriction is alphabet equivariant.

The reviewed note correctly says “supported only on.” Neither the source nor its review proves that both candidates are nonzero for every in-range \(n,k\).

### 3.2 The decisive diagonality check

The rectangular identity

\[
C_k=(E_{k-1}^Y+E_k^Y)C_k(E_{k-1}^N+E_k^N)
\]

alone would allow four blocks, including \(E_{k-1}^YC_kE_k^N\) and \(E_k^YC_kE_{k-1}^N\). By itself it would not justify (4.3)–(4.8).

The cited source proves more. Its equation (3.5) is

\[
\mathcal R(T_k)
=\bigoplus_{j\in S_k}\ \bigoplus_{\theta\vdash j}
J_YP_{n,k}A_{n,\lambda(j,\theta)}
T_k
P_{2n,k}A_{2n,\lambda(j,\theta)}J_N^*,
\]

with the **same** partition \(\lambda(j,\theta)=(q-j,\theta)\) on output and input. This follows from alphabet equivariance: an intertwiner commutes with the central isotypic projectors. Consequently

\[
E_a^YC_kE_b^N=0\qquad(a\ne b).
\]

The statement is diagonal even in the full partition label, not merely in defect. The matching register is alphabet-trivial and changes only multiplicity spaces. A level-\(k\) block therefore cannot connect YES defect \(d\) to NO defect \(d'\ne d\).

It follows that

\[
C_k=C_{k\to k-1}+C_{k\to k},\qquad
C_{k\to d}:=E_d^YC_kE_d^N,
\]

with \(C_1=C_{1\to1}\) and \(C_0=0\). The move from (4.1) to (4.3) is correct, but logically uses equivariance/source (3.5), not rectangular support alone.

### 3.3 Orthogonality, parity, and exact defect assembly

If \(|k-k'|\ge2\), the permitted defect sets are disjoint on both sides. Therefore

\[
C_k^*C_{k'}=C_kC_{k'}^*=0.
\]

Within each parity class, different levels differ by at least two. Lemma 2.1 gives an exact maximum inside each parity; the triangle inequality between the even and odd sums gives (4.5).

A fixed defect \(d\) can arise only as:

- the matched block of level \(k=d\);
- the one-defect block of level \(k=d+1\).

Hence, for coefficients supported on the proved level range,

\[
\sum_kc_kC_k
=\bigoplus_d
\left(c_dC_{d\to d}+c_{d+1}C_{d+1\to d}\right).
\]

The \(d\)-summand maps \(E_d^N\mathcal H_N^{\rm leg}\) into \(E_d^Y\mathcal H_Y^{\rm leg}\). Distinct \(d\)'s therefore have orthogonal coimages and ranges, so its norm is the maximum over \(d\). Equations (4.6)–(4.8) are legitimate.

### 3.4 Required range correction

The Phi source sets \(T_0=0\) and then says “henceforth \(1\le k<K\).” Its use of BR's subgroup-support lemma is range-qualified, and the independent Phi review explicitly requires that qualifier. The cross-\(k\) note writes (4.1), (4.3)–(4.8), and corresponding status rows as though they held for all \(k\ge2\) and arbitrary coefficient sequences.

This is a real wording overclaim, but not a gap in the witness proof: every nonzero \(\alpha_k\) has \(k<K\). Restricting the theorem and coefficient sequence to the proved range repairs it.

## 4. Diamond split and the cancellation question

Family split proves the atom identity

\[
\bar W_k=\bar X_k+\bar Y_k+\bar Z_k+T_k
\]

and verifies the representatives

\[
\bar X_k\mapsto\bar X_k,\quad
\bar Y_k\mapsto\bar Y_k,\quad
T_k\mapsto T_k,\quad
\bar Z_k\mapsto-\bar X_{k-1}.
\]

For the last arrow, the blocks share the partner covector, tail, right projector, and matching-stack normalization. Only the queried projector differs, and

\[
\Delta_1\circ\Pi_1
=\Delta_1\circ(I-\Pi_0)
=-\Delta_1\circ\Pi_0.
\]

Linearity and reindexing yield

\[
D=\sum_d(\alpha_d-\alpha_{d+1})X_d
 +\sum_d\alpha_dY_d+\sum_k\alpha_kC_k.
\]

Legal restriction preserves the entrywise diamond equality. Combining this with the defect diagonality gives

\[
D=\bigoplus_dD_d,
\]

where

\[
D_d=\beta_dX_d+\alpha_dY_d
+\alpha_dC_{d\to d}
+\alpha_{d+1}C_{d+1\to d},
\qquad
\beta_d:=\alpha_d-\alpha_{d+1}.
\]

At fixed \(d\), all four operators may act between the same aggregate defect spaces. No cited result gives cross-channel orthogonality, Pythagoras, or cancellation there.

The condition

\[
\sup_{1\le k<K}
\|\beta_{k-1}X_{k-1}+\alpha_kL_k\|=O(1),
\qquad L_k=C_{k\to k-1},
\]

is well-posed: both summands are maps between the full legal spaces, supported on defect \(k-1\) on both sides. An identity

\[
\alpha_kL_k=-\beta_{k-1}X_{k-1}+R_k,
\qquad \sup_k\|R_k\|=O(1),
\]

would imply it. The \(O(1)\) is naturally uniform over \(1\le k<K(n)\). The note correctly labels both statements unproved and does not infer cancellation merely from common defect.

## 5. Independent re-derivation of the assembly arithmetic

### 5.1 Exact coefficients

For

\[
\alpha_k=(K-k)_+,\qquad K=\lfloor n^{1/3}\rfloor,
\]

we have

\[
\beta_d=\alpha_d-\alpha_{d+1}
=\begin{cases}
1,&0\le d<K,\\
0,&\text{otherwise}.
\end{cases}
\]

This is the mechanism in BR:686–698. BR does **not** weight \(X_d\) by \(\alpha_d\) after applying the query mask; the \(\bar Z_{d+1}\mapsto-\bar X_d\) term changes its coefficient to the taper difference. Therefore the feared bound
\(\max_d\alpha_d\|X_d\|\asymp K\) is not the assembly at issue.

### 5.2 Per-defect triangle estimate

Since \(D=\bigoplus_dD_d\),

\[
\|D\|=\max_d\|D_d\|.
\]

Use

\[
\|X_d\|\le\rho_d,\qquad
\|Y_d\|\le\rho_d\sqrt2\sqrt{\frac dn},
\]

\[
\|C_{d\to d}\|
\le\rho_d\|T_d\|
\le\rho_d\frac{\sqrt6}{\sqrt{n-2d+1}},
\]

and, setting \(k=d+1\),

\[
\|C_{d+1\to d}\|
\le d\rho_d\|T_{d+1}\|
\le d\rho_d\frac{\sqrt6}{\sqrt{n-2d-1}}.
\]

The latter two contributions occur only for \(d\ge1\): \(C_0=0\), and \(C_1\) has no defect-zero block. Consequently

\[
\boxed{
\begin{aligned}
\|D\|\le\max_{0\le d<K}\rho_d\Bigg[
&|\beta_d|
+\sqrt2\,\alpha_d\sqrt{\frac dn}\\
&+\mathbf1_{\{d\ge1\}}
 \frac{\sqrt6\,\alpha_d}{\sqrt{n-2d+1}}\\
&+\mathbf1_{\{d\ge1\}}
 \frac{\sqrt6\,d\alpha_{d+1}}{\sqrt{n-2d-1}}
\Bigg].
\end{aligned}}
\]

This is exactly (6.2). In particular, the level-\(d+1\), defect-\(d\) block has legality factor \(d\rho_d\), explaining both the \(d\) and the common \(\rho_d\) in the last term.

### 5.3 Hook envelope

Uniformly for \(0\le d<K\), the cited hook bound is

\[
1\le\rho_d\le e^{n^{-1/3}}=1+O(n^{-1/3}).
\]

It changes the leading term only by a relative \(1+o(1)\) factor and preserves boundedness of the lower-order terms.

### 5.4 X-channel

Because \(\beta_d=1\) on the ramp,

\[
\max_{d<K}\rho_d|\beta_d|=1+o(1).
\]

Thus the legal \(X\) contribution is \(O(1)\), not \(O(K)\). This is precisely BR's condition
\(|\alpha_{k-1}-\alpha_k|\le1\).

### 5.5 Y-channel

Ignoring the uniform \(1+o(1)\) hook factor, maximize

\[
g(d)=\sqrt2(K-d)\sqrt{\frac dn}.
\]

For real \(d\in[0,K]\), maximizing \(g(d)^2=2(K-d)^2d/n\) gives

\[
\frac{d}{dd}\bigl((K-d)^2d\bigr)
=(K-d)(K-3d),
\]

so the interior maximizer is \(d=K/3\). Therefore

\[
\max_d g(d)
=\frac{2\sqrt2}{3\sqrt3}\frac{K^{3/2}}{\sqrt n}+o(1)
=\frac{2\sqrt2}{3\sqrt3}+o(1).
\]

The \(Y\)-channel is uniformly \(O(1)\). This is BR's
\(|\alpha_k|\le\sqrt{n/k}\) condition in optimized form.

### 5.6 Matched Phi block

Uniformly on the ramp,

\[
\max_{1\le d<K}
\frac{\sqrt6\,\alpha_d}{\sqrt{n-2d+1}}
=O\left(\frac K{\sqrt n}\right)
=O(n^{-1/6}).
\]

This term tends to zero.

### 5.7 One-defect Phi block

Here

\[
d\alpha_{d+1}=d(K-d-1)
=\frac{(K-1)^2}{4}
-\left(d-\frac{K-1}{2}\right)^2.
\]

Its integer maximum is

\[
\frac{(K-1)^2}{4}+O(1).
\]

Since \(d<K=O(n^{1/3})\),

\[
(n-2d-1)^{-1/2}
=n^{-1/2}(1+O(n^{-2/3}))
\]

uniformly. Combining this with \(\rho_d=1+O(n^{-1/3})\) and
\(K=n^{1/3}+O(1)\) gives

\[
\begin{aligned}
&\sqrt6\left(\frac{(K-1)^2}{4}+O(1)\right)
n^{-1/2}(1+O(n^{-1/3}))\\
&\hspace{2cm}
=\left(\frac{\sqrt6}{4}+o(1)\right)n^{1/6}.
\end{aligned}
\]

This is the only growing term in the proved envelope.

### 5.8 Why the final coefficient doubles

The preceding estimates give

\[
\|D\|
\le\left(\frac{\sqrt6}{4}+o(1)\right)n^{1/6}+O(1).
\]

The chosen diamond representative satisfies the general comparison

\[
\|\Gamma_n\circ\Delta_1^{\rm leg}\|
\le2\|D\|.
\]

Hence

\[
\|\Gamma_n\circ\Delta_1^{\rm leg}\|
\le\left(\frac{\sqrt6}{2}+o(1)\right)n^{1/6}+O(1).
\]

The coefficient doubles only here. No extra factor two occurs in a channel estimate.

The \(O(1)\) remainder is valid: \(X\) and \(Y\) are bounded, the matched Phi term tends to zero, endpoint and floor errors are bounded, and doubling a uniform \(O(1)\) term remains \(O(1)\).

## 6. Citation audit

Repeated status-table citations are covered with their first substantive use.

| citation(s) in the reviewed note | verdict | what the cited material supports |
|---|---|---|
| `se_familysplit:56–74` | **PASS** | Defines the integer taper and BR-family witness decomposition. |
| `se_familysplit:78–89` | **PASS** | Defines legal YES/NO sets and position invariance. |
| `se_familysplit:91–103,106–130` | **PASS** | Defines normalized legal restriction, common normalization, and the legal witness. |
| `se_bridge2_pin:16–32,45–63` | **PASS** | Defines weight/alphabet projectors and legal spaces; matching is alphabet-trivial. |
| `se_bridge2_pin:74–83`; `se_phi_legal:239–247` | **PASS** | Defines the same matched-degree scalar under the two local naming conventions. |
| `se_bridge2_pin:205–236` | **PASS** | Peter–Weyl annihilation below \(k\), the opposite weight bound, exact legal-NO defect, and adjoint form. |
| `se_bridge2_pin:238–300` | **PASS** | Alphabet equivariance, exact output weight, restriction transport, and the two-sided exact-\(k\) identity. |
| `se_bridge2_pin_review:30–36` | **PASS** | Independently confirms pinning, compatibility, equivariance, output weight, and identity (4.7). |
| `se_bridge2_pin:310–380,382–392`; review `:35–39` | **PASS** | Proves/confirms \(X/Y\) bounds and \(Y_0=0\). |
| `se_familysplit:190–239`; `se_phi_legal:73–104` | **PASS** | Channel definitions, atom split, literal Phi carrier, \(T_k\), and \(T_0=0\). |
| `SE_STAGE2_YES_CARRIER_PROMPT:219–229` | **PASS** | Gives the one-sided counterexample and correctly requires both row and column disjointness. |
| `se_phi_legal:142–220` | **PASS IN RANGE** | Position lower bound, exact-weight upper bound, legal two-level survival, and \(k=1\) endpoint. |
| `se_phi_legal:222–237` | **PASS IN RANGE** | Alphabet equivariance and the diagonal same-\(\lambda\) decomposition on both legal sides. This is load-bearing for (4.3)–(4.8). |
| `se_phi_legal_review:28–33,230–239` | **PASS, WITH REQUIRED QUALIFIERS** | Confirms support and diagonality while requiring “supported only on” and BR's range qualifier. The reviewed note adopts the former but not consistently the latter. |
| `se_phi_legal:267–326` | **PASS IN RANGE** | Matched and one-defect block **upper bounds**, with two-sided factor \(k-1\). |
| `se_phi_legal:328–362` | **PASS IN RANGE** | Uniform hook envelope on the witness range. |
| `se_phi_legal:364–406`; review `:34–42` | **PASS IN RANGE** | Full per-level factor and ambient \(\sqrt6/\sqrt{n-2k+1}\) bound. |
| `se_familysplit:243–255` | **PASS** | Entrywise diamond requirement, nonuniqueness, and linearity. |
| `se_familysplit:243–288`; `se_bridge2_reviews:55–64` | **PASS** | Verifies all four assignments, especially \(\bar Z_k\mapsto-\bar X_{k-1}\). |
| `se_familysplit:290–329` | **PASS** | Exact signed ambient representative and its normalized legal restriction. |
| `SE_PROOF_DAG:524–532`; `se_phi_legal:459–470` | **PASS** | Records cross-channel cancellation/correlated taming as open and states its obligations. |
| `se_familysplit:332–340` | **PASS** | Legal factor-two diamond inequality. |
| `exact_band_descent_analysis:449–466` | **PASS** | Same \(Y\)-channel optimization and constant-order conclusion. |
| `se_phi_legal_review:175–204` | **PASS** | Independent conditional derivation of the \(\sqrt6/4\) envelope coefficient. |
| `exact_band_descent_analysis:76–87` | **PASS AS HISTORICAL CLAIM, NOT PROOF** | Asserts exactly the legal \(X/Y\) orthogonality described in the disposition row. |
| `exact_band_descent_analysis:288–340,346–400` | **PASS AS CHARACTERIZED** | The first range depends on asserted support (5.3); the later range argues strict alphabet support but does not replace PIN's proof. |
| `SE_HANDOFF_CONTINUE_PROOF:60–61` | **PASS AS HISTORICAL SCOPE RECORD** | Records cross-\(k\) only for the \(S_n\times S_n\) family and contains the stale line citation identified by the DAG. |
| `se_familysplit:318–349`; `se_bridge2_reviews:55–68` | **PASS** | Identifies the actual witness channels and confirms family split without claiming legal cross-\(k\). |
| `SE_BRIDGE_COMMISSION_PROMPT:610–613,630–633,321–328` | **PASS** | Records the then-open bridge, retitles the tool ambient-only, and distinguishes ambient from legal orthogonality. |
| `SE_PROOF_DAG:483–490` | **PASS AS PRIOR STATUS** | Records crossk as open with the conflicts later adjudicated. |
| `se_phi_legal_review:230–247` | **PASS** | Requires support/range corrections and leaves the true \(O(1)\) tame rescue open. |

No false load-bearing citation was found. The citation-to-claim problem is one of **scope**: the Phi sources prove their cited conclusions in a stated range, whereas the reviewed note sometimes presents them without that range.

## 7. Disposition and status-table audit

| reviewed-note record/row | review disposition |
|---|---|
| Old exact_band “no loss” record | **KEEP.** The conclusion is now derivable from PIN; the old document did not itself supply the later exact alphabet identity. |
| Handoff \(S_n\times S_n\) scope | **KEEP.** Family split identifies the witness; PIN supplies the missing legal theorem for \(X/Y\), not Phi. |
| Ambient-only tool ruling | **KEEP.** The current proof does not use ambient numerical orthogonality as legal evidence. |
| Stage-2 parity caveat | **KEEP AS ANSWERED IN RANGE.** Phi source (3.5) supplies both-side diagonal support. |
| Prior `SE.denom.crossk` OPEN row | **UPDATE TO DISCHARGED FOR THE WITNESS RANGE.** Every nonzero tapered level is covered. |
| Legal alphabet grading/equivariance | **KEEP PROVED.** |
| \(X_k,Y_k\) exact defect \(k\) | **KEEP PROVED.** |
| \(X/Y\) orthogonality and maximum | **KEEP PROVED.** |
| Phi \(\{k-1,k\}\) support, distance-two orthogonality, parity, regrouping | **CHANGE TO “PROVED IN THE WITNESS RANGE \(1\le k<K\)”**, with \(C_0=0\). |
| Phi block/ambient bounds | **CHANGE TO “PROVED IN THE STATED SOURCE RANGE.”** They are upper bounds, not block-norm equalities. |
| Exact signed legal diamond split | **KEEP PROVED.** |
| Within-defect cross-channel orthogonality/cancellation | **KEEP OPEN / NO PROOF.** |
| (6.2) and \(n^{1/6}\) envelope | **KEEP PROVED AS AN UPPER ENVELOPE.** It is not a lower bound on the true norm. |
| True \(O(1)\) legal denominator | **KEEP OPEN.** |

The note does not make the suspected \(O(K)\) \(X\)-channel error: Section 5 correctly turns the signed reindexing into \(\beta_dX_d\), and Section 6 correctly uses \(|\beta_d|=1\). It also correctly refrains from claiming cancellation.

**FINAL VERDICT: CONFIRMED WITH REQUIRED SCOPE/CONVERGENCE CORRECTIONS — `SE.denom.crossk` PASSES/DISCHARGES for the tapered witness range; the exact defect regrouping and assembly arithmetic are correct; no \(O(K)\) \(X\)-term is present; the proved denominator envelope is \(n^{1/6}+O(1)\), while a true \(O(1)\) legal denominator remains OPEN.**
