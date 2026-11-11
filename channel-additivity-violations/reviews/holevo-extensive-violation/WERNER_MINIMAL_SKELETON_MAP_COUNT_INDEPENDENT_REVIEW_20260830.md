# Independent review: Werner minimal-skeleton map count

Date: 2026-08-30

Reviewer: independent Codex review context `/root/su3_shorter_route`.

Independence declaration: this review did not author
`WERNER_MINIMAL_SKELETON_MAP_COUNT_20260830.md` or the four proposer-side claims reviewed below.
The review reconstructed the combinatorial and algebraic estimates from the checked-in text.  It
did not use web access and did not edit canonical YAML.

## 1. Scope and inspected materials

Primary object:

- `holevo-extensive-violation/artifacts/WERNER_MINIMAL_SKELETON_MAP_COUNT_20260830.md`, file
  SHA-256
  `a1c0d7ad068f7dbe33175abd7fbb41bc115125c1fd58ac6ba5461feab3ebe710`.

Proposer nodes:

| node | file SHA-256 |
|---|---|
| `HEXT.rooted-orientable-map-handle-count` | `f9df01192d9bf62ba3dbc45609174d3f1dab81b3d55012503cbeb7200a2968d2` |
| `HEXT.multiboundary-paired-stack-label-components` | `18ea782616fa5fbb3ad125da6b624c0e709a8f87e71062a7c7dc9e4a92af0874` |
| `HEXT.werner-minimal-catalan-weight` | `3182696676e1b3f8eb9729537ee4deb63815cbd8f1308fc7a1c6536386668c79` |
| `HEXT.werner-minimal-skeleton-map-bound` | `e90f09900052f1d8dd6805a03a35291ee6f8b14e5a9d9a65bb62060537cd7095` |

Open interface nodes:

| node | file SHA-256 |
|---|---|
| `HEXT.werner-contraction-skeleton-ribbon-injection` | `9839dcfaf9c4e587ecb14294d70335a94b7c7038eaa7c56fe412bc2f333c3c7f` |
| `HEXT.werner-handle-sliced-paired-stack-certificate` | `dbcdfec7d8e2814c1876f2699fae473a7b9af49e21c47a7457b947986e9e32b4` |
| `HEXT.werner-boundary-preserving-genus-reduction` | `998122f79ae60673bf9cd528f800fb26f316fd2e3461795e69ffb1bfafc7fcfa` |

The review also inspected the exact genus-zero fixed-slot argument in
`WERNER_REVERSAL_COLLISION_ENCODING_20260830.md`, its independent review finding `STRC-IR-06`,
the degree and minimal-path conventions in
`WERNER_FINITE_D_WEINGARTEN_REMAINDER_GATE_20260830.md`, the locally archived
Collins--Matsumoto primary source already used by
`HEXT.werner-monotone-weingarten-tail-summability`, the exact Werner spectral reduction, and the
current centered-bound node.  No local primary source for the unicellular trisection theorem was
present.

## 2. Exact claim hashes

The following are `sha256(claim.strip())` after YAML folding and CRLF normalization.

| node | exact claim hash | review recommendation |
|---|---|---|
| `HEXT.rooted-orientable-map-handle-count` | `sha256:377fb1d332c6ec920c0c5d33df977946179e93a6139b229886f31db950f00963` | internal count PASS; remain `CONJECTURED` pending a primary trisection source and source-level review |
| `HEXT.multiboundary-paired-stack-label-components` | `sha256:70827847a3713182a56d45810adac1c4d1adce022f8ac7e18dca69c7406f7924` | PASS; may promote to `PROVED` |
| `HEXT.werner-minimal-catalan-weight` | `sha256:82a54db26f9887fab15962f597b42c9d9b7c5a50b2dc86c713e0b066cc51cf54` | mathematical PASS; may promote to `PROVED` after adding the explicit archived primary-source assumption |
| `HEXT.werner-minimal-skeleton-map-bound` | `sha256:3402909496a53e97299edc96799cfb442eb02f2018827316443a8100022088fa` | implication PASS; at most `CERTIFIED*` after route/premise repair; not `PROVED` while interfaces are OPEN |
| `HEXT.werner-contraction-skeleton-ribbon-injection` | `sha256:96328efa4bb5a4456d4768d4bd851463cdc4ec60b2f422b8654eb75054e5d4c5` | honestly `OPEN` |
| `HEXT.werner-handle-sliced-paired-stack-certificate` | `sha256:80a963d4bfbe5bfbfc5cebb041b22538d4617dc8ea47e484742a53478a25e6d4` | honestly `OPEN` |
| `HEXT.werner-boundary-preserving-genus-reduction` | `sha256:da2372c1444105ffdc94c2170774c956ce455e70d63c013b3d0ac9f2fcf0644b` | honestly `OPEN` |
| boundary claim `HEXT.same-tuple-werner-centered-bound` | `sha256:c221c71b9f3cb3294d7c9c7d979cf1a154042ea4ec013f95d3fc7955c2c38da5` | unresolved; no promotion |

## 3. Findings

### Finding WMSC-IR-01 — CONDITIONAL PASS: dual-tree reduction and rooted-map constants

**Applies to:** `HEXT.rooted-orientable-map-handle-count`, exact claim hash
`sha256:377fb1d332c6ec920c0c5d33df977946179e93a6139b229886f31db950f00963`.

The internal finite encoding is sound conditional on the quoted unicellular trisection theorem.
Deleting primal edges dual to a dual spanning tree merges all faces, preserves connectedness and
genus, and leaves a unicellular core with `q` edges.  The deleted `t=E-q` edges become noncrossing
chords in the unique disk face.  The endpoint distribution and matching costs are bounded by

\[
 \binom{2t+2q-1}{2q-1}\le4^E,
 \qquad
 \operatorname{Cat}_t\le4^t.
\]

The planar unicellular core contributes `Cat_q<=4^q`.  Hence, for fixed `q`, the three
exponential factors are exactly

\[
 4^q4^E4^t=4^{q+t+E}=16^E.
\]

There are at most `E+1` values of `q`; `2E` safely records a possibly deleted original root; and
`(2E)^B` records the additional directed corners.  Conditional on at most `(8E)^3` inverse data
per genus-lowering slice, this reconstructs

\[
 M(E,h;B)\le2E(E+1)16^E(2E)^B(8E)^{3h}.
\]

At `E=2N,B=2`, the polynomial factor is

\[
 2(2N)(2N+1)(4N)^2=64N^3(2N+1),
\]

while `16^(2N)=256^N` and `(8E)^(3h)=(16N)^(3h)`.  Equation (14) of the artifact is correct.
The extra two-corner marking is conservative even if one trace corner could serve as the map root.

**External-dependency verdict.**  The step asserting that every positive-genus rooted
unicellular map has a selectable trisection whose one-step slicing preserves the edge set and
unique face, lowers genus by exactly one, and is inverted by three corner choices plus at most the
local multiplicity absorbed in `(8E)^3`, is a genuine external theorem.  The repository contains
no archived primary source for it, and the node has no protocol-level `assumptions` entry.  A
primary citation is required by `DAG_PROTOCOL.md`; an unlocated statement that the theorem is
standard is not sufficient for `PROVED`.  A likely bibliographic recollection is not evidence:
the exact version and local multiplicity must be checked against an archived primary source.

**Verdict:** the derivation and constants pass conditionally, but this review does not license a
promotion of the node.  After adding a locatable primary source and explicit assumption, a short
source-level supplemental review is still required.

### Finding WMSC-IR-02 — PASS: multi-boundary fixed-slot and component count

**Applies to:** `HEXT.multiboundary-paired-stack-label-components`, exact claim hash
`sha256:70827847a3713182a56d45810adac1c4d1adce022f8ac7e18dca69c7406f7924`.

For one paired boundary rank map and one sign, list the forward surviving physical indices in
increasing order and the reverse list in decreasing order.  After cyclic cuts the identification
has rank form `j -> s-j mod r`.  At a fixed physical slot, its increasing ranks `alpha(i),beta(i)`
satisfy

\[
 \alpha(i)+\beta(i)=s\pmod r.
\]

Along the intersection of the two physical-index sets both ranks strictly increase.  Their sum is
strictly increasing in `[0,2r-2]`, so one residue class modulo `r` occurs at most twice.  This gives
at most two fixed slots for each sign and at most four for one paired boundary map.  Because the
`b` maps partition their unmatched slots, the total fixed-slot count is at most `4b`.

Every cancellation edge joins distinct slots, and every nonfixed boundary-map edge also joins
distinct slots.  Thus only a fixed slot can form a singleton equality component.  With `2N`
vertices,

\[
 c(H)\le f+{2N-f\over2}=N+{f\over2}\le N+2b.
\]

This proof correctly generalizes the already reviewed `b=1` fixed-slot argument.  It neither
assumes nor proves that a Werner skeleton possesses the certificate; that is kept in a separate
OPEN interface.

**Verdict:** self-contained PASS.  This node may promote to `PROVED` at the reviewed claim hash.

### Finding WMSC-IR-03 — PASS WITH SOURCE-LINK REPAIR: Catalan normalization

**Applies to:** `HEXT.werner-minimal-catalan-weight`, exact claim hash
`sha256:82a54db26f9887fab15962f597b42c9d9b7c5a50b2dc86c713e0b066cc51cf54`.

For active label `v`, the balanced degree `p_v` is the common number of starred and unstarred
occurrences.  Across the product of the two length-`2N` traces there are exactly `2N` unstarred
occurrences, hence

\[
 \sum_vp_v=2N.
\]

At minimal monotone length, the absolute coefficient is

\[
 P_0(\pi_v)=|\operatorname{Moeb}(\pi_v)|
 =\prod_{c\in\operatorname{Cycles}(\pi_v)}\operatorname{Cat}_{|c|-1}.
\]

Since `Cat_(ell-1)<=4^(ell-1)<=4^ell`,

\[
 P_0(\pi_v)\le4^{p_v},
 \qquad
 \prod_vP_0(\pi_v)\le4^{\sum_vp_v}=4^{2N}=16^N.
\]

The use of `4^(p_v)` is deliberately looser than the available `4^(p_v-#cycles)`, but it is
valid.  No Catalan factor is counted twice: the ribbon shape count does not enumerate monotone
paths.

The minimal-path/Möbius identity is an external unitary-Weingarten input.  A local
Collins--Matsumoto primary PDF and exact theorem locators are already registered for the
Weingarten-tail node, but the present route-free Catalan node does not declare that input under
`assumptions`.  The mathematical claim passes; protocol-compliant promotion requires adding the
same explicit primary-source assumption (or a proper route to an established node containing the
needed statement).

**Verdict:** mathematical PASS.  Promote to `PROVED` only after the source-link repair; no new
mathematical review is needed if the added assumption quotes the already archived exact
minimal-path identity without changing the claim.

### Finding WMSC-IR-04 — PASS: conditional mass algebra and binary-decoration constant

**Applies to:** `HEXT.werner-minimal-skeleton-map-bound`, exact claim hash
`sha256:3402909496a53e97299edc96799cfb442eb02f2018827316443a8100022088fa`.

Under the two stated Werner interfaces, the five factors are:

\[
 \begin{array}{c|c}
 \text{source}&\text{factor}\\ \hline
 \text{map shapes}&64N^3(2N+1)256^N(16N)^{3h}\\
 \text{minimal Catalan weight}&16^N\\
 \text{label assignments}&m^{N+4+8h}\\
 \text{moment normalization}&m^{-2N}\\
 \text{loop deficit}&d^{-2h}.
 \end{array}
\]

Their product is exactly

\[
 64N^3(2N+1)m^4
 \left({4096\over m}\right)^N
 \left({m^8(16N)^3\over d^2}\right)^h.
\]

No `m`, `N`, or `d` exponent is missing.  The positive-genus sum is geometric with ratio

\[
 q_{N,d,m}={m^8(16N)^3\over d^2}=o_m(1)
\]

uniformly for `N<=c_m log d`.  One local decoration with `K` choices per each of `E=2N`
ribbons multiplies the planar base by `K^(2N)`, so `4096` becomes `4096K^2`; for a binary flag it
becomes `16384`.  This bookkeeping is correct.

The artifact's alternative local-surgery interface is also algebraically correct.  Deleting at
most `aLh` equality edges raises the component count by at most `aLh`; restoring them can only
merge components.  Any fixed `aL` therefore changes only the handle ratio to
`m^(aL)(16N)^3/d^2=o_m(1)`.

**DAG verdict.**  The node currently records load-bearing OPEN nodes as `node-evidence`, although
`DAG_PROTOCOL.md` reserves that kind for non-load-bearing cross-references.  Its conditional
implication should be represented as a route whose premises include the rooted-map count,
multi-boundary component count, Catalan weight, lossless ribbon injection and explicit
handle-sliced certificate.  The weaker boundary-preserving genus-reduction node belongs to a
separate alternative route whose implication would use the genus-zero component bound.  A route
implication may be reviewed as proved, but the node cannot be `PROVED` while a load-bearing premise
is OPEN.

**Verdict:** the conditional implication passes.  After route/premise repair and the source
repairs in Findings WMSC-IR-01 and WMSC-IR-03, the node is eligible for at most `CERTIFIED*` with
the unresolved Werner interfaces stated as caveats.  It is not eligible for `PROVED` now.

### Finding WMSC-IR-05 — PASS: paired-stack handle exponent

Under the explicit handle-sliced certificate, the initial two paired boundary maps and at most
four new maps per handle give

\[
 b\le2+4h.
\]

Finding WMSC-IR-02 then gives

\[
 c(H)\le N+2b\le N+4+8h,
\]

and hence `m^(N+4+8h)` assignments.  Starting with two rather than the sharper genus-zero value
one is conservative.  The number four is not derived from map trisection and is correctly kept
inside the OPEN Werner-specific interface.  No statement in the artifact silently proves it.

**Verdict:** the fixed-slot consequence is correct conditional on the interface; the interface
itself remains OPEN.

### Finding WMSC-IR-06 — PASS: exact Werner-threshold base comparison

With `A=1+9(1+eta)^2/m`,

\[
 h_W^2=(A^2-1)(1-m^{-2})
 =\left({18(1+\eta)^2\over m}
       +{81(1+\eta)^4\over m^2}\right)(1-m^{-2}).
\]

For `eta>=0`,

\[
 h_W^2\ge {18\over m}(1-m^{-2}),
\]

so

\[
 {4096/m\over h_W}
 \le {4096\over\sqrt{18m}\sqrt{1-m^{-2}}}.
\]

The denominator is increasing for `m>1`.  At the endpoint `m=e^18` the right side is
`0.1191443242114996`; every allowed integer has `m>e^18`, so the strict `<0.12` claim is correct.
Multiplying by four for `K=2` gives `0.4765772968459984<0.48` at that endpoint.  The inequalities
have the advertised, albeit narrow, numerical margins.

For the return sector,

\[
 r_{\rm ret}={3m-4\over m^2h_W}
 ={1\over\sqrt{2m}(1+\eta)}(1+o_m(1)).
\]

Choosing even `N~c_m log d` with `c_m>2/(-log r_ret)` makes the prefactor
`d^2r_ret^N` vanish.  Since `r_map<1`, the nonreturn factor
`N^4r_map^N` vanishes for every fixed positive `c_m`; the handle and monotone-Weingarten ratios
are `o_m(1)`.  The conditional Markov closure is algebraically correct.

**Verdict:** all base comparisons, powers and logarithmic quantifiers pass.  This verifies only
the implication, not either missing encoding interface.

### Finding WMSC-IR-07 — PASS: the three interfaces remain honestly OPEN

**Exact reviewed hashes:**

- ribbon injection:
  `sha256:96328efa4bb5a4456d4768d4bd851463cdc4ec60b2f422b8654eb75054e5d4c5`;
- handle-sliced paired-stack certificate:
  `sha256:80a963d4bfbe5bfbfc5cebb041b22538d4617dc8ea47e484742a53478a25e6d4`;
- boundary-preserving genus reduction:
  `sha256:da2372c1444105ffdc94c2170774c956ce455e70d63c013b3d0ac9f2fcf0644b`.

The artifact does not give an inverse from the uncolored rooted map and finite local flags to all
per-label pairings, does not prove equality between map genus and half the full matrix-index loop
deficit, and does not exclude a hidden factorial edge ordering.  The first interface is therefore
correctly OPEN.

Ordinary topological trisection does not preserve the two physical trace permutations or the
monotone forward/reversal label orders.  The artifact explicitly assumes, rather than derives,
the `b<=2+4h` certificate.  Tree--cotree cutting can create `Theta(N)` boundary incidences and does
not repair this.  The second interface is correctly OPEN.

The weaker bounded local-surgery statement would suffice for the mass estimate, but no universal
support constants `a,L` are constructed or refuted.  It is an honest alternative OPEN node, not a
consequence of Proposition 1.  The third interface is correctly OPEN.

**Verdict:** retain all three levels and frontiers unchanged.  None may promote from this review.

### Finding WMSC-IR-08 — PASS: exact scope and boundary claim

The artifact consistently restricts the map estimate to connected two-boundary nonreturn minimal
skeletons.  Two-disk return diagrams, genus-zero reversal collisions and positive monotone-path
excesses are kept in their previously established interfaces.  The intended limit fixes `m` and
`eta`, sends `d` to infinity, and takes even `N<=c_m log d`.  It does not claim a generic Haar
counterexample, a high-probability norm theorem, or a result for the full coefficient space.

At exact centered-claim hash
`sha256:c221c71b9f3cb3294d7c9c7d979cf1a154042ea4ec013f95d3fc7955c2c38da5`,
the growing-moment route still depends on the OPEN ribbon injection and one of the two OPEN
genus-reduction interfaces.  The centered-spectrum node remains unresolved; no promotion follows.

## 4. Promotion summary

1. `HEXT.multiboundary-paired-stack-label-components` may promote directly to `PROVED` at exact
   reviewed claim hash
   `sha256:70827847a3713182a56d45810adac1c4d1adce022f8ac7e18dca69c7406f7924`.
2. `HEXT.werner-minimal-catalan-weight` may promote to `PROVED` after its node explicitly records
   the already archived primary unitary-Weingarten source/assumption.  Its mathematics does not
   need repair.
3. `HEXT.rooted-orientable-map-handle-count` must remain `CONJECTURED` until an archived primary
   source is linked and independently checked for the exact one-step trisection and inverse local
   multiplicity used by `(8E)^3`.
4. `HEXT.werner-minimal-skeleton-map-bound` has a correct conditional implication but should be
   converted to explicit DAG routes.  After the abstract source repairs it may be `CERTIFIED*`;
   it cannot be `PROVED` while its Werner-specific premises remain OPEN.
5. The three interface nodes and `HEXT.same-tuple-werner-centered-bound` receive no promotion.

No canonical YAML was modified by this review.
