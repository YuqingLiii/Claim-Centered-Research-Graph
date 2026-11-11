# CircDist Gross Round92 proposer report

## Verdict

`MATERIAL-CHECKED-PROGRESS-NOT-CLOSED`.

The Gross root and its gap route remain `CONJECTURED`; the only licensed interval remains
`D*_Gross in {11,12}`.  No canonical YAML was edited.  No commit or push was made.  This
is a proposer package and requires a fresh independent review before any canonical use.

## Bound starting point

Round92 begins from the independently reviewed Round90 frontier: iteration 124,
`started:false`, 14,484 inherited order blocks, 164 exact EFSSCs, selector state
`854c2b50...fce2c3`, semantic source `d155a897...397e`, and the checked but unsolved
19,046-assertion / 401,040-variable / 1,345,190-clause CNF
`2dd07d33...7e5a`.  `INPUT_BINDINGS.json` binds those bytes, the Round91 review, the
current scheduler and node, and both complete Round90 manifests.

## Phase A: weight-9 slack synthesis

The generator first reconstructed the reviewed i115 Zerr and i119 Xerr nine-column
mechanisms from their actual schedules.  For each it recomputed the zero 72-bit syndrome,
nonzero 12-bit logical vector, canonical terminal residual support, physical suffix support,
and invariance modulo the full same-sector check row.

It then exhausted the declared finite families before iteration 124 was solved:

| family | exact census | retained novel ordinary selectors |
|---|---:|---:|
| one-column completions of i115 / i119 | 351 + 351 | 11 + 29 |
| all proper nonempty deletion minors | 510 + 510 | 2 + 1 |
| compatible same-sector unions with weight at most 10 | 0 filtered | 0 |
| pairwise same-sector GF(2) differences | 6 of 6,642 pairs had weight 1–10 | 1 |
| one source-cube order-atom deletions | 101 | 0 relaxed cubes |

All 97 strictly broader atom-deleted cubes had an explicit uncovered local-order
countertuple; four deletions were redundant.  Zero domains were discarded only as local
selector results and were never interpreted as schedule absence.

After semantic deduplication, 44 ordinary exact EFSSCs remained.  Their support-domain
counts and local-order-domain counts are stored individually in the 1,039,449-byte
`synthesis/weight9_synthesis.json` proof object.  The two completion totals were 22 and
104 support tuples and 7,167,126,011,904 and 40,660,597,997,568 local-order tuples.

The separate exact frozen-CNF strict-expansion query was SAT: all 164 old selector
predicates were false and exactly one new predicate was true,
`r92-r90-i119-Xerr-plus-R_61_2`.  Its ten named columns have zero syndrome and logical
vector `101100000001`; the full 403,773-variable assignment satisfies all 1,356,870
clauses and maps to an audited 864-interaction, 648-overlap frozen schedule.  This proves
that the installed 44-term union is strictly broader than the old union.  It does not
prove a universal cover.  Only after this witness and all domain proofs passed were the
44 terms atomically installed, producing 208 selectors and the augmented iteration-124
CNF `6f1c386e...0a014`.

## Phase B: strict serial continuation

Iterations 124 through 135 were processed in order.  Every outer formula was SAT.  Every
complete assignment was checked clause by clause and mapped to a legal frozen schedule.
Both complete unrestricted direct-360 sectors were then built and solved; all 24 were SAT,
all assignments satisfied every clause, and every named mechanism passed canonical and
physical replay before the two corresponding EFSSCs were atomically appended.

| iteration | outer | Xerr weight | Zerr weight |
|---:|---|---:|---:|
| 124 | SAT | 10 | 9 |
| 125 | SAT | 10 | 10 |
| 126 | SAT | 10 | 10 |
| 127 | SAT | 10 | 10 |
| 128 | SAT | 10 | 10 |
| 129 | SAT | 10 | 10 |
| 130 | SAT | 10 | 10 |
| 131 | SAT | 10 | 10 |
| 132 | SAT | 10 | 10 |
| 133 | SAT | 9 | 10 |
| 134 | SAT | 10 | 10 |
| 135 | SAT | 10 | 10 |

Every solver invocation enabled textual proof output.  Because every formula was SAT,
the 36 streams contain no empty clause and are not UNSAT certificates.  Their complete
hash/byte/LF disposition is retained.  One small actual-formula SAT stream is retained
and rejected by DRAT-trim in full, corrupt, and truncated forms.  Separate fixture controls
accept valid DRAT, generate and accept LRAT, and reject corrupt/truncated DRAT and LRAT.

## Fresh frontier

The exact continuation is iteration 136, `started:false`, 232 selectors, selector state
`1692d905...fa81`, semantic source `a5615158...4ebe`, source file
`a71fb5e7...c5d8`, and a checked 19,114-assertion / 406,656-variable /
1,372,232-clause CNF `289acad6...b64e`.

The positive results close twelve CEGAR transitions and establish a strict Phase-A union
expansion.  They do not close the remaining quantified schedule domain, prove repair
absence, or narrow `D*_Gross`.

