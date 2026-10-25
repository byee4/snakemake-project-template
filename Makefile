.DEFAULT_GOAL := help
.PHONY: help setup dry-run run test lint clean

# Snakemake also loads profiles/default, which builds each rule's conda env.
SNAKEMAKE := uv run snakemake

help: ## Show available commands
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | \
		awk 'BEGIN {FS = ":.*?## "}; {printf "  \\033[36m%-12s\\033[0m %s\\n", $$1, $$2}'

setup: ## Install the locked environment and the Git commit hooks
	uv sync
	@if git config core.hooksPath >/dev/null; then \
		echo "core.hooksPath is set, so pre-commit can't install its hook; run make lint before committing."; \
	else uv run pre-commit install; fi

dry-run: ## Show the test-fixture job graph without writing outputs
	$(SNAKEMAKE) --dry-run --configfile config/test.yaml

run: ## Run the workflow on config/config.yaml (real inputs: ask first)
	$(SNAKEMAKE) --configfile config/config.yaml

test: ## Run the tests, including the workflow on the test fixture
	uv run pytest -q

lint: ## Run ruff, snakefmt, snakemake --lint and the rule checks
	uv run pre-commit run --all-files

clean: ## Delete only generated results and Snakemake metadata
	rm -rf .snakemake results/report.txt results/test logs
