# Commands
PYTHON = python
PIP = pip

# Dependencies & scripts
REQUIREMENTS = requirements.txt
SANITIZER = vndb-sanitizer.py
PLOT = visualize.py

# Default target, run one by one
all:
	$(MAKE) install
	$(MAKE) plot

install: $(VENV) ## install dependencies in venv
	$(PIP) install -r $(REQUIREMENTS)

$(VENV):
	@echo "Setting up virtualenv..."
	virtualenv $(VENV)
	source $(VENV)/bin/activate; \
	$(PIP) install -r $(REQUIREMENTS)

plot: $(PLOT) ## generate plots
	$(PYTHON) $(PLOT)

clean: ## clean up outputs
	-rm output/*.html

uninstall: ## uninstall venv & clean cache
	@echo "Cleaning up..."
	@deactivate || true
	rm -rf $(VENV)
	pip cache purge || true

help: ## show this help
	@echo "Specify a command:"
	@grep -E '^[0-9a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[0;36m%-12s\033[m %s\n", $$1, $$2}'
	@echo ""
.PHONY: help
