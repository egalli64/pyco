"""
Python Course - Part 4

https://github.com/egalli64/pyco

Module 1 - File

The module os: makedirs
"""

import os

path = "/tmp/"
try:
    os.makedirs(path, exist_ok=True)
    print(f"Make dir {path} (exist ok), then try to create it again (exist not ok)")
    os.makedirs(path)
except FileExistsError as ex:
    print("Can't create directory:", ex)
