from pypdf import PdfReader , PdfWriter
import os

print("Welcome To PDF Merged ")
path = input("Paste The Path Where The PDF's ")
output_path = input("Paste The Path Where The merged pdf should show")

writer = PdfWriter()
for files in os.listdir(path):
    pass
if files.endswith(".pdf"):
    pdf_path = os.path.join(path,files)
    reader = PdfReader(pdf_path)
    
    for page in reader.pages:
        writer.add_page(page)
    
with open (output_path, "wb") as f:
    writer.write(f)

print("Pdf's Merged Successfully!!!")