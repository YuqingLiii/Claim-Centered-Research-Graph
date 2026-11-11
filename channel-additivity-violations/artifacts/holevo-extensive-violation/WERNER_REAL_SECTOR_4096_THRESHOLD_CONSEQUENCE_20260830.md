# Real-Werner sector consequence under the centered 4096 threshold

Date: 2026-08-30

Status: proposer-side consequence assembly for Question 3. The two premises used below are
`PROVED`, but the new exact route and claim remain `CONJECTURED` until a fresh independent review
hash-binds them. This note does not modify or replace the older `m>e^18` real-Werner node.

## 1. Exact scoped statement

Fix an integer `m>=2` and `eta>=0` such that

\[
 [18m(1+\eta)^2+81(1+\eta)^4](1-m^{-2})>4096^2.       \tag{1}
\]

For each `d`, let `U_1^(d),...,U_m^(d)` be independent Haar unitaries in `U(d)`, and put

\[
 R_U={1\over m^2}\sum_{v,a=1}^m
 U_v^*U_a\otimes U_a^*U_v,
 \qquad
 A=1+{9(1+\eta)^2\over m},
\]

\[
 H=\sqrt{(A^2-1)(1-m^{-2})}.
\]

Let `M_U=C^* tensor C^*` be the same-tuple two-leg coefficient map in the established project
convention, and let `F_m` be the flip on `C^m tensor C^m`. The proposed consequence is

\[
 \Pr\left\{
   \|M_U(Y)\|_\infty\le {A\over m}\|Y\|_2
   \text{ simultaneously for every }
   Y=\alpha I_{m^2}+\beta F_m,\ \alpha,\beta\in\mathbb R
 \right\}\longrightarrow1.                              \tag{2}
\]

In particular, (2) holds for every fixed `eta>=0` and every integer `m>=932064`.

## 2. Two-premise proof

Define the centered spectral event

\[
 E_d=\left\{\|R_U-I_{d^2}/m\|_\infty\le H\right\}.       \tag{3}
\]

The `PROVED` node
`HEXT.same-tuple-werner-centered-bound-4096-threshold` states, under (1), that

\[
 \Pr(E_d)\longrightarrow1.                               \tag{4}
\]

For each fixed unitary tuple, the `PROVED` node
`HEXT.same-tuple-werner-spectral-reduction` states the deterministic equivalence

\[
 E_d
 \quad\Longleftrightarrow\quad
 \|M_U(Y)\|_\infty\le {A\over m}\|Y\|_2
 \text{ for every real }Y=\alpha I_{m^2}+\beta F_m.       \tag{5}
\]

The event on the right side of (5) is exactly the event in (2), not merely an event containing
or contained in it. Hence its probability equals `Pr(E_d)` for every `d`, and (4) proves (2).
The integer corollary is inherited verbatim from the first premise.

## 3. Why this is a new node rather than an edit

The existing node `HEXT.same-tuple-real-werner-sector-large-m` has the different public
hypothesis `m>e^18` and a different exact claim hash. It remains valid historical state. The new
node records the strictly stronger parameter interface (1), including the smaller eta-uniform
integer threshold `932064`, without rewriting that older proposition or its events.

## 4. Strict boundary

The conclusion is simultaneous only over the real two-dimensional Werner coefficient span

\[
 \operatorname{span}_{\mathbb R}\{I_{m^2},F_m\}.
\]

It does not prove the corresponding estimate for arbitrary Hermitian coefficients, arbitrary
complex coefficients outside this real span, the physical global `n=2` optimization, any
all-copy statement, absolute-unbounded leakage, or full-size extensive violation. No such node
may inherit a completion level from this consequence.

## 5. Review gate

Before promotion, a reviewer independent of this proposer-side registration must verify:

1. both premise claims and their current `PROVED` hashes;
2. the exact identity dimensions `I_(d^2)` and `I_(m^2)`;
3. the normalization `A/m` and Hilbert--Schmidt norm on coefficients;
4. the event equality, rather than a one-way implication with a lost probability quantifier;
5. the fixed-`m`, fixed-`eta`, then `d->infinity` order; and
6. the strict non-propagation boundary in Section 4.
