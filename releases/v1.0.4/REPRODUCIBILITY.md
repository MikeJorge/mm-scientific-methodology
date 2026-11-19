# Reproducibility — MM Methodology v1.0.4

## Static distribution

Extract [MM_METHODOLOGY_V104_EN_US_SITE_v1.0.0.zip](MM_METHODOLOGY_V104_EN_US_SITE_v1.0.0.zip) and open index.html, preserving the folder structure. It contains 33 regular files, including 20 HTML pages. No JavaScript, MkDocs build or scientific runtime is required.

Archive: 787,968 bytes; SHA-256 `554b4b862373825151f181726dc66234ee9978f4c5ef8bff44f34f5d992e73f3`. Expected static Git tree (100644 files): `6fc861b5d410de174daea1cb53e3430e15de7bf3`. The [manifest](PUBLIC_RELEASE_MANIFEST.json) records all member hashes and Git blob identities. An expected tree identifies prepared bytes, not an already observed deployment.

The unchanged repository verifier retains its v1.0.2 defaults. Select this version explicitly from the repository root:

```text
python verify_public_release.py --snapshot releases/v1.0.4/MM_METHODOLOGY_V104_EN_US_SITE_v1.0.0.zip --manifest releases/v1.0.4/PUBLIC_RELEASE_MANIFEST.json
```

On Windows, `py -3` may replace `python`. The verifier checks archive/member identities, CRC and Git tree without executing site contents or using the network.

## Didactic example

The site includes downloads/MM_VV_LEARNING_AND_FRESH_READER_KIT_v1.0.0.zip (17,577 bytes; SHA-256 `8f20af6630df7ca32b35a9792e734fc60a7b0b5e4200645ec99a2a0bc674c012`). Extract it, read README.md and run `python run_demo.py` with Python 3.10 or newer. Only the standard library is used. New receipts go to a new runs/ directory; the frozen criteria and preparation receipt are preserved.

The original preparation observed 44/44 comparisons. Re-running synthetic arithmetic does not validate a scientific model or observe an external participant. The participant protocol remains NOT_RUN until an actual attributable session occurs.

## Existing figures and supplement

The original five figure files and v1.0.2 reproducibility supplement remain byte-identical to v1.0.3. The new MM conceptual flow is supplied as two responsive SVGs; its Mermaid source is in the learning kit. Existing figure version identifiers are intentionally retained.

The figure/source supplement and the learning kit have different purposes. Neither supplies an installable scientific runtime or permission to operate protected systems. Existing [rights](../../LICENSING.md), contact channels and certified authorities remain controlling.
