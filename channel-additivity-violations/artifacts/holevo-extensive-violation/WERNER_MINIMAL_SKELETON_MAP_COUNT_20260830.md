# Werner finite-\(d\) gate: minimal contraction-skeleton map count

Date: 2026-08-30

Status: proposer-side Question 3 artifact. No canonical YAML is changed. This note proves an
abstract fixed-genus rooted-map count and a paired-stack label-entropy bound. Together they give
the required `C_0^N N^{O(h)}` estimate **conditional on two explicit Werner interfaces**: a
lossless genus-preserving contraction-skeleton ribbon encoding and a paired-stack certificate after handle
slicing. Neither interface is derived from the matrix indices here, so the centered-spectrum node
is not promoted and remains mathematically unresolved.

No web access and no numerical computation are used.

## 1. Outcome

Let `N=2k` be the even trace-moment order. The completed abstract estimate is:

> A two-boundary orientable ribbon skeleton with `E=2N` ribbons and genus `h` has at most
> \[
>  64N^3(2N+1)\,256^N(16N)^{3h}
> \tag{1}
> \]
> rooted topological shapes. Under the lossless skeleton-to-shape interface below, each bare
> skeleton has total minimal Möbius/Catalan weight at most `16^N`. If its `h` handle-slicing
> operations leave a planar paired-stack certificate for the tuple labels, then the number of
> compatible label assignments is at most
> \[
>  m^{N+4+8h}.
> \tag{2}
> \]

After the moment normalization `m^{-2N}` and the topological factor `d^{-2h}`, the resulting
nonreturn minimal-skeleton absolute mass is bounded by

\[
 \boxed{
 \mathcal B_{N,h}^{\min}
 \le
 64N^3(2N+1)m^4\left(\frac{4096}{m}\right)^N
 \left(\frac{m^8(16N)^3}{d^2}\right)^h.}
\tag{3}
\]

The constants are deliberately loose but are small enough for the project regime. Since
`ln m>18` and `eta>=0`, the exact definition of `h_W` gives

\[
 h_W^2
 =\left(\frac{18(1+\eta)^2}{m}
       +\frac{81(1+\eta)^4}{m^2}\right)(1-m^{-2})
 \ge\frac{18}{m}(1-m^{-2}).
\]

Therefore

\[
 \frac{4096/m}{h_W}
 \le
 \frac{4096}{\sqrt{18m}\sqrt{1-m^{-2}}}
 <0.12
\tag{4}
\]

at the smallest allowed `m` and nonnegative `eta`. Also, for `N<=c_m log d`,

\[
 \frac{m^8(16N)^3}{d^2}=o_m(1).
\tag{5}
\]

Thus (3), if both interfaces are verified, is sufficient when combined with:

- the return-word base `(3m-4)/m^2`;
- the monotone-Weingarten tail factor
  `theta/(1-theta)` with `theta=6(2N)^{7/2}/d^2`; and
- Markov at an even `N=Theta(log d)`.

The remaining interfaces are precise:

1. every Werner contraction skeleton `(sigma_v,tau_v)_v` must map injectively to an orientable
   two-boundary ribbon map with exactly `2N` ribbons once the rooted trace orders and tuple labels
   are supplied, with no additional ordering factor such as `(2N)!`, and map genus must equal half
   of the matrix-index loop deficit; and
2. after a constant-complexity-per-handle slicing, its generator-label constraints must admit the
   multi-boundary paired-stack certificate of Section 4.

The generic topology and conditional-certificate label counting are proved below. The two bullets
above are exactly the unproved Werner-specific interfaces, and therefore no centered-spectrum
theorem is claimed.

There is some robustness in the first bullet. If inverse reconstruction needs `K^E` finite local
decorations in addition to the uncolored map, equation (3) has `4096K^2` in place of `4096`.
At the smallest allowed `m`, the target still closes for `K<=2`:

\[
 \frac{16384/m}{h_W}<0.48.
\]

Thus one independent binary flag per ribbon is harmless. A factorial edge ordering is fatal, and
the present constants do not certify three or more choices per ribbon.

## 2. Ribbon-map model and terminology

A rooted orientable map is a connected graph cellularly embedded in an oriented closed surface,
with a distinguished directed corner. Loops and multiple edges are allowed. We additionally mark
the two cyclic trace boundaries and their starting corners. The genus is `h`.

For a unitary Weingarten contraction, use the standard double-line picture:

- every unstarred occurrence contributes an oriented ribbon dart;
- the independent row and column pairings `sigma_v,tau_v` glue its two index strands to starred
  occurrence strands;
- the two matrix traces give two distinguished boundary cycles; and
- each closed free index loop contributes a factor `d`.

At minimal monotone length, a skeleton `(sigma_v,tau_v)_v` carries the coefficient

\[
 \prod_v P_0(\pi_v),\qquad
 \pi_v=\sigma_v\tau_v^{-1},
\tag{6}
\]

where `P_0(pi)` is the product of `Cat_(ell-1)` over the cycles of `pi`. Consequently

\[
 P_0(\pi_v)\le4^{p_v},
 \qquad
 \prod_vP_0(\pi_v)\le4^{\sum_vp_v}=4^{2N}=16^N.
\tag{7}
\]

This separates the path multiplicity from the map count; no path-to-map injection is assumed.
Since

\[
 \sum_vp_v=2N,
\tag{8}
\]

there are `E=2N` matched occurrence ribbons.

For an annular nonreturn diagram, genus zero has Euler/loop exponent zero. Each handle lowers the
index-loop exponent by two, giving `d^{-2h}`. Two-disk return diagrams have a `d^2` maximum and
are separated by the existing free-group return estimate.

Everything after this paragraph is a finite combinatorial theorem for maps satisfying this
model. What is not proved is that the full index expansion has a lossless map encoding with
exactly these conventions and no hidden permutation labels.

## 3. A fixed-genus rooted-map count

### Proposition 1

Let `M(E,h;B)` be the number of orientable rooted maps with `E>=1` edges, genus `h`, and `B`
additional marked directed corners. Then

\[
 M(E,h;B)
 \le
 2E(E+1)\,16^E(2E)^B(8E)^{3h}.
\tag{9}
\]

Only the exponential dependence on `E` and polynomial-per-handle dependence matter. The constants
and exponent `3h` are not optimized.

### Proof

We use two standard finite encodings and state the loss in each one.

**Unicellular-core encoding.** Choose canonically a spanning tree of the dual map and delete the
corresponding primal edges. The deletion merges all faces, does not change genus, and does not
disconnect the primal map: the primal edges complementary to a dual spanning tree contain a
primal spanning tree. Suppose the resulting unicellular core has `q` edges and `t=E-q`
edges were deleted. In its unique disk face, the deleted edges are recovered as noncrossing
chords. For `q>=1`, distributing their `2t` cyclically ordered endpoints among the `2q` core
corners costs

\[
 \binom{2t+2q-1}{2q-1}\le 2^{2E}=4^E,
\tag{10}
\]

and their noncrossing matching costs at most `Cat_t<=4^t`. There is no twist choice: an edge
drawn in an oriented disk has the unique orientable ribbon attachment. The exceptional `q=0`
case has one vertex and genus zero and is bounded directly by `Cat_E<=4^E`.

**Trisection slicing.** A rooted orientable unicellular map of positive genus has a canonically
selectable trisection. Slicing its vertex at the three distinguished corners preserves the edge
set and unique face and lowers genus by one. Conversely, the preceding map is reconstructed by
choosing at most three directed corners and one of finitely many cyclic interleavings. Since
`h<=E/2`, there are at most `4E` available corners throughout; one inverse gluing is bounded by
`(8E)^3` choices. Iterating `h` times and using the Catalan bound `4^E` for planar unicellular
maps gives

\[
 U(q,h)\le4^q(8q)^{3h}\le4^q(8E)^{3h}.
\tag{11}
\]

For fixed `q`, multiplying the three exponential factors gives

\[
 4^q\,4^E\,4^t=4^{q+t+E}=16^E.
\tag{12}
\]

There are at most `E+1` choices of `q`. A factor `2E` records the original root corner if it is
not inherited by the core, and `(2E)^B` records the additional marked corners. The canonical
dual tree and slicing choices make the encoding injective. This proves (9). `square`

The only external combinatorial input in Proposition 1 is the trisection statement used above:
one trisection lowers unicellular genus by exactly one without changing `q`, and its inverse is
specified by three corners plus one of finitely many local interleavings. This statement is
exactly strong enough for the factor `(8E)^{3h}`; no fixed-genus asymptotic enumeration is used.

For reference, the exact genus-zero rooted planar-map count is

\[
 \frac{2\,3^E(2E)!}{E!(E+2)!}
 \le2\,12^E,
\tag{13}
\]

so the exponential constant in (9) is conservative.

### Two trace boundaries

Set `E=2N` and use `B=2` for the two marked trace boundaries. Equation (9) gives

\[
 M(2N,h;2)
 \le64N^3(2N+1)\,256^N(16N)^{3h}.
\tag{14}
\]

This is equation (1).

The nonreturn covariance sector addressed here is the connected two-boundary sector. A
two-component, two-disk diagram belongs to the separately controlled return/product sector; no
untracked inflation of the exponential base is absorbed into (14).

## 4. Label entropy after handle slicing

There are `2N` external tuple-label slots:

\[
 V_1,A_1,\ldots,V_N,A_N.
\]

Every cancellation or Haar contraction that joins equal generator labels gives an equality edge
on these slots. The number of valid assignments is at most `m^{c(H)}`, where `c(H)` is the number
of connected components of the equality graph `H`.

The genus-zero two-boundary paired-stack analysis in
`WERNER_REVERSAL_COLLISION_ENCODING_20260830.md` proved

\[
 c(H)\le N+2.
\tag{15}
\]

The following multi-boundary extension is the needed stable form. To avoid confusing this count
with the `B` marked corners in Proposition 1, write `b` for the number of paired boundary rank
maps in a label certificate.

### Proposition 2

Suppose a planar sliced skeleton has `b` paired boundary rank maps. For each map and each sign,
the surviving forward slots occur in increasing physical-index order and the surviving reverse
slots in decreasing physical-index order, up to cyclic cuts; the two lists are identified by an
orientation-reversing cyclic rank map. Suppose these maps partition the unmatched slots, and
every label slot is either:

- joined to a distinct slot by a cancellation/equality edge; or
- unmatched and joined through one of these boundary rank maps.

Then

\[
 c(H)\le N+2b.
\tag{16}
\]

### Proof

On one boundary and for one sign, enumerate the forward unmatched indices in increasing cyclic
order and the reverse unmatched indices in decreasing cyclic order. A cyclic identification has
rank form

\[
 j\longmapsto s-j\pmod r.
\tag{17}
\]

As in the two-boundary proof, a physical fixed slot satisfies

\[
 \alpha(i)+\beta(i)\equiv s\pmod r.
\tag{18}
\]

The rank sum is strictly increasing in `i` and lies in an interval of length below `2r`, so there
are at most two fixed slots of one sign. There are two signs, hence at most four fixed slots per
paired boundary rank map.

Every nonfixed component contains at least two vertices. If `f<=4b` is the total number of fixed
slots, then

\[
 c(H)\le f+\frac{2N-f}{2}
 =N+\frac f2
 \le N+2b.
\tag{19}
\]

This proves Proposition 2. `square`

### Conditional Corollary 3

Assume the Werner ribbon skeleton admits a genus-lowering slicing sequence such that each handle
slicing creates at most four additional paired boundary rank maps **in the induced label
certificate**, and the final genus-zero constraints obey Proposition 2. After `h` slicings,

\[
 b\le2+4h.
\tag{20}
\]

Undoing the slicings and restoring any removed equality constraints can only merge components.
Proposition 2 yields

\[
 c(H)\le N+2(2+4h)=N+4+8h,
\tag{21}
\]

and hence at most

\[
 m^{N+4+8h}
\tag{22}
\]

tuple-label assignments. This is equation (2).

The load-bearing hypothesis is that the planar sliced skeleton really decomposes into the boundary
paired-stack identifications of Proposition 2. This is automatic for the genus-zero
forward/block-reversal collision diagrams already encoded, but it has not been derived here for
every sliced minimal Weingarten skeleton. The numerical bound of four new paired rank maps per
handle is part of this hypothesis, not a consequence of Proposition 1's trisection count.

## 5. Conditional minimal-skeleton bound

Assume the two Werner-specific encoding bullets in Section 1 and take absolute values. Then:

- Proposition 1 gives `64N^3(2N+1)\,256^N(16N)^{3h}` shapes;
- equation (7) gives at most `16^N` total minimal Möbius weight per skeleton;
- Corollary 3 gives `m^{N+4+8h}` labelings;
- the moment coefficient contributes `m^{-2N}`; and
- genus `h` contributes `d^{-2h}` relative to the nonreturn annular scale.

Multiplying these four factors proves

\[
 \mathcal B_{N,h}^{\min}
 \le
 64N^3(2N+1)\,4096^N(16N)^{3h}
 m^{N+4+8h}m^{-2N}d^{-2h},
\tag{23}
\]

which is exactly (3).

Summing `h>=1` is geometric once

\[
 q_{N,d,m}:=\frac{m^8(16N)^3}{d^2}<1:
\tag{24}
\]

\[
 \sum_{h\ge1}\mathcal B_{N,h}^{\min}
 \le
 64N^3(2N+1)m^4\left(\frac{4096}{m}\right)^N
 \frac{q_{N,d,m}}{1-q_{N,d,m}}.
\tag{25}
\]

For fixed `m` and `N<=c_m log d`, `q_{N,d,m}->0`.

The monotone-path result from
`WERNER_FINITE_D_WEINGARTEN_REMAINDER_GATE_20260830.md` multiplies the entire minimal-skeleton
absolute mass by at most

\[
 \frac1{1-\theta_{N,d}},
 \qquad
 \theta_{N,d}=\frac{6(2N)^{7/2}}{d^2}=o(1).
\tag{26}
\]

Thus the two finite-`d` corrections are simultaneously summable.

## 6. Conditional logarithmic-moment closure

This section records the implication only; it is not promoted because the encoding bridge is
unproved.

Let

\[
 r_{\rm ret}
 :=\frac{3m-4}{m^2h_W}
 =\frac1{\sqrt{2m}(1+\eta)}(1+o_m(1))
\tag{27}
\]

and

\[
 r_{\rm map}
 :=\frac{4096/m}{h_W}
 \le\frac{4096}{\sqrt{18m}\sqrt{1-m^{-2}}}.
\tag{28}
\]

In the intended regime both are strictly below one. Choose an even

\[
 N=2k\sim c_m\log d
\tag{29}
\]

with

\[
 c_m>\frac{2}{-\log r_{\rm ret}}.
\tag{30}
\]

Then the return contribution divided by `h_W^N` is `O(d^2r_{\rm ret}^N)=o(1)`. Equations
(25)--(28) give a nonreturn contribution `O_m(N^4r_{\rm map}^N)=o(1)`, with both handle and monotone
tails equal to `1+o(1)` multiplicative corrections. Markov would therefore give

\[
 \Pr\{\|S_U\|>h_W\}\longrightarrow0.
\tag{31}
\]

The conclusion (31) is conditional solely on the two encoding bullets in Section 1. It is not a
proved result of this artifact.

## 7. Failed counting routes and exact losses

### 7.1 Unrestricted permutation enumeration

Summing independently over all `sigma_v,tau_v` gives factorial entropy. At
`N=c_m log d`, a bound `exp(O(N log N))` becomes `d^{O(c_m log log d)}` and eventually defeats
every fixed power of `d^{-1}`. It cannot be repaired by taking `c_m` smaller but fixed.

### 7.2 Counting crossings instead of handles

One handle can support `Theta(N^2)` pairwise crossings. Therefore selecting all crossing pairs
can cost `N^{Theta(N)}` even at fixed genus. Trisection slicing is essential: one operation is
specified by only three corners, independent of the number of drawn crossings.

### 7.3 Demanding a uniform `C^N` coefficient at each genus

The repeated-label monotone paths in the preceding artifact already force `(N-1)^g` at excess
genus `g`. The correct statement permits `N^{O(g)}` and retains `d^{-2g}`.

### 7.4 Treating boundary positions as arbitrary edge labels

Giving all `2N` ribbons independent names would add `(2N)!`. In trace diagrams the occurrence
positions are already ordered along two rooted trace boundaries; once the map and boundary roots
are specified, those positions are read in their given cyclic order. The lossless encoding audit
must verify that no further arbitrary edge permutation is required.

### 7.5 Tree--cotree does not prove the label bound

A tree--cotree decomposition leaves `2h` residual edges representing the surface homology, but
deleting only those edges does not in general planarize an arbitrary embedded graph or preserve
the trace-boundary stack orders. The cut graph also contains a spanning tree, which can have
`Theta(N)` edges. Cutting along that whole tree can create `Theta(N)` boundary incidences, giving
only `b=O(N)` in Proposition 2. This would allow as many as `m^{N+Theta(N)}` labelings and loses the
target at fixed large `m`. Hence the slogan "two edges per handle" is not a proof of Corollary 3;
one needs a vertex-slicing/permutation construction that preserves the monotone physical-index
orders with only `O(1)` new paired rank maps per handle.

## 8. Exact remaining bridge

A direct index-level proof should define, for every balanced edge sequence and every tuple
`(sigma_v,tau_v)`:

1. the oriented ribbons and the two trace boundary permutations;
2. the Euler identity equating matrix-index loop deficit with `2h`;
3. a constant-complexity-per-handle slicing sequence acting on the label constraints;
4. the induced boundary stack words and their reversal rank maps; and
5. an inverse reconstruction showing that the data counted in Propositions 1--2 recover the
   original skeleton without an extra factorial ordering.

The Möbius/Catalan multiplicity is already removed from this interface by (7). Item 1 is standard
unitary ribbon-graph bookkeeping but still needs an explicit inverse because the two trace orders
must replace arbitrary edge labels. Items 3--5 are the real same-tuple interface: they must
preserve the external generator-label slots through the slicing. An explicit permutation
construction should settle the gate one way or the other.

The smallest useful next lemma can be stated without the provisional constant four:

> **Boundary-preserving genus-reduction lemma (missing).** There are universal integers `a,L`
> such that every connected minimal Werner skeleton of loop-defect `2h` can be changed into a
> genus-zero forward/reversal skeleton by at most `ah` local permutation surgeries. Each surgery
> changes at most `L` tuple-label equality incidences, while the two rooted trace permutations are
> kept fixed.

If this holds, delete the at most `aLh` affected equality edges before applying the genus-zero
paired-stack bound (15). Restoring them can only merge components, so

\[
 c(H)\le N+2+aLh.
\]

The shape count then gives a handle ratio

\[
 \frac{m^{aL}(16N)^3}{d^2},
\]

which is `o_m(1)` for every fixed `a,L,m` and `N<=c_m log d`. Thus **any universal local-surgery
constant is sufficient**; the particular provisional value `aL=8` used in (2)--(3) is not
load-bearing. Ordinary unicellular trisection proves the analogous unrooted topological surgery,
but not preservation of the two physical trace permutations. That preservation is the exact
additional assertion needed here.

## 9. Quantifiers and scope

- Proposition 1 is a deterministic count for every finite `E,h,B`.
- Proposition 2 is a deterministic equality-graph bound under the stated paired-stack
  certificate. Corollary 3 is conditional on the explicitly stated slicing interface.
- The intended quantifiers in the conditional implication are: fixed integer `m` with
  `ln m>18`, fixed `eta>=0`, `d->infinity`, and even `N<=c_m log d`.
- Equation (3) is conditional on the Werner contraction-skeleton encoding satisfying both bullets in
  Section 1.
- The constants may be improved, but `4096` is below the Werner allowance for `ln m>18` with
  ratio less than `0.12` already at the smallest allowed `m`.
- No high-probability norm bound or generic Haar counterexample is proved.
- The absolute-unbounded extensive-violation result is separate; only the unresolved full-size
  Question 3 Werner subgate is discussed.

## 10. Candidate atomic DAG claims (not applied)

No canonical YAML is edited. Suggested claims, all at most `CONJECTURED` pending review:

1. `HEXT.rooted-orientable-map-handle-count`
   - claim: Proposition 1, with shape count
     `2E(E+1)16^E(2E)^B(8E)^{3h}`;
   - evidence: Section 3.
2. `HEXT.multiboundary-paired-stack-label-components`
   - claim: under the stated certificate, `c(H)<=N+2b`;
   - evidence: Proposition 2.
3. `HEXT.werner-minimal-catalan-weight`
   - claim: `prod_v P_0(pi_v)<=16^N` whenever `sum_v p_v=2N`;
   - evidence: equation (7).
4. `HEXT.werner-contraction-skeleton-ribbon-injection`
   - claim: Section 1 bullet 1 holds, possibly with at most one binary local flag per ribbon;
   - status: `CONJECTURED`; an inverse permutation construction is still required.
5. `HEXT.werner-handle-sliced-paired-stack-certificate`
   - claim: Section 1 bullet 2 holds with `b<=2+4h`;
   - status: `CONJECTURED`; tree--cotree alone is insufficient by Section 7.5.
6. `HEXT.werner-boundary-preserving-genus-reduction`
   - weaker sufficient claim: the missing lemma in Section 8 holds for some universal `a,L`;
   - status: `CONJECTURED`; any finite `aL` suffices at fixed `m`.
7. `HEXT.werner-minimal-skeleton-map-bound`
   - conditional claim: items 1--4 plus either item 5 or item 6 imply the required
     `C_0^N N^{O(h)}d^{-2h}` bound; equation (3) is the `aL=8` version, with `4096` replaced by
     `16384` if the binary decoration allowance is used;
   - status: no higher than `CONJECTURED`.
8. `HEXT.same-tuple-werner-centered-bound`
   - proposed route: return estimate + monotone-tail lemma + items 4--7 imply the logarithmic
     moment conclusion in Section 6;
   - do not promote until the encoding is derived and independently audited.
