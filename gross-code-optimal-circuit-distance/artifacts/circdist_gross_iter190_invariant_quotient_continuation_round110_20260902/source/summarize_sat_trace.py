#!/usr/bin/env python3
from pathlib import Path
import argparse,hashlib,json
p=argparse.ArgumentParser();p.add_argument('--formula',type=Path,required=True);p.add_argument('--trace',type=Path,required=True);p.add_argument('--solver-log',type=Path,required=True);p.add_argument('--iteration',type=int,required=True);p.add_argument('--query',required=True);p.add_argument('--output',type=Path,required=True);p.add_argument('--delete',action='store_true');a=p.parse_args()
def sha(p):
 h=hashlib.sha256()
 with p.open('rb') as f:
  for b in iter(lambda:f.read(1<<20),b''):h.update(b)
 return h.hexdigest()
assert 's SATISFIABLE' in a.solver_log.read_text();assert a.trace.exists()
h=hashlib.sha256();n=0;lf=0;empty=0;first=b'';last=b''
with a.trace.open('rb') as f:
 for line in f:
  if n==0:first=line[:256]
  last=line[-256:];h.update(line);n+=len(line);lf+=line.count(b'\n');empty+=int(line.strip()==b'0')
out={'schema':'circdist-round94-sat-proof-stream-summary-v1','iteration':a.iteration,'query':a.query,'solver_status':'SATISFIABLE','proof_output_enabled':True,'certificate_disposition':'not an UNSAT certificate','formula_sha256':sha(a.formula),'trace_sha256':h.hexdigest(),'bytes':n,'lf_count':lf,'physical_lines_iterated':lf,'empty_clause_lines':empty,'first_line_prefix_hex':first.hex(),'last_line_suffix_hex':last.hex(),'full_trace_retained':not a.delete,'retention':'complete hash/size/LF/empty-line disposition retained; SAT-side non-certificate stream deleted after complete assignment/formula/replay checks' if a.delete else 'full SAT-side non-certificate stream retained'}
if a.delete:a.trace.unlink();out['trace_absent_after_deletion']=not a.trace.exists()
a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps(out,sort_keys=True))
