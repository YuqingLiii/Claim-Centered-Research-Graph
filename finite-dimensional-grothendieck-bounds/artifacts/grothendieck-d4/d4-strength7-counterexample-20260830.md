# Exact counterexample to strength-7 covering and its local-facet audit

Date: 2026-08-30  
Status: **exact counterexample and exact orbit-level obstruction, awaiting
independent review**.  No canonical DAG level is changed by this draft.

## 1. Covering-array question

For seven coordinates, a cut sign vector has `2^(7-1)=64` distinct patterns
after quotienting by simultaneous reversal of all seven signs.  The known
`307200` equality cuts would form a strength-7 covering array if every
seven-coordinate cluster projected onto all `64` patterns.

This is false.  In fact, the lexicographically first possible cluster

\[
S_0=(0,1,2,3,4,5,6)                                        \tag{1}
\]

is already a counterexample.  Its projection contains exactly `36` patterns:

```text
0, 2, 4, 6, 8, 9, 10, 11, 14, 16, 17, 18, 20, 22, 24, 25, 26, 27,
32, 33, 36, 37, 38, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 52, 53, 57
```

The missing `28` codes are

```text
1, 3, 5, 7, 12, 13, 15, 19, 21, 23, 28, 29, 30, 31,
34, 35, 39, 50, 51, 54, 55, 56, 58, 59, 60, 61, 62, 63.
```

Here a code stores the six signs relative to the first sign.  The calculation
uses the exact `4800` terminal six-faces and expands only their intersections
with (1); no floating-point or sampling step is involved.

Therefore:

> **Strength-7 refutation.**  The `307200` known equality cuts are not a
> strength-7 covering array on the `600` coordinates.

## 2. Complete symmetry orbit of the counterexample

Under the five H4 coordinate generators and party swap, (1) has an orbit of
size `7200`.  It remains the lexicographically least member.  A deterministic
encoding of the sorted orbit has SHA-256

```text
0967fdde3d8b760d0acde0c3bd54075a7ce6b39c76caa6c5777784160bfa47d9
```

No cluster in this orbit contains one of the `1200` terminal free six-sets.
Signed coordinate permutations preserve projected-pattern cardinality, so
all `7200` clusters are strength-7 counterexamples with `36` projected cut
vertices.

## 3. Does the missing-pattern cluster support a tight facet?

Missing cut vertices do not by themselves imply that the observed vertices
lie on a proper face.  A local linear cut expression on seven coordinates has
the form

\[
c+\sum_{0\leq i<j<7}a_{ij}x_{ij},                           \tag{2}
\]

where `x_ij` is the cut indicator on edge `ij`.  Thus its coefficient space
has dimension

\[
1+\binom72=22.                                               \tag{3}
\]

For each observed pattern, form its row of the `22` features in (3).  The
following `22` observed pattern codes give a square submatrix:

```text
0, 2, 4, 6, 8, 9, 10, 11, 14, 16, 17, 18, 20, 24, 25, 32, 33, 36,
37, 38, 40, 48
```

Fraction-free Bareiss elimination gives the exact determinant

\[
-32768=-2^{15}\neq0.                                        \tag{4}

Hence the `36 x 22` feature matrix has full rank `22`.  The only affine
linear expression (2) that is zero on all `36` observed vertices is the zero
expression.

> **Local-facet no-go on the counterexample orbit.**  No proper `CUT_7`
> facet, hypermetric or non-hypermetric, supported on (1) can be tight on all
> known equality cuts.  By symmetry, the same holds on all `7200` clusters in
> its orbit.

Consequently this missing-pattern orbit does not produce a cut lower-bound
strengthening that preserves the known equality cuts: there is no nonzero
candidate facet to lift or test.

## 4. Interpretation

The two notions must be kept separate:

* **vertex covering** fails: only `36/64` projected vertices occur;
* **linear unisolvence** holds: those `36` vertices already span the complete
  `22`-dimensional affine cut-feature space.

Thus global strength 7 is too strong for the known equality set, while the
failure does not automatically expose a local equality-compatible facet.

## 5. Replay

Checker:

```text
grothendieck-d4/tools/h4_strength7_counterexample_checker.py
```

SHA-256:

```text
80d2f305828745dd1a07a396ac87216e00c91ca4902b74bb2d6613949f08ae20
```

Run from the repository root with `numpy` and `h5py` available:

```sh
python3 \
  grothendieck-d4/tools/h4_strength7_counterexample_checker.py
```

The expected status is `EXACT_STRENGTH7_COUNTEREXAMPLE_PASSED`.

## 6. Status split

**REFUTED exactly in this draft:**

* the claim that the known equality cuts form a strength-7 covering array.

**Established exactly in this draft, awaiting review:**

* the explicit lexicographically first counterexample cluster (1);
* the exact `36` observed and `28` missing pattern census;
* the complete `7200`-cluster H4-plus-swap orbit census;
* the determinant certificate (4); and
* absence of every equality-compatible proper local `CUT_7` facet on that
  complete orbit.

**Still open:**

* whether every seven-coordinate projection has full rank `22` even though
  many fail full vertex coverage;
* classification of the remaining seven-cluster orbits by projection rank;
* equality-compatible facets on any rank-deficient orbit, should one exist;
* completeness of the known equality set; and
* the global classical upper bound.
