"""
Franchise Investor Academy (FIA) — Automated eBook PDF Compiler
================================================================
Compiles Markdown chapters of any Academy volume into a publication-grade,
print-ready PDF document using Python-Markdown and headless Chrome/Edge.

Usage:
    python tools/education/compile_book_to_pdf.py
    python tools/education/compile_book_to_pdf.py --book book-01-first-time-investor-handbook
    python tools/education/compile_book_to_pdf.py --book book-01-first-time-investor-handbook --output Book-01-First-Time-Investor-Handbook.pdf
"""

import os
import sys
import re
import argparse
import subprocess
import shutil
import tempfile
from typing import List, Optional

try:
    import markdown
except ImportError:
    print("[ERROR] 'markdown' package is not installed. Run: pip install markdown")
    sys.exit(1)


def find_browser_executable() -> Optional[str]:
    """Locate Google Chrome or Microsoft Edge executable across common Windows/macOS/Linux paths."""
    candidates = [
        # Windows Chrome
        r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
        os.path.expandvars(r"%LOCALAPPDATA%\Google\Chrome\Application\chrome.exe"),
        # Windows Edge
        r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
        r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
        # macOS
        "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
        "/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge",
        # Linux
        "/usr/bin/google-chrome",
        "/usr/bin/chromium-browser",
        "/usr/bin/chromium",
        "/usr/bin/microsoft-edge",
    ]
    for path in candidates:
        if os.path.exists(path):
            return path
    
    # Try which / where in PATH
    for name in ["chrome", "google-chrome", "msedge", "chromium"]:
        found = shutil.which(name)
        if found:
            return found
            
    return None


def get_book_files(book_dir: str) -> List[str]:
    """Return an ordered list of Markdown file paths for the given book directory."""
    if not os.path.exists(book_dir):
        raise FileNotFoundError(f"Book directory not found: {book_dir}")
        
    all_files = [f for f in os.listdir(book_dir) if f.endswith(".md")]
    
    # Preferred ordering: README first, chapters 01..99, then quizzes/case studies/appendices
    readme = [f for f in all_files if f.lower() == "readme.md"]
    chapters = sorted([f for f in all_files if re.match(r"^chapter-\d+", f, re.IGNORECASE)])
    quizzes = [f for f in all_files if "quiz" in f.lower() or "case-stud" in f.lower()]
    others = sorted([f for f in all_files if f not in readme and f not in chapters and f not in quizzes])
    
    ordered = readme + chapters + quizzes + others
    return [os.path.join(book_dir, f) for f in ordered]


def preprocess_markdown(content: str) -> str:
    """Transform GitHub alerts (> [!WARNING], etc.) into styled HTML admonition blocks."""
    alert_types = {
        "NOTE": ("#0969da", "#ddf4ff", "ℹ️ NOTE"),
        "TIP": ("#1a7f37", "#dafbe1", "💡 TIP"),
        "IMPORTANT": ("#8250df", "#fbefff", "🎓 IMPORTANT"),
        "WARNING": ("#9a6700", "#fff8c5", "⚠️ WARNING"),
        "CAUTION": ("#cf222e", "#ffebe9", "🛑 CAUTION"),
    }
    
    for alert, (border_col, bg_col, label) in alert_types.items():
        pattern = re.compile(rf'>\s*\[!{alert}\]\s*\n((?:>.*(?:\n|$))*)', re.MULTILINE)
        
        def replace_alert(match):
            body_lines = match.group(1).splitlines()
            cleaned_lines = [re.sub(r'^>\s?', '', line) for line in body_lines]
            inner_text = "\n".join(cleaned_lines)
            return (
                f'<div class="admonition admonition-{alert.lower()}">\n'
                f'<div class="admonition-title">{label}</div>\n'
                f'{inner_text}\n'
                f'</div>\n\n'
            )
            
        content = pattern.sub(replace_alert, content)
        
    # Convert relative file links that point to .md into bold text anchors for clean printing
    content = re.sub(r'\[([^\]]+)\]\([^)]+\.md(?:#[^)]*)?\)', r'**\1**', content)
    return content


def get_css_styles() -> str:
    """Return print-optimized CSS stylesheet for corporate eBook publications."""
    return """
    @page {
        size: A4;
        margin: 20mm 15mm 20mm 15mm;
        @bottom-right {
            content: counter(page);
            font-family: 'Segoe UI', Arial, sans-serif;
            font-size: 9pt;
            color: #666;
        }
        @bottom-left {
            content: "Franchise Investor Academy — Franchise Business Modeling Platform";
            font-family: 'Segoe UI', Arial, sans-serif;
            font-size: 8pt;
            color: #888;
        }
    }

    body {
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
        color: #24292f;
        line-height: 1.6;
        font-size: 10.5pt;
        background-color: #ffffff;
    }

    .chapter-break {
        page-break-before: always;
        margin-top: 2rem;
    }

    .cover-page {
        page-break-after: always;
        height: 85vh;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        text-align: center;
        border: 2px solid #0969da;
        padding: 40px;
        background: linear-gradient(135deg, #f6f8fa 0%, #ffffff 100%);
        border-radius: 8px;
    }

    .cover-title {
        font-size: 26pt;
        font-weight: 800;
        color: #0969da;
        margin-bottom: 12px;
        line-height: 1.2;
    }

    .cover-subtitle {
        font-size: 14pt;
        color: #57606a;
        margin-bottom: 30px;
        max-width: 600px;
        line-height: 1.4;
    }

    .cover-badge {
        display: inline-block;
        padding: 6px 14px;
        background-color: #0969da;
        color: white;
        font-weight: 600;
        font-size: 9pt;
        border-radius: 20px;
        text-transform: uppercase;
        letter-spacing: 1px;
        margin-bottom: 25px;
    }

    .cover-meta {
        font-size: 10pt;
        color: #6e7781;
        margin-top: 40px;
        border-top: 1px solid #d0d7de;
        padding-top: 20px;
        width: 80%;
    }

    h1 {
        font-size: 20pt;
        color: #0969da;
        border-bottom: 2px solid #d0d7de;
        padding-bottom: 6px;
        margin-top: 24px;
        margin-bottom: 16px;
        page-break-after: avoid;
    }

    h2 {
        font-size: 14pt;
        color: #1f2328;
        border-bottom: 1px solid #eaeef2;
        padding-bottom: 4px;
        margin-top: 20px;
        margin-bottom: 12px;
        page-break-after: avoid;
    }

    h3 {
        font-size: 12pt;
        color: #24292f;
        margin-top: 16px;
        margin-bottom: 8px;
        page-break-after: avoid;
    }

    p, li {
        margin-bottom: 8px;
        text-align: justify;
    }

    table {
        width: 100%;
        border-collapse: collapse;
        margin: 16px 0;
        font-size: 9pt;
        page-break-inside: avoid;
    }

    th, td {
        border: 1px solid #d0d7de;
        padding: 6px 10px;
        text-align: left;
    }

    th {
        background-color: #f6f8fa;
        color: #1f2328;
        font-weight: 600;
    }

    tr:nth-child(even) {
        background-color: #fcfcfc;
    }

    pre {
        background-color: #f6f8fa;
        border: 1px solid #d0d7de;
        border-radius: 6px;
        padding: 12px;
        overflow-x: auto;
        font-family: 'Consolas', 'Courier New', monospace;
        font-size: 8.5pt;
        page-break-inside: avoid;
        margin: 14px 0;
        line-height: 1.4;
    }

    code {
        font-family: 'Consolas', 'Courier New', monospace;
        background-color: #eff1f3;
        padding: 2px 4px;
        border-radius: 4px;
        font-size: 9pt;
    }

    pre code {
        background: none;
        padding: 0;
    }

    blockquote {
        margin: 12px 0;
        padding: 6px 14px;
        color: #57606a;
        border-left: 4px solid #d0d7de;
        background-color: #f6f8fa;
        page-break-inside: avoid;
    }

    .admonition {
        border-left: 4px solid #0969da;
        background-color: #f6f8fa;
        padding: 10px 14px;
        margin: 14px 0;
        border-radius: 0 6px 6px 0;
        page-break-inside: avoid;
    }

    .admonition-title {
        font-weight: 700;
        font-size: 10pt;
        margin-bottom: 4px;
    }

    .admonition-warning {
        border-left-color: #bf8700;
        background-color: #fffbeb;
    }
    .admonition-warning .admonition-title { color: #9a6700; }

    .admonition-important {
        border-left-color: #8250df;
        background-color: #fbf7ff;
    }
    .admonition-important .admonition-title { color: #8250df; }

    .admonition-caution {
        border-left-color: #cf222e;
        background-color: #fff5f5;
    }
    .admonition-caution .admonition-title { color: #cf222e; }

    .admonition-tip {
        border-left-color: #1a7f37;
        background-color: #f3faf5;
    }
    .admonition-tip .admonition-title { color: #1a7f37; }

    hr {
        border: 0;
        border-top: 1px solid #d0d7de;
        margin: 20px 0;
    }
    """


def compile_book_to_pdf(book_dir: str, output_pdf: str, keep_html: bool = False) -> str:
    """Compile all markdown files in book_dir into a single PDF document."""
    browser_path = find_browser_executable()
    if not browser_path:
        raise RuntimeError("No Chromium/Edge browser found. Please install Chrome or Edge.")
        
    print(f"[INFO] Using headless browser: {browser_path}")
    
    files = get_book_files(book_dir)
    print(f"[INFO] Found {len(files)} files to compile in {os.path.basename(book_dir)}:")
    for f in files:
        print(f"  - {os.path.basename(f)}")
        
    md_compiler = markdown.Markdown(extensions=['tables', 'fenced_code', 'toc'])
    
    # Extract book title from README if present
    book_title = "Franchise Investor Academy Volume"
    book_subtitle = "Educational Publication for Franchise Investors"
    
    readme_path = os.path.join(book_dir, "README.md")
    if os.path.exists(readme_path):
        with open(readme_path, "r", encoding="utf-8") as rf:
            lines = [l.strip() for l in rf.readlines() if l.strip()]
            if lines and lines[0].startswith("# "):
                book_title = lines[0].replace("# ", "")
            if len(lines) > 1 and lines[1].startswith("## "):
                book_subtitle = lines[1].replace("## ", "")
                
    # Build complete HTML string
    html_parts = [
        "<!DOCTYPE html>",
        "<html lang='en'>",
        "<head>",
        "<meta charset='utf-8'>",
        f"<title>{book_title}</title>",
        f"<style>{get_css_styles()}</style>",
        "</head>",
        "<body>",
        # Cover Page
        "<div class='cover-page'>",
        "<div class='cover-badge'>Franchise Investor Academy • Volume Release</div>",
        f"<div class='cover-title'>{book_title}</div>",
        f"<div class='cover-subtitle'>{book_subtitle}</div>",
        "<div class='cover-meta'>",
        "<p><strong>Publisher:</strong> Franchise Business Modeling & Intelligence Platform</p>",
        "<p><strong>Curriculum:</strong> Track 1 (Beginner Level) • Industry-Agnostic Investor Education</p>",
        "<p><strong>Publication Date:</strong> October 2026 • Reference Release (v1.0.0)</p>",
        "</div>",
        "</div>"
    ]
    
    # Process each markdown file
    for i, fpath in enumerate(files):
        with open(fpath, "r", encoding="utf-8", errors="ignore") as f:
            raw_text = f.read()
            
        processed_text = preprocess_markdown(raw_text)
        rendered_html = md_compiler.convert(processed_text)
        
        # Add page break before subsequent chapters
        if i > 0:
            html_parts.append("<div class='chapter-break'></div>")
            
        html_parts.append(rendered_html)
        md_compiler.reset()
        
    html_parts.append("</body></html>")
    full_html = "\n".join(html_parts)
    
    # Write to a temporary HTML file
    temp_dir = tempfile.gettempdir()
    temp_html_path = os.path.join(temp_dir, f"{os.path.basename(book_dir)}_temp.html")
    with open(temp_html_path, "w", encoding="utf-8") as hf:
        hf.write(full_html)
        
    abs_output_pdf = os.path.abspath(output_pdf)
    os.makedirs(os.path.dirname(abs_output_pdf), exist_ok=True)
    
    print(f"[INFO] Rendering PDF via headless browser: {os.path.basename(abs_output_pdf)} ...")
    
    # Launch browser with --headless=new and --print-to-pdf
    cmd = [
        browser_path,
        "--headless=new",
        "--disable-gpu",
        "--no-pdf-header-footer",
        f"--print-to-pdf={abs_output_pdf}",
        f"file:///{temp_html_path.replace(os.sep, '/')}"
    ]
    
    result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=60)
    
    if not os.path.exists(abs_output_pdf) or os.path.getsize(abs_output_pdf) == 0:
        raise RuntimeError(f"PDF generation failed! Exit code: {result.returncode}, Stderr: {result.stderr.decode('utf-8', errors='ignore')}")
        
    pdf_size_kb = os.path.getsize(abs_output_pdf) / 1024
    print(f"[SUCCESS] PDF generated successfully: {abs_output_pdf} ({pdf_size_kb:.1f} KB)")
    
    if keep_html:
        html_out = abs_output_pdf.replace(".pdf", ".html")
        shutil.copy(temp_html_path, html_out)
        print(f"[INFO] Preserved HTML source: {html_out}")
        
    if os.path.exists(temp_html_path):
        os.remove(temp_html_path)
        
    return abs_output_pdf


def main():
    repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
    default_book = os.path.join(repo_root, "education", "franchise-investor-academy", "book-01-first-time-investor-handbook")
    default_output = os.path.join(default_book, "Book-01-The-First-Time-Franchise-Investors-Handbook.pdf")
    
    parser = argparse.ArgumentParser(description="Compile Academy eBook volumes into a publication-grade PDF.")
    parser.add_argument("--book", default=default_book, help="Path to book directory or folder name in education/franchise-investor-academy/")
    parser.add_argument("--output", default=default_output, help="Target output PDF file path")
    parser.add_argument("--keep-html", action="store_true", help="Keep intermediate HTML file for web viewing or debugging")
    
    args = parser.parse_args()
    
    # Allow passing just the folder name (e.g., --book book-01-first-time-investor-handbook)
    target_book_dir = args.book
    if not os.path.isdir(target_book_dir):
        alt_path = os.path.join(repo_root, "education", "franchise-investor-academy", args.book)
        if os.path.isdir(alt_path):
            target_book_dir = alt_path
        else:
            print(f"[ERROR] Cannot locate book directory: {args.book}")
            sys.exit(1)
            
    try:
        compile_book_to_pdf(target_book_dir, args.output, keep_html=args.keep_html)
    except Exception as e:
        print(f"[ERROR] Failed to compile PDF: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
