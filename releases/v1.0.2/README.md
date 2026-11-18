# MM Scientific Software Development and Assurance Methodology

**A versioned, evidence-governed methodology for the engineering, verification, validation, traceability, and controlled release of scientific software.**

[**Read the published methodology**](https://mikejorge.github.io/mm-scientific-methodology/) · [Audit and traceability](https://mikejorge.github.io/mm-scientific-methodology/audit/) · [Reproducibility supplement](https://mikejorge.github.io/mm-scientific-methodology/downloads/mm-methodology-v1.0.2-reproducibility-supplement.zip) · [Citation](CITATION.md) · [Licensing](LICENSING.md)

| Publication metadata | Verified or controlled identity |
| --- | --- |
| Scientific edition | **v1.0.2** |
| Publication type | Scientific development and assurance **methodology / technical documentation**; **not** an installable MM runtime |
| Author and principal investigator | **Michael Allim Jorge** · [ORCID 0000-0002-7288-2095](https://orcid.org/0000-0002-7288-2095) |
| Public site | <https://mikejorge.github.io/mm-scientific-methodology/> |
| Source of the deployed static site | [`gh-pages`](https://github.com/MikeJorge/mm-scientific-methodology/tree/gh-pages), repository root |
| Public distribution and version documentation | [`main`](https://github.com/MikeJorge/mm-scientific-methodology/tree/main) |
| First verified HTTPS publication | **17 November 2026**; Work readback recorded 17/17 HTML routes and 25/25 public payload files |
| Frozen public site | **26 Git files**: 25 approved distribution files plus the empty `.nojekyll` sentinel |
| Digital object identifier | **None assigned**; do not infer a Zenodo deposit or journal publication |

> **Scope and authority.** This is a public documentation projection of the controlled MM/MHSMM scientific-development methodology. Publication, passing a static-site check, and possession of this repository **do not** certify a scientific model, grant operational permission, authorize execution, or establish endorsement by NASA, ISO, USP, or any other institution.

## 1. What this publication contributes

MM defines how a modular scientific software system is **specified, built, checked, validated for its intended use, integrated, documented, independently examined, and released under explicit authority**. Its governing assurance questions are complementary: **Was the system built correctly?** (*verification*) and **Was the correct system built for the scientific purpose?** (*validation*).

The methodology joins scientific questions and domain models to software-engineering controls: typed interface contracts; dimensional, spatial, and temporal consistency; numerical and statistical assurance; uncertainty quantification; independently checkable evidence; release identity; and a fail-closed authorization regime. It is applicable to the MM/MHSMM modular modeling context and describes a transferable engineering approach **without asserting universal validation of any model or implementation**.

**Core mechanisms, as specified by the published methodology:**

- **Authority hierarchy:** certified scientific architecture governs; the subordinate assurance manual refines operational requirements but cannot override architectural prohibitions.
- **Four execution-control planes:** **Control**, **Execution**, **Authority**, and **Evidence/Provenance**, with **Data/Catalog governance** as a cross-cutting function—not a fifth execution plane.
- **Gate contracts:** scoped inputs, permitted effects, roles, preconditions, evidence predicates, exhaustive terminal-state classes, independent readback, a single next admissible action, and `STOP=true`.
- **Evidence discipline:** `DIRECT`, `BOUND`, `DERIVED`, `HISTORICAL`, and `NOT_ESTABLISHED` are distinct states; derived or historical evidence must not masquerade as a current direct observation.
- **Scientific quality:** traceability from scientific intent to requirements, architecture, detailed design, implementation, V&V, integration, uncertainty, and scientifically credible claims.
- **Separation of duties:** execution and independent assurance have different roles; missing, inconsistent, or inadmissible evidence yields **HOLD**, not inferred PASS.

The published material includes a register of **197 manual requirement records**, a **50-record Architecture–Manual crosswalk**, playbooks/checklists, source-status information, content-conservation evidence, and bounded historical assurance records. These are navigational and traceability artifacts; their public availability does not make private operational evidence public.

## 2. Where to start

| Reader | Entry point | Follow with |
| --- | --- | --- |
| Scientist / modeler | [Purpose, scientific lifecycle, V&V, uncertainty](https://mikejorge.github.io/mm-scientific-methodology/) | [Glossary](https://mikejorge.github.io/mm-scientific-methodology/audit/glossary/) and [source register](https://mikejorge.github.io/mm-scientific-methodology/audit/source-reference-register/) |
| Software architect / senior developer | [Development architecture](https://mikejorge.github.io/mm-scientific-methodology/architecture-figure/) | [Architecture–Manual crosswalk](https://mikejorge.github.io/mm-scientific-methodology/audit/architecture-manual-crosswalk/) and [playbooks](https://mikejorge.github.io/mm-scientific-methodology/audit/playbooks-checklists/) |
| Independent auditor / reviewer | [Audit and traceability](https://mikejorge.github.io/mm-scientific-methodology/audit/) | [197 requirement records](https://mikejorge.github.io/mm-scientific-methodology/audit/manual-requirements/), [identities](https://mikejorge.github.io/mm-scientific-methodology/audit/certified-identities/), and [conservation crosswalk](https://mikejorge.github.io/mm-scientific-methodology/audit/conservation-crosswalk/) |
| Reproducibility / provenance reader | [Reproducibility boundary](REPRODUCIBILITY.md) | [Evidence overlay](https://mikejorge.github.io/mm-scientific-methodology/audit/evidence-overlay/) and [local execution-adapter figure](https://mikejorge.github.io/mm-scientific-methodology/local-execution-adapter/) |
| Editor or prospective citer | [Citation guidance](CITATION.md) | [Release notes](RELEASE_NOTES_v1.0.2.md) and [licensing boundaries](LICENSING.md) |

The website contains **17 HTML pages**: 15 methodology/assurance pages and two bilingual legal pages. Read the [audience pathways](https://mikejorge.github.io/mm-scientific-methodology/audit/audience-pathways/) for a curated navigation sequence.

## 3. Repository and publication architecture

```text
Private engineering/execution evidence (not distributed here)
    | authorized, reviewed public projection
    v
main: version documentation + full public ZIP snapshot + manifest
    | exact static payload (no scientific runtime)
    v
gh-pages: 17 HTML + 5 figure assets + CSS + sitemap + supplement + .nojekyll
    | GitHub Pages: Deploy from gh-pages / (root)
    v
https://mikejorge.github.io/mm-scientific-methodology/
```

This **dedicated methodology repository** is distinct from the [historical MHSMM software repository](https://github.com/MikeJorge/modulo-minimo-MHSMM) and the separately controlled private MkDocs executor. Neither the historical software's maturity nor the private executor's assurance receipts should be inferred from the public site.

```text
main/
├── README.md                          # entry point and scientific scope
├── CITATION.md                        # citable description; no invented DOI
├── LICENSING.md                       # differentiated IP/licensing notices
├── REPRODUCIBILITY.md                 # scientific reproducibility boundary
├── RELEASE_NOTES_v1.0.2.md           # edition and publication provenance
├── PUBLIC_RELEASE_MANIFEST.json       # per-member hashes and Git blob IDs
├── verify_public_release.py           # read-only, standard-library verifier
└── releases/v1.0.2/
    └── MM_METHODOLOGY_V102_DEDICATED_GHPAGES_SITE_NOT_DEPLOYED_v1.0.0.zip

gh-pages/
├── index.html                          # primary scientific methodology
├── architecture-figure/
├── local-execution-adapter/
├── audit/                              # 12 pages of review/traceability
├── legal/privacy/
├── legal/copyright-licensing/
├── assets/                             # CSS and figure assets
├── downloads/                          # versioned public supplement
├── sitemap.xml
└── .nojekyll                          # deployment sentinel
```

The ZIP filename retains `NOT_DEPLOYED` because **the snapshot was frozen before publication**; it is preserved as an immutable identifier, **not** a claim about the current HTTPS status. Likewise, `repository_creation_executed=false` and `publication_executed=false` in the historical `PUBLIC_RELEASE_MANIFEST.json` describe its **pre-publication preparation state**, not the subsequently verified deployment. Do not rewrite the frozen manifest to retroactively change that provenance.

## 4. Immutable v1.0.2 evidence anchors

| Artifact | Exact identity |
| --- | --- |
| Frozen site snapshot ZIP | **728,136 bytes** · SHA-256 `096a3bac4fde59ee42792343a3880e33e794b7c02c1870750ff882cb095ab92b` |
| Deployed `gh-pages` Git tree | `d6dbd9b7b275d80066bbe631c7c90b7b85466cd2` |
| Deployment commit verified at initial publication | `acd8a9310f3e1c3c536de18cabbf3afabbd1ba13` |
| Public scientific supplement ZIP | **77,416 bytes** · SHA-256 `f1acba06eadfa3aa19bed8eb16798b9d9edb09f977e942dedbd6461e1180c4a9` |
| Approved original public release | 25 files; 24 byte-conserved in the dedicated-repository projection, and 17 site-map URLs rebound to its new public address |
| Initial HTTPS verification | 17/17 sitemap HTML routes and 25/25 public content-file identities (reported by Work, 17 November 2026, 20:49 BRT) |

**Hash semantics:** SHA-256 identifies distributed bytes. Git SHA-1 identifies Git objects/trees in this repository; it is **not** a cryptographic signature or a substitute for independent scientific validation. The embedded manifest and external hash comparisons help detect drift, but a compromised repository could change an artifact and its own manifest together. Retain independent evidence of release identity for high-assurance use.

## 5. Verify the frozen snapshot locally

Requirements: **Python 3.9+ (standard library only)**; no MkDocs installation, scientific runtime, credentials, environment provisioning, or external Python dependencies are required.

```bash
git clone https://github.com/MikeJorge/mm-scientific-methodology.git
cd mm-scientific-methodology
python verify_public_release.py
```

On Windows, use `py -3 verify_public_release.py` if `python` is not on `PATH`. The verifier is read-only: it does **not** extract or execute ZIP members. It checks the snapshot size and SHA-256, ZIP CRC, exact file inventory, all 26 per-file lengths and SHA-256 digests, all Git blob object IDs, and the reconstructed recursive Git tree.

Expected output includes:

```text
PASS: MM public release snapshot integrity
version=1.0.2
snapshot_sha256=096a3bac4fde59ee42792343a3880e33e794b7c02c1870750ff882cb095ab92b
verified_files=26
git_tree_sha1=d6dbd9b7b275d80066bbe631c7c90b7b85466cd2
supplement_sha256=f1acba06eadfa3aa19bed8eb16798b9d9edb09f977e942dedbd6461e1180c4a9
scope=static_snapshot_integrity_only; no scientific runtime executed
```

For an independent Git-level comparison:

```bash
git fetch origin gh-pages
git rev-parse origin/gh-pages^{tree}
```

For a **version-pinned comparison**, first select the recorded deployment commit rather than assuming that a moving branch will remain unchanged. A future `v1.0.2` tag, if issued, should identify the versioned **`main` distribution commit**; its embedded snapshot and manifest bind the deployed `gh-pages` tree. An attached GitHub Release ZIP is an additional distribution surface, not the authority for different scientific content.

## 6. Reproducibility: what the supplement does and does not establish

The [versioned public supplement](https://mikejorge.github.io/mm-scientific-methodology/downloads/mm-methodology-v1.0.2-reproducibility-supplement.zip) includes **12 approved original scientific sources**: two Python figure-generator scripts, nine selected machine-readable research/assurance records, and one figure source manifest, plus five distribution, licensing, and provenance files (17 supplement members total).

It supports inspection of selected figure sources and published traceability data. It **does not** package a complete executable MM scientific model, DSSAT integration, credentials, independent oracle, live adapter, private QA receipts, or authority to perform protected operations. Figure-generation reproducibility may require the dependencies and conditions described in the supplement; the verifier above checks **bytes**, not numerical reproducibility, model credibility, or scientific correctness.

The second figure's [C2PA/provenance note](https://mikejorge.github.io/mm-scientific-methodology/local-execution-adapter/#figure2-c2pa-provenance) documents associated metadata and expressly does **not** assert independent signature verification or infer that the diagram was generated by an image-generation model. The recorded Python/Matplotlib provenance is retained.

## 7. Governance, changes, and scientific claims

This is a **controlled edition**. Proposed changes should identify the impacted authority, scientific/engineering requirement, intended use, affected interfaces, falsifiable acceptance predicate, necessary test evidence, independent reviewer, and resulting release boundary. Preserve a distinction between **historical certification**, **current publication evidence**, and **runtime authorization**. A passing website check is not evidence that the scientific software is operationally or scientifically validated.

For subsequent editions, use separate versioned records rather than silently modifying the v1.0.2 snapshot. Do not disclose unpublished inventories, credentials, assurance receipts, or private execution controls in public artifacts. A public contribution or issue does not itself authorize a Gate or a change to protected scientific systems.

## 8. Attribution, rights, privacy, and contact

- **Citation:** [CITATION.md](CITATION.md). No DOI has been assigned; refer to the version, repository, and any **actually issued** tag/Release rather than inventing a persistent identifier.
- **Copyright/IP:** [Licensing scope](LICENSING.md) and [website legal notice](https://mikejorge.github.io/mm-scientific-methodology/legal/copyright-licensing/). An MIT license in the historical software repository is **not** a blanket license for this methodology's text, figures, and third-party content; no additional general CC BY grant is implied.
- **Privacy:** [Bilingual privacy notice](https://mikejorge.github.io/mm-scientific-methodology/legal/privacy/). GitHub Pages hosting and email providers may process data independently of the static site's code.
- **Academic/scientific correspondence:** [rhallim.michael@usp.br](mailto:rhallim.michael@usp.br).
- **Privacy, permissions, IP, and legal correspondence:** [rhallim.michael@gmail.com](mailto:rhallim.michael@gmail.com). Do not submit personal or confidential records through public GitHub issues.

**Institutional boundary:** Academic affiliation, citations to standards or NASA guidance, and the use of a university email address do not establish institutional ownership, approval, certification, or endorsement.

---

**Version discipline:** v1.0.2 identifies the methodology edition and its published public distribution. **Static-site identity, software-runtime authority, independent scientific validation, archival DOI, and GitHub Release issuance are distinct propositions and must be evidenced separately.**
