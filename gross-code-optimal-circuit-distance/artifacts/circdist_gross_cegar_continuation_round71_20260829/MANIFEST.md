# Package manifest and claim boundary

This directory is one immutable proposer package. `SHA256SUMS.txt` covers every file except itself; its own SHA-256 is the external root seal. `PAYLOAD_SHA256SUMS.txt` is an additional pre-verification inventory. Deterministically compressed files are indexed by both compressed and original hashes in `COMPRESSED_INVENTORY.json`.

The only verdict token is `MATERIAL-CHECKED-PROGRESS-NOT-CLOSED`. The package licenses 48 new raw-replayed candidate-exact blocks and continuation at iteration 30 with 6,260 installed blocks. It licenses no absence, repair, exhaustion, route change, node edit, level change, or exact value of `D*_Gross`.
