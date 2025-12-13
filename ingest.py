import pdfplumber
import os
import json

# Directory containing raw PDF datasheets
RAW_DIR = "data/raw"

# Directory to store processed JSON output
PROCESSED_DIR = "data/processed"

# Ensure processed data directory exists
os.makedirs(PROCESSED_DIR, exist_ok=True)


def process_pdf(pdf_path):
    """
    Extracts text content from a PDF datasheet page by page
    and converts it into structured chunks with metadata.
    """
    chunks = []
    with pdfplumber.open(pdf_path) as pdf:
        for page_num, page in enumerate(pdf.pages, start=1):
            text = page.extract_text()
            if text:
                chunks.append({
                    "text": text.strip(),
                    "source": os.path.basename(pdf_path),
                    "page": page_num
                })
    return chunks


# Process all PDF files in the raw data directory
for file in os.listdir(RAW_DIR):
    if file.endswith(".pdf"):
        pdf_path = os.path.join(RAW_DIR, file)
        chunks = process_pdf(pdf_path)

        out_file = file.replace(".pdf", ".json")
        out_path = os.path.join(PROCESSED_DIR, out_file)

        # Save extracted text as JSON
        with open(out_path, "w", encoding="utf-8") as f:
            json.dump(chunks, f, indent=2)

print("PDF processing complete.")
