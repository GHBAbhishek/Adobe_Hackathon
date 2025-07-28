import os
import json
from PyPDF2 import PdfReader

def detect_heading_level(text, font_size):
    if font_size >= 18:
        return "H1"
    elif font_size >= 14:
        return "H2"
    elif font_size >= 12:
        return "H3"
    return None

def extract_outline(pdf_path):
    reader = PdfReader(pdf_path)
    outline = []
    title = os.path.basename(pdf_path).replace(".pdf", "")

    for page_num, page in enumerate(reader.pages):
        try:
            text = page.extract_text()
            if not text:
                continue
            lines = text.split('\n')
            for line in lines:
                stripped = line.strip()
                if not stripped:
                    continue
                font_size = 14 if stripped.isupper() else 12
                level = detect_heading_level(stripped, font_size)
                if level:
                    outline.append({
                        "level": level,
                        "text": stripped,
                        "page": page_num + 1
                    })
        except:
            continue

    return {
        "title": title,
        "outline": outline
    }

def main():
    input_dir = "C:\\Users\\Abhishek\\Desktop\\Adobe Hackathon\\Challenge_1a\\sample_dataset\\pdfs"
    output_dir = "C:\\Users\\Abhishek\Desktop\\Adobe Hackathon\\Challenge_1a\\sample_dataset\\outputs"
    os.makedirs(output_dir, exist_ok=True)

    for filename in os.listdir(input_dir):
        if filename.endswith(".pdf"):
            pdf_path = os.path.join(input_dir, filename)
            output_json = extract_outline(pdf_path)
            json_filename = filename.replace(".pdf", ".json")
            json_path = os.path.join(output_dir, json_filename)
            with open(json_path, "w") as f:
                json.dump(output_json, f, indent=2)

if __name__ == "__main__":
    main()
