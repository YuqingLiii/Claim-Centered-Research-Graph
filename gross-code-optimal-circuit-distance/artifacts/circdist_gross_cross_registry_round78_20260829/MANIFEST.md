# Manifest and release stages

Development full verification runs on the uncompressed staging tree and is not an accepted release gate. Deterministic gzip then writes `COMPRESSED_INVENTORY.json` with compressed and uncompressed SHA-256 plus `mtime=0`. Accepted quick and full verification run on that final compressed tree with `--allow-unsealed`; their logs remain external because inserting them would change the certified tree.

Only then are `PAYLOAD_SHA256SUMS.txt` and the non-self `SHA256SUMS.txt` created. No payload or gzip member may change after accepted preseal full verification. The sealed directory is renamed atomically from same-device external staging into the authorized target. Post-copy sealed full and quick verification use `--repo-root` for live bindings. Repository inventory and Git tripwires exclude the authorized target and must match before/after exactly.
