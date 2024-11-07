#!/bin/bash

# PDFFusion - PDF Merging Script Runner
# Author: Satyam Purwar
# Description: This script processes PDF files from the input directory,
# merges them using a Python script, and saves the output in the specified directory.

# Define directories
INPUT_DIR=data/input
OUTPUT_DIR=data/output

# Run the Python script to merge PDFs
python pdf.py "$INPUT_DIR" "$OUTPUT_DIR"

# Notify completion of the PDF merging process
echo "PDF merging process completed."