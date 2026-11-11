# Independent review: Werner two-boundary constellation weighted count

Date: 2026-08-30

Reviewer: independent Codex review context `/root/full_size_leakage`.

Independence declaration: this reviewer did not author
`WERNER_TWO_BOUNDARY_CONSTELLATION_WEIGHTED_COUNT_20260830.md`. The review reconstructed the
rooted-map injection, the tree--cotree code, all powers of `2,N,m,d`, and the equality-component
example from the checked-in definitions. It used no web access, no large computation, and made no
canonical YAML change.

## 1. Executive verdict

The rooted two-face constellation injection, absence of a factorial or color multiplier, the
positive-genus spanning-tree/cotree code, the `h>=1` constant calculation, the minimal Catalan
weight, and the monotone-Weingarten multiplier all **PASS**.

The artifact nevertheless does **not** license completion-level promotion of the current claim
`HEXT.werner-two-boundary-constellation-count`. Its planar input (6) is a false equality. Already
at `e=2,v=2`, it gives six rooted planar maps, while the exact rooted-permutation enumeration gives
five. Equations (7)--(8) therefore do not follow from the proof as written. The desired right-hand
side is a plausible and standard upper bound, and the usual correct two-face coefficient would
repair the proof without changing `32768`, but neither that correct formula nor an independent
self-contained proof of the needed upper bound is currently supplied.

Accordingly:

- the current every-`h` claim, exact hash
  `sha256:918abca3f6ba28a5ad1d894a5b9e917cc5114081c8a7fcdd16dc28c78d0bb603`,
  may move from `OPEN` to at most `CONJECTURED`, with the planar repair explicit;
- the narrower positive-genus claim in Section 3, exact hash
  `sha256:300c642a7cab1717445a387e793666fa416ead65bd0731f9be684701d8f30cf6`,
  passes and may be registered and promoted through a protocol-complete route; and
- no finding here promotes `HEXT.same-tuple-werner-centered-bound` or the full-size extensive
  violation. Both retain their present unresolved status.

The equality-graph family is correct as a method obstruction, and it has an even-`N` strengthening
directly inside the even-moment sector. It refutes a genus-independent component allowance, not
the centered spectral bound: its own normalized leading mass is strongly suppressed by its
linearly growing genus.

## 2. Inspected objects and exact hashes

| object | SHA-256 |
|---|---|
| `DAG_PROTOCOL.md` | `d8775b511431e6e9dc7a5be6200af80bd612e7e7d5f5ff10bb14ef748791a095` |
| `FILE_PROTOCOL.md` | `d9d6fb57a26fef3b70fc05bda74a29101d83a43df60e06eaeb345e76980fc595` |
| `artifacts/WERNER_TWO_BOUNDARY_CONSTELLATION_WEIGHTED_COUNT_20260830.md` | `f4d0b8b92366c0aa353b3f7794c9a0b1a5326aa0602ecc9323f6f9a9e51a8bab` |
| raw `nodes/HEXT.werner-two-boundary-constellation-count.yaml` | `0e79a2590f57f164696fcd33e4789da41a2a398761436e8178cd8ea5f7c51030` |
| raw `nodes/HEXT.same-tuple-werner-centered-bound.yaml` | `6f5943d8e564e653e0e0a25caf500ca883131933fdca37d6455a25d6fbacde9e` |

The exact claim hashes below are `sha256(claim.strip())` after YAML folding and line-ending
normalization.

| claim | exact claim hash | review verdict |
|---|---|---|
| current `HEXT.werner-two-boundary-constellation-count` | `sha256:918abca3f6ba28a5ad1d894a5b9e917cc5114081c8a7fcdd16dc28c78d0bb603` | every-`h` completion FAILS pending planar repair; at most `CONJECTURED` |
| current `HEXT.same-tuple-werner-centered-bound` | `sha256:c221c71b9f3cb3294d7c9c7d979cf1a154042ea4ec013f95d3fc7955c2c38da5` | unresolved; no promotion |
| proposed positive-genus weighted count, quoted in Section 3 | `sha256:300c642a7cab1717445a387e793666fa416ead65bd0731f9be684701d8f30cf6` | PASS; may promote through explicit premises |
| proposed ordinary positive-genus count, quoted in Finding WTBC-IR-02 | `sha256:42ebc41b59af9d480ec395ad6188ab95ca22092e3806c5c5284a46f02c2dc8d3` | PASS |
| proposed even identity-pairing obstruction, quoted in Finding WTBC-IR-07 | `sha256:932db446425cb53de07e3a043bac0670aff523e875221f8ea94012e1be3c6be8` | PASS |

## 3. The narrow claim that passes

The exact reviewed statement is:

> For every N>=2 and h>=1, the total minimal Catalan weight of all connected triples ABC=rho of
> genus h is at most 4096^N N^(43h). Consequently, for every integer m>e^18, the fixed constant
> D=4096 satisfies D<sqrt(18m).

Its exact hash is
`sha256:300c642a7cab1717445a387e793666fa416ead65bd0731f9be684701d8f30cf6`.
It is stronger than the admissible-only statement in its structural class, but it is narrower
because it excludes `h=0`. Findings 1--4 below give a complete proof from already proved project
premises.

## 4. Findings

### Finding WTBC-IR-01 — PASS: rooted two-face forgetting is injective

**Applies to:** the positive-genus claims in Section 2 and the injection part of the current
every-`h` claim.

For every constellation dart `s`, the incidence map has the four-step face segment

\[
 a_s\longmapsto b_s\longmapsto\bar b_{Cs}
 \longmapsto\bar a_{BCs}\longmapsto a_{ABCs}=a_{\rho s}.
\]

Thus every face has the periodic halfedge phases

\[
 a, b, \bar b, \bar a.
\]

After forgetting incidence colors, an oriented root on each of the two ordered faces determines
the phase of every halfedge by directed face distance modulo four. The phase distinguishes the
two kinds of halfedges at a `B` vertex as well as the `A` and `C` vertices. Every fourth halfedge,
read from the two roots, restores the fixed physical dart names in the two `rho` orders. The
ordinary edge involution and recovered vertex rotations then restore `A,B,C`.

Both face roots are load-bearing. With them retained, an ordinary-map automorphism fixing the
code fixes every halfedge on both face cycles and is trivial. There is therefore no hidden
`(2N)!`, face-rotation, `2^e`, or `3^e` multiplier. The ordinary incidence map has exactly
`e=4N` edges, not `2N`.

**Verdict:** PASS.

### Finding WTBC-IR-02 — PASS: the tree--cotree code and absence of `r!`

**Applies to:** proposed ordinary positive-genus count hash
`sha256:42ebc41b59af9d480ec395ad6188ab95ca22092e3806c5c5284a46f02c2dc8d3`.

For a connected orientable genus-`h` map with `e` edges and two faces, Euler gives

\[
 V=e-2h.
\]

A spanning tree has `V-1=e-2h-1` edges, hence there are exactly

\[
 r=e-(V-1)=2h+1
\]

non-tree edges. Deterministic depth-first exploration from the first face root selects the tree
and orders the non-tree edges. Deleting them in reverse order leaves the induced plane tree on all
vertices. The reverse data consist of an ordered pair of insertion corners and, conservatively,
one orientation bit per restored edge. A loop whose two ends occupy one old corner is covered by
the orientation bit and the deliberately doubled corner code.

At every stage there are at most `4e` safe corner codes, so one reinsertion costs at most
`32e^2`; each of the two face roots costs at most `4e`. A rooted plane tree with `e-r` edges costs
at most `4^(e-r)<=4^e`. Therefore

\[
 R_{e,h}^{(2)}\le4^e(4e)^2(32e^2)^{2h+1}.
\]

The decoder restores the tree rotation system, then the recorded edges in list order, then the
two roots. Since the list order is fixed by the encoder and explicitly retained by the decoder,
no `r!` factor is missing. Nothing in this counting code is asserted to preserve physical labels
or remain in the constellation image after an intermediate deletion.

The exact reviewed ordinary-count statement is:

> Every connected genus-h two-boundary Werner constellation with E=2N darts injects into a
> connected orientable ordinary map with e=4N edges and two ordered rooted faces; for h>=1 the
> number of such triples is at most 4^e(4e)^2(32e^2)^(2h+1), without a factorial or color
> multiplier.

Its exact hash is
`sha256:42ebc41b59af9d480ec395ad6188ab95ca22092e3806c5c5284a46f02c2dc8d3`.

**Verdict:** PASS.

### Finding WTBC-IR-03 — PASS: positive-genus constants `4096` and `43`

**Applies to:** positive-genus weighted-count hash
`sha256:300c642a7cab1717445a387e793666fa416ead65bd0731f9be684701d8f30cf6`.

For `h>=1`, the polynomial part of the preceding code satisfies

\[
 (4e)^2(32e^2)^{2h+1}
 =512e^4(1024e^4)^h
 \le(2^{19}e^8)^h.
\]

The last inequality is equality at `h=1` and gains the factor `(512e^4)^(h-1)` thereafter.
For every triple, the minimal Catalan weight is at most

\[
 P_0(C)\le4^E=2^e,
\]

where `E=2N` and `e=4N`. Multiplying by the map factor `4^e` gives

\[
 8^e=4096^N.
\]

Moreover

\[
 2^{19}e^8=2^{35}N^8\le N^{43}\qquad(N\ge2).
\]

Thus, for every `N>=2,h>=1`,

\[
 S_{N,h}\le4096^N N^{43h}.
\]

No positive-genus connected triple exists at `N=1`, so the omitted case is vacuous. This proof
does not use the planar coefficient challenged below.

**Verdict:** PASS.

### Finding WTBC-IR-04 — FAIL AS WRITTEN: planar coefficient (6)

**Applies to:** current every-`h` claim hash
`sha256:918abca3f6ba28a5ad1d894a5b9e917cc5114081c8a7fcdd16dc28c78d0bb603`.

The asserted refined coefficient

\[
 \frac{(2e)!}{v!(v-1)!(e-v+1)!(e-v+2)!}
\]

is not the number of rooted planar maps with `e` edges and `v` vertices. At `e=2,v=2` it equals
six. To audit the smallest case directly, fix edge involution

\[
 \alpha=(0\ 1)(2\ 3)
\]

and root dart `0`. Up to the only nontrivial root-preserving relabeling `(2 3)`, the transitive
rotation permutations with exactly two vertex cycles and with `sigma alpha` having exactly two
face cycles have five orbits. Representatives may be taken with vertex/face cycle pairs

\[
\begin{array}{c|c}
 (0)(1\ 2\ 3)&(0\ 2\ 1)(3)\\
 (0\ 1\ 2)(3)&(0\ 2\ 3)(1)\\
 (0\ 2\ 1)(3)&(0)(1\ 2\ 3)\\
 (0\ 2\ 3)(1)&(0\ 1\ 2)(3)\\
 (0\ 2)(1\ 3)&(0\ 3)(1\ 2).
\end{array}
\]

Hence the exact value is five, not six. Formula (7) and therefore (8) do not follow from (6).

The standard corrected two-face coefficient is

\[
 T_e=\frac{4^e-\binom{2e}{e}}2,
\]

which gives `1,5,22,93` for `e=1,2,3,4`. This review records it only as the natural repair target;
the proposer must supply either a self-contained unicyclic-map derivation or a locatable primary
source before using it at completion level. Once supplied, it retains the desired downstream
bound, because Cauchy--Schwarz gives

\[
 4^e=\left(\sum_{j=0}^e\binom ej\right)^2
 \le(e+1)\sum_{j=0}^e\binom ej^2
 =(e+1)\binom{2e}{e},
\]

and hence

\[
 T_e\le\frac e2\binom{2e}{e}.
\]

Thus the numerical conclusion is repairable without changing (8), but the present artifact does
not yet prove its `h=0` case.

**Verdict:** completion-level FAIL pending a local planar repair. The current claim may become
`CONJECTURED`, not `PROVED`.

### Finding WTBC-IR-05 — CONDITIONAL PASS: `32768`, exponent `43`, and `log m>18`

**Applies to:** current every-`h` claim hash
`sha256:918abca3f6ba28a5ad1d894a5b9e917cc5114081c8a7fcdd16dc28c78d0bb603`.

Conditional on the repaired planar inequality

\[
 R_{e,0}^{(2)}\le e^2\binom{2e}{e}\le e^24^e,
\]

the artifact's constant algebra is correct. Catalan weighting supplies `2^e`, so at `e=4N`

\[
 e^28^e=16N^2\,4096^N.
\]

For `N>=2`, `16N^2<=8^N`; the `N=1` case is bounded directly. Therefore the planar base is
`32768^N`. Positive genus has the stronger base `4096^N` by Finding 3 and the same exponent
`43h`.

The threshold comparison is also correct and uses natural logarithms:

\[
 \log(32768^2/18)=30\log2-\log18
 =17.9040436589\ldots<18.
\]

Thus every integer `m>e^18` satisfies

\[
 32768<\sqrt{18m}.
\]

There is no hidden claim for small `m`; the conclusion is tied to the project's large-`m`
regime. The quantifiers are: fix such an `m`, use the universal numerical constants
`D=32768,alpha=43`, then quantify over every `N,h`.

**Verdict:** constants and quantifiers PASS conditional on Finding 4's planar repair.

### Finding WTBC-IR-06 — PASS: Catalan and monotone-Weingarten scopes

**Applies to:** the positive-genus claim and artifact Sections 5 and 7.

For cycles of `C` of lengths `ell_j`,

\[
 P_0(C)=\prod_j\operatorname{Cat}_{\ell_j-1}
 \le4^{E-\#C}\le4^E=16^N=2^e.
\]

For an admissible skeleton this is exactly the product over label blocks, since `C` is block
diagonal and its global cycles are the union of the block cycles. Extending the same definition
to every abstract triple only enlarges the structural sum. This step is already covered by the
PROVED premise `HEXT.werner-minimal-catalan-weight`, exact claim hash
`sha256:82a54db26f9887fab15962f597b42c9d9b7c5a50b2dc86c713e0b066cc51cf54`.

The monotone-path statement is separate from the minimal weighted-count claim. The already
PROVED skeletonwise estimate gives

\[
 \sum_{g\ge0}P_g(C)d^{-2g}
 \le\frac{P_0(C)}{1-6(2N)^{7/2}/d^2}
\]

when the denominator is positive. The multi-label convolution and constant were independently
reviewed at claim hash
`sha256:e47cd4541145cc59fcd04cf217f738d0ceb6c126508210d4c169af7fc0c8c0e4`.
For fixed `m` and `N<=c_m log d`, the multiplier is `1+o(1)`. It introduces no factorial, but it
does not count minimal skeletons or physical labels.

**Verdict:** PASS with the stated separation of scopes.

### Finding WTBC-IR-07 — PASS WITH A SHARPER SCOPE: equality-component obstruction

**Applies to:** proposed obstruction hash
`sha256:932db446425cb53de07e3a043bac0670aff523e875221f8ea94012e1be3c6be8`.

For `sigma=tau=id`, the equality graph has only self-loops and therefore

\[
 \kappa=2N.
\]

The constellation is `A=J,B=K=Jrho,C=id`. The group generated by `J,K` contains `rho=JK`; from
one `V` slot, powers of `rho` reach every `V` slot and `J` reaches every `A` slot, so the triple is
connected for every `N`, not only odd `N`.

For odd `N`, `K` has one cycle and the genus is `(N-1)/2`, as the artifact states. More relevant
to the even trace moments, for even `N`, `K` has two cycles and

\[
 \#A+\#B+\#C=N+2+2N=3N+2,
 \qquad h=\frac{N-2}{2}.                                    \tag{R1}
\]

Identity pairings preserve every physical coloring. Independently choosing each ordered pair
`(v_i,a_i)` with `v_i!=a_i` gives exactly `[m(m-1)]^N` compatible edge-label sequences.
Consequently no bound `kappa<=N+O(1)` can hold even on the connected even-moment sector. A bound
of the proposed form

\[
 \kappa\le N+b+Lh
\]

is not refuted; (R1) only forces asymptotically `L>=2` (and at `L=2`, `b>=2` for the even family).

The exact reviewed obstruction statement is:

> For every even N>=4, the identity pairings sigma=tau=id define a connected admissible Werner
> constellation with equality-graph component count kappa=2N and genus h=(N-2)/2, and admit
> [m(m-1)]^N physical edge-label sequences. Hence no uniform bound kappa<=N+O(1) holds on the
> connected even-moment sector, although this family does not refute a bound
> kappa<=N+b+Lh with L>=2 or the centered spectral bound.

Its exact hash is
`sha256:932db446425cb53de07e3a043bac0670aff523e875221f8ea94012e1be3c6be8`.

Its actual centered-bound impact is limited. At minimal Weingarten length, the normalization,
label multiplicity, and Euler factor for the even family combine as

\[
 m^{-2N}[m(m-1)]^N d^{-2h}
 =\left(\frac{m-1}{m}\right)^N d^{-(N-2)}.                  \tag{R2}
\]

This vanishes for each fixed even `N>=4`, and is superpolynomially small when
`N=Theta(log d)`. Moreover a coefficientwise family does not by itself give a lower bound on the
fully summed centered moment after all contractions are assembled. The family therefore exposes
why ordinary-map count alone cannot supply a genus-independent label bound; it is not evidence
against the spectral target.

**Verdict:** obstruction PASS; centered bound unaffected at the level of verdict.

### Finding WTBC-IR-08 — PASS: what remains outside the structural count

Even after the planar repair, the structural node counts only connected minimal skeletons. A
centered-moment theorem still needs:

1. a label-weighted estimate, such as a proved bound
   `kappa<=N+b+Lh`, or a joint weighted sum that avoids taking the maximum `kappa`;
2. treatment of the two-component sector, whose Euler power is `d^(2-2h)` rather than `d^(-2h)`;
3. the already proved exact Euler/Weingarten interface and monotone excess tail; and
4. an even `N=Theta(log d)` Markov assembly at the target constant.

The weighted structural count does not imply item 1. The identity family proves only that item 1
cannot have `L=0`. It does not show that a joint label-and-genus count fails.

**Verdict:** `HEXT.same-tuple-werner-centered-bound`, exact hash
`sha256:c221c71b9f3cb3294d7c9c7d979cf1a154042ea4ec013f95d3fc7955c2c38da5`,
remains `CONJECTURED`; the full-size extensive result remains `OPEN`.

## 5. Executable promotion and repair instructions

No instruction below was applied in this review.

### 5.1 Current every-`h` node

For `HEXT.werner-two-boundary-constellation-count`:

1. Do **not** promote the current claim to `PROVED` from the reviewed artifact.
2. It is protocol-consistent to move `OPEN -> CONJECTURED`, link Findings WTBC-IR-01--06, and add
   the caveat that the planar coefficient (6) is false and `h=0` awaits repair.
3. Add a frontier gate requiring a self-contained proof or locatable primary source for
   `R_(e,0)^(2)<=e^2 binom(2e,e)`. The corrected coefficient
   `(4^e-binom(2e,e))/2` is one sufficient route.
4. Preserve the reviewed artifact and place the correction in a new repair artifact. Remove the
   stray carriage-return character in the displayed transitivity condition when preparing that
   repair; it is typographical, not mathematical.
5. Register a route whose load-bearing premises include
   `HEXT.werner-contraction-skeleton-ribbon-injection` and
   `HEXT.werner-minimal-catalan-weight`. The route implication must cite the repaired planar proof,
   Findings 1--6, and retain exact claim hash
   `sha256:918abca3f6ba28a5ad1d894a5b9e917cc5114081c8a7fcdd16dc28c78d0bb603`.
6. After a supplemental independent review of the new planar proof and assembled route, the
   unchanged original claim may promote to `PROVED`; no change to `D=32768,alpha=43` is needed.

### 5.2 Narrow positive-genus node

Create an atomic node such as `HEXT.werner-positive-genus-two-boundary-weighted-count` with the
exact statement and hash from Section 3. Give it a route with premises

- `HEXT.werner-contraction-skeleton-ribbon-injection`; and
- `HEXT.werner-minimal-catalan-weight`.

Use Findings WTBC-IR-01--03 and WTBC-IR-06 as the independently reviewed route implication. With
those already `PROVED` premises and the exact reviewed statement hash
`sha256:300c642a7cab1717445a387e793666fa416ead65bd0731f9be684701d8f30cf6`,
the atomic node may promote to `PROVED`. This promotion does not propagate to the every-`h` node.

Optionally split the purely ordinary-map part into a node at exact hash
`sha256:42ebc41b59af9d480ec395ad6188ab95ca22092e3806c5c5284a46f02c2dc8d3`,
supported by Findings 1--2.

### 5.3 Equality obstruction and centered node

Register the even identity-pairing statement in Finding 7 as a separate obstruction node at exact
hash `sha256:932db446425cb53de07e3a043bac0670aff523e875221f8ea94012e1be3c6be8`;
it may promote to `PROVED` from that finding. Its caveats must quote (R2) and state that it does not
refute the centered spectral claim.

Do not promote `HEXT.same-tuple-werner-centered-bound`. Add the structural count only as
non-load-bearing evidence until an explicit route includes a proved equality-component/joint-label
premise and the two-component analysis. Do not promote the full-size extensive goal.

## 6. Final scope statement

This review proves the positive-genus structural weighted count and validates all of its stated
large-`m` constants. It does not certify the planar coefficient in the proposer artifact, does not
prove the all-genus node, does not control compatible labels, and does not establish a growing even
moment or high-probability spectral theorem. Absolute-unbounded extensive violation remains a
separate completed result; the full-size extensive Question 3 remains **OPEN**.
