# Independent review: Werner boundary-preserving support-five gate

Date: 2026-08-30

Reviewer: independent Codex review context `/root/weyl_majorization_audit`.

## Independence, scope, and method

I did not author
`holevo-extensive-violation/artifacts/WERNER_BOUNDARY_PRESERVING_SUPPORT_FIVE_GATE_20260830.md`
or any of the claims proposed there. I read `DAG_PROTOCOL.md` and `FILE_PROTOCOL.md` in full and
reconstructed the permutation identities, the `N=4` example, the support-four obstruction, and
the support-five move independently. I did not use web access, start a certificate or enumeration
process, or edit canonical YAML. This immutable report is the only project file created by the
review.

The review covers:

1. the fixed-`rho` normal form and its exact recovered-arrow cost;
2. admissibility, connectedness, and genus of the displayed `N=4` input skeleton;
3. completeness of the `S_4` first-return reduction for all union supports of size at most four;
4. the conclusion `Delta<=0` for that full support range;
5. the displayed support-five product, connectedness, genus decrement, arrow count, label loss,
   and minimal Catalan factor; and
6. the precise boundary between this singleton example and the still-open universal/full-size
   assertions.

The instruction not to recompute is material. I checked the orbit coverage and row totals in the
displayed finite table, but did not rerun its 20-by-576 histogram. Instead, I give below an
independent Cayley-distance proof of the load-bearing inequality for every support of size at most
four.

## Executive verdict

The mathematical core **passes**, with one scope qualification that must be retained at node
registration: the support-five output is a connected genus-zero **structural constellation**, not
an admissible contraction for the original two-label coloring. The artifact already permits such
intermediate structural moves and charges their changed pairing arrows as label defects, so this is
not a defect in the artifact. It would become a mathematical error only if a node called the output
an admissible Werner contraction.

Three atomic statements are safe to register and assess `PROVED`, using the exact review-locked
wording and hashes in the next section:

1. the fixed-boundary surgery normal form and arrow/label cost;
2. the support-at-most-four obstruction for the one displayed admissible `N=4` input; and
3. the explicit support-five structural genus-one base case.

Combining the last two shows that the minimum union support of a genus-lowering fixed-`rho`
**structural** move for this one skeleton is five. It does not show that every positive-genus
skeleton has a support-five move, or even a uniformly bounded-support move. The universal
boundary-preserving genus-reduction claim remains `OPEN`, the weighted constellation-count claim
remains `OPEN`, and the full same-tuple centered-spectrum claim remains unresolved. No full-size
extensive conclusion follows.

## Immutable inputs and exact hashes

| object | SHA-256 |
|---|---|
| `DAG_PROTOCOL.md` | `d8775b511431e6e9dc7a5be6200af80bd612e7e7d5f5ff10bb14ef748791a095` |
| `FILE_PROTOCOL.md` | `d9d6fb57a26fef3b70fc05bda74a29101d83a43df60e06eaeb345e76980fc595` |
| reviewed artifact | `970ca548853db5038f8362fc963a2109d4fbbd7f66f4058b62d6116fcc6457f3` |
| `HEXT.werner-boundary-preserving-genus-reduction.yaml` | `3a59fdae98ffea42c536eaad0310c9f9b831de033fc759f481ee8666f9b233e2` |
| `HEXT.werner-two-boundary-constellation-count.yaml` | `0e79a2590f57f164696fcd33e4789da41a2a398761436e8178cd8ea5f7c51030` |
| `HEXT.same-tuple-werner-centered-bound.yaml` | `6f5943d8e564e653e0e0a25caf500ca883131933fdca37d6455a25d6fbacde9e` |

The three proposed atom names were not canonical YAML files at review time. To make the review
hash-bindable, I lock the exact prospective claim text here. Hashes are
`sha256(claim.strip())` after ordinary UTF-8 encoding; the blockquote soft line breaks below are
single spaces, matching YAML folded-scalar normalization.

### `HEXT.werner-boundary-surgery-normal-form`

> Fix permutations J and rho. If ABC=rho, then every structural triple A'B'C'=rho is uniquely
> A'=Ap, B'=p^(-1)Bq, C'=q^(-1)C. Under sigma=A^(-1)J and
> tau=C^(-1)A^(-1)J, exactly |supp(p)| row arrows and |supp(qp^(-1))| column
> arrows change. Thus a move with s=|supp(p) union supp(q)| changes at most 2s tuple-label
> equality incidences and costs at most m^(2s) in label summation.

Exact claim hash:
`sha256:911646e9e5f10a79e820d1f8b46621265300f405cfb687ee537aea87e3d4ff2b`.

### `HEXT.werner-support-four-surgery-obstruction`

> On X={0,...,7}, let A=(0 5)(1 6)(2 7)(3 4), B=(0 4)(1 5)(2 6)(3 7),
> C=(4 6)(5 7), and rho=(0 3 2 1)(4 7 6 5). This is a connected admissible N=4
> genus-one Werner skeleton, and every fixed-rho structural move A'=Ap, B'=p^(-1)Bq,
> C'=q^(-1)C with |supp(p) union supp(q)|<=4 satisfies #A'+#B'+#C'<=14.
> Hence no connected structural move of union support at most four lowers its genus.

Exact claim hash:
`sha256:ef280ec2c336b60ab11753de38fce1a30dda4296afce6d64b25612e0a44f1912`.

### `HEXT.werner-support-five-genus-one-base-case`

> For A=(0 5)(1 6)(2 7)(3 4), B=(0 4)(1 5)(2 6)(3 7), C=(4 6)(5 7), and
> rho=(0 3 2 1)(4 7 6 5), the fixed-rho structural move p=(0 5)(1 6), q=(4 6)
> gives A'=(2 7)(3 4), B'=(0 4 2 1)(3 7)(5 6), and C'=(5 7). The output
> structural constellation is connected and genus zero; it need not preserve the original tuple
> coloring. The union support has size five, exactly nine row/column arrows change, and the minimal
> Catalan factor P0(C')/P0(C) equals one.

Exact claim hash:
`sha256:97e76f903e4307804fcb0f49f26772e4e704d22bdf20e13e14c4f4b70f63ec0b`.

Current exact hashes of the unresolved canonical claims are:

| node | exact claim hash | verdict |
|---|---|---|
| `HEXT.werner-boundary-preserving-genus-reduction` | `sha256:da2372c1444105ffdc94c2170774c956ce455e70d63c013b3d0ac9f2fcf0644b` | remains `OPEN` |
| `HEXT.werner-two-boundary-constellation-count` | `sha256:918abca3f6ba28a5ad1d894a5b9e917cc5114081c8a7fcdd16dc28c78d0bb603` | remains `OPEN` |
| `HEXT.same-tuple-werner-centered-bound` | `sha256:c221c71b9f3cb3294d7c9c7d979cf1a154042ea4ec013f95d3fc7955c2c38da5` | remains unresolved; no promotion |

## Findings

### Finding WBPS5-IR-01 — PASS: fixed-boundary normal form is exact and unique

**Locator:** reviewed artifact, `## 2. Every fixed-boundary surgery has a normal form`, equations
`(8)--(10)`.

Given `A'B'C'=ABC`, define

`p=A^(-1)A'` and `q=(AB)^(-1)A'B'`.

Then `A'=Ap`, `A'B'=ABq`, hence `B'=p^(-1)Bq`, and cancellation in the fixed product gives
`C'=q^(-1)C`. Conversely these formulas multiply to `ABC`. The displayed definitions also prove
uniqueness; there is no residual gauge freedom once `A,B,C` are fixed.

**Verdict:** PASS for the prospective normal-form claim at hash
`sha256:911646e9e5f10a79e820d1f8b46621265300f405cfb687ee537aea87e3d4ff2b`.

### Finding WBPS5-IR-02 — PASS: recovered arrows and `m^(2s)` defect cost

**Locator:** reviewed artifact, `## 2`, equations `(11)--(15)`.

The inverse encoding gives

`sigma'=A'^(-1)J=p^(-1)sigma`

and

`tau'=C'^(-1)sigma'=C^(-1)q p^(-1)C tau`.

Because a permutation is bijective, left multiplication by `r` changes exactly `|supp(r)|`
arrows. Thus the row count is exactly `|supp(p)|`; the column multiplier is conjugate to
`qp^(-1)`, so the column count is exactly `|supp(qp^(-1))|`. Both supports lie inside
`supp(p) union supp(q)`, giving at most `2s` changed arrows. Deleting `L` old equality-graph
edges raises the component count by at most `L`, and adding replacement edges cannot raise it.
The label-summation loss is therefore at most `m^L<=m^(2s)`.

This is defect accounting for a structural move. It does not assert that the recovered pairings
preserve the original coloring.

**Verdict:** PASS.

### Finding WBPS5-IR-03 — PASS: the `N=4` input is an actual admissible connected genus-one skeleton

**Locator:** reviewed artifact, `## 4. An actual admissible genus-one skeleton`, equations
`(16)--(20)`.

The displayed `sigma` and `tau` preserve the two blocks `{0,1,2,3}` and `{4,5,6,7}`, so with
`lambda(V_i)=1`, `lambda(A_i)=2` they satisfy both exact admissibility equations. The recovered
permutations are

`A=(0 5)(1 6)(2 7)(3 4)`,

`B=(0 4)(1 5)(2 6)(3 7)`, and

`C=(4 6)(5 7)`.

Their product is `rho=(0 3 2 1)(4 7 6 5)`. The union of the `A` and `B` matching edges is the
single alternating eight-cycle

`0-5-1-6-2-7-3-4-0`,

so the generated action is transitive. Finally `#A=4`, `#B=4`, `#C=6`, and with `E=8` the
connected Euler identity reads `14=2E-2h`, hence `h=1`.

**Verdict:** PASS.

### Finding WBPS5-IR-04 — PASS: first-return reduction and the 20 support orbits are complete

**Locator:** reviewed artifact, `## 5. Exact obstruction at support at most four`, equations
`(21)--(25)` and Table 1.

For any permutation `P`, deleting excursions outside `S` leaves one cycle of the first-return
permutation for every original cycle meeting `S`; cycles disjoint from `S` cancel from the cycle
difference. This proves equation `(22)` and then the local expression `(24)`.

All ordered moves supported on a four-set `S` are covered by `(p,q) in Sym(S)^2`, including moves
whose actual union support is smaller. Any support of size below four can be enlarged to a
four-set without changing `p,q`, so a classification of all four-sets is sufficient.

The simultaneous rotation `g=(0 1 2 3)(4 5 6 7)` commutes with `A,B,C`. Burnside's count is

`(70+2+6+2)/4=20`:

the identity fixes all 70 four-sets, `g` and `g^3` fix only the two color blocks, and `g^2`
fixes the six unions of two of its four 2-cycles. Table 1 has two orbits of size one, two of size
two, and sixteen of size four, totaling 70. Every row totals `24^2=576`. Thus its orbit and pair
indexing is exhaustive.

**Verdict:** PASS for completeness of the classification. Per the no-recomputation instruction,
this review does not separately certify every non-load-bearing histogram bin.

### Finding WBPS5-IR-05 — PASS: independent proof of `Delta<=0` for every union support of size at most four

**Locator:** reviewed artifact, `## 5`, Lemmas 1--2 and the conclusion immediately after Table 1.

There is a short proof independent of the displayed histogram. For a four-set `S`, the
first-return permutations `a=r_(A,S)`, `b=r_(B,S)`, `c=r_(C,S)` are exactly the matching edges of
`A,B,C` whose two endpoints lie in `S`: if the mate of a point lies outside `S`, an involution
returns to the original point on its second step, producing a fixed point in the first-return map.

Let `ell(u)=4-#u` be transposition length on `Sym(S)`, and let `d(x,y)=ell(x^(-1)y)`. The local
cycle change is

`Delta=ell(a)+ell(b)+ell(c)-[ell(ap)+ell(b q p^(-1))+ell(c q^(-1))]`.

Put `x=bp`. Since `a,b,c` are involutions, the bracket equals

`d(ba,x)+d(x,q)+d(q,c)`,

which is at least `d(ba,c)=ell(abc)` by the triangle inequality.

It remains only to compare `ell(abc)` with the three individual lengths. The graph on the eight
darts whose edges are all transpositions of `A`, `B`, and `C` has girth five. Indeed, `A union B`
is the alternating eight-cycle above; the two `C` chords are `(4 6)` and `(5 7)`, and the endpoints
of each chord are at distance four along that cycle. No cycle with both disjoint `C` chords can
have length below six. Hence the subgraph induced by any `|S|<=4` is a forest. A product of the
edge transpositions of a forest has transposition length equal to its number of edges, in any
order. Therefore

`ell(abc)=ell(a)+ell(b)+ell(c)`.

The bracket is at least the initial length sum, so `Delta<=0` for every `p,q` with union support
at most four. This proves the load-bearing conclusion without trusting any unrerun table bin.

Because a connected one-handle reduction would require `Delta=2`, none exists in this support
range. The stronger cycle-sum statement holds even when disconnected structural outputs are
allowed.

**Verdict:** PASS for the prospective obstruction claim at hash
`sha256:ef280ec2c336b60ab11753de38fce1a30dda4296afce6d64b25612e0a44f1912`.

### Finding WBPS5-IR-06 — PASS with explicit structural-output scope: the support-five move

**Locator:** reviewed artifact, `## 6. A connected support-five reduction of the same skeleton`,
equations `(26)--(30)`.

For `p=(0 5)(1 6)` and `q=(4 6)`, direct cancellation and multiplication give

`A'=(2 7)(3 4)`,

`B'=(0 4 2 1)(3 7)(5 6)`, and

`C'=(5 7)`.

The normal form proves `A'B'C'=rho`. The cycle counts are `6,3,7`, versus `4,4,6`, so
`Delta=2`. Connectedness is also exact: the `B'` four-cycle reaches `0,1,2,4`; the two `A'`
edges then reach `7,3`; `C'` reaches `5` from `7`; and the `B'` edge `(5 6)` reaches `6`.
Thus the output is transitive and `6+3+7=16=2E`, giving genus zero.

The union support is `{0,1,4,5,6}`, of size five. Moreover

`|supp(p)|=4` and `qp^(-1)=(0 5)(1 4 6)` has support five,

so exactly nine recovered arrows change and the label-defect loss is at most `m^9`. Both `C` and
`C'` have minimal Catalan product one.

The recovered `sigma'=p^(-1)sigma` does not preserve the original color blocks; for example its
cycle decomposition contains `(0 3 2 6 7 4)`. Therefore this endpoint is not another admissible
contraction for the original coloring. This is consistent with the artifact's explicit structural
defect convention, but must be stated in the registered base-case claim.

**Verdict:** PASS for the prospective base-case claim at hash
`sha256:97e76f903e4307804fcb0f49f26772e4e704d22bdf20e13e14c4f4b70f63ec0b`.

### Finding WBPS5-IR-07 — PASS: exact threshold only for the singleton skeleton; universal gate remains open

**Locator:** reviewed artifact, `## 7. What a universal support-five surgery would buy`, `## 8.
What has and has not been proved`, and `## 9. Candidate atomic DAG claims`.

Findings WBPS5-IR-05 and WBPS5-IR-06 together prove that five is the minimum union support for a
genus-lowering fixed-boundary structural move on the single displayed input skeleton. They prove
two negative/positive base facts, not a universal construction. Equations `(31)--(35)` are
correctly conditional cost accounting: a hypothetical support-five move has at most `m^10` label
cost in general; the example happens to use only `m^9`. The artifact does not convert the
hypothesis into a theorem.

**Verdict:** the existing universal claim at
`sha256:da2372c1444105ffdc94c2170774c956ce455e70d63c013b3d0ac9f2fcf0644b`
must remain `OPEN`. The full-size extensive route remains `OPEN`.

## Promotion and repair instructions

1. Register the three prospective atomic claims only with the exact scope and claim text in this
   review, and link the corresponding findings with their exact claim hashes. Each may be assessed
   `PROVED`.
2. For `HEXT.werner-support-five-genus-one-base-case`, say **structural constellation** and retain
   that the endpoint need not preserve the original coloring. Do not describe the endpoint as an
   admissible Werner contraction.
3. If a separate statement claims that the minimum support is exactly five, make it a route or
   node whose premises are the support-four obstruction and the support-five base case. Bind the
   implication to this one displayed `N=4` skeleton.
4. Repair the non-claim caveat/frontier wording in
   `HEXT.werner-boundary-preserving-genus-reduction.yaml`: the prior lower bound “support at least
   three” is stale. The reviewed example rules out every union support at most four, so any
   universal one-step theorem of this normal-form kind must allow support at least five. The node's
   claim text and exact claim hash need not change, and its assessment remains `OPEN`.
5. Do not infer a universal support-five theorem, a weighted all-constellation bound, the centered
   spectrum claim, or any extensive violation. Those remain unresolved.

## Limitations

- No finite enumeration was rerun, as explicitly required. The review certifies the decisive
  support-four inequality by an independent forest/Cayley proof; exact individual histogram counts
  in Table 1 remain supplementary.
- The review checks only the fixed-`rho` structural surgery interface in the named artifact. It
  does not supply a universal bounded-support construction, a planar endpoint count, or a
  target-compatible weighted genus count.
- The `m^9` factor is an upper bound from nine changed equality arrows, not a claim that the
  equality-component count always increases by nine.
- No conclusion is drawn about a different skeleton, a different boundary permutation, or an
  admissible-color-preserving support-five endpoint.
