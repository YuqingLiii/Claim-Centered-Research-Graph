#!/usr/bin/env python3
"""
Exact finite refutation of the entire affine dual family L_alpha.
Python 3.9+; numpy,h5py,sympy. No Sage and no numerical eigenvalues.

For every real alpha, one of two explicit complete-K polynomials has
L_alpha(q^2)<0:

  q_- = Phi^sgn_1145,
  L_alpha(q_-^2)=7200(alpha-1).

  q_+ = -68 + 2 Phi^triv_601 - Phi^triv_613
        + 4 Phi^triv_900 + Phi^triv_1086,
  L_alpha(q_+^2)=724+4500 sqrt(5)
                 -(675+12375 sqrt(5)) alpha.

Here
 Phi^chi_m = (1/|H_m|) sum_g chi(g) (g.z_m)
for chi either the trivial or Coxeter-sign character and H_m the signed
stabilizer of monomial m. The script verifies both polynomials lie in the
certified K by exact base-restriction annihilation plus generator covariance.
It independently reconstructs the affine moment formulas via the full
14400-element group Fourier sum in Q(sqrt(5)).
"""
import sys,json,hashlib,math
from fractions import Fraction
import numpy as np,h5py,sympy as sp

if len(sys.argv) not in (4,):
    raise SystemExit('usage: python h4_full_affine_family_exact_refuter.py MAT SYSTEM_JSON COMPLETE_K_JSON')
mat,system_path,complete_path=sys.argv[1:]
sys.path.insert(0,'/mnt/data')
import h4_K_full_dual_slice_release as base
import h4_nogap_irrep_cache as ng

EXPECTED_AMBIENT_ALPHA23_SHA='560163be3dfc9900adb8e6df9ce0885ac88a70af10551a34cf51a7ea25e8f9cf'
EXPECTED_NOGAP_SHA='44835ca3c57ca8b172a539c081a046a79282d15ae38c1968955bdb9871d3ccb8'
EXPECTED_DUALBASE_SHA='2dac591911395609f300260a704554a9b791433491b9584ae753fa0e97594149'
EXPECTED_SYSTEM_SHA='45621c09720050d0f6ffded8712d018c68eb6e72a93fc773cb940a00e3578fb8'
EXPECTED_COMPLETE_SHA='1b44a00376ba29e8c0815870c16f000c2f165573b299b522055b9e8ea701eb9c'


def sha_file(p):
    h=hashlib.sha256()
    with open(p,'rb') as f:
        for b in iter(lambda:f.read(1<<20),b''):h.update(b)
    return h.hexdigest()


if sha_file(base.__file__)!=EXPECTED_DUALBASE_SHA:raise RuntimeError('dual-base source SHA mismatch')
if sha_file(ng.__file__)!=EXPECTED_NOGAP_SHA:raise RuntimeError('no-GAP source SHA mismatch')
if sha_file(system_path)!=EXPECTED_SYSTEM_SHA:raise RuntimeError('system JSON SHA mismatch')
if sha_file(complete_path)!=EXPECTED_COMPLETE_SHA:raise RuntimeError('complete-K JSON SHA mismatch')


def q5mul(x1,y1,x2,y2):
    return x1*x2+5*y1*y2,x1*y2+y1*x2


def q5sign(a,b):
    a=Fraction(a);b=Fraction(b)
    if b==0:return (a>0)-(a<0)
    if a==0:return (b>0)-(b<0)
    if a>0 and b>0:return 1
    if a<0 and b<0:return -1
    lhs=a*a;rhs=5*b*b
    if lhs==rhs:return 0
    if a>0 and b<0:return 1 if lhs>rhs else -1
    return -1 if lhs>rhs else 1


def act_poly(coeff,p,s):
    out=np.zeros_like(coeff)
    for m in np.flatnonzero(coeff):
        mm,sg=base.act_mid(int(m),p,s)
        out[mm]+=int(coeff[m])*int(sg)
    return out


def transformed(rep_mid,cert_elements):
    S=base.mid_support(rep_mid);deg=len(S)
    sg=np.empty(base.ORDER,dtype=np.int64)
    aa=np.full(base.ORDER,-1,dtype=np.int16)
    bb=np.full(base.ORDER,-1,dtype=np.int16)
    for g,(p,s) in enumerate(cert_elements):
        mm,z=base.act_mid(rep_mid,p,s);ss=base.mid_support(mm)
        sg[g]=int(z)
        if len(ss):aa[g]=ss[0]
        if len(ss)==2:bb[g]=ss[1]
    return {'deg':deg,'sign':sg,'a':aa,'b':bb}


def ell_affine_scaled_D2(rep_mid,tr,X6,Y6,D):
    """D^2 ell_alpha(g)=(a0+b0 sqrt5)+alpha(a1+b1 sqrt5)."""
    S=base.mid_support(rep_mid);d1=len(S);d2=int(tr['deg']);sg=tr['sign']
    Z=np.zeros(base.ORDER,dtype=np.int64)
    a0=Z.copy();b0=Z.copy();a1=Z.copy();b1=Z.copy()
    if (d1+d2)&1:return a0,b0,a1,b1
    if d1==0 and d2==0:
        a0=sg*D*D;return a0,b0,a1,b1
    if d1==0 and d2==2:
        a=tr['a'].astype(np.int64);b=tr['b'].astype(np.int64)
        return sg*D*X6[a,b],sg*D*Y6[a,b],a1,b1
    if d1==2 and d2==0:
        a,b=S;a0[:]=sg*D*int(X6[a,b]);b0[:]=sg*D*int(Y6[a,b]);return a0,b0,a1,b1
    if d1==1 and d2==1:
        a=S[0];c=tr['a'].astype(np.int64);same=(c==a)
        a0[same]=sg[same]*D*D;ns=~same
        a0[ns]=sg[ns]*D*X6[a,c[ns]];b0[ns]=sg[ns]*D*Y6[a,c[ns]]
        return a0,b0,a1,b1
    if d1!=2 or d2!=2:return a0,b0,a1,b1
    a,b=S;c=tr['a'].astype(np.int64);d=tr['b'].astype(np.int64)
    eq=((c==a)&(d==b))|((c==b)&(d==a));a0[eq]=sg[eq]*D*D
    sharea=(c==a)|(d==a);shareb=(c==b)|(d==b);share=(sharea|shareb)&(~eq)
    ii=np.flatnonzero(share)
    if len(ii):
        cc=c[ii];dd=d[ii];rem1=np.where(sharea[ii],b,a)
        shared=np.where((cc==a)|(cc==b),cc,dd);rem2=np.where(cc==shared,dd,cc)
        a0[ii]=sg[ii]*D*X6[rem1,rem2];b0[ii]=sg[ii]*D*Y6[rem1,rem2]
    dis=(~eq)&(~share);ii=np.flatnonzero(dis)
    if len(ii):
        cc=c[ii];dd=d[ii]
        r0,r1=q5mul(int(X6[a,b]),int(Y6[a,b]),X6[cc,dd],Y6[cc,dd])
        s0,s1=q5mul(X6[a,cc],Y6[a,cc],X6[b,dd],Y6[b,dd])
        t0,t1=q5mul(X6[a,dd],Y6[a,dd],X6[b,cc],Y6[b,cc])
        a1[ii]=sg[ii]*(r0+s0+t0);b1[ii]=sg[ii]*(r1+s1+t1)
    return a0,b0,a1,b1


def make_phi(m,chi,cert_elements,rec_by_mid):
    inds,chars=base.orbit_stabilizer(m,cert_elements)
    if not all(int(chars[k])==int(chi[int(g)]) for k,g in enumerate(inds)):
        raise RuntimeError('stabilizer character mismatch m=%d'%m)
    H=len(inds);acc=np.zeros(base.MON_DIM,dtype=np.int32)
    for g,(p,s) in enumerate(cert_elements):
        mm,sg=base.act_mid(m,p,s);acc[mm]+=int(chi[g])*int(sg)
    if np.any(acc%H):raise RuntimeError('Reynolds numerator not divisible by H')
    phi=(acc//H).astype(np.int16)
    if not set(int(x) for x in phi).issubset({-1,0,1}):raise RuntimeError('Phi coefficients not +/-1')
    if np.count_nonzero(phi)!=int(rec_by_mid[m]['size']):raise RuntimeError('Phi orbit-size mismatch')
    return phi,H,hashlib.sha256(phi.astype(np.int8).tobytes()).hexdigest()


def affine_moment_of_phi_combination(mids,coeffs,chi,Hs,cert_elements,X6,Y6,D):
    tr=[transformed(m,cert_elements) for m in mids]
    out=[Fraction(0) for _ in range(4)]
    # ambient formula |G|/(Hi Hj) * Fourier / D^2
    for i,m in enumerate(mids):
        for j in range(len(mids)):
            e=ell_affine_scaled_D2(m,tr[j],X6,Y6,D)
            f=[sum(int(chi[g])*int(arr[g]) for g in range(base.ORDER)) for arr in e]
            fac=Fraction(base.ORDER*coeffs[i]*coeffs[j],Hs[i]*Hs[j]*D*D)
            for k in range(4):out[k]+=fac*f[k]
    return tuple(out)

# provenance and certified data
base.init_pairs()
if base.md5_file(mat)!=base.EXPECTED_MD5:raise RuntimeError('MAT MD5 mismatch')
with h5py.File(mat,'r') as f:
    A=base.exact_int_matrix(f['A'][()],'A');P=np.asarray(f['P'][()],float)
    ax=base.exact_sign_vector(f['ax'][()],'ax');by=base.exact_sign_vector(f['by'][()],'by')
if base.canonical_A_sha(A)!=base.EXPECTED_A_SHA:raise RuntimeError('A SHA mismatch')
complete=json.load(open(complete_path))
if complete['final_status']!='PROVED_COMPLETE_K_DECOMPOSITION':raise RuntimeError('complete K not proved')
if complete['isotypic_table_sha256']!=base.EXPECTED_ISOTYPIC_SHA:raise RuntimeError('K table hash mismatch')

Q,Qdata,G,Hdata,ff=ng.structural_construction()
system,cert_elements,cert_gens,action_sha=ng.load_and_match_certified_action(system_path,G)
if action_sha!=base.EXPECTED_ACTION_SHA:raise RuntimeError('action hash mismatch')
triv=np.ones(base.ORDER,dtype=np.int8)
sign=np.empty(base.ORDER,dtype=np.int8);sign[0]=1
for g in range(1,base.ORDER):sign[g]=-sign[int(G['parent'][g])]
# character hashes against complete K IDs 12 and 13
for rid,ch in ((12,triv),(13,sign)):
    rec=[r for r in complete['isotypic_blocks'] if int(r['gap_irrep_id'])==rid][0]
    raw=b''.join(int(int(x)%base.PRIME).to_bytes(4,'little') for x in ch)
    if hashlib.sha256(raw).hexdigest()!=rec['full_character_sha256_mod_p']:
        raise RuntimeError('character hash mismatch irrep %d'%rid)

pair_rel,_=base.enumerate_pair_support_orbits(cert_gens)
hright=[sum(int(ax[i])*int(A[i,j]) for i in range(base.N)) for j in range(base.N)]
Zlines=[j for j,h in enumerate(hright) if h==0]
if Zlines!=[46,56,85,99,131,148]:raise RuntimeError('zero set mismatch')
killed_ids,killed_bool=base.killed_pair_data(pair_rel,Zlines)
faceR=base.Face(ax,by,'y',Zlines);faceL=base.Face(by,ax,'x',Zlines)
Rseed=np.vstack([base.direct_residual_seed_matrix(faceR,killed_bool),base.direct_residual_seed_matrix(faceL,killed_bool)]).astype(np.int64)
_,orbit_records=base.enumerate_W_orbits(cert_gens,pair_rel,set(killed_ids));rec_by_mid={int(r['rep_mid']):r for r in orbit_records}

# exact P
pe=base.reconstruct_P_exact_and_AP(A,P);PX=np.asarray(pe['X'],np.int64);PY=np.asarray(pe['Y'],np.int64);D=int(pe['D'])
idx=np.arange(600)%300;X6=PX[np.ix_(idx,idx)];Y6=PY[np.ix_(idx,idx)]
if D!=8:raise RuntimeError('unexpected P denominator')

# Witness 1: sign orbit Phi_1145
phiM,HM,hM=make_phi(1145,sign,cert_elements,rec_by_mid)
if HM!=2:raise RuntimeError('Phi_1145 stabilizer !=2')
qminus=phiM.copy();bres1=<email-redacted>(np.int64)
if np.any(bres1):raise RuntimeError('qminus base restrictions nonzero')
if not all(np.array_equal(act_poly(qminus,p,s),-qminus) for p,s in cert_gens):raise RuntimeError('qminus sign covariance failed')
form1=affine_moment_of_phi_combination([1145],[1],sign,[HM],cert_elements,X6,Y6,D)
if form1!=(Fraction(-7200),Fraction(0),Fraction(7200),Fraction(0)):
    raise RuntimeError('qminus affine form mismatch %r'%(form1,))

# Previously certified alpha=2/3 witness, now extended exactly for all alpha.
old_mids=[673,727];old_coeff=[-1,1];old_phis=[];old_H=[];old_hash=[]
for m in old_mids:
    ph,H,h=make_phi(m,sign,cert_elements,rec_by_mid);old_phis.append(ph);old_H.append(H);old_hash.append(h)
qold=-old_phis[0].astype(np.int32)+old_phis[1].astype(np.int32)
old_bres=<email-redacted>(np.int64)
if np.any(old_bres):raise RuntimeError('previous q base restrictions nonzero')
if not all(np.array_equal(act_poly(qold,p,s),-qold) for p,s in cert_gens):raise RuntimeError('previous q sign covariance failed')
old_form=affine_moment_of_phi_combination(old_mids,old_coeff,sign,old_H,cert_elements,X6,Y6,D)
if old_form!=(Fraction(-7200),Fraction(0),Fraction(11700),Fraction(-900)):
    raise RuntimeError('previous q affine extension mismatch %r'%(old_form,))
old_gamma0=Fraction(26,41);old_gamma1=Fraction(2,41)

# Witness 2: invariant five-term combination
mids2=[0,601,613,900,1086];coeff2=[-68,2,-1,4,1]
phis=[];Hs=[];hashes=[]
for m in mids2:
    ph,H,h=make_phi(m,triv,cert_elements,rec_by_mid);phis.append(ph);Hs.append(H);hashes.append(h)
if Hs!=[14400,24,4,48,4]:raise RuntimeError('qplus stabilizer census mismatch %r'%Hs)
qplus=np.zeros(base.MON_DIM,dtype=np.int32)
for c,ph in zip(coeff2,phis):qplus+=int(c)*ph.astype(np.int32)
bres2=<email-redacted>(np.int64)
if np.any(bres2):raise RuntimeError('qplus base restrictions nonzero %r'%bres2.tolist())
if not all(np.array_equal(act_poly(qplus,p,s),qplus) for p,s in cert_gens):raise RuntimeError('qplus invariance failed')
form2=affine_moment_of_phi_combination(mids2,coeff2,triv,Hs,cert_elements,X6,Y6,D)
expected2=(Fraction(724),Fraction(4500),Fraction(-675),Fraction(-12375))
if form2!=expected2:raise RuntimeError('qplus affine form mismatch %r'% (form2,))

# threshold beta and exact coverage
# beta=(724+4500s)/(675+12375s), denominator positive.
beta_num=(Fraction(724),Fraction(4500));beta_den=(Fraction(675),Fraction(12375))
if q5sign(*beta_num)<=0 or q5sign(*beta_den)<=0:raise RuntimeError('beta signs wrong')
# beta < 1 iff denominator-numerator=(-49)+7875 sqrt5 >0.
if q5sign(Fraction(-49),Fraction(7875))<=0:raise RuntimeError('beta<1 proof failed')
# rationalized closed form
# (a+bs)/(c+ds)=((ac-5bd)+(bc-ad)s)/(c^2-5d^2)
a,b=beta_num;c,d=beta_den
denrat=c*c-5*d*d
brat0=(a*c-5*b*d)/denrat;brat1=(b*c-a*d)/denrat
if q5sign(brat0,brat1)<=0:raise RuntimeError('rationalized beta not positive')

qminus_hash=hashlib.sha256(qminus.astype(np.int16).tobytes()).hexdigest()
qplus_hash=hashlib.sha256(qplus.astype(np.int32).tobytes()).hexdigest()

out={
 'status':'PROVED_NO_ALPHA_FEASIBLE_IN_AFFINE_FAMILY',
 'proof_status':'PROVED_EXACT_FINITE_COVERING',
 'family':{
  'L_degree2':'X_ab with X=[[P,P],[P,P]]',
  'L_odd':'0',
  'L_four_distinct':'alpha*(X_ab*X_cd+X_ac*X_bd+X_ad*X_bc)',
  'boolean_reduction_first':True,
  'separation_objective':'C-<A,P>, independent of alpha and exactly negative',
 },
 'previous_alpha23_witness_affine_extension':{
  'formula':'q_old=-Phi_sign_673+Phi_sign_727',
  'rep_mids':old_mids,'stabilizer_orders':old_H,'Phi_sha256':old_hash,
  'q_coefficient_sha256':hashlib.sha256(qold.astype(np.int16).tobytes()).hexdigest(),
  'base_14_restrictions':[int(x) for x in old_bres],
  'L_alpha_q2':'900*((13-sqrt(5))*alpha-8)',
  'critical_alpha':'(26+2*sqrt(5))/41',
  'negative_region':'alpha < (26+2*sqrt(5))/41',
  'alpha_2_over_3_value':'600*(1-sqrt(5))',
 },
 'witness_alpha_less_than_1':{
  'irrep_id':13,'character':'Coxeter sign','formula':'q_minus=Phi_sign_1145',
  'rep_mids':[1145],'stabilizer_orders':[HM],'Phi_sha256':[hM],
  'q_coefficient_sha256':qminus_hash,'q_nonzero_coefficients':int(np.count_nonzero(qminus)),
  'base_14_restrictions':[int(x) for x in bres1],
  'generator_covariance':'g_i q_minus = -q_minus for all four Coxeter generators',
  'L_alpha_q2':'7200*(alpha-1)',
  'negative_region':'alpha < 1',
 },
 'witness_alpha_greater_than_beta':{
  'irrep_id':12,'character':'trivial',
  'formula':'q_plus=-68+2*Phi_601-Phi_613+4*Phi_900+Phi_1086',
  'rep_mids':mids2,'coefficients':coeff2,'stabilizer_orders':Hs,'Phi_sha256':hashes,
  'q_coefficient_sha256':qplus_hash,'q_nonzero_coefficients':int(np.count_nonzero(qplus)),
  'base_14_restrictions':[int(x) for x in bres2],
  'generator_covariance':'g_i q_plus = q_plus for all four Coxeter generators',
  'L_alpha_q2':'724+4500*sqrt(5)-(675+12375*sqrt(5))*alpha',
  'beta':'(724+4500*sqrt(5))/(675+12375*sqrt(5))',
  'beta_rationalized':'%s + (%s)*sqrt(5)'%(brat0,brat1),
  'beta_numeric':float(brat0)+float(brat1)*math.sqrt(5),
  'beta_less_than_1_certificate':'(675+12375*sqrt(5))-(724+4500*sqrt(5))=-49+7875*sqrt(5)>0',
  'negative_region':'alpha > beta',
 },
 'covering':{
  'sets':['(-infinity,1)','(beta,+infinity)'],
  'overlap_nonempty':True,
  'reason':'beta<1, hence every real alpha is in at least one negative-witness region',
  'alpha_equal_1':'q_plus is strictly negative because 1>beta',
 },
 'separation':{
  'L_alpha_f':'541220854025436800-706968072319078800*sqrt(5)',
  'sign_exact':-1,
  'independent_of_alpha':True,
 },
 'provenance':{
  'mat_md5':base.EXPECTED_MD5,'A_sha256':base.EXPECTED_A_SHA,'action_sha256':base.EXPECTED_ACTION_SHA,
  'complete_K_isotypic_sha256':base.EXPECTED_ISOTYPIC_SHA,'complete_K_output_sha256':sha_file(complete_path),
  'system_json_sha256':sha_file(system_path),'nogap_source_sha256':sha_file(ng.__file__),'dualbase_source_sha256':sha_file(base.__file__),
 },
 'scope':'Refutes every member L_alpha of this affine SOS-dual family; does not prove or refute omega_1(A)=C and does not decide arbitrary degree-4 pseudoexpectations outside this family.',
 'preserved_facts':{'prior_invariant_seed_SOS_test':'INCONCLUSIVE','rank4_full_elliptope_extension':'PROVED_IMPOSSIBLE','alpha_2_over_3':'CERTIFIED_REFUTED'},
}
raw=json.dumps(out,sort_keys=True,separators=(',',':')).encode();outpath=mat+'.full_affine_family_exact_refutation.json';open(outpath,'wb').write(raw)
disp=dict(out);disp['output_path']=outpath;disp['output_sha256']=hashlib.sha256(raw).hexdigest();print(json.dumps(disp,indent=2,sort_keys=True))
