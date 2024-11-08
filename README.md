# PDFFusion: Streamlined PDF Merging and Image Conversion Application

PDFFusion is a user-friendly web application designed to simplify the process of merging multiple PDF files and converting images to PDF. With its intuitive interface, users of all technical backgrounds can easily combine PDFs and images into a single document.

## Prerequisites

- **Miniconda**: Essential for setting up the project environment. Download from [Miniconda's official site](https://docs.conda.io/en/latest/miniconda.html).

## Quick Start Guide

1. **Clone the Repository**
   ```bash
   git clone https://github.com/satyampurwar/PDFFusion.git
   cd PDFFusion
   ```

2. **Set Up Environment**
   ```bash
   conda create --name pdfmerge python=3.12.4 -y
   conda activate pdfmerge
   pip install -r deploy/conda/requirements.txt
   conda env export --name pdfmerge > deploy/conda/linux_py312.yml
   ```

3. **Maintaining Code Quality**
   ```bash
   chmod +x shell/code_quality.sh
   ./shell/code_quality.sh
   ```

4. **Packaging and Installation**
   ```bash
   # Upgrade build tools
   python3 -m pip install --upgrade build

   # Build the package
   python3 -m build

   # Install the package
   pip install --force-reinstall dist/pdffusion-0.0.0-py3-none-any.whl
   ```
   Note: Replace `0.0.0` with the actual version number of your package.

   After installation, you can import and use PDFFusion in your Python projects:
   ```python
   from pdffusion.utility import convert_images_and_delete, merge_pdfs
   ```

5. **Launch Application**
   ```bash
   chmod +x shell/run.sh
   ./shell/run.sh
   ```

6. **Accessing PDFFusion**
   Launch your web browser and navigate to `http://127.0.0.1:5000`
   
   **Note**: The `index.html` file was generated using Generative AI. It has been manually tested and is functioning correctly.

## How to Use

1. Click "Upload" to select PDF files and/or image files (PNG, JPG, JPEG, GIF, BMP)
2. Press "Process" to convert images to PDF and merge all PDFs
3. Download your newly merged PDF

## Key Features

- **Intuitive Web Interface**: Designed for ease of use
- **Multi-File Support**: Merge several PDFs and convert multiple images simultaneously
- **Image to PDF Conversion**: Automatically converts uploaded images to PDF format
- **Instant Download**: Get your merged PDF immediately after processing

## Future Enhancements

1. Implement working and tested drag-and-drop feature for file uploading

## Contribute

We welcome contributions! Fork the repository and submit a pull request to help improve PDFFusion.

## License

PDFFusion is released under the MIT License. See [LICENSE](LICENSE) for details.

## Support

For issues or feature requests, please open an issue in this repository.

Simplify your PDF merging and image conversion process with PDFFusion today!