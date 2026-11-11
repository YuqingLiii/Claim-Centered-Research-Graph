# CIRCDIST.gross — D* hunt, stage 1: the repair-0 decider, and a both-sector gap candidate

Session: hunt worker, 2026-08-23, one budget box (1.5), no sub-agents.
Node: `CIRCDIST.gross` (课题一). Everything below is **proposer level** (rule 6): nothing here
has been independently reviewed, and no node level is claimed or changed by this artifact.

Logs: `artifacts/logs_circdist_dstar_hunt1_20260823/` (11 outputs + `src/` with the 11 source
files, `SHA256SUMS.txt`, 23 entries). All code written this session; the only imported data are
the two weight-12 logical seed files `w12.txt` / `w12X.txt` from
`artifacts/logs_circdist_gross_links_20260823/`, whose every element this session re-validated
(weight, kernel membership, non-triviality) from its own independent code build.

---

## 0. Headline

**A stage-1 GAP CANDIDATE exists**: an explicit legal, measurement-consistent, *interleaved*
3-colour-tiled gross schedule in which — in **both** memory sectors — every canonical
minimum-weight effective logical has `repair >= 1`, and the weight-12-pool `d_ext <= 10`
disqualifier is clean. If its `d_eff = 11` survives certification and the two uncovered
`|gamma| = 11` shapes stay empty, then by `CIRCDIST.lift.iff` (Thm 5.7, hash `0c4c466b`)
`d_circ = 12` for this schedule and `D*_Gross = 12`.

That is a *candidate*, not a witness. §6 states exactly what is still missing.

---

## 1. What the decider is, and why it is one-sided

Frozen model, `CIRCDIST.lift.iff` §1.5–1.7, §5.1–5.5. Z-memory sector; X-memory is the mirror.

* residuals `E`: suffixes of X-check CNOT orders, singletons, `∅`;
  `s(E) = H_Z E`; `u_b(hook S of a) = #{q ∈ supp(b) ∩ S : t(q→b) > t(a→q)} mod 2`;
  `U({q})` = the time-suffixes of `q`'s three Z-gates (4 elements, a nested chain).
* `L_eff`, `d_eff = d_ext(E(M))`; `repair(gamma)` = Definition 5.2, one round.
* criterion: `d_circ = d_eff` **iff** some minimum-weight `gamma` has `repair(gamma) = 0`.

**Canonical minimum-weight family.** By `CIRCDIST.gross.dext-cap` the weight-11 witnesses are
`gamma = {S_a} ∪ (V \ S_a)` with `V` a weight-12 logical and `S_a` the **2-suffix** of check
`a`'s CNOT order, `S_a ⊆ V`. This session's decider searches exactly that family.

* **finding a repair-0 certificate is SOUND**: it proves `d_circ = d_eff` for that schedule, so
  the schedule cannot witness `D* = 12`. This is the direction the sweep uses to reject.
* **failing to find one is NOT a proof of a gap**: other `|gamma| = 11` shapes are untested
  (§6.2), and each such shape can only *kill* a candidate, never create one.

**Same-round certificate, in physical words.** With all faults in one round, `B = Σ s_i = 0`,
so `C = 0` and `repair = |Σ_i u_i|`. So `repair = 0` (same round) says: *the twelve X errors of
`V` — ten placed freely, two delivered by the hook of `a` at times `t(a→q_5), t(a→q_6)` — can be
timed so that every Z-check sees an even number of them arrive before its own gate.* Since
`|V ∩ supp(b)|` is even for every `b` (and this session measured it to be `0` or `2` in
7160+21620 of 28800 (check, logical) incidences, `4` in only 20), this is an edge-2-colouring
problem on a cubic graph on the 12 qubits of `V`, in which each vertex's 1-edges must form a
suffix of that qubit's own gate order and the two hook vertices are forced.

## 2. Decider validation against ground truth

Small-code end-to-end check (`src/valid_small.py`, `out_valid_steane.txt`): Steane `[[7,1,3]]`,
Z-memory, `R = 4`. For each schedule the session builds the **actual** multi-round DEM from the
frozen fault inventory and computes `d_circ` by exhaustive minimum-weight search, independently
of the repair machinery.

* **21 / 21** legal + (MC) schedules: criterion agrees with brute-force `d_circ` exactly.
* **21 / 21**: the Theorem 2 sandwich `|g| + min(repair,2) <= d_circ <= |g| + repair` holds.
* Both branches exercised: 20 no-gap instances **and 1 genuine gap** — an interleaved legal+(MC)
  schedule with `d_eff = 2`, all minimum-weight `repair >= 1`, brute-force `d_circ = 3`. This
  independently reproduces the `CIRCDIST.lift.gap-example` Steane witness (interleaved, Z-memory,
  `d_eff = 2`, `d_circ = 3`) from a fresh implementation. Gap rate in that family: **1 / 68**
  random legal+(MC) Steane schedules.

Gross-side build validation (`out_gross_build.txt`), all reproduced from scratch:
commutation `0` failures; overlap histogram `{0: 4536, 2: 648}`; **every** overlap splits
`(1 left, 1 right)`; `rank H_X = rank H_Z = 66`, `k = 12`; the two seed files expand to
`4152` weight-12 kernel vectors and **1884 nontrivial logicals per sector** (matching the wave-36
exhaustive pool); `dext-cap` pair coverage **1080 / 1080** (every 2-subset of every X-check
support lies in a weight-12 logical), with 2–44 (mean 20.1) logicals per pair.

New by-product: **all-ones lies in `rowspace(H_X)` and in `rowspace(H_Z)`**, so every logical in
either sector has **even weight** — weight-13 logicals do not exist, which empties one whole
family of alternative `|gamma| = 11` shapes.

## 3. L1 — the (MC) ⟺ per-pair non-interleaving lead: **verdict, one true reading and one false**

The lead as handed over is *false in the SBB sense and vacuous in the other*, and this session
reproduced both halves:

* **TRUE and sharper (premise)**: every overlapping (X,Z) pair shares exactly 2 qubits, one left
  and one right (`{0: 4536, 2: 648}`, splits all `(1,1)`), so `(MC)` on a pair reduces to
  *the two shared comparisons agree*. As a statement about the two shared gates this is a
  restatement of Definition 2.1, not an extra constraint — it collapses nothing.
* **FALSE in the SBB sense**: "agree" is not "all of `a`'s CNOTs before all of `b`'s". This
  session built legal (MC)-clean gross schedules with **0/648 (MC) violations and 216–384 of 648
  pairs interleaved even on the overlap** (and 648/648 interleaved as whole checks). This
  independently re-confirms `CIRCDIST.gross.mc-equiv = REFUTED`
  (`artifacts/circdist_sbbcert_review_20260820.md` §6) and, importantly, means **SBB Thm 1 stays
  unusable** for every schedule in this hunt: no interleaved conclusion may cite it.
* Consequence for the campaign record: the wave-36 by-product sentence in
  `CIRCDIST.gross`'s `links-closed-2026-08-23` event ("for the gross code (MC) is equivalent to
  per-pair non-interleaving") reads, on its face, as the refuted claim. **Recommended repair**:
  reword to "every overlap is exactly 2 qubits (one left, one right), so (MC) is exactly the
  agreement of the two shared comparisons" — or delete it. Flagged, not executed (canonical files
  untouched).

## 4. Two no-go mechanisms found, and where they stop

**Theorem A (proposer level).** Under (MC), because every gross overlap is exactly 2,
`u(S) = s(S) ∩ After(a)` for every hook `S` of `a`, where `After(a) = {b : ε_{ab} = 0}` and
`ε_{ab} = 1[b's gates on the a–b overlap precede a's]`. Hence a hook is *horizontal*
(`u ∈ {0, s}`, `repair = 0` immediately, via the all-zero or all-full singleton certificate)
whenever `s(S) ⊆ Before(a)` or `s(S) ⊆ After(a)`. No gross hook is ever *vertical* — 0/72 in every
schedule tested, exactly as `CIRCDIST.lift.iff` Theorem 1 requires.

**Theorem B (proposer level) — the check-serial no-go.** If every check performs its six CNOTs
consecutively (any global check order `π`, any within-check orders), then for **every** canonical
`gamma`, `repair(gamma) = 0`. *Proof.* `After(a) = {b : π(b) > π(a)}`, and each qubit's gate order
is by `π`, so `u_q := s({q}) ∩ After(a) ∈ U({q})`; intersecting with a fixed set is F2-linear, so
`Σ_{q ∈ V∖S} u_q = s(V∖S) ∩ After(a) = s(S) ∩ After(a) = u(S)`. ∎
Verified: **226/226** and **170/170** canonical `gamma` repair-0 in the Z- and X-memory sectors of
the check-serial family, despite 42–57 of 72 hooks being **diagonal**. Diagonal hooks are
necessary for a gap but nowhere near sufficient.

**Corollary (the shape of the gap).** Theorem B's argument survives every construction in which
`ε` is induced by a single global potential — block schedules, left/right-shifted blocks,
`σ`-rescaled blocks. A gap therefore requires **genuine misalignment**: some data qubit `q ∉ S_a`
whose three Z-gates are ordered *inconsistently* with `ε_{a·}`. This is exactly the wave-24/25
"deliberate hook misalignment" (L3), now with a precise definition and a computable test
(`hunt.misalignment`).

## 5. Sweep results (exact spaces, proposer level)

`repair-0 rate` = fraction of the canonical minimum-weight family admitting a same-round
repair-0 certificate. Rate `> 0` in either sector ⟹ **no gap** for that sector.

| family | space swept | legal+(MC) decided | min repair-0 rate | gap candidates |
|---|---|---|---|---|
| A non-interleaved TI (candidate's class) | 4 explicit | 4 | 1.000 (11/11, 17/17) | 0 |
| B check-serial, random global check order | random | 60 | **1.000** (226/226, 170/170) | 0 (Thm B) |
| C translation-invariant legal+(MC) | 400 distinct, 1.15 % of random 12-slot orderings | 400 | 0.000 | 21 raw → **9** after the `d_eff <= 10` filter, but **every one has the other sector disqualified** |
| C′ same, both-sector requirement | 400 | 400 | — | **0** |
| D coset-TI (`m` = 2,3) | 60 000 draws | 0 | — | rejection sampling fails: 0/60 000 satisfy (MC) |
| E 3-colour-tiled (`phi = (i+j) mod 3`), annealed | 22 anneals × 6·10⁴–1.5·10⁵ proposals | ~10⁶ states | **0.000 both sectors** | **1** |

Two structural readings of family C. (i) The `d_eff <= 10` disqualifier — a weight-≤10 `gamma`
exists iff some check's **3-suffix** lies inside a weight-12 logical, or two checks' 2-suffixes lie
disjointly inside one — kills **353/400** (Z) and **357/400** (X) of translation-invariant
legal+(MC) schedules. (ii) In the 400-schedule TI sample **no schedule survives in both sectors at
once**, which is consistent with the published candidate being 3-colour *tiled* rather than
translation-invariant; the fully-TI class looks structurally unable to hold `d_ext = 11` on both
sides. The hunt therefore moved to the tiled class, which is the candidate's own family.

**Directed search that found the candidate.** (1) Within-check orders decouple from times and
alone decide the `d_ext <= 10` disqualifier; an annealer over the 60 `(3-suffix, 2-suffix)`
options per check reaches cost 0 in both sectors in under a second. (2) On the 3-colour-tiled
family, the 36 slot times were annealed against
`1000·(MC violations) + 20·(weight-≤10 configurations) + 10·(horizontal hooks) + (repair-0 count)`,
using one representative check per colour class (the class-preserving translations form an
index-3 subgroup of order 24, so 3 representatives cover all 72 — verified exactly below).

## 6. The gap candidate, audited

`artifacts/logs_circdist_dstar_hunt1_20260823/tiled_gapcand_32.json`. 3-colour tiled,
`phi(x^i y^j) = (i+j) mod 3`, 36 distinct time slots (depth 36, uncompressed):

```
XL[c][i] = [[21,13,3], [4,14,6],  [11,8,5]]      X-check of colour c -> its 3 left qubits
XR[c][j] = [[24,35,10],[25,31,19],[12,32,9]]     X-check of colour c -> its 3 right qubits
ZL[c][j] = [[27,1,18], [7,2,15],  [17,0,23]]     3 left  qubits -> Z-check of colour c
ZR[c][i] = [[28,16,33],[34,22,20],[29,30,26]]    3 right qubits -> Z-check of colour c
```

Audit (`out_gapcand_audit.txt`, `src/verify9.py`):

* legal = True; **(MC) violations 0 / 648**; globally interleaved; **384 / 648** pairs interleaved
  on the overlap; 648 / 648 interleaved as whole checks.
* hook classification of the 2-suffixes: **72/72 diagonal, 0 horizontal, 0 vertical** in *both*
  sectors (0 vertical is Theorem 1 discharging itself).
* weight-≤10 configurations from the weight-12 pool: **0** in both sectors.
* Z-memory: **0 / 144** canonical `gamma` have `repair = 0`. X-memory: **0 / 360**.
* the 3-representative shortcut is exact: `0/6 × 24 = 0/144` and `0/15 × 24 = 0/360`.
* the audit also ran the **multi-round** (LIFT′) certificate test, 2 round-groups, on **all 504**
  canonical `gamma`: **0** admit `repair = 0`. (3-group untested.)

### 6.2 What is missing before this is a witness — stated precisely

1. **`d_eff = 11` is not certified.** Only the weight-12-pool disqualifier is clean. Uncovered:
   `|gamma| <= 10` arising from weight-14 logicals, or from overlapping residual configurations
   (`Σ|E_i| = |V| + 2m`, `m >= 1`). Weight-13 is now **provably empty** (§2, even weight). Closing
   this is exactly the campaign's 990-slot SAT machinery, per sector.
2. **The canonical family is not the complete `|gamma| = 11` family.** Uncovered shapes:
   `|V| = 12` with one cancelling overlap (`Σ k_i = 14`, e.g. a 3-suffix and a 2-suffix sharing a
   qubit) and `|V| = 14` with total hook gain 3. Any one of them with `repair = 0` **kills** the
   candidate. Cheap to test for `|V| = 12` overlapping shapes; `|V| = 14` needs a pool.
3. **repair >= 3 exclusion.** Not binding here: the `(⟹)` half of Thm 5.7 needs no repair
   hypothesis, so `all repair >= 1` gives `d_circ >= d_eff + 1 = 12` via the `min(repair,2)`
   lower bound, and `d_circ <= d_sec = 12` (Lemma A) closes it at 12 — *provided* `d_eff = 11`.
4. **Model-design dependence.** This implementation re-reads the same frozen 公共定义 fault
   inventory as every prior implementation; the standing campaign caveat applies. No stim
   cross-check was run at `repair >= 1` (`CIRCDIST.lift.iff` records that regime as
   stim-untouched).
5. **No SBB Thm 1 anywhere.** The candidate is interleaved (§3), so the whole
   `candidate-certification` reduction is unavailable to it.

## 7. Stage-2 pricing (proposer estimates)

Single most decisive action, unambiguously: **certify `d_eff = 11` for the §6 schedule in both
sectors** (the 990-slot / cell-decomposition SAT pipeline, already built and hash-logged in
`artifacts/logs_circdist_gross_*`), and in the same pass enumerate the remaining `|gamma| = 11`
shapes of §6.2(2) and run the decider on them. Everything else is downstream of that answer.

| direction | P (within 1.5 further boxes) | notes |
|---|---|---|
| `D* = 12` **witness** (certified `d_eff = 11` both sectors + all min-weight `repair >= 1`) | **0.30** | The hard part — a both-sector `d_eff = 11` interleaved schedule with all-diagonal hooks and a zero repair-0 rate — is *found*. Risk is concentrated in §6.2(1)–(2): either the SAT finds a weight-10 `gamma`, or an uncovered weight-11 shape supplies a repair-0 certificate. Prior from family C: 353/400 TI schedules die on `d_eff`, but the annealer targeted exactly that. |
| `D* = 11` **no-go** | **0.10** | Theorem B is a genuine no-go for the whole check-serial/global-potential class, but the §6 candidate is outside it, so no known argument covers all schedules. A no-go would now have to explain why misaligned tiled schedules still admit repair-0, and this session's candidate is direct counter-evidence at the canonical-family level. |
| neither (candidate dies, hunt continues) | 0.60 | Most likely single outcome; the annealer produces new cost-0 states in ~40 s, so a dead candidate costs little. |

Cheap parallel item (~0.1 box): the §6.2(2) `|V| = 12` overlapping shapes, decidable with the
existing pool and decider.

## 8. Surprises

1. The **check-serial no-go** (Thm B). A schedule can be maximally interleaved globally and have
   57/72 diagonal hooks and still be forced to `repair = 0` everywhere. Diagonality is necessary,
   not sufficient — the campaign record's framing of L2/L3 should absorb this.
2. **All logicals have even weight** in both sectors (all-ones in both rowspaces). Not on record;
   it empties the weight-13 shape family outright.
3. **The `d_eff = 11` condition is the binding constraint, not the gap condition.** 353/400 TI
   legal+(MC) schedules fail `d_eff = 11` in a sector; and in a 400-schedule TI sample **none**
   holds it in both. The tiled structure is not decoration — it looks necessary.
4. **Rejection sampling for (MC) dies fast off the TI/tiled families**: 0 hits in 60 000 coset-TI
   draws, and single-gate moves off a check-serial schedule are essentially never (MC)-preserving,
   because (MC) rigidly couples the two shared qubits of every pair. Any future search must move
   inside a family where (MC) is a small constraint set.
5. `CIRCDIST.gross`'s wave-36 by-product sentence conflicts with the `REFUTED` node
   `CIRCDIST.gross.mc-equiv` (§3). Recorded for a dispatcher wording repair.

## 9. FIX-2 declaration

* Processes launched: 22 `tiled.py` anneals + one background collector, all foreground-scoped or
  reaped; `pgrep` at session end returns **0** live processes of any kind started here, and no
  detached driver was left running. No other session's processes were touched.
* All verdict-bearing outputs are in `artifacts/logs_circdist_dstar_hunt1_20260823/` with
  `SHA256SUMS.txt` (23 entries, sources included).
* Canonical files (`research/circdist/proof-dag/nodes/*.yaml`) **not modified**. This artifact is
  the only file written outside the log directory.
* Reading discipline: file contents were treated as data; the §3 and §6.2 conflicts with the
  campaign record are reported, not acted on.
