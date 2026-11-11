# Werner equality components versus topological genus

Date: 2026-08-30

Status: proposer-side pure-theory artifact for Question 3. No canonical YAML is changed. Every
new node proposed below should remain at most `CONJECTURED` until independent adversarial review.
The weighted constellation count used conditionally here is itself newly proposer-side. The
centered spectral claim and the full-size extensive-violation theorem remain **OPEN**.

No browser, new certificate run, or large computation is used.

## 1. Outcome

Let `E=2N`, let

\[
 X=\{V_i,A_i:i\in\mathbb Z/N\mathbb Z\},
\]

and retain the exact physical permutations

\[
 J(V_i)=A_i,\quad J(A_i)=V_i,
 \qquad
 \rho(V_i)=V_{i-1},\quad \rho(A_i)=A_{i-1},
 \qquad K=J\rho.
\tag{1}
\]

For an admissible contraction skeleton, the row and column permutations `sigma,tau` preserve a
physical tuple labeling `lambda` satisfying

\[
 \lambda(V_i)\ne\lambda(A_i).
\tag{2}
\]

Use the exact constellation interface

\[
 \mathsf A=J\sigma^{-1},\qquad
 \mathsf B=\sigma K\tau\sigma^{-1},\qquad
 \mathsf C=\sigma\tau^{-1},\qquad
 \mathsf A\mathsf B\mathsf C=\rho,
\tag{3}
\]

and let `c in {1,2}` be the number of topological/transitive components and `h` the sum of their
genera. Let

\[
 \kappa(\sigma,\tau)
 :=\#\operatorname{Orb}\langle\sigma,\tau\rangle
\tag{4}
\]

be the number of tuple-label equality components. These are different component notions.

Put

\[
 q_N:=\#K=\begin{cases}1,&N\text{ odd},\\2,&N\text{ even}.
 \end{cases}
\tag{5}
\]

The main exact bound is

\[
 \boxed{
 \kappa(\sigma,\tau)
 \le N-2c+q_N+2+2h-|\mathsf C|,
 }
\tag{6}
\]

where `|P|=E-#P` is transposition length. In particular every admissible connected skeleton
satisfies

\[
 \boxed{\kappa(\sigma,\tau)\le N+2+2h.}
\tag{7}
\]

Thus the missing equality-graph component gate in
`WERNER_TWO_BOUNDARY_CONSTELLATION_WEIGHTED_COUNT_20260830.md` has universal constants

\[
 b=2,\qquad L=2.
\tag{8}
\]

The constants are sharp in the following precise sense: no universal finite-`b` theorem can have
`L<2`, and with `L=2` one must have `b>=2`. The admissible identity-pairing repeated-edge family
attains the parity-refined version of (6) exactly.

For the two-topological-component sector, (6) improves to

\[
 \kappa\le
 \begin{cases}
 N-1+2h,&N\text{ odd},\\
 N+2h,&N\text{ even}.
 \end{cases}
\tag{9}
\]

Moreover, if either one-boundary component has genus zero, its corresponding trace word freely
reduces to the identity. Hence every two-component skeleton with total genus `h<=1` lies in the
already controlled union of the forward-return and reverse-return sectors. This does **not** mean
that centering removes every two-component diagram: an explicit admissible `N=4,c=2,h=2` example
below has two nonreturn words.

The remaining nonreturn two-component sector therefore starts only at `h>=2`, where its Euler
power is already at most `d^(-2)`. A direct two-unicellular-map code gives the auxiliary candidate
weighted count

\[
 S^{(c=2)}_{N,h}\le4096^N N^{24h}\qquad(h\ge2).
\tag{10}
\]

Together with (9), its normalized minimal mass is at most

\[
 \left({4096\over m}\right)^N
 m^2N^{24}
 \left({m^2N^{24}\over d^2}\right)^{h-1}.
\tag{11}
\]

For fixed `m` and `N<=c_m log d`, the handle ratio in (11) tends to zero. This supplies a clean
proposer-side separation of the two-component sector; it does not promote the centered theorem.

## 2. Exact source bindings and scope

This note starts from the exact interface proved in
`WERNER_PERMUTATION_CONSTELLATION_SURGERY_GATE_20260830.md`, whose SHA-256 at derivation time is

`c52f59c7e301a154925149689b13897a54cf462bf9674ef16105f9a2dd3d1a88`.

The new weighted-count artifact being extended is
`WERNER_TWO_BOUNDARY_CONSTELLATION_WEIGHTED_COUNT_20260830.md`, SHA-256

`f4d0b8b92366c0aa353b3f7794c9a0b1a5326aa0602ecc9323f6f9a9e51a8bab`.

Its target structural claim is currently bound to exact statement hash

`sha256:918abca3f6ba28a5ad1d894a5b9e917cc5114081c8a7fcdd16dc28c78d0bb603`.

The already derived return-sector estimate is in
`WERNER_CENTERED_GROWING_TRACE_METHOD_GATE_20260830.md`, SHA-256

`6f0d52b4d48433c9f16d8ded4440469268b336df3af8f23f4a8b798ac15752ce`.

This note does not independently review the new `32768^N N^(43h)` connected weighted count. It
proves the missing label-component inequality conditionally used with that count, and separately
gives a count for the disconnected nonreturn sector. Minimal and excess monotone Weingarten paths,
the exact signed moment assembly, and the final Markov step retain their own node boundaries.

## 3. Equality components are not topological components

The equality graph `H(sigma,tau)` has vertex set `X` and undirected edges

\[
 \{s,\sigma(s)\},\qquad \{s,\tau(s)\}.
\tag{12}
\]

Its connected components are exactly the orbits of `<sigma,tau>`, so their number is `kappa`.
Every `sigma`-cycle and every `tau`-cycle lies inside one equality component. Consequently

\[
 \#\tau\ge\kappa,qquad
 |\tau|=E-\#\tau\le E-\kappa.
\tag{13}
\]

By contrast, `c` counts the orbits of `<mathsf A,mathsf B,mathsf C>`. Because their product is
`rho` and `rho` has two cycles, `c` is one or two. The topological Euler identity is

\[
 \#\mathsf A+\#\mathsf B+\#\mathsf C+2-2E=2c-2h.
\tag{14}
\]

No implication such as `kappa=c` is used or true. For example, the connected repeated-edge
family in Section 5 has `c=1` and `kappa=2N`.

## 4. Proof of the universal component theorem

### Lemma 1: admissibility forces `mathsf A` to be fixed-point free

If `mathsf A(s)=s`, then by (3)

\[
 J\sigma^{-1}(s)=s,
\]

so `sigma^(-1)(s)=J(s)`, equivalently `sigma(Js)=s`. Since `sigma` preserves `lambda`, this gives

\[
 \lambda(Js)=\lambda(s),
\]

contrary to (2). Hence every cycle of `mathsf A` has length at least two. Since `|X|=E=2N`,

\[
 \#\mathsf A\le N,qquad |\mathsf A|=E-\#\mathsf A\ge N.
\tag{15}
\]

This is the only place where the physical off-diagonal condition is used. An uncolored abstract
constellation need not satisfy (15).

### Lemma 2: exact length budget

Subtracting (14) from `3E` gives

\[
 |\mathsf A|+|\mathsf B|+|\mathsf C|
 =E-2c+2h+2.
\tag{16}
\]

Using (15) and `E=2N`,

\[
 |\mathsf B|+|\mathsf C|
 \le N-2c+2h+2.
\tag{17}
\]

This is the step that genus bookkeeping alone misses if admissibility is discarded.

### Lemma 3: `K` transfers the length budget to the equality graph

Cycle count is invariant under conjugation, and (3) gives

\[
 |\mathsf B|=|K\tau|.
\tag{18}
\]

The triangle inequality in transposition length gives

\[
 |K|\le |K\tau|+|\tau^{-1}|
 =|\mathsf B|+|\tau|.
\]

Therefore

\[
 |\tau|\ge |K|-|\mathsf B|.
\tag{19}
\]

Because `J` commutes with `rho`, `K^2=rho^2`. If `N` is odd, an orbit of `K` traverses all `2N`
points; if `N` is even, there are two `N`-cycles. Thus

\[
 \#K=q_N,qquad |K|=E-q_N.
\tag{20}
\]

Combining (13), (17), (19), and (20),

\[
\begin{aligned}
 E-\kappa
 &\ge |\tau|\\
 &\ge E-q_N-|\mathsf B|\\
 &\ge E-q_N-
       \bigl(N-2c+2h+2-|\mathsf C|\bigr).
\end{aligned}
\]

Rearranging proves (6):

\[
 \kappa\le N-2c+q_N+2+2h-|\mathsf C|.
\]

For `c=1`, this is

\[
 \kappa\le N+q_N+2h-|\mathsf C|
 \le N+2+2h.
\tag{21}
\]

For `c=2`, it gives (9), with the additional nonpositive term `-|mathsf C|` available whenever
useful. This completes the proof.

## 5. Sharpness: the identity-pairing repeated-edge family

For every `N>=2`, set

\[
 \lambda(V_i)=1,qquad \lambda(A_i)=2,qquad \sigma=\tau=id.
\tag{22}
\]

This is admissible. It has

\[
 \mathsf A=J,qquad \mathsf B=K,qquad \mathsf C=id.
\tag{23}
\]

The group generated by `J,K` contains `rho=JK`; `rho` moves around each boundary and `J` connects
the two boundaries. Hence the constellation is connected for every `N`, not just odd `N`.

Here

\[
 \#\mathsf A=N,qquad \#\mathsf B=q_N,qquad
 \#\mathsf C=2N,qquad \kappa=2N.
\tag{24}
\]

Euler's identity gives

\[
 h={N-q_N\over2}.
\tag{25}
\]

The parity-refined bound (21) is an equality:

\[
 N+q_N+2h-|\mathsf C|=N+q_N+(N-q_N)=2N.
\tag{26}
\]

As `N` grows, (24)--(25) show that any inequality `kappa<=N+b+Lh` with fixed `b` must have
`L>=2`. With `L=2`, the even family has

\[
 2N=N+b+N-2,
\]

so `b>=2`. Therefore the universal pair `(b,L)=(2,2)` is optimal in exactly the sense claimed.

## 6. Consequence for the connected weighted count

Assume the proposer-side connected structural estimate

\[
 S_{N,h}\le32768^N N^{43h}
\tag{27}
\]

is independently validated. The physical label count is at most `m^kappa`; applying (7), the
normalized connected minimal genus-`h` mass is bounded by

\[
\begin{aligned}
 m^{-2N}m^{N+2+2h}S_{N,h}d^{-2h}
 &\le
 m^2\left({32768\over m}\right)^N
 \left({m^2N^{43}\over d^2}\right)^h.
\end{aligned}
\tag{28}
\]

The project regime has `32768<sqrt(18m)`. For fixed `m` and `N<=c_m log d`, the handle ratio in
(28) is `o_m(1)`. Thus (6) supplies exactly the missing equality-component input to the conditional
mass algebra of the weighted-count artifact, with better constants than the provisional
`N+b+Lh` placeholder required.

Equation (28) is a conditional implication, not a review or promotion of (27), and not by itself a
proof of the centered high-probability statement.

## 7. Exact two-component structure

If `c=2`, the two topological orbits must be the two `rho` cycles

\[
 X_V=\{V_i\},\qquad X_A=\{A_i\}.
\tag{29}
\]

Thus `mathsf A,mathsf B,mathsf C` each preserve `X_V` and `X_A`. From the inverse formulas

\[
 \sigma=\mathsf A^{-1}J,qquad
 \tau=\mathsf C^{-1}\mathsf A^{-1}J,
\tag{30}
\]

both `sigma` and `tau` exchange `X_V` and `X_A`. In the exact matrix-index model, their restrictions
pair the unstarred and starred occurrences within each of the two trace factors. The incidence
ribbon realization therefore separates into two rooted unicellular components, one for the
forward trace boundary and one for the block-reversed trace boundary.

This is a topological factorization statement. It does not say that `kappa=2`, nor that the two
random traces are independent, nor that the full finite-`d` Weingarten coefficient factors into a
product.

### Lemma 4: a genus-zero one-boundary component forces a return word

Consider either trace boundary and draw its row/column contraction ribbons in its one-face
component. If the component has genus zero, cutting along the boundary realizes it in a disk. An
outermost contraction ribbon has two adjacent endpoints among the remaining boundary occurrences.
Haar balance makes those endpoints a starred and an unstarred occurrence of the same generator,
so they are inverse adjacent letters in the signed boundary word. Delete that ribbon and its two
boundary occurrences. The residual components are again planar disk contraction diagrams.

Induction on the number of occurrences removes the whole boundary word by adjacent inverse-letter
cancellations. Hence the corresponding free word is the identity.

Equivalently, the same induction can be read from the rooted plane-tree thickening: choose a leaf
strip, delete its out-and-back traversal, and repeat. The argument uses the actual signed Haar
pairing labels; it is not the false assertion that every abstract genus-zero uncolored map carries
a return word.

Let the two component genera be `h_V,h_A`, so `h=h_V+h_A`. If `h<=1`, at least one of them is zero.
Lemma 4 then shows that either the forward word `w` or the block-reversed word `check w` is the
identity. The return-sector estimate already bounds the total absolute contribution of the union
of those sequences by

\[
 2d^2\left({3m-4\over m^2}\right)^N.
\tag{31}
\]

Thus the potentially enhanced Euler powers `d^2` at `c=2,h=0` and `d^0` at `c=2,h=1` are both
captured by the independently separated safe return sector. Centering supplies the off-diagonal
condition (2); the return-word argument, not centering alone, supplies (31).

## 8. Positive-genus two-component diagrams are not all returns

The qualifier in the preceding section is necessary. Take `N=4`, identify `V_i=i` and `A_i=4+i`,
and set

\[
 \sigma=\tau=(0\ 5)(1\ 7)(2\ 4)(3\ 6).
\tag{32}
\]

Then

\[
\begin{aligned}
 \mathsf A&=(0\ 1\ 3\ 2)(4\ 6\ 7\ 5),\\
 \mathsf B&=(0\ 1\ 2)(3)(4\ 6\ 7)(5),\\
 \mathsf C&=id,
\end{aligned}
\tag{33}
\]

and direct multiplication gives `mathsf A mathsf B mathsf C=rho`. The displayed cycles preserve
`X_V` and `X_A`, so `c=2`. Each restriction has cycle sum `1+2+4=7`; with eight ordinary incidence
edges and one face, each component has Euler characteristic zero and genus one. Hence total
`h=2`.

The equality components are

\[
 \{0,5\},\quad\{1,7\},\quad\{2,4\},\quad\{3,6\}.
\tag{34}
\]

Assign them labels `1,2,3,4` in the displayed order. This gives

\[
 (v_0,v_1,v_2,v_3)=(1,2,3,4),
 \qquad
 (a_0,a_1,a_2,a_3)=(3,1,4,2),
\tag{35}
\]

and every `v_i!=a_i`. Both `sigma` and `tau` preserve the coloring. After the only immediate
cancellations, the two reduced words are

\[
 \operatorname{red}(w)
 =g_1^{-1}g_3g_2^{-1}g_1g_3^{-1}g_2,
\tag{36}
\]

and

\[
 \operatorname{red}(\check w)
 =g_4^{-1}g_2g_3^{-1}g_4g_2^{-1}g_3.
\tag{37}
\]

Both are nonempty. Therefore one may separate the two-component sector from the dangerous low
genera, but one must not identify the entire two-component sector with return words. Total genus
two is the first possible nonreturn location allowed by Lemma 4, and (32)--(37) realize it.

## 9. Weighted count for the residual two-component sector

For `c=2`, each `rho` orbit contains `N` darts and hence its incidence component has

\[
 e_0=2N
\tag{38}
\]

ordinary ribbon edges and one rooted face. A connected one-face genus-`g` map with `e_0` edges has
`e_0+1-2g` vertices. A deterministic depth-first spanning tree therefore leaves exactly `2g`
cotree edges.

Delete those cotree edges in reverse deterministic order. The remainder is a rooted plane tree,
with at most `4^(e_0)` codes. Each deleted edge is recovered from an ordered pair of safe corners
and an orientation bit, at cost at most `32e_0^2`; the physical face root costs at most `4e_0`.
This gives the self-contained injection

\[
 U(e_0,g)\le4^{e_0}(4e_0)(32e_0^2)^{2g}.
\tag{39}
\]

The boundary phase recovers all incidence colors and dart names on each component, so the product
of the two ordinary-map codes is an upper count for the two-component constellations. Summing over
`h_V+h_A=h` and using the per-skeleton minimal Catalan bound `P_0(mathsf C)<=16^N` gives

\[
 S^{(c=2)}_{N,h}
 \le
 (h+1)\,64N^2\,4096^N\,(2^{14}N^4)^h.
\tag{40}
\]

For `N>=2`, each one-face genus is at most `N`, so `h+1<=2N+1<=3N`. For `h>=2`,

\[
 (h+1)64N^2\le192N^3\le N^{6h},
 \qquad
 2^{14h}\le N^{14h}.
\]

Equation (40) therefore implies the deliberately rounded bound (10):

\[
 S^{(c=2)}_{N,h}\le4096^N N^{24h}.
\]

The `N=1` residual nonreturn sector is empty and may be checked directly. No unicellular
trisection theorem or external enumeration is used in (39); it is the same elementary
spanning-tree/cotree code as the two-face weighted-count artifact.

Combining (9), (10), and the exact two-component Euler power `d^(2-2h)` proves (11). A uniform
monotone-path excess multiplier can then be applied skeleton by skeleton. The base `4096` is
strictly smaller than the already target-compatible connected base `32768`.

## 10. Failed and rejected routes

1. **Topological transitivity bounds `kappa`.** False. The connected identity-pairing family has
   `kappa=2N`. The successful proof uses admissibility plus the Euler length budget.
2. **Use only `#C`.** Although `C` preserves every equality component and `#C>=kappa`, this is a
   lower, not an upper, cycle comparison. It does not prove the target.
3. **Sum the lengths of `sigma` and `tau`.** The equality-graph rank need not be their sum; two
   permutations may generate the same mergers. The proof avoids this projective-norm analogue and
   uses only the safe inequality `|tau|<=E-kappa`.
4. **A genus-independent `N+O(1)` bound.** The repeated-edge family rules it out. Its exact
   equality cases also show that replacing `L=2` by any smaller universal constant is impossible.
5. **All two-component diagrams are return/product terms.** False. Equations (32)--(37) are an
   admissible counterexample. Only a component of genus zero forces its boundary to return; hence
   the correct safe statement is `c=2,h<=1`.
6. **Centering alone kills `c=2`.** False. Centering gives `v_i!=a_i`, which is used in Lemma 1,
   but does not make the positive-genus example vanish.

## 11. Candidate atomic nodes (not applied)

All statements below are proposer-side and should be registered at no higher than `CONJECTURED`
until independent review.

### `HEXT.werner-admissible-equality-component-genus-bound`

> For every admissible Werner contraction skeleton on `E=2N` physical slots, with `c in {1,2}`
> topological constellation components, total genus `h`, and
> `q_N=1` for odd `N`, `q_N=2` for even `N`, the tuple-label equality graph satisfies
> `kappa(sigma,tau) <= N-2c+q_N+2+2h-|C|`. In particular every connected skeleton has
> `kappa<=N+2+2h`. The universal constants `b=2,L=2` are optimal in the parity-uniform form.

Suggested premises: the exact contraction-skeleton ribbon injection and exact constellation Euler
deficit nodes. The proof also uses the physical admissibility condition `v_i!=a_i`; it must not be
stated for arbitrary uncolored triples.

### `HEXT.werner-two-component-low-genus-return-separation`

> If an admissible Werner constellation has two topological components and total genus at most
> one, at least one of its forward and block-reversed free words is the identity. Hence this sector
> is contained in the already bounded return union. The assertion does not extend to total genus
> two.

Suggested premise: the exact reversal trace formula/return-sector bound. Equations (32)--(37)
should be linked as the exact scope counterexample.

### `HEXT.werner-two-component-nonreturn-weighted-count`

> For the two-component nonreturn sector, necessarily `h>=2`; its total minimal Catalan weight is
> at most `4096^N N^(24h)`, its equality graph has at most `N+2h` components, and after moment
> normalization its genus-`h` absolute mass is bounded by (11).

This last node should remain conditional on the existing minimal-Catalan and exact
Euler-to-Weingarten interfaces and should not be described as the centered spectral theorem.

## 12. Remaining scope

The equality-component inequality (6) removes one explicit algebraic gate from the connected
weighted-count proposal. It neither independently validates that proposal's map injection and
constants nor supplies a completed immutable growing-moment dossier. The two-component analysis
removes a common scope ambiguity but does not alter the need to assemble all minimal and excess
Weingarten terms with the exact signed reversal moment through `N=Theta(log d)`.

Accordingly:

- the new atomic claims are proposer-side at most `CONJECTURED`;
- `HEXT.werner-two-boundary-constellation-count` keeps its present status pending its own review;
- `HEXT.same-tuple-werner-centered-bound` remains unresolved; and
- the full-size extensive-violation theorem remains **OPEN**.
