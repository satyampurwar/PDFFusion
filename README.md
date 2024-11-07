# PDFFusion: Streamlined PDF Merging Application

PDFFusion is a user-friendly web application designed to simplify the process of merging multiple PDF files. With its intuitive interface, users of all technical backgrounds can easily combine PDFs into a single document.

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

3. **Launch Application**
   ```bash
   chmod +x run.sh
   ./run.sh
   ```

4. **Accessing PDFFusion**
   Launch your web browser and navigate to `http://127.0.0.1:5000`
   
   **Note**: The `index.html` file was generated using Generative AI. It has been manually tested and is functioning correctly.

   **Future Enhancements**:
   1. Implement working and tested drag-and-drop feature for file uploading
   2. Enable file merging in the user-specified order

## How to Use

1. Click "Upload" to select PDF files
2. Press "Merge" to combine selected files
3. Download your newly merged PDF

## Key Features

- **Intuitive Web Interface**: Designed for ease of use
- **Multi-File Support**: Merge several PDFs simultaneously
- **Instant Download**: Get your merged PDF immediately after processing

## Contribute

We welcome contributions! Fork the repository and submit a pull request to help improve PDFFusion.

## License

PDFFusion is released under the MIT License. See [LICENSE](LICENSE) for details.

## Support

For issues or feature requests, please open an issue in this repository.

Simplify your PDF merging process with PDFFusion today!