# Reproducibility boundary — MM Methodology v1.0.3

## Select and verify the exact snapshot

The [version 1.0.3 site ZIP](MM_METHODOLOGY_V103_EN_US_SITE_v1.0.0.zip) has 750,541 bytes and SHA-256 63a548ef7ffc405280cd39331d360f3f6427b269bd67a22c904be88aec8e6cbd. Its [version-specific manifest](PUBLIC_RELEASE_MANIFEST.json) binds 26 file identities and the locally expected static Git tree b8898263e12142ef66056c10ee46cf6cdad1f750, using regular-file mode 100644.

Run the unchanged [repository verifier](../../verify_public_release.py) from the repository root with explicit version-specific arguments:

```bash
python verify_public_release.py --snapshot releases/v1.0.3/MM_METHODOLOGY_V103_EN_US_SITE_v1.0.0.zip --manifest releases/v1.0.3/PUBLIC_RELEASE_MANIFEST.json
```

On Windows:

```text
py -3 verify_public_release.py --snapshot releases/v1.0.3/MM_METHODOLOGY_V103_EN_US_SITE_v1.0.0.zip --manifest releases/v1.0.3/PUBLIC_RELEASE_MANIFEST.json
```

The root verifier's defaults and root manifest remain v1.0.2. The explicit arguments select the v1.0.3 snapshot and manifest. The verifier checks bytes, ZIP CRC, member paths, file lengths, SHA-256, Git blob IDs and a reconstructed Git tree. It does not execute supplied content, build MkDocs, contact a website, reproduce scientific results or establish live deployment.

## Unchanged scientific supplement

The supplementary archive remains [mm-methodology-v1.0.2-reproducibility-supplement.zip](https://mikejorge.github.io/mm-scientific-methodology/downloads/mm-methodology-v1.0.2-reproducibility-supplement.zip):

| Identity | Value |
|---|---|
| Path inside the site snapshot | downloads/mm-methodology-v1.0.2-reproducibility-supplement.zip |
| Bytes | 77,416 |
| SHA-256 | f1acba06eadfa3aa19bed8eb16798b9d9edb09f977e942dedbd6461e1180c4a9 |
| Approved original sources | 12 |
| Complete supplement members | 17 |

The 12 sources comprise two Python figure generators, nine selected machine-readable records and one figure source manifest; the other five members provide distribution, licensing and provenance metadata. The supplement's original bytes and version remain unchanged. Its retained historical statements must be read in their preparation context.

The supplement does not include an installable MM scientific runtime, live adapter, independent oracle, credentials, nonpublic inventories or private assurance receipts. Figure generation requires the applicable recorded environment and source-specific instructions. Hash equality or a successful HTML rendering does not establish numerical reproducibility, model validity or permission to operate infrastructure.

## Scope of the derivative

The distribution descends from R1, SHA-256 e7da9a2cad8deb50cb64649b4e172608ba9c9d9112819799aaa5187fb11baa74, through the finite edition/status delta described in the [release notes](RELEASE_NOTES.md). The native-browser observation remains bound to that R1 parent. Static source conservation and a reconstructed tree are distinct evidence from browser rendering or an observed deployment.

Rights remain governed by the supplement's notices, the website's component-level notices and [LICENSING.md](../../LICENSING.md). No additional general license or disclosure permission is created. Scientific and operational authority remains with the certified Architecture, Manual, Evidence Base and applicable execution records.
