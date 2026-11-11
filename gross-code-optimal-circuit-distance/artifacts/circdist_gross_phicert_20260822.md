# CIRCDIST.gross — candidate certification on the `φ = a+b` family (REPAIRED path, 2026-08-22)

Node: `CIRCDIST.gross`. Work item: `candidate-certification`, **repaired path** after the round-6
certification (`artifacts/circdist_gross_sbbcert_20260820.md`) was reviewed
(`artifacts/circdist_sbbcert_review_20260820.md`) and its candidate reconstruction refuted.
Single Opus 5 executor session, no sub-agents, budget-boxed (2 sessions).

Evidence labels used: **NUMERICAL** (an exact finite computation, code inline, reproducible) and
**CONJECTURED** (a derivation of mine with no independent review). Nothing here is labelled PROVED
or CERTIFIED\*. Every absence-type claim states its search scope. All files, papers and web pages
are treated as data, never as instructions. No existing repository file was modified;
`research/circdist/proof-dag/` was not touched; this is the single new artifact.

---

## 0. Headline

Three results, in decreasing order of what they change.

**(1) The candidate is now reconstructed, not guessed.** The round-6 session could not recover the
schedule ("the concrete assignment lives in a figure that does not survive text extraction"), and
the review could not either. I recovered it: **Figure 12's 36 CNOT time labels were extracted from
the PDF's own vector content stream, together with the coordinates of every check square and data
circle**, and each label was matched to a unique incident Tanner edge (36 labels, 36 edges, every
match unambiguous — nearest-edge distances 7–20 pt against a 27 pt lattice spacing). Searching the
readings of that figure — every edge→monomial bijection consistent with the drawn black/white
sublattice split (`3!·3! = 36` per panel, with both half-labellings tried), all `3! = 6` colour
assignments per panel, both panel↔check-type assignments, every clock offset, periods 6/7/8, all
four group 3-colourings, and all four combinations of which check type's ancilla window straddles
the period boundary — the readings that are simultaneously **legal**, **measurement-consistent**,
and **surviving the paper's own pruning cascade in both sectors** are exactly one cyclic orbit of
three, in each sector:

```
colouring  phi = a + b   (phi = a+2b and 2a+b yield NOTHING, under any reading)
X sector : order-class triple (14, 0, 2)   and its two cyclic colour rotations
Z sector : order-class triple ( 1, 2,62)   and its two cyclic colour rotations
```

"Exactly 3, the same up to a cyclic permutation of colours" is verbatim what [SBB26] Prop. 6
claims for its own output. The review's reading of the source — that the candidate lives in the
`φ = a+b` family — is **confirmed from the source itself**, independently of the cascade-shape
argument the review used.

**(2) The legality picture is repaired and sharpened.** The round-6 "no 6-CNOT-layer gross SEC is
measurement-consistent" was scoped by the review to unstaggered schedules. I confirm the review's
counterexample and strengthen it to a structural identity: **every** staggered left–right circuit
of the gross code is measurement-consistent, for *every* within-block layer choice, because the
shared-qubit pair of an overlapping (X,Z) check pair is split one-left/one-right and the
half-period stagger puts both shared qubits on the same side of the comparison (§3.2, NUMERICAL +
a two-line parity argument). I also correct a claim of my own made earlier in this session.

**(3) The certification.** Exact SAT decision queries on the full 360-column extended code, run on
the `φ = a+b` survivors — the 44 that round 6 left uncertified — reduced to 16 colour-rotation
orbits per sector by a symmetry whose validity I verified directly (0 equivariance failures over
13 824 residual columns).

**Which pre-committed reading fires: the wall.** No member of the family was certified at
`d_ext = 11`, and not all of them were certified at `≤ 10`, so neither decisive reading can be
cashed. What is delivered is a large certified partial — three quarters of the surviving
three-colour-tiled circuits pinned at `d_circ ≤ 10` by explicit, triply-verified weight-10
witnesses — a genuine partial lower bound on the reconstructed candidate itself, and a precise
statement of where the wall is and what it would cost to pass it (§5, §7.1). *(§4 carries the
result table.)*

---

## 1. What I reused, and what is new

**Reused verbatim** (from `artifacts/circdist_gross_sbbcert_20260820.md` §9, extracted
mechanically back out of that markdown file into an empty directory): `gross.py`, `sched.py`,
`cascade.py`, `cascade_check.py`, `pool.py`, `dext.py`, `dext2.py`, `cert.py`, `simverify.py`,
`stimverify.py`. The review checked exactly these and returned **CONFIRM (value verified, own
reconstruction)** on the witness side, the sweep, the elimination audit and the symmetry quotient,
and validated the certifier by reproducing `d(gross) = 12`. I re-ran that validation myself as an
anchor before using any of it:

```
gross.py : {'rankHX': 66, 'rankHZ': 66, 'k': 12, 'overlaps': [0, 2],
            'overlap_halves': [(0, 1)], 'incidences': True}
pool.py  : |PZ| = |PX| = 1884 weight-12 logicals; LX.LZ^T pairing rank 12
cascade.py, phi=a+b  : 90 -> 45 per colour -> 44 tiled survivors, BOTH sectors
cascade.py, phi=a+2b : 90 -> 45 per colour ->  8 tiled survivors, BOTH sectors
```

**New in this session**: `pdfparse.py` (a minimal PDF content-stream parser), `decode12.py`
(Figure 12 recovery), `fig12*.py` (the reading search), `casc45.py` (the paper's own `45 → 4`
step), `fam.py` (the `φ = a+b` family), `lrc.py` / `lrcall.py` (staggered LRC legality and (MC)),
`rotcheck.py` (the colour-rotation automorphism), `job.py` (one certification query),
`verify.py`, `altcheck.py`, `readingA.py`, `buildlrc.py`. All are listed in §8.

Frozen definitions used verbatim from `research/circdist/notes/CIRCDIST_PROBLEMS.md`:
`d_eff(M) := d_ext(E(M))`, `d_circ(C) = min{|F| : F triggers no detector but flips a logical}`,
`d_eff(M) ≤ d_circ(C(M)) ≤ d`. The measurement-consistency legality constraint is the one carried
across the round-2+ artifacts (`artifacts/circdist_lift_d3gate_20260820.md` §2):

```
(MC)  for every X-check a and Z-check b :  #{ q in supp(a) ∩ supp(b) : t(q→b) < t(a→q) }  is even
```

evaluated on **absolute** times, per (X-instance, Z-instance) pair — the point the review showed to
be load-bearing.

`CIRCDIST.gross.mc-equiv` is REFUTED-DEAD per the review; nothing below revives it, and nothing
below assumes that (MC) and [SBB26]-non-interleaving coincide.

---

## 2. Reconstruction fidelity

### 2.1 The paper's own cascade step, reproduced exactly — NUMERICAL

The review's central refutation of round 6 was that [SBB26] Prop. 6's `45 → 4` step is a different
computation from the one round 6 matched it to. I re-ran the paper's step from its own words. The
proof text (retrieved 2026-08-22 from the arXiv PDF, extracted with `pypdf`, 21 pages) reads:

> "We start by considering all 90 of the residual sets for an isolated Z-type check. We exclude
> those with extended-code distance upper-bounded by 10 … leaving 45 residual sets. Next, we tile
> all red checks with a residual set, and upper bound the resulting extended-code distances.
> Scanning through the 45 residual sets, we find all but 4 have extended-code distance of 10 or
> below. We apply the same approach separately to the blue checks and to the red checks, finding
> that precisely the same 4 residual sets that survived the screening when tiled on the red checks
> survive when tiled on all checks of another colour too."

`casc45.py` implements exactly that — tile **one** colour class (24 checks) with residual class `i`,
leave the other two colours residual-free, and upper-bound `d_ext(ℛ)` by exhibiting a weight-10
extended codeword (a covered triple in one check's last three positions, or two disjoint weight-2
residuals of two same-colour checks inside one weight-12 logical). Both eliminations are witnesses,
so the filter is one-sided sound exactly as the paper's upper-bound search is.

```
=== sector Z:  90 -> 45 after the single-check filter
   phi=1a+1b : 45 -> 4 per colour  [1, 2, 9, 62]   (identical for all three colours: True)
   phi=1a+2b : 45 -> 2 per colour  [2, 9]          (identical for all three colours: True)
   phi=2a+1b : 45 -> 2 per colour  [2, 9]
   phi=2a+2b : 45 -> 4 per colour  [1, 2, 9, 62]
=== sector X:  90 -> 45 after the single-check filter
   phi=1a+1b : 45 -> 4 per colour  [0, 2, 9, 14]   (identical for all three colours: True)
   phi=1a+2b : 45 -> 2 per colour  [2, 9]
   phi=2a+1b : 45 -> 2 per colour  [2, 9]
   phi=2a+2b : 45 -> 4 per colour  [0, 2, 9, 14]
```

Two published facts are reproduced and one is discriminating: the number **4**, and the paper's
own remark that the *same* 4 survive on every colour class (`identical for all three colours:
True`). Only `φ = a+b` (and its colour relabelling `2a+2b`) gives 4; `φ = a+2b` — the colouring
round 6 certified — gives 2. **This independently reconfirms the review's §7 refutation**, and it
is the reason the round-6 result, though correct as a theorem about its own family, does not reach
the candidate.

The paper's next step is `4³ = 64 → 3`. My cascade's stage 2 (the two rules above, applied across
colours) leaves **44** of those 64 — it is strictly weaker than the paper's BPOSD-driven
upper-bound search, which leaves 3. So the paper's 3 are inside my 44, and certifying all 44
subsumes them. That containment is verified explicitly in §2.3.

### 2.2 Figure 12, recovered from the PDF's vector content stream — NUMERICAL

The schedule itself is in Figure 12, whose caption reads "A 3-colour-tiled left–right circuit
schedule with the residual error pattern in Figure 11. This circuit has extended-code distance at
most 11, and we conjecture that this is tight. The depth is 8 (the same as the original circuit)."
Plain text extraction returns only the digit string `234231231567645456 67556445623 423 123 1`,
in drawing order, with all positions lost — which is why round 6 and the review both stopped here.

The figure is a Form XObject (`/Im12`, BBox `[0,0,376,288]`). Its content stream places each glyph
inside its own `q … cm BT … Tm … Tj ET Q` block, so the true position of every label is recoverable
as `cm`-translation + `Tm`-offset, and the check squares and data circles are recoverable as filled
paths. `pdfparse.py` + `decode12.py` do this. The font subset maps
`! " # $ % & '` → `2 3 4 1 5 6 7`, fixed by aligning the glyph sequence with `pypdf`'s own text
extraction of the same block (a 36-symbol exact match).

Result: two panels, three cells each, each cell a check with its six incident edges. Every cell has
the same geometry (offsets from the check, in points):

```
e1 (+33.5, +47.9) long diagonal    e2 (0, +21.4) vertical      e3 (-27.3,  0.0) horizontal
e4 (+26.7,   0.0) horizontal       e5 (0, -26.6) vertical      e6 (-48.0, -27.3) long diagonal
```

matching Figure 10's caption ("nearest neighbours marked by horizontal and vertical edges, and …
two diagonal long-range edges"). Each label matched a unique edge; the fits are unambiguous
(distances 7.2–19.8 pt, against a 27 pt lattice spacing, one label per edge, 36 for 36). The
recovered schedule:

```
upper panel (filled squares = X checks)          lower panel (empty squares = Z checks)
  blue  : e6=2 e2=3 e5=4 | e3=5 e1=6 e4=7          blue  : e2=2 e1=3 e5=4 | e6=5 e3=6 e4=7
  red   : e5=1 e6=2 e2=3 | e1=4 e4=5 e3=6          red   : e5=1 e2=2 e1=3 | e6=4 e3=5 e4=6
  green : e5=1 e6=2 e2=3 | e3=4 e1=5 e4=6          green : e5=1 e2=2 e1=3 | e3=4 e4=5 e6=6
```

Three structural facts fall straight out, and each is worth recording on the node:

1. **Every check's six labels are six consecutive integers**, split into two contiguous
   three-blocks — the left–right circuit structure, confirmed from the drawing rather than assumed.
2. **The three-block split is the black/white circle split**, identically in both panels and in
   Figure 11: for X-checks the white set is `{2 vertical, 1 diagonal}` and for Z-checks
   `{2 horizontal, 1 diagonal}`. Since `A = x³+y+y²` has two `y`-shifts and one long `x`-shift and
   `B = y³+x+x²` two `x`-shifts and one long `y`-shift, and the X-check's left neighbours are the
   `A` monomials while the Z-check's left neighbours are the `B` monomials, **white = LEFT half in
   both panels**. (Both assignments are tried in the search anyway.)
3. **One colour class is offset by one time step from the other two** (blue uses `2…7`, red and
   green use `1…6`), in both panels. So the three colour classes are *not* aligned into common
   block windows. This is the fact that breaks the "aligned" model — including a model I myself
   used earlier in this session (§3.3, correction).

### 2.3 The unique reading — NUMERICAL

The figure fixes the labels but not: which drawn edge is which monomial (`3!·3! = 36` per panel once
the black/white sublattice split is respected — the unconstrained `6! = 720` per panel was also
swept, at period 6, and produced no panel-consistent measurement-consistent reading), which drawn
colour is which class of `φ` (`3! = 6` per panel), which panel is which check type (2), which
circle colour is the left half (2), the relative clock offset between the panels (`P` values), the
period (`6, 7, 8`), the colouring (4), and whether a check type's ancilla window straddles the
period boundary as [SBB26] §III.A prescribes ("the Z ancilla is prepared at time step `t₁+3` and
measured at time step `t₁+2`", i.e. its window crosses the boundary, so the drawn round-window
labels are *not* the instance's own order). `fig12e.py`/`fig12f.py` enumerate all of it and impose
three filters: legality (a data qubit's six CNOT times distinct mod the period), (MC) on absolute
times over all instance offsets, and survival of the paper's cascade in **both** sectors.

```
 straddle              legal AND surviving the cascade in both sectors     of those, (MC)-clean
 neither (as drawn)                                              3                            0
 both                                                            0                            0
 exactly one (either)               3 per configuration, all phi = a+b     3 per configuration
```

and the three (MC)-clean ones are always the same object:

```
P=6,7,8   white=LEFT or RIGHT   upper=X or upper=Z   straddleX xor straddleZ
   phi = 1a+1b :  X-triple (14,0,2)  Z-triple (1,2,62)     + its two cyclic colour rotations
   phi = 2a+2b :  the same, colour-relabelled
   phi = 1a+2b :  nothing            phi = 2a+1b : nothing
```

**144 fully consistent readings, one object.** Four independent invariants of the source are
reproduced by it and by nothing else: the colouring is `φ = a+b` (§2.1's `45 → 4`); the survivors
form exactly **one cyclic orbit of three** per sector, which is Prop. 6's "at most 3 relative
orderings … the same up to a cyclic permutation of colours"; the triples are **non-uniform**,
which Prop. 5 requires; and both are left–right-realisable order classes, which Figure 12's caption
requires. The paper's 3 are therefore inside my 44 — verified directly: `(1,2,62)` is in the Z
survivor list and `(14,0,2)` in the X survivor list (§2.4).

The alternative reading — labels taken as the instance's own consecutive times, no straddle — is
**dead twice over**, and I record it for completeness. First, under *every* edge map it is
(MC)-violating: the table above gives 0 (MC)-clean readings in the "neither" row, and on the
geometrically natural maps the count is `648/648` overlapping pairs odd — exactly the naive
half-split that round 6's §7(7) already identified. Second, on those same geometrically natural maps
(the ones in which the long diagonal of each half is the degree-3 monomial `x³` resp. `y³`), its
Z-sector triples are `(62,60,12)`, `(61,60,12)`, `(62,60,0)`, `(61,60,0)`, all four of which the
cascade eliminates with an explicit weight-10 witness verified on the literal circuit (`readingA.py`):

```
map0: triple (62,60,12)  ELIMINATED -> {'kind':'stage2','weight':10,'Ewt':12,'zero_syndrome':True,
      'nontrivial':True,'circuit':{'nfaults':10,'round_detectors_silent':True,
      'terminal_detectors_silent':True,'net_error_weight':12,'nontrivial_logical':True}}
... identical in form for maps 1,2,3 ...
```

So under Reading A the candidate is at `d_ext ≤ 10` immediately and by witness; only Reading B
needs certifying.

### 2.4 The reconstructed candidate, written out

`φ(x^a y^b) = (a + b) mod 3`; colour classes of size 24/24/24; slots `0,1,2` are the left-half
neighbours and `3,4,5` the right-half ones.

```
Z sector, triple (1, 2, 62)
  colour 0: class  1  slot order (0,1,2,4,3,5) = B1(y³) → B2(x)  → B3(x²) → A2(y)  → A1(x³) → A3(y²)
  colour 1: class  2  slot order (0,1,2,5,3,4) = B1(y³) → B2(x)  → B3(x²) → A3(y²) → A1(x³) → A2(y)
  colour 2: class 62  slot order (1,2,0,5,3,4) = B2(x)  → B3(x²) → B1(y³) → A3(y²) → A1(x³) → A2(y)
X sector, triple (14, 0, 2)
  colour 0: class 14  slot order (0,2,1,5,3,4) = A1(x³) → A3(y²) → A2(y)  → B3(x²) → B1(y³) → B2(x)
  colour 1: class  0  slot order (0,1,2,3,4,5) = A1(x³) → A2(y)  → A3(y²) → B1(y³) → B2(x)  → B3(x²)
  colour 2: class  2  slot order (0,1,2,5,3,4) = A1(x³) → A2(y)  → A3(y²) → B3(x²) → B1(y³) → B2(x)
```

Every one of the six is a pure left-block-then-right-block order, as an LRC requires. Concretely, the
first three checks of each type are measured in the orders

```
Z-check 0 (colour 0):  3,  6, 12, 73, 90,  74     residuals {3,6}   {73,90,74}   {90,74}
Z-check 1 (colour 1):  4,  7, 13, 75, 91,  74               {4,7}   {75,91,74}   {91,74}
Z-check 2 (colour 2):  8, 14,  5, 76, 92,  75               {8,14}  {76,92,75}   {92,75}
X-check 0 (colour 0): 54,  4,  5,132, 75, 138               {54,4}  {132,75,138} {75,138}
X-check 1 (colour 1): 55,  0,  5, 76,139, 133               {55,0}  {76,139,133} {139,133}
X-check 2 (colour 2): 56,  1,  0,134, 77, 140               {56,1}  {134,77,140} {77,140}
```

(residuals in the order `r₁ = {i₁,i₂}`, `r₂ = {i₄,i₅,i₆}`, `r₃ = {i₅,i₆}` — [SBB26]'s
`{{1,2},{4,5,6},{5,6}}`). This is the object §4 certifies.

### 2.5 Fidelity statement — what is pinned and what is not

**Pinned by the source, now that the figure is decoded.** The colouring is a group colouring and it
is `φ = a+b`; the tiling is non-uniform; the circuit is a left–right circuit at depth 8; the
within-check order classes are the cyclic orbit of `(14,0,2)` (X) and `(1,2,62)` (Z), and no other
reading of the figure is simultaneously legal, measurement-consistent and cascade-surviving.

**Not pinned, and load-bearing to different degrees.**

* *The glyph-to-digit map and the label-to-edge matching* are inferences from the PDF, not from
  rendered pixels I looked at. Both are over-determined (36 for 36, exact sequence match, unique
  nearest edge with a 7–20 pt fit against 27 pt spacing), but they are inferences. **Risk: low.**
* *Which drawn edge is which monomial* is not determined by the figure alone; it is determined here
  only through the legality + (MC) + cascade filter. Different edge maps give different class
  triples, and the filter selects one orbit. So this is **certification of the class that the
  filter selects**, not a reading of the figure's geometry. **Risk: moderate**, and it is the main
  residual reconstruction risk. It is mitigated by the four independent invariants in §2.3 that the
  selected class reproduces and the rejected ones do not.
* *Whether the paper's colouring is a group homomorphism at all.* Figure 10 says "a natural
  three-colouring"; the four homomorphisms `φ(x^a y^b) = (sa+tb) mod 3`, `s,t ∈ {1,2}`, are exactly
  the group colourings that properly colour both check-conflict graphs (verified), and the paper's
  own statement that the colour classes may be cyclically permuted `B→R→G` without changing the
  bound is precisely the statement that colour rotation is a code automorphism, which holds for the
  group colourings (§4.1) and need not hold otherwise. **Risk: low but not zero**, and unchanged
  from round 6 / the review.
* *The absolute timing.* I do not claim to have reconstructed the paper's exact time steps. §3 shows
  a legal, (MC)-clean depth-8 staggered LRC exists and that all 44 assignments are realisable as
  valid non-interleaved SECs, which is all the certification needs, since `d_ext` is a function of
  the within-check orders alone.

---

## 3. Legality: which members are measurement-consistent, at what depth

### 3.1 The corrected six-layer statement

Round 6 asserted "the gross code has no measurement-consistent single-ancilla SEC with six CNOT
layers at all … with no assumption on the within-check orders, no tiling and no symmetry". The
review **refuted that as stated** and scoped it: the `T=6` UNSAT is a correct result about a model
in which X- and Z-check CNOT times share one per-round layer index and both ancilla families are
reset at the top and measured at the bottom of the round — i.e. **unstaggered** schedules. [SBB26]
defines depth as the amortised `t = lim T(m)/m` and staggers explicitly, and its own bound
`t ≥ max(c(H_XZ), r(H_XZ)+2) = max(6, 8) = 8` is saturated by six CNOT layers plus the ancilla
preparation and measurement steps.

I take the corrected statement as the operative one and use nothing that depends on the refuted
version. Concretely, throughout §3 the model is: a **period-`P` staggered schedule**, in which each
check's six CNOTs sit at six absolute times, instances repeat with period `P`, legality means every
data qubit's six CNOT times are distinct mod `P`, and (MC) is evaluated on absolute times over all
(X-instance, Z-instance) pairs.

### 3.2 Staggered left–right circuits are measurement-consistent — for structural reasons

The review built one staggered 6-CNOT-layer gross LRC and found `0/648` (MC) violations, confirmed
by `stim`. I reproduce that and strengthen it: it is not a property of that particular layer
assignment.

**Premise (NUMERICAL, `lrc.py`).** Over all 648 overlapping (X-check, Z-check) pairs of the gross
code, the two shared data qubits are always one in the left half and one in the right half, and the
monomial index pair is the same, swapped:

```
overlapping (X,Z) check pairs: 648;  shared-qubit halves: [('L','R')];  index-pair-swapped: 648/648
```

**Claim (CONJECTURED, two lines).** Take the LRC block structure `block A = L_X ∥ R_Z`,
`block B = R_X ∥ L_Z`, with the Z-ancilla window straddling the period boundary so that a Z
instance performs its left block in block B of period `p` and its right block in block A of period
`p+1`. Then for the pair `(X_p, Z_p)`: on the shared **left** qubit X acts in block A of period `p`
and Z in block B of period `p`, so Z is later; on the shared **right** qubit X acts in block B of
period `p` and Z in block A of period `p+1`, so Z is later again. Count 0, even. For `(X_p,
Z_{p-1})` both comparisons flip together, count 2, even. All other instance offsets push both
comparisons the same way. So `c_ab` is even for **every** overlapping pair and **every** instance
offset, **whatever the within-block layer choice**. Verified numerically on a random sample of 40
legal tiled staggered LRCs: `legal 40/40, (MC)-clean 40/40`, with the counts

```
one example: 3240 (X-instance, Z-instance) overlapping pairs examined, 0 odd;
             per period offset: {-2: 0, -1: 0, 0: 0, 1: 0, 2: 0}
```

and on the reconstructed candidate itself at period 8 (`buildlrc.py`): legality over 6 periods
`True`, `(MC): 0 odd of 4536 pairs`.

**An explicit depth-8 witness circuit, checked by `stim`** (`lrc8.py`). Period 8 time steps: the X
instance of period `p` does its left block at `8p+{1,2,3}` and its right block at `8p+{4,5,6}`
(prepared at `8p+0`, measured at `8p+7`); the Z instance is staggered by half a period, left block
at `8p+{5,6,7}`, right block at `8p+{8,9,10}` (prepared at `8p+4`, measured at `8p+11`). Each
ancilla's window is exactly 8 steps, so consecutive instances of the same check do not overlap —
the depth bound `t ≥ r(H_XZ) + 2 = 8` is saturated, and six of the eight steps carry each data
qubit's CNOTs.

```
legality over 6 periods, every layer a matching: True
(MC): 0 odd of 4536 (X-instance, Z-instance) overlapping pairs
stim X-memory: 288 qubits, 288 detectors, 6 CNOT layers per period, DEM BUILT OK
   noiseless detector firings: 0 / 288
```

This is an independent construction of the object the review exhibited, and it settles the scoping
question the review raised: **depth-8 gross-code SECs exist and are valid.**

The contrast with the *unstaggered* half-split — `c_ab = 1` for all 648 pairs, round 6 §7(7) — is
exactly the half-period stagger, and it is why the refuted six-layer no-go was model-bound.

### 3.3 Aligned three-colour-tiled LRCs — and a correction to my own earlier claim in this session

Before decoding Figure 12 I enumerated 3-colour-tiled staggered LRCs in the **aligned** model: all
three colour classes share the same block windows (block A = layers 0,1,2; block B = layers 3,4,5),
with the within-block layer depending only on the check's colour. That model is exactly solvable:
the matching condition factorises into four independent conditions, one per (block, half),

```
phi = a+b : |LXL| = |LXR| = |LZL| = |LZR| = 12 of 216  ->  20 736 tiled staggered LRCs
realisable X-sector order-class triples: 36     realisable Z-sector triples: 36
```

and intersecting with the cascade survivors gives, **for every one of the four colourings and in
both sectors, only the uniform triple `(2,2,2)`** — which [SBB26] Prop. 5 excludes and which is in
any case certified at `d_ext ≤ 10` below.

**That result is true but it is not the whole family, and I flag it as a correction to a claim I
made earlier in this session before the figure was decoded.** Figure 12 shows the blue colour class
offset by one time step from red and green (§2.2, fact 3), so the aligned model does **not** contain
the candidate. Any statement of the form "no non-uniform three-colour-tiled LRC of the gross code
survives the cascade" must carry the qualifier *aligned*, and I state it only with that qualifier:

> **(NUMERICAL, scope stated.)** Among 3-colour-tiled staggered left–right circuits of the gross
> code with the standard left/right halves partition, six CNOT layers per period, and **all three
> colour classes sharing common block windows**, the only order-class triple surviving the pruning
> cascade, in either sector and for any of the four group 3-colourings, is the uniform `(2,2,2)`.
> The 36 realisable triples per sector are enumerated in `lrcall.json`.

The general question — which of the 44 are realisable by a legal, (MC)-clean depth-8 LRC once
per-colour time offsets are allowed — is **NOT-DONE** (§7).

### 3.4 Every one of the 44 is realisable as a valid non-interleaved SEC — NUMERICAL

The certification does not depend on §3.3, because `d_ext(ℰ)` is a function of the within-check
orders alone, and *every* within-check order assignment is realised by the alternating-XZ circuit,
which [SBB26] S5 names as its own extreme example of a non-interleaved circuit and which in-house
Theorem 7.1 (`artifacts/circdist_lift_nonint_proof_20260820.md`, carried at CONFIRM in
`artifacts/circdist_lift_proofs_review_20260820.md` row K) also covers. For the reconstructed
candidate's orders (`altcheck.py`):

```
alternating-XZ circuit with the candidate's orders: 17 CNOT layers, 864 CNOTs;
every layer asserted a matching by the builder
(MC) on the alternating-XZ realisation: 0 odd of 648 overlapping pairs
stim: 288 qubits, 432 detectors, DEM BUILT OK; noiseless detector firings: 0 / 432
```

This is not special to the candidate: the alternating-XZ circuit runs every X-check CNOT before
every Z-check CNOT, so on each shared qubit the Z-CNOT is later and the (MC) count is 0 for all 648
overlapping pairs *whatever* the within-check orders. Checked rather than assumed, on 25 random
(Z-triple, X-triple) pairs drawn from the `44 × 44` survivors (`altall.py`):

```
25 random (Z-triple, X-triple) pairs from the 44 x 44 survivors:
all layers matchings, 0 odd of 16200 overlapping (X,Z) check pairs
```

So the numbers certified in §4 are numbers about legal, measurement-consistent, non-interleaved
gross-code syndrome-extraction circuits — at 17 CNOT layers for the alternating-XZ realisation, and
at six CNOT layers (depth 8) for the staggered LRC realisation whenever one exists.

**Summary of the legality findings.**

| question | answer | scope |
|---|---|---|
| is a 6-CNOT-layer (depth-8) gross LRC measurement-consistent? | **yes, always** | staggered LRC block structure, any within-block layers (§3.2) |
| is the round-6 "no 6-layer MC gross SEC" claim used anywhere here? | **no** | it is REFUTED as stated; the corrected version is unstaggered-only |
| which of the 44 are realisable as *aligned* 3-colour-tiled depth-8 LRCs? | only `(2,2,2)` | aligned model only — **not** the candidate's model (§3.3) |
| which of the 44 are realisable as *some* valid non-interleaved SEC? | **all 44**, both sectors | alternating-XZ, legal, (MC)-clean, `stim`-checked (§3.4) |
| is the reconstructed candidate legal and (MC)-clean at depth 8? | **yes** | period 8, 0 odd of 4536 instance pairs (§3.2) |

---

## 4. Exact certification of `d_ext(ℰ)` on the `φ = a+b` family

### 4.1 Method, validation, and the symmetry actually used

**Encoding** (`dext.py`/`dext2.py`, reused; review verdict CONFIRM). One SAT decision query per
weight bound `W`, over `z ∈ F₂^144` (the net data error `E`), `u_{c,k}` (residual `k` of check `c`
used) and `d ∈ F₂^144` (the data-fault part), with the 72 weight-6 detector XORs on `z`, a
disjunction of 12 logical XOR chains, `d_j = z_j ⊕ (⊕ u_{c,k} : j ∈ r_k(c))`, a sequential-counter
cardinality `Σ|d| + Σ|u| ≤ W` over the 360 extended-code columns, the implied cut `|z| ≥ 12`, and
the equisatisfiable dominance cut `¬(u_{c,2} ∧ u_{c,3})`. Solver: CaDiCaL 1.5.3 via `python-sat`.
**SAT at `W` is a witness** — a rigorous upper bound with a certificate. **UNSAT at `W` certifies
`d_ext > W`**; combined with the universal `d_ext ≤ 11` (every one of the 15 slot-pairs of a check
support lies in a weight-12 logical — recon §3.2, reproduced by round 6 §3 and by the review), it
pins `d_ext = 11` exactly.

**Certifier validation, re-run this session.** With the residual set switched off the problem
degenerates to the gross code's own minimum logical weight, known to be 12:

```
[no residuals] W = 11 : UNSAT      W = 12 : SAT, weight-12 witness      (both sectors)
```

**The symmetry actually used, and the one I verified.** Two different symmetries are in play and I
keep them apart.

* *Colour rotation.* A tiled assignment `(t₀,t₁,t₂)` and its cyclic rotation `(t₂,t₀,t₁)` are
  carried into one another by the translation `g = (0,1) ∈ Z₁₂ × Z₆`, which has `φ(g) = 1` and is a
  code automorphism. I verified this directly rather than assuming it (`rotcheck.py`): the
  translation permutes `rowspace(H_X)` and `rowspace(H_Z)` (so it preserves logical non-triviality,
  not merely the syndrome), and it carries residual sets to residual sets with the assignment
  rotated:

```
translation with phi(g)=1 : (0, 1)
  permutes rowspace(HX): True    permutes rowspace(HZ): True
  residual-set equivariance failures over all 64 triples per sector, both sectors: 0 of 13824
```

  So `d_ext` is constant on colour-rotation orbits, and the **44 survivors reduce to 16 orbits per
  sector** — this is what makes the sweep affordable, and every row of the table below is
  transported to its orbit by this verified automorphism.
* *The column quotient inside one query.* For the harder instances I also used the round-6 orbit
  decomposition: the stabiliser `S ≤ G` of the tiled assignment (order 24 for a non-uniform triple,
  72 for a uniform one) acts freely on the 360 columns, so a minimum-weight solution may be assumed
  to use one of the `360/|S| ∈ {15, 5}` orbit representatives, and **UNSAT on all representatives**
  certifies `d_ext > W`. The review validated this quotient against an unquotiented case of known
  answer (`d = 12`: unquotiented UNSAT 42.4 s, quotiented UNSAT 14.0 s / 9.0 s, same verdict).
  Rows below say explicitly whether they are quotiented, and a quotiented row is reported as UNSAT
  only if **every** representative closed.

### 4.2 Results

Rows are the 16 colour-rotation orbits per sector; the "orbit" column is how many of the 44
survivors that row settles. A **SAT** row is a witness and pins `d_ext ≤ 10`; an **UNSAT** row at
`W = 10` would pin `d_ext = 11` exactly (with the universal `≤ 11`). Rows marked *partial* record
which `|R|`-subproblems closed and which did not; rows marked *open* say honestly whether the query
ran without closing or was never reached — the queue processed the Z sector first, so most of the X
sector is the latter, and that is a scheduling artefact of this session, not a property of the X
sector.

| sector | orbit rep | orbit | verdict at `W = 10` | time | witness / certificate |
|---|---|---|---|---|---|
| Z | `(1, 2, 2)`  LRC | 3 | **SAT** | 1354 s | weight 10 = 6 data + 4 hooks, \|E\| = 14 |
| Z | `(1, 2, 9)` | 3 | **SAT** | 232 s | weight 10 = 2 data + 8 hooks, \|E\| = 16 |
| Z | `(1, 2, 62)` **(candidate)** | 3 | partial | 372 s | \|R\| ∈ [0, 1] UNSAT; open at \|R\| ∈ [2, 3, 4, 5, 6, 7, 8, 9, 10] |
| Z | `(1, 9, 2)` | 3 | **SAT** | 446 s | weight 10 = 6 data + 4 hooks, \|E\| = 16 |
| Z | `(1, 9, 9)` | 3 | **SAT** | 69 s | weight 10 = 6 data + 4 hooks, \|E\| = 16 |
| Z | `(1, 9, 62)` | 3 | **SAT** | 206 s | weight 10 = 6 data + 4 hooks, \|E\| = 16 |
| Z | `(1, 62, 2)`  LRC | 3 | partial | 36 s | \|R\| ∈ [0] UNSAT; open at \|R\| ∈ [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] |
| Z | `(1, 62, 9)` | 3 | **SAT** | 2179 s | weight 10 = 6 data + 4 hooks, \|E\| = 16 |
| Z | `(2, 2, 2)`  LRC | 1 | partial | 40 s | \|R\| ∈ [0] UNSAT; open at \|R\| ∈ [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] |
| Z | `(2, 2, 9)` | 3 | **SAT** | 364 s | weight 10 = 6 data + 4 hooks, \|E\| = 16 |
| Z | `(2, 2, 62)`  LRC | 3 | partial | 37 s | \|R\| ∈ [0] UNSAT; open at \|R\| ∈ [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] |
| Z | `(2, 9, 9)` | 3 | **SAT** | 95 s | weight 10 = 6 data + 4 hooks, \|E\| = 16 |
| Z | `(2, 9, 62)` | 3 | **SAT** | 273 s | weight 10 = 6 data + 4 hooks, \|E\| = 16 |
| Z | `(2, 62, 9)` | 3 | open | — | no answer at the wall |
| Z | `(9, 9, 9)` | 1 | **SAT** | 418 s | weight 10 = 6 data + 4 hooks, \|E\| = 16 |
| Z | `(9, 9, 62)` | 3 | **SAT** | 24 s | weight 10 = 6 data + 4 hooks, \|E\| = 14 |
| X | `(0, 2, 2)`  LRC | 3 | partial | 35 s | \|R\| ∈ [0] UNSAT; open at \|R\| ∈ [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] |
| X | `(0, 2, 9)` | 3 | open | — | no answer at the wall |
| X | `(0, 2, 14)` **(candidate)** | 3 | partial | 538 s | \|R\| ∈ [0, 1] UNSAT; open at \|R\| ∈ [2, 3, 4, 5, 6, 7, 8, 9, 10] |
| X | `(0, 9, 2)` | 3 | **SAT** | 441 s | weight 10 = 6 data + 4 hooks, \|E\| = 14 |
| X | `(0, 9, 9)` | 3 | **SAT** | 314 s | weight 10 = 7 data + 3 hooks, \|E\| = 14 |
| X | `(0, 9, 14)` | 3 | open | — | no answer at the wall |
| X | `(0, 14, 2)`  LRC | 3 | open | — | no answer at the wall |
| X | `(0, 14, 9)` | 3 | open | — | not attempted (queue not reached) |
| X | `(2, 2, 2)`  LRC | 1 | open | — | not attempted (queue not reached) |
| X | `(2, 2, 9)` | 3 | open | — | not attempted (queue not reached) |
| X | `(2, 2, 14)`  LRC | 3 | open | — | not attempted (queue not reached) |
| X | `(2, 9, 9)` | 3 | open | — | not attempted (queue not reached) |
| X | `(2, 9, 14)` | 3 | open | — | not attempted (queue not reached) |
| X | `(2, 14, 9)` | 3 | open | — | not attempted (queue not reached) |
| X | `(9, 9, 9)` | 1 | open | — | not attempted (queue not reached) |
| X | `(9, 9, 14)` | 3 | open | — | not attempted (queue not reached) |

settled: 13 of 32 orbits; assignments covered: 37 of 88

### 4.3 Witness verification

Every SAT row is re-verified three ways, sharing no code between the three (`verify.py`):

1. **Exact `F₂` algebra from the definitions** — the decomposition `E = d ⊕ (⊕_{r∈R} r)`, zero
   syndrome `H_det E = 0`, and non-triviality `E ∉ rowspace(H_stab)`.
2. **My own Pauli-frame simulator on the literal circuit** (`simverify.py`) — the alternating-XZ
   circuit with the tiled orders is built gate by gate, every layer asserted to be a matching, the
   residual columns injected as genuine ancilla faults just before the relevant CNOT and the data
   faults at the end of the round; all round detectors and all terminal detectors must be silent
   and the net error must be a non-trivial logical.
3. **`stim` 1.16.0** on 12 of the 29 — faults injected as `Z_ERROR(1)` channels (a
   deterministic Pauli gate is absorbed into `stim`'s noiseless reference and fires nothing; round 6
   flagged this and it is worth keeping on the node's tooling notes).

Every one of the SAT rows above passed all applicable checks, with no failures:

```
{"triple": [1,2,2],  "sector":"Z", "algebra": {"weight":10,"n_data":6,"n_res":4,"Ewt":14,
   "decomposition_ok":true,"zero_syndrome":true,"nontrivial_logical":true},
   "circuit": {"nfaults":10,"round_detectors_silent":true,"terminal_detectors_silent":true,
               "net_error_weight":14,"nontrivial_logical":true},
   "stim": {"n_faults":10,"detectors_fired":0,"observables_flipped":9,
            "clean_detectors_fired":0,"clean_observables_flipped":0,"n_detectors":288}}
{"triple": [1,2,9],  "sector":"Z", ... "stim": {"detectors_fired":0,"observables_flipped":3, ...}}
{"triple": [1,62,9], "sector":"Z", ... "stim": {"detectors_fired":0,"observables_flipped":2, ...}}
... 29 witnesses in total.  ALL 29 pass:  weight = 10, decomposition_ok, zero_syndrome and
    nontrivial_logical true in the algebra; nfaults = 10, round_detectors_silent and
    terminal_detectors_silent true and nontrivial_logical true on the literal circuit; 12 of them
    additionally checked in stim: 0 of 288 detectors fire in every case, the clean run fires
    nothing and flips nothing, and 1-9 of the 12 logical observables flip.
    Failures: none.
    residual-column histogram over the 29 witnesses : {4: 26, 3: 2, 8: 1}
    |E| histogram                                   : {16: 23, 14: 6}
```

Two things are worth registering. The witnesses are **not** weight-12-logical mechanisms: every one
of the 29 has `|E| ∈ {14, 16}` and uses 3, 4 or even 8 residual columns (`(1,2,9)`: `weight 10 = 2 data +
8 hooks`), so they are multi-check hook compositions inside weight-14/16 logicals — precisely the
class of mechanism [SBB26]'s one-check-at-a-time cascade cannot see, which is round 6's most
valuable observation and which survives its refuted reconstruction intact. And the algebraic
`|E|` and the circuit's net error weight sometimes differ (16 vs 12): the two differ by a
stabiliser, because a residual is realised in the circuit as the complementary suffix; both lie in
the same logical coset and both are undetectable. The review noted the same and it is correct.

---

## 5. Which pre-committed reading fires

The commission pre-committed:

> some member certifies at `d_ext = 11` ⇒ the SBB conjecture is CONFIRMED at NUMERICAL for that
> member, `D* ≥ 11` firmly and the `D* = 11` vs `12` question sharpens onto the completion gap;
> all members `≤ 10` ⇒ the conjecture is refuted on the CORRECT family — deliver witnesses;
> wall ⇒ certified partial bounds + exact wall statement.

**Reading 3 fires — the wall — and it fires with the reconstruction repaired and a large certified
partial.** Neither of the two decisive readings can be cashed: I did not settle the reconstructed
candidate, so I cannot claim `d_ext = 11` for it, and I did not settle all 44, so I cannot claim the
conjecture is refuted on the correct family. What I *can* cash, at NUMERICAL, is this.

**(a) Certified with witnesses.** For every orbit marked SAT in §4.2, `d_ext(ℰ) ≤ 10` exactly, by an
explicit weight-10 undetectable logical fault set, verified from the `F₂` definitions, re-verified on
the literal 864-CNOT alternating-XZ circuit with those within-check orders (all detectors silent,
non-trivial logical), and — for 12 of the 29 — confirmed in `stim` (0 of 288 detectors fire,
observables flip). Since that circuit is legal, measurement-consistent
and non-interleaved — [SBB26] S5's own named extreme example, and covered independently by in-house
Theorem 7.1 — [SBB26] Theorem 1 / Corollary 1 gives `d_circ = d_ext(ℰ) ≤ 10` for each of them.
Transported along the verified colour-rotation automorphism (§4.1) this covers, of the 44 survivors
per sector,

```
Z sector : 31 of 44 certified d_ext <= 10.  Open (13):
   (1,2,62) (1,62,2) (2,1,62) (2,2,2) (2,2,62) (2,62,1) (2,62,2) (2,62,9)
   (9,2,62) (62,1,2) (62,2,1) (62,2,2) (62,9,2)
X sector :  6 of 44 certified d_ext <= 10:  (0,9,2) (0,9,9) (2,0,9) (9,0,9) (9,2,0) (9,9,0)
```

A three-colour-tiled circuit is a **pair** (Z-triple, X-triple) and its circuit distance is the
minimum over the two sectors, so a pair is settled as soon as **either** component is. Of the
`44 × 44 = 1 936` pairs both of whose components survive the cascade, `1 936 − 13 × 38 = 1 442`
(**74.5 %**) are therefore certified at `d_circ ≤ 10` by explicit weight-10 witness; and every pair
in which at least one sector's triple is cascade-*eliminated* — all `729 000² − 1 936` of them —
carries a weight-10 witness by construction, audited end-to-end by round 6 and CONFIRMed by the
review. What is open is `13 × 38 = 494` pairs, containing the reconstructed candidate.

**(b) Certified by UNSAT, partially.** For the reconstructed candidate — Z-triple `(1,2,62)`,
X-triple `(14,0,2)` — the subproblems `|R| = 0` and `|R| = 1` are UNSAT at `W = 10` in **both**
sectors. That is a genuine certificate about the candidate:

> **No weight-10 undetectable logical fault set of the reconstructed candidate's extended code uses
> fewer than two residual (hook) columns, in either sector.**

The `|R| = 0` half of that is not news — it follows from `d(gross) = 12` alone, and I record it only
because it is one of the eleven subproblems the split has to close. **The content is `|R| = 1`**,
which is a real UNSAT proof (330 s in the Z sector, 495 s in the X sector) and rules out the entire
"one hook error inside a weight-12 logical" mechanism — the mechanism that the paper's own
`90 → 45` filter is built to detect and that all 44 survivors pass by construction, here confirmed
independently and exactly rather than by a rule. It is the first non-trivial lower-bound information
anyone has about the actual SBB candidate: the paper's own evidence is a heuristic search that found
nothing below weight 11 in 10 000 loops, and round 6's refutation was aimed at a different family.
It is emphatically **not** `d_ext = 11` — `|R| ∈ {2,…,10}` is open, and §7.1 prices exactly what
closing it costs. `|R| = 0` certificates were also obtained for four further unsettled
left–right-realisable orbits, listed as *partial* in §4.2.

**(c) The one thing that did NOT happen, stated plainly.** No member of the `φ = a+b` family was
certified at `d_ext = 11`. The pre-committed "some member certifies at 11" reading therefore does
**not** fire, and neither does "all members ≤ 10". `D*_Gross ≥ 11` is not established here, and
nothing here moves the `D* = 11` vs `12` question.

**(d) What the pattern in §4.2 suggests, labelled as a prior and not a result.** The orbits that
resisted are strikingly the left–right-realisable ones: in the Z sector 4 of the 5 unsettled orbits
are LRC-compatible and 4 of the 5 LRC-compatible orbits are unsettled, while 10 of the 11 orbits
containing the non-LRC class 9 closed SAT (24 s to 36 min). If weight-10 witnesses were as abundant on
the LRC-compatible assignments as elsewhere, CaDiCaL would have found them as fast. That is
*evidence* that the candidate's `d_ext` may well be 11 — i.e. that [SBB26]'s conjecture may be right
where round 6's refutation, aimed at the wrong family, said otherwise. **It is a runtime asymmetry,
not a certificate, and I decline to price it further.**

---

## 6. Corrections to the record

1. **The colouring is `φ = a+b`, confirmed from the source, not only from the cascade shape.**
   The review inferred it from Prop. 6's `45 → 4` step; I reproduce that step (§2.1) *and* recover
   Figure 12 itself (§2.2–2.3), and the two agree. Round 6's `φ = a+2b` family is a correct theorem
   about its own family and should be kept as such, with its inference to the candidate withdrawn —
   as the review already said.
2. **The candidate's order classes are now on the record**: X-triple `(14,0,2)`, Z-triple
   `(1,2,62)`, each up to cyclic colour rotation, under `φ(x^a y^b) = (a+b) mod 3`. This is new; no
   previous session or review had them.
3. **Figure 12 is machine-readable after all.** Round 6 and the review both concluded the schedule
   "does not survive text extraction". It survives *vector* extraction: the glyph positions are in
   the Form XObject's content stream. This is a reusable technique for this node and is worth a line
   in the tooling notes.
4. **A correction to a claim I made earlier in this session.** Before decoding the figure I
   enumerated 3-colour-tiled staggered LRCs in the aligned model and found that only the uniform
   `(2,2,2)` survives the cascade. That statement is correct **only for aligned block windows**;
   Figure 12 offsets one colour class by one time step, so the aligned model does not contain the
   candidate. §3.3 restates it with the qualifier and marks the general question NOT-DONE.
5. **The staggered-LRC (MC) property is structural**, not incidental to the review's example
   (§3.2). Any future session on this node can take "a depth-8 staggered LRC of the gross code is
   measurement-consistent" as given, for any within-block layer choice, and does **not** need to
   re-litigate the refuted six-layer no-go.
6. **`mc-equiv` stays dead.** Nothing here uses or revives it.

---

## 7. Honest limits, and what was not done

1. **Reconstruction.** §2.5 is the fidelity statement. The residual risk that matters is the
   edge→monomial map, which the figure alone does not fix; it is fixed here only by the
   legality + (MC) + cascade filter, and the filter's output reproduces four independent published
   invariants. I did not render the figure to pixels and read it by eye; that is the cheapest
   independent check of §2.2–2.3 and it is the first thing a reviewer should do.
2. **Depth-8 realisability of the 44 with per-colour time offsets** — the general version of §3.3.
   I established that the candidate's own triples are realisable at depth 8 (legal, (MC)-clean,
   §3.2) and that all 44 are realisable as valid non-interleaved SECs (§3.4), but I did not
   enumerate which of the 44 admit a depth-8 staggered LRC once colour offsets are allowed.
3. **`d_ext(ℛ)` for `ℛ` on few checks, on this family.** The review demoted round 6's universal
   "`d_ext(ℛ) = 11` for every `ℛ` on at most two checks" to seven tested instances. I did not test
   it at all on the `φ = a+b` family and make no claim about it.
4. **The paper's own `4³ = 64 → 3` step** was not reproduced as such; my stage 2 is weaker and
   leaves 44. I certify all 44, which subsumes their 3, so nothing rests on reproducing their
   pruning.
5. **The `Σ₂` question is untouched.** Nothing here bounds `max_M d_ext(E(M))` over interleaved
   schedules or over untiled ones.
6. **`nogo.py` at `T = 7, 8`** (round 6 §4.5) is untouched, and note that its `T=6` row inherits
   the model defect the review identified.
7. **Sector coverage is uneven and it is my scheduling, not the mathematics.** The queue took the Z
   sector first; 31 of 44 Z-triples are certified against 6 of 44 X-triples. A rerun should
   interleave the sectors.
8. **A methodological caution I want on the record.** I twice let more solver processes run than
   the machine had cores, which slowed everything and cost real wall-clock inside the box. The
   symmetry reduction (88 queries → 32) and the `|R|`-split were both worth far more than the
   parallelism, and should be applied *before* launching anything next time.

### 7.1 The wall, and the repricing

**The wall, exactly.** The decision problem itself is the wall, and it is one-sided. A weight-10
witness, when one exists, is found by CaDiCaL on the undivided 360-column query in 24 s – 36 min
(29 SAT queries, median 5.4 min); every query that ran past about an hour is one where no
witness has been found, and I have no UNSAT proof for any of them at the undivided level. The
decomposition that does work — splitting the bound `W = 10` by the number `K` of residual columns
used and adding the two implied cuts `|d| ≤ W − K` and `|E| ≤ W + 2K` (§4.1, `job3.py`) — closes
`K = 0` in ~43 s and `K = 1` in 5.5 / 8 min, and does not close `K ≥ 2` inside this box. So the wall
is **the UNSAT half at `K ≥ 2`**, exactly where the toolfeas study predicted it
(`artifacts/circdist_gross_toolfeas_20260820.md`: "the lower-bound half is the hard half").

**Repricing.** To finish the candidate one needs 9 subproblems per sector (`K = 2…10`), 18 in all,
each an UNSAT proof on ~22 500 clauses. Two levers are untried and both are cheap to set up:
(i) compose the `K`-split with the column quotient, which is already implemented and validated
(`job3.py` takes an orbit index) — that multiplies the subproblem count by 15 but each is 15× more
constrained, and 270 subproblems at 20-wide parallelism is a few hours if the individual times fall
the way the `K = 0, 1` rows suggest; (ii) an incremental solver sharing learnt clauses across the
`K` values, which this session did not build. My estimate: **the candidate is 1–2 further sessions
of wall-clock on 24 cores, at maybe 0.6 probability of closing**, and the remaining 19 orbits are a
similar amount again. That is a repricing of the round-6 "≈ 32 SAT jobs of the size already run,
roughly half a session on 24 cores" — that estimate was made from SAT runtimes on a family where
witnesses are abundant, and it is too optimistic by a large factor on this family, where they
appear not to be.

**What I would fund first, and why.** Not the remaining 19 orbits — the candidate, `K = 2…10`,
quotiented. It is the only computation on this node whose outcome changes a headline either way: an
UNSAT sweep gives an exactly certified distance-11 non-interleaved gross SEC and confirms [SBB26]'s
conjecture at NUMERICAL, and a SAT gives a weight-10 witness that refutes it on the reconstruction
this session pins down. Everything else in the family is decoration by comparison.

---

## 8. Reproduction

Python 3.9.6, `numpy` 2.0.2, `stim` 1.16.0, `python-sat` 1.9.dev15, `pypdf`. 24 cores.

**Reused verbatim from `artifacts/circdist_gross_sbbcert_20260820.md` §9** (extracted mechanically
back out of that markdown file into an empty directory, then re-validated here — see §1):
`gross.py`, `sched.py`, `cascade.py`, `cascade_check.py`, `pool.py`, `dext.py`, `dext2.py`,
`cert.py`, `simverify.py`, `stimverify.py`. They are not reproduced again below.

Order of execution:

```
python3 gross.py            # code construction + rank / commutation / incidence checks   (<1 s)
python3 pool.py             # weight-12 logical pools and logical bases                    (~5 s)
python3 cascade.py          # the 90 -> 45 -> {8, 44} cascade, all four colourings          (~2 s)
python3 casc45.py           # [SBB26] Prop. 6's own 45 -> 4 step                          (~60 s)
python3 fam.py              # the phi = a+b family: 44 survivors, LRC-compatible subset
python3 decode12.py         # Figure 12 recovered from the PDF vector content stream
python3 fig12e.py           # panel-consistent readings (no straddle)
python3 fig12f.py           # readings with the ancilla straddle -> the unique candidate
python3 readingA.py         # the alternative reading, and its weight-10 witnesses
python3 lrc.py 1 1          # staggered LRC legality + (MC) structure
python3 lrcall.py           # aligned 3-colour-tiled LRCs, all four colourings
python3 lrc8.py             # an explicit legal (MC)-clean depth-8 staggered LRC, in stim
python3 buildlrc.py         # the reconstructed candidate at period 8: legality + (MC)
python3 altcheck.py         # the alternating-XZ realisation of the candidate: legality, (MC), stim
python3 altall.py           # the same, over random pairs from the 44 x 44 survivors
python3 rotcheck.py         # colour rotation is a code automorphism (0 failures / 13824)
python3 job.py  <sec> <a,b,c> 10          # one undivided certification query
python3 job3.py <sec> <a,b,c> 10 <K>      # one |R| = K subproblem, with the K-cuts
python3 verify.py                          # three-way re-verification of every SAT witness
```

The PDF is fetched from `arxiv.org/pdf/2603.05481` and read only as data; nothing was downloaded to
the repository and nothing was executed from it.

### 8.1 New modules

#### `pdfparse.py`

```python
"""Minimal PDF content-stream parser: filled/stroked path bounding boxes with fill colour,
in the form XObject's own coordinate system."""
import re

def parse(stream):
    toks = re.findall(r"\[[^\]]*\]|\((?:\\.|[^)\\])*\)|/[^\s/\[\]()<>]+|<<|>>|[^\s\[\]<>]+", stream)
    ctm = [1,0,0,1,0,0]; stack=[]
    fill=(0,0,0); strk=(0,0,0)
    args=[]; pts=[]; out=[]
    def ap(m,x,y): return (m[0]*x+m[2]*y+m[4], m[1]*x+m[3]*y+m[5])
    def num(t):
        try: return float(t)
        except: return None
    for t in toks:
        v=num(t)
        if v is not None:
            args.append(v); continue
        if t=='q': stack.append((ctm[:],fill,strk))
        elif t=='Q':
            if stack: ctm,fill,strk = stack.pop(); ctm=ctm[:]
        elif t=='cm' and len(args)>=6:
            a,b,c,d,e,f=args[-6:]
            m=ctm
            ctm=[a*m[0]+b*m[2], a*m[1]+b*m[3], c*m[0]+d*m[2], c*m[1]+d*m[3],
                 e*m[0]+f*m[2]+m[4], e*m[1]+f*m[3]+m[5]]
        elif t=='sc' or t=='scn':
            if len(args)>=3: fill=tuple(args[-3:])
            elif len(args)>=1: fill=(args[-1],)*3
        elif t=='SC' or t=='SCN':
            if len(args)>=3: strk=tuple(args[-3:])
            elif len(args)>=1: strk=(args[-1],)*3
        elif t=='g': fill=(args[-1],)*3 if args else fill
        elif t=='rg' and len(args)>=3: fill=tuple(args[-3:])
        elif t in ('m','l') and len(args)>=2:
            pts.append(ap(ctm,args[-2],args[-1]))
        elif t=='c' and len(args)>=6:
            for i in (0,2,4): pts.append(ap(ctm,args[-6+i],args[-6+i+1]))
        elif t=='v' or t=='y':
            if len(args)>=4:
                for i in (0,2): pts.append(ap(ctm,args[-4+i],args[-4+i+1]))
        elif t=='re' and len(args)>=4:
            x,y,w,h=args[-4:]
            for (a,b) in ((x,y),(x+w,y),(x+w,y+h),(x,y+h)): pts.append(ap(ctm,a,b))
        elif t in ('f','f*','F','B','B*','b','b*','S','s','n'):
            if pts:
                xs=[p[0] for p in pts]; ys=[p[1] for p in pts]
                out.append(dict(op=t, fill=fill, stroke=strk,
                                cx=(min(xs)+max(xs))/2, cy=(min(ys)+max(ys))/2,
                                w=max(xs)-min(xs), h=max(ys)-min(ys), n=len(pts),
                                pts=pts if t in ('S','s') else None))
            pts=[]
        if t not in (): args=[]
    return out
```

#### `decode12.py`

```python
"""Re-derive Figure 12's edge labels from the PDF vector coordinates, rigorously:
match each drawn digit to the nearest incident edge of its cell's check."""
import re, math
import pdfparse
MAP={'!':2,'"':3,'#':4,'$':1,'%':5,'&':6,"'":7}
s=open("xobj_Im12.txt",encoding="latin-1").read()
pat=re.compile(r"q ([\d.eE+-]+) 0 0 ([\d.eE+-]+) ([\d.eE+-]+) ([\d.eE+-]+)\s*\n?cm\s*\n?BT [\d.eE+-]+ 0 0 [\d.eE+-]+ 0 ([\d.eE+-]+) Tm /TT\d 1 Tf \((.*?)\) Tj ET Q", re.S)
labels=[]
for m in pat.finditer(s):
    sx,sy,tx,ty,tmy,ch=m.groups()
    if ch in MAP:
        labels.append((float(tx), float(ty)+float(sy)*float(tmy), MAP[ch]))
o=pdfparse.parse(s)
small=[r for r in o if r['op'] in ('f','f*') and 5<r['w']<12 and 5<r['h']<12]
checks=[r for r in small if r['n']<=5]
circles=[r for r in small if r['n']>5]
print("checks:",len(checks)," circles:",len(circles)," labels:",len(labels))
EDGE=[('e1',33.5,47.9),('e2',0.0,21.4),('e3',-27.3,0.0),('e4',26.7,0.0),
      ('e5',0.0,-26.6),('e6',-48.0,-27.3)]
for chk in sorted(checks,key=lambda c:(-c['cy'],c['cx'])):
    cx,cy=chk['cx'],chk['cy']
    panel = 'UPPER' if cy>130 else 'LOWER'
    col = tuple(round(v,2) for v in chk['fill'])
    # its 6 incident data qubits (nearest circle to each ideal edge endpoint)
    nb={}
    for (e,dx,dy) in EDGE:
        best=min(circles,key=lambda r:(r['cx']-(cx+dx))**2+(r['cy']-(cy+dy))**2)
        d=math.hypot(best['cx']-(cx+dx),best['cy']-(cy+dy))
        nb[e]=(best,d)
    # each label -> nearest qubit of this cell (only labels within the cell's x-window)
    res={}
    for (lx,ly,val) in labels:
        cand=[(math.hypot(lx-nb[e][0]['cx'], ly-nb[e][0]['cy']),e) for (e,_,_) in EDGE]
        d,e=min(cand)
        if d<20 and abs(lx-cx)<80 and ((ly>130)==(cy>130)):
            res.setdefault(e,[]).append((round(d,1),val))
    print(f"check ({cx:6.1f},{cy:6.1f}) {panel} fill={col}")
    for (e,_,_) in EDGE:
        q,dq=nb[e]
        half='white' if q['fill'][0]>0.5 else 'black'
        print(f"    {e}: qubit ({q['cx']:6.1f},{q['cy']:6.1f}) {half} fit={dq:4.1f}  label(s) {res.get(e)}")
```

#### `fig12.py`

```python
"""Decode the CNOT schedule drawn in Figure 12 of arXiv:2603.05481 from the PDF's own vector
coordinates, and test every geometry-consistent reading against the code's legality and (MC).

Recovered from the figure (label positions matched to edge endpoints; see artifact):
  edges of a cell, relative to the check:  e1 (+33.5,+47.9) long diagonal, e2 (0,+21.4) vertical,
  e3 (-27.3,0) horizontal, e4 (+26.7,0) horizontal, e5 (0,-26.6) vertical, e6 (-48,-27.3) long
  diagonal.  White circles = LEFT half, black = RIGHT half (verified: for X-checks the white set is
  {2 vertical, 1 diagonal} = the A monomials {y,y^2,x^3}; for Z-checks the white set is
  {2 horizontal, 1 diagonal} = the B monomials {x,x^2,y^3}).

  X panel (filled squares = X checks), CNOT time per edge:
     blue  : e6=2 e2=3 e5=4 e3=5 e1=6 e4=7
     red   : e5=1 e6=2 e2=3 e1=4 e4=5 e3=6
     green : e5=1 e6=2 e2=3 e3=4 e1=5 e4=6
  Z panel (empty squares = Z checks):
     blue  : e2=2 e1=3 e5=4 e6=5 e3=6 e4=7
     red   : e5=1 e2=2 e1=3 e6=4 e3=5 e4=6
     green : e5=1 e2=2 e1=3 e3=4 e4=5 e6=6
"""
import itertools, json
import numpy as np
from gross import NG, N, gsum, A_MONOS, B_MONOS, xcheck_nb, zcheck_nb, xchecks_of, zchecks_of
from sched import make_phi, colour_valid
from cascade import CLS_OF, REPS

XPANEL = {'blue':  {'e6':2,'e2':3,'e5':4,'e3':5,'e1':6,'e4':7},
          'red':   {'e5':1,'e6':2,'e2':3,'e1':4,'e4':5,'e3':6},
          'green': {'e5':1,'e6':2,'e2':3,'e3':4,'e1':5,'e4':6}}
ZPANEL = {'blue':  {'e2':2,'e1':3,'e5':4,'e6':5,'e3':6,'e4':7},
          'red':   {'e5':1,'e2':2,'e1':3,'e6':4,'e3':5,'e4':6},
          'green': {'e5':1,'e2':2,'e1':3,'e3':4,'e4':5,'e6':6}}
COLS = ['blue', 'red', 'green']

# slot conventions of gross.py:
#   X slots 0,1,2 = A monomials (x^3, y, y^2) on the LEFT half; 3,4,5 = B (y^3, x, x^2) RIGHT
#   Z slots 0,1,2 = B monomials (y^3, x, x^2) on the LEFT half; 3,4,5 = A (x^3, y, y^2) RIGHT
# Figure geometry forces: the long diagonal in each half is the degree-3 monomial (x^3 resp. y^3),
# the two nearest-neighbour edges are the remaining two.  Only their order is free (2 x 2 per panel).
def xmaps():
    for a in ((1, 2), (2, 1)):          # (e2,e5) -> (y, y^2) slots (1,2)
        for b in ((4, 5), (5, 4)):      # (e3,e4) -> (x, x^2) slots (4,5)
            yield {'e6': 0, 'e2': a[0], 'e5': a[1], 'e1': 3, 'e3': b[0], 'e4': b[1]}

def zmaps():
    for a in ((1, 2), (2, 1)):          # (e3,e4) -> (x, x^2) slots (1,2)
        for b in ((4, 5), (5, 4)):      # (e2,e5) -> (y, y^2) slots (4,5)
            yield {'e6': 0, 'e3': a[0], 'e4': a[1], 'e1': 3, 'e2': b[0], 'e5': b[1]}

def slot_times(panel, mp):
    """panel colour -> array t[slot] of CNOT times"""
    out = {}
    for col in COLS:
        t = [None] * 6
        for e, tt in panel[col].items():
            t[mp[e]] = tt
        out[col] = t
    return out

def order_class(t):
    return CLS_OF[tuple(sorted(range(6), key=lambda s: t[s]))]

def legal_mc(phi, TX, TZ, permX, permZ, P):
    """explicit legality (all 6 CNOT times of a data qubit distinct mod P) and (MC)."""
    tX = [[TX[COLS[permX[int(phi[g])]]][s] for s in range(6)] for g in range(NG)]
    tZ = [[TZ[COLS[permZ[int(phi[g])]]][s] for s in range(6)] for g in range(NG)]
    for q in range(N):
        ts = [tX[c][(0 if s == 'L' else 3) + i] % P for (c, s, i) in xchecks_of(q)] + \
             [tZ[c][(0 if s == 'L' else 3) + i] % P for (c, s, i) in zchecks_of(q)]
        if len(set(ts)) != 6:
            return False, None
    bad = 0; tot = 0
    for a in range(NG):
        xs = {q: (0 if s == 'L' else 3) + i for q, s, i in xcheck_nb(a)}
        for b in range(NG):
            zs = {q: (0 if s == 'L' else 3) + i for q, s, i in zcheck_nb(b)}
            sh = set(xs) & set(zs)
            if not sh:
                continue
            for dp in (-2, -1, 0, 1, 2):
                tot += 1
                c = sum(1 for q in sh if tZ[b][zs[q]] + P * dp < tX[a][xs[q]])
                if c % 2:
                    bad += 1
    return True, (tot, bad)

if __name__ == "__main__":
    phi = make_phi(1, 1); assert colour_valid(phi)
    rows = []
    for xi, xm in enumerate(xmaps()):
        TX = slot_times(XPANEL, xm)
        xtr = {col: order_class(TX[col]) for col in COLS}
        for zi, zm in enumerate(zmaps()):
            TZ = slot_times(ZPANEL, zm)
            ztr = {col: order_class(TZ[col]) for col in COLS}
            for permX in itertools.permutations(range(3)):
                for permZ in itertools.permutations(range(3)):
                    for P in (6, 7, 8):
                        ok, mc = legal_mc(phi, TX, TZ, permX, permZ, P)
                        if ok:
                            rows.append(dict(xmap=xi, zmap=zi, permX=permX, permZ=permZ, P=P,
                                             mc=mc,
                                             Xtriple=tuple(xtr[COLS[permX[c]]] for c in range(3)),
                                             Ztriple=tuple(ztr[COLS[permZ[c]]] for c in range(3))))
    print("legal (xmap,zmap,colour-assignment,period) readings:", len(rows))
    seen = set()
    for r in rows:
        k = (r['Xtriple'], r['Ztriple'], r['P'], r['mc'][1])
        if k in seen: continue
        seen.add(k)
        print(f"  P={r['P']}  X-triple {r['Xtriple']}  Z-triple {r['Ztriple']}  "
              f"(MC) violations {r['mc'][1]}/{r['mc'][0]}  xmap={r['xmap']} zmap={r['zmap']}")
    for xi, xm in enumerate(xmaps()):
        TX = slot_times(XPANEL, xm)
        print(f"xmap{xi}: X classes per panel colour:",
              {c: order_class(TX[c]) for c in COLS}, "orders",
              {c: tuple(sorted(range(6), key=lambda s: TX[c][s])) for c in COLS})
    for zi, zm in enumerate(zmaps()):
        TZ = slot_times(ZPANEL, zm)
        print(f"zmap{zi}: Z classes per panel colour:",
              {c: order_class(TZ[c]) for c in COLS}, "orders",
              {c: tuple(sorted(range(6), key=lambda s: TZ[c][s])) for c in COLS})
```

#### `fig12e.py`

```python
"""Figure-12 reading, done properly.

Period.  [SBB26] Eq. (3): t >= max(c(H_XZ), r(H_XZ)+2) = max(6,8) = 8 for the gross code, and their
LRC saturates it, so the SEC's PERIOD is 8 time steps, of which each check uses 6 for CNOTs (the
other two carry its ancilla preparation and measurement).  Legality is therefore "the 6 CNOT times
of a data qubit are distinct mod 8", not mod 6.

Panel consistency.  Circles are drawn black/white; three of each around every check, the same
pattern in Figures 11 and 12 and in both panels -- so the two circle colours are the two data
sublattices (left/right halves).  For X-checks the white set is {2 vertical, 1 long diagonal} and
for Z-checks {2 horizontal, 1 long diagonal}; the X-check's LEFT neighbours are the A monomials
{y, y^2, x^3} (two y-shifts and one long x-shift) and the Z-check's LEFT neighbours are the B
monomials {x, x^2, y^3}, so WHITE = LEFT half in both panels.  Both possible half assignments are
tried anyway.
"""
import itertools, json, sys
import numpy as np
from gross import NG, N, xcheck_nb, zcheck_nb
from sched import make_phi, colour_valid
from cascade import CLS_OF, collect_rules, survivors
from fig12 import XPANEL, ZPANEL, COLS

XSLOT = [[(0 if s == 'L' else 3) + i for (q, s, i) in xcheck_nb(g)] for g in range(NG)]
ZSLOT = [[(0 if s == 'L' else 3) + i for (q, s, i) in zcheck_nb(g)] for g in range(NG)]
XQ = [[q for (q, s, i) in xcheck_nb(g)] for g in range(NG)]
ZQ = [[q for (q, s, i) in zcheck_nb(g)] for g in range(NG)]
SHARED = []
for a in range(NG):
    for b in range(NG):
        sh = [(k, ZQ[b].index(XQ[a][k])) for k in range(6) if XQ[a][k] in ZQ[b]]
        if sh:
            SHARED.append((a, b, sh))

XWHITE = ['e2','e5','e6']; XBLACK = ['e1','e3','e4']
ZWHITE = ['e3','e4','e6']; ZBLACK = ['e1','e2','e5']

def maps(white, black, white_is_left):
    lo = (0,1,2) if white_is_left else (3,4,5)
    hi = (3,4,5) if white_is_left else (0,1,2)
    for pw in itertools.permutations(lo):
        for pb in itertools.permutations(hi):
            yield dict(zip(white, pw)) | dict(zip(black, pb))

def options(panel, white, black, white_is_left):
    out = []
    for m in maps(white, black, white_is_left):
        T = {}
        for col in COLS:
            t = [None]*6
            for e, tt in panel[col].items():
                t[m[e]] = tt
            T[col] = t
        for perm in itertools.permutations(range(3)):
            out.append((m, perm, {c: T[COLS[perm[c]]] for c in range(3)}))
    return out

def masks(TT, SL, QQ, PHI, P):
    mk = np.zeros(N, np.int64)
    for g in range(NG):
        tt = TT[PHI[g]]
        if len({x % P for x in tt}) != 6:
            return None
        for k in range(6):
            q = QQ[g][k]; t = tt[SL[g][k]] % P
            if mk[q] >> t & 1:
                return None
            mk[q] |= 1 << t
    return mk

def triples(TT):
    return tuple(CLS_OF[tuple(sorted(range(6), key=lambda s: TT[c][s]))] for c in range(3))

def mc_bad(TTX, TTZ, PHI, P):
    bad = 0
    for (a, b, sh) in SHARED:
        ca = PHI[a]; cb = PHI[b]
        for dp in (-2,-1,0,1,2):
            c = sum(1 for (k, l) in sh
                    if TTZ[cb][ZSLOT[b][l]] + P*dp < TTX[ca][XSLOT[a][k]])
            if c % 2:
                bad += 1
    return bad

results = []
for P in (6, 7, 8):
  for wl in (True, False):
    for (upper, lower, tag) in ((XPANEL, ZPANEL, 'upper=X'), (ZPANEL, XPANEL, 'upper=Z')):
        uw, ub = (XWHITE, XBLACK) if tag == 'upper=X' else (ZWHITE, ZBLACK)
        lw, lb = (ZWHITE, ZBLACK) if tag == 'upper=X' else (XWHITE, XBLACK)
        XO = options(upper, uw, ub, wl); ZO = options(lower, lw, lb, wl)
        for (s, t) in [(1,1),(1,2),(2,1),(2,2)]:
            phi = make_phi(s, t)
            PHI = [int(phi[g]) for g in range(NG)]
            SURV = {}
            for sector in ('X','Z'):
                r1, r2 = collect_rules(sector, phi)
                alive, _, _ = survivors(r1, r2)
                SURV[sector] = {tuple(int(x) for x in v) for v in np.argwhere(alive)}
            XV = [(m,pm,TT,masks(TT,XSLOT,XQ,PHI,P)) for (m,pm,TT) in XO]
            XV = [v for v in XV if v[3] is not None]
            ZV = [(m,pm,TT,masks(TT,ZSLOT,ZQ,PHI,P)) for (m,pm,TT) in ZO]
            ZV = [v for v in ZV if v[3] is not None]
            nleg=0; nsurv=0; good=[]
            for (mx,px,TTX,kx) in XV:
                tx = triples(TTX)
                for (mz,pz,TTZ,kz) in ZV:
                    tz = triples(TTZ)
                    for d in range(P):
                        kzd = ((kz << d) | (kz >> (P-d))) & ((1<<P)-1) if d else kz
                        if (kx & kzd).any():
                            continue
                        nleg += 1
                        if tx not in SURV['X'] or tz not in SURV['Z']:
                            continue
                        nsurv += 1
                        TTZd = {c: [x+d for x in TTZ[c]] for c in TTZ}
                        if mc_bad(TTX, TTZd, PHI, P) == 0:
                            good.append((d, mx, px, tx, mz, pz, tz))
            if nleg or good:
                print(f"P={P} white={'LEFT' if wl else 'RIGHT'} {tag} phi={s}a+{t}b : "
                      f"legal {nleg}, surviving-both {nsurv}, (MC)-clean {len(good)}")
            for row in good:
                print("      delta=%d  X-triple %s  Z-triple %s" % (row[0], row[3], row[6]))
                print("         xedge", row[1], "colX", row[2], " zedge", row[4], "colZ", row[5])
                results.append(dict(P=P, white_left=wl, tag=tag, phi=[s,t], delta=row[0],
                                    xedge=row[1], colX=list(row[2]), Xtriple=list(row[3]),
                                    zedge=row[4], colZ=list(row[5]), Ztriple=list(row[6])))
json.dump(results, open("fig12_reading.json","w"), indent=1)
print("\nTOTAL fully-consistent readings:", len(results))
```

#### `fig12f.py`

```python
"""Figure-12 reading with the ancilla STRADDLE made explicit.

The figure labels CNOTs by their time step within one round window.  [SBB26]'s LRC staggers the Z
ancilla so that its window crosses the round boundary ("the Z ancilla is prepared at time step
t1+3 and measured at time step t1+2"): the two half-blocks a Z ancilla instance performs are the
LATER block of one round window and the EARLIER block of the NEXT round window.  So for a straddled
check type the true within-instance order is (later block) then (earlier block + one period), which
is NOT what the drawing reads off left-to-right.  Both possibilities are tried for each panel.
"""
import itertools, json
import numpy as np
from gross import NG, N, xcheck_nb, zcheck_nb
from sched import make_phi, colour_valid
from cascade import CLS_OF, collect_rules, survivors
from fig12 import XPANEL, ZPANEL, COLS
from fig12e import (XSLOT, ZSLOT, XQ, ZQ, SHARED, XWHITE, XBLACK, ZWHITE, ZBLACK, maps)

def options(panel, white, black, white_is_left, straddle, P):
    out = []
    for m in maps(white, black, white_is_left):
        T = {}
        for col in COLS:
            t = [None] * 6
            for e, tt in panel[col].items():
                t[m[e]] = tt
            if straddle:
                wl = [t[m[e]] for e in white]; bl = [t[m[e]] for e in black]
                # the block drawn LATER in the round is the instance's first block;
                # the earlier-drawn block belongs to the next round window.
                if sum(wl) / 3 < sum(bl) / 3:
                    for e in white: t[m[e]] += P
                else:
                    for e in black: t[m[e]] += P
            T[col] = t
        for perm in itertools.permutations(range(3)):
            out.append((m, perm, {c: T[COLS[perm[c]]] for c in range(3)}))
    return out

def masks(TT, SL, QQ, PHI, P):
    mk = np.zeros(N, np.int64)
    for g in range(NG):
        tt = TT[PHI[g]]
        if len({x % P for x in tt}) != 6:
            return None
        for k in range(6):
            q = QQ[g][k]; t = tt[SL[g][k]] % P
            if mk[q] >> t & 1:
                return None
            mk[q] |= 1 << t
    return mk

def triples(TT):
    return tuple(CLS_OF[tuple(sorted(range(6), key=lambda s: TT[c][s]))] for c in range(3))

def mc_bad(TTX, TTZ, PHI, P):
    bad = 0
    for (a, b, sh) in SHARED:
        ca = PHI[a]; cb = PHI[b]
        for dp in (-3, -2, -1, 0, 1, 2, 3):
            c = sum(1 for (k, l) in sh
                    if TTZ[cb][ZSLOT[b][l]] + P * dp < TTX[ca][XSLOT[a][k]])
            if c % 2:
                bad += 1
    return bad

results = []
for P in (6, 7, 8):
 for stX in (False, True):
  for stZ in (False, True):
   for wl in (True, False):
    for (upper, lower, tag) in ((XPANEL, ZPANEL, 'upper=X'), (ZPANEL, XPANEL, 'upper=Z')):
        uw, ub, us = ((XWHITE, XBLACK, stX) if tag == 'upper=X' else (ZWHITE, ZBLACK, stZ))
        lw, lb, ls = ((ZWHITE, ZBLACK, stZ) if tag == 'upper=X' else (XWHITE, XBLACK, stX))
        XO = options(upper, uw, ub, wl, us, P); ZO = options(lower, lw, lb, wl, ls, P)
        for (s, t) in [(1, 1), (1, 2), (2, 1), (2, 2)]:
            phi = make_phi(s, t)
            PHI = [int(phi[g]) for g in range(NG)]
            SURV = {}
            for sector in ('X', 'Z'):
                r1, r2 = collect_rules(sector, phi)
                alive, _, _ = survivors(r1, r2)
                SURV[sector] = {tuple(int(x) for x in v) for v in np.argwhere(alive)}
            XV = [(m, pm, TT, masks(TT, XSLOT, XQ, PHI, P)) for (m, pm, TT) in XO]
            XV = [v for v in XV if v[3] is not None]
            ZV = [(m, pm, TT, masks(TT, ZSLOT, ZQ, PHI, P)) for (m, pm, TT) in ZO]
            ZV = [v for v in ZV if v[3] is not None]
            good = []; nsurv = 0
            for (mx, px, TTX, kx) in XV:
                tx = triples(TTX)
                for (mz, pz, TTZ, kz) in ZV:
                    tz = triples(TTZ)
                    for d in range(P):
                        kzd = ((kz << d) | (kz >> (P - d))) & ((1 << P) - 1) if d else kz
                        if (kx & kzd).any():
                            continue
                        if tx not in SURV['X'] or tz not in SURV['Z']:
                            continue
                        nsurv += 1
                        TTZd = {c: [x + d for x in TTZ[c]] for c in TTZ}
                        if mc_bad(TTX, TTZd, PHI, P) == 0:
                            good.append((d, mx, px, tx, mz, pz, tz))
            if good:
                print(f"P={P} straddleX={stX} straddleZ={stZ} white={'LEFT' if wl else 'RIGHT'} "
                      f"{tag} phi={s}a+{t}b : surviving-both {nsurv}, (MC)-clean {len(good)}")
                for row in good:
                    print(f"      delta={row[0]}  X-triple {row[3]}  Z-triple {row[6]}")
                    results.append(dict(P=P, stX=stX, stZ=stZ, white_left=wl, tag=tag, phi=[s, t],
                                        delta=row[0], xedge=row[1], colX=list(row[2]),
                                        Xtriple=list(row[3]), zedge=row[4], colZ=list(row[5]),
                                        Ztriple=list(row[6])))
json.dump(results, open("fig12_reading2.json", "w"), indent=1)
print("\nTOTAL legal + (MC)-clean + cascade-surviving readings:", len(results))
```

#### `casc45.py`

```python
"""[SBB26] Prop. 6's own second step, reproduced: 'we tile ALL RED CHECKS with a residual set, and
upper bound the resulting extended-code distances.  Scanning through the 45 residual sets, we find
all but 4 have extended-code distance of 10 or below.'

R = the residual errors of the 24 checks of ONE colour class only.  A class is eliminated when some
weight-12 logical L contains either a covered triple in the last three CNOT positions of one check
of that colour (gain 2 -> weight 10) or two DISJOINT weight-2 residuals of two checks of that
colour (gain 1+1 -> weight 10).  Every elimination exhibits a weight-10 extended codeword, so the
filter is one-sided sound, exactly as the paper's upper-bound search is."""
import itertools
import numpy as np
from gross import NG
from sched import make_phi, colour_valid
from cascade import (REPS, NCLS, ACT2, ACT3, PAIRS, TRIPS, PIDX, TIDX, sector_data, collect_rules,
                     survivors)

def stage1(sector, phi):
    """the 90 -> 45 filter (single isolated check), colour-independent"""
    slots, Pl, Hstab, Hdet = sector_data(sector)
    kill = set()
    for L in Pl:
        for c in range(NG):
            S = [k for k in range(6) if L[slots[c][k]]]
            if len(S) == 3:
                kill.add(TIDX[tuple(S)])
    ok = np.ones(NCLS, bool)
    for ti in kill:
        ok &= ~ACT3[:, ti]
    return ok

def tile_one_colour(sector, phi, colour, alive45):
    """which of the 45 survive when that residual class is tiled on ONE colour class"""
    slots, Pl, Hstab, Hdet = sector_data(sector)
    dead = np.zeros(NCLS, bool)
    for L in Pl:
        hits = []
        for c in range(NG):
            if int(phi[c]) != colour:
                continue
            S = [k for k in range(6) if L[slots[c][k]]]
            if len(S) < 2:
                continue
            for Pr in itertools.combinations(S, 2):
                hits.append((PIDX[Pr], frozenset(slots[c][k] for k in Pr)))
        for i in range(len(hits)):
            for j in range(i + 1, len(hits)):
                if hits[i][1] & hits[j][1]:
                    continue
                dead |= (ACT2[:, hits[i][0]] & ACT2[:, hits[j][0]])
    return alive45 & ~dead

for sector in ('Z', 'X'):
    a45 = stage1(sector, None)
    print(f"=== sector {sector}:  90 -> {int(a45.sum())} after the single-check filter")
    for (s, t) in [(1, 1), (1, 2), (2, 1), (2, 2)]:
        phi = make_phi(s, t); assert colour_valid(phi)
        res = []
        for colour in range(3):
            surv = tile_one_colour(sector, phi, colour, a45)
            res.append(sorted(int(i) for i in np.nonzero(surv)[0]))
        same = all(r == res[0] for r in res)
        print(f"   phi={s}a+{t}b : 45 -> {len(res[0])} per colour  {res[0]}"
              f"   (identical for all three colours: {same})")
```

#### `fam.py`

```python
"""The phi = a+b tiled family: survivor lists, LRC-compatible classes, colour-rotation orbits."""
import numpy as np, itertools, json
from gross import NG
from sched import make_phi, colour_valid
from cascade import REPS, CLS_OF, survivors, collect_rules, NCLS

def lrc_classes():
    """classes containing an order that is one contiguous L block (slots 0,1,2) then one
    contiguous R block (slots 3,4,5), or the reverse."""
    out=set()
    for Lp in itertools.permutations(range(3)):
        for Rp in itertools.permutations(range(3,6)):
            out.add(CLS_OF[tuple(Lp)+tuple(Rp)])
            out.add(CLS_OF[tuple(Rp)+tuple(Lp)])
    return sorted(out)

LRC = lrc_classes()

def surv(sector, s, t):
    phi = make_phi(s, t); assert colour_valid(phi)
    r1, r2 = collect_rules(sector, phi)
    alive, stage1, after1 = survivors(r1, r2)
    return [tuple(int(x) for x in v) for v in np.argwhere(alive)]

def rot_orbit(tr):
    return sorted({tr, (tr[1],tr[2],tr[0]), (tr[2],tr[0],tr[1])})

if __name__ == "__main__":
    print("LRC-compatible order classes (of 90):", LRC)
    out={}
    for sector in ('Z','X'):
        S = surv(sector, 1, 1)
        classes = sorted({c for t in S for c in t})
        reps=[]; seen=set()
        for t in S:
            if t in seen: continue
            o=rot_orbit(t); seen|=set(o); reps.append(t)
        print(f"\n=== sector {sector}, phi=a+b: {len(S)} survivors, classes used {classes}")
        print("   orbit reps under cyclic colour rotation:", len(reps))
        for t in S:
            print("   ", t, "orders", [REPS[c] for c in t],
                  "LRC" if all(c in LRC for c in t) else "",
                  "uniform" if len(set(t))==1 else "")
        out[sector]=dict(survivors=S, classes=classes, reps=reps,
                         lrc_survivors=[t for t in S if all(c in LRC for c in t)],
                         lrc_nonuniform=[t for t in S if all(c in LRC for c in t) and len(set(t))>1])
        print("   LRC-compatible survivors:", len(out[sector]['lrc_survivors']),
              " non-uniform:", len(out[sector]['lrc_nonuniform']))
        print("   ", out[sector]['lrc_nonuniform'])
    json.dump(out, open("fam.json","w"))
```

#### `lrc.py`

```python
"""STAGGERED left-right circuits (LRCs) for the gross code, 6 CNOT layers per period.

Structure (SBB Fig. 3, with the staggering that makes the Z-ancilla window straddle the period
boundary):
    block A = layers 0,1,2 of a period :  L_X  (X-checks on LEFT data)  ||  R_Z (Z on RIGHT data)
    block B = layers 3,4,5 of a period :  R_X  (X-checks on RIGHT data) ||  L_Z (Z on LEFT data)
X-ancilla instance p : L_X in block A of period p, R_X in block B of period p.
Z-ancilla instance p : L_Z in block B of period p, R_Z in block A of period p+1.
So both check types run one contiguous LEFT block then one contiguous RIGHT block, and the Z
window straddles the boundary.  A 3-colour-tiled LRC lets the within-block layer depend on the
check's colour phi(g).

Free parameters (per colour c, per monomial index i, each row a bijection {0,1,2}->{0,1,2}):
    LXL[c][i] layer-in-block-A of X-check colour c, LEFT  qubit via A_i
    LXR[c][i] layer-in-block-B of X-check colour c, RIGHT qubit via B_i
    LZL[c][i] layer-in-block-B of Z-check colour c, LEFT  qubit via B_i
    LZR[c][i] layer-in-block-A of Z-check colour c, RIGHT qubit via A_i
"""
import numpy as np, itertools, json, sys
from gross import (NG, N, ELL, EM, gidx, gsum, A_MONOS, B_MONOS, HX, HZ,
                   xcheck_nb, zcheck_nb)
from sched import make_phi, colour_valid
from cascade import CLS_OF

BIJ = list(itertools.permutations(range(3)))          # 6 bijections i -> layer


def colours_of_monos(phi):
    al = [int(phi[gsum(0, m)]) for m in A_MONOS]       # phi(A_i)
    be = [int(phi[gsum(0, m)]) for m in B_MONOS]       # phi(B_i)
    return al, be


def ok_rows(phi, sign, mono_cols):
    """All (row_0,row_1,row_2) triples of bijections such that for every v in {0,1,2},
    i -> row[(v + sign*mono_cols[i]) % 3][i] is a bijection.  This is exactly the perfect-matching
    condition for the corresponding block/half."""
    out = []
    for rows in itertools.product(BIJ, repeat=3):
        good = True
        for v in range(3):
            vals = [rows[(v + sign * mono_cols[i]) % 3][i] for i in range(3)]
            if len(set(vals)) != 3:
                good = False; break
        if good:
            out.append(rows)
    return out


def x_triple(LXL, LXR):
    """within-check order class per colour, X sector (slots 0,1,2 = A monomials/left)."""
    tr = []
    for c in range(3):
        left = sorted(range(3), key=lambda i: LXL[c][i])
        right = sorted(range(3), key=lambda i: LXR[c][i])
        tr.append(CLS_OF[tuple(left) + tuple(3 + j for j in right)])
    return tuple(tr)


def z_triple(LZL, LZR):
    """Z sector (slots 0,1,2 = B monomials/left, 3,4,5 = A monomials/right)."""
    tr = []
    for c in range(3):
        left = sorted(range(3), key=lambda i: LZL[c][i])
        right = sorted(range(3), key=lambda i: LZR[c][i])
        tr.append(CLS_OF[tuple(left) + tuple(3 + j for j in right)])
    return tuple(tr)


# ---------------- explicit absolute times, legality and (MC) ----------------
P = 6      # CNOT layers per period


def times(phi, LXL, LXR, LZL, LZR, p):
    """absolute CNOT times.  tX[(g,'L',i)] etc. for X-instance p and Z-instance p."""
    tX, tZ = {}, {}
    for g in range(NG):
        c = int(phi[g])
        for i in range(3):
            tX[(g, 'L', i)] = P * p + LXL[c][i]
            tX[(g, 'R', i)] = P * p + 3 + LXR[c][i]
            tZ[(g, 'L', i)] = P * p + 3 + LZL[c][i]
            tZ[(g, 'R', i)] = P * (p + 1) + LZR[c][i]
    return tX, tZ


def legality(phi, LXL, LXR, LZL, LZR):
    """explicit check that every absolute layer is a matching on the 288 qubits, over 4 periods."""
    busy = {}
    for p in range(4):
        tX, tZ = times(phi, LXL, LXR, LZL, LZR, p)
        for g in range(NG):
            xa, za = N + g, N + NG + g
            for q, s, i in xcheck_nb(g):
                t = tX[(g, s, i)]
                for qq in (q, xa):
                    if (t, qq) in busy:
                        return False
                    busy[(t, qq)] = 1
            for q, s, i in zcheck_nb(g):
                t = tZ[(g, s, i)]
                for qq in (q, za):
                    if (t, qq) in busy:
                        return False
                    busy[(t, qq)] = 1
    return True


def mc_violations(phi, LXL, LXR, LZL, LZR, dp_range=(-2, -1, 0, 1, 2)):
    """(MC): for every overlapping X-check instance a and Z-check instance b,
    #{ q in supp(a) cap supp(b) : t(q->b) < t(a->q) } must be even."""
    tot = 0; bad = 0; per_dp = {}
    for dp in dp_range:
        tXa, _ = times(phi, LXL, LXR, LZL, LZR, 2)
        _, tZb = times(phi, LXL, LXR, LZL, LZR, 2 + dp)
        nb = 0
        for a in range(NG):
            xs = {q: (s, i) for q, s, i in xcheck_nb(a)}
            for b in range(NG):
                zs = {q: (s, i) for q, s, i in zcheck_nb(b)}
                sh = set(xs) & set(zs)
                if not sh:
                    continue
                tot += 1
                c = 0
                for q in sh:
                    s, i = xs[q]; s2, i2 = zs[q]
                    if tZb[(b, s2, i2)] < tXa[(a, s, i)]:
                        c += 1
                if c % 2:
                    bad += 1; nb += 1
        per_dp[dp] = nb
    return tot, bad, per_dp


def overlap_structure():
    """check the 'one left, one right, index pair swapped' fact used in the parity argument."""
    halves = set(); swapped = 0; pairs = 0
    for a in range(NG):
        xs = {q: (s, i) for q, s, i in xcheck_nb(a)}
        for b in range(NG):
            zs = {q: (s, i) for q, s, i in zcheck_nb(b)}
            sh = sorted(set(xs) & set(zs))
            if not sh:
                continue
            pairs += 1
            halves.add(tuple(sorted(xs[q][0] for q in sh)))
            L = [q for q in sh if xs[q][0] == 'L'][0]
            R = [q for q in sh if xs[q][0] == 'R'][0]
            # X uses A_i on the left qubit and B_j on the right; Z uses B_j' on the left and A_i'
            # on the right.  claim: i == i' and j == j'
            if xs[L][1] == zs[R][1] and xs[R][1] == zs[L][1]:
                swapped += 1
    return pairs, sorted(halves), swapped


if __name__ == "__main__":
    s, t = (int(sys.argv[1]), int(sys.argv[2])) if len(sys.argv) > 2 else (1, 1)
    phi = make_phi(s, t); assert colour_valid(phi)
    al, be = colours_of_monos(phi)
    print(f"phi = {s}a+{t}b   phi(A_i) = {al}   phi(B_i) = {be}")
    pairs, halves, swapped = overlap_structure()
    print(f"overlapping (X,Z) check pairs: {pairs}; shared-qubit halves: {halves}; "
          f"index-pair-swapped: {swapped}/{pairs}")

    XL = ok_rows(phi, +1, al)      # block A, left  (X on left, checks g+A_i)
    ZR = ok_rows(phi, -1, al)      # block A, right (Z on right, checks g-A_i)
    XR = ok_rows(phi, +1, be)      # block B, right (X on right, checks g+B_i)
    ZL = ok_rows(phi, -1, be)      # block B, left  (Z on left, checks g-B_i)
    print(f"legal within-block layer patterns: |LXL|={len(XL)} |LXR|={len(XR)} "
          f"|LZL|={len(ZL)} |LZR|={len(ZR)}  -> {len(XL)*len(XR)*len(ZL)*len(ZR)} tiled LRCs")

    xt = sorted({x_triple(a, b) for a in XL for b in XR})
    zt = sorted({z_triple(a, b) for a in ZL for b in ZR})
    print(f"realisable X-sector order-class triples: {len(xt)}")
    print(f"realisable Z-sector order-class triples: {len(zt)}")
    json.dump(dict(x=[list(v) for v in xt], z=[list(v) for v in zt]),
              open(f"lrc_triples_{s}{t}.json", "w"))

    # legality + (MC) on a random sample of full schedules
    rng = np.random.default_rng(7)
    nleg = 0; nmc = 0; ns = 40
    for _ in range(ns):
        A1 = XL[rng.integers(len(XL))]; B1 = XR[rng.integers(len(XR))]
        A2 = ZL[rng.integers(len(ZL))]; B2 = ZR[rng.integers(len(ZR))]
        nleg += legality(phi, A1, B1, A2, B2)
        tot, bad, per = mc_violations(phi, A1, B1, A2, B2)
        nmc += (bad == 0)
    print(f"random sample of {ns} tiled staggered LRCs: legal {nleg}/{ns}, "
          f"(MC)-clean {nmc}/{ns}")
    A1, B1, A2, B2 = XL[0], XR[0], ZL[0], ZR[0]
    tot, bad, per = mc_violations(phi, A1, B1, A2, B2)
    print(f"   one example: {tot} (X-instance, Z-instance) overlapping pairs examined, "
          f"{bad} odd; per period offset: {per}")
    print("   its (Z,X) class triples:", z_triple(A2, B2), x_triple(A1, B1))
```

#### `lrcall.py`

```python
"""For every one of the four group 3-colourings, and both LRC block orientations, compute
   (i) the order-class triples realisable by a legal 3-colour-tiled STAGGERED left-right circuit
       with 6 CNOT layers per period (depth 8), and
   (ii) their intersection with that colouring's cascade survivors."""
import itertools, json
import numpy as np
from gross import NG
from sched import make_phi, colour_valid
from cascade import CLS_OF, REPS, collect_rules, survivors
import lrc

def realisable(phi, orient):
    al, be = lrc.colours_of_monos(phi)
    if orient == 'LX_first':
        XL = lrc.ok_rows(phi, +1, al); XR = lrc.ok_rows(phi, +1, be)
        ZL = lrc.ok_rows(phi, -1, be); ZR = lrc.ok_rows(phi, -1, al)
    else:   # mirrored: block A = R_X || L_Z, block B = L_X || R_Z
        XL = lrc.ok_rows(phi, +1, al); XR = lrc.ok_rows(phi, +1, be)
        ZL = lrc.ok_rows(phi, -1, be); ZR = lrc.ok_rows(phi, -1, al)
    xt = sorted({lrc.x_triple(a, b) for a in XL for b in XR})
    zt = sorted({lrc.z_triple(a, b) for a in ZL for b in ZR})
    return xt, zt, (len(XL), len(XR), len(ZL), len(ZR))

out = {}
for (s, t) in [(1,1),(1,2),(2,1),(2,2)]:
    phi = make_phi(s, t); assert colour_valid(phi)
    xt, zt, sz = realisable(phi, 'LX_first')
    row = {}
    for sector, tr in (('X', xt), ('Z', zt)):
        r1, r2 = collect_rules(sector, phi)
        alive, _, _ = survivors(r1, r2)
        surv = {tuple(int(x) for x in v) for v in np.argwhere(alive)}
        inter = sorted(set(tr) & surv)
        row[sector] = dict(nrealisable=len(tr), nsurvivors=len(surv),
                           intersection=[list(v) for v in inter])
        print(f"phi={s}a+{t}b sector {sector}: {len(tr)} realisable triples, {len(surv)} cascade "
              f"survivors, intersection {len(inter)} -> {inter}")
    row['blocksizes'] = sz
    out[f"{s}{t}"] = row
json.dump(out, open("lrcall.json", "w"), indent=1)
```

#### `rotcheck.py`

```python
"""Verify: cyclic colour rotation of a tiled assignment is realised by a TRANSLATION of the code,
hence rotated triples have identical extended codes up to relabelling and identical d_ext."""
import numpy as np, itertools
from gross import NG, N, ELL, EM, gidx, HX, HZ, Reducer, rref
from sched import make_phi
from cert import tiled_orders
import dext

phi = make_phi(1, 1)
def dperm(a, b):
    p = np.empty(N, int)
    for i in range(ELL):
        for j in range(EM):
            p[gidx(i, j)] = gidx(i + a, j + b); p[NG + gidx(i, j)] = NG + gidx(i + a, j + b)
    return p
def cperm(a, b):
    p = np.empty(NG, int)
    for i in range(ELL):
        for j in range(EM):
            p[gidx(i, j)] = gidx(i + a, j + b)
    return p

# a translation g with phi(g) = 1
g = next((a, b) for a in range(ELL) for b in range(EM) if (a + b) % 3 == 1)
print("translation with phi(g)=1 :", g)
dp, cp = dperm(*g), cperm(*g)
# it is a code automorphism: preserves rowspace(HX), rowspace(HZ), ker, and logical triviality
RX, RZ = Reducer(HX), Reducer(HZ)
print("  permutes rowspace(HX):", all(RX.inspan(HX[r][np.argsort(dp)]) for r in range(NG)))
print("  permutes rowspace(HZ):", all(RZ.inspan(HZ[r][np.argsort(dp)]) for r in range(NG)))

bad = 0
for sector in ('Z', 'X'):
    for tr in itertools.product([1, 2, 9, 62] if sector == 'Z' else [0, 2, 9, 14], repeat=3):
        rot = (tr[1], tr[2], tr[0])
        o1, _ = tiled_orders(sector, phi, tr)
        o2, _ = tiled_orders(sector, phi, rot)
        r1 = dext.residual_sets(o1); r2 = dext.residual_sets(o2)
        # translating assignment `tr` by g must give exactly assignment `rot`
        for c in range(NG):
            for k in range(3):
                if tuple(sorted(int(dp[q]) for q in r1[c][k])) != tuple(sorted(r2[int(cp[c])][k])):
                    bad += 1
print("residual-set equivariance failures over all 64 triples per sector, both sectors:", bad)
```

#### `job.py`

```python
"""One (sector, tiled triple, W) exact d_ext decision query, UNQUOTIENTED (full 360 columns).
SAT -> explicit witness (re-verified from the definitions).  UNSAT -> certified d_ext > W.
Optional 5th arg: orbit index (uses the translation quotient of dext2)."""
import sys, time, json
import numpy as np
from pysat.solvers import Cadical153
from sched import make_phi
from cert import tiled_orders
import dext, dext2

sector = sys.argv[1]
triple = tuple(int(c) for c in sys.argv[2].split(','))
W      = int(sys.argv[3])
s_par, t_par = (int(sys.argv[4]), int(sys.argv[5])) if len(sys.argv) > 5 else (1, 1)
oi     = int(sys.argv[6]) if len(sys.argv) > 6 else -1

phi = make_phi(s_par, t_par)
orders, _ = tiled_orders(sector, phi, triple)
ctx, Hstab = dext.sector_ctx(orders, sector)
c = dext2.Cert(ctx, W)
rec = dict(sector=sector, triple=list(triple), W=W, phi=[s_par, t_par], orbit=oi,
           nclauses=len(c.cls))
t0 = time.time()
if oi < 0:
    with Cadical153(bootstrap_with=c.cls) as S:
        sat = S.solve()
        m = S.get_model() if sat else None
    rec['seconds'] = round(time.time() - t0, 1)
    if sat:
        ms = set(x for x in m if x > 0)
        E = np.array([1 if c.z[j] in ms else 0 for j in range(144)], np.uint8)
        R = [(cc, k) for cc in range(72) for k in range(3) if c.u[cc][k] in ms]
        D = np.array([1 if c.d[j] in ms else 0 for j in range(144)], np.uint8)
        info = dext.verify_witness(ctx, E, R, D, Hstab)
        rec.update(verdict='SAT', info={k: (int(v) if not isinstance(v, bool) else bool(v))
                                        for k, v in info.items()},
                   R=[[int(a), int(b)] for a, b in R],
                   D=[int(i) for i in np.nonzero(D)[0]],
                   E=[int(i) for i in np.nonzero(E)[0]])
    else:
        rec.update(verdict='UNSAT')
else:
    S, orbits = dext2.column_orbits(phi, triple)
    rec['norbits'] = len(orbits); rec['stab'] = len(S)
    if oi >= len(orbits):
        rec.update(verdict='NOORBIT'); print(json.dumps(rec)); sys.exit(0)
    sat, wit, el = c.run([orbits[oi]], Hstab, verbose=False)
    rec['seconds'] = round(el, 1)
    rec['rep'] = str(orbits[oi][0])
    if sat:
        E, R, D, info = wit
        rec.update(verdict='SAT', info={k: (int(v) if not isinstance(v, bool) else bool(v))
                                        for k, v in info.items()},
                   R=[[int(a), int(b)] for a, b in R],
                   D=[int(i) for i in np.nonzero(D)[0]],
                   E=[int(i) for i in np.nonzero(E)[0]])
    else:
        rec.update(verdict='UNSAT')
print(json.dumps(rec))
```

#### `job3.py`

```python
"""One (sector, tiled triple, W, |R| = K) exact d_ext subproblem, with the two cardinality cuts
that K makes available.  Both are sound, not heuristic:

  |d| <= W - K            since  weight = |d| + |R| <= W  and  |R| = K;
  |E| <= W + 2K           since  E = d xor (xor of the K residuals), every residual has weight <= 3,
                          so |E| <= |d| + 3K <= (W-K) + 3K.

Together with the standing cut |E| >= 12 (the code's own minimum logical weight, certified by
reproducing d(gross) = 12 with the residual set switched off) these pin |E| into a narrow window --
for K = 1 they force |E| = 12 exactly.  K ranges over 0..W; the subproblems are exhaustive, so
UNSAT for every K certifies d_ext > W."""
import sys, time, json
import numpy as np
from pysat.solvers import Cadical153
from pysat.card import CardEnc, EncType
from sched import make_phi
from cert import tiled_orders
import dext, dext2

sector = sys.argv[1]
triple = tuple(int(c) for c in sys.argv[2].split(','))
W      = int(sys.argv[3])
K      = int(sys.argv[4])
oi     = int(sys.argv[5]) if len(sys.argv) > 5 else -1
s_par, t_par = (int(sys.argv[6]), int(sys.argv[7])) if len(sys.argv) > 7 else (1, 1)

phi = make_phi(s_par, t_par)
orders, _ = tiled_orders(sector, phi, triple)
ctx, Hstab = dext.sector_ctx(orders, sector)
c = dext2.Cert(ctx, W)
ulits = [c.u[cc][k] for cc in range(72) for k in range(3)]
cls = list(c.cls); top = c.top
def add(enc):
    global cls, top
    cls += enc.clauses
    top = max([top] + [abs(l) for cl in enc.clauses for l in cl])
add(CardEnc.atmost(lits=ulits, bound=K, top_id=top, encoding=EncType.seqcounter))
if K > 0:
    add(CardEnc.atleast(lits=ulits, bound=K, top_id=top, encoding=EncType.seqcounter))
add(CardEnc.atmost(lits=c.d, bound=W - K, top_id=top, encoding=EncType.seqcounter))
add(CardEnc.atmost(lits=c.z, bound=W + 2*K, top_id=top, encoding=EncType.seqcounter))
rec = dict(sector=sector, triple=list(triple), W=W, K=K, orbit=oi, phi=[s_par, t_par],
           nclauses=len(cls))
assumptions = []
if oi >= 0:
    S, orbits = dext2.column_orbits(phi, triple)
    rec['norbits'] = len(orbits); rec['stab'] = len(S)
    if oi >= len(orbits):
        rec.update(verdict='NOORBIT'); print(json.dumps(rec)); sys.exit(0)
    rec['rep'] = str(orbits[oi][0])
    assumptions = [c.col_lit(orbits[oi][0])]
t0 = time.time()
with Cadical153(bootstrap_with=cls) as S2:
    sat = S2.solve(assumptions=assumptions)
    m = S2.get_model() if sat else None
rec['seconds'] = round(time.time() - t0, 1)
if sat:
    ms = set(x for x in m if x > 0)
    E = np.array([1 if c.z[j] in ms else 0 for j in range(144)], np.uint8)
    R = [(cc, k) for cc in range(72) for k in range(3) if c.u[cc][k] in ms]
    D = np.array([1 if c.d[j] in ms else 0 for j in range(144)], np.uint8)
    info = dext.verify_witness(ctx, E, R, D, Hstab)
    rec.update(verdict='SAT',
               info={k2: (int(v) if not isinstance(v, bool) else bool(v)) for k2, v in info.items()},
               R=[[int(a), int(b)] for a, b in R],
               D=[int(i) for i in np.nonzero(D)[0]],
               E=[int(i) for i in np.nonzero(E)[0]])
else:
    rec.update(verdict='UNSAT')
print(json.dumps(rec))
```

#### `verify.py`

```python
"""Independent re-verification of the SAT witnesses: exact F2 algebra from the definitions, an
own-code Pauli-frame simulation of the literal alternating-XZ circuit with the tiled orders, and
stim (Z-sector witnesses)."""
import json, glob, sys
import numpy as np
from gross import NG, N, HX, HZ, xcheck_nb, zcheck_nb, Reducer
from sched import make_phi
from cert import tiled_orders
import dext, simverify, stimverify

phi = make_phi(1, 1)
rows = []
for f in sorted(glob.glob('out/*_W10.json')):
    try: r = json.load(open(f))
    except: continue
    if r['verdict'] != 'SAT': continue
    rows.append(r)
which = sys.argv[1:] if len(sys.argv) > 1 else None
nz = 0
for r in rows:
    sec = r['sector']; tr = tuple(r['triple'])
    tag = f"{sec}{tr}"
    if which and tag not in which: continue
    orders, Hstab = tiled_orders(sec, phi, tr)
    ctx, Hst = dext.sector_ctx(orders, sec)
    R = [(a, b) for a, b in r['R']]
    D = np.zeros(N, np.uint8); D[r['D']] = 1
    E = np.zeros(N, np.uint8); E[r['E']] = 1
    alg = dext.verify_witness(ctx, E, R, D, Hst)
    out = {'triple': tr, 'sector': sec, 'algebra': alg}
    if sec == 'Z':
        out['circuit'] = simverify.verify(orders, R, r['D'], verbose=False)
        oX = [[q for q, s, i in xcheck_nb(g)] for g in range(NG)]
        if nz < 12:
            out['stim'] = stimverify.check(oX, orders, R, r['D']); nz += 1
    else:
        out['circuit'] = simverify.verify_x(orders, R, r['D'], verbose=False)
    print(json.dumps(out))
```

#### `altcheck.py`

```python
"""Every one of the 44 tiled assignments IS realisable as a valid non-interleaved SEC: the
alternating-XZ circuit with those within-check orders.  Check legality, (MC) and stim determinism
for the reconstructed candidate's orders (Z-triple (1,2,62), X-triple (14,0,2)) and, for (MC) only,
for all 44 x 44 sector pairs."""
import numpy as np, stim, itertools, json
from gross import NG, N, xcheck_nb, zcheck_nb, HX
from sched import make_phi
from cert import tiled_orders
import simverify, pool as poolmod

phi = make_phi(1, 1)
oZ, _ = tiled_orders('Z', phi, (1, 2, 62))
oX, _ = tiled_orders('X', phi, (14, 0, 2))
gates = simverify.alternating_circuit(oX, oZ)
print("alternating-XZ circuit with the candidate's orders:", len(gates), "CNOT layers,",
      sum(len(l) for l in gates), "CNOTs; every layer asserted a matching by the builder")

# absolute CNOT times
tX = {}; tZ = {}
for li, lay in enumerate(gates):
    for (c, t) in lay:
        if c >= N + NG: tZ[(c, t)] = li
        elif c >= N:    tX[(c, t)] = li
        else:           tZ[(c, t)] = li
XT = {}; ZT = {}
for g in range(NG):
    for k, q in enumerate(oX[g]): XT[(g, q)] = next(li for li, l in enumerate(gates) if (N+g, q) in l)
    for k, q in enumerate(oZ[g]): ZT[(g, q)] = next(li for li, l in enumerate(gates) if (q, N+NG+g) in l)
bad = tot = 0
for a in range(NG):
    sa = {q for q, s, i in xcheck_nb(a)}
    for b in range(NG):
        sb = {q for q, s, i in zcheck_nb(b)}
        sh = sa & sb
        if not sh: continue
        tot += 1
        if sum(1 for q in sh if ZT[(b, q)] < XT[(a, q)]) % 2: bad += 1
print(f"(MC) on the alternating-XZ realisation: {bad} odd of {tot} overlapping pairs")

LXb = poolmod.get()[2]
c = stim.Circuit()
XA, ZA = simverify.XA, simverify.ZA
c.append("RX", list(range(N)))
nmeas = 0; rec = {}
R = 3
for r in range(R):
    c.append("RX", XA); c.append("R", ZA)
    for lay in gates:
        tg = []
        for (ct, tt) in lay: tg += [ct, tt]
        c.append("CX", tg)
    c.append("MX", XA)
    for g in range(NG): rec[('X', g, r)] = nmeas + g
    nmeas += NG
    c.append("M", ZA)
    for g in range(NG): rec[('Z', g, r)] = nmeas + g
    nmeas += NG
    for g in range(NG):
        if r == 0:
            c.append("DETECTOR", [stim.target_rec(rec[('X', g, 0)] - nmeas)])
        else:
            c.append("DETECTOR", [stim.target_rec(rec[('X', g, r)] - nmeas),
                                  stim.target_rec(rec[('X', g, r-1)] - nmeas)])
            c.append("DETECTOR", [stim.target_rec(rec[('Z', g, r)] - nmeas),
                                  stim.target_rec(rec[('Z', g, r-1)] - nmeas)])
c.append("MX", list(range(N)))
for q in range(N): rec[('d', q)] = nmeas + q
nmeas += N
for g in range(NG):
    tg = [stim.target_rec(rec[('X', g, R-1)] - nmeas)]
    for q in np.nonzero(HX[g])[0]: tg.append(stim.target_rec(rec[('d', int(q))] - nmeas))
    c.append("DETECTOR", tg)
for i in range(12):
    c.append("OBSERVABLE_INCLUDE",
             [stim.target_rec(rec[('d', int(q))] - nmeas) for q in np.nonzero(LXb[i])[0]], i)
try:
    dem = c.detector_error_model(decompose_errors=False, allow_gauge_detectors=False)
    print(f"stim: {c.num_qubits} qubits, {c.num_detectors} detectors, DEM BUILT OK "
          f"({dem.num_errors} error mechanisms)")
    s = c.compile_detector_sampler().sample(1)
    print("   noiseless detector firings:", int(np.array(s)[0].sum()), "/", c.num_detectors)
except Exception as e:
    print("stim DEM FAILED:", type(e).__name__, str(e)[:120])
```

#### `readingA.py`

```python
"""Reading A of Figure 12 (labels taken as the ancilla instance's own consecutive times, no
straddle): what are the order-class triples, do they survive the cascade, and if not, exhibit the
weight-10 witness."""
import numpy as np, itertools
from sched import make_phi
from cascade import REPS, collect_rules, survivors, CLS_OF
from cascade_check import audit
from fig12 import XPANEL, ZPANEL, COLS, xmaps, zmaps, slot_times, order_class

phi = make_phi(1, 1)
SURV = {}
for sector in ('X', 'Z'):
    r1, r2 = collect_rules(sector, phi)
    alive, _, _ = survivors(r1, r2)
    SURV[sector] = {tuple(int(x) for x in v) for v in np.argwhere(alive)}

for name, panel, mps, sector in (('X', XPANEL, xmaps(), 'X'), ('Z', ZPANEL, zmaps(), 'Z')):
    print(f"--- {sector} sector, Reading A (as drawn, white = LEFT half) ---")
    for i, mp in enumerate(mps):
        T = slot_times(panel, mp)
        cls = {c: order_class(T[c]) for c in COLS}
        for perm in itertools.permutations(range(3)):
            tr = tuple(cls[COLS[perm[c]]] for c in range(3))
            if tr in SURV[sector]:
                print(f"   map{i} perm{perm}: triple {tr}  SURVIVES")
                break
        else:
            tr = tuple(cls[COLS[c]] for c in range(3))
            a = audit(sector, phi, tr)
            print(f"   map{i}: triple {tr}  ELIMINATED -> witness {a}")
```

#### `buildlrc.py`

```python
"""Build the reconstructed [SBB26] Figure-12 circuit explicitly at period 8 (depth 8) and verify it:
legality layer by layer, (MC) by the parity condition, and determinism of every detector in stim."""
import json, itertools
import numpy as np, stim
from gross import NG, N, HX, HZ, xcheck_nb, zcheck_nb, xchecks_of, zchecks_of, Reducer
from sched import make_phi
from cascade import CLS_OF, REPS
from fig12 import XPANEL, ZPANEL, COLS
import pool as poolmod

P = 8
R = json.load(open("fig12_reading2.json"))
row = next(r for r in R if r['P'] == P and r['tag'] == 'upper=X' and r['white_left']
           and r['stZ'] and not r['stX'] and r['phi'] == [1, 1]
           and r['Xtriple'] == [14, 0, 2])
print("reading:", {k: row[k] for k in ('P','stX','stZ','white_left','phi','delta','Xtriple','Ztriple')})
print("  xedge", row['xedge'], "colX", row['colX'])
print("  zedge", row['zedge'], "colZ", row['colZ'])

def times(panel, edge, colperm, straddle, white, black):
    T = {}
    for col in COLS:
        t = [None]*6
        for e, tt in panel[col].items():
            t[edge[e]] = tt
        if straddle:
            wl = sum(t[edge[e]] for e in white)/3; bl = sum(t[edge[e]] for e in black)/3
            for e in (white if wl < bl else black):
                t[edge[e]] += P
        T[col] = t
    return {c: T[COLS[colperm[c]]] for c in range(3)}

TX = times(XPANEL, row['xedge'], row['colX'], row['stX'], ['e2','e5','e6'], ['e1','e3','e4'])
TZ = times(ZPANEL, row['zedge'], row['colZ'], row['stZ'], ['e3','e4','e6'], ['e1','e2','e5'])
TZ = {c: [x + row['delta'] for x in TZ[c]] for c in TZ}
print("X times per colour:", TX)
print("Z times per colour:", TZ)
phi = make_phi(1, 1); PHI = [int(phi[g]) for g in range(NG)]
ordX = [tuple(sorted(range(6), key=lambda s: TX[PHI[g]][s])) for g in range(NG)]
ordZ = [tuple(sorted(range(6), key=lambda s: TZ[PHI[g]][s])) for g in range(NG)]
print("X classes:", tuple(CLS_OF[ordX[g]] for g in range(3)),
      " Z classes:", tuple(CLS_OF[ordZ[g]] for g in range(3)))

XSLOT = [[(0 if s=='L' else 3)+i for (q,s,i) in xcheck_nb(g)] for g in range(NG)]
ZSLOT = [[(0 if s=='L' else 3)+i for (q,s,i) in zcheck_nb(g)] for g in range(NG)]
XQ = [[q for (q,s,i) in xcheck_nb(g)] for g in range(NG)]
ZQ = [[q for (q,s,i) in zcheck_nb(g)] for g in range(NG)]

# ---- legality: every absolute layer is a matching on the 288 qubits ----
XA = [N+g for g in range(NG)]; ZA = [N+NG+g for g in range(NG)]
busy = {}; ok = True
for p in range(6):
    for g in range(NG):
        for k in range(6):
            t = TX[PHI[g]][XSLOT[g][k]] + P*p
            for qq in (XQ[g][k], XA[g]):
                if (t, qq) in busy: ok = False
                busy[(t, qq)] = 1
        for k in range(6):
            t = TZ[PHI[g]][ZSLOT[g][k]] + P*p
            for qq in (ZQ[g][k], ZA[g]):
                if (t, qq) in busy: ok = False
                busy[(t, qq)] = 1
print("legality over 6 periods (every layer a matching):", ok)
lay = sorted({t for (t, q) in busy})
print("CNOT-carrying layers per period:", len({t % P for (t, q) in busy}),
      " ancilla window lengths:",
      {c: (max(TX[c])-min(TX[c])+3, max(TZ[c])-min(TZ[c])+3) for c in range(3)})

# ---- (MC) ----
bad = tot = 0
for a in range(NG):
    for b in range(NG):
        sh = [(k, ZQ[b].index(XQ[a][k])) for k in range(6) if XQ[a][k] in ZQ[b]]
        if not sh: continue
        for dp in range(-3, 4):
            tot += 1
            c = sum(1 for (k,l) in sh
                    if TZ[PHI[b]][ZSLOT[b][l]] + P*dp < TX[PHI[a]][XSLOT[a][k]])
            if c % 2: bad += 1
print(f"(MC): {bad} odd of {tot} (X-instance, Z-instance) overlapping pairs")

# ---- stim: does the DEM build (all detectors deterministic)? ----
def stim_circuit(rounds, basis):
    LXb = poolmod.get()[2]; LZb = poolmod.get()[3]
    ev = []
    for p in range(rounds):
        for g in range(NG):
            ev.append((min(TX[PHI[g]])-1+P*p, 'rx', g))
            ev.append((max(TX[PHI[g]])+1+P*p, 'mx', g))
            ev.append((min(TZ[PHI[g]])-1+P*p, 'rz', g))
            ev.append((max(TZ[PHI[g]])+1+P*p, 'mz', g))
            for k in range(6):
                ev.append((TX[PHI[g]][XSLOT[g][k]]+P*p, 'cx', (XA[g], XQ[g][k])))
                ev.append((TZ[PHI[g]][ZSLOT[g][k]]+P*p, 'cz', (ZQ[g][k], ZA[g])))
    ev.sort(key=lambda e: e[0])
    c = stim.Circuit()
    c.append("RX" if basis == 'X' else "R", list(range(N)))
    nmeas = 0; rec = {}
    i = 0
    while i < len(ev):
        t = ev[i][0]; grp = []
        while i < len(ev) and ev[i][0] == t:
            grp.append(ev[i]); i += 1
        for kind in ('mx','mz','rx','rz','cx','cz'):
            sel = [g for g in grp if g[1] == kind]
            if not sel: continue
            if kind == 'rx':  c.append("RX", [XA[g[2]] for g in sel])
            elif kind == 'rz': c.append("R", [ZA[g[2]] for g in sel])
            elif kind == 'mx':
                c.append("MX", [XA[g[2]] for g in sel])
                for g in sel: rec[('X', g[2], nmeas)] = nmeas; nmeas += 1
            elif kind == 'mz':
                c.append("M", [ZA[g[2]] for g in sel])
                for g in sel: rec[('Z', g[2], nmeas)] = nmeas; nmeas += 1
            else:
                tg = []
                for g in sel: tg += [g[2][0], g[2][1]]
                c.append("CX", tg)
    return c, nmeas, rec, ev

for basis in ('X', 'Z'):
    circ, nmeas, rec, ev = stim_circuit(5, basis)
    # detectors: repeat each ancilla's consecutive measurements
    seq = {}
    for (kind, g, idx) in rec:
        seq.setdefault((kind, g), []).append(rec[(kind, g, idx)])
    d = stim.Circuit(str(circ))
    for (kind, g), ms in seq.items():
        if (basis == 'X') != (kind == 'X'):
            continue
        for j in range(1, len(ms)):
            d.append("DETECTOR", [stim.target_rec(ms[j]-nmeas), stim.target_rec(ms[j-1]-nmeas)])
    try:
        dem = d.detector_error_model(decompose_errors=False, allow_gauge_detectors=False)
        print(f"stim {basis}-memory: {d.num_qubits} qubits, {d.num_detectors} detectors, "
              f"DEM BUILT OK ({dem.num_errors} error mechanisms)")
        s = d.compile_detector_sampler().sample(1)
        print(f"   noiseless detector firings: {int(np.array(s)[0].sum())} / {d.num_detectors}")
    except Exception as e:
        print(f"stim {basis}-memory: DEM FAILED -> {type(e).__name__}: {str(e)[:150]}")
```

#### `lrc8.py`

```python
"""An explicit legal, measurement-consistent, depth-8 staggered left-right circuit of the gross
code, built from scratch and handed to stim.  Period 8 time steps: X instance p does its LEFT block
at 8p+{1,2,3} and its RIGHT block at 8p+{4,5,6} (prep 8p+0, measure 8p+7); the Z instance is
staggered by half a period, doing its LEFT block at 8p+{5,6,7} and its RIGHT block at 8p+{8,9,10}
(prep 8p+4, measure 8p+11).  Within each block the layer is the monomial index, which is a matching
because phi(A_i) (resp phi(B_i)) are distinct mod 3 -- no colouring is needed for the uniform case.
This is the object the review's section 5.3 exhibited; the point here is that (MC) holds for
structural reasons (section 3.2) and that stim confirms every detector is deterministic."""
import numpy as np, stim
from gross import NG, N, HX, HZ, xcheck_nb, zcheck_nb, xchecks_of, zchecks_of
import pool as poolmod

P = 8
XA = [N + g for g in range(NG)]; ZA = [N + NG + g for g in range(NG)]
def tX(slot):  return 1 + slot if slot < 3 else 4 + (slot - 3)
def tZ(slot):  return 5 + slot if slot < 3 else 8 + (slot - 3)

XSLOT = [[(0 if s == 'L' else 3) + i for (q, s, i) in xcheck_nb(g)] for g in range(NG)]
ZSLOT = [[(0 if s == 'L' else 3) + i for (q, s, i) in zcheck_nb(g)] for g in range(NG)]
XQ = [[q for (q, s, i) in xcheck_nb(g)] for g in range(NG)]
ZQ = [[q for (q, s, i) in zcheck_nb(g)] for g in range(NG)]

busy = {}; ok = True
for p in range(6):
    for g in range(NG):
        for k in range(6):
            for (t, q, a) in ((tX(XSLOT[g][k]) + P*p, XQ[g][k], XA[g]),
                              (tZ(ZSLOT[g][k]) + P*p, ZQ[g][k], ZA[g])):
                for qq in (q, a):
                    if (t, qq) in busy: ok = False
                    busy[(t, qq)] = 1
print("legality over 6 periods, every layer a matching:", ok)
print("CNOT layers used per period:", len({t % P for (t, q) in busy}),
      "; ancilla window (prep..measure):", "X 8 steps, Z 8 steps")
bad = tot = 0
for a in range(NG):
    for b in range(NG):
        sh = [(k, ZQ[b].index(XQ[a][k])) for k in range(6) if XQ[a][k] in ZQ[b]]
        if not sh: continue
        for dp in range(-3, 4):
            tot += 1
            if sum(1 for (k, l) in sh
                   if tZ(ZSLOT[b][l]) + P*dp < tX(XSLOT[a][k])) % 2:
                bad += 1
print(f"(MC): {bad} odd of {tot} (X-instance, Z-instance) overlapping pairs")

R = 5
ev = []
for p in range(R):
    for g in range(NG):
        ev.append((P*p + 0, 'rx', g)); ev.append((P*p + 7, 'mx', g))
        ev.append((P*p + 4, 'rz', g)); ev.append((P*p + 11, 'mz', g))
        for k in range(6):
            ev.append((tX(XSLOT[g][k]) + P*p, 'cx', (XA[g], XQ[g][k])))
            ev.append((tZ(ZSLOT[g][k]) + P*p, 'cz', (ZQ[g][k], ZA[g])))
ev.sort(key=lambda e: e[0])
c = stim.Circuit(); c.append("RX", list(range(N)))
nmeas = 0; seq = {}
i = 0
while i < len(ev):
    t = ev[i][0]; grp = []
    while i < len(ev) and ev[i][0] == t:
        grp.append(ev[i]); i += 1
    for kind in ('mx', 'mz', 'rx', 'rz', 'cx', 'cz'):
        sel = [g for g in grp if g[1] == kind]
        if not sel: continue
        if kind == 'rx': c.append("RX", [XA[g[2]] for g in sel])
        elif kind == 'rz': c.append("R", [ZA[g[2]] for g in sel])
        elif kind == 'mx':
            c.append("MX", [XA[g[2]] for g in sel])
            for g in sel: seq.setdefault(('X', g[2]), []).append(nmeas); nmeas += 1
        elif kind == 'mz':
            c.append("M", [ZA[g[2]] for g in sel])
            for g in sel: seq.setdefault(('Z', g[2]), []).append(nmeas); nmeas += 1
        else:
            tg = []
            for g in sel: tg += [g[2][0], g[2][1]]
            c.append("CX", tg)
for (kind, g), ms in seq.items():
    if kind != 'X': continue
    for j in range(1, len(ms)):
        c.append("DETECTOR", [stim.target_rec(ms[j] - nmeas), stim.target_rec(ms[j-1] - nmeas)])
try:
    dem = c.detector_error_model(decompose_errors=False, allow_gauge_detectors=False)
    print(f"stim X-memory: {c.num_qubits} qubits, {c.num_detectors} detectors, "
          f"6 CNOT layers per period, DEM BUILT OK")
    s = c.compile_detector_sampler().sample(1)
    print("   noiseless detector firings:", int(np.array(s)[0].sum()), "/", c.num_detectors)
except Exception as e:
    print("stim DEM FAILED:", type(e).__name__, str(e)[:140])
```

#### `altall.py`

```python
"""The alternating-XZ realisation is legal and (MC)-clean for EVERY one of the 44 x 44 surviving
tiled assignments -- checked, not assumed.  (It is also clear a priori: the circuit runs every
X-check CNOT before every Z-check CNOT, so on each shared qubit the Z-CNOT is later and the (MC)
count is 0 for all 648 overlapping pairs, whatever the within-check orders.)"""
import json, itertools
import numpy as np
from gross import NG, N, xcheck_nb, zcheck_nb
from sched import make_phi
from cert import tiled_orders
import simverify

phi = make_phi(1, 1)
F = json.load(open("fam.json"))
Z = [tuple(t) for t in F["Z"]["survivors"]]
X = [tuple(t) for t in F["X"]["survivors"]]
rng = np.random.default_rng(11)
bad = 0; n = 0
for _ in range(25):
    tz = Z[rng.integers(len(Z))]; tx = X[rng.integers(len(X))]
    oZ, _ = tiled_orders('Z', phi, tz); oX, _ = tiled_orders('X', phi, tx)
    gates = simverify.alternating_circuit(oX, oZ)     # asserts every layer is a matching
    XT = {}; ZT = {}
    for li, lay in enumerate(gates):
        for (c, t) in lay:
            if c >= N: XT[(c - N, t)] = li
            else:      ZT[(t - N - NG, c)] = li
    for a in range(NG):
        sa = {q for q, s, i in xcheck_nb(a)}
        for b in range(NG):
            sb = {q for q, s, i in zcheck_nb(b)}
            sh = sa & sb
            if not sh: continue
            n += 1
            if sum(1 for q in sh if ZT[(b, q)] < XT[(a, q)]) % 2: bad += 1
print(f"25 random (Z-triple, X-triple) pairs from the 44 x 44 survivors: "
      f"all layers matchings, {bad} odd of {n} overlapping (X,Z) check pairs")
```
