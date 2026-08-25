# Independent rule-6 review of SE.br.cor16

**Reviewed:** se/artifacts/se_cor16_20260718.md  
**DAG node:** SE.br.cor16  
**Posture:** independent and adversarial; every citation in the note was checked against the cited lines.

## Executive result

The mathematical lower bound is correct:

\[
\operatorname{Adv}^{\pm}(\operatorname{SE}(n,2n))
\ge \left(\frac{2}{\sqrt6}-o(1)\right)n^{1/6}.
\]

The adversary theorem applies, the exact legal numerator is at least
\(K=\lfloor n^{1/3}\rfloor\), the denominator result is for the same normalized
integer-taper witness, and the all-position symmetry and ratio arithmetic are
valid.

Three documentation corrections are required:

1. Note line 47 names the wrong symmetry group. The relevant trivial
   representation is for BR's **position group** \(S_n\times S_n\), not the
   alphabet group \(S_q\). The annihilation conclusion remains correct.
2. The cited sources do not establish the priority claim “first explicit
   adversary lower bound.” They support the historical background but do not
   exclude all earlier explicit, suboptimal, small-alphabet witnesses.
3. Some status-table records overstate their citations: BR:715–724 does not
   alone prove the exact \(q=2n\) normalization; the cited family review does
   not independently review that normalization; and the cited legal-set lines
   state only within-half invariance, not the half swap.

## Per-step verdicts

| step | verdict | finding |
|---|---|---|
| 1. Adversary theorem and feasibility | **PASS** | BR:170–200 states the negative-weight quarter-matrix SDP, masks, constraints, scaling, and \(Q=\Theta(\mathrm{Adv})\). Homogeneity gives the ratio in the direction used. The witness is a nonzero real legal YES-by-NO matrix, and its maximum masked norm is positive. |
| 2. Numerator | **PASS WITH NOTATION CORRECTION** | In the common legal gauge, level zero is \(q!^{-1}J\), while every \(k>0\) position-isotype projector kills the legal all-ones vector. Hence \(\Gamma_n\mathbf1_N=K\mathbf1_Y\) and \(\|\Gamma_n\|\ge K\). Replace \(S_q\) by \(S_n\times S_n\). |
| 3. Denominator at position 1 | **PASS** | se_crossk (6.2)–(6.6) and its review use the same \(q=2n\), \(K=\lfloor n^{1/3}\rfloor\), taper, and normalized restriction. They prove \(\|\Gamma_n\circ\Delta_1\|\le(\sqrt6/2+o(1))n^{1/6}+O(1)\), including endpoints. |
| 4. Maximum over positions | **PASS, CITATION INCOMPLETE** | Within-half permutations and the half swap make this witness transitive on all \(2n\) positions. BR:537–538 states the ambient conclusion, but the note's legal-invariance citation supplies only within-half permutations. |
| 5. Ratio and scope | **PASS for mathematics; FAIL for priority** | The floor, reciprocal asymptotics, and epsilon statement are correct. The note honestly leaves the \(\Omega(n^{1/3})\) explicit-witness target open. The word “first” is not supported. |
| 6. Status table | **FAIL as a citation/review record; no mathematical gap** | The denominator and ratio rows are accurate. The witness, theorem, numerator, and maximum rows need the qualifications above. |

## 1. Adversary theorem and feasibility

BR:175–196 defines a nonzero \(f^{-1}(1)\times f^{-1}(0)\) adversary
matrix and maximizes \(\|\Gamma\|\) subject to
\(\|\Delta_i\circ\Gamma\|\le1\) for every position. BR:198–200 explicitly
permits scaling an arbitrary adversary matrix. Thus, for

\[
D(\Gamma):=\max_i\|\Gamma\circ\Delta_i\|>0,
\]

the scaled matrix is feasible and

\[
\operatorname{Adv}^{\pm}(F)\ge\frac{\|\Gamma\|}{D(\Gamma)}.
\]

This is the correct direction and form. BR writes \(\operatorname{Adv}\) while
calling it the negative-weight adversary bound; \(\operatorname{Adv}^{\pm}\)
is a notational variant. There is no nonnegativity condition on entries.

BR:302–333 gives the positive/negative orientation and legal deletion. The
note's matrix has precisely the required legal indexing. Its vectors,
projectors, tensor sums, and position-isotype projectors can be taken real.

The maximum masked norm cannot vanish. The numerator proof gives
\(\Gamma_n\ne0\). Choose a nonzero entry \(\Gamma_n[y,x]\). A legal YES string
and legal NO string cannot be identical, so \(y_i\ne x_i\) for some \(i\).
That entry survives in \(\Gamma_n\circ\Delta_i\), making its norm positive.

## 2. Independent numerator and normalization audit

At \(q=2n\),

\[
|N_n|=(q)_{2n}=q!,\qquad
|Y_n|=|M_{\rm se}|(q)_n=n!(q)_n=q!.
\]

The NO identity counts bijections. A legal YES input is a bipartite matching
between halves plus an injective symbol assignment to its edges.

The normalization in se_familysplit:91–126 is compatible with BR's block
normalization. Raw BR level zero has constant entry

\[
\frac{q^{-3n/2}}{\sqrt{n!}},
\]

and the common probability-\(L^2\) legal restriction scalar is

\[
c_0=\frac{q^{3n/2}}{\sqrt{(q)_n(q)_{2n}}}.
\]

Their product is

\[
\frac1{\sqrt{n!(q)_n(q)_{2n}}}=\frac1{q!}.
\]

Thus level zero is exactly \(q!^{-1}J\). For unit all-ones vectors,

\[
q!^{-1}J\mathbf1_N=\mathbf1_Y.
\]

For \(k>0\), \(P_k\) consists of position \(S_n\times S_n\) isotypes with
total first-row defect \(k\). It is orthogonal to the trivial position isotype
containing \(\mathbf1_N\). Legal restriction preserves the position action, so
\(P_k\mathbf1_N=0\). Consequently

\[
\Gamma_n\mathbf1_N=K\mathbf1_Y,\qquad \|\Gamma_n\|\ge K.
\]

BR:715–721 is about the **legal restricted operators** and supplies the
trivial-isotype mechanism. But BR assumes \(q=\Omega(n^2)\) and concludes only
that level zero retains \(\Omega(1)\) norm. Exact norm one at \(q=2n\) comes
from the separate count and normalization. The note's phrase “trivial
\(S_q\)-representation” is a group-label error: BR uses
\(\mathfrak S_{\rm se}=S_n\times S_n\), the position group.

There is no taper mismatch in the actual proof. BR displays
\(\max\{n^{1/3}-k,0\}\); the note and denominator proof consistently use
\((K-k)_+\). They differ for noncubes, but BR's decomposition is linear in
arbitrary coefficients and all needed estimates are re-established for the
integer taper. It gives \(K=n^{1/3}+O(1)\) and changes no asymptotic constant.

## 3. Denominator audit

The se_crossk object is the note's object: lines 11–17 set \(q=2n\),
\(K=\lfloor n^{1/3}\rfloor\), and \(\alpha_k=(K-k)_+\); lines 19–25 use the
same probability-\(L^2\) restriction \(\mathcal R\); and
se_familysplit:119–130 identifies it with the single \(q!^{-1}\) factor.

For the chosen legal diamond representative \(D\), (6.2) proves

\[
\|D\|\le\max_{0\le d<K}\rho_d\left[
|\beta_d|+\sqrt2\alpha_d\sqrt{\frac dn}
+\mathbf1_{d\ge1}\frac{\sqrt6\alpha_d}{\sqrt{n-2d+1}}
+\mathbf1_{d\ge1}\frac{\sqrt6d\alpha_{d+1}}{\sqrt{n-2d-1}}
\right],
\]

where \(\beta_d=1\) on the ramp and
\(\rho_d=1+O(n^{-1/3})\) uniformly. The endpoint indicators correctly remove
\(C_0\) and the nonexistent defect-zero block of \(C_1\); out-of-range
coefficients vanish.

The contributions are

\[
X=O(1),\quad Y=O(1),\quad
\Phi_{\rm matched}=O(K/\sqrt n)=O(n^{-1/6}),
\]

while

\[
d\alpha_{d+1}=d(K-d-1)
=\frac{(K-1)^2}{4}
-\left(d-\frac{K-1}{2}\right)^2
\]

gives the sole growing envelope
\((\sqrt6/4+o(1))n^{1/6}\). BR's diamond comparison contributes one factor of
two:

\[
\|\Gamma_n\circ\Delta_1\|
\le2\|D\|
\le\left(\frac{\sqrt6}{2}+o(1)\right)n^{1/6}+O(1).
\]

The review at se_crossk_review:245–437 reconstructs the coefficient
difference, (6.2), all four envelopes, and the single doubling. Its 479–500
disposition correctly limits the result to the tapered witness range. No
normalization, taper, endpoint, or equation-number mismatch was found.

## 4. Independent all-position symmetry check

Within each half, \(S_n\times S_n\) preserves the legal sets, matching stack,
\(P_k\), and masks. Thus masked norms are constant separately in the halves.

Let \(\tau\) swap the halves. It preserves both promises and permutes the
bipartite matching set. Moreover, \(\Psi_0\) is symmetric because
\(\Pi_0\otimes e_0^*=e_0^*\otimes\Pi_0\), \(\Psi_1\) is symmetric by its
two-term definition, and
\(P_k=\sum_{\ell=0}^k\bar\Pi_{k-\ell}^{(n)}\otimes\bar\Pi_\ell^{(n)}\) is
invariant under swapping factors. Therefore permutation unitaries satisfy

\[
U_\tau\Gamma_nV_\tau^*=\Gamma_n,\qquad
U_\tau(\Gamma_n\circ\Delta_i)V_\tau^*
=\Gamma_n\circ\Delta_{\tau(i)}.
\]

Spectral norms are equal, proving

\[
\max_{i\in[2n]}\|\Gamma_n\circ\Delta_i\|
=\|\Gamma_n\circ\Delta_1\|.
\]

The conclusion is sound, but the citations are incomplete. BR:377–385 defines
\(\mathfrak S_{\rm se}=S_n\times S_n\), which has two position orbits, although
BR:537–538 later states equality for every position. The note's
se_familysplit:78–89 citation likewise mentions only within-half invariance.

## 5. Independent ratio arithmetic

Let \(a=\sqrt6/2\). For some \(\eta_n\to0\) and fixed \(C\),

\[
D_n\le(a+\eta_n)n^{1/6}+C=(a+o(1))n^{1/6}.
\]

Also,

\[
K=\lfloor n^{1/3}\rfloor
=n^{1/3}\bigl(1+O(n^{-1/3})\bigr).
\]

Hence

\[
\frac{\|\Gamma_n\|}{D_n}
\ge\frac K{D_n}
\ge n^{1/6}\frac{1+O(n^{-1/3})}{\sqrt6/2+o(1)}
=\left(\frac2{\sqrt6}-o(1)\right)n^{1/6}.
\]

This is equivalent to the note's epsilon statement. Hidden constants are not
effective in the cited sources, so declining to give a numerical \(n_0\) is
correct.

## 6. Citation audit

| cited source/range | verdict | audit |
|---|---|---|
| se_familysplit:78–89; BR:302–325 | **PASS** | Defines the promises, orientation, and equal \(q=2n\) counts. |
| BR:170–200 | **PASS** | States the negative-weight SDP, masks, scaling, and \(Q=\Theta(\mathrm{Adv})\). |
| BR:1496–1502, 1516–1522 | **PASS** | HLS07 and LMR11 bibliography entries named by BR. |
| BR:484–488, 523–532 | **PASS** | Gives \(\Psi_0,\Psi_1\), tensor sum, and matching-stack normalization. |
| BR:600–611 | **PASS** | Defines the Set-Equality position-isotype projector. |
| se_familysplit:91–130 | **PASS** | States normalized legal restriction, common \(q!^{-1}\), and the legal witness. |
| SE_PROOF_DAG:291–295; SE_HANDOFF_CONTINUE_PROOF:28–37 | **PASS AS INTERNAL RECORDS** | Record the definition and normalization, but are not independent proofs. |
| BR:715–724 | **PASS for the legal all-ones mechanism; FAIL if used alone for exact normalization** | Higher levels kill the trivial position isotype; BR gets only \(\Omega(1)\) at level zero under \(q=\Omega(n^2)\). |
| SE_PROOF_DAG:297–300 | **FAIL AS AN “AUDIT”** | Records the claim and finite measurements; does not prove exact all-\(n\) normalization. |
| se_familysplit:78–89, 98–126 | **PASS** | Supports equal cardinalities and common normalization. |
| se_crossk:277–304, 308–350, 315–352 | **PASS** | Contains (6.1)–(6.6), endpoints, all channel estimates, and doubling. |
| se_crossk_review:280–323, 325–437, 479–500 | **PASS** | Reproduces (6.2), checks the envelopes and factor two, and confirms the witness-range result. The definition of \(\beta_d\) is slightly earlier at 245–263. |
| BR:537–538 plus se_familysplit:78–89 | **FAIL AS A COMPLETE LEGAL ALL-POSITION PROOF** | BR states the ambient conclusion; the legal citation only gives within-half invariance. The half-swap proof above repairs it. |
| SE_PROOF_DAG:541–549, 567–578 | **PASS** | Records the open \(O(1)\) Phi problem and proved \(n^{1/6}\) envelope. |
| Rosmanis:1071–1078; BR:108–120 | **PASS for background; FAIL for priority** | Supports the known query bound, old large-alphabet restriction, failed small-alphabet analysis, and abstract existence. Does not prove “first explicit.” |
| SE_HANDOFF_CONTINUE_PROOF:20–26 | **FAIL AS EXTERNAL PRIORITY EVIDENCE** | An internal assertion that citations were read is not reproducible external priority evidence. |
| SE_PROOF_DAG:546–548 | **PASS** | Consistent with \(K\ge2\iff n\ge8\); theorem is asymptotic. |
| se_bridge2_reviews:55–68 | **FAIL AS A NORMALIZATION REVIEW CITATION** | Reviews family split and diamond assignments, not exact \(q!^{-1}\) normalization. |
| BR:170–200, 323–333 in the status row | **FAIL AS THE COMPLETE FEASIBILITY RECORD** | Gives theorem, indexing, and deletion. Reality, nonzeroness, and positive denominator are proved in the note/review. |
| se_crossk:277–352 and review in the status row | **PASS** | Proves and reviews the position-1 bound, endpoints, and range. |

## 7. Scope and status-table audit

The Scope section is honest about the mathematical reach: it proves only
\(\Omega(n^{1/6})\), not the known \(\Theta(n^{1/3})\) query complexity, and
leaves an \(O(1)\) denominator open. BR:108–120 and Rosmanis:1071–1078 support
that history. They do not support **first**. A defensible replacement is:

> Equations (2)–(3) give an explicit adversary lower bound for Set Equality at
> the minimal alphabet. The cited sources do not establish a priority claim.

| status row | disposition |
|---|---|
| Explicit witness and normalization | **KEEP PROVED**, but remove the claim that se_bridge2_reviews:55–68 reviews normalization or cite an actual normalization audit. |
| Adversary feasibility and theorem | **KEEP PROVED**, citing BR for the theorem and this note/review for witness feasibility. |
| Numerator | **KEEP PROVED**, with separate exact-normalization support and \(S_q\) corrected to \(S_n\times S_n\). |
| Denominator at \(i=1\) | **KEEP PROVED** for the tapered witness range. |
| Maximum over positions | **KEEP PROVED**, adding the half-swap derivation. |
| Ratio and query lower bound | **KEEP PROVED**. |
| Rule-6 review | **UPDATE** to the qualified confirmation below. |

**FINAL VERDICT: CONFIRMED WITH REQUIRED CORRECTIONS — the mathematical DAG node SE.br.cor16 is proved and may be discharged, but the note should correct the symmetry-group label, add half-swap/exact-normalization support to its status records, and remove or qualify the unsupported “first explicit adversary bound” priority claim.**
