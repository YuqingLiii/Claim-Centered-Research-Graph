# Round126 theorem and scope notes

## 1. Exact quotient consequence

Let `B198(t,u)` be the reviewed base CNF. Its primary variables encode ten-bit edge times `t`, and `u` are uniquely constrained definitional auxiliaries. Let

`G = (Z_12 x Z_6) semidirect C_2`, with `|G|=144`.

The quotient is

`Q198 = B198 AND (AND over g != e of LexLE(t, g.t))`.

Every appended lex comparator is an exact Boolean recurrence, every appended clause was reconstructed independently, and the base CNF is a byte-exact prefix. Since `B198` is invariant under `G`, each finite `G`-orbit of base models has a lexicographically least primary-time vector. That least vector satisfies all 143 non-strict leaders, so `SAT(B198) => SAT(Q198)`. The reverse implication is immediate because `B198` is a conjunct of `Q198`. This argument permits stabilizers and assumes no free action. The retained model assigns all 4,387,647 variables, satisfies all 21,434,596 clauses, and is independently shown to be the least of 144 distinct schedule images.

## 2. Complete direct-360 mechanism criterion

For a sector `S`, enumerate all 360 physical fault columns `c_j` and Boolean selectors `y_j`. Let `H_S` contain all 72 detector rows and `L_S` all 12 logical rows. The direct query is exactly

`sum_j y_j <= 10`,

`H_S (sum_j y_j c_j) = 0 over GF(2)`,

`OR_r [L_S (sum_j y_j c_j)]_r = 1`.

There is no pool, residual-pattern, check-count, within-check-family, sampling, or partial restriction. Each sector returned a complete weight-10 SAT assignment. Separate clause checkers cover every variable and clause. A standard-library auditor reconstructs all 360 columns per sector, the canonical and physical supports, all 72 syndrome bits, all 12 logical bits, stabilizer membership in both representations, stabilizer rank 66, logical quotient dimension 12, and cross-pairing rank 12. Therefore either SAT sector is a sound candidate-kill certificate; both sectors are retained for symmetric adjudication.

## 3. Translation and CSS closure

Write a coordinate as `q=6i+j`, with `i in Z_12`, `j in Z_6`. Translation acts by

`T_(a,b)(q) = 6((i+a) mod 12) + ((j+b) mod 6)`

in each 72-qubit half. CSS duality swaps `X` and `Z`, negates the check coordinate, and maps data coordinates by exchanging halves and negating the within-half coordinate. Residual kind is fixed. Direct enumeration on all 864 named edges verifies `D^2=I` and `D T_delta D=T_-delta`, giving the order-144 action. Each of the Xerr, Zerr, CSS-dual-of-Xerr, and CSS-dual-of-Zerr translation orbits has identity stabilizer and size 72. All 288 schedules and mechanisms were physically replayed. Full semantic tuple comparisons prove the four orbits pairwise disjoint and collision-free against the 51,840-selector inherited registry.

## 4. Scientific boundary

The iteration-198 schedule candidate is killed and 288 sound selector exclusions are installed in a deterministic iteration-199 frontier. This is material progress, but it is not a legal distance-12 witness, a whole-family universal distance-at-most-11 theorem, root closure, exhaustion, or interval narrowing. `CIRCDIST.gross` and `gap-via-lift` remain `CONJECTURED`; `D*_Gross` remains in `{11,12}`.
