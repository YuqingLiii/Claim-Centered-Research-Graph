# CIRCDIST.gross — circuit-distance certification tooling feasibility (2026-08-20)

Background feasibility study (spawned by the round-1 gross recon before the no-sub-agent rule;
committed by the dispatcher). Repricing input for the candidate-certification route.

## Headline

Nobody has exactly certified the circuit-level distance of a gross-code syndrome-extraction
circuit as of Aug 2026. The exact-certification frontier for BB circuits: d_circ = 6 for the
[[72,12,6]] SEC (m4riCC 11 s; Gurobi 2.9 h) and d_circ = 8 for [[90,8,10]]
(arXiv:2503.10988 App. D, shortest_error_sat_problem + MaxSAT). The gross SEC is 1-2 rungs above
the frontier: Gurobi 8 h returns incumbent 11 unclosed; MIP-SCIP/CLISAT return nothing usable;
heuristics (m4riRW 316 s, QDistEvol 6.3 h) reach upper bound 10.

Reframing: for the standard Bravyi depth-7 gross SEC an explicit weight-10 undetectable logical
is KNOWN (arXiv:2308.07915 Table 1, d_circ <= 10; "all 936 variants of the syndrome cycle give
d_circ <= 10", conjectured = 10) — this is the source of the "936" figure. The SBB candidate
(arXiv:2603.05481) is a DIFFERENT, depth-8 conjectured-11 circuit; SBB Thm 1 reduces
non-interleaved circuit distance to d_ext of an extended code ("potentially allowing the exact
distance to be determined") — the most promising structural shortcut in the literature, and the
route CIRCDIST.gross's candidate-certification already uses. Contrast: the gross CODE distance 12
certifies in 5.7 s (m4riCC), 58.6 s (Gurobi) — circuit vs code is the whole difficulty; the
360-column Thm-1 reduction sits on the code side of that divide.

## Measured obstructions for the direct DEM route (gross SEC, 12 rounds, Stim 1.16)

72,504 error mechanisms / 1,728 detectors / 12 observables; 97% of mechanisms non-graphlike
(mean detector degree 237); shortest_graphlike_error fails outright; WCNF 660,945 vars /
2,427,997 clauses. Connected-cluster growth N(3) = 3.9e7 with rising branching (~86) =>
~1e21-1e23 cluster visits extrapolated at w = 10 (upper envelope). LP relaxation of GF(2) parity
is vacuous (MILP degenerates to enumeration); the lower-bound half is the hard half
(arXiv:2606.12445's stated bottleneck). Honest estimate for closing the gross SEC by
decision-query MaxSAT (UNSAT at weight 9/10, MaxCDCL or CASHWMaxSAT, per-observable): weeks of
cluster CPU, 20-40% chance within a month, no guarantee.

## The untouched symmetry gap

No distance solver in the literature exploits BB automorphisms (checked: 2603.22532 uses
CCstart=-1 i.e. unrestricted; 2606.12445 has zero symmetry breaking; Magma's
IncludeAutomorphism/quasi-cyclic machinery has never been fed BB groups). Measured on the
Z-filtered deduplicated gross DEM: 8,784 columns in degree classes all divisible by 72 = 12*6,
consistent with a free Z12 x Z6 action => at most 122 orbit representatives => ~70x
constant-factor saving for a symmetry-aware search. Prefactor, not exponent. Adjacent uses:
arXiv:2511.15177 (shift automorphisms + time decimation, for generating logicals, not
certifying); arXiv:2506.03094 App. A.8 (ZX-duality halves CPLEX subproblems).

## Certification-tool taxonomy (verified against the 2603.22532 workbook + tool docs)

Certify lower bounds: stim shortest_error_sat_problem (decision query, UNSAT = certificate);
dist_m4ri method 2/3 (dmin-1 = certified LB); MILP dual bound; DistQLDPC (codes only).
Upper bounds only (never cite as distance): search_for_undetectable_logical_errors (docstring:
heuristic), shortest_graphlike_error (graphlike relaxation, can overshoot), BP-OSD, QDistRnd,
QDistEvol, tesseract, ldpc.estimate_code_distance.

## Uncertainty flags

d_circ(gross SEC) = 10 is a conjecture, not a theorem. DEM mechanism counts differ from the
paper's Table 20 by counting conventions (dedup ~15%); detector counts match exactly. The single
missing number: the dual bound Gurobi actually proved in its 8 h gross run (workbook records only
the incumbent 11). Noise model changes d_circ (EM3 gives <= 8). Verification levels per item in
the underlying session transcript; nothing in the repository was modified by the study itself.
