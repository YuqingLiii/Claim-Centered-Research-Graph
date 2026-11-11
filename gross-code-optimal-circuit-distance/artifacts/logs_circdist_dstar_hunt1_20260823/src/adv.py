"""STEP 2 of the directed hunt: with the within-check orders FIXED at a d_ext=11-compatible
assignment, search the legal+(MC) time assignments for one in which EVERY canonical
minimum-weight gamma has repair >= 1, in BOTH sectors.

State: a total order of the 864 CNOTs (times = positions; legality automatic, all distinct).
Invariant: each check's own gates keep their prescribed order.  Moves: relocate one gate
inside the window allowed by its check-order neighbours.  (MC) is re-checked after each move
and a move that breaks it is rejected -- so the walk stays on the (MC) manifold, which is
non-empty because the check-serial schedule lies on it."""
import itertools, random, sys, json, time, collections
from lift import Schedule, Sector, popc, sameround_repair0
import gross as G, hunt as H
NG=G.NG; CSSG=G.CSSG
rng=random.Random(int(sys.argv[3]) if len(sys.argv)>3 else 11)
PX,PZ=H.pools(); pidxX=H.pair_index(PX); pidxZ=H.pair_index(PZ)
tidxX=H.triple_index(PX); tidxZ=H.triple_index(PZ)
ordZ=json.load(open('orders_Z.json'))   # X-check orders (3-suffix T,S) for Z-memory
ordX=json.load(open('orders_X.json'))   # Z-check orders

def full_orders(checks, part):
    """complete each check's order: prefix = the other 3 qubits (random), then T\\S, then S."""
    out=[]
    for a in range(len(checks)):
        T,S=[tuple(x) for x in part[a]]
        S=list(S); mid=[q for q in T if q not in S]
        pre=[q for q in checks[a] if q not in T]; rng.shuffle(pre)
        out.append(pre+mid+S)
    return out

OX=full_orders(CSSG.Xchecks, ordZ)      # X-check CNOT orders
OZ=full_orders(CSSG.Zchecks, ordX)      # Z-check CNOT orders

# ---- initial state: check-serial in a random check order (guaranteed (MC))
seq=[]
chk=[('X',g) for g in range(NG)]+[('Z',g) for g in range(NG)]
rng.shuffle(chk)
for typ,g in chk:
    for q in (OX[g] if typ=='X' else OZ[g]):
        seq.append((typ,g,q))

def to_sched(seq):
    tX={};tZ={}
    for t,(typ,g,q) in enumerate(seq):
        if typ=='X': tX[(g,q)]=t
        else: tZ[(q,g)]=t
    return Schedule(CSSG,tX,tZ)

OVL=CSSG.overlaps
def mcok(pos):
    for (a,b,sh) in OVL:
        c=0
        for q in sh:
            if pos[('Z',b,q)]<pos[('X',a,q)]: c^=1
        if c: return False
    return True

def evaluate(seq, full=False):
    s=to_sched(seq)
    res={}
    tot0=0; tott=0; horiz=0
    for lab,mir,pidx,tidx in (('Z',False,pidxX,tidxX),('X',True,pidxZ,tidxZ)):
        sec=Sector(CSSG,s,mirror=mir)
        h=0; n0=0; nt=0
        for a in range(NG):
            S=sec.hook(a,2); kind,u,sv=sec.classify_hook(a,S)
            if kind in ('trivial','horizontal'): h+=1
        horiz+=h
        if full and h==0:
            n0,nt,_=H.decide_rate(sec,pidx)
        res[lab]=(h,n0,nt)
        tot0+=n0; tott+=nt
    return horiz, tot0, tott, res, s

pos={g:i for i,g in enumerate(seq)}
assert mcok(pos), "initial check-serial schedule must be (MC)"
best=evaluate(seq)
print("start: horizontal 2-suffix hooks (both sectors, /144) =",best[0]); sys.stdout.flush()

ITERS=int(sys.argv[1]) if len(sys.argv)>1 else 4000
t0=time.time(); cur=best[0]; acc=0
for it in range(ITERS):
    i=rng.randrange(len(seq))
    typ,g,q=seq[i]
    # window: between the previous and next gate of the SAME check
    lo=0; hi=len(seq)-1
    for j in range(i-1,-1,-1):
        if seq[j][0]==typ and seq[j][1]==g: lo=j+1; break
    for j in range(i+1,len(seq)):
        if seq[j][0]==typ and seq[j][1]==g: hi=j-1; break
    if hi<=lo: continue
    k=rng.randrange(lo,hi+1)
    if k==i: continue
    ns=seq[:]; item=ns.pop(i); ns.insert(k,item)
    npos={gg:ii for ii,gg in enumerate(ns)}
    if not mcok(npos): continue
    h,_,_,_,_=evaluate(ns)
    if h<=cur:
        if h<cur: acc+=1
        seq=ns; cur=h
        if cur==0: break
print("after %d proposals: horizontal hooks = %d  (accepted improvements %d, %.0fs)"
      % (it+1,cur,acc,time.time()-t0)); sys.stdout.flush()
h,n0,nt,res,s=evaluate(seq,full=True)
print("FINAL  mc_violations=%d  pair_int=%d strict_pair_int=%d  glob_int=%s"
      % (len(s.mc_violations()), s.interleaved_pairs(), s.strict_interleaved_pairs(),
         s.globally_interleaved()))
print("       per sector (horizontal hooks, repair-0 count, canonical family size):",res)
if h==0 and nt and n0==0:
    print("*** STAGE-1 GAP CANDIDATE (both sectors, canonical family) ***")
    json.dump([list(x) for x in seq], open('gapcand_seq.json','w'))
