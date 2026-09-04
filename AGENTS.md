# AGENTS.md — Snakemake Project Template

Operating instructions for people and coding agents working in this workflow.

## Project shape

```
config/             User-editable pipeline configuration.
workflow/Snakefile  Workflow entry point; includes rules/*.smk.
workflow/rules/     Rules grouped by logical pipeline stage.
resources/          Small tracked example inputs only; large inputs stay outside Git.
results/            Generated outputs (ignored, except .gitkeep).
profiles/            Execution-profile settings; add cluster profiles here.
tests/               Lightweight workflow and configuration checks.
docs/                Design notes and the maintained codemap.
```

## Working rules

1. Read `docs/codemap.md` and the affected rule/config before changing a workflow.
2. Create a branch before every feature or bugfix; never commit directly to `main`.
3. Keep rules declarative: declare every input, output, parameter, resource, and
   conda/container environment. Do not hide workflow work in untracked scripts.
4. Never commit large source data, generated results, credentials, or `.snakemake/`.
   Document data acquisition and use config paths or environment variables instead.
5. Make every rule reproducible: outputs must derive solely from declared inputs,
   params, software environment, and code.
6. Update `README.md`, `config/config.yaml`, and `docs/codemap.md` when a public
   pipeline interface, input, output, or invocation changes.

## Before reporting a change complete

Run the relevant checks, at minimum:

```bash
make lint
make test
```

For a changed execution profile, also run its dry-run command. Describe any test
data, external service, or scheduler requirement that could not be exercised.
