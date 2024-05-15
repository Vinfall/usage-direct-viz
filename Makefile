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

# Install dependencies for Python
install: $(REQUIREMENTS)
	$(PIP) install -r $(REQUIREMENTS)

# Generate plots
plot: $(PLOT)
	$(PYTHON) $(PLOT)

# Clean up outputs
clean:
	-rm output/*.html
