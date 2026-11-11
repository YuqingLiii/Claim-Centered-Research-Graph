# Round-68 sealed package manifest

`SHA256SUMS.txt` is the authoritative complete file inventory and digest ledger. It covers every regular file in this package except the top-level ledger itself, including `tooling/SHA256SUMS.txt`. `PAYLOAD_SHA256SUMS.txt` freezes all computational and evidentiary payload files and excludes only itself plus `MANIFEST.md`, `FINAL_AUDIT.txt`, and the top-level `SHA256SUMS.txt`.

## Inventory summary

Total regular files: **102**.

| path group | files |
|---|---:|
| `(top level)` | 28 |
| `candidate` | 4 |
| `controls` | 27 |
| `direct360` | 10 |
| `solver` | 6 |
| `src` | 17 |
| `tooling` | 10 |

## Verdict-bearing objects

- `VERDICT.txt`: the sole verdict and exact residual.
- `README.md`: self-contained algebra, encoding, candidate, witness, toolchain, controls, limitations, and review license.
- `candidate/candidate.json`: complete 864-edge schedule, audit, both 360-column bindings, logical bases, and asserted-block exclusions.
- `direct360/{Xerr,Zerr}.{cnf,columns.json,variables.json,clauses.jsonl,summary.json}`: complete direct formulas and dictionaries.
- `solver/{Xerr,Zerr}.{solver.log,run.txt,drat.gz}`: exact retained foreground proof-logging SAT runs.
- `verification.json`: complete assignment/DIMACS/raw-physics replay for the primary mechanisms.
- `cegar_continuation5.json`: five exact outer schedules, ten raw mechanisms, and ten sound blocks.
- `controls/proof_checker/`: positive DRAT/LRAT chain and rejected corrupted-proof controls.
- `tooling/`: exact solver/checker binaries, source archives, build metadata, and CaDiCaL test log.
- `SOURCE_BINDINGS.json` and `BINDING_DRIFT.json`: current disk bindings and inherited-package drift analysis.
- `PROCESS_LEDGER.md`, `ATTACK_LEDGER.md`, `COMMANDS.txt`, and `FINAL_AUDIT.txt`: FIX-2 process disclosure, rejected branches, exact commands, cleanup, process, and repository-delta audit.
- `verify.py`, `final_verification.log`, and `final_verification.run.json`: self-contained replay entrypoint and retained live-binding replay.

## Complete immutable-payload inventory

The following table gives the full path, byte count, and SHA-256 for every payload file. The four structural ledgers are bound by the complete top-level `SHA256SUMS.txt`.

| path | bytes | SHA-256 |
|---|---:|---|
| `ATTACK_LEDGER.md` | 4222 | `40bbf18cb7ee40f008e1947b383a7de71088ca7db57d853171a63bd0079ce85b` |
| `BINDING_DRIFT.json` | 7853 | `0a31c80b17b8a5a13f9c7702265cc44b7c72a3037b99196800ec6b50e2970c59` |
| `COMMANDS.txt` | 3520 | `718758968472bd64c9aec09693480b1f39f3c2cc76929b1840eba5e21ad0b9db` |
| `PROCESS_LEDGER.md` | 4375 | `84e1a61b90f95a585c14f0e9a7e7520c4386f468eade1b36e98e76c70983855e` |
| `README.md` | 17513 | `86dfaf012e7a1598c9a0a0ee0157ffe84f4491d83c05fc496580e121f9ed83fd` |
| `REVIEW_LICENSE.txt` | 1227 | `3145a39ed0495a499f5b0743b7c54410debb6dbc2d36ebfd4581805338408e0b` |
| `SOURCE_BINDINGS.json` | 103636 | `622eeee8830af481efe5c2ee40c1c7a4d05b99d0878caf08f3477276283712e7` |
| `VERDICT.txt` | 310 | `c2b99af588d96b14045f2484496747cd689b13b74c5b447716190549643eb3b0` |
| `build_summary.json` | 3083 | `92bc10e5ea24f55b86e5c36f1bcc878537e2d378e7f22cee46e0fdf275863434` |
| `candidate/candidate.json` | 777856 | `df79a45177f6dbc0610e11e87c531070d9863562928982089a59a720fe148959` |
| `candidate/candidate_outer.smt2` | 652238 | `528d8de887cf63d3bd3cda3409157720d4197e24a5e1f817764edb7b8f2cb6df` |
| `candidate/global_single_clause_certificates.json` | 5120142 | `37ad518c2455d55e57bc5758ad1131ee8e9cb7f244ca0579307b156225ede775` |
| `candidate/round62_blocks_replay.json` | 50865 | `5736e6d2ed92f6d01f5aa0515308590fcfe50697684979d0ac5548d4f1cde62b` |
| `cegar_continuation5.json` | 207751 | `6a1947455997c9e4f028abce018015f811ca38020876a58fd01c2993232b8f65` |
| `controls/C1_Zerr.run.txt` | 376 | `55f192ce27b3d939013837d0d9706e8dd3714a001561aac4062a673908a50157` |
| `controls/C1_Zerr.solver.log` | 24052 | `c6105934855f3a835aaaf1d98fd08cc1b1390b7f74508b4a22527f65fbaebf6f` |
| `controls/C1_Zerr.summary.json` | 897 | `0bcf980c06d0231c8bdd3234122b0e41a1127fd41349d306682ceb15b418df40` |
| `controls/C1_Zerr_expected_witness.json` | 2429 | `ca23be67c74a257c9d9a8185766a88cee8768fbb6283b13cef16a15a90258c89` |
| `controls/Zerr_glucose42.json` | 63536 | `f3d8ab605def0883cc902b780e8b4d4ec35e58cd7643b15c197bd19d48206f89` |
| `controls/Zerr_glucose42.run.json` | 590 | `27fa8c867db61144d74f7eedfaa95940c1b4a13491cafae98bfd6c09ea1b303f` |
| `controls/Zerr_glucose42.stdout.log` | 0 | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |
| `controls/Zerr_glucose42_raw_replay.json` | 13504 | `c16dacb4983c959cc5ce44d46285cca7be3eba99c63fedacd8a415b21c3ad0df` |
| `controls/encoding_controls.json` | 1229 | `264909d7ccca9212d84a8363e7bf95375ca4be94adc0d3a437fe4f0fcaf08f78` |
| `controls/proof_checker/php6_5.cnf` | 1445 | `d9357f5203d4bd8315b7287b7543ad97072386a92980d498d1b36b3d39fb1fa9` |
| `controls/proof_checker/php6_5.drat` | 3114 | `b6c2e560bb08c84d583ca94799951a21c8cae5de35d6d04d77bc4842e9c18ecd` |
| `controls/proof_checker/php6_5.drat_trim.log` | 369 | `940932dca350ffc4d207936f773f7f2a2b29571f65fcd30c177b79365c1a6553` |
| `controls/proof_checker/php6_5.drat_trim.run.txt` | 469 | `f00891c4941665445c886ed75e70c72259dc98fee5b870122cab553cc9425df6` |
| `controls/proof_checker/php6_5.lrat` | 10851 | `0723e34b24bfa7b1b8432f1606f5ba9c43e325e1c8e9eab6195b45d3cedcfd0f` |
| `controls/proof_checker/php6_5.lrat_check.log` | 192 | `54b78d5976475e8834663f5cc7cc530ff2338fd46f3d678f0feac39315512c1c` |
| `controls/proof_checker/php6_5.lrat_check.run.json` | 478 | `7cd91d6e6c1eb6b22c8bbfec206d39d72658aa3b6bbc0e75f58161174cd9162b` |
| `controls/proof_checker/php6_5.solver.log` | 4630 | `d982d1278b4dc5a8802bf285a138614007d6764db1a46052ab03c07730e54717` |
| `controls/proof_checker/php6_5.solver.run.txt` | 389 | `996a4b4f2703785edfc2df0ff573ec6071e34c6d8c31dfcdf754d95c19f91f8b` |
| `controls/proof_checker/php6_5_corrupted.drat_trim.log` | 369 | `f8279870f3ed14d9e0f6380dd102a7195479642239c08aa08261524c83d1a1eb` |
| `controls/proof_checker/php6_5_corrupted.drat_trim.run.txt` | 462 | `0c55a732546a54185bdafbf7245bd620de8a6557570d9cf66792b4193cd8c203` |
| `controls/proof_checker/php6_5_corrupted.lrat_check.log` | 255 | `ec5553864144a099068519043983a9fa1272d0bf1c246a663a9fe3e6b0f55094` |
| `controls/proof_checker/php6_5_corrupted.lrat_check.run.json` | 507 | `208d905a6576533b1581aac6607974b19e79f7fa5f0a00dda75ded76f3dc41d2` |
| `controls/proof_checker/php6_5_corrupted_missing_empty_clause.drat` | 3112 | `903ae3f0191bc1f4dd1697f718f6cf2714225f76371601f0c0e19676b449d7a0` |
| `controls/proof_checker/php6_5_corrupted_truncated.drat_trim.log` | 153 | `ace8c757b1a689ff3c6795ae42edee8734af62a20da23a008dc57b6ccb5cbaca` |
| `controls/proof_checker/php6_5_corrupted_truncated.drat_trim.run.txt` | 469 | `a0606a0f1d0daca244fbd34c39a72dd35d307062e4dae9d3edc96ccba3fb1f97` |
| `controls/proof_checker/php6_5_corrupted_truncated_10_lines.drat` | 158 | `16960f5aa9d84658b25c9b0544e51d6dc848a96a97cae19549a585421a660081` |
| `controls/proof_checker/php6_5_corrupted_truncated_10_lines.lrat` | 646 | `4e749aa5afffba5c1bfa0444021170527ad83b2bcd0857f845b1a5bcb73fdee7` |
| `direct360/Xerr.clauses.jsonl` | 2489781 | `97efc95c4ad410fbbe4812bfa5dbc9c6c0d4af91c5969255e1e82f9270e3b0a3` |
| `direct360/Xerr.cnf` | 360573 | `23baae8614d921d1289dbeff77c8ef893007b35e7b97cbd9f3c693d28bd86ecb` |
| `direct360/Xerr.columns.json` | 364818 | `75e5b5409576de8af1af4b0e3b41878faba5cf41dde90d422c6569c8108e55dc` |
| `direct360/Xerr.summary.json` | 897 | `68e2f07d9546521404deccf6abd1f52a44cdfe4482c1a6c690f04cd663e36a0f` |
| `direct360/Xerr.variables.json` | 1342980 | `cdaab4ecd89e74a7ec70bcb88d7322dbe6563ee9f61969033b01c0fd8ee47241` |
| `direct360/Zerr.clauses.jsonl` | 2520971 | `929ad13ffb845cb494e0761f3bbc70d4c955206d89e872794f4b276256b8749d` |
| `direct360/Zerr.cnf` | 364415 | `ef7401f7d05e6e7ce84c6bcb07eecdfbfaecdff65d653b97529bea7d54a6022d` |
| `direct360/Zerr.columns.json` | 343922 | `73a94b271456f5ff94dcaf70d1a5486afebd4f435c7d0509612d95083d2e76d2` |
| `direct360/Zerr.summary.json` | 897 | `6755526b89f99b34cb8e3b198c4fcf0c8e161cd9967b848b1fe535fc41f6cbf0` |
| `direct360/Zerr.variables.json` | 1357074 | `2b9d47641c212f56476cbadfe3b0c5a414063597ab3af547b472b21581d341d1` |
| `evidence_closure_check.log` | 12455 | `0351964463117c7a7b039ec22726e96d13e84d2afccb4249848ba6439fdfd418` |
| `evidence_closure_check.run.json` | 277 | `b64d43118a34c7ffede610cbb4b3abe478b2788dc7998e5edf1f00cb1b739c6a` |
| `final_verification.log` | 1561 | `7a5f70522a5fa875f647080e0a9ec232eb0f93226cd2715f6b58ee26700396a1` |
| `final_verification.run.json` | 591 | `a92129a8a7d60745a1f54dc7e8cff91363749f9850d29b0de0be783510e99b8c` |
| `preflight_replays.log` | 2404 | `c59b1b4d9e3bcc3b79425e6876349747470db38fdf3d1e0fb693c6b584c98afb` |
| `preflight_round63_sealed_static.log` | 745 | `3deb441c9fa33016be30044540c9014358190d954a160d25f3dcff1b78e2df8f` |
| `preflight_seals.log` | 1789 | `0568276f69ab3d72d8d3e38b7b4348967dbff2a5163fe88f050fd0db206a8280` |
| `preseal_verification.log` | 1561 | `7a5f70522a5fa875f647080e0a9ec232eb0f93226cd2715f6b58ee26700396a1` |
| `proof_dag_check.log` | 43 | `c43e0a23f474af4c5b8e013612205d543c71c16b623dd0e3dde3d38615667068` |
| `proof_dag_check.run.json` | 270 | `aa2a80804279dd67e5b40364dff665bb8fdbb6adb3e2e0ceb6eeef86c4dd3c02` |
| `requirements.txt` | 66 | `e5ace88d19150ff07d84704ca6e9f4a4a070c2f588a6502e4ca0bfe99ebf6ee6` |
| `solver/Xerr.drat.gz` | 7995294 | `426189a67f48a9a7d0974e53f3408fc0d426abbafd42a08627094599d93ea94d` |
| `solver/Xerr.run.txt` | 290 | `a034b8a1a03a1cfaa96efe4faec7bdd4462092901e236d45bc0d7a7bf1f906ae` |
| `solver/Xerr.solver.log` | 44255 | `5f97fa5a9e128a0c89063efd3b1e67bc727f99b24cf641079203ff8f788b4940` |
| `solver/Zerr.drat.gz` | 817 | `b58dca69b07dfd4dc6c3e9afa4829bfc304c22be38917b4a18d6d6dc37d6c7c6` |
| `solver/Zerr.run.txt` | 290 | `3c79c4128f7a5afdd7b50c249fbf9d061aee89d2e34deaac4c09d0db382da8cb` |
| `solver/Zerr.solver.log` | 37577 | `ff8dd82affd03b0e45371f538e074a983150147f639c6cc7a933ff8af9d59ae2` |
| `src/continue_cegar.py` | 3375 | `3784117694ed2aa01db2709123c3b02465d35308de366878e52753f472e678fd` |
| `src/encoding_controls.py` | 1611 | `3fdf3125f996a1d5ad0973c0f5df0299dd36347fc8b1c6f0137ac38ac27640bf` |
| `src/global_single_clauses.json` | 1952 | `b403b238f7e82b2ba116fc6e413aa540cf01efea5c6cfb1dda83da96092b3394` |
| `src/inputs/w12X.txt` | 10743 | `1460a15c2ae372fa602fca810aa05bf9fb62426aba121b84931d8fec5c3d6697` |
| `src/inputs/w12Z.txt` | 11175 | `981be6c7aa8a42ab00a8925007a4a0567724ab7b46bd157383087f18b0af8125` |
| `src/make_bindings.py` | 2057 | `7cfc0339b0fd0b10baf145340b6745cd2678a82abeace82bcff54cb8c288672e` |
| `src/pysat_control.py` | 676 | `2ee6b23de245927bd9975ba2e530ab1d325820dae27aef8b1cc84972a807bf64` |
| `src/round62_cegar20.json` | 505193 | `c05ddbc13645d31c754417942305324ecc2e6aa243ae1c1a967b112d7d2b505f` |
| `src/round63_src/model.py` | 31007 | `60663244444b5ee43eb811592b45f4dbfa39f7cec7583f9ad340ae2b45d26829` |
| `src/round63_src/negative_controls.py` | 5237 | `6c4026dc2489fc88a752164cd9cd5cc4d51820b141a49bb85e788f219ddf4108` |
| `src/round63_src/outer.py` | 3799 | `82255250c845f5470fa7396ed6926ba4189d99775fd95f439c0c1ea1e04d3bd9` |
| `src/round63_src/pattern.py` | 8197 | `e3ab219cba69d218dc1fd6f7d9a9a5b0575fd30e004dfdb74f17bfba2de88540` |
| `src/round63_src/pattern_cegar.py` | 4527 | `bf33dc547a11673c6394a1b4ad07889f9b4d9db773d4564d43cc2b736605a4f4` |
| `src/round63_src/run.py` | 9873 | `33e8289309d40825d0161512315fb4820526a7ec429c74173f70ca0408afedc9` |
| `src/round68_build.py` | 22509 | `67efd99a354dec6ef7639b6a7fa9bab0590ef41cab7cbab1e6a55e87434c2404` |
| `src/round68_verify.py` | 8004 | `896ab0284d6394e11bd110240451e240a6b70cdf5412ad28e1c0bfdeb70ed957` |
| `src/run_limited.py` | 934 | `ef6b75cf21cd74df6ad2b58f9972334a8366d3e4fa16933050a13144af0a9421` |
| `tooling/SHA256SUMS.txt` | 821 | `69c110c1a171b966c6a5f205d001534a5416bd2656ab3f79d8c1efe39058086f` |
| `tooling/cadical-1.9.5-arm64-macos` | 967144 | `fafdf4fb95a54ccee9b59f346544761896e40b076780a93f000e0357f20080c9` |
| `tooling/cadical-rel-1.9.5-source.tar.gz` | 689601 | `ea4c7fd0151060725fde7bfe391fb18372255bee94ea4c7e354e1f73b54387ed` |
| `tooling/cadical_make_test.log` | 199342 | `919b63171a0475ab7974b411178280f64e4e20c89d8e6af0873fbb337b48323c` |
| `tooling/cadical_make_test.run.txt` | 30 | `bff544d4a1ab492303250bfafa75816e03b7099cbf7d2255ccb3057b3ca68491` |
| `tooling/cadical_source_build.txt` | 349 | `25c47a48359c770acde53ff8703cdc0bf99bcde4be8f8de1654e339d7664e762` |
| `tooling/drat-trim-arm64-macos` | 70120 | `f58f63b0f76945d4c4c9ff6e87afaf870f579e67c0f7cca589492df8fc7ebd47` |
| `tooling/drat-trim-source.tar.gz` | 7294515 | `bfe65f9028c772614888daace1985cb66555018c8e77b9bf6b15e6ab91c4f7e1` |
| `tooling/drat_trim_source_build.txt` | 256 | `83680e380b01b25d50dfd079df31f3ef604830deb32da39b3e0b603a4ce6e367` |
| `tooling/lrat-check-arm64-macos` | 36552 | `bd7eb8052623525814a0a37502b47f05375d9d9dfaf96ddc2fcd858958517cea` |
| `verification.json` | 32493 | `8b2f256b24b2df9a064aea0324cb0386ed73a76ed8703a17906f3a267c646c41` |
| `verification_replay.log` | 1561 | `7a5f70522a5fa875f647080e0a9ec232eb0f93226cd2715f6b58ee26700396a1` |
| `verify.py` | 9551 | `f83ee01a1d8617a641b44ddc7ca5a997335019c531dce3861088fb5e0a23e713` |

## Structural ledgers

- `PAYLOAD_SHA256SUMS.txt`
- `MANIFEST.md`
- `FINAL_AUDIT.txt`
- `SHA256SUMS.txt` (self-excluded complete seal)
