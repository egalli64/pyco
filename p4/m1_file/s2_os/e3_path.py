"""
Python Course - Part 4

https://github.com/egalli64/pyco

Module 1 - File

The module os: path.isfile, path.isdir
"""

import os

for path in [".", "README.md", "missing"]:
    print(f"'{path}' is a file?", os.path.isfile(path))
    print(f"'{path}' is a directory?", os.path.isdir(path))
