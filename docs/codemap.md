# Code map

| Path | Purpose |
| --- | --- |
| `config/config.yaml` | User-facing run inputs and output locations. |
| `workflow/Snakefile` | Workflow entry point and default target. |
| `workflow/rules/report.smk` | Minimal example rule that produces a report from a tracked input. |
| `workflow/envs/base.yaml` | Per-rule Conda environment declaration for the example rule. |
| `profiles/default/` | Portable local execution defaults; add a separate site profile for a cluster. |
| `resources/` | Tiny tracked example input; never add large experimental data. |
| `results/` | Generated outputs, ignored by Git. |
<!-- TEMPLATE-ONLY:START -->
| `scripts/create_project.py` | Devboard-compatible, non-interactive project generator. |
<!-- TEMPLATE-ONLY:END -->

When adding a pipeline stage, put its rule(s) in `workflow/rules/`, include the
file from `workflow/Snakefile`, expose user choices in `config/config.yaml`, and
update this map plus the README's layout section.
