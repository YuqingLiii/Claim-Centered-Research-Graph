# Independent hostile review — KSUM.B4b.U1

Date: 2026-07-19
Reviewer: fresh independent completing reviewer; authored none of the target mathematics; no wanted verdict
Network: not used
Run provenance: ksum/artifacts/logs_ksum_expU_20260719/codex_U1review_run.log

## Pre-action reload

Before doing mathematics I reloaded research/RESEARCH_STRUCTURE_PROTOCOL.md, DAG_PROTOCOL.md (including rule 6), ksum/proof-dag/NODE_INDEX.md, the target KSUM.B4b.U1 and parent KSUM.B4b node files, Appendix B of ksum/paper/ksum_small_alphabet.tex, and ksum/artifacts/references/abi_2103.16390_src/claw.tex.

I also read the local cyclic plateau passage, KSUM.B4a, the ABI recurrence and Zhang-base cards, the Childs–Eisenberg card, and the MNRS statement in ksum/artifacts/references/ksum_W_walkopt/bonnetain_et_al_2509.13909v1_eprint_src/prelim.tex.

## Ruling

**CERTIFIED* with named caveats; not PROVED.** The recurrence, invariant, and requested degree-of-freedom spot checks are correct under the explicit charged-recurrence hypothesis below. The submitted prose does not define an airtight algorithmic family theorem: independent-selector cost is partly a family axiom, and a child upper bound is used as if it were a compulsory lower-bound charge. The cyclic plateau closes only the narrower case of an all-range, range-independent generic base.

The certified statement is:

> In the charged black-box recurrence model F_SC^charge below, with fixed depth (allowed to depend on epsilon), independent nonamortized residual-coordinate access, independent generic children, and a range-independent all-q base of exponent rho, the limiting q exponent is 1-1/(2 rho). With the Johnson/MNRS base rho=2/3, there is no fixed theta<1/4 for which the model yields O_epsilon(N^(1/2+epsilon) q^theta) for every epsilon>0.

This is an obstruction to a specified cost-accounting template, not a quantum query lower bound for every algorithm informally describable as sample–compress.

## Hypothesis that closes the family boundary

Call the precise reviewed model F_SC^charge. It has the target node's syntactic restrictions plus:

1. Recursion depth D is fixed independently of s,q, but may depend on epsilon. A level's sample parameter may depend on state and depth.
2. A worst-case profile may realize b=Theta-tilde(min{s,qs/ell}). Each virtual residual coordinate is selected independently and charged Omega-tilde(sqrt(s/b)) original queries. Queried information is not cached, shared, or amortized between virtual coordinates, children, or levels.
3. A child with monomial charge Theta-tilde(m^a q^c) is charged that many virtual-coordinate calls on the hard profile. This is a definition of the accounting model; an O-tilde child upper bound alone does not establish it for arbitrary algorithms.
4. Children are generic all-input pair solvers unless a residual promise is declared. Constant or subpolynomially many children are independent and share no queried data.
5. A range-independent base m^rho means a uniform bounded-error upper bound for the same cyclic 2-Sum problem for all relevant m,q,t, with no hidden q-dependent exponent. Johnson/MNRS has rho=2/3; pair-Grover has rho=1.

Without items 2–3, same-level batched selection, caching, a cross-level data structure, or another query-reusing composition could reasonably be called sample–compress informally while evading this recurrence.

## Attack 1 — family definition

**Verdict: fails as an airtight algorithm-family theorem; passes after the named hypothesis.**

The node describes the intended ABI implementation, but “generic residual selection” and “generic child” lack an oracle-level definition; same-level batching is not expressly covered by the cross-level exclusion; and the calculation starts from Q_child=O-tilde(m^a q^c) and multiplies that upper bound by selector cost. That derives a specified implementation's cost, not a mandatory algorithm lower bound. A tight residual-mass profile does not by itself prove a direct-sum or composition theorem.

The mass ceiling is sharp at exponent scale. Use Theta(q) nonfixed involution orbits, populate only one side of each with multiplicity Theta(s/ell), and add one rare witness orbit. A random sample misses a constant fraction of decoy values, leaving Theta(qs/ell) residual positions without decoy witnesses. This does not repair the missing query-composition lower bound.

## Attack 2 — invariant and schedules

**Verdict: pass in F_SC^charge.**

Put ell=s^alpha and q=s^kappa. For a child charge m^a q^c with a>=1/2 and tight b=s^(1+kappa-alpha), the composed child exponent is

E_child = 1/2 + (a-1/2)(1+kappa-alpha) + c kappa.

The level exponent is max{alpha,1/2,E_child}. For a>1/2, alpha and E_child move oppositely and bind at

alpha(a+1/2)=a+(a-1/2+c)kappa.

Thus a'=a/(a+1/2) and c'=(a-1/2+c)/(a+1/2). At a=1/2 equalization degenerates because residual size cancels, but the limiting map is a'=1/2,c'=c. The sqrt(s) work is slack. If ell<q, a hard profile leaves residual mass Theta(s), so the level cannot improve on skipping it.

From (2/3,0), direct iteration gives a_D=2^(D+1)/(2^(D+2)-1), c_D=(2^D-1)/(2^(D+2)-1), and c_D=1/4-(3/2)(a_D-1/2). From (rho,0), the invariant is c=(1-1/(2rho))-(a-1/2)/rho; a 1/6 limit requires rho<=3/5.

Nonuniform depth schedules do not help. The Bellman step minimizes the pointwise maximum above. The parent operator is monotone in the child's pointwise cost, so replacing an optimal remaining-depth child with a nonoptimal schedule cannot improve a later level. For an affine child the minimizer is exactly Phi. Coordinatewise Phi is increasing in a and c in the relevant region.

The exact quantifier is no fixed theta<1/4 for every epsilon>0. Each finite depth has c_D<1/4 but also a_D>1/2, so it is not a counterexample. Depth is fixed independently of input size. Appendix B's short-list Johnson and direct large-q branches are consistent with this active-recursion calculation.

## Attack 3 — plateau

**Verdict: pass only for an explicitly uniform range-independent base; otherwise there is a quantifier hole.**

If Q_base(m,q)=O-tilde(m^rho) for every input and q, instantiate q=Theta(m). The proved cyclic 2-Sum plateau Omega(m^(2/3)) forces rho>=2/3.

It does not force every useful residual solver's m-exponent to be 2/3. It does not automatically apply to residual promises. For m^a q^c it gives only a+c>=2/3. Moreover q=Theta(m) lies outside the recursion's active q<=m^(2/3) region, so a piecewise generic solver could be faster only there and revert to Johnson at the plateau. “Optimal generic base m^(2/3)” is therefore too broad unless generic means the all-q range-independent base in hypothesis 5. A q-dependent or promise-aware solver is a genuine escape.

## Attack 4 — degree-of-freedom spot checks

**Verdict: the requested rows pass; one wording defect and one omitted derivation remain.**

Residual Johnson/MNRS: let gamma=Theta-tilde(sqrt(s/b)). Setup is S=Theta-tilde(r gamma), update U=Theta-tilde(gamma), the Johnson gap is delta=Theta(1/r), and a fixed witness has marked fraction epsilon=Theta((r/b)^2). The on-disk MNRS formula S+epsilon^(-1/2)(delta^(-1/2)U+C), with query-free checking, gives gamma(r+b/sqrt(r)). Balancing gives r=Theta(b^(2/3)) and Theta-tilde(sqrt(s)b^(1/6)). The formula passes. The row's phrase “setup/update costs Theta-tilde(sqrt(s/b))” is inaccurate literally: setup has the extra factor r.

Pair-Grover: Theta(b^2) pairs require Theta(b) Grover tests, each with O(1) virtual evaluations, for Theta-tilde(b sqrt(s/b))=Theta-tilde(sqrt(sb)). This is worse than the walk for nonconstant b.

Dyadic stratification: a multiplicity-mu value is missed with probability exp(-Theta(ell mu/s)). Bucket multiplicities dyadically. Above Theta((s/ell)log(qs)), a union bound removes all buckets with high probability; below it, at most q values contribute O-tilde(qs/ell). Theta(q) one-sided decoys at mu=Theta(s/ell) attain the scale. Only logarithms change. The node states but does not derive this.

The checked MNRS theorem text is physically under ksum/artifacts/references and is reached from cards/catalog material under research/literature; no MNRS theorem text itself was found under research/literature.

## Attack 5 — consistency

**Verdict: pass.**

Appendix B's algorithm lies on the boundary: finite D has a_D>1/2 and c_D<1/4; D(epsilon) gives O_epsilon(N^(1/2+epsilon)q^(1/4)). ABI's k=2 recurrence has the same limit. At q=Theta(N), cyclic 2-Sum/claw is Theta(N^(2/3)); Appendix B uses direct Johnson in the large-q/short-list regime. At q=N^(2/3), N^(1/2)q^(1/4)=N^(2/3). There is no contradiction.

## Defects

| ID | Severity | Location | Defect | Repair/interpretation |
|---|---|---|---|---|
| D1 | MAJOR | Family F_SC bullets 3–6; Exact one-level balance through (U1.3) | Soft terms and an upper-bound-to-lower-bound direction change do not establish an algorithm-family lower bound. | State F_SC^charge hypotheses 1–4 and call the result a cost-model certificate; a true family theorem needs a composition/direct-sum proof. |
| D2 | MODERATE | Iteration plateau paragraph; Binding constraint and escape conditions | Plateau constrains only an all-q range-independent generic base. | Retain uniformity and name q-dependent/promise-aware bases as escapes. |
| D3 | MINOR | Claim; depth-schedule row | Theta and depth quantifiers are implicit. | Theta is fixed independently of epsilon; depth is fixed independently of input size but may depend on epsilon. |
| D4 | MINOR | Johnson/MNRS and multiplicity rows | Setup wording omits r; dyadic proof is omitted. | Correct the wording and cite/add the derivation. |

## What I did not check

- I did not prove the missing quantum direct-sum/composition lower bound; that is D1.
- I did not search the network or import any absent variable-time/chained-walk theorem.
- I did not review the manuscript outside Appendix B and the plateau passages.
- I did not rerun numerics; the obstruction uses none.
- I do not claim correlated, batched, q-dependent, or promise-aware sample–compress algorithms cannot beat 1/4.

## Status action

Under DAG_PROTOCOL rule 6, this completed archived independent review licenses **CERTIFIED*** with D1–D2 as named caveats. It does not license PROVED because the original family boundary is not airtight. It does not license REFUTED because no concrete in-family algorithm beating 1/4 was produced. B4b, B4, and the root remain OPEN because a scoped family certificate does not close the global exponent window.
