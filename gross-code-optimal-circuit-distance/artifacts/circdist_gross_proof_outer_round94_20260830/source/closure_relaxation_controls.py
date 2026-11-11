#!/usr/bin/env python3
from pathlib import Path
import argparse,json,sys
p=argparse.ArgumentParser();p.add_argument('--state',type=Path,required=True);p.add_argument('--candidate',type=Path,required=True);p.add_argument('--direct',type=Path,required=True);p.add_argument('--vendor',type=Path,required=True);p.add_argument('--output',type=Path,required=True);a=p.parse_args()
state=json.loads(a.state.read_text());cand=json.loads(a.candidate.read_text());direct=json.loads(a.direct.read_text())
sys.path[:0]=[str(a.vendor/'src/round63_src'),str(a.vendor/'src')];import model;import round68_build as builder
_,_,lx,lz=builder.load_context();current=builder.sectors(cand['compressed_times'],lx,lz)
schedule_witness=None
for s in state['selectors']:
 if not s.get('source_times'):continue
 source=builder.sectors(s['source_times'],lx,lz);vs=model.verify_named_selection(source[s['sector']],s['selected_names'],10);vc=model.verify_named_selection(current[s['sector']],s['selected_names'],10)
 if vs['ok'] and not vc['ok']:
  schedule_witness={'selector_id':s['mechanism_id'],'sector':s['sector'],'selected_names':s['selected_names'],'source_schedule_verification':vs,'iteration136_schedule_verification':vc,'conclusion':'candidate-validity is schedule dependent; replacing the dynamic EFSSC predicate by an unconditional contradiction is false'};break
assert schedule_witness is not None
weight_witness=None
for sec in ('Xerr','Zerr'):
 m=direct['sectors'][sec]['mechanism'];fw=m['fault_count'];nw=len(m['canonical_replay']['net_support'])
 if fw!=nw:
  weight_witness={'sector':sec,'selected_names':m['selected_names'],'fault_location_weight':fw,'net_data_support_weight':nw,'conclusion':'fault count is the number of distinct named locations; net support Hamming weight cannot replace it'};break
assert weight_witness is not None
out={'schema':'circdist-round94-closure-relaxation-controls-v1','status':'PASS','schedule_globalization_counterexample':schedule_witness,'fault_weight_quotient_counterexample':weight_witness,'scope':'exact counterexamples reject two tempting relaxations; they add no selector and prove no absence'}
a.output.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps({'status':'PASS','schedule_selector':schedule_witness['selector_id'],'fault_sector':weight_witness['sector']},sort_keys=True))
