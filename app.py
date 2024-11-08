"""
PDFFusion - Streamlined PDF Merging and Image Conversion Application

Author: Satyam Purwar

Description:
    PDFFusion is a Flask-based web application designed to facilitate the 
    merging of multiple PDF files and conversion of images to PDF. Users can 
    upload PDF files and image files through a simple web interface. The 
    application processes these files and provides an option to download 
    the merged output file.

Features:
    - Upload multiple PDF and image files simultaneously or one by one.
    - Process uploaded files for merging and conversion.
    - Download the resulting merged PDF file.
    - Clear temporary input and output directories from environment after processing.

Usage:
    To run the application, execute this script and navigate to 
    http://127.0.0.1:5000 in your web browser. Ensure that the required 
    dependencies are installed and the necessary environment is set up.
"""

import os
import shutil
import subprocess

from flask import (
    Flask,
    after_this_request,
    jsonify,
    render_template,
    request,
    send_file,
)
from werkzeug.utils import secure_filename

from pdffusion.utility import convert_images_and_delete, merge_pdfs

app = Flask(__name__)

# Configuration
app.config["UPLOAD_FOLDER"] = "data/input"
app.config["OUTPUT_FOLDER"] = "data/output"
app.config["ALLOWED_EXTENSIONS"] = {"pdf", "png", "jpg", "jpeg", "gif", "bmp"}

# Ensure the input and output directories exist
os.makedirs(app.config["UPLOAD_FOLDER"], exist_ok=True)
os.makedirs(app.config["OUTPUT_FOLDER"], exist_ok=True)


def allowed_file(filename):
    """
    Check if the file has an allowed extension.

    Args:
        filename (str): Name of the file to check.

    Returns:
        bool: True if the file has an allowed extension, False otherwise.
    """
    return (
        "." in filename
        and filename.rsplit(".", 1)[1].lower() in app.config["ALLOWED_EXTENSIONS"]
    )


def clear_directories():
    """
    Clear the input and output directories by removing their contents,
    recreating them, and adding .gitkeep files.
    """
    # Clear and recreate the upload folder
    shutil.rmtree(app.config["UPLOAD_FOLDER"], ignore_errors=True)
    os.makedirs(app.config["UPLOAD_FOLDER"], exist_ok=True)

    # Clear and recreate the output folder
    shutil.rmtree(app.config["OUTPUT_FOLDER"], ignore_errors=True)
    os.makedirs(app.config["OUTPUT_FOLDER"], exist_ok=True)

    # Add .gitkeep files to both directories
    open(os.path.join(app.config["UPLOAD_FOLDER"], ".gitkeep"), "a").close()
    open(os.path.join(app.config["OUTPUT_FOLDER"], ".gitkeep"), "a").close()


@app.route("/", methods=["GET", "POST"])
def index():
    """
    Handle the main page of the application. Allows users to upload files
    and process them.

    Returns:
        - Rendered HTML page on GET request.
        - JSON response with error message or success message on POST request.
    """
    if request.method == "POST":
        if "files[]" not in request.files:
            return jsonify({"error": "No file part in the request"}), 400

        files = request.files.getlist("files[]")

        if not files or all(file.filename == "" for file in files):
            return jsonify({"error": "No selected file"}), 400

        for file in files:
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))

        return jsonify({"message": "Files uploaded successfully"}), 200

    return render_template("index.html")


@app.route("/process", methods=["POST"])
def process_files():
    """
    Process uploaded PDF files and images using functions from utility.py.

    Returns:
        - JSON response with success message or an error message.
    """
    try:
        # Convert images to PDF and delete originals
        convert_images_and_delete(app.config["UPLOAD_FOLDER"])

        # Merge PDFs
        merge_pdfs(
            input_dir=app.config["UPLOAD_FOLDER"],
            output_dir=app.config["OUTPUT_FOLDER"],
            sort_by="name",
        )

        # Check for generated output files
        output_files = os.listdir(app.config["OUTPUT_FOLDER"])

        if output_files:
            latest_file = max(
                output_files,
                key=lambda f: os.path.getmtime(
                    os.path.join(app.config["OUTPUT_FOLDER"], f)
                ),
            )
            return (
                jsonify(
                    {"message": "Files processed successfully", "filename": latest_file}
                ),
                200,
            )

        return jsonify({"error": "No output file generated"}), 500
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/download/<filename>", methods=["GET"])
def download_file(filename):
    """
    Download the processed file.

    Args:
        filename (str): Name of the file to download.

    Returns:
        - File attachment for download.
    """
    file_path = os.path.join(app.config["OUTPUT_FOLDER"], filename)

    @after_this_request
    def clear_after_request(response):
        clear_directories()
        return response

    return send_file(file_path, as_attachment=True, download_name="merged.pdf")


if __name__ == "__main__":
    app.run(debug=True)
