# Theorem notes

## 1. Exact branch semantics

Branch A requires one complete legal frozen `S_Gross` schedule whose unrestricted direct Xerr and Zerr minimum fault weights are both at least 12. Branch B requires a proof covering every legal frozen `S_Gross` schedule and showing at least one error sector has a nontrivial undetected mechanism of weight at most 11. A SAT outer schedule is evidence for neither branch until direct adjudication; a SAT direct trace proves only the decoded candidate fails Branch A; a finite registry is not a universal exhaustion theorem.

## 2. Direct mechanism reconstruction

For each sector, the direct query has 360 primary fault columns and only: (i) a cardinality recurrence for weight at most 10, (ii) 72 syndrome XOR rows set to zero, (iii) 12 logical-parity XOR rows, and (iv) a disjunction requiring at least one logical parity. There is no pool, residual-pattern, check-count, or within-check order restriction. The independent standard-library audit rebuilds Gross incidence, all 720 columns, each hook suffix from the schedule, the detector/stabilizer row spaces, and the 12-dimensional logical quotient. For the ten selected names it computes both canonical and physical XOR supports, obtains zero syndrome in each representation, equal nonzero logical parity vectors, and proves neither support lies in the appropriate stabilizer span. Thus both mechanisms are physical nonstabilizers, not encoding artifacts.

## 3. CSS involution

Write group coordinates as `g=(i,j)` in `Z_12 x Z_6`. Translation is `T_delta`. The involution is

`D: X:c:q <-> Z:-c:D(q)`,

where `D(q)=72+(-q)` for `q<72` and `D(72+r)=-r`; residual kind positions and layer labels are fixed. Exhaustive edge checks establish `D^2=1` and `D T_delta D=T_-delta`. Concrete check supports, data incidences, all 648 MC overlaps, detector/stabilizer spans, logical quotient, resource conflicts, and global interleaving are preserved (with X/Z exchanged). Hence a reviewed block or direct selector transports soundly under D.

The iter193 registry was translation closed but not D closed: exactly nine nonfree size-36 block orbits (324 blocks) and one nonfree size-36 selector orbit (36 selectors) were absent. Those images were installed with explicit parent provenance, stabilizers, collision checks, and translated physical replay. The new Xerr mechanism has orbit size 36 with stabilizer two; the Zerr mechanism has orbit size 72 with trivial stabilizer. Their CSS images form two additional disjoint orbits of the same respective sizes. The four candidate orbits therefore add `36+72+36+72=216` selectors. Iter194 has `814068+324=814392` blocks and `50580+36+216=50832` selectors.

## 4. Order-144 quotient and nonfree orbits

The full action is `G=(Z_12 x Z_6) semidirect C_2`, represented by `T_delta D^epsilon`. The checker constructs 144 distinct permutations of all 864 named edges and verifies all `144^2*864=17,915,904` composition cases. Registry closure under translation generators plus closure under D implies closure under every element of G. This implication does not require free action.

For each of the 143 nonidentity elements h, flatten the 864 ten-bit time words in canonical edge-name order, most significant bit first, and impose `x <=lex h.x`. At bit i the recurrence is

`le_i <-> ((!x_i) & y_i) | ((x_i==y_i) & le_(i+1))`, with `le_n=true`.

Eight truth-table clauses uniquely define each recurrence variable; one root unit clause asserts each complete comparison. The independent checker exhausts all 16 primitive truth assignments, rejects corrupt/truncated primitive controls, verifies the complete base body as an identical prefix, and reconstructs every appended clause.

Forward satisfiability is immediate because a quotient model is a base model. Conversely, for any base schedule S, the finite set `{h.S:h in G}` has at least one lexicographically least vector C. Source/base invariance makes C a base schedule, and minimality gives `C<=h.C` for every h. Each recurrence then has a unique satisfying extension. Equal images caused by stabilizers satisfy the non-strict comparison, so no size-144/freeness premise is hidden. Therefore the fresh order-144 quotient is equisatisfiable with the full iter194 base family. It remains unstarted; this theorem is not an UNSAT result.

## 5. Exact remaining gap

No checked artifact establishes that the installed exclusion registry exhausts all schedules with distance below 12. Even a future quotient UNSAT proof would show that the particular iter194 base plus its sound exclusions has no surviving schedule; the universal Branch B conclusion additionally depends on the sound interpretation that every exclusion corresponds to a verified low-weight mechanism, which is supplied record by record here and inherited from reviewed parents. This package does not claim a current frozen-family UNSAT theorem because iter194 was not solved.
