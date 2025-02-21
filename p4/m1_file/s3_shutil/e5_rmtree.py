"""
Python Course - Part 4

https://github.com/egalli64/pyco

Module 1 - File

The module shutil: rmtree
"""

import shutil

try:
    shutil.rmtree("/tmp/other/")
except FileNotFoundError as ex:
    print("Can't remove directory:", ex)
