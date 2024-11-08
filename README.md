# PDFFusion: Streamlined Image Conversion & PDF Merging Application

PDFFusion is a sophisticated web application designed to simplify the process of converting images to PDF and merging multiple PDF files. With its intuitive interface, users of all technical backgrounds can efficiently combine PDFs and images into a single document.

## Prerequisites

- **Miniconda**: Required for setting up the project environment. Download from [Miniconda's official site](https://docs.conda.io/en/latest/miniconda.html).

## Installation and Setup

1. **Clone the Repository**
   ```bash
   git clone https://github.com/satyampurwar/PDFFusion.git
   cd PDFFusion
   ```

2. **Configure Environment**
   ```bash
   conda create --name pdfmerge python=3.12.4 -y
   conda activate pdfmerge
   pip install -r deploy/conda/requirements.txt
   conda env export --name pdfmerge > deploy/conda/linux_py312.yml
   ```

3. **Ensure Code Quality**
   ```bash
   chmod +x shell/code_quality.sh
   ./shell/code_quality.sh
   ```

4. **Package and Install**
   ```bash
   python3 -m pip install --upgrade build
   python3 -m build
   pip install --force-reinstall dist/pdffusion-0.0.0-py3-none-any.whl
   ```
   Note: Replace `0.0.0` with the current version number of your package.

   After installation, import and use PDFFusion in your Python projects:
   ```python
   from pdffusion.utility import convert_images_and_delete, merge_pdfs
   ```

5. **Launch Application**
   ```bash
   chmod +x shell/run.sh
   ./shell/run.sh
   ```

6. **Access PDFFusion**: Open your web browser and navigate to `http://127.0.0.1:5000`
   
   **Note**: The `index.html` file was generated using Generative AI and has been manually tested for functionality.

## Usage Instructions

1. Click "Upload" to select PDF files and/or image files (PNG, JPG, JPEG, GIF, BMP)
2. Click "Process Files" to convert images to PDF and merge all PDFs
3. Click "Download" to retrieve the newly merged PDF

## Key Features

- **User-Friendly Web Interface**: Designed for intuitive operation
- **Multi-File Processing**: Merge multiple PDFs and convert various images simultaneously
- **Image to PDF Conversion**: Seamlessly converts uploaded images to PDF format
- **Instant Download**: Provides immediate access to the merged PDF after processing

## Roadmap

1. Testing of drag-and-drop feature for file uploading

## Contributing

We welcome contributions to PDFFusion. Please fork the repository and submit a pull request with your proposed changes.

## License

PDFFusion is distributed under the MIT License. See [LICENSE](LICENSE) for full details.

## Support

For technical issues or feature requests, please open an issue in this repository.

Enhance your document management workflow with PDFFusion today!