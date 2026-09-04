# Data management

Keep source data outside this repository unless it is a tiny, redistributable
fixture such as `resources/example.txt`. Point to external inputs in
`config/config.yaml` (or a per-run config file) and record their provenance,
checksums, and access requirements in the run notes.

Generated outputs belong under `results/` and remain ignored. For a production
workflow, use a project- or site-specific Snakemake profile to declare executor,
storage, and resource settings; do not commit scheduler credentials or secrets.
