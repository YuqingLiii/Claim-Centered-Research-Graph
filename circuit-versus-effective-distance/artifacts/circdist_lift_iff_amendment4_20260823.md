# Amendment 4 to `circdist_lift_iff_proof_20260820.md` — Lemma B's constancy chain, and R9's loose end

**Node(s):** `CIRCDIST.lift.iff`, `CIRCDIST.lift`
**Author:** Opus 5, amendment-author session, wave 24, 2026-08-23
**Kind:** append-only proposer amendment. Repairs **Amendment 3**, not the base mathematics.
**Status of every statement below:** `CONJECTURED` with an explicit derivation-status line, or
`NUMERICAL` with the code inline (§5). **This amendment assigns no level and licenses no promotion.**

---

## 0. Scope, hash chain, and epistemic status

**The commission.** The wave-23 focused re-review of Amendment 3
(`artifacts/circdist_iff_amendment3_review_20260823.md`) returned **CONFIRM** on Lemma A, the
crossed pairing, the whole-circuit surprise, the corrected `R`-hypothesis, the tightness family and
the independent sweep, and re-bound both claims at `CERTIFIED*`. It also found **three** things
wrong with Amendment 3 itself. This amendment installs exactly those three repairs and nothing
else:

| item | target | reviewer's locus | action |
|---|---|---|---|
| **A4-R1** | Amendment 3 §2.3, Lemma B's *Derivation*, constancy step | review §3.7 | the inequality `d_{R'} ≤ d_∞` is **backwards**; install the reviewer's one-clause repair |
| **A4-R2** | Amendment 1 §3.4, its replacement block for base §8 item 4 | review §3.6, second bullet | Amendment 3's R9 disposed of this by prose; supply the missing **exact** block replacement |
| **A4-R3** | Amendment 3 §8, verification checklist | review §3.6, first bullet | the checklist says **15** `Old` quotations; there are **17** |

Two of the three are defects in *prose about the mathematics* rather than in the mathematics: A4-R1
is a derivation gap whose conclusion is unaffected (§2.2, §5.2), and A4-R3 is a miscount. A4-R2 is
the one that leaves a **refuted statement standing verbatim in live text**, and is the most
consequential of the three.

**The exact inputs are bound as follows.** Reproduced by `anchors.py` (§5.1); genuine output in
§5.4.

```text
base proof
  artifacts/circdist_lift_iff_proof_20260820.md
  SHA-256  97cb3c8da839d1b96f58c281145cec8b70269ed3e6dfb29136f0bda00f564979
  size     90225 bytes, 1497 lines

Amendment 1                                   (A4-R2 edits this file's §3.4)
  artifacts/circdist_lift_iff_amendment1_20260820.md
  SHA-256  7220d538a9ee680711f591de30dbcc52bb80aa669a778ed3468cc9781c80a467
  size     34143 bytes, 618 lines

Amendment 2                                   (its §3.2 sub-clause edit is absorbed by A4-R2)
  artifacts/circdist_lift_iff_amendment2_20260820.md
  SHA-256  0ab3ce438fe6a3971be43a7090518087a9bd06566345d33326ca8e3e19079603
  size     11783 bytes, 239 lines

Amendment 3                                   (A4-R1 and A4-R3 edit this file)
  artifacts/circdist_lift_iff_amendment3_20260823.md
  SHA-256  e35324bfdf16d49e2b3a1bc4297d7fbed4feb0ce412b9ecec9b3fcc4cfd9e28c
  size     75528 bytes, 1388 lines

wave-23 re-review acted on                    (the commissioning document)
  artifacts/circdist_iff_amendment3_review_20260823.md
  SHA-256  0e3321977659a1333445b6b5734e0a1288febd8e0ce06afc6b4d9fc8250aa7c4
  size     21329 bytes, 324 lines

wave-17 review (context; not repaired here)
  artifacts/circdist_lift_claimrepair2_review_20260823.md
  SHA-256  9a0d3378e3fbc655114593cc52417b006fc51d2e5b3f57be43fef4373271cfc7
  size     32656 bytes, 476 lines
```

Amendment 3 reproduces at the digest the commission names (`e35324bf…`). If any bound hash fails to
reproduce, this amendment is void until it is re-derived against the changed input.

**Model code.** §5's numerics run Amendment 3's own §6.0 `persector.py`, extracted verbatim from
`e35324bf…` — 312 lines, unmodified. Re-using the proposer's own ground-truth simulator is
deliberate: A4-R1 is a claim about a *derivation*, and the point is to test the derivation against
the same model the derivation is about, not to re-litigate the model.

**Epistemic ceiling.** This amendment is **unreviewed**. Its §2 derivations are proposer-level. It
does not inherit the wave-23 review's `CERTIFIED*` and does not confer it.

---

## 1. A4-R1 — Lemma B's constancy step

### 1.1 The defect, as the reviewer states it

The wave-23 re-review, §3.7, quoting Amendment 3 §2.3:

> The derivation reads:
>
> > "let `R' > R ≥ d_∞` and let `F` be a minimum-weight undetectable logical of `C_{R'}(M)`,
> > `|F| = d_{R'}`. By 5.9 its occupied rounds form a contiguous interval of span
> > `≤ |F| = d_{R'} ≤ d_∞ ≤ R`"
>
> **`d_{R'} ≤ d_∞` is the inequality backwards.** `d_R` is non-increasing with limit `d_∞`, so
> `d_{R'} ≥ d_∞` for every finite `R'`, with equality only past the stabilisation point. As written
> the chain that delivers `span ≤ R` does not close, and this step is load-bearing: it is what
> identifies `d_R` with the bi-infinite `d_∞` in 5.6(a) and what transports `(⟸)` of 5.7 to finite `R`.

And the repair, which the reviewer states as already verified:

> **The repair is one clause and I verified it.** `d_R` is a non-increasing sequence of non-negative
> integers, so it stabilises at some finite `R₀` with `d_{R'} = d_∞` for all `R' ≥ R₀`. Choose
> `R' = max(R, R₀) + 1`; then `|F| = d_{R'} = d_∞ ≤ R` and the rest of the argument runs unchanged.

I agree with both halves, and I have re-derived the corrected chain and re-run the numerics rather
than take the verification on report. §1.2 and §5 are that work.

### 1.2 The corrected chain, re-derived here

Write `d_R := d_circ(C_R(M))` for a fixed memory sector, `d_∞ := lim_R d_R`.

1. **Monotonicity** (unchanged). More rounds give more fault locations with the boundaries
   unchanged, so `d_{R+1} ≤ d_R`; the sequence is non-increasing, the limit exists, and
   `d_R ≥ d_∞` for every finite `R`. *This is the step the broken clause contradicts.*
2. **Stabilisation** (the new clause). `(d_R)` is a non-increasing sequence of **non-negative
   integers**, so by well-ordering it is eventually constant: there is a finite `R₀` with
   `d_{R'} = d_∞` for every `R' ≥ R₀`. No bound on `R₀` is claimed or needed — only finiteness.
3. **The choice.** Fix `R ≥ d_∞` and put `R' := max(R, R₀) + 1`. Then `R' > R` and `R' ≥ R₀`, so
   `d_{R'} = d_∞`.
4. **The witness.** Let `F` be a minimum-weight undetectable logical of `C_{R'}(M)`; then
   `|F| = d_{R'} = d_∞`.
5. **The span bound.** By 5.9, `F`'s occupied rounds form a contiguous interval of span
   `≤ |F| = d_∞ ≤ R`, the last inequality being the standing hypothesis `R ≥ d_∞`. *The chain now
   closes.*
6. **Translation.** By Lemma 4.1 the detector index set is the full interval at both ends and the
   bulk is time-translation invariant, so `F` may be translated to start at round `0`, and, having
   span `≤ R`, it lands inside `C_R(M)`. Hence `d_R ≤ |F| = d_∞`.
7. **Conclusion.** With (1), `d_R = d_∞` for every `R ≥ d_∞`. Since Lemma A gives `d_∞ ≤ d_sec`,
   `R ≥ d_sec ⟹ R ≥ d_∞`, so `d_R` is constant for all `R ≥ d_sec` with value `d_{R = d_sec}`. ∎

*Derivation status: complete.*

**What changed, exactly.** The original argument fixed an arbitrary `R' > R` and needed `d_{R'}`
small; the corrected one *chooses* `R'` past stabilisation so that `d_{R'}` is exactly `d_∞`. The
original closed with `d_R = d_{R'}` for an arbitrary `R'`; the corrected one closes with
`d_R = d_∞` directly, which is what Lemma B asserts — so the repair is, if anything, a shortening.
**Lemma B's statement is untouched.** Only its derivation moves.

### 1.3 A caveat the reviewer did not state, and I do

The reviewer says the repair is "one clause". That is true, but it is worth recording *why* the
error survived Amendment 3's own 194-instance sweep and my 192-instance hunt: **on every instance
either of us can reach, `d_R` is already constant from `R = 1`** (§5.3: stabilisation index
`R₀ = 1` in 192/192). Where `R₀ = 1` we have `d_{R'} = d_∞` identically, so the broken clause
`d_{R'} ≤ d_∞` is *accidentally true, with equality*, and no simulation can falsify it.

The defect is therefore **a logical gap, not a numerically witnessed falsehood**: the step is not
licensed by the hypotheses it cites, even though its conclusion happens to hold throughout the
reachable family. §5.2 settles it in the only register that can — order-theoretically, over all
non-increasing non-negative integer sequences, where the original inference fails on 190 of 210 and
the repaired one on none of 1224. I flag this as a **DEVIATION** from a bare reading of the
commission ("run a numerical check confirming the corrected inequality direction"): the numerical
check *does* confirm the corrected direction (`d_{R'} ≥ d_∞`, 148/148), but it cannot exhibit the
broken direction failing, and I decline to imply otherwise.

---

## 2. A4-R2 — the block R9 left standing

### 2.1 The defect

Amendment 3's R9 reads, in full:

> Amendment 1's 5.10(1′) is superseded by R8's 5.10(1‴); its `≤ d` occurrences inherit the same
> per-sector / whole-circuit split.

It then gives exact replacements for Amendment 1 **§3.6** only. But Amendment 1 §3.4 contains a
*second* replacement block — its replacement for base **§8 item 4** — which supersession prose does
not reach, and which still literally reads "per sector, `d_R` is constant for `R ≥ d`, so the window
bound is `B(r,d) = d`". That is the **refuted per-sector form, stated verbatim, in live text**: it
is precisely what Amendment 3 §2.5's asymmetric codes refute and what the wave-17 witness
(`d_X = 3`, `d_Z = 2`, `d = 2`, `d_circ(Z-mem) = 3 > d`) falsifies. Amendment 2 §3.2 edited only
that block's `R_sat` sub-clause, so nothing else reaches it either.

The passage **is** on Amendment 3's §4 dependent-passage list, so the list is complete; what is
missing is the replacement. §2.2 supplies it.

### 2.2 The replacement is not a mechanical `d → d_sec`

Three things have to be folded into one block, and this is why prose supersession was not enough:

* **Amendment 3 Lemma A / Lemma B** — per sector the constant is `d_sec`, not `d`; the window bound
  is `B(r,d) = d_sec`.
* **Amendment 3 Lemma B′ / R8** — whole-circuit the constant *is* `d` and the block's original
  claim is true on that reading; `R_sat` is defined in the frozen 公共定义 against the
  whole-circuit `d_R(M)`, so the `R_sat` clause must stay whole-circuit.
* **Amendment 2 §3.2 (L2)** — the finite branch is `R_sat(M) = 1`, not `R_sat(M) ≤ d`.

A blanket `d → d_sec` would have been **wrong**: it would have broken the `R_sat` dichotomy, which
needs `d`. The block has to carry *both* constants, each on its own reading. The new block below
does, and it absorbs Amendment 2 §3.2's sub-clause edit rather than contradicting it — after A4-R2,
Amendment 2 §3.2 is discharged, not overridden.

---

## 3. Exact replacements

Three replacements. Each `Old` is quoted byte-exact and verified to occur **exactly once** in its
named source (§5.4).

### A4-R1 — Amendment 3 §2.3, Lemma B's *Derivation*

> **Old:** "Lemma A gives `d_R ≤ d_sec` for every `R`, hence `d_∞ ≤ d_sec`. Constancy: let
> `R' > R ≥ d_∞` and let `F` be a minimum-weight undetectable logical of `C_{R'}(M)`,
> `|F| = d_{R'}`. By 5.9 its occupied rounds form a contiguous interval of span
> `≤ |F| = d_{R'} ≤ d_∞ ≤ R`; by Lemma 4.1 the detector index set is the full interval at both ends
> and the bulk is time-translation invariant, so `F` may be translated to start at round `0` and
> lands inside `C_R(M)`, whence `d_R ≤ d_{R'}`. With monotonicity, `d_R = d_{R'}`. ∎"

> **New:** "Lemma A gives `d_R ≤ d_sec` for every `R`, hence `d_∞ ≤ d_sec`. Constancy: fix
> `R ≥ d_∞`. Since `(d_R)` is a non-increasing sequence of **non-negative integers** it is
> eventually constant — there is a finite `R₀` with `d_{R'} = d_∞` for every `R' ≥ R₀` (no bound on
> `R₀` is needed, only finiteness). Put `R' := max(R, R₀) + 1`, so that `R' > R` and
> `d_{R'} = d_∞`, and let `F` be a minimum-weight undetectable logical of `C_{R'}(M)`, so that
> `|F| = d_{R'} = d_∞`. By 5.9 its occupied rounds form a contiguous interval of span
> `≤ |F| = d_∞ ≤ R`, the last step being the hypothesis `R ≥ d_∞`; by Lemma 4.1 the detector index
> set is the full interval at both ends and the bulk is time-translation invariant, so `F` may be
> translated to start at round `0` and, having span `≤ R`, lands inside `C_R(M)`, whence
> `d_R ≤ |F| = d_∞`. With monotonicity (`d_R ≥ d_∞`), `d_R = d_∞`. ∎"

**Scope note.** The replacement is confined to the *Constancy* sentence and its chain. Monotonicity
and Ceiling are reproduced unchanged; the trailing commentary sentence of §2.3 ("This is the base
derivation of 5.10(1) with `d` replaced by `d_∞` …") is **not** touched and remains correct.

### A4-R2 — Amendment 1 §3.4, the replacement block for base §8 item 4

> **Old:** "4. **A `CIRCDIST.sat` deliverable falls out, in the corrected form.** 5.10(1′): for
> every single-ancilla CSS schedule with ideal boundaries, per sector, `d_R` is constant for
> `R ≥ d`, so the window bound is `B(r,d) = d`; and `R_sat(M) ≤ d` **iff** `d_∞(M) = d`, otherwise
> `R_sat(M) = ∞`. The finite-window content is the real deliverable; the identification of it with
> `R_sat` was an error and is withdrawn. The `sat` node should check whether its commission's model
> coincides with §1 before adopting even the corrected form."

> **New:** "4. **A `CIRCDIST.sat` deliverable falls out, in the corrected form.** 5.10(1‴)
> (Amendment 2 §3.1 as repaired by Amendment 3 R8): for every single-ancilla CSS schedule with
> ideal boundaries, `d_R(M)` is non-increasing in `R`. **Per sector** it is constant for
> `R ≥ d_sec`, that sector's own spatial distance (`d_X` for the Z-memory, `d_Z` for the X-memory,
> Definition A.0), and the per-sector window bound is `B(r,d) = d_sec`; the constant `d` is **not**
> available per sector (Amendment 3 Lemma A and the asymmetric codes of §2.5). **Whole-circuit** —
> `d_R(M) := d_circ(C_R(M))` the min over the two sectors per Definition 1.5, which is the reading
> the frozen `R_sat` definition uses — it is constant for `R ≥ d`, so `B(r,d) = d` (Amendment 3
> Lemma B′), and `R_sat(M) = 1` **iff** `d_∞(M) = d`, otherwise `R_sat(M) = ∞` (Amendment 2 §3.2).
> The finite-window content is the real deliverable; the identification of it with `R_sat` was an
> error and is withdrawn. The `sat` node should check whether its commission's model coincides with
> §1 before adopting even the corrected form, and must not read the per-sector window bound as
> `d`."

**Absorption note.** This block supersedes Amendment 2 §3.2's sub-clause edit by *carrying* it: the
`R_sat(M) = 1` form is reproduced above, so §3.2's instruction is discharged rather than
contradicted. Amendment 2 §3.2 quoted the sub-clause in ASCII transliteration
("`R_sat(M) <= d` iff `d_infty(M) = d`") whereas Amendment 1's bytes are Unicode
("`R_sat(M) ≤ d` **iff** `d_∞(M) = d`"); the `Old` above is Amendment 1's actual bytes.

### A4-R3 — Amendment 3 §8, verification checklist

> **Old:** "- [x] Checked every "Old" quotation of §3 programmatically against its source file: all
> 15 occur exactly once, modulo line-wrapping."

> **New:** "- [x] Checked every "Old" quotation of §3 programmatically against its source file: all
> **17** occur exactly once, modulo line-wrapping. (The count read 15 until Amendment 4 A4-R3; the
> check itself was run on all 17, so the correction is to the tally, not to the work. Amendment 4
> adds three more such quotations, in its own §3.)"

**Census.** I counted independently rather than adopt the reviewer's figure: 17 blockquote lines
beginning `> **Old` in Amendment 3 §3, distributed R1×2, R2×1, R3×1, R4×1, R5×1, R6×2, R7×3, R8×2,
R9×2, R10×2, R11×1, R12×0. Genuine output in §5.4.

---

## 4. Dependent-passage list

Everything that reads the repaired text, and its status after this amendment.

| passage | depends on | effect of Amendment 4 |
|---|---|---|
| Amendment 3 §2.3, **Lemma B** statement | — | **none.** The statement is unchanged; only its derivation moves (A4-R1). |
| Amendment 3 §2.3, **Lemma B′** | Lemma B, for the sector attaining the min | **none in content**; its citation of Lemma B now points at a closed chain. Reviewer §3.7 concurs; §5.3 C1–C8 confirms numerically. |
| Amendment 3 §2.3, **Lemma C** | Lemma A's ceiling `d_sec`, *not* `d_∞` | **none.** Independently re-checked here: window `W = d_sec` returns `d_circ` on 148/148 (§5.3, C7). |
| Amendment 3 §2.4, **5.6′/5.7′** | Lemma B, to identify `d_R` with `d_∞` at finite `R` | **none in content.** This is the load-bearing consumer the reviewer names; A4-R1 is what makes it sound. |
| Amendment 3 §3 **R6** replacement text | Lemma A (`w = d_{R'} ≤ d_sec`), not `d_∞` | **none.** Re-checked: `d_{R'} ≤ d_sec` on 148/148 (§5.3, C8). |
| Amendment 3 §3 **R8**, 5.10(1‴) per-sector clause | Lemma B | **none in content**; sound after A4-R1. Its whole-circuit clause is quoted into the new §8-item-4 block by A4-R2. |
| Amendment 3 §3 **R9**, Amendment 1 §3.6 | — | **none.** R9's §3.6 replacements stand as written; A4-R2 supplies only the block R9 omitted. |
| **Amendment 1 §3.4**, base §8-item-4 block | the refuted per-sector form | **replaced** (A4-R2). This is the only live text this amendment changes the content of. |
| **Amendment 2 §3.2** | Amendment 1 §3.4's `R_sat` sub-clause | **discharged by absorption** (A4-R2), not overridden. |
| Amendment 3 §2.5, tightness / asymmetric family | Lemma A only | **none.** Not re-derived here; cited. |
| Amendment 3 §5.1/§5.2, claim strings | the constant, unchanged by this amendment | **none.** `0c4c466b…`, `9bec82a5…` stand (§5.4). |
| wave-23 review §4.2's both-fixes root variant `582f9e06…` | S1 + `d_sec` | **none.** Not touched here. |
| Amendment 3 §8 checklist | — | **tally corrected** (A4-R3). No verification result changes. |

No passage on this list requires a *further* replacement. In particular I checked, and did not
find, any other live occurrence of the refuted per-sector "`constant for R ≥ d`" form outside the
block A4-R2 replaces.

---

## 5. NUMERICAL verification — code and genuine output

Four scripts. `persector.py` is Amendment 3 §6.0 verbatim (312 lines, extracted from `e35324bf…`)
and is not reproduced here; the three new scripts are given in full.

### 5.1 `anchors.py` — input binding and quotation uniqueness

```python
#!/usr/bin/env python3
"""Amendment 4: bind the inputs, and assert each 'Old' quotation is unique in its source."""
import hashlib, os

ROOT = "<repo>"
F = lambda p: os.path.join(ROOT, p)

BOUND = [
    ("base proof",   "artifacts/circdist_lift_iff_proof_20260820.md"),
    ("Amendment 1",  "artifacts/circdist_lift_iff_amendment1_20260820.md"),
    ("Amendment 2",  "artifacts/circdist_lift_iff_amendment2_20260820.md"),
    ("Amendment 3",  "artifacts/circdist_lift_iff_amendment3_20260823.md"),
    ("wave-23 re-review", "artifacts/circdist_iff_amendment3_review_20260823.md"),
    ("wave-17 review",    "artifacts/circdist_lift_claimrepair2_review_20260823.md"),
]

print("=== bound inputs ===")
for lbl, p in BOUND:
    b = open(F(p), "rb").read()
    print("%-20s %s  %6d bytes %5d lines  %s"
          % (lbl, hashlib.sha256(b).hexdigest(), len(b), b.count(b"\n"), os.path.basename(p)))

A3 = open(F("artifacts/circdist_lift_iff_amendment3_20260823.md"), encoding="utf-8").read()
A1 = open(F("artifacts/circdist_lift_iff_amendment1_20260820.md"), encoding="utf-8").read()

OLD_R1 = """> Lemma A gives `d_R ≤ d_sec` for every `R`, hence `d_∞ ≤ d_sec`. Constancy: let `R' > R ≥ d_∞` and
> let `F` be a minimum-weight undetectable logical of `C_{R'}(M)`, `|F| = d_{R'}`. By 5.9 its
> occupied rounds form a contiguous interval of span `≤ |F| = d_{R'} ≤ d_∞ ≤ R`; by Lemma 4.1 the
> detector index set is the full interval at both ends and the bulk is time-translation invariant,
> so `F` may be translated to start at round `0` and lands inside `C_R(M)`, whence `d_R ≤ d_{R'}`.
> With monotonicity, `d_R = d_{R'}`. ∎"""

OLD_R2 = """> 4. **A `CIRCDIST.sat` deliverable falls out, in the corrected form.** 5.10(1′): for every
>    single-ancilla CSS schedule with ideal boundaries, per sector, `d_R` is constant for `R ≥ d`,
>    so the window bound is `B(r,d) = d`; and `R_sat(M) ≤ d` **iff** `d_∞(M) = d`, otherwise
>    `R_sat(M) = ∞`. The finite-window content is the real deliverable; the identification of it
>    with `R_sat` was an error and is withdrawn. The `sat` node should check whether its
>    commission's model coincides with §1 before adopting even the corrected form."""

OLD_R3 = """- [x] Checked every "Old" quotation of §3 programmatically against its source file: all 15 occur
  exactly once, modulo line-wrapping."""

print()
print("=== 'Old' quotation uniqueness ===")
for tag, src, srcname, q in (("A4-R1", A3, "Amendment 3 §2.3", OLD_R1),
                             ("A4-R2", A1, "Amendment 1 §3.4", OLD_R2),
                             ("A4-R3", A3, "Amendment 3 §8",   OLD_R3)):
    n = src.count(q)
    print("%-6s in %-18s : %d occurrence(s)  %-4s  (%d chars)"
          % (tag, srcname, n, "OK" if n == 1 else "FAIL", len(q)))
    assert n == 1, tag

print()
print("=== Amendment 3 §3 'Old' quotation census (A4-R3's subject) ===")
sec3 = A3[A3.index("## 3. Exact replacements in the base proof"):A3.index("## 4. Dependent-passage list")]
n_old = sum(1 for ln in sec3.split("\n") if ln.startswith("> **Old"))
print("blockquote lines beginning '> **Old' in Amendment 3 §3 : %d" % n_old)
print("Amendment 3 §8 checklist asserts                      : 15")
print("verdict                                              : checklist short by %d" % (n_old - 15))

print()
print("=== claim strings this amendment does NOT touch ===")
for lbl, h in (("CIRCDIST.lift.iff corrected (A3 §5.1)",
                "0c4c466b895d938d2028140967d87974ee2216b3cebcc48967804f530e227240"),
               ("CIRCDIST.lift  d_sec-only variant (A3 §5.2)",
                "9bec82a557e7421efd1faceee31f36ef888511c5b85c687d2fed77a1c1e21ae9"),
               ("CIRCDIST.lift  both-fixes variant (review §4.2)",
                "582f9e06b887dd46ae2fa6be73917b853ceefbb13c08b5da699256496b7389d0")):
    print("  %-48s %s  UNCHANGED" % (lbl, h[:16] + "…"))
```

### 5.2 `chain_check.py` — the logic of the constancy step, model-free

The constancy step consumes **only** that `(d_R)` is non-increasing in the non-negative integers.
So it can be tested exhaustively over all such sequences, with no quantum code in sight. This is
the check that actually adjudicates A4-R1, for the reason given in §1.3.

```python
#!/usr/bin/env python3
"""Order-theoretic check of Lemma B's constancy step, independent of the QEC model.

The step consumes only: (d_R) non-increasing, non-negative integers, d_infty its limit.
Enumerate EVERY such sequence over a small range and test the two chains.

  ORIGINAL (Amendment 3 §2.3): fix R >= d_infty, take ANY R' > R, assert d_{R'} <= d_infty.
  REPAIRED (review §3.7):      fix R >= d_infty, take R' = max(R,R0)+1 where R0 is the
                               stabilisation index; assert |F| = d_{R'} = d_infty <= R.

A sequence is "eventually constant" past R0; we model d_{R'} for R' > len(seq) as d_infty.
"""
import itertools

MAXV, LEN = 4, 6

def seqs():
    for s in itertools.product(range(MAXV + 1), repeat=LEN):
        if all(s[i + 1] <= s[i] for i in range(LEN - 1)):
            yield s

def d(seq, R):                       # 1-based; constant past the end
    return seq[R - 1] if R <= len(seq) else seq[-1]

def main():
    tot = 0
    orig_bad = orig_bad_seqs = 0
    rep_bad = 0
    rep_inst = 0
    witnesses = []
    for s in seqs():
        tot += 1
        d_inf = s[-1]
        R0 = next(i + 1 for i, v in enumerate(s) if v == d_inf)
        seq_bad = False
        for R in range(1, LEN + 1):
            if R < d_inf:
                continue
            # ---- ORIGINAL: "let R' > R ... |F| = d_{R'} <= d_infty"
            for Rp in range(R + 1, LEN + 3):
                if not (d(s, Rp) <= d_inf):
                    orig_bad += 1
                    seq_bad = True
                    if len(witnesses) < 6:
                        witnesses.append((s, R, Rp, d(s, Rp), d_inf))
            # ---- REPAIRED: R' = max(R,R0)+1
            Rp = max(R, R0) + 1
            rep_inst += 1
            wF = d(s, Rp)
            if not (wF == d_inf and d_inf <= R):
                rep_bad += 1
        if seq_bad:
            orig_bad_seqs += 1

    print("non-increasing non-negative integer sequences enumerated (len %d, values 0..%d): %d"
          % (LEN, MAXV, tot))
    print()
    print("ORIGINAL chain  'let R' > R >= d_inf ... |F| = d_{R'} <= d_inf'")
    print("  (sequence, R') pairs where the asserted inequality is FALSE : %d" % orig_bad)
    print("  sequences admitting at least one such falsifying choice     : %d / %d"
          % (orig_bad_seqs, tot))
    print("  -> the step is NOT licensed by the hypotheses it cites.")
    print()
    print("  first falsifying witnesses (seq, R, R', d_{R'}, d_inf):")
    for w in witnesses:
        print("    seq=%s  R=%d  R'=%d  d_{R'}=%d  d_inf=%d   %d <= %d is FALSE"
              % (w[0], w[1], w[2], w[3], w[4], w[3], w[4]))
    print()
    print("REPAIRED chain  \"R' = max(R,R0)+1 ; |F| = d_{R'} = d_inf <= R\"")
    print("  instantiations checked                                      : %d" % rep_inst)
    print("  failures                                                     : %d" % rep_bad)
    print("  -> the corrected chain closes on every sequence and every R >= d_inf.")

if __name__ == '__main__':
    main()
```

**Genuine output.**

```text
non-increasing non-negative integer sequences enumerated (len 6, values 0..4): 210

ORIGINAL chain  'let R' > R >= d_inf ... |F| = d_{R'} <= d_inf'
  (sequence, R') pairs where the asserted inequality is FALSE : 1235
  sequences admitting at least one such falsifying choice     : 190 / 210
  -> the step is NOT licensed by the hypotheses it cites.

  first falsifying witnesses (seq, R, R', d_{R'}, d_inf):
    seq=(1, 1, 0, 0, 0, 0)  R=1  R'=2  d_{R'}=1  d_inf=0   1 <= 0 is FALSE
    seq=(1, 1, 1, 0, 0, 0)  R=1  R'=2  d_{R'}=1  d_inf=0   1 <= 0 is FALSE
    seq=(1, 1, 1, 0, 0, 0)  R=1  R'=3  d_{R'}=1  d_inf=0   1 <= 0 is FALSE
    seq=(1, 1, 1, 0, 0, 0)  R=2  R'=3  d_{R'}=1  d_inf=0   1 <= 0 is FALSE
    seq=(1, 1, 1, 1, 0, 0)  R=1  R'=2  d_{R'}=1  d_inf=0   1 <= 0 is FALSE
    seq=(1, 1, 1, 1, 0, 0)  R=1  R'=3  d_{R'}=1  d_inf=0   1 <= 0 is FALSE

REPAIRED chain  "R' = max(R,R0)+1 ; |F| = d_{R'} = d_inf <= R"
  instantiations checked                                      : 1224
  failures                                                     : 0
  -> the corrected chain closes on every sequence and every R >= d_inf.
```

### 5.3 `run_lemmaB.py` — the corrected chain on real instances

Ground-truth `d_R` by direct multi-round frame simulation (`persector.py`), per sector, on the
wave-17 witness plus chain / cyclic-chain / random asymmetric CSS codes. Checks C1–C8 as documented
in the docstring; C5 instantiates the **repaired** chain at every `R ≥ d_∞`.

```python
#!/usr/bin/env python3
"""Amendment 4 NUMERICAL: the corrected Lemma B constancy chain (Amendment 3 §2.3).

Checks, per (code, schedule, sector) instance, with d_R obtained by GROUND-TRUTH
multi-round frame simulation (persector.py, Amendment 3 §6.0 verbatim):

  C1  monotonicity           d_{R+1} <= d_R                                   (Lemma B, unchanged)
  C2  CORRECTED direction    d_{R'} >= d_infty for every finite R'            (what monotonicity gives)
  C3  BROKEN clause          d_{R'} <= d_infty  -- counted, expected to FAIL when not yet stabilised
  C4  stabilisation          exists finite R0 with d_{R'} = d_infty for R' >= R0; R0 <= d_sec
  C5  REPAIRED chain         for every R >= d_infty, with R' = max(R,R0)+1:
                               |F| = d_{R'} = d_infty <= R   and   d_R = d_infty
  C6  Lemma A ceiling        d_R <= d_sec for every R                         (unaffected)
  C7  Lemma C window         sec510 at W = d_sec returns d_circ               (unaffected)
  C8  R6 replacement chain   w = d_{R'} <= d_sec                              (unaffected)
"""
import sys, os, random
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from persector import *


def chain(m):
    n = 2 * m
    A = [{2 * i, 2 * i + 1} for i in range(m)]
    B = [{2 * i, 2 * i + 1, 2 * i + 2, 2 * i + 3} for i in range(m - 1)]
    return n, A, B


def cyclic_chain(m):
    n = 2 * m
    A = [{2 * i, 2 * i + 1} for i in range(m)]
    B = [{2 * i, 2 * i + 1, (2 * i + 2) % n, (2 * i + 3) % n} for i in range(m)]
    return n, A, B


def witness6():
    """The wave-17 witness: n=6, d_X=3, d_Z=2, d=2 (Amendment 3 §6.1, verbatim)."""
    n = 6
    A = [{0, 1}, {2, 3}, {4, 5}]              # X-checks
    B = [{0, 1, 2, 3}, {2, 3, 4, 5}]          # Z-checks
    return n, A, B


def random_codes(rng, want, nmax=8):
    """Amendment 3 §6.2's generator, verbatim, for the decreasing-d_R hunt."""
    out = []; seen = set(); tries = 0
    while len(out) < want and tries < 200000:
        tries += 1
        n = rng.randint(5, nmax); rX = rng.randint(1, 3); A = []
        for _ in range(rX):
            w = rng.randint(2, min(4, n)); A.append(set(rng.sample(range(n), w)))
        HA = [mask(a) for a in A]; rA, pA = rref(list(HA))
        if len(rA) != rX: continue
        dual = [v for v in range(1, 1 << n) if all(pc(v & h) % 2 == 0 for h in HA)]
        if not dual: continue
        need = n - len(rA) - 1
        if need < 1: continue
        B = []
        for _ in range(min(need + rng.randint(0, 1), 4)):
            v = rng.choice(dual); B.append({q for q in range(n) if (v >> q) & 1})
        HB = [mask(b) for b in B]
        if len(rref(list(HB))[0]) != need: continue
        if any(len(b) < 2 or len(b) > 6 for b in B): continue
        dX, dZ, k, XL, ZL, _, _ = spatial_distances(n, A, B)
        if k != 1 or dX is None or dZ is None: continue
        if dX == dZ: continue
        if min(dX, dZ) < 2: continue
        if max(dX, dZ) > 5: continue
        key = (n, tuple(sorted(tuple(sorted(a)) for a in A)),
                  tuple(sorted(tuple(sorted(b)) for b in B)))
        if key in seen: continue
        seen.add(key); out.append(("rand%02d" % len(out), n, A, B))
    return out


def analyse(tag, n, A, B, gates, Rmax):
    dX, dZ, k, XL, ZL, _, _ = spatial_distances(n, A, B)
    if k != 1 or dX is None or dZ is None:
        return None
    d = min(dX, dZ)
    d_sec = dX                                   # this sector's own spatial distance
    inj, T = fault_menu(n, A, B, gates)
    data = one_round_data(n, A, B, gates, T, ZL, inj)
    dR = []
    for R in range(1, Rmax + 1):
        cols = columns(n, A, B, gates, T, R, ZL, inj)
        dR.append(dcirc_bfs(cols, cap=d_sec + 1))
    if any(v is None for v in dR):
        return None
    d_inf = dR[-1]

    r = dict(tag=tag, n=n, dX=dX, dZ=dZ, d=d, d_sec=d_sec, dR=list(dR), d_inf=d_inf)

    # C1 monotonicity
    r['C1'] = all(dR[i + 1] <= dR[i] for i in range(len(dR) - 1))
    # C2 corrected direction  d_{R'} >= d_infty
    r['C2'] = all(v >= d_inf for v in dR)
    # C3 broken clause d_{R'} <= d_infty : record where it fails
    r['C3_fail_R'] = [i + 1 for i, v in enumerate(dR) if not (v <= d_inf)]
    r['strict_decrease'] = len(r['C3_fail_R']) > 0
    # C4 stabilisation index R0 (1-based smallest R with d_R = d_infty)
    R0 = next(i + 1 for i, v in enumerate(dR) if v == d_inf)
    r['R0'] = R0
    r['C4'] = all(dR[i] == d_inf for i in range(R0 - 1, len(dR))) and R0 <= d_sec
    # C5 repaired chain, for every R >= d_infty inside the simulated range
    c5 = True; c5n = 0
    for R in range(1, Rmax + 1):
        if R < d_inf:
            continue
        Rp = max(R, R0) + 1
        if Rp > Rmax:                            # d_{R'} = d_infty past stabilisation
            wF = d_inf
        else:
            wF = dR[Rp - 1]
        c5n += 1
        if not (wF == d_inf and d_inf <= R and dR[R - 1] == d_inf):
            c5 = False
    r['C5'] = c5; r['C5_n'] = c5n
    # C6 Lemma A ceiling
    r['C6'] = all(v <= d_sec for v in dR)
    # C7 Lemma C window at W = d_sec
    r['C7'] = (sec510(data, len(B), d_sec) == d_inf)
    # C8 R6's chain w = d_{R'} <= d_sec
    r['C8'] = all(v <= d_sec for v in dR)
    bad, tot = graph_like(data, len(B))
    r['glike'] = (bad == 0)
    return r


def main():
    rng = random.Random(20260823)
    codes = [("witness6", ) + witness6()]
    for m in (3, 4, 5):
        codes.append(("chain%d" % m, ) + chain(m))
    for m in (3, 4):
        codes.append(("cyc%d" % m, ) + cyclic_chain(m))
    codes += random_codes(rng, 30)

    rows = []
    for (name, n, A, B) in codes:
        Rmax = 5 if n <= 8 else 4
        got = 0
        for kind in ['NI_Zfirst', 'NI_Xfirst'] + ['random'] * 40:
            gates, tx, tz = make_schedule(n, A, B, kind, rng)
            if not mc_ok(n, A, B, tx, tz):
                continue
            if kind == 'random' and got >= 3:
                break
            r = analyse("%s/%s/Zmem" % (name, kind), n, A, B, gates, Rmax)
            if r: rows.append(r)
            A2, B2, g2, tx2, tz2 = mirror_instance(n, A, B, tx, tz)
            r = analyse("%s/%s/Xmem" % (name, kind), n, A2, B2, g2, Rmax)
            if r: rows.append(r)
            got += 1

    keys = ['C1', 'C2', 'C4', 'C5', 'C6', 'C7', 'C8']
    print("instances analysed: %d" % len(rows))
    print()
    print("%-26s %4s %4s %5s %5s %-18s %5s %3s  %s" %
          ("tag", "d_X", "d_Z", "d", "d_sec", "d_R (R=1,2,...)", "d_inf", "R0", "C1..C8"))
    dec = 0
    for r in rows:
        flags = ''.join('.' if r[k] else 'X' for k in keys)
        if r['strict_decrease']:
            dec += 1
        print("%-26s %4d %4d %5d %5d %-18s %5d %3d  %s%s" %
              (r['tag'], r['dX'], r['dZ'], r['d'], r['d_sec'], str(r['dR']),
               r['d_inf'], r['R0'], flags,
               "   <-- d_R strictly decreases; broken clause d_R'<=d_inf FALSE at R=%s"
               % r['C3_fail_R'] if r['strict_decrease'] else ""))
    print()
    for k in keys:
        nfail = sum(1 for r in rows if not r[k])
        print("  %-4s violations: %d / %d" % (k, nfail, len(rows)))
    print()
    print("  instances where d_R strictly decreases (broken clause d_{R'} <= d_inf is FALSE"
          " for some finite R'): %d / %d" % (dec, len(rows)))
    print("  C5 repaired-chain instantiations checked (one per R >= d_inf per instance): %d"
          % sum(r['C5_n'] for r in rows))
    print("  graph-like instances: %d / %d" % (sum(1 for r in rows if r['glike']), len(rows)))


if __name__ == '__main__':
    main()
```

**Genuine output** (first 14 of 148 instance rows shown; the elided 134 rows are all `.......`,
as the violation tallies below confirm).

```text
instances analysed: 148

tag                         d_X  d_Z     d d_sec d_R (R=1,2,...)    d_inf  R0  C1..C8
witness6/NI_Zfirst/Zmem       3    2     2     3 [3, 3, 3, 3, 3]        3   1  .......
witness6/NI_Zfirst/Xmem       2    3     2     2 [1, 1, 1, 1, 1]        1   1  .......
witness6/NI_Xfirst/Zmem       3    2     2     3 [3, 3, 3, 3, 3]        3   1  .......
witness6/NI_Xfirst/Xmem       2    3     2     2 [1, 1, 1, 1, 1]        1   1  .......
chain3/NI_Zfirst/Zmem         3    2     2     3 [3, 3, 3, 3, 3]        3   1  .......
chain3/NI_Zfirst/Xmem         2    3     2     2 [1, 1, 1, 1, 1]        1   1  .......
chain3/NI_Xfirst/Zmem         3    2     2     3 [3, 3, 3, 3, 3]        3   1  .......
chain3/NI_Xfirst/Xmem         2    3     2     2 [1, 1, 1, 1, 1]        1   1  .......
chain3/random/Zmem            3    2     2     3 [3, 3, 3, 3, 3]        3   1  .......
chain3/random/Xmem            2    3     2     2 [1, 1, 1, 1, 1]        1   1  .......
chain4/NI_Zfirst/Zmem         4    2     2     4 [4, 4, 4, 4, 4]        4   1  .......
chain4/NI_Zfirst/Xmem         2    4     2     2 [1, 1, 1, 1, 1]        1   1  .......
chain4/NI_Xfirst/Zmem         4    2     2     4 [4, 4, 4, 4, 4]        4   1  .......
                                    [ ... 134 further rows, all flags '.......' ... ]

  C1   violations: 0 / 148
  C2   violations: 0 / 148
  C4   violations: 0 / 148
  C5   violations: 0 / 148
  C6   violations: 0 / 148
  C7   violations: 0 / 148
  C8   violations: 0 / 148

  instances where d_R strictly decreases (broken clause d_{R'} <= d_inf is FALSE for some finite R'): 0 / 148
  C5 repaired-chain instantiations checked (one per R >= d_inf per instance): 588
  graph-like instances: 59 / 148
```

**Reading.** C2 (`d_{R'} ≥ d_∞`, the *corrected* direction) holds 148/148 — this is the direction
monotonicity actually supplies, and the direction Amendment 3's text got backwards. C5 confirms the
repaired chain at 588 separate `(instance, R)` instantiations. C7 and C8 confirm the reviewer's
scope claim directly: **Lemma C and R6's replacement text are unaffected**, because both route
through Lemma A's `d_sec` and never through `d_∞`. Lemma B′ is likewise unaffected — it consumes
Lemma B's *statement*, which A4-R1 does not change.

The last three lines are the §1.3 caveat, in data: **no** instance strictly decreases.

### 5.4 `hunt_decrease.py` — and why the sweep cannot witness the defect

A dedicated hunt for a strictly decreasing `d_R`, over the same code families with up to 25
schedules each including heavily interleaved random ones — the setting where a temporal witness
cheaper than every spatial one could appear.

```python
#!/usr/bin/env python3
"""Targeted hunt: does d_R ever STRICTLY decrease in R?

If it never does, the broken clause `d_{R'} <= d_infty` of Amendment 3 §2.3 holds
with equality on every instance reachable here, and its falsity is a LOGICAL gap
(monotonicity does not license it) rather than a numerically witnessed one.
Heavily interleaved random schedules are the place a temporal witness cheaper than
every spatial one could appear.
"""
import sys, os, random
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from persector import *
from run_lemmaB import chain, cyclic_chain, witness6, random_codes

def main():
    rng = random.Random(4242)
    codes = [("witness6", ) + witness6()]
    for m in (3, 4, 5):
        codes.append(("chain%d" % m, ) + chain(m))
    for m in (3, 4):
        codes.append(("cyc%d" % m, ) + cyclic_chain(m))
    codes += random_codes(rng, 40)

    tested = 0; dec = []; R0hist = {}
    for (name, n, A, B) in codes:
        Rmax = 5 if n <= 7 else 4
        for si in range(25):
            kind = 'random' if si >= 2 else ('NI_Zfirst', 'NI_Xfirst')[si]
            gates, tx, tz = make_schedule(n, A, B, kind, rng)
            if not mc_ok(n, A, B, tx, tz):
                continue
            A2, B2, g2, tx2, tz2 = mirror_instance(n, A, B, tx, tz)
            for lbl, (nn, AA, BB, gg) in (("Zmem", (n, A, B, gates)),
                                          ("Xmem", (n, A2, B2, g2))):
                dX, dZ, k, XL, ZL, _, _ = spatial_distances(nn, AA, BB)
                if k != 1 or dX is None or dZ is None:
                    continue
                inj, T = fault_menu(nn, AA, BB, gg)
                dR = []
                for R in range(1, Rmax + 1):
                    cols = columns(nn, AA, BB, gg, T, R, ZL, inj)
                    v = dcirc_bfs(cols, cap=dX + 1)
                    if v is None:
                        dR = None; break
                    dR.append(v)
                if not dR:
                    continue
                tested += 1
                d_inf = dR[-1]
                R0 = next(i + 1 for i, v in enumerate(dR) if v == d_inf)
                R0hist[R0] = R0hist.get(R0, 0) + 1
                if dR[0] != dR[-1]:
                    dec.append(("%s/%s/%s" % (name, kind, lbl), dX, dZ, dR))
                    print("STRICT DECREASE: %-24s d_X=%d d_Z=%d  d_R=%s"
                          % ("%s/%s/%s" % (name, kind, lbl), dX, dZ, dR))
    print()
    print("instances tested                     : %d" % tested)
    print("instances with strictly decreasing d_R: %d" % len(dec))
    print("stabilisation index R0 histogram      : %s"
          % dict(sorted(R0hist.items())))

if __name__ == '__main__':
    main()
```

**Genuine output.**

```text
instances tested                     : 192
instances with strictly decreasing d_R: 0
stabilisation index R0 histogram      : {1: 192}
```

`R₀ = 1` in 192/192. Every reachable instance has a minimum-weight witness of round-span 1 — which
is exactly Lemma A's construction, a weight-`d_sec` single-round spatial fault. So `d_{R'} = d_∞`
identically, the broken clause is true with equality, and **no amount of simulation in this family
can falsify it**. §5.2 is therefore not a supplement to §5.3 but the load-bearing check for A4-R1.

### 5.5 `anchors.py` genuine output

```text
=== bound inputs ===
base proof           97cb3c8da839d1b96f58c281145cec8b70269ed3e6dfb29136f0bda00f564979   90225 bytes  1497 lines  circdist_lift_iff_proof_20260820.md
Amendment 1          7220d538a9ee680711f591de30dbcc52bb80aa669a778ed3468cc9781c80a467   34143 bytes   618 lines  circdist_lift_iff_amendment1_20260820.md
Amendment 2          0ab3ce438fe6a3971be43a7090518087a9bd06566345d33326ca8e3e19079603   11783 bytes   239 lines  circdist_lift_iff_amendment2_20260820.md
Amendment 3          e35324bfdf16d49e2b3a1bc4297d7fbed4feb0ce412b9ecec9b3fcc4cfd9e28c   75528 bytes  1388 lines  circdist_lift_iff_amendment3_20260823.md
wave-23 re-review    0e3321977659a1333445b6b5734e0a1288febd8e0ce06afc6b4d9fc8250aa7c4   21329 bytes   324 lines  circdist_iff_amendment3_review_20260823.md
wave-17 review       9a0d3378e3fbc655114593cc52417b006fc51d2e5b3f57be43fef4373271cfc7   32656 bytes   476 lines  circdist_lift_claimrepair2_review_20260823.md

=== 'Old' quotation uniqueness ===
A4-R1  in Amendment 3 §2.3   : 1 occurrence(s)  OK    (528 chars)
A4-R2  in Amendment 1 §3.4   : 1 occurrence(s)  OK    (552 chars)
A4-R3  in Amendment 3 §8     : 1 occurrence(s)  OK    (134 chars)

=== Amendment 3 §3 'Old' quotation census (A4-R3's subject) ===
blockquote lines beginning '> **Old' in Amendment 3 §3 : 17
Amendment 3 §8 checklist asserts                      : 15
verdict                                              : checklist short by 2

=== claim strings this amendment does NOT touch ===
  CIRCDIST.lift.iff corrected (A3 §5.1)            0c4c466b895d938d…  UNCHANGED
  CIRCDIST.lift  d_sec-only variant (A3 §5.2)      9bec82a557e7421e…  UNCHANGED
  CIRCDIST.lift  both-fixes variant (review §4.2)  582f9e06b887dd46…  UNCHANGED
```

---

## 6. What this amendment does **NOT** change

Stated explicitly, because the commission asks for it and because an amendment-to-an-amendment is
exactly where scope creep would hide.

1. **The `d_sec` constant proofs are untouched.** Lemma A (§2.2 of Amendment 3, the per-sector
   spatial ceiling `d_circ(sector) ≤ d_sec`), its crossed-pairing argument, the whole-circuit
   Lemma B′, Lemma C, and the §2.5 tightness family with its unboundedness result are **not**
   re-derived, weakened, strengthened, or edited here. A4-R1 repairs the *derivation* of Lemma B's
   constancy step only. **Lemma B's statement does not change**, and neither does any constant
   anywhere in the amendment family.
2. **No claim text changes. `0c4c466b…` stays untouched.** The corrected `CIRCDIST.lift.iff` claim
   string proposed at Amendment 3 §5.1 and re-verified at review §4.1, the root variant
   `9bec82a5…`, and the review's both-fixes root variant `582f9e06…` are all reproduced unchanged
   in §5.5 and are not edited, re-proposed, or re-hashed. **A claim edit is a dispatcher act.**
3. **No level is assigned or changed.** The wave-23 review's `CERTIFIED*` on both nodes stands as
   that reviewer set it. In particular I do **not** claim that A4-R1 promotes anything: the
   reviewer's ground 1 for withholding `PROVED` falls away once this repair lands, but grounds 2
   (installation) and 3 (review coverage) do not, and clearing them is not a proposer act.
4. **The `repair ≥ 3` gap is not repaired**, and remains outside the node claim per wave-16.
5. **Root blockers S1/S2 are not touched.**
6. **The `sat` family is not adjudicated.** A4-R2 rewrites a `CIRCDIST.sat`-facing block, but it
   only propagates the per-sector/whole-circuit split already established in Amendment 3; the
   cross-node flag on Corollary 7.3's `d_eff` (Amendment 3 §7 item 4) is carried forward, not
   resolved.
7. **Amendment 3's R1–R12 are not re-opened.** The wave-23 review drift-checked all 17 quotations
   and found them exact; I re-counted them (§5.5) but did not re-verify each against its source,
   and I record that as a limitation, not as a confirmation.
8. **No canonical file was modified.** `research/circdist/`, the proof-DAG, node records, the
   frozen 公共定义 and the scheduler were read only. This artifact is the sole file written.

---

## 7. Deviations

One, recorded in full at §1.3 and repeated here so it is not buried:

* **DEVIATION (scope of the numerical check for A4-R1).** The commission asks for "a numerical
  check on 3+ instances confirming the corrected inequality direction". I ran 148 instances and the
  corrected direction holds on all of them (§5.3, C2) — but I also found that the *broken*
  direction cannot be falsified numerically in this family, because `d_R` stabilises at `R₀ = 1` in
  192/192 instances (§5.4). Reporting only the 148 clean instances would have implied a
  discriminating test that was not performed. I therefore added `chain_check.py` (§5.2), which
  settles the step in the register that actually discriminates, and I state plainly that A4-R1 is a
  **derivation** repair with **no numerical consequence** — the same conclusion the reviewer
  reached about Lemma C, B′ and R6, now extended to Lemma B's own conclusion.

Nothing else in this amendment departs from the commission. No fourth repair was installed, no
other passage was edited, and no defect I noticed in passing was acted on.

---

## 8. Verification checklist

- [x] Reproduced the SHA-256 hashes and byte/line counts of the base proof, Amendments 1–3, the
  wave-23 re-review and the wave-17 review before writing; Amendment 3 reproduces at `e35324bf…`
  as the commission names (§5.5).
- [x] Read the wave-23 re-review §3.6 and §3.7 in full, and quoted the reviewer's statement of the
  defect and of the repair verbatim (§1.1).
- [x] Re-derived the corrected constancy chain independently, step by step (§1.2), rather than
  transcribing the reviewer's one-clause repair; confirmed it closes and that it *shortens* the
  original conclusion from `d_R = d_{R'}` to `d_R = d_∞`.
- [x] Checked all three "Old" quotations programmatically against their sources: each occurs
  **exactly once**, byte-exact including Unicode (§5.5).
- [x] Counted Amendment 3 §3's `Old` quotations independently: **17**, confirming the reviewer's
  count and the checklist's shortfall of 2 (§5.5).
- [x] Verified the corrected inequality direction `d_{R'} ≥ d_∞` on 148 (code, schedule, sector)
  instances, both sectors, ground truth by direct multi-round simulation: 0 violations (§5.3).
- [x] Instantiated the repaired chain at 588 separate `(instance, R ≥ d_∞)` pairs: 0 failures.
- [x] Confirmed the reviewer's scope claim independently — **Lemma C** (C7, window `W = d_sec`
  returns `d_circ`, 148/148), **R6's replacement text** (C8, `d_{R'} ≤ d_sec`, 148/148), and
  **Lemma B′** (consumes Lemma B's unchanged statement) are unaffected.
- [x] Settled the constancy step model-free over all 210 non-increasing non-negative integer
  sequences of length 6: original inference falsifiable on 190/210, repaired inference fails on
  0/1224 instantiations (§5.2).
- [x] Recorded, rather than concealed, that no reachable instance falsifies the broken clause
  (`R₀ = 1` in 192/192) and flagged the consequence as a DEVIATION (§1.3, §7).
- [x] Confirmed A4-R2's new block carries *both* constants on their correct readings, and that a
  blanket `d → d_sec` would have broken the `R_sat` dichotomy (§2.2).
- [x] Confirmed A4-R2 absorbs Amendment 2 §3.2's sub-clause edit rather than contradicting it.
- [x] Searched for other live occurrences of the refuted per-sector "constant for `R ≥ d`" form
  outside the A4-R2 block; found none (§4).
- [x] Confirmed the three claim digests this amendment does not touch (§5.5).
- [x] No existing file, proof-DAG object, node record, scheduler file, generated view or canonical
  record was modified; `research/` was read only. This artifact is append-only and is the sole
  file written by this session.

**No promotion.** This append-only proposer amendment supplies three checkable repairs to
Amendment 3 and Amendment 1. It assigns no status to the base proof, to any amendment, to these
repairs, or to either node, and it is itself unreviewed.
