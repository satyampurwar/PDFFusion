#!/usr/bin/env python3

"""
PDFFusion - PDF Merging and Image Conversion Script

Author: Satyam Purwar
Description: This script merges multiple PDF files from an input directory into a single PDF file
in an output directory. It also converts images to PDF and saves the result in the input directory.

Usage:
    python pdf.py <input_directory> <output_directory>
"""

import argparse
import os
import re
from io import BytesIO

from PIL import Image
from PyPDF2 import PdfReader, PdfWriter


def convert_images_and_delete(input_dir):
    """
    Convert all images in the input directory to individual PDFs with the same file name,
    save them in the input directory, and delete the original images.

    Args:
        input_dir (str): Path to the directory containing input image files.

    Returns:
        list: List of paths to the created PDF files, or None if no images were found.
    """
    image_files = [
        f
        for f in os.listdir(input_dir)
        if f.lower().endswith((".png", ".jpg", ".jpeg", ".gif", ".bmp"))
    ]

    if not image_files:
        print(f"No image files found in {input_dir}")
        return None

    pdf_paths = []

    for filename in image_files:
        file_path = os.path.join(input_dir, filename)
        pdf_filename = os.path.splitext(filename)[0] + ".pdf"
        output_pdf_path = os.path.join(input_dir, pdf_filename)

        try:
            with Image.open(file_path) as img:
                # Convert image to RGB mode if it's not already
                if img.mode != "RGB":
                    img = img.convert("RGB")

                # Resize image if it's too large (adjust dimensions as needed)
                max_size = (1000, 1000)  # Maximum width and height
                img.thumbnail(max_size, Image.LANCZOS)

                # Save image to a BytesIO object
                img_byte_arr = BytesIO()
                img.save(img_byte_arr, format="PDF", resolution=100.0, quality=85)
                img_byte_arr.seek(0)

                # Create a new PDF writer for each image
                pdf_writer = PdfWriter()
                pdf_writer.add_page(PdfReader(img_byte_arr).pages[0])

                # Save the optimized PDF
                with open(output_pdf_path, "wb") as f:
                    pdf_writer.write(f)

                pdf_paths.append(output_pdf_path)

        except Exception as e:
            print(f"Error processing {filename}: {str(e)}")
            continue

    if not pdf_paths:
        print("No images were successfully converted to PDF pages.")
        return None

    # Delete the image files after conversion
    for filename in image_files:
        try:
            os.remove(os.path.join(input_dir, filename))
        except Exception as e:
            print(f"Error deleting {filename}: {str(e)}")

    print(
        f"Images converted to optimized PDFs successfully. Output saved to: {pdf_paths}"
    )
    return pdf_paths


def natural_sort_key(s):
    """
    Generate a sorting key for natural sorting.
    This function splits the string into components of digits and non-digits,
    allowing for natural ordering of numbers within strings.

    Args:
        s (str): The string to create a sort key for.

    Returns:
        list: A list of components for sorting.
    """
    return [
        int(text) if text.isdigit() else text.lower() for text in re.split(r"(\d+)", s)
    ]


def merge_pdfs(input_dir, output_dir, sort_by="name"):
    """
    Merge all PDF files in the input directory into a single PDF file in the output directory.

    Args:
        input_dir (str): Path to the directory containing input PDF files.
        output_dir (str): Path to the directory where the merged PDF will be saved.
        sort_by (str): Sorting criteria. Options: 'name', 'date', 'date_name'. Default is 'name'.

    Returns:
        None

    Raises:
        FileNotFoundError: If the input directory doesn't exist.
        PermissionError: If there's no write permission for the output directory.
    """
    if not os.path.exists(input_dir):
        raise FileNotFoundError(f"Input directory not found: {input_dir}")

    pdf_files = [f for f in os.listdir(input_dir) if f.endswith(".pdf")]

    if not pdf_files:
        print(f"No PDF files found in {input_dir}")
        return

    # Sort the PDF files based on the specified criteria
    if sort_by == "name":
        pdf_files.sort(key=natural_sort_key)  # Use natural sort for names
    elif sort_by == "date":
        pdf_files.sort(key=lambda x: os.path.getmtime(os.path.join(input_dir, x)))
    elif sort_by == "date_name":
        pdf_files.sort(key=lambda x: (os.path.getmtime(os.path.join(input_dir, x)), x))
    else:
        print(f"Invalid sort_by option: {sort_by}. Using default 'name' sorting.")
        pdf_files.sort()

    merger = PdfWriter()

    for filename in pdf_files:
        filepath = os.path.join(input_dir, filename)
        try:
            with open(filepath, "rb") as file:
                pdf = PdfReader(file)
                for page in pdf.pages:
                    merger.add_page(page)
        except Exception as e:
            print(f"Error processing {filename}: {str(e)}")

    if len(merger.pages) == 0:
        print("No PDF pages were successfully added to the merged document.")
        return

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    output_path = os.path.join(output_dir, "merged_output.pdf")

    try:
        with open(output_path, "wb") as output_file:
            merger.write(output_file)
    except PermissionError:
        raise PermissionError(f"No write permission for output directory: {output_dir}")

    print(f"PDFs merged successfully. Output saved to: {output_path}")


def main():
    """
    Main function to parse command-line arguments and call the merge_pdfs function.

    Parses input and output directory paths from command line arguments.
    """
    parser = argparse.ArgumentParser(
        description="Merge PDF files and convert images to PDF from an input directory.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Example:
    python pdf.py ./data/input ./data/output

This will merge all PDF files in ./data/input, convert images to PDF (saving in ./data/input),
and save the merged PDF in ./data/output.
        """,
    )

    # Define command-line arguments
    parser.add_argument(
        "input_dir", help="Directory containing input PDF files and images"
    )
    parser.add_argument("output_dir", help="Directory for the output merged PDF")

    args = parser.parse_args()

    try:
        # Convert images to PDF and delete originals, saving the result in the input directory
        image_pdf = convert_images_and_delete(args.input_dir)

        # Merge PDFs
        merge_pdfs(args.input_dir, args.output_dir)

        # If an image PDF was created, mention it in the output
        if image_pdf:
            print(f"Note: Images were converted to PDF and saved as {image_pdf}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    main()
