from pathlib import Path
import markdown
from weasyprint import HTML

def convert_markdown_to_PDF(md_path: Path, pdf_path: Path) -> None:

    md_text = md_path.read_text(encoding="utf-8")
    html_body = markdown.markdown(md_text, extensions=["extra", "tables"])

    html_full = f"""
    <html>
    <head>
        <meta charset="utf-8">
        <style>
            body {{ font-family: Arial, sans-serif; margin: 40px; }}
            h1, h2, h3 {{ margin-top: 24px; }}
            code {{ background: #f4f4f4; padding: 2px 4px; }}
        </style>
    </head>
    <body>
        {html_body}
    </body>
    </html>
    """

    HTML(string=html_full).write_pdf(str(pdf_path))

def main():

    print("START")
    
    md_file = Path("input.md")
    pdf_file = Path("output.pdf")

    if not md_file.exists():
        print("File not found")
        return
    
    convert_markdown_to_PDF(md_file, pdf_file)

    print(f"Created: {pdf_file.resolve()}")

if __name__ == "__main__":
    main()

