from pathlib import Path

# Load the Markdown content (uploaded as Rdocument.md)
md_path = Path("src/pages/page-content/Rdocument.md")
html_output_path = Path("src/pages/basic_r_programming.html")

# Read the markdown content
with open(md_path, "r", encoding="utf-8") as f:
    md_content = f.read()

# HTML shell to wrap the Markdown content (converted manually later)
html_template = f"""
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <title>Basic R Programming</title>
  <style>
    body {{
      font-family: Arial, sans-serif;
      line-height: 1.6;
      padding: 2rem;
      max-width: 900px;
      margin: auto;
      background: #fdfdfd;
    }}
    h1, h2, h3 {{
      color: #2a4b7c;
    }}
    pre {{
      background: #f5f5f5;
      padding: 1em;
      border-left: 4px solid #ccc;
      overflow-x: auto;
    }}
    code {{
      font-family: monospace;
      background: #f4f4f4;
      padding: 0.1em 0.3em;
    }}
    a {{
      color: #1b6d85;
      text-decoration: none;
    }}
    a:hover {{
      text-decoration: underline;
    }}
    ul {{
      margin-left: 1.2rem;
    }}
    img {{
      max-width: 120px;
    }}
    .footer {{
      margin-top: 4rem;
      font-size: 0.9em;
      text-align: center;
      color: #888;
    }}
    hr {{
      border: none;
      border-top: 1px solid #ccc;
      margin: 2rem 0;
    }}
  </style>
</head>
<body>

<img src="../img/R_logo.png" alt="R logo" />

<h1>Basic R Programming</h1>

<pre><code>
{md_content}
</code></pre>

<div class="footer">
  © 2025 Khon Kaen University National Phenome Institute (KKUNPhI)
</div>

</body>
</html>
"""

# Write HTML file
with open(html_output_path, "w", encoding="utf-8") as f:
    f.write(html_template)

html_output_path.name
