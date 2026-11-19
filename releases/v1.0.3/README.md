# MM Scientific Software Development and Assurance Methodology

**Documentary edition v1.0.3**

A versioned, evidence-governed methodology for the engineering, verification, validation, traceability, and controlled release of scientific software.

[Methodology website](https://mikejorge.github.io/mm-scientific-methodology/) · [Audit and traceability](https://mikejorge.github.io/mm-scientific-methodology/audit/) · [v1.0.3 citation](releases/v1.0.3/CITATION.md) · [v1.0.3 reproducibility](releases/v1.0.3/REPRODUCIBILITY.md) · [Licensing](LICENSING.md)

| Edition information | Identity |
|---|---|
| Author and principal investigator | Michael Allim Jorge · [ORCID 0000-0002-7288-2095](https://orcid.org/0000-0002-7288-2095) |
| Edition | 1.0.3 |
| Object | Scientific development and assurance methodology and controlled technical documentation |
| Website address | https://mikejorge.github.io/mm-scientific-methodology/ |
| Frozen distribution | [Version 1.0.3 site ZIP](releases/v1.0.3/MM_METHODOLOGY_V103_EN_US_SITE_v1.0.0.zip) |
| Artifact manifest | [Version 1.0.3 manifest](releases/v1.0.3/PUBLIC_RELEASE_MANIFEST.json) |
| Edition changes | [Version 1.0.3 release notes](releases/v1.0.3/RELEASE_NOTES.md) |
| Website file set | 26 regular files, including 17 HTML pages and nine non-HTML members |

## Purpose and authority

MM defines how a modular scientific software system is specified, built, checked, validated for its intended use, integrated, documented, independently examined, and released under explicit authority. Its governing assurance questions are complementary: Was the system built correctly? (verification) and Was the correct system built for the scientific purpose? (validation).

The methodology joins scientific questions and domain models to software-engineering controls: typed interface contracts; dimensional, spatial, and temporal consistency; numerical and statistical assurance; uncertainty quantification; independently checkable evidence; release identity; and a fail-closed authorization regime. It describes a transferable engineering approach without asserting universal validation of any model or implementation.

Certified Architecture, the subordinate Manual, the Evidence Base and applicable execution records retain their authority. The methodology includes 197 Manual requirement records, a 50-record Architecture–Manual crosswalk, playbooks, checklists and source/provenance records. Public access to those records does not disclose the private execution evidence or authorize scientific operation.

This repository provides a documentation projection. Website publication, static-file verification and repository access do not establish model validation, runtime permission, regulatory compliance, institutional ownership or endorsement by NASA, ISO, USP or another institution. The historical [MHSMM software repository](https://github.com/MikeJorge/modulo-minimo-MHSMM) and the controlled execution infrastructure remain separate.

## Read the edition

| Reader need | Entry point |
|---|---|
| Methodological narrative and scientific lifecycle | [Methodology website](https://mikejorge.github.io/mm-scientific-methodology/) |
| Terminology and cited sources | [Glossary](https://mikejorge.github.io/mm-scientific-methodology/audit/glossary/) and [source register](https://mikejorge.github.io/mm-scientific-methodology/audit/source-reference-register/) |
| Requirements and architecture | [Manual records](https://mikejorge.github.io/mm-scientific-methodology/audit/manual-requirements/) and [Architecture–Manual crosswalk](https://mikejorge.github.io/mm-scientific-methodology/audit/architecture-manual-crosswalk/) |
| Figure sources and reuse limits | [Version 1.0.3 reproducibility guidance](releases/v1.0.3/REPRODUCIBILITY.md) |
| Citation and edition differences | [Citation](releases/v1.0.3/CITATION.md) and [release notes](releases/v1.0.3/RELEASE_NOTES.md) |

The address above is the repository's website destination. A version number or local expected tree in an artifact manifest is not, by itself, evidence of which bytes a live server currently delivers. Actual deployment events and HTTPS comparisons belong to their execution receipt.

## Exact v1.0.3 distribution

| Object | Identity |
|---|---|
| Snapshot | MM_METHODOLOGY_V103_EN_US_SITE_v1.0.0.zip |
| Snapshot bytes | 750,541 |
| Snapshot SHA-256 | 63a548ef7ffc405280cd39331d360f3f6427b269bd67a22c904be88aec8e6cbd |
| Expected static Git tree, mode 100644 | b8898263e12142ef66056c10ee46cf6cdad1f750 |
| Unchanged scientific supplement | 77,416 bytes; SHA-256 f1acba06eadfa3aa19bed8eb16798b9d9edb09f977e942dedbd6461e1180c4a9 |

The version-specific manifest binds all 26 file lengths, SHA-256 values and Git blob IDs. Its expected tree is calculated locally from those files; it is not an asserted remote commit. SHA-256 and Git object IDs identify bytes and objects, not signatures or scientific validity.

## Verify the selected version

The unchanged root verifier and its default arguments retain the v1.0.2 distribution. To select v1.0.3, run the following from the repository root:

```bash
python verify_public_release.py --snapshot releases/v1.0.3/MM_METHODOLOGY_V103_EN_US_SITE_v1.0.0.zip --manifest releases/v1.0.3/PUBLIC_RELEASE_MANIFEST.json
```

On Windows, the equivalent Python launcher command is:

```text
py -3 verify_public_release.py --snapshot releases/v1.0.3/MM_METHODOLOGY_V103_EN_US_SITE_v1.0.0.zip --manifest releases/v1.0.3/PUBLIC_RELEASE_MANIFEST.json
```

The existing standard-library verifier checks the archive identity, CRC, exact member set, per-file hashes, Git blob IDs and reconstructed static tree. It does not execute the site contents, recreate figures, run MM software, contact the network or establish live deployment.

## Assurance scope

Version 1.0.3 contains source-bound American English, terminology, first-use definition and navigation improvements, together with readable projections of unchanged certified records. Independent native-browser evidence applies to the exact R1 parent, SHA-256 e7da9a2cad8deb50cb64649b4e172608ba9c9d9112819799aaa5187fb11baa74. The distribution here adds a finite current-edition/status delta: 21 rules at 81 occurrences in 17 HTML files. Its nine non-HTML members and controlled records remain conserved.

The original native screenshots are not relabeled as observations of this different ZIP. The [release notes](releases/v1.0.3/RELEASE_NOTES.md) explain the separate status derivation and the retained EVID-01 capture limitation. These source and artifact records do not replace the release-specific decision or execution receipt.

## Historical v1.0.2 records

For the original reading context, use the [README at tag v1.0.2](https://github.com/MikeJorge/mm-scientific-methodology/blob/v1.0.2/README.md) and its tagged companion documents. The [archived README copy](releases/v1.0.2/README.md) is byte-identical to that predecessor. Its original relative links are deliberately preserved; the tagged README is the preferred way to follow them.

The root CITATION.md, REPRODUCIBILITY.md, PUBLIC_RELEASE_MANIFEST.json, RELEASE_NOTES_v1.0.2.md and verifier defaults remain the v1.0.2 records. The original v1.0.2 site snapshot remains in its existing path. Use the version-specific v1.0.3 links above for this edition. Root LICENSING.md retains the applicable differentiated rights notice.

Preparation-time flags in frozen manifests describe when those records were made. They are preserved as provenance and must not be silently rewritten to simulate later deployment events.

## Reproducibility, rights and contact

The unchanged [v1.0.2 reproducibility supplement](https://mikejorge.github.io/mm-scientific-methodology/downloads/mm-methodology-v1.0.2-reproducibility-supplement.zip) contains 12 approved original sources: two Python figure generators, nine selected machine-readable records and one figure source manifest, plus distribution and rights metadata. It is not an installable scientific model, live adapter, credential collection or permission to operate scientific infrastructure.

Rights are described in [LICENSING.md](LICENSING.md), the [website notice](https://mikejorge.github.io/mm-scientific-methodology/legal/copyright-licensing/) and the supplement's component notices. The historical MIT license is not a blanket license for all methodology text, figures or third-party material. This edition creates no new general Creative Commons grant, IP assignment or institutional endorsement.

For academic or scientific correspondence: [rhallim.michael@usp.br](mailto:rhallim.michael@usp.br). For privacy, rights, licensing or permissions: [rhallim.michael@gmail.com](mailto:rhallim.michael@gmail.com). The [privacy notice](https://mikejorge.github.io/mm-scientific-methodology/legal/privacy/) distinguishes the project's static content from hosting-provider processing. Do not send personal or confidential material through public issues.

No DOI is supplied by these edition documents. Use the [citation guidance](releases/v1.0.3/CITATION.md), the exact snapshot identity and version references that have actually been issued.
