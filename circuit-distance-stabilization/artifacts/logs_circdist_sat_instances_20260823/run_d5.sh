#!/bin/bash
cd "$(dirname "$0")"
python3 exp_surface.py 3 --stim > d3_full.log 2> d3_full.err
for i in $(seq 0 15); do
  python3 exp_surface.py 5 --stim --only $i > d5_only$i.log 2> d5_only$i.err &
done
wait
cat d5_only*.log > d5_full.log
echo DONE
