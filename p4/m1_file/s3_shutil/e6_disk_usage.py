"""
Python Course - Part 4

https://github.com/egalli64/pyco

Module 1 - File

The module shutil: disk_usage
"""

import shutil

try:
    print(shutil.disk_usage("/"))
except FileNotFoundError as ex:
    print(ex)
