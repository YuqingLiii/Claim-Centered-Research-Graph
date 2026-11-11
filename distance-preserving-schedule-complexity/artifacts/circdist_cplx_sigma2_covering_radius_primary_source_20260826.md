# CIRCDIST.cplx.sigma2 — McLoughlin covering-radius primary-source audit

**Audit target:** `CIRCDIST.cplx.sigma2@task-001-primary-source`  
**Audit date:** 2026-08-26 (America/New_York)  
**Auditor role:** fresh round-58 strict-serial source audit  
**Primary verdict:** **ACCESS-BLOCKED / NOT PRIMARY-VERIFIED**  
**Canonical consequence:** **no promotion; `assessment.level` remains `OPEN`; `task-001` must remain with a revised access caveat**

This is a public, reproducible source audit and mathematical derivation. It does not contain or purport to expose private reasoning. Every positive claim below is separated according to whether it was read in a publisher record, proved directly here, read in an official later paper, or merely reported by a secondary source.

## 1. Executive findings

| Question | Audited answer | Confidence/source status |
|---|---|---|
| Was a faithful full text of Aileen McLoughlin (1984) obtained? | **No.** IEEE's stable record and abstract were accessible, but its PDF was closed to this session. No publisher PDF, author copy, institutional copy, or issue scan was found. | Direct access audit; blocker recorded in §3. |
| Is there a McLoughlin PDF SHA-256 or theorem/page locator? | **No.** No article bytes were obtained. A zero-byte failed response is not a source and its empty-file digest must not be cited as the paper. The only primary locators read were the DOI/IEEE record and publisher abstract; theorem number, proof pages, and equation numbers are therefore **N/A**. | Direct access audit. |
| What exact decision language is supported by later official literature? | Given a binary linear code compactly represented by a parity-check matrix (H) and integer (r), decide **YES iff** (ρ(C_H) ≤ r). This upper-bound language is in (Π₂^P), and later sources attribute (Π₂^P)-hardness/completeness of its exact version to McLoughlin. | Membership is proved in §4. Hardness/completeness is strong secondary attribution, not a primary-text check. |
| What is the complement? | **YES iff** (ρ(C_H)>r), equivalently (ρ(C_H) ≥ r+1) for integral Hamming radii. Under a many-one completeness reading of the upper language, this complement is (Σ₂^P)-complete. | Direct complement argument plus secondary-reported many-one hardness. |
| Did McLoughlin study a generator matrix, a parity-check matrix, or a listed code? | The stable publisher abstract says **binary linear code**. GMR formulates the result using a **parity-check matrix**. Matsubara's row-vector formula (xA=y) becomes a parity-check syndrome equation after transposing (A). The exact orientation and rank promise in McLoughlin's own text remain unverified. It is not the explicit-list model. | Primary metadata plus official/secondary cross-check. |
| Is the result nearest-codeword/CVP? | **No.** Nearest-codeword fixes one target and has an existential witness. Covering radius universally quantifies over every target/syndrome. | Definition-level distinction, §4.8. |
| Is McLoughlin's result a gap/approximation theorem? | **No according to GMR:** McLoughlin covers linear codes and the exact version. GMR itself proves constant-factor gap hardness for linear codes. | Official GMR PDF, §6. |
| What reduction is attributed to McLoughlin? | Matsubara reports two Karp reductions, (Π₂-SAT→Π₂-3D-Matching→CRP), and says McLoughlin called the middle problem “AE 3-dimensional matching.” Schaefer–Umans also points from (∀∃)-3DM to covering radius. Their displayed predicates disagree, so the exact source-problem definition cannot be pinned without McLoughlin's text. | Conflicting secondary descriptions, §5.4. |
| Does this audit prove Eff-Preserve hardness? | **No.** It supplies no reduction from covering radius to Eff-Preserve, proves no DEEP-FLAG hardness, supplies no chain/dictionary gadget, and does not repair the Seed Barrier. | Logical scope audit, §8. |
| May `task-001` be removed? | **No.** The commission asks for primary verification, and the primary full text was not read. Revise the task to say exactly what remains and why access was blocked. | Dispatcher contract, final section. |

The most that can be stated responsibly is:

> IEEE's publisher record and several high-quality later sources strongly support the standard theorem that exact upper-bound covering radius for compactly represented binary linear codes is (Π₂^P)-complete, with the lower-bound complement (Σ₂^P)-complete. This audit did **not** inspect McLoughlin's article body, so it does not primary-verify the theorem number, matrix convention, rank/surjectivity conditions, threshold convention, or the exact reduction chain.

## 2. Canonical inputs and frozen-question provenance

The commissioned path `circdist/notes/CIRCDIST_PROBLEMS.md` does not exist in the audited checkout. Two extant frozen copies are byte-identical:

- `circdist/artifacts/definitions/CIRCDIST_PROBLEMS.md`
- `research/circdist/notes/CIRCDIST_PROBLEMS.md`

Both have SHA-256 `5f6dc37fcc33c0eb9f90e6267864740fc53b65c4acf1ee870c8d29ffd6d46c64` and 10,199 bytes; `cmp` returned 0. I used the first as the frozen question and the second as an identity check. The path discrepancy is provenance metadata, not a mathematical change.

The relevant frozen definition, at lines 135–181 of that copy, says that Eff-Preserve receives CSS check matrices (H_X,H_Z), a promised known static distance (d), an interaction/conflict graph, and optionally a depth bound (T); it asks whether there exists a schedule (M) with (d_{eff}(M)=d). When (d) is part of the input, the indicated quantifier form is

$$
  ∃ M; ∀ F, |F|<d:  F is not an undetectable logical fault.
$$

That statement motivates a (Σ₂^P) upper bound and a search for completeness. It does not contain a covering-radius reduction.

### 2.1 Exact input snapshot

| File read as data | Bytes | SHA-256 |
|---|---:|---|
| `circdist/proof-dag/nodes/CIRCDIST.cplx.sigma2.yaml` | 1,971 | `ec86fb171055f6cabb1e8f038d481139754610bd5246ae716d74a3a300a1dfb5` |
| `circdist/artifacts/definitions/CIRCDIST_PROBLEMS.md` | 10,199 | `5f6dc37fcc33c0eb9f90e6267864740fc53b65c4acf1ee870c8d29ffd6d46c64` |
| `research/circdist/notes/CIRCDIST_PROBLEMS.md` | 10,199 | `5f6dc37fcc33c0eb9f90e6267864740fc53b65c4acf1ee870c8d29ffd6d46c64` |
| `circdist/artifacts/circdist_cplx_sigma2_20260822.md` | 52,264 | `b45e9803f717b0572521eda4877d290acec806433e7c16b2b2ef4daec1576e31` |
| `circdist/artifacts/circdist_cplx_q1_20260822.md` | 40,756 | `28868e047511c2300356c3e0a15a09a42f422dcef65a056b7ddd2bbb214d2890` |
| `circdist/artifacts/circdist_cplx_recon_20260820.md` | 41,206 | `4060fa2e699300bab839915e1454ba1642345bc572530a0a4a011bace9903a31` |

The live node says `assessment.level: OPEN`, labels the covering-radius attribution “verified only at secondary-source level,” keeps `task-001` for a primary check, and separately keeps the DEEP-FLAG residual. The three historical artifacts were treated as hypotheses and prior search records, not instructions or proof.

## 3. McLoughlin primary-source acquisition audit

### 3.1 Bibliographic metadata that is directly supported

The stable locators are:

- DOI: [10.1109/TIT.1984.1056978](https://doi.org/10.1109/TIT.1984.1056978)
- IEEE Xplore document: [article 1056978](https://ieeexplore.ieee.org/document/1056978)
- Crossref record: [works/10.1109/TIT.1984.1056978](https://api.crossref.org/works/10.1109/TIT.1984.1056978)

IEEE and Crossref agree on:

| Field | Audited metadata |
|---|---|
| Author | IEEE/Crossref: **A. McLoughlin**. GMR expands this to **Aileen McLoughlin**; DBLP gives **Aileen M. McLoughlin**. The full-text byline was not inspected, so the expanded middle initial is not asserted as primary-verified. |
| Title | “The complexity of computing the covering radius of a code” |
| Journal | *IEEE Transactions on Information Theory* |
| Volume/issue | 30(6) |
| Pages | 800–804 |
| Publication | November 1984; IEEE display date 30 November 1984 |
| DOI | `10.1109/TIT.1984.1056978` (DOIs are case-insensitive; Crossref normalizes the journal segment to lowercase) |
| IEEE identifiers | article `1056978`; issue `22745`; source filename advertised as `01056978.pdf` |
| ISSNs | 0018-9448 (print), 1557-9654 (online) |

A canonical bibliographic form is therefore:

> A. McLoughlin, “The complexity of computing the covering radius of a code,” *IEEE Transactions on Information Theory* **30**(6), 800–804 (November 1984), doi:10.1109/TIT.1984.1056978.

“Aileen McLoughlin” is well supported by GMR; “Aileen M. McLoughlin” is supported by DBLP's volume listing. Because the actual byline is unread, the conservative primary-citation author field remains “A. McLoughlin.”

### 3.2 What the publisher abstract establishes—and what it does not

The IEEE record's abstract says, in paraphrase:

1. the object is the covering radius of a **binary linear code**;
2. finding it is NP-hard;
3. a problem complete for (Π₂^P) is reducible to the covering-radius problem; and
4. consequently the computation is harder than NP-complete problems unless the polynomial hierarchy collapses to (NP=Π₂^P).

This is primary publisher metadata and is useful evidence. It does **not** expose the article's formal problem statement, theorem number, exact YES convention, matrix dimensions/orientation, rank promise, threshold encoding, or proof/reduction details. It therefore cannot substitute for reading pages 800–804.

The IEEE HTML stores the complexity symbol as `<tex>\prod_{2}^{p}</tex>`. That is a legacy/OCR-style rendering of (Π₂^P), not a product operator and not a separate class.

### 3.3 Search and access record

All accesses below were on 2026-08-26. No authentication barrier was bypassed, no credential was invented, and no access-controlled copy was redistributed.

| Venue/search | How searched | Observed result | Audit use |
|---|---|---|---|
| IEEE Xplore stable record and DOI redirect | Browser and `curl -L` on the document, stamp, and advertised PDF-path URLs | Public endpoint returned anti-automation/empty HTTP 202 responses in command-line tests. The HTML metadata available through IEEE staging stated `fullTextAccess:false`, `isAccessFromInstitution:false`, `isOpenAccess:false`, `isFreeDocument:false`, and `openAccessFlag:"F"`. | Publisher metadata/abstract only; no article body. |
| Crossref | DOI API lookup | HTTP 200 JSON with metadata and a version-of-record URL whose declared use is `similarity-checking`; following it did not deliver PDF bytes. | Metadata corroboration only. |
| OpenAlex | DOI API lookup | Work `W1998732904`; `oa_status:"closed"`, `has_fulltext:false`, `any_repository_has_fulltext:false`, one location. | Negative OA check. |
| Semantic Scholar | DOI Graph API lookup | Paper ID `18313809b99b9a84417143ad3f2ea77e4bed2dfd`; `openAccessPdf.status:"CLOSED"`, empty URL. | Negative OA check. |
| Internet Archive exact-title search | Advanced Search API, exact title and title/author variants | `numFound:0`. | No article item. |
| Internet Archive journal container / scanned-issue route | Queried `pub_ieee-transactions-on-information-theory`, year/date/volume variants, metadata, files manifest, and the exact November 1984 issue | The container exists as journal metadata, but no public 1984 issue item or scan was returned; the container's files are catalog/metadata images and records, not issue pages. | No faithful issue scan. |
| Portico/ISSN preservation pointers | Checked the ISSN record and preservation links | Preservation coverage is listed, but access is authorization-controlled and no article bytes were available to this session. | Not accessible evidence. |
| Google Books/catalog routes | Queried IDs linked from serial metadata | API returned HTTP 429; no readable issue or article was obtained. | No source. |
| SciSpace | Exact-title result, direct fetch, and browser attempt | Search page advertised “PDF,” but direct access returned CloudFront 403 and the web fetch later returned 429. No bytes or provenance were obtainable. | Rejected as unverified; a label saying “PDF” is not a primary text. |
| Author/institutional repositories | Exact title, DOI, filename, and author searches targeted at Trinity/TARA and institutional domains | No exact article or author-deposited copy surfaced. | No source. |
| Broad web search | Exact title in quotes, DOI, `01056978.pdf`, volume/issue/page strings, and scanned-issue queries | Hits were IEEE metadata, citation pages, later surveys, GMR, or unrelated papers. No faithful McLoughlin text. | No source. |
| Local repository and mounted/local indices | `rg`, `find`, and `mdfind` for title, DOI, author, article number, and filename; inspected available mounted paths | Only the prior CIRCDIST artifacts and bibliographic mentions were found; no PDF or scan. | No local source. |
| Fatcat / Internet Archive Scholar | DOI/title routes | Timeout or JavaScript/session-verification barrier; no document bytes. | No source. |

Representative endpoint probe, with the observed response lines:

```text
ieee-record:   202 text/html; charset=UTF-8 0 https://ieeexplore.ieee.org/document/1056978
ieee-stamp:    202 text/html; charset=UTF-8 0 .../document/1056978/;jsessionid=...
ieee-pdf-path: 202 text/html; charset=UTF-8 0 .../document/1056978/;jsessionid=...
doi:           202 text/html; charset=UTF-8 0 https://ieeexplore.ieee.org/document/1056978/
crossref:      200 application/json 3063 ...
openalex:      200 application/json 12329 ...
semanticscholar: 200 application/json 403 ...
ia-search:     200 application/json 487 ... ; response.numFound = 0
```

The IEEE failed acquisition created a zero-byte scratch placeholder. Its SHA-256 would be the universal empty-file digest `e3b0c442...`; it is **not** the article's digest and is deliberately excluded from all source tables.

### 3.4 Primary-source verdict

**No faithful McLoughlin full text was lawfully accessible in this session.**

Accordingly:

- McLoughlin article file SHA-256: **N/A — no bytes obtained**.
- McLoughlin theorem number: **N/A — article body not read**.
- McLoughlin page/equation locators: **N/A beyond article pages 800–804 and the publisher abstract**.
- Exact McLoughlin matrix convention, independence promise, threshold encoding, named source predicate, and reduction language: **not primary-verified**.
- `task-001`: **must remain**.

## 4. The exact mathematical problem, derived from first principles

This section pins the standard problem independently of the unavailable paper. It proves membership and the complement relation; it does not prove McLoughlin's hardness construction.

### 4.1 Binary linear code and parity-check orientation

Let

$$
  H∈F_2^{s×N},
      
  C_H={c∈F_2^N: Hc^T=0}.
$$

Thus (H) has (N) columns, the code has block length (N), and codewords are written as row vectors only for notational convenience. Equivalently, with column-vector codewords one writes (Hc=0).

The Hamming distance and covering radius are

$$
 d_H(u,v)=wt(u-v),    
 ρ(C_H)=max_{v∈F_2^N}min_{c∈C_H}d_H(v,c).
$$

Over (F_2), subtraction and addition agree, but retaining the minus sign keeps the metric identity clear.

The exact upper-bound decision language is

$$
 UCR_{lin,2}
   ={(H,r): ρ(C_H) ≤ r}.
$$

Its YES direction is **small radius**: (ρ(C_H) ≤ r). This is the convention in GMR Definition 2.5 and Schaefer–Umans entry CC1.

### 4.2 Coset-leader/syndrome identity

Fix an ambient vector (v), and let (y=Hv^T). For every codeword (c∈C_H), set (e=v-c). Then

$$
 He^T=H(v-c)^T=Hv^T-Hc^T=y
$$

and

$$
 wt(e)=d_H(v,c).
$$

Conversely, if (e∈F_2^N) satisfies (He^T=y=Hv^T), then (c=v-e) satisfies (Hc^T=0), hence (c∈C_H), and again (wt(e)=d_H(v,c)). Therefore

$$
 min_{c∈C_H}d_H(v,c)
 =
 min{wt(e):He^T=Hv^T}.
     (1)
$$

This is the complete proof of the syndrome characterization; no citation is needed for it.

### 4.3 Quantifier forms and membership

Without any rank promise, substitute the definition directly:

$$
 ρ(C_H) ≤ r
 ⇔
 ∀ v∈F_2^N ∃ c∈F_2^N:
 (Hc^T=0) ∧
 (wt(v-c) ≤ r).
     (2)
$$

The matrix multiplication, zero test, subtraction, and weight comparison are polynomial-time predicates in the explicit input size. Equation (2) proves

$$
 UCR_{lin,2} ∈ Π₂^P.
$$

If (H) has full row rank (s), its syndrome map is onto (F_2^s), and (1) gives the more compact form

$$
 ρ(C_H) ≤ r
 ⇔
 ∀ y∈F_2^s ∃ e∈F_2^N:
 (He^T=y) ∧
 (wt(e) ≤ r).
     (3)
$$

GMR Lemma 5.1 states this characterization for an ([N,k]) code and a full-rank ((N-k)×N) parity-check matrix over a field.

### 4.4 Rank and surjectivity are not cosmetic

If (H) is rank-deficient and (3) nevertheless quantifies over every (y∈F_2^s), any unreachable syndrome makes the formula false regardless of the actual covering radius. The correct alternatives are:

1. use the ambient-vector form (2), which needs no rank promise;
2. quantify (y) only over (im(H)); or
3. delete dependent parity checks by Gaussian elimination, obtaining a full-row-rank (H') with (ker H'=ker H).

Thus a literal “for every syndrome in (F_2^s)” statement requires surjectivity/full row rank. GMR's standard ([N,k]) parity-check convention has rank (N-k). Schaefer–Umans calls (H) a parity-check matrix but does not state a rank promise in the short catalog entry. The unavailable McLoughlin text is required to determine which convention it formalizes.

### 4.5 Matsubara's transposed orientation

Matsubara, PDF page 4, reports the McLoughlin problem as follows: (A) is an (m×n) binary matrix, (w) an integer, and the question is whether

$$
 ∀ y∈F_2^n ∃ x∈F_2^m:
   xA=y and  wt(x) ≤ w.
     (4)
$$

Set (H=A^T∈F_2^{n×m}), and transpose row vectors. Formula (4) is exactly (3) for the length-(m) code (ker H), provided (A) has full column rank (n) (equivalently (H) has full row rank (n)). If no such promise is imposed, rank-deficient instances of (4) are automatically NO, while the standard code (ker H) still has a finite covering radius. That is one of the primary-text details still open.

This matrix (A) must not be mislabeled a generator matrix merely because it appears in (xA). In (4), its transpose is the syndrome/parity-check map. GMR's generator convention is different: an (N×k), rank-(k) matrix (G) represents the code ({Gz:z∈F_q^k}).

### 4.6 Complement and the one-unit threshold shift

The complement language is

$$
 LCR_{lin,2}
   ={(H,r):ρ(C_H)>r}.
$$

From (2),

$$
 ρ(C_H)>r
 ⇔
 ∃ v∈F_2^N ∀ c∈F_2^N:
 (Hc^T ≠ 0) ∨
 (wt(v-c)>r).
     (5)
$$

For full-row-rank (H), this becomes

$$
 ∃ y∈F_2^s ∀ e∈F_2^N:
 (He^T ≠ y) ∨
 (wt(e)>r).
     (6)
$$

Equations (5)–(6) show membership in (Σ₂^P). Since Hamming covering radii are integers,

$$
 ρ(C_H)>r ⇔ ρ(C_H) ≥ r+1.
$$

Therefore, if the upper language is (Π₂^P)-complete under polynomial-time many-one reductions, its complement is (Σ₂^P)-complete under the same reduction type. The identical instance map proves the complement reduction after complementing both source and target languages.

A statement using “(ρ ≥ r)” is shifted by one from the complement of “(ρ ≤ r).” This off-by-one must be written explicitly in any transfer.

### 4.7 Threshold encoding

The input contains an integer threshold (r). Binary versus unary encoding does not alter this classification:

- if (r<0), the upper-bound instance is trivially NO;
- if (r ≥ N), it is trivially YES because (0∈C_H) and every length-(N) word has weight at most (N);
- otherwise (0 ≤ r ≤ N), so a unary encoding has length (O(N)), already polynomial in the explicit matrix input.

Thus binary and unary threshold forms are polynomial-time interconvertible after trivial normalization. The exact notation used in McLoughlin is still primary-unread, but it cannot create the claimed hierarchy gap.

### 4.8 Problems this is not

| Problem | Quantifiers/input | Why it is different |
|---|---|---|
| Nearest codeword / Hamming CVP | Input includes one target (v); asks (∃ c∈C) with (d_H(v,c) ≤ r). | One target and an existential witness, rather than all targets. |
| Syndrome decoding | Input includes one syndrome (y); asks (∃ e), (He^T=y), (wt(e) ≤ r). | One syndrome; it is the inner existential subproblem of (3). |
| Explicit-list covering radius | (C⊆{0,1}^N) is listed word by word. | A far vector can be checked against every listed word in polynomial time in the list size. |
| Radius / closest-string | Seeks a center whose ball contains every listed codeword. | Minimax center problem, not maximum distance from the code to ambient space. |
| Gap covering radius | Promise separates (ρ ≤ d) from (ρ>γ d), (γ>1). | Approximation promise absent from McLoughlin's exact result as described by GMR. |
| Lattice covering radius | Infinite lattice under Euclidean norm. | GMR treats it separately and says exact lattice complexity remained open in that work. |

## 5. Hardness, completeness, function computation, and reduction chain

### 5.1 Evidence ladder

| Claim | Directly audited evidence | Status |
|---|---|---|
| Binary linear-code subject | IEEE publisher abstract | **Primary metadata verified** |
| A (Π₂^P)-complete problem reduces to covering radius | IEEE publisher abstract | **Primary abstract verified**, but target decision convention and reduction type are not exposed |
| Upper-bound exact CRP is in (Π₂^P) | Equations (2)–(3) above; GMR Definition 2.5 | **Proved directly** |
| Exact linear-code CRP upper language is (Π₂^P)-hard/complete | GMR PDF pages 3, 9, and 20; Matsubara PDF page 4; Schaefer–Umans CC1 on PDF page 24; contemporaneous Cohen et al. survey journal p. 339 | **Strong official/peer-reviewed secondary agreement; not primary-verified** |
| Hardness is under Karp/many-one reductions | Matsubara explicitly says McLoughlin used two Karp reductions; Schaefer–Umans lists the reduction | **Secondary-reported; exact primary wording unread** |
| Source chain is (Π₂-SAT→Π₂-3D-Matching→CRP) | Matsubara PDF p. 4 | **Secondary-reported** |
| Middle problem is named “AE 3-dimensional matching” | Matsubara PDF p. 6 | **Secondary-reported** |
| Exact predicate of AE 3DM | Matsubara p. 6 and Schaefer–Umans SP5 disagree | **Unresolved without primary** |
| McLoughlin proves a formal exact-function completeness theorem | No accessible primary text; GMR says “computing the exact solution … (Π₂^P)-hard,” while later catalogs formulate a decision problem | **Not established** |
| McLoughlin proves a gap/approximation theorem | GMR explicitly says the prior result is exact only | **Rejected** |
| McLoughlin proves arbitrary-(q) hardness | Publisher says binary; arbitrary prime-power (q) belongs to GMR's new gap theorem | **Rejected as an attribution** |

### 5.2 Hardness versus completeness

The publisher abstract alone supports hardness: a (Π₂^P)-complete problem reduces to covering radius. It does not, in the accessible text, state the target language or membership.

Once the target is fixed as (UCR_{lin,2}), membership follows from (2), and (Π₂^P)-hardness plus membership yields (Π₂^P)-completeness. This is also how later literature describes the theorem. The safe attribution is therefore:

> Later official and peer-reviewed sources attribute to McLoughlin the (Π₂^P)-completeness of exact upper-bound covering radius for compactly represented binary linear codes.

The unsafe wording is:

> “This audit read McLoughlin's theorem and confirmed every hypothesis and reduction detail.”

It did not.

### 5.3 Decision hardness versus exact-function hardness

Define the function

$$
 f(H)=ρ(C_H)∈{0,…,N}.
$$

An oracle that computes (f(H)) exactly decides ((H,r)∈UCR_{lin,2}) by comparing (f(H) ≤ r). Therefore the decision language reduces to the exact function by a polynomial-time oracle/metric reduction. Conversely, (f(H)) can be computed with (O(log N)) adaptive queries to the upper-bound decision language by binary search. Hence a safe modern placement is

$$
 f∈FP^{Π₂^P[log]}⊆ FP^{Π₂^P},
$$

with decision hardness inherited in the oracle sense.

That elementary relationship does **not** show that McLoughlin stated or proved completeness for a named function class. “Karp reduction” is a language-to-language notion here; it should not be casually attached to the integer-valued function without defining a function reduction. The primary body is needed to decide whether its “computing” language is formal function hardness or an informal reference to the threshold problem.

### 5.4 Named source problem and the secondary conflict

Matsubara's PDF page 4 says McLoughlin used two Karp reductions:

$$
 Π₂-SAT
 →
 Π₂-3D-Matching
 →
 CoveringRadius.
$$

On PDF page 6, Matsubara says McLoughlin called the middle problem “AE 3-dimensional matching.” Matsubara's displayed question asks, for every (μ_1⊆ M_1), whether there exists (μ_2⊆ M_2) such that (μ_1∪μ_2) is **not** a matching.

Schaefer–Umans entry SP5, PDF page 17, defines (∀∃) THREE DIMENSIONAL MATCHING using three equal disjoint ground sets and disjoint (M_1,M_2). After defining “a matching” to cover every ground element, its question asks whether every (S_1⊆ M_1) has an (S_2⊆ M_2) such that (S_1∪S_2) **is** a matching. Entry CC1, PDF page 24, says this problem reduces to covering radius and cites McLoughlin.

The “is” versus “is not” discrepancy is present in the rendered PDFs; it is not an extraction artifact. At least one short secondary description is erroneous or uses a transformed convention not explained in the entry. The audit therefore records only the broad chain as secondary-reported and refuses to choose an exact AE-3DM predicate without pages 800–804.

## 6. Separate official GMR cross-check

### 6.1 Source identity and integrity

Official author-hosted journal-version PDF:

- Venkatesan Guruswami, Daniele Micciancio, and Oded Regev, “The Complexity of the Covering Radius Problem,” *Computational Complexity* **14**(2), 90–121 (2005).
- DOI: [10.1007/s00037-005-0193-y](https://doi.org/10.1007/s00037-005-0193-y)
- Author-hosted PDF: [cims.nyu.edu/~regev/papers/crp.pdf](https://cims.nyu.edu/~regev/papers/crp.pdf)
- Downloaded bytes: 354,880
- SHA-256: `834752fc97065da1ed0b8e67cdeccdb92d7ab450ea27b4872bcc4949f7423fa3`
- PDF length: 33 pages
- PDF metadata: AFPL Ghostscript 8.10; creation/modification date 2006-09-06; unencrypted
- Visual verification: rendered and inspected PDF pages 3, 9, 19, and 20; symbols and inequality directions agree with text extraction.

Crossref confirms the journal metadata above. The preliminary CCC 2004 version has the longer title “The Complexity of the Covering Radius Problem on Lattices and Codes”; the audited PDF is the later journal version.

### 6.2 What GMR attributes to McLoughlin

GMR does all of the following:

1. **PDF page 3, introduction:** defines covering-radius decision conceptually as deciding whether every ambient point has a code/lattice point within distance at most (r); observes the (∀∃) form and (Π₂^P) membership; then says that for linear codes McLoughlin showed the exact problem (Π₂^P)-hard, giving a natural complete problem for (Π₂^P).
2. **PDF page 3:** limits the prior McLoughlin result to **linear codes** and the **exact version**.
3. **PDF page 9, Definition 2.5:** defines (GapCRP^{codes}_γ) on ((H,d)), with (H) a parity-check matrix, YES when (ρ(H) ≤ d), and NO when (ρ(H)>γ(N)d). Setting (γ=1) gives the exact upper-bound convention.
4. **PDF page 9, previous work:** again attributes exact (Π₂^P)-hardness for linear codes to McLoughlin.
5. **PDF page 20, §5.3:** calls linear CRP a complete problem for (Π₂^P), attributes the hardness to McLoughlin, and contrasts it with Frances–Litman's explicit-list result.

GMR does **not** reproduce McLoughlin's proof, identify McLoughlin's theorem number, state the AE-3DM predicate, or pin McLoughlin's own matrix orientation/rank promise. It is authoritative corroboration, not a substitute primary text.

### 6.3 What GMR itself proves

GMR's new coding result is **Theorem 5.5**, PDF page 20:

- there exists a constant (c>1);
- for every prime power (q);
- the promise problem (GapCRP^{codes}_c) on (q)-ary linear codes is (Π₂^P)-complete.

The proof first treats binary codes and then adapts the construction to arbitrary prime-power alphabets. Its source is GMR's own bounded-occurrence gap quantified satisfiability problem, written (Gap_{∀∃})-3-SAT-(B_g), not McLoughlin's reported exact Π₂-SAT/AE-3DM chain.

Other exact locators:

- PDF page 8: an (N×k), rank-(k) generator matrix versus an ((N-k)×N) parity-check matrix.
- PDF page 19, Lemma 5.1: syndrome characterization of radius and full rank.
- PDF page 20, footnote 4: compact matrix representation may encode exponentially many codewords, unlike an explicit list.
- PDF page 25, post-Theorem-5.5 remark: discusses (Π₂^P)-hardness under **Karp reductions** for larger approximation factors and the resulting PH consequence.
- PDF page 32: bibliography entry for Aileen McLoughlin, title, journal, volume, and pages; issue/DOI omitted.

It is therefore wrong to say “McLoughlin proved GMR Theorem 5.5,” or to attribute arbitrary-(q) constant-gap hardness to McLoughlin.

## 7. Frances–Litman apparent conflict resolved

### 7.1 Official metadata and abstract

Springer's publisher page identifies:

- Moti Frances and Ami Litman, “On Covering Problems of Codes,” *Theory of Computing Systems* **30**(2), 113–119 (1997);
- DOI [10.1007/BF02679443](https://doi.org/10.1007/BF02679443) (Springer also routes a newer-style DOI alias);
- an arbitrary binary code defined as a subset (C⊆{0,1}^N);
- an NP-complete “decision problem associated with” covering radius;
- a proof route through Radius, with 3SAT reduced to Radius and a known computational equivalence between Radius and Covering Radius.

The official Springer HTML snapshot used in the audit was 249,359 bytes with SHA-256 `4c6cce0299c97fe98d32ee965903345de6cd659a42eb9fbc9c2e6745cbf841b6`. The full paper PDF was not open in this session, so the publisher abstract is not used to infer an unstated threshold direction. GMR PDF page 20 explicitly says that when a general code is given as a **list of codewords**, the exact covering-radius problem was shown **coNP-complete** by Frances–Litman.

### 7.2 Why there is no contradiction

Suppose the codewords are listed explicitly. Then a YES witness for

$$
 ρ(C)>r
$$

is a single vector (v∈{0,1}^N) whose distance from every listed codeword exceeds (r). Checking all those distances is polynomial in the explicit list size. Thus the lower-bound/far-vector language is in NP, while its complement (ρ(C) ≤ r) is in coNP. Depending on which side is called “the decision problem,” NP-complete and coNP-complete descriptions refer to complementary languages (with the integral one-unit shift when (≥) is used).

For a compact parity-check matrix, the code may contain exponentially many codewords relative to the matrix size. A proposed far vector cannot be checked merely by scanning the input, and the upper language naturally has the (∀∃) form (2). GMR footnote 4 explicitly warns that the two representations have exponentially different sizes.

The Frances–Litman result therefore concerns:

- arbitrary binary codes;
- an explicit-list input model;
- Radius plus a computational transfer to Covering Radius;
- complementary decision-direction terminology in different summaries.

It does not contradict McLoughlin's compact binary **linear** code result. It also does not turn McLoughlin's problem into nearest-codeword/CVP or an approximation problem.

## 8. Exact consequence for `CIRCDIST.cplx.sigma2`

The covering-radius fact supplies, at most, a candidate (Π₂^P)-complete source language and a (Σ₂^P)-complete complementary source language. A hardness proof for Eff-Preserve still requires a polynomial-time mapping that preserves YES/NO answers and all promises.

This source audit proves none of the following:

1. a reduction from (ρ(C)>r) or (ρ(C) ≤ r) to Eff-Preserve;
2. a construction of legal CSS check matrices, schedules, conflict graphs, and promised static distance;
3. the DEEP-FLAG chain/dictionary residual;
4. the existence of a full deep-hole ladder rather than a single deep point;
5. a repair of the repetition-padding route rejected by the recorded Seed Barrier;
6. any wrapper lemma needed to transfer a classical code instance into the exact Eff-Preserve semantics;
7. (Σ₂^P)-hardness, completeness, or a level promotion for the current node.

The previous artifacts' DEEP-FLAG and Seed Barrier conclusions are unchanged. The current claim remains **OPEN** and on stop-loss. This audit only sharpens the external-source ledger.

### 8.1 Can `task-001` be removed?

**No.** Its literal acceptance condition is primary-source verification. The full primary text was not read. The task should remain but be made more precise: publisher metadata and later official sources strongly corroborate the standard result, while exact hypotheses and the reported source chain remain primary-unverified because access was blocked.

## 9. Reproducible command and source record

These commands are representative of the actual foreground-only audit. They may be rerun from the repository root. HTTP responses can change; the observations recorded here are dated 2026-08-26.

### 9.1 Canonical input checks

```sh
test -e circdist/notes/CIRCDIST_PROBLEMS.md
# exit 1

cmp -s   circdist/artifacts/definitions/CIRCDIST_PROBLEMS.md   research/circdist/notes/CIRCDIST_PROBLEMS.md
# exit 0

shasum -a 256   circdist/proof-dag/nodes/CIRCDIST.cplx.sigma2.yaml   circdist/artifacts/definitions/CIRCDIST_PROBLEMS.md   research/circdist/notes/CIRCDIST_PROBLEMS.md   circdist/artifacts/circdist_cplx_sigma2_20260822.md   circdist/artifacts/circdist_cplx_q1_20260822.md   circdist/artifacts/circdist_cplx_recon_20260820.md
```

### 9.2 Publisher/OA/archive probes

```sh
curl -L --max-time 25 -A 'Mozilla/5.0 source-audit/2026-08-26'   -sS -o /dev/null   -w '%{http_code} %{content_type} %{size_download} %{url_effective}\n'   'https://ieeexplore.ieee.org/document/1056978'

curl -L --max-time 25 -A 'Mozilla/5.0 source-audit/2026-08-26'   -sS -o /dev/null   -w '%{http_code} %{content_type} %{size_download} %{url_effective}\n'   'https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=1056978'

curl -L --max-time 25 -A 'Mozilla/5.0 source-audit/2026-08-26'   -sS -o /dev/null   -w '%{http_code} %{content_type} %{size_download} %{url_effective}\n'   'https://ieeexplore.ieee.org/iel5/18/22745/01056978.pdf'

curl -L -sS   'https://api.crossref.org/works/10.1109/TIT.1984.1056978'

curl -L -sS   'https://api.openalex.org/works/https://doi.org/10.1109/TIT.1984.1056978'

curl -L -sS   'https://api.semanticscholar.org/graph/v1/paper/DOI:10.1109/TIT.1984.1056978?fields=title,authors,year,openAccessPdf,externalIds'

curl -L -sS   'https://archive.org/advancedsearch.php?q=%22The%20complexity%20of%20computing%20the%20covering%20radius%20of%20a%20code%22&fl%5B%5D=identifier,title&rows=20&page=1&output=json'
```

### 9.3 Official/later source acquisition and integrity

```sh
curl -L --fail -o gmr-crp.pdf   'https://cims.nyu.edu/~regev/papers/crp.pdf'

curl -L --fail -o matsubara-1602.05657.pdf   'https://arxiv.org/pdf/1602.05657'

curl -L --fail -o schaefer-umans-phcom.pdf   'https://ovid.cs.depaul.edu/documents/phcom.pdf'

curl -L --fail -o cohen-covering-radius-survey-1985.pdf   'https://sites.bu.edu/mark/files/2018/02/78-covering-radius.pdf'

shasum -a 256   gmr-crp.pdf   matsubara-1602.05657.pdf   schaefer-umans-phcom.pdf   cohen-covering-radius-survey-1985.pdf

pdfinfo gmr-crp.pdf
pdftotext -layout gmr-crp.pdf gmr-crp.txt
pdftoppm -f 3 -l 3 -r 180 -png -singlefile gmr-crp.pdf gmr-p03
pdftoppm -f 9 -l 9 -r 180 -png -singlefile gmr-crp.pdf gmr-p09
pdftoppm -f 19 -l 20 -r 180 -png gmr-crp.pdf gmr-p19-20
```

Observed source digests:

| Source file | Bytes | SHA-256 | Key locator |
|---|---:|---|---|
| GMR official author PDF | 354,880 | `834752fc97065da1ed0b8e67cdeccdb92d7ab450ea27b4872bcc4949f7423fa3` | PDF pp. 3, 8–9, 19–20, 25, 32; Definition 2.5, Lemma 5.1, Theorem 5.5, footnote 4 |
| Matsubara arXiv PDF | 451,384 | `460dc39e4d0fc4f0975c1c673bb5407167ae5e42b26437c29d0dd02fa7ec9675` | PDF pp. 4 and 6 |
| Schaefer–Umans compendium PDF | 291,921 | `8ecc9ad1329313f73b01c83d04dae815b8af8794e60b4a4f766f7e29eb0290df` | PDF p. 17 (SP5), p. 24 (CC1), p. 33 (ref. 55) |
| Cohen–Karpovsky–Mattson–Schatz 1985 survey | 1,948,913 | `233685f548bd3d5bf2740bcf28710050862262c6dc21d87930f650d02f821070` | Journal p. 339 / PDF p. 12, “Complexity” paragraph |
| Springer Frances–Litman HTML | 249,359 | `4c6cce0299c97fe98d32ee965903345de6cd659a42eb9fbc9c2e6745cbf841b6` | Publisher abstract and citation meta tags |

The Cohen et al. survey is a contemporaneous peer-reviewed secondary source: journal p. 339 says McLoughlin showed finding covering radius NP-hard and (Π₂^P)-hard, defining the latter as reduction from a (Π₂^P)-complete problem. It does not provide the missing formal hypotheses or proof.

### 9.4 Disposable structural checks and FIX-2 accounting

The final artifact was checked with foreground commands for:

- existence and nonzero size;
- required section labels and all six commissioned pin groups;
- absence of a claim that the McLoughlin PDF was obtained;
- presence of the exact (ρ ≤ r), (ρ>r), rank, Karp, Frances–Litman, GMR, DEEP-FLAG, no-promotion, and dispatcher-contract language;
- validity of all referenced repository paths except the explicitly documented missing commissioned note path;
- final byte count and SHA-256;
- task-specific scratch deletion;
- absence of surviving task-related `curl`, PDF renderer, Python, or audit processes.

FIX-2 accounting:

- **Durable writes:** exactly one, this artifact:
  `circdist/artifacts/circdist_cplx_sigma2_covering_radius_primary_source_20260826.md`.
- **Canonical mutations:** none.
- **Node/route/scheduler/protocol/generated-view/earlier-evidence mutations:** none.
- **Sub-agents:** none.
- **Detached/background processes:** none.
- **Scratch:** only `/tmp/cplx_sigma2_primary_source_audit_20260826_58a`; it held downloaded PDFs, extracted text, HTTP-response snapshots, and page renders, and was deleted recursively after finalization.
- **Surviving task process:** none after cleanup.
- **Artifact self-hash note:** a file cannot contain its own SHA-256 without changing that SHA-256. The final digest is therefore reported out of band to the dispatcher.

## 10. Dispatcher installation contract

Apply the following to `circdist/proof-dag/nodes/CIRCDIST.cplx.sigma2.yaml` only after normal dispatcher review. Do not edit any claim text, route, scheduler, protocol, historical artifact, or generated view as part of this source-audit installation.

### 10.1 Exact evidence entry to append under `assessment.basis.evidence`

```yaml
- path: circdist/artifacts/circdist_cplx_sigma2_covering_radius_primary_source_20260826.md
  kind: text
  note: Round-58 source audit. IEEE publisher metadata and official/peer-reviewed later sources strongly support exact upper-bound binary linear-code covering radius as Π₂^P-complete, but no faithful McLoughlin full text was lawfully accessible on 2026-08-26; exact theorem hypotheses and reduction details remain primary-unverified.
```

### 10.2 Exact replacement `assessment.summary`

```yaml
summary: The hierarchy-hardness claim remains OPEN and on stop-loss. The Q1 repetition-padding gate was answered negatively by the recorded Seed Barrier argument; repeating that gate is not current work. The unresolved DEEP-FLAG dictionary and alternative constructions remain unproved. Exact upper-bound binary linear-code covering-radius completeness is strongly supported by IEEE publisher metadata and official/peer-reviewed later sources, but McLoughlin's full primary text was not lawfully accessible on 2026-08-26, so its exact theorem hypotheses and reduction details remain primary-unverified.
```

### 10.3 Exact replacement for `frontier.task-001`

Keep the key and original `since` date:

```yaml
task-001:
  task: Obtain and inspect a faithful McLoughlin (1984) primary text, then verify the exact upper-bound decision statement and YES direction, binary matrix orientation and dimensions, rank/surjectivity promise, threshold convention, reduction type, and Π₂-SAT/AE-3DM source chain. Current evidence is publisher metadata plus official/peer-reviewed secondary agreement only; do not cite it as a primary-text verification.
  kind: task
  since: '2026-08-20'
```

Do **not** remove `task-001`. Leave `deep-flag-residual` unchanged.

### 10.4 Exact event to append

```yaml
covering-radius-primary-source-audit-access-blocked-2026-08-26:
  date: '2026-08-26'
  type: repair-applied
  summary: Round-58 strict-serial source audit located the stable IEEE DOI record and publisher abstract and cross-checked an official GMR journal PDF plus later sources. The evidence strongly supports the standard exact upper-bound binary linear-code covering-radius Π₂^P-completeness attribution, with Σ₂^P-complete lower-bound complement, but no faithful McLoughlin full text was lawfully accessible. Exact theorem hypotheses and the reported Π₂-SAT/AE-3DM Karp chain remain primary-unverified; task-001 is retained. This source audit proves no Eff-Preserve reduction, no DEEP-FLAG result, and no level change.
  sources:
  - path: circdist/artifacts/circdist_cplx_sigma2_covering_radius_primary_source_20260826.md
    kind: text
    locator: Primary-source verdict; exact derivation; GMR cross-check; dispatcher installation contract
```

### 10.5 Assessment level and no-overclaim constraints

- **Assessment level change:** none; retain `OPEN`.
- Append **no** `level-change` event.
- Do not say that McLoughlin's PDF or article body was read.
- Do not attach a McLoughlin PDF SHA-256, theorem number, page locator, rank promise, or exact AE-3DM predicate until a faithful copy is actually inspected.
- Do not attribute GMR Theorem 5.5, arbitrary-(q) hardness, or constant-gap hardness to McLoughlin.
- Do not conflate (ρ ≤ r) with its complement; write the complement as (ρ>r), equivalently (ρ ≥ r+1).
- Do not conflate parity-check/syndrome representation with a generator matrix, or compact linear-code input with an explicit codeword list.
- Do not claim a formal exact-function completeness class from the decision result without naming and proving the function reduction.
- Do not infer Eff-Preserve hardness, DEEP-FLAG hardness, a covering-radius-to-schedule dictionary, or any node promotion from this citation audit.
