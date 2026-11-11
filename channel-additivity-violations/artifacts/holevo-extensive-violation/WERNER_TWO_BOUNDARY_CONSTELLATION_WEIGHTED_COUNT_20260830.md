# Two-boundary Werner constellations: a target-compatible weighted count

Date: 2026-08-30

Status: independent pure-theory derivation for Question 3. This is a candidate proof of the
structural weighted-count node, not an independently reviewed completion record. No canonical YAML
is changed. The candidate conclusion should remain at most `CONJECTURED` until adversarial review.
The centered-spectrum claim and the full-size extensive-violation theorem remain unresolved.

No new large computation and no support-at-least-three surgery are used.

## 1. Outcome

Let

\[
 E=2N
\]

be the number of constellation darts and let

\[
 e=2E=4N
\]

be the number of ordinary edges in the incidence ribbon map. Fix the two rooted boundary cycles
of `rho`. For connected triples

\[
 \mathsf A\mathsf B\mathsf C=\rho
\]

of orientable genus `h`, define

\[
 S_{N,h}:=
 \sum_{\substack{\mathsf A\mathsf B\mathsf C=\rho\\
                  \langle\mathsf A,\mathsf B,\mathsf C\rangle\ {m transitive}\\
                  g=h}}
 P_0(\mathsf C),
\tag{1}
\]

where `P_0` is the absolute minimal Möbius/Catalan weight. The sum in (1) is over **all** connected
triples, so it upper-bounds the admissible subset appearing in
`HEXT.werner-two-boundary-constellation-count`.

The argument below gives the explicit candidate bound

\[
 \boxed{S_{N,h}\le 32768^N N^{43h}.}
\tag{2}
\]

In the project regime `ln m>18`,

\[
 32768<\sqrt{18m},
\tag{3}
\]

because

\[
 \log(32768^2/18)=30\log2-\log18<18.
\]

Thus (2) is target-compatible for the exact current claim

`sha256:918abca3f6ba28a5ad1d894a5b9e917cc5114081c8a7fcdd16dc28c78d0bb603`.

The proof is an ordinary-map **counting code**, not a physical genus-lowering surgery. It does not
preserve the Haar-label equality graph during its intermediate deletions, and it makes no claim
about support-three surgery.

There is a separate, load-bearing obstruction to using (2) as a proof of the centered bound:
ordinary map count and Catalan weight do not count compatible tuple labelings. A further uniform
bound on the number of equality-graph components per genus is still missing. Section 8 states the
exact needed quantifier and gives a family showing why the genus dependence cannot be omitted.

## 2. Exact rooted-map interface and the absence of a factorial

The lossless constellation realization has vertex cycles `A`, `B`, and `C`, two ordinary edges
per dart, and the two faces prescribed by `rho`. Starting at an `a` halfedge, its face walk has the
four-periodic form

\[
 A,\ B,\ C,\ B,\ A,\ B,\ C,\ B,\ldots
\tag{4}
\]

and four face steps send the dart name `s` to `rho(s)`. The two distinguished halfedges
`a_(V_0)` and `a_(A_0)` root and order the two faces.

Forget the vertex colors and halfedge-type names but retain:

1. the oriented ribbon map;
2. the order of its two faces;
3. one distinguished oriented halfedge on each face; and
4. the information that both roots have phase zero in the period (4).

This forgetting map is injective on constellation images. Indeed, the phase of every halfedge is
its distance modulo four from the appropriate face root. Hence its `A/B/C` vertex color and its
`a,b,bar(b),bar(a)` type are recovered. Every fourth position recovers the physical dart names in
the fixed `rho` order. The recovered vertex rotations then recover the cycles of
`A`, `B`, and `C`. Consequently two distinct rooted triples cannot become the same doubly
face-rooted ordinary map.

This is where the fixed boundary order matters. If the two `rho` cycles were not rooted and
ordered, one would have to restore rotations, roots, and possibly dart names. Here no `(2N)!`
factor occurs. Conversely, the second face root must not be silently discarded: relative to the
usual one-root convention it costs at most `2e`, only a polynomial factor.

Let `R_(e,h)^(2)` denote the number of connected orientable ordinary maps of genus `h`, with `e`
edges and exactly two ordered, rooted faces. The injection gives

\[
 \#\{\text{connected genus-}h\text{ constellation triples}\}
 \le R_{e,h}^{(2)},\qquad e=4N.
\tag{5}
\]

The map on the right is deliberately uncolored. No additional `2^e` or `3^e` color factor is
needed because the two boundary phases recover the coloring uniquely on the image.

## 3. Planar base: exact two-face enumeration

The refined rooted-planar-map coefficient with `e` edges and `v` vertices is

\[
 M_{e,v}=
 \frac{(2e)!}
 {v!(v-1)!(e-v+1)!(e-v+2)!}.
\tag{6}
\]

It follows from the usual root-edge decomposition and bivariate Lagrange coefficient extraction;
equivalently, (6) is the coefficient form obtained by recording vertices and faces in the planar
map recursion. For two faces, Euler gives `v=e`, and therefore

\[
 M_{e,e}=\frac e2\binom{2e}{e}.
\tag{7}
\]

Formula (7) also follows by duality from the `v=2` specialization of (6). Root the ordinary map
at the first physical face root. The other face is then the unique second face and has at most
`2e` possible rooted halfedges. Hence

\[
 R_{e,0}^{(2)}
 \le 2e M_{e,e}
 =e^2\binom{2e}{e}
 \le e^2 4^e.
\tag{8}
\]

This is the quantitative gain lost by the generic all-face map count. With two faces fixed, the
planar exponential base is `4` per ordinary edge, not `16`.

## 4. Positive genus: a spanning-tree/cotree counting code

For a connected genus-`h` map with `e` edges and exactly two faces, Euler gives

\[
 V=e-2h.
\tag{9}
\]

Every spanning tree therefore contains `V-1=e-2h-1` edges, and the number of cotree edges is

\[
 r=e-(V-1)=2h+1.
\tag{10}
\]

This exact `2h+1` count is the only genus input needed below.

Use the first face root and the vertex rotations to run a deterministic depth-first exploration.
It chooses a canonical spanning tree and orders the `r` cotree edges by first encounter. Delete
those cotree edges in reverse order. The remaining ribbon graph is a plane tree. To reconstruct
the original map, record for every deleted edge the two corners at which it is reinserted and an
orientation bit. Also record the two final face-root halfedges.

This is an injective code:

- the plane tree and ordered reinsertion data recover the full vertex rotations and edge
  involution;
- deterministic exploration eliminates an `r!` ordering factor; and
- the two recorded halfedges restore the ordered face roots.

A plane tree with `e-r` edges has at most `4^(e-r)` possibilities. At every reinsertion stage
there are fewer than `4e` safe corner codes, so an ordered pair plus an orientation bit has at
most `32e^2` codes. Each face root has at most `4e` safe codes. Therefore

\[
 R_{e,h}^{(2)}
 \le 4^e(4e)^2(32e^2)^{2h+1}.
\tag{11}
\]

The deliberately loose factor `4e` also covers the one-vertex convention and a root lying on a
cotree edge. No topological move is required to remain inside the Werner incidence class; (11)
is only an injection into finite combinatorial codes.

For `h>=1`, the genus-independent polynomial in (11) can be charged to the first handle:

\[
 R_{e,h}^{(2)}
 \le 4^e\bigl(2^{19}e^8\bigr)^h.
\tag{12}
\]

Indeed, `(4e)^2(32e^2)=512e^4`, the remaining `2h` reinsertion factors give
`(1024e^4)^h`, and `512e^4<=(512e^4)^h` for `h>=1`.

## 5. Minimal Catalan weight

If the cycles of `C` have lengths `l_1,...,l_k`, then

\[
 P_0(\mathsf C)=\prod_j\operatorname{Cat}_{l_j-1}.
\]

Using `Cat_q<=4^q` gives

\[
 P_0(\mathsf C)
 \le4^{\sum_j(l_j-1)}
 =4^{E-\#\mathsf C}
 \le4^E.
\tag{13}
\]

Since `E=2N` and `e=2E=4N`, this is simply

\[
 P_0(\mathsf C)\le2^e=16^N.
\tag{14}
\]

This is a per-triple upper bound. It converts the ordinary-map counts (8) and (12) into weighted
counts without confusing an unweighted map count with the minimal Weingarten mass.

## 6. Constants

For `h=0`, equations (5), (8), and (14) give

\[
 S_{N,0}
 \le e^2 8^e
 =16N^2\,4096^N.
\tag{15}
\]

For every `N>=2`,

\[
 16N^2\le8^N,
\tag{16}
\]

with equality at `N=2` and an immediate ratio induction thereafter. Thus

\[
 S_{N,0}\le32768^N.
\tag{17}
\]

For `N=1`, there are at most `(2!)^2=4` choices of `A,B`, with `C` forced and
`P_0(C)=1`, so (17) also holds.

For `h>=1`, equations (5), (12), and (14) give

\[
 S_{N,h}
 \le4096^N\bigl(2^{19}(4N)^8\bigr)^h
 =4096^N\bigl(2^{35}N^8\bigr)^h.
\tag{18}
\]

There is no positive-genus connected triple at `N=1`: the genus identity would require
`#A+#B+#C=4-2h`, while the left side is at least three. For `N>=2`,

\[
 2^{35}\le N^{35},
\]

so

\[
 S_{N,h}\le4096^N N^{43h}
 \le32768^N N^{43h}.
\tag{19}
\]

Equations (17) and (19) prove the candidate bound (2), with

\[
 D=32768,\qquad \alpha=43.
\]

The constants are intentionally conservative. The important facts are the `4096^N` raw weighted
base and a polynomial loss per handle.

## 7. Monotone Weingarten paths

The structural genus `h` and the monotone-path excess `g` are different indices. At minimal path
length, the constellation contributes `P_0(C)d^(-2h)` in the connected sector. The already
reviewed monotone-path estimate gives, for each fixed skeleton,

\[
 \sum_{g\ge0}P_g(\mathsf C)d^{-2g}
 \le \frac{P_0(\mathsf C)}{1-\theta_{N,d}},
 \qquad
 \theta_{N,d}=\frac{6(2N)^{7/2}}{d^2},
\tag{20}
\]

whenever `theta_(N,d)<1`. Because this multiplier is uniform skeleton by skeleton, summing (20)
over (1) gives

\[
 \text{full path weight at structural genus }h
 \le \frac{32768^N N^{43h}}{1-\theta_{N,d}}.
\tag{21}
\]

For fixed `m` and `N<=c_m log d`, the multiplier is `1+o(1)`. Thus monotone backtracking does not
alter the exponential base `D` and does not create another factorial. It also does not solve the
label-count problem below.

## 8. Equality-graph components: the remaining centered-bound obstruction

Let `kappa(sigma,tau)` be the number of connected components of the equality graph generated by
the row and column pairings. For one fixed structural triple, the number of compatible physical
tuple labelings is at most

\[
 m^{\kappa(\sigma,\tau)}.
\tag{22}
\]

The constellation component count and `kappa` must not be conflated:

- transitivity of `(A,B,C)` is the topological connectedness used in (1) and gives `d^(-2h)`;
- `kappa` counts generator-label degrees of freedom and supplies powers of `m`.

Neither the ordinary map count nor the Catalan weight bounds `kappa`. A sufficient additional
statement would be the existence of universal constants `b,L` such that every counted admissible
connected genus-`h` skeleton satisfies

\[
 \kappa(\sigma,\tau)\le N+b+Lh.
\tag{23}
\]

Under (23), the normalized minimal genus-`h` mass would obey

\[
 m^{-2N}\,m^{N+b+Lh}\,S_{N,h}\,d^{-2h}
 \le
 m^b\left(\frac{32768}{m}\right)^N
 \left(\frac{m^L N^{43}}{d^2}\right)^h.
\tag{24}
\]

The inequality `32768<sqrt(18m)` is exactly what makes

\[
 32768/m<\sqrt{18/m},
\]

the target-compatible planar base. For fixed `m` and `N<=c_m log d`, the bracket in (24) is
`o_m(1)`, so positive genera would sum geometrically.

But (23) is not proved for the full class. The identity-pairing family makes the necessity of an
`h`-dependent label allowance rigorous. Take odd `N`, `sigma=tau=id`. Then the equality graph has

\[
 \kappa=2N,
\]

while the connected constellation has genus `(N-1)/2`. All `[m(m-1)]^N` edge-label sequences are
compatible. Hence no genus-independent bound of the form `kappa<=N+O(1)` can hold on all connected
constellations. This family is consistent with a bound having `L>=2`; it does not refute (23).

There is a second scope boundary: (1) counts only the transitive sector. Two-component
constellations have a different Euler power `d^(2-2h)` and require their own return/centering
analysis. They are not silently included in (24).

Therefore (2), even after independent review, would prove the structural weighted-count node but
would not by itself prove `HEXT.same-tuple-werner-centered-bound`.

## 9. Ordinary count, weighted count, and sufficient moment theorem

The three logically distinct statements are:

1. **Ordinary rooted-map count.** Equations (8) and (12) count uncolored two-face ribbon maps.
   Boundary phase makes this an upper bound for constellation triples without a color or
   factorial multiplier.
2. **Minimal weighted constellation count.** Multiplying by (14) gives (2). This is the exact
   target of `HEXT.werner-two-boundary-constellation-count`.
3. **Centered-moment bound.** This additionally needs a uniform equality-component theorem such
   as (23), treatment of the two-component sector, the exact Euler-to-Weingarten interface, and
   the already reviewed monotone tail. Only then does the fixed-`m`, `N=O(log d)` quantifier in
   (24) become available.

An exponential ordinary map count alone is not enough; an exponential Catalan-weighted count
alone is still not enough for the centered theorem; and a fixed-`N` moment statement is not enough
for an extreme-eigenvalue bound. These quantifiers must remain separate.

## 10. Status recommendation and limitations

The derivation supplies a target-compatible candidate proof of the exact current structural
claim, with explicit constants `D=32768` and `alpha=43`. Because this artifact is newly derived
and has not received independent adversarial review, the node should be at most `CONJECTURED`; no
canonical change is made here.

The most review-sensitive points are:

- the face-phase injectivity after forgetting the three colors;
- the rooted planar coefficient (6) and its root convention;
- the canonical spanning-tree/cotree code and the absence of an ordering factorial; and
- the separation between topological components and equality-graph components.

No claim is made that the spanning-tree deletion is an admissible physical surgery. No
support-at-least-three surgery is proposed or repeated. The missing equality-component theorem is
not hidden inside the structural count. `HEXT.same-tuple-werner-centered-bound` remains unresolved,
and the full-size extensive-violation statement remains `OPEN`.
