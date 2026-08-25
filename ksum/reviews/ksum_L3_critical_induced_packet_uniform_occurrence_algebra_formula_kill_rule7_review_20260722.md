# Fresh hostile Rule-7 review — uniform critical-family occurrence multiplicity formula

Date: 2026-07-22  
Reviewer: fresh independent formula-level checker  
Controlling node:
`KSUM.B4b.L3.ALT.hidden-frequency-mask.critical-endpoint.ALT.induced-packet-occurrence-pencil-classification`  
Target artifact:
`ksum/artifacts/ksum_L3_critical_induced_packet_uniform_occurrence_algebra_formula_kill_20260722.md`

## 1. Formal verdict

**MINOR / STRICTLY SCOPED PASS.**

The review independently verifies, over characteristic zero and for every legal critical-family
integer `s>=4`,

\[
 \boxed{\dim\operatorname{Hom}_{S_d\wr S_a}
 (S^{(a-1,1)},S^{(ad-s-1,s,1)})
 =\sum_{j=0}^{s-2}p(j)},
 \qquad a=s^2,\quad d=4s+1.
\]

It also verifies `C_4=4`, `C_5=7`, and the first legal failure of the registered quadratic formula:

\[
 C_6=12\ne 11=1+\binom52.
\]

Therefore the registered **joint conjunction** is false and may be banked as refuted at this
formula scope. The broad controlling occurrence-pencil node remains `OPEN`: this review does not
classify any occurrence operator algebra or any physical/downstream object.

The minor is a scope/notation correction, not a defect in the multiplicity proof. The displayed
candidate writes `\mathbb Q^{,s-3}` and does not formally define whether `\mathcal A_s` denotes
only an abstract algebra or the observed multiplicity-free natural-module block decomposition.
Dimension `12` refutes the multiplicity conjunct and hence the conjunction. It also refutes the
intended exhaustive `3` scalar-line plus `8`-dimensional-complement **module** ansatz. It does not,
by dimension alone, refute a standalone abstract isomorphism
`Q^3 direct-sum M_8(Q)` acting with repeated simple-module multiplicities. The target correctly
withholds an actual `s=6` algebra classification; this review makes that boundary unambiguous.

## 2. Anchoring seal and independence

Before opening, grepping, hashing, or executing the proposer artifact, tool, JSON, log, checksum,
or updated canonical paragraphs, the reviewer:

1. read `DAG_PROTOCOL.md` and `research/RESEARCH_STRUCTURE_PROTOCOL.md` in full;
2. used only generic characteristic-zero group/Specht definitions and the already frozen reviewed
   `s=4`/`s=5` packages for notation and two finite consistency values;
3. derived the Jacobi--Trudi signs, both orbit catalogues, every stability inequality, and the
   partition-sum formula independently;
4. built and ran a stdlib-only exact checker that imports no proposer code; and
5. sealed the blind baseline at SHA-256
   `1D9CEA4E2B192C49B3F63254DD42FDAAE3F3233260B27497B42BF2683BC0AD7E`.

The post-seal derivation coincides with the proposer in the group notation `K,K_0`, the four
Jacobi--Trudi terms, and the final partition formula. That coincidence is explicitly flagged here;
the prior immutable hash and pre-target checker output establish that it was independently reached.

The sealed prose table contained hand-transcription errors in the non-load-bearing auxiliary fixed
dimensions for `s=7,9,10`. The formula, multiplicities, `s=4,5,6` rows, checker output, and first
obstruction were correct. The baseline remains byte-immutable and a post-seal erratum is archived
at SHA-256 `B6645980937B97A9309351AAE94DDE46A91E01771DC9E49409961C35F84EFB40`.

## 3. Independent derivation

Let `F` be a characteristic-zero field, `N=ad`,

\[
 H=S_d^a,\qquad K=H\rtimes S_a,\qquad K_0=H\rtimes S_{a-1},
\]

where `K_0` stabilizes one block, and inflate `V_a=S^(a-1,1)` from `S_a=K/H`.
The `K`-permutation module on blocks has the typed decomposition

\[
 \operatorname{Ind}_{K_0}^{K}{\bf1}\cong {\bf1}\oplus V_a,
 \qquad a=1+(a-1).
\]

Frobenius reciprocity therefore gives

\[
 \dim_F\operatorname{Hom}_{K}(V_a,S^\theta)
 =\dim_F(S^\theta)^{K_0}-\dim_F(S^\theta)^K.
\tag{3.1}
\]

For `theta=(N-s-1,s,1)`, direct determinant expansion gives the signs `+,-,-,+`:

\[
 s_\theta=h_{N-s-1}h_sh_1-h_{N-s-1}h_{s+1}
 -h_{N-s}h_{s-1}h_1+h_{N-s+1}h_{s-1}.
\tag{3.2}
\]

Write `p(r)` for the ordinary partition number, `p(0)=1`, and
`P_r=sum_(j=0)^r p(j)`. In the required low-tail range, the full-wreath orbit counts are

\[
 O_K(N-t,t)=p(t),\qquad O_K(N-t-1,t,1)=P_t.
\tag{3.3}
\]

For the block-stabilizer wreath subgroup they are

\[
 O_{K_0}(N-t,t)=P_t,
\qquad
 O_{K_0}(N-t-1,t,1)=\sum_{j=0}^t(t-j+2)p(j).
\tag{3.4}
\]

Equation (3.4) separates the singleton-in-block-zero case from the case where block zero and the
singleton's block have ordered occupancies. Applying (3.2) yields

\[
 \dim(S^\theta)^K=p(s-1)+p(s)-p(s+1),
\]

\[
 \dim(S^\theta)^{K_0}=P_s-p(s+1),
\]

and their difference is `P_(s-2)`. This agrees exactly with the target derivation.

## 4. Rule 7(a): complete type/dimension audit

There are no matrix/operator identities in the target. Every displayed representation, character,
and fixed-space identity was nevertheless typed as follows.

| Target displays | Domain/type and dimension audit |
|---|---|
| (1.1) | `C_s` is an integer. Interpreted safely, `A_s` is a unital `Q`-subalgebra of `End_Q(Z_s)`. The abstract direct-sum algebra does not itself encode multiplicities of its simple modules on `Z_s`; this is the minor scope correction above. |
| (1.2)--(1.4) | Equalities in `Z`; `p(j)` is the ordinary partition number. Exact addition gives `C_6=12`. |
| (2.1) | `a,d,M` are positive integers and `theta` is a partition of `M`; indeed `M>=2s+1` for all `s>=4`. |
| (2.2) | `K` is a subgroup of `S_M` acting on `a` blocks of size `d`; `|K|=(d!)^a a!`. `K_0` has order `(d!)^a(a-1)!`. |
| (2.3) | `V_a` and `S^theta` are finite-dimensional `Q[K]`-modules; the base group acts trivially on `V_a`. `Z_s=Hom_K(V_a,S^theta)` is a finite-dimensional `Q`-space. |
| (2.5) | Isomorphism of `Q[K]`-modules. The left side has dimension `[K:K_0]=a`; the right side has dimension `1+(a-1)=a`. |
| (2.6) | Equality of nonnegative integer dimensions obtained from `Hom_K(-,S^theta)` and Frobenius reciprocity; both fixed spaces lie in the same `S^theta`. |
| (3.1) | For a composition `mu` of `M`, `M^mu` is the `Q[S_M]` tabloid permutation module of dimension `M!/prod_i mu_i!`; its `L`-fixed dimension is the orbit count. Both symmetric functions in the inner product are homogeneous of degree `M`. |
| (3.2) | Equality in the degree-`M` symmetric-function/character ring. The `3 x 3` determinant has exactly the four surviving terms and signs `+,-,-,+`. |
| (3.3), (4.1)--(5.4) | Equalities of integer orbit counts or fixed-space dimensions. Every low-row composition sums to `M`; no map between unequal carriers is asserted. |

The characteristic-zero hypothesis is load-bearing for the character/Grothendieck subtraction and
semisimple multiplicity interpretation. No positive-characteristic claim is licensed.

## 5. Rule 7(b): regime-complete identity gates

The only qualitative regime is the stable low-tail regime used by the four Jacobi--Trudi terms.
The two-row counts require `0<=t<=s+1`; the three-row counts require `0<=t<=s`. The target leaves
these ranges implicit in Sections 4--5, which is the second local quantifier clarification of this
review. No formula outside these ranges is licensed.

For `a=s^2,d=4s+1,s>=4`, all required conditions hold uniformly:

- `d-1>=s`, so the singleton's block can hold the singleton and all `s` row-two points;
- `a>=s+1`, so every full-wreath occupancy partition needed here fits;
- `a-1>=s+1`, so the pointed two-row tail of size `s+1` fits outside block zero;
- `a-2>=s`, so the two-distinguished-block three-row case fits; and
- `ad>=2s+1`, so `theta` is a partition.

The target's stronger `a-2>=s+1` implies both pointed block-count requirements and is true for
every legal `s`. Thus there is no omitted boundary member, eventual-stability threshold, or
untested multiplicity branch. The proof is symbolic for all `s>=4`; finite rows are gates, not an
interpolation proof.

## 6. Rules 7(c)--(g)

### 7(c), anchoring

Satisfied by the pre-target seal and independent construction in Section 2. The notation/formula
coincidence is disclosed rather than treated as evidence of independence.

### 7(d), no frozen-input immunity

The frozen `s=4` and `s=5` packages are used only for the values `4` and `7`. Their operator-level
algebra reviews are not used to infer any all-`s` orbit formula. The new review reopens the group,
Jacobi--Trudi, fixed-space, capacity, and first-new-member calculations from scratch.

### 7(e), standing failure modes

- **Dropped/extra factors:** no Reynolds normalization is used; permutation fixed dimensions are
  orbit counts. The `a`-dimensional induction module decomposes as `1+(a-1)` with no missing factor.
- **Type/dimension mismatch:** all modules and character degrees are audited in Section 4. No raw
  bilinear form is multiplied as an endomorphism.
- **Undefined range:** `legal` resolves to `s>=4,a=s^2,d=4s+1`; the implicit `t` range is made
  explicit in Section 5. `A_s` receives only the safe scoped interpretation in Section 1.
- **Colored orbit substitution:** (3.3)--(3.4) classify actual `K` and `K_0` orbits on full
  tabloids. Distinguished blocks are part of the actual subgroup action, not surrogate colors.
- **Values with a broken printed derivation:** the review independently generates the determinant
  signs and bounded orbit counts; it does not accept agreement of the printed rows alone.

### 7(f), value versus formula

The proposer program evaluates the **same printed stable orbit formulas** and so is formula-coupled;
its finite output cannot independently verify the prose. The blind checker is a separate
construction: it generates the determinant signs, enumerates bounded integer partitions for the
actual `a,d` capacities, independently computes `p(j)` two ways, and then compares all eight orbit
counts. That construction agrees with every proposer row. This distinction is recorded in the
verdict.

### 7(g), quantifier hygiene

`p(j)`, `legal`, the critical family, `K`, `K_0`, `V_a`, `theta`, and the field are resolved. The
review explicitly restricts the auxiliary `t` formulas to the used low-tail range and withholds the
ambiguous standalone abstract-algebra reading of `A_s`. All `s>=4` claims are supported by uniform
inequalities rather than a finite sweep.

## 7. Exact comparison and provenance audit

Target hashes at review time:

| target file | SHA-256 |
|---|---|
| proposer artifact | `F28B00B328889BC1000B44A71B07D1648EF5108D1FA5E2E58D539B2B9D84655B` |
| proposer tool | `AB5FB57D3F00A79ACAFFD8E3AB00DB49EFC52A3671E522E7F29FB0C6B61C9E11` |
| proposer JSON | `81C355FDB2E079B79837B1313644BF32ADB9A5708C040A450C92C38FB9E05F0C` |
| proposer log | `60C796D0C729E849916703FEE664546B5BB70BE65BFF468EB93D82CE6D7A95A5` |
| proposer checksum package | `21F7DA054C88058E02EC8DF0C07D09F1EEF0FFD2628DD65F1897EC1F96E231D2` |

All four entries in the proposer checksum package rehash successfully. After blind comparison, the
proposer command was rerun to the review directory. The fresh JSON and log are byte-identical to
the archived proposer outputs.

Independent evidence hashes:

| review evidence | SHA-256 |
|---|---|
| independent checker | `4F2F773FC21C40F4CFA38C657C9787E446A4BB0FC857519D85FAE76618096582` |
| blind exact output | `F23DA59BBFEAB988AD397A553E5DE53D5F7F7BBB7F3A4B6F65021F9FC189CF4A` |
| blind exact log | `BC32C6BD7253FA556F9DD6918983EEF2E9C10E8E8E7B034DEF327B5E3BCC00DA` |
| fresh proposer JSON | `81C355FDB2E079B79837B1313644BF32ADB9A5708C040A450C92C38FB9E05F0C` |
| fresh proposer log | `60C796D0C729E849916703FEE664546B5BB70BE65BFF468EB93D82CE6D7A95A5` |
| post-seal comparison source | `6EACBE6FD5B561A32E9DB4B49566506C2750DC861FFC5B5613C4E233898E0728` |
| post-seal comparison JSON | `170F7571881F43B33B536CC674021673425ED6B9FBA92BCE76A7E2DFBD1D0F5F` |
| post-seal comparison log | `0161F2888EEB0CF59457A3D663A601824ACC73D5FE48ECD70C6F49A3B573A9D6` |

The two machine statuses are `ALL_INDEPENDENT_EXACT_GATES_PASS` and
`ALL_POSTSEAL_COMPARISON_GATES_PASS`.

The canonical node resolves uniquely through `NODE_INDEX.md`, has no status-propagating parents or
children, and remains `OPEN`; its pending-review language and proposer-tier provenance were
consistent at the freeze point. Per commission, this reviewer made no canonical/shared DAG edit.

## 8. Exact licensed and withheld scope

This review licenses only:

1. the characteristic-zero formula
   `C_s=sum_(j=0)^(s-2)p(j)` for `a=s^2,d=4s+1,s>=4`;
2. the fixed-space formulas used to derive it, in the explicit low-tail range;
3. agreement with the frozen reviewed finite values `C_4=4,C_5=7`;
4. the first legal quadratic obstruction `C_6=12` versus `11`;
5. formal refutation of the registered **joint** quadratic occurrence/algebra conjunction; and
6. impossibility of the intended multiplicity-free `3` scalar-line plus `8`-dimensional-complement
   carrier ansatz at `s=6`.

This review expressly withholds:

- a truth or falsity verdict on the standalone abstract-algebra isomorphism conjunct when module
  multiplicities are not specified;
- the actual `s=6` occurrence endomorphisms, commutant, invariant subspaces, splitting field,
  generated algebra, or any replacement decomposition;
- any uniform operator-algebra classification from the multiplicity formula;
- every alphabet, Pieri, physical assembly, NO/YES, transfer, feasibility, asymptotic, query,
  numerator, or exponent inference; and
- any promotion or status change of the broad controlling node, which remains `OPEN`.

No physical or downstream evidence was used to reach this verdict.
