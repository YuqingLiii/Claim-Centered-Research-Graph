# CIRCDIST.lift — literature verification, part 2: systoles/girth under covers (2026-08-20)

Second background verification sweep (spawned by the round-1 lift recon; committed by the
dispatcher). Companion to `artifacts/circdist_lift_litverify_20260820.md`.

## Mathematical warning that bears on the lift framework

- **Homotopy systole IS monotone under covers** (pullback metric): sys_pi(cover) >= sys_pi(base);
  two-line proof from Hatcher Prop 1.31 (p_* injective on pi_1). VERIFIED. No numbered statement
  exists in Gromov 1996 / Guth arXiv:1003.4247; Katz 2007 unverified — cite the argument, not a
  numbering.
- **Homology systole is NOT monotone under covers.** Explicit checkable counterexample (verifier's
  own construction, elementary): genus-2 surface with a short separating neck; a Z/2 cover makes
  the neck's lifts non-separating, so sys_H drops from >= L to <= epsilon. Mechanism: p_* is
  injective on pi_1 but NOT on H_1; the transfer identity pi_* tau_* = n (Hatcher §3.G, pp.
  321-322, unnumbered text; Prop 3G.1 is the field-coefficient statement) bounds ker(pi^*) and
  never gives injectivity of pushforward.
- **Consequence for CIRCDIST.lift:** "distance can only go up under lifts" is FALSE in general for
  the same reason (a lifted codeword with epsilon(x) = 0 escapes the base-distance bound — exactly
  ker(p_*) on H_1); consistent with Guemard Remark 3.14 and with the SRB Thm 4.8 projection
  argument (weight non-increase + possible triviality). The iff criterion's premise "full
  spacetime logicals project to effective logicals" must be stated at the right level
  (nontriviality can die under projection) — the graph-like case survives because there
  sys_H = sys_pi = girth.
- **Graph girth IS monotone under lifts** (folklore; mechanism verified in Bocharova et al.
  arXiv:1108.0840 §IV: cycles of the lift = zero-voltage cycles of the base; Even-Halabi
  arXiv:1302.3518 Prop 10/Cor 11; Hoory arXiv:2401.01238; Exoo-Jajcay girth-of-lifts theorem via
  Dynamic Cage Survey DS16 Thm 21 — the 2011 paper itself remains paywalled/unread).

## Citation corrections (verified by fetching full texts)

- Freedman-Hastings arXiv:2012.02249 (GAFA 2021): their "lifting" means lifting an F2 complex to
  Z, NOT covering spaces; no distance-under-covering statement. Do not cite for that. (arXiv id
  now pinned, resolving the part-1 flag.)
- Hastings-Haah-O'Donnell arXiv:2009.03921: fiber bundle != covering; not a source on distance
  under covers.
- Bilu-Linial (Combinatorica 2006): contains NO girth-vs-lift statement — do not cite for girth.
- Symons-Rajput-Browne arXiv:2511.13560: the words "systole" and "girth" do not appear — do not
  cite it for systolic statements.
- Weibel: "chain map induces H_n map" is EXERCISE 1.1.2; chain-homotopy invariance is Lemma 1.4.5
  (p. 17). Cite Hatcher Prop 2.9/2.12 for theorem-grade statements.
- The canonical "distance from systoles of covers" line is Guth-Lubotzky arXiv:1310.5555 (JMP
  2014) + Murillo arXiv:1610.03870 (§8: congruence-cover systole growth => d >= c1 n^0.2).

## Verification levels

Fetched and read: Hatcher (Props 1.31, 2.9, 2.12, Thm 2.10, §3.G), Gromov 1996, Guth 1003.4247,
Bocharova 1108.0840, Even-Halabi 1302.3518, Hoory 2401.01238, Bilu-Linial published PDF,
Freedman-Hastings 2012.02249, HHO 2009.03921, Guemard 2404.16736, Murillo 1610.03870, SRB
2511.13560, Weibel (Cambridge Core scan), DS16 survey. Abstract-level: Guth-Lubotzky, Guemard
2505.14327, Jeronimo et al., PK 2012.04068, BE 2012.09271. UNVERIFIED: Katz 2007 numbering;
Kelley-Walker ISIT 2008 content; Exoo-Jajcay 2011 internal numbering; Freedman-Meyer-Luo full
bibliographic data; Brown GTM 87 III.9 proposition numbers; the genus-2 counterexample against
independent literature.
