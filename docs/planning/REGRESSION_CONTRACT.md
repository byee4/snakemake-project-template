# REGRESSION_CONTRACT — <Project Name>

<!--
  PURPOSE
    This file defines "the workflow matches the notebook." For each
    output, it states whether the comparison must be byte-for-byte
    (identical SHA-256), numeric within a stated tolerance, or
    excluded from comparison.

    Phase 4 regression tests read this file and act on every entry.
    Without it, "does the workflow match the notebook?" devolves into
    eyeballing PDFs — which is how silent scientific drift sneaks in.

  WHEN IT IS WRITTEN
    Phase 2 — Review. Signed at the Review gate.
    Regenerating the `expected/` directory later requires the Review
    gate to fire again (`git tag review/<intent_id>+1`).

  WHO SIGNS
    The project lead and at least one peer with bench knowledge of the
    science. Not just the PR author.
-->

## Reference fixture

- **Path:** `tests/fixtures/`
- **Description:** <!-- e.g. "50k-read public ENCODE paired-end FASTQ + chr22-only STAR index" -->
- **Source(s):** <!-- accessions or URLs -->
- **Frozen expected outputs:** `tests/fixtures/expected/`

## Outputs

### Byte-exact

These outputs must equal the notebook's outputs on the reference fixture exactly. Compared via SHA-256.

| Output | Path (relative to run directory) | Notebook SHA-256 |
| --- | --- | --- |
| <!-- e.g. counts_tsv --> | <!-- results/<sample>/counts.tsv --> | <!-- abc123... --> |

### Numeric within tolerance

These outputs must be numerically equivalent within the stated tolerance. Compared by parsing the file and using `pytest.approx`.

| Output | Path | Comparison fields | Relative tolerance | Justification |
| --- | --- | --- | --- | --- |
| <!-- e.g. fastp_json --> | <!-- results/<sample>/fastp.json --> | <!-- summary.before_filtering.q30_rate --> | <!-- 1e-9 --> | <!-- floating-point reductions in fastp >=0.23 --> |

### Excluded from comparison

These outputs are recorded in the regression report but not compared. Each line states **why**.

| Output | Reason for exclusion |
| --- | --- |
| <!-- e.g. qc_pdf --> | <!-- PDF rendering varies across matplotlib versions --> |
| <!-- e.g. multiqc_html --> | <!-- embeds run timestamp --> |

## How a failing regression is investigated

1. Run `make test` and read the failing assertion, locally or in the GitHub Actions log.
2. For each byte-exact failure, run the workflow locally on the same fixture and diff the two outputs with `cmp`.
3. For numeric failures, inspect the offending field and decide whether the tolerance band needs to be widened (justified) or the workflow needs to be fixed.
4. **Never** regenerate `expected/` to make a failing test pass without re-firing the Review gate. That is "regression test laundering" and is a documented failure mode in the [Notebook to Snakemake Workflow tutorial](https://github.com/YeoLab/ai-kb/blob/main/Tutorials/Research_Accelerators/Notebook_to_Snakemake_Workflow_Beginner.md#common-failure-modes).

## Sign-off

- Drafted by: <!-- AI agent + date -->
- Project lead approval: <!-- name + date -->
- Domain peer approval: <!-- name + date -->
- Tag: `review/<intent_id>` <!-- once approved -->
