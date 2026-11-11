# Exact translation theorem and Round104 incremental closure

## 1. Scope

This note proves the symmetry and continuation facts used in Round104. It does
not close either exact Gross root branch. The iteration-187 invariant quotient
is SAT, and both complete direct sectors for its model are SAT. The valid
conclusion is a new invariant iteration-188 frontier, not a distance-12 circuit
and not a universal distance-11 ceiling.

All finite enumerations cited below are retained in
`frontier/iter188_full_invariant_quotient/independent_check.json`,
`verification/iter187_direct_independent_audit.json`, and
`verification/iter188_incremental_orbit_closure_independent.json`.

## 2. Gross geometry and group action

Let

\[
G=\mathbb Z_{12}\times\mathbb Z_6,\qquad |G|=72.
\]

Represent a check index as (c=6i+j). For
(delta=(a,b)\in G), define

\[
\tau_\delta(c)=6((i+a)\bmod 12)+((j+b)\bmod 6).
\]

There are two 72-element data sheets. For (q<72), use the same formula;
for (q\ge 72), set

\[
\tau_\delta(q)=72+\tau_\delta(q-72).
\]

An edge (e=(K,c,q)), (K\in\{X,Z\}), is relabeled as
(	au_\delta(e)=(K,	au_\delta(c),	au_\delta(q))). For a schedule
(S:E\to\{0,\ldots,863\}), the translated schedule is defined by

\[
(\delta S)(\tau_\delta(e))=S(e).
\]

Modular addition proves

\[
\tau_0=\operatorname{id},\qquad
\tau_\delta\tau_\epsilon=\tau_{\delta+\epsilon},\qquad
\tau_\delta^{-1}=\tau_{-\delta}.
\]

The independent quotient checker exhaustively verified 72 edge bijections,
864 identity cases, 4,478,976 composition cases, 20,736 geometry/incidence
cases, 46,656 overlap cases, 10,368 stabilizer/detector row permutations, and
51,840 direct-column equivariance cases.

## 3. Legal schedules are equivariant

A frozen schedule is legal when all 864 edges have bounded integer times, the
six edges at every check are distinct, edges sharing a data qubit do not
conflict, all 648 two-qubit X/Z overlaps obey measurement-circuit consistency,
and the X and Z sectors globally interleave. Each condition is defined solely
by incidence, equality, and strict order, all of which are permuted by
(	au_\delta). Therefore

\[
S\text{ legal}\iff \delta S\text{ legal}.
\]

Round104 also checked this statement directly on all 72 translations of the
retained schedule. Every translation used 451 layers, had maximum time 450,
and had no conflict or measurement-circuit violation.

## 4. Complete direct sectors

For either error sector, the complete direct query has 360 primary columns:

\[
144\text{ data singletons}+72\text{ checks}\times3\text{ hook kinds}.
\]

If the six qubits of a hook check, ordered by schedule time, are
((q_0,\ldots,q_5)), the canonical representatives are

\[
R_0=\{q_0,q_1\},\quad R_1=\{q_3,q_4,q_5\},\quad
R_2=\{q_4,q_5\}.
\]

The corresponding physical hook suffixes are

\[
P_0=\{q_2,q_3,q_4,q_5\},\quad P_1=R_1,\quad P_2=R_2.
\]

(P_0\triangle R_0) is the entire weight-six check stabilizer, so canonical
and physical representatives have the same detector syndrome and logical
class. The CNF asks for a distinct set (J\subseteq\{0,\ldots,359\}) with

\[
|J|\le 10,\quad \bigoplus_{j\in J}\sigma(c_j)=0,
\quad \bigvee_{r=0}^{11}
\left\langle\bigoplus_{j\in J}c_j,\ell_r\right\rangle=1.
\]

There is no pool, residual-pattern, check-count, or within-check order-family
restriction. The independent standard-library checker reconstructed all 720
columns without importing the frozen model modules, verified stabilizer ranks
66 and 66, verified the 12-dimensional logical pairing, reconstructed all 144
syndrome/logical equation rows, and checked every clause of both SAT models.

Translation permutes data singleton names and pairs ((c,k)) bijectively.
Thus a distinct-name, weight-at-most-10, zero-syndrome, nonstabilizer mechanism
on (S) translates to one with the same properties on (delta S).

## 5. Exact invariant registry

At iteration 187 the reviewed full-invariant source contained 517,140 block
formulas and 24,012 exact selectors. Round104 retained every block and selector
in the same order, then appended the complete 72-element orbit of each of the
two new direct mechanisms.

The independent incremental checker established:

| property | result |
|---|---:|
| old/new blocks | 517,140 / 517,140 |
| unique block formulas | 517,140 |
| block generator cases | 1,034,280 |
| old/new selectors | 24,012 / 24,156 |
| appended selectors | 144 |
| Xerr parent orbit | 72 |
| Zerr parent orbit | 72 |
| collisions | 0 |
| selector generator cases | 48,312 |
| translated schedule replays | 72 |
| translated physical mechanism replays | 144 |

Block equality was checked through a streaming canonical semantic digest;
selector prefix equality was checked record by record. Complete normalized
tuples, rather than hashes, determined selector membership and collision
accounting. SHA-256 labels were recomputed after tuple equality was known.

Closure under generators ((1,0)) and ((0,1)) implies closure under all of
(G). Hence the iteration-188 base formula (F_{188}) is invariant:

\[
F_{188}(S)\iff F_{188}(\delta S),\qquad \delta\in G.
\]

## 6. Lex-leader quotient

Let (v(S)) be the 8,640-bit vector obtained from the 864 ten-bit time words in
canonical edge-name order and most-significant-bit-first order. For every
nonidentity (delta\), the quotient appends

\[
v(S)\le_{\rm lex}v(\delta S).
\]

The recurrence bit is

\[
L_i=(\neg x_i\wedge y_i)\vee((x_i=y_i)\wedge L_{i+1}),
\qquad L_n=\mathsf{true}.
\]

All 16 truth-table cases were checked. There is one uniquely defined recurrence
variable per compared bit, so the lex extension is unique once the base
assignment is fixed. The checker reconstructed all 4,907,591 appended clauses
and verified that the 6,890,981-clause base is an exact prefix.

Every finite orbit contains a least vector. Invariance then gives the exact
equisatisfiability theorem

\[
F_{188}\text{ SAT}\iff
F_{188}\wedge\bigwedge_{\delta\ne0}
[v(S)\le_{\rm lex}v(\delta S)]\text{ SAT}.
\]

The reverse implication is immediate. For the forward implication, translate
any base model to an orbit-minimal representative; invariance preserves every
base clause and the representative satisfies all leaders. A stabilizer can make
several group elements attain the minimum, but they produce the same vector.

## 7. Exact meaning of a future quotient UNSAT

An independently proof-checked UNSAT result for the fresh iteration-188
quotient would imply that its invariant base has no model. The universal frozen
family distance-11 ceiling would then require every additional link below:

1. the frozen source exactly represents all legal in-scope schedules;
2. each inherited block and selector is sound;
3. the registry is invariant (proved above);
4. the lex quotient is equisatisfiable (proved above);
5. the UNSAT proof checks independently, including proof controls;
6. exclusion of every surviving schedule is equivalent to existence of a
   complete direct weight-at-most-10 mechanism;
7. the reviewed relation between that direct mechanism and
   (d_{\rm circ}\le11) applies universally.

Round104 does not invoke this chain because iteration 187 returned SAT and the
fresh iteration-188 quotient has never been started.

## 8. Round104 conclusion

The iteration-187 representative is a legal schedule, but its Xerr and Zerr
queries each have a physically replayed weight-10 mechanism. It is therefore
not an explicit distance-12 circuit. Adding the two complete translation orbits
is sound and preserves invariance, producing a scientifically material but
nonclosing continuation. The smallest honest residual is the exact fresh
iteration-188 quotient with SHA-256
`29b16602aa5cdf0e4207271cb50045454ea0aba9254396d732414459a4029215`.

