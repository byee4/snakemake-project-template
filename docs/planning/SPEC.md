# SPEC — <Project Name>

<!--
  PURPOSE
    This is the contract that describes what the source notebook does.
    Every later phase (Review, Build, Test, Deploy) measures itself
    against this file. No code is written until SPEC.md is reviewed
    and a project lead has commented `approve: plan` on the pull
    request that introduces it.

  HOW TO FILL IT IN
    1. Have your AI coding partner read the notebook and produce a
       first draft, following the RULES FOR THE AI below.
    2. Read every section yourself against the original notebook.
    3. Where the AI wrote [NEEDS_INFO: ...], answer the question.
    4. Where the AI guessed a number, correct it from the notebook.
    5. Open a pull request and request review from the project lead.

  RULES FOR THE AI
    - Do not invent parameters, accessions, or thresholds.
    - Mark cells that only print or plot as "diagnostic only."
    - Carry over every constant byte-identical; the notebook's seed
      stays the notebook's seed.
    - If a cell looks ambiguous, write [NEEDS_INFO: ...] instead of
      guessing.
-->

## Goal

<!-- One sentence. Example: -->
<!-- "Take paired-end bulk RNA-seq FASTQ for a cohort of N samples, trim adapters, align to GRCh38, count reads per gene, and produce a MultiQC report plus a count matrix." -->

TODO

## Data Classification

- **Highest data class for any input:** <!-- Class 0 (Public; UC P1) | Class 1 (Internal; UC P2) | Class 2 (Controlled; UC P3) | Class 3 (Restricted; UC P4) -->
- **Restricted inputs (if any):** <!-- list, or "none" -->
- **Approved tool tier for this work:** <!-- A | B | C -->

See the [Glossary entries on Data Class](https://github.com/YeoLab/ai-kb/blob/main/Glossary.md#data-class) if unsure.

## Scope

### In scope

<!-- List every cell or block of the notebook that does scientific work.
     For each: what files it reads, what files it writes. -->

- TODO

### Out of scope

<!-- What the workflow will not do. Examples: "downstream DE analysis,"
     "patient cohort linkage," "cross-species alignment." -->

- TODO

### Do not touch

<!-- Files, directories, or parameters that must be preserved exactly. -->

- The random seed value(s) listed in `PARAMS.md`.
- TODO

## Inputs

| Input | Path / source | Data class | How to verify |
| --- | --- | --- | --- |
| <!-- e.g. paired R1 FASTQ --> | <!-- ENCFF... or local path --> | <!-- 0/1/2/3 --> | <!-- e.g. sha256 + ENCODE accession --> |

## Output Contract

| Output | Location | Schema / fields | Downstream consumer |
| --- | --- | --- | --- |
| <!-- e.g. counts.tsv --> | <!-- results/{sample}/counts.tsv --> | <!-- columns: gene_id (str), counts (int) --> | <!-- e.g. DESeq2 script, manuscript Figure 3 --> |

## Plan

<!-- Number the steps in run order. Each step should map to a node in dag.yaml. -->

1. TODO
2. TODO
3. TODO

## Acceptance checks

<!-- How a reviewer will know each step is correct. Be specific. -->

- [ ] TODO — e.g. "counts.tsv has one row per gene in the GTF and no negative values."
- [ ] TODO
- [ ] TODO

## Constraints / Do Not Touch

<!-- Anything that must carry over exactly: random seeds, version pins,
     hand-picked thresholds with a citation, etc. -->

- TODO

## Open questions

<!-- Anything the AI flagged as [NEEDS_INFO: ...] that has not yet been answered. -->

- TODO

---

## Sign-off

- Spec author: <!-- name and date -->
- Project lead approval: <!-- name and date; PR comment `approve: plan` -->
- Tag: `plan/<intent_id>` <!-- once approved -->
