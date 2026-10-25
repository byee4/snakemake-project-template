# AGENTS.md — Snakemake Project Template

Operating instructions for people and coding agents working in this workflow.

## Project shape

```
config/config.yaml  Run configuration for real inputs.
config/test.yaml    Test configuration; points at tests/fixtures/.
workflow/Snakefile  Workflow entry point; includes rules/*.smk.
workflow/rules/     Rules grouped by logical pipeline stage.
workflow/envs/      Per-rule conda environments, with pinned versions.
resources/          Small tracked example inputs only; large inputs stay outside Git.
results/            Generated outputs (ignored, except .gitkeep).
profiles/           Execution-profile settings; add cluster profiles here.
tests/              Workflow checks and the regression test.
tests/fixtures/     Tiny public test input and its frozen expected output.
docs/               Design notes and the maintained codemap.
docs/planning/      Notebook-conversion plan: SPEC, PARAMS, dag.yaml and others.
```

## Data boundaries

- **Highest expected data class:** <!-- Class 0 (Public; UC P1) | Class 1 (Internal; UC P2) | Class 2 (Controlled; UC P3) | Class 3 (Restricted; UC P4) -->
- **Allowed data:** `tests/fixtures/` and `resources/` (Class 0). <!-- add project-specific paths -->
- **Denied data:** `data/raw/`, `data/restricted/`, and anything outside this repository unless listed above.
- **Secrets:** `.env` stays local and ignored by Git. Never print, paste or commit its contents.

## Working rules

1. Read `docs/codemap.md` and the affected rule/config before changing a workflow.
   When converting a notebook, also read `docs/planning/SPEC.md`, `PARAMS.md` and `dag.yaml`.
2. Create a branch before every feature or bugfix; never commit directly to `main`.
3. Keep rules declarative: declare every input, output, parameter, resource, and
   conda/container environment. Do not hide workflow work in untracked scripts.
4. Never commit large source data, generated results, credentials, or `.snakemake/`.
   Document data acquisition and use config paths or environment variables instead.
5. Make every rule reproducible: outputs must derive solely from declared inputs,
   params, software environment, and code.
6. Update `README.md`, `config/config.yaml`, and `docs/codemap.md` when a public
   pipeline interface, input, output, or invocation changes.
7. Do not invent parameters, thresholds or accessions; write `[NEEDS_INFO: ...]` instead.
8. Never regenerate `tests/fixtures/expected/` to make a failing test pass. Explain
   the difference and let a person decide.
9. Do not use container tags named `latest`, `pip`/`conda install` inside a rule, or
   cluster paths (`/scratch`, `/oasis`, `/tscc`) outside config. `make lint` checks these.
10. Ask a person before pushing to `main`, opening a PR, sending data to an external
    service, running the workflow on real data (`make run` or a cluster profile),
    deleting files, or changing `.github/`.

## Before reporting a change complete

Run the relevant checks, at minimum:

```bash
make lint
make dry-run
make test
```

Report each command and its result. Describe any test data, external service, or
scheduler requirement that could not be exercised. When you stop, list the files you
changed and any `[NEEDS_INFO: ...]` markers you left.
