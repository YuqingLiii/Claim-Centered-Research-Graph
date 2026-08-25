# Fresh Rule-7 review: finite YES alphabet point-child gate at `a=16`

Date: 2026-07-22  
Controlling node:
`KSUM.B4b.L3.ALT.hidden-frequency-mask.critical-endpoint.ALT.induced-packet-occurrence-pencil-classification`  
Reviewed artifact:
`ksum/artifacts/ksum_L3_critical_induced_packet_yes_alphabet_point_child_gate_a16_20260722.md`  
Reviewed artifact SHA-256:
`F83B3F4F376A9499DB7B4B6E7281AAF422DE940417FB0C34B999A7BFC6A0ED50`

## Verdict

**MINOR / SCOPED PASS.**  A genuinely isolated pre-proposer derivation and an independent exact
checker confirm the complete finite YES point-child object at

\[
 a=16,\qquad q=64,\qquad t=1,\qquad \tau=(61,2),
\]

for one fixed raw mark.  The licensed finite facts are:

* the three-parent closure `(62,2),(61,3),(61,2,1)` with complete multiplicities `1,5,10`;
* all sixteen YES multiplicity columns and all eight marked Mackey sectors, with ranks
  `(1,1,1,1,5,1,5,1)`;
* the unequal-cell Mackey factor
  `sqrt(n_target*d_target/(n_source*d_source))` and the failure of the old equal-cell scaling;
* the exact JM characteristic and minimal-polynomial identities, its three parent projectors,
  and a square exact parent/Mackey isometry;
* eight exact same-fixed-mark point-child projectors, their resolution of `I_16`, all 28 actual
  zero products and commutators, every parent-pair codiagonal block, and algebra/commutant
  dimensions `8` and `56`;
* both physical `16 x 10` orientation isometries and, for each, an exact six-column orthogonal
  complement with parent dimensions `0+2+4`.

The **MINOR** qualifications are provenance and presentation defects, not false finite values.
The proposer JSON writes the 28 product/commutator rank fields as zero after checking the raw
coordinate projectors; it does not multiply the archived parent-gauge tables.  The independent
checker performs those 56 actual matrix operations exactly.  Also, the proposer artifact counts
each orientation image and its six-dimensional complement but does not archive either orientation
map or its unmatched columns.  The independent checker constructs both maps and both exact
complements.  Finally, the proposer uses a floating comparison only to choose column signs; that
choice is gauge-only and no exact rank, projector, or normalization depends on it.

The controlling node remains **OPEN**.  This review does not complete its occurrence-pencil or
physical-assembly claim.

## 1. Independence, anchoring, and evidence

### 1.1 Governing blind seal

The no-context checker first read both repository protocols and only the reviewed predecessor
definitions.  Before opening or grepping the YES artifact, tool, output, contaminated baseline,
or target node, it archived

`ksum/artifacts/ksum_L3_yes_alphabet_point_child_gate_a16_rule7_isolated_checker_seal_20260722.md`,

SHA-256
`4E1843E78D87181A3021D6DB647339AAE58E81E1E5C56D87308DC1809B77B980`.
That seal independently froze the character, parent/sector counts, unequal-cell normalization,
JM/projector expectations, orientation types, unmatched dimensions, algebra dimensions, and
scope cuts.  No desired values or verdict were supplied.

An earlier main-review artifact,
`ksum/artifacts/ksum_L3_critical_induced_packet_yes_alphabet_point_child_gate_a16_rule7_blind_baseline_20260722.md`,
SHA-256
`69A4C46E98C6AA2E723A14EF1E5ED8DE1257FF9092483F38BFC3FF00C0607987`,
is explicitly labelled **anchoring-contaminated, not blind** because a broad repository search
surfaced two terse canonical-node result snippets.  It is retained for disclosure and is not used
to satisfy Rule 7(c).

### 1.2 Independent checker and immutable output

The post-seal checker does not import either proposer tool:

* checker: `ksum/tools/ksum_l3_yes_alphabet_point_child_gate_rule7_independent.py`, SHA-256
  `538A1711FD19147F3F1266118F848A175816DE06DD6937CA56CB228A9ACE6694`;
* exact output:
  `ksum/artifacts/logs_ksum_L3_yes_alphabet_point_child_gate_rule7_independent_20260722/independent_exact.json`,
  SHA-256 `D0C6F1F38C3CC616CB76900303C3F2C3E806610D86990EFB1125C88003DA925B`;
* run log in the same directory, SHA-256
  `2E1E2E6E8F6204B54CCFDA1A63AFE4168A56D9B84D905EAF62BC31EC6E65C48D`;
* commands, SHA-256
  `275822D1E00FA54302AABC43DE675987161D7A64E449E4387F429715D46386BE`;
* `manifest.json`, SHA-256
  `37014254F217E5329DF98D3A66EF88B6FE8E5C88B2433B3D49B597773E303327`;
* `SHA256SUMS.txt`, whose own SHA-256 is
  `3E91AA70CB494FD5F2B35C3C5866248E156469680BE1FFBFE2BD62B183A7C0C6`.

Every line in that checksum file was rehashed successfully.  The exact output reports
`ALL_INDEPENDENT_YES_ALPHABET_RULE7_GATES_PASS` and `discrepancies=[]`.

### 1.3 Proposer provenance and secondary rerun

The proposer inputs are:

| file | SHA-256 |
|---|---|
| reviewed artifact | `F83B3F4F376A9499DB7B4B6E7281AAF422DE940417FB0C34B999A7BFC6A0ED50` |
| `ksum/tools/ksum_l3_yes_alphabet_point_child_gate.py` | `3DE2DD5E77CBAB60D1C5CA30CDB12EEC1B96C481BC4408AC6257630AC3E2903C` |
| original `ksum/artifacts/logs_ksum_L3_yes_alphabet_point_child_gate_20260722/run.json` | `05C07213ECB406D0F61118BCF214D551F59170074CC5E2399EB1A5F6AEAAB333` |

Only after the independent construction and exact comparison passed was the proposer rerun.  The
fresh output
`ksum/artifacts/logs_ksum_L3_yes_alphabet_point_child_gate_rule7_review_20260722/fresh_proposer_run.json`
is byte-identical to the original JSON, with the same SHA-256
`05C07213ECB406D0F61118BCF214D551F59170074CC5E2399EB1A5F6AEAAB333`;
stderr is empty.  This is a secondary reproducibility check, not the proof of an exact claim.

## 2. Independent mathematical reconstruction

### 2.1 Full character and parent closure

The exact YES subgroup has ordered cell sizes

\[
 (|U|,|C|,|L|,|R|,|H_L|,|H_R|)=(1,1,15,15,16,16)
\]

and character

\[
 \operatorname{ch}M_1=h_1^2h_{15}^2s_{(15,1)}^2
 =h_{15}^4h_1^4-2h_{16}h_{15}^3h_1^3+h_{16}^2h_{15}^2h_1^2.
\]

The addable cells of `(61,2)` are exactly `(1,62),(2,3),(3,1)`.  An independently implemented
reverse-Pieri interlacing recurrence gives:

| parent | first term | middle term | last term | signed multiplicity |
|---|---:|---:|---:|---:|
| `(62,2)` | 24 | 18 | 13 | `24-2*18+13=1` |
| `(61,3)` | 56 | 38 | 25 | `56-2*38+25=5` |
| `(61,2,1)` | 88 | 55 | 32 | `88-2*55+32=10` |

Thus the complete fixed-child parent multiplicity space is
`Y_(1,tau)=R^1 direct-sum R^5 direct-sum R^10`, of dimension sixteen.

### 2.2 Complete marked inventory

Restriction of either heavy standard is
`V_16 downarrow S_15 = 1 direct-sum V_15`.  Independently applying the same character recurrence
after marking each cell gives:

| raw outcome | exact Pieri combination | rank | local carrier dimension `d_chi` |
|---|---:|---:|---:|
| `U` | `18-2*13+9` | 1 | 225 |
| `C` | `18-2*13+9` | 1 | 225 |
| `L` | `24-2*18+13` | 1 | 225 |
| `R` | `24-2*18+13` | 1 | 225 |
| `H_L,eta=1` | `18-13` | 5 | 15 per multiplicity line |
| `H_L,eta=V15` | `24-18-18+13` | 1 | 210 |
| `H_R,eta=1` | `18-13` | 5 | 15 per multiplicity line |
| `H_R,eta=V15` | `24-18-18+13` | 1 | 210 |

The complete raw column order is

\[
 U,C,L,R,
 H_{L,1,0},\ldots,H_{L,1,4},H_{L,V15},
 H_{R,1,0},\ldots,H_{R,1,4},H_{R,V15}.
\]

The query-inactive cell `U` must be retained for the exhaustive marked resolution.  It is not
thereby declared a queried status.

### 2.3 Unequal-cell normalization

For a sector from a cell of size `n_c` with local irreducible dimension `d_c`, its marked
`S_63` Mackey summand has dimension

\[
 \frac{63!}{\prod_e n_e!}\,n_cd_c.
\]

Therefore a column from source `c` to row/destination `d` in normalized Frobenius coordinates
has the exact factor

\[
 \boxed{\sqrt{\frac{n_dd_d}{n_cd_c}}}.
\]

The sixteen `n_c d_c` weights are

\[
 225,225,3375,3375,
 \underbrace{240,\ldots,240}_{5},3360,
 \underbrace{240,\ldots,240}_{5},3360.
\]

This is distinct from the local Hilbert--Schmidt divisors `225`, `15`, and `210`.  Replacing the
boxed factor by the old equal-cell factor gives an exact nonsymmetric matrix: the independent
guard finds skew rank eight and the first skew entry `14`.  Thus the correction is load-bearing,
not cosmetic.

### 2.4 Both orientation images and all unmatched columns

The reviewed NO parent multiplicities are `(1,3,6)`.  The two raw rare-sector maps at `a=16` are

\[
\begin{aligned}
 j_L(A)&=\tfrac14 C+\tfrac{\sqrt{15}}4L,&
 j_L(B)&=\tfrac14 U+\tfrac{\sqrt{15}}4R,\\
 j_R(A)&=\tfrac14 U+\tfrac{\sqrt{15}}4L,&
 j_R(B)&=\tfrac14 C+\tfrac{\sqrt{15}}4R.
\end{aligned}
\]

For a heavy `eta=1` line, use coarse coefficient order
`(internal,A,B,marked-heavy)` with metric `diag(14,16,16,15)` and fine order
`(internal,U,C,L,R,marked-heavy)` with metric `diag(14,1,1,15,15,15)`.  The two physical splits are

\[
 S_L(x,a,b,m)=(x,b,a,a,b,m),\qquad
 S_R(x,a,b,m)=(x,a,b,a,b,m).
\]

Both preserve the weighted metric.  Passing to exact orthonormal constraint-kernel bases gives
the two `5 x 3` heavy-trivial isometries; each heavy-`V15` line maps identically.  The resulting
raw maps `j_L,j_R:R^10->R^16` satisfy exactly

\[
 j_o^Tj_o=I_{10},\qquad X_1j_o=j_oX_0,
 \qquad o=L,R.
\]

In parent order their only nonzero blocks have types

\[
 \mathbb R^1\to\mathbb R^1,qquad
 \mathbb R^3\to\mathbb R^5,qquad
 \mathbb R^6\to\mathbb R^{10},
\]

all of full source rank.  Projected-coordinate exact Gram--Schmidt constructs, for each
orientation, `u_o:R^6->R^16` satisfying

\[
 u_o^Tu_o=I_6,\qquad j_o^Tu_o=0,\qquad
 j_oj_o^T+u_ou_o^T=I_{16}.
\]

The six columns split by parent as `(0,2,4)`.  Both full `16 x 6` matrices are archived in the
independent JSON.  The two image projectors are not equal, so no orientation-free complement or
zero padding has been substituted.

### 2.5 JM, parent gauge, and exact status tables

The three addable-box contents are `61,1,-2`.  The archived exact JM matrix is symmetric and
satisfies

\[
 \chi_X(x)=(x-61)(x-1)^5(x+2)^{10},\qquad
 (X-61I)(X-I)(X+2I)=0.
\]

The independent checker reconstructs from the archived `X`, rather than trusting summary flags,

\[
 P_{61}=\frac{(X-I)(X+2I)}{3780},\quad
 P_1=-\frac{(X-61I)(X+2I)}{180},\quad
 P_{-2}=\frac{(X-61I)(X-I)}{189}.
\]

They equal the archived projectors, are symmetric idempotents of ranks `(1,5,10)`, are mutually
orthogonal, and sum to `I_16`.  The archived exact matrix `E` is square orthogonal and obeys
`XE=E diag(61,1^5,(-2)^10)`.

For every raw sector projector `D_chi`, the checker reconstructs the actual table

\[
 C_\chi=E^TD_\chi E\in\operatorname{End}(\mathbb R^{16})
\]

and compares every exact entry to the JSON.  The eight ranks are
`(1,1,1,1,5,1,5,1)`, every table is symmetric and idempotent, and their entrywise sum is `I_16`.
For all 28 unordered pairs, the checker actually forms both matrices and obtains

\[
 C_\chi C_{\chi'}=0,\qquad [C_\chi,C_{\chi'}]=0.
\]

All three off-diagonal parent blocks are nonzero in every table.  Their block ranks in the
`1|5|10` split are `(1,1,1)` for each rank-one table and `(1,1,5)` for each rank-five table.  All
24 displayed radical witnesses agree exactly with the archived matrices.

After complexification, the generated algebra and commutant are therefore

\[
 \mathcal A\cong\mathbb C^8,\qquad \dim\mathcal A=8,
\]

\[
 \mathcal A'\cong M_1(\mathbb C)^{\oplus6}\oplus M_5(\mathbb C)^{\oplus2},
 \qquad \dim\mathcal A'=56.
\]

## 3. Rule-7(a): complete type audit

Write `Y=Y_(1,tau)=R^16`, `Y_0=R^10`, and `f^tau=1890`.

| object/display | source and target | dimension/type result |
|---|---|---|
| harmonic boundary in (4.1) | `R^binom(63,2) -> R^63` | kernel dimension `1890`; realizes `S^tau` |
| passive local row | `V_16 tensor V_16 -> S^tau` | `225 -> 1890`; HS divisor 225 |
| heavy `eta=1` local row | `V_16 -> S^tau` | `15 -> 1890`; five multiplicity rows; HS divisor 15 |
| heavy `eta=V15` local row | `V_15 tensor V_16 -> S^tau` | `210 -> 1890`; HS divisor 210 |
| coefficient kernel | subspace of `R^6` with metric `diag(14,1,1,15,15,15)` | one constraint, exact dimension five |
| factorization (4.5) | equality in `S_64` | `r_c,r_d,h in S_64`, `l in S_63`; all 378 `(d,i)` cases checked |
| `X=J_64` | `Y -> Y` | exact symmetric `16 x 16` endomorphism |
| `P_61,P_1,P_-2` | `Y -> Y` | exact `16 x 16` parent projections of ranks `1,5,10` |
| `E` | parent multiplicity coordinates `R^(1+5+10) -> Y` | exact orthogonal `16 x 16` isometry |
| `D_chi` | `Y -> Y` in Mackey gauge | eight disjoint coordinate projectors |
| `C_chi=E^T D_chi E` | parent multiplicity space to itself | exact `16 x 16` endomorphism |
| cross-parent block `(nu,nu')` | `R^(m_(1,nu')) -> R^(m_(1,nu))` | legal after common `S_63` restriction; all three pairs tested |
| `j_o` | `Y_0 -> Y` | exact `16 x 10` isometry, block diagonal in the three `S_64` parents |
| `u_o` | `R^6 -> Y` | exact `16 x 6` orthogonal complement, parent ranks `0,2,4` |
| `P_o=j_oj_o^T` | `Y -> Y` | exact rank-ten orientation-image projector |
| full marked table | `S^tau tensor Y -> S^tau tensor Y` | `I_(S^tau) tensor C_chi`; full dimension `1890*16` |

No ordinary NO/YES commutator is typed: the two answer tables act on unequal spaces.  This review
constructs the two embeddings but does not use them to assert an orientation-pulled transfer or
commutator result.

## 4. Rule-7(b): regime-complete identity gates

The finite claim contains all qualitatively distinct regimes and all are exercised at identity
level:

* parent multiplicities `1`, `5`, and `10`, not only a multiplicity-one parent;
* marked ranks `1` and `5`;
* cell sizes `1`, `15`, and `16`;
* local carrier dimensions `15`, `210`, and `225`;
* passive, heavy-trivial, and heavy-standard rows on both sides;
* the query-inactive `U` cell as part of exhaustive marked restriction;
* both physical orientations, all ten common columns, and all six unmatched columns for each;
* all three parent projectors, all eight status projectors, all 28 distinct products, all 28
  commutators, and all 24 parent-pair block witnesses.

The proposer computes the same exact JM matrix for two shifted exact unit-vector profiles.  Those
profiles use the same chosen vector on the two heavy legs.  The independent checker additionally
constructs a genuinely mixed admissible left/right unit profile.  Vector independence is closed
at formula level: the summed contraction is equivariant on each irreducible local product carrier
and hence a Schur scalar.  It is not inferred merely from agreement at two vectors.

## 5. Rule-7(c)--(g)

### 5.1 Anchoring ban

**PASS.**  The governing no-context seal was complete before any target inspection and contains
the values and gates later found in the proposer.  The contaminated main baseline is disclosed and
excluded from the Rule-7 evidence.

### 5.2 No frozen-input immunity

**PASS.**  The review reopens exactly the aspects of the reviewed `t=0` gate used here: the
`1|3|6` parent source, the raw rare/heavy coefficient gauges, and the orientation refinement.  It
does not infer unequal-cell normalization from the equal-cell review.  The old files remain
byte-identical.

### 5.3 Standing failure-mode list

| standing attack | disposition |
|---|---|
| dropped/extra normalization | PASS; derived `sqrt(n_d d_d/(n_c d_c))`; equal-cell substitution has exact skew rank 8 |
| type/dimension mismatch | PASS; Section 3 types every operator and all multiplicity/carrier dimensions |
| undefined term or missing stability range | PASS after Section 6 definitions; this is one finite point and has no unstated stability threshold |
| colored-orbit sum substituted for full central sum | PASS; `J_64` uses all 63 transpositions and all six destination cells; all 378 coset factorizations are present |
| numerics support values while printed derivation is broken | PASS with the provenance split below; all licensed identities are exact and the printed normalization/type formulas were audited separately |

Additional hostile gates also pass: no parent or multiplicity line is selected away; `U` is not
dropped; both orientation complements are explicit; old parent labels are not made into false
superselection tags; no nonorthonormal transpose is used; and the reviewed `t=0` archive is not
modified.

### 5.4 Value versus formula

**PASS with explicit decoupling.**  Independent construction establishes the parent/sector
characters, normalization law and failure guard, and both orientation maps/complements.  Exact
parsing independently recomputes the identities of the archived JM, projectors, `E`, and tables,
including actual products and block ranks.  Separately, the review audits why the harmonic
embeddings are isometric, why the Mackey factor has the displayed cell-size ratio, why `J_64` is
the complete centralizer element in scope, and why `C=E^TDE` is the normalized physical table.
The byte-identical proposer rerun is reproducibility only.

### 5.5 Quantifier hygiene

**PASS.**  The exact terms used here mean:

* **one fixed raw mark:** one palette coordinate `z` is fixed while its physical cell status varies;
  it does not mean that `z` is always in cell `C`;
* **same mark:** every table in one product uses that same `z`; it excludes distinct `z,w`;
* **complete point-child packet:** all sixteen multiplicity columns over the three parents sharing
  this one `tau`; it is not the entire all-`tau`, all-occurrence physical source;
* **common image:** the rank-ten image of one specified physical `j_o`;
* **unmatched complement:** the orthogonal six-dimensional complement of that specified image,
  with parent dimensions `(0,2,4)`; it is orientation dependent;
* **parent gauge:** the single common exact orthonormal basis obtained from the three JM spectral
  projectors;
* **query-inactive `U`:** required in the exhaustive Mackey resolution but not promoted to a
  physical query branch.

## 6. Preserved `t=0` archive

The following reviewed predecessor files were hashed before and after the YES review and are
unchanged:

| file | preserved SHA-256 |
|---|---|
| `ksum/artifacts/ksum_L3_critical_induced_packet_alphabet_point_child_gate_a16_20260722.md` | `ECF051FEF929E8B461E05539F8E2D227766C7AE0650EB30A8D7A1AB628E7B6D5` |
| its blind baseline | `B4FBEAD1A9310DBBE7E99D0D88D3481C0B79EE94EBC11C4E00B62CEA03B32170` |
| its Rule-7 review | `4A8FEE28DFD4FC91EEB6E7B5F89BC8A0A3C26491895AC1AFE6889982E1560137` |
| `ksum/tools/ksum_l3_alphabet_point_child_gate.py` | `A247A6DB9EEDE94EBB83626ED3F41EB3047A99B2487901597A0D7EF5BBDA010F` |
| `ksum/tools/ksum_l3_alphabet_point_child_gate_rule7_check.py` | `050398A04A26CBD19FE422143A261CFA5C31546343DFBBA6754694366499E6B1` |
| original `t=0` `run.json` | `8281115792877C373B88C53601E34F99C1DDC72BBCA45048CB16258559100976` |
| prior fresh proposer run | `921A6BE0C5157C75121082A626596A2E4BEC1A4C8D861B9DBC99053F85A7271D` |
| prior independent audit JSON | `2AC4CD40B26C2E95A25C49EDCE154A4DCD81B234EE57EB54A6AC580394817902` |

## 7. Exact licensed and withheld scope

### Licensed

This review licenses exactly the finite `a=16,q=64,t=1,tau=(61,2)` alphabet point-child
multiplicity calculation for one fixed raw mark: the complete `1|5|10` parent closure, the full
sixteen-column marked restriction, the eight-projector codiagonal resolution and its
`C^8`/commutant algebra, the exact JM parent recovery, and both rank-ten physical orientation
images with their full six-column complements.

### Explicitly withheld

This review does **not** license:

1. any distinct-mark (`z != w`) table, product, or commutator;
2. occurrence restriction Grams, position-Pieri scalars, or their assembly with this alphabet
   factor;
3. a NO-to-YES transfer, an orientation-pulled cross-answer effect, or a native rectangular
   transfer conclusion;
4. any spectrum other than the finite alphabet JM spectrum explicitly audited above;
5. simultaneous diagonalization or noncommutation of an assembled physical pencil;
6. feasibility of any resolvent, Sylvester, holonomy, or adversary coefficient law;
7. any all-`s` formula, asymptotic inference, query attenuation, numerator, or exponent.

The finite result is a correct input table.  It is not a proof of the controlling node's broader
classification claim.

