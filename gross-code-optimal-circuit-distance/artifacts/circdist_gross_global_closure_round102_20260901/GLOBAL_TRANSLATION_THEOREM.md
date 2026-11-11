# Round102 exact translation action, invariant closure, and orbit quotient

## Scope and verdict

This note proves an exact finite symmetry reduction for the reviewed frozen
Gross scheduling model.  It does **not** prove either Gross root branch by
itself.  The corrected invariant quotient is SAT, so its role is to supply a
fully audited canonical schedule candidate and a reusable global reduction.
An UNSAT result for a quotient can be lifted globally only when the formula to
which the lex leaders are appended is invariant under the action below.

The earlier exploratory quotient over the unclosed iteration-185 registry is
not invariant and is therefore not a valid global quotient.  Its SAT schedule
and direct witnesses remain valid point evidence; its quotient-coverage claim
is retracted.  All numerical claims below concern the corrected full closure.

## Definitions

Let

\[
G=\mathbb Z_{12}\times\mathbb Z_6,
\qquad |G|=72.
\]

Write a Gross check index as \(c=6i+j\), where \(0\le i<12\) and
\(0\le j<6\).  For \(\delta=(a,b)\in G\), define

\[
\tau_\delta(c)=6((i+a)\bmod 12)+((j+b)\bmod 6).
\]

The 144 data qubits are two 72-element sheets.  If \(q<72\), set
\(\tau_\delta(q)=\tau_\delta(c=q)\).  If \(q\ge72\), set
\(\tau_\delta(q)=72+\tau_\delta(c=q-72)\).  On an interaction edge
\(e=(K,c,q)\), for \(K\in\{X,Z\}\), set

\[
\tau_\delta(e)=(K,\tau_\delta(c),\tau_\delta(q)).
\]

For a schedule \(S:E\to\{0,\ldots,1023\}\), use the left action

\[
(\delta S)(\tau_\delta(e))=S(e).
\]

An order atom \(t_{e_1}<t_{e_2}\) is sent to
\(t_{\tau_\delta(e_1)}<t_{\tau_\delta(e_2)}\).  A block is transformed atom
by atom.  A direct selector is transformed by translating its data support and
its check-indexed local fault kinds; its sector is unchanged.

## Lemma 1: this is a finite group action by bijections

For every edge, qubit, and check,

\[
\tau_{(0,0)}=\mathrm{id},\qquad
\tau_\delta\tau_\epsilon=\tau_{\delta+\epsilon},\qquad
\tau_\delta^{-1}=\tau_{-\delta}.
\]

These identities follow directly from modular addition on the two coordinate
factors and from preserving the data-qubit sheet bit.  The independent checker
enumerated all 72 edge permutations, all 864 identity-edge cases, and
4,478,976 edge-composition cases.  It also checked 20,736 geometry/check/
incidence cases and 46,656 overlap cases.  Thus the action preserves every
finite index relation used by the frozen scheduling semantics.

## Lemma 2: legal schedules and direct mechanisms are equivariant

Relabeling by \(\tau_\delta\) permutes, without changing truth:

* edge-time bounds and edge distinctness constraints;
* same-qubit and same-check exclusion relations;
* measurement-circuit precedence relations;
* global interleaving and extrema predicates;
* detector rows, logical rows, and the 360 named direct columns in each sector.

The independent action checker exhaustively tested 10,368 stabilizer/detector
row permutation cases and 51,840 direct-column equivariance cases.  It also
replayed 144 translated witnesses, covering both sectors over all 72 group
elements.  Consequently a distinct-name direct mechanism of weight \(w\),
zero detector syndrome, and nonzero logical effect on \(\delta S\) maps under
\(-\delta\) to a mechanism with the same three properties on \(S\).  Names are
permuted bijectively, so translation cannot create a selected-name collision or
change weight.

## Lemma 3: the corrected registry is exactly invariant

The input had 14,484 block records representing 14,477 distinct block
semantics and 474 selector records.  Exact orbit closure under all 72 elements
produced:

| object | parent-element pairs | distinct semantics | collisions |
|---|---:|---:|---:|
| blocks | 1,042,848 | 517,140 | 525,708 |
| selectors | 34,128 | 23,868 | 10,260 |

Block parent orbits were 90 of size 36 and 14,394 of size 72.  Selector parent
orbits were one of size 36 and 473 of size 72.  The selector closure contains
12,492 Xerr and 11,376 Zerr semantics.  The block union consists of 1,440
unary, 900 round-62, 500,868 generalized, and 13,932 dynamic semantics.

Identity and collision decisions used complete normalized tuples, never hash
equality.  Hashes label records only.  The independent checker reconstructed
every one of the 517,140 block and 23,868 selector provenance records from its
cited parent and group element.  It proved exact expected/observed set equality
and checked closure under the two generators in 1,034,280 block cases and
47,736 selector cases.  Closure under generators implies closure under all of
\(G\).  Therefore the corrected source formula \(F\) is invariant:

\[
F(S)\iff F(\delta S)\quad\text{for every }\delta\in G.
\]

This implication uses the soundness of each inherited block and exact direct
selector as reviewed evidence; orbit closure does not strengthen a cut beyond
its translated semantics.

## Lemma 4: the 71 lex leaders choose an orbit-minimal schedule vector

Let \(v(S)\) be the 8,640-bit raw schedule vector: 864 edge times, ten bits per
time word, in the frozen canonical edge/bit order used by the compiler.  For
every nonidentity \(\delta\in G\), append the exact lexicographic constraint

\[
v(S)\le_{\rm lex} v(\delta S).
\]

Every finite orbit has a least vector.  Hence every model of invariant \(F\)
has at least one translated model satisfying all 71 leaders.  If multiple group
elements attain the minimum, they produce the same schedule vector and differ
by an element of the schedule stabilizer.  The representative vector is
unique; the attaining group element need not be.

The recurrence encoding introduces one equality-prefix chain per nonidentity
translation.  Its four-input local truth table was checked in all 16 cases.
The independent checker reconstructed all 4,907,591 appended clauses, checked
the 6,867,095-clause base as an exact prefix, and established a unique extension
of every base assignment to the recurrence variables.  The corrected quotient
has 2,447,800 variables and 11,774,686 clauses, below signed 32-bit variable and
signed 64-bit clause limits.  Compilation and checking stream clauses and do
not enumerate schedule assignments.

## Theorem: corrected quotient equisatisfiability and lifting

Let \(Q=F\wedge\bigwedge_{\delta\ne0}
[v(S)\le_{\rm lex}v(\delta S)]\).  Then

\[
F\text{ is SAT}\iff Q\text{ is SAT}.
\]

The reverse direction is immediate because \(Q\Rightarrow F\).  For the
forward direction, translate any model of \(F\) to an orbit-minimal schedule;
Lemma 3 preserves \(F\), and Lemma 4 supplies every lex leader.  Lemma 2 lifts
any installed direct witness on the representative back to every schedule in
its orbit, with sector, distinct-name weight, zero syndrome, and nontrivial
logical class preserved.

Thus a proof-checked UNSAT certificate for this corrected quotient would prove
that no legal frozen schedule survives the fully closed installed exclusions.
That is the exact global conclusion supported by this finite quotient.  It
would become the requested root branch only together with the reviewed theorem
that every installed exclusion is sound and that survival is exactly the
absence of a named-weight-at-most-10 direct mechanism in the complete frozen
model.

## Current disposition

The corrected quotient CNF has SHA-256
`f6dec16c6ee19ee1a041d3eb78786171558f54805c3038ce9c311c62b82d7c13`
and is SAT.  Its complete assignment satisfies all 11,774,686 clauses.  The
decoded legal frozen schedule uses 483 compressed layers, has no closed block
or selector hit, and has compressed-schedule SHA-256
`f6a806a1b90535d497da63b154960f9ebf172c6c740356470cdeda56866bd5cf`.
Therefore neither root branch follows from the quotient solve.  Complete
unrestricted direct-360 adjudication of this candidate is recorded separately;
an UNKNOWN or time-bounded direct result is not an absence proof.

## Bound evidence

The machine-checkable records are:

* `global/iter185_translation_quotient/independent_check.json` for the action;
* `frontier/iter186_full_invariant/closure_plan.json` for multiplicities and
  orbit sizes;
* `frontier/iter186_full_invariant/independent_closure_check.json` for exact set
  equality, provenance, generator invariance, and the base-encoding link;
* `frontier/iter186_full_invariant_quotient/independent_check.json` for the lex
  encoding and quotient counts;
* `frontier/iter186_full_invariant_quotient/assignment_independent_check.json`
  and `replay.json` for the SAT assignment and frozen-schedule replay.

