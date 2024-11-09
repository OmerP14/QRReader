from pdf2image import convert_from_path
import cv2
import numpy as np
import os
import re
import pandas as pd
from pyzbar.pyzbar import decode

# Regex pattern to find UUIDs
uuid_pattern = re.compile(r'\b[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}\b')

# Folder containing PDF files
folder_path = "C:\\Users\\user\\Desktop\\mgrs"

# List PDF files
pdf_files = []
for filename in os.listdir(folder_path):
    if filename.endswith(".pdf"):
        full_path = os.path.join(folder_path, filename)
        pdf_files.append(full_path)

# Function to read QR codes from a PDF
def read_qr_code_from_pdf(pdf_file):
    uuids_from_qr = set()  # Use a set to store unique UUIDs
    images = convert_from_path(pdf_file, dpi=300)  # Increase DPI here

    for img in images:
        img_array = np.array(img)

        # Convert image to grayscale
        gray = cv2.cvtColor(img_array, cv2.COLOR_RGB2GRAY)

        # Sharpen the image
        kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
        sharpened = cv2.filter2D(gray, -1, kernel)

        # Convert image to binary
        _, binary_img = cv2.threshold(sharpened, 127, 255, cv2.THRESH_BINARY)

        # Decode QR codes
        decoded_objects = decode(binary_img)

        for obj in decoded_objects:
            # Check for UUID
            uuids_from_qr.update(uuid_pattern.findall(obj.data.decode('utf-8')))  # Add to set

    return list(uuids_from_qr)  # Convert set to list

# Read QR codes and collect UUIDs
qr_uuid_data = {
    "File Name": [],
    "UUID": []
}

for i, pdf_file in enumerate(pdf_files):
    base_name = os.path.basename(pdf_file)
    uuids = read_qr_code_from_pdf(pdf_file)

    if uuids:
        for uuid in uuids:
            qr_uuid_data["File Name"].append(base_name)
            qr_uuid_data["UUID"].append(uuid)
    else:
        # Add a row if no UUID is found
        qr_uuid_data["File Name"].append(base_name)
        qr_uuid_data["UUID"].append("No UUID found")

    # Print information after every 100 files are processed
    if (i + 1) % 100 == 0:
        print(f"{i + 1} files processed...")

# Create DataFrame and print it
qr_uuid_table = pd.DataFrame(qr_uuid_data)
print(qr_uuid_table)

# Write DataFrame to Excel file
qr_uuid_table.to_excel("C:\\Users\\user\\Desktop\\qr_uuid_results.xlsx", index=False)
