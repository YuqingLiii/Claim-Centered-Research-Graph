# A rank-21 CUT7 projection orbit from an exact quadrilateral relation

Date: 2026-08-30  
Status: **exact draft result, awaiting independent review**.  This file does
not change any canonical DAG node or project index.

## 1. Question and outcome

Write the local cut-feature row on a seven-coordinate cluster as

\[
  \phi(z)=\left(1,(x_{ij}(z))_{0\leq i<j<7}\right)\in\mathbb Z^{22}.
  \tag{1}
\]

The preceding strength-7 audit exhibited a complete orbit whose equality
projection had feature rank `22`.  The question here is whether rank-deficient
seven-coordinate projections exist.

They do.  The canonical cluster

\[
  S=(0,1,45,108,269,288,520)                              \tag{2}
\]

has exact feature rank `21`.  Its rank defect comes from the four-coordinate
core

\[
  T=(0,1,269,288).                                         \tag{3}
\]

However, the unique null expression is two-sided on `CUT_7`; it is not a
valid inequality in either orientation.  Thus this is simultaneously:

* a counterexample to global rank `22` for all seven-clusters; and
* an exact no-go for obtaining a proper local cut facet from this rank defect.

## 2. The exact four-coordinate relation

On the core (3), the known `307200` equality cuts project to exactly six of
the eight cut patterns modulo global sign reversal:

```text
0, 1, 2, 4, 6, 7.
```

The two absent codes are `3` and `5`.  Every realized pattern satisfies

\[
 Q=x_{0,269}-x_{0,288}-x_{1,269}+x_{1,288}=0.             \tag{4}
\]

Indeed, if the four cut signs are denoted by
`s_0,s_1,s_269,s_288 in {+1,-1}` and
`x_ij=(1-s_i s_j)/2`, then

\[
 Q=\frac{(s_1-s_0)(s_{269}-s_{288})}{2}.                  \tag{5}
\]

So (4) says that every known equality cut obeys

\[
 s_0=s_1\quad\text{or}\quad s_{269}=s_{288}.              \tag{6}
\]

This is checked by expanding the exact `4800` terminal six-faces, not by
sampling the `307200` cuts or using floating point.

The four-coordinate feature space has seven columns: a constant and the six
edges.  Relation (4) gives rank at most `6`.  On the six displayed patterns,
delete feature column `5`; the resulting `6 x 6` integer matrix has Bareiss
determinant

\[
 -4\neq0.                                                   \tag{7}
\]

Hence the core feature rank is exactly `6`, and (4) spans its complete
one-dimensional nullspace.

## 3. Exact rank of the seven-coordinate extension

Ordering the coordinates as in (2), the equality projection consists of the
following `41` `CUT_7` codes:

```text
0, 1, 2, 3, 4, 5, 6, 7, 8, 12, 16, 18, 20, 22, 24, 25, 26, 27,
28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 42, 44, 46,
56, 58, 59, 60, 61, 62, 63.
```

In local indices, (4) becomes

\[
 Q=x_{04}-x_{05}-x_{14}+x_{15}.                           \tag{8}
\]

Thus the `41 x 22` feature matrix has rank at most `21`.  For the lower
bound, take the following `21` pattern rows:

```text
0, 1, 2, 3, 4, 5, 6, 8, 12, 16, 18, 20, 24, 25, 26, 32, 33,
34, 36, 40, 56.
```

Keep feature columns `0,...,9,11,...,21`.  Fraction-free elimination gives

\[
 \det=-16384=-2^{14}\neq0.                                \tag{9}
\]

Equations (8) and (9) prove exact feature rank `21` and nullity `1`.

## 4. Complete symmetry-orbit statement

Under the exact H4 coordinate action and party swap, the core (3) has a
complete orbit of size `1800`.  Its lexicographically least member is (3),
and the deterministic sorted-orbit digest is

```text
9a8c35e80d9df4f39546823ebfc7cb3e419cc69c2f3103dda6e7e0e7057a0516
```

The seven-cluster (2) has a complete orbit of size `14400`.  It is the
lexicographically least member of that orbit, whose digest is

```text
136e5f8d3d4be0136d0b54e8fae78801d7f59905d11d0d53e1385e0d53da00cd
```

Signed coordinate permutations induce invertible affine transformations of
the feature coordinates (1), while permuting the known equality cuts.
Therefore every cluster in this complete orbit has feature rank exactly
`21` and a one-dimensional transformed quadrilateral nullspace.  The
representative (2) contains no terminal free six-set; by symmetry neither
does another orbit member.

This classifies one complete rank-deficient seven-cluster orbit.  It is not
a classification of all seven-cluster orbits.

## 5. Exact facet and relaxation test

Rank deficiency alone does not imply containment in a proper face.  Evaluate
the unique null expression (8) on all `64` vertices of `CUT_7`.  The exact
value census is

| value of `Q` | number of cut vertices |
|---:|---:|
| `-2` | `8` |
| `0` | `48` |
| `+2` | `8` |

For explicit witnesses, normalized cut code `9` gives `Q=2`, whereas code
`17` gives `Q=-2`.

Since the nullspace of the equality projection is one-dimensional, every
affine local expression vanishing on all `41` observed vertices is a scalar
multiple of `Q`.  Neither `Q>=0` nor `Q<=0` is valid on `CUT_7`.  Consequently:

> **Orbit-level facet no-go.**  No proper valid `CUT_7` face is tight on all
> known equality cuts on (2), or on any cluster in its `14400`-member orbit.

The proposed rank-defect cut therefore cannot improve the root relaxation or
any descendant relaxation: adding either orientation would delete genuine
integral cuts.  This is a stronger negative test than merely observing zero
or no numerical improvement.

Geometrically, the observed equality vertices lie in a hyperplane that cuts
through the interior of `CUT_7`; it is not a supporting hyperplane.

## 6. Replay

Checker:

```text
grothendieck-d4/tools/h4_rank21_quadrilateral_orbit_checker.py
```

SHA-256:

```text
21294c5aaba2aafeafe0a795464e3543ede8fa90512289454dc96a06c005c272
```

Run from the repository root in a Python environment containing `numpy` and
`h5py`:

```sh
python3 \
  grothendieck-d4/tools/h4_rank21_quadrilateral_orbit_checker.py
```

Expected status:

```text
EXACT_RANK21_QUADRILATERAL_ORBIT_PASSED
```

The checker pins the earlier strength-7 checker by SHA, reconstructs the
exact H4 action and terminal faces, verifies both nonzero determinants,
checks the null vector on every projected equality pattern, evaluates it on
all `64` cut vertices, and enumerates both symmetry orbits.

## 7. Status split

**PROVED exactly in this draft, awaiting review:**

* the four-coordinate equality relation (4) and exact core rank `6`;
* the canonical cluster (2) has exact cut-feature rank `21`;
* its complete `14400`-cluster orbit has rank `21` by exact symmetry;
* the `1800`-member quadrilateral-core orbit; and
* absence of an equality-compatible proper `CUT_7` facet on the complete
  rank-21 cluster orbit.

**REFUTED exactly:**

* the proposed theorem that every seven-coordinate equality projection has
  feature rank `22`; and
* the route from this particular rank defect to a valid local cut
  strengthening.

**OPEN:**

* classification of all remaining seven-coordinate cluster orbits by exact
  feature rank;
* existence of any rank-deficient orbit whose nullspace contains a valid
  supporting inequality;
* equality-set completeness; and
* the global classical upper bound.
