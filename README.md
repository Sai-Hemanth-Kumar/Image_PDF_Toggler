# PDF Image Converter

Convert between images and PDFs via a simple interactive CLI.

## Features
- Convert single image into a single PDF
- Convert multiple images into a single PDF
- Convert each page of a PDF into separate image files (JPEG)
- Validates paths, file types, and overwrites safely
- Time-stamped output filenames to avoid collisions

## Requirements
- Python 3.8+
- pip
- Python packages: `img2pdf`, `pdf2image`
- Poppler (runtime dependency required by `pdf2image`)

## Install
1. Install Python dependencies
   ```bash
   pip install img2pdf pdf2image
   ```
2. Install Poppler (required for PDF → Images)
   - Windows: Download a Poppler build and add its `bin` folder to your PATH. For example, download from the "Poppler for Windows" releases and extract, then add the `.../poppler-<version>/Library/bin` (or `bin`) directory to PATH.
   - macOS: `brew install poppler`
   - Ubuntu/Debian: `sudo apt-get update && sudo apt-get install -y poppler-utils`

   After installation, ensure the `poppler` executables(bin) are available on your PATH.

## Usage
Run the program from the project directory:
```bash
python PDF_Image_Converter.py
```
Then choose an option in the interactive menu:
- `1`: Convert Images to PDF
  - Enter one or more image file paths when prompted (supported: `.jpg`, `.jpeg`, `.png`, `.bmp`, `.tiff`, `.gif`).
  - Provide a full output path ending with `.pdf` (e.g., `H:\\Documents\\output.pdf`).
- `2`: Convert PDF to Images
  - Provide the input PDF path.
  - Provide an existing output folder where images will be saved.
- `3`: Exit

### Output details
- Images → PDF: Produces a single PDF at the path you specify.
- PDF → Images: Saves each page as a `.jpg` in the chosen folder, named like:
  `your_pdf_name_page_<page_number>_<YYYYMMDDHHMMSS>.jpg`

## Examples
- Images → PDF (Windows-style path example):
  - Input images: `H:\\Pictures\\img1.jpg`, `H:\\Pictures\\img2.png`
  - Output PDF: `H:\\Documents\\merged.pdf`
- PDF → Images:
  - Input PDF: `Sample Files/PDF/sample.pdf`
  - Output folder: `H:\\Documents\\Images`

## Troubleshooting
- "Poppler not installed or not in PATH": Install Poppler and ensure `pdftoppm` is accessible in your PATH. Reopen your terminal after updating PATH.
- Permission denied / path errors: Verify the paths exist and you have write permissions. On Windows, prefer full absolute paths.
- Non-PDF input for PDF → Images: Ensure the input ends with `.pdf`.

## Notes
- `pdf2image` uses a default DPI of 200 in this app; increase quality by adjusting the `dpi` parameter in `PDF_Image_Converter.py` if needed.
- The program is purely interactive and does not take command-line arguments.
- Sample files are provided in the `Sample Files/` folder for quick testing: `Image/pic.jpg` and `PDF/sample.pdf`.

## Acknowledgements
- [`img2pdf`](https://pypi.org/project/img2pdf/)
- [`pdf2image`](https://pypi.org/project/pdf2image/)
- Poppler (PDF rendering backend)

## Validation rules
- **Valid paths**
  - Inputs must exist. File paths are required where files are expected; folders are rejected in those prompts.
  - Output folder for PDF → Images must exist and be a folder.
- **Only images for Images → PDF**
  - Allowed extensions: `.jpg`, `.jpeg`, `.png`, `.bmp`, `.tiff`, `.gif`.
- **Only PDF for PDF → Images**
  - Input must end with `.pdf`.
- **Output naming and overwrite**
  - Images → PDF: Output path must end with `.pdf`. If the file exists, you will be asked to confirm overwrite.
  - PDF → Images: Each page is saved as `.jpg` with page number and timestamp.
- **General**
  - Prefer absolute paths on Windows and make sure backslashes are properly escaped when writing paths inside scripts.
