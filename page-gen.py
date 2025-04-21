from pathlib import Path
import os
import zipfile

# Define paths
zip_path = "src/pages/page-content/Archive.zip"
extract_dir = "src/pages/page-content"
output_dir = "src/pages/"

# Extract the zip file
with zipfile.ZipFile(zip_path, 'r') as zip_ref:
    zip_ref.extractall(extract_dir)

# Walk through folders and gather SVG file structure
folder_structure = {}
for root, dirs, files in os.walk(extract_dir):
    svg_files = [f for f in files if f.lower().endswith('.svg')]
    if svg_files:
        relative_path = os.path.relpath(root, extract_dir)
        folder_structure[relative_path] = svg_files

# Helper function to read SVG content
def read_svg_content(svg_path):
    with open(svg_path, 'r', encoding='utf-8') as f:
        return f.read()

# HTML Template WITHOUT showing file names
html_template_embedded_svg = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{folder}r</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            background-color: #fdfdfd;
            margin: 0;
            padding: 0;
        }}
        h1 {{
            text-align: center;
            padding: 20px;
            background-color: #f0f0f0;
            border-bottom: 1px solid #ccc;
        }}
        .page {{
            page-break-after: always;
            padding: 0;
        }}
        svg {{
            width: 100vw;
            height: auto;
            display: block;
        }}
        footer {{
            background-color: #343a40;
            color: white;
            text-align: center;
            padding: 20px;
            position: relative;
            bottom: 0;
            width: 100%;
        }}
        footer a {{
            color: #f8f9fa;
            text-decoration: none;
        }}
        footer a:hover {{
            text-decoration: underline;
        }}
        button {{
            background-color: #1b6d85;
            color: white;
            padding: 10px 20px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            text-align: center;
        }}
        .home-button {{
            text-align: center;
            margin: 20px;
        }}
    </style>
</head>
<body>

    {pages}

    <div class="home-button">
      <button onclick="location.href='https://kkunphi.github.io/phenomic-short-course/'">Home</button>
    </div>

    <footer>
      <p>© 2025 Khon Kaen University National Phenome Institute (KKUNPhI) | 
      <a href="https://kkunphi.github.io/Agbio2/">Visit Us Facebook</a></p>
    </footer>

    <script>
    function bootstrapStylePandocTables() {{
      $('tr.odd').parent('tbody').parent('table').addClass('table table-condensed');
    }}
    $(document).ready(function () {{
      bootstrapStylePandocTables();
    }});
    </script>

    <script>
    $(document).ready(function () {{
      window.buildTabsets("TOC");
      $('.tabset-dropdown > .nav-tabs > li').click(function () {{
        $(this).parent().toggleClass('nav-tabs-open');
      }});
    }});
    </script>

    <script>
    (function () {{
      var script = document.createElement("script");
      script.type = "text/javascript";
      script.src  = "https://mathjax.rstudio.com/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML";
      document.getElementsByTagName("head")[0].appendChild(script);
    }})();
    </script>

</body>
</html>
"""

# Generate HTML with embedded SVG for each folder
for folder, svg_files in folder_structure.items():
    if folder.startswith("__MACOSX"):
        continue

    sorted_svgs = sorted(svg_files, key=lambda f: f.lower())
    pages_html = ""
    for svg in sorted_svgs:
        svg_path = Path(extract_dir) / folder / svg
        if not svg_path.exists():
            continue
        svg_code = read_svg_content(svg_path)
        pages_html += f"""
        <div class="page">
            {svg_code}
        </div>
        """

    html_content = html_template_embedded_svg.format(folder=folder, pages=pages_html)
    html_filename = f"{folder.replace(' ', '_')}_embedded.html"
    html_path = os.path.join(output_dir, html_filename)

    with open(html_path, "w", encoding="utf-8") as f:
        f.write(html_content)

print("✅ HTML files generated in:", output_dir)
