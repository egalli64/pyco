"""
Python Course - Part 4

https://github.com/egalli64/pyco

Module 1 - File

The module os: listdir
"""

import os

for path in [".", "/tmp/"]:
    try:
        print(f"The content of '{path}' is", os.listdir(path))
    except FileNotFoundError as ex:
        print("Can't list directory:", ex)
