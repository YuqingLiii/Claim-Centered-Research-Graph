# Hostile independent audit: k-Sum final gaps

Date: 2026-07-18

Scope: only the three requested targets. Section 4 and Appendix A were treated as trusted except at their interfaces with these targets.

Severity: HIGH changes a main conclusion; MODERATE makes a stated claim false or leaves a real but locally repairable gap; LOW is an auxiliary falsehood/imprecision that does not damage the main conclusion.

## Verdicts first

### TARGET 1 - DEFECT(MODERATE, multiple exact locations)

The two-query simulation, core threshold arithmetic, and orbit parametrization are correct. A referee-level pass nevertheless fails for these exact defects.

1. **MODERATE - ksum/paper/ksum_small_alphabet.tex:36.** The abstract says the negative set “is never a single orbit for q>=3” but omits the proposition's essential hypothesis sigma != id. It is false for sigma=id: at q=N the negatives are the ED bijections and form one orbit; at q>N the injections also form one orbit (though not a regular action). Add “when sigma != id.”

2. **MODERATE - ksum_small_alphabet.tex:211.** The lower-bound constant does not scale as untruncated c^(1/6) for every c>0. That dependence arises only in the case cN<=q<N-1, asymptotically possible only for c<1. On q>=N-1 the proof caps kappa at n-1 and obtains an absolute constant. The uniform dependence is min{1,c^(1/6)} up to absolute factors.

3. **MODERATE residual overclaim - ksum_small_alphabet.tex:61 (and ambiguously line 35).** After discussing arbitrary finite abelian groups, line 61 says without restoring cyclic/target qualifiers that the tight bound holds as soon as q=Omega(N). Read for all groups, this is false: if G is elementary abelian of order q<N with q=Theta(N) and t=0, pigeonhole forces a duplicate on every length-N input, so 2-Sum is constant. The proved threshold corollary is for Z_q (all targets for odd q; t=0 for even q).

4. **LOW proof gap - ksum_small_alphabet.tex:217.** The large-q case invokes the target-zero encoding but the corollary promises every target for odd q. Invoke lem:shift before the split or in this case. This costs another absolute factor 2 and repairs the proof.

5. **LOW false oracle aside - ksum_small_alphabet.tex:115.** “Only XOR-by-a-constant” admits a one-query conjugation is false. For an invertible binary linear A and U_A|b>=|Ab>, U_A O_y U_A^(-1)=O_{Ay}; a nontrivial bit permutation is a counterexample. The two-query upper bound used by the paper remains valid; only the asserted necessity/classification fails.

6. **LOW type error - ksum_small_alphabet.tex:437.** C[D_0] is an S_N x C(sigma) module while the ED sum lambda boxtimes lambda is an S_N x S_N module. They are not directly objects of one representation category, so “not isomorphic” needs a specified identification/pullback. The correct invariant-dimension obstruction still holds: the former has trivial multiplicity at least 2, the ED pattern exactly 1.

7. **LOW wording - ksum_small_alphabet.tex:436.** “Grows with N” is false if it means strictly at every increment. With tau=0,m=2 the count p_<=2(N)=floor(N/2)+1 is 2 at both N=2 and N=3. It is nondecreasing and unbounded.

No HIGH defect was found: after these local repairs, the threshold theorem and Rosmanis obstruction survive.

### TARGET 2 - DEFECT(MODERATE, exact locations ksum/artifacts/ksum_F0_obstruction_note.md:23,81-87,95,103-105,159-161,172,175 and ksum/tools/ksum_f0_captable.py block [4])

The value-search algorithm, Tani cap, endpoint exponent, and reachability-zone algebra are correct. Two material presentation/quantifier defects remain.

1. **MODERATE - wrong cap table.** Lines 81-87 label a column “cap @ R=sqrt(n)” but print only the walk cap (k-1)/(k+1). The combined cap at theta=1/2 is min{1/2,(k-1)/(k+1)}. Thus k>=4 entries must be 1/2, not 3/5,2/3,5/7,... . The checker repeats the display bug in block [4] by printing cap_half without min(cap_half,1/2). Its assertions do not test that column, so PASS does not validate it.

2. **MODERATE quantifier defect - endpoint versus uniform donor.** Lines 23-24 define a donor as a bound valid throughout R<=rho(n)=Theta(n). Lines 93-96 prove only the local endpoint equivalence
   Omega(sqrt(n) R^c*) at R=Theta(n) iff Q_k(n,Theta(n))=Theta(n^(k/(k+1))).
   Walk optimality at the endpoint does not imply the same donor form uniformly for all smaller R. Lines 103-105, 172, and 175 use the broader word “donor” without retaining the endpoint qualifier. State the iff only for the endpoint lower bound; the uniform-family converse is unproved.

3. **LOW - line 161.** The blocked “low-q half” is not literally half. In E=log_N q coordinates its relative length is 2/5 for k=4, 5/9 for k=5, and varies with k. “Low-q sub-zone” is accurate.

The rest of Target 2 is correct conditional on the separately assumed W3E-2 embedding.

### TARGET 3 - DEFECT(LOW, exact DAG range attribution); dependency VERIFIED

Network access worked. MTZ proves the needed soft lower-bound exponent and it applies for every fixed k>=4, so the paper's crossover is safe. The exact theorem is stronger: Theorem 1.1 says, “For any constant k >= 2, the approximate degree and quantum query complexity ... is Omega-tilde(N^(3/4-1/(4k))).” It assumes range at least domain in that formulation. See the [primary arXiv paper](https://arxiv.org/pdf/2002.08389) and [abstract](https://arxiv.org/abs/2002.08389).

- ksum_small_alphabet.tex:409-412 is true: restricting a k>=2 theorem to k>=4 is valid, and k>=4 is exactly where this exponent strictly exceeds 2/3.
- ksum/artifacts/ksum_W3_donor_survey.md:31 is correct if “improves” refers to that useful regime.
- **LOW defect - ksum/notes/KSUM_PROOF_DAG.md:304.** “MTZ requires k>=4” is false. The theorem applies for fixed k>=2; k=3 gives exactly 2/3, and k=2 is weaker than the known 2/3. Say the MTZ exponent becomes an improvement/useful crossover at k>=4.
- The bibliography pin at ksum/paper/refs.bib:173-180 matches the primary source (authors, TQC 2020, DOI, arXiv ID).


## Independent derivations and checks

### 1. Oracle relabeling and query-transfer direction

Use query registers I,B and a clean ancilla A. On |i>|b>|0>:

1. Query O_y on I,A to get |i>|b>|y_i>.
2. Apply V: |i>|b>|a> -> |i>|b XOR phi_i(a)>|a>. For fixed (i,a), XOR by the fixed classical string phi_i(a) permutes the B basis, so V is unitary. It depends only on the public maps phi_i, not on input y. On non-power-of-two alphabets it can be extended arbitrarily over invalid encodings.
3. Query O_y on I,A again. Because XOR is self-inverse this returns A to |0> and leaves B as |b XOR phi_i(y_i)>.

This is coherent in superposition, has no input-dependent interleaved unitary, and leaves no garbage. Replacing every query of a T-query f algorithm gives Q(g)<=2Q(f) for g=f o phi. If each phi_i is bijective (including onto a restricted code alphabet), applying the same construction to phi^(-1) gives Q(f)<=2Q(g), hence only the claimed Theta-equivalence with absolute constants.

For a lower-bound transfer, with g the donor and f the larger problem restricted to codewords,
Q(g) <= 2 Q(f|code) <= 2 Q(f),
so Q(f)>=Q(g)/2. This validates the O(T) language at line 91 and the Omega transfers at lines 159, 169, 229, 292-293, and 582-583. No downstream use assumes one-query relabeling. The separate “only XOR-by-a-constant” aside is refuted by the linear-map example in the verdict.

### 2. Threshold corollary, case by case

Put n=floor(N/2) and work asymptotically with n>=3 and cN>=5.

**Case q>=N-1.** Choose kappa=n-1. Then 2<=kappa<n, exactly ABI's on-page range. The encoding needs q>=2kappa+1=2n-1. If N=2n, N-1=2n-1; if N=2n+1, N-1=2n. Thus q>=N-1 implies the encoding condition. The donor gives
Omega(sqrt(n)(n-1)^(1/6))=Omega(N^(2/3)).
For odd q and arbitrary t, lem:shift must additionally reduce to t=0; its factor 2 is harmless. Even q is claimed only for t=0.

**Case cN<=q<N-1.** Set kappa=floor((q-1)/2). Since q>=5, kappa>=2. Since q is integral and q<N-1, q<=N-2, hence
kappa<=floor((N-3)/2)<=2n-1,
inside Tani's stated 2<=kappa<=2n-1 range. Also q>=2kappa+1 by construction.

If q is odd, kappa=(q-1)/2 and thm:main-odd applies, including arbitrary t via translation. If q is even and t=0, |Z_q[2]|=2, so thm:main-general uses kappa'=(q-2)/2=floor((q-1)/2)=kappa. For q>=5, kappa>=q/3>=cN/3, giving
sqrt(n) kappa^(1/6) >= C c^(1/6) N^(2/3)
in this case.

The cases are disjoint and exhaustive: q=N-1 belongs to the first, and every q>=cN is either >=N-1 or below. An independent integer sweep for 6<=N<=100 found no range or encoding violation.

### 3. Orbit proposition from first principles

Decompose sigma into tau fixed points and m=(q-tau)/2 two-cycles. A negative string has exactly these constraints:

- each fixed value occurs at most once, since two copies satisfy 2a=t;
- from a two-cycle {a,sigma(a)}, at most one side occurs;
- one chosen nonfixed side may repeat arbitrarily, since 2a!=t.

Quotienting by S_N leaves a multiset. S_tau is transitive on f-subsets of fixed points, so the fixed part is just 0<=f<=min(tau,N). The wreath product can permute the m cycles and flip their sides, so the remaining invariant is the sorted list of positive cycle occupation counts: a partition lambda of N-f into at most m positive parts. Lambda is empty iff f=N. Conversely, choose the fixed points and one side of each required cycle and assign the partition multiplicities; every pair (f,lambda) is realized. With p_<=m(0)=1, the orbit count is
sum_(f=0)^(min(tau,N)) p_<=m(N-f).

Because sigma!=id, m>=1. If m>=2, (0,(N)) and (0,(N-1,1)) are distinct valid orbits for every N>=2. If m=1, q>=3 forces tau=q-2>=1, and (0,(N)) versus (1,(N-1)) are distinct. This exhausts m>=1. Only q=2,tau=0,m=1 leaves one orbit. A direct count for tau<=5,m<=4,2<=N<=10 found no counterexample.

The two N=2 witnesses also check:

- For q=3,tau=1,m=1, (a,b) with fixed a and nonfixed b is negative. A position swap cannot be matched by the centralizer because a commuting permutation preserves the fixed set.
- For m>=2, (a,a) on one side of one cycle is negative. Both identity and a flip of another cycle fix it, so uniqueness fails.

For any finite group action on X, invariant functions in C[X] are exactly the functions constant on each orbit; orbit indicators are a basis. Thus the trivial multiplicity is the orbit count, at least 2. The ED bijection bimodule has one trivial external-tensor constituent. This proves the multiplicity obstruction, with the cross-group wording repair noted above.

Finally sigma=id means t-x=x for every x. Taking x=0 gives t=0, then 2x=0 for all x, so G has exponent 2. The ED regular comparison additionally needs q=N: negatives are bijections with no unused-value stabilizer. At q>N they are injections and still one orbit, but unused values give stabilizers. Line 440's substantive comparison is correct.

### 4. Tone-down scan

The precise informal theorem at lines 77-78 and proposition at lines 433-440 retain sigma!=id and restrict the result to the Rosmanis single-orbit/regular mechanism. The abstract drops sigma!=id (line 36), and threshold prose drops the cyclic/target qualification (line 61). Those are residual overclaims. I found no body theorem purporting to rule out every possible adaptation of Rosmanis's method.


### 5. Value-search upper bound

For fixed value v and list j, testing v in im(f_j) is Grover search over n positions, O(sqrt(n)) queries at constant error. In coherent form, compute the bounded-error answer, copy its output bit, and reverse; this only changes constants. Amplify each of the constant k membership tests to error at most 1/(10k), costing O(sqrt(n) log k)=O(sqrt(n)); a union bound makes the AND predicate B_v wrong with probability at most 1/10.

Robust search over R bounded-error predicates uses O(sqrt(R)) predicate calls, for O(sqrt(Rn)) queries. Even without that theorem, amplify B_v to O(1/R) error and use ordinary amplitude amplification, obtaining O(sqrt(Rn) log R). Hence the note's conservative O-tilde(sqrt(Rn)) bound and error handling are correct.

### 6. Tani walk and donor cap

This link was verified from the primary source, not left ON-TRUST. Tani's standard-oracle Corollary 11 gives O((product_i N_i)^(1/(k+1))) for constant k when product_(i=2)^k N_i=O(N_1^k). Equal domains N_i=n satisfy n^(k-1)=O(n^k) and give O(n^(k/(k+1))). The codomain does not occur in the bound. A finding algorithm also decides existence. See [Tani, Corollary 11](https://arxiv.org/pdf/0708.2584).

Let R=n^theta, 0<theta<=1. A donor Omega(sqrt(n)R^c) has exponent 1/2+theta c. Value search gives
1/2+theta c <= (1+theta)/2, hence c<=1/2.
Tani gives
1/2+theta c <= k/(k+1),
hence c<=(k-1)/(2 theta(k+1)).
Strictly exceeding either exponent contradicts the corresponding upper bound even with polylogarithmic factors. Therefore
c<=min{1/2,(k-1)/(2 theta(k+1))}.

At theta=1 the second term is below 1/2, yielding exactly (k-1)/(2(k+1)). For k=2 this is 1/6, consistent with ABI's endpoint lower bound and the n^(2/3) walk upper bound.

### 7. Transfer corollaries and reachability

Conditionally on W3E-2, q=Theta_k(R^(k-1)) and N=Theta_k(n). With R=n^theta,
q=Theta(N^(theta(k-1))),
and a fixed exponent c transfers to k-Sum exponent 1/2+theta c. Setting this equal to k/(k+1) yields
c_req(theta)=(k-1)/(2 theta(k+1)).

For c*=(k-1)/(2(k+1)), equality requires theta=1, so this fixed dream exponent reaches the target only at q=Theta(N^(k-1)). At that endpoint its lower bound matches Tani's upper bound, proving the local walk-optimality iff.

At smaller ranges, value search requires c_req(theta)<=1/2, equivalently theta>=(k-1)/(k+1). In E=log_N q=theta(k-1) coordinates, reachability is not ruled out only when
E>=(k-1)^2/(k+1).
For every k>=4 this lower endpoint exceeds 1, so
1<=E<(k-1)^2/(k+1)
is unreachable by any donor of the stated form. The zone arithmetic is correct; “half” is not.

### 8. Checker hash and execution

Before execution:
SHA-256(ksum/tools/ksum_f0_captable.py)
= 130a06fde1f4eb5d83be407f7bb5141c90ce06f271bba40d5f034060946f2609.

This matches the note's prefix 130a06fde1f4eb5d....

The requested <machine-local-path-redacted> was unavailable to this process (direct spawn ENOENT; PowerShell also reported it unrecognized). I ran the unchanged, hash-checked script with <machine-local-path-redacted> Exit status was 0, stderr empty, and the last line was “ALL EXACT-ARITHMETIC ASSERTIONS PASSED.” This verifies the assertions actually present, not the erroneous unasserted display in block [4]. See ksum/artifacts/logs_ksum_GAP_20260718/captable_rerun.log.

### 9. MTZ pin and crossover arithmetic

The primary source proves the soft exponent 3/4-1/(4k) for every fixed k>=2 (range at least domain in Theorem 1.1). It describes this as a polynomial improvement for constants k>=4, explaining the repo wording.

MTZ crossover:
3/4-1/(4k)>2/3
iff 1/12>1/(4k)
iff k>3,
so for integral k exactly k>=4.

BKT crossover:
3/4-1/(2k)>2/3
iff 1/12>1/(2k)
iff k>6,
so exactly k>=7.

Both inequalities at ksum_small_alphabet.tex:408-411 are correct.

## Defects ranked by severity

1. **MODERATE:** false unqualified single-orbit claim (ksum_small_alphabet.tex:36).
2. **MODERATE:** unqualified all-abelian reading of the linear threshold (line 61; line 35 ambiguous).
3. **MODERATE:** incorrect untruncated c^(1/6) dependence (line 211).
4. **MODERATE:** global donor/walk-optimality iff beyond the endpoint quantifier (ksum_F0_obstruction_note.md:23,95,103-105,172,175).
5. **MODERATE:** wrong combined cap column and checker coverage hole (note lines 81-87; checker block [4]).
6. **LOW:** omitted odd-target translation in large-q threshold case (paper line 217).
7. **LOW:** false “only XOR-by-a-constant” classification (paper line 115).
8. **LOW:** ill-typed cross-group representation isomorphism (paper line 437).
9. **LOW:** DAG says MTZ requires k>=4 (KSUM_PROOF_DAG.md:304).
10. **LOW:** orbit count “grows” is not strictly true (paper line 436).
11. **LOW:** “low-q half” is not literally half (note line 161).

## WHAT I DID NOT CHECK

- I did not re-audit Section 4 or Appendix A except at interfaces with these targets, as instructed.
- I did not recompile the 18-page paper or inspect every rendered page. An attempted arXiv screenshot of the MTZ theorem page hit a cache error; I checked the primary PDF's extracted theorem text and arXiv abstract.
- I did not re-prove ABI's small-range claw lower bound, Tani 2024's range-reduction theorem, Rosmanis's adversary decomposition, or the Belovs-Spalek/Johnson-walk results. Tani 2009 and MTZ 2020 were checked from primary arXiv PDFs.
- I did not independently audit W3E-2; Target 2 transfer claims remain conditional on q=Theta_k(R^(k-1)).
- I did not verify the Hoyer-Mosca-de Wolf paper from its primary PDF. The amplified construction already proves the claimed soft-Oh value-search bound.
- I did not conduct a fresh comprehensive literature/prior-art search for absent k-partite lower bounds.
- I did not prove that no adaptation of Rosmanis's method can work; I checked only the stated orbit, stabilizer, multiplicity, and repeated-value-block obstructions.
- I could not execute with the exact WindowsApps Python named in the request because it was unavailable. I did execute the hash-identical script with another local Python and recorded both facts.
- I did not use git or run any command that modifies git state.
