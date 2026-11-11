# Affine H4 symmetry and exact equality terminals for the d=4 cut

Date: 2026-08-30  
Status: **complete exact lemma, awaiting independent review**.  The global
classical upper bound remains **OPEN**.

## 1. Setup

Let `A` be the frozen symmetric 300 by 300 integer matrix, let `a,b` be the
archived sign pair, and put

\[
 B_{ij}=a_iA_{ij}b_j,\qquad
 C=a^TAb=2081044153087351400.
\]

For bit vectors `s,t` define

\[
 x(s)_i=a_i(-1)^{s_i},\qquad
 y(t)_j=b_j(-1)^{t_j},
\]

\[
 W(s,t)=\frac{C-x(s)^TAy(t)}2,
 \qquad F(s)=\min_t W(s,t).
\]

The exact right-variable elimination formula is

\[
 F(s)=\sum_{i:s_i=1}r_i+
       \sum_j\min\left(0,c_j-2\sum_{i:s_i=1}B_{ij}\right),       \tag{1}
\]

where `r_i=sum_j B_ij` and `c_j=sum_i B_ij`.

## 2. Exact affine action on the eliminated function

Write a signed H4 element as `g=(p,epsilon)`, acting on a sign vector by

\[
 (gz)_i=\epsilon_i z_{p(i)}.
\]

The four archived generators satisfy, entry by entry over the integers,

\[
 A_{ij}=\epsilon_i\epsilon_j A_{p(i),p(j)}.                    \tag{2}
\]

Define two translation bits

\[
 \alpha_i^a(g)=[a_i\epsilon_i a_{p(i)}=-1],\qquad
 \alpha_i^b(g)=[b_i\epsilon_i b_{p(i)}=-1],
\]

and affine maps on bit vectors

\[
 \phi_g^a(s)_i=s_{p(i)}\mathbin{\mathsf{xor}}\alpha_i^a(g),
 \qquad
 \phi_g^b(t)_i=t_{p(i)}\mathbin{\mathsf{xor}}\alpha_i^b(g).    \tag{3}
\]

Direct substitution gives

\[
 gx(s)=x(\phi_g^a(s)),\qquad gy(t)=y(\phi_g^b(t)).              \tag{4}
\]

Equation (2) then implies the exact identities

\[
 W(\phi_g^a(s),\phi_g^b(t))=W(s,t),\qquad
 F(\phi_g^a(s))=F(s).                                         \tag{5}
\]

The second equality follows because `phi_g^b` is a bijection.  Thus the full
14400-element signed H4 group, not merely the six-element stabilizer of the
selected witness pair, is available for exact canonicalization of the
left-only pseudo-Boolean function.  The action is affine: its translations
are precisely the H4 images of the selected candidate.

The checker generates all 14400 signed permutations and reproduces the
archived action SHA-256

```text
1a5582d7fd1ce1c01135421413aa8fb7c6761fc953622e37387231f58c5f0097
```

The left translations `alpha^a(g)` form 2400 distinct points, each with
multiplicity six.  This recovers the candidate stabilizer order six directly
in the affine left action.

The same action applies to ternary partial assignments used by a left-only
coverage DAG: fixed bits transform by (3), while a free bit remains free.  An
exhaustive orbit calculation under the four generators gives the first two
nontrivial layer sizes:

| fixed left coordinates | raw ternary nodes | affine-H4 orbits |
|---:|---:|---:|
| 1 | 600 | 1 |
| 2 | 179400 | 34 |

For the two-fixed-coordinate layer the exact orbit-size distribution is

```text
1200: 6 orbits
1800: 1 orbit
2400: 2 orbits
3600: 6 orbits
7200: 18 orbits
14400: 1 orbit
```

Thus exact canonicalization reduces the whole depth-one layer to one node and
the depth-two layer to 34 nodes.  This is a finite statement about the
coverage-DAG search space, not a lower bound on `F`.

## 3. Two base six-faces after exact elimination

The switched column fields are all nonnegative, and their exact zero set is

\[
 Z=\{46,56,85,99,131,148\}.                                  \tag{6}
\]

Therefore `F(0)=0`, and exactly the 64 right assignments supported in `Z`
minimize the right variables at `s=0`.

Let

\[
 \delta_i=[a_i\ne b_i].
\]

The matrix is symmetric and `|delta|=83`.  Party swap sends the preceding
right six-face to the left six-face

\[
 s=\delta\mathbin{\mathsf{xor}}u,quad u\subseteq Z,
 \qquad t=\delta.                                               \tag{7}
\]

For all 64 choices of `u`, exact evaluation of (1) gives

\[
 F(\delta\mathbin{\mathsf{xor}}u)=0.                           \tag{8}
\]

Moreover every one of the 300 right fields in (1) is nonzero, with its sign
selecting `t=delta`.  Hence the minimizing right assignment in (7) is unique
for every point of the base left face.  This is stronger than merely checking
that the displayed sign pair has value `C`.

## 4. Exact terminal orbit census

Applying (3) to the two base faces produces the following descriptors.  Put
`V_g=p^{-1}(Z)`.

* Right-face terminal:

  \[
  s=\alpha^a(g),\qquad
  t\in \alpha^b(g)+\langle V_g\rangle.
  \]

* Swapped-left-face terminal:

  \[
  s\in \alpha^a(g)+(\delta\circ p)+\langle V_g\rangle,
  \qquad
  t=\alpha^b(g)+(\delta\circ p).
  \]

Here addition is xor and `+<V_g>` means independently flipping the six listed
coordinates.  Exact enumeration gives:

| certified object | exact count |
|---|---:|
| distinct right six-face descriptors | 2400 |
| distinct swapped-left six-face descriptors | 2400 |
| points in the swapped-left faces | 153600 |
| affine left translation points | 2400 |
| distinct left assignments certified to have `F(s)=0` | 156000 |
| sign pairs of value exactly `C` from the right-face family | 153600 |
| sign pairs of value exactly `C` from the swapped-left family | 153600 |
| union of the two sign-pair families | 307200 |

There are three exact disjointness statements:

1. the 2400 swapped-left six-faces are pairwise disjoint;
2. their 153600 left points are disjoint from the 2400 affine translation
   points supporting the right-face terminals; and
3. the two 153600-element families of sign pairs are disjoint.

Consequently a left-only coverage certificate may terminate immediately at
at least 156000 explicitly described left assignments: 2400 fixed-left
right-face terminals and 2400 pairwise-disjoint left six-face terminals.
This does **not** say that these are all zeros of `F`.

## 5. Replay

The exact checker is

```text
grothendieck-d4/tools/h4_affine_equality_terminals_checker.py
```

with SHA-256

```text
d9b7687704e3ac8575e3bcd9c092b06270315b439aeadbd40a141143da2435dd
```

In a Python environment containing `numpy` and `h5py`, run from the repository
root:

```sh
python3 \
  grothendieck-d4/tools/h4_affine_equality_terminals_checker.py
```

The checker verifies the MAT MD5 and canonical `A` hash, checks exact signed
invariance of every Coxeter generator, regenerates the full group and its
action hash, evaluates (1) using Python integers on the 64 base left-face
points, exhaustively computes the one- and two-fixed-coordinate affine orbit
censuses, and checks all finite face incidences and pair counts.  Its final
status is `EXACT_CHECK_PASSED`.

## 6. Scope and remaining gap

Established by the proof and checker:

* full affine H4 invariance of `W` and the left-eliminated function `F`;
* exact canonical coverage counts 1 and 34 at depths one and two;
* exact minimization on both base six-faces;
* 2400 pairwise-disjoint swapped-left six-faces;
* 156000 explicit left assignments with `F=0`; and
* 307200 explicit sign pairs with objective value exactly `C`.

Not established:

* `F(s)>=0` for every one of the `2^300` left assignments;
* completeness of the two H4 orbits of six-faces or of the displayed
  `C`-level sign pairs; or
* any high-order rational cut-polytope dual closing a branch outside these
  terminal sets.

The exact lemma therefore advances the canonical-coverage and terminal parts
of certificate version 2, but the high-order bound-terminal construction
remains the global bottleneck.
