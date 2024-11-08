#!/bin/bash

# Script to format and lint Python files in the package directory

# Define the target directory and files
TARGET_DIR="src/pdffusion"
FILES=("utility.py")

# Check if the target directory exists
if [[ ! -d "$TARGET_DIR" ]]; then
    echo "Error: Directory $TARGET_DIR not found!"
    exit 1
fi

# Function to format and lint a file
format_and_lint() {
    local file="$1"

    echo "Processing $file..."
    
    # Format the code using Black
    black "$file" || { echo "Error formatting $file with Black"; exit 1; }

    # Sort imports using isort
    isort "$file" || { echo "Error sorting imports in $file with isort"; exit 1; }

    # Lint the code using flake8
    flake8 "$file" || { echo "Linting errors found in $file"; }
}

# Iterate over each file and process it
for file in "${FILES[@]}"; do
    format_and_lint "$TARGET_DIR/$file"
done

echo "Code formatting and linting completed successfully for all files."

# Script to format and lint Python application code

# Define the target file
TARGET_FILE="app.py"

# Check if the target file exists
if [[ ! -f "$TARGET_FILE" ]]; then
    echo "Error: $TARGET_FILE not found!"
    exit 1
fi

# Format the code using Black
echo "Formatting code with Black..."
black "$TARGET_FILE"

# Sort imports using isort
echo "Sorting imports with isort..."
isort "$TARGET_FILE"

# Lint the code using flake8
echo "Linting code with flake8..."
flake8 "$TARGET_FILE"

echo "Code formatting and linting completed successfully."