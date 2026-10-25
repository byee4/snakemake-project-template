# Snakemake Project Template

A small, reproducible starting point for a data-processing workflow built with
[Snakemake](https://snakemake.github.io/). It provides a clear rule/config
layout, an executable example, local execution defaults, CI, and a generator
that Devboard can run non-interactively.

## Quick start

You need [uv](https://docs.astral.sh/uv/) and conda 24.7.1 or newer (for example
[Miniforge](https://github.com/conda-forge/miniforge)); Snakemake 9 uses it to build
each rule's environment.

<!-- TEMPLATE-ONLY:START -->

### From GitHub

Click **Use this template** on GitHub, or run:

```bash
gh repo create my-workflow --template byee4/snakemake-project-template --private --clone
cd my-workflow
```

Then replace the project name in `README.md`, `AGENTS.md` and `config/config.yaml`.

### From the generator

The generator copies the template, replaces its name and initializes Git:

```bash
git clone https://github.com/byee4/snakemake-project-template.git
python3 snakemake-project-template/scripts/create_project.py rnaseq-qc \
  --slug rnaseq-qc --name "RNA-seq QC" --skip-sync --skip-index
cd rnaseq-qc
```

Use `--github OWNER/REPOSITORY` to create and push a repository, or leave it to
Devboard's opt-in GitHub checkbox. The generator never overwrites an existing
target and leaves the template itself untouched.

<!-- TEMPLATE-ONLY:END -->

### Set up and check

```bash
make setup
make dry-run
make test
```

## What you get

```
config/config.yaml          Run-specific paths and parameters
config/test.yaml            Test configuration pointing at tests/fixtures/
workflow/Snakefile          Workflow entry point and default target
workflow/rules/report.smk   Small example rule to replace with your first stage
profiles/default/           Local profile defaults; builds each rule's conda env
resources/example.txt       Tiny tracked input for the example workflow
results/                    Generated outputs (ignored by Git)
tests/                      Workflow checks and the regression test
tests/fixtures/             Test input and its frozen expected output
docs/                       Code map and data-management guidance
docs/planning/              Templates for planning a notebook conversion
AGENTS.md                   Instructions for coding agents (CLAUDE.md imports it)
```

The starter workflow converts a tracked input into a report. `make test` runs it
on `tests/fixtures/input.txt` and compares the result byte for byte with
`tests/fixtures/expected/report.txt`. Replace `workflow/rules/report.smk` with
your first scientific or production stage, then replace the fixture and its
expected output to match.

Converting a notebook? Fill the files in [docs/planning](docs/planning/README.md)
first.

## Working with the workflow

Edit `config/config.yaml` to define inputs and outputs, then add rules below
`workflow/rules/` and include them from `workflow/Snakefile`. Check every change:

| Command | What it does |
| --- | --- |
| `make lint` | Runs ruff, snakefmt, `snakemake --lint` and rule checks through pre-commit |
| `make dry-run` | Shows the job graph for `config/test.yaml` without running it |
| `make test` | Runs pytest, including the workflow on the test fixture |
| `make run` | Runs the workflow on `config/config.yaml` |

CI runs `make lint`, `make dry-run` and `make test` on every pull request.

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
