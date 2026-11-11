"""LINK 4 part 2: literal 360-column extended code, column diff, bidirectional round-trip."""
import sys,os,json,random,pickle
sys.path.insert(0,os.path.abspath('gen')); sys.path.insert(0,os.path.abspath('.'))
import numpy as np
from gross import NG as tNG, N as tN, Reducer
from sched import make_phi
from cert import tiled_orders
import dext
import gr as mine
from filt import CANON
L,M=12,6; NG=72; N=144
def neg(q):
    h,p=(0,q) if q<NG else (NG,q-NG); i,j=divmod(p,M); return h+((-i)%L)*M+((-j)%M)
def myslots(sec,g):
    if sec=='X': return [mine.gadd(g,m) for m in mine.Amon]+[NG+mine.gadd(g,m) for m in mine.Bmon]
    return [mine.gadd(g,(-m[0],-m[1])) for m in mine.Bmon]+[NG+mine.gadd(g,(-m[0],-m[1])) for m in mine.Amon]
def myphi(g):
    i,j=divmod(g,M); return (2*i+2*j)%3
random.seed(20260823)
OUT={}
for sec,triple in (('Z',(1,2,62)),('X',(14,0,2))):
    # ---------- MY literal 360-column extended code (my indexing) ----------
    Hdet = mine.HX if sec=='Z' else mine.HZ         # 72 rows, int masks over 144 qubits
    Hstab= mine.HZ if sec=='Z' else mine.HX
    pool  = pickle.load(open('poolZ.pkl' if sec=='Z' else 'poolX.pkl','rb'))
    lpool = pickle.load(open('poolX.pkl' if sec=='Z' else 'poolZ.pkl','rb'))   # OPPOSITE type
    RS,pv = mine.rref(Hstab)
    # 12-row logical basis independent mod rowspace(Hstab)
    Lb=[]; cur=list(Hdet)          # L rows are logicals of the opposite type: in ker(Hstab)
    for v in lpool:
        if len(mine.rref(cur+[v])[0])>len(mine.rref(cur)[0]):
            cur=cur+[v]; Lb.append(v)
        if len(Lb)==12: break
    assert len(Lb)==12
    Lrows=Lb
    myres={g:[tuple(o[p] for p in ((0,1),(3,4,5),(4,5))[k]) for k in range(3)]
           for g in range(NG) for o in [[myslots(sec,g)[k] for k in CANON[triple[myphi(g)]]]]}
    RESLIST=[(g,k) for g in range(NG) for k in range(3)]
    def chi(g,k):
        m=0
        for q in myres[g][k]: m^=1<<q
        return m
    # H_ext column for residual (g,k) = XOR of Hdet columns of its qubits  == Hdet . chi
    def Hsyn(v): return sum(((mine.popc(Hdet[e]&v)&1)<<e) for e in range(NG))
    def Lsyn(v): return sum(((mine.popc(Lrows[i]&v)&1)<<i) for i in range(12))
    Hcol=[Hsyn(1<<q) for q in range(N)]+[Hsyn(chi(g,k)) for (g,k) in RESLIST]
    Lcol=[Lsyn(1<<q) for q in range(N)]+[Lsyn(chi(g,k)) for (g,k) in RESLIST]
    assert len(Hcol)==360
    # ---------- their ctx ----------
    orders,_=tiled_orders(sec,make_phi(1,1),triple)
    ctx,Hst=dext.sector_ctx(orders,sec)
    tHcol=[]
    for q in range(tN): tHcol.append(int(''.join(str(int(b)) for b in ctx.Hdet[::-1,q]),2))
    for g in range(tNG):
        for k in range(3):
            v=0
            for q in ctx.res[g][k]: v^=tHcol[q]
            tHcol.append(v)
    # relabel my columns into their index space: their qubit q == my qubit neg(q);
    # their row e == my row neg(e)
    def rerow(v): return sum(((v>>e)&1)<<neg(e) for e in range(NG))
    myH_in_theirs=[rerow(Hcol[neg(q)]) for q in range(N)]
    theirres_key={}
    for g in range(tNG):
        for k in range(3): theirres_key[(g,k)]=tuple(sorted(ctx.res[g][k]))
    myres_key={}
    for g in range(NG):
        for k in range(3): myres_key[(neg(g),k)]=tuple(sorted(neg(q) for q in myres[g][k]))
    colmatch = all(myH_in_theirs[q]==tHcol[q] for q in range(N))
    resmatch = all(theirres_key[(g,k)]==myres_key[(g,k)] for g in range(tNG) for k in range(3))
    # residual columns compared as multisets of 72-bit vectors
    def rcol(res_key,Hc):
        out=[]
        for g in range(tNG):
            for k in range(3):
                v=0
                for q in res_key[(g,k)]: v^=Hc[q]
                out.append(v)
        return out
    rc_t=rcol(theirres_key,tHcol[:tN]); rc_m=rcol(myres_key,myH_in_theirs)
    # ---------- round trip ----------
    samples=[]; okA=okB=0; cells=set()
    HZrows=Hstab
    for trial in range(400):
        E=random.choice(pool)
        for _ in range(random.randint(0,3)): E^=random.choice(HZrows)
        if mine.popc(E)>24: continue
        K=random.choice([0,1,2,3,4,5,6,7,8])
        R=random.sample(RESLIST,K)
        xd=E
        for (g,k) in R: xd^=chi(g,k)
        w=mine.popc(xd)+K
        cell=(K,mine.popc(E))
        # direction B: fault set -> extended-code vector, checked on the literal 360-col matrices
        xs=[q for q in range(N) if (xd>>q)&1]+[N+RESLIST.index(r) for r in R]
        hs=0; ls=0
        for c in xs: hs^=Hcol[c]; ls^=Lcol[c]
        nz = (hs==0) and (ls!=0)
        # direction A: extended vector -> fault set -> syndrome check
        Eb=0
        for c in xs:
            Eb ^= (1<<c) if c<N else chi(*RESLIST[c-N])
        synE = all(mine.popc(Hdet[e]&Eb)%2==0 for e in range(NG))
        logE = not mine.inspan(Eb,RS,pv)
        roundtrip = (Eb==E) and (synE==(hs==0)) and (logE==(ls!=0)) and nz
        # cross-check against THEIR verifier on the same sample (their index space)
        Et=np.zeros(tN,np.uint8); Dt=np.zeros(tN,np.uint8)
        for q in range(N):
            if (E>>q)&1: Et[neg(q)]=1
            if (xd>>q)&1: Dt[neg(q)]=1
        Rt=[(neg(g),k) for (g,k) in R]
        info=dext.verify_witness(ctx,Et,Rt,Dt,Hst)
        agree=(info['decomposition_ok'] and info['zero_syndrome']==synE
               and info['nontrivial_logical']==logE and info['weight']==w and info['Ewt']==mine.popc(E))
        okA+=roundtrip; okB+=agree; cells.add(cell)
        samples.append((cell,w,roundtrip,agree))
        if len(samples)>=60: break
    OUT[sec]=dict(residual_sets_match=resmatch, data_columns_match=colmatch,
                  residual_columns_match=(rc_t==rc_m), n_ext_columns=len(Hcol),
                  samples=len(samples), cells_covered=len(cells),
                  roundtrip_pass=okA, crossimpl_agree=okB,
                  cell_list=sorted(cells))
# ---------- the two recorded w11 witnesses, checked on MY extended code ----------
W11={'Z':(48,0,[49,54,57,59,60,120,125,127,131,135,137,138],[49,57,59,120,125,127,131,135,137,138]),
     'X':(18,0,[0,15,22,39,47,83,84,102,107,109,117,133],[15,39,47,83,84,102,107,109,117,133])}
rec={}
for sec,(chk,k,Ei,Di) in W11.items():
    triple=(1,2,62) if sec=='Z' else (14,0,2)
    Hdet = mine.HX if sec=='Z' else mine.HZ; Hstab= mine.HZ if sec=='Z' else mine.HX
    RS,pv=mine.rref(Hstab)
    g=neg(chk)
    o=[myslots(sec,g)[t] for t in CANON[triple[myphi(g)]]]
    r=tuple(sorted(neg(q) for q in [o[0],o[1]] ))   # k=0 -> positions (0,1)
    E=0
    for q in Ei: E|=1<<neg(q)          # recorded witness is in THEIR index space
    D=0
    for q in Di: D|=1<<neg(q)
    chim=0
    for q in r: chim^=1<<neg(q)        # bring my residual back to my own space
    rec[sec]=dict(residual_from_my_build=sorted(r), residual_recorded=[54,60] if sec=='Z' else [0,22], decomposition_ok=((D^chim)==E),
                  zero_syndrome=all(mine.popc(Hdet[e]&E)%2==0 for e in range(NG)),
                  nontrivial=not mine.inspan(E,RS,pv), weight=mine.popc(D)+1, Ewt=mine.popc(E))
OUT['recorded_w11_witnesses_on_my_extended_code']=rec
for k,v in OUT.items():
    if k=='recorded_w11_witnesses_on_my_extended_code':
        for s2,d in v.items(): print('W11',s2,d)
    else:
        print('SECTOR',k,{a:b for a,b in v.items() if a!='cell_list'})
        print('   cells covered:',v['cell_list'])
