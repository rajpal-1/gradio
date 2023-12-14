#!/usr/bin/env python

import re
from pathlib import Path

README_TEMPLATE_FILEPATH = "readme_template.md"
GETTING_STARTED_TEMPLATE_FILEPATH = "guides/01_getting-started/01_quickstart.md"

readme_template = Path(README_TEMPLATE_FILEPATH).read_text()
getting_started_template = Path(GETTING_STARTED_TEMPLATE_FILEPATH).read_text()
getting_started_template = getting_started_template.replace("# Quickstart", "")
getting_started_template = getting_started_template.replace("Tip:", "✍️ Tip:")

# Extract all the code and demo tags from the getting started template
code_tags = re.findall(r"\$code_([^\s]+)", getting_started_template)
demo_tags = re.findall(r"\$demo_([^\s]+)", getting_started_template)
codes = {}
demos = {}

for src in code_tags:
    context = Path(f"demo/{src}/run.py").read_text()
    # Replace the condition to run the demo directly with actual launch code
    context = re.sub(r"if __name__(.*[\n$]*)*", "demo.launch()", context)
    codes[src] = f"```python\n{context}\n```\n"  # Convert to Markdown code block

for src in demo_tags:
    demos[src] = f"![`{src}` demo](demo/{src}/screenshot.gif)"

# Replace the headers in the getting started template with a smaller header (e.g. H3 instead of H2) to
# make the README more readable and less cluttered.
getting_started_template = re.sub(r"^(#+)", r"#\1", getting_started_template, flags=re.MULTILINE)
readme_template = readme_template.replace("$getting_started", getting_started_template)

# Now put the codes and the screenshots in the README template
readme_template = re.sub(r"\$code_([^\s]+)", lambda x: codes[x.group(1)], readme_template)
readme_template = re.sub(r"\$demo_([^\s]+)", lambda x: demos[x.group(1)], readme_template)

# Save the README template to the actual README.md file (with a note about the editing)
EDITING_NOTE = ("<!-- DO NOT EDIT THIS FILE DIRECTLY. INSTEAD EDIT THE `readme_template.md` OR "
                "`guides/1)getting_started/1)quickstart.md` TEMPLATES AND THEN RUN `render_readme.py` SCRIPT. -->")
Path("README.md").write_text(f"{EDITING_NOTE}\n\n{readme_template}")
