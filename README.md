QR Code UUID Extractor
This project reads QR codes from PDF files and extracts UUIDs from them. The UUIDs are then saved into an Excel file for further use. This script can be particularly useful if you have many documents with embedded QR codes and need to automate the extraction of unique IDs.

Prerequisites
Make sure you have the following Python libraries installed:

pdf2image
opencv-python (OpenCV)
numpy
pandas
pyzbar
To install all the dependencies, use the following command:
"pip install pdf2image opencv-python numpy pandas pyzbar"
Additionally, the pdf2image library requires poppler to be installed. You can download poppler from "https://github.com/oschwartz10612/poppler-windows" for Windows or use a package manager like brew for macOS:"brew install poppler"


Usage
Place all the PDF files you want to process in a specific folder.
Update the folder_path variable in the script to match the location of your PDF files.
Run the script using Python:
sh
"python qr_uuid_extractor.py"


The script will:
Read the PDF files from the specified folder.
Extract any QR codes found within the files.
Identify UUIDs from these QR codes.
Save the results to an Excel file (qr_uuid_results.xlsx) located on your desktop.

***************************************************************************

Example Output
After running the script, you will find an Excel file named qr_uuid_results.xlsx on your desktop. This file will look like:

File Name	UUID
example1.pdf	123e4567-e89b-12d3-a456-426614174000
example2.pdf	No UUID found
example3.pdf	987e6543-e21b-34f7-c890-426614174111

