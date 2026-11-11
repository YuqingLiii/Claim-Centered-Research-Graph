
"""Dedup-aware, claim-file driver.  Implements the predecessor's own recommended fix:
the claim lives in the FILESYSTEM (os.open(..., O_CREAT|O_EXCL)), so any number of
independently launched drivers -- including ones inherited mid-flight -- cooperate
without knowing about each other.

usage: drive10.py <logfile> <nworkers> <timeout_s> <queue.json>
queue.json: [[sector, "a,b,c", W, K, Ew, orbit, solver], ...]  in dispatch order
"""
import json, os, sys, subprocess, time, glob, threading, hashlib

HERE = os.path.dirname(os.path.abspath(__file__))
LOGFILE = sys.argv[1]; NW = int(sys.argv[2]); TMO = int(sys.argv[3]); QF = sys.argv[4]
CLAIMS = os.path.join(HERE, 'claims'); os.makedirs(CLAIMS, exist_ok=True)
os.makedirs(os.path.dirname(LOGFILE) or '.', exist_ok=True)

# every log dir we know about: rescued repo copy, inherited live dir, mine
LOGDIRS = [
    "<home>/Documents/Codex/2026-08-07/i-have-connected-an-old-windows/outputs/Windows-SSD-Recovery-2026-08-07/Research-Projects/discovery-new-algorithms/artifacts/logs_circdist_gross_drivers_20260823",
    os.path.join(os.path.dirname(HERE), 'work', 'logs'),
    os.path.join(HERE, 'logs'),
]
CAND = {('Z', (1, 2, 62)), ('X', (14, 0, 2))}

def decided():
    """set of (sector,K,Ew,orbit) already decided SAT/UNSAT on a candidate triple, any log"""
    out = set()
    for D in LOGDIRS:
        for L in glob.glob(os.path.join(D, '*.jsonl')):
            try: fh = open(L)
            except OSError: continue
            for ln in fh:
                ln = ln.strip()
                if not ln: continue
                try: r = json.loads(ln)
                except Exception: continue
                if r.get('verdict') not in ('SAT', 'UNSAT'): continue
                if 'triple' not in r or r.get('W') != 10: continue
                if (r['sector'], tuple(r['triple'])) not in CAND: continue
                if r.get('orbit', -1) < 0: continue
                out.add((r['sector'], r['K'], r['Ew'], r['orbit']))
    return out

def inflight():
    """(sector,K,Ew,orbit) currently being solved by ANY job7*.py on this machine"""
    out = set()
    try:
        ps = subprocess.run(['ps', '-eo', 'command'], capture_output=True, text=True, timeout=30).stdout
    except Exception:
        return out
    for ln in ps.splitlines():
        if 'job7' not in ln or 'grep' in ln: continue
        t = ln.split()
        try:
            i = max(j for j, x in enumerate(t) if x.endswith('job7.py') or x.endswith('job7k.py'))
        except ValueError:
            continue
        a = t[i+1:]
        if len(a) < 6: continue
        try:
            sec = a[0]; K = int(a[3]); Ew = int(a[4]); orb = int(a[5])
        except Exception:
            continue
        out.add((sec, K, Ew, orb))
    return out

lock = threading.Lock()
logfh = open(LOGFILE, 'a', buffering=1)
outfh = open(LOGFILE.replace('.jsonl', '.out'), 'a', buffering=1)

def emit(s):
    with lock:
        outfh.write(f"[{time.strftime('%H:%M:%S')}] {s}\n")

def worker(q):
    while True:
        with lock:
            if not q: return
            task = q.pop(0)
        sec, trip, W, K, Ew, orb, solver = task
        key = (sec, K, Ew, orb)
        if key in decided():
            emit(f"SKIP decided {key}"); continue
        if key in inflight():
            emit(f"SKIP inflight {key} (inherited driver is on it)"); continue
        cname = os.path.join(CLAIMS, f"{sec}_{K}_{Ew}_{orb}.claim")
        try:
            fd = os.open(cname, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
            os.write(fd, f"{os.getpid()} {time.time()} {solver}\n".encode()); os.close(fd)
        except FileExistsError:
            emit(f"SKIP claimed {key}"); continue
        emit(f"START {key} solver={solver} tmo={TMO}")
        t0 = time.time()
        try:
            p = subprocess.run([sys.executable, os.path.join(HERE, 'job7k.py'),
                                sec, trip, str(W), str(K), str(Ew), str(orb), solver],
                               capture_output=True, text=True, timeout=TMO, cwd=HERE)
            wall = round(time.time() - t0, 1)
            line = p.stdout.strip().splitlines()[-1] if p.stdout.strip() else ''
            if line.startswith('{'):
                r = json.loads(line); r['wall'] = wall
                with lock: logfh.write(json.dumps(r) + "\n")
                emit(f"DONE  {key} {r['verdict']} {r['seconds']}s (wall {wall})")
            else:
                with lock: logfh.write(json.dumps(dict(
                    sector=sec, triple=[int(x) for x in trip.split(',')], W=W, K=K, Ew=Ew,
                    orbit=orb, solver=solver, verdict='CRASH', wall=wall,
                    stderr=p.stderr[-400:])) + "\n")
                emit(f"CRASH {key} {p.stderr[-200:]}")
                os.unlink(cname)
        except subprocess.TimeoutExpired:
            wall = round(time.time() - t0, 1)
            with lock: logfh.write(json.dumps(dict(
                sector=sec, triple=[int(x) for x in trip.split(',')], W=W, K=K, Ew=Ew,
                orbit=orb, solver=solver, verdict='TIMEOUT', wall=wall)) + "\n")
            emit(f"TMO   {key} after {wall}s")
            os.unlink(cname)   # release so a later/longer run can retry

q = json.load(open(QF))
emit(f"driver start pid={os.getpid()} nworkers={NW} timeout={TMO} queue={len(q)}")
ths = [threading.Thread(target=worker, args=(q,), daemon=True) for _ in range(NW)]
for t in ths: t.start()
for t in ths: t.join()
emit("driver done")
