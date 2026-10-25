# tools.md — <Project Name>

<!--
  PURPOSE
    This file pins every command-line tool the workflow uses to an
    exact version and cites the source for every default parameter.
    Results depend on tool versions; pinning is the difference
    between "reproducible in 2027" and "the binary is gone, sorry."

  WHEN
    Phase 2 — Review. Drafted by the AI agent during the skeptic
    pass, finalized at the Review gate.

  HOW TO USE
    - Every conda env file under `workflow/envs/` pins the version
      listed here.
    - Every container image referenced in the Snakefile uses an
      `@sha256:` digest derived from the version listed here.
    - Any default parameter without a citation gets a [NEEDS_SOURCE: ...]
      marker until resolved.
-->

## Tool table

| Tool | Version pin | Conda channel | Container (with digest) | Purpose |
| --- | --- | --- | --- | --- |
| <!-- e.g. fastp --> | <!-- 0.23.4 --> | <!-- bioconda --> | <!-- biocontainers/fastp@sha256:abc... --> | <!-- adapter trimming --> |
| <!-- e.g. STAR --> | <!-- 2.7.11b --> | <!-- bioconda --> | <!-- biocontainers/star@sha256:def... --> | <!-- RNA-seq alignment --> |
| <!-- e.g. featureCounts (subread) --> | <!-- 2.0.6 --> | <!-- bioconda --> | <!-- biocontainers/subread@sha256:... --> | <!-- read summarization --> |
| <!-- e.g. multiqc --> | <!-- 1.22.1 --> | <!-- bioconda --> | <!-- biocontainers/multiqc@sha256:... --> | <!-- QC aggregation --> |
| <!-- e.g. python --> | <!-- 3.11.9 --> | <!-- conda-forge --> | <!-- n/a (env) --> | <!-- script runtime --> |

## Default parameters with citation

For every non-trivial default value used in the workflow, list it and cite a source (paper, vendor manual, lab protocol, or notebook author's decision).

| Tool | Parameter | Value | Source |
| --- | --- | --- | --- |
| <!-- e.g. fastp --> | <!-- --qualified_quality_phred --> | <!-- 15 --> | <!-- fastp default; cite Chen 2018 --> |
| <!-- e.g. STAR --> | <!-- --outFilterMismatchNoverLmax --> | <!-- 0.04 --> | <!-- [NEEDS_SOURCE: ...] --> |

## Tools the workflow is forbidden from installing at runtime

These rules are enforced by `pre-commit` and CI:

- No `pip install ...` inside a rule's `shell:` block.
- No `conda install ...` inside a rule's `shell:` block.
- No container tag named `latest`.
- No hardcoded paths under `/scratch`, `/oasis`, or `/tscc` outside `config.yaml`.

## Sign-off

- Drafted by: <!-- AI agent + date -->
- Project lead approval: <!-- name + date; PR comment `approve: review` -->
