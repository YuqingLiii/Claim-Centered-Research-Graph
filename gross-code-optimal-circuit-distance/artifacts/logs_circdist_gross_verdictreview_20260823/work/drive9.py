"""Dedup-aware completion driver.

The predecessor's drive7.py (pid 5675) is STILL RUNNING over spec_final.json with 30 workers.
This driver works the SAME open frontier but (a) orders jobs cheapest-first by the empirical
hardness model of predict.py, and (b) re-checks, immediately before every dispatch, both the
union of all jsonl logs and the live process table, so it never repeats a sub-query that the
other driver has already decided or currently has in flight.  That is the deduplication the
predecessor's §7.5(6) records losing half an hour to.
"""
import subprocess, sys, os, json, time, threading
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import cert4, predict
from inflight import inflight

HERE = os.path.dirname(os.path.abspath(__file__))
LOG  = os.path.join(HERE, sys.argv[1])
NPROC= int(sys.argv[2])
TMO  = float(sys.argv[3]) if len(sys.argv) > 3 else 7200.0
TRI  = {'Z':'1,2,62','X':'14,0,2'}

def open_jobs():
    rec = predict.load()
    m,_ = predict.model(rec)
    jobs = []
    for sec in ('Z','X'):
        for (K,Ew) in cert4.cells(10):
            if Ew == 12:            # decided completely and independently by enum12.py
                continue
            for orb in range(9):
                if (sec,K,Ew,orb) in rec:
                    continue
                jobs.append((predict.predict(m,K,Ew,orb), sec, K, Ew, orb))
    jobs.sort()
    return jobs, rec

lock = threading.Lock()
done_local = set()

def claim(sec,K,Ew,orb):
    """Return True iff nobody else has decided or is running this sub-query."""
    with lock:
        if (sec,K,Ew,orb) in done_local:
            return False
        rec = predict.load()
        if (sec,K,Ew,orb) in rec:
            return False
        if (sec,TRI[sec],K,Ew,orb) in inflight():
            return False
        done_local.add((sec,K,Ew,orb))
        return True

JOBS,_ = open_jobs()
qi = [0]
print(f"{len(JOBS)} open sub-queries; cheapest-first; {NPROC} workers; per-job timeout {TMO}s",
      flush=True)

def worker():
    while True:
        with lock:
            if qi[0] >= len(JOBS):
                return
            i = qi[0]; qi[0] += 1
            est, sec, K, Ew, orb = JOBS[i]
        if not claim(sec,K,Ew,orb):
            print(f"[{i+1}/{len(JOBS)}] SKIP (other driver) {sec} K={K} Ew={Ew} o={orb}", flush=True)
            continue
        args = [sec, TRI[sec], '10', str(K), str(Ew), str(orb)]
        t0 = time.time()
        try:
            p = subprocess.run([sys.executable, os.path.join(HERE,'job7.py')] + args,
                               capture_output=True, text=True, cwd=HERE, timeout=TMO)
            out = p.stdout.strip().splitlines()
            line = out[-1] if out else ''
            try:
                rec = json.loads(line)
            except Exception:
                rec = dict(sector=sec, triple=[int(x) for x in TRI[sec].split(',')], W=10, K=K,
                           Ew=Ew, orbit=orb, verdict='CRASH', raw=line[:300],
                           err=p.stderr[-300:])
        except subprocess.TimeoutExpired:
            rec = dict(sector=sec, triple=[int(x) for x in TRI[sec].split(',')], W=10, K=K,
                       Ew=Ew, orbit=orb, verdict='TIMEOUT', tmo=TMO)
        rec['wall'] = round(time.time()-t0, 1); rec['est'] = est; rec['driver'] = 'drive9'
        with lock:
            with open(LOG,'a') as f:
                f.write(json.dumps(rec)+"\n")
        flag = '  <<<<< SAT >>>>>' if rec.get('verdict')=='SAT' else ''
        print(f"[{i+1}/{len(JOBS)}] {sec} K={K} Ew={Ew} o={orb} est={est:.0f}s -> "
              f"{rec.get('verdict')} {rec['wall']}s{flag}", flush=True)

ts = [threading.Thread(target=worker) for _ in range(NPROC)]
for t in ts: t.start()
for t in ts: t.join()
print("drive9 done", flush=True)
