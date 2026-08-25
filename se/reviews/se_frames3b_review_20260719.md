# Independent adversarial review of R3b

Date: 2026-07-19

Object: `se/artifacts/se_frames3b_20260719.md`

Role: fresh independent reviewer; no source repair and no DAG edit

## 0. Verdict

The operator-level no-go is real. It is not caused by a mis-built gate.
The two mixed-color sectors independently reproduce the exact ratios
(17/12) and (2), after checking the branch normalizations, the
(delta_z+1) weights, and the (B_\theta(q)^2) target. Therefore the
simultaneous operator route (F3.40)--(F3.41) is dead project-wide as stated.

The proposed trace successor ((M_{\rm phys})) is correctly typed and does
imply both inequalities in (F3.42)=(R.33). It passes the nine submitted exact
gates, including an independent reconstruction of the two refuting sectors.
It remains CONJECTURED because no all-(c) proof or (c=2) identity-level gate
exists. It is also not literally the minimal sufficient trace statement:
the two conclusions (F3.42), written in the (S/L) variables, are strictly
weaker and already sufficient. ((M_{\rm phys})) is nevertheless a clean,
natural stronger frontier lemma.

The scalar countermodel is valid. The dominance inequalities remain strong
pressure evidence, but R3b's displayed fraction for the (0.3035) maximum is
not exact: it is a `Fraction(float)` artifact. The corresponding rational-table
candidate gives (163/537=0.303538175046555\ldots). The stretch dimensions and
the absence of a (c=2) construction are correctly recorded.

| check | verdict |
|---|---|
| Z1, necessary implication | **CONFIRMED** |
| Z2, two refuting gates | **CONFIRMED** |
| Z3, ((M_{\rm phys})) | **GAP**: implication and gates confirmed; minimality claim rejected; all-(c) proof remains open |
| Z4, scalar countermodel | **CONFIRMED** |
| Z5, dominance and stretch | **GAP**: inequalities/dimensions confirmed; “exact” maximum fraction refuted |
| Z6, honesty and conditional chain | **CONFIRMED**, with one conservative under-classification noted below |

Promotion recommendation: mark the target route (F3.40)--(F3.41)
**REFUTED / DEAD** and the mathematical no-go proposition **PROVED as a
refutation**, citing this review and its independent gate log. Keep
((M_{\rm phys})), (F3.42), (R.33), and (C_Y'=15/4) **CONJECTURED**. No
promotion of the trace successor is licensed by the nine (c=1) gates.

## 1. Independent type audit and retyping

Let

[
 \mathcal C=P_\xi V_\lambda,\qquad \dim\mathcal C=dc,
 \qquad \mathcal O=\operatorname{Ran}P_{\rm comp},\qquad
 \dim\mathcal O=R,
]

and

[
 T=N_{a,b}f^\alpha f^\beta,qquad
 N_{a,b}=\binom{n-1}{a}\binom{n-1-a}{b}.
]

Thus (c=c_{\alpha\beta}^{\theta}) occurs in the carrier dimension (dc),
not as an extra copy on an output branch. The physical branch has type

[
 B_{h,\gamma}:\mathcal C\longrightarrow\mathcal O,qquad
 B_{h,\gamma}\in\mathbb C^{R\times dc}.
]

I retype (R3b.1)--(R3b.3) as follows:

[
 K_{h,\gamma}:\mathbb C^T\to\mathcal O
 \quad(R\times T),\qquad
 U_h:\mathbb C^T\to\mathcal C
 \quad(dc\times T),
]

[
 B_{h,\gamma}=K_{h,\gamma}U_h^*,\qquad
 U_h^*U_h\preceq I_T,                                      \tag{R3b.1'}
]

[
 \mathcal K_h:=K_{h,0}^*K_{h,0}
 +\sum_z(\delta_z+1)K_{h,z}^*K_{h,z}
 \preceq B_\theta(q)^2I_T,                                \tag{R3b.2'}
]

[
 B_{h,0}^*B_{h,0}
 +\sum_z(\delta_z+1)B_{h,z}^*B_{h,z}
 \preceq B_\theta(q)^2I_{dc}.                             \tag{R3b.3'}
]

Every term in (R3b.2') is (T\times T); every term in (R3b.3') is
(dc\times dc).

For the trace successor, define independently

[
 \mathscr X_h=\bigoplus_{s\in\mathcal D_{a,b}}
 \operatorname{Ran}\Pi_{D_{h,s}},
 \qquad \dim\mathscr X_h=N_{a,b}f^\theta.
]

There is no factor (c) in this ambient direct sum. Define

[
 L_h:\mathcal C\to\mathscr X_h,qquad
 L_hx=(\Pi_{D_{h,s}}P_\xi x)_s,
 \qquad L_h\in\mathbb C^{(N_{a,b}f^\theta)\times dc},
]

[
 S_{h,\gamma}:\mathscr X_h\to\mathcal O,qquad
 S_{h,\gamma}(y_s)_s
 =P_{\rm comp}\sum_s\rho_\lambda(\tau_{h,s})Q_\gamma y_s,
 \qquad S_{h,\gamma}\in
 \mathbb C^{R\times(N_{a,b}f^\theta)}.
]

Direct expansion gives the exact identity

[
 B_{h,\gamma}=S_{h,\gamma}L_h:
 \mathbb C^{dc}\to\mathbb C^R.                            \tag{1.1}
]

Finally, my retyped successor statement is

[
 \operatorname{Tr}_{\mathcal C}\!\left[
 L_h^*\left(S_{h,0}^*S_{h,0}
 +\sum_z(\delta_z+1)S_{h,z}^*S_{h,z}\right)L_h
 \right]
 \le B_\theta(q)^2T.                                      \tag{Mphys'}
]

The parenthesized map is an
((N_{a,b}f^\theta)\times(N_{a,b}f^\theta)) endomorphism of
(\mathscr X_h); after the (L_h^*(\cdot)L_h) sandwich the operator is
(dc\times dc), including all (c) multiplicity directions. The trace is
therefore well defined and the right side intentionally contains (T), not
(Tc).

The admissible/strict terminology resolves through R3b's explicit import of
(F3.3)--(F3.38), which in turn cites `se_frames1_20260719.md`, Definition
2.1. The long and tail branches, (delta_z), (B_\theta(q)), and the tame
range also resolve in those cited definitions. I found no unresolved term of
art that changes the quantifiers of the reviewed claims.

## 2. Z1: necessary consequence

Starting from (R3b.1'),

[
 B_{h,0}^*B_{h,0}
 +\sum_z(\delta_z+1)B_{h,z}^*B_{h,z}
 =U_h\mathcal K_hU_h^*.
]

Because (U_h^*U_h\preceq I_T), every singular value of (U_h) is at most
one; hence (U_hU_h^*\preceq I_{dc}). Congruencing (R3b.2') by (U_h)
gives

[
 U_h\mathcal K_hU_h^*
 \preceq B_\theta(q)^2U_hU_h^*
 \preceq B_\theta(q)^2I_{dc}.
]

This is airtight. It does not assume that (U_h) has full rank, that
(T=dc), or that the (K)'s arise from a particular output frame. My
derivation coincides notationally with R3b because the displayed statement
itself fixes (B,K,U); the substantive check is the singular-value step
(U_h^*U_h\preceq I_T\Rightarrow U_hU_h^*\preceq I_{dc}), which is valid
for rectangular (dc\times T) matrices.

**Z1 verdict: CONFIRMED.**

## 3. Z2: independent refuting gates

### 3.1 Construction paths

The independent script does not import the R3b gate script. It uses a
rational Young-seminormal model with its invariant diagonal Gram. It builds
(P_\xi) by the exact (S_{n-1}\times S_n) character average,
(P_{\rm comp}) by the exact (S_n) average, and the query branches from
the Jucys--Murphy eigenprojectors for the two (S_{q-1}) children.

The fixed-set route constructs

[
 A_h=\sum_{(I,J)\in\mathcal D_{1,1}}
 \rho_\lambda(\tau_{I,J})\Pi_{D_{I,J}}P_\xi
]

with exact rational matrices. It obtains each (Pi_D) by conjugating an
independently averaged pointwise-stabilizer projector. This exercises
(F3.19), not the grouped-polar (K/U) candidate.

The separate literal route enumerates all (8!=40320) permutations. For
the canonical split ((a,b)=(1,1)), its coefficient is the coefficient of
(xy) in

[
 (8\mathbf1[g(1)=1]-1)
 \prod_{i=2}^4\left(
 1+(8\mathbf1[g(i)=i]-1)x
 +(8\mathbf1[g(\bar i)=i]-1)y\right).
]

It then applies the reviewed reflection split, dividing the raw Fourier
matrix by (8^2\,6!), dividing the long branch additionally by (omega),
and putting the reflection minus sign on the tail. This literal path uses a
different coefficient construction from the fixed-set path. Its final
matrix comparison was numerical in the rational representation gauge; the
exact spectra below come from the separate exact fixed-set matrices. The
literal-vs-formula infinity-norm residuals are below (5\times10^{-13}).

### 3.2 Normalization audit

For (	heta=(2)),

[
 f^{(6,2)}=20,quad f^{(5,2)}=14,quad
 p_0=7/10,quad \omega=3/7,quad
 \delta=5,quad \delta+1=6,quad
 B_\theta(8)=\frac{\binom82}{20}=\frac75.
]

Thus the gate target is (B_\theta(8)^2=49/25).

For (	heta=(1,1)),

[
 f^{(6,1,1)}=21,quad f^{(5,1,1)}=15,quad
 p_0=5/7,quad \omega=2/5,quad
 \delta=7,quad \delta+1=8,quad
 B_\theta(8)=\frac{\binom82}{21}=\frac43.
]

Thus the gate target is (16/9). These values agree with the proposer code.
The proposer code also uses the correct (q^j(q-j)!) raw scale, long-branch
(omega^{-1}), tail sign, completion projector normalization, and squared
target. No (n!^{-1/2}), (q!), matching average, or multiplicity factor is
missing from these physical branch gates.

### 3.3 Exact results

| sector | exact nonzero spectrum of the weighted physical Gram | maximum | target | ratio |
|---|---|---:|---:|---:|
| ((4,8,2),(2),(1,1)) | (28/25,833/300,833/300) | (833/300) | (49/25) | (17/12) |
| ((4,8,2),(1,1),(1,1)) | (4/9,4/9,32/9) | (32/9) | (16/9) | (2) |

The exact branch traces also reproduce R3b:

| sector | (operatorname{Tr}B_0^*B_0) | (operatorname{Tr}B_z^*B_z) | weighted trace |
|---|---:|---:|---:|
| ((2),(1,1)) | (1862/375) | (427/1500) | (1001/150) |
| ((1,1),(1,1)) | (256/63) | (1/21) | (40/9) |

The submitted nine-gate program was also rerun unchanged. All nine formula
identities, literal-kernel identities, (F3.42) checks, and
((M_{\rm phys})) checks pass; only the two rows above fail the necessary
operator inequality and the grouped-polar (F3.41) check.

A counterexample at (c=1) is sufficient against the universally stated
operator factorization. The unavailable (c=2) gate cannot rescue it.

**Z2 verdict: CONFIRMED. The operator route is dead project-wide as stated.**

## 4. Z3: the trace successor

Using (1.1), the left side of (Mphys') is exactly

[
 \|B_{h,0}\|_{\rm HS}^2
 +\sum_z(\delta_z+1)\|B_{h,z}\|_{\rm HS}^2.
]

All terms are nonnegative. Discarding the tail terms gives

[
 \|B_{h,0}\|_{\rm HS}^2\le B_\theta(q)^2T.
]

If (delta_{\min}=\min_z\delta_z), then

[
 (\delta_{\min}+1)\sum_z\|B_{h,z}\|_{\rm HS}^2
 \le\sum_z(\delta_z+1)\|B_{h,z}\|_{\rm HS}^2
 \le B_\theta(q)^2T,
]

which is the second inequality in (F3.42)=(R.33). Both steps are valid even
with several tail branches.

The independent refuting-gate construction gives

[
 1001/150<294/25,qquad 40/9<32/3,
]

so the two hostile rows independently pass (Mphys'). The unchanged submitted
program confirms the other seven rows.

The word “minimal” in R3b is too strong. A strictly weaker sufficient trace
statement is the conjunction

[
 \operatorname{Tr}(L_h^*S_{h,0}^*S_{h,0}L_h)\le B_\theta(q)^2T,
]

[
 \operatorname{Tr}\!\left(
 L_h^*\sum_zS_{h,z}^*S_{h,z}L_h\right)
 \le\frac{B_\theta(q)^2T}{\delta_{\min}+1}.
]

Equivalently, one may put the two normalized traces inside a maximum. This
is exactly (F3.42) in the (S/L) variables and is implied by, but does not
imply, the joint-budget statement (Mphys'). Thus (Mphys') is a stronger and
more structured conjecture, not the logically minimal sufficient one.

**Z3 verdict: GAP.** The formulation is review-clean as a natural new
frontier statement, and its implication is proved, but its minimality claim
is false and its all-(c) content remains unproved. Keep it CONJECTURED.

## 5. Z4: scalar countermodel

Take (dc=1,T=2,B_\theta(q)=1), and one branch
(B=[\sqrt2]:\mathbb C\to\mathbb C). Then

[
 \|B\|_{\rm HS}^2=2=B_\theta(q)^2T,
]

so the relevant trace cap is saturated. If
(B=KU^*), with (U\in\mathbb C^{1\times2}),
(K\in\mathbb C^{1\times2}), (U^*U\preceq I_2), and
(K^*K\preceq I_2), then

[
 \sqrt2=\|B\|\le\|K\|\,\|U\|\le1,
]

a contradiction. The dimensions and norm implications are correct. This
shows that a Hilbert--Schmidt cap alone cannot recover the operator
factorization.

**Z4 verdict: CONFIRMED.**

## 6. Z5: dominance and stretch

I recomputed the exact (F3.47) envelope formula for all 40 JSON rows from
((n,\theta,a,b,\alpha,\beta,d)); every result equals the stored exact
envelope. All 40 stored rational value candidates are below those envelopes.
The nine small rows and six (n=5) rows also rerun below their stated
conditional envelopes.

The maximum occurs at
((n,j,\theta,a,b)=(9,3,(1,1,1),0,3)). The stored rational candidate and
exact envelope are

[
 \frac{489}{2380},\qquad \frac{1611}{2380},
]

so their exact ratio is

[
 \frac{489}{1611}=\frac{163}{537}
 =0.303538175046555\ldots.
]

R3b's fraction
(7402555353896389/24387559662836536) is the exact ratio of the two binary
floating-point fields after conversion to `Fraction`; it is not the exact
mathematical ratio of the rational table entries. The decimal and the
identity of the worst row are unaffected. Moreover, the 40 “values” are
numerically computed values with rational candidates, not exact symbolic
evaluations in this audit. Accordingly, the dominance conclusion is
confirmed as numerical pressure evidence, not as the stated set of 40 exact
values.

At the stretch point I independently obtain

[
 f^{(8,3,2,1)}=23296,quad
 f^{(3,2,1)}=16,quad f^{(4,2,1)}=35,quad d=560,quad dc=1120,
]

[
 T=\binom63\binom33(f^{(2,1)})^2=80,qquad M=240240.
]

The LR coefficient is (c_{(2,1),(2,1)}^{(3,2,1)}=2), represented by the
two LR words (112) and (121). The physical and complete-colored set
counts are respectively (20) and (700). Thus the budget box is correct.

For the already refuted operator target, the stretch construction is moot,
not a possible rescue. For (Mphys'), the honest classification is exactly
the one R3b ultimately gives: (c=2) **UNTESTED**, with the required
(23296\times1120) exact subduction embedding unavailable. “Infeasible” is
a record of the present construction budget, not a mathematical
infeasibility theorem for the trace lemma.

**Z5 verdict: GAP** because the exact maximum fraction and the exactness
description of the 40-row values are wrong; the inequalities, decimal
maximum, stretch dimensions, and untested label are confirmed.

## 7. Z6: status and conditionality audit

R3b is honest about the main logical separation:

- the exact finite gates refute (F3.40)--(F3.41), but do not refute
  (F3.42) or (Mphys');
- all nine tests are at (c=1), and the (c=2) trace gate is explicitly
  untested;
- (F3.47), (C_Y'=15/4), and the downstream assembly remain conditional
  on (F3.42) or the stronger successor;
- dominance is described as pressure evidence and is not used to repair the
  false factorization;
- no stretch (K/V) matrices are fabricated.

The pre-review overall ceiling and pending-review markers were appropriate.
After this independent review, the no-go/route-refutation may be promoted as
recommended in Section 0, while the trace claims must not move.

One row is conservatively under-classified: (R3b.24), here (1.1), is a
definition-level exact factorization and follows by direct expansion. It
does not need to remain “NUMERICAL/CONJECTURED” as an identity, although no
useful norm bound follows from it. This under-classification is not an
overclaim and does not affect the ceiling.

**Z6 verdict: CONFIRMED.**

## 8. Rule-7 accounting

- **7a:** Sections 1--2 retype every in-scope factorization and trace map,
  including the (c)-dependent carrier dimension.
- **7b:** all nine submitted gates were rerun; the two decisive gates were
  independently reconstructed. A (c=2) gate is unnecessary to refute the
  universal operator route but remains mandatory before promoting the
  all-(c) trace successor.
- **7c:** the necessary implication was rederived from rectangular-operator
  singular values. The coincident notation is disclosed in Section 2.
- **7d:** no earlier review was treated as covering the new operator-level
  necessary condition or the (c\ne1) trace regime.
- **7e:** branch scale, long-branch (omega), tail sign,
  (delta_z+1), (B_\theta(q)^2), completion normalization, physical
  versus complete colored sets, carrier multiplicity, and ambient/carrier
  trace were separately checked.
- **7f:** the exact spectra come from an independent fixed-set construction;
  the literal (q!)-term path is a separate coefficient construction and
  agrees numerically at matrix level. The unchanged proposer program also
  reran its exact literal formula. These roles are not conflated.
- **7g:** admissibility, strictness, branch terminology, and ranges resolve
  to the cited definitions.

**Overall Rule-7 verdict: PASS for the operator no-go/refutation. GAP for
the trace successor as a theorem, exactly because the (c=2) regime is
untested and no all-(c) proof exists.**

## 9. Reproduction

Python:
`<machine-local-path-redacted>`

Review scripts and logs are in
`se/artifacts/logs_se_frames3brev_20260719/`. The SHA-256 manifest in that
directory covers this review, the independent scripts and logs, the
submitted R3b artifact, and the submitted gate scripts used in the audit.
