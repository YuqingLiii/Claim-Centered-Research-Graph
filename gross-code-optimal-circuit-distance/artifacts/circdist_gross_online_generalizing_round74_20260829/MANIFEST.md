# Manifest semantics

`SHA256SUMS.txt` is the package-root external seal and excludes only itself. It covers nested predecessor seals, payload, preseal verification records, documentation, and `PAYLOAD_SHA256SUMS.txt`. Its own SHA-256 is reported outside the immutable package.

`PAYLOAD_SHA256SUMS.txt` covers research payload and source files before final verification logs and root manifests. `COMPRESSED_INVENTORY.json` records each `.gz` path, its deterministic header mtime (`0`), compressed bytes/hash, and decompressed bytes/hash. Original uncompressed paths must be absent.

The nested round-72 package retains its own immutable seal. `verify.py` checks both manifest layers, every compressed member, and optional live source bindings.
