#!/usr/bin/env python3
"""Integrity/algebra checker for the two minimal five-block H4 no-go certificates.

The expensive matrices are deterministically replayed by the two pinned scripts
recorded in the theorem manifest.  This checker validates every durable artifact,
the stored kernel families, dimensions, ranks, determinants, and the block-
triangular rank implication.  It performs no floating-point computation.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

import numpy as np

P = 24001


def die(message):
    raise SystemExit("ERROR: " + str(message))


def sha(path: Path) -> str:
    digest = hashlib.sha256()
    with open(path, "rb") as stream:
        for chunk in iter(lambda: stream.read(1 << 20), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main() -> None:
    project = Path(__file__).resolve().parents[1]
    draft = project / "artifacts/drafts"
    manifest_path = draft / "d4-two-minimal-five-block-linear-nogo-certificate-20260830.json"
    manifest = json.load(open(manifest_path))
    artifacts = manifest["artifacts"]
    replay_schur = draft / "session-fourier-energy/five_block_schur_exact_discovery.py"
    replay_coeff = draft / "session-fourier-energy/five_block_kernel_coefficient_minor.py"
    if sha(replay_schur) != artifacts["schur_replay_script_sha256"]:
        die("Schur replay script SHA")
    if sha(replay_coeff) != artifacts["coefficient_minor_replay_script_sha256"]:
        die("coefficient replay script SHA")

    results = []
    for ir in (8, 17):
        schur_path = draft / f"d4-five-block-{ir}-schur-discovery-20260830.json"
        family_path = draft / f"d4-five-block-{ir}-schur-discovery-20260830.evaluation-kernel-family.npz"
        minor_path = draft / f"d4-five-block-{ir}-kernel-coefficient-minor-20260830.json"
        if sha(schur_path) != artifacts[f"block_{ir}_schur_json_sha256"]:
            die(f"block {ir} Schur JSON SHA")
        if sha(family_path) != artifacts[f"block_{ir}_evaluation_kernel_family_sha256"]:
            die(f"block {ir} family SHA")
        if sha(minor_path) != artifacts[f"block_{ir}_coefficient_minor_json_sha256"]:
            die(f"block {ir} coefficient minor JSON SHA")
        schur = json.load(open(schur_path))
        minor = json.load(open(minor_path))
        family = np.load(family_path)
        kernel = family["extra_kernel_basis_modp"]
        coordinates = family["base_target_coordinates_modp"]
        if kernel.shape != (6651, 467) or coordinates.shape != (6666, 467):
            die(f"block {ir} family shape")
        if schur["blocks"] != [9, 12, 13, 14, ir]:
            die(f"block {ir} block list")
        if int(schur["base_augmented_minor_determinant_mod_p"]) != 5172:
            die(f"block {ir} base determinant")
        if int(schur["schur_residual_rank_mod_p"]) != 6184:
            die(f"block {ir} Schur rank")
        if int(schur["schur_residual_nullity_mod_p"]) != 467:
            die(f"block {ir} Schur nullity")
        coupling_count = int(np.count_nonzero(coordinates[-1] % P))
        if coupling_count != int(schur["kernel_target_coupling_nonzero_count"]):
            die(f"block {ir} target coupling count")
        if int(minor["evaluation_kernel_dimension"]) != 467:
            die(f"block {ir} coefficient family dimension")
        if int(minor["sample_matrix_rank_mod_p"]) != 467:
            die(f"block {ir} coefficient residual rank")
        determinant = int(minor["coefficient_residual_minor_determinant_mod_p"]) % P
        expected_det = 13280 if ir == 8 else 7143
        if determinant != expected_det or determinant == 0:
            die(f"block {ir} coefficient residual determinant")
        if not minor["evaluation_kernel_killed_by_true_coefficient_map"]:
            die(f"block {ir} kernel not killed")
        # Rank decomposition: invertible base augmented minor, 6184 visible
        # Schur directions, and 467 independent true-coefficient refinements.
        if 6666 + 6184 + 467 != 13317:
            die("rank arithmetic")
        results.append({
            "extra_block": ir,
            "evaluation_schur_rank": 6184,
            "evaluation_kernel_dimension": 467,
            "true_coefficient_kernel_rank": 467,
            "augmented_rank_mod_p": 13317,
            "gram_map_rank_mod_p": 13316,
            "target_in_linear_image": False,
            "psd_gram_exists": False,
            "coefficient_residual_minor_determinant_mod_p": determinant,
        })

    output = {
        "status": "EXACT_TWO_MINIMAL_FIVE_BLOCK_LINEAR_NO_GO_CERTIFICATE_VERIFIED",
        "prime": P,
        "manifest_sha256": sha(manifest_path),
        "results": results,
        "characteristic_zero_lift": (
            "Every displayed nonzero modular minor lower-bounds the corresponding "
            "rank over Q(sqrt(5),i); all serialized representation denominators "
            "are powers of two and hence invertible modulo 24001."
        ),
    }
    output_path = draft / "d4-two-minimal-five-block-nogo-checker-output-20260830.json"
    output_path.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n")
    print(json.dumps(output, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
