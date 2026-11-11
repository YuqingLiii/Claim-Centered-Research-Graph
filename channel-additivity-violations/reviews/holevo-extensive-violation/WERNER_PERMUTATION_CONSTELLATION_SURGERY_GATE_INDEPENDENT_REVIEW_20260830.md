# Independent review: Werner permutation constellation and surgery gate

Date: 2026-08-30

Reviewer: independent Codex review context `/root/su3_shorter_route`.

## Independence and scope

I did not author `WERNER_PERMUTATION_CONSTELLATION_SURGERY_GATE_20260830.md` or the five new
proposer-side claims reviewed below. I reconstructed the finite permutation algebra, incidence
ribbon surface, Euler exponent, local surgery, recursive subclass count, and repeated-edge
obstruction independently. I used no web access and no large computation. I did not edit canonical
YAML; this report is the only project file created by the review.

This review covers exactly:

1. `HEXT.werner-contraction-skeleton-ribbon-injection`;
2. `HEXT.werner-constellation-euler-deficit`;
3. `HEXT.werner-common-cycle-local-surgery`;
4. `HEXT.werner-ab-reducible-subclass-count`;
5. `HEXT.werner-pairwise-surgery-obstruction`;
6. retirement of route `explicit-handle-stack-route` in
   `HEXT.werner-minimal-skeleton-map-bound`; and
7. the present OPEN status of `HEXT.werner-two-boundary-constellation-count` and
   `HEXT.werner-boundary-preserving-genus-reduction`.

It does not review or prove the full same-tuple centered bound.

## Executive verdict

The five mathematical claims **PASS** at the exact claim hashes below. The encoding, Euler, local
surgery, and repeated-edge obstruction nodes may promote to `PROVED`. The recursive-subclass claim
also passes mathematically, but its `d^(-2)` handle cost depends on the Euler claim and its component
loss depends on the recovered-arrow surgery claim. For a protocol-complete promotion, it should
first receive a route whose premises include the encoding, Euler-deficit, and common-cycle-surgery
nodes (or equivalently duplicate the external Weingarten assumption and all load-bearing lemmas at
node level). Once those premises and that implication are linked, it may promote to `PROVED` without
further mathematics.

Retiring the old favorable `2N`-ordinary-edge generic-map route is correct. Its attached proof
cannot use the amended exact ribbon premise: the actual incidence realization has `4N` ordinary
edges. However, the evidence does **not** exhibit a Werner mass violating the numerical implication,
and the proposer artifact explicitly says the desired structured count may still be true. Thus the
route's current `REFUTED` assessment overstates the evidence under the DAG protocol. The route
should remain retired but have an `OPEN` implication assessment, with the failed `2N` application
recorded as evidence rather than as a counterexample. The node-level `OPEN` assessment is correct.

Both replacement interfaces remain honestly `OPEN`.

## Protocol, sources, and exact hashes

I read the governing protocols in full:

| file | SHA-256 |
|---|---|
| `DAG_PROTOCOL.md` | `d8775b511431e6e9dc7a5be6200af80bd612e7e7d5f5ff10bb14ef748791a095` |
| `FILE_PROTOCOL.md` | `d9d6fb57a26fef3b70fc05bda74a29101d83a43df60e06eaeb345e76980fc595` |

Reviewed prose and external source bindings:

| file | SHA-256 |
|---|---|
| `artifacts/WERNER_PERMUTATION_CONSTELLATION_SURGERY_GATE_20260830.md` | `c52f59c7e301a154925149689b13897a54cf462bf9674ef16105f9a2dd3d1a88` |
| `artifacts/WERNER_MINIMAL_SKELETON_MAP_COUNT_20260830.md` | `a1c0d7ad068f7dbe33175abd7fbb41bc115125c1fd58ac6ba5461feab3ebe710` |
| `reviews/WERNER_MINIMAL_SKELETON_MAP_COUNT_INDEPENDENT_REVIEW_20260830.md` | `cf3e5e60860cf2bebc1f22660fafac5b0b0a5d07466cedc6d9c150f1b988bf6c` |
| `artifacts/primary-sources/collins-matsumoto-1701.04493.pdf` | `42becfc0db3534ade549855727aa759fe8531b95c49d99851a56f53515f2d172` |

I visually checked PDF page 8, Theorem 2.7, and page 10, Lemma 3.3. The theorem gives

`(-1)^|pi| d^(p+|pi|) Wg^U(pi,d) = sum_(g>=0) #P(pi,|pi|+2g)d^(-2g)`.

Lemma 3.3 identifies the `g=0` coefficient as a positive product of Catalan numbers. The nonzero
minimal term therefore supplies precisely the registered leading power `d^(-p-|pi|)`, with
`|pi|=p-#pi`. The Euler node's external assumption and locator are adequate.

Exact statement and current raw-node hashes are:

| node/object | exact statement hash | raw YAML SHA-256 | verdict |
|---|---|---|---|
| `HEXT.werner-contraction-skeleton-ribbon-injection` claim | `sha256:288e0f5df3ca6a53915325c487648184b9be0ff950c1e52c5db7689468c730f7` | `b4d8d785eeff191108c5b9034a60616545a5a2db83fe3b9abb733eb6b43646d6` | PASS; may promote |
| `HEXT.werner-constellation-euler-deficit` claim | `sha256:c1c37d08c4f0cf37cb698b26a03d48cef0dd668686b71ed3a8391fed63c1d62a` | `80a5530c507ce486903dc0556bd038d59397ebc4ab5bd5411a314076ae9221a3` | PASS; may promote |
| `HEXT.werner-common-cycle-local-surgery` claim | `sha256:19631dc700741544c0bc652095123edb8234aa7524f74745f9c153ba66fb2e3b` | `e95f1bb47772b35f53ad6969c29a7cff249705ddd330f2ed0980c9ba54bfa8b7` | PASS; may promote |
| `HEXT.werner-ab-reducible-subclass-count` claim | `sha256:836a4585dce43dffab7d92921a711a5f376d5c15ade83e491439f2866a817eec` | `b9286991a82900ea998169ff65cb382c5c4d83a8626054691d94fe0e54e63100` | mathematical PASS; add route/premises before promotion |
| `HEXT.werner-pairwise-surgery-obstruction` claim | `sha256:9ae3d0d9e612b1a5e965a9438e02577b0ffa038ad35bd570999ef227ba048d1b` | `5b1ab195bb036a74fb98673c1680c8088ff617f464bc79b15a3a940e619fa16a` | PASS; may promote |
| retired `explicit-handle-stack-route` implication | `sha256:3402909496a53e97299edc96799cfb442eb02f2018827316443a8100022088fa` | node file `77d90da4ac91acd62378afb5243e44847099e047c575949f317cb3729541cdab` | retirement PASS; `REFUTED` level not licensed |
| `HEXT.werner-minimal-skeleton-map-bound` claim | `sha256:3402909496a53e97299edc96799cfb442eb02f2018827316443a8100022088fa` | same node file | honestly `OPEN` |
| `HEXT.werner-two-boundary-constellation-count` claim | `sha256:918abca3f6ba28a5ad1d894a5b9e917cc5114081c8a7fcdd16dc28c78d0bb603` | `f91a39d0a6b08a2202a5701933f1760ce347145b03ae493d67611016aab09eb4` | honestly `OPEN` |
| `HEXT.werner-boundary-preserving-genus-reduction` claim | `sha256:da2372c1444105ffdc94c2170774c956ce455e70d63c013b3d0ac9f2fcf0644b` | `6b160a9196a7fd8f26366a79efa44ccc912e8e0f9bd8154ce6d3638c15c43843` | honestly `OPEN` |

## Findings

### Finding WPCS-IR-01 — PASS: exact finite indices and inverse constellation coordinates

**Applies to:** encoding claim hash
`sha256:288e0f5df3ca6a53915325c487648184b9be0ff950c1e52c5db7689468c730f7`.

In the two traces, the unstarred row variables are correctly indexed by

`r(A_i)=y_i`, `r(V_i)=w_i`,

while the starred row of physical slot `s` is `r(Js)`. The unstarred columns are

`q(A_i)=x_(i+1)`, `q(V_i)=z_(i+1)`,

and the starred column of slot `s` is `q(Ks)`, because
`K(V_i)=A_(i-1)` and `K(A_i)=V_(i-1)`. Hence the row and column delta constraints have exactly
`#(J sigma)` and `#(K tau)` loops. There is no reversal or off-by-one error in the physical index
model.

For composition read from right to left,

`A=J sigma^(-1)`, `B=sigma K tau sigma^(-1)`, `C=sigma tau^(-1)`

gives

`ABC = J K = rho`.

Conversely `A^(-1)J=sigma`, and then `C^(-1)A^(-1)J=tau`. Thus the map is injective and
surjective onto triples satisfying the displayed formulas. It introduces no choice of a separate
edge ordering.

I independently tested these identities for 600 random pairs `(sigma,tau)` at `1<=N<=6`; every
inverse and cycle-count identity passed.

**Verdict:** PASS.

### Finding WPCS-IR-02 — PASS: halfedge realization has two rho faces and 4N ordinary edges

**Applies to:** the same encoding claim.

The realization has, for each of the `E=2N` constellation darts `s`, one `A--B` edge with
halfedges `a_s,bar(a)_s` and one `B--C` edge with halfedges `b_s,bar(b)_s`. It therefore has
`2E=4N` ordinary ribbon edges and `4E=8N` halfedges.

With face permutation equal to vertex rotation after edge reversal, one obtains

`a_s -> b_s -> bar(b)_(Cs) -> bar(a)_(BCs) -> a_(ABCs)=a_(rho s)`.

Every face orbit visits the four halfedge types in this order. Consequently faces are in bijection
with the two cycles of `rho`; each has `4N` halfedges. Roots at `a_(V_0)` and `a_(A_0)`, together
with the face direction and the two incidence-edge colors, recover every physical dart and both
ordinary edges attached to it. This is enough to exclude an additional `(2N)!` decoration.

The random checks in Finding 1 also constructed the full `8N`-halfedge permutations. Every case
had exactly two face cycles of length `4N` and the claimed component orbits.

**Verdict:** PASS. The former `2N` ordinary-edge application is definitively incorrect, while the
lossless/no-factorial part is correct.

### Finding WPCS-IR-03 — PASS: Euler loop deficit and minimal Weingarten power

**Applies to:** Euler claim hash
`sha256:c1c37d08c4f0cf37cb698b26a03d48cef0dd668686b71ed3a8391fed63c1d62a`.

The incidence surface has

`V=#A+#B+#C`, `E_rib=2E`, and `F=#rho=2`.

Its connected components are the orbits of `<A,B,C>`. Since `rho=ABC` lies in this group, every
component is a union of entire `rho` cycles; hence `c` is one or two. For total genus `h`, Euler's
formula is exactly

`#A+#B+#C+2-2E = 2c-2h`.

Cycle conjugacy gives `#A=#(J sigma)`, `#B=#(K tau)`, and
`#C=#(sigma tau^(-1))`. For label degree `p_v`, the visually checked external theorem gives the
minimal factor `d^(-p_v-|pi_v|)`, where `|pi_v|=p_v-#pi_v`. Since `sum_v p_v=E` and the global
`C` is the block sum of the label permutations, the product is `d^(-2E+#C)`. Multiplication by
the exact row/column loop factor yields

`d^(#A+#B+#C-2E)=d^(2c-2h-2)`.

For `c=1` this is exactly `d^(-2h)`. For `c=2` it is `d^(2-2h)`; the claim and artifact correctly
avoid identifying that entire sector with return words.

**Verdict:** PASS with an adequate archived primary-source assumption.

### Finding WPCS-IR-04 — PASS: common-cycle surgery and recovered-arrow support

**Applies to:** surgery claim hash
`sha256:19631dc700741544c0bc652095123edb8234aa7524f74745f9c153ba66fb2e3b`.

For `t=(xy)`, the `A--B` update satisfies

`(At)(tB)C=ABC=rho`.

If `x,y` are in one `A` cycle, right multiplication by `t` splits that cycle; if they are in one
`B` cycle, left multiplication splits a cycle because `tB` is conjugate to `Bt`. Thus the vertex
cycle sum increases by exactly two. With `E,F,c` fixed and both constellations connected, Euler's
formula forces `h'=h-1`. If the move splits the surface into two components, the Euler gain can
instead increase `c`; the node correctly retains connectedness as a load-bearing hypothesis.

Using the exact inverse coordinates,

`sigma'=t sigma`, `tau'=C^(-1)tC tau`.

Left multiplication by a transposition changes precisely the arrows whose old images are its two
support points, hence at most two `sigma` and two `tau` arrows. The `B--C` update
`(A,Bt,tC)` has `sigma'=sigma` and the same displayed `tau'`, so it changes at most two column
arrows. These are structural moves; the artifact correctly warns that the modified pairings need
not preserve the original coloring.

**Verdict:** PASS; no hidden admissibility or universality claim.

### Finding WPCS-IR-05 — MATHEMATICAL PASS: recursive subclass factors

**Applies to:** subclass claim hash
`sha256:836a4585dce43dffab7d92921a711a5f376d5c15ade83e491439f2866a817eec`.

The lexicographically chosen forward reduction makes the endpoint and ordered transposition list
a code for each subclass member. Given a planar endpoint and one transposition, the inverse update
is again `(A',B')->(A't,tB')`; therefore no direction flag is required. At most
`binom(E,2)^h=binom(2N,2)^h` histories occur.

One step replaces at most two row-pairing and two column-pairing equality edges. After `h` steps,
delete the at most `4h` affected edges from both endpoint graphs. Each deletion raises the number
of components by at most one, and restoring edges only merges. The assumed planar endpoint bound
`c(H)<=N+2` therefore gives `c(H_original)<=N+2+4h`, and hence the label loss per handle is at
most `m^4`.

The surgery keeps `C` fixed, so its minimal Möbius/Catalan coefficient is unchanged. Combining

`binom(2N,2) <= 2N^2`, `m^4`, and `d^(-2)`

gives exactly `2m^4N^2/d^2` per handle. For fixed `m` and `N<=c_m log d`, its supremum tends to
zero. No extra monotone-path factor is hidden inside this per-handle count.

The subclass is genuinely nonempty: at `N=3`, `sigma=tau=id` has genus one, the registered
`(V_0 A_0)` surgery reaches genus zero, and its endpoint equality graph has five components,
exactly `N+2`.

**Verdict:** the mathematics passes. Before `PROVED`, register the encoding, Euler and surgery
claims as route premises (or duplicate their complete assumptions). The current route-free node
does not make its load-bearing internal and external dependencies machine-visible.

### Finding WPCS-IR-06 — PASS: universal quantifier in the repeated-edge obstruction

**Applies to:** obstruction claim hash
`sha256:9ae3d0d9e612b1a5e965a9438e02577b0ffa038ad35bd570999ef227ba048d1b`.

For the actual admissible coloring `lambda(V_i)=1`, `lambda(A_i)=2` and
`sigma=tau=id`, one has `A=J`, `B=K=Jrho`, `C=id`. When `N` is odd,

`K^2=rho^2`, `K^N=J`,

so `K` is one `2N`-cycle and `<J,K>` is transitive. The cycle counts give genus `(N-1)/2`.

The universal quantifier over the first split is complete: every nontrivial `A` cycle is exactly
one pair `{V_i,A_i}`, while all points lie in the unique `B` cycle. Hence every allowed first
`A--B` surgery is one of the `N` transpositions `t_i=(V_i A_i)`, with no other case omitted.

For each `i`, `Jt_i` has two singleton points and the other `N-1` pairs, while `t_iK` consists of
two `N`-cycles. The two members of every remaining `J` pair are `K^N` apart and land in opposite
new `B` cycles. Thus there is no further nontrivial common `A--B` pair. Since `C=id` has only
singletons, no `B--C` move exists. Any remaining `Jt_i` pair connects the two `B` cycles, so the
new constellation stays connected. Euler then gives `(N-3)/2>0` for every odd `N>=5`.

I exhaustively checked every first split for `N=5,7,9,11`; all connectivity, genus, and empty
common-pair assertions agree with the proof.

**Verdict:** PASS. This refutes only the stated support-two common-cycle induction and leaves
higher-support surgery and the centered target open.

### Finding WPCS-IR-07 — retirement is necessary, but `REFUTED` overstates the implication evidence

**Applies to:** retired route implication and node claim hash
`sha256:3402909496a53e97299edc96799cfb442eb02f2018827316443a8100022088fa`.

The attached old proof applies the generic rooted-map estimate with `L=E=2N` ordinary edges. The
exact halfedge construction proves that the actual incidence map has `L=2E=4N` ordinary edges.
Substitution into the same generic count changes the map exponential from `16^(2N)` to
`16^(4N)`. With the independent minimal Catalan factor `16^N`, the planar base becomes

`16^(5N)=1048576^N`,

not the claimed `4096^N`; the polynomial handle factor also uses `8L=32N`, not `16N`. Therefore
the proof linked to `explicit-handle-stack-route` cannot establish its implication from the
amended exact premise. Retirement and the `route-retired` event are correct, and the abstract
ordinary-map theorem is unaffected.

However, neither the exact edge count nor the large generic upper bound is a counterexample to
the numerical statement that the structured Werner mass might satisfy the smaller bound by a
sharper argument. Section 9 explicitly says the desired count is not shown false. Under
`DAG_PROTOCOL.md`, `REFUTED` applies to the route implication, not merely to one failed proof
instantiation. The current `basis.counterexamples` therefore over-propagates the failure.

**Verdict:** keep the route retired, but change its assessment from `REFUTED` to `OPEN` and record
the 4N correction as failure evidence. Keep the node `OPEN`. The obsolete
`independent-conditional-map-bound-review` frontier may be removed once this finding is linked;
the live work is already owned by the two replacement OPEN nodes.

### Finding WPCS-IR-08 — PASS: both replacement interfaces remain honestly OPEN

**Applies to:** exact claims
`sha256:918abca3f6ba28a5ad1d894a5b9e917cc5114081c8a7fcdd16dc28c78d0bb603`
and `sha256:da2372c1444105ffdc94c2170774c956ce455e70d63c013b3d0ac9f2fcf0644b`.

For the weighted-constellation count, the generic `4N`-edge estimate is much too large at the
target base. Proposition 3 supplies polynomial-per-handle histories only for the recursively
`A--B`-reducible subclass, and Finding 6 gives actual positive-genus skeletons outside a complete
pairwise reduction. No argument bounds the total Catalan weight of every connected admissible
triple by `D^N N^(alpha h)` with `D<sqrt(18m)`. The count node is honestly `OPEN`.

For universal boundary-preserving genus reduction, Lemmas 1--2 cover only common-cycle pairs and
can lose connectedness; the repeated-edge family proves that these moves can stall. No support
three move, four-endpoint switch, universal constants `a,L`, or lift back to bounded changes of
physical tuple-label incidences has been supplied. The genus-reduction node is honestly `OPEN`.

**Verdict:** retain both OPEN levels, caveats, and live frontiers.

## Independent checks performed

Without modifying project evidence, I:

- reconstructed the four matrix-entry index families and both loop permutations;
- verified the constellation inverse and cycle identities for 600 random finite permutation pairs;
- explicitly constructed the `8N` halfedge face permutation and recovered the two rooted faces;
- checked the Euler exponent against the archived primary Theorem 2.7;
- verified both surgery inverses and recovered-arrow supports algebraically;
- recomputed every history, label-component, Catalan, `N`, `m`, and `d` factor in Proposition 3;
- exhaustively checked all first splits of the repeated-edge obstruction for four odd sizes; and
- recomputed the old route's constants at the corrected `4N` ordinary-edge count.

## Promotion and repair instructions

At the exact hashes in this report:

1. promote `HEXT.werner-contraction-skeleton-ribbon-injection` to `PROVED`;
2. promote `HEXT.werner-constellation-euler-deficit` to `PROVED`;
3. promote `HEXT.werner-common-cycle-local-surgery` to `PROVED`;
4. add a route from those three claims to `HEXT.werner-ab-reducible-subclass-count`, then promote
   its reviewed implication and node to `PROVED`;
5. promote `HEXT.werner-pairwise-surgery-obstruction` to `PROVED`;
6. preserve retirement of `explicit-handle-stack-route`, but replace its unsupported `REFUTED`
   implication assessment by `OPEN` failure evidence; and
7. leave `HEXT.werner-minimal-skeleton-map-bound`,
   `HEXT.werner-two-boundary-constellation-count`, and
   `HEXT.werner-boundary-preserving-genus-reduction` at `OPEN`.

No aggregate, centered-spectrum, or extensive-violation theorem follows from this review.
