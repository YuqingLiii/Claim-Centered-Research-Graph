# Fresh Rule-7 review: first-target alphabet point-child gate at `a=16`

Date: 2026-07-22  
Reviewer: fresh independent instance; not the proposer  
Controlling node:
`KSUM.B4b.L3.ALT.hidden-frequency-mask.critical-endpoint.ALT.induced-packet-occurrence-pencil-classification`

## Verdict

**MINOR / SCOPED PASS** for exactly the finite NO-alphabet statement

\[
 a=16,\qquad q=64,\qquad t=0,\qquad
 \tau_*=(61,2),\qquad\text{one fixed common raw mark}.
\]

The complete parent closure, multiplicities `1,3,6`, six marked Mackey ranks
`1,1,3,1,3,1`, exact `10 x 10` Jucys--Murphy matrix, canonical parent gauge, all six
same-mark point-child tables, their cross-parent blocks, orthogonal resolution, algebra
`C^6`, and commutant dimension `22` pass fresh exact review.

This does **not** complete the controlling node.  It licenses no claim about a second raw mark,
YES, another `a`, a uniform family, occurrence restrictions, position-Pieri assembly, a physical
one-side pencil, query attenuation, a numerator, or an exponent.

The `MINOR` qualification is for two broken TeX tokens in the proposer Markdown, not for a failed
mathematical gate:

1. lines 32--35 split the intended `\mathrm{rare}` token across lines;
2. lines 86--87 split the intended `\mathrm{horizontal}` token across lines.

They should be repaired before publication.  The program also uses a 30-digit numerical sign test
only to choose the positive-leading representative of an already exact one-dimensional gauge.
That comparison changes at most column signs and is not load-bearing for any rank, projector,
normalization, commutator, or algebra claim.

## 1. Independence and blind freeze

Before opening the proposer derivation, tool, or JSON, I froze a hostile baseline in
`ksum/artifacts/ksum_L3_critical_induced_packet_alphabet_point_child_gate_a16_rule7_blind_baseline_20260722.md`.
The commission and a claim-facing repository search had disclosed the scope and the claimed
Frobenius characteristic, which I treated as the statement to audit.  They did not disclose a
wanted verdict.  The baseline independently predicted:

* the three addable parents `(62,2)`, `(61,3)`, `(61,2,1)`;
* contents `61,1,-2`;
* Pieri rows `(13,9,6)`, `(25,16,10)`, `(32,17,8)` and multiplicities `1,3,6`;
* marked ranks `3,1,3,1,1,1` in left-trivial, left-standard, right-trivial,
  right-standard, rare-A, rare-B order;
* same-mark orthogonal completeness, algebra `C^6`, and commutant dimension `22`, conditional on
  the proposed gauge and normalization actually being unitary.

The baseline also froze fourteen failure modes, including the omitted three-row parent, `c>1`
line deletion, a nonorthogonal harmonic gauge, a wrong Schur trace divisor, value-only checks,
same-mark/distinct-mark confusion, and finite-to-asymptotic overreach.  The proposer was opened only
after this freeze.

## 2. Inputs and fresh provenance

The reviewed immutable proposer inputs are:

| input | SHA-256 | result |
|---|---|---|
| proposer artifact `ksum/artifacts/ksum_L3_critical_induced_packet_alphabet_point_child_gate_a16_20260722.md` | `ECF051FEF929E8B461E05539F8E2D227766C7AE0650EB30A8D7A1AB628E7B6D5` | hash matches commission |
| proposer tool `ksum/tools/ksum_l3_alphabet_point_child_gate.py` | `A247A6DB9EEDE94EBB83626ED3F41EB3047A99B2487901597A0D7EF5BBDA010F` | hash matches commission |
| proposer JSON `ksum/artifacts/logs_ksum_L3_alphabet_point_child_gate_20260722/run.json` | `8281115792877C373B88C53601E34F99C1DDC72BBCA45048CB16258559100976` | hash matches commission |

Fresh reviewer evidence is:

| evidence | SHA-256 | role |
|---|---|---|
| blind baseline | `B4FBEAD1A9310DBBE7E99D0D88D3481C0B79EE94EBC11C4E00B62CEA03B32170` | pre-proof derivation and hostile gates |
| reviewer checker `ksum/tools/ksum_l3_alphabet_point_child_gate_rule7_check.py` | `050398A04A26CBD19FE422143A261CFA5C31546343DFBBA6754694366499E6B1` | independent recurrence, construction audit, and parsed-matrix gates |
| fresh proposer rerun `ksum/artifacts/logs_ksum_L3_alphabet_point_child_gate_rule7_review_20260722/fresh_proposer_run.json` | `921A6BE0C5157C75121082A626596A2E4BEC1A4C8D861B9DBC99053F85A7271D` | clean rerun; semantically identical to archived JSON |
| fresh audit `ksum/artifacts/logs_ksum_L3_alphabet_point_child_gate_rule7_review_20260722/audit.json` | `2AC4CD40B26C2E95A25C49EDCE154A4DCD81B234EE57EB54A6AC580394817902` | contains result field `ALL_ALPHABET_POINT_CHILD_RULE7_GATES_PASS` |

The fresh checker was run from the repository root as

```powershell
python ksum/tools/ksum_l3_alphabet_point_child_gate_rule7_check.py
```

and printed `ALL_ALPHABET_POINT_CHILD_RULE7_GATES_PASS`.

## 3. From-scratch mathematical reconstruction

### 3.1 Raw and marked modules

Let

\[
 G=S_{64},\qquad H=S_{16}^A\times S_{16}^B\times S_{16}^L\times S_{16}^R,
\]

and let `V_16=S^(15,1)` be the fifteen-dimensional standard representation.  The NO alphabet
module used here is

\[
 M_0=\operatorname{Ind}_H^G
 (\mathbf1_A\boxtimes\mathbf1_B\boxtimes V_{16,L}\boxtimes V_{16,R}).
\]

Therefore, by the ordinary Frobenius characteristic of outer induction,

\[
 \operatorname{ch}M_0=h_{16}^2s_{(15,1)}^2.
\]

This rederives the load-bearing input rather than granting it frozen-input immunity.

Fix raw letter `64` and let `K=S_63` be its point stabilizer.  The double cosets `K\G/H` are
exactly the four cells containing the marked letter.  Their local carriers are

| marked cell | local carrier | carrier dimension | multiplicity at `tau_*` |
|---|---|---:|---:|
| `A` rare | `V_16,L tensor V_16,R` | 225 | 1 |
| `B` rare | `V_16,L tensor V_16,R` | 225 | 1 |
| `L`, `eta=1` | `1 tensor V_16,R` | 15 | 3 |
| `L`, `eta=V_15` | `V_15,L tensor V_16,R` | 210 | 1 |
| `R`, `eta=1` | `V_16,L tensor 1` | 15 | 3 |
| `R`, `eta=V_15` | `V_16,L tensor V_15,R` | 210 | 1 |

Here `V_15=S^(14,1)` has dimension fourteen and
`V_16 downarrow S_15 = 1 direct-sum V_15`.  Thus every status and every multiplicity regime in
scope is present before a matrix is constructed.

### 3.2 Independent character calculation

I independently counted each complete-function coefficient with a reviewer-written recurrence
that enumerates bounded inner partitions and tests a horizontal strip in **conjugate** coordinates.
It does not call the proposer's interlacing enumerator.  With
`s_(15,1)=h_15 h_1-h_16`, the results are

| parent | `A` | `B` | `C` | `A-2B+C` |
|---|---:|---:|---:|---:|
| `(62,2)` | 13 | 9 | 6 | 1 |
| `(61,3)` | 25 | 16 | 10 | 3 |
| `(61,2,1)` | 32 | 17 | 8 | 6 |

The addable-box enumeration is exhaustive: the only boxes are `(1,62)`, `(2,3)`, and `(3,1)`.
The marked characteristics independently give `9-6=3`, `13-9-9+6=1`, and
`13-2*9+6=1`; mirroring the heavy side and duplicating the rare cell yields total
`3+1+3+1+1+1=10`.

### 3.3 Sparse point-child carrier

For `n=63`, the unsigned vertex-edge incidence matrix of the complete graph has rank `63`, so

\[
 \ker\left(\mathbb R^{\binom{63}{2}}\longrightarrow\mathbb R^{63},
 x\longmapsto\left(\sum_{j\ne i}x_{\{i,j\}}\right)_i\right)
\]

has dimension `binom(63,2)-63=1890=f^(61,2)` and is the standard harmonic-edge realization of
`S^(61,2)`.  The reviewer checker verifies exact zero vertex sums and unit norm for both proposer
test choices in all ten multiplicity lines.

For an `eta=1` heavy sector, the four coefficient coordinates have weighted edge norm
`diag(14,16,16,15)` and harmonic constraint

\[
 14a+16b+16c+15d=0.
\]

The three printed vectors satisfy this constraint and have exact weighted Gram `I_3`; hence they
are a complete orthonormal basis of that three-dimensional multiplicity.  The rank-15 and rank-14
local projectors are exact symmetric idempotents, and all local carrier dimensions agree with the
table above.

The map is equivariant because permutations within a heavy block act by relabeling the active
standard vector, while permutations of the other blocks either relabel a constant cross-edge
fiber or act trivially.  The three support patterns in the `eta=1` case are block-orbit sums and
therefore transform by the same opposite-heavy standard.  This establishes the Schur-scalar use;
it is not inferred merely from two favorable coordinates.  As an extra gate, the reviewer reran
the entire JM contraction with a third **mixed** pair of independent standard vectors and obtained
the same exact matrix.

### 3.4 Cosets, JM, and the parent gauge

For every destination cell and all `i<64`, the reviewer checked the actual permutation equality

\[
 (i,64)r_d=l r_c h,\qquad l\in K,\quad h\in H.
\]

All `4*63=252` factorizations pass, `l` fixes the mark, `h` preserves each of the four original
cells, and `c` is the unique cell containing the marked preimage.  Normalized Frobenius
reciprocity gives the proposer's factor `sqrt(dim U_d/dim U_c)`; the listed dimensions are exactly
`225,225,15,15,15,210,15,15,15,210`.  With the isometric local embeddings, this constructs the
multiplicity matrix of the self-adjoint group-algebra element
`X_64=sum_(i<64)(i,64)`.

The parsed exact matrix is symmetric.  Independently, Young branching says that on the
`S^tau_*` child inside parent `S^nu`, `X_64` acts by the content of `nu/tau_*`.  The contents are
`61,1,-2`, with multiplicities `1,3,6`, so the expected characteristic polynomial is

\[
 (x-61)(x-1)^3(x+2)^6.
\]

The actual matrix has exactly this polynomial and satisfies the corresponding degree-three
minimal-polynomial identity entrywise.  Its three Lagrange projectors are exact symmetric
idempotents of ranks `1,3,6`, are mutually orthogonal, and sum to `I_10`.  The archived projectors
equal the reviewer-recomputed polynomials in JM.  The printed matrix `E` is exactly orthogonal and
satisfies

\[
 J E=E\operatorname{diag}(61,1,1,1,-2,-2,-2,-2,-2,-2).
\]

Thus `E` is an isometry from the ordered parent-multiplicity gauge to the ordered marked-Mackey
gauge.  The floating sign test mentioned in the verdict only replaces individual columns of `E`
by their negatives.

### 3.5 Point-child tables and normalization

In the marked-Mackey gauge, each of the six same-mark outcomes is an orthogonal coordinate
projector `D_chi`.  For a heavy branch its full local map has domain
`eta tensor V_16` of dimension `d_eta*15`, where `d_1=1` and `d_(V_15)=14`, and codomain
`S^tau_*` of dimension `1890`.  For a rare branch the domain has dimension `15^2=225`.

Schur's lemma turns the full-carrier Gram into a scalar on this local irreducible.  Dividing the
Hilbert--Schmidt trace by `d_eta*15` (or `15^2` for rare) leaves precisely the multiplicity
projector.  Because the harmonic embeddings were checked isometric, there is no extra carrier,
coset, or Specht-dimension factor.  Changing to the parent gauge gives the typed identity

\[
 C_\chi=E^T D_\chi E\in\operatorname{End}(\mathbb R^{10}).
\]

The reviewer reconstructed every table from this formula and compared every exact entry with the
fresh JSON.  The actual matrices, not the proposer's Boolean summary fields, satisfy:

* symmetry, idempotence, and ranks `(1,1,3,1,3,1)` in `A,B,L1,LV15,R1,RV15` order;
* all fifteen distinct products equal zero entrywise, hence all commutators equal zero;
* their sum is `I_10`;
* all three unordered parent-block pairs are nonzero in **each** of the six tables;
* the four printed radical witnesses agree exactly.

The cross-parent block ranks are:

| table | `(62,2)`--`(61,3)` | `(62,2)`--`(61,2,1)` | `(61,3)`--`(61,2,1)` |
|---|---:|---:|---:|
| `L,1` | 1 | 1 | 3 |
| `L,V15` | 1 | 1 | 1 |
| `R,1` | 1 | 1 | 3 |
| `R,V15` | 1 | 1 | 1 |
| rare `A` | 1 | 1 | 1 |
| rare `B` | 1 | 1 | 1 |

Thus the codiagonal conclusion is gauge-invariant at block level and does not rest on one chosen
entry.  Six nonzero pairwise-orthogonal projectors are linearly independent, so their unital
star-algebra has dimension six and is `C^6`.  Conjugating to the marked gauge makes its commutant
the direct sum of full matrix algebras on block ranks `1,1,3,1,3,1`; its dimension is therefore
`1+1+9+1+9+1=22`.

## 4. Rule-7(a): complete type audit

The scope has no free asymptotic parameter: `a=16`, `q=64`, `t=0` throughout.  The only
multiplicity parameter is the parent copy index `alpha=1,...,m_(0,nu)`, with all `1+3+6` values
retained.

| display | domain/codomain and dimension audit | verdict |
|---|---|---|
| (1.1) | `tau_* |- 63`; each listed `nu |- 64`; `nu/tau_*` is one box and the branching line `Hom_(S_63)(S^tau_*,S^nu downarrow)` is one-dimensional | PASS; closure exhaustive |
| (1.2) | `m_(0,nu)=dim Hom_(S_64)(S^nu,M_0)`; values `1,3,6` | PASS, including `c>1` |
| (1.3) | decomposition of `Y_tau=Hom_(S_63)(S^tau,Res M_0)`, dimension ten; local carrier dimensions are `225,225,15x3,210,15x3,210` before Schur reduction | PASS |
| (1.4) | characteristic polynomial of `J in End(Y_tau)`, a `10 x 10` self-adjoint matrix; the full isotypic operator is `I_1890 tensor J` on dimension `18900` | PASS |
| (1.5) | each displayed `C` is in `End(Y_tau)=M_10`; it is a multiplicity Gram, not a full occurrence/query operator | PASS |
| (2.1) | homogeneous degree-64 symmetric-function identity representing the `S_64` module `M_0` | PASS |
| (2.2) | for `lambda |- sum r_i`, both sides are integers; each `mu |- sum_(i<k)r_i` and `lambda/mu` is a horizontal `r_k` strip | PASS; broken `mathrm` token is typographical |
| (2.3) | homogeneous degree-63 characters of the marked `S_63` modules; `1` has dimension 1, `V_15` dimension 14, the untouched heavy standard dimension 15 | PASS |
| (2.4) | scalar multiplicity identity `13-9-9+6=1` | PASS |
| (3.1) | `S^(61,2)` and the harmonic kernel both have dimension 1890; permutation action relabels the 1953 edge coordinates | PASS |
| (3.2) | three vectors in a four-coordinate coefficient space with weighted metric `diag(14,16,16,15)` and one harmonic constraint; hence dimension three | PASS exact |
| (3.3) | ordered orthonormal basis of `Y_tau`, with ten multiplicity lines | PASS |
| (3.4) | identity in `S_64`; `r_c,r_d,h in S_64`, `h in H`, `l in K=S_63`; all 252 instances checked | PASS |
| (3.5) | scalar contents of the three one-box branching lines | PASS |
| (3.6) | `E:R^10_parent -> R^10_Mackey`, square orthogonal; columns split `1|3|6` | PASS |
| (4.1) | four displayed `D` matrices are `10 x 10` orthogonal projectors in the marked gauge; the two rare matrices occupy the other two coordinate lines | PASS |
| (4.2) | `E^T D E in End(R^10_parent)`; normalized full domains have dimensions `15`, `210`, or `225`, codomain dimension `1890` | PASS; divisor audited |
| (4.3) | scalar entries between specified columns of different parent blocks | PASS exact |
| (4.4) | identities in `End(R^10)` and scalar traces | PASS on actual matrices |
| (4.5) | resolution of identity in `End(R^10)` | PASS entrywise |
| (4.6) | products and commutators in `End(R^10)`; ranks are exact zero | PASS for all 15 pairs |
| (4.7) | unital star-subalgebra of `End(C^10)` generated by six nonzero orthogonal projectors | PASS; dimension six |
| (4.8) | commutant inside `End(C^10)` with block sizes `1,1,3,1,3,1` | PASS; dimension 22 |

No displayed conjugator is asserted to normalize an unrelated subgroup.  The only conjugations by
`r_c` transport the original Young subgroup to the correct marked-cell subgroup, while every `h`
used in (3.4) was checked to preserve all four original cells.

## 5. Rule-7(b): regime-complete identity gates

| regime in the stated claim | identity-level gate | result |
|---|---|---|
| parent multiplicity `c=1` | full `(62,2)` JM projector and all table rows/columns | PASS |
| parent multiplicity `c=3` | full `(61,3)` `3 x 3` diagonal block and both cross blocks | PASS |
| parent multiplicity `c=6` | full `(61,2,1)` `6 x 6` diagonal block and both cross blocks | PASS |
| rare `A`, rare `B` | actual rank-one `10 x 10` tables | PASS |
| left/right, `eta=1` | actual rank-three `10 x 10` tables | PASS |
| left/right, `eta=V15` | actual rank-one `10 x 10` tables | PASS |
| all fifteen same-mark table pairs | exact products and commutators | PASS |
| all three unordered old-parent pairs | exact nonzero block ranks in every table | PASS |
| distinct raw marks | excluded from claim; no gate | UNTESTED / NOT LICENSED |
| YES or any `a != 16` | excluded from claim; no gate | UNTESTED / NOT LICENSED |

Thus both `c=1` and `c>1` regimes are exercised at the full matrix-identity level, not merely by
traces or dimensions.

## 6. Rule-7(c)--(g)

### 6.1 Anchoring ban

The baseline was written before the proof was opened.  Its reverse-Pieri derivation and failure
predictions were independent.  The later reviewer checker uses a different conjugate-strip test.
Notation necessarily overlaps on canonical partitions and symmetric functions; no proposer matrix
formula was copied into the blind baseline.

### 6.2 No frozen-input immunity

The review re-opened every input at the granularity used here:

* the raw induced module and its Frobenius characteristic were rederived;
* the complete `c=1,3,6` parent closure was recomputed;
* the marked Mackey decomposition and local carrier dimensions were recomputed;
* the harmonic embeddings, all coset factorizations, JM self-adjointness, parent spectral
  projectors, and Schur normalization were rechecked.

Earlier complete-packet or cross-side reviews are not used to infer the finite same-side tables.

### 6.3 Failure-mode diversity

* **Dropped/extra normalization:** the local domains have dimensions `15`, `210`, and `225`; the
  normalized trace divisors and isometric embeddings were checked explicitly.
* **Type/dimension mismatch:** every display is typed above, including the full `1890 x 10`
  isotypic carrier behind the `10 x 10` multiplicity matrix.
* **Undefined terms/stability range:** `rare`, `heavy`, `same mark`, the groups, and the exact finite
  range are resolved in this report.  No word such as `admissible` or `taper` occurs.
* **Colored orbit versus central sum:** the six `C_chi` resolve one fixed marked raw letter.  They
  are not substituted for a sum over all raw marks.  Only JM uses the explicitly stated full sum
  `sum_(i<64)(i,64)`.
* **Values right/formula wrong:** two broken TeX tokens are called out despite all numbers passing.
  The exact formulas, group factorizations, and matrices were audited separately from the rerun.
* **Omitted parents/multiplicity lines:** the three-row parent and all six of its lines are present.
* **Gauge artifacts:** block ranks, projector relations, and algebra dimensions are invariant under
  allowed block-orthogonal parent gauge changes.
* **Same versus distinct mark:** distinct-mark projectors are explicitly withheld.

### 6.4 Value-versus-formula decoupling

The fresh JSON is a rerun of the proposer implementation, not a second implementation of the full
JM contraction.  It establishes reproducibility only.  Separately:

* character values come from the reviewer's independent conjugate-strip recurrence;
* all 252 group factorizations and sparse-map norm/harmonic gates are reviewer-side checks;
* a third mixed Schur vector probes the contraction formula;
* every matrix identity is recomputed from the actual exact printed matrices, ignoring the
  proposer's Boolean summary fields;
* the displayed derivation is audited analytically in Sections 3--4.

The proposer hardcodes no final JM or `C` matrix.  It does hardcode the three coefficient vectors,
parent specifications, and sector inventory; each of those inputs was independently derived and
checked here before its generated values were accepted.

### 6.5 Quantifier hygiene

The licensed quantifiers are literal and finite: one answer (`NO`), one parameter pair
`(a,q)=(16,64)`, one child `tau_*`, the complete three-parent closure, all ten multiplicity lines,
all six Mackey outcomes, and one common fixed raw mark.  `Rare` means the marked letter lies in
cell `A` or `B`; `heavy` means it lies in `L` or `R`; `same mark` means all six projectors use the
same point stabilizer `S_63`.  No asymptotic or physical-query term is left implicit.

## 7. Licensed and withheld conclusions

### Licensed

1. The complete active parent closure is `(62,2),(61,3),(61,2,1)` with NO multiplicities `1,3,6`.
2. The six same-mark Mackey ranks are `1,1,3,1,3,1` in `A,B,L1,LV15,R1,RV15` order.
3. The exact marked JM matrix is self-adjoint with characteristic polynomial
   `(x-61)(x-1)^3(x+2)^6`; its parent projectors and canonical gauge are exact.
4. All six same-mark `10 x 10` alphabet point-child tables are exact orthogonal projectors, sum to
   identity, and have nonzero blocks across every pair of old parents.
5. Their distinct products and commutators vanish; their generated star-algebra is `C^6` and its
   commutant has dimension `22`.

### Not licensed

1. Any relation between point-child projectors for two different raw marks.
2. Any YES table, any other `a` or `q`, or a uniform/asymptotic statement.
3. Any occurrence restriction, position-Pieri scalar, assembled physical Gram/pencil, attenuation,
   numerator, feasibility, query complexity, or exponent conclusion.
4. Completion or promotion of the broad occurrence-pencil classification node; it remains OPEN.
