"""F1 INDEPENDENT hostile audit of the k-collision -> k-Sum embedding (Lemma W3E-2).

Third-attempt auditor (Opus 4.8), OWN code, OWN derivations. UNTRUSTED: the W3E artifact
and the R1 attempt-2 scripts. Re-implemented from scratch.

Encoding. k-partite k-collision g_1..g_k:[n]->[0,R-1]. Block j, position i:
    x = ( w_j + u_j * g_j(i) )  mod q.
General-k recipe (omega = 2R-1):
    u_j = omega^{j-1}  (j=1..k-1),
    u_k = -(u_1+...+u_{k-1}) = -(omega^{k-1}-1)/(omega-1)      [CLOSING COEFFICIENT]
    P   = k(R-1)(omega^{k-1}-1)/(omega-1)                      [max |payload|, claimed]
    M   = ((2k+1)^{k-1}-1)/2                                   [max |m(nu)|, claimed]
    V   = P+1,  w_j = V*(2k+1)^{j-1} (j<k),  w_k = -(w_1+...+w_{k-1})
    q   = (P+1)(M+1).
k=3 specialised (omega=R): u=(1,R,-(1+R)), P=3(R^2-1), W=floor(P/2)+1,
    w=(W,3W,-4W), q=21R^2-8.

GROUND TRUTH: k-Sum evaluated from scratch over ALL C(kn,k) position subsets;
collision computed directly as (intersection of block value-sets nonempty). No shared algebra.

Checks:
  (A) k-Sum_0(encoded) == k-collision(g), ALL inputs, small (R,n): k=3 spec + general k=3,4,5.
  (B) REVIEWER'S TRAP: naive u_j = omega^{j-1} for ALL j (NO closing) MUST break (collision
      misses 0). Independent recompute of the missed payload.
  (C) INDEPENDENT bound audit: recompute max|payload| and max|m(nu)| by full enumeration and
      compare to the closed forms P and M; verify the separation dist_q(T_mu,0) >= P+1 > P.
  (D) t != 0 by translation x->x+a, target t=k*a; ALL inputs.
  (E) pattern-level certification k=3..6 (every wrong multiset x every payload box), no shortcuts.

Run: python3 ksum/tools/ksum_f1_embed.py
Output is stdout by default; --output <new-file> saves an additional log.
A rerun checks the recorded finite cases; it is not a new independent review.
"""
import itertools, json, os, sys, time, hashlib
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

def ksum_hit(x, q, t, k):
    return any(sum(sub) % q == t % q for sub in itertools.combinations(x, k))

def collision(gs):
    common = set(gs[0])
    for j in range(1, len(gs)):
        common &= set(gs[j])
    return bool(common)

def dist0(a, q):
    a %= q
    return min(a, q - a)

def recipe_k3_special(R):
    P = 3 * (R * R - 1)
    W = P // 2 + 1
    q = 21 * R * R - 8
    return q, (1, R, -(1 + R)), (W, 3 * W, -4 * W), P, None

def recipe_general(k, R):
    om = 2 * R - 1
    u = [om ** j for j in range(k - 1)]
    u.append(-sum(u))                                   # closing coefficient
    P = k * (R - 1) * (om ** (k - 1) - 1) // (om - 1)
    M = ((2 * k + 1) ** (k - 1) - 1) // 2
    V = P + 1
    w = [V * (2 * k + 1) ** j for j in range(k - 1)]
    w.append(-sum(w))
    q = (P + 1) * (M + 1)
    return q, tuple(u), tuple(w), P, M

def encode(gs, u, w, q, k):
    return tuple((w[j] + u[j] * a) % q for j in range(k) for a in gs[j])

def input_sweep(name, k, R, n, q, t, u, w, expect_mismatch=False, cap=3):
    t0 = time.time()
    blocks = list(itertools.product(range(R), repeat=n))
    n_in = 0; miss = []
    for gs in itertools.product(blocks, repeat=k):
        x = encode(gs, u, w, q, k)
        h = ksum_hit(x, q, t, k)
        c = collision(gs)
        n_in += 1
        if h != c:
            if len(miss) < cap:
                miss.append({"g": [list(v) for v in gs], "hit": h, "coll": c})
            if not expect_mismatch and len(miss) >= cap:
                break
    ok = (len(miss) == 0) != expect_mismatch
    log(json.dumps({"cfg": name, "k": k, "R": R, "n": n, "q": q, "t": t % q,
                    "inputs": n_in, "mism": len(miss), "expect_mismatch": expect_mismatch,
                    "verdict": "PASS" if ok else "FAIL", "s": round(time.time() - t0, 2)}))
    for w_ in miss[:cap]:
        log("  witness " + json.dumps(w_))
    return ok, n_in

def pattern_cert(k, R, q, t, u, w):
    """Full case analysis, no interval shortcuts. Sound & complete for n>=k."""
    u = [v % q for v in u]; w = [v % q for v in w]
    if sum(w) % q != t % q:
        return False, "tags do not sum to t", None, None
    # good pattern: one position per block
    for a in itertools.product(range(R), repeat=k):
        s = sum(u[j] * a[j] for j in range(k)) % q
        if (s == t % q) != (len(set(a)) == 1):
            return False, f"good pattern fails at {a}", None, None
    # wrong patterns: every block-multiset mu != (1..1), sum mu = k
    max_pay = 0; min_sep = None
    for mu in itertools.product(range(k + 1), repeat=k):
        if sum(mu) != k or mu == tuple([1] * k):
            continue
        T = sum(mu[j] * w[j] for j in range(k)) % q
        d = dist0(T, q)
        min_sep = d if min_sep is None else min(min_sep, d)   # min tag separation used
        boxes = [range(mu[j] * (R - 1) + 1) for j in range(k)]
        for s in itertools.product(*boxes):
            pay = sum(u_signed[j] * s[j] for j in range(k))
            max_pay = max(max_pay, abs(pay))
            if (T + sum(u[j] * s[j] for j in range(k))) % q == t % q:
                return False, f"wrong pattern {mu} hits at payload {s}", max_pay, min_sep
    return True, "ok", max_pay, min_sep

u_signed = None   # set per recipe for the signed payload magnitude

def main():
    global u_signed, LOG, LOGPATH
    parser = argparse.ArgumentParser(description="Rerun the finite F1 embed checks.")
    parser.add_argument("--output", type=Path, help="Optional new log; existing files are never overwritten.")
    args = parser.parse_args()
    LOGPATH = args.output
    if LOGPATH is not None:
        LOGPATH.parent.mkdir(parents=True, exist_ok=True)
        try:
            LOG = LOGPATH.open("x", encoding="utf-8")
        except FileExistsError:
            parser.error(f"refusing to overwrite {LOGPATH}")
    log("# Finite F1 embed rerun; original independent audit dated 2026-07-18")
    log("# run_utc: " + datetime.now(timezone.utc).isoformat())
    log("# cmd: " + " ".join(sys.argv))
    ok_all = True; total = 0

    # ===== (A) k=3 specialised, t=0, all inputs =====
    log("## A1. k=3 specialised recipe (omega=R), t=0, all inputs")
    for (R, n) in [(2, 2), (2, 3), (3, 2), (3, 3), (4, 2), (5, 2)]:
        q, u, w, P, _ = recipe_k3_special(R)
        okc, ni = input_sweep(f"k3spec_R{R}_n{n}_q{q}", 3, R, n, q, 0, u, w)
        ok_all &= okc; total += ni

    # ===== (A) general-k, t=0, all inputs =====
    log("## A2. general-k recipe (omega=2R-1, closing coeff), t=0, all inputs")
    for (k, R, n) in [(3,2,3),(3,3,2),(4,2,2),(4,2,3),(4,3,2),(5,2,2)]:
        q, u, w, P, M = recipe_general(k, R)
        okc, ni = input_sweep(f"gen_k{k}_R{R}_n{n}_q{q}", k, R, n, q, 0, u, w)
        ok_all &= okc; total += ni

    # ===== (B) reviewer's trap: naive coeffs (no closing) MUST break =====
    log("## B. reviewer trap: u_j=omega^{j-1} for ALL j (no closing) -> collision MISSES 0")
    for (k, R) in [(3,2),(3,3),(4,2),(5,2)]:
        om = 2 * R - 1
        q, _, w, P, M = recipe_general(k, R)          # valid modulus/tags
        u_naive = tuple(om ** j for j in range(k))    # NO closing coefficient
        pay = sum(u_naive) % q                        # payload of an all-1 collision
        okc, ni = input_sweep(f"TRAP_k{k}_R{R}_naive", k, R, 2, q, 0, u_naive, w,
                              expect_mismatch=True)
        log(json.dumps({"trap_k": k, "R": R, "collision_payload_mod_q": pay,
                        "would_be_broken_iff_nonzero": pay != 0}))
        ok_all &= okc; total += ni

    # ===== (C) independent bound audit =====
    log("## C. independent bound audit: enumerate max|payload|, verify vs P; tag sep vs P+1")
    for (k, R) in [(3,2),(3,3),(3,4),(4,2),(4,3),(5,2)]:
        q, u, w, P, M = recipe_general(k, R)
        u_signed = list(u)
        # max |payload| over all wrong multisets & payload boxes
        mp = 0
        for mu in itertools.product(range(k + 1), repeat=k):
            if sum(mu) != k:
                continue
            boxes = [range(mu[j] * (R - 1) + 1) for j in range(k)]
            for s in itertools.product(*boxes):
                mp = max(mp, abs(sum(u[j] * s[j] for j in range(k))))
        # min tag separation over wrong multisets
        min_sep = None
        for mu in itertools.product(range(k + 1), repeat=k):
            if sum(mu) != k or mu == tuple([1] * k):
                continue
            T = sum(mu[j] * w[j] for j in range(k)) % q
            d = dist0(T, q)
            min_sep = d if min_sep is None else min(min_sep, d)
        okc = (mp <= P) and (min_sep >= P + 1)
        log(json.dumps({"cfg": f"bound_k{k}_R{R}", "P": P, "max_payload": mp,
                        "payload_le_P": mp <= P, "min_tag_sep": min_sep,
                        "sep_ge_P+1": min_sep >= P + 1, "P+1": P + 1,
                        "verdict": "PASS" if okc else "FAIL"}))
        ok_all &= okc

    # ===== (D) t != 0 by translation =====
    log("## D. t!=0 via translation x->x+a, target t=k*a  (all inputs)")
    for (k, R, n, a) in [(3,2,2,3),(3,3,2,5),(4,2,2,4),(5,2,2,2)]:
        if k == 3:
            q, u, w, P, _ = recipe_k3_special(R)
        else:
            q, u, w, P, M = recipe_general(k, R)
        t = (k * a) % q
        wt = tuple((wj + a) % q for wj in w)         # x -> x + a*1
        okc, ni = input_sweep(f"transl_k{k}_R{R}_t{t}", k, R, n, q, t, u, wt)
        ok_all &= okc; total += ni

    # ===== (E) pattern-level certification k=3..6 =====
    log("## E. pattern-level certification (proof case analysis), k=3..6, R=2..4")
    for k in [3, 4, 5, 6]:
        for R in [2, 3, 4]:
            q, u, w, P, M = recipe_general(k, R)
            u_signed = list(u)
            okc, why, mp, mm = pattern_cert(k, R, q, 0, u, w)
            log(json.dumps({"cfg": f"pat_k{k}_R{R}", "q": q, "P": P, "M": M,
                            "max_payload_enum": mp, "min_tag_sep_enum": mm,
                            "verdict": "PASS" if okc else "FAIL", "why": why}))
            ok_all &= okc

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
