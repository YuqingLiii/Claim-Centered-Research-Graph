#!/usr/bin/env python3
"""Reviewer-independent CNF REBUILD (no solve): rebuild the exact formula job7k.py would hand the
solver for a given (sector, triple, W, K, Ew, orbit) and hash it, so the recorded cnf_sha256 can be
checked without paying for the solve."""
import sys, os, json, hashlib, glob, collections
import numpy as np
HERE=os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE,'..','work'))
from sched import make_phi
from cert import tiled_orders
import dext, dext2, cert7
CAND={'Z':(1,2,62),'X':(14,0,2)}
def rebuild(sector, triple, W, K, Ew, oi):
    phi=make_phi(1,1)
    orders,_=tiled_orders(sector,phi,triple)
    ctx,Hstab=dext.sector_ctx(orders,sector)
    c=cert7.Cert7(ctx,W,K,Ew)
    cls=list(c.cls)
    if oi>=0:
        S,orbits=dext2.column_orbits(phi,triple)
        rorb=[(rep,orb) for (rep,orb) in orbits if rep[0]=='r']
        rep,orb=rorb[oi]
        cls.append([c.col_lit(rep)])
        for jj in range(oi):
            for col in rorb[jj][1]: cls.append([-c.col_lit(col)])
    h=hashlib.sha256()
    for cl in cls: h.update((" ".join(map(str,cl))+"\n").encode())
    return h.hexdigest()[:32], len(cls), c.top

# recorded hashes, read from the logs
ROOT=os.path.normpath(os.path.join(HERE,'..','..'))
lines=set(); rec={}
for D in sorted(glob.glob(os.path.join(ROOT,'logs_circdist_gross_*'))):
    if 'verdictreview' in os.path.basename(D): continue
    for L in sorted(glob.glob(os.path.join(D,'*.jsonl'))):
        for line in open(L):
            line=line.strip()
            if not line or line in lines: continue
            lines.add(line); r=json.loads(line)
            if r.get('verdict') in ('SAT','UNSAT') and r.get('W')==10 and r.get('orbit') is not None and r['orbit']>=0:
                if tuple(r.get('triple',()))==CAND.get(r.get('sector')):
                    rec.setdefault((r['sector'],r['K'],r['Ew'],r['orbit']),[]).append(r)

TARGETS=[('Z',9,22,0),('X',5,18,0),('Z',7,18,0),('X',6,18,0),('Z',6,18,0),('X',8,22,0),
         ('Z',8,22,0),('Z',6,20,0),('Z',6,20,1),('Z',7,20,0),('X',7,20,0),('Z',5,18,0)]
print("INDEPENDENT CNF REBUILD (no solve) OF THE HISTORIC-TIMEOUT SUB-QUERIES")
print("%-16s %10s %8s  %-34s %-34s %s" % ("sub-query","clauses","vars","recorded cnf_sha256","rebuilt","match"))
ok=0; tot=0
for (sec,K,Ew,o) in TARGETS:
    tr=CAND[sec]
    hh,ncl,nv=rebuild(sec,tr,10,K,Ew,o)
    rs={r.get('cnf_sha256') for r in rec.get((sec,K,Ew,o),[])}
    m = hh in rs
    tot+=1; ok+= 1 if m else 0
    print("%-16s %10d %8d  %-34s %-34s %s" % ("%s (%d,%d) o%d"%(sec,K,Ew,o), ncl, nv,
          ",".join(sorted(x or '-' for x in rs)) or 'NO RECORD', hh, "MATCH" if m else "MISMATCH"))
print()
print("rebuilt %d formulas, %d matched the recorded cnf_sha256" % (tot, ok))
