"""Run a list of job4 cells with a bounded process pool, append every result line to a jsonl log."""
import subprocess, sys, os, json, time, threading

HERE = os.path.dirname(os.path.abspath(__file__))
LOG = os.path.join(HERE, sys.argv[1])
NPROC = int(sys.argv[2])
SPEC = json.load(open(os.path.join(HERE, sys.argv[3])))   # list of arg-lists
TMO = float(sys.argv[4]) if len(sys.argv) > 4 else None

lock = threading.Lock()
queue = list(SPEC)
qi = [0]


def worker():
    while True:
        with lock:
            if qi[0] >= len(queue):
                return
            i = qi[0]; qi[0] += 1
            args = queue[i]
        t0 = time.time()
        try:
            p = subprocess.run([sys.executable, os.path.join(HERE, 'job4.py')]
                               + [str(a) for a in args],
                               capture_output=True, text=True, cwd=HERE, timeout=TMO)
            out = p.stdout.strip().splitlines()
            line = out[-1] if out else json.dumps(dict(args=args, verdict='CRASH',
                                                       err=p.stderr[-400:]))
            try:
                rec = json.loads(line)
            except Exception:
                rec = dict(args=args, verdict='CRASH', raw=line[:400], err=p.stderr[-400:])
        except subprocess.TimeoutExpired:
            rec = dict(args=args, verdict='TIMEOUT', tmo=TMO)
        rec['wall'] = round(time.time() - t0, 1)
        with lock:
            with open(LOG, 'a') as f:
                f.write(json.dumps(rec) + "\n")
            print(f"[{i+1}/{len(queue)}] {args} -> {rec.get('verdict')} {rec['wall']}s", flush=True)


ts = [threading.Thread(target=worker) for _ in range(NPROC)]
for t in ts:
    t.start()
for t in ts:
    t.join()
print("done")
