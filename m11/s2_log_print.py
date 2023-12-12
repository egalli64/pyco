"""
Python Course

https://github.com/egalli64/pyco

Module 11 - Log and Test

Log with print()

From terminal, redirect the stderr stream to file with 2>
"""
import sys

print("INFO: enter the script", file=sys.stderr)
print("Hello, user")
print("INFO: exit the script", file=sys.stderr)
