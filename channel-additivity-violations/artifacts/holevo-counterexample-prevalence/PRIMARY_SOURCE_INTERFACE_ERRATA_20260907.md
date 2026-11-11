# Primary-source interface erratum

Date: 2026-09-07

Status: project-local interface clarification. The archived PDF is immutable; this note does not
edit it or replace its theorem.

## Collins--Youn, arXiv:1907.07856v2, Theorem 3.3

In the printed proof on PDF pp. 11--12, the displayed definition of `E_K` does not enforce
inequality outside `K`, although the subsequent argument needs a disjoint partition by the exact
equality set. Read the partitioning set as

`K_0={j : v_j=w_j}`.

For each exact block, the proof gives a norm upper bound. After summing blocks and applying
Cauchy--Schwarz, the required statement is

`sum_(K_0 proper subset [J]) m^(|K_0|/2) 3^(J-|K_0|) ||a_(K_0)||_HS`

`<= sqrt((m+9)^J-m^J) ||a||_HS`.

This is the interface used in `PRODUCT_HAAR_MOE_ATOMIC_THEOREM_20260830.md`. It preserves the
Theorem 3.3 upper bound needed by the proof; no equality of the norm of a sum is assumed.
