
"""Rebuild the CNF of EVERY recorded candidate sub-query and check its hash against the
record.  Tries cert4 / cert6 / cert7; a record is VERIFIED if some encoding reproduces both
its clause counts and its hash exactly."""
import json, os, sys, glob, hashlib, collections, time
from sched import make_phi
from cert import tiled_orders
import dext, dext2, cert4, cert6, cert7

CAND={'Z':(1,2,62),'X':(14,0,2)}
LOGDIRS=sys.argv[1:]
recs=[]
seen=set()
for D in LOGDIRS:
    for L in sorted(glob.glob(os.path.join(D,'*.jsonl'))):
        for ln in open(L):
            ln=ln.strip()
            if not ln: continue
            try: r=json.loads(ln)
            except: continue
            if r.get('verdict') not in ('SAT','UNSAT'): continue
            if 'triple' not in r or r.get('W')!=10: continue
            if tuple(r['triple'])!=CAND.get(r['sector']): continue
            if r.get('orbit',-1)<0: continue
            if not r.get('cnf_sha256'): continue
            sig=(r['sector'],r['K'],r['Ew'],r['orbit'],r['cnf_sha256'])
            if sig in seen: continue
            seen.add(sig); r['_log']=os.path.basename(L); recs.append(r)
print("distinct (sub-query, hash) records to verify:", len(recs), flush=True)

phi=make_phi(1,1)
CTX={}; RORB={}
for sec,trip in CAND.items():
    orders,_=tiled_orders(sec,phi,trip)
    CTX[sec]=dext.sector_ctx(orders,sec)[0]
    S,orbits=dext2.column_orbits(phi,trip)
    RORB[sec]=[(rep,orb) for (rep,orb) in orbits if rep[0]=='r']

CACHE={}
def build(sec,K,Ew,oi,cls_name):
    key=(sec,K,Ew,cls_name)
    if key not in CACHE:
        C={'cert4':cert4.Cert4,'cert6':cert6.Cert6,'cert7':cert7.Cert7}[cls_name]
        CACHE[key]=C(CTX[sec],10,K,Ew)
        if len(CACHE)>40: CACHE.pop(next(iter(CACHE)))
    c=CACHE[key]
    cls=list(c.cls)
    rorb=RORB[sec]
    rep,orb=rorb[oi]
    cls.append([c.col_lit(rep)])
    for jj in range(oi):
        for col in rorb[jj][1]:
            cls.append([-c.col_lit(col)])
    h=hashlib.sha256()
    for cl in cls: h.update((" ".join(map(str,cl))+"\n").encode())
    return h.hexdigest()[:32], len(c.cls), len(cls)

res=collections.Counter(); fails=[]; encused=collections.Counter()
t0=time.time()
for i,r in enumerate(recs):
    ok=False
    for nm in ('cert7','cert4','cert6'):
        try: hh,nc,ncf=build(r['sector'],r['K'],r['Ew'],r['orbit'],nm)
        except Exception as e: continue
        if hh==r['cnf_sha256']:
            ok=True; encused[nm]+=1
            if r.get('nclauses') not in (None,nc) or r.get('nclauses_final') not in (None,ncf):
                res['hash_ok_count_mismatch']+=1
            break
    if ok: res['VERIFIED']+=1
    else:
        res['FAILED']+=1
        fails.append((r['sector'],r['K'],r['Ew'],r['orbit'],r['cnf_sha256'],r['_log'],r.get('nclauses')))
    if (i+1)%100==0: print(f"  {i+1}/{len(recs)}  {dict(res)}  {round(time.time()-t0)}s", flush=True)
print("\n=== RESULT ===")
print(dict(res)); print("encoding used:", dict(encused))
print("failures:", len(fails))
for f in fails[:40]: print("   FAIL", f)
