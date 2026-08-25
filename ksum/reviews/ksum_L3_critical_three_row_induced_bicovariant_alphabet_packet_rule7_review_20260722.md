# Fresh Rule-7 review: induced bicovariant alphabet-packet first gate

Date: 2026-07-22  
Controlling node:
`KSUM.B4b.L3.ALT.hidden-frequency-mask.critical-endpoint.ALT.three-row-induced-bicovariant-alphabet-packet-kernel`  
Reviewed artifact:
`ksum/artifacts/ksum_L3_critical_three_row_induced_bicovariant_alphabet_packet_first_gate_20260722.md`  
Reviewed SHA-256:
`047CA5FEB7E4A5D27A687106F87F4BD1F838B68BF4695E79BE18B23EBBA1CC59`

## Verdict

**MINOR / SCOPED PASS.**  The subgroup-induced module, the two literal coset refinements, the
all-multiplicity isometries, the Schur-positive identity, the packet-width and multiplicity lower
bounds, the Johnson cross-Gram including normalization and multiplicities, the singular data, and
the marked `1/a+(a-1)/a` mass identities are correct for the artifact's stated algebraic scope

\[
 p=0,\qquad u=1,\qquad q=4a,\qquad a\ge2.
\]

They remain correct after tensoring by an explicitly stated common occurrence isometry, including
external occurrence ranks `c=1` and `c>1`.  The heavy-cell maps really are identities on the full
`V_a boxtimes V_a` fibers.  An exact all-full-type refinement of the printed result is

\[
 Z_{0,\nu}=\bigoplus_{j=0}^a \mathbb C^{c_{\nu,j}},\qquad
 c_{\nu,j}=[s_\nu]\,s_{(2a-j,j)}s_{(a-1,1)}^2,
 \tag{R.1}
\]

and

\[
 (J_L^*J_R)|_{S^\nu\otimes Z_{0,\nu}}
 =I_{S^\nu}\otimes
   \bigoplus_{j=0}^a\lambda_j I_{c_{\nu,j}},
 \qquad
 \lambda_j=1-\frac{j(2a-j+1)}{a^2}.
 \tag{R.2}
\]

Thus the conclusion is not anchored at multiplicity one: it covers every `c_(nu,j)>=0`, including
sectors with `c_(nu,j)>1` and full types containing several different Johnson degrees.

Two scope corrections are required.

1. At `u=1`, `J_L=A_L/a` and `J_R=A_R/a` are **formula-level identical** to the two immediate
   collision-split orbitals (up to swapping the orientation names).  General coefficients scalar
   in `j` belong to the support-quotiented Johnson algebra of outer UIC, so they are contained in
   the addressed-UIC architecture after the passive address lift.  They are not literally an
   arbitrary addressed `Gamma_UIC`, and nonconstant `j` coefficients were not covered by the old
   two-constant calculation alone.  The artifact's phrase “exactly the old Johnson/UIC
   mechanism” is valid only with this containment/quotient meaning.
2. `a=2` makes the internal heavy fiber `V_2 boxtimes V_2` one-dimensional; it does **not** make
   every full `S_8` multiplicity one.  The independent complete decomposition has 18 NO full
   types, maximum NO multiplicity 6, and ten full types meeting more than one Johnson sector.
   The printed lower bound “multiplicity at least `a-1`” is still correct; only a possible
   multiplicity-one reading is rejected.

The broad canonical claim asks for two `O(m^(-1/6))` query norms and a surviving growing
three-row numerator.  This first gate proves neither.  The node therefore remains **OPEN**; this
review licenses the scoped first-gate facts only and licenses no completion status, no REFUTED
disposition, and no downstream exponent claim.

## 1. Anchoring record and independent construction

I first read `DAG_PROTOCOL.md` and `research/RESEARCH_STRUCTURE_PROTOCOL.md` in full, then
read only the controlling node's `Claim`, `Role in DAG`, and `Dependencies`.  Before opening the
reviewed proof I reconstructed the following model from the frozen promise.

There is one provenance blemish that must not be hidden: a repository-wide term search intended to
locate baseline notation surfaced grep snippets containing the proposer's headline “Johnson”
conclusion before I opened its derivation.  I did not use or read the proof body at that point, but
this prevents calling my first pass perfectly answer-blind.  To restore a genuine anchoring check,
I also commissioned a no-context fresh instance that was forbidden to read or grep the proposer
artifact and asked it to derive the same coset map from the promise alone.  Its derivation agreed
with (R.3)--(R.9) below.  Independently, the archived checker constructs the two relations directly
from finite sets and never imports proposer formulas or data.  The agreement is therefore
construction-level, not a replay of the printed display.

My pre-proof construction used fine-cell order `(L,R,C,U,H_L,H_R)`, whereas the proposer later used
`(U,C,L,R,H_L,H_R)`.  The names `J_L,J_R` were fixed by the commission and the two orientation
names can be interchanged harmlessly; the relation, entries, and cross-Gram are invariant under
that rename.  The notation coincidence `A,B,H_L,H_R` comes from the frozen promise, not from the
proposer derivation.

Let `G=S_(4a)` and realize

\[
 V(H)=\{x\in\mathbb C^H:\sum_{z\in H}x_z=0\}\cong S^{(a-1,1)}.
\]

For an ordered NO palette partition `xi=(A,B,H_L,H_R)`, all four cells have size `a`.  Put

\[
 \mathcal M_0=
 \bigoplus_\xi V(H_L)\otimes V(H_R)
 \cong\operatorname{Ind}_{S_a^4}^{S_{4a}}
   (1\boxtimes1\boxtimes V_a\boxtimes V_a).
 \tag{R.3}
\]

For an ordered YES partition `eta=(L,R,C,U,H_L,H_R)` with cell sizes
`a-1,a-1,1,1,a,a`, put

\[
 \mathcal M_1=
 \bigoplus_\eta V(H_L)\otimes V(H_R).
 \tag{R.4}
\]

The dimensions are

\[
 d_0=\frac{(4a)!}{(a!)^4}(a-1)^2,
 \qquad d_1=a^2d_0.
 \tag{R.5}
\]

In the canonical bundle basis, with `v in V(H_L) tensor V(H_R)`, the two physical refinements are

\[
 \begin{aligned}
 J_L|A,B,H_L,H_R;v\rangle
 &=\frac1a\sum_{c\in A}\sum_{u\in B}
 |A-c,B-u,C=c,U=u,H_L,H_R;v\rangle,\\
 J_R|A,B,H_L,H_R;v\rangle
 &=\frac1a\sum_{u\in A}\sum_{c\in B}
 |A-u,B-c,C=c,U=u,H_L,H_R;v\rangle.
 \end{aligned}
 \tag{R.6}
\]

Each column has `a^2` mutually orthogonal fine states and each fine state has a unique coarsening
of either orientation.  Hence both maps are `G`-equivariant isometries
`M_0 -> M_1`.  The displayed `v` is unchanged.  This is a literal identity on both heavy standard
fibers, not a scalar inferred from their dimensions and not a hidden normalizer action.

A fine state in a left column `(A,B)` is in one right column, namely

\[
 (A',B')=(A-c+u,B-u+c).
\]

Therefore

\[
 \langle A',B';w|J_L^*J_R|A,B;v\rangle
 =\frac1{a^2}
  1_{\{|A\cap A'|=a-1\}}
  1_{H_L'=H_L,H_R'=H_R}\langle w,v\rangle.
 \tag{R.7}
\]

For fixed `T=A union B` and fixed ordered heavy cells, this is the degree-`a^2` Johnson adjacency
on `J(2a,a)`, divided by `a^2`, tensored with `I_(a-1)^2`.  Its eigenvalue and one-fiber
multiplicity at degree `j` are

\[
 \lambda_j=\frac{(a-j)^2-j}{a^2},\qquad
 d_j={2a\choose j}-{2a\choose j-1},\qquad 0\le j\le a.
 \tag{R.8}
\]

Globally `d_j` is repeated

\[
 R_a(a-1)^2,
 \qquad R_a=\frac{(4a)!}{(2a)!(a!)^2},
 \tag{R.9}
\]

times.  Induction in stages through
`S_(2a) x S_a x S_a` gives (R.1)--(R.2), so the formula covers the full multiplicity spaces rather
than only aggregate traces.

Only after fixing (R.3)--(R.9) did I read the proposer artifact in full and compare displays.

## 2. Subgroup induction, characters, width, and multiplicity

### 2.1 The characteristic identity comes from an actual subgroup map

For either physical orientation the fine subgroup is contained in the coarse subgroup, pairing
`S_(a-1) x S_1` inside each rare `S_a`.  Induction in stages gives

\[
 \operatorname{Ind}_{S_{a-1}\times S_1}^{S_a}1
 \cong1\oplus V_a
\]

as an orthogonal unitary `S_a`-module.  Thus

\[
 M_1\cong\operatorname{Ind}_{S_a^4}^{S_{4a}}
  ((1\oplus V_a)\boxtimes(1\oplus V_a)\boxtimes V_a\boxtimes V_a),
 \tag{R.10}
\]

and its trivial/trivial rare-cell summand is the concrete image of `J_L` (or of `J_R` for the
other subgroup inclusion).  Taking Frobenius characteristics yields

\[
 h_1h_{a-1}=h_a+s_{(a-1,1)},\qquad
 F_1=F_0+2h_as_{(a-1,1)}^3+s_{(a-1,1)}^4.
 \tag{R.11}
\]

This proves coefficient positivity and the physical rectangular isometry separately.  No
coefficientwise inequality is being mistaken for a map.

For every `nu` let `m_(t,nu)=[s_nu]F_t`.  Equivariance and isometry give

\[
 J_o=\bigoplus_\nu I_{S^\nu}\otimes j_{o,\nu},
 \quad
 j_{o,\nu}:\mathbb C^{m_{0,\nu}}\hookrightarrow
             \mathbb C^{m_{1,\nu}}.
 \tag{R.12}
\]

This is well typed even when `m_(0,nu)>1` and `m_(1,nu)>m_(0,nu)`.

### 2.2 Width and growing multiplicity

The printed Pieri expansion

\[
 h_a^2=\sum_{j=0}^a s_{(2a-j,j)}
\]

is exact.  Direct LR-tableau enumeration independently confirms that
`s_(a-1,1)^2` contains `(2a-2-k,k+2)` for every `0<=k<=a-2`.  Adding highest weights gives
the `2a-1` distinct partitions

\[
 (4a-r-2,r+2),\qquad0\le r\le2a-2.
\]

At `r=a-1`, the `a-1` distinct pairs
`(j,k)=(1,a-2),...,(a-1,0)` contribute positively to the same full type
`(3a-1,a+1)`.  Therefore the printed lower bounds `width>=2a-1` and
`multiplicity>=a-1` are correct.  They are lower bounds, not exact packet statistics.

## 3. Per-display type audit

Write `D=a-1`, `d_0=dim M_0`, `d_1=a^2d_0`, and `f^nu=dim S^nu`.

| proposer display | domain -> codomain and dimensions | audit |
|---|---|---|
| (2.4), (2.7) | `M_0` and `M_1` are unitary `G`-modules of dimensions `d_0,d_1` | PASS; stabilizer representations are explicit |
| (3.4) | `Ind_(S_(a-1)xS_1)^(S_a) 1 -> 1 direct-sum V_a`, both dimension `a` | PASS; actual subgroup induction |
| (3.5) | unitary `G`-module isomorphism; summand dimensions add to `d_1` | PASS |
| (3.6) | `J_L,J_R:M_0 -> M_1`, rectangular `d_1 x d_0` | PASS; coefficient `1/a`, unique coarsening |
| (3.7) | `J_o^*J_o:M_0 -> M_0`, `d_0 x d_0` | PASS, exact identity |
| (3.8)--(3.9) | `j_(o,nu):C^(m_(0,nu))->C^(m_(1,nu))`; full block is `f^nu m_(1,nu)` by `f^nu m_(0,nu)` | PASS for every `nu`, including unequal ranks and all multiplicities |
| (5.2) | `K=J_L^*J_R:M_0 -> M_0` | PASS; entries (R.7), heavy fibers `I_D tensor I_D` |
| (5.7) | both sides are endomorphisms of `M_0` | PASS because `K=K^*` |
| (5.8) | singular data of maps `M_0 -> M_1` | PASS; follows from the complete spectrum, including `a=2` |
| (6.1) | `Q_YJ_o` and `J_oP_X` are maps `M_0 -> M_1`; each `P_X` is on `M_0`, each `Q_Y` on `M_1` | PASS; literal cell projectors, not full-parent pinches |
| (6.2) | `J_o^*Q_YJ_o:M_0 -> M_0` | PASS; exact effects `1/a` and `(a-1)/a` |
| occurrence extension | `J_o tensor R:M_0 tensor C^(c_0) -> M_1 tensor C^(c_1)` for an isometry `R:C^(c_0)->C^(c_1)`, requiring `c_0<=c_1` | PASS on the stated common rank; no claim on the unmatched codomain complement |
| (7.1) | `A_L,A_R:C^(X_0)->C^(X_1)` are `d_1 x d_0` zero-one orbitals at `u=1`; `J_o=A_o/a` | PASS, up to orientation-name swap |
| (7.2) | masked rectangular maps; changed orientation norm `1/sqrt(a)`, unchanged orientation zero | PASS for the immediate relation |
| (8.1)--(8.3) | proposed occurrence endomorphisms/coefficients are not fully typed because actual edges, pencils, and face spaces are deliberately undefined | NOT A CLAIM; the artifact correctly labels them registrations and does not use them in the verdict |

For an external common occurrence isometry `R`, the cross-Gram is

\[
 (J_L\otimes R)^*(J_R\otimes R)=K\otimes I_{c_0}.
\]

If the two orientations used different occurrence maps `R_L,R_R`, the correct expression would be
`K tensor R_L^*R_R`; the artifact does not claim otherwise.

## 4. Exact independent gates

Checker: `ksum/tools/ksum_l3_induced_packet_rule7_check.py`  
Checker SHA-256: `446731984000E37013B5C43472AB9C95C175749D16141AF29A674D7FBDCB72CC`  
Raw log: `ksum/artifacts/logs_ksum_L3_induced_packet_rule7_20260722/run.log`  
Raw-log SHA-256: `EBB2F426A678719A66674DDA63A81E5B67D5C57318BA1AE5D1812A9368B782FC`  
Manifest: `ksum/artifacts/logs_ksum_L3_induced_packet_rule7_20260722/SHA256SUMS.txt`

The checker uses exact integer incidence Grams, exact SymPy characteristic polynomials, and direct
LR-tableau enumeration.  It runs the following identity-level regimes.

1. `a=2,c=1`; `a=2,c=2`; `a=3,c=1`; `a=3,c=2`.
2. Both `J_L` and `J_R`, their two self-Grams, the full entrywise cross-Gram, and every fixed-point
   marked map/effect identity for both rare cells and all four fine cells.
3. The full `V_a boxtimes V_a tensor C^c` fiber.  Every same-fiber entry is copied and every
   different-fiber Gram is zero.  At `a=3,c=2` this is an eight-dimensional internal fiber, so the
   gate is not a one-dimensional proxy.
4. Every full `S_8` and `S_12` type, every `m_(0,nu),m_(1,nu)`, and every `c_(nu,j)` sector.  The
   exact dimension sums recover `dim M_0` and `dim M_1`.
5. A deliberate outside-scope gate `a=2,u=2`.  It finds off-diagonal entries in
   `A_L^*A_L` and both fixed-unused-cell swaps and changed-unused-cell three-cycles in
   `A_L^*A_R`, proving that the `u=1` isometry/Johnson formula is not silently being extrapolated.

Selected exact outputs are:

| regime | exact result |
|---|---|
| `a=2` | `spec(K)={1^1,0^3,(-1/2)^2}` per Johnson fiber; marked masses `1/2,1/2` |
| `a=3` | `spec(K)={1^1,(1/3)^5,(-1/9)^9,(-1/3)^5}` per Johnson fiber; marked masses `1/3,2/3` |
| full `S_8` packet | 18 NO full types, max `m_(0,nu)=6`, ten types with multiple `j` sectors |
| full `S_12` packet | 54 NO full types, max `m_(0,nu)=32`, 44 types with multiple `j` sectors |
| `u=2` scope guard | row degree 2, column degree 4; `A_L/a` not an isometry; cross-Gram not pure Johnson |

The checker verifies both an independent construction of the objects and the proposer's printed
formulas.  Agreement of independently constructed values corroborates the claim but would not by
itself verify the printed derivation; Sections 1--3 separately check the subgroup maps and every
displayed operator identity.

## 5. Johnson spectrum, singular values, and marked mass

The standard Johnson eigenvalue `(a-j)^2-j` and multiplicity
`binom(2a,j)-binom(2a,j-1)` give the printed normalized spectrum.  The eigenvalues are strictly
decreasing in `j`, so there is no hidden degeneracy between distinct degrees.  The bottom value is
`lambda_a=-1/a` and `lambda_1=1-2/a`.  Consequently

\[
 (J_L\pm J_R)^*(J_L\pm J_R)=2(I\pm K)
\]

has exactly the printed data:

* `||J_L+J_R||=2` and its smallest singular value is `sqrt(2(1-1/a))`;
* `J_L-J_R` kills `j=0`, has smallest nonzero singular value `2/sqrt(a)` at `j=1`, and norm
  `sqrt(2+2/a)` at `j=a`.

For each palette point `z`, direct counting gives

\[
 J_L^*Q_C(z)J_L=\frac1aP_A(z),\qquad
 J_L^*Q_L(z)J_L=\frac{a-1}{a}P_A(z),
\]

and the other six orientation/cell identities by symmetry.  These are effects on `M_0`, whereas
`Q_CJ_L` and `Q_LJ_L` are maps into orthogonal fine-cell subspaces of `M_1`; the artifact does not
confuse the map with its squared mass.  Their sum is exactly `P_A`, so retaining only the
singleton branch loses real physical mass.

The point projectors commute only with the marked `S_(q-1)`, not with `S_q`.  Therefore it is
illegal to append the old full-parent name as an orthogonal superselection tag after the query.
Conversely, the unmarked `J_o` is `S_q`-equivariant and never maps inequivalent full irreps.  The
artifact uses the two symmetry levels correctly.

## 6. Exact baseline comparison and its limits

### 6.1 Immediate two-orientation baseline

At `u=1`, a YES fine palette has one unused label.  Coarsening it in either orientation is unique;
therefore each zero-one relation `A_L,A_R` has row degree 1 and column degree `a^2`, norm `a`, and

\[
 J_L=A_L/a,\qquad J_R=A_R/a
\]

exactly.  This is formula-level equality of relations, not merely spectral similarity.  Hence the
constant-coefficient sum/contrast is exactly the earlier two-orbital law.

For coefficients depending on Johnson degree, induction in stages shows that the full scalar
support algebra is generated by the `a+1` spectral projectors of `K`.  Lifting constantly over the
ordered position/address fibers embeds this algebra into the outer UIC adversary space.  This
proves **containment in the support-quotiented Johnson/UIC architecture**.  It does not identify
`J_L f(K)+J_R g(K)` with every addressed `Gamma_UIC`; the latter may depend on ordered addresses
and is strictly more general.  It also does not mean the prior two-constant norm calculation
already optimized arbitrary `f,g`.

Thus the review confirms the proposer's scalar-novelty failure in the following exact sense:
support-only scalar Johnson-degree laws are not a new architecture beyond UIC.  Any statement
about their asymptotic adversary value must use the independent UIC theorem/upper bound; it is not
inferred from the finite gates here.  No nonseparable packet/occurrence coefficient is covered.

### 6.2 `u>1`, `p>0`, and the rest of the frozen family

For `u>1`, write the NO unused cell as `W`, `|W|=u-1`.  A fine unused cell is `U=W union {z}`.
A fine row has `u` possible coarse predecessors, so the columns of the immediate incidence overlap.
`A_o/a` is no longer an isometry.  Moreover the cross-Gram contains both an `A<->B` swap with
`W` fixed and a three-cell move `A -> B -> W -> A`.  It is not the single Johnson walk (R.7).

For `p>0`, the two heavy-frequency classes have different multiplicities and the exact heavy
stabilizer is refined; the `S_a` standard fiber used in (R.3) is no longer the stated exact
stabilizer type without a new restriction calculation.  Therefore this review covers neither
regime.  It also does not assert that every critical integer `(N,q)` realizes `p=0,u=1`; it checks
the algebraic subfamily whenever those equalities hold.

### 6.3 The `q=5` shared-NO cascade

At `q=5`, the frozen parameter is `a=1`, so `dim V_a=a-1=0` and this bicovariant packet is absent.
The proved shared-NO construction instead lives in a signed central histogram/moment space on
reflected slot totals and obtains a high-`C_t` tail by barycentric cancellation.  It is not a
Fourier realization of (R.6), and no formula, norm, correlation, or endpoint conclusion transfers
between them.  The only analogy is that two orientations share a coarse object and their contrast
kills a constant component.

## 7. Standing failure-mode audit

* **Dropped/extra normalization:** PASS.  `a^2` refinements force `1/a`, not `1/a^2` or
  `1/sqrt(a)`.  Cross entries are `1/a^2`.  Global spectral multiplicities include the repetition
  factor (R.9).
* **Type/dimension mismatch:** PASS in the scoped module.  All rectangular maps, unequal
  multiplicities, adjoints, projectors, internal fibers, and external occurrence ranks are typed
  in Section 3.
* **Undefined terms/stability ranges:** PASS after the definitions in Section 8.  There is no
  unstated asymptotic stability threshold in the finite alphabet gate.  “Growing” applies only to
  the lower bound as `a` varies and gives no growth conclusion at the isolated value `a=2`.
* **Colored orbit substituted for a full central sum:** PASS.  The local Johnson block is induced
  over every choice of union and ordered heavy cells.  Formula (R.2) is `G`-equivariant on the full
  induced module; the fixed-color computation is only one identical fiber, not the definition of
  a noncentral replacement.
* **Numerics validate values while the printed derivation is broken:** PASS.  The subgroup
  inclusions, induction in stages, LR witnesses, and exact entry calculation were audited
  analytically.  Numerical/exact finite gates are corroboration and regime tests only.
* **Parent tag as false superselection:** PASS.  Marked projectors are literal `S_(q-1)` effects;
  no full-parent pinching is inserted.
* **Literal map/effect confusion:** PASS.  `QJ` and `J^*QJ` have different types and are treated
  separately.
* **Multiplicity-one anchoring:** PASS after the stated minor clarification.  Formula (R.2) and the
  checker cover every `c_(nu,j)`, including `c_(nu,j)>1`; `a=2` is not globally multiplicity one.
* **Illegal cross-irrep map:** PASS.  Unmarked maps are `G`-intertwiners and block diagonal in
  `nu`; only physical marked restriction may join common `S_(q-1)` children.
* **Frozen-input immunity:** no prior Johnson or LR review is load-bearing here.  Both were
  rederived.  The prior two-box `1/(2a)` truncation is context only and is not licensed or
  re-reviewed by this verdict.  The UIC comparison was reopened at formula-versus-containment
  level.  The `q=5` review is used only to identify its different typed space.

## 8. Quantifier and terminology hygiene

* **Complete packet:** the entire concrete module `M_0` in (R.3), embedded by one of (R.6); it is
  not a hand-selected set of full types.
* **Common multiplicity:** every one of the `m_(0,nu)` domain copies maps isometrically into the
  `m_(1,nu)` codomain copies.  It does not claim equality of NO/YES multiplicities or control of
  the unmatched YES complement.
* **Physical orientation:** one of the two actual subgroup refinements pairing `C,U` with the two
  rare cells.  It is not an arbitrary phase convention.
* **Internal `V_a` identity:** the same vectors in `V(H_L) tensor V(H_R)` are carried to the fine
  state with unchanged heavy cells.  After full Fourier decomposition, `K` is (R.2), not a single
  scalar on all of `Z_(0,nu)`.
* **External occurrence rank `c`:** the dimension of an additional common occurrence space.  It is
  distinct from `D=a-1`, from `m_(t,nu)`, and from `c_(nu,j)` in (R.1).
* **Scalar Johnson degree:** a coefficient scalar on each intermediate
  `S^(2a-j,j)` sector and passive on every occurrence/internal channel.  It may vary with `j`.
* **Baseline equivalence:** exact relation equality for `J_L,J_R`; containment/quotient equivalence
  for arbitrary scalar `j` laws; not equality to an arbitrary addressed UIC adversary.
* **Legal range:** all algebraic identities hold for every integer `a>=2` in the exact
  `p=0,u=1,q=4a` quotient.  `a=2` is a valid finite alphabet gate but supplies no asymptotic
  “growing” statement by itself.  No claim is made for `a=1`, `u>1`, `p>0`, all critical `(N,q)`,
  or the broad node's query/numerator obligations.

## 9. Rule-7(a)--(g) ledger

| rule | result |
|---|---|
| 7(a) type audit | PASS, Section 3; all displayed operator identities, unequal ranks, internal fibers, and full multiplicities typed |
| 7(b) regime-complete identity gates | PASS for the scoped claim: `a=2,3`, `c=1,2`, L/R, NO/YES, singleton/residual, all `S_8/S_12` full-type sectors; explicit `u=2` nonextension gate |
| 7(c) anchoring ban | PASS with disclosed search-snippet blemish and a separate no-context blind derivation; construction fixed before full proposer proof, notation coincidence recorded |
| 7(d) no frozen-input immunity | PASS; Johnson, Pieri/LR, UIC comparison, and multiplicity use reopened; two-box facts excluded from the verdict |
| 7(e) failure-mode diversity | PASS, Section 7 |
| 7(f) value-vs-formula decoupling | PASS, Section 4; independent object values and printed derivation adjudicated separately |
| 7(g) quantifier hygiene | PASS after the explicit definitions and scope cuts in Section 8 |

## 10. Disposition

The reviewed first-gate artifact receives **MINOR / SCOPED PASS**.  The MINOR points are the needed
UIC formula-versus-containment wording and the warning that one-dimensional `V_2 boxtimes V_2`
does not imply one-dimensional full-type multiplicity spaces.  Neither changes the exact subgroup,
cross-Gram, spectrum, marked-mass, width, or lower-bound formulas.

The canonical node remains **OPEN** because the first gate does not construct legal
packet/occurrence coefficients with both claimed query bounds and a surviving numerator.  The
review does not test or authorize the three registered nonseparable continuations and does not
infer any asymptotic exponent from the finite gates.
