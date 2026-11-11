# Hierarchical fixed-partner strong-additivity gate — 2026-08-29

## Question tested

Can one use a sequence of random channels `Phi_n` which is asymptotically additive against every
fixed finite-dimensional partner `Xi`, while `Phi_n tensor conjugate(Phi_n)` keeps a fixed positive
minimum-output-entropy defect? If yes, successively increasing the channel dimensions would make
the unwanted single-side defects summable and the matched cross defects linear.

Canonical node: `ADDGAP.hierarchical-strong-additivity`.

## Primary source checked

Benoit Collins, Motohisa Fukuda, and Ion Nechita, *On the convergence of output sets of quantum
channels*, arXiv:1311.7571v2 (2014), <https://arxiv.org/abs/1311.7571>.

The paper's abstract says that for certain sequences `Psi_n`, the output sets of both `Psi_n` and
`Xi tensor Psi_n` converge for any fixed channel `Xi`. The exact result is Theorem 8.1.

## Exact scope of Theorem 8.1

Under strong convergence of the random projection and its fixed matrix coefficients, Theorem 8.1
states only that, for every fixed finite-dimensional channel `Xi`, there exists a convex body `K`
such that the pure-input output set of `Xi tensor Psi_n` converges to `K` in the sense of Theorem
3.9.

It does **not** identify `K` with the convex hull of product outputs, and it does not state

`Smin(Xi tensor Psi_n) -> Smin(Xi)+Smin(Psi_n)`.

The obstruction is explicit in the source immediately after Theorem 8.1: the authors say that the
limiting output set is difficult to analyze in general and that they cannot describe it even when
`Xi` is the identity map. Section 8.2 obtains an exact product-output-set formula only when `Xi` is
an entanglement-breaking channel satisfying an additional hypothesis (Theorem 8.7). Strong
additivity with an entanglement-breaking partner is already known and cannot create the required
amplification.

## Verdict

The advertised “along with any other quantum channel” phrase is a **convergence-existence** result,
not a fixed-partner minimum-output-entropy additivity result. It therefore does not pass the gate.

No primary theorem was found in the bounded follow-up search that supplies the missing global
entropy equality for an arbitrary fixed partner. The hierarchical blueprint remains mathematically
valid as a conditional lemma, but this literature route is PARKED pending a genuinely stronger
theorem or a new proof of the entropy minimization.

## What would reopen the route

A suitable theorem must provide, for the same channel family carrying the conjugate-pair defect,

`Smin(Xi tensor Phi_n) >= Smin(Xi)+Smin(Phi_n)-epsilon_n(Xi)`

for every fixed `Xi`, with `epsilon_n(Xi)->0`, and must also hold for `conjugate(Phi_n)`. Mere
convergence of an unidentified output set, evaluation of fixed input sequences, or additivity only
against entanglement-breaking partners is insufficient.

