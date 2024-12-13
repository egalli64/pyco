"""
Python Course - Part 4

https://github.com/egalli64/pyco

Module 1 - File

The Path class
"""

from pathlib import Path
from random import random

OUTPUT_FILENAME = "random_values.txt"

content = ""
for value in range(10):
    content += str(random()) + "\n"

output_path = Path(OUTPUT_FILENAME)
if output_path.exists():
    print(f"The file {OUTPUT_FILENAME} already exists!")
else:
    # if we don't check, it would overwrite existing data
    output_path.write_text(content)
