# Exact H4-reduced no-go theorem for pentagonal hypermetrics

Date: 2026-08-30  
Status: **complete exact obstruction, awaiting independent review**.  The
global classical upper bound and equality-set completeness remain **OPEN**.

## 1. Question and answer

Let `U` be the implicit `307200 x 600` sign matrix of the currently certified
`C`-level cuts, and let

\[
M=U^TU.
\]

The previous triangle audit reduced equality-compatible hypermetric discovery
to the exact shell

\[
b^TMb=307200.                                                 \tag{1}
\]

The next candidate family is the pentagonal pattern

\[
b=e_i+e_j+e_k-e_l-e_m.                                       \tag{2}
\]

This note gives a complete, symmetry-reduced exact census and proves:

> **Five-term no-go.**  No vector with exactly five nonzero coefficients,
> each in `{+1,-1}`, satisfies (1).  In particular, no pentagonal vector (2)
> is tight on all `307200` known equality cuts.

The proof is stronger than a floating-point energy search.  It uses the exact
decomposition of the known cuts into `4800` six-dimensional terminal faces
and checks an equivalent collection of integer conditions.  The result is
relative to the known equality set: it neither proves that this set is
complete nor proves the desired global upper bound.

## 2. Hypermetric equality and the exact matrix

For a cut sign vector `u` and an integer vector `b` whose coordinate sum is
odd,

\[
h_b(u)=\frac{(b^Tu)^2-1}{4}\geq 0.                            \tag{3}
\]

The inequality holds because `b^Tu` is an odd integer.  It is tight exactly
when `b^Tu` is `+1` or `-1`.  Summing over the known cuts gives

\[
\sum_u h_b(u)=\frac{b^TMb-307200}{4}.                        \tag{4}
\]

Thus (1) is necessary and sufficient for `b` to be tight on every known cut.
The checker independently reconstructs `M` from the six-faces using exact
`int64` arithmetic and verifies its canonical hash:

```text
shape:                    600 x 600
diagonal:                 307200
canonical int64 SHA-256:  71a507ef2e641adf4515907dec377f8552b7a07e5fae75196f8ba9ba6ff0b3f1
```

## 3. A terminal-face equality lemma

Consider one known six-face.  Let `V` be its six free coordinates, and let
`f` be its fixed sign vector, with `f_i=0` on `V`.  Suppose `b` has exactly
five nonzero coefficients in `{+1,-1}`.  Put

\[
r=|\operatorname{supp}(b)\cap V|,
\qquad
A=\sum_{i\notin V}b_if_i.
\]

As the face variables range independently, `b^Tu` ranges over

\[
A+\epsilon_1+\cdots+\epsilon_r,
\qquad \epsilon_i\in\{+1,-1\},                              \tag{5}
\]

where the signs of the coefficients have been absorbed into the independent
`epsilon_i`.  Every vertex of the face is tight if and only if every value in
(5) has absolute value one.  This happens exactly in the following two cases:

\[
(r=0\text{ and }|A|=1)
\quad\text{or}\quad
(r=1\text{ and }A=0).                                       \tag{6}
\]

For `r>=2`, (5) contains at least three distinct values in an arithmetic
progression of step two, so they cannot all belong to `{-1,+1}`.  Therefore
(6) is an exact necessary and sufficient terminal condition.  In particular,
two selected support coordinates may never be simultaneously free in any
known terminal face.

## 4. H4 reduction and meet in the middle

The exact affine H4 action is transitive on the `600` signed literals of one
party.  The equality terminals are also closed under party swap.  Therefore,
if any five-term candidate exists, an equivalent candidate has one signed
literal fixed to `+e_0`.

Coordinate `0` is free in exactly `48` of the `4800` terminal faces.  Removing
the coordinate itself and all coordinates that are co-free with it leaves

```text
555 allowed coordinates
1110 allowed signed literals
```

On each of those `48` faces, the other four selected literals must have fixed
sum zero by (6).  Split the four literals into two unordered pairs.  For each
locally legal pair, record its exact `48`-entry contribution vector.  The
other pair must have the negative contribution vector.  This is a complete
meet-in-the-middle reduction, not a heuristic: every four-element set has a
pair partition, and every equality-compatible set must occur in a pair of
opposite signature buckets.

The exact census is:

```text
locally legal signed-literal pairs:       568692
distinct 48-face pair signatures:         134755
unordered complementary pair-pairings:  3164360
after all co-free conflict constraints:   652266
after all 4800 exact face conditions:           0
```

The last line proves the five-term no-go theorem.  By (4), it is equivalent to
the absence of five-term `{+1,-1}` vectors on the exact quadratic shell (1).

## 5. A first non-hypermetric small-cluster obstruction

The same terminal geometry excludes a broad family of seven-coordinate local
facets without needing their explicit coefficient lists.

There are `1200` distinct terminal free six-sets `V` across both parties.  For
each `j` outside `V`, form the seven-coordinate cluster

\[
S=V\cup\{j\}.                                                 \tag{7}
\]

All `1200*594=712800` extensions are distinct.  On the terminal face with
free set `V`, the sign of `j` is fixed while the six signs in `V` range over
all `2^6` possibilities.  Modulo global sign, these are exactly all `64` cut
vertices on seven labeled coordinates.  Consequently, a local linear
cut-polytope inequality supported on `S` that is tight on this whole terminal
face is tight on every vertex of `CUT_7`.  It is therefore an identity, not a
proper facet.

> **Seven-cluster facet no-go.**  No proper local `CUT_7` facet, hypermetric
> or genuinely non-hypermetric, supported on a cluster (7) can vanish on all
> known equality cuts.

Under H4 together with party swap, the `712800` clusters form `73` orbits:

```text
orbit size  2400:   6 orbits
orbit size  3600:   4 orbits
orbit size  7200:  31 orbits
orbit size 14400:  32 orbits
```

This is a rigorous first obstruction for non-hypermetric local facets, but it
does not cover arbitrary seven-coordinate clusters.

## 6. Replay

Checker:

```text
grothendieck-d4/tools/h4_pentagonal_hypermetric_no_go_checker.py
```

SHA-256:

```text
ee6bb77e12b53515ecc9bed001f92d833aa2da74c06daf9e78cb295d9f0a88f3
```

Run from the repository root in an environment containing `numpy` and
`h5py`:

```sh
python3 \
  grothendieck-d4/tools/h4_pentagonal_hypermetric_no_go_checker.py
```

The final status is `EXACT_PENTAGONAL_NO_GO_PASSED`.

## 7. Status split

**Established exactly in this draft (not yet independently reviewed):**

* the terminal-face equality criterion (6);
* the complete H4-reduced five-term census and pentagonal no-go;
* the `712800`-cluster, `73`-orbit census; and
* the seven-cluster proper-facet no-go, including non-hypermetric facets on
  those clusters.

**Refuted routes relative to the known equality terminals:**

* a root strengthening by any single pentagonal hypermetric required to stay
  tight on all known equality cuts;
* any nonnegative cone of five-term hypermetrics with that same tightness
  requirement (each nonzero generator has positive aggregate slack); and
* a proper seven-node local facet supported on a terminal free six-set plus
  one coordinate.

**Still open:**

* completeness of the `307200` known `C`-level sign pairs;
* seven-term and higher hypermetrics;
* proper `CUT_7` facets on the remaining seven-coordinate cluster orbits;
* larger non-hypermetric cluster facets; and
* the global inequality `W(s,t)>=0`.

The next exact search should exploit the same face criterion on the uncovered
seven-coordinate cluster orbits before attempting arbitrary facet lifting.
