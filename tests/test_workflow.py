"""Structural checks that do not require a Snakemake installation."""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_workflow_entry_point_includes_rules_and_default_target() -> None:
    snakefile = (ROOT / "workflow" / "Snakefile").read_text()
    assert 'include: "rules/report.smk"' in snakefile
    assert "rule all:" in snakefile


def test_example_configuration_points_to_tracked_input() -> None:
    config = (ROOT / "config" / "config.yaml").read_text()
    assert "resources/example.txt" in config
    assert (ROOT / "resources" / "example.txt").is_file()
