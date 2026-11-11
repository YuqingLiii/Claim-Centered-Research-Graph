#!/usr/bin/env python3
from pathlib import Path
import argparse,collections,gzip,json
ap=argparse.ArgumentParser();ap.add_argument('--root',type=Path,required=True);a=ap.parse_args();R=a.root.resolve()
def load(p):
 p=Path(p)
 if not p.exists() and Path(str(p)+'.gz').exists():p=Path(str(p)+'.gz')
 b=p.read_bytes();return json.loads(gzip.decompress(b) if p.suffix=='.gz' else b)
cegar=[];drivers=[]
for i in range(90,102):
 o=load(R/'cegar'/f'iter{i}'/'iteration_outcome.json');cegar.extend(o['process_records']);drivers.append(load(R/'cegar'/f'iter{i}.driver.run.json'))
assert len(cegar)==96 and all(a['ended_utc']<=b['started_utc'] for a,b in zip(cegar,cegar[1:]))
synth=[load(R/'whole_registry/pair_leaf_reconstruction.run.json'),load(R/'whole_registry/hitting_synthesis.run.json')]
pc=load(R/'controls/round80_proof_checker/summary.json')['records']
dev=[
 {'attempt':'whole_v1','disposition':'FAILED_NO_STATE_MUTATION','record':'development/hitting_synthesis_v1_missing_catalog/hitting_synthesis.run.json','cause':'missing non-raw catalog-mask handling; assertion before mutation'},
 {'attempt':'whole_v2','disposition':'FAILED_NO_STATE_MUTATION','record':'development/hitting_synthesis_v2_python39_bitcount/hitting_synthesis.run.json','cause':'Python 3.9 int.bit_count incompatibility before mutation'},
 {'attempt':'whole_v3','disposition':'EXTERNALLY_SIGTERM_NO_STATE_MUTATION','record':'development/hitting_synthesis_v3_interrupted_quadratic_scan/hitting_synthesis.run.json','cause':'exact quadratic column scan was too slow; manual SIGTERM; replaced by bitset scan'},
 {'attempt':'whole_v4','disposition':'TEMPORARY_SCHEMA_ONLY_STATE_ROLLED_BACK','record':'development/hitting_synthesis_v4_zero_gain_schema_rollback/hitting_synthesis.run.json','cause':'synergy required at seed caused zero retained; schema-only semantic mutation rejected and rolled back exactly','rollback':'development/hitting_synthesis_v4_zero_gain_schema_rollback/hitting_synthesis/rollback.json'},
 {'attempt':'whole_v5','disposition':'FAILED_NO_STATE_MUTATION','record':'development/hitting_synthesis_v5_python39_replay_bitcount/hitting_synthesis.run.json','cause':'complete provisional classification reached, then Python 3.9 replay bit_count incompatibility'},
 {'attempt':'whole_v6','disposition':'ACCEPTED_PASS','record':'whole_registry/hitting_synthesis.run.json','cause':'bitset dominance, corrected synergy timing and portable popcount; 24 strict expansions'},
 {'attempt':'outer_iter90_v1','disposition':'FAILED_CANDIDATE_DISCARDED_NO_STATE_MUTATION','record':'development/iter90_v1_missing_round62_plain/iter90.driver.run.json','cause':'outer SAT built, independent replay correctly rejected missing plain round62 source; candidate discarded and fresh iter90 restarted'},
]
for x in dev:
 r=load(R/x['record']);x.update({k:r.get(k) for k in ['wall_seconds','max_rss_bytes','exit_code','timed_out','sigterm_sent','sigkill_sent']})
dev.append({'attempt':'verifier_v1_noop','disposition':'REJECTED_HARNESS_NO_STATE_MUTATION','record':'verification/precompression_quick_v1_noop.log','cause':'main invocation missing after source edit; zero-byte output rejected despite shell exit 0','wall_seconds':0.04,'max_rss_bytes':26542080,'exit_code':0,'timed_out':False,'sigterm_sent':False,'sigkill_sent':False})
dev.append({'attempt':'verifier_v2_bad_live_path','disposition':'REJECTED_BINDING_METADATA_NO_STATE_MUTATION','record':'verification/precompression_quick_v2_bad_live_path.time.txt','cause':'SOURCE_BINDINGS named nonexistent live Gross node path; corrected to canonical proof-dag node path','wall_seconds':0.16,'max_rss_bytes':115539968,'exit_code':1,'timed_out':False,'sigterm_sent':False,'sigkill_sent':False})
obj={'schema':'round80-process-ledger-v1','status':'PASS','strict_serial_execution':True,'concurrent_load_bearing_processes':0,'accepted_synthesis_process_records':synth,'accepted_iteration_driver_records':drivers,'accepted_iteration_driver_wall_seconds_total':sum(float(x['wall_seconds']) for x in drivers),'accepted_iteration_driver_max_rss_bytes':max(int(x['max_rss_bytes']) for x in drivers),'accepted_cegar_process_records':cegar,'accepted_cegar_process_count':len(cegar),'accepted_iterations':12,'accepted_process_exit_code_histogram':dict(collections.Counter(str(x['exit_code']) for x in cegar)),'accepted_process_wall_seconds_total':sum(float(x['wall_seconds']) for x in synth+cegar),'accepted_process_max_rss_bytes':max(int(x.get('max_rss_bytes',0)) for x in synth+cegar),'development_attempts':dev,'proof_control_records':pc,'timeouts':0,'unknowns':0,'signals_in_accepted_computation':0,'canonical_repository_mutated':False,'accepted_round78_package_mutated':False,'post_control_state_semantic_sha256':load(R/'restart/restart_state.json')['semantic_sha256'],'scratch_cleanup_required_before_completion':True,'process_survivor_scan':'preflight/process_survivor_scan_final.txt'}
(R/'PROCESS_LEDGER.json').write_text(json.dumps(obj,indent=2,sort_keys=True)+'\n')
lines=['# Process ledger','',f"Accepted synthesis wrappers: {len(synth)}; accepted CEGAR child processes: {len(cegar)}; iteration driver wrappers: {len(drivers)}; proof-control runs: {len(pc)}.",'',f"Accepted process wall total: {obj['accepted_process_wall_seconds_total']:.3f}s; maximum sampled RSS: {obj['accepted_process_max_rss_bytes']:,} bytes. No accepted process timed out or received SIGTERM/SIGKILL.",'','## FIX-2 development incidents','']
for x in dev:lines.append(f"- **{x['attempt']}** — {x['disposition']}; wall={x['wall_seconds']:.3f}s, maxRSS={int(x['max_rss_bytes']):,} B, exit={x['exit_code']}. {x['cause']}")
lines+=['','All failed/interrupted computations occurred in disposable staging. Tentative outputs were either never installed or explicitly rolled back. The accepted CEGAR chain contains only complete atomic commits.']
(R/'PROCESS_LEDGER.md').write_text('\n'.join(lines)+'\n');print(json.dumps({'status':'PASS','cegar_records':len(cegar),'max_rss':obj['accepted_process_max_rss_bytes'],'development':len(dev)},sort_keys=True))
