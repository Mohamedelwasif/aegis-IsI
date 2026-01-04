import os
import markdown
from xhtml2pdf import pisa

# Configuration
SOURCE_DIR = "AEGIS_Documentation"
OUTPUT_DIR = "AEGIS_Official_Docs"

# CSS Styles for Glassmorphism/Professional Look
CSS = """
@page {
    size: A4;
    margin: 2cm;
}
body {
    font-family: Helvetica, Arial, sans-serif;
    font-size: 12pt;
    line-height: 1.5;
    color: #333;
}
h1 {
    color: #2563EB;
    border-bottom: 2px solid #2563EB;
    padding-bottom: 10px;
    margin-top: 0;
}
h2 {
    color: #1E40AF;
    margin-top: 20px;
    border-bottom: 1px solid #E5E7EB;
}
h3 {
    color: #374151;
    margin-top: 15px;
}
pre {
    background-color: #F3F4F6;
    border: 1px solid #D1D5DB;
    padding: 10px;
    font-family: monospace;
    font-size: 10pt;
    white-space: pre-wrap;
}
code {
    background-color: #F3F4F6;
    padding: 2px 4px;
    border-radius: 4px;
    font-family: monospace;
}
ul, ol {
    margin-bottom: 10px;
}
li {
    margin-bottom: 5px;
}
.diagram-placeholder {
    background-color: #EFF6FF;
    border: 1px dashed #2563EB;
    color: #1E40AF;
    padding: 20px;
    text-align: center;
    margin: 20px 0;
    border-radius: 8px;
}
"""

# Mapping from Source MD to Target PDF Name
MAPPING = {
    "01_Product_Overview.md": "AEGIS_Product_Overview.pdf",
    "02_System_Architecture.md": "AEGIS_System_Architecture.pdf",
    "03_Security_Model.md": "AEGIS_Security_Model.pdf",  # Added for completeness, though not in exact user list
    "05_AI_Engine.md": "AEGIS_AI_UEBA_Engine.pdf",
    "06_SOAR_Playbooks.md": "AEGIS_SOAR_Playbooks.pdf",
    "07_Deployment_Guide.md": "AEGIS_Deployment_Guide.pdf",
    "08_Compliance_Forensics.md": "AEGIS_Compliance_Forensics.pdf",
    "04_API_Reference.md": "AEGIS_API_Reference.pdf",
    "09_Admin_Operations.md": "AEGIS_Operations_Admin.pdf"
}

def convert_md_to_pdf(md_file, pdf_file):
    md_path = os.path.join(SOURCE_DIR, md_file)
    pdf_path = os.path.join(OUTPUT_DIR, pdf_file)

    if not os.path.exists(md_path):
        print(f"Skipping {md_file}: File not found.")
        return

    print(f"Converting {md_file} to {pdf_file}...")

    with open(md_path, "r", encoding="utf-8") as f:
        text = f.read()

    # Pre-process Mermaid blocks to placeholders
    # Simple replacement for ```mermaid ... ``` blocks
    while "```mermaid" in text:
        start = text.find("```mermaid")
        end = text.find("```", start + 3)
        if end == -1:
            break
        
        # Extract content to maybe describe it, or just replace
        text = text[:start] + '<div class="diagram-placeholder"><strong>[Mermaid Diagram]</strong><br/>Please view the online documentation to interact with this diagram.</div>' + text[end+3:]

    # Convert Markdown to HTML
    html_content = markdown.markdown(text, extensions=['extra', 'codehilite'])

    # Wrap in HTML structure with CSS
    full_html = f"""
    <html>
    <head>
        <style>{CSS}</style>
    </head>
    <body>
        {html_content}
    </body>
    </html>
    """

    # Generate PDF
    with open(pdf_path, "wb") as pdf_out:
        pisa_status = pisa.CreatePDF(full_html, dest=pdf_out)

    if pisa_status.err:
        print(f"Error converting {md_file}")
    else:
        print(f"Successfully created {pdf_file}")

def main():
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    for md_file, pdf_file in MAPPING.items():
        convert_md_to_pdf(md_file, pdf_file)

if __name__ == "__main__":
    main()
