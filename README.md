# MM Scientific Software Development and Assurance Methodology

**A practical guide to requirements, modular design, verification, validation, and evidence-based decisions in scientific software.**

MM helps research teams connect a scientific need to software requirements, interface contracts, implementation, and the evidence needed to accept a result. It makes two questions explicit: **does the software satisfy its specification, and is it suitable for its intended scientific use?**

The methodology is intended for research software engineers, scientists, solution architects, and reviewers. It provides a documented lifecycle, a Manual of 197 requirement records across 16 domains, operational checklists, and a complete synthetic learning example.

**Published edition: [v1.0.4](https://github.com/MikeJorge/mm-scientific-methodology/releases/tag/v1.0.4)** · Documentation and learning materials · 19 November 2026

[Read the methodology](https://mikejorge.github.io/mm-scientific-methodology/) · [Explore the worked example](https://mikejorge.github.io/mm-scientific-methodology/learn/worked-example/) · [Download the website](https://github.com/MikeJorge/mm-scientific-methodology/releases/download/v1.0.4/MM_METHODOLOGY_V104_EN_US_SITE_v1.0.0.zip) · [Release notes](releases/v1.0.4/RELEASE_NOTES.md)

## Start here

Choose the route that matches your task. Reading the website requires only a browser.

| I want to… | Start with | Then use |
|---|---|---|
| Understand the method | [Purpose and intended use](https://mikejorge.github.io/mm-scientific-methodology/#1-purpose) | [Verification and validation](https://mikejorge.github.io/mm-scientific-methodology/learn/verification-validation/) and the [worked example](https://mikejorge.github.io/mm-scientific-methodology/learn/worked-example/) |
| Develop or review a bounded change | [Developer and architect pathway](https://mikejorge.github.io/mm-scientific-methodology/audit/audience-pathways/#senior-developer-solution-architect) | [Requirements](https://mikejorge.github.io/mm-scientific-methodology/audit/manual-requirements/) and the [development-change checklist](https://mikejorge.github.io/mm-scientific-methodology/audit/playbooks-checklists/#cl-dev-indexed) |
| Assess scientific suitability | [Scientist pathway](https://mikejorge.github.io/mm-scientific-methodology/audit/audience-pathways/#scientist) | [Model credibility](https://mikejorge.github.io/mm-scientific-methodology/#17-scientific-model-credibility) and [scientific claim discipline](https://mikejorge.github.io/mm-scientific-methodology/#22-claim-discipline-for-scientific-publications) |
| Inspect a claim and its evidence | [Audit and traceability](https://mikejorge.github.io/mm-scientific-methodology/audit/) | [Architecture–Manual crosswalk](https://mikejorge.github.io/mm-scientific-methodology/audit/architecture-manual-crosswalk/) and [certified identities](https://mikejorge.github.io/mm-scientific-methodology/audit/certified-identities/) |
| Observe whether a new reader can apply the method | [Fresh-reader protocol](https://mikejorge.github.io/mm-scientific-methodology/learn/independent-walkthrough/) | The participant task, five-competency rubric, and session record in the learning kit |

**For a first-contact assessment, begin with the protocol.** Record prior exposure and preserve the participant's first response before substantive hints or the worked solution. Keep any later assisted response separate. The public availability of the example and assessor guidance must be considered when interpreting a session.

## Apply the method to a bounded change

Use this reading sequence alongside the [full development lifecycle](https://mikejorge.github.io/mm-scientific-methodology/#7-scientific-software-development-lifecycle) and the applicable [playbooks and checklists](https://mikejorge.github.io/mm-scientific-methodology/audit/playbooks-checklists/).

1. **Describe the scientific need and intended use.** Identify the user, the decision to support, operating conditions, assumptions, and consequences of an incorrect result.
2. **Map requirements to modules and contracts.** Identify the applicable requirements and define inputs, outputs, units, time semantics, missing-data behavior, and interface versions. See the [minimum inter-module contract](https://mikejorge.github.io/mm-scientific-methodology/#42-minimum-inter-module-contract).
3. **Define acceptance criteria before evaluating results.** Make the verification reference and validation reference explicit; identify the evidence needed for each decision.
4. **Implement and collect attributable evidence.** Preserve the relevant code, data, configuration, test expectations, and observed results so that another reviewer can reconstruct the comparison.
5. **Review the evidence and record the decision.** State what the evidence supports, which questions remain unresolved, and which next action is permitted under the applicable controls.

The [verification and validation guide](https://mikejorge.github.io/mm-scientific-methodology/learn/verification-validation/) explains the distinction:

| Evaluation | Question | Reference |
|---|---|---|
| **Verification** | Does the implementation satisfy the applicable specification? | Requirements, interface contracts, and specified expected behavior |
| **Validation** | Is the result adequate for the intended use? | Scientific need, concept of operations, users, and operating conditions |

In the worked example, total supply equals total demand, yet a deficit exists in one period. An aggregate calculation can satisfy **SRS-AGGREGATE** while failing **SRS-PERIOD** and the intended use that requires locating each deficit. The period-based solution is accepted only within the exercise's declared assumptions, contract, and fixtures.

## Run the worked example

**Requirements:** Python 3.10 or newer. The kit uses only the Python standard library; execution does not require package installation or network access.

1. [Download the learning kit](https://mikejorge.github.io/mm-scientific-methodology/downloads/MM_VV_LEARNING_AND_FRESH_READER_KIT_v1.0.0.zip) and extract it.
2. Read `README.md` and `CONOPS_AND_ACCEPTANCE.md` in the extracted kit. Review the frozen criteria and fixtures before inspecting the recorded results.
3. Open a terminal in the extracted folder containing `run_demo.py` and run the command for your environment.

**macOS / Linux:**

```bash
python3 run_demo.py
```

**Windows PowerShell:**

```powershell
py -3 run_demo.py
```

A successful run of the supplied fixtures reports:

```text
PASS_DIDACTIC_CHECKS
CHECKS=44/44
EVIDENCE_DIRECTORY=<path to the new run directory>
```

Inspect `RESULT.json` in the printed directory under `runs/`. Each run creates a new record; the supplied preparation receipt remains in `observed_preparation/`. A failed check returns a nonzero exit status.

The 44 comparisons cover two functions and 22 synthetic fixtures. They demonstrate the declared teaching contract. They do not establish the validity of a real scientific model. For session design and interpretation, use the separate [fresh-reader protocol](https://mikejorge.github.io/mm-scientific-methodology/learn/independent-walkthrough/#session-sequence).

## Download and verify v1.0.4

### Read the website offline

[Download the complete website ZIP](https://github.com/MikeJorge/mm-scientific-methodology/releases/download/v1.0.4/MM_METHODOLOGY_V104_EN_US_SITE_v1.0.0.zip), extract it, and open `index.html`. Keep the extracted folders together so that navigation, styles, figures, and downloads resolve correctly. The archive contains **20 HTML pages and 13 other files**. External references still require Internet access.

The website is a static distribution. No site build is needed to read it. The learning kit is also included in its `downloads/` folder and is extracted separately to run the example.

<details>
<summary><strong>Verify the release snapshot from a repository checkout</strong></summary>

The repository supplies `verify_public_release.py`, the version-specific manifest, and the website ZIP. The website ZIP itself does not include this repository verifier.

To obtain the frozen v1.0.4 checkout, use Git from a parent directory in which a new `mm-scientific-methodology` folder can be created:

```bash
git clone --branch v1.0.4 --single-branch https://github.com/MikeJorge/mm-scientific-methodology.git
cd mm-scientific-methodology
```

From the **repository root**, run:

```bash
python3 verify_public_release.py --snapshot releases/v1.0.4/MM_METHODOLOGY_V104_EN_US_SITE_v1.0.0.zip --manifest releases/v1.0.4/PUBLIC_RELEASE_MANIFEST.json
```

On Windows, replace `python3` with `py -3`. Select both v1.0.4 paths explicitly: the verifier's defaults still refer to the preserved v1.0.2 distribution.

The verifier uses the Python standard library to check the ZIP identity, CRC, member hashes, and reconstructed static Git tree. Its checks run locally without executing website contents or scientific software and without network requests. See the [version-specific reproducibility guidance](releases/v1.0.4/REPRODUCIBILITY.md).

**Published ZIP:** `MM_METHODOLOGY_V104_EN_US_SITE_v1.0.0.zip`  
**Size:** 787,968 bytes  
**SHA-256:**

```text
554b4b862373825151f181726dc66234ee9978f4c5ef8bff44f34f5d992e73f3
```

The [v1.0.4 manifest](releases/v1.0.4/PUBLIC_RELEASE_MANIFEST.json) provides the individual file identities. The [published release](https://github.com/MikeJorge/mm-scientific-methodology/releases/tag/v1.0.4) provides the distribution and release date.

</details>

## Reference library

| Material | Use it to… |
|---|---|
| [Architecture figure](https://mikejorge.github.io/mm-scientific-methodology/architecture-figure/) | Understand the scientific modules and their relationships |
| [Manual requirements](https://mikejorge.github.io/mm-scientific-methodology/audit/manual-requirements/) | Find the 197 DM records, their applicability, and evidence expectations |
| [Playbooks and checklists](https://mikejorge.github.io/mm-scientific-methodology/audit/playbooks-checklists/) | Prepare development, review, incident, and release activities |
| [Glossary](https://mikejorge.github.io/mm-scientific-methodology/audit/glossary/) | Resolve terminology and abbreviations |
| [Source and reference register](https://mikejorge.github.io/mm-scientific-methodology/audit/source-reference-register/) | Trace statements to their methodological and technical sources |
| [v1.0.4 release notes](releases/v1.0.4/RELEASE_NOTES.md) | Identify what changed in the documentary and learning edition |

## Scope and evidence

The published methodology explains the controlled MM development process. Certified Architecture, the Manual, Evidence Base, and applicable execution records retain authority. The documentation does not grant permission to run scientific systems. The [historical MHSMM software repository](https://github.com/MikeJorge/modulo-minimo-MHSMM) is a separate project object.

The learning example uses synthetic arithmetic. **External developer evaluation has not yet been run; observed participants: 0.** The protocol is ready for use, while empirical adoption effectiveness and real-world model validity remain unestablished.

The verification/validation diagram is an original MM illustration based on [NASA references identified in the guide](https://mikejorge.github.io/mm-scientific-methodology/learn/verification-validation/#sources-and-scope). This publication makes no claim of NASA, ISO, USP, or other institutional certification or endorsement.

## Versions and citation

Use the [v1.0.4 citation](releases/v1.0.4/CITATION.md) and identify the edition used in your work. The observed release date is **19 November 2026**. No DOI is assigned.

For reproducible references, use the [v1.0.4 tag](https://github.com/MikeJorge/mm-scientific-methodology/tree/v1.0.4) and its versioned release files. This README may evolve on `main`; the frozen distribution remains versioned separately.

Previous editions remain available: [v1.0.3](https://github.com/MikeJorge/mm-scientific-methodology/releases/tag/v1.0.3) and [v1.0.2](https://github.com/MikeJorge/mm-scientific-methodology/releases/tag/v1.0.2). Root-level `CITATION.md`, `REPRODUCIBILITY.md`, `PUBLIC_RELEASE_MANIFEST.json`, and `RELEASE_NOTES_v1.0.2.md` retain the historical v1.0.2 context. Use the **`releases/v1.0.4/` links above** for this edition.

## Author, feedback, and rights

**Michael Allim Jorge** — author and principal investigator. [ORCID: 0000-0002-7288-2095](https://orcid.org/0000-0002-7288-2095).

- **Documentation feedback:** [open an issue](https://github.com/MikeJorge/mm-scientific-methodology/issues), identifying the page or section, edition, expected behavior, and a minimal example where applicable.
- **Academic correspondence:** [rhallim.michael@usp.br](mailto:rhallim.michael@usp.br).
- **Privacy, rights, and permissions:** [rhallim.michael@gmail.com](mailto:rhallim.michael@gmail.com).

Rights are defined by [LICENSING.md](LICENSING.md), the [website copyright notice](https://mikejorge.github.io/mm-scientific-methodology/legal/copyright-licensing/), and the component-level provenance notices. The historical MIT license does not apply automatically to all methodology text, figures, or third-party material. Consult the applicable notice before reuse. See also the [privacy notice](https://mikejorge.github.io/mm-scientific-methodology/legal/privacy/).
