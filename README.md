# OCR to Excel Conversion using EasyOCR

This script extracts text from an image file and converts it into an Excel spreadsheet. It uses **EasyOCR** for optical character recognition (OCR) to detect and extract text from an image and then saves the extracted text in an Excel file using **Pandas**.

## Requirements

Before running the script, make sure you have the following Python libraries installed:

- `easyocr`: for performing OCR on the image.
- `pandas`: for creating and saving the extracted text in an Excel file.
- `openpyxl`: required for saving Excel files.

To install the required dependencies, you can run the following command:

```bash
pip install easyocr pandas openpyxl

## Output

The script will generate an output.xlsx file that contains all the extracted text from the image. Each line of text will be stored in a separate row in the Excel file.
