# Independent §7.10 review — SE tier-1 Lean development (`se/lean/`)

## Provenance

- **Reviewer:** fresh Opus 5 subagent, spawned 2026-07-30 by the coordinating agent for this
  review only.
- **Independence statement (DAG_PROTOCOL §3 rule 6):** I did not author any part of the Lean
  development, the node `lean:` metadata, the build artifacts, or the report under review; I was
  given no wanted outcome and no verdict was suggested to me. My commission named the checklist,
  not the answer.
- **Reviewed objects (all read from disk, 2026-07-30):**
  - development: `se/lean/` (19 `.lean` files incl. `lakefile.lean`, `README.md`);
  - build evidence: `se/artifacts/logs_se_lean_20260730/`;
  - report: `se/artifacts/se_lean_t1_20260730.md`;
  - prose sources: `se/proof-dag/nodes/*.md` (frontmatter `composition:` +
    `## Composition proof` + `## Claim`), `se/proof-dag/NODE_INDEX.md`;
  - manuscript: `se/paper/se_explicit_witness.tex` (Theorem B `thm:main`,
    Conjecture H `conj:H`, Prop. `lem:omega-lower`).
- **Governing rules re-read in full before work:** `DAG_PROTOCOL.md` (esp. §2, §3 rules
  1–8, §7 incl. §7.10), `research/RESEARCH_STRUCTURE_PROTOCOL.md`,
  `research/PRETASK_RELOAD_PROMPT.md`, `se/README.md`,
  `se/proof-dag/nodes/SE.formal.t1.yaml`.
- **Write footprint of this review:** this file only. No node file, no `.lean` source, no artifact
  was modified. The only side effect on disk is the regenerated *gitignored* build cache
  `se/lean/.lake/build/` (wiped and rebuilt by me for V1); no tracked file
  changed.
- **Conflicts between commission text and disk protocols:** none.

### Pre-action position (recorded before work)

- Target node `SE.formal.t1`, status on disk **OPEN** (`role: tool`, non-propagating).
- Role: **reviewer**.
- Highest status my evidence could license: this review is the rule-6/rule-7 gate for the T1
  development's own evidence. A green build is run evidence and caps at **NUMERICAL** under §2;
  nothing here can raise `SE.goal`, `SE.br`, `SE.denom`, `SE.denom.Phi.legal.tame`, or any H1–H4
  node, because those are conditional on hypotheses this development assumes. The status write
  itself belongs to the proposer/coordinator, citing this artifact.

### Independent tooling I wrote and ran (inlined below so this review is reproducible)

1. My own frozen-Claim hasher, implemented from the freeze *rule sentence* in the report
   (`## Claim` section, UTF-8, CRLF→LF, stripped) **without reading** the executor's
   `claim_hashes.py` (rule 7c, anchoring ban) — §V3 below.
2. My own SHA-ledger verifier — §V6.
3. `RevAudit.lean`, run via `lake env lean` against the built project (it adds nothing to the
   project): an **exhaustive** axiom census over every `SE` declaration, signature prints, and a
   **from-scratch counter-model** proving that hypothesis H4 is load-bearing — §V2, §V5.

---

## V1 — Build reproduction  **PASS**

I wiped the SE build outputs (`.lake/build/lib/lean/SE*`, `.lake/build/ir/SE*`) and ran the
build myself:

```
cd se/proof-dag/lean && lake build        # Lake 5.0.0-src+68218e8 (Lean 4.31.0)
...
✔ [3055/3056] Built SE (25s)
Build completed successfully (3056 jobs).
exit=0
```

- True exit status: **0**. Job count **3056**, matching
  `se/artifacts/logs_se_lean_20260730/lake_build_transcript.txt:58`.
- **Zero** `error`/`warning`/`failed` lines in my transcript (the archived
  `lake_build_run2_with_lint_warning.txt` correctly preserves the earlier one-lint run; the
  fix-cycle record is honest).
- Toolchain matches the pin: `lean-toolchain` = `leanprover/lean4:v4.31.0`, `lakefile.lean:15`
  requires Mathlib `@ "v4.31.0"`.
- **Axiom output comparison:** I extracted the 33 `depends on axioms` lines from *my* run and
  diffed them against `se/artifacts/logs_se_lean_20260730/print_axioms.txt` (both normalized by
  stripping the `info: SE/Trust.lean:L:C:` prefix and sorting): **identical, 33/33**, every one
  exactly `[propext, Classical.choice, Quot.sound]`.

## V2 — Axiom / hole census  **PASS (stronger than the archived census)**

**Text search** over the tree (`grep -rn`, excluding `.lake/`) for
`sorry`, `axiom`, `native_decide`, `implemented_by`, `opaque`, `extern`: every hit is inside a
comment or docstring (e.g. `SE/Trust.lean:11`, `SE/SelfTest.lean:10`, `SE/Support/Cbrt.lean:9`).
**No declaration** in the development is a `sorry`, an `axiom`, an `opaque`, or uses
`native_decide`/`implemented_by`. This matches `SE/Trust.lean` §§A–E and §E's "None".

**Machine census.** `SE/Trust.lean:134-166` prints axioms for 33 *hand-picked* names. §7.10 item 2
asks for every top theorem, and the development contains many more theorems than 33 (e.g.
`SE.K_pow_le`, `SE.rpow_sub_one_le_K`, `SE.envBound_pos`, `SE.abs_beta_le_one`,
`SE.one_le_distort`, `SE.Mconst_split`, …). I therefore ran an exhaustive scan rather than trusting
the list:

```lean
run_cmd do
  let env ← Lean.getEnv
  let mut scanned := 0; let mut bad : Array Name := #[]; let mut sorried : Array Name := #[]
  for (n, _) in env.constants.toList do
    if (`SE).isPrefixOf n && !n.isInternal then
      scanned := scanned + 1
      let ax ← Lean.collectAxioms n
      for a in ax do
        if a == ``sorryAx then sorried := sorried.push n
        else if a != ``propext && a != ``Classical.choice && a != ``Quot.sound then
          bad := bad.push n
  Lean.logInfo s!"REVIEW-A scanned={scanned} nonstandard={bad.size} {bad} sorryAx={sorried.size} {sorried}"
```

Result:

```
REVIEW-A scanned=163 nonstandard=0 #[] sorryAx=0 #[]
```

**163** `SE.*` declarations, **0** non-standard axiom dependencies, **0** `sorryAx`. Nothing sits
outside `Trust.lean`'s trust boundary. PASS.

*Observation (not a defect):* the 33-name census is a proper subset of the environment; the report
describes it as "every top-level theorem in `SE/Trust.lean`'s census", which is true but circular.
Suggest replacing it with the environment-scanning `run_cmd` above so the census cannot silently
fall behind the file.

## V3 — Faithfulness of the nine node modules  **PASS with two findings (F1, F2)**

### V3.a Docstring metadata (node id, dated status, verbatim frozen Claim, hash) — PASS

All nine node modules carry the node id, node-file path, kind/role, parents/children, an
epistemic status explicitly dated "read from the node file on 2026-07-30", and the frozen Claim
quoted verbatim: `SE/goal.lean:7-24`, `SE/br.lean:6-19`, `SE/denom.lean:8-21`,
`SE/denom/taper.lean:5-15`, `SE/denom/Phi/legal/tame.lean:7-25`,
`SE/denom/Phi/legal/trace/t6.lean:6-37`, `.../gram/interface.lean:6-27`,
`.../omega/interface.lean:6-24`, `.../sect.lean:6-29`. I compared each quoted block
character-by-character against the node file's `## Claim` section: **all nine verbatim**, with the
only difference being the declared uniform indentation, which each module states explicitly and
excludes from the hash.

### V3.b Hash recomputation (my own implementation of the freeze rule) — PASS, 10/10

```python
def claim_section(path):
    raw = path.read_bytes().decode("utf-8").replace("\r\n", "\n")
    m = re.search(r"^## Claim\n(.*?)(?=^## )", raw, re.S | re.M)
    return m.group(1).strip()
sha256(claim_section(p).encode("utf-8")).hexdigest()
```

| node | recomputed sha256 | vs module docstring / `lean.claim_hash` / report table |
|---|---|---|
| `SE.goal` | `cb578c2f…5362` | MATCH |
| `SE.br` | `01590f3f…5e63` | MATCH |
| `SE.denom` | `c1db854e…4a9b` | MATCH |
| `SE.denom.taper` | `a79e1c59…4a02` | MATCH |
| `SE.denom.Phi.legal.tame` | `a203b64b…23b5` | MATCH |
| `SE.denom.Phi.legal.trace.t6` | `5c485604…b0bd` | MATCH |
| `SE.denom.Phi.legal.gram.interface` | `ee41bc7f…d465` | MATCH |
| `SE.denom.Phi.legal.omega.interface` | `25ff3a77…7a02` | MATCH |
| `SE.denom.Phi.legal.sect` | `0ef0e835…f401` | MATCH |
| `SE.denom.assembly.envelope` | `b7d6f765…bd6c` | MATCH |

Ten independent recomputations, ten matches, three-way consistent (module docstring, node
frontmatter, report table). No node drift.

### V3.c Lean `Claim` vs prose Claim — PASS for eight, **F1 for `sect`**

- **`goal.Claim`** (`SE/goal.lean:74-78`) renders the frozen `Ω(n^{1/3})` as the explicit
  `Tendsto (epsB ρ) atTop (𝓝 0) ∧ ∀ n ≥ 27, (C − ε_n)·n^{1/3} ≤ adv n`. Explicit ⇒ **stronger**
  than the frozen `Ω(·)`; no quantifier dropped. The "explicit witness" half of the frozen Claim is
  *not* rendered, which the module says in its own words (`SE/goal.lean:33-35`) — an honest
  under-claim, not a weakening.
- **`br.Claim`** (`SE/br.lean:62-64`) is the ratio bound only; the ratio → `Adv±` passage is
  deliberately in the GOAL route (declared `SE/br.lean:22-30`). Matches where the prose block on
  `SE.goal.yaml:75-86` draws the boundary. No weakening.
- **`denom.Claim`** (`SE/denom.lean:85-86`) renders the frozen `O(1)` as `maskNorm ≤ 2·envBound`,
  explicit ⇒ stronger.
- **`taper.Claim`** (`SE/denom/taper.lean:157-159`) renders conjuncts 1 and 3 of three; conjunct 2
  (TIGHT `|a_k| ≤ √(n/k)`) is **not** rendered. This is a *proper fragment* of a node whose status
  is PROVED, and it is declared three times (`taper.lean:18-34`, `Trust.lean:92-95`, report R2,
  node `lean.rel`). Acceptable as declared; see F5 for where the caveat still gets lost.
- **`tame.Claim`** (`.../tame.lean:78-81`) legitimately differs in *form* from a frozen status
  line, and renders paper eq:omega-lower-global. Declared (`tame.lean:28-36`, report §"differ" 1).
- **H1** (`t6.lean:67-69`): norm shadow `‖M_ξ‖ ≤ (15/4)B²ω` of the PSD statement
  `M_ξ ⪯ (15/4)B²ω I_c`. With `mxi_nonneg` (`Interface.lean:153`) the frozen Claim **implies** the
  shadow; same quantifier ("every admissible strict sector"). Safe direction. The joint-trace
  identity and the (CT)/(JT) targets are correctly *not* assumed.
- **H2** (`gram/interface.lean:58-61`): norm consequence of the operator identity; the scalar
  `r_top/(B²ω)` is positive by `rtop_pos`/`bthe_pos`/`omega_pos`, so no absolute value is lost.
  The Schur lift is invisible — declared loudly (`gram/interface.lean:36-40`, README item 3).
- **H3** (`omega/interface.lean:54-58`): (i) is the *submultiplicative consequence* of the frozen
  identity (an inequality — weaker as a hypothesis, hence safe), (ii) the polar norm equality.
  Both parts present, matching the node's two-part statement.

**F1 (MEDIUM) — the H4 hypothesis is strictly stronger than Conjecture H(H4); the report's
"frozen ⟹ shadow" sentence is not established for H4.**

`sect.Claim` (`SE/denom/Phi/legal/sect.lean:63-64`) is

```lean
∀ n j B, 0 ≤ B → (∀ s, F.admissible n j s → F.csectS n j s ≤ B) → F.cLower n j ≤ B
```

— quantified over **all** `n, j`. The frozen prose (node `SE.denom.Phi.legal.sect.yaml`, `## Claim`;
paper `conj:H`, `se_explicit_witness.tex:1298-1299`) says "**For every active `j`**", inside a
conjecture whose preamble fixes `j ≥ 1` and `n ≥ 3j` (`se_explicit_witness.tex:1213-1216`), and the
proposition that consumes it is scoped `1 ≤ j < K−1, n ≥ 3j`
(`se_explicit_witness.tex:1805-1807`). So Conjecture H does **not** imply the Lean hypothesis:
at `j = 0` and at `j ≥ K−1` the Lean hypothesis asserts something the frozen Claim is silent about
(at a level with no admissible sector it forces `cLower n j ≤ 0`).

This is *used*, not merely stated: `tame.composition` applies `h4` at every `j` with `j < n`
(`tame.lean:169-174`), and `denom.block_le` invokes `htame` at every `d` with `1 ≤ d < K n`
(`denom.lean:163`), which includes the endpoint `d = K−1` outside the paper's active range (there
the coefficient `alpha (K n) (d+1) = 0`, so the extra strength is mathematically harmless — but it
is still assumed).

Consequences: (a) `se/artifacts/se_lean_t1_20260730.md:123-126` ("the implication runs the safe way
(frozen Claim ⟹ shadow), so a theorem proved from the shadows is proved from the Claims") is
**inaccurate for H4**; (b) `tame.Claim`'s conclusion is correspondingly stated for all `j < n`,
strictly wider than paper eq:omega-lower-global's `1 ≤ j < K−1`. Nothing proved is wrong; the
*conditionality* is on a stronger conjecture than the manuscript's. Also a rule-7g point: "active
`j`" is a term of art that resolves to no definition in `conj:H` or on the node — only to a
parenthetical in the proof of `lem:omega-lower`.

**F2 (MINOR) — stale Lean pointer in a node's composition metadata.**
`se/proof-dag/nodes/SE.denom.Phi.legal.tame.yaml:14` still reads
`… Lean mirror in se/lean (SE/Assembly.lean: gcan_le -> csect_le -> cLower_le), pending
restructure to proof-dag/lean`. Both the directory `se/lean/` and `SE/Assembly.lean` no
longer exist (verified on disk); the restructure is complete. A reader of that node is pointed at a
deleted file.

### V3.d Composition hypothesis lists vs prose blocks and `lean.rel` — PASS (as declared)

Signatures printed from the built environment (my `#check`):

```
@SE.goal.composition_via_br : ∀ {F}, F.Cited → SE.br.Claim F → SE.goal.Claim F
@SE.br.composition          : ∀ {F}, F.Cited → SE.denom.Claim F → SE.br.Claim F
@SE.denom.composition       : ∀ {F}, F.Cited → SE.denom.taper.Claim → SE.denom.Phi.legal.tame.Claim F → SE.denom.Claim F
@SE.denom.Phi.legal.tame.composition :
  ∀ {F}, F.Cited → t6.Claim F → gram.interface.Claim F → omega.interface.Claim F → sect.Claim F → tame.Claim F
SE.denom.taper.holds        : SE.denom.taper.Claim
```

No undeclared premise appears anywhere: every non-child premise is either `F.Cited` (each field
named to its manuscript label *and* its node in `SE/Interface.lean:91-159`) or a declared
grandchild. Cross-check against the prose:

- `tame`: prose block (`SE.denom.Phi.legal.tame.yaml`, `## Composition proof`, four links H1→H4 plus
  "found supplies the typed objects") ↔ Lean premises `t6/gram.interface/omega.interface/sect`
  + `Cited`; `found` unrendered with its rule-7b `c≥2` caveat carried in the header
  (`tame.lean:53-59`), in `Trust.lean:96-100`, and in the node's `lean.rel`. Consistent.
- `denom`: prose steps 1–5 ↔ `Cited.mask_from_D` (1–2), `block_le` (3+5), `Cited.defect_orth` (4),
  `taper.Claim` conj. 1, `tame.Claim`. The five cited children are mapped field-by-field in
  `denom.lean:44-58`, matching `Trust.lean` §D3 and the node's `lean.rel`. Consistent. (One
  looseness: the prose step 5 names the *discrete* maximum `max_d d(K−d−1)=⌊(K−1)²/4⌋`, which is
  Theorem-A arithmetic; the conditional Lean route instead uses the continuous
  `(1−x)√x ≤ 2√3/9` of `Support/Envelope.lean`. `SE.taper_max` exists and is axiom-clean but is not
  on the Theorem-B path. Not a defect — worth one clarifying sentence.)
- `goal`: one route only; `ros` REFUTED/DEAD, `mdh`/`sdp`/`jz` have `proof: null` on
  `SE.goal.yaml:20-43`, so there is no prose route proof to mirror — R5's reasoning is correct, and
  rendering one would have invented content.
- `br`: `num`/`def` enter as `Cited.numerator`/`Cited.maskNorm_pos` (D5), which is faithful to the
  node's own prose.

## V4 — Conclusion fidelity vs the manuscript's Theorem B  **PASS**

Paper (`se_explicit_witness.tex:156-168`): assuming Conjecture H, for `q = 2n`,
`Adv(SE(n,2n)) ≥ (9/(18+4√6+3√10) − o(1))·n^{1/3}`, constant printed as
`0.2413852814754581733…`.

Lean `SE.goal.Claim` (`goal.lean:74-78`) with `Cconst := 9/(18+4√6+3√10)` (`Support/Defs.lean:53`):

| paper | Lean | verdict |
|---|---|---|
| constant `9/(18+4√6+3√10)` | `Cconst`, *and* `SE.Cconst_digits` pins `0.2413852814754581732 < C < 0.2413852814754581734` (`Support/Constants.lean:135-149`) | equal, plus a 19-digit certificate the paper only asserts |
| `q = 2n` | carried by the carrier convention (`Interface.lean:29-31`), no separate `q` at tier 1 | faithful, declared |
| `− o(1)` (asymptotic, no window) | explicit `ε_n = epsB ρ n` **with** `Tendsto … (𝓝 0)` proved, holding for **every** `n ≥ 27` | **stronger** |
| window | `n ≥ 27` ⇔ `K ≥ 3`, matching "empty for `n<27`; first active tuple `(K,n,j)=(3,27,1)`" (`:1864`, `:1898-1900`) | consistent |
| uniformity in `i`, `θ`, LR `c ≥ 1` | in `i` inside `Cited.mask_from_D` (paper §9 half-swap transitivity); in `θ` via `rtop_le_rho`; in `c` because the sector index carries `c` and `mxiS/gcanS/csectS` are whole-block norms (`Interface.lean:86-90`) | assumed at the interface, declared; tier 1 cannot check it |
| `1/(2(1+M)) = C`, `M = (4√6+3√10)/18` | `inv_two_one_add_Mconst`, `Mconst_eq` proved (`Constants.lean:70-106`) | equal |

I re-derived the chain myself before reading the proofs: `dNorm ≤ envBound` → `maskNorm ≤ 2·envBound`
→ `K/(2·envBound) ≤ ‖Γ‖/‖Γ∘Δ‖ ≤ adv` → with `n^{1/3} − 1 ≤ K` (`Cbrt.lean:96`) and the algebraic
identity `(C − epsB)·n^{1/3} = (n^{1/3}−1)/(2·envBound)` (`goal.lean:129-133`), the claim follows.
No inequality is reversed; no rendering is weaker than its paper form.

`SE/br.lean` likewise matches paper eq:denfinal `‖Γ_n∘Δ_1‖ ≤ 2(1+M)+o(1)` with the `o(1)` made
explicit via `envBound` and `tendsto_envBound` (`Limits.lean:226`).

## V5 — Vacuity  **PASS with one finding (F3)**

Three separate ways the conditional theorem could be worthless were checked.

1. **Contradictory hypotheses?** No. `SelfTest.emptySectorFrame` and `SelfTest.liveSectorFrame`
   (`SelfTest.lean:125-146`, `216-222`) satisfy `Cited ∧ H1 ∧ H2 ∧ H3 ∧ H4`
   (`hypotheses_consistent`, `hypotheses_consistent_live`), and `liveSectorFrame_goal`
   (`SelfTest.lean:325-330`) runs the **full four-composition chain**
   `tame.composition → denom.composition → br.composition → goal.composition_via_br` on a concrete
   model. I re-ran all of it; it is axiom-clean. The live model is genuinely non-degenerate in the
   *sector* layer: admissible sectors exist for every `1 ≤ j, 3j ≤ n`, `ω` takes the physical
   boundary value `j/(2(n−j))`, and H1 holds **with equality**, so `Cited.omega_le` and H1 are
   exercised at their extreme point rather than slackly.
2. **Hypotheses that do nothing?** I did not accept the report's argument (F-list: "deleting the
   `h4` parameter makes `tame.composition` fail to elaborate"), which only shows arity. I built my
   own counter-model instead: `bigLowerFrame := { liveSectorFrame with cLower := fun _ j => if j = 0
   then 0 else 10 }` and proved, in Lean, against the built project:

   ```lean
   theorem bigLower_cited  : bigLowerFrame.Cited                                  -- all 25 fields
   theorem bigLower_t6     : denom.Phi.legal.trace.t6.Claim bigLowerFrame
   theorem bigLower_gram   : denom.Phi.legal.gram.interface.Claim bigLowerFrame
   theorem bigLower_omega  : denom.Phi.legal.omega.interface.Claim bigLowerFrame
   theorem bigLower_not_tame : ¬ denom.Phi.legal.tame.Claim bigLowerFrame          -- at (n,j)=(100,1)
   theorem bigLower_not_sect : ¬ denom.Phi.legal.sect.Claim bigLowerFrame          -- corollary
   ```

   All six compile. So there is a frame satisfying `Cited ∧ H1 ∧ H2 ∧ H3` on which the conclusion
   `tame.Claim` is **false**: H4 is genuinely load-bearing, not decorative, and `tame.composition`
   is not provable without it. This is the mechanical rendering of external-review finding T3-G1
   that the node asks for, at full strength.
3. **Conclusion trivially true?** No. On the live model `goal.Claim` reduces to
   `(C − ε_n)·n^{1/3} ≤ K n` for all `n ≥ 27`, a real inequality, not `0 ≤ x`. The one place a
   vacuity trap was plausible — `Cited.defect_orth` at `n = 0`, where an unrestricted premise would
   force `‖D‖ ≤ B` for negative `B` and collapse the development — was *spotted and closed by the
   author* with the `1 ≤ n` guard and an explicit comment (`Interface.lean:106-111`). Good practice;
   I confirmed the guard is what makes `emptySectorFrame_cited.defect_orth` provable rather than
   vacuous.

**F3 (MEDIUM) — the non-vacuity models are degenerate in exactly the four channel norms the
theorem is about.** I verified by `rfl` against the built project:

```lean
example : SelfTest.liveSectorFrame.cLower 100 7 = 0 := rfl
example : SelfTest.liveSectorFrame.csectS 100 7 PUnit.unit = 0 := rfl
example : SelfTest.liveSectorFrame.yNorm  100 7 = 0 := rfl
example : SelfTest.liveSectorFrame.cDiag  100 7 = 0 := rfl
```

Both models therefore satisfy H4 only because `cLower ≡ 0`, and satisfy `Cited.y_bound`,
`cDiag_bound`, `tame.Claim` by `0 ≤ nonneg`. Consequently the self-tests establish *consistency* of
the hypothesis bundle but **not** consistency with a frame in which the bounded quantities are
non-zero and the envelope is near-tight — i.e. they do not exclude the possibility that
`Cited ∧ H1–H4` forces the interesting channels to vanish. (My `bigLowerFrame` shows the channel
fields *can* be non-zero while `Cited ∧ H1 ∧ H2 ∧ H3` holds, but there H4 fails by construction.)
The report's phrasing at `se/artifacts/se_lean_t1_20260730.md:156-158` ("prove the hypotheses
CONSISTENT (non-vacuity)") is literally true and honestly qualified ("They are models, not Set
Equality data"), so this is a **strengthening request**, not a false statement.

## V6 — Honesty, metadata, and build evidence  **PASS with four findings (F4–F7)**

**Scope clauses (§7.9) — verbatim, PASS.** `se/lean/README.md:25-28` and
`se/artifacts/se_lean_t1_20260730.md:99-102` both carry, word for word:
"A theorem proved against an abstract interface is exactly as strong as the results that interface
cites, and not one notch stronger." and "`lean-checked` is an evidence attribute, never a status."
Both also spell out what a green build does **not** establish for *this* development
(README:37-57; report:104-111), including the two blind spots (mis-typed H2, non-exhaustive H4) and
"it is not an independent review".

**Wording sweep — PASS.** `grep -rin "now verified|is verified|theorem is proved|proves theorem
b|machine-verified|formally verified"` over the whole Lean tree, README and report returns
**nothing**. Every relevant sentence is of the form "the DERIVATION is machine-checked; it says
nothing about the hypotheses" (`goal.lean:95-100`, `br.lean:49-50`, `denom.lean:69-70`,
`tame.lean:61-62`, and each hypothesis module's "Claim is a hypothesis"). The report's build line
("GREEN … sorry-free") is accompanied by the §2 cap statement. No status inflation found.

**Report table vs disk — PASS.** All nine node modules in the table exist at the stated paths with
the stated `Claim`/composition names (verified against the built environment, not just the text);
the `SE.denom.assembly.envelope` row correctly records `none` with the R1 reason. The declared
non-node modules match the disk exactly (`SE.lean`, `Interface`, `Support/{Defs,Cbrt,Constants,
Envelope,Limits}`, `SelfTest`, `Trust`). Counts check out: 19 `.lean` files = 18 sources +
`lakefile.lean`.

**Coordinator's `lean:` metadata — PASS.** 28 node files carry a `lean:` key: 9 full blocks and 19
`lean: none  # reason`. Every full block's `module`, `file`, `claim`, `composition`, `state`,
`claim_hash`, `build` matches reality (I resolved each name in the built environment and each hash
independently). Every `rel` list matches the actual premise list, including the two declared
deviations (R3 grandchildren + unrendered `found`; R4 cited children). The `NODE_INDEX.md` Lean
column agrees with the node files row by row. All **19** `lean: none` reasons are accurate; I
checked each against the code, in particular: `X`→`Cited.x_bound`, `Y`→`Cited.y_bound`,
`crossk`→`Cited.defect_orth`, `decomp`→`Cited.block_triangle`, `familysplit`+`decomp`→
`Cited.mask_from_D`, `br.num`→`Cited.numerator`, `br.def`→`Cited.maskNorm_pos`,
`assembly`→`composition: none` (confirmed at `SE.denom.assembly.yaml:11`),
`found`→ caveat declared on `tame.lean`, `Phi`/`Phi.legal`/`trace`/`gram`/`omega` → genuine
import-graph skips.

**Build evidence (§7.7) — PASS.** `command.txt`, full transcript with true exit status,
`print_axioms.txt`, and `SHA256SUMS.txt` are all present. I re-verified the ledger myself over
LF-normalized bytes: **25/25 entries match, 0 mismatches, 0 missing**, and every `.lean` source on
disk is covered.

**F4 (MEDIUM) — the target node does not cite its own deliverable (rule 8c / structure-protocol
§6).** `se/proof-dag/nodes/SE.formal.t1.yaml` never mentions
`se/artifacts/se_lean_t1_20260730.md`; its Work record stops at the 2026-07-30 Stage-A/collision entry
(lines 108-127), its Evidence section still lists only the pre-build items, and its Adversarial
reviews section says "None yet". The completed green build (a run: command + log + SHA) is
NUMERICAL-tier evidence that should be on the node with a `pending-review:` marker, and this review
must be cited there once read. Additionally the node itself carries **no `lean:` field at all**,
while §7.4 says "A non-formalized node records `lean: none` with a reason. Silence is invalid."
(`NODE_INDEX.md:14` shows `none` for it, so index and node disagree in kind if not in content.)

**F5 (MINOR) — a declared caveat is lost one level up.** `SE.denom.taper` renders a *proper
fragment* (R2), and this is declared in the module, in `Trust.lean` §D1, in the report, and in the
node's `lean.rel`. But `NODE_INDEX.md:24` shows the bare word `proved` in the Lean column, with no
fragment marker. That is exactly the failure mode rule 6 was written against ("the caveat must be
unlosable at every depth") — a reader of the index alone concludes the taper node is fully
mechanized.

**F6 (MINOR, process) — the §7.6 anti-drift checks are not mechanized.** §7.6 assigns seven checks
to "the checker"; `tools/proof_dag_check.py` contains no Lean logic at all (the only occurrence of
"lean" is a comment at line 94), and `--problem se` passes (82 nodes) without examining any `lean:`
block. Every drift found in this review (F1's quantifier scope aside, F2 and F4 are pure metadata
drift) is of the class those checks would catch automatically.

**F7 (MINOR–MEDIUM) — the node's definition self-test obligation is only partly discharged, and the
report does not mention it.** `SE.formal.t1.yaml:48-50` requires as *mitigation* that "the Lean
definitions must reproduce the independently brute-forced exact ratios `2, 4/3, 6/5` at `n=1,2,3`
… as decidable checks". What `SE/SelfTest.lean:92-98` actually does is define
`collapseRatio n := 2n/(2n−1)` and check `collapseRatio 1 = 2`, `= 4/3`, `= 6/5` — a hand-written
formula reproducing the target values, exercising **no definition of this development** (rule 7f,
value-vs-formula). The genuinely definitional part — `K 1 = K 2 = K 3 = 1`, `α₀ = 1`, `α₁ = 0`
(`SelfTest.lean:101-105`) — *is* real, and the module is honest that tier 1 cannot derive the ratio
(`SelfTest.lean:84-90`). The gap is that the report never states that this commissioned mitigation
is only partially met. (The rest of the self-test battery is strong: 12 `K`-boundary values via
`K_unique`, 8 kernel-`decide` evaluations of the discrete taper maximum cross-checked against
`taper_max`, the taper coefficients, and the 19-digit constant.)

**Housekeeping (not a finding):** `se/artifacts/se_lean_t1_20260730.md` and
`se/artifacts/logs_se_lean_20260730/lake_build_transcript.txt` are modified-but-uncommitted, and
`command.txt` / `print_axioms.txt` / `SHA256SUMS.txt` are untracked. The report's footprint
paragraph (lines 208-213) says "Nothing under `proof-dag/nodes/` was touched", which is true of the
*executor* but not of the session — 28 node files are modified by the coordinator's backfill. One
clarifying clause would remove the ambiguity.

---

## Fix list

| # | Severity | Fix |
|---|---|---|
| F1 | MEDIUM | Either (a) restrict `sect.Claim` to the active range (`1 ≤ j`, `3j ≤ n`, `j < K n − 1`) and re-scope `tame.Claim` accordingly, handling `d = K−1` in `denom.block_le` by `alpha (K n) (d+1) = 0` and `d = 0` by `Cited.cLower_zero`; or (b) keep the wider statement and **correct** `se/artifacts/se_lean_t1_20260730.md:123-126` to say that H4's shadow is *not* implied by the frozen Claim, adding the scope gap to the Honest-limitations list and to `sect.lean`'s header. Option (a) is preferable: it makes the Lean theorem conditional on exactly Conjecture H. Also resolve or define the term of art "active `j`" on the node (rule 7g). |
| F3 | MEDIUM | Add a third self-test model with `cLower`, `csectS`, `yNorm`, `cDiag` **strictly positive** satisfying `Cited ∧ H1–H4` (e.g. `csectS := √(15/8)·√(j/(n−j))`, `cLower := ` the same value, `yNorm := √2·√(d/n)`), so that non-vacuity is witnessed in the quantities the theorem bounds and not only in the sector layer. Retain the existing models. |
| F4 | MEDIUM | Append to `SE.formal.t1.yaml`: a dated Work-record/Evidence entry citing `se/artifacts/se_lean_t1_20260730.md` + `se/artifacts/logs_se_lean_20260730/` (command, transcript, exit status, SHA ledger) at **NUMERICAL** with a `pending-review:` marker, then an Adversarial-reviews entry citing *this* file. Add a `lean:` field to the node (`lean: none  # tool node: this node IS the formalization; its modules are the nine node modules it produced`). |
| F7 | MINOR–MED | State in the report (and ideally on the node) that the commissioned `2, 4/3, 6/5` mitigation is discharged only at the definitional level (`K = 1` collapse, `α₀ = 1`); `collapseRatio` is a restated formula, not an independent construction. |
| F2 | MINOR | Update `SE.denom.Phi.legal.tame.yaml:14` `composition.proof` to point at `se/lean/SE/denom/Phi/legal/tame.lean` (`gcan_le → csect_le → composition`); drop the "pending restructure" clause and the dead `se/lean` / `SE/Assembly.lean` reference. |
| F5 | MINOR | In `NODE_INDEX.md`, render the taper row's Lean state as `proved (fragment, R2)` (or add a footnote), so the R2 caveat survives at index depth. |
| F6 | MINOR | Implement §7.6 checks 1–6 in `tools/proof_dag_check.py` (module/file/`Claim`/composition existence, hash agreement, premise-vs-children with declared-deviation allowlist, import graph vs edges). Consider replacing `Trust.lean`'s 33-name census with the environment-scanning `run_cmd` used in §V2 of this review. |

## Verdict

**PASS-WITH-FIXES.**

The build reproduces exactly (exit 0, 3056 jobs, axiom output identical to the archive); the
development is `sorry`-free and axiom-clean across **all 163** `SE` declarations, not merely the 33
named ones; all ten frozen-Claim hashes recompute independently and match three ways; the nine
module `Claim`s are faithful to their frozen prose (renderings are explicit-and-stronger, never
weaker); the top conclusion is equivalent-or-stronger than the manuscript's Theorem B including the
constant, its 19 certified digits, and the `n ≥ 27` window; the conditional theorem is **not**
vacuous, and I independently proved by counter-model that H4 is load-bearing; and the honesty
apparatus (README, `Trust.lean` §D, report limitations, `lean: none` reasons) is accurate and
unusually candid about what tier 1 cannot see.

The seven findings are one genuine fidelity defect (F1: the H4 hypothesis is stated more widely
than Conjecture H, so the report's "frozen ⟹ shadow" sentence over-claims for H4), one
strengthening request (F3), one atomic-update omission on the target node (F4), and four minor
metadata/process items. None of them is a soundness break, a hidden hole, or a status overreach, so
no FAIL is warranted; but F1 and F4 should be applied **before** any node cites this development
through the rule-6/rule-7 gate.

**Status licensing (§2):** this review completes the independent-review gate for the T1
development's *own* evidence only. It licenses `SE.formal.t1` to move from OPEN to **NUMERICAL**
(green-build run evidence) — or, at the coordinator's discretion after F1/F4 are applied, to
CERTIFIED\* as a *tool* node with the caveat "single reviewer; tier-1 shadows only; H2 type content
and H4 exhaustiveness unverifiable at this tier". It licenses **no** status change on `SE.goal`,
`SE.br`, `SE.denom`, `SE.denom.Phi.legal.tame`, `SE.denom.taper` (fragment only), or any of
H1–H4: a machine-checked conditional derivation is evidence about the derivation, and every one of
those nodes is gated on hypotheses this development assumes rather than proves.
