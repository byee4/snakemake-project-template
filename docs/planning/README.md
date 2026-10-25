# Planning a notebook conversion

Fill these files before asking an agent to turn a notebook into rules. They
record what the notebook does and what must not change, so the conversion can be
reviewed against them. Delete this folder if the project isn't converting a
notebook.

| File | Purpose |
| --- | --- |
| [SPEC.md](SPEC.md) | Question, inputs, outputs, scope and acceptance checks |
| [PARAMS.md](PARAMS.md) | Every constant in the notebook, its meaning and source |
| [dag.yaml](dag.yaml) | Steps and file dependencies |
| [REGRESSION_CONTRACT.md](REGRESSION_CONTRACT.md) | Outputs to compare with the notebook, and justified tolerances |
| [tools.md](tools.md) | Tool versions and parameter sources |
| [DEPLOY.md](DEPLOY.md) | Run environment, cost and recovery plan for a real run |
