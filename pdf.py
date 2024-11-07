#!/usr/bin/env python3

"""
PDFFusion - PDF Merging Script

Author: Satyam Purwar
Description: This script merges multiple PDF files from an input directory into a single PDF file
in an output directory.

Usage:
    python pdf.py <input_directory> <output_directory>
"""

import os
import argparse
from PyPDF2 import PdfMerger

def merge_pdfs(input_dir, output_dir):
    """
    Merge all PDF files in the input directory into a single PDF file in the output directory.

    Args:
        input_dir (str): Path to the directory containing input PDF files.
        output_dir (str): Path to the directory where the merged PDF will be saved.

    Returns:
        None

    Raises:
        FileNotFoundError: If the input directory doesn't exist.
        PermissionError: If there's no write permission for the output directory.
    """
    merger = PdfMerger()
    
    # Check if the input directory exists
    if not os.path.exists(input_dir):
        raise FileNotFoundError(f"Input directory not found: {input_dir}")

    # List all PDF files in the input directory
    pdf_files = [f for f in os.listdir(input_dir) if f.endswith('.pdf')]
    
    if not pdf_files:
        print(f"No PDF files found in {input_dir}")
        return

    # Append each PDF file to the merger
    for filename in pdf_files:
        filepath = os.path.join(input_dir, filename)
        merger.append(filepath)
    
    # Create output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    output_path = os.path.join(output_dir, "output.pdf")
    
    try:
        # Write the merged PDF to the output path
        merger.write(output_path)
    except PermissionError:
        raise PermissionError(f"No write permission for output directory: {output_dir}")
    finally:
        merger.close()  # Ensure that resources are released
    
    print(f"PDFs merged successfully. Output saved to: {output_path}")

def main():
    """
    Main function to parse command-line arguments and call the merge_pdfs function.
    
    Parses input and output directory paths from command line arguments.
    """
    parser = argparse.ArgumentParser(
        description="Merge PDF files from an input directory into a single PDF file.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Example:
    python pdf.py ./data/input ./data/output

This will merge all PDF files in ./data/input and save the result as output.pdf in ./data/output.
        """
    )
    
    # Define command-line arguments
    parser.add_argument("input_dir", help="Directory containing input PDF files")
    parser.add_argument("output_dir", help="Directory for the merged PDF output")
    
    args = parser.parse_args()
    
    try:
        merge_pdfs(args.input_dir, args.output_dir)
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()