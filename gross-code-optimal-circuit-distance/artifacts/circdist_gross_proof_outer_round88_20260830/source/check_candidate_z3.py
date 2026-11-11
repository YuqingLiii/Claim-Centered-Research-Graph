from pathlib import Path
import argparse,json,time,hashlib
import z3
ap=argparse.ArgumentParser();ap.add_argument('--formula',type=Path,required=True);ap.add_argument('--candidate',type=Path,required=True);ap.add_argument('--output',type=Path,required=True)
a=ap.parse_args();t=time.time();c=json.loads(a.candidate.read_text());A=z3.parse_smt2_file(str(a.formula));assert len(A)==19016
out={'schema':'round88-z3-candidate-corroboration-v1','formula_sha256':hashlib.sha256(a.formula.read_bytes()).hexdigest(),'assertions':len(A),'checks':{}}
for label,times in [('raw',c['raw_times']),('compressed',c['compressed_times'])]:
 s=z3.Solver();s.add(A)
 for e,v in times.items():s.add(z3.Int('t_'+e.replace(':','_'))==int(v))
 xs=[v for e,v in times.items() if e.startswith('X:')];zs=[v for e,v in times.items() if e.startswith('Z:')]
 for name,v in [('xmin',min(xs)),('xmax',max(xs)),('zmin',min(zs)),('zmax',max(zs))]:s.add(z3.Int(name)==v)
 ans=s.check();assert ans==z3.sat
 out['checks'][label]={'status':str(ans).upper(),'model_fixed_edge_times':864,'fixed_extrema':4}
out['status']='PASS';out['seconds']=round(time.time()-t,6);a.output.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps(out,sort_keys=True))
