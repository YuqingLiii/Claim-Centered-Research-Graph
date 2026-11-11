# Werner finite-\(d\) gate: exact permutation constellation and local surgery

Date: 2026-08-30

Status: proposer-side Question 3 artifact. No canonical YAML is changed. This note proves an
exact, lossless permutation/index encoding of every Werner contraction skeleton, proves its Euler
loop-deficit identity, and proves a bounded-support handle surgery for a recursively defined
nontrivial subclass. It also gives an actual repeated-edge family on which all two-factor
common-cycle transposition surgeries stall while positive genus remains. The universal surgery
and the full-size centered bound remain open.

No web access and no large numerical computation are used.

## 1. Outcome

Let `N` be the trace-moment order and put `E=2N`. On the physical slot set

\[
 X=\{V_i,A_i:i\in\mathbb Z/N\mathbb Z\},
\tag{1}
\]

define

\[
 J(V_i)=A_i,\quad J(A_i)=V_i,
 \qquad
 \rho(V_i)=V_{i-1},\quad \rho(A_i)=A_{i-1},
 \qquad K=J\rho=\rho J.
\tag{2}
\]

The two cycles of `rho`, rooted at `V_0,A_0`, are the fixed boundary orders induced by the
physical trace wirings after the matrix factors are collapsed to tuple slots.

For every balanced Haar contraction, let `sigma,tau in S_X` be the global row and column
pairings. They preserve the tuple-label coloring and are block diagonal over generator labels.
Define

\[
 \boxed{
 \mathsf A=J\sigma^{-1},\qquad
 \mathsf B=\sigma K\tau\sigma^{-1},\qquad
 \mathsf C=\sigma\tau^{-1}.}
\tag{3}
\]

Then exactly

\[
 \mathsf A\mathsf B\mathsf C=\rho.
\tag{4}
\]

Conversely,

\[
 \sigma=\mathsf A^{-1}J,\qquad
 \tau=\mathsf C^{-1}\mathsf A^{-1}J,
\tag{5}
\]

so (3) is lossless and introduces no edge-ordering factorial. The correct bare topological object
is therefore a rooted two-boundary **three-permutation constellation**, not automatically an
ordinary map with only `E` edges.

If `c` is the number of transitive components of the constellation and `h` its total orientable
genus, its minimal-Weingarten power of `d` is exactly

\[
 \#\mathsf A+\#\mathsf B+\#\mathsf C-2E
 =2c-2h-2.
\tag{6}
\]

In particular, every connected skeleton has power `d^(-2h)`. This proves the previously
missing Euler loop-deficit identity.

There is also a rigorous local surgery. If `t=(xy)` has `x,y` in the same cycle of both
`mathsf A` and `mathsf B`, set

\[
 (\mathsf A',\mathsf B',\mathsf C')
 =(\mathsf A t,t\mathsf B,\mathsf C).
\tag{7}
\]

It fixes `rho`, changes only the two-point support of `t`, and, when the new constellation remains
connected, lowers genus by exactly one. It changes at most four row/column pairing arrows. A
recursively reducible depth-`h` subclass therefore has at most

\[
 \binom{E}{2}^{h}\le(2N^2)^h
\tag{8}
\]

reverse-surgery histories and at most `m^(N+2+4h)` tuple-label assignments whenever its planar
endpoint has the paired-stack component bound `N+2`. Since `mathsf C` is fixed, the minimal
Möbius/Catalan weight is fixed as well. After `d^(-2h)`, the per-handle factor is at most

\[
 \frac{2m^4N^2}{d^2}=o_m(1)
 \qquad(N\le c_m\log d).
\tag{9}
\]

This closes that subclass once its planar baseline is controlled. It does not cover all
skeletons. For every odd `N>=5`, the actual repeated-edge skeleton `sigma=tau=id` has genus
`(N-1)/2`; after one allowed surgery it still has genus `(N-3)/2>0`, but no further surgery of
type (7), nor its `mathsf B,mathsf C` analogue, is possible. Thus pairwise common-cycle splitting
is rigorously insufficient; a universal proof needs a three-point or more general
boundary-preserving move.

## 2. Exact matrix-index model

For an edge sequence `e_i=(v_i,a_i)`, write the two traces in the exact moment as

\[
 \operatorname{Tr}\prod_{i=0}^{N-1}(U_{v_i}^*U_{a_i}),
 \qquad
 \operatorname{Tr}\prod_{i=0}^{N-1}(U_{a_i}^*U_{v_i}).
\tag{10}
\]

The second expression equals the complex conjugate of the block-reversed trace. Introduce cyclic
matrix indices `x_i,y_i,z_i,w_i`. The product of matrix entries is

\[
 \prod_i
 \overline{(U_{v_i})_{y_i x_i}}
 (U_{a_i})_{y_i x_{i+1}}
 \overline{(U_{a_i})_{w_i z_i}}
 (U_{v_i})_{w_i z_{i+1}}.
\tag{11}
\]

Each physical slot has one unstarred and one starred occurrence:

| slot | unstarred row, column | starred underlying row, column |
|---|---|---|
| `A_i` | `y_i,x_(i+1)` | `w_i,z_i` |
| `V_i` | `w_i,z_(i+1)` | `y_i,x_i` |

Index the unstarred row variables by

\[
 r(A_i)=y_i,qquad r(V_i)=w_i.
\tag{12}
\]

The starred row belonging to slot `s` is `r(Js)`. Likewise, index unstarred column variables by

\[
 q(A_i)=x_{i+1},\qquad q(V_i)=z_{i+1}.
\tag{13}
\]

The starred column belonging to `s` is `q(Ks)`, because

\[
 K(V_i)=A_{i-1},\qquad K(A_i)=V_{i-1}.
\tag{14}
\]

For each generator label `v`, the unitary Weingarten formula pairs unstarred occurrences with
starred occurrences by two bijections `sigma_v,tau_v`. Identifying both occurrence sets with
their physical slots gives global permutations `sigma,tau` of `X`. The row Kronecker constraints
are

\[
 r(s)=r(J\sigma(s)),
\tag{15}
\]

and the column constraints are

\[
 q(s)=q(K\tau(s)).
\tag{16}
\]

Therefore the number of free matrix-index loops is exactly

\[
 L(\sigma,\tau)=\#(J\sigma)+\#(K\tau).
\tag{17}
\]

No asymptotic theorem enters (11)--(17); these are finite identities for every `d,N` and every
pair of contraction permutations.

## 3. Lossless two-boundary constellation

Write `#P` for the number of cycles of a permutation `P`. The permutations in (3) have

\[
 \#\mathsf A=\#(J\sigma),\qquad
 \#\mathsf B=\#(K\tau),\qquad
 \#\mathsf C=\#(\sigma\tau^{-1}).
\tag{18}
\]

The first equality follows because `J sigma^(-1)` is conjugate to `sigma^(-1)J`, whose inverse is
`J sigma`; the second is conjugacy by `sigma`. Direct multiplication proves (4):

\[
 (J\sigma^{-1})(\sigma K\tau\sigma^{-1})(\sigma\tau^{-1})
 =JK=\rho.
\tag{19}
\]

Equations (5) follow immediately from `mathsf A` and `mathsf C`; `mathsf B` is then forced by
`mathsf A mathsf B mathsf C=rho`. Hence two distinct contraction skeletons cannot have the same
rooted constellation.

### 3.1 Ribbon realization

The tuple `(mathsf A,mathsf B,mathsf C,rho^(-1))` has product identity on `E` darts. Its oriented
incidence ribbon complex has two edges per dart. Denote the halfedges of the `A--B` edge of `s` by
`a_s,bar(a)_s`, and those of the `B--C` edge by `b_s,bar(b)_s`; the edge involution pairs the
barred and unbarred versions. Define the vertex rotation by

\[
 \begin{array}{lll}
 A\text{-vertices}:&a_s\mapsto a_{\mathsf A s},\\
 B\text{-vertices}:&\bar a_s\mapsto b_s,
                    &b_s\mapsto\bar a_{\mathsf B s},\\
 C\text{-vertices}:&\bar b_s\mapsto\bar b_{\mathsf C s}.
 \end{array}
\]

Thus the 0-cells are exactly the cycles of `mathsf A,mathsf B,mathsf C`, and there are `2E`
ordinary ribbon edges. If `phi` is the face permutation (vertex rotation after the edge
involution), then four successive face steps give

\[
 a_s\longmapsto b_s\longmapsto\bar b_{\mathsf C s}
 \longmapsto\bar a_{\mathsf B\mathsf C s}
 \longmapsto a_{\mathsf A\mathsf B\mathsf C s}
 =a_{\rho s}.
\]

Hence the faces are exactly the cycles of `rho`, rooted at `a_(V_0),a_(A_0)`. Every vertex link
is a circle, so the complex is an orientable, possibly disconnected surface. Reading the two
rooted face cycles every four steps names every dart in physical order; consequently passing
between the permutation tuple and the rooted colored ribbon complex introduces no `(2N)!`
factor.

This realization has `2E=4N` ordinary ribbon edges. This corrects the optimistic interface in
`WERNER_MINIMAL_SKELETON_MAP_COUNT_20260830.md`: its abstract ordinary-map theorem remains valid,
but a bare Werner skeleton does **not** instantiate its provisional `E=2N` application through
(3). One would need either a sharper count for these structured `2E`-edge constellations or a
separate minimal-path-expanded compression. Neither is proved here.

## 4. Euler loop-deficit identity

Let `c` be the number of orbits of the group generated by
`mathsf A,mathsf B,mathsf C`. Because their product is `rho`, every orbit is a union of `rho`
cycles. Since `#rho=2`, one has `c in {1,2}`.

The incidence complex has

\[
 V=\#\mathsf A+\#\mathsf B+\#\mathsf C,\qquad
 E_{\rm rib}=2E,\qquad F=\#\rho=2.
\tag{20}
\]

If `h` is the sum of the genera of its `c` connected components, Euler's formula gives

\[
 \#\mathsf A+\#\mathsf B+\#\mathsf C+2-2E
 =2c-2h.
\tag{21}
\]

For each active label, let `p_v` be its number of physical slots and
`pi_v=sigma_v tau_v^(-1)`. The minimal unitary Weingarten term has power

\[
 d^{-p_v-|\pi_v|},
 \qquad |\pi_v|=p_v-\#\pi_v.
\tag{22}
\]

Since `sum_v p_v=E` and global `mathsf C=sigma tau^(-1)` is block diagonal over labels, the
product of all minimal Weingarten powers is

\[
 d^{-E-|\mathsf C|}=d^{-2E+\#\mathsf C}.
\tag{23}
\]

The index sums contribute `d^(#mathsf A+#mathsf B)` by (17)--(18). Combining with (23) gives

\[
 d^{\#\mathsf A+\#\mathsf B+\#\mathsf C-2E}
 =d^{2c-2h-2},
\tag{24}
\]

which proves (6). In the connected sector `c=1`, every topological handle costs exactly `d^(-2)`.
In the two-component sector the power is `d^(2-2h)`; this note does not silently identify every
positive-genus disconnected term with the already controlled free-word return sector.

## 5. Exact tuple-label constraints

Let `lambda:X->[m]` be the physical coloring

\[
 \lambda(V_i)=v_i,\qquad \lambda(A_i)=a_i,\qquad v_i\ne a_i.
\tag{25}
\]

A contraction skeleton is admissible exactly when

\[
 \lambda\circ\sigma=\lambda,qquad
 \lambda\circ\tau=\lambda.
\tag{26}
\]

Using (5), this is equivalently

\[
 \lambda(\mathsf A^{-1}Js)=\lambda(s),qquad
 \lambda(\mathsf C^{-1}\mathsf A^{-1}Js)=\lambda(s)
 \quad(s\in X).
\tag{27}
\]

Let `H(sigma,tau)` be the undirected equality graph on `X` with edges

\[
 \{s,\sigma(s)\},\qquad \{s,\tau(s)\}.
\tag{28}
\]

Self-loops are allowed. For a fixed structural skeleton, the number of compatible labelings is at
most `m^(c(H))`; imposing `v_i!=a_i` only decreases it. Equations (27)--(28) are the exact
permutation interface that a future paired-stack proof must control.

## 6. Bounded-support common-cycle surgeries

We use the elementary split/join fact: for a permutation `P` and transposition `t=(xy)`,

\[
 \#(Pt)=\#P+1
 \quad\Longleftrightarrow\quad
 x,y\text{ lie in the same cycle of }P.
\tag{29}
\]

The same criterion holds for `tP`, since left multiplication is right multiplication by the
conjugate transposition `P^(-1)tP`.

### Lemma 1: `A--B` surgery

Assume `x!=y` lie in the same cycle of both `mathsf A` and `mathsf B`, and let `t=(xy)`. Define
(7). Then:

1. `mathsf A' mathsf B' mathsf C'=rho` exactly;
2. `#mathsf A'=#mathsf A+1` and `#mathsf B'=#mathsf B+1`;
3. the Euler characteristic increases by two; and
4. if the new tuple is transitive, its genus is `h-1`.

**Proof.** The product identity is

\[
 (\mathsf A t)(t\mathsf B)\mathsf C
 =\mathsf A\mathsf B\mathsf C=\rho.
\]

Both cycle assertions are (29), and (21) gives the last two statements. `square`

The recovered contraction permutations after surgery are

\[
 \sigma'=t\sigma,qquad
 \tau'=\mathsf C^{-1}t\mathsf C\,\tau.
\tag{30}
\]

Thus at most two `sigma` arrows and two `tau` arrows change.

### Lemma 2: `B--C` surgery

If `x,y` lie in the same cycle of both `mathsf B` and `mathsf C`, then

\[
 (\mathsf A',\mathsf B',\mathsf C')
 =(\mathsf A,\mathsf B t,t\mathsf C)
\tag{31}
\]

also fixes `rho`, raises the cycle sum by two, and lowers genus by one whenever transitivity is
preserved. Here `sigma'=sigma` and

\[
 \tau'=\mathsf C^{-1}t\mathsf C\,\tau,
\tag{32}
\]

so only two column-pairing arrows change.

The connectedness hypothesis is necessary. If a surgery raises the component count from one to
two, the Euler increase can be absorbed by `c` instead of lowering `h`. No genus reduction is
claimed in that case.

The recovered `sigma',tau'` need not preserve the original coloring `lambda`: the transposition
may exchange two different generator labels. The surgery is therefore a structural encoding
move, not automatically another nonzero Haar term. This is harmless only when the violated
pairing arrows are explicitly counted as defects, as in Proposition 3; one must not silently
treat every intermediate constellation as an admissible physical density-matrix contraction.

## 7. A rigorously controlled recursive subclass

Fix a collection `P_N` of connected genus-zero structural constellations whose equality graphs
satisfy

\[
 c(H)\le N+2.
\tag{33}
\]

For example, `P_N` may be restricted to structures carrying the explicit genus-zero
forward/block-reversal paired-stack certificate from the previous collision artifact.

Define `R_(N,0)=P_N`. Recursively, a connected constellation belongs to `R_(N,h)` if its
lexicographically first admissible `A--B` surgery (7) remains connected and belongs to
`R_(N,h-1)`. The lexicographic convention merely chooses one code when several reductions exist.

### Proposition 3

For this subclass:

\[
 |R_{N,h}|\le |P_N|\binom{E}{2}^h,
\tag{34}
\]

and every original admissible skeleton in `R_(N,h)` satisfies

\[
 c(H)\le N+2+4h.
\tag{35}
\]

Moreover `mathsf C` and hence the minimal coefficient `P_0(mathsf C)` are unchanged along the
entire reduction.

**Proof.** Starting from the planar endpoint, the ordered list of `h` transpositions reconstructs
the initial triple uniquely because (7) is involutive. There are at most `binom(E,2)` choices at
each inverse step, proving (34).

By (30), one step replaces at most two row-pairing arrows and two column-pairing arrows. After `h`
steps, the initial equality graph differs from the planar endpoint graph by at most `4h` edge
replacements. Delete the affected edges from both graphs. Removing one edge can increase the
number of components by at most one, while restoring edges can only merge components. Equation
(33) therefore gives (35). Finally, (7) leaves `mathsf C` fixed. `square`

After the moment normalization, (34)--(35), the Euler factor `d^(-2h)`, and `E=2N`, every handle
costs at most the factor in (9). The already proved monotone-Weingarten excess multiplier

\[
 \left(1-6(2N)^{7/2}/d^2\right)^{-1}=1+o(1)
\tag{36}
\]

is uniform on this subclass for `N<=c_m log d`. Hence the local surgery loss is quantitatively
sufficient; only the planar baseline for the chosen `P_N` remains to be supplied.

### 7.1 Explicit actual genus-one member

Take `N=3`, `lambda(V_i)=1`, `lambda(A_i)=2`, and `sigma=tau=id`. This is the repeated edge
sequence `e_i=(1,2)` with identity pairings. Then

\[
 \mathsf A=J=(V_0A_0)(V_1A_1)(V_2A_2),
 \quad
 \mathsf B=K=(V_0A_2V_1A_0V_2A_1),
 \quad
 \mathsf C=id.
\tag{37}
\]

The triple is transitive and

\[
 \#\mathsf A+\#\mathsf B+\#\mathsf C=3+1+6=10=2E-2,
\]

so it has genus one. With `t=(V_0 A_0)`, both common-cycle hypotheses hold. The surgery produces
`#mathsf A'=4,#mathsf B'=2,#mathsf C'=6`; it stays transitive and has genus zero. Its structural
endpoint equality graph has five components, exactly `N+2`. Thus the recursive subclass is
nonempty for an actual admissible Werner skeleton, not merely for an abstract constellation.

## 8. A repeated-edge obstruction to pairwise overlap surgery

The preceding move is not universal. Let `N>=5` be odd and again take the actual repeated-edge
skeleton

\[
 \lambda(V_i)=1,\quad\lambda(A_i)=2,\quad\sigma=\tau=id.
\tag{38}
\]

Then `mathsf A=J`, `mathsf B=K=Jrho`, and `mathsf C=id`. Because `J` commutes with `rho`,

\[
 K^2=\rho^2,\qquad K^N=J
\tag{39}
\]

for odd `N`. It follows that `K` is one `2N`-cycle. The group generated by `J,K` contains `rho`
and connects the two `rho` cycles, so the constellation is transitive. Its Euler characteristic
and genus are

\[
 \chi=N+1+2N+2-4N=3-N,
 \qquad h=\frac{N-1}{2}.
\tag{40}
\]

Every `A` cycle is the pair `{V_i,A_i}`, and both points lie in the unique `B` cycle, so one
`A--B` surgery is possible. Choose `t_i=(V_i A_i)`. Then `Jt_i` fixes `V_i,A_i` and keeps the
other `N-1` pairs. The permutation `t_iK` splits the `2N`-cycle into two `N`-cycles.

The two members of every remaining `J` pair lie in different new `B` cycles. Indeed,
`A_j=J(V_j)=K^N(V_j)`, so they are opposite points of the original `K` cycle, while multiplication
by `t_i` cuts that cycle at the opposite points `V_i,A_i`. Consequently:

- no two distinct points lie in a common cycle of both `mathsf A'=Jt_i` and `mathsf B'=t_iK`;
- `mathsf C=id` has only singleton cycles, so no `B--C` surgery is possible; and
- the new triple remains transitive because every nontrivial `Jt_i` pair joins the two `t_iK`
  cycles.

Its remaining genus is

\[
 h'=(N-3)/2>0.
\tag{41}
\]

Thus all surgeries (7) and (31) stall after one step on this actual family. This is not a
counterexample to a bounded-support surgery of size three or more, nor to a boundary-cutting
paired-stack construction. It rigorously rules out the simplest universal two-factor
common-cycle transposition induction.

## 9. What the exact encoding does to the previous map route

The exact interface settles two questions and reopens one quantitative point.

1. **No factorial is intrinsic.** The fixed rooted `rho` cycles name the darts in physical order,
   and (5) recovers `sigma,tau` exactly.
2. **The `d^(-2h)` factor is exact.** It is Euler characteristic (24), not a heuristic genus
   assignment.
3. **The bare object has `2E=4N` ordinary incidence edges.** Applying the earlier generic
   `16^L` map count with `L=4N`, and then the crude `P_0(C)<=16^N`, has planar base
   `16^(4N)16^N=1048576^N`, far above the Werner allowance. The earlier favorable `4096^N` base
   depended on an unproved `L=E` compression.

This does not show that the desired count is false. These are highly structured two-face,
three-colored incidence maps. A sharp two-face/constellation count of the form

\[
 \sum_{\substack{\mathsf A\mathsf B\mathsf C=\rho\\
                  \text{connected genus }h}}
 P_0(\mathsf C)
 \le D^N N^{\alpha h}
\tag{42}
\]

with `D<sqrt(18m)` at `ln m>18` is still plausible. Proposition 3 proves the polynomial-per-handle
part for its recursive subclass. The obstruction in Section 8 shows that a universal proof of
(42) cannot use only the pairwise overlap moves (7) and (31).

## 10. Smallest next lemma

The exact remaining surgery statement is now:

> **Physical-boundary-preserving constellation surgery (OPEN).** There are universal `s,L,alpha`
> such that every connected genus-`h` triple `A B C=rho` arising from an admissible Werner
> skeleton admits one of at most `N^alpha` local moves supported on at most `s` darts. The move
> fixes the two rooted cycles of `rho`, remains connected, lowers genus by one, and changes at most
> `L` arrows in the recovered pairings `sigma,tau`.

Any fixed `s,L,alpha` is quantitatively sufficient at `N<=c_m log d`: the handle factor becomes
`m^L N^alpha/d^2=o_m(1)`. Section 8 proves that the special case `s=2` consisting only of adjacent
factor split/split transpositions is false. The next credible cases are:

- a three-dart trisection changing two of `A,B,C` while keeping their product `rho`; or
- a four-endpoint chord switch in the `2E`-edge incidence map, together with a proof that it lifts
  back to at most `L` defects in (27).

The latter lift, not ordinary topological planarization by itself, is load-bearing: an arbitrary
two-face map surgery can destroy the alternating three-color incidence structure and need not
leave a physical forward/reversal paired-stack certificate.

## 11. Quantifiers and scope

- Equations (3)--(5), (11)--(21), and (25)--(28) are finite permutation/index identities for every
  `N,d`, every edge sequence, and every admissible pair of Haar contraction permutations.
  Equations (6) and (22)--(24) identify the minimal term in the large-`d` Weingarten expansion;
  the project regime `N<=c_m log d` is eventually inside its validity range.
- The only imported analytic inputs are the exact leading unitary-Weingarten power and
  Möbius/Catalan coefficient in (22), and the already audited monotone-tail estimate (36). The
  permutation encoding, incidence surface, Euler identity, and local surgeries are derived here.
- The Euler genus is total genus across permutation orbits. The connected `d^(-2h)` conclusion is
  stated only for `c=1`.
- Lemmas 1--2 are deterministic conditional surgeries; genus falls only when connectedness is
  preserved.
- Proposition 3 controls only the recursively `A--B`-reducible subclass, not every skeleton.
- Section 8 is an obstruction only to the stated pairwise split/split surgeries.
- No bound on the full minimal-skeleton absolute mass, no high-probability norm bound, and no
  counterexample to the Werner target are proved.
- The absolute-unbounded extensive-violation theorem is separate. This note addresses only the
  unresolved full-size Question 3 gate.

## 12. Candidate atomic DAG claims (not applied)

No canonical YAML is edited. Suggested claims remain at most `CONJECTURED` pending independent
audit:

1. `HEXT.werner-exact-constellation-encoding`
   - claim: equations (1)--(5) give a lossless rooted two-boundary encoding of `sigma,tau`.
2. `HEXT.werner-constellation-euler-deficit`
   - claim: the exact minimal-term power is `d^(2c-2h-2)`; connected terms cost `d^(-2h)`.
3. `HEXT.werner-common-cycle-local-surgery`
   - claim: Lemmas 1--2 give support-two, boundary-preserving genus reduction when their cycle and
     connectedness hypotheses hold.
4. `HEXT.werner-ab-reducible-subclass-count`
   - claim: equations (34)--(36) give `N^(2h)` histories and `m^(4h)` label loss for the recursive
     subclass.
5. `HEXT.werner-pairwise-surgery-obstruction`
   - claim: the odd repeated-edge family (38)--(41) stalls with positive remaining genus.
6. `HEXT.werner-two-boundary-constellation-count`
   - missing claim: prove the weighted count (42) at a target-compatible base.
7. `HEXT.werner-physical-boundary-preserving-surgery`
   - missing claim: prove the OPEN lemma in Section 10 with some universal bounded support.
8. `HEXT.same-tuple-werner-centered-bound`
   - do not promote; it still requires items 6--7 or an alternative cancellation-preserving
     argument.
