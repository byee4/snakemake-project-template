"""Run the workflow on the test fixture and compare it with the frozen output."""

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_workflow_output_matches_expected_fixture() -> None:
    subprocess.run(
        [sys.executable, "-m", "snakemake", "--configfile", "config/test.yaml", "--forceall"],
        cwd=ROOT,
        check=True,
    )
    output = (ROOT / "results" / "test" / "report.txt").read_bytes()
    expected = (ROOT / "tests" / "fixtures" / "expected" / "report.txt").read_bytes()
    assert output == expected
