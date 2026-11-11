# CIRCDIST.lift — literature verification of load-bearing assumptions (2026-08-20)

Produced by a background verification agent spawned by the round-1 lift recon session; committed
by the dispatcher. Resolves the recon report's UNVERIFIED flags A1/A4
(`artifacts/circdist_lift_recon_20260820.md`). Verification levels are stated per item.

## Three corrections to the recon's citation premises

1. There is NO theorem named "Net Voltage Theorem" and the word "monodromy" never appears in
   Gross-Tucker. The needed statement — a closed walk lifts closed iff its net voltage is the
   identity — is the u=v specialization of **[GT87, Thm. 2.1.2]** (net voltage on a walk; lift of
   a u->v walk of net voltage b starting at u_a ends at v_{ab}).
2. arXiv:1904.02703 (Panteleev-Kalachev, Quantum 5, 585 (2021)) introduces GENERALIZED HYPERGRAPH
   PRODUCT codes; the name and general definition of "lifted product" come from
   **arXiv:2012.04068** (Panteleev-Kalachev, IEEE TIT 2021, doi:10.1109/TIT.2021.3119384, §III-D).
3. Gross-Tucker's branched coverings (§4.2, p. 174) are of SURFACES, not graphs. For branched
   coverings of graphs the correct reference is **Baker-Norine harmonic morphisms**.

## Verified primary anchors (text actually read by the verifier)

- **[GT87]** Gross & Tucker, *Topological Graph Theory*, Wiley 1987 / Dover 2001. Chapter 2:
  ordinary voltage graph and right derived graph (§2.1.2, pp. 57-58); unique walk lifting
  (Thm 2.1.1); net voltage / terminal vertex (Thm 2.1.2); cycle preimages — k-cycle with net
  voltage of order m lifts to |Γ|/m km-cycles (Thm 2.1.3); free actions ⇔ derived graphs
  (Thm 2.2.2, the "Gross-Tucker theorem"); combinatorial covering projection = star bijections
  (§2.3.3, Warning 2.3.1: valence preservation insufficient); permutation voltage graphs (§2.4,
  Thms 2.4.1-2.4.4; Thm 2.4.5: every covering arises from a permutation voltage assignment);
  T-voltage spanning-tree normalization (§2.5.2, Thms 2.5.3/2.5.4 — voltages determined up to
  equivalence by cotree values); voltage assignments ⇔ homomorphisms π₁(G,u)→Γ (§2.5.3, both
  directions proved; the Hom(H₁(G),Γ) form for abelian Γ is the standard immediate consequence,
  NOT spelled out in GT); Betti number β(G)=1−|V|+|E| (p. 135; the dimension theorem itself is
  Diestel Thm 1.9.5, GT sets it as an exercise).
- **[BN09]** Baker & Norine, "Harmonic morphisms and hyperelliptic graphs", IMRN 2009(15)
  2914-2955, arXiv:0707.1309. Harmonic morphism definition; deg(x)=deg(φ(x))·m_φ(x)+v_φ(x);
  covering = harmonic with m=1, v=0 (Example 3.4); Riemann-Hurwitz for graphs (Thm 2.14);
  φ*: H¹(G′)→H¹(G) injective, φ_*: H¹(G)→H¹(G′) surjective (Cor 4.22). Origin of harmonic graph
  morphisms: Urakawa, Glasgow Math. J. 42(3) (2000) 319-334 (record only).
- **[Hat02]** Hatcher, *Algebraic Topology*: chain maps induce homology maps (Prop 2.9, p. 111);
  chain-homotopic maps agree on homology (Prop 2.12); path/homotopy lifting (Props 1.30, 1.34);
  transfer homomorphism for n-sheeted coverings, π_♯τ = n (§3.G).
- **[Die17]** Diestel, *Graph Theory* 5th ed., Thm 1.9.5: fundamental cycles/cuts of a spanning
  tree are bases; dim C(G) = m−n+1.
- **[BH14]** Bravyi-Hastings, arXiv:1311.0885, §II.A: homological description of CSS codes.
- **[BE21]** Breuckmann-Eberhardt, arXiv:2012.09271, IEEE TIT 67(10):6653, §II-B-2: CSS codes ⇔
  length-two chain complexes; d = min weight of a nontrivial H_i / H^i representative.
- **[TZ09/14]** Tillich-Zémor, arXiv:0903.0566, IEEE TIT 60(2):1193. Distance is Thm 15; written
  in Tanner-product, not chain-complex, language (the chain rephrasing is later literature).
- **[Gue25]** Guemard, "Lifts of quantum CSS codes", arXiv:2404.16736, IEEE TIT 71 (2025) 5418 —
  the closest prior art: voltage assignments on Tanner cone-complexes (Def 2.9 lift; Thm 3.10
  coverings of the cone-complex give CSS codes; Prop 3.13 parameters; Prop 4.1 Goursat
  classification of HPC lifts; **Remark 3.14: computing dimension/distance of a lifted code is
  open in general** — "at least as difficult as determining the 1st homology and the systole of a
  surface").
- **[SRB25]** Symons-Rajput-Browne, "Sequences of Bivariate Bicycle Codes from Covering Graphs",
  arXiv:2511.13560 (v3 Aug 2026): voltage graphs by name (citing Gross 1974, GT Dover); projection
  chain map (Thm 4.1), transfer/lift chain map (Thm 4.3), p∘τ = h·I (Lemma 4.4); k_h ≥ k
  (Thm 4.5); d ≤ d_h ≤ h·d for odd h with k_h = k (Thms 4.7/4.8); weight-preserving section
  criterion (Thm 4.9); proof of Thm 4.8 contains the projection-weight-non-increase +
  possible-triviality argument.
- **[HL26]** Hirasaki-Lee, "Lifting Lifted Product Codes", arXiv:2607.28621: group-extension
  lifts, vertex switching = voltage gauge, chain/cochain maps across families.
- **[FMS26]** Freij-Hollanti-Morris-Šapokaitė, arXiv:2606.11987: H_X/H_Z Tanner-graph isomorphism
  for LP codes. [ATB26] Aydin-Tamo-Barg, arXiv:2606.17268: survey pointers incl. Kelley-Walker
  "LDPC codes from voltage graphs" (ISIT 2008, doi:10.1109/ISIT.2008.4595095).
- **[KK10]** Kelley-Kliewer, arXiv:1006.2977: coding-theory restatement of GT Thm 2.4.3.
- **[JMOPT22]** Jeronimo et al., "Explicit Abelian Lifts and Quantum LDPC Codes",
  arXiv:2112.01647 (ITCS 2022): abelian permutation-voltage lifts (abstract-level verification).

## Partially verified (record confirmed, text not opened — re-verify before load-bearing use)

- Exoo & Jajcay, "On the girth of voltage graph lifts", Eur. J. Combin. 32 (2011) 554-562 —
  reported: girth(lift) equals shortest closed non-reversing identity-net-voltage walk in base.
- Kelley & Walker ISIT 2008; Freedman-Meyer-Luo "Z₂-systolic freedom and quantum codes" (2002);
  Bilu-Linial 2-lifts (Combinatorica 26(5) 2006); Urakawa 2000.

## NOT verified — do not cite from this report

- Any Riemannian systole-under-covering statement (Gromov/Katz/Guth numberings).
- The arXiv id of Freedman-Hastings "Building manifolds from quantum codes" (GAFA 2021,
  doi:10.1007/s00039-021-00567-3 — doi verified, arXiv id not).

## Literature-gap statement (verified by absence checks)

The lifted-product/balanced-product line (arXiv:2012.04068, arXiv:2012.09271) contains zero
occurrences of "voltage" and does not cite Gross-Tucker; only Guemard (2024/25),
Symons-Rajput-Browne (2025/26), and Hirasaki-Lee (2026) make the covering/voltage connection
explicit, and Guemard's Remark 3.14 leaves lifted-code distance open — the CIRCDIST.lift
closed-lift criterion would land in open territory.
