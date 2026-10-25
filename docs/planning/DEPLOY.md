# DEPLOY — <Project Name>

<!--
  PURPOSE
    The deploy plan. The PI (or delegated approver) reads this before
    signing the Deploy gate. It is the document that says, in plain
    language, what is about to happen on the cluster and what to do
    if it goes wrong.

  WHEN
    Phase 5 — Deploy. Drafted by the AI; reviewed by the project
    owner; approved by the PI.

  RULES
    - The HUMAN runs the deploy commands, not the AI.
    - The deploy command runs only after the PI has posted
      `approve: deploy` on the pull request.
    - The dry-run output and the cost estimate must match what is
      written below; if they have drifted, the deploy plan is stale.
-->

## Release identity

- **Release tag:** <!-- v1.0.0-<short-description> -->
- **Intent ID:** <!-- the ResearchIntent id this run satisfies -->
- **Author / preparer:** <!-- name + date -->
- **Approver (PI or delegate):** <!-- name + date -->

## Target environment

- **Cluster / platform:** <!-- TSCC / Kubernetes / local workstation -->
- **Profile path:** <!-- profiles/tscc/config.yaml -->
- **Account or budget code:** <!-- e.g. SLURM account -->
- **Storage destination:** <!-- absolute path on shared storage -->

## Configuration in use

- **`config.yaml` snapshot:** <!-- relative path; the actual file is checked in for this release -->
- **Sample sheet:** <!-- path + SHA-256 -->
- **Reference build:** <!-- e.g. GRCh38, GENCODE v44 -->
- **Highest data class involved:** <!-- Class 0 (Public; UC P1) | Class 1 (Internal; UC P2) | Class 2 (Controlled; UC P3) | Class 3 (Restricted; UC P4) -->

## Expected costs

| Resource | Estimate | Source |
| --- | --- | --- |
| Wall-clock time | <!-- e.g. 6 hours --> | <!-- dry run + last similar run --> |
| CPU-hours | <!-- e.g. 120 --> | <!-- dry run --> |
| Memory peak | <!-- e.g. 64 GB --> | <!-- per-rule resources.mem_mb --> |
| Storage written | <!-- e.g. 400 GB --> | <!-- output contract estimate --> |
| Dollar / credit cost | <!-- if applicable --> | <!-- billing rate --> |

## Dry-run summary

Paste the output of:

```bash
snakemake -n --configfile config/config.yaml --profile profiles/<target>/
```

Below:

```
TODO — paste dry-run job graph here
```

## Difference from the last similar run

<!-- One paragraph. If this is the first run, say so. Otherwise list the
     changes since the previous tag: tool version bumps, parameter
     changes, sample-sheet additions, environment changes. -->

TODO

## Rollback path

If the run goes sideways, here is how to undo it:

1. <!-- e.g. "stop submitted jobs: scancel --user=<user>" -->
2. <!-- e.g. "remove half-written outputs: rm -rf <output_dir>" -->
3. <!-- e.g. "check out previous release tag: git checkout vX.Y.Z-1" -->
4. <!-- e.g. "redeploy previous release if production-critical" -->

## Communication plan

- **Who to notify before deploying:** <!-- e.g. collaborators expecting outputs by Friday -->
- **Where success / failure will be reported:** <!-- e.g. Slack #project-x -->
- **Who is on call during the run:** <!-- name -->

## Sign-off

- AI-prepared on: <!-- date -->
- Project owner reviewed: <!-- name + date -->
- PI approved: <!-- name + date; PR comment `approve: deploy` -->
- Human executor of the deploy command: <!-- name + date -->
- Release tagged with: `git tag -s vX.Y.Z` <!-- by whom -->

## Post-run reconciliation

After the run finishes, list the receipts that prove the run was sound. These feed `audit.<sha256>.json`.

- **Output tree walked against SPEC.md Output Contract:** <!-- pass | fail + details -->
- **Regression test re-run on deployed envs / containers:** <!-- pass | fail + details -->
- **Audit file written to:** <!-- e.g. audits/audit.<sha256>.json -->
- **Reliance approver:** <!-- name + date; PR comment `approve: reliance` -->
