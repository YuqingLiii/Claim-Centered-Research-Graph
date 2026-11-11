# Planar repair for the two-boundary Werner rooted-map count

Date: 2026-08-30

Status: proposer-side Question 3 artifact. No canonical YAML is changed. This note gives a
fully self-contained deletion code for connected oriented planar maps with exactly two faces and
proves the doubly face-rooted estimate needed by
`HEXT.werner-two-boundary-constellation-count`. It replaces the incorrect refined planar-map
formula in `WERNER_TWO_BOUNDARY_CONSTELLATION_WEIGHTED_COUNT_20260830.md`; it does not use or cite
an unarchived enumeration formula.

The target node must remain at most `CONJECTURED` until this repair receives independent review.
The equality-component gate, the centered spectral bound, and full-size extensive Question 3
remain open.

No web access or numerical enumeration is used.

## 1. Result

Let `T_e` be the number of isomorphism classes of connected oriented planar maps with `e>=1`
edges, exactly two faces, and one distinguished directed halfedge. The face incident to the
distinguished halfedge is called the first face; the other face is the second face.

Let `R_(e,0)^(2)` be the number of such maps after additionally choosing one distinguished
directed boundary halfedge of the second face. Equivalently, the two faces are ordered and each
has its own directed root halfedge.

The main bounds are

\[
 \boxed{
 T_e\le \frac e2\binom{2e}{e},
 \qquad
 R_{e,0}^{(2)}\le e^2\binom{2e}{e}.}                         \tag{1}
\]

The proof deletes one canonically selected non-bridge edge from the unique cycle of the underlying
unicyclic multigraph. If the original root survives, the code is a rooted plane tree plus an
unordered pair of corners with repetition. If the root is itself the unique cycle loop, the code
is a corner-rooted plane tree plus one corner and, only when both insertion sites coincide, one
local order choice. The two classes exactly fit the right side of the first inequality in (1).

Loops, parallel edges, repeated insertion corners, orientation-preserving isomorphisms, and both
face roots are included explicitly below.

## 2. Root and isomorphism conventions

An oriented combinatorial map is a finite halfedge set `H`, a fixed-point-free involution
`alpha` pairing the two halfedges of every edge, and a permutation `sigma` whose cycles are the
positive cyclic orders at vertices. Connectedness means that `<alpha,sigma>` acts transitively on
`H`. Faces are the cycles of the corresponding face permutation; the choice between the
equivalent conventions `sigma alpha` and `alpha sigma` is immaterial for the counts, and we fix
`sigma alpha`.

A **directed root halfedge** is an element `r in H`, not merely an unoriented root edge. Its face
is the face cycle containing `r`. Two rooted maps are isomorphic when a halfedge bijection
intertwines `alpha` and `sigma` and sends every named root halfedge to the corresponding named root
halfedge. The cyclic orders, hence the orientation, must be preserved.

A connected rooted map has no nontrivial root-preserving automorphism: an automorphism fixing `r`
and commuting with `alpha,sigma` fixes the entire orbit of `r`, which is all of `H`. Thus the codes
below count rooted isomorphism classes directly; there is no division by automorphism group order.
The same conclusion follows from the explicit decoders even if one does not use this observation.

A corner is an occurrence of a gap between consecutive halfedges in a vertex rotation. A plane
tree with `n>=1` edges has exactly

\[
 \sum_v\deg(v)=2n                                                \tag{2}
\]

corners. The one-vertex zero-edge tree has one conventional corner.

## 3. Plane-tree count with either root convention

The number of plane trees with `n` edges and one directed root halfedge is

\[
 \operatorname{Cat}_n=\frac1{n+1}\binom{2n}{n}.              \tag{3}
\]

For completeness, traverse the tree boundary from the root in positive orientation, recording an
up-step when an edge is first crossed away from the root side and a down-step when it is crossed
back. This is a Dyck word of length `2n`; the usual stack reconstruction recovers the ordered
children at every vertex and the rooted tree. The cycle-lemma count of Dyck words is (3).

For `n>=1`, rooting at a corner gives the same number: the first halfedge following the root corner
in the positive contour is a directed root halfedge, and the corner immediately preceding a
directed root halfedge is the inverse map. For `n=0`, both conventions have one object. Hence
`Cat_n` counts both directed-halfedge-rooted and corner-rooted plane trees.

## 4. Every planar two-face map is unicyclic

Let a connected planar map have `e` edges, `V` vertices, and exactly two faces. Euler's identity
gives

\[
 V-e+2=2,
 \qquad V=e.                                                   \tag{4}
\]

Its underlying connected multigraph therefore has first Betti number

\[
 e-V+1=1.                                                      \tag{5}
\]

Consequently its non-bridge edges form one unique cycle core. The core is allowed to be

- one loop;
- a two-edge cycle of parallel edges; or
- an ordinary cycle of length at least three.

All remaining edges are bridges in plane trees attached to core vertices. Thus deleting any core
edge leaves a connected graph with `e-1` edges and `e` vertices, hence a tree. Restricting the
vertex rotations gives a plane tree.

This graph-theoretic statement handles loops and multiple edges without replacing the map by a
simple graph.

## 5. A canonical core-edge selector

For injectivity it is enough to choose one core edge invariantly from the rooted oriented map. The
following explicit selector will be used.

1. If the root edge is a bridge, its endpoints have distances to the core differing by one.
   Start at the nearer endpoint, follow the unique path to the core, and let `v` be the first core
   vertex. The incoming path halfedge and the positive rotation at `v` choose the first core
   halfedge encountered after it. Select the underlying core edge.
2. If the root edge belongs to a core cycle of length at least two, follow the directed root
   halfedge to its head vertex and select the other core edge incident there. This edge is distinct
   from the root edge, including for a two-edge parallel cycle.
3. If the root edge is the length-one core loop, select the root edge itself. This is the only case
   in which the chosen edge equals the root edge.

For a bridge attached directly to a core vertex, its core-side halfedge is the incoming path
halfedge in item 1. If the core is a loop, either of its two halfedges may be encountered first,
but both name the same selected edge. Thus the selector is defined in every case.

Every step uses only graph distance, the directed root, and the positive vertex rotations, so the
selector is preserved by rooted orientation-preserving isomorphisms.

## 6. Class I: the original root survives deletion

Assume the selected core edge is not the root edge. Delete its two halfedges from their vertex
rotations. The result is a plane tree with

\[
 n=e-1                                                        \tag{6}
\]

edges, rooted by the unchanged original directed halfedge.

The two deleted halfedge positions become two corners of the tree. They may be

- at different vertices;
- distinct corners at the same vertex; or
- the same corner, as can occur after deleting a loop with no intervening halfedges.

Because the deleted edge is not rooted, its two ends are not ordered. The deletion data are
therefore a two-element multiset of the `2n` tree corners. The number of possibilities is

\[
 \binom{2n+1}{2}=n(2n+1).                                    \tag{7}
\]

### Decoder

Given a rooted plane tree and an unordered corner pair with repetition, insert two new halfedges
in the named gaps and pair them by `alpha`. If the corners are distinct, exchanging the two new
halfedge names gives the same unrooted inserted edge. If the corners coincide, the two possible
orders of the new halfedges in that gap are likewise interchanged by swapping their names, so
there is still one rooted-map isomorphism class.

The reconstructed rotation system is connected and orientable. It has `e` vertices and `e`
edges. If it has `F` faces and genus `g`, Euler gives

\[
 F=2-2g.
\]

Every finite map has at least one face, so `g=0,F=2`. Hence the decoder always produces a planar
two-face map. On codes produced by deletion it restores the original map and its root. The code is
therefore injective even though codes not selected canonically by their decoded map are harmless
overcounts.

By (3) and (7), Class I contains at most

\[
 \operatorname{Cat}_n\,n(2n+1)                              \tag{8}
\]

rooted maps.

## 7. Class II: the root is the unique cycle loop

Now assume the selected edge is the root edge. By Section 5 this means that the root edge is the
unique length-one cycle loop. Delete its directed root halfedge `r` and its mate `alpha(r)`.
The result is again a plane tree with `n=e-1` edges.

The orientation of the original root orders the two deletion sites. Let `c_0` be the site of `r`
and `c_1` the site of `alpha(r)` after deletion. Root the tree at `c_0` and mark `c_1`.

If `n>=1`, there are `2n-1` choices with `c_1!=c_0`. If `c_1=c_0`, at most two local cyclic
orders of `r,alpha(r)` in the common gap must be distinguished because `r` is rooted and cannot be
interchanged with its mate. Thus the number of reconstruction records over one corner-rooted tree
is at most

\[
 (2n-1)+2=2n+1.                                               \tag{9}
\]

For `n=0`, there is exactly one rooted one-loop map, also agreeing with the value `2n+1=1`.

### Decoder

Insert the new directed root halfedge at `c_0`, its mate at `c_1`, and use the recorded local order
when the corners coincide. Pair them to form the root loop. This restores the original rotations,
root, and two faces. The same Euler argument as in Class I shows that every decoded map is planar
with two faces.

Class II therefore contains at most

\[
 \operatorname{Cat}_n(2n+1)                                 \tag{10}
\]

maps.

## 8. The singly rooted bound

Classes I and II are disjoint and exhaustive. Adding (8) and (10), with `n=e-1`, gives

\[
\begin{aligned}
 T_e
 &\le \operatorname{Cat}_{e-1}\,e(2e-1)\\
 &=\binom{2e-2}{e-1}(2e-1).                                  \tag{11}
\end{aligned}
\]

The last equality uses

\[
 \operatorname{Cat}_{e-1}=\frac1e\binom{2e-2}{e-1}.
\]

Finally,

\[
 \binom{2e}{e}
 =\frac{(2e)(2e-1)}{e^2}\binom{2e-2}{e-1},
\]

so (11) is exactly

\[
 \boxed{T_e\le\frac e2\binom{2e}{e}.}                       \tag{12}
\]

For `e=1`, both sides equal one. No external planar-map enumeration has entered the proof.

## 9. Adding the second ordered face root

In a singly rooted two-face map, the first directed root halfedge determines the first face. The
other face is uniquely the second face. Its boundary length, counted with multiplicity of directed
halfedge occurrences, is at most the total number `2e` of halfedges. This remains true for bridges:
the two sides of a bridge are distinct directed halfedges, even when they lie on the same face.

Therefore forgetting the second root maps a doubly face-rooted map to a singly rooted map with a
fiber of size at most `2e`. Combining with (12),

\[
 R_{e,0}^{(2)}
 \le2eT_e
 \le e^2\binom{2e}{e}.                                      \tag{13}
\]

The face order is not an additional factor: the first root names the first face and the unique
remaining face is second. The second root is a directed boundary halfedge, exactly as counted by
the fiber above.

This proves (1) with all root conventions explicit.

## 10. Repair of the Werner planar constant

The independently proved rooted-phase injection sends every connected planar Werner
constellation on `E=2N` darts injectively to one of the maps counted by (13), with

\[
 e=2E=4N.                                                     \tag{14}
\]

There is no factorial or color multiplier. The minimal Catalan weight of each triple is at most

\[
 P_0(C)\le4^E=2^e.                                           \tag{15}
\]

Using `binom(2e,e)<=4^e`, equations (13)--(15) give

\[
\begin{aligned}
 S_{N,0}
 &\le e^2\binom{2e}{e}\,2^e\\
 &\le e^28^e\\
 &=16N^2\,4096^N.                                            \tag{16}
\end{aligned}
\]

For `N>=2`,

\[
 16N^2\le8^N,                                                \tag{17}
\]

with equality at `N=2` and a ratio induction thereafter. Hence

\[
 S_{N,0}\le32768^N.                                         \tag{18}
\]

For `N=1`, at most `(2!)^2=4` choices of `A,B` are possible, `C` is forced, and
`P_0(C)=1`, so (18) also holds.

The positive-genus tree--cotree argument, which does not use the repaired planar step, gives

\[
 S_{N,h}\le4096^N N^{43h}le32768^N N^{43h}qquad(h\ge1).    \tag{19}
\]

Combining (18)--(19) restores the proposed all-genus bound

\[
 \boxed{S_{N,h}\le32768^N N^{43h}}                           \tag{20}
\]

for all `N>=1,h>=0`. Finally,

\[
 \log(32768^2/18)=30\log2-\log18
 =17.9040436589\ldots<18,                                    \tag{21}
\]

so every integer `m>e^18` satisfies `32768<sqrt(18m)`.

Equations (13) and (16) are the only repairs needed in the planar branch. The false refined
coefficient from the earlier artifact is not used.

## 11. Exact claims and implication hashes

Hashes below are `sha256(statement.strip())` with the statements quoted exactly.

### 11.1 Singly rooted lemma

> For every integer e>=1, the number T_e of isomorphism classes of connected oriented planar maps
> with e edges, exactly two faces, and one distinguished directed halfedge satisfies
> T_e<=(e/2) binom(2e,e).

Exact hash:
`sha256:99b4fc8a1b6c08ed9a36942e4f9012a7dc1e42b5820c14a926b83de65cd09ce6`.

### 11.2 Doubly face-rooted planar lemma

> For every integer e>=1, the number R_(e,0)^(2) of isomorphism classes of connected oriented
> planar maps with e edges, exactly two ordered faces, and one distinguished directed boundary
> halfedge on each face satisfies R_(e,0)^(2)<=e^2 binom(2e,e).

Exact hash:
`sha256:0f07c313c810842eb7e0eb912962eea4b0895adedaa10ba4cac9dea0aaaf42c8`.

### 11.3 Repaired route implication

> The lossless rooted Werner constellation injection, the planar doubly face-rooted map bound, the
> positive-genus tree-cotree count, and the minimal Catalan weight bound jointly imply that in the
> regime m>e^18 the total minimal Catalan weight of connected admissible genus-h triples ABC=rho
> is at most 32768^N N^(43h) for every N and h, with 32768<sqrt(18m).

Exact hash:
`sha256:64b8e9fb8161425c5f94b416af059f8e5ce623c14bc58f3fa7137198a5f1bc99`.

The unchanged target-node claim has exact hash

`sha256:918abca3f6ba28a5ad1d894a5b9e917cc5114081c8a7fcdd16dc28c78d0bb603`.

## 12. Proposed DAG integration (not applied)

No canonical YAML is edited.

1. Register an atomic node such as `HEXT.werner-planar-two-boundary-rooted-map-count` with the
   exact claim and hash in Section 11.2. Keep it at most `CONJECTURED` until an independent agent
   audits the selector, the repeated-corner decoders, the Catalan count, and both root conventions.
2. Preserve the earlier weighted-count artifact and its independent review as the record of the
   failed formula. Link this repair as the replacement planar proof; do not silently rewrite the
   negative finding.
3. In `HEXT.werner-two-boundary-constellation-count`, register a route with load-bearing premises
   including:
   - `HEXT.werner-contraction-skeleton-ribbon-injection`;
   - `HEXT.werner-minimal-catalan-weight`;
   - the new planar node in item 1; and
   - the independently reviewed positive-genus weighted-count node, or an atomic ordinary
     positive-genus tree--cotree count from which it follows.
4. Use Section 11.3 as the route implication. Keep both the route and target node at most
   `CONJECTURED` until a different reviewer checks this artifact and the assembled dependency
   chain at their exact hashes.
5. After that independent review, the route and unchanged target claim may promote according to
   the DAG protocol. This structural promotion would still not promote
   `HEXT.same-tuple-werner-centered-bound`: compatible label components and the two-component
   sector remain separate load-bearing gates.

## 13. Scope

- The proof counts orientable combinatorial maps up to root-preserving isomorphism. It neither
  assumes labeled vertices nor divides by automorphism weights.
- Loops, parallel edges, bridges, coincident insertion corners, and the zero-edge intermediate
  tree are explicit in Sections 4--7.
- The first root halfedge orders the two faces; the factor `2e` in Section 9 is only the second
  directed face root.
- The planar deletion is a counting code, not a physical Werner surgery and not an equality-graph
  operation.
- The result repairs only the structural minimal-Catalan count. It supplies no equality-component
  theorem, no two-component centered-moment analysis, and no spectral probability bound.
- The absolute-unbounded extensive result is separate. Full-size extensive Question 3 remains
  **OPEN**.

