# Seal convention

`SHA256SUMS.txt` is the external root seal. It lists every physical package file except itself exactly once, using repository-independent relative paths and SHA-256 of stored bytes.

`PAYLOAD_SHA256SUMS.txt` is a complete non-self payload manifest. It lists every physical package file except itself and `SHA256SUMS.txt`; there are no mutable or unsealed output slots.

`COMPRESSED_INVENTORY.json` enumerates every `.gz` member and binds its deterministic stored bytes, gzip `mtime=0`, decompressed bytes, compressed/uncompressed sizes and both SHA-256 hashes. The corresponding uncompressed physical file must be absent.

Accepted-preseal and post-copy execution logs are written outside the immutable package. This avoids the impossible self-reference of inserting a log into the tree after that log has certified it.
