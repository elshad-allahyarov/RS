import sys
from pathlib import Path

try:
    from pypdf import PdfReader
except Exception as import_error:
    print(f"Failed to import pypdf: {import_error}", file=sys.stderr)
    sys.exit(1)

PDF_PATH = Path('/workspace/Parameter_Free_Particle_Masses.pdf')
OUT_PATH = Path('/workspace/Parameter_Free_Particle_Masses.txt')

if not PDF_PATH.exists():
    print(f"PDF not found: {PDF_PATH}", file=sys.stderr)
    sys.exit(2)

reader = PdfReader(str(PDF_PATH))
num_pages = len(reader.pages)

with OUT_PATH.open('w', encoding='utf-8') as f_out:
    f_out.write(f"[PAGES] {num_pages}\n\n")
    for i, page in enumerate(reader.pages, start=1):
        try:
            text = page.extract_text() or ''
        except Exception as e:
            text = f"[extract_error: {e}]"
        f_out.write(f"\n--- PAGE {i} ---\n")
        f_out.write(text)
        f_out.write("\n")

print(f"Extracted {num_pages} pages to {OUT_PATH}")