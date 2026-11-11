# Round100 synthesis proof

## Frozen row semantics

For a fixed sector, selector row `j` carries exact GF(2) vectors: a 360-bit named mask `n_j`, canonical and physical supports, canonical and physical 72-bit detector syndromes `s^c_j,s^p_j`, and 12-bit logical actions `l^c_j,l^p_j`. All vectors are regenerated from the frozen model. The order-six decision vector is

\[
v_j=(s^c_j,s^p_j)\in\mathbb F_2^{144}.
\]

It is stored in four explicitly little-endian 64-bit limbs. Unused high bits are checked zero. Equality is full `std::array<uint64_t,4>` equality; hashes and checksums never decide membership.

## Exact six-distinct MITM theorem

Every canonical six-distinct index set has one sorted representation

\[
i_0<i_1<i_2<i_3<i_4<i_5
\]

and one split `L=(i0,i1,i2)`, `U=(i3,i4,i5)` satisfying `max(L)<min(U)`. Define the triple key `K(a,b,c)=v_a xor v_b xor v_c`. In characteristic two,

\[
v_{i_0}\oplus\cdots\oplus v_{i_5}=0
\iff K(L)=K(U).
\]

The algorithm enumerates all `C(n,3)` triples, sorts by the complete key, and within each equal-key group enumerates every ordered pair with `max(L)<min(U)`. Coverage follows by mapping every syndrome-zero six-set to its unique split. Soundness follows because every emitted separated pair has six distinct sorted indices and equal keys. Uniqueness follows because a sorted six-set has only one first-three/last-three split. Small-universe controls exhaust `C(n,6)` for every `n=6..12`.

X enumerated 317,750 triples for the closed-form domain 4,690,625,500; Z enumerated 209,934 triples for 2,025,023,364. In both sectors every canonical, physical, and combined triple-key group had size one, so there were zero separated equal-key pairs and zero eligible results. The exact algorithm therefore closes the six-distinct domains without streaming 6.716 billion tuples.

The C++ table row is 152 bytes. Nominal table storage was 48,298,000 bytes (X) and 31,909,968 bytes (Z); measured peak RSS was 51,347,456 and 34,553,856 bytes. Retained science runtimes were 0.160842 and 0.074303 seconds. The independent Python replay regenerated all 234 row effects, all 545,126 triples, every histogram/checksum, the endianness controls, and every eligible stream in 6.626 seconds.

X triple checksum: `c030453f472dc14de03249734a8ea38d0b9bfbaba48441bcd1383d579b0ff978`. Z: `aa95d9754426a758eb47a8ff7e82e8debd69abcdbb6a91556b720d84c7981300`. Both combined-candidate checksums are zero.

## Stronger exact span theorem

For coefficients `x_j in F2`, the CNF constructs every named bit, both syndrome vectors, and both logical vectors by exact XOR equivalences. It asserts named weight 1..10 through an exact at-least-j recurrence, both syndromes zero, canonical logical action equal to physical logical action and nonzero, and the full 360-bit named mask different from each installed same-sector selector mask. The query therefore asks for a novel valid low-weight mask anywhere in the whole reviewed selector span.

Both CNFs are UNSAT. X DRAT `b14ece4b00c0c0ade83e8477fc2b6b97a230cb8622c928b4d5bd3d616d34ebb8`, LRAT `88cde84e0153be278136e17c5f2c733b134b20ec8b8142318da657566d4eb2b1`. Z DRAT `718512fdfc7e3c4695e0ac866f27fbfba95dad848d6c5131a1e013a2870bb58e`, LRAT `14502bc70ab7f0ced69f90ec8504ef555c3cb8a18b1f0e548576b71c7b7dfd7c`. Independent Z3 rebuilt the equations without CNF auxiliaries, checked 8 complete gate truth assignments and 544,766 cardinality recurrence cases, and returned UNSAT for coefficient domains `2^125` and `2^109`.

## Mixed-sector reduction

Let a CSS mechanism have component name sets `N_X,N_Z` and total weight `|N_X union N_Z|`. Undetected means each component syndrome is zero. If its mixed logical action is nontrivial, at least one component logical action is nontrivial. For each component,

\[
|N_S|\le |N_X\cup N_Z|\le 10.
\]

Thus any undetected nontrivial mixed mechanism in the direct bound contains an undetected nontrivial same-sector component in the same bound. Checked absence of both components would imply mixed absence; the Round100 direct queries were SAT, so this reduction supplies no global closure.
