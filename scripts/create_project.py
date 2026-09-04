#!/usr/bin/env python3
"""Create a git-initialized Snakemake workflow project from this template.

This non-interactive generator is the contract used by Devboard Quick Start. It
copies the template into a target that does not yet exist, replaces the template
identity, initializes Git, and can optionally install the environment, refresh
the codebase-memory graph, and create a private GitHub repository.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path

EXCLUDED_NAMES = {
    ".git",
    ".venv",
    ".snakemake",
    "__pycache__",
    ".pytest_cache",
    ".ruff_cache",
    ".DS_Store",
    "logs",
}
EXCLUDED_SUFFIXES = {".pyc"}
EXCLUDED_SCRIPTS = {"create_project.py"}
TEMPLATE_SLUG = "snakemake-project-template"
TEMPLATE_NAME = "Snakemake Project Template"
TEMPLATE_OWNER = "brian-yee"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("target", type=Path, help="new project directory; must not exist")
    parser.add_argument("--slug", required=True, help="lowercase slug, e.g. rnaseq-qc")
    parser.add_argument("--name", required=True, help="display name, e.g. RNA-seq QC")
    parser.add_argument("--github", help="GitHub OWNER/REPOSITORY to create and push to")
    parser.add_argument(
        "--visibility", choices=("private", "public"), default="private",
        help="visibility for a repository created with --github (default: private)",
    )
    parser.add_argument("--skip-sync", action="store_true", help="do not run `uv sync`")
    parser.add_argument(
        "--skip-index", action="store_true",
        help="do not refresh the codebase-memory graph after creation",
    )
    parser.add_argument(
        "--skip-beads", action="store_true",
        help="accepted for generator-contract compatibility; this template has no Beads step",
    )
    return parser.parse_args()


def validate_slug(slug: str) -> None:
    if not re.fullmatch(r"[a-z][a-z0-9-]*", slug):
        raise ValueError(
            "--slug must start with a lowercase letter and contain only lowercase "
            "letters, digits, and hyphens"
        )


def validate_github_repository(repository: str | None) -> None:
    if repository and not re.fullmatch(r"[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+", repository):
        raise ValueError("--github must use OWNER/REPOSITORY form")


def copy_template(source: Path, target: Path) -> None:
    def ignore(directory: str, names: list[str]) -> set[str]:
        skipped = {
            name
            for name in names
            if name in EXCLUDED_NAMES or Path(name).suffix in EXCLUDED_SUFFIXES
        }
        if Path(directory).name == "scripts":
            skipped |= {name for name in names if name in EXCLUDED_SCRIPTS}
        if Path(directory).name == "results":
            # Keep the directory placeholder but never carry generated outputs.
            skipped |= {name for name in names if name != ".gitkeep"}
        return skipped

    shutil.copytree(source, target, ignore=ignore)


def replace_template_identifiers(target: Path, slug: str, name: str, owner: str) -> None:
    for path in target.rglob("*"):
        if not path.is_file() or path.suffix in EXCLUDED_SUFFIXES:
            continue
        try:
            content = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        # The template README has source-only setup instructions. Generated
        # projects do not carry this generator, so remove those sections before
        # replacing the template identity.
        content = re.sub(
            r"<!-- TEMPLATE-ONLY:START -->.*?<!-- TEMPLATE-ONLY:END -->\n?",
            "",
            content,
            flags=re.DOTALL,
        )
        content = content.replace(f"{TEMPLATE_OWNER}/{TEMPLATE_SLUG}", f"{owner}/{slug}")
        content = content.replace(TEMPLATE_NAME, name)
        content = content.replace(TEMPLATE_SLUG, slug)
        path.write_text(content, encoding="utf-8")


def run(command: list[str], cwd: Path) -> None:
    subprocess.run(command, cwd=cwd, check=True)


def git_environment() -> dict[str, str]:
    return os.environ | {
        "GIT_AUTHOR_NAME": "Template Bootstrap",
        "GIT_AUTHOR_EMAIL": "template-bootstrap@localhost",
        "GIT_COMMITTER_NAME": "Template Bootstrap",
        "GIT_COMMITTER_EMAIL": "template-bootstrap@localhost",
    }


def initialize_git(target: Path) -> None:
    run(["git", "init", "-b", "main"], target)
    run(["git", "add", "-A"], target)
    subprocess.run(
        ["git", "commit", "-m", "Initial template bootstrap"],
        cwd=target,
        check=True,
        env=git_environment(),
    )


def setup_environment(target: Path) -> None:
    if shutil.which("uv") is None:
        raise RuntimeError("uv is required to set up the environment; install uv or pass --skip-sync.")
    run(["uv", "sync"], target)


def refresh_codebase_graph(target: Path) -> None:
    payload = json.dumps({"repo_path": str(target), "persistence": True})
    if shutil.which("codebase-memory-mcp") is None:
        print(
            "codebase-memory-mcp not found; skipping graph refresh. On an MCP-enabled "
            f"host, run:\\n  echo '{payload}' | codebase-memory-mcp cli index_repository"
        )
        return
    subprocess.run(
        ["codebase-memory-mcp", "cli", "index_repository"],
        cwd=target,
        check=True,
        input=payload,
        text=True,
    )


def create_github_repository(target: Path, repository: str, visibility: str) -> None:
    if shutil.which("gh") is None:
        raise RuntimeError("GitHub CLI is required for --github; install and authenticate `gh`.")
    run(
        ["gh", "repo", "create", repository, f"--{visibility}", "--source", str(target),
         "--remote", "origin", "--push"],
        target,
    )


def main() -> int:
    args = parse_args()
    source = Path(__file__).resolve().parents[1]
    target = args.target.resolve()
    validate_slug(args.slug)
    validate_github_repository(args.github)
    if target.exists():
        raise ValueError(f"target already exists: {target}")

    owner = args.github.split("/", 1)[0] if args.github else TEMPLATE_OWNER
    copy_template(source, target)
    replace_template_identifiers(target, args.slug, args.name, owner)
    initialize_git(target)
    if not args.skip_sync:
        setup_environment(target)
    if not args.skip_index:
        refresh_codebase_graph(target)
    if args.github:
        create_github_repository(target, args.github, args.visibility)

    print(f"Created {args.name} at {target}")
    print(f"Next: cd {target} && make setup && make dry-run && make test")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (RuntimeError, ValueError, subprocess.CalledProcessError) as error:
        print(f"error: {error}", file=sys.stderr)
        raise SystemExit(2) from error
