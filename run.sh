#!/bin/bash

# PDFFusion - Streamlined PDF Merging Application Runner
# Author: Satyam Purwar
# Description: This script prepares the environment and runs the PDFFusion application.
#              It clears the input and output directories before launching the main application.

# Define directories
INPUT_DIR="data/input"
OUTPUT_DIR="data/output"

# Function to clear directories
clear_directories() {
    echo "Clearing input and output directories..."
    
    # Remove and recreate input directory
    if [ -d "$INPUT_DIR" ]; then
        rm -rf "$INPUT_DIR"
    fi
    mkdir -p "$INPUT_DIR"
    touch "$INPUT_DIR/.gitkeep"
    
    # Remove and recreate output directory
    if [ -d "$OUTPUT_DIR" ]; then
        rm -rf "$OUTPUT_DIR"
    fi
    mkdir -p "$OUTPUT_DIR"
    touch "$OUTPUT_DIR/.gitkeep"
    
    echo "Directories cleared successfully."
}

# Clear directories before running the application
clear_directories

# Run the application
echo "Running the application..."
python app.py