# Independent review: Werner equality-component genus gate

Date: 2026-08-30

Reviewer: independent Codex review context `/root/weyl_majorization_audit`.

## Independence and scope

I did not author
`holevo-extensive-violation/artifacts/WERNER_EQUALITY_COMPONENT_GENUS_GATE_20260830.md`
or any of its proposed atomic statements. I read `DAG_PROTOCOL.md` and `FILE_PROTOCOL.md` in full
and independently reconstructed the permutation-length argument, the two-component topology, the
genus-two counterexample, and the one-face tree--cotree count. I did not use web access, start a
computation, or edit canonical YAML. This immutable review is the only project file created by the
review.

The review checks exactly:

1. admissibility and fixed points of `A`;
2. the Euler transposition-length budget and every inequality direction involving `tau`, `K`, and
   the equality-component number `kappa`;
3. the parity-refined bound
   `kappa<=N-2c+q_N+2+2h-|C|`, its connected `(b,L)=(2,2)` corollary, and sharpness;
4. the `c=2` decomposition into the two physical boundary components and the planar-component
   free-return implication;
5. the explicit `N=4,c=2,h=2` nonreturn example;
6. the `4096^N N^(24h)` residual two-component weighted count; and
7. the exact `m` and `d` normalization, including the distinction between minimal paths and the
   excess monotone-path multiplier.

It does not re-review the separate connected positive-genus weighted-count theorem, prove its
planar case, assemble the signed growing moment, prove the centered spectral claim, or imply the
full-size extensive-violation theorem.

## Executive verdict

The three mathematical atoms proposed by the artifact **pass**, after locking their exact scope as
in this review.

- The admissible equality-component genus bound is safe for `PROVED` once its route explicitly
  lists the already-`PROVED` constellation-encoding and Euler-deficit premises.
- The two-component low-genus return separation is safe for `PROVED`. Its genus-two scope
  counterexample uses four distinct generator labels, so the nonextension statement must say
  `m>=4` (automatically true in the project regime).
- The two-component weighted count is mathematically safe for `PROVED` after an explicit route
  lists the new equality bound plus the already-`PROVED` ribbon injection, Euler power, minimal
  Catalan weight, and monotone-tail nodes. Its mass formula is a **minimal-path** formula; a claim
  about all monotone paths must include the uniform factor `1/(1-theta)`.

The equality theorem supplies `(b,L)=(2,2)` for connected positive-genus mass accounting, but it
does not repair the separate connected planar-count defect. No centered or full-size conclusion is
licensed.

## Immutable inputs and exact hashes

| object | SHA-256 |
|---|---|
| `DAG_PROTOCOL.md` | `d8775b511431e6e9dc7a5be6200af80bd612e7e7d5f5ff10bb14ef748791a095` |
| `FILE_PROTOCOL.md` | `d9d6fb57a26fef3b70fc05bda74a29101d83a43df60e06eaeb345e76980fc595` |
| reviewed artifact | `1aac1c071b61dc3809a3bcf28339263508e301062eba8980e8b287a64ef92be7` |
| exact constellation source artifact | `c52f59c7e301a154925149689b13897a54cf462bf9674ef16105f9a2dd3d1a88` |
| two-boundary weighted-count source artifact | `f4d0b8b92366c0aa353b3f7794c9a0b1a5326aa0602ecc9323f6f9a9e51a8bab` |
| exact reversal/return source artifact | `6f0d52b4d48433c9f16d8ded4440469268b336df3af8f23f4a8b798ac15752ce` |

The three proposed node names were not canonical YAML files at review time. The following exact
prospective claim texts are review-locked; blockquote soft line breaks are single spaces for
`sha256(claim.strip())`, matching YAML folded-scalar normalization.

### `HEXT.werner-admissible-equality-component-genus-bound`

> For every admissible Werner contraction skeleton on E=2N physical slots, with c in {1,2}
> topological constellation components, total genus h, and q_N=1 for odd N and q_N=2 for even N,
> the tuple-label equality graph satisfies
> kappa(sigma,tau)<=N-2c+q_N+2+2h-|C|. In particular every connected skeleton has
> kappa<=N+2+2h. The universal constants b=2 and L=2 are optimal in the parity-uniform bound
> kappa<=N+b+Lh.

Exact claim hash:
`sha256:443c7023066be044f8795ef5d036a159f652ccb78bb6b51d15d0a95904791651`.

### `HEXT.werner-two-component-low-genus-return-separation`

> If an admissible Werner constellation has two topological components and total genus at most
> one, then at least one of its forward and block-reversed free words is the identity, so its trace
> sequence belongs to the union of the forward-return and reverse-return sectors. This follows
> because each topological component is a rooted unicellular map and every planar component is a
> plane tree whose Haar-labelled boundary word freely reduces to the identity. The assertion does
> not extend to total genus two when m>=4.

Exact claim hash:
`sha256:c523f97093f9490b81572424cc273a25e9224cdbff285506d7a376dc304e9724`.

### `HEXT.werner-two-component-nonreturn-weighted-count`

> For every N>=2 and h>=2, the total minimal Catalan weight of all two-topological-component
> structural Werner constellations of total genus h is at most 4096^N N^(24h). Every admissible
> member has at most N+2h equality components. Consequently, after m^(-2N) moment normalization,
> the admissible subset's total minimal-path genus-h absolute mass is at most
> (4096/m)^N m^2 N^24 (m^2 N^24/d^2)^(h-1). A skeletonwise excess-path sum adds at most the
> factor 1/(1-6(2N)^(7/2)/d^2) whenever the denominator is positive.

Exact claim hash:
`sha256:16edb16e7ddcce4a044c0fe7608bc73bfe530a0fad52e02fc9f1a05fe7488c32`.

Existing load-bearing premise hashes are:

| node | exact claim hash | current level |
|---|---|---|
| `HEXT.werner-contraction-skeleton-ribbon-injection` | `sha256:288e0f5df3ca6a53915325c487648184b9be0ff950c1e52c5db7689468c730f7` | `PROVED` |
| `HEXT.werner-constellation-euler-deficit` | `sha256:c1c37d08c4f0cf37cb698b26a03d48cef0dd668686b71ed3a8391fed63c1d62a` | `PROVED` |
| `HEXT.werner-minimal-catalan-weight` | `sha256:82a54db26f9887fab15962f597b42c9d9b7c5a50b2dc86c713e0b066cc51cf54` | `PROVED` |
| `HEXT.werner-monotone-weingarten-tail-summability` | `sha256:e47cd4541145cc59fcd04cf217f738d0ceb6c126508210d4c169af7fc0c8c0e4` | `PROVED` |
| `HEXT.werner-positive-genus-two-boundary-weighted-count` | `sha256:300c642a7cab1717445a387e793666fa416ead65bd0731f9be684701d8f30cf6` | `PROVED`, `h>=1` only |
| `HEXT.same-tuple-werner-centered-bound` | `sha256:c221c71b9f3cb3294d7c9c7d979cf1a154042ea4ec013f95d3fc7955c2c38da5` | unresolved; no promotion |

## Findings

### Finding WECG-IR-01 — PASS: admissibility forces `A` to have no fixed point

**Stable locator:** reviewed artifact, `## 4. Proof of the universal component theorem`, Lemma 1,
equations `(15)`.

If `A(s)=s` and `A=J sigma^(-1)`, then `sigma^(-1)(s)=Js`, equivalently
`sigma(Js)=s`. Admissibility gives `lambda(sigma(Js))=lambda(Js)`, hence
`lambda(s)=lambda(Js)`. Since `J` exchanges the physical pair `V_i,A_i`, this contradicts the
off-diagonal condition `lambda(V_i)!=lambda(A_i)`. Thus every `A` cycle has length at least two,
so

`#A<=E/2=N` and `|A|=E-#A>=N`.

The conclusion is physical: it is false for an arbitrary uncolored triple `ABC=rho`.

**Verdict:** PASS.

### Finding WECG-IR-02 — PASS: Euler length budget and all inequality directions

**Stable locator:** reviewed artifact, `## 3` equations `(13)--(14)` and `## 4` Lemmas 2--3,
equations `(16)--(20)`.

Euler gives

`#A+#B+#C+2-2E=2c-2h`.

Subtracting the cycle sum from `3E` yields exactly

`|A|+|B|+|C|=E-2c+2h+2`.

Using `|A|>=N` and `E=2N` gives the upper budget

`|B|+|C|<=N-2c+2h+2`.

The equality graph has `kappa` orbits under `<sigma,tau>`. Every `tau` cycle lies within one such
orbit, so `#tau>=kappa`, and therefore

`|tau|=E-#tau<=E-kappa`.

The direction is important: this is an upper bound on `|tau|`. On the other side,
`B=sigma K tau sigma^(-1)` gives `|B|=|K tau|`. The transposition metric triangle inequality is

`|K|<=|K tau|+|tau^(-1)|=|B|+|tau|`,

so

`|tau|>=|K|-|B|`.

Thus the proof correctly sandwiches `|tau|`; it never reverses either inequality.

Finally `K=J rho` has one `2N`-cycle for odd `N` and two `N`-cycles for even `N`, hence
`#K=q_N` and `|K|=E-q_N`.

**Verdict:** PASS.

### Finding WECG-IR-03 — PASS: exact parity-refined component bound

**Stable locator:** reviewed artifact, `## 4`, derivation immediately following equation `(20)`.

Combining the two bounds on `|tau|` gives

`E-kappa >= E-q_N-|B|`, hence `kappa<=q_N+|B|`.

The Euler budget gives

`|B|<=N-2c+2h+2-|C|`.

Therefore

`kappa<=N-2c+q_N+2+2h-|C|`.

For `c=1`, this is `kappa<=N+q_N+2h-|C|<=N+2+2h`. For `c=2`, it is
`kappa<=N-1+2h` for odd `N` and `kappa<=N+2h` for even `N`, with the additional useful
`-|C|` term suppressed in the displayed parity-uniform forms.

**Verdict:** PASS for exact claim hash
`sha256:443c7023066be044f8795ef5d036a159f652ccb78bb6b51d15d0a95904791651`.

### Finding WECG-IR-04 — PASS: connected `(b,L)=(2,2)` is sharp in the stated sense

**Stable locator:** reviewed artifact, `## 5. Sharpness`, equations `(22)--(26)`.

For `sigma=tau=id`, the two-color labeling `lambda(V_i)=1`, `lambda(A_i)=2` is admissible,
and

`A=J`, `B=K`, `C=id`, `kappa=2N`.

The group generated by `J,K` contains `rho=JK`; `rho` traverses each boundary and `J` joins the
two, so the constellation is connected for both parities. Its genus is

`h=(N-q_N)/2`.

The refined connected bound is an equality:

`N+q_N+2h-|C|=2N`.

If a universal inequality `kappa<=N+b+Lh` had `L<2`, the required `b` would diverge linearly in
`N`. With `L=2`, the even family has `h=(N-2)/2`, forcing `b>=2`. Thus no smaller `L`, and no
smaller `b` at `L=2`, works uniformly.

**Verdict:** PASS; the artifact's notion of optimality is exact and not overstated.

### Finding WECG-IR-05 — PASS: `c=2` gives two rooted unicellular trace components

**Stable locator:** reviewed artifact, `## 7. Exact two-component structure`, equations
`(29)--(30)`.

Because `rho=ABC` belongs to the generated group, every `rho` cycle lies in a topological orbit.
There are exactly two `rho` cycles and, when `c=2`, exactly two nonempty orbits covering all darts;
therefore the orbits are precisely `X_V` and `X_A`. Each of `A,B,C` preserves both sets.

The inverse formulas

`sigma=A^(-1)J` and `tau=C^(-1)A^(-1)J`

show that `sigma,tau` exchange `X_V` and `X_A`. Under the reviewed physical occurrence dictionary,
this means an unstarred occurrence in either trace is paired with a starred occurrence in the same
trace. The two-face ribbon realization consequently separates into the ordered forward and
block-reversed one-face components. This is a topological decomposition only; it does not imply
`kappa=2`, trace independence, or factorization of finite-`d` Weingarten coefficients.

There is also a nonfatal strengthening not used in the artifact: because `sigma` itself exchanges
two sets of size `N`, every `<sigma,tau>` equality orbit contains at least one `V` dart and one `A`
dart. Hence `kappa<=N` throughout the `c=2` sector. The displayed parity bound `(9)` and all later
mass estimates remain correct, but they are not optimal for `c=2`.

**Verdict:** PASS.

### Finding WECG-IR-06 — PASS: a planar one-boundary component forces the corresponding free return

**Stable locator:** reviewed artifact, `## 7`, Lemma 4 and the paragraph following it.

A connected orientable one-face map of genus zero with `e_0` edges has
`V=e_0+1`; its underlying graph is therefore a tree. The contour of a plane tree pairs the two
sides of every edge noncrossingly. By the exact Haar occurrence labeling, those two boundary
occurrences are a starred and an unstarred occurrence of the same generator, hence inverse free
letters. Removing a leaf strip deletes an adjacent inverse pair from the remaining contour.
Induction removes the entire word. A cut at the physical root does not change the conclusion:
cyclically moving a tree contour only conjugates a word already equal to the identity.

This argument uses both the exact incidence phase dictionary and Haar generator labels. It would
be false for an arbitrary uncolored plane tree.

If `h=h_V+h_A<=1`, at least one component genus is zero, so at least one of `w` and `check w` is
the identity. Hence the corresponding trace sequence lies in the union of the already reviewed
return sectors.

**Verdict:** PASS for the low-genus part of claim hash
`sha256:c523f97093f9490b81572424cc273a25e9224cdbff285506d7a376dc304e9724`.

### Finding WECG-IR-07 — PASS with `m>=4` scope: the first nonreturn example is `N=4,c=2,h=2`

**Stable locator:** reviewed artifact, `## 8. Positive-genus two-component diagrams are not all
returns`, equations `(32)--(37)`.

For

`sigma=tau=(0 5)(1 7)(2 4)(3 6)`,

the inverse constellation formulas give exactly the displayed two four-cycles for `A`, the two
three-cycles plus two fixed points for `B`, and `C=id`. Their product is `rho`; all three preserve
`X_V,X_A`, so `c=2`. On each four-dart component the cycle sum is `1+2+4=7`, while the component
has eight ordinary incidence edges and one face. Thus `7-8+1=0=2-2g`, so each genus is one and
the total genus is two.

The four equality components are the four displayed transpositions. Assigning distinct labels
`1,2,3,4` gives

`v=(1,2,3,4)` and `a=(3,1,4,2)`,

with every `v_i!=a_i`. Forward block multiplication cancels only the adjacent `g_4 g_4^(-1)`
pair and leaves equation `(36)`. Reversing the four blocks cancels only `g_1 g_1^(-1)` and leaves
equation `(37)`. Both reduced words are nonempty.

The construction explicitly needs at least four available generator labels as written. The
artifact should state `m>=4` when using it as a scope counterexample; this is harmless in the
project's large-`m` regime.

**Verdict:** PASS for the nonextension clause of claim hash
`sha256:c523f97093f9490b81572424cc273a25e9224cdbff285506d7a376dc304e9724`.

### Finding WECG-IR-08 — PASS: one-face tree--cotree code and the `4096^N N^(24h)` bound

**Stable locator:** reviewed artifact, `## 9. Weighted count for the residual two-component
sector`, equations `(38)--(40)`.

Each ordered boundary component has `N` constellation darts, `e_0=2N` ordinary edges, one rooted
face, and genus `g`. Euler gives `V=e_0+1-2g`; a spanning tree has `e_0-2g` edges, leaving exactly
`2g` cotree edges. A deterministic depth-first traversal from the physical root canonically
chooses the tree and orders the cotree edges, so no factorial is needed.

Deleting the cotree edges in reverse order leaves a plane tree, counted by at most `4^e_0`. Each
edge reinsertion uses an ordered pair of fewer than `4e_0` safe corners and one orientation bit,
at most `32e_0^2`; the physical face root costs at most `4e_0`. Therefore

`U(e_0,g)<=4^e_0 (4e_0)(32e_0^2)^(2g)`.

The two physical faces are ordered, so the product of their codes needs no component-swap factor.
Their boundary phases reconstruct halfedge types, vertex colors, and physical dart names; using
uncolored ordinary-map codes is an upper injection, not an assertion that intermediate deletions
remain Werner-admissible.

Summing the ordered genus splits `h_V+h_A=h` and multiplying the per-skeleton minimal Catalan bound
`16^N` gives

`(h+1) 64N^2 4096^N (2^14 N^4)^h`.

For `N>=2`, `h+1<=3N`. When `h>=2`,

`192N^3<=N^(6h)` and `2^(14h)<=N^(14h)`.

Together with the existing `N^(4h)` factor this proves

`S_(N,h)^(c=2)<=4096^N N^(24h)`.

The count actually covers all structural `c=2` constellations at those genera, so it certainly
covers the nonreturn subset.

**Verdict:** PASS for the weighted-count part of claim hash
`sha256:16edb16e7ddcce4a044c0fe7608bc73bfe530a0fad52e02fc9f1a05fe7488c32`.

### Finding WECG-IR-09 — PASS after wording repair: exact `m,d` normalization and excess paths

**Stable locator:** reviewed artifact, equations `(9)--(11)` and final paragraphs of `## 9`.

For admissible `c=2` skeletons, the uniform parity bound is `kappa<=N+2h`; therefore the number
of compatible labelings is at most `m^(N+2h)`. The moment contributes `m^(-2N)`, and the minimal
Euler power is `d^(2-2h)`. Multiplying by the weighted count gives

`m^(-2N) m^(N+2h) 4096^N N^(24h) d^(2-2h)`

which is exactly

`(4096/m)^N m^2 N^24 (m^2 N^24/d^2)^(h-1)`.

For fixed `m` and `N<=c_m log d`, the handle ratio `m^2N^24/d^2` tends to zero. The separate
monotone-tail theorem is uniform skeleton by skeleton and multiplies the total minimal mass by at
most

`1/(1-theta)`, where `theta=6(2N)^(7/2)/d^2<1`.

Equation `(11)` in the artifact is therefore a minimal-path mass bound. The candidate node's phrase
“genus-h absolute mass” is too broad unless it either says “minimal-path” or includes the displayed
`1/(1-theta)` multiplier and the monotone-tail premise. The review-locked claim above makes this
repair.

Using the stronger `kappa<=N` observation from Finding WECG-IR-05 would remove the factor `m^(2h)`
and improve the handle ratio, but that improvement is not needed to validate equation `(11)`.

**Verdict:** repaired exact claim PASS at
`sha256:16edb16e7ddcce4a044c0fe7608bc73bfe530a0fad52e02fc9f1a05fe7488c32`.

### Finding WECG-IR-10 — scope boundary: connected planar, centered, and full-size remain unresolved

**Stable locator:** reviewed artifact, `## 6. Consequence for the connected weighted count` and
`## 12. Remaining scope`.

The equality theorem supplies the previously missing factor `m^(N+2+2h)` in the connected
positive-genus count. The structural theorem currently registered as
`HEXT.werner-positive-genus-two-boundary-weighted-count` is independently proved only for `h>=1`.
Thus equation `(28)` is a valid positive-genus conditional corollary once the new equality node is
linked, but this review does not validate a connected `h=0` estimate. The earlier planar formula
has its own recorded defect.

Even after separating the `c=2,h<=1` return union and bounding `c=2,h>=2`, the exact signed
forward/reversal growing moment still requires its remaining connected/planar assembly and final
Markov step. Nothing here proves the centered high-probability statement or the full-size theorem.

**Verdict:** no parent promotion.

## Promotion and repair instructions

1. Register `HEXT.werner-admissible-equality-component-genus-bound` with the exact text/hash in
   this review. Its route must list
   `HEXT.werner-contraction-skeleton-ribbon-injection` and
   `HEXT.werner-constellation-euler-deficit`. It may then be assessed `PROVED`.
2. Register `HEXT.werner-two-component-low-genus-return-separation` with the exact text/hash here,
   link Findings WECG-IR-05 through WECG-IR-07, and record that its genus-two counterexample uses
   `m>=4`. It may be assessed `PROVED`.
3. Register the two-component weighted-count node only with the repaired exact claim text/hash in
   this review. Its route should list the ribbon injection, Euler deficit, minimal Catalan weight,
   monotone-tail theorem, and the new equality-component bound. It may promote to `PROVED` after
   those premise links and the reviewed implication are present.
4. Do not use the unqualified candidate wording “genus-h absolute mass”. Without the
   monotone-tail multiplier it must say “minimal-path genus-h absolute mass”.
5. Optionally strengthen the `c=2` label bound to `kappa<=N`, since `sigma` exchanges the two
   physical boundary sets. The artifact's weaker `N+2h` bound and its stated `m,d` normalization
   are still valid and need no repair for correctness.
6. The connected positive-genus mass implication may cite the new equality bound together with
   `HEXT.werner-positive-genus-two-boundary-weighted-count`; do not extend it to `h=0` without a
   repaired planar proof.
7. Do not promote `HEXT.same-tuple-werner-centered-bound`, any full-size node, or any aggregate
   route from this review.

## Limitations

- No enumeration or certificate was rerun. The displayed finite `N=4` example was checked by
  direct hand composition and free reduction.
- This review certifies a counting upper bound, not the existence of a genus-lowering surgery and
  not a sign-sensitive cancellation theorem.
- The map code counts structural constellations; admissibility enters only through the separate
  equality-component bound and can only reduce the set.
- The return-union estimate is an absolute safe-sector bound. It does not imply that the two trace
  factors are probabilistically independent or that their Weingarten coefficients factor.
