from PyPDF2 import PdfReader, PdfWriter
from PIL import Image
import os

def mergepdf(pdf_list, output_path):
    writer = PdfWriter()
    for pdf in pdf_list:
        reader = PdfReader()
        for page in range(len(reader.pages)):
            writer.add_page(reader.pages[page])
    with open(output_path, 'wb') as output_pdf:
        writer.write(output_pdf)
    print(f"Merged PDF saved to {output_path}")

