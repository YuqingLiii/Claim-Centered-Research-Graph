#!/usr/bin/env python3
"""
Exact constructor/specification for the COMPLETE H4-invariant Boolean degree-4
SOS-dual problem for the certified 300x300 d=4 instance.

Python 3.9+; dependencies numpy,h5py.  Requires g++ for the fast exhaustive
quartic orbit index.  It does NOT solve the SDP.  It constructs the full,
unrestricted invariant moment coordinate system and the exact compressed
product table defining every block pencil.

Usage:
  python h4_full_invariant_dual_spec.py \
    d4_n1_300x300.mat \
    d4_n1_300x300.mat.H4_level2_exact_system.json \
    d4_n1_300x300.mat.complete_K_isotypic.json \
    h4_nogap_irrep_cache.py \
    h4_K_full_dual_slice_release.py \
    OUTDIR

Place h4_moment_orbit_index.cpp and h4_product_moment_map.cpp beside this file.

Mathematics represented by the output
-------------------------------------
An H4-invariant functional L on squarefree Boolean monomials of degree <=4
has one coordinate for each orientable signed monomial orbit.  Odd moments
vanish.  If O_i,O_j are non-D degree<=2 monomial orbit representatives, the
product table records, for each g in H4,

    L(m_i * g m_j) = sign[i,j,g] * theta[id[i,j,g]],

with id=-1 meaning the signed support orbit is nonorientable and hence every
H4-invariant L vanishes there.

With the corrected coefficient-functional convention, the complete K kernel
in irrep rho is ker C_rho where residual restrictions use r(g^{-1}m).  The
full block pencil is

 M_rho(theta)=Z_rho^* B_rho(theta) Z_rho,
 B_(O,a),(O',b)=1/sqrt(|H_O||H_O'|)
   v_O,a^* [sum_g sign(O,O',g) theta_id rho(g)] v_O',b.

Feasibility after positive scaling is

    C*theta_empty - sum_t objective_B[t]*theta_t = -1,
    M_rho(theta) >= 0  for the 20 nonzero complete-K blocks.

The constructor proves by signed Burnside enumeration that there are 752621
invariant moment coordinates through degree four, then proves from the exact
product table that only 746825 occur even in (W-D)^2; the other 5796 quartic
moments are therefore certainly irrelevant to K^2 and can be deleted.  The
746825-coordinate set is sufficient, not claimed minimal after K compression.
"""
import sys,os,json,math,hashlib,subprocess,importlib.util,struct,shutil
from pathlib import Path
import numpy as np
import h5py

EXPECTED_MD5='b5223ca2fd5c4cbe52e93a23a4570b9f'
EXPECTED_A_SHA='5fc272a61a97c0aa9f42ef86266756500401c701a6f33a3b30bde4dbe6f113e5'
EXPECTED_SYSTEM_SHA='45621c09720050d0f6ffded8712d018c68eb6e72a93fc773cb940a00e3578fb8'
EXPECTED_COMPLETE_SHA='1b44a00376ba29e8c0815870c16f000c2f165573b299b522055b9e8ea701eb9c'
EXPECTED_ISOTYPIC_SHA='48a2ab8d4485825bf26c2903b7ded2331dc04af3927399e36cc54433bdeb865d'
EXPECTED_ACTION_SHA='1a5582d7fd1ce1c01135421413aa8fb7c6761fc953622e37387231f58c5f0097'
EXPECTED_NOGAP_SHA='44835ca3c57ca8b172a539c081a046a79282d15ae38c1968955bdb9871d3ccb8'
EXPECTED_DUALBASE_SHA='2dac591911395609f300260a704554a9b791433491b9584ae753fa0e97594149'
CVAL=2081044153087351400
N=300; ORDER=14400
OFFSETS={(2,0):1,(1,1):17,(0,2):39,(4,0):55,(3,1):47212,(2,2):234908,(1,3):517768,(0,4):705464}
EXPECTED_RAW={(4,0):47194,(3,1):187771,(2,2):282935,(1,3):187771,(0,4):47194}
EXPECTED_ORI={(4,0):47157,(3,1):187696,(2,2):282860,(1,3):187696,(0,4):47157}
BLOCK_SIZES=[582,465,611,211,611,822,235,162,107,397,504,43,17,107,166,235,162,504,384,286]

def die(s): raise SystemExit('ERROR: '+str(s))
def sha(path,kind='sha256'):
 h=getattr(hashlib,kind)();
 with open(path,'rb') as f:
  for z in iter(lambda:f.read(1<<20),b''):h.update(z)
 return h.hexdigest()
def load(path,name):
 sp=importlib.util.spec_from_file_location(name,path);m=importlib.util.module_from_spec(sp);sp.loader.exec_module(m);return m
def Ash(A):
 h=hashlib.sha256()
 for x in A.ravel(order='C'):h.update(int(x).to_bytes(8,'little',signed=True))
 return h.hexdigest()

def burnside(cert_elements):
 K=4; raw={(a,b):0 for a in range(5) for b in range(5-a)}; ori=raw.copy()
 for perm,sign in cert_elements:
  pr=[1]+[0]*K; ps=[1]+[0]*K; seen=[False]*N
  for i in range(N):
   if seen[i]:continue
   z=i;L=0;sg=1
   while not seen[z]:seen[z]=True;L+=1;sg*=int(sign[z]);z=int(perm[z])
   nr=pr[:];ns=ps[:]
   for d in range(K-L+1):nr[d+L]+=pr[d];ns[d+L]+=sg*ps[d]
   pr,ps=nr,ns
  for a in range(5):
   for b in range(5-a):raw[(a,b)]+=pr[a]*pr[b];ori[(a,b)]+=ps[a]*ps[b]
 for D in (raw,ori):
  for k in D:
   if D[k]%ORDER:die('Burnside nonintegral')
   D[k]//=ORDER
 return raw,ori

def make_deg2_maps(out,cert_elements):
 to0=[[] for _ in range(N)]
 for gi,(p,s) in enumerate(cert_elements):
  for i in range(N):
   if int(p[i])==0:to0[i].append(gi)
 if any(len(z)!=48 for z in to0):die('line stabilizer size !=48')
 summaries=[]
 for a,b,er,eo in [(2,0,18,16),(1,1,23,22),(0,2,18,16)]:
  if (a,b)==(2,0):keys=[((0,j),()) for j in range(1,N)]
  elif (a,b)==(0,2):keys=[((),(0,j)) for j in range(1,N)]
  else:keys=[((0,),(j,)) for j in range(N)]
  index={x:i for i,x in enumerate(keys)};oid=[-1]*len(keys);sgn=[0]*len(keys);reps=[];ok=[]
  for ii,S in enumerate(keys):
   if oid[ii]>=0:continue
   rid=len(reps);reps.append(S);ok.append(True);X,Y=S;anchors=X if a else Y
   for line in anchors:
    for gi in to0[line]:
     p,s=cert_elements[gi];XX=tuple(sorted(int(p[x]) for x in X));YY=tuple(sorted(int(p[y]) for y in Y));z=1
     for x in X:z*=int(s[x])
     for y in Y:z*=int(s[y])
     jj=index[(XX,YY)]
     if oid[jj]<0:oid[jj]=rid;sgn[jj]=z
     elif oid[jj]!=rid:die('deg2 orbit collision')
     elif sgn[jj]!=z:ok[rid]=False
   if sgn[ii]!=1:ok[rid]=False
   sgn[ii]=1
  if len(reps)!=er or sum(ok)!=eo:die('deg2 count mismatch')
  lid={r:k for k,r in enumerate([r for r in range(len(reps)) if ok[r]])};code=np.zeros(len(keys),dtype='<i4')
  for i,r in enumerate(oid):
   if ok[r]:code[i]=sgn[i]*(lid[r]+1)
  mf=out/f'moment_map_{a}_{b}.i32';code.tofile(mf);rf=out/f'moment_reps_{a}_{b}.txt'
  with open(rf,'w') as f:
   for r in range(len(reps)):
    if ok[r]:f.write(f'{lid[r]} X:{",".join(map(str,reps[r][0]))}, Y:{",".join(map(str,reps[r][1]))},\n')
  summaries.append({'a':a,'b':b,'raw_orbits':er,'orientable_orbits':eo,'map_sha256':sha(mf),'reps_sha256':sha(rf)})
 return summaries

def main():
 if len(sys.argv)!=7:die('usage: ... MAT SYSTEM COMPLETE NOGAP DUALBASE OUTDIR')
 mat,system_path,complete_path,nogap_path,dual_path,outdir=sys.argv[1:];out=Path(outdir);out.mkdir(parents=True,exist_ok=True)
 checks=[(sha(mat,'md5'),EXPECTED_MD5,'MAT md5'),(sha(system_path),EXPECTED_SYSTEM_SHA,'system sha'),(sha(complete_path),EXPECTED_COMPLETE_SHA,'complete sha'),(sha(nogap_path),EXPECTED_NOGAP_SHA,'nogap sha'),(sha(dual_path),EXPECTED_DUALBASE_SHA,'dual sha')]
 for got,want,n in checks:
  if got!=want:die(f'{n}: {got} != {want}')
 ng=load(nogap_path,'ng');base=load(dual_path,'dualbase');base.init_pairs();Q,Qdata,G,Hdata,ff=ng.structural_construction();system,els,gens,action=ng.load_and_match_certified_action(system_path,G)
 if action!=EXPECTED_ACTION_SHA:die('action hash')
 with h5py.File(mat,'r') as f:A=base.exact_int_matrix(f['A'][()],'A');ax=base.exact_sign_vector(f['ax'][()],'ax')
 if Ash(A)!=EXPECTED_A_SHA:die('A sha')
 complete=json.load(open(complete_path));
 if complete.get('final_status')!='PROVED_COMPLETE_K_DECOMPOSITION' or complete.get('isotypic_table_sha256')!=EXPECTED_ISOTYPIC_SHA:die('complete-K theorem mismatch')
 # Exact Burnside census.
 raw,ori=burnside(els)
 if [sum(raw[(a,k-a)] for a in range(k+1)) for k in range(5)] != [1,2,59,5500,752865]:die('raw Burnside totals')
 if [sum(ori[(a,k-a)] for a in range(k+1)) for k in range(5)] != [1,0,54,0,752566]:die('signed Burnside totals')
 # Group binaries.
 P=np.stack([p for p,s in els]).astype('<u2');S=np.stack([s for p,s in els]).astype('i1');P.tofile(out/'h4_perm_u16.bin');S.tofile(out/'h4_sign_i8.bin')
 deg2=make_deg2_maps(out,els)
 # Determine D and 54 non-D module reps.
 hright=[sum(int(ax[i])*int(A[i,j]) for i in range(N)) for j in range(N)];Z=[j for j,h in enumerate(hright) if h==0]
 pr,precs=base.enumerate_pair_support_orbits(gens);killed,kbool=base.killed_pair_data(pr,Z);rel,recs=base.enumerate_W_orbits(gens,pr,set(killed));non=[r for r in recs if not r['in_D']]
 if len(non)!=54:die('non-D orbit count')
 with open(out/'nonD_reps.bin','wb') as f:
  for r in non:
   ss=list(base.mid_support(r['rep_mid']));v=ss+[65535]*(2-len(ss));f.write(struct.pack('<BHH',len(ss),v[0],v[1]))
 json.dump([{'nonD_index':i,'orbit_id':r['orbit_id'],'rep_mid':r['rep_mid'],'type':r['type'],'support':list(base.mid_support(r['rep_mid'])),'size':r['size']} for i,r in enumerate(non)],open(out/'nonD_orbit_reps.json','w'),sort_keys=True,separators=(',',':'))
 # Helper sources beside this script.
 here=Path(__file__).resolve().parent; cpp1=here/'h4_moment_orbit_index.cpp';cpp2=here/'h4_product_moment_map.cpp'
 if not cpp1.exists() or not cpp2.exists():die('place the two C++ helpers beside this script')
 c1=out/'orbit_index';c2=out/'product_map_builder';subprocess.run(['g++','-O3','-std=c++17',str(cpp1),'-o',str(c1)],check=True);subprocess.run(['g++','-O3','-std=c++17',str(cpp2),'-o',str(c2)],check=True)
 subprocess.run([str(c1),str(out/'h4_perm_u16.bin'),str(out/'h4_sign_i8.bin'),str(out)],check=True)
 subprocess.run([str(c2),str(out/'h4_perm_u16.bin'),str(out/'h4_sign_i8.bin'),str(out/'nonD_reps.bin'),str(out),str(out/'product_map')],check=True)
 # Validate degree4 helper result against independent Burnside.
 q4=json.load(open(out/'moment_orbit_index_summary.json'))
 if q4['degree4_raw_total']!=752865 or q4['degree4_orientable_total']!=752566:die('quartic helper totals')
 # Exact objective coefficients on 55 lower moments.
 to0=[None]*N
 for gi,(p,s) in enumerate(els):
  for i in range(N):
   if to0[i] is None and int(p[i])==0:to0[i]=gi
 mp=np.fromfile(out/'moment_map_1_1.i32',dtype='<i4');bc=[0]*55
 for i in range(N):
  g=to0[i];p,s=els[g]
  for j in range(N):
   code=int(mp[int(p[j])])
   if code==0:
    if int(A[i,j])!=0:die('A nonzero on nonorientable xy orbit')
    continue
   orient=int(s[i])*int(s[j])*(1 if code>0 else -1);mid=17+abs(code)-1;bc[mid]+=int(A[i,j])*orient
 json.dump(bc,open(out/'objective_B_coeffs55.json','w'),separators=(',',':'))
 # Active non-D module indices per surviving irrep, exactly by finite-field character restriction.
 pmod=24001;active={};union=set();byid={int(r['gap_irrep_id']):r for r in complete['isotypic_blocks']}
 stabs=[base.orbit_stabilizer(r['rep_mid'],els) for r in non]
 for ri,meta in enumerate(Hdata['irreps']):
  if int(byid[ri+1]['m_K_if_certified'])==0:continue
  aa=[];tot=0;ch=Hdata['characters'][ri]
  for ni,r in enumerate(non):
   inds,chars=stabs[ni];v=sum(int(c)*int(ch[int(g)]) for g,c in zip(inds,chars))%pmod;v=v*pow(len(inds),pmod-2,pmod)%pmod
   if v:
    if v>int(meta['degree']):die('bad fixed multiplicity')
    aa.append((ni,int(r['orbit_id']),int(v)));union.add(ni);tot+=v
  if tot!=int(byid[ri+1]['m_W_minus_D_exact']):die('m(W-D) character audit')
  active[ri+1]=aa
 if sorted(set(range(54))-union)!=[1,2]:die('surviving K should exclude only odd x,y modules')
 # Product table exact support sizes.
 ids=np.memmap(out/'product_map.id.i32',dtype='<i4',mode='r',shape=(1485,ORDER));pairidx={}
 for line in open(out/'product_map.pairs.txt'):
  z,i,j=map(int,line.split());pairidx[(i,j)]=z
 global_ids=np.unique(ids);global_ids=global_ids[global_ids>=0];effective=len(global_ids)
 if effective!=746825:die('effective moment count !=746825')
 blockrows=[]; support_cache={}
 for ir in range(1,21):
  inds0=sorted(set(x[0] for x in active[ir])); key=tuple(inds0); ps=[]
  for ai,i in enumerate(inds0):
   for j in inds0[ai:]:ps.append(pairidx[(i,j)])
  if key not in support_cache:
   touched=np.zeros(752621,dtype=np.bool_)
   for pp in ps:
    row=ids[pp]; z=row[row>=0]; touched[z]=True
   support_cache[key]=(int(touched.sum()),int(touched[55:].sum()),int(touched[1:55].sum()))
  nm,nq,n2=support_cache[key]
  blockrows.append({'gap_irrep_id':ir,'degree':int(Hdata['irreps'][ir-1]['degree']),'matrix_size':int(byid[ir]['m_K_if_certified']),'symmetric_coordinates':int(byid[ir]['m_K_if_certified'])*(int(byid[ir]['m_K_if_certified'])+1)//2,'active_monomial_modules':len(inds0),'orbit_module_pairs':len(ps),'precompression_moment_coordinates_touched':nm,'precompression_quartic_coordinates_touched':nq,'precompression_quadratic_coordinates_touched':n2})
 spec={'status':'EXACT_FULL_INVARIANT_DUAL_SPEC_CONSTRUCTED','provenance':{'mat_md5':EXPECTED_MD5,'A_sha256':EXPECTED_A_SHA,'system_sha256':EXPECTED_SYSTEM_SHA,'complete_K_output_sha256':EXPECTED_COMPLETE_SHA,'complete_K_isotypic_sha256':EXPECTED_ISOTYPIC_SHA,'action_sha256':EXPECTED_ACTION_SHA,'nogap_sha256':EXPECTED_NOGAP_SHA,'dualbase_sha256':EXPECTED_DUALBASE_SHA},'averaging_reduction':'barL(p)=|G|^-1 sum_g L(gp); K and f are G-invariant, so positivity on K and L(f)<0 are preserved','moment_coordinates':{'raw_support_orbits_by_total_degree':[1,2,59,5500,752865],'orientable_signed_orbits_by_total_degree':[1,0,54,0,752566],'total_invariant_moments_through_degree4':752621,'coordinates_after_proved_WminusD_product_pruning':effective,'provably_irrelevant_quartic_coordinates':752621-effective,'additional_redundancy_after_K_compression_not_computed':True,'bidegree4':{f'{a},{4-a}':{'raw':raw[(a,4-a)],'orientable':ori[(a,4-a)]} for a in range(5)},'global_offsets':{f'{a},{b}':v for (a,b),v in OFFSETS.items()}},'normalization':{'equation':'C*theta[0] - sum_t objective_B_coeffs55[t]*theta[t] = -1','C':CVAL,'objective_B_coeffs55_sha256':sha(out/'objective_B_coeffs55.json')},'block_pencils':blockrows,'total_real_symmetric_block_coordinates':sum(x['symmetric_coordinates'] for x in blockrows),'product_table':{'pair_count':1485,'group_order':ORDER,'id_shape':[1485,ORDER],'id_sha256':sha(out/'product_map.id.i32'),'sign_sha256':sha(out/'product_map.sgn.i8'),'pairs_sha256':sha(out/'product_map.pairs.txt'),'nonD_reps_sha256':sha(out/'nonD_reps.bin')},'exact_pencil_formula':'M_rho(theta)=Z_rho^* B_rho(theta) Z_rho; B_(O,a),(Oprime,b)=1/sqrt(|H_O||H_Oprime|) v_O,a^* [sum_g sigma_OOprime(g)*theta[kappa_OOprime(g)] rho(g)] v_Oprime,b. Corrected residual map defining Z uses r(g^{-1}m).','feasibility':'find theta in R^746825 with normalization and all 20 M_rho(theta) positive semidefinite'}
 rawjs=json.dumps(spec,sort_keys=True,separators=(',',':')).encode();(out/'full_invariant_dual_spec.json').write_bytes(rawjs);display=dict(spec);display['output_sha256']=hashlib.sha256(rawjs).hexdigest();print(json.dumps(display,indent=2,sort_keys=True))
if __name__=='__main__':main()
