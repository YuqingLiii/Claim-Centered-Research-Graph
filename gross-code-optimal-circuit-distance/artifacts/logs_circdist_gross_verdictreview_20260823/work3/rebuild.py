#!/usr/bin/env python3
"""rebuild.py -- rebuild the CNF of every record in a given set of (key -> recorded hash)
pairs, in THIS namespace, and compare.  No solve.

usage: rebuild.py post          # the post-handoff driver records only
       rebuild.py all DIR...    # every distinct (sub-query, hash) in the union
"""
import sys, os, json, glob, hashlib, collections, time

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from sched import make_phi
from cert import tiled_orders
import dext, dext2, cert4, cert6, cert7

_ctx = {}


def ctx_for(sector, triple):
    k = (sector, triple)
    if k not in _ctx:
        phi = make_phi(1, 1)
        orders, _ = tiled_orders(sector, phi, triple)
        _ctx[k] = dext.sector_ctx(orders, sector)[0]
    return _ctx[k]


_orb = {}


def rorb_for(triple):
    if triple not in _orb:
        phi = make_phi(1, 1)
        S, orbits = dext2.column_orbits(phi, triple)
        _orb[triple] = (S, [(rep, orb) for (rep, orb) in orbits if rep[0] == 'r'])
    return _orb[triple]


ENC = {'cert7': cert7.Cert7, 'cert4': cert4.Cert4, 'cert6': cert6.Cert6}


def build_hash(sector, triple, W, K, Ew, oi, enc):
    ctx = ctx_for(sector, triple)
    c = ENC[enc](ctx, W, K, Ew)
    cls = list(c.cls)
    if oi >= 0:
        S, rorb = rorb_for(triple)
        rep, orb = rorb[oi]
        cls.append([c.col_lit(rep)])
        for jj in range(oi):
            for col in rorb[jj][1]:
                cls.append([-c.col_lit(col)])
    h = hashlib.sha256()
    for cl in cls:
        h.update((" ".join(map(str, cl)) + "\n").encode())
    return h.hexdigest()[:32], len(cls)


POST = [
    # sector, triple,        K, Ew, orbit, recorded hash,                      provenance
    ('X', (14, 0, 2), 8, 20, 0, '27abef7a63adc65e5c28055b1cbdafcc', 'harvest/d10.jsonl   kissat 5420.3s'),
    ('Z', (1, 2, 62), 8, 20, 0, '32cf5a255215b3fad59a3ce8d739ac80', 'harvest/d10.jsonl   kissat 6746.2s'),
    ('Z', (1, 2, 62), 7, 16, 1, '6f4aa59dac5aa99d0784727ab466ef72', 'harvest/d10.jsonl   kissat 6800.1s'),
    ('Z', (1, 2, 62), 6, 16, 1, 'bfd07e4b4fdd796380440445b7479b7c', 'harvest/d10.jsonl   kissat 7665.3s'),
    ('X', (14, 0, 2), 8, 22, 0, '151cecf0bcb08fd8f944d6eff60b27c1', 'LIVE final.jsonl    cd15   9301.4s'),
    # the two drive7 records that post-date the wave-6 cell tables' Z rows
    ('Z', (1, 2, 62), 6, 20, 1, None, 'live final.jsonl    cd15   7396.2s'),
    ('Z', (1, 2, 62), 8, 22, 0, None, 'live final.jsonl    cd15   7559.6s'),
]

mode = sys.argv[1] if len(sys.argv) > 1 else 'post'

if mode == 'post':
    print("POST-HANDOFF DRIVER RECORDS -- independent CNF rebuild in a fresh namespace")
    print("=" * 100)
    ok = bad = 0
    for sec, tri, K, Ew, oi, rec, prov in POST:
        got, nc = build_hash(sec, tri, 10, K, Ew, oi, 'cert7')
        if rec is None:
            print("  %s (%2d,%2d) orbit %d  [%s]  rebuilt %s  nclauses_final=%d   (no hash quoted here)"
                  % (sec, K, Ew, oi, prov, got, nc))
            continue
        v = "MATCH" if got == rec else "*** MISMATCH ***"
        ok += got == rec
        bad += got != rec
        print("  %s (%2d,%2d) orbit %d  [%s]\n      recorded %s\n      rebuilt  %s  nclauses_final=%d   %s"
              % (sec, K, Ew, oi, prov, rec, got, nc, v))
    print("=" * 100)
    print("  MATCH: %d    MISMATCH: %d" % (ok, bad))
    sys.exit(0)

# ------------------------------------------------------------------ full union rebuild
DIRS = sys.argv[2:]
CAND = {('Z', (1, 2, 62)), ('X', (14, 0, 2))}
want = {}
for D in DIRS:
    for L in sorted(glob.glob(os.path.join(D, '*.jsonl'))):
        for ln in open(L):
            ln = ln.strip()
            if not ln:
                continue
            try:
                r = json.loads(ln)
            except Exception:
                continue
            if r.get('verdict') not in ('SAT', 'UNSAT'):
                continue
            if 'triple' not in r or r.get('W') != 10:
                continue
            if (r['sector'], tuple(r['triple'])) not in CAND:
                continue
            if r.get('orbit', -1) < 0:
                continue
            key = (r['sector'], tuple(r['triple']), r['K'], r['Ew'], r['orbit'],
                   r['cnf_sha256'], r.get('nclauses_final') or -1)
            want.setdefault(key, os.path.basename(D) + '/' + os.path.basename(L))

print("distinct (sub-query, recorded-hash) pairs to verify: %d" % len(want))
t0 = time.time()
ok = collections.Counter()
fails = []
for i, (key, prov) in enumerate(sorted(want.items())):
    sec, tri, K, Ew, oi, rh, ncf = key
    hit = None
    for enc in ('cert7', 'cert4', 'cert6'):
        try:
            got, nc = build_hash(sec, tri, 10, K, Ew, oi, enc)
        except Exception:
            continue
        if got == rh:
            hit = enc
            break
    if hit:
        ok[hit] += 1
    else:
        fails.append((key, prov))
    if (i + 1) % 100 == 0:
        print("   ... %d/%d  (%.0f s)" % (i + 1, len(want), time.time() - t0), flush=True)
print()
print("VERIFIED : %d" % sum(ok.values()))
print("FAILED   : %d" % len(fails))
print("by encoding that reproduced it: %s" % dict(ok))
for key, prov in fails:
    print("   FAIL %s  [%s]" % (str(key), prov))
print("elapsed %.0f s" % (time.time() - t0))
