# PARAMS — <Project Name>

<!--
  PURPOSE
    Every hard-coded constant in the source notebook lives here. The
    notebook's `seed = 42` stays `42`. No "modernized" defaults, no
    rounding, no silent re-derivation.

    The values in this table become keys in `config.yaml` during
    Phase 3. The Snakemake rules read from `config.yaml`, never from
    inlined constants.

  HOW TO FILL IT IN
    1. Have your AI coding partner scan the notebook (and any
       helper modules it imports) for every literal value used as
       a parameter. That includes file paths, thresholds, k-values,
       random seeds, batch sizes, and version strings.
    2. For each, fill in one row of the table below.
    3. If a value has no citation, the AI should mark it
       [NEEDS_SOURCE: ...] and the project owner should resolve it
       before the Review gate.
-->

## Parameter table

| Name | Current value | Where used (cell / file) | Suggested config key | Source / citation |
| --- | --- | --- | --- | --- |
| <!-- e.g. random_seed --> | <!-- 42 --> | <!-- cell #2 --> | <!-- random_seed --> | <!-- notebook author's choice --> |
| <!-- e.g. min_mapq --> | <!-- 30 --> | <!-- cell #6 --> | <!-- align.min_mapq --> | <!-- [NEEDS_SOURCE: ...] --> |
| <!-- e.g. star_version --> | <!-- 2.7.11b --> | <!-- envs/align.yaml --> | <!-- tools.star.version --> | <!-- pinned per tools.md --> |

## Notes

- A magic number in code with no entry in this table is a bug.
- A magic number whose `Source / citation` is empty is unfinished work; resolve it before signing the Review gate.
- Random seeds must be configurable but defaulted to the notebook's original value.

## Sign-off

- Drafted by: <!-- AI agent + date -->
- Reviewed by: <!-- project owner + date -->
- Final approval at the Plan gate: <!-- project lead + date; PR comment `approve: plan` -->
