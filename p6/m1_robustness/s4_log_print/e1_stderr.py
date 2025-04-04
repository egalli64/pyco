"""
Python Course - Part 6

https://github.com/egalli64/pyco

Module 1 - Code robustness

Log with print() to standard error

From terminal, redirect the stderr stream to the log file
    Ex: python script.py 2> script.log
"""
import sys

print("INFO: enter the script", file=sys.stderr)
print("Hello, user")
print("INFO: exit the script", file=sys.stderr)
