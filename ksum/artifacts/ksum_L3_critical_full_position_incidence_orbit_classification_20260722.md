# L3 critical endpoint: full pair position-incidence orbit classification

Date: 2026-07-22  
Canonical scope:
`KSUM.B4b.L3.ALT.hidden-frequency-mask.critical-endpoint.ALT.full-position-incidence-three-layer-word-kernel`  
Verdict: **exact structural classification on the legal `p=0,u=1` subsequence; genuine new
joint orbit data beyond the two address maps, but the full family is still a colored
transportation/Young-Hecke bimodule; no adversary or exponent claim**  
Status discipline: proposer-tier analytic work; no canonical-node or ancestor edit; independent
review pending

## 1. Verdict

On the decisive `p=0,u=1` subsequence, the full colored graph `D(x_1,x_0)` has a smaller exact
description than the two-copy graph with an equality matching.

1. Merge the two label copies along the raw-label equality matching.
2. On the resulting common palette of `q=4a` vertices, record two nonnegative integer matrices
   `C_L,C_R`.  The entry `C_s(v,w)` is the number of physical side-`s` positions whose YES label
   is `v` and whose NO label is `w`.
3. Quotient the pair `(C_L,C_R)` by simultaneous permutation of palette vertices having the same
   YES/NO type pair.

The resulting joint permutation orbit is a minimal complete invariant.  Equivalently, before
merging the equality matching it is a transportation-table triple

\[
 (E,C_L,C_R),
\tag{1.1}
\]

where `E` records how the YES and NO label-type partitions meet.  At `d>=2`, `E` is recoverable
from the four row/column degree vectors of `C_L,C_R`, so the joint orbit of the matrix pair alone
is complete.

This data is **not** determined by the repaired singleton matching, the heavy/address matching,
their two input-wise relative maps, or the two repair endpoints.  A two-heavy-label family with
block

\[
 C_L^{(k)}=
 \begin{pmatrix}k&d-k\\ d-k&k\end{pmatrix},
 \qquad 0\le k\le d,
\tag{1.2}
\]

holds all of that old data fixed while producing distinct full position-incidence orbits.
Normalized address incidence does not erase (1.1): it is constant on every pair of presentation
fibers and therefore pulls exactly through `R_1(\cdot)R_0^*`.

There is nevertheless no new algebraic species outside fixed multipliers.  Each side matrix is a
fixed-middle Gram relation

\[
 G_s=F_{1,s}^*I_{[n]}F_{0,s},
\tag{1.3}
\]

and arbitrary scalar functions or joint `L/R` words in the full invariant form the rectangular
colored Young-Hecke bimodule

\[
 e_{K_1}\,\mathbb C[G]\,e_{K_0}.
\tag{1.4}
\]

Polynomial words are fixed partition-diagram multipliers on tensor powers; an arbitrary function
is a fixed multiplier in the regular orbital decomposition.  Thus the proposed third layer is
genuinely larger than the previously audited two-matching convolution algebra, but it is still a
standalone full-occurrence partition/Hecke system.

This observation does **not** import the earlier fixed-middle partial-trace ceiling.  A physical
query points one occurrence edge and deletes precisely the marked types lying on the equality
matching.  The marked multiplier is therefore an off-equality one-point extension of (1.4), not
the same middle operator copied into every marked branch.  Signed cancellation between unmarked
orbitals while all off-equality marked blocks remain small is structurally possible and is exactly
the still-open adversary obligation.  No coefficient achieving it is supplied here.

## 2. Exact `p=0,u=1` types

Take the infinite legal subsequence

\[
 a=k^2,\qquad q=4k^2,\qquad d=k,\qquad m=d+1,
 \qquad n=a(d+1)=am,
\tag{2.1}
\]

so

\[
 p=(n-a)-ad=0,\qquad u=q-4a+1=1.
\tag{2.2}
\]

Let `Omega_t` be the label-copy set for answer class `t`.  Both have size `q=4a`.  The YES type
set and sizes are

\[
 \mathcal T_1=\{U,C,L_1,R_1,L_d,R_d\},
\qquad
 (n_{1,\alpha})_{\alpha\in\mathcal T_1}
 =(1,1,a-1,a-1,a,a),
\tag{2.3}
\]

where `U` is unused and `C` is the unique label used once on each side.  The NO type set and
sizes are

\[
 \mathcal T_0=\{L_1,R_1,L_d,R_d\},
\qquad
 (n_{0,\beta})_{\beta\in\mathcal T_0}=(a,a,a,a).
\tag{2.4}
\]

For `s in {L,R}`, write `r^t_s(v)` for the side multiplicity of label `v`.  The complete table is

\[
\begin{array}{c|rrrrrr}
 \alpha\in\mathcal T_1&U&C&L_1&R_1&L_d&R_d\\ \hline
 r^1_L(\alpha)&0&1&1&0&d&0\\
 r^1_R(\alpha)&0&1&0&1&0&d
\end{array},
\tag{2.5}
\]

\[
\begin{array}{c|rrrr}
 \beta\in\mathcal T_0&L_1&R_1&L_d&R_d\\ \hline
 r^0_L(\beta)&1&0&d&0\\
 r^0_R(\beta)&0&1&0&d.
\end{array}
\tag{2.6}
\]

Each side has

\[
 \sum_{v\in\Omega_t}r^t_s(v)=a+ad=n.
\tag{2.7}
\]

The exact stabilizer has the typed wreath-product form

\[
 K_t=
 \left[
   \prod_{v\in\Omega_t}
   \bigl(S_{r^t_L(v)}\times S_{r^t_R(v)}\bigr)
 \right]
 \rtimes
 \left[
   \prod_{\gamma\in\mathcal T_t}S_{n_{t,\gamma}}
 \right].
\tag{2.8}
\]

The first bracket permutes occurrences inside one label fiber, separately on the two physical
sides.  The second permutes whole labels of the same joint type together with their occurrence
fibers.  Trivial `S_0,S_1` factors are understood.  Formula (2.8) is the `p=0,u=1` specialization
of the stabilizers used in `X_t=G/K_t` for

\[
 G=S_n^{(L)}\times S_n^{(R)}\times S_q.
\tag{2.9}
\]

## 3. Typed occurrence maps and the fixed-middle Gram relation

Let `P_s=[n]_s` be the physical position set on side `s`.  For an input `x_t`, define its label
map

\[
 b_{t,s}:P_s\longrightarrow\Omega_t.
\tag{3.1}
\]

The raw label-position incidence operator is

\[
 B_{t,s}:\mathbb C^{P_s}\longrightarrow\mathbb C^{\Omega_t},
 \qquad
 B_{t,s}[v,i]={\bf1}[b_{t,s}(i)=v].
\tag{3.2}
\]

Its dimensions are `q x n`, and

\[
 B_{t,s}B_{t,s}^*=D_{t,s},
 \qquad
 D_{t,s}=\operatorname{diag}(r^t_s(v):v\in\Omega_t).
\tag{3.3}
\]

Let `Omega^+_(t,s)={v:r^t_s(v)>0}`.  It has size `2a` for every `t,s`.  On that positive-degree
space define the isometry

\[
 F_{t,s}=B_{t,s}^*D_{t,s}^{-1/2}:
 \mathbb C^{\Omega^+_{t,s}}\longrightarrow\mathbb C^{P_s}.
\tag{3.4}
\]

For a YES/NO pair, the raw side-contingency map and its normalized version are

\[
 C_s=B_{1,s}B_{0,s}^*:
 \mathbb C^{\Omega_0}\longrightarrow\mathbb C^{\Omega_1},
\tag{3.5}
\]

\[
 G_s=D_{1,s}^{-1/2}C_sD_{0,s}^{-1/2}
 =F_{1,s}^*I_{\mathbb C^{P_s}}F_{0,s}:
 \mathbb C^{\Omega^+_{0,s}}\longrightarrow
 \mathbb C^{\Omega^+_{1,s}}.
\tag{3.6}
\]

Entrywise,

\[
 C_s(v,w)=
 |\{i\in P_s:b_{1,s}(i)=v,\ b_{0,s}(i)=w\}|,
\tag{3.7}
\]

so

\[
 \sum_wC_s(v,w)=r^1_s(v),
 \qquad
 \sum_vC_s(v,w)=r^0_s(w).
\tag{3.8}
\]

Equation (3.6) makes the two statements that must not be conflated precise:

* `G_s` is joint YES/NO data and is not determined by either input's address map;
* at the linear carrier level it is a fixed-middle Gram matrix of two input-wise occurrence
  embeddings.

An equivalent occurrence-token description exposes all multiplicities.  Put

\[
 \mathcal O_{t,s}
 =\bigsqcup_{v\in\Omega_t}\{v\}\times[r^t_s(v)],
 \qquad |\mathcal O_{t,s}|=n,
\tag{3.9}
\]

and choose a bijection `eta_(t,s):mathcal O_(t,s)->P_s` compatible with `b_(t,s)`.  Physical
position equality induces

\[
 \Pi_s=\eta_{1,s}^{-1}\eta_{0,s}:
 \mathcal O_{0,s}\longrightarrow\mathcal O_{1,s}.
\tag{3.10}
\]

The internal occurrence groups

\[
 W_{t,s}=\prod_{v\in\Omega_t}S_{r^t_s(v)}
\tag{3.11}
\]

act by `Pi_s -> w_(1,s) Pi_s w_(0,s)^(-1)`.  The double coset of `Pi_s` is exactly the table
`C_s`.  For fixed labeled margins, the number of occurrence bijections in that double coset is

\[
 {\displaystyle
   \prod_v r^1_s(v)!\prod_w r^0_s(w)!
  \over
  \displaystyle\prod_{v,w}C_s(v,w)!},
\tag{3.12}
\]

because the intersection stabilizer has order `prod_(v,w) C_s(v,w)!`.

## 4. Minimal complete orbit invariant

Before choosing a common palette gauge, let

\[
 M:\Omega_0\longrightarrow\Omega_1
\tag{4.1}
\]

be the raw-label equality matching.  Its type-intersection table is

\[
 E_{\alpha\beta}
 =|\Omega_{1,\alpha}\cap M(\Omega_{0,\beta})|,
 \qquad
 \alpha\in\mathcal T_1,\ \beta\in\mathcal T_0.
\tag{4.2}
\]

The margins of `E` are (2.3)--(2.4).  Let `mathcal E` be the finite set of all such tables.  For
one `E`, identify `Omega_0` with `Omega_1` through `M` and write the common palette as

\[
 \Omega_E=\bigsqcup_{\alpha,\beta}[E_{\alpha\beta}].
\tag{4.3}
\]

A vertex in the `(alpha,beta)` cell remembers both its YES and NO types.  The residual palette
gauge is

\[
 H_E=\prod_{\alpha,\beta}S_{E_{\alpha\beta}}.
\tag{4.4}
\]

For `s in {L,R}`, define the transportation set

\[
 \mathcal T_s(E)=
 \left\{C\in\mathbb N^{\Omega_E\times\Omega_E}:
 \begin{array}{l}
  \sum_wC(v,w)=r^1_s(\alpha(v)),\\
  \sum_vC(v,w)=r^0_s(\beta(w))
 \end{array}
 \right\}.
\tag{4.5}
\]

The group `H_E` acts simultaneously by

\[
 h:(C_L,C_R)\longmapsto
 (P_hC_LP_h^{-1},P_hC_RP_h^{-1}).
\tag{4.6}
\]

### Classification theorem

There is a canonical bijection

\[
 \boxed{
 K_1\backslash G/K_0
 \ \longleftrightarrow\ 
 \bigsqcup_{E\in\mathcal E}
 H_E\backslash\bigl(\mathcal T_L(E)\times\mathcal T_R(E)\bigr).
 }
\tag{4.7}
\]

To prove injectivity, an isomorphism of the merged palette sends `E` to `E` and conjugates both
contingency matrices as in (4.6).  For the converse, use `h` to define the common alphabet
permutation.  For each side and every cell `(v,w)`, the two pairs contain exactly `C_s(v,w)`
positions with endpoint labels `(v,w)`.  Choose a bijection between the corresponding position
cells.  Their disjoint union is a side-`s` position permutation.  Together with the alphabet
permutation, the two side permutations give an element of `G` carrying one pair to the other.

Thus (4.7) is complete, not merely necessary.  It is smaller than `D(x_1,x_0)` because the two
label copies and `M_=` have been merged, but it loses no information.

For `d>=2`, the YES type of a common-palette vertex is recovered from its row-degree pair

\[
 \left(\sum_wC_L(v,w),\sum_wC_R(v,w)\right)
 \in\{(0,0),(1,1),(1,0),(0,1),(d,0),(0,d)\},
\tag{4.8}
\]

and the NO type is recovered from the analogous column-degree pair.  Hence the `(alpha,beta)`
color and `E` are determined by `(C_L,C_R)`.  On the infinite subsequence (2.1), the minimal
complete invariant can therefore be stated simply as the simultaneous permutation-isomorphism
class of the two colored adjacency matrices.

Conditional on `E`, the two transportation sets factor because `S_n^(L)` and `S_n^(R)` are
independent, but the quotient does not generally factor:

\[
 \mathbb C[\mathcal T_L(E)\times\mathcal T_R(E)]^{H_E}
 \ne
 \mathbb C[\mathcal T_L(E)]^{H_E}\otimes
 \mathbb C[\mathcal T_R(E)]^{H_E}.
\tag{4.9}
\]

The diagonal palette action in (4.6) is the genuine joint `L/R` coupling.

## 5. Exact independence from the old address data

Fix, for example, the feasible equality table with nonzero cells

\[
 E_{L_d,L_d}=a,\quad E_{R_d,R_d}=a,\quad
 E_{L_1,L_1}=a-1,\quad E_{C,L_1}=1,\quad
 E_{R_1,R_1}=a-1,\quad E_{U,R_1}=1.
\tag{5.0}
\]

It has a cell of size `a` identifying the YES `L_d` labels with the NO `L_d` labels.  Fix every
singleton incidence, every right-side incidence, both input-wise
singleton-to-heavy address maps, and both repair endpoints.  Select two labels `u_1,u_2` in that
heavy cell.  On their left-heavy occurrence fibers use (1.2), and leave every other heavy label
on a fixed diagonal block of multiplicity `d`.

Every matrix in (1.2) has the required row and column sums `d`, so every `k` is a legal physical
position incidence.  Reindexing the two common palette labels simultaneously fixes the displayed
symmetric matrix; it cannot change `k`.  Therefore the `d+1` choices are distinct orbits in
(4.7).

Nothing in the two address maps records how occurrences of `u_1,u_2` overlap the comparison
input's occurrence fibers.  The repair endpoints live among the singleton labels and are also
unchanged.  This gives the exact separation

\[
 (r_1,r_0,\text{repair endpoints})
 \quad\not\Longrightarrow\quad
 [C_L,C_R].
\tag{5.1}
\]

The full-position layer is therefore not a renaming of the natural two-matching cycle word.

## 6. The smallest joint words and the query mark

Keep

\[
 M:\mathbb C^{\Omega_0}\longrightarrow\mathbb C^{\Omega_1}
\tag{6.0}
\]

explicit for type checking.  The shortest closed
word made from one side-incidence edge and the equality matching is

\[
 W_{=,s}=\operatorname{Tr}_{\mathbb C^{\Omega_1}}(C_sM^{-1}).
\tag{6.1}
\]

After the common-palette gauge `M=I`, this is `Tr(C_s)`, the number of side-`s` positions on
which the two input values agree.  It is variable even though all row and column margins are
fixed.  In (1.2), the selected component contributes `2k` to (6.1).

This is the absolute smallest nonconstant joint word, but it is only a one-edge overlap count.
The first normalized statistic that sees how an entire contingency table is distributed is

\[
 W_{2,s}=\operatorname{Tr}(G_sG_s^*)
 =\sum_{v,w}{C_s(v,w)^2\over r^1_s(v)r^0_s(w)}.
\tag{6.2}
\]

The selected heavy block (1.2) contributes

\[
 {2\bigl(k^2+(d-k)^2\bigr)\over d^2}.
\tag{6.3}
\]

If the linear equality count is fixed, (6.2) still contains new information.  For example, on
three heavy labels take a circulant `d`-regular block with first row

\[
 (k,r,d-k-r).
\tag{6.4}
\]

Changing `r` while keeping `k` fixed preserves every margin and `Tr(C_s)=3k`, but changes the
square sum in (6.2) except for the obvious reflection symmetry.

There are also genuinely mixed-side words.  The shortest typed one is

\[
 W_{LR}=\operatorname{Tr}_{\mathbb C^{\Omega_1}}
 (C_LM^{-1}C_RM^{-1}),
\tag{6.5}
\]

which becomes `Tr(C_LC_R)` after merging the equality matching.  It records a closed word with
one `L` position edge, one `R` position edge, and the two required equality returns.  It depends
on the relative alignment of `C_L,C_R` under the diagonal action (4.6), not only on their two
separate conjugacy classes.

Cycle traces are useful formula-defined invariants but are not a complete basis: nonisomorphic
colored multigraphs can have identical closed-walk spectra.  Completeness requires the orbit basis
in Section 7, or equivalently all colored finite-pattern counts.

Now mark one physical coordinate `i` on side `s`.  In the common-palette graph this distinguishes
one occurrence edge

\[
 v\xrightarrow{s}w.
\tag{6.6}
\]

The queried values are equal exactly when `v=w`, because the equality matching has been gauged to
the identity.  Thus the physical query mask keeps precisely the marked types with

\[
 v\ne w.
\tag{6.7}
\]

In the two-heavy block (1.2), the two diagonal marked types are equality types of total
multiplicity `2k`, while the two off-diagonal marked types are query-visible and have total
multiplicity `2(d-k)`.  This is the smallest exact illustration of why unmarked full-position
data and the query-visible marked system differ.

## 7. Formula-defined orbital basis and dimension growth

For an orbit

\[
 \omega=(E,[C_L,C_R]_{H_E})
\tag{7.1}
\]

in (4.7), define the zero-one rectangular orbital matrix

\[
 A_\omega[x_1,x_0]
 ={\bf1}[(E(x_1,x_0),C_L(x_1,x_0),C_R(x_1,x_0))\in\omega].
\tag{7.2}
\]

Then

\[
 \{A_\omega:\omega\in K_1\backslash G/K_0\}
\tag{7.3}
\]

is a formula-defined basis of every `G`-invariant rectangular coefficient.  If

\[
 I_\omega=K_1\cap g_\omega K_0g_\omega^{-1},
\tag{7.4}
\]

its exact row and column degrees and raw norm are

\[
 r_\omega={|K_1|\over|I_\omega|},
 \qquad
 s_\omega={|K_0|\over|I_\omega|},
 \qquad
 \|A_\omega\|=\sqrt{r_\omega s_\omega}.
\tag{7.5}
\]

Hence

\[
 \widehat A_\omega={A_\omega\over\sqrt{r_\omega s_\omega}}
\tag{7.6}
\]

is the canonical normalized basis with no hidden row/column measure convention.

The exact orbital dimension is

\[
 \dim e_{K_1}\mathbb C[G]e_{K_0}
 =\sum_{E\in\mathcal E}
 \left|H_E\backslash
  (\mathcal T_L(E)\times\mathcal T_R(E))\right|.
\tag{7.7}
\]

For fixed `E`, Burnside gives the completely explicit count

\[
 {1\over|H_E|}\sum_{h\in H_E}
 |\operatorname{Fix}_{\mathcal T_L(E)}(h)|
 |\operatorname{Fix}_{\mathcal T_R(E)}(h)|.
\tag{7.8}
\]

The dimension is not bounded by the one/two-endpoint ranks `2` or `7`.  To obtain a clean lower
bound, use the aligned `L_d/L_d` palette cell of size `a`, freeze every other block, and set

\[
 C_L^{(\sigma)}=(d-1)I_a+P_\sigma,
 \qquad \sigma\in S_a.
\tag{7.9}
\]

Every row and column sum is `d`.  Simultaneous palette conjugation sends (7.9) to
`(d-1)I+P_(h sigma h^(-1))`, and the matrix determines `P_sigma`.  Thus its orbits are in
bijection with conjugacy classes of `S_a`, so

\[
 \dim e_{K_1}\mathbb C[G]e_{K_0}\ge p(a),
\tag{7.10}
\]

where `p(a)` is the partition number.  On (2.1), the standard analytic asymptotic gives
`p(a)=exp(Theta(sqrt(a)))=exp(Theta(m))`.  This is an orbital-dimension statement only; it is not
evidence for any adversary exponent.

## 8. Partition/Hecke reduction of arbitrary scalar laws

Let

\[
 \mathcal H_{10}=e_{K_1}\mathbb C[G]e_{K_0}.
\tag{8.1}
\]

Because `K_1` and `K_0` differ, this is a rectangular Hecke bimodule rather than one square
algebra.  The basis (7.3) identifies it with the full space of scalar functions on (4.7).
Consequently every scalar law

\[
 f(E,[C_L,C_R])
\tag{8.2}
\]

is a standalone orbital multiplier in (8.1), including nonlinear functions, arbitrary cycle
weights, and joint `L/R` trace words.

In Fourier form, for an irreducible `rho` of `G`, put

\[
 M_t(\rho)=V_\rho^{K_t}.
\tag{8.3}
\]

Then

\[
 \mathcal H_{10}\cong
 \bigoplus_{\rho\in\widehat G}
 \operatorname{Hom}(M_0(\rho),M_1(\rho)).
\tag{8.4}
\]

An arbitrary invariant coefficient is therefore a fixed collection of multipliers

\[
 \widehat f(\rho):M_0(\rho)\longrightarrow M_1(\rho).
\tag{8.5}
\]

At bounded polynomial degree the same statement has a smaller diagrammatic realization.  A
monomial in entries of `C_L,C_R` selects finitely many occurrence edges; after quotienting by
palette and occurrence permutations, only their equality partition and `L/R` colors remain.
Thus degree-`ell` words are fixed colored partition-diagram multipliers on the `ell`-fold tensor
powers of the occurrence embeddings (3.4).  Taking all degrees recovers the full orbital basis.

Therefore no scalar or nonlinear three-layer word avoids **fixed-multiplier form as a matter of
representation theory**.  What it can avoid is the much narrower two-matching statement that all
data reduce to one relative permutation with only one/two repair points.  The multiplicity spaces
and orbit rank in (8.4) now grow at least as in (7.10).

## 9. Exact survival under normalized address incidence

Let

\[
 \pi_t:\mathcal Y_t\longrightarrow X_t
\tag{9.1}
\]

be the addressed-presentation maps.  On `u=1`, both fibers have size `C=(a!)^2`, and the
normalized coisometries are `R_t=C^(-1/2)Q_t`.

Let `f` be any scalar function of the physical invariant (4.7), and lift it to presentation pairs
by

\[
 \widetilde f(\widetilde x_1,\widetilde x_0)
 =f(\pi_1(\widetilde x_1),\pi_0(\widetilde x_0)).
\tag{9.2}
\]

It is constant on each row-fiber/column-fiber pair.  Hence for every lifted operator
`widetilde Gamma` of the correct rectangular type,

\[
 \boxed{
 R_1(\widetilde\Gamma\circ\widetilde f)R_0^*
 =(R_1\widetilde\Gamma R_0^*)\circ f.
 }
\tag{9.3}
\]

This is an entrywise identity; the common factor `1/C` appears on both sides.  For general `u`
the same proof carries the exact `1/(C sqrt(u))` factor.  Thus normalized incidence may forget a
hidden address chart, but it cannot forget the physical pair-contingency invariant.

## 10. Why the earlier fixed-middle partial-trace ceiling does not settle this system

The LR-multiplicity audit considered a factor

\[
 U_1(z_1)^*AU_0(z_0)
\tag{10.1}
\]

whose fixed middle operator `A` was independent of the occurrence pair.  Marking a coordinate
only restricted the representation carrier.  The unmarked partial trace was a convex combination
of the marked branch partial traces, so some marked branch retained its norm.  For a pure
multiplicity mixer the identical matrix appeared in every branch.

Full position incidence violates the tensor-factor/scalar-mask hypothesis needed for that ceiling,
even though it remains a fixed multiplier in the broader sense of Section 8.  Its broad Fourier
multiplier is fixed, but the input frames now encode the full physical occurrence assignment; a
query acts on those frames rather than only on a separate scalar base kernel.  Marking a physical
coordinate points an edge of `C_s`, and the query mask deletes all pointed equality edges.  If `T_eta` denotes a
one-point orbital and `forget(eta)=omega`, then exactly

\[
 A_\omega=\sum_{\eta:\operatorname{forget}(\eta)=\omega}T_\eta,
\tag{10.2}
\]

while

\[
 A_\omega\circ\Delta_i
 =\sum_{\substack{\eta:\operatorname{forget}(\eta)=\omega\\
                   \text{marked edge off }M_=}}
 T_\eta.
\tag{10.3}
\]

The equality-marked summands in (10.2) are absent from (10.3).  Therefore the unmarked block is
not a convex combination of only the query-visible marked blocks, and there is no analogue of the
LR inequality `||W_K||<=max_eta||W_eta||` from fixed-middle factorization alone.

The only structural escape left by this classification is consequently precise:

* choose signed orbital coefficients in (7.3) whose unmarked Hecke block adds coherently;
* prove that every **off-equality** left- and right-pointed block in (10.3) is smaller by the
  required factor;
* retain the outer `a^(2/3)` contribution and cover all physical roles.

This can happen, if at all, through occurrence-incidence cancellation in the marked partition
system.  Merely choosing a higher character, a nonlinear scalar word, or a large orbital space is
not itself such a proof.  No coefficient is proposed or tested in this memo.

## 11. Gate ledger

| Obligation | Outcome |
|---|---|
| exact legal regime | infinite `p=0,u=1`, `q=4a`, `n=a(d+1)` subsequence |
| YES/NO label types and sizes | explicit in (2.3)--(2.6) |
| stabilizer/wreath action | typed in (2.8) |
| side occurrence sets | size `n`, equations (3.9)--(3.11) |
| raw and normalized pair incidence | `C_s=B_1B_0^*`, `G_s=F_1^*F_0` |
| occurrence multiplicity | exact double-coset count (3.12) |
| minimal complete invariant | transportation-orbit bijection (4.7) |
| redundancy of explicit type table | degree recovery for `d>=2`, equation (4.8) |
| independence from old two-matching data | exact `2 x 2` family (1.2), Section 5 |
| shortest variable word | equality overlap `Tr(C_sM^(-1))` |
| first distributional word | weighted square sum `Tr(G_sG_s^*)` |
| mixed `L/R` word | typed formula (6.5) |
| query mark | one edge; keep exactly `v!=w` |
| formula-defined complete basis | orbitals (7.2)--(7.6) |
| exact orbital dimension | (7.7)--(7.8) |
| dimension growth | at least `p(a)=exp(Theta(m))` on the subsequence |
| arbitrary scalar/nonlinear laws | full colored Young-Hecke bimodule, Section 8 |
| normalized address incidence | exact pull-through identity (9.3) |
| earlier LR partial-trace ceiling | inapplicable because equality marked branches are deleted |
| missing `m^(1/6)` separation | unproved; no coefficient supplied |
| numerical exponent inference | none |
| completion status | none; independent review pending |

## 12. Source and scope ledger

The exact histogram, stabilizers, full graph `D(x,y)`, and one-point orbital query rule are from
`ksum/artifacts/ksum_L3_critical_orbit_intertwiner_attempt_20260721.md`.  The exact `C/uC` normalized
incidences are from
`ksum/artifacts/ksum_L3_critical_coupled_uic_address_cycle_attempt_20260721.md`.  The two-matching
factorization boundary is from
`ksum/artifacts/ksum_L3_critical_cycle_word_factorization_audit_20260722.md`.  The fixed-middle
partial-trace ceiling is from
`ksum/artifacts/ksum_L3_critical_lr_multiplicity_mixing_audit_20260722.md`.  The independent `P/Q`
occurrence cut and selector-forgetting boundary are from
`ksum/artifacts/ksum_L3_critical_sparse_delocalized_multiblock_attempt_20260722.md` and
`ksum/artifacts/ksum_L3_critical_coupled_multiblock_inner_attempt_20260722.md`.

The present memo classifies the full position-incidence orbit exactly on `p=0,u=1`.  It does not
construct a three-layer adversary, prove any norm separation, handle `p>0,u>1`, or license a
completion-tier DAG status.  It generates no new ansatz beyond the already registered full-
position-incidence node.

## 13. Bottom line

The full pair position-incidence graph contains real information that the two repaired/address
matchings cannot see.  The smallest example is just a variable heavy-fiber overlap table; the
complete data are two coupled transportation matrices, not a third perfect matching and not a
bounded endpoint selector.

At the same time, every scalar or nonlinear law in those matrices remains a fixed multiplier in a
colored partition/Young-Hecke bimodule.  Calling a coefficient a "three-layer word" does not by
itself leave that system.  What is genuinely new is the marked action: a query points an
occurrence edge and removes the equality-pointed branches.  That deletion is exactly what prevents
the old fixed-middle partial-trace no-go from closing the route.

Thus the structural gate passes and the exponent gate remains completely open.  A successful next
step must give explicit signed weights in the orbital basis and prove a growing separation against
every off-equality one-point extension; dimension growth or a cycle statistic alone is not
evidence of such a separation.
