"""F1 INDEPENDENT hostile audit of the k>=3 inherited-floor reduction (Lemma W3E-1).

Third-attempt auditor (Opus 4.8), OWN code, OWN derivations. Treats the W3E artifact
and the R1 attempt-2 scripts as UNTRUSTED and re-implements from scratch.

Two constructions are checked, because the audit must (a) validate W3E-1 AS AUTHORED and
(b) validate the cleaner variant that will go into the revised inherited-floor construction:

  FREEZE  (W3E-1 as authored): freeze k-2 coords to the CONSTANT C0 = floor(q/(k-1)),
          induced target t0 = (k-2)*C0; live part = even 2m claw window.
          All-t via a one-coordinate delta-shift window + the translation identity.

  CORE    (cleaner, general-k): freeze k-2 coords to a POSITIVE core
          c_1..c_{k-3} = U := kK+1,  c_{k-2} = tstar - (k-3)U   (so sum(core)=tstar,
          every nonempty subset sum in [U, tstar]); live part = even 2m claw window.
          Odd live count handled by ONE parked coordinate v* = tstar + (k-1)K + 1.
          Window of realizable targets tstar:
             even N-(k-2):  tstar in [ (k-2)(kK+1),  q - kK - 1 ]
             odd  N-(k-2):  tstar in [ (k-2)(kK+1),  q - 2(k-1)K - 2 ]
          All-t via the translation identity k-Sum_t(x)=k-Sum_{t+k a}(x+a*1).

GROUND TRUTH: k-Sum is evaluated from scratch over ALL C(N,k) position subsets
(itertools.combinations); Claw(f,g) := exists i,j f(i)=g(j) computed directly from the
live functions. The checker shares NO algebra with the constructions.

Attack points explicitly exercised (per the audit mandate):
  * all-t coverage incl. gcd(k,q)>1 (k=4 even q -> g=2; k=6 -> g in {2,3,6}; k=5,q=55 -> g=5)
  * k=5 odd padding (the parked coordinate), which W3E left unwritten for k>=5
  * every bad block/live pattern class (full enumeration is implicit in the from-scratch oracle)
  * wraparound control (large K vs q, boundary q)
  * exact thresholds (negative controls at/just outside the window)

Run: python3 ksum/tools/ksum_f1_floor.py
Output is stdout by default; --output <new-file> saves an additional log.
A rerun checks the recorded finite cases; it is not a new independent review.
"""
import itertools, json, os, sys, time, math, hashlib, random
import argparse
from datetime import datetime, timezone
from pathlib import Path

# Importing this module never creates or truncates a log.
LOG = None
LOGPATH = None

def log(msg):
    print(msg)
    if LOG is not None:
        LOG.write(msg + "\n"); LOG.flush()

# ---------- ground-truth oracle (shares nothing with the constructions) ----------
def ksum_hit(x, q, t, k):
    """True iff some k of the N positions sum to t (mod q). From scratch."""
    return any(sum(sub) % q == t % q for sub in itertools.combinations(x, k))

def claw(f, g):
    fs = set(f)
    return any(gj in fs for gj in g)

def dist0(a, q):
    a %= q
    return min(a, q - a)

# ---------- FREEZE construction (W3E-1 as authored) ----------
def C0_of(q, k):
    return q // (k - 1)

def build_freeze(k, K, q, delta, f, g):
    """k-2 frozen coords: (k-3) copies of C0, one copy of C0+delta. Live = f then -g.
    Induced target is t = t0 + delta with t0 = (k-2)C0."""
    C0 = C0_of(q, k)
    frozen = [C0] * (k - 3) + [(C0 + delta) % q]      # k-2 coords total
    live = [v % q for v in f] + [(q - v) % q for v in g]
    return [c % q for c in frozen] + live

def freeze_target(k, K, q, delta):
    C0 = C0_of(q, k)
    return ((k - 2) * C0 + delta) % q

# ---------- CORE construction (the revised inherited-floor construction) ----------
def build_core_even(k, K, q, tstar, f, g):
    U = k * K + 1
    core = [U] * (k - 3) + [tstar - (k - 3) * U]       # sum = tstar
    live = [v % q for v in f] + [(q - v) % q for v in g]
    return [c % q for c in core] + live

def build_core_odd(k, K, q, tstar, f, g, vstar=None):
    U = k * K + 1
    if vstar is None:
        vstar = tstar + (k - 1) * K + 1
    core = [U] * (k - 3) + [tstar - (k - 3) * U]
    live = [v % q for v in f] + [(q - v) % q for v in g]
    return [c % q for c in core] + [vstar % q] + live

def win_core_even(k, K, q):
    return (k - 2) * (k * K + 1), q - k * K - 1        # [lo, hi] inclusive
def win_core_odd(k, K, q):
    return (k - 2) * (k * K + 1), q - 2 * (k - 1) * K - 2
def thr_core_even(k, K):
    return (k - 1) * (k * K + 2)
def thr_core_odd(k, K):
    return (k * k - 2) * K + 2 * k - 1

# ---------- exhaustive input sweep ----------
def sweep(name, k, q, t, N, builder, m, expect_mismatch=False, cap=3):
    t0 = time.time(); n_in = 0; miss = []
    K = builder_K                       # window size, set by caller before each sweep
    for f in itertools.product(range(1, K + 1), repeat=m):
        for g in itertools.product(range(1, K + 1), repeat=m):
            x = builder(f, g)
            assert len(x) == N, (name, len(x), N)
            h = ksum_hit(x, q, t, k)
            c = claw(f, g)
            n_in += 1
            if h != c:
                if len(miss) < cap:
                    miss.append({"f": list(f), "g": list(g), "x": x, "hit": h, "claw": c})
                if not expect_mismatch and len(miss) >= cap:
                    break
        else:
            continue
        break
    ok = (len(miss) == 0) != expect_mismatch
    log(json.dumps({"cfg": name, "k": k, "q": q, "t": t % q, "N": N, "m": m,
                    "inputs": n_in, "mism": len(miss), "expect_mismatch": expect_mismatch,
                    "verdict": "PASS" if ok else "FAIL", "s": round(time.time() - t0, 2)}))
    for w in miss[:cap]:
        log("  witness " + json.dumps(w))
    return ok, n_in

# global K passed to sweep via closure variable
builder_K = None

def main():
    global builder_K, LOG, LOGPATH
    parser = argparse.ArgumentParser(description="Rerun the finite F1 floor checks.")
    parser.add_argument("--output", type=Path, help="Optional new log; existing files are never overwritten.")
    args = parser.parse_args()
    LOGPATH = args.output
    if LOGPATH is not None:
        LOGPATH.parent.mkdir(parents=True, exist_ok=True)
        try:
            LOG = LOGPATH.open("x", encoding="utf-8")
        except FileExistsError:
            parser.error(f"refusing to overwrite {LOGPATH}")
    log("# Finite F1 floor rerun; original independent audit dated 2026-07-18")
    log("# run_utc: " + datetime.now(timezone.utc).isoformat())
    log("# cmd: " + " ".join(sys.argv))
    ok_all = True; total = 0

    # ===================================================================
    # PART A: CORE construction, EVEN live count, sweep ALL in-window tstar
    # ===================================================================
    log("## A. CORE even: all in-window tstar, all live inputs, from-scratch oracle")
    for (k, K, q, m) in [(3,2,16,2),(3,2,21,3),(3,3,24,2),(4,2,30,2),(4,2,34,3),
                         (5,2,48,3),(5,2,55,3),(5,3,80,3),(6,2,65,3)]:
        lo, hi = win_core_even(k, K, q)
        assert hi >= lo, ("empty even window", k, K, q, lo, hi)  # q >= (k-1)(kK+1)
        builder_K = K
        cnt = 0
        for tstar in range(lo, hi + 1):
            N = (k - 2) + 2 * m
            b = (lambda f, g, k=k, K=K, q=q, tstar=tstar: build_core_even(k, K, q, tstar, f, g))
            okc, ni = sweep(f"Aeven_k{k}_K{K}_q{q}_t{tstar}", k, q, tstar % q, N, b, m)
            ok_all &= okc; total += ni; cnt += 1
        log(json.dumps({"summ_A": f"k{k}_K{K}_q{q}", "window": [lo, hi], "targets": cnt}))

    # ===================================================================
    # PART B: CORE construction, ODD live count (parked v*), incl. k=5
    # ===================================================================
    log("## B. CORE odd (parked v*): all in-window tstar, all live inputs; k=3,4,5")
    for (k, K, q, m) in [(3,2,19,2),(3,2,24,3),(4,2,35,2),(4,2,44,3),
                         (5,2,55,3),(5,2,60,3),(5,3,90,3),(6,2,75,3)]:
        lo, hi = win_core_odd(k, K, q)
        assert hi >= lo, ("empty odd window", k, K, q, lo, hi)
        builder_K = K
        cnt = 0
        for tstar in range(lo, hi + 1):
            N = (k - 2) + 2 * m + 1     # one parked coordinate
            b = (lambda f, g, k=k, K=K, q=q, tstar=tstar: build_core_odd(k, K, q, tstar, f, g))
            okc, ni = sweep(f"Bodd_k{k}_K{K}_q{q}_t{tstar}", k, q, tstar % q, N, b, m)
            ok_all &= okc; total += ni; cnt += 1
        log(json.dumps({"summ_B": f"k{k}_K{K}_q{q}", "window": [lo, hi], "targets": cnt}))

    # ===================================================================
    # PART C: ALL-t coverage via translation. FULL Z_q sweep. gcd stressed.
    # ===================================================================
    log("## C. ALL-t via translation identity: full Z_q sweep; gcd(k,q) stressed")
    def all_t(tag, k, K, q, parity, m):
        globals()["builder_K"] = K
        lo, hi = (win_core_even(k, K, q) if parity == "even" else win_core_odd(k, K, q))
        g = math.gcd(k, q)
        wlen = hi - lo + 1
        ok = True; tot = 0; uncovered = []
        for t in range(q):
            a = None
            for aa in range(q):
                if lo <= (t + k * aa) % q <= hi:
                    a = aa; break
            if a is None:
                uncovered.append(t); ok = False; continue
            tstar = (t + k * a) % q
            if parity == "even":
                base = lambda f, gg, k=k, K=K, q=q, tstar=tstar: build_core_even(k, K, q, tstar, f, gg)
                N = (k - 2) + 2 * m
            else:
                base = lambda f, gg, k=k, K=K, q=q, tstar=tstar: build_core_odd(k, K, q, tstar, f, gg)
                N = (k - 2) + 2 * m + 1
            # realise target t: shift EVERY coordinate down by a  (x -> x - a*1)
            b = lambda f, gg, a=a, base=base, q=q: [(v - a) % q for v in base(f, gg)]
            okc, ni = sweep(f"{tag}_t{t}", k, q, t, N, b, m)
            ok &= okc; tot += ni
        log(json.dumps({"summ_C": tag, "q": q, "gcd_k_q": g, "window_len": wlen,
                        "len_ge_gcd": wlen >= g, "uncovered_t": uncovered,
                        "verdict": "PASS" if ok and not uncovered else "FAIL"}))
        return ok and not uncovered, tot
    for (k, K, q, par, m) in [(3,2,16,"even",2),(3,2,19,"odd",2),
                              (4,3,52,"even",2),(4,2,44,"odd",3),   # k=4 even q: g=2 and g=4
                              (4,2,40,"even",2),                     # g=gcd(4,40)=4
                              (5,2,55,"odd",3),                      # g=gcd(5,55)=5
                              (6,2,72,"even",3)]:                    # g=gcd(6,72)=6 (worst), q>=thr=70
        okc, tot = all_t(f"ALLT_k{k}_K{K}_q{q}_{par}", k, K, q, par, m)
        ok_all &= okc; total += tot
    # Informational: BELOW the all-t threshold, coverage MUST be partial (threshold load-bearing)
    globals()["builder_K"] = 2
    lo6, hi6 = win_core_even(6, 2, 66)
    covered = sum(1 for t in range(66) if any(lo6 <= (t + 6*a) % 66 <= hi6 for a in range(66)))
    log(json.dumps({"below_thr_demo": "k6_K2_q66", "window": [lo6, hi6],
                    "window_len": hi6 - lo6 + 1, "gcd_k_q": math.gcd(6, 66),
                    "targets_covered": covered, "of_q": 66,
                    "note": "partial coverage EXPECTED below thr=70; confirms gcd threshold is real"}))

    # ===================================================================
    # PART D: FREEZE construction (W3E-1 as authored) -- reduction identity
    #          + delta-window target coverage.  Independent re-check.
    # ===================================================================
    log("## D. FREEZE (W3E-1 as authored): reduction identity + delta-window coverage")
    for (k, K, q, m) in [(3,2,14,2),(3,3,20,3),(4,2,27,2),(4,2,30,3),(5,2,44,3),(6,2,65,3)]:
        C0 = C0_of(q, k)
        assert q >= (k - 1) * (k * K + 1), (k, K, q)
        Delta = C0 - k * K - 1
        builder_K = K
        # sweep delta over the whole admissible window
        cnt = 0
        for delta in range(-Delta, Delta + 1):
            t = freeze_target(k, K, q, delta)
            N = (k - 2) + 2 * m
            b = lambda f, g, k=k, K=K, q=q, delta=delta: build_freeze(k, K, q, delta, f, g)
            okc, ni = sweep(f"Dfrz_k{k}_K{K}_q{q}_d{delta}", k, q, t, N, b, m)
            ok_all &= okc; total += ni; cnt += 1
        log(json.dumps({"summ_D": f"k{k}_K{K}_q{q}", "C0": C0, "Delta": Delta,
                        "deltas_swept": cnt, "t0": freeze_target(k, K, q, 0)}))

    # ===================================================================
    # PART E: NEGATIVE CONTROLS -- the windows are load-bearing
    # ===================================================================
    log("## E. Negative controls (expect_mismatch=True): reduction MUST break")
    # E1: the ALL-LIVE boundary is load-bearing. At target t=kK (dist_q=kK), the all-live
    #     k-subset of f-side K's sums to kK with NO claw. Works for EVERY k (pure-live, no core).
    #     This is the constraint dist_q(t,0) > kK that pins the window; verified non-vacuous.
    for (k, K, q) in [(3,2,21),(4,2,34),(5,2,55),(6,2,70)]:
        m = k                                 # need >=k same-sign live coords
        N = 2 * m
        t = k * K                             # exactly the boundary, in the danger zone
        builder_K = K
        # f = all K's (positive side), g = all 1's (so no claw since K>=2 != 1)
        b = lambda f, g, k=k, K=K, q=q: ([K] * m + [(q - 1) % q] * m)  # ignores f,g; fixed witness family
        # but sweep varies f,g; instead do a direct one-shot check:
        x = [K] * m + [(q - 1) % q] * m
        hit = ksum_hit(x, q, t, k); cl = claw((K,) * m, (1,) * m)
        okc = (hit and not cl)
        log(json.dumps({"cfg": f"NEGalllive_k{k}_K{K}_q{q}_t{t}", "x_head": x[:k+1],
                        "target": t, "hit": hit, "claw": cl,
                        "verdict": "PASS" if okc else "FAIL",
                        "note": "all-live no-claw hit at boundary t=kK -> window must exclude it"}))
        ok_all &= okc; total += 1
    # E3: CORE odd, MISPLACED parked v* inside the danger zone (v*=K) -> breaks
    for (k, K, q) in [(3,2,24),(5,2,60)]:
        lo, hi = win_core_odd(k, K, q); tstar = lo + 1
        m = 2
        N = (k - 2) + 2 * m + 1
        builder_K = K
        b = lambda f, g, k=k, K=K, q=q, tstar=tstar: build_core_odd(k, K, q, tstar, f, g, vstar=K)
        okc, ni = sweep(f"NEGvstar_k{k}_K{K}_q{q}", k, q, tstar % q, N, b, m,
                        expect_mismatch=True)
        ok_all &= okc; total += ni

    # ===================================================================
    # PART F: WRAPAROUND / boundary stress -- q exactly at even-threshold,
    #          and the naive over-freeze pathology (documents WHY padding is subtle)
    # ===================================================================
    log("## F. wraparound + boundary + the over-freeze pathology")
    for (k, K) in [(3,2),(4,2),(5,2),(6,2),(4,3)]:
        q = thr_core_even(k, K)
        lo, hi = win_core_even(k, K, q)
        g = math.gcd(k, q)
        log(json.dumps({"boundary_even_thr": True, "k": k, "K": K, "q": q,
                        "window": [lo, hi], "window_len": hi - lo + 1,
                        "gcd_k_q": g, "len_ge_gcd": (hi - lo + 1) >= g}))
    # Over-freeze pathology: adding EXTRA C0-constants (naive W3E padding) can create a hit.
    # Demonstrates the k>=5 gap in W3E-1's padding; the CORE construction avoids it (no extra
    # constants: only ONE parked v*).  Here we exhibit the failure for k=3, q=24 (C0=12):
    k, K, q = 3, 2, 24
    C0 = C0_of(q, k); t0 = (k - 2) * C0 % q
    over = [C0, C0, C0]                       # three C0's: a k=3 subset of frozen pads
    hit = (3 * C0) % q == t0
    log(json.dumps({"overfreeze_pathology": True, "k": k, "q": q, "C0": C0, "t0": t0,
                    "three_C0_sum_mod_q": (3 * C0) % q, "spurious_hit": hit,
                    "note": "naive pad-with-C0 self-hits; CORE avoids it"}))

    log(f"# TOTAL inputs checked: {total}")
    log(f"# OVERALL: {'ALL PASS' if ok_all else 'FAILURES PRESENT'}")
    if LOG is not None:
        LOG.close()
        LOG = None

    def sha(p):
        h = hashlib.sha256()
        with open(p, "rb") as fh:
            h.update(fh.read())
        return h.hexdigest()
    print("SHA256 script:", sha(os.path.abspath(__file__)))
    if LOGPATH is not None:
        print("SHA256 log   :", sha(LOGPATH))
    sys.exit(0 if ok_all else 1)

if __name__ == "__main__":
    main()
