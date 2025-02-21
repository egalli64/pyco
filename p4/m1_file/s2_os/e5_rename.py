"""
Python Course - Part 4

https://github.com/egalli64/pyco

Module 1 - File

The module os: rename
"""

import os

try:
    os.rename("/tmp/hello.txt", "/tmp/ciao.txt")
except FileNotFoundError as ex:
    print("Can't rename:", ex)

try:
    os.rename("/tmp/missing", "/tmp/other")
except FileNotFoundError as ex:
    print("Can't rename:", ex)
