# Primary-source interface errata

Date: 2026-09-07

Status: local interface clarification. The archived PDFs are immutable primary sources; this file
does not edit them or silently replace their statements.

## Collins--Youn, arXiv:1907.07856v2, Theorem 3.3

In the printed proof on PDF pp. 11--12, the displayed definition of `E_K` does not enforce
inequality outside `K`, although the subsequent argument needs a disjoint partition by the exact
equality set. Read the partitioning set as

`K_0={j : v_j=w_j}`.

For each exact block, the proof gives a norm **upper bound**. After summing blocks and applying
Cauchy--Schwarz, the required statement is

`sum_(K_0 proper subset [J]) m^(|K_0|/2) 3^(J-|K_0|) ||a_(K_0)||_HS`

`<= sqrt((m+9)^J-m^J) ||a||_HS`.

The corrected inequality is the interface used in
`FINITE_DIMENSIONAL_UNBOUNDED_GAP_PROOF_20260829.md` and
`PRODUCT_HAAR_MOE_ATOMIC_THEOREM_20260830.md`. It preserves the theorem bound needed by the local
proof; no equality of the norm of a sum is assumed.

## Hayden--Penington, arXiv:2012.07861v1, Eq. (1)

The printed introductory capacity formula on PDF p. 2 omits the normalization by `1/n`. The
unassisted classical capacity used in this repository is

`C(N)=lim_(n->infinity) chi(N tensor n)/n`.

The Q1 proof and the fixed-channel regularization node already use this normalized formula. The
Hayden--Penington PDF is used only for the full-size extensive question and its conditional
dichotomy, not as authority for the misprinted unnormalized expression.

## Scope

These are source-interface errata, not new claims about the archived papers and not evidence that
the full-size extensive question has been solved. The absolute-unbounded finite-dimensional atom
remains separate from the OPEN Hayden--Penington-scale root.
