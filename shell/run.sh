#!/bin/bash

# Set strict mode
set -euo pipefail

# Define directories
INPUT_DIR="data/input"
OUTPUT_DIR="data/output"

# Check if directories exist
if [ ! -d "$INPUT_DIR" ]; then
    echo "Error: Input directory '$INPUT_DIR' does not exist."
    exit 1
fi

if [ ! -d "$OUTPUT_DIR" ]; then
    echo "Creating output directory '$OUTPUT_DIR'..."
    mkdir -p "$OUTPUT_DIR"
fi

# Main execution
echo "Starting PDFFusion setup..."

# Clear directories before running the application
echo "Clearing input and output directories..."
rm -rf "$INPUT_DIR"/* "$OUTPUT_DIR"/* || true
echo "Directories cleared successfully."

# Add the project root to PYTHONPATH
export PYTHONPATH="$PYTHONPATH:$(pwd)/src"

# Run the application
echo "Running the application..."
if python app.py; then
    echo "PDFFusion application exited successfully."
else
    echo "Error: PDFFusion application encountered an issue."
    exit 1
fi