"""
Python Course - Part 4

https://github.com/egalli64/pyco

Module 1 - File

The module os: remove
"""

import os

try:
    os.remove("/tmp/missing.txt")
except FileNotFoundError as ex:
    print("Can't remove:", ex)
