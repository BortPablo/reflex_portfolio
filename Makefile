help:
	@echo "┌──────────────────────────────────────────────┐"
	@echo "│ Makefile for Portfolio web creation (reflex) │"
	@echo "└──────────────────────────────────────────────┘"
	@echo "┌───────────────────────────────┐┌────────────────────────────────────────────────────────────────────────┐"
	@echo "│ Command                       ││ Description                                                            │"
	@echo "├───────────────────────────────┤├────────────────────────────────────────────────────────────────────────┤"
	@echo "│ - make help                   ││ - Show this help message                                               │"
	@echo "│ - make setup                  ││ - Create virtual environment and install dependencies                  │"
	@echo "│ - make clean                  ││ - Remove virtual environment and create requirements.txt               │"
	@echo "└───────────────────────────────┘└────────────────────────────────────────────────────────────────────────┘"

setup:
	@echo "Creating virtual environment..."
	python3 -m virtualenv venv
	@echo "Installing dependencies..."
	venv/bin/pip install reflex
	@echo "Starting VSCode..."
	code .
	@echo "Initializing reflex..."
	reflex init

clean:
	@echo "Removing virtual environment..."
	rm -rf venv

