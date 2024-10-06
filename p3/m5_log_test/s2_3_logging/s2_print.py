"""
Python Course - Part 3

https://github.com/egalli64/pyco

Module 5 - Log and Test

Log with print()

From terminal, redirect the stderr stream to the log file
    Ex: python script.py 2> script.log
"""
import sys

print("INFO: enter the script", file=sys.stderr)
print("Hello, user")
print("INFO: exit the script", file=sys.stderr)
