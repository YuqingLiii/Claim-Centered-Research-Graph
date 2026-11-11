# CIRCDIST.sat — budget-boxed recon (Opus 5 executor, proposer role), 2026-08-20

Node: `CIRCDIST.sat` (research/circdist/proof-dag/nodes/CIRCDIST.sat.yaml), frontier task-001.
Source problem statement: `research/circdist/notes/CIRCDIST_PROBLEMS.md`, 公共定义 + 课题四.

This is a **recon** artifact. Nothing here is PROVED. Structural claims are labeled
**CONJECTURED** (a reviewable blueprint exists, written out below); computational results are
labeled **NUMERICAL** (reproducible run, stated scope). Route P/D numbers are scheduling
estimates per `research/VALUATION_PROTOCOL.md` §5, not confidence scores.

---

## 0. Executive summary — read this before commissioning further work

Three findings, in decreasing order of how much they should change the lead's plan.

**(F1) The boundary convention in 公共定义 fixes the sign of the monotonicity, and under the
stated convention it is the *unexpected* sign.** `C_R(M)` is specified with a *standard
initialization and a final ideal data readout*. Under that convention a fault-free round can
always be appended (and prepended), so — CONJECTURED, blueprint in §3.4 —

> `d_{R+1}(M) ≤ d_R(M)` for every `R ≥ 1`: **`d_R` is non-increasing in `R`.**

Extra rounds add fault locations without adding any protection, because the ideal spacelike
readout already supplies the terminal syndrome. Consequently

> `R_sat(M) ∈ {1, ∞}` — it is `1` if `d_R = d` for every `R`, and `∞` otherwise.

`R_sat` as literally defined therefore carries one bit, not a number. The substantive quantity is
the **stabilization index** `R_stab(M) := min{ R : d_R(M) = d_∞(M) }`, where
`d_∞ := lim_R d_R = min_R d_R`. §5 recommends re-scoping the node claim onto `R_stab`.

**(F2) The pumping theorem is available with a bound that does not depend on `r` at all.** The
target theorem asks for `B(r,d)` with `r` the cross-round state-space dimension. The
fault-free-round splitting argument (§3.5) gives — CONJECTURED —

> `R_stab(M) ≤ d_∞(M) ≤ d`, i.e. **`B(r,d) = d`**, independent of `r`.

A minimum-weight undetectable logical realized in the fewest rounds must have *at least one fault
in every round*, hence spans at most `d − 1` rounds. So `d_1, …, d_d` determine the entire
sequence `(d_R)_{R≥1}`, and finiteness of `R_sat` is decided by a single check at `R = d`. This is
much stronger than the `(d+2)^{4^r}` pigeonhole bound that the finite-truncated-semiring argument
gives for free (§3.6), and stronger than anything the tropical transient literature can give
(§6, A2: Nowak–Charron-Bost Thm 5.4 shows no bound in the dimension alone exists in general —
our escape is that the min-plus eigenvalue here is exactly `0` and weights are integers capped
at `d`).

**(F3) Empirically `R_stab = 1` in every schedule tested — 7610 legal schedules, three code
families, zero exceptions.** NUMERICAL, §7. If `R_stab = 1` holds in general for single-ancilla
CSS extractors, then `d_R(M) = d_1(M)` for all `R` and the whole `R → d_R` question is vacuous
under the stated conventions. Deciding whether `R_stab ≥ 2` is *possible at all* is the sharpest
open sub-question this recon surfaces, and §4 route `single-round-dominance` is built around it.

The phenomenon the problem statement is evidently reaching for — `d_R` *rising* to `d`, with
`R_sat ≈ d` — is real, but it lives in the setting where the **logical output is timelike** (a
measurement outcome, as in lattice surgery), not spacelike. Beverland–Huang–Kliuchnikov state
exactly this for their `XX`-measurement channel (§6, A5). §5 gives the two-convention split that
would recover the intended question.

---

## 1. Setting, notation, and scope clauses

Fix a CSS code `Q = [[n, k, d]]` with `X`-stabilizer check matrix `H_X` (`m_X` rows) and
`Z`-stabilizer check matrix `H_Z` (`m_Z` rows). Fix a single-round schedule `M` in the class of
公共定义: one ancilla per stabilizer generator, ancilla prepared once and measured once per
round, exactly one CNOT per (check, data qubit in its support), at most one two-qubit gate per
physical qubit per time step. `M` occupies `T` time steps.

`C_R(M)` = ideal logical-`|0⟩` initialization, `R` identical rounds of `M`, ideal final
transversal `Z` readout. `d_R(M) = d_circ(C_R(M))` = minimum number of elementary faults forming
an undetectable configuration that flips a nontrivial logical (Bombín et al. and BHK Def. III.1,
§6 A4/A5).

**Scope clauses used throughout (each is a place a route can fail):**

- **S1 (sector decoupling).** We analyze the `Z`-memory experiment restricted to the
  `X`-error / `Z`-check sector: elementary faults are recorded by their `X`-component only, and
  the logical event is an `X_L` flip. This is the standard CSS splitting (BHK §VII B, §6 A9).
  The `Z` sector is the mirror image. Whether `min` over the two sectors equals the true
  `d_circ` in the presence of `Y` faults is the usual caveat and is *not* re-derived here.
- **S2 (detector window `w = 2`).** Bulk detectors are `D_{g,r} = m_{g,r} ⊕ m_{g,r−1}`. Round-1
  `Z`-check detectors are absolute (`D_{g,1} = m_{g,1}`) because `|0⟩^{⊗n}` is a `+1` eigenstate
  of every `Z`-stabilizer. The final ideal readout supplies `D_{g,R+1}`. Everything in §3
  generalizes to `w > 2` at the cost of `B(r,d) = w·(d+1) + d`; see §3.7.
- **S3 (elementary faults, unit weight).** Each fault location contributes weight 1. Which
  locations exist (idles included or not; prep vs. measurement flips separated or not) is a
  modeling choice; §7 shows the `d = 3` surface-code answer is insensitive to the idle choice.

---

## 2. The single-round dictionary — the only data `M` contributes

**Lemma 2.1 (transparency of a fault-free round).** CONJECTURED. In a single-ancilla CSS
extraction round, a data Pauli `E` present before the round is *unchanged* after the round, and
its only effect is to flip exactly the outcomes of the checks it anticommutes with.

*Blueprint.* For a `Z`-check the data qubit is the CNOT **control** and the ancilla the target:
`X_c ↦ X_c X_t` (the ancilla picks up the error, the data keeps it), `Z_c ↦ Z_c` . For an
`X`-check the ancilla is the control and the data the **target**: `X_t ↦ X_t`, `Z_t ↦ Z_t Z_c`.
In both cases the data component is untouched and the ancilla accumulates exactly the
commutator bit. Ancillas are reset each round, so nothing else crosses the round boundary. ∎

This is the lemma the whole node rests on; it is exactly where a schedule outside the 公共定义
class (flag ancillas, cat states, repeated CNOTs) would break the analysis.

Because the `X` sector is `F_2`-linear, the effect of a round is additive in (incoming error,
round faults). Define, for one round:

- `Δ ∈ F_2^n` — the net residual data-`X` error created by the round's faults;
- `μ ∈ F_2^{m_Z}` — the *extra* `Z`-check outcome flips created by the round's faults
  (i.e. total flip `o_r = H_Z E_{r−1} ⊕ μ_r`).

**Definition 2.2 (single-round fault dictionary).**
`w_M(δ, μ) := min{ |S| : S a set of elementary faults in one round with residual class δ and
extra flips μ }`, where `δ` is taken in `F_2^n / rowspace(H_X)`.

`w_M` is a minimum-weight-coset function: each elementary fault contributes one vector in
`F_2^{r} ⊕ F_2^{m_Z}` with `r := n − rank(H_X)`, and `w_M` is the minimum number of such vectors
summing to the target. It is computed by one BFS over `2^{r + m_Z}` targets, or by a
weight-capped BFS.

---

## 3. Structural results (all CONJECTURED — blueprints given)

### 3.1 The detector constraint collapses to a syndrome-tracking recursion

**Lemma 3.1.** In `C_R(M)` (scope S1–S3), a fault configuration is undetectable **iff**
`o_r = 0` for every `r ∈ {1, …, R}` and `H_Z E_R = 0`; equivalently

> `μ_r = H_Z E_{r−1}` for `r = 1, …, R`,  with `E_0 = 0`,  and `H_Z E_R = 0`,

where `E_r = Δ_1 ⊕ … ⊕ Δ_r`. It is *nontrivial* iff `[E_R] ∉ rowspace(H_X)`.

*Blueprint.* Round-1 absolute detector gives `o_1 = 0`; each differential detector gives
`o_r = o_{r−1}`; induction gives `o_r = 0` for all `r`. The final ideal readout compares the
true terminal syndrome `H_Z E_R` against `o_R = 0`. ∎

The consequence worth flagging: **there is no free timelike gauge.** Both time boundaries pin
`o_r`, so a chain of measurement-outcome flips alone can never be undetectable. Under the stated
convention the timelike measurement mechanism is *structurally excluded* as a sole limiter; it
can only participate in mixed spacetime mechanisms. Contrast §6 A5 (BHK §VIII B), where the
logical output is itself a measurement outcome and the timelike mechanism is the binding one.

### 3.2 The min-plus transfer matrix (deliverable (a))

**Definition 3.2.** State space `Σ := F_2^n / rowspace(H_X)`, `|Σ| = 2^r`, `r = n − rank(H_X)`.
(For the rotated surface code, `r = (d²+1)/2`.) Over the min-plus semiring
`(R_{≥0} ∪ {+∞}, min, +)` define

> **`A[E, E'] := w_M( [E' ⊕ E], H_Z E )`.**

Note the syndrome argument depends only on the *source* state, which is what makes this a
genuine matrix (the transition cost is a function of the ordered pair alone). Set boundary
vectors `u_E = 0` iff `E = [0]` else `∞`, and `v_E = 0` iff `H_Z E = 0` and
`[E] ∉ rowspace(H_X)`, else `∞`.

**Claim 3.3 (transfer-matrix representation).** CONJECTURED.
> `d_R(M) = u^⊤ ⊙ A^{⊙R} ⊙ v`,
and when `k = 1` this is literally the single matrix element `(A^{⊙R})_{[0],[X_L]}`.

*Blueprint.* Lemma 3.1 puts undetectable nontrivial configurations in bijection with sequences
`(Δ_1, …, Δ_R)` satisfying the recursion; Definition 2.2 makes the weight of the cheapest
realization of each step `A[E_{r−1}, E_r]`; the min-plus product is exactly the minimization over
intermediate states. Markov sufficiency of `[E]` is Lemma 2.1 plus ancilla reset. ∎

### 3.3 Spectral structure: the min-plus eigenvalue is `0` and the cyclicity is `1`

**Claim 3.4.** CONJECTURED. `A[E,E] = 0` **iff** `H_Z E = 0`; every other transition has strictly
positive cost, and there are no other zero-weight cycles. Hence `λ_{min-plus}(A) = 0` and the
critical graph is a set of `2^{2k}` self-loops with cyclicity `1`.

*Blueprint.* A weight-0 round has `Δ = 0` and `μ = 0`; Lemma 3.1 then forces `H_Z E = 0`.
Zero-weight cycles are concatenations of zero-weight transitions, which are exactly these
self-loops. ∎

Cross-check: with `λ = 0` and cyclicity `1`, the cyclicity theorem (§6 A1) predicts `A^{⊙R}`
becomes **eventually constant**, not merely eventually periodic. That is consistent with §3.4–3.5
and is a useful independent sanity condition on any implementation. It is *not* load-bearing —
see F2 and §6 A2.

### 3.4 Monotonicity: `d_R` is non-increasing (deliverable — this is F1)

**Claim 3.5 (padding).** CONJECTURED. `d_{R+1}(M) ≤ d_R(M)` for all `R ≥ 1`.

*Blueprint.* Let `F` be undetectable and nontrivial in `C_R` with `|F| = d_R`. By Lemma 3.1,
`H_Z E_R = 0`. Insert a fault-free round `R+1`. Its outcome flip is `o_{R+1} = H_Z E_R ⊕ 0 = 0`,
so `D_{R+1} = o_{R+1} ⊕ o_R = 0`, and the final detector `D_{R+2} = H_Z E_R ⊕ o_{R+1} = 0`. The
terminal logical class is unchanged. So `F` (reindexed) is undetectable and nontrivial in
`C_{R+1}` with the same weight. Prepending works identically since `E_0 = 0`. ∎

**Corollary 3.6.** `(d_R)_{R≥1}` is non-increasing and bounded in `[1, d]`, hence eventually
constant with limit `d_∞ = min_R d_R`; and

> `R_sat(M) = 1` if `d_∞ = d`, and `R_sat(M) = ∞` otherwise.

Also `d_eff(M) ≤ d_∞ ≤ d_1`, so the completion gap of 课题二 is `g_∞ = d_∞ − d_eff` at
saturation — a direct cross-link to `CIRCDIST.lift`.

### 3.5 The finite-window / pumping theorem with `B(r,d) = d` (deliverable (b), this is F2)

**Lemma 3.7 (fault-free rounds split configurations).** CONJECTURED. Let `F` be undetectable and
nontrivial in `C_R` and let round `t` carry no fault. Then `H_Z E_t = 0` and:
- if `[E_t] ∉ rowspace(H_X)`, the restriction of `F` to rounds `1..t` is undetectable and
  nontrivial in `C_t`;
- if `[E_t] ∈ rowspace(H_X)`, the restriction of `F` to rounds `t+1..R` is undetectable and
  nontrivial in `C_{R−t}` (after reindexing; `E_t ≡ 0` makes the shifted round `t+1` behave as a
  first round).

*Blueprint.* `H_Z E_t = 0` is Lemma 3.1 applied to the fault-free round (`μ_t = 0`). The prefix
then satisfies exactly the constraint system of `C_t` and terminates with zero syndrome; the
suffix satisfies exactly the constraint system of `C_{R−t}` started from a stabilizer-equivalent
identity. ∎

This is the same mechanism as **BHK's contiguity lemma** (§6 A5) — a simple undetectable
configuration in a time-local channel must be contiguous in time — specialized to a fixed
periodic extractor, where the pieces are *themselves* circuits of the same family. That
self-similarity is what upgrades a locality statement into an exact recursion.

**Claim 3.8 (finite window).** CONJECTURED. Let `d_∞ = min_R d_R` and
`R_stab = min{R : d_R = d_∞}`. Then **every round of a minimum-weight configuration realizing
`d_∞` in `C_{R_stab}` carries at least one fault**, hence

> `R_stab(M) ≤ d_∞(M) ≤ d`,  i.e.  **`B(r,d) = d`**, with no dependence on `r`.

*Blueprint.* Take `R = R_stab` and `F` of weight `d_∞` in `C_R`. If some round `t` is fault-free,
Lemma 3.7 yields a violating configuration of weight `≤ d_∞` in `C_t` or in `C_{R−t}`. By
minimality of `d_∞` that weight is exactly `d_∞`, so the complementary part has weight `0`, so
`d_t = d_∞` or `d_{R−t} = d_∞` with `t < R` or `R − t < R` — contradicting minimality of
`R_stab`. Hence every round is faulty and `R ≤ |F| = d_∞`. ∎

**Corollary 3.9 (decidability by finitely many checks).** `d_1, d_2, …, d_d` determine the whole
sequence: `d_R = d_d` for all `R ≥ d`. In particular `R_sat(M) < ∞` iff `d_d(M) = d`, and
`R_stab(M)` is read off the first `d` terms. This is precisely the conclusion the node claim
asks for, obtained with a `B` far smaller than anticipated.

### 3.6 The unconditional fallback bound

Even without Lemma 3.7, `B` is finite for a soft reason worth recording. Cap the semiring at `d`:
work in the **finite** min-plus semiring `S_d = {0, 1, …, d, ∞}` with `a ⊕' b = min(a+b, ∞)` and
everything above `d` collapsed to `∞` (legitimate because `d_R ≤ d` always). Then `A ∈ S_d^{Σ×Σ}`
lies in a finite set of size `(d+2)^{|Σ|²}`, so `(A^{⊙R})_R` is eventually periodic by pigeonhole
with `transient + period ≤ (d+2)^{4^r}`. Ugly, but explicit, computable, and it needs no lemma
about the circuit at all. Useful as the "even if 3.7 fails" premise of route `pumping-window`.

### 3.7 Longer detector windows

If detectors span `w` consecutive rounds, the state gains a measurement-memory component
`μ ∈ (F_2^{m_Z})^{w−1}` (so `r ↦ r + (w−1)m_Z`), a fault-free *run* of length `w−1` is needed to
reach a fixed point, and Lemma 3.7 applies to a fault-free run of length `≥ w`. Pigeonhole on
`W ≤ d−1` faulty rounds gives `B(r,d) = w(d+1) + d`. Still independent of `r`.

---

## 4. Candidate routes (deliverable 1)

Six routes. Premises are stated as sub-claims that would become their own DAG nodes. `P` =
estimated closure probability with one-line justification; `D` = sessions to next evidence level
or decisive failure.

### R1 · `min-plus-transfer-matrix`

**Premises.**
- `P1.1` *Round transparency*: Lemma 2.1 — a fault-free single-ancilla CSS extraction round
  leaves any data Pauli unchanged and flips exactly its syndrome bits.
- `P1.2` *Detector collapse*: Lemma 3.1 — undetectability ⟺ `μ_r = H_Z E_{r−1}` for all `r`,
  `E_0 = 0`, `H_Z E_R = 0`.
- `P1.3` *Markov sufficiency*: `[E_r] ∈ F_2^n/rowspace(H_X)` is a sufficient statistic for the
  future; equivalently the single-round dictionary `w_M` of Def. 2.2 is well defined on classes.
- `P1.4` *Boundary vectors*: the stated `u`, `v` correctly encode ideal init and ideal readout.

**Implication sketch.** P1.1+P1.3 make the round map a function of the ordered pair of classes;
P1.2 pins the measurement argument to the source state, so `A[E,E'] = w_M([E'⊕E], H_Z E)` is a
matrix; associativity of the min-plus product then gives `d_R = u^⊤ ⊙ A^{⊙R} ⊙ v`, with
`|Σ| = 2^r`, `r = n − rank(H_X)`. Cites A1 only for interpretation (`λ = 0`, cyclicity 1), not
for correctness.

**P = 0.85** — mostly bookkeeping over an `F_2`-linear circuit; the model is already implemented
and reproduces Stim on the surface code (§7). Residual risk is entirely in scope clauses S1–S3.
**D = 1.**

### R2 · `pumping-window`

**Premises.** P1.1–P1.3, plus
- `P2.1` *Zero-cost characterization*: `A[E,E] = 0` ⟺ `H_Z E = 0`; no other zero-weight cycles.
- `P2.2` *Splitting lemma*: Lemma 3.7.
- `P2.3` *Truncated-semiring fallback*: §3.6, giving `B ≤ (d+2)^{4^r}` unconditionally.

**Implication sketch.** P2.2 applied at a minimal-`R` minimum-weight witness forces every round
to be faulty, hence `R_stab ≤ d_∞ ≤ d` and `B(r,d) = d`; P2.3 keeps the route alive with a worse
bound if P2.2 fails under a weaker scope (e.g. `w > 2`, flag ancillas). Delivers the node's
"finite-window/pumping theorem with explicit computable `B(r,d)`" and the decidability corollary.

**P = 0.7** — the argument is short and I have not found a gap, but it leans on P1.2, which is
exactly where the boundary convention enters; a different convention (F1/§5) changes the
statement, not merely the constant. **D = 1.**

### R3 · `boundary-pinned-monotonicity`

**Premises.**
- `P3.1` *Terminal zero syndrome*: `H_Z E_R = 0` for any undetectable configuration (from P1.2).
- `P3.2` *Padding*: appending/prepending a fault-free round preserves undetectability, weight and
  logical class (Claim 3.5).
- `P3.3` *Convention dependence*: the same statement is **false** when the logical output is a
  measurement outcome rather than an ideal data readout; the correct scope clause is identified
  and the two conventions are separated.

**Implication sketch.** P3.1+P3.2 give `d_{R+1} ≤ d_R`; boundedness in `[1,d]` gives convergence;
combining with the definition of `R_sat` gives the dichotomy `R_sat ∈ {1, ∞}` and the
re-scoping onto `R_stab`. P3.3 is what makes this a *scope* result rather than a refutation of
the node's motivation.

**P = 0.8** — three-line argument, checked numerically at 7610 schedules with no violation, and
the sign matches the intuition that an ideal spacelike readout makes extra rounds pure liability.
**D = 0.5.**

### R4 · `periodic-strip-shortest-path` (graph-like specialization, surface-code case)

**Premises.** R1's premises, plus
- `P4.1` *Graph-likeness*: for the surface-code schedule the `X`-sector check matrix admits a
  check basis in which every fault has Hamming weight ≤ 2 (BHK's basis-existential definition,
  §6 A9) — so the DEM is a syndrome graph.
- `P4.2` *Periodic-strip / voltage model*: `C_R` becomes a finite strip of `R` copies of one
  period of a `Z`-periodic graph; "nontrivial logical" becomes "nonzero label" for a
  `Z_2^{2k}`-valued voltage; `d_R` becomes the minimum-weight nonzero-label walk between the two
  time boundaries.
- `P4.3` *Window in the graph model*: the minimizer is achieved within `d` layers (Claim 3.8
  specialized, or a direct cut argument in the strip).
- `P4.4` *Worked case*: exact `d_R` for the standard rotated-surface-code schedule and for a
  hook-misaligned schedule, at `d = 3, 5, 7`.

**Implication sketch.** With P4.1–P4.2 the problem is the shortest nonzero-label path problem in
a group-labeled graph, for which a strongly polynomial `O(nm)` algorithm exists (§6 A8,
Iwata–Yamaguchi); P4.3 truncates the infinite strip; P4.4 instantiates the worked case demanded
by the node's 最低验收结果. This route also gives the cheapest *proof-grade* algorithm for `d_R`
in the matchable case, as opposed to the exponential dictionary BFS.

**P = 0.65** — every ingredient exists in the literature, but the periodic-strip nonzero-voltage
statement is precisely the one the literature sweep could **not** find stated (§6 A8 caveat), so
it must be assembled rather than cited. **D = 1–2.**

### R5 · `trellis-matroid-generalization` (beyond graph-like — deliberately a *later* route)

**Premises.**
- `P5.1` *Convolutional identification*: the spacetime DEM of a fixed periodic extractor is a
  **terminated time-invariant convolutional code** over `F_2`, whose minimal trellis state at
  each cut is exactly `[E_r] ∈ F_2^n/rowspace(H_X)`; `d_∞` is its free distance restricted to the
  nontrivial-logical coset.
- `P5.2` *Coset subtlety*: "nontrivial logical" is an affine/coset condition, not a linear one
  (cf. A4: Delfosse–Paetznick's outcome code is *affine*); the free-distance machinery must be
  stated for the coset.
- `P5.3` *Matroid handle*: for non-graph-like check matrices, use the binary-matroid structure
  BHK already point to (§6 A9) to get bounds where exact search is infeasible.
- `P5.4` *qLDPC instantiation*: a bivariate-bicycle schedule (e.g. `[[72,12,6]]`, or the gross
  code for the cross-link to `CIRCDIST.gross`).

**Implication sketch.** P5.1 replaces the ad-hoc dictionary with standard trellis theory and
makes `R_stab` an error-event length; P5.2 keeps the statement honest; P5.3+P5.4 discharge the
node's "at least one qLDPC schedule" requirement in the hypergraph case where matching-based
tools do not apply. Deliberately sequenced *after* R1–R3: it is the only route whose cost is
dominated by computation rather than argument.

**P = 0.5** — the identification is natural and I believe it, but I did not find it stated in the
QEC literature, and the coset issue (P5.2) is a real technical wrinkle; the qLDPC computation is
the expensive part (exact hypergraph distance search, §6 A7 hardness). **D = 2–3.**

### R6 · `mechanism-attribution`

**Premises.**
- `P6.1` *Partition definition*: classify a minimum-weight witness `F` for `d_∞` by
  (i) its **temporal span** `R_stab` and (ii) whether it must touch round 1 or the readout layer.
  Single-round span ⟹ hook/bulk; multi-round span with both data and flip faults ⟹ mixed
  spacetime; forced boundary contact ⟹ boundary; flip-faults-only ⟹ timelike measurement.
- `P6.2` *Exclusion theorem*: under the stated ideal-readout convention, the timelike class is
  **empty** — Lemma 3.1 pins `o_r ≡ 0` at both time boundaries, so no configuration of
  measurement-flip faults alone is undetectable.
- `P6.3` *Hook vocabulary alignment*: express the hook/bulk class in BHK's **hazardous / brazen
  hook fault** language (§6 A6) so the attribution is comparable across the project.
- `P6.4` *Convention contrast*: exhibit the timelike class as nonempty in the
  logical-measurement-output convention (lattice surgery `XX` channel, §6 A5) — establishing that
  the attribution is a statement about the boundary, not about `M`.

**Implication sketch.** P6.1 makes attribution a computable function of the first `d` terms of
`(d_R)` plus one boundary-contact test on the witness — both inside the `B(r,d) = d` window.
P6.2 turns the four-way split into a two-way split (hook/bulk vs. mixed) under the stated
convention, which is a substantive, falsifiable claim rather than a taxonomy. P6.4 is what makes
it explanatory.

**P = 0.6** — P6.2 follows from Lemma 3.1 and is cheap; the risk is that P6.1 is a *definition*
and a reviewer may reject it as not canonical. Anchoring it to BHK's hook vocabulary (P6.3) is
the mitigation. **D = 1.**

### R7 · `single-round-dominance` (registered as a *conjecture-or-refutation* route)

Not one of the required (a)–(e), but this recon's most informative next step, so it is registered
explicitly.

**Premises.**
- `P7.1` *Statement*: for every `M` in the 公共定义 class, `d_R(M) = d_1(M)` for all `R ≥ 1`
  (equivalently `R_stab(M) = 1`).
- `P7.2` *Or a witness*: an explicit `(Q, M)` with `d_2 < d_1`, i.e. a genuine two-round
  spacetime mechanism.

**Implication sketch.** If P7.1 holds, `CIRCDIST.sat` under the stated conventions reduces
entirely to `d_eff`-style single-round analysis, and the node should be re-scoped or PARKED in
favour of `CIRCDIST.lift`. If P7.2 holds, the multi-round mechanism it exhibits is the central
object of the node and everything else follows. Either outcome is decisive.

Evidence so far (§7): 7610 legal schedules across the rotated surface code (`d=3`), Steane
`[[7,1,3]]` and Shor `[[9,1,3]]`, at depths `T ∈ {4,5,6,8,10}` — **all constant**. Note this is
*not* evidence for a theorem: `d = 3` leaves almost no room (`R_stab ≤ d_∞ ≤ 3`), so the search
must move to `d ≥ 5`.

**P = 0.55** for reaching a decision (either branch); **P ≈ 0.35** that P7.1 is the true branch —
the naive projection of a two-round witness into one round fails to cancel `Σ_r H_Z E_{r−1}`, so
there is no visible obstruction to `R_stab ≥ 2`. **D = 1–2.**

---

## 5. The single cheapest decisive gate (deliverable 2)

> **GATE.** Compute the exact sequence `d_1, …, d_{d+2}` for the rotated surface code at
> `d = 3, 5, 7`, for (i) the standard schedule and (ii) at least one hook-misaligned schedule,
> by two independent methods: the min-plus transfer matrix of §3.2 and a DEM search
> (`stim.Circuit.shortest_graphlike_error`, with the exactness caveat of §6 A7).

It is the cheapest decisive gate because a *single* run discriminates all of R1, R2, R3 and R7
simultaneously, and each outcome has a pre-committed reading:

| Outcome | Reading |
|---|---|
| `d_R` constant in `R`, both schedules, both methods | R1/R3 corroborated; `R_stab = 1`; R7 branch P7.1 favoured; **the node should be re-scoped per F1 before more effort** |
| `d_R` strictly **decreasing** somewhere | R3 corroborated and R7 branch P7.2 delivered — the witness is the node's central object; `R_stab` computed directly |
| `d_R` strictly **increasing** anywhere | **R3 is refuted**; the failure must be localized to P3.1 or P3.2, which in practice means the implemented circuit's detector/boundary structure differs from S2 — diagnose *which* lemma, since that is exactly the F1 scope question |
| transfer matrix and Stim disagree | localize to S1 (sector decoupling), S3 (fault model), or the graph-like restriction of `shortest_graphlike_error` — all three are cheap to isolate |

**Status: partially executed in this session** (see §7): `d = 3` transfer matrix and `d = 3,5,7`
Stim both gave the *constant* outcome. What remains is the `d = 5, 7` transfer-matrix arm
(needs a weight-capped Dijkstra rather than a full BFS over `2^{r+m_Z}` targets) and the
hook-misaligned arm at `d ≥ 5`.

Interpretation notes the gate is designed to produce:
- **Eventual periodicity** of `d_R` is *not* what to expect here — Claim 3.4 says the min-plus
  eigenvalue is `0` and the critical cyclicity is `1`, so the prediction is eventual
  **constancy**, and any observed period `> 1` would refute Claim 3.4 and hence P2.1.
- **Min-plus eigenvalue interpretation**: `λ(A) = 0` is the statement "the circuit has fault-free
  rounds available at zero-syndrome states". A hypothetical schedule with `λ(A) > 0` would be one
  where *no* round can be fault-free — impossible in this class, so `λ(A) > 0` observed anywhere
  means an implementation bug, which makes it a useful assertion to leave in the code.

---

## 6. Load-bearing external results, as ASSUMPTIONS

Format: exact statement (or explicit paraphrase flag), source, and what it is load-bearing for.
Verification status is reported honestly; several items were checked against primary sources in
this session and several were not.

**A1 — Cyclicity theorem for max-plus (equivalently min-plus) matrix powers.** *Statement:* for
irreducible `A` there exist `T ≥ 0` and `γ ≥ 1` with `A^{⊗(t+γ)} = λ^{⊗γ} ⊗ A^{⊗t}` for all
`t ≥ T`, where `λ` is the unique max-plus eigenvalue and `γ` the cyclicity of the critical graph.
*Source:* Cohen, Dubois, Quadrat, Viot, INRIA RR-191 (1983) / IEEE TAC 30(3):210–220 (1985).
Textbook form: Baccelli–Cohen–Olsder–Quadrat, *Synchronization and Linearity* (Wiley 1992),
**Definition 3.111 + Theorem 3.112** — **not** Theorem 3.109, despite that number being widely
repeated in the literature (3.108/3.109 are the `lim A^k = Q` statements). Also Butkovič,
*Max-linear Systems* (Springer 2010), Thm 8.3.6 (Nachtigall's critical-part refinement,
`T_c(A) ≤ n²`). *Load-bearing for:* nothing. Used only as an interpretive cross-check on
Claim 3.4 (`λ = 0`, cyclicity 1 ⟹ eventual constancy). Recording it as non-load-bearing is
deliberate: §3.5 is self-contained.

**A2 — No transient bound in the dimension alone.** *Statement:* Nowak–Charron-Bost,
"An Overview of Transience Bounds in Max-Plus Algebra" (arXiv:1405.3458), **Theorem 5.4**: for
any sequences `D_n ≤ M_n` there exist irreducible `n×n` max-plus matrices with
`λ − λ₂ = D_n`, `‖A‖ = M_n`, and transient `Ω(n²‖A‖/(λ−λ₂))`; the survey concludes explicitly
that "no upper bound only in terms of `n` exists". Known bounds (Hartmann–Arguelles, Math. of OR
24(2):414–439, 1999; Merlet–Nowak–Sergeev, LAA 461:163–199, 2014) split into a pattern-only part
and a value-dependent part. *Load-bearing for:* the **claim that F2 is a genuine improvement**.
Generic tropical theory cannot deliver an `r`-free `B`; §3.5 can, because `λ = 0` exactly and
weights are integers capped at `d`.

**A3 — Reducible case, and the decidability boundary.** *Statement (i):* De Schutter, LAA
307:103–117 (2000), **Theorem 3.3**: for general (reducible) `A` in Frobenius normal form the
entry sequences are ultimately *periodic* with an lcm period and possibly **several different
rates across residue classes** — his **Example 3.6** is an explicit 7×7 counterexample to the
naive "`(A^{R+p})_{ij} = (A^R)_{ij} + c`" form, and he notes two published papers stating that
form incorrectly. *Statement (ii):* for a **unary** alphabet (powers of one fixed matrix) the
theory is decidable and polynomial — Gaubert, INRIA RR-2162 (1994); Bonnier-Rigny & Krob, TCS
134(1):27–50 (1994) (complete axiomatization for one-letter tropical rational expressions);
Molnárová & Pribiš, DAM 103:167–175 (2000) (`O(n³)` period). *Statement (iii):* Krob, IJAC
4(3):405–426 (1994) — equality of rational series over the tropical semiring is **undecidable**;
this requires **≥ 2 letters**, i.e. products of *different* matrices. *Load-bearing for:* the
scope clause "our automaton has one letter". Any generalization of `CIRCDIST.sat` to
*non-identical* rounds (e.g. alternating schedules) crosses the Krob boundary and loses the
generic decidability guarantee. This is a real hazard for any future `CIRCDIST.sat` variant and
should be recorded on the node.

**A4 — Spacetime code of a Clifford circuit.** *Correction to a common attribution:* Delfosse &
Paetznick, "Spacetime codes of Clifford circuits" (arXiv:2304.05943) **does not define circuit
distance** — verified by full-text search in this session (0 hits for "circuit distance",
"fault distance", "undetectable"). Their Theorem 1 gives the outcome code as an **affine**
subspace, Theorem 2 the spacetime stabilizer code `[[n(Δ+1), N−(m−k)]]`, Theorem 3 the decoding
reduction. *The correct source for the distance statement is:* Gottesman, "Opportunities and
Challenges in Fault-Tolerant Quantum Computation" (arXiv:2210.15844), §5–6, masked distances
`d_U ≤ d_T ≤ d` and **Theorem 6.1** (a circuit corrects a set of fault paths iff the spacetime
code corrects the corresponding errors using only the always-unmasked stabilizer; correctable up
to `⌊(d_U−1)/2⌋` faults). *Load-bearing for:* the definitional frame of R5/P5.1–P5.2 (the
affineness of the outcome code is exactly the coset subtlety).

**A5 — Composition theorem for stabilizer channels: SUFFICIENT only.** *Statement:*
Beverland, Huang, Kliuchnikov, "Fault tolerance of stabilizer channels" (arXiv:2401.12017),
**Theorem VI.2**: for compatible time-local channels `C_α, C_β, C_γ` with unit-weight faults, if
`C_α∘C_β` and `C_β∘C_γ` have fault distance `≥ d` and `C_β`'s time-local partition has size
`≥ d`, then `C_α∘C_β∘C_γ` has fault distance `≥ d`. The `d+1` check length is theirs verbatim
("at the expense of analyzing all possible compositions of `d+1` such channels"). *Important:*
the **abstract** says "necessary conditions"; the **body** (§I and §VI opening) says
**sufficient**, and no necessity result appears in the paper — cite §VI/Thm VI.2, not the
abstract. *Why sufficiency only, for a fixed periodic extractor:* (i) the conclusion is one-sided
(`≥ d`), never an equality, and there is no converse; (ii) the proof is a pigeonhole containment
calibrated to a pre-chosen `d`, so it never examines mechanisms spanning more than `d`
partitions; (iii) finite windows introduce artificial time boundaries — BHK themselves warn
(§III C, fn. [45]) that the output-syndrome convention "is equivalent to appending a perfect
round" and that this "does not lead to spurious analysis results" needs care. This is exactly the
gap 课题四 identifies, and it is real. *Also load-bearing:* BHK's **contiguity lemma** is the
ancestor of Lemma 3.7, and BHK **§VIII B** is the citable statement of the timelike folklore —
"These time-like logical faults require us to use `d` repeated rounds — if fewer repetitions were
made then the undetectable logical outcome flip could occur with fewer than `d` faults" — in a
channel whose logical output is a **measurement outcome**. That contrast is the backbone of F1
and P6.4. BHK §VIII also documents a case where `d` rounds is *not* the right count (their
logical-Hadamard deformation drops below code distance; `≈ d/2` rounds suffice elsewhere), and
their full-distance claims are verified only for `d = 3,…,11` and **conjectured** beyond.
*Status:* arXiv-only as far as could be verified; flag as possibly stale.

**A6 — Hook faults, formally.** BHK §IV: "there is no generally applicable definition of a hook
fault"; theirs is "`F` is a hook fault with respect to `F_sub ⊂ F` if there is no equivalent
elementary fault of `F_sub`", with **Definition IV.1** splitting **hazardous** (contained in a
minimum-weight nontrivial undetectable configuration) from **brazen** (equivalent to a subset of
one for `F_sub`), and the consequences: no hazardous hook ⟹ `d(F) = d(F_sub)`; any brazen hook
⟹ `d(F) < d(F_sub)`. Origin of the term: Dennis, Kitaev, Landahl, Preskill, "Topological quantum
memory", J. Math. Phys. 43:4452–4505 (2002). *Load-bearing for:* P6.3.

**A7 — Computing circuit distance: methods and hardness.** *Methods:* BHK §VII — Dijkstra-style
graph search (they attribute the implementation to Stim, Gidney, Quantum 5:497 (2021)) and a
shortest-odd-cycle reduction with runtime `O(n_L(|V||E| + |V|² log|V|))`; beyond graph-like, only
bounds (BP-OSD upper bounds; binary-matroid structure). *Caveat that matters for §7:* Webster,
Jacob, Higgott, "Distance-Finding Algorithms for Quantum Codes and Circuits" (arXiv:2603.22532)
classify "Stim undetectable error methods" among **heuristic** methods that "can only give a
bound on distance" — so `shortest_graphlike_error` should be read as an upper bound (exact only
within the graph-like restriction). *Hardness:* verified — maximum-likelihood decoding is NP-hard
for linear codes (Berlekamp, McEliece, van Tilborg, IEEE TIT 24(3):384–386, 1978) and #P-hard for
stabilizer codes (Iyer & Poulin, IEEE TIT 61(9):5209–5223, 2015). **UNVERIFIED and deliberately
not cited:** Vardy (1997) for minimum-distance NP-hardness and Kapshikar–Kundu for the quantum
analogue — these are *distance-computation* results, distinct from the *decoding* results above,
and conflating them is a referee-catchable error. Anyone completing R5 must re-check them.

**A8 — Shortest nonzero-label path in a group-labeled graph.** *Statement:* Iwata & Yamaguchi,
"Finding a Shortest Non-zero Path in Group-Labeled Graphs", Combinatorica (2022), DOI
10.1007/s00493-021-4736-x (arXiv:1906.04062): for a `Γ`-labeled graph with **nonnegative** edge
lengths, a shortest non-zero path is found in `O(nm)`, and a shortest non-zero cycle in
`O(n(m + n log n))`; any `α ∈ Γ` may replace `1_Γ` as the forbidden label. Related: Fox, SODA
2013 (shortest non-contractible / non-null-homologous cycles in directed surface graphs, via a
restriction of the **infinite cyclic cover**); Cohen & Megiddo, JACM 40(4):791–830 (1993)
(zero-weight-cycle detection in `Z^d`-weighted digraphs: strongly polynomial for fixed `d`,
LP-equivalent otherwise); Höfting & Wanke, SIAM J. Comput. 24(5):1051–1067 (1995) (minimum cost
paths in periodic graphs). *Load-bearing for:* R4/P4.2. **Honest gap:** the literature sweep
found **no** paper stating the specific theorem "minimum weight of a nonzero-voltage closed walk
in a `Z`-periodic strip with arbitrary weights". Two obstructions were flagged and are *not*
established: negative-weight walks can send the infimum to `−∞` (our weights are nonnegative, so
this is fine here), and it is not obvious the optimal winding number can be taken `±1`. R4 must
assemble this, not cite it. Also flagged: two incompatible secondary summaries of what
Höfting–Wanke prove (polynomial vs. NP-hard-with-pseudopolynomial) — the SIAM paper must be read
directly before citing.

**A9 — Graph-like vs. hypergraph detector error models.** *Statement:* BHK §VII B — a channel
check matrix `A_Σ` is **graph-like** if **there exists** a check basis `Σ'` with the same span in
which every column has Hamming weight 1 or 2 (a basis-*existential* condition, which most informal
statements get wrong); the syndrome graph is then built with a boundary vertex for weight-1
columns, and undetectable faults correspond to cycles. The standard CSS splitting that makes
circuit-level surface-code noise graph-like is theirs verbatim. Detector error models themselves:
Stim's DEM file-format documentation ("a list of independent error mechanisms… symptoms… frame
changes"); Gidney, Quantum 5:497 (2021) for the simulator. *Load-bearing for:* P4.1 and the scope
boundary between R4 and R5.

**A10 — qLDPC instantiation.** Bravyi, Cross, Gambetta, Maslov, Rall, Yoder,
"High-threshold and low-overhead fault-tolerant quantum memory", Nature 627:778 (2024),
arXiv:2308.07915 (author list corrected in this session). Follow-up computing gross-code circuit
distance: Strikis, Browne, Beverland, "High-performance syndrome extraction circuits for quantum
codes", arXiv:2603.05481 — best known SECs for the gross code achieve circuit distance **at most
10**; their **Proposition 4** proves any *non-interleaved* SEC has `d_circ ≤ 11`; `d_circ = 11`
is **conjectured**, not proved. *Load-bearing for:* P5.4, and it is the precise statement of the
"已知结果" in 课题一, so it should be attached to `CIRCDIST.gross` as well. *Not cited:* the
"936 depth-7 variants ⟹ `d_circ ≤ 10`" figure that circulates via the Error Correction Zoo — no
primary source was identified for it.

**A11 — Round counts are not universally `≈ d`.** Zhou, Zhao, Cain, Bluvstein, Maskara,
Duckering, Hu, Wang, Kubica, Lukin, "Low-Overhead Transversal Fault Tolerance for Universal
Quantum Computation", Nature (2025), DOI 10.1038/s41586-025-09543-5 (arXiv:2406.17653): standard
constructions "require multiple extraction rounds — on the order of the code distance `d`", but
logical operations can be done fault-tolerantly with a **constant** number of rounds using
transversal gates plus correlated decoding. *Load-bearing for:* keeping any blanket "`R = d` is
necessary" claim out of the node.

---

## 7. NUMERICAL results from this session

Scope: `Z`-memory sector (S1), detector window `w = 2` (S2), unit-weight elementary faults (S3).
Two independent implementations. Reproduction commands in §9.

**(N1) Exact min-plus transfer matrix, rotated surface code `d = 3`.** State space
`r = n − rank(H_X) = 9 − 4 = 5`, `|Σ| = 32`, `m_Z = 4`; `A` computed exactly from the
single-round dictionary; `d_R = (A^{⊙R})_{[0],[X_L]}` for `R = 1..10`.

| schedule (corner order Z-checks / X-checks) | `d_R`, `R = 1..10` |
|---|---|
| `NW NE SW SE` / `NW SW NE SE` | `2 2 2 2 2 2 2 2 2 2` |
| `NW NE SW SE` / `NW NE SW SE` | `3 3 3 3 3 3 3 3 3 3` |
| `NW SW NE SE` / `NW SW NE SE` | `2 2 2 2 2 2 2 2 2 2` |
| first row, idle faults removed | `2 2 2 2 2 2 2 2 2 2` |

Zero-weight self-loops occur at exactly the 2 zero-syndrome states in every case, confirming
Claim 3.4 numerically (`λ(A) = 0`, cyclicity 1).

**(N2) Independent Stim cross-check.** `shortest_graphlike_error` on
`stim.Circuit.generated(...)` (upper bound per A7):

| circuit | `d_R` |
|---|---|
| `surface_code:rotated_memory_z`, `d = 3`, `R = 1..12` | `3` throughout |
| `surface_code:rotated_memory_z`, `d = 5`, `R = 1..12` | `5` throughout |
| `surface_code:rotated_memory_z`, `d = 7`, `R = 1..12` | `7` throughout |
| `surface_code:unrotated_memory_z`, `d = 3, 5`, `R = 1..8` | `3` / `5` throughout |
| `repetition_code:memory`, `d = 3, 5`, `R = 1..8` | `3` / `5` throughout |

Agreement with N1 on the `d_R = 3` schedule, and the constancy is confirmed at `d = 5, 7` where
the transfer-matrix arm was not run.

**(N3) Schedule sweep — 7610 legal schedules, all with constant `d_R`.**

| family | depths `T` | legal schedules | distinct `d_R` sequences |
|---|---|---|---|
| rotated surface `d=3`, uniform per check type (all `24×24` corner-order pairs) | 4 | 96 | `[2]*8` ×16, `[3]*8` ×80 |
| rotated surface `d=3`, independent order per check | 4 | 72 | `[2]*6` ×24, `[3]*6` ×48 |
| rotated surface `d=3`, arbitrary slot assignment | 4,5,6,8,10 | 6085 | only `[2]*6` and `[3]*6` |
| Steane `[[7,1,3]]` (hypergraph DEM) | 6,8 | 680 | only `[2]*6` and `[3]*6` |
| Shor `[[9,1,3]]` | 6,8 | 677 | only `[1]*6`, `[2]*6`, `[3]*6` |

**Not a single non-constant sequence, and not a single increase.** This is consistent with
Claim 3.5 (non-increasing) and with `R_stab = 1`. It is *weak* evidence for R7/P7.1 because
`d = 3` bounds `R_stab ≤ d_∞ ≤ 3`; the search must move to `d ≥ 5`, where the transfer-matrix
method needs a weight-capped Dijkstra (the full BFS over `2^{r+m_Z} = 2^{25}` targets is out of
reach in the current implementation).

---

## 8. What this recon recommends

1. **Re-scope the node claim before spending another session on it.** Under 公共定义 as written,
   `R_sat` carries one bit (F1) and `B(r,d) = d` (F2). The node's stated deliverables are
   *achievable*, but they will not say what the claim text implies they will say. Two options:
   (a) keep the convention and re-target the claim onto `d_∞`, `R_stab`, and the mechanism
   dichotomy; or (b) add a second convention — logical output as a **measurement outcome** /
   noisy or absent terminal readout — under which `d_R` is non-decreasing, `R_sat ≈ d`, and the
   timelike mechanism is live (A5, BHK §VIII B). Option (b) is what makes 课题四 a genuinely
   different problem from 课题二; option (a) risks collapsing it into `CIRCDIST.lift`.
2. **Sequence R3 → R1 → R2 → R6 → R7 → R4 → R5.** R3 is half a session and is the one that
   decides the re-scoping. R7 is the highest-information experiment.
3. **Do not import the tropical transient machinery as a premise.** A1/A2 say it cannot give an
   `r`-free bound; §3.5 can. Keep A1 as a cross-check only.
4. **Record the Krob boundary (A3) on the node now.** It is invisible in the current claim text
   but it is exactly the wall any "non-identical rounds" generalization hits.
5. **Two literature corrections should propagate to sibling nodes.** Delfosse–Paetznick does not
   define circuit distance (use Gottesman Thm 6.1); BHK's composition theorem is sufficient, not
   necessary, despite its abstract. And `CIRCDIST.gross` should carry Strikis–Browne–Beverland
   (A10) as the primary source for its "已知结果".

---

## 9. Reproduction

Scripts written to the session scratchpad (not committed; no repo file other than this artifact
was modified):

```
<scratchpad>/sat_tm.py    # exact min-plus transfer matrix, rotated surface code d=3  (N1)
<scratchpad>/stimcheck.py # Stim cross-check across d and R                            (N2)
<scratchpad>/sweep.py     # uniform + per-check schedule sweep, surface d=3            (N3)
<scratchpad>/sweep2.py    # arbitrary-depth slot-assignment sweep, surface d=3         (N3)
<scratchpad>/generic.py   # generic CSS driver; Steane sweep                           (N3)
<scratchpad>/shor.py      # Shor [[9,1,3]] sweep                                       (N3)
```

`stim 1.16.0` was installed into a scratchpad-local `--target` directory; the repository
environment was not modified. Run with `PYTHONPATH=<scratchpad>/pylibs`.

Anyone re-running these should first re-derive Lemma 2.1 independently: every numerical result
above inherits its correctness, and it is the cheapest thing to get subtly wrong.
