# PDF Summary and Keyword Extractor 📚

This Flask application allows users to upload PDF documents (preferably in Marathi) to extract a summary and the most frequent keywords. It also provides English translations for both the summary and keywords. The application leverages Tesseract for OCR to handle PDFs that are image-based.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Installing Tesseract-OCR](#installing-tesseract-ocr)
  - [Windows](#windows)
  - [Linux](#linux)
  - [macOS](#macos)
- [Setup](#setup)
- [Running the Application](#running-the-application)
- [Note](#note)

## Prerequisites

Before you begin, ensure you have met the following requirements:
- 🐍 Python 3.6 or higher installed
- 📖 Tesseract-OCR installed on your system

## Installing Tesseract-OCR

Tesseract is an open-source OCR engine that this application uses to extract text from images. Follow the instructions for your operating system:

### Windows

1. Download the installer from [Tesseract at UB Mannheim](https://github.com/UB-Mannheim/tesseract/wiki).
2. Run the installer and follow the instructions, noting the installation path.
3. Add Tesseract to your system's PATH environment variable:
   - Right-click on 'This PC' or 'My Computer' and select 'Properties'.
   - Navigate to 'Advanced system settings' > 'Environment Variables'.
   - Find the 'Path' variable in the 'System variables' section and click 'Edit'.
   - Add the path to the Tesseract installation folder (e.g., `C:\Program Files\Tesseract-OCR`).
   - Click 'OK' to save your changes.

### Linux

```bash```
sudo apt update
sudo apt install tesseract-ocr
sudo apt install libtesseract-dev


### macOS

```bash```
brew install tesseract

## Setup
1. Clone this repository:
```bash```
git clone https://github.com/niharikakuchhal/pdf-translate.git
cd pdf-translate

2. Create and activate a virtual environment:
```bash```
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3.  Install the required packages:
```bash```
pip install -r requirements.txt

## Running the Application
#### Using Flask's Command
Set the FLASK_APP environment variable and run the application:
```bash```
export FLASK_APP=app.py  # Use `set` instead of `export` on Windows
flask run

Open your web browser and navigate to http://127.0.0.1:5000/ to use the application.

## Note
Tesseract OCR Setup: Make sure `pytesseract.pytesseract.tesseract_cmd` is set to your Tesseract-OCR installation path.

pytesseract.pytesseract.tesseract_cmd = r'/usr/local/bin/tesseract'  # Adjust path as needed



