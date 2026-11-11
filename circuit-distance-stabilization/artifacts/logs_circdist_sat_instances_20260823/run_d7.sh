#!/bin/bash
cd "$(dirname "$0")"
for s in std_aligned mis_both mis_Xonly mis_Zonly; do
  python3 -u exp_d7.py $s > d7_milp_$s.log 2>&1 &
  for b in Z X; do
    python3 -u exp_d7_stim.py $s $b > d7_stim_${s}_$b.log 2>&1 &
  done
done
wait
echo D7_DONE
