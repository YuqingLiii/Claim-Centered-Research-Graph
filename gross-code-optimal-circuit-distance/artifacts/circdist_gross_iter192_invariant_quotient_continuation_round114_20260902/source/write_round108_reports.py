#!/usr/bin/env python3
"""Write the public Round108 scientific report, theorem notes, and failure ledger."""
from pathlib import Path
import argparse, hashlib, json

def load(p): return json.loads(Path(p).read_text())
def sha(p):
    h=hashlib.sha256()
    with Path(p).open('rb') as f:
        for b in iter(lambda:f.read(8<<20),b''): h.update(b)
    return h.hexdigest()
def write(p,s): Path(p).write_text(s.rstrip()+'\n')

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--root',type=Path,required=True); a=ap.parse_args(); r=a.root.resolve()
    res=load(r/'RESULT.json'); fresh=load(r/'FRESH_FRONTIER.json'); direct=load(r/'verification/iter189_direct_independent_audit.json')
    traces=load(r/'verification/iter189_sat_trace_streams.json'); closure=load(r/'verification/iter190_incremental_orbit_closure_independent.json')
    proof=load(r/'verification/proof_controls.json'); gates=load(r/'verification/repository_validators/summary.json'); pre=load(r/'verification/preseal_replay_binding.json')
    sol={x['name']:x for x in res['solver_processes']}
    outer=next(x for x in res['solver_processes'] if 'quotient' in x['name']); xs=next(x for x in res['solver_processes'] if 'Xerr' in x['name']); zs=next(x for x in res['solver_processes'] if 'Zerr' in x['name'])
    x=direct['sectors']['Xerr']; z=direct['sectors']['Zerr']
    report=f"""# Circdist Gross Round108: iteration-189 invariant-quotient continuation

## Verdict

**MATERIAL-CHECKED-CONTINUATION-NOT-CLOSED.** The exact reviewed iteration-189 quotient is SAT. The reconstructed schedule is legal, but both complete unrestricted direct-360 sectors are SAT and each supplies a checked weight-10 undetected nonstabilizer mechanism. The candidate therefore is not a distance-12 witness. Branch A and branch B both remain open. `CIRCDIST.gross` and `gap-via-lift` remain `CONJECTURED`; the licensed residual remains `D*_Gross in {{11,12}}`.

No repair was entered after complete direct-sector adjudication. Exactly two full free `Z_12 x Z_6` translation orbits, 72 selectors from each sector, were appended atomically. The only next frontier is fresh/unstarted iteration 190. It was compiled and independently checked, but it was not solved.

## Bound input and start condition

Round108 bound the reviewed Round106 package and Round107 review before science. The live and copied hashes agree:

- scheduler: `13c74772427b20aaf8128633459ee995c62e60dd1b79090c458d00e9a0994343`
- canonical Gross node: `8b805a806d5b704047f4ccca648c92efe11740d7c5b7825659eb1e6b7b5dc977`
- Round107 review: `eda1d894cde8a56fd7eac9188ed2bb73bef4ddd7842e2fcb091435cbd759c036`
- reviewed predecessor root manifest: `0b9cc6d4074e8397062219ec8d079afbcf0388e14912ab925b5d66ac00c61c9d`, all 432 rows checked
- iteration-189 source: `b3bdfbe8924490da1e20230ff856515d13173966bc4170c6078b7aab9e36558b`
- semantic source: `e8b17eac5c55f1b1c32fb84972dcc2c52ce259c99a65200c8ed7bc046c811eb4`
- state: `8bb97ba8ff7590f178aaff29f51da8ab6953b1fae90bcf6952546d31f59c6f97`
- selector state: `8e4db1fbf08e24b81995a6ac1b25f791480edebd06e560442e2ca49a5ad5cefa`

The mandatory quotient was `frontier/iter189_full_invariant_quotient/outer.cnf`, SHA-256 `3ece12a1ea0ee6502982fecfcaf75debae985ea2ddff93ea3b875552c0714df7`, with 2,460,741 variables, 11,816,927 clauses, and 545,909 assertions including 71 lex leaders. Its base had SHA-256 `f5ccbe6aa4c0a0df5940cd979809003182416900e76a6cc6e3755e493cc6b178`, 1,847,301 variables, 6,909,336 clauses, and 545,838 assertions. The registry contained 517,140 blocks and 24,300 selectors. Exact allowlists and absence of solver/model/assignment/proof files established that iteration 189 was fresh and unstarted.

## Definitions and encoded statement

Let `E` be the ordered set of 864 frozen check-data interactions and let a schedule be a map `S:E -> {{0,...,1023}}`. `vec(S)` is the ordered concatenation of the ten-bit edge times. `Legal(S)` is the conjunction of time bounds, edge distinctness, MC constraints, overlap and whole-check interleaving, global interleaving, extrema requirements, and every installed block/selector exclusion. The retained compiler realizes

`Base(S) := Legal(S) and all installed exclusions(S)`

with a unique definitional extension: projecting a CNF model yields exactly one bounded schedule, and every satisfying bounded schedule has exactly one assignment to the auxiliary gates.

The translation group is `G = Z_12 x Z_6`, of order 72. The group acts bijectively on geometry, edges, schedule vectors, detector rows, logical rows, direct columns, blocks, and selectors. The quotient is

`Q(S) := Base(S) and AND_{{g in G, g != e}} [vec(S) <=_lex vec(g.S)]`.

Because every finite orbit has a lexicographically least vector, `Base` is satisfiable iff `Q` is satisfiable. Stabilizers can give several minimizing group elements, but they give the same schedule vector; no uniqueness-of-group-element assumption is used.

A direct mechanism is a set of ten named columns from the unrestricted 360-column sector formula. It is adverse when its detector syndrome is zero and its logical class is nonzero, equivalently its physical support is outside the stabilizer row span. The independent checker reconstructs all 360 columns and both canonical and physical actions from geometry and the frozen schedule.

## Independent pre-solve reconstruction

Before launching CaDiCaL, four foreground checks independently established:

1. all 432 predecessor manifest rows, copied inputs, immutable hashes, exact allowlists, and freshness;
2. the source/base bijection for all 545,838 assertions, 6,909,336 clauses, 1,838,621 definitions, roots, and negative controls;
3. 517,140 exact blocks, 24,300 exact selectors, the 72 edge bijections, 4,478,976 group-composition cases, and full registry invariance;
4. byte-exact base-prefix preservation, all appended quotient clauses, the action, recurrence and root semantics, unique extension, and finite-orbit equisatisfiability.

These checks did not use a solver result and were completed before the mandatory solve.

## Mandatory quotient solve and model replay

One foreground CaDiCaL process ran with proof output enabled, no binary proof, no portfolio, and no concurrent solver/checker. PID {outer['child_pid']} returned 10 (SAT) after {outer['wall_seconds']:.6f} seconds; it was attached, did not time out, and was reaped. The complete assignment assigns every one of 2,460,741 variables exactly once and satisfies all 11,816,927 clauses. Its assignment SHA-256 is `c992d5938b3b2531bd559ca085e723061f43479ece3510f94eef27a14768a498`; the solver log SHA-256 is `4869b3e7a98b640554ab8b5c7a5459774d87fa640f7740e60dba903502cae2da`.

Physical reconstruction produced 864 edges in exactly 448 used layers, times 0 through 447, with zero conflicts and zero MC violations. It found 648 overlap pairs, 125 interleaved overlap pairs, 409 whole-check interleaved pairs, and a passing global-interleaving predicate. The compressed schedule SHA-256 is `0c1fc8bfede56c24fd3e5b10bbcb03b215aefc271dd3471d2c34cfdd7626fcba`; the raw schedule SHA-256 is `32766475687d5a87efdc3b61367daa97107dd57ea29281d22b889030476713ff`.

All 72 translated schedule vectors were reconstructed. They were distinct, the stabilizer size was one, the candidate was lexicographically least, and all 71 nonidentity roots were strict. A removed-root negative control failed only the selected root `(11,3)`; reversed lex direction, a truncated assignment, and a one-variable mutation were all rejected.

## Complete unrestricted direct adjudication

The direct builder reconstructed all 360 columns in each sector without pool, residual, check-count, or ordering restrictions. Formula and assignment checks were byte-exact and complete.

### Xerr

- CNF: 6,102 variables, 22,988 clauses, SHA-256 `3a103f690d095b80f18a0499ba022d3dc2c8311c49629c431709a2746707bfbf`
- solver: PID {xs['child_pid']}, return 10 (SAT), {xs['wall_seconds']:.6f} seconds, attached and reaped
- assignment: SHA-256 `52601f873e94d5532690713cf84505059a9cb5dbd9444098107ccbd453ad6dc1`; all variables and clauses checked
- selected names: `{' '.join(x['selected_names'])}`
- canonical support: `{x['canonical_net_support']}`
- physical support: `{x['physical_net_support']}`
- detector syndrome: empty in both reconstructions
- logical parities: `{x['logical_parities']}`; canonical and physical nonstabilizer checks pass

### Zerr

- CNF: 6,100 variables, 22,980 clauses, SHA-256 `576c1646bdb37eb8c14ca5029e29d763bfd8aac019fd20b351684e116a261b0f`
- solver: PID {zs['child_pid']}, return 10 (SAT), {zs['wall_seconds']:.6f} seconds, attached and reaped
- assignment: SHA-256 `f5b1b6479bf0fbbda7142f3b7577a8b2fa28b77129de9c0a1c220fbd80bf409e`; all variables and clauses checked
- selected names: `{' '.join(z['selected_names'])}`
- canonical support: `{z['canonical_net_support']}`
- physical support: `{z['physical_net_support']}`
- detector syndrome: empty in both reconstructions
- logical parities: `{z['logical_parities']}`; canonical and physical nonstabilizer checks pass

Both vendor-backed and separate Python-standard-library replays reconstructed the syndrome, logical action, stabilizer membership, canonical support, physical hooks, and exact schedule semantics. Either SAT sector is enough to exclude this candidate; both are retained to discharge the requested complete sector adjudication.

## Branch analysis

**Branch A is not proved.** It would require a legal iteration-189 candidate with both complete unrestricted direct sectors UNSAT under independently accepted proof certificates, plus the remaining exact-circuit obligations. Instead, both sectors are SAT and exhibit explicit weight-10 adverse mechanisms.

**Branch B is not entered and not proved.** It would require UNSAT of the exact mandatory quotient, a valid DRAT translated to LRAT and independently checked against that CNF, plus registry invariance, quotient equisatisfiability, and exhaustive selector/block semantics. The mandatory quotient is SAT. No Gross UNSAT certificate exists in this package.

Candidate-specific exclusion does not narrow the root interval. The result is a continuation step, not a theorem closure.

## SAT traces and proof controls

All three solver launches had proof-side output enabled. Since all three results are SAT, those streams are search traces, never certificates. Raw streams totaled {traces['raw_bytes']:,} bytes and were replaced only after deterministic gzip roundtrip verification; gzip files total {traces['gzip_bytes']:,} bytes. There are zero empty-clause lines. The exact descriptors retain raw and gzip hashes, raw byte counts, and LF counts. The three superseded raw files were deleted.

Pinned DRAT/LRAT controls are independent tooling tests only. Valid DRAT was accepted and translated; generated LRAT was accepted; corrupt and truncated DRAT and LRAT controls were rejected. Six nested children (PIDs 9191 through 9196) are recorded with exact intervals and expected return codes `0,0,1,1,1,1`; all were foreground, non-overlapping, not timed out, and reaped. These controls do not turn SAT traces into certificates.

## One atomic orbit step

The two checked parent mechanisms have trivial stabilizer in `G`, so orbit-stabilizer gives `|G.m| = 72/1 = 72` for each. Their normalized selector tuples are disjoint from the 24,300 old selectors and from one another. Hence the exact update is

`24,300 + 72 + 72 - 0 collisions = 24,444 selectors`.

The closure audit checked 72 translated schedules, 144 translated physical mechanisms, 1,034,280 block-generator cases, and 48,888 selector-generator cases. Every translated schedule remained legal; every translated mechanism retained weight 10, zero syndrome, and nonstabilizer status. The block registry stayed at 517,140 and the full post-addition registry is invariant.

## Fresh iteration-190 frontier — not solved

- source SHA-256: `5231e7f5b4cd2a74390a5d137b9927276ce73829dc599ddc064ab8f2c94a2d2e`
- semantic source SHA-256: `76881a021258e6fda565ecfe0ad61c1fe0e6f6a97a418ea806c6d3193b692c00`
- state SHA-256: `af31130cbb6f0f80d2b37b3ba27d1b1d86fa5b18a80c1e02aa3de02504863be4`
- selector-state SHA-256: `02b71bfed57c070359b77d69514397a021734aec7563057c02eeff29f4b6cdbd`
- base: 1,850,757 variables, 6,920,296 clauses, 545,982 assertions, SHA-256 `e3ec0d0b146fc4ade428052d1a14737ffade9974dfc37dd79fa8411841d45fc8`
- quotient: 2,464,197 variables, 11,827,887 clauses, 546,053 assertions including 71 lex leaders, SHA-256 `12f2fe58f4bfcaff19d543cdb60411f1659e86c8b4f16f599a2d1679aeeca767`

The base source/CNF bijection and quotient action/prefix/equisatisfiability checks both pass. Exact allowlists contain only source, formula, trace, root and audit files. No solver/model/assignment/proof artifact exists in either fresh frontier. `started=false`, `stop=null`. Round108 did not solve iteration 190.

## Replays, gates, and governance

The final preseal scientific replay ran 18 children strictly serially, with no interval overlap, no timeout, no detached process, and every child reaped. Its external record has SHA-256 `{pre['sha256']}`, {pre['bytes']:,} bytes and {pre['lf']} LF. It reconstructs the input binding, all source/base/registry/action checks, the complete quotient assignment, physical schedule, direct formulas and assignments, both independent direct replays, the two full orbits, fresh base and quotient, trace roundtrips, and proof controls.

Repository gates pass 10/10: live governance bindings, Circdist DAG, all-project DAG, migration, release contracts, DAG contracts, Lean selftest (23/23), duplicate YAML keys, `git diff --check`, and evidence-closure interpretation. The raw evidence-closure command returned its expected code 1 with 378 unique diagnostics, all under this new uninstalled proposer package; stderr was empty. Canonical and scheduler bytes were unchanged, and the proposed YAML is byte-identical to the bound canonical YAML.

## Scope and limitations

This package proves the exact iteration-189 candidate exclusion and exact construction of the fresh iteration-190 frontier. It does not prove an explicit distance-12 circuit, a universal distance-at-most-11 ceiling, `CIRCDIST.gross`, gap-via-lift, or any statement outside the frozen Gross family. It does not claim SAT proof streams as certificates. It does not install its proposed YAML. The smallest honest residual is to solve the exact fresh iteration-190 quotient proof-first and adjudicate both unrestricted direct sectors if SAT.

All public claims above are replayable from retained objects and scripts. Private hidden reasoning is neither an artifact nor a claimed source of evidence.
"""
    write(r/'REPORT.md',report)

    theorem=f"""# Round108 theorem notes

## Objects

Let `G = Z_12 x Z_6`, `|G|=72`. Let `E` be the ordered 864-edge frozen interaction set. A bounded schedule is `S in [0,1023]^E`; `v(S)` is its fixed ordered ten-bit vector. The retained source defines `Legal(S)` through exact geometry, distinctness, MC, overlap, whole-check and global-interleaving predicates plus installed exclusion roots.

Let `B_189` be the iteration-189 base CNF and `Q_189` its quotient. Their checked dimensions and hashes are:

- `B_189`: `(1,847,301 variables, 6,909,336 clauses)`, SHA-256 `f5ccbe6aa4c0a0df5940cd979809003182416900e76a6cc6e3755e493cc6b178`;
- `Q_189`: `(2,460,741 variables, 11,816,927 clauses)`, SHA-256 `3ece12a1ea0ee6502982fecfcaf75debae985ea2ddff93ea3b875552c0714df7`.

`Q_189 = B_189 AND (AND_{{g != e}} v(S) <=_lex v(g.S))`, encoded by 71 lex roots and a uniquely determined definitional recurrence.

## Lemma 1 — source/base bijection

The independent source compiler audit streams every retained assertion and definition. It matches all 545,838 roots and all 6,909,336 clauses of `B_189`, including negative controls. Therefore projection of a CNF model to the primary schedule bits is a bounded legal source schedule satisfying exactly the installed exclusions, and every such source schedule has one auxiliary extension.

## Lemma 2 — action and registry invariance

For every `g,h in G`, the reconstructed edge map is a bijection and `g.(h.e)=(g+h).e`; 72 edge bijections, 4,478,976 composition cases and 864 identity cases pass. Geometry incidence, overlaps, detector rows, logical rows and all 720 direct columns are equivariant. All 517,140 blocks and 24,300 iteration-189 selectors are closed under the two generators and therefore under `G`.

## Lemma 3 — quotient/base equisatisfiability

For a base model `S`, the finite orbit `{{g.S:g in G}}` has at least one lexicographically least vector. Choose a minimizer `g0`; invariance from Lemma 2 gives `Base(g0.S)`. Minimality gives `v(g0.S)<=_lex v(h.g0.S)` for every nonidentity `h`, so `g0.S` extends uniquely to a quotient model. Conversely, deleting the lex extension from any quotient model leaves a base model. Thus `SAT(B_189) iff SAT(Q_189)`. Stabilizer ties do not alter the schedule vector and do not affect the implication.

## Lemma 4 — checked quotient model

The retained assignment assigns variables `1..2,460,741` exactly once. Streaming clause evaluation checks 11,816,927 terminated clauses and finds none false. The reconstructed schedule is legal: 864 edges, 448 used layers, bounds `[0,447]`, zero conflicts, zero MC violations, 648 overlap pairs, 125 overlap-interleaving pairs, 409 whole-check-interleaving pairs, and passing global interleaving. All 71 quotient roots hold; the orbit has 72 distinct vectors and trivial stabilizer.

Therefore `Q_189` and `B_189` are SAT. This immediately rules out entering branch B at iteration 189.

## Lemma 5 — complete direct SAT mechanisms

For each sector, the builder enumerates the unrestricted 144 data columns plus all retained hook columns for 360 total columns and encodes exactly ten selected names, zero detector syndrome and nonzero logical class. Complete assignments satisfy every clause:

- Xerr: 6,102 variables, 22,988 clauses; selected `{' '.join(x['selected_names'])}`;
- Zerr: 6,100 variables, 22,980 clauses; selected `{' '.join(z['selected_names'])}`.

Independent standard-library reconstruction yields empty canonical and physical syndromes and nonzero logical parity. Row-reduction places neither physical support in the stabilizer span. Thus each selected set is an explicit weight-10 adverse mechanism for this schedule.

Consequently the candidate's circuit distance is at most 10 under the complete direct mechanism semantics and it cannot be used for branch A. This candidate-specific conclusion does not change the campaign interval.

## Lemma 6 — atomic orbit cuts

For each parent mechanism `m`, exact translation replay finds `Stab_G(m)={{e}}`. Orbit-stabilizer gives `|G.m|=72`. Normalized semantic tuple comparison finds no duplicate against the old registry and no collision between the Xerr and Zerr orbits. Every translated mechanism remains named, weight 10, zero-syndrome and nonstabilizer on its translated legal schedule. Appending both full orbits therefore adds exactly 144 selectors and preserves invariance:

`24,300 + 72 + 72 = 24,444`.

No partial orbit is installed.

## Lemma 7 — fresh iteration-190 formula

The post-addition source has SHA-256 `5231e7f5b4cd2a74390a5d137b9927276ce73829dc599ddc064ab8f2c94a2d2e`; its full registry is invariant. The independently checked base has SHA-256 `e3ec0d0b146fc4ade428052d1a14737ffade9974dfc37dd79fa8411841d45fc8`. The quotient checker replays the 72-element action, preserves the exact base prefix, reconstructs all 4,907,591 appended clauses, and proves unique extension and finite-orbit equisatisfiability for quotient SHA-256 `12f2fe58f4bfcaff19d543cdb60411f1659e86c8b4f16f599a2d1679aeeca767`.

The exact file allowlists contain no solve output. Hence iteration 190 is fresh and unstarted.

## Root theorem status

Branch A requires an explicit legal candidate with both complete unrestricted direct sectors certified UNSAT and all circuit obligations independently replayed. Lemma 5 gives the opposite outcome for this candidate. Branch B requires certified UNSAT of the exact quotient plus the universal lifting composition. Lemma 4 gives SAT. Therefore neither branch is proved.

The licensed statement remains:

`CIRCDIST.gross = CONJECTURED`, `gap-via-lift = CONJECTURED`, `D*_Gross in {{11,12}}`.

The package proves only the material continuation: exact iteration-189 exclusion, exact full-orbit update, and exact fresh iteration-190 frontier. SAT proof-side streams are search traces; proof-tool controls are not Gross certificates.
"""
    write(r/'THEOREM_NOTES.md',theorem)

    failure="""# Round108 failure ledger

This ledger was frozen before payload sealing. There were **zero scientific failures or UNKNOWN outcomes**. Every solver produced a complete SAT result, every required assignment and physical replay passed, both direct sectors were fully adjudicated, and the fresh frontier checks passed.

## F108-001 — orchestration visibility gaps

During long wrapped stages, the interactive exec transport twice stopped exposing the live session even though the recorded foreground child continued. No replacement computation was overlapped. Retained PID records, completion outputs and later censuses establish that the children exited and were reaped. Disposition: interface-only; no scientific artifact was accepted from an unknown process state.

## F108-002 — pre-execution adaptation defects

Static inspection and `py_compile` caught stale iteration/source-label and assertion-count references while adapting the continuation scripts. The affected drafts were never launched and produced no scientific output. Disposition: corrected before execution; the executed scripts and replay use iteration 189 as input and iteration 190 as the fresh output.

## F108-003 — first frontier-advance launch failed

`verification/logs/process/advance_iter190_full_invariant_frontier.json` records PID 7336, return code 1, 6.575234 seconds, attached, no timeout and reaped. The vendored Z3 directory was not on `PYTHONPATH`; failure occurred before frontier output. Stdout/stderr are retained. The corrected strictly serial retry set `PYTHONPATH=python/site-packages`; PID 7356 returned 0 and was independently replayed. Disposition: fully disclosed execution failure; no output from the failed launch was used.

## F108-004 — proof-control PID fields initially incomplete

The first proof-control wrapper (PID 8220) verified tool behavior but its six nested tool invocations lacked child-PID and reap fields in the JSON result. Before freezing, the control driver was changed to foreground `Popen` calls with exact intervals, timeout/reap/detach fields and expected return codes. The corrected parent PID 9190 and child PIDs 9191–9196 are retained; all six were reaped. A second complete 18-step preseal replay exercised the corrected code. Disposition: FIX-2 metadata defect corrected without changing scientific conclusions.

## Superseded verification runs

The first full preseal replay passed but preceded the F108-004 metadata enhancement. It remains in the process log as a superseded passing run. The final preseal replay is the binding used by `RESULT.json` and the report. Raw SAT search streams were deleted only after deterministic gzip roundtrip checks; descriptors retain raw hashes, byte and LF counts. No raw proof object required for a certificate was deleted because all three results were SAT.

## Scope of process accounting

All solvers, science checkers, replay children, proof-control children, repository-gate children, sealers and final censuses use attached foreground processes with retained PID/interval/outcome records. Read-only inspection and Codex transport orchestration outside those wrappers are not scientific computations and are disclosed here rather than represented as solver evidence. No background or detached compute was used. Final post-root verification records are external by design so that the sealed package is not mutated.
"""
    write(r/'FAILURE_LEDGER.md',failure)
    write(r/'PROPOSED_CANONICAL_DELTA.md',"""# Proposed canonical delta

No canonical delta is proposed. `PROPOSED_CIRCDIST.gross.yaml` is byte-identical to the bound canonical `CIRCDIST.gross.yaml` (SHA-256 `8b805a806d5b704047f4ccca648c92efe11740d7c5b7825659eb1e6b7b5dc977`). The proposer package is not installed. Gross and gap-via-lift remain `CONJECTURED`, and `D*_Gross` remains in `{11,12}`.
""")
    write(r/'BOOTSTRAP_COMMAND.txt',"./replay.sh /absolute/external/path/round108-replay.json")
    print(json.dumps({'status':'PASS','report_bytes':(r/'REPORT.md').stat().st_size,'theorem_notes_bytes':(r/'THEOREM_NOTES.md').stat().st_size,'failures':4},sort_keys=True))

if __name__=='__main__': main()
