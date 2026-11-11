# A rank-20 CUT7 orbit from two exact quadrilateral relations

Date: 2026-08-30  
Status: **exact draft result, awaiting independent review**.  No canonical
YAML, index, or graph is modified here.

## 1. Result

The preceding rank-21 audit found an H4-plus-party-swap orbit of
four-coordinate cores on which every known equality cut satisfies a
quadrilateral relation.  Combining two distinct cores gives a still lower
rank seven-cluster.

The canonical representative is

\[
 S_{20}=(0,1,2,248,268,269,288).                           \tag{1}
\]

For the feature map consisting of a constant and the `21` `CUT_7` edge
coordinates, the known equality projection on (1) has exact rank `20`.
Its complete H4-plus-party-swap orbit has size `3600`.

The two-dimensional nullspace does **not** contain a valid nonzero `CUT_7`
inequality.  Hence the rank defect gives no local facet and no strengthening
of the classical cut relaxation.

## 2. Systematic double-core census

Let `O_4` be the complete `1800`-member orbit of the core

\[
 (0,1,269,288).                                             \tag{2}
\]

First classify the core relation itself.  A signed pair event is a relation
`s_a=epsilon s_b`, with `a<b` and `epsilon in {+1,-1}`.  There are
`2*C(600,2)=359400` such events.  Exact orbit enumeration under H4 and party
swap gives `70` signed-pair-event orbits, with deterministic orbit-record
digest

```text
a0ba7c275933803d23f08429c0ac743251611713add5d296793e371b68340c86
```

For one representative of each orbit, restrict the `4800 x 600` terminal-face
sign matrix to the faces on which the first pair event is not identically
true.  A second disjoint pair completes a quadrilateral identity precisely
when its two columns are fixed and equal up to the required sign on every
restricted row.  Exact column-signature grouping finds partners for only one
of the `70` representatives:

```text
(0,1,+): (269,288,+), (286,295,+), (289,299,+).
```

The three displayed supports all lie in `O_4`.  Consequently **every**
two-pair quadrilateral identity of the form

\[
 (s_a-\epsilon s_b)(s_c-\eta s_d)=0
\]

belongs to the single support orbit `O_4`.

Enumerate every unordered pair of distinct cores in `O_4` that intersects,
and retain pairs whose union has at most seven coordinates.  Exact set
enumeration gives

| item | count |
|---|---:|
| intersecting core pairs | `36000` |
| distinct unions of size `6` | `3600` |
| distinct unions of size `7` | `32400` |

Every size-7 union contains exactly two members of `O_4`.  The
lexicographically least size-7 union is precisely (1), arising from

\[
 (0,1,269,288),\qquad (0,2,248,268).                       \tag{3}
\]

An additional exact triple-incidence audit checks every one-coordinate
extension of the `3600` size-6 unions.  None contains a third core.  Therefore
no seven-coordinate set contains three quadrilateral cores from this complete
family.  In particular, quadrilateral identities alone cannot force feature
rank below `20` on seven coordinates.

Thus (1) is not the output of blind random sampling: it is the canonical
first candidate in a complete exact pair-union census of the previously
proved core orbit.

## 3. Exact rank certificate

Modulo simultaneous reversal of all seven cut signs, the known equality
cuts project onto the following `34` codes on (1):

```text
0, 1, 2, 3, 4, 5, 8, 9, 12, 13, 14, 15, 16, 18, 20, 28, 30,
32, 34, 40, 44, 46, 48, 49, 50, 51, 52, 53, 56, 57, 60, 61, 62, 63.
```

Using the local ordering in (1), the two relations supplied by (3) are

\[
\begin{aligned}
 Q_1&=x_{05}-x_{06}-x_{15}+x_{16},\\
 Q_2&=x_{03}-x_{04}-x_{23}+x_{24}.
\end{aligned}                                               \tag{4}
\]

Every one of the `34` rows annihilates both coefficient vectors, and the two
vectors are independent.  Hence the feature rank is at most `20`.

For the reverse inequality, choose the `20` pattern rows

```text
0, 1, 2, 3, 4, 5, 8, 9, 12, 14, 16, 18, 20, 28, 32, 34, 40,
44, 48, 49
```

and feature columns

```text
0,1,2,3,4,5,6,7,8,9,10,12,14,15,16,17,18,19,20,21.
```

The resulting integer `20 x 20` matrix has fraction-free Bareiss
determinant

\[
 -8192=-2^{13}\neq0.                                       \tag{5}
\]

Therefore the exact feature rank is `20`, and (4) is a basis of the complete
nullspace.

The H4-plus-party-swap orbit of (1) has size `3600`, has (1) as its least
member, and has sorted-orbit digest

```text
48931b756d544220564820b4701355b0c7f191a5c5092bf0872b406ea0188337
```

Signed symmetry acts invertibly on affine cut features, so every orbit member
has exact rank `20`.

## 4. No valid facet in the two-dimensional nullspace

Evaluate `(Q_1,Q_2)` on all `64` vertices of `CUT_7`.  The exact joint value
census is

| value | count |
|---|---:|
| `(-2,-2)` | `1` |
| `(-2,0)` | `6` |
| `(-2,2)` | `1` |
| `(0,-2)` | `6` |
| `(0,0)` | `36` |
| `(0,2)` | `6` |
| `(2,-2)` | `1` |
| `(2,0)` | `6` |
| `(2,2)` | `1` |

In particular, normalized cut codes `17` and `33` give `(2,0)` and
`(-2,0)`, while codes `6` and `10` give `(0,2)` and `(0,-2)`.

Suppose a nullspace combination `lambda Q_1+mu Q_2` were nonnegative on all
cut vertices.  The first witness pair forces simultaneously `lambda>=0` and
`lambda<=0`, hence `lambda=0`.  The second pair likewise forces `mu=0`.
The same conclusion holds for the opposite orientation.

Therefore:

> **Rank-20 orbit facet no-go.**  The only valid `CUT_7` inequality in the
> equality-compatible nullspace of (1) is zero.  No proper local face is tight
> on all known equality cuts on any cluster in the complete `3600`-member
> orbit.

Adding a nonzero nullspace combination to a cut relaxation would exclude a
genuine integral cut.  Hence this rank defect cannot improve the root or any
descendant cut relaxation.

## 5. Replay

Checker:

```text
grothendieck-d4/tools/h4_rank20_double_quadrilateral_checker.py
```

SHA-256:

```text
6c17403a88c6917c582d5aa3b7c25142c50bc48559574b24773e3752b939f030
```

Run from the repository root with `numpy` and `h5py` available:

```sh
python3 \
  grothendieck-d4/tools/h4_rank20_double_quadrilateral_checker.py
```

Expected status:

```text
EXACT_RANK20_DOUBLE_QUADRILATERAL_PASSED
```

The checker pins the rank-21 checker by SHA, reconstructs all exact equality
faces and group actions, classifies all `359400` signed pair events into `70`
orbits, proves the single-core-orbit theorem, repeats the complete `36000`
core-pair and size-6-extension census, verifies (4), checks determinant (5),
enumerates the `3600`-cluster orbit, and tests every `CUT_7` vertex against the
full nullspace basis.

## 6. Status split

**PROVED exactly in this draft, awaiting review:**

* the complete pair-union census inside the `1800`-core orbit;
* completeness of that core orbit for all signed two-pair quadrilateral
  identities;
* no seven-coordinate set contains three such cores;
* the canonical cluster (1) has exact cut-feature rank `20`;
* its complete `3600`-cluster orbit has exact rank `20`; and
* no equality-compatible proper `CUT_7` facet exists on that orbit.

**REFUTED exactly:**

* any universal seven-cluster rank lower bound of `21` or `22`; and
* the route from this two-dimensional nullspace to a valid cut
  strengthening.

**OPEN:**

* whether some seven-cluster has feature rank below `20` through a genuinely
  non-quadrilateral relation;
* a complete exact rank census over all seven-cluster orbits;
* whether any other rank-deficient nullspace contains a supporting
  inequality;
* completeness of the known equality set; and
* the global classical upper bound.
