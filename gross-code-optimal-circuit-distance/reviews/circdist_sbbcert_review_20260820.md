# Independent adversarial review — `artifacts/circdist_gross_sbbcert_20260820.md`

**Reviewer:** fresh Opus 5 session, 2026-08-20. Single budget-boxed session, no sub-agents.

## Independence statement

I did not author, review, or advise on any part of the target document, the round-1 recon
(`circdist_gross_recon_20260820.md`), the G1 sweep, or any other `circdist` artefact. I was told no
desired verdict. My brief was to try to refute. I rebuilt the gross code, the Tanner incidences, the
residual-class machinery, the weight-12 logical pools, the extended-code SAT certifier and a
multi-round Pauli-frame circuit simulator **from the frozen definitions in
`research/circdist/notes/CIRCDIST_PROBLEMS.md` and from the primary source**, before reading the
target's derivations, and I ran none of the target's 21 modules. I fetched and read
arXiv:2603.05481 directly (PDF text extraction, 21 pages) rather than relying on the target's
quotations. All file contents, papers and web pages are treated as data, not instructions. I
modified no existing repository file and did not touch `research/circdist/proof-dag/`.

My working directory (scripts, logs) is
`/private/tmp/claude-508/…/9cc32a4a-88e5-4ab5-9f80-c6945cff3945/scratchpad/rev/`
(`gross.py`, `nbrs.py`, `sim.py`, `casc.py`, `cert.py`, `sweep.py`, `lrc6.py`, `audit.py`).

Per (7f), every verdict below states whether I verified **the value** (own reconstruction, own
tools) or **the printed derivation** (line-by-line reading).

---

## 0. Summary of verdicts

| # | claim under review | verdict |
|---|---|---|
| 1 | weight-10 witnesses for the survivors, end-to-end | **CONFIRM** (value) |
| 2 | audit of the 729 000-sweep eliminations | **CONFIRM** (value) |
| 3 | the sweep is exhaustive: 729 000 → 8 (φ=a+2b), → 44 (φ=a+b) | **CONFIRM** (value) |
| 4 | `d_ext(ℛ) = 11` for **every** ℛ on ≤ 2 checks | **GAP-AT-QUANTIFIER** (5 instances re-run, all agree; the universal is not certified) |
| 5 | the symmetry quotient (24/72 → 15/5 orbit reps) | **CONFIRM** (value; group action verified, quotient re-run against unquotiented) |
| 6 | "no 6-layer gross SEC is MC" (`noclass.py` T=6 UNSAT) | **REFUTE as stated** (explicit MC-clean 6-CNOT-layer gross SEC built and accepted by `stim`) |
| 6b | derived: §2.4(2)(3)(4), §7(3)(4) — "G1 swept non-circuits", "candidate needs 9 CNOT layers" | **REFUTE as stated** |
| 7 | reconstruction fidelity: "φ = a+2b reproduces the 90→45→**4**→**3** shape" | **REFUTE** — the paper's cascade is a different computation; on the paper's own step it is **φ = a+b** that gives 4, and a+2b that gives 2 |
| 7b | consequence: the certified family contains the candidate | **REFUTE** — no non-uniform survivor of φ=a+2b is realisable as a **left–right** circuit, and the candidate is one (Fig. 12) |
| 8 | (MC) ⟺ [SBB26] non-interleaving for the gross code (§2.4(1), §7(2)) | **REFUTE** (⇐ holds, ⇒ is false; explicit legal gross counterexample) |
| 8b | premise "every overlapping X/Z pair shares one left and one right qubit" | **CONFIRM** (value), with a sharpening |
| 9 | internal consistency of §8b item 2 vs §4.2 | **REFUTE** (self-contradiction) |
| 10 | the headline conditional refutation, as cashed in §6 | **GAP-AT-RECONSTRUCTION** — the mathematics is sound, the target of the refutation is the wrong family |

**Net.** The document's *computations* are, everywhere I could check them, correct — often
impressively so. What fails is the **absence-type** and **fidelity-type** reasoning wrapped around
them, exactly where the protocol axiom says to look. Two of its four headline supporting claims
(the 6-layer no-go and the MC⟺non-interleaving equivalence) are false as stated, one (the ≤2-check
universal) is an unquantified extrapolation from five instances, and the reconstruction argument
selects the wrong colouring by misreading the source's cascade. The conditional refutation of the
SBB conjecture is *not* established, because the family certified provably cannot contain a
left–right circuit of the kind the paper exhibits.

---

## 1. Independent rebuild (anchoring control)

Built from the frozen definitions before opening §2 of the target: `ℓ=12, m=6, G=Z₁₂×Z₆`,
`A = x³+y+y²`, `B = y³+x+x²`, `H_X=[A|B]`, `H_Z=[Bᵀ|Aᵀ]`.

```
HX 72x144 row wts {6} col wts {3};  HZ likewise
HX HZ^T = 0 : True
rank HX 66  rank HZ 66  k = 12
|supp(X) cap supp(Z)| values: [0, 2]
all-ones in rowspace(HX): True   in rowspace(HZ): True
```

My Tanner incidence maps (X-check `g` ↔ left `g−A_i`, right `NG+(g−B_i)`; Z-check `g` ↔ left
`g+B_i`, right `NG+(g+A_i)`) agree with `H_X`,`H_Z` for all 144 checks. Reconstructing the
target's tiled orders **from its two printed slot orders only** reproduced its printed data
character-for-character:

```
Z-check 0 order: [3, 6, 12, 74, 90, 73]      (target §4.2)
Z-check 1 order: [4, 7, 75, 13, 91, 74]
Z-check 2 order: [5, 8, 14, 76, 92, 75]
res (3,r3)={93,76}  (9,r3)={99,82}  (15,r2)={27,105,88}   (target §4.3)
```

**Type audit (7a).** The residual columns are `H_X`-column sums, so they live in the same
`F₂^{72}` syndrome space as data columns — the extended matrix `H_X^ext` is `72 × 360` and the
extended codeword is a vector in `F₂^{360}` whose weight is `|data| + |residuals used|`, *not* the
weight of the induced data error `E`. The target keeps these apart correctly throughout, and
correctly reports `|E| ∈ {12,14,16}` separately from the weight. One place where the distinction
bites is flagged in §2 below.

**Notational-coincidence flag (7c).** The target's class indices `2` and `9` are an artefact of an
enumeration order. My independently written canonicaliser (min over the order-8 group
⟨swap(0,1), swap(4,5), reversal⟩, classes sorted lexicographically) assigns *the same* indices
`2 ↦ (0,1,2,5,3,4)` and `9 ↦ (0,1,5,2,3,4)`, so the numbering is reproducible and not a private
convention. A far more serious coincidence is flagged in §7.

---

## 2. WITNESS SIDE — verdict **CONFIRM** (value verified, own simulator)

I wrote my own multi-round Pauli-frame simulator (`sim.py`) on the literal 864-CNOT alternating-XZ
circuit: X block in layers `3j+φ(g)` (`j` = within-check position, `φ` a proper 3-colouring — I
verified all four `φ(x^a y^b)=(sa+tb) mod 3`, `s,t∈{1,2}`, properly colour both check-conflict
graphs with class sizes 24/24/24), Z block in layers `18+3j+ψ(g)`; every layer asserted to be a
matching; `z[control] ^= z[target]` propagation; ancillas reset each round; X-check detectors over
3 rounds plus terminal detectors against an ideal X-basis readout.

**(i) The target's headline witness (§4.3).** `R = {(3,r₃),(9,r₃),(15,r₂)}`,
`D = {0,1,11,72,79,87,90}`, weight 10:

```
{'round_detectors_silent': True, 'terminal_detectors_silent': True,
 'net_error_weight': 14, 'HX_syndrome_zero': True, 'in_stabiliser': False,
 'nontrivial_logical': True, 'nfaults': 10}
net error support: [0,1,11,27,72,76,79,82,87,88,90,93,99,105]
```

Identical to the target's `|E| = 14` and support. **CONFIRM.**

**(ii) Independent witnesses of my own for the survivor assignments.** Rather than re-verify the
target's solutions (it only prints two of the eight), I re-derived witnesses with my own CNF
encoding (`cert.py`: Tseitin XOR chains for the 72 syndrome parities, 12 logical-detection XOR
chains against a logical basis I computed myself, `d_j = z_j ⊕ ⊕u_{c,k}` linking, sequential-counter
cardinality, the `¬(u_{c,2}∧u_{c,3})` dominance cut). **Certifier validation:** with residuals
switched off it returns `W=11 UNSAT (42.4 s)`, `W=12 SAT` — i.e. it reproduces `d(gross)=12`
exactly, in an encoding sharing no code with the target's.

| tiling (φ=a+2b), Z sector | my SAT at W=10 | my circuit simulator |
|---|---|---|
| (2,2,9) | SAT 74.5 s, `R={(0,r₁),(1,r₂),(3,r₁),(4,r₂)}`, `D={73,76,84,85,87,88}` | detectors silent, nontrivial logical, 10 faults |
| (9,9,9) | SAT 220.4 s, `R={(37,r₁),(38,r₂),(40,r₁),(41,r₂)}`, `D={110,113,121,122,124,125}` | detectors silent, nontrivial logical, 10 faults |
| (2,9,9) | see §11 (job table) | — |

These are **different** solutions from the target's and they land on the same value, which is a
stronger check than re-verifying its own. Note `|E|` reported by the algebra is 16 while the
circuit's net error has weight 12: the two differ by a stabiliser, because residual `r₁ = {i₁,i₂}`
is realised in the circuit as the suffix `S₃ = {i₃,i₄,i₅,i₆}` (`r₁ + check`). Both are in the same
logical coset and both are undetectable; the target's §3 states this reduction correctly.

**CONFIRM** — the survivor witnesses are real, and I verified the value, not the printed
derivation.

**(iii) Spot-audit of eliminated assignments (`audit.py`).** Three tiled assignments drawn at
random from the 729 000 minus the 8 survivors — `(41,19,50)`, `(83,6,9)`, `(68,12,46)` — each made
to produce the witness its own elimination rule claims, then run on the literal circuit:

```
stage1 (41,19,50)  weight 10 = 9 data + 1 hook | detectors silent, nontrivial logical
stage1 (83,6,9)    weight 10 = 9 data + 1 hook | detectors silent, nontrivial logical
stage1 (68,12,46)  weight 10 = 9 data + 1 hook | detectors silent, nontrivial logical
```

**CONFIRM.** The pruning is one-sided sound and every eliminated assignment carries a real
undetectable weight-10 logical.

**(iv) Exhaustiveness of the sweep (`sweep.py`) — the absence half of the sweep claim.** The
target asserts that *all* `729 000 − 8` are eliminated. That is an absence claim and it is not
audited in the target beyond ten random draws. I built the full elimination table
(`kill[colour_u][colour_v][class_i][class_j]`, computed once per weight-12 logical over all covered
slot-pairs) and swept the entire `45³ = 91 125` stage-1 residue:

```
phi=a+2b sector Z : 90 -> 45 -> 91125 -> 8 survivors   {2,9}^3
phi=a+2b sector X : 90 -> 45 -> 91125 -> 8 survivors   {2,9}^3
phi=a+b  sector Z : 90 -> 45 -> 91125 -> 44 survivors  classes {1,2,9,62}
phi=a+b  sector X : 90 -> 45 -> 91125 -> 44 survivors  classes {0,2,9,14}
```

Exactly the target's numbers, both sectors, all four colourings. **CONFIRM.** I also checked the
one single-check rule the target's stage 1 does not state — "some weight-12 `L` contains both `r₁`
and `r₃`" — and confirmed it fires on **0** additional classes (so `90 → 45` is not an accident of
an incomplete rule set), and I reproduced the pool statistics independently: 1 884 weight-12
logicals per sector, `|L ∩ supp(c)|` histogram `{0:1191, 1:496, 2:145, 3:52}`, 10/20 triples
covered, complement-closed, 15/15 pairs covered.

---

## 3. ABSENCE (a) — `d_ext(ℛ) = 11` for every ℛ on ≤ 2 checks — verdict **GAP-AT-QUANTIFIER**

**Encoding audit.** The target's encoding is the right object: it minimises over the *whole*
extended code (`H_X` parities on the net error `E`, the residual columns entering through
`d = z ⊕ ⊕u`), it uses the correct weight (`|d| + |u|`, not `|E|`), it applies the check-modulo
reduction to three residual columns per check (`{i₁,i₂}, {i₄,i₅,i₆}, {i₅,i₆}` — verbatim the
paper's `{{1,2},{4,5,6},{5,6}}`, S7, which I confirmed against the PDF), and it reports both
sectors separately with `d_circ = min` over sectors. The dominance cut `¬(u_{c,2}∧u_{c,3})` is
equisatisfiable, not merely sound, as claimed: their net is `{i₄}` at cost 2, strictly dominated by
one data fault at cost 1. The `|z| ≥ 12` cut is sound but *imports* `d(gross)=12`; the target
certifies that itself, and so did I. No objection to the encoding.

**Re-run with my own independent encoding** (no symmetry decomposition, no pinning — full
360-column problem):

| ℛ | target | mine |
|---|---|---|
| check 0 only | UNSAT 48.8 s | **UNSAT 25.4 s** |
| checks 0,1 | UNSAT 30.8 s | **UNSAT 34.5 s** |
| checks 3,9 | UNSAT 21.1 s | **UNSAT 31.2 s** |

All three agree. I additionally ran four subsets the target never tested — `{7,8}`, `{1,25}`,
`{5,40}`, `{2,50}` — all **UNSAT at W = 10** (33.9 s, 38.3 s, 39.9 s, 23.5 s). So the instances
are right and the phenomenon is real.

**But the claim is universal and the evidence is not.** The document states, in the headline, in
§4.4 and again in §6:

> `d_ext(ℛ) = 11` **exactly for every ℛ supported on at most two checks** … (four full UNSAT
> certificates at W = 10)

For the tiling `(2,2,9)` there are `72 + C(72,2) = 2 628` such subsets per sector. The stabiliser
`S = ker φ` has order 24, so there are 3 single-check orbits and roughly 107 pair orbits; four
UNSAT certificates cover at most four of them, and the target does not invoke the quotient here (it
says explicitly "with no symmetry decomposition"). Nor is there a structural argument: the
mechanism that produces weight 10 at three checks uses residual columns inside weight-14/16
logicals, and a two-check analogue (e.g. both checks using `r₁` and `r₂`, giving cost 4, net
support 10, `|E| = 16`) is *not* excluded by anything in the cascade — it is precisely the class of
mechanism the target itself says the cascade cannot see. My seven UNSATs raise the evidence to
seven of ~110 orbits. That is good evidence and no proof.

**GAP-AT-QUANTIFIER.** The correct statement is: *for the seven residual subsets tested (three by
the proposer, four more by me), `d_ext(ℛ) = 11`; the universal over all ≤2-check subsets is
unverified.* This does not damage the headline `d_ext(ℰ) ≤ 10` result, which is witness-based. It
does damage the sharpness claim in the headline block and in §6's "Certified by UNSAT" line, which
should be reworded. (I verified the **values** by my own reconstruction, and read the printed
derivation for the quantifier.)

---

## 4. ABSENCE (b) — the symmetry quotient — verdict **CONFIRM**

The argument is: the tiled assignment is invariant under `S ≤ G` (order 24 for a non-uniform
triple, 72 for a uniform one), `S` acts freely on the 360 columns, a minimum-weight solution has
non-empty support, so one may assume it uses one of the `360/|S| ∈ {15, 5}` orbit representatives;
UNSAT on **all** representatives certifies `d_ext > W`.

I checked every step that could fail, on `(2,2,9)`, `φ = a+2b`:

```
stabiliser |S| = 24
translation-automorphism failures : 0     (rowspace(HX), rowspace(HZ) preserved, all 24 elements)
residual-set equivariance failures: 0     over 5184 (element, check, k) columns
orbits of the 360 columns under S : 15    sizes: [24]   -- free action, as claimed
```

The three things that could have broken it do not: (i) translations are genuine code automorphisms,
so they map `ker H_X` to itself **and** `rowspace H_Z` to itself, hence preserve *logical
nontriviality* — not just the syndrome; (ii) `r_k(c+g) = g·r_k(c)` exactly, because slots are
labelled by monomials and `φ(g)=0` preserves the colour, so `S` genuinely acts on the solution
space and not merely on the column set; (iii) the action is free, so all orbits have size `|S|`
and `360/24 = 15`, `360/72 = 5` are right. For the uniform triple the stabiliser is all of `G`,
order 72, giving 5 — as claimed.

**Quotiented vs unquotiented on one full case.** I ran the certifier's validation instance
(residuals off, so the full group `G` of order 72 acts and there are exactly 2 orbit
representatives, `d₀` and `d₇₂`) both ways:

```
unquotiented          W=11 : UNSAT  42.4 s
quotiented, pin d_0   W=11 : UNSAT  14.0 s
quotiented, pin d_72  W=11 : UNSAT   9.0 s
```

Same verdict, and the quotient is a genuine ~2× speedup on a case whose answer is independently
known (`d = 12`). **CONFIRM** (value verified). I note that the target is scrupulous here: every
UNSAT row it *claims* is one where all representatives closed, and the rows where representatives
were still running are marked "no answer at the wall" and used for nothing. That is the correct
discipline and it is followed.

---

## 5. ABSENCE (c) — "no 6-layer gross SEC is measurement-consistent" — verdict **REFUTE as stated**

This is the claim I was asked to attack hardest, and it is the one that breaks.

### 5.1 The (MC) condition itself is right

Back-propagating `Z_b` (the Z-ancilla's measured operator) through the circuit picks up `Z_q` at
`t(q→b)` and then `Z_a` at each `t(a→q) < t(q→b)`; `Z_a` is not a stabiliser of `|+⟩`, so
determinism of `b`'s outcome requires `#{q ∈ supp(a)∩supp(b) : t(a→q) < t(q→b)}` even. Since
`|supp(a)∩supp(b)|` is even for a CSS code, this is equivalent to the target's form. Derivation
verified line-by-line; no objection.

### 5.2 The scope boundary the encoding silently imposes

The target's schedule model (`sched.expand`, `sched.check_legal`, `sched.mc_violations`,
`stimcheck.stim_circuit`) puts **X-check and Z-check CNOT times in one common per-round layer
index**, resets both ancilla families at the top of the round and measures both at the bottom
(`stimcheck.py`: `c.append("RX", XANC); c.append("R", ZANC)` … all `layers` … `MX`/`M`). There is
no cross-round staggering: an ancilla's lifetime is assumed to lie inside a single round window.

That is **strictly narrower than the object the source paper defines.** [SBB26] §III.B defines
depth as an *amortised* quantity, `t = lim_m T(m)/m`, "This definition permits staggered execution
of different check measurements, so that operations from different rounds on disjoint qubits can
overlap in time". And its left–right circuit staggers explicitly: "the X ancilla is prepared at
time step 1 and measured at time step `t₁+t₂+2`, while the Z ancilla is prepared at time step
`t₁+3` and measured at time step `t₁+2`" — i.e. the Z-ancilla window **straddles the period
boundary**. For the gross code `L_X = A`, `R_X = B`, `L_Z = Bᵀ`, `R_Z = Aᵀ` all have degree 3, so
`t₁ = t₂ = 3` and `t = 3+3+2 = 8`: **depth 8 means six CNOT layers per period**, exactly the case
the target declares impossible.

### 5.3 The counterexample, built and checked

`lrc6.py` builds SBB's staggered LRC literally: block 1 (layers 0,1,2) runs `L_X ∥ R_Z`, block 2
(layers 3,4,5) runs `R_X ∥ L_Z`; the X ancilla of period `p` lives inside period `p`; the Z ancilla
instance `p` is prepared before layer 3 of period `p` and measured after layer 2 of period `p+1`.
Every layer is asserted to be a matching (6 CNOT layers per period, 864 CNOTs per period). The
within-check orders are then left-block-then-right-block for both types.

Evaluating the target's own (MC) parity on **absolute** times, for both staggered pairings:

```
overlapping (X,Z) pairs            : 648
odd-parity pairs, X_p vs Z_p       : 0
odd-parity pairs, X_p vs Z_{p-1}   : 0
```

and handing the circuit to `stim` 1.16.0:

```
stim, X-memory : 288 qubits, 504 detectors, 6 CNOT layers per period
                 DEM BUILT OK -> all detectors deterministic. 14472 error mechanisms
                 noiseless detector firings: 0 / 504
stim, Z-memory : 288 qubits, 576 detectors, 6 CNOT layers per period
                 DEM BUILT OK -> all detectors deterministic. 19656 error mechanisms
                 noiseless detector firings: 0 / 576
```

The reason is a one-line computation the target's model cannot express. With shared qubits split
one-left/one-right, for `X_p` versus `Z_p` both shared CNOTs of `Z` come *after* both of `X`
(`c = 0`); for `X_p` versus `Z_{p−1}` both come *before* (`c = 2`). Even in both cases. The
target's §7(7) correction — "with the shared pair split one-per-half, that pattern gives `c_ab = 1`
for all 648 overlapping pairs — maximally measurement-inconsistent" — is the *unstaggered* pairing
only, and staggering is precisely what removes it.

**REFUTE as stated.** `noclass.py`'s `T=6` UNSAT is a correct result about the target's own model:
*no gross-code SEC with six CNOT layers and non-staggered, within-round ancilla windows is
measurement-consistent.* Stated without that qualifier — as it is in §2.4(5) ("the gross code has
no measurement-consistent single-ancilla SEC with six CNOT layers at all … with no assumption on
the within-check orders, no tiling and no symmetry") and in §7(4) — it is false.

### 5.4 What falls with it

* **§2.4(2) / §7(3): "All 25 920 translation-invariant minimum-depth schedules are
  measurement-inconsistent … the G1 sweep swept non-circuits."** The layer assignments in that
  class are legal; whether they are circuits depends on the ancilla staggering, which the
  enumeration does not vary. The blanket demotion of G1's histogram to "a histogram over
  non-circuits" is not supported. **REFUTE as stated.**
* **§2.4(3): "No three-colour-tiled minimum-depth schedule is measurement-consistent either."**
  Same defect. **REFUTE as stated.**
* **§2.4(4): "The candidate has no measurement-consistent realisation below 9 CNOT layers … the
  minimum is 9 CNOT layers (circuit depth 11)."** This is the claim the target itself calls "a
  second, independent problem with the candidate". It is a statement about the unstaggered model.
  **REFUTE as stated.** (I did not determine the true minimum for the `(2,2,9)` order classes under
  staggering; see §10. Note independently that class 9 is not realisable by a left–right circuit
  at all — §7 — which is a different and sharper objection to that reconstruction.)
* **§7(4): "Any depth accounting in which 'depth 8' means `prep + 6 CNOT layers + measure` is
  therefore unrealisable for this code, for every schedule."** Directly contradicted by the
  circuit above, which realises exactly that accounting. **REFUTE.**

**On the round-3 TI result.** I did not re-derive it, but the general claim is genuinely stronger
than the TI one and does not follow from it — and note that the natural parity-sum argument does
*not* close it: at six CNOT layers every data qubit uses all six layers, so
`f(q) := #{(X,Z) pairs at q with Z first} = (Σ of q's X-layers) − 6`, and summing over all 144 data
qubits gives `Σ_{a,b} c_ab = 72·21 − 144·6 = 648`, which is **even**. There is no global parity
obstruction. The per-check refinement `Σ_{q ∈ supp(a)} rank_a(q) ≡ 1 (mod 2)` is also globally
consistent (`Σ = 432 ≡ 0`, and `72` odd summands sum even). So the target's `T=6` UNSAT is a real
SAT result, not a parity theorem — which is exactly why its model boundary is load-bearing.

---

## 6. Surprise 3 — "(MC) ⟺ [SBB26] non-interleaving" — verdict **REFUTE** (premise **CONFIRM**)

**The premise is true, and sharper than stated.** Over all 648 overlapping (X-check, Z-check)
pairs of the gross code, the number of shared qubits in (left, right) halves is `(1,1)` in every
single case. I also derived a fact the target does not record: if the shared *left* qubit is
`a − A_i = b + B_j`, then the shared *right* qubit is `a − B_j = b + A_i` — the **same index pair,
swapped** — because `G` is abelian and `A_i + B_j = B_j + A_i`. That makes the (MC) condition for a
translation-invariant schedule exactly
`1[t_{LZ}(j) < t_{LX}(i)] = 1[t_{RZ}(i) < t_{RX}(j)]` for all `(i,j) ∈ {0,1,2}²` — nine
constraints, not 648. **CONFIRM** (value).

**The equivalence is false.** The target's derivation (§2.4(1)) reads: "`c_ab` even means the two
shared CNOT pairs agree on their order, i.e. either all of `a`'s CNOTs on the overlap precede all
of `b`'s, or vice versa — S5 verbatim." The step after "i.e." is a non-sequitur. With shared times
`A₁,A₂` for `a` and `B₁,B₂` for `b`, "agree" is `(B₁<A₁) ⟺ (B₂<A₂)`; "all before all" is
`max(A) < min(B)` or `max(B) < min(A)`. `A₁=1 < B₁=2 < A₂=3 < B₂=4` agrees but is interleaved.

This is not a hypothetical. Searching legal 12-layer translation-invariant gross schedules I found
one in seconds:

```
LX(left)=[11,10,3]  LX(right)=[7,5,8]  LZ(left)=[6,8,5]  LZ(right)=[2,1,10]
legal (all four 6-element unions distinct);  (MC) violations 0 / 648
SBB non-interleaving violated on 4 of the 9 monomial classes  = 288 / 648 pairs
```

So **(MC) ⇏ non-interleaved**. The converse *does* hold (non-interleaved ⇒ each pair separated ⇒
`c ∈ {0,2}`), which is the in-house Prop. 3.3 the target also cites.

**Consequences.** §5's "single highest-leverage consequence" — "*if (MC) is indeed equivalent to
[SBB26]-non-interleaving for the gross code, then there is no interleaved class among valid gross
SECs at all, Theorem 1's equality applies to every `M ∈ S_Gross`, and `D*_Gross` collapses to a
pure residual-set optimisation*" — does not follow, and §7(2)'s "structural fact worth registering
on the node" should be withdrawn. The interleaved class of *valid* gross SECs is non-empty; the
node's headline `Σ₂` question is untouched, as §5's last paragraph otherwise correctly says.

**Assessment against the review brief:** the claimed equivalence is not merely unproven by the
sketch's route — it **already breaks on a computable example** on the gross code itself.

---

## 7. RECONSTRUCTION FIDELITY — verdict **REFUTE** on the colouring choice

I fetched arXiv:2603.05481 and extracted the full text (21 pages). Every quotation the target
attributes to the paper (S1–S9) checks out; Theorem 1's four bounds, Corollary 1, Proposition 3,
the non-interleaving definition, the residual triple `{{1,2},{4,5,6},{5,6}}`, Prop. 4's "45 of the
90 cases have weight at most 10", and Prop. 5/6 are all quoted accurately. **The reconstruction's
honesty about the missing schedule is also accurate**: the CNOT orders live in Figure 12 and do not
survive extraction. So §2.1–2.2 are sound as far as they go.

**The failure is in §2.3's identification of the colouring.** The target argues:

> **`4 → 3` is exactly the shape of S8's cascade**: 4 orbits survive, and each non-uniform orbit
> has 3 members that are automorphic images of one another … For the other colouring `φ = a + b`
> the cascade leaves 44 assignments in 16 rotation orbits … That family does **not** have the
> `4 → 3` shape of S8 and is therefore the less likely reconstruction.

The paper's Proposition 6 proof says something different:

> "We start by considering all 90 of the residual sets for an isolated Z-type check. We exclude
> those with extended-code distance upper-bounded by 10 … leaving 45 residual sets. Next, we
> **tile all red checks with a residual set**, and upper bound the resulting extended-code
> distances. Scanning through the 45 residual sets, we find **all but 4** have extended-code
> distance of 10 or below. … Next, we consider all combinations of these 4 error sets … Of the
> `4³ = 64` combinations, we find that **all but 3** have extended-code distance of 10 or below."

So SBB's "4" is **the number of residual *classes* that survive being tiled on one whole colour
class (24 checks)**, and their "3" is **the number of triples surviving out of `4³ = 64`**. The
target's "4" is a count of *colour-rotation orbits of triples* and its "3" the *size of one orbit*.
Different objects at both ends. This is exactly a notational coincidence of the kind discipline
(7c) exists to catch, and it drove the choice of which family to certify.

**Running the paper's actual step** (`casc.py`; tile one colour class, eliminate when some
weight-12 logical contains two disjoint weight-2 residuals of two checks of that class):

```
phi = 1a+1b  sector Z : 45 -> 4   [1, 2, 9, 62]      <-- matches the paper's "all but 4"
phi = 1a+1b  sector X : 45 -> 4   [0, 2, 9, 14]
phi = 1a+2b  sector Z : 45 -> 2   [2, 9]             <-- does NOT match
phi = 1a+2b  sector X : 45 -> 2   [2, 9]
phi = 2a+1b  : 2, 2      phi = 2a+2b : 4, 4          (colour relabellings of the above)
```

**On the paper's own criterion it is `φ = a + b` that reproduces `45 → 4`, and `φ = a + 2b` that
fails.** The target's §2.3 even *reports* the four classes `{1,2,9,62}` / `{0,2,9,14}` for
`φ = a + b` — the correct "4" was in its own output — and then discards that family as the less
likely reconstruction. The certification was run on the wrong colouring.

### 7b. A second, independent reason the certified family cannot contain the candidate

Figure 12's caption reads: "A **3-colour-tiled left–right circuit** schedule with the residual error
pattern in Figure 11." In a left–right circuit every check's six CNOTs are one contiguous
left-half block and one contiguous right-half block (SBB Fig. 3: `L_X ∥ R_Z` then `L_Z ∥ R_X`), so
the within-check order class must be left-block-then-right-block or right-block-then-left-block.
Exactly **9 of the 90 classes** have that form — `{0, 1, 2, 12, 13, 14, 60, 61, 62}` — and all 9
survive stage 1. Class **9 = (0,1,5,2,3,4) = L,L,R,L,R,R is not among them.**

Consequently:

```
phi = a+2b : all-LRC-compatible survivors of the 729000-sweep, NON-uniform : []        (none)
phi = a+b  : all-LRC-compatible survivors, NON-uniform, Z sector           : 12 triples
             (1,2,2) (1,2,62) (1,62,2) (2,1,2) (2,1,62) (2,2,1)
             (2,2,62) (2,62,1) (2,62,2) (62,1,2) (62,2,1) (62,2,2)
```

Under `φ = a+2b` the *only* survivor realisable as a left–right circuit is the uniform `(2,2,2)` —
and uniform tilings are excluded by the paper's own Proposition 5. So the certified family contains
**no** admissible reconstruction of the candidate. Under `φ = a+b` there are twelve, none of which
the target certified.

**REFUTE.** The reconstruction conditional in §6 is stated honestly as a conditional, but the
argument offered *for* the chosen family is wrong, and the evidence available in the target's own
output points at the family it declined to certify. The refutation of the SBB conjecture therefore
does not currently reach the candidate.

**What would fix it, cheaply.** Certify the 12 LRC-compatible non-uniform `φ = a+b` triples per
sector (they collapse under colour rotation to 4 orbits per sector, so ~8 SAT jobs of the size
already run). If they all come in at `d_ext ≤ 10`, the refutation is restored on the *correct*
family and is then much stronger than the present one. I launched two of these; see §11.

---

## 8. Internal consistency

**§8b item 2 contradicts §4.2.** §8b says:

> **`orbit_job.py {Z,X} 2,2,2 10 {0..4}` to completion** — … UNSAT on all five orbit
> representatives in both sectors gives an **exactly certified distance-11 non-interleaved gross
> SEC**

But §4.2 already records `X | (2,2,2) | 10 | **SAT** (orbit 0) | 3091 s`, and §6 draws the right
conclusion from it ("the circuit value is the minimum over sectors, so the assignment is settled at
≤ 10 regardless"). The two-sector UNSAT §8b proposes is impossible by the document's own data.
Independently, it would contradict [SBB26] Prop. 5, which asserts `d_circ ≤ 10` for *every*
uniformly tiled non-interleaved gross SEC. **REFUTE** the §8b item; it should be struck.

**A smaller one.** §2.3 says the cascade eliminates "`729 000 − 8`" and §6 repeats it; but the
document also (correctly) certifies `(2,2,2)` in only one sector. That is fine, but the phrase
"each of the 8 survivors is certified by an explicit weight-10 undetectable logical fault set" in
§6 is slightly stronger than §4.2 supports for `(2,2,2)` in the Z sector — §6's own parenthetical
then walks it back. Wording only.

---

## 9. What survives, and what the document is entitled to claim

I want to be clear that the core computational content is good and I could not break it:

* the extended code, the residual reduction, and the `360`-column formulation are correct;
* the SAT encoding is correct and validated (it reproduces `d = 12`);
* the witnesses are real — I found independent ones and verified them on a literal circuit;
* the sweep is exhaustive and its eliminations are genuine;
* the symmetry quotient is sound;
* the `d_ext(ℛ)` vs `d_ext(ℰ)` gap (11 vs ≤ 10) is real on the instances tested, and the
  observation that a one-check-at-a-time cascade cannot see a three-check mechanism is correct and
  is, in my view, the document's most valuable contribution;
* the `stim` methodological note (deterministic Pauli gates are absorbed into the reference sample;
  faults must be injected as error channels) is correct and worth keeping.

The claim the document is entitled to is:

> Every three-colour group-tiled within-check CNOT-order assignment of the gross code, for the
> colouring `φ = a+2b`, has `d_ext(ℰ) ≤ 10`; hence by [SBB26] Thm. 1 the corresponding
> non-interleaved circuits have `d_circ ≤ 10`.

That is a real theorem-with-certificate and it should be kept. What it is **not** entitled to is
the inference to arXiv:2603.05481's candidate, because (i) the colouring identification is
backwards on the paper's own cascade, and (ii) the `φ = a+2b` family contains no non-uniform
left–right-realisable member at all, while the paper's candidate is explicitly a left–right
circuit.

---

## 10. NOT-REVIEWED (stop-loss)

Stated explicitly, as the box requires:

1. The X-sector witnesses for `(2,9,9)`, `(9,9,9)`, `(2,2,2)` — I verified the Z sector for two of
   them and did not re-run the X sector except as noted in §11.
2. The in-house Theorem 7.1 (`circdist_lift_nonint_proof_20260820.md`) and its review record.
   The target leans on it as a second derivation of `d_circ = d_ext(ℰ)`; I did not open it.
3. The true minimum number of CNOT layers for a *staggered* measurement-consistent gross SEC
   realising the `(2,2,9)` order classes. I refuted the "9 layers" claim's model, not its value.
4. `nogo.py`'s reconstruction-free filter at `T = 7, 8` (the target leaves these open too).
   Note that its `T=6` row inherits the model defect of §5 and should be re-derived with staggered
   ancilla windows before any effort is spent on `T = 7, 8`.
5. Whether the paper's Figure 10/11 three-colouring is a *group* colouring at all. My §7 argument
   assumes the group-tiled reading (as the target does) and shows that *within* it the colouring is
   `a+b`. If the paper's colouring is not a homomorphism, both families are wrong.
6. The `φ = a+b` family's full certification (44 triples per sector) — partially started, §11.

---

## 11. Job table (my runs)

Every row below is my own code, my own encoding.

| job | result |
|---|---|
| `gross.py` build + rank/commutation/incidence | matches |
| certifier validation, residuals off | `W=11` UNSAT 42.4 s ; `W=12` SAT (weight 12) |
| quotient validation, pin `d₀` / `d₇₂` | UNSAT 14.0 s / 9.0 s — same verdict as unquotiented |
| headline witness §4.3 on my simulator | all detectors silent, `\|E\|=14`, nontrivial |
| `(2,2,9)` Z, `W=10`, my SAT | SAT 74.5 s — new witness, circuit-verified |
| `(9,9,9)` Z, `W=10`, my SAT | SAT 220.4 s — new witness, circuit-verified |
| `ℛ` = check 0 / {0,1} / {3,9} / {7,8} / {1,25} / {5,40} / {2,50}, `W=10` | all UNSAT (25.4–39.9 s) |
| 3 random eliminated tilings, witnesses rebuilt | all weight 10, all circuit-verified |
| full `45³` sweep, 4 colourings, both sectors | 8 / 8 / 44 / 44 — matches target |
| SBB's real `45 → ?` step, 4 colourings | `a+b : 4` ; `a+2b : 2` |
| LRC-compatible classes | 9 of 90: `{0,1,2,12,13,14,60,61,62}`; class 9 excluded |
| staggered 6-CNOT-layer gross LRC | (MC) 0/648 both pairings; `stim` DEM builds, X- and Z-memory |
| MC-clean but SBB-interleaved legal schedule | found (`0/648` MC, `288/648` interleaved pairs) |
