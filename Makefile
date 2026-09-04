.DEFAULT_GOAL := help
.PHONY: help setup dry-run run test lint clean

SNAKEMAKE := uv run snakemake

help: ## Show available commands
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | \
		awk 'BEGIN {FS = ":.*?## "}; {printf "  \\033[36m%-12s\\033[0m %s\\n", $$1, $$2}'

setup: ## Install the locked workflow environment
	uv sync

dry-run: ## Render the directed acyclic graph without writing outputs
	$(SNAKEMAKE) --cores 1 --dry-run --configfile config/config.yaml

run: ## Execute the example workflow locally
	$(SNAKEMAKE) --cores 1 --configfile config/config.yaml --printshellcmds

test: ## Run the example workflow and check its expected output
	$(SNAKEMAKE) --cores 1 --configfile config/config.yaml --rerun-incomplete
	@test -s results/report.txt

lint: ## Check rule declarations and workflow quality
	$(SNAKEMAKE) --lint --configfile config/config.yaml

clean: ## Delete only generated example results and Snakemake metadata
	rm -rf .snakemake results/report.txt logs
