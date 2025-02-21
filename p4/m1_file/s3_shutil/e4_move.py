"""
Python Course - Part 4

https://github.com/egalli64/pyco

Module 1 - File

The module shutil: move
"""

import shutil

try:
    shutil.move("/tmp/hello.txt", "/tmp/ciao.txt")
except FileNotFoundError as ex:
    print("Can't move:", ex)

try:
    shutil.move("/tmp/missing", "/tmp/other")
except (FileNotFoundError, shutil.Error) as ex:
    print("Can't move:", ex)
