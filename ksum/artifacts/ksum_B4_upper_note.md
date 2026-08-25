# B4 upper-bound note: porting the ABI small-range claw algorithm to cyclic 2-Sum

**Status: CONJECTURED — pending-review:** the port and its analysis below are new, single-author work. Under DAG_PROTOCOL.md rule 6 they are not a completion claim until a fresh independent reviewer has finished and archived a review. No numerical evidence is claimed.

**Verdict candidate.** The ABI algorithm appears to port to 2-Sum over Z_q. The single-list change leaves ABI's compression recurrence intact. Compression samples residual indices with replacement, however, and can duplicate one original position. That creates a false 2-Sum witness exactly when the duplicated value is a fixed point of sigma(x)=t-x. For cyclic groups there are at most two such values; an O(sqrt(N)) preprocessing step detects genuine multiplicity-two fixed-point witnesses and then excludes all remaining fixed-point positions from compression. Subject to the reconstructed implementation details in Sections 3 and 5, the resulting query bound is

    Q(2-Sum_{Z_q,t,N}) = O_epsilon(N^{1/2+epsilon} q^{1/4})

for every q >= 2 and every target t. For q <= N^{2/3} it comes from the recursive ABI port; for q >= N^{2/3} it follows from the range-independent O(N^{2/3}) Johnson walk. This is the exact ABI-style form: a family of fixed-depth bounds whose N-exponent approaches 1/2 and whose q-exponent approaches 1/4. I do not promote it to either N^{1/2+o(1)}q^{1/4} or sqrt(N)q^{1/4+o(1)} without controlling recursion-depth-dependent constants.

## 1. On-disk problem facts used

The paper defines 2-Sum by distinct positions and records the involution form: a hit has x_j=sigma(x_i), where sigma(x)=t-x, and tau=#{x:2x=t} is the number of fixed points (ksum/paper/ksum_small_alphabet.tex:117-123). Thus:

- if a != sigma(a), any occurrence of a and any occurrence of sigma(a) at distinct positions form a hit;
- if a=sigma(a), a hit needs two distinct occurrences of a.

The on-disk C7 classification says that the k=2 problem is determined, up to constant query factors, by (N,q,tau) and the cycle type of sigma (ksum/paper/ksum_small_alphabet.tex:228-230). The final report invokes the translation theorem to cover every target at odd q (ksum/notes/KSUM_FINAL_REPORT.md:21); the actual lemma states that targets differing by an element of 2G are equivalent and proves it by a uniform coordinate shift (ksum/paper/ksum_small_alphabet.tex:164-170).

The available range-independent upper bound is the Johnson-walk bound O(N^{k/(k+1)}), hence O(N^{2/3}) at k=2 (ksum/paper/ksum_small_alphabet.tex:48). The paper explicitly records that no better small-q upper bound was known and asks whether the ABI algorithm has a 2-Sum analog (ksum/paper/ksum_small_alphabet.tex:449-455).

## 2. ABI extraction

Here ABI's n is the length of each claw list and ABI's k is the range size; below I write the latter as kappa to avoid collision with k-Sum notation.

### Exact statement

ABI define claw on two length-n lists at ksum/artifacts/references/abi_2103.16390_src/claw.tex:120-133. Their abstract places the result in the regime 2 <= kappa < n and states lower and upper bounds (ksum/artifacts/references/abi_2103.16390_src/claw.tex:84-90). The theorem itself says:

> “For all epsilon>0” the complexity is O(n^{1/2+epsilon} k^{1/4}).

This is ksum/artifacts/references/abi_2103.16390_src/claw.tex:140-143; the same contribution is announced at ksum/artifacts/references/abi_2103.16390_src/claw.tex:135-138.

### Algorithm actually written in ABI

ABI set kappa=n^varkappa and introduce a sample exponent alpha (ksum/artifacts/references/abi_2103.16390_src/claw.tex:145-148). Their steps are:

1. Sample ell=4 n^alpha ln n positions from the first list, query them, and Grover-search the entire second list for a sampled value (ksum/artifacts/references/abi_2103.16390_src/claw.tex:149-155). Repeat with the roles of the lists reversed (ksum/artifacts/references/abi_2103.16390_src/claw.tex:156-160). This catches every claw incident to a sampled value.
2. Let B,B' be the indices whose values were not seen in their respective samples (ksum/artifacts/references/abi_2103.16390_src/claw.tex:172-175). A Chernoff/union-bound argument shows that every unseen value has multiplicity below n^{1-alpha}, so both residual list sizes are at most kappa n^{1-alpha} (ksum/artifacts/references/abi_2103.16390_src/claw.tex:177-194).
3. Form virtual residual lists. For each virtual coordinate, ABI fixes a pseudorandom permutation and uses Grover minimum search to return the first residual index in that permutation (ksum/artifacts/references/abi_2103.16390_src/claw.tex:161-170). With 4b ln n permutations, every residual index is represented with high probability (ksum/artifacts/references/abi_2103.16390_src/claw.tex:196-204). The first residual element occurs early enough that one virtual-oracle query costs tilde O(sqrt(n/b)) original queries (ksum/artifacts/references/abi_2103.16390_src/claw.tex:206-220).
Load-bearing source phrases are: ABI say “Select a random sample” of size ell=4 n^alpha ln n (ksum/artifacts/references/abi_2103.16390_src/claw.tex:148-152); the virtual oracle uses “Grover's minimum search” to return the first unseen value (ksum/artifacts/references/abi_2103.16390_src/claw.tex:161-170); and their tail bound concludes that “both b and b' are at most” kappa n^{1-alpha} (ksum/artifacts/references/abi_2103.16390_src/claw.tex:188-194).

4. Recursively solve claw on the virtual residual lists. The displayed cost is

       tilde O(n^alpha + n^{1/2}
               + Q(Claw_{4b ln n -> kappa}) n^{1/2-beta/2}),

   where b=n^beta (ksum/artifacts/references/abi_2103.16390_src/claw.tex:222-225). At recursion depth zero ABI uses the ordinary O(n^{2/3}) claw algorithm (ksum/artifacts/references/abi_2103.16390_src/claw.tex:227-251), i.e. the standard Johnson-walk endpoint mentioned in their introduction (ksum/artifacts/references/abi_2103.16390_src/claw.tex:106-111). The walk is therefore at the bottom of the recursion, on the compressed virtual instance; the outer levels are sampling, Grover search, and residual-oracle construction.

### Where kappa^{1/4} comes from

One level using the n^{2/3} base costs n^{1/2+beta/6}, with beta <= varkappa+1-alpha; balancing this against sample cost gives alpha=(4+varkappa)/7 (ksum/artifacts/references/abi_2103.16390_src/claw.tex:227-238). That is not yet the final quarter-power.

ABI recursively bootstrap the improved algorithm. If A_0 is the n^{2/3} algorithm and A_i calls A_{i-1} on the compressed instance, they obtain

    Q(A_i)=tilde O(n^{T_i(varkappa)}),

    T_i(varkappa)=((2^i-1)varkappa+2^{i+1})/(2^{i+2}-1)

(ksum/artifacts/references/abi_2103.16390_src/claw.tex:240-251). They choose alpha=T_i(varkappa), verify that this is legal for 0<=varkappa<=2/3, and identify the compressed range exponent as varkappa/(1-alpha+varkappa) (ksum/artifacts/references/abi_2103.16390_src/claw.tex:252-266). The recursive-cost exponent and its balancing inequality are written at ksum/artifacts/references/abi_2103.16390_src/claw.tex:263-281. Finally,

    T_i(varkappa) -> 1/2 + varkappa/4,

because its two coefficients tend to 1/2 and 1/4 (ksum/artifacts/references/abi_2103.16390_src/claw.tex:284-286). Thus the quarter-power is the fixed point of repeated sample/compress recursion, not a single Johnson-walk balance.

### What ABI only sketches (my identification)

The following details are not supplied in claw.tex and must be reconstructed for a full query algorithm:

- the residual size b is input-dependent but is treated as known in the recursive call (ksum/artifacts/references/abi_2103.16390_src/claw.tex:161-175);
- two residual sizes b,b' are introduced but the displayed recursive instance uses only b (ksum/artifacts/references/abi_2103.16390_src/claw.tex:172-175; ksum/artifacts/references/abi_2103.16390_src/claw.tex:193-194; ksum/artifacts/references/abi_2103.16390_src/claw.tex:222-225);
- “pseudorandom permutation” and Grover minimum search are named, but a coherent bounded-error implementation and nested error reduction are not specified (ksum/artifacts/references/abi_2103.16390_src/claw.tex:161-170; ksum/artifacts/references/abi_2103.16390_src/claw.tex:206-220);
- the proof explicitly analyzes the recursive regime varkappa<=2/3 (ksum/artifacts/references/abi_2103.16390_src/claw.tex:243-260) but does not spell out the easy large-range fallback to n^{2/3}.

These do not affect the exponent calculation, but they matter to an honest port. Section 5 records the reconstruction used here.

## 3. Ported single-list algorithm

Fix Z_q, target t, and input x_1,...,x_N. The description is for one recursive level A_i; A_0 is the standard O(N^{2/3}) Johnson-walk algorithm.

### Step F: dispose of fixed points

Classically compute F={v in Z_q:2v=t}. In a cyclic group:

- odd q: |F|=1;
- even q, odd t: |F|=0;
- even q, even t: |F|=2.

For each v in F, Grover-find one index with value v, then Grover-find a second distinct index with value v. If it exists, output 1. This costs O(sqrt(N)) because |F|<=2. After a negative result, each fixed-point value occurs at most once. Exclude every fixed-point-valued index from every later residual set.

This preprocessing is load-bearing: without it, the virtual compression below can copy one original fixed-point index into two virtual coordinates and manufacture a false hit.

### Step S: sample and search

Write q=N^varkappa and choose alpha as in ABI. Select a uniform sample A subseteq [N] of size ell=C N^alpha log N, query it, and let S be the set of sampled non-fixed values.

1. Check without further queries whether two distinct sampled positions sum to t.
2. Grover-search j notin A for x_j in sigma(S)={t-s:s in S}. If found, output 1.

If both tests are negative, every remaining witness lies in

    B={j in [N]: x_j notin F and x_j notin S}.

On the usual high-probability sampling event, every non-fixed value omitted from S occurs fewer than N^{1-alpha} times. There are at most q values, hence

    b=|B| <= q N^{1-alpha}.

This is exactly the counting fact ABI use for each of their two residual lists, now applied once. A union bound over the q<=N^{2/3} recursive regime makes the failure probability inverse-polynomial when C is a sufficiently large absolute constant.

### Step C: compress the residual list

Estimate b within a constant factor by quantum approximate counting on the predicate defining B. If b=0, return 0. Fix L=C' b log N independent random permutations pi_1,...,pi_L of [N]. Define

    r_s = the first index of B in permutation pi_s, and z_s=x_{r_s}.

The random choices are fixed before the recursive quantum computation. A virtual query to z_s uses reversible minimum finding with the B predicate and costs tilde O(sqrt(N/b)) queries. Run A_{i-1} on the length-L virtual list z with the same target t and range Z_q.

### Correctness of compression — the single-list issue

Conditioned on fixed B, each r_s is an independent uniform element of B. Therefore

    Pr[some j in B is absent] <= b(1-1/b)^L <= b exp(-L/b),

which is inverse-polynomial for large enough C'. On the coverage event, every genuine residual pair appears in the virtual list.

Conversely, suppose two distinct virtual coordinates form a hit. If their underlying indices r_s,r_u are distinct, they are a genuine original pair. If r_s=r_u, the virtual hit implies 2x_{r_s}=t, so x_{r_s} is a fixed point. Step F excluded every such index from B, a contradiction. Hence compression creates no false positive.

This is the entire structural difference from claw. In ABI, repeated virtual copies of an index stay on one side and cannot alone make a cross-list claw. In single-list 2-Sum, repeated copies are safe for non-fixed values and unsafe exactly at fixed points; Step F removes exactly that obstruction.

## 4. Query analysis

For q<=N^{2/3}, put varkappa=log_N q. Use ABI's depth-i choice

    alpha=T_i(varkappa)=((2^i-1)varkappa+2^{i+1})/(2^{i+2}-1).

The fixed-point search, cross-sample Grover search, and approximate count cost at most tilde O(sqrt(N)) plus tilde O(sqrt(N/b)), while loading the sample costs tilde O(N^alpha). Because T_i(varkappa)>=1/2, these are within the claimed level cost (the b=O(1) case contributes only tilde O(sqrt(N))).

The compressed length is L=tilde O(b)<=tilde O(qN^{1-alpha}); one compressed-oracle query costs tilde O(sqrt(N/b)). Since every recursive exponent is at least 1/2, the recursive term is monotone in b and is maximized at the displayed upper bound. Consequently its normalized exponent is the same expression ABI obtain:

    (1-alpha+varkappa)
      T_{i-1}(varkappa/(1-alpha+varkappa))
      + (alpha-varkappa)/2.

ABI's algebra shows this is at most T_i(varkappa) (ksum/artifacts/references/abi_2103.16390_src/claw.tex:263-281). No term introduced by the port has a larger exponent. Thus

    Q(A_i;N,q)=tilde O(N^{T_i(varkappa)})

under the reconstructed oracle/error implementation. Writing

    T_i(varkappa)=a_i+c_i varkappa,
    a_i=2^{i+1}/(2^{i+2}-1),
    c_i=(2^i-1)/(2^{i+2}-1),

we have a_i -> 1/2 and c_i -> 1/4. Given epsilon>0, choose a constant depth i=i(epsilon) with a_i<=1/2+epsilon; also c_i<=1/4. Then

    N^{T_i(varkappa)}=N^{a_i}q^{c_i}
      <= N^{1/2+epsilon}q^{1/4}.

For q>=N^{2/3}, the base Johnson walk gives

    N^{2/3} <= N^{1/2}q^{1/4},

so no recursion is needed. Polylogarithmic factors are absorbed into N^epsilon in the usual asymptotic statement.

## 5. Reconstruction details not proved in ABI's text

The mathematical port above uses the following standard query-model completions. They are **my reconstruction**, not statements quoted from ABI:

1. Use amplitude estimation/quantum approximate counting to obtain a constant-factor estimate of b, including a separate zero test, in tilde O(sqrt(N/max{b,1})) queries.
2. Replace ABI's unspecified pseudorandom permutations by truly random fixed permutations; computation and random-bit cost are free in query complexity. Use reversible minimum finding to implement r_s coherently. Truncate/amplify each virtual-oracle evaluation so its error is inverse-polynomial in the number of calls.
3. Amplify the recursive algorithm and union-bound sampling, coverage, counting, and nested-oracle errors to a fixed bounded error. At constant recursion depth this costs only polylogarithmic factors.
4. Cap samples and dispatch finitely many small-N cases directly. This removes irrelevant asymptotic edge cases where C N^alpha log N>N.

These completions are plausible and standard, but I have not located or written a full circuit-level composition lemma on disk. This is the principal item an independent reviewer should audit before any status promotion.

## 6. Targets and parity

The port works directly with any sigma(x)=t-x, but the on-disk translation lemma gives a clean canonical reduction. Targets t,t' are equivalent when t'-t is in 2Z_q (ksum/paper/ksum_small_alphabet.tex:164-170):

- if q is odd, 2Z_q=Z_q, so every target translates to t=0 and tau=1;
- if q is even, 2Z_q is the even residues, so even targets translate to t=0 (tau=2) and odd targets translate to t=1 (tau=0).

The two even-q classes are both covered by Step F. A coordinate translation is a fixed value relabeling and costs at most the absolute two-query simulation factor documented at ksum/paper/ksum_small_alphabet.tex:104-115. Hence parity changes constants, not the exponent.

## 7. Outcome, limitations, and pending review

**B4a outcome: CONJECTURED — pending-review.** There is no exponent obstruction from the single-list/involution twist. After fixed-point preprocessing, the ABI recursion ports and gives the candidate upper bound O_epsilon(N^{1/2+epsilon}q^{1/4}), as a fixed-depth family approaching the exponents 1/2 in N and 1/4 in q. This note does not assert a uniform little-o reformulation because it does not control depth-dependent constants.

The exact obstruction to the naive port is nevertheless real and precise: virtual compression samples residual indices with replacement; duplicating one original index creates a false pair iff its value satisfies 2x=t. Removing fixed-point-valued residual indices after checking their true multiplicities repairs it at O(sqrt(N)) cost for Z_q because tau<=2.

This note does **not** claim the same bound for arbitrary abelian groups with growing tau. Checking all fixed-point values separately would cost O(tau sqrt(N)), while treating their multiplicity problem as element distinctness can cost O(N^{2/3}); a separate argument would be needed to retain the small-range improvement there.

### WHAT I DID NOT CHECK

- No independent reviewer has audited the port, recurrence transfer, or reconstructed coherent-oracle details. This is why every new result here remains CONJECTURED — pending-review:.
- I did not run optional numerics. No script, log, numerical status, or provenance triplet is produced.
- I did not verify a circuit-level theorem for composing bounded-error minimum finding with a recursively queried virtual oracle; only query-exponent accounting and standard amplification are given.
- I did not audit ABI's original two-list handling of unequal residual sizes b,b'; the single-list port has only one residual size and avoids that issue.
- I did not claim time- or space-efficiency. The argument is solely in the quantum query model, where fixed random permutations and classical data structures are free.
- I did not access any off-disk source. A formal review still needs either an on-disk proof or a pinned external citation for constant-factor quantum approximate counting and coherent/nested minimum-finding error reduction; none was located in this pass.
