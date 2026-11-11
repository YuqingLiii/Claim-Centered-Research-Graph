#!/usr/bin/env python3
"""
Exact ambient refutation of the alpha=2/3 full-K dual candidate.
Python 3.9+; dependencies numpy,h5py,sympy.
No Sage, no floating eigenvalues, no numerical nullspaces.

Witness:
  q = -Phi_673 + Phi_727,
  Phi_m = (1/|H_m|) sum_{g in H4} rho(g) (g . z_m),
where rho is the Coxeter sign character and z_m is the squarefree monomial
with degree<=2 monomial ID m.

The verifier proves:
  * |H_673|=|H_727|=4 and both stabilizer signed characters equal rho;
  * Phi_673,Phi_727 have disjoint support of size 3600 and coefficients +/-1;
  * every one of the 14 base residual equality functionals annihilates q;
  * each Coxeter generator sends q to -q, hence every H4 translate of every
    base restriction also annihilates q, so q lies in the certified K;
  * using the complete four-distinct Boolean moment formula with alpha=2/3,
       L(q^2) = 600*(1-sqrt(5)) < 0.
Thus mu^*(L_{2/3}) is NOT PSD on K.
"""
import sys,json,hashlib,math
import numpy as np,h5py,sympy as sp
sys.path.insert(0,'/mnt/data')
import h4_K_full_dual_slice_release as base
import h4_nogap_irrep_cache as ng
import h4_K_alpha23_exact_ldlt as ex

EXPECTED_REFUTATION_SHA='74326f9ed3ab9aacb37a82ab753af84c4bf2a14b96f00547575f2a2f61209dbb'


def sha_file(p):
 h=hashlib.sha256();
 with open(p,'rb') as f:
  for b in iter(lambda:f.read(1<<20),b''): h.update(b)
 return h.hexdigest()


def act_poly(coeff,p,s):
 out=np.zeros_like(coeff)
 nz=np.flatnonzero(coeff)
 for m in nz:
  mm,sg=base.act_mid(int(m),p,s)
  out[mm]+=int(coeff[m])*int(sg)
 return out


def main():
 if len(sys.argv)!=4:
  raise SystemExit('usage: python h4_alpha23_irrep13_ambient_verifier.py MAT SYSTEM_JSON COMPLETE_K_JSON')
 mat,system_path,complete_path=sys.argv[1:]
 base.init_pairs()
 if base.md5_file(mat)!=base.EXPECTED_MD5: raise RuntimeError('MAT MD5 mismatch')
 with h5py.File(mat,'r') as f:
  A=base.exact_int_matrix(f['A'][()],'A'); P=np.asarray(f['P'][()],float)
  ax=base.exact_sign_vector(f['ax'][()],'ax'); by=base.exact_sign_vector(f['by'][()],'by')
 if base.canonical_A_sha(A)!=base.EXPECTED_A_SHA: raise RuntimeError('A SHA mismatch')
 complete=json.load(open(complete_path))
 if complete['final_status']!='PROVED_COMPLETE_K_DECOMPOSITION': raise RuntimeError('K not certified')
 if complete['isotypic_table_sha256']!=base.EXPECTED_ISOTYPIC_SHA: raise RuntimeError('K table SHA mismatch')
 ir13=[r for r in complete['isotypic_blocks'] if int(r['gap_irrep_id'])==13][0]
 if (int(ir13['degree']),int(ir13['m_W_minus_D_exact']),int(ir13['m_K_if_certified']))!=(1,19,17):
  raise RuntimeError('irrep13 metadata mismatch')

 Q,Qdata,G,Hdata,ff=ng.structural_construction()
 system,cert_elements,cert_gens,action_sha=ng.load_and_match_certified_action(system_path,G)
 if action_sha!=base.EXPECTED_ACTION_SHA: raise RuntimeError('action SHA mismatch')

 # Coxeter sign character in structural BFS ordering.
 rho=np.empty(base.ORDER,dtype=np.int8); rho[0]=1
 for a in range(1,base.ORDER): rho[a]=-rho[int(G['parent'][a])]
 raw=b''.join(int(int(x)%base.PRIME).to_bytes(4,'little') for x in rho)
 charsha=hashlib.sha256(raw).hexdigest()
 if charsha!=ir13['full_character_sha256_mod_p']: raise RuntimeError('sign character hash mismatch')

 # D and base residual restrictions.
 pair_rel,_=base.enumerate_pair_support_orbits(cert_gens)
 hright=[sum(int(ax[i])*int(A[i,j]) for i in range(300)) for j in range(300)]
 Z=[j for j,h in enumerate(hright) if h==0]
 if Z!=[46,56,85,99,131,148]: raise RuntimeError('zero set mismatch')
 killed_ids,killed_bool=base.killed_pair_data(pair_rel,Z)
 faceR=base.Face(ax,by,'y',Z); faceL=base.Face(by,ax,'x',Z)
 Rseed=np.vstack([base.direct_residual_seed_matrix(faceR,killed_bool),base.direct_residual_seed_matrix(faceL,killed_bool)]).astype(np.int64)
 _,orbit_records=base.enumerate_W_orbits(cert_gens,pair_rel,set(killed_ids))
 rec_by_mid={int(r['rep_mid']):r for r in orbit_records}
 mids=(673,727)
 for m in mids:
  if rec_by_mid[m]['in_D']: raise RuntimeError('witness orbit unexpectedly lies in D')

 # Exact signed orbit eigenvectors Phi_m.
 phis=[]; stab_orders=[]; support_sizes=[]; phihashes=[]
 for m in mids:
  inds,chars=base.orbit_stabilizer(m,cert_elements)
  if not all(int(chars[k])==int(rho[int(g)]) for k,g in enumerate(inds)):
   raise RuntimeError('stabilizer character mismatch at m=%d'%m)
  H=len(inds); stab_orders.append(H)
  acc=np.zeros(base.MON_DIM,dtype=np.int32)
  for g,(p,s) in enumerate(cert_elements):
   mm,sg=base.act_mid(m,p,s)
   acc[mm]+=int(rho[g])*int(sg)
  if np.any(acc%H): raise RuntimeError('orbit Reynolds sum not divisible by stabilizer')
  phi=(acc//H).astype(np.int8)
  vals=set(int(x) for x in phi)
  if not vals.issubset({-1,0,1}): raise RuntimeError('Phi coefficients not 0,+/-1')
  supp=int(np.count_nonzero(phi)); support_sizes.append(supp)
  if supp!=int(rec_by_mid[m]['size']): raise RuntimeError('orbit support-size mismatch')
  phis.append(phi)
  phihashes.append(hashlib.sha256(phi.tobytes()).hexdigest())

 if stab_orders!=[4,4] or support_sizes!=[3600,3600]: raise RuntimeError('unexpected witness orbit census')
 if np.any((phis[0]!=0)&(phis[1]!=0)): raise RuntimeError('two witness orbit supports overlap')
 q=(-phis[0].astype(np.int16)+phis[1].astype(np.int16))
 if np.count_nonzero(q)!=7200 or set(int(x) for x in q)!={-1,0,1}: raise RuntimeError('q support/coset coefficients wrong')
 qhash=hashlib.sha256(q.astype(np.int8).tobytes()).hexdigest()

 # Base restrictions vanish exactly.
 base_res=(Rseed.astype(np.int64)@q.astype(np.int64))
 if np.any(base_res): raise RuntimeError('base residual restrictions do not annihilate q: %r'%base_res.tolist())

 # q is a sign eigenvector under all four Coxeter generators.
 generator_res=[]
 for gi,(p,s) in enumerate(cert_gens):
  gq=act_poly(q,p,s)
  ok=bool(np.array_equal(gq,-q))
  generator_res.append(ok)
  if not ok: raise RuntimeError('q is not sign-covariant under generator %d'%gi)
 # Therefore for arbitrary g, gq=rho(g)q by generation; together with base_res=0
 # all translated residual restrictions vanish.

 # Exact P and the 2x2 group-Fourier moment matrix on the two orbit modules.
 pe=base.reconstruct_P_exact_and_AP(A,P)
 PX=np.asarray(pe['X'],np.int64); PY=np.asarray(pe['Y'],np.int64); PD=int(pe['D'])
 idx=np.arange(600)%300; X6=PX[np.ix_(idx,idx)]; Y6=PY[np.ix_(idx,idx)]
 trans=[ex.transformed_arrays(base,m,cert_elements) for m in mids]
 F0=np.zeros((2,2),dtype=object); F1=np.zeros((2,2),dtype=object)
 for i,m in enumerate(mids):
  for j in range(2):
   e0,e1=ex.ell_scaled_for_pair(base,m,trans[j],X6,Y6,PD)
   F0[i,j]=sum(int(rho[g])*int(e0[g]) for g in range(base.ORDER))
   F1[i,j]=sum(int(rho[g])*int(e1[g]) for g in range(base.ORDER))
 if not np.array_equal(F0,F0.T) or not np.array_equal(F1,F1.T): raise RuntimeError('2x2 Fourier form not symmetric')

 # multiplicity vector y=(-1,+1), exactly the ambient q above.
 y=np.array([-1,1],dtype=object)
 qa=int(y@F0@y); qb=int(y@F1@y)
 if (qa,qb)!=(128,-128): raise RuntimeError('unexpected scaled Fourier value %r'%((qa,qb),))
 # common ell denominator is 3D^2; ambient orbit sum contributes |G|/(H_i H_j)=900
 # because both H_i=H_j=4.
 DL=3*PD*PD
 if DL!=192: raise RuntimeError('unexpected moment denominator %d'%DL)
 factor=base.ORDER//(4*4)
 if factor!=900: raise RuntimeError('orbit normalization factor !=900')
 # L(q^2)=900*(128-128sqrt5)/192 = 600*(1-sqrt5).
 from fractions import Fraction
 la=Fraction(factor*qa,DL); lb=Fraction(factor*qb,DL)
 if (la,lb)!=(Fraction(600),Fraction(-600)): raise RuntimeError('ambient q^2 value did not simplify to 600(1-sqrt5)')
 if not (la>0 and lb<0 and la*la < 5*lb*lb): raise RuntimeError('exact negativity sign test failed')

 # Independent direct normalization identity for the group averaging derivation.
 # Phi_i=(1/H_i)sum_a rho(a) a.m_i. Invariance of L yields
 # L(Phi_i Phi_j)=|G|/(H_i H_j) sum_k rho(k)L(m_i*k.m_j).
 normalization_identity='L(Phi_i Phi_j)=14400/(H_i H_j) * F_ij, with H_i=H_j=4'

 out={
  'status':'REFUTED_ALPHA_2_OVER_3',
  'proof_status':'PROVED_EXACT_AMBIENT_NEGATIVE_WITNESS',
  'block':{
   'gap_irrep_id':13,'degree':1,'m_W_minus_D_exact':19,'residual_rank_exact':2,'mK':17,
   'character_sha256_mod_p':charsha,
  },
  'witness':{
   'formula':'q=-Phi_673+Phi_727; Phi_m=(1/|H_m|) sum_g rho(g) (g.z_m)',
   'rep_mids':[673,727],'orbit_ids':[int(rec_by_mid[m]['orbit_id']) for m in mids],
   'stabilizer_orders':stab_orders,'orbit_support_sizes':support_sizes,
   'Phi_sha256':phihashes,'q_coefficient_sha256':qhash,'q_nonzero_coefficients':7200,
   'base_14_restrictions':[int(x) for x in base_res],
   'coxeter_generator_covariance_q_to_minus_q':generator_res,
   'therefore_all_H4_translated_restrictions_zero':True,
  },
  'moment':{
   'boolean_four_distinct_formula':'(2/3)*(X_ab*X_cd+X_ac*X_bd+X_ad*X_bc)',
   'reduce_repeated_variables_first':True,
   'scaled_2x2_F_rational':[[int(F0[i,j]) for j in range(2)] for i in range(2)],
   'scaled_2x2_F_sqrt5':[[int(F1[i,j]) for j in range(2)] for i in range(2)],
   'common_positive_denominator':DL,
   'multiplicity_vector':[-1,1],
   'scaled_quadratic_value':'128-128*sqrt(5)',
   'orbit_average_factor':factor,
   'normalization_identity':normalization_identity,
   'ambient_L_q2':'600-600*sqrt(5)',
   'ambient_L_q2_sign_exact':-1,
   'exact_sign_test':'600^2 < 5*600^2',
  },
  'provenance':{
   'mat_md5':base.EXPECTED_MD5,'A_sha256':base.EXPECTED_A_SHA,'action_sha256':base.EXPECTED_ACTION_SHA,
   'complete_K_isotypic_sha256':base.EXPECTED_ISOTYPIC_SHA,
   'complete_K_output_sha256':sha_file(complete_path),
  },
  'preserved_facts':{
   'prior_invariant_seed_SOS_test':'INCONCLUSIVE',
   'rank4_full_elliptope_extension':'PROVED_IMPOSSIBLE',
  }
 }
 raw=json.dumps(out,sort_keys=True,separators=(',',':')).encode()
 outpath=mat+'.alpha23_irrep13_ambient_refutation.json'; open(outpath,'wb').write(raw)
 disp=dict(out); disp['output_path']=outpath; disp['output_sha256']=hashlib.sha256(raw).hexdigest()
 print(json.dumps(disp,indent=2,sort_keys=True))

if __name__=='__main__': main()
