# Snakemake Project Template

A small, reproducible starting point for a data-processing workflow built with
[Snakemake](https://snakemake.github.io/). It provides a clear rule/config
layout, an executable example, local execution defaults, CI, and a generator
that Devboard can run non-interactively.

## Quick start

### From Devboard

In Devboard's **Quick start** panel, select **Snakemake workflow**, name the
project, choose a folder, and optionally create a private GitHub repository.
The generated project has its own Git repository and starts on `main`.

<!-- TEMPLATE-ONLY:START -->

### From the generator

```bash
cd ~/Documents/work/03_templates/snakemake-project-template
python3 scripts/create_project.py ~/Documents/work/01_active/rnaseq-qc \
  --slug rnaseq-qc --name "RNA-seq QC" --skip-sync --skip-index
```

Then initialize and verify it:

```bash
cd ~/Documents/work/01_active/rnaseq-qc
make setup
make dry-run
make test
```

Use `--github OWNER/REPOSITORY` to create and push a repository, or leave it to
Devboard's opt-in GitHub checkbox. The generator never overwrites an existing
target and leaves the template itself untouched.

<!-- TEMPLATE-ONLY:END -->

## What you get

```
config/config.yaml          Run-specific paths and parameters
workflow/Snakefile          Workflow entry point and default target
workflow/rules/report.smk   Small example rule to replace with your first stage
profiles/default/           Portable local profile defaults
resources/example.txt       Tiny tracked input for the example workflow
results/                    Generated outputs (ignored by Git)
docs/                       Code map and data-management guidance
```

The starter workflow converts the tracked example input into
`results/report.txt`. This is intentionally simple: it gives `make test` and CI
a real DAG to run while you replace `workflow/rules/report.smk` with your first
scientific or production stage.

## Working with the workflow

Edit `config/config.yaml` to define inputs and outputs, then add rules below
`workflow/rules/` and include them from `workflow/Snakefile`. Start every change
with a dry run:

```bash
make dry-run
make lint
make test
```

For a cluster or cloud executor, add a separate profile under `profiles/` or in
your local configuration. Keep account identifiers, credentials, and
site-specific settings outside Git. See [data management](docs/data-management.md)
and [the code map](docs/codemap.md) for the project conventions.

<!-- TEMPLATE-ONLY:START -->

## Devboard integration

Devboard registers this template as `snakemake-workflow` in its
`quick_start.types` registry. It calls the generator with the selected target,
slug, and name plus `--skip-sync --skip-beads`, so clicking Create remains fast;
run `make setup` afterward. The generator also supports `--skip-index` for a
fully local manual scaffold and `--github OWNER/REPOSITORY` for a private repo.

<!-- TEMPLATE-ONLY:END -->
