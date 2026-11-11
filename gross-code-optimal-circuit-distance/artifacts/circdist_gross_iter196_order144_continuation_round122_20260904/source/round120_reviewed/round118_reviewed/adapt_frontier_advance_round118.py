from pathlib import Path
import hashlib
p=Path('/private/tmp/circdist-round118-iter194-order144-work/advance_css_closed_frontier_round118.py')
s=p.read_text()
def rep(old,new,count=1):
 global s
 n=s.count(old)
 assert n==count,(n,count,old[:100])
 s=s.replace(old,new)
# Provenance namespace first.
s=s.replace('Round116','Round118').replace('round116','round118').replace('r116-','r118-')
rep('Build deterministic iteration 194 with exact nonfree CSS closure and new exclusions.',
    'Build deterministic iteration 195 with full order-144 closure and new sound exclusions.')
rep('assert len(old_bkeys) == len(old_bset) == 814068','assert len(old_bkeys) == len(old_bset) == 814392')
rep('assert len(old_skeys) == len(old_sset) == 50580','assert len(old_skeys) == len(old_sset) == 50832')
rep('assert len(missing_blocks) == 324 and len(bparts) == 9 and {len(orbit) for _, orbit in bparts} == {36}',
    'assert len(missing_blocks) == 0 and len(bparts) == 0')
rep('assert len(missing_selectors) == 36 and len(sparts) == 1 and {len(orbit) for _, orbit in sparts} == {36}',
    'assert len(missing_selectors) == 0 and len(sparts) == 0')
s=s.replace('"source_iteration": 193','"source_iteration": 194')
s=s.replace('iter193','iter194')
rep('assert [len(orbit) for orbit in candidate_sets] == [36, 72, 36, 72]',
    'assert [len(orbit) for orbit in candidate_sets] == [72, 36, 72, 36]')
rep('assert len(blocks) == 814392','assert len(blocks) == 814392')
rep('assert len(selectors) == 50832','assert len(selectors) == 51048')
rep('source["schema"] = "circdist-gross-iteration194-full-translation-closure-finite-source-v1"',
    'source["schema"] = "circdist-gross-iteration195-full-order144-closure-finite-source-v1"')
rep('"round118_inherited_nonfree_block_orbits_installed": 9','"round118_inherited_nonfree_block_orbits_installed": 0')
rep('"round118_inherited_nonfree_selector_orbits_installed": 1','"round118_inherited_nonfree_selector_orbits_installed": 0')
rep('"round118_candidate_selector_orbit_sizes": [36, 72, 36, 72]',
    '"round118_candidate_selector_orbit_sizes": [72, 36, 72, 36]')
rep('"next_iteration": 194','"next_iteration": 195')
rep('fresh checked unstarted iteration-194 source after exact nonfree CSS closure and four iter194 mechanism orbits; no iteration-194 solver disposition',
    'fresh checked unstarted iteration-195 source after four sound iter194 mechanism/CSS orbits; no iteration-195 solver disposition')
rep('"selector_orbits_detail": selector_orbit_rows[:1]',
    '"selector_orbits_detail": selector_orbit_rows[:len(sparts)]')
rep('"orbit_detail": selector_orbit_rows[1:]','"orbit_detail": selector_orbit_rows[len(sparts):]')
rep('"fresh_frontier": {"iteration": 194, "started": False, "solver_invocations": 0}',
    '"fresh_frontier": {"iteration": 195, "started": False, "solver_invocations": 0}')
p.write_text(s)
print({'status':'PASS','bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()})
