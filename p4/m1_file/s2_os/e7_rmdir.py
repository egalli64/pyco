"""
Python Course - Part 4

https://github.com/egalli64/pyco

Module 1 - File

The module os: rmdir
"""

import os

try:
    os.rmdir("/tmp/missing")
except (FileNotFoundError, OSError) as ex:
    print("Can't remove directory:", ex)
