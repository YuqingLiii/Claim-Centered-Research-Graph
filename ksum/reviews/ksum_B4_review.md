# Independent hostile review of the B4 cyclic 2-Sum upper-bound note

Review target: ksum/artifacts/ksum_B4_upper_note.md  
Reviewed SHA-256: c99c681233b5795b089338532ca58f57d6c64a781ac35d7719be37b90ba91e84

ABI source checked: ksum/artifacts/references/abi_2103.16390_src/claw.tex  
SHA-256: a3cce85beb4780becfec3d7474f85f4945751ea8df422552b7eaea271904fef9

Reviewer/run provenance: fresh Codex hostile-review session, 2026-07-18, working
directory <machine-local-path-redacted> no network used.
Transcript: ksum/artifacts/logs_ksum_B4_20260718/codex_review_run.log. The ordinary
PowerShell sandbox helper failed to launch twice because
codex-windows-sandbox-setup.exe was not found. Repository reads and hashes were
therefore done through the sandboxed Node REPL. apply_patch then failed even on
a one-line probe, so the requested review/DAG writes used that same sandboxed
filesystem fallback. No numerical claim, script, or numerical log was used.

## Ruling

B4a remains **CONJECTURED**. The candidate theorem is not refuted, and the
single-list/fixed-point repair is structurally correct. But the note is not a
complete bounded-query proof as written. It omits:

1. the recursive subcase in which the actual compressed length is too small for
   ABI's inductive small-range hypothesis; and
2. a worst-case query cap on the low-probability event that sampling leaves a
   residual larger than its high-probability bound.

Both omissions are repairable, and repairs are derived below. Those repairs are
new material in this review and have not themselves received the independent
review required for a completion-tier status.

Defect count: **2 MAJOR, 2 MINOR, 0 FATAL**. There is no counterexample to the
claimed asymptotic bound, so REFUTED would overstate the evidence.

## Step 1 — ABI source extraction

**Verdict: PASS, with one harmless source typo and one disclosed source-level
ambiguity.** I read the actual upper-bound proof in claw.tex.

Load-bearing lines:

- Lines 125–132 define the two-list claw. Lines 84–90 state the regime
  2 <= k < n and upper bound O(n^(1/2+epsilon) k^(1/4)); lines 140–143 repeat
  the theorem.
- Lines 148–155 say “Select a random sample” of size 4 n^alpha ln n, query it,
  and Grover-search the other list. Lines 156–160 reverse the lists.
- Lines 161–170 call the recursive claw algorithm and specify a
  “pseudorandom permutation” plus “Grover's minimum search” returning the first
  unseen entry.
- Lines 172–175 define B,B' and b. Lines 177–194 give the sampling tail
  argument and conclude that “both b and b' are at most” k n^(1-alpha) with
  probability 1-o(1).
- Lines 196–204 use 4b ln n permutations and claim residual coverage. Lines
  206–220 put the first residual element within O((n/b) log n) positions and
  charge O-tilde(sqrt(n/b)) per virtual query.
- Lines 222–225 display the recurrence

      O-tilde(n^alpha + n^(1/2)
              + Q(Claw_(4b ln n -> k)) n^(1/2-beta/2)).

- Lines 240–251 define A_0,A_i and

      T_i(kappa)=((2^i-1)kappa+2^(i+1))/(2^(i+2)-1).

  Lines 252–281 verify the inductive balance for 0 <= kappa <= 2/3, and lines
  284–286 give limiting coefficients 1/4 and 1/2.

Every substantive claim attributed to ABI is in the source. The note correctly
labels approximate counting, truly random permutations, coherent error
reduction, and the all-range fallback as its own reconstruction.

Qualifications:

1. claw.tex:169 tests y against the undefined X_(A'); context and lines 158,173
   show Y_(A') is intended. The note silently uses the intended sample set.
   This is a MINOR source transcription issue, not a false mathematical
   attribution.
2. ABI defines only |B|=b but uses 4b ln n virtual coordinates for B and B'
   although line 193 separately mentions b'. Thus ABI does not justify unequal
   residual sizes as written. The note explicitly flags this at lines 70–73;
   the single-list port has only one residual size.

## Step 2 — independent reconstruction

### Search/walk and within-list structure

Take a sample A of ell=Theta(n^alpha log n) positions and store their values.
Pairs inside A are checked with no further queries. One Grover search over
positions outside A, using predicate x_j in sigma(S), catches every pair having
a sampled endpoint; stored-set membership is query-free.

After a correct negative search, every remaining pair has both endpoint values
outside S, hence both indices in B. If an outside value also occurred at a
sampled position, its partner would satisfy the Grover predicate and would have
been found. Thus the one-sample construction loses no within-list pair and does
not assume a claw bipartition.

The base is the Johnson walk on r-subsets. Setup costs r queries, update costs
O(1), spectral gap is Theta(1/r), and a fixed witness marks
Omega((r/n)^2) of the subsets. Its query cost is

    O(r + (n/r)sqrt(r)) = O(r+n/sqrt(r)),

minimized at r=Theta(n^(2/3)). Marking uses stored values and distinct indices,
so the base works for every q,t and does not conflate equality with partnership.

### Fixed points and compression

For Z_q, 2v=t has one solution for odd q, zero for even q and odd t, and two for
even q and even t. Thus all fixed-point values—not just one—are listed without
input queries.

For each v, search for and verify one occurrence, then search the complement of
that index for and verify a second. With per-search error delta, the total is at
most 4 delta. Missing a first or second occurrence can cause a false negative
after exclusion, but only on this charged error event. On the good event, a
negative result proves multiplicity at most one, so excluding every fixed-point
position is safe.

Independent uniform permutations make each first residual index independent
uniform on B. With L=Theta(b log n),

    Pr[some residual index absent] <= b exp(-L/b).

Coverage preserves every genuine residual pair. A virtual hit whose coordinates
map to distinct original indices is genuine. If both map to the same index,
2x_i=t, making it a fixed point, which was excluded. Compression therefore
creates no false pair and loses no genuine pair on the coverage good event.
This argument remains valid through multiple recursion levels.

### Balance and the missing recursive subcase

Let q=n^kappa, alpha=T_i(kappa), and on the sampling good event
b <= q n^(1-alpha). A virtual query costs O-tilde(sqrt(n/b)). If the actual
compressed length m=Theta(b log n) satisfies q <= m^(2/3), the inductive
small-range bound applies. Its recursive term is

    n^(1/2) b^(-1/2) m^T_(i-1)(log_m q).

It is nondecreasing in b. At b=q n^(1-alpha), its normalized exponent is

    (1-alpha+kappa)
      T_(i-1)(kappa/(1-alpha+kappa))
      +(alpha-kappa)/2,

which ABI lines 263–281 bound by T_i(kappa). Repeated balancing gives

    T_i(kappa)=a_i+c_i kappa,
    a_i=2^(i+1)/(2^(i+2)-1),
    c_i=(2^i-1)/(2^(i+2)-1),

with limiting coefficients 1/2 and 1/4.

For a particular input, however, b can be much smaller than its upper bound, so
q > m^(2/3). The displayed inductive hypothesis is then unavailable. The
repair is an internal Johnson fallback:

    O-tilde(n^(1/2)b^(-1/2)b^(2/3))
      = O-tilde(n^(1/2)b^(1/6))
      <= O-tilde(n^(1/2)q^(1/4)),

because b < q^(3/2). For 0<=kappa<=2/3 this is at most n^T_i(kappa), since for
d=2^(i+2)-1,

    T_i(kappa)-(1/2+kappa/4)=(2-3kappa)/(4d) >= 0.

This repairs the case, but it is absent from the note (D1).

### Query/error accounting

One level costs O-tilde(n^alpha) to load the sample, O-tilde(sqrt n) for the
partner and fixed-point searches, and O-tilde(sqrt(n/max{b,1})) for relative
counting with a separate zero search. Since alpha>=1/2, these fit the level
budget.

Using an upper constant-factor estimate b_hat, take
L=Theta(b_hat log n) and search the first
K=Theta((n/b_hat)log n) permutation positions (capped at n) for the minimum
marked position. Constants absorb counting slack, giving
O-tilde(sqrt(n/b)) virtual-query cost on the good events.

Returned candidates can be verified. Minimum finding can be made a clean
approximate oracle by deferring measurements, computing, copying, and
uncomputing. If a recursive call makes M virtual queries, amplify each virtual
oracle to operator error O(1/M); the hybrid bound keeps total error constant.
At fixed recursion depth, sampling, coverage, counting, Grover, walk, and
nested-oracle errors cost only polylogarithmic overhead.

A high-probability bound on b does not, however, bound maximum queries on a bad
sample. A complete algorithm must use the count to abort/truncate when an upper
estimate exceeds a constant multiple of q n^(1-alpha), charging that rare event
to failure probability. The note does not specify this cap (D2).

## Defects

### D1 — MAJOR: induction used outside its proved range

Location: ksum/artifacts/ksum_B4_upper_note.md:132–144, especially 138–144.

The note applies the T_(i-1) expression for every actual b, although ABI's
induction only covers range exponent at most 2/3 relative to the recursive
length. Monotonicity does not authorize an out-of-domain formula. The internal
Johnson fallback and inequality above repair it, but require independent review.

### D2 — MAJOR: no worst-case query cap on bad sampling

Location: ksum/artifacts/ksum_B4_upper_note.md:104–116, 136–144, and 169–172.

The residual bound is probabilistic, while L and recursive work depend on the
observed residual. On a bad sample the written algorithm can exceed the claimed
worst-case query budget. Bounded-error query complexity does not allow an
over-budget branch merely because it is unlikely. Abort/truncate after an upper
constant-factor count (or fixed retries) and include the event in the error
budget.

### D3 — MINOR: epsilon is spent twice

Location: ksum/artifacts/ksum_B4_upper_note.md:154–163.

The note chooses depth with a_i<=1/2+epsilon and then absorbs polylogarithms into
another N^epsilon. Literally that yields 1/2+2epsilon. Start with epsilon/2:
use half for depth and half for logarithms.

### D4 — MINOR: deterministic fixed-point wording hides search error

Location: ksum/artifacts/ksum_B4_upper_note.md:89 and 171.

“After a negative result” proves multiplicity at most one only on the amplified
search good event. An undetected double followed by exclusion is a possible
false negative. The generic amplification sentence can cover it, but the proof
should name this event, verify candidates, and allocate error over both searches
for both possible fixed values.

## Step 3 — range, parity, and quantifiers

**Verdict: PASS after D1/D2 repairs; no odd-q assumption is needed.**

- For 2 <= q <= N^(2/3), kappa lies in [0,2/3],
  alpha=T_i(kappa)<=2/3, and alpha>=kappa, as ABI requires.
- For q >= N^(2/3), the range-independent base satisfies
  N^(2/3) <= N^(1/2)q^(1/4). No q<N or q=O(N) assumption remains.
- The algorithm works directly with sigma(x)=t-x. Translation confirms one
  target class for odd q and, for even q, an even class with two fixed points
  and odd class with none. Step F handles both.
- Given requested epsilon>0, choose depth for epsilon/2 and spend the other half
  on fixed-depth polylogarithms. Constants may depend on epsilon. No uniform
  little-o statement follows.
- Finitely many small N and oversized formal samples can be dispatched directly.

## Step 4 — numerics

Not run. No ksum/tools/ksum_b4r_*.py scripts were present. These analytic defects are
not decided by small instances. No numerical evidence or SHA-256 triplet is
claimed.

## What I did not check

- ABI's lower-bound section.
- The literature proofs of Johnson walk, Grover search, approximate counting,
  or minimum finding; I used their standard bounded-error query guarantees and
  checked their composition here.
- A gate/time/space-efficient circuit implementation. This is query complexity.
- Arbitrary abelian groups with growing |{v:2v=t}|; tau<=2 is load-bearing.
- Optional numerics or numerical logs as mathematical support.
- The reviewed note itself was not edited, per the append-only instruction.

## Final status justification

Attribution and the core single-list repair pass. No bipartition is needed;
non-fixed duplicates are harmless; all cyclic fixed points and all parity/target
classes are handled; and the limiting q^(1/4) balance is correct. D1 and D2 are
nevertheless proof-completeness defects in quantified branches. Because this
review first supplies their repairs and those repairs are not independently
checked, rule 6 licenses neither PROVED nor CERTIFIED*. B4a remains
**CONJECTURED**, now with a completed review and concrete repair list.
