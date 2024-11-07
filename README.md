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