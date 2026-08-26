#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ksum_r3_parity.py  --  R3 independent micro-audit of Lemma lem:core-odd
=======================================================================

Fresh, from-scratch verifier for the PARITY REPAIR lemma of
research/ksum/paper/revision_k3.tex  (labelled Lemma [Odd case] = lem:core-odd):

    "Under the hypotheses of Proposition core-even but with the stronger window
     t <= q - 2(k-1)K - 2, adjoin the parked coordinate v = t + (k-1)K + 1,
     giving N = (k-2) + 2m + 1.  Then kSum_{Z_q,t,N}(x) = Claw_{m->K}(f,g) for
     every input."

The author (F1 pass) verified this exhaustively only for k=3..6 and correctly
refused to self-stamp the general-k claim.  This script is written by a FRESH
instance (R3) that did NOT author the lemma.  It shares NO algebra with the
encoders: the k-Sum oracle simply enumerates ALL C(N,k) position subsets and
tests their modular sum, and Claw is computed directly by definition.  The only
"construction" code below is a faithful transcription of the paper's own
build recipe (a-c), which is exactly the object under test.

Contents
--------
  PART A  Arithmetic-threshold audit (symbolic identities, k=3..12, K=2..6)
  PART B  Even-case cross-check (Proposition core-even), k=3..7  -- trust anchor
  PART C  Input-level audit of lem:core-odd, k=3..8  (INCLUDES k=7, k=8 > k=6)
  PART D  Dedicated "no subset containing v ever hits t" assertion, k=3..8
  PART E  Pattern-level audit (exact core sums x full live-sum range), k=3..10
  PART F  Full all-t coverage via the translation identity, k=3,4
  PART G  Negative controls: parked value / window are load-bearing

Every PART prints a PASS/FAIL line; a FAIL sets the global exit flag.  The final
VERDICT line is the machine-checkable summary.

Run:
  python3 ksum/tools/ksum_r3_parity.py
"""

import sys
import math
import itertools
from math import gcd

FAILURES = []           # list of (part, message)
def check(part, cond, msg):
    tag = "PASS" if cond else "FAIL"
    if not cond:
        FAILURES.append((part, msg))
    print(f"  [{tag}] {msg}")
    return cond

# ----------------------------------------------------------------------------
# Independent oracle + direct Claw.  NO shared algebra with the construction.
# ----------------------------------------------------------------------------
def ksum_oracle(x, k, q, t):
    """1 iff SOME size-k subset of positions of x sums to t mod q.  Brute force."""
    tmod = t % q
    for S in itertools.combinations(range(len(x)), k):
        s = 0
        for i in S:
            s += x[i]
        if s % q == tmod:
            return 1
    return 0

def ksum_hits_containing(x, k, q, t, must_index):
    """Return list of hitting k-subsets that CONTAIN position must_index."""
    tmod = t % q
    hits = []
    others = [i for i in range(len(x)) if i != must_index]
    for S in itertools.combinations(others, k - 1):
        s = x[must_index] + sum(x[i] for i in S)
        if s % q == tmod:
            hits.append((must_index,) + S)
    return hits

def claw(f, g):
    """1 iff f(i)=g(j) for some i,j  (direct definition)."""
    gs = set(g)
    return 1 if any(fi in gs for fi in f) else 0

# ----------------------------------------------------------------------------
# Faithful transcription of the paper's build recipe (revision_k3.tex, (a)-(c)).
# core (a): c_i = U (1<=i<=k-3),  c_{k-2} = t-(k-3)U      (k=3 -> single [t])
# live (b): f(1..m) in {1..K}; then (-g(1..m)) mod q
# park (c): v = t + (k-1)K + 1               (odd case only)
# ----------------------------------------------------------------------------
def build_core(k, K, q, t):
    U = k * K + 1
    core = [U] * (k - 3) + [t - (k - 3) * U]      # length k-2 (empty prefix for k=3)
    return [c % q for c in core]

def build_live(K, q, f, g):
    return [fi % q for fi in f] + [(-gj) % q for gj in g]

def build_x_even(k, K, q, t, f, g):
    return build_core(k, K, q, t) + build_live(K, q, f, g)

def build_x_odd(k, K, q, t, f, g, v_override=None):
    U = k * K + 1
    v = (t + (k - 1) * K + 1) if v_override is None else v_override
    x = build_core(k, K, q, t) + build_live(K, q, f, g)
    x.append(v % q)
    return x                     # parked coordinate is the LAST position

def W_even(k, K, q):
    U = k * K + 1
    return ((k - 2) * U, q - U)                 # inclusive [lo, hi]

def W_odd(k, K, q):
    U = k * K + 1
    return ((k - 2) * U, q - 2 * (k - 1) * K - 2)

def all_fg(K, m):
    """All (f,g) in {1..K}^m x {1..K}^m."""
    dom = range(1, K + 1)
    for f in itertools.product(dom, repeat=m):
        for g in itertools.product(dom, repeat=m):
            yield list(f), list(g)

# ============================================================================
# PART A -- arithmetic-threshold audit
# ============================================================================
def part_A():
    print("\n=== PART A: arithmetic-threshold identities (k=3..12, K=2..6) ===")
    ok = True
    for k in range(3, 13):
        for K in range(2, 7):
            U = k * K + 1
            # pick a generic q above the odd threshold so windows are non-empty
            q_odd_thr = (k * k - 2) * K + 2 * k - 1
            q_even_thr = (k - 1) * (k * K + 2)
            for q in (q_odd_thr, q_odd_thr + 1, q_odd_thr + 7, 2 * q_odd_thr):
                lo_e, hi_e = W_even(k, K, q)
                lo_o, hi_o = W_odd(k, K, q)
                len_e = hi_e - lo_e + 1
                len_o = hi_o - lo_o + 1
                # (1) claimed closed form  |W_odd| = q - [(k^2-2)K + 2k-1] + k
                claim_o = q - q_odd_thr + k
                ok &= (len_o == claim_o)
                # (2) |W_even| = q - (k-1)(kK+1) + 1
                ok &= (len_e == q - (k - 1) * (k * K + 1) + 1)
                # (3) threshold equivalences
                ok &= ((len_o >= k) == (q >= q_odd_thr))
                ok &= ((len_e >= k) == (q >= q_even_thr))
                # (4) W_odd subset of W_even  (odd ceiling only tightened)
                ok &= (lo_o == lo_e and hi_o <= hi_e)
                #     equivalently U <= 2(k-1)K + 2
                ok &= (U <= 2 * (k - 1) * K + 2)
                # (5) coverage: gcd(k,q) <= k <= |W_odd| at/above threshold
                if q >= q_odd_thr:
                    ok &= (gcd(k, q) <= k <= len_o)
                # (6) core well-formed: need t >= (k-2)U to have non-empty window;
                #     lo_o = (k-2)U exactly
                ok &= (lo_o == (k - 2) * U)
    check("A", ok, "all threshold identities & inclusions hold for k=3..12, K=2..6")
    # explicit witness of the hand-expansion for one (k,K)
    k, K, q = 5, 3, 200
    lo_o, hi_o = W_odd(k, K, q)
    hand = q - ((k * k - 2) * K + 2 * k - 1) + k
    check("A", (hi_o - lo_o + 1) == hand,
          f"witness k=5,K=3,q=200: |W_odd|={hi_o-lo_o+1} == q-[(k^2-2)K+2k-1]+k={hand}")

# ============================================================================
# PART B -- even-case trust anchor (Proposition core-even)
# ============================================================================
def part_B():
    print("\n=== PART B: even-case cross-check kSum==Claw (Prop core-even), k=3..7 ===")
    # (k, K, m); q at even threshold (covers Prop hypothesis q>=(k-1)(kK+1))
    cases = [(3, 3, 4), (4, 3, 3), (5, 2, 3), (6, 2, 2), (7, 2, 2)]
    total = 0
    for (k, K, m) in cases:
        q = (k - 1) * (k * K + 2)                 # even coverage threshold
        lo, hi = W_even(k, K, q)
        N = (k - 2) + 2 * m
        cnt = 0; bad = 0
        for t in range(lo, hi + 1):
            for f, g in all_fg(K, m):
                x = build_x_even(k, K, q, t, f, g)
                if len(x) != N:
                    bad += 1; continue
                if ksum_oracle(x, k, q, t) != claw(f, g):
                    bad += 1
                cnt += 1
        total += cnt
        check("B", bad == 0,
              f"k={k} K={K} m={m} q={q} N={N}: {cnt} even inputs, {bad} mismatches")
    print(f"  (PART B total even inputs checked: {total})")

# ============================================================================
# PART C -- input-level audit of lem:core-odd, k=3..8  (INCLUDES k=7 and k=8)
# ============================================================================
def part_C():
    print("\n=== PART C: ODD-case input-level kSum==Claw (lem:core-odd), k=3..8 ===")
    # (k, K, m); q at ODD threshold (>= its own hypotheses); sweep ALL t in W_odd
    cases = [(3, 3, 4), (4, 3, 3), (5, 2, 3), (6, 2, 2), (7, 2, 2), (8, 2, 2)]
    total = 0
    for (k, K, m) in cases:
        q = (k * k - 2) * K + 2 * k - 1           # odd coverage threshold
        lo, hi = W_odd(k, K, q)
        N = (k - 2) + 2 * m + 1
        cnt = 0; bad = 0
        for t in range(lo, hi + 1):
            for f, g in all_fg(K, m):
                x = build_x_odd(k, K, q, t, f, g)
                if len(x) != N:
                    bad += 1; continue
                if ksum_oracle(x, k, q, t) != claw(f, g):
                    bad += 1
                cnt += 1
        total += cnt
        beyond = " (>k=6, author did NOT self-stamp)" if k >= 7 else ""
        check("C", bad == 0,
              f"k={k} K={K} m={m} q={q} N={N}: {cnt} odd inputs, {bad} mismatches{beyond}")
    print(f"  (PART C total odd inputs checked: {total})")

# ============================================================================
# PART D -- dedicated "no k-subset containing v ever hits t" over real inputs
# ============================================================================
def part_D():
    print("\n=== PART D: no subset CONTAINING the parked coord v hits t, k=3..8 ===")
    cases = [(3, 3, 3), (4, 3, 3), (5, 2, 3), (6, 2, 2), (7, 2, 2), (8, 2, 2)]
    total = 0
    for (k, K, m) in cases:
        q = (k * k - 2) * K + 2 * k - 1
        lo, hi = W_odd(k, K, q)
        N = (k - 2) + 2 * m + 1
        v_index = N - 1
        leaks = 0; cnt = 0
        for t in range(lo, hi + 1):
            for f, g in all_fg(K, m):
                x = build_x_odd(k, K, q, t, f, g)
                hits = ksum_hits_containing(x, k, q, t, v_index)
                if hits:
                    leaks += 1
                cnt += 1
        total += cnt
        check("D", leaks == 0,
              f"k={k} K={K} m={m} q={q}: {cnt} inputs, {leaks} with a v-containing hit")
    print(f"  (PART D total inputs scanned: {total})")

# ============================================================================
# PART E -- pattern-level audit: exact core sums x full live-sum range, k=3..10
#           Verifies the proof's W-interval  W in [1, q-1]  for ALL patterns
#           (v with a frozen + (k-1-a) live, every integer live sum in [-lK,lK]).
# ============================================================================
def part_E():
    print("\n=== PART E: pattern-level W in [1,q-1] over ALL v-patterns, k=3..10 ===")
    for k in range(3, 11):
        K = 2
        q = (k * k - 2) * K + 2 * k - 1
        lo, hi = W_odd(k, K, q)
        allpass = True
        Wmin_glob, Wmax_glob = None, None
        proof_hi_ok = True
        for t in (lo, (lo + hi) // 2, hi):        # low / mid / high in-window t
            core = build_core(k, K, q, t)          # exact core values (integers)
            idx = list(range(len(core)))
            for r in range(len(idx) + 1):          # a = |A| = 0..k-2
                for A in itertools.combinations(idx, r):
                    sumA = sum(core[i] for i in A)
                    a = r
                    ell = (k - 1) - a               # live count (>=1 since a<=k-2)
                    if ell < 1:
                        allpass = False
                        continue
                    lo_s, hi_s = -ell * K, ell * K
                    for s in range(lo_s, hi_s + 1):
                        W = (k - 1) * K + 1 + sumA + s
                        if not (1 <= W <= q - 1):
                            allpass = False
                        Wmin_glob = W if Wmin_glob is None else min(Wmin_glob, W)
                        Wmax_glob = W if Wmax_glob is None else max(Wmax_glob, W)
                    # proof's own claimed envelope  W in [1, t+2(k-1)K+1]
                    if not (t + 2 * (k - 1) * K + 1 <= q - 1):
                        proof_hi_ok = False
        beyond = " (>k=6)" if k >= 7 else ""
        check("E", allpass,
              f"k={k} K={K} q={q}: all v-pattern W in [{Wmin_glob},{Wmax_glob}] subset [1,{q-1}]{beyond}")
        check("E", proof_hi_ok,
              f"k={k}: proof envelope hi t+2(k-1)K+1 <= q-1 at all in-window t")

# ============================================================================
# PART F -- full all-t coverage via translation identity, k=3,4
#   For every target t* in Z_q we pick a with t*+k*a in W_odd, build the
#   in-window instance for target (t*+k*a), then translate x -> x - a*1 and
#   check kSum_{t*}(x - a1) == Claw.  This exercises lem:transl-cover end to end.
# ============================================================================
def part_F():
    print("\n=== PART F: full Z_q target coverage via translation, k=3,4 ===")
    cases = [(3, 3, 3), (4, 2, 3)]
    for (k, K, m) in cases:
        q = (k * k - 2) * K + 2 * k - 1
        lo, hi = W_odd(k, K, q)
        window = list(range(lo, hi + 1))
        N = (k - 2) + 2 * m + 1
        cnt = 0; bad = 0; uncovered = 0
        # test a representative but exhaustive-in-t sweep with a small (f,g) sample
        fg_sample = list(itertools.islice(all_fg(K, m), 0, None, max(1, (K**(2*m))//8)))
        for tstar in range(q):
            # find a in [0,q) with (tstar + k*a) mod q in window
            a_found = None
            for a in range(q):
                if ((tstar + k * a) % q) in window:
                    a_found = a; break
            if a_found is None:
                uncovered += 1
                continue
            tin = (tstar + k * a_found) % q
            for f, g in fg_sample:
                x = build_x_odd(k, K, q, tin, f, g)
                xt = [(xi - a_found) % q for xi in x]     # translate by -a*1
                if ksum_oracle(xt, k, q, tstar) != claw(f, g):
                    bad += 1
                cnt += 1
        check("F", uncovered == 0,
              f"k={k} q={q}: every one of {q} targets t* reachable into W_odd (uncovered={uncovered})")
        check("F", bad == 0,
              f"k={k} q={q}: {cnt} translated instances, {bad} mismatches over full Z_q")

# ============================================================================
# PART G -- negative controls (the construction's choices are load-bearing)
# ============================================================================
def part_G():
    print("\n=== PART G: negative controls -- parked value & window are load-bearing ===")

    # G1 (robust): the safe parked value is v = t+(k-1)K+1, the FIRST value above
    #     the reachable band.  Any wrong placement v' strictly below it, in
    #     [t-kK, t+(k-1)K], leaks for SOME no-claw input.  (A single fixed offset
    #     need NOT leak -- e.g. v'=t+1 needs live-sum -1, unreachable over {1,2}
    #     without a claw -- so we scan the band and demand at least one leak.)
    print("  -- G1: some wrong parked placement v' in [t-kK, safe-1] leaks --")
    for (k, K, m) in [(3, 3, 3), (4, 2, 3), (5, 2, 3)]:
        q = (k * k - 2) * K + 2 * k - 1
        lo, hi = W_odd(k, K, q)
        t = lo
        safe_v = t + (k - 1) * K + 1
        found = None
        for vp in range(t - k * K, safe_v):        # every wrong placement up to safe-1
            for f, g in all_fg(K, m):
                if claw(f, g):
                    continue
                x = build_x_odd(k, K, q, t, f, g, v_override=vp)
                if ksum_hits_containing(x, k, q, t, len(x) - 1):
                    found = (vp, vp - t)
                    break
            if found:
                break
        check("G", found is not None,
              f"k={k}: wrong placement leaks (witness v'-t={found[1] if found else None}) -> v placement load-bearing")

    # G1-tight: the "+1" in v=t+(k-1)K+1 is EXACTLY tight.  Placing v'=t+(k-1)K
    #     (one below safe) leaks whenever m>=k-1: the no-claw input f=1,g=K has a
    #     block of (-K)'s; picking k-1 of them gives live-sum -(k-1)K, and
    #     v' + -(k-1)K = t.  Confirms the margin cannot be shrunk by 1.
    print("  -- G1-tight: v'=t+(k-1)K (safe-1) leaks when m>=k-1 -> +1 margin is tight --")
    for (k, K, m) in [(3, 2, 2), (4, 2, 3)]:                  # m >= k-1
        q = (k * k - 2) * K + 2 * k - 1
        lo, hi = W_odd(k, K, q)
        t = lo
        vp = t + (k - 1) * K                                   # safe minus 1
        f = [1] * m
        g = [K] * m                                           # no claw (K>=2)
        x = build_x_odd(k, K, q, t, f, g, v_override=vp)
        leaks = bool(ksum_hits_containing(x, k, q, t, len(x) - 1))
        check("G", leaks,
              f"k={k}: v'=t+(k-1)K leaks on (f=1,g=K) -> safe threshold +1 is tight")

    # G2: correct v but target pushed OUTSIDE W_odd (high side); confirm a real
    #     v-subset can then reach t for a no-claw input -> window is load-bearing.
    print("  -- G2: target pushed past W_odd until a real v-subset can reach t --")
    for (k, K, m) in [(3, 3, 4), (4, 2, 3)]:
        q = (k * k - 2) * K + 2 * k - 1
        lo, hi = W_odd(k, K, q)
        exposed_at = None
        for t in range(hi + 1, q):                            # strictly outside the window
            found = False
            for f, g in all_fg(K, m):
                if claw(f, g):
                    continue
                x = build_x_odd(k, K, q, t, f, g)             # correct v = t+(k-1)K+1
                if ksum_hits_containing(x, k, q, t, len(x) - 1):
                    found = True
                    break
            if found:
                exposed_at = t
                break
        check("G", exposed_at is not None,
              f"k={k}: beyond W_odd a v-subset leaks (first at t={exposed_at}, hi_W_odd={hi}) -> window load-bearing")

    # G3: sanity -- INSIDE the window with correct v, NO no-claw input leaks
    #     through v (mirror of PART D, kept as an explicit control).
    print("  -- G3: inside W_odd with correct v, no-claw inputs never leak through v --")
    for (k, K, m) in [(3, 3, 3), (6, 2, 2), (7, 2, 2)]:
        q = (k * k - 2) * K + 2 * k - 1
        lo, hi = W_odd(k, K, q)
        leak = 0
        cnt = 0
        for t in range(lo, hi + 1):
            for f, g in all_fg(K, m):
                if claw(f, g):
                    continue
                x = build_x_odd(k, K, q, t, f, g)
                if ksum_hits_containing(x, k, q, t, len(x) - 1):
                    leak += 1
                cnt += 1
        check("G", leak == 0,
              f"k={k}: {cnt} no-claw inputs in-window, {leak} leaks through v")

# ============================================================================
def main():
    print("=" * 76)
    print("R3 finite parity-repair checks")
    print("target: the odd-length inherited-floor construction recorded by KSUM.A1f")
    print("original independent audit: 2026-07-18; this execution is a rerun, not a new review")
    print("oracle: brute-force over all C(N,k) subsets; shares no algebra w/ encoders")
    print(f"python: {sys.version.split()[0]}")
    print("=" * 76)
    part_A()
    part_B()
    part_C()
    part_D()
    part_E()
    part_F()
    part_G()
    print("\n" + "=" * 76)
    if FAILURES:
        print(f"VERDICT: DEFECT -- {len(FAILURES)} check(s) failed:")
        for part, msg in FAILURES:
            print(f"   [{part}] {msg}")
        print("=" * 76)
        sys.exit(1)
    else:
        print("VERDICT: PASS -- the parity-repair claim holds on every checked instance.")
        print("  * arithmetic thresholds & window inclusions: identities confirmed k=3..12")
        print("  * even-case anchor kSum==Claw: confirmed k=3..7")
        print("  * ODD-case kSum==Claw (the lemma): confirmed k=3..8 (incl. k=7,8 > k=6)")
        print("  * no k-subset containing v ever hits t: confirmed k=3..8 (input-level)")
        print("  * pattern-level W in [1,q-1] over all v-patterns: confirmed k=3..10")
        print("  * full Z_q coverage via translation: confirmed k=3,4")
        print("  * negative controls (v placement & window load-bearing): confirmed")
        print("=" * 76)
        sys.exit(0)

if __name__ == "__main__":
    main()
