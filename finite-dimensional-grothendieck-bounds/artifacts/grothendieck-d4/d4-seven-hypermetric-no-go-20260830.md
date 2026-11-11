# Exact H4-reduced no-go theorem for seven-term hypermetrics

Date: 2026-08-30  
Status: **complete exact obstruction, awaiting independent review**.  The
global classical upper bound and equality-set completeness remain **OPEN**.

## 1. Result

Let `U` be the implicit sign matrix of the `307200` currently known `C`-level
cuts and let `M=U^TU`.  This note proves the exact finite statement

> **Seven-term no-go.**  There is no vector `b` with exactly seven nonzero
> coefficients, each in `{+1,-1}`, for which
>
> \[
> b^TMb=307200.                                               \tag{1}
> \]

In particular, this excludes every seven-term hypermetric with four `+1`
coefficients, three `-1` coefficients, and coefficient sum one.

The note also strictly excludes one complete, previously uncovered orbit of
seven-coordinate local cut-polytope facets:

> **Uncovered CUT7-orbit no-go.**  The H4-plus-party-swap orbit of
>
> ```text
> (0, 35, 137, 284, 320, 471, 594)
> ```
>
> has size `14400`, none of its clusters contains a terminal free six-set,
> and no proper `CUT_7` facet supported on any cluster in the orbit can be
> tight on all known equality cuts.

Both statements are relative to the known equality terminals.  They do not
prove that the `307200` cuts exhaust the equality set or that the candidate
classical value is a global upper bound.

## 2. Exact equality criterion

For an integer vector `b` with odd coordinate sum and a cut sign vector `u`,

\[
h_b(u)=\frac{(b^Tu)^2-1}{4}\geq0.                            \tag{2}
\]

Summing over the known cuts gives

\[
\sum_u h_b(u)=\frac{b^TMb-307200}{4}.                        \tag{3}
\]

Consequently, (1) holds if and only if `b^Tu` is `+1` or `-1` on every known
cut.  The checker reconstructs `M` from the `4800` terminal six-faces with
exact integer arithmetic and verifies

```text
canonical int64 SHA-256:
71a507ef2e641adf4515907dec377f8552b7a07e5fae75196f8ba9ba6ff0b3f1
```

The terminal-face lemma from the five-term audit applies without change.  If
`V` is the free six-set of a terminal face, `r` selected support coordinates
belong to `V`, and `A` is the signed contribution of the fixed selected
coordinates, then the whole face is tight precisely when

\[
(r=0\text{ and }|A|=1)
\quad\text{or}\quad
(r=1\text{ and }A=0).                                       \tag{4}
\]

In particular, a candidate support cannot contain two coordinates that are
co-free in a terminal face.

## 3. Symmetry and the 48-face signature

The signed affine H4 action is transitive on the `600` signed literals of one
party, and exact symmetry of the original matrix permits party swap.
Therefore a hypothetical seven-term candidate can be transformed so that one
literal is `+e_0`.  This reduction does not need to preserve the conventional
coefficient-sum-one normalization: the search deliberately covers the larger
class of all seven-term `{+1,-1}` vectors.

Coordinate `0` is free in `48` terminal faces.  Removing it and every
coordinate co-free with it leaves `555` coordinates and `1110` signed
literals.  On each of those `48` faces, the remaining six literals must have
fixed sum zero.

For a signed literal `ell`, let `P(ell)` be its 48-bit positive-value mask.
For a triple `T=(ell_1,ell_2,ell_3)`, its coordinatewise positive counts lie
in `{0,1,2,3}`.  They are represented exactly by two 48-bit words:

\[
\begin{aligned}
p(T)&=P(\ell_1)\mathbin{\mathrm{xor}}P(\ell_2)
      \mathbin{\mathrm{xor}}P(\ell_3),\\
m(T)&=(P(\ell_1)P(\ell_2))\mathbin{\mathrm{or}}
      (P(\ell_1)P(\ell_3))\mathbin{\mathrm{or}}
      (P(\ell_2)P(\ell_3)).                                 \tag{5}
\end{aligned}

Here juxtaposition in (5) denotes bitwise `and`.  The pair `(p,m)` is an exact
96-bit encoding of all 48 counts: the four possibilities `0,1,2,3` map to
`(0,0),(1,0),(0,1),(1,1)`.

Split the six remaining candidate literals into triples `A` and `B`, and let
`C=-B` be obtained by reversing the signs of the literals in `B`.  The six
literals balance on all 48 faces exactly when

\[
(p(A),m(A))=(p(C),m(C)).                                    \tag{6}

Every globally compatible support is internally conflict-free, so both `A`
and `C` occur in the exhaustive triple list.  Conversely, two distinct
triple representations satisfying (6), with disjoint and mutually
non-conflicting coordinate supports, give every possible candidate surviving
the first 48 faces.  Thus this meet-in-the-middle reduction is complete.

## 4. Complete exact census

The C++ kernel enumerates every internally conflict-free signed triple and
sorts them by (6).  A deterministic 64-bit hash is used only to accelerate
the first grouping.  Within every repeated hash bucket, the kernel recomputes
and compares the full 96-bit signature (5); hence hash collision assumptions
are not part of the proof.

The exact census is:

```text
internally conflict-free signed triples:       178939832
repeated hash groups:                            18022838
repeated exact-signature groups:                 18022838
same-signature triple-representation pairings: 3457621250
after all cross-support conflict tests:          356229760
after all 4800 terminal-face conditions:                 0
```

The zero in the last line proves the seven-term no-go.  Together with (3), it
is a complete exact exclusion of the seven-coordinate `{+1,-1}` shell of
(1), not a failure to locate a vector by local search.

## 5. A complete uncovered CUT7 cluster orbit

The canonical cluster

\[
S=(0,35,137,284,320,471,594)                                \tag{7}
\]

does not contain any of the `1200` terminal free six-sets.  Its orbit under
the five H4 coordinate generators and party swap has size `14400`; direct
membership checks show that no cluster in the orbit contains such a six-set.

Nevertheless, projecting the known terminal faces onto (7), normalizing by
global sign, gives all

\[
2^{7-1}=64
\]

cut vertices on seven labeled coordinates.  Any local linear cut-polytope
inequality supported on `S` and tight on all known cuts is therefore tight on
every vertex of `CUT_7`.  It is an identity and cannot be a proper facet.
H4 and party-swap invariance propagate this conclusion to the complete
`14400`-cluster orbit.  This rules out hypermetric and non-hypermetric facets
uniformly on that orbit.

## 6. Replay

Wrapper checker:

```text
grothendieck-d4/tools/h4_seven_hypermetric_no_go_checker.py
```

SHA-256:

```text
858ccef0f7a565b56e683ba8f73b0a23ce08c15a73303ce7b6c43e325ad8dc84
```

Pinned C++ kernel:

```text
grothendieck-d4/tools/h4_seven_hypermetric_mitm.cpp
```

SHA-256:

```text
c4cbbb3aa344ccff37c8a67480112346a3cad23cf0da704ad6710af07554a749
```

Run from the repository root in an environment containing `numpy`, `h5py`,
and a C++17 compiler:

```sh
python3 \
  grothendieck-d4/tools/h4_seven_hypermetric_no_go_checker.py
```

The run uses approximately 3.5 GB of working memory for the compact triple
records and prints `EXACT_SEVEN_TERM_NO_GO_PASSED`.

## 7. Status split

**Established exactly in this draft (not independently reviewed):**

* the complete 178939832-triple, 3457621250-pairing census;
* absence of all equality-compatible seven-term `{+1,-1}` vectors;
* absence of conventional coefficient-sum-one seven-term hypermetrics;
* the exact `14400`-cluster orbit census for (7); and
* full `CUT_7` projection and proper-facet no-go on that orbit.

**Refuted routes relative to the known equality terminals:**

* a root strengthening by a seven-term `{+1,-1}` hypermetric required to
  remain tight on all known equality cuts; and
* any proper local `CUT_7` facet, including a non-hypermetric facet, supported
  on the orbit (7).

**Still open:**

* completeness of the known equality cuts;
* nine-term and more general integer hypermetrics;
* other seven-coordinate cluster orbits whose known-cut projection is not yet
  certified full;
* larger non-hypermetric facets and nonlocal cut certificates; and
* the global inequality `W(s,t)>=0`.
