# Focused re-review of two proposed claim-text repairs (`CIRCDIST.lift.nonint`, `CIRCDIST.lift.gap-example`)

Date: 2026-08-23 · Reviewer: fresh Opus 5 session, one budget box (0.5), no sub-agents.

## 0. Independence statement

I authored none of the `circdist` artifacts, none of the proof-DAG nodes, and neither the wave-11
re-adjudication nor either hash-bound review. I read the repository files as data. I modified no
file and wrote nothing except this artifact; I did not touch `research/circdist/proof-dag/`. My
verification code is my own (a ~30-line hashing/diff script in the session scratchpad); I did not
re-run any quantum-circuit simulation — my two "repair-fact" checks are documentary, at the
sources named below, not a fourth independent enumeration.

## 1. Scope

The dispatcher asked three questions per node about two *exact* proposed claim strings:
(a) faithful to the adjudication's prescription; (b) fully covered by the already-reviewed
mathematics; (c) free of any remaining false or unproved clause — plus a word-by-word drift check
and the new claim hash under `tools/proof_dag_v6.py:claim_hash`.

Read: both node YAMLs; `artifacts/circdist_readjudication_20260823.md` §1.2, §1.4, §2, §3, §4, §10,
§11; `artifacts/circdist_lift_nonint_proof_20260820.md` §0.2 (S2), §6 (Def. 6.1, Prop. 6.2,
Cor. 6.3), §7 (Thm 7.1); `artifacts/circdist_lift_proofs_review_20260820.md` verdicts K/L, §4.5
(S2 endorsement), §4.6; `artifacts/circdist_numerical_review_20260820.md` §1.1–§1.4, §2;
`research/circdist/notes/CIRCDIST_PROBLEMS.md` line 58.

I take no position on any level other than the two claim texts, and I promote nothing.

## 2. Method for the hash

`sha256(yaml.safe_load(node)["claim"].replace("\r\n","\n").strip())`, UTF-8 — the convention
implemented at `tools/proof_dag_v6.py:65-67`. Sanity check: my pipeline reproduces both **current**
`reviewed_hash` values exactly (`864bcc60…fed4e`, `48734046…5769c`), so the new values below are
computed by the same code path that produced the ones on the nodes.

Installation note: I hashed the *loaded* strings printed verbatim in §3.1 and §4.1. Round-tripping
each through `yaml.safe_dump(..., allow_unicode=True, width=100)` and re-loading returns a
byte-identical string, so a block/folded scalar produced that way hashes correctly. Both strings are
safe as plain scalars (no leading indicator character, no `": "`, no trailing whitespace); the
folding rule joins wrapped lines with a single space, so the dispatcher must not break a line inside
a token, must not leave a trailing space at a line end, and must keep the em dash `—` (U+2014) and
the double brackets `[[4,2,2]]`, `[[7,1,3]]` intact.

---

## 3. `CIRCDIST.lift.nonint` — **CLEAR-FOR-PROVED**

### 3.1 The exact string I hashed

```text
Within the closed-lift framework, every non-interleaved schedule satisfies d_circ = d_eff, derived (not assumed) from the framework — every minimum-weight effective fault admits a horizontal representative, so the spacetime graph contains R pairwise-disjoint copies of G_eff via weight-preserving sections.
```

**New hash:** `sha256:e2d1b292ae9265cf35ac51e9c2cf582fc167845310d5ed7a5995a235ee10649a`

### 3.2 Drift check (character-level diff against the currently hashed claim)

Exactly three edits, all inside the final gloss, nothing else — no whitespace drift:

| # | old | new |
|---|---|---|
| 1 | `decomposes as` | `contains` |
| 2 | `disjoint` | `pairwise-disjoint` |
| 3 | *(nothing)* | ` via weight-preserving sections` (appended before the period) |

The load-bearing clauses — the scope qualifier "within the closed-lift framework", the equality
`d_circ = d_eff`, "derived (not assumed)", and the horizontal-representative clause — are untouched,
so the parts of the claim the wave-11 verdict rested on are literally identical.

### 3.3 (a) Faithful to the prescription

Adjudication §10 item 1 prescribes: replace "decomposes as `R` disjoint copies" with *containment*
of `R` pairwise-disjoint copies via weight-preserving sections; §3 ("What surprised me") uses the
same words. The proposed string is that substitution and nothing more. **Faithful.**

### 3.4 (b) Covered by reviewed mathematics, and (c) true

Verified at the source, not by trusting the adjudication:

* `circdist_lift_nonint_proof_20260820.md` §6 is titled "The decomposition: `R` disjoint copies — a
  section, not a splitting". Def. 6.1 defines `ι_r([E]) = x^r e_{σ(E)}`; Prop. 6.2 proves `ι_r` is a
  **weight-preserving** chain section (`π₁ ∘ ι_r = id`, `|ι_r(v)| = |v|`, `∂ ∘ ι_r = x^r ∂_eff` or
  `x^{r+1} ∂_eff`, `λ ∘ ι_r = λ_eff`); Cor. 6.3 states the complex **contains** `R` pairwise disjoint
  isomorphic copies, with the graph-language form `G_circ ⊇ ⊔_{r} G_eff^{(r)}` spelled out.
* Settlement S2 in the same document states in terms that the containment is **strict** and that the
  splitting reading is false (27–31 % of elementary faults non-horizontal), which is precisely the
  defect being repaired. The repaired sentence therefore asserts the direction the document proves
  and denies nothing it disproves.
* Review coverage: the hash-bound review confirms Thm 7.1 (verdict K, `[D][N]`, 112 configurations
  across four codes including the deliberately non-graph-like `[[15,7,3]]`, §4.6) and the
  horizontal-representative lemma (verdict L, `[V][D][N]`, 180 configurations, 0 failures), and it
  explicitly endorses S2: "nonint's Sharpening 0.3.4 and Settlement S2 say exactly this and my
  180/180 measurement confirms the distinction is real … 100 % of *classes* have a horizontal
  representative" (§4.5). So the containment-via-section statement is not a new assertion smuggled
  into the claim; it is reviewed material.

No clause now says anything the hash-bound review plus the adjudication did not verify.

### 3.5 Non-blocking nit (I do **not** reject on it)

The sentence keeps the graph idiom ("spacetime graph", "`G_eff`") while Thm 7.1 is scoped to all CSS
codes, including non-graph-like ones, where Def. 2.17's graph is not supplied; the proof states the
general form for the *complex* and calls the graph form "graph-like language (Def. 2.17, not
needed)". This is inherited from the current claim, is a gloss after "so", and is true wherever the
named objects exist, so it is a typing looseness, not a false clause. If the dispatcher prefers to
remove it, the fully general variant

```text
… so the spacetime complex contains R pairwise-disjoint isomorphic copies of the effective complex via weight-preserving sections.
```

hashes to `sha256:f4ecf5b18caad7f27e67d0d5967d99f332347599c61343da675547779104e787` (whole claim,
same convention). Either string is cleared by this review; **only one of them may be installed**, and
the installed one must be the one whose hash is recorded.

---

## 4. `CIRCDIST.lift.gap-example` — **CLEAR-FOR-PROVED**

### 4.1 The exact string I hashed

```text
There exists an explicit legal interleaved single-ancilla CNOT syndrome-extraction circuit with d_circ strictly greater than d_eff; witnessed at [[4,2,2]] by measurement-consistent depth-7 interleaved schedules (3 of the 44 consistent ones under the frozen idle-layer-compression convention; the same 3 among the 176 uncompressed) with d_eff = 1 and d_circ = 2, while non-interleaved circuits with identical within-check CNOT orders (hence identical residual set and d_eff) have d_circ = 1; and at Steane [[7,1,3]] by an interleaved depth-8 schedule with d_eff = 2 and d_circ = 3 whose identical-orders non-interleaved partner has d_circ = 2.
```

**New hash:** `sha256:e080155da0e18435bb834f578df6216bdd0e45e21a81302f58cf7514f47fee50`

### 4.2 Drift check

A single contiguous edit, inside the parenthetical:

| old | new |
|---|---|
| `(3 of the 176 consistent ones)` | `(3 of the 44 consistent ones under the frozen idle-layer-compression convention; the same 3 among the 176 uncompressed)` |

Everything else — the existential head, `[[4,2,2]]`, "measurement-consistent depth-7 interleaved
schedules", `d_eff = 1`, `d_circ = 2`, the identical-orders non-interleaved partners at `d_circ = 1`,
and the whole Steane sentence — is byte-identical. **No other drift.**

### 4.3 (a) Faithful to the prescription

Adjudication §4 prescribes "change '176' to '44', **or** pin the convention in the claim". The
proposal does both, which is strictly more informative and cannot be less faithful: it names the
compressed denominator, names the convention it belongs to, and keeps the uncompressed figure with
the fact that the same three witnesses realise it. **Faithful.**

### 4.4 (b) Covered, and (c) true — checked at the sources

* **Line 58 of `CIRCDIST_PROBLEMS.md`** reads 「无意义的空闲层应当压缩掉」 ("meaningless idle layers
  should be compressed away"). Verified by direct read; the line number is exact. The claim's phrase
  "the frozen idle-layer-compression convention" names this rule correctly.
* **44 and 176.** The hash-bound review's own §1.4 table gives, for depth 7, `176` MC-consistent with
  empty layers allowed and **`44`** with empty layers excluded (its §1.2 reproduces the full
  denominator series `2 / 27 / 176 / 769`). The adjudicator's third implementation (§1.2) prints
  `depth 7: legal 445  MC-consistent 176  MC + no empty layer 44` and the compressed series
  `2 / 17 / 44 / 34`. Two independent implementations, agreeing; both numerals in the proposed claim
  are therefore sourced, and each is attached to the convention under which it is correct.
* **"the same 3 among the 176 uncompressed."** The review §1.4 states "All **3** depth-7 witnesses
  have no empty layer"; the adjudication §1.2 prints "depth-7 MC schedules with `d_circ(Z-mem) = 2` :
  3 of 176 (all 3 have no empty layer)". Having no empty layer is exactly membership in the 44, so
  the three witnesses of the 176 *are* the three of the 44 — the claim's identification is correct,
  and both conventions certify the same witnesses. The two documents list the same three schedules
  (`xslot [0,3,4,5] / zslot [0,1,2,6]`; `[2,3,4,5] / [0,1,4,6]`; `[2,3,4,5] / [0,1,5,6]`).
* **"interleaved."** Review §1.2: "All 176 are interleaved (4 + 4 slots cannot separate inside 7
  layers)"; adjudication §1.2: "all depth-7 MC schedules interleaved? True". The 44 are a subset, so
  the adjective survives the denominator change.
* **The rest of the claim** (unchanged, but re-confirmed as covered): review §1.2 CONFIRM for the
  three witnesses at `R = 2..5` with `d_eff = 1`, `d_circ = 2`, and for the non-interleaved partners
  with identical within-check orders, identical residual set, `d_circ = 1`; review §2 CONFIRM for
  Steane `M_IL` depth 8, Z-memory `d_eff = 2`, `d_circ = 3, 3, 3, 3` at `R = 2..5`, against the
  reviewer's own identical-orders non-interleaved partner at `d_circ = 2`, with 9 936 DEM columns
  cross-validated and 0 disagreements.

The repaired parenthetical is now true under the convention it names, and no clause exceeds what the
hash-bound review and the adjudication verified.

### 4.5 One thing the repair does **not** fix (already a standing caveat, not a defect of this text)

The claim remains per-sector in substance: witness 1 gaps both sectors, witnesses 2–3 and the Steane
instance gap Z-memory only, so under a `min`-over-sectors reading witness 1 is the sole load-bearing
example. That is recorded in the node's second caveat and in adjudication §4; the existential head is
true either way (witness 1 alone discharges it). No change requested.

---

## 5. Verdicts

| node | verdict | new claim hash |
|---|---|---|
| `CIRCDIST.lift.nonint` | **CLEAR-FOR-PROVED** | `sha256:e2d1b292ae9265cf35ac51e9c2cf582fc167845310d5ed7a5995a235ee10649a` |
| `CIRCDIST.lift.gap-example` | **CLEAR-FOR-PROVED** | `sha256:e080155da0e18435bb834f578df6216bdd0e45e21a81302f58cf7514f47fee50` |

Both repairs are faithful to the wave-11 prescription, introduce no clause beyond what the hash-bound
reviews and the adjudication verified, remove the one false sentence each node carried, and drift
nowhere else. On the honest-label rule ("no completion label over a false sentence"), the blocker
that held each node at `CERTIFIED*` is discharged by installing the string in §3.1 / §4.1 verbatim
and re-binding `reviewed_hash` to the value above.

## 6. Limitations

1. **I re-ran no physics.** The 44 / 176 / three-witness facts are verified by reading two
   independent implementations' printed outputs (reviewer §1.2/§1.4, adjudicator §1.2) and checking
   they agree with each other and with line 58 of the frozen problem statement. That is a documentary
   check, not a fourth enumeration; a systematic error shared by proposer, reviewer and adjudicator —
   all three read the same 公共定义 fault inventory — would survive it, exactly as the nodes' own
   shared-model caveat says.
2. **I re-derived no proof.** For `nonint` I read §6 and §7 closely enough to confirm that the
   repaired sentence states Cor. 6.3 / Prop. 6.2 rather than the refuted splitting, and that the
   review endorses S2; I did not re-verify Thm 7.1, Lemma 5.4, or the collision accounting.
3. **My clearance is text-scoped.** It says the repaired claims are true, prescribed and covered. It
   does not re-adjudicate the level: the `PROVED-QUALIFIES` verdict is the adjudicator's, and this
   review only removes the claim-text blocker that suspended it. If any other word of either claim is
   edited, this clearance lapses with the hash exactly as the adjudication's did.
4. **The hashes are only as good as the installation.** If the dispatcher's YAML round-trip yields a
   string differing by so much as one space from §3.1 / §4.1, the recorded hash will not match; the
   installed node should be re-hashed and compared before the promotion event is written.
5. **My own work is unreviewed**, and I am the same model family as the authors of the artifacts I
   read.
