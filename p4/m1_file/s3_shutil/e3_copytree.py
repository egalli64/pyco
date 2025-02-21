"""
Python Course - Part 4

https://github.com/egalli64/pyco

Module 1 - File

The module shutil: copytree
"""

import shutil

try:
    shutil.copytree("/tmp/", "/tmp/other/")
except (FileNotFoundError, FileExistsError) as ex:
    print("Can't copy:", ex)
