"""
Python Course - Part 6

https://github.com/egalli64/pyco

Module 1 - Log and Test

Log with print() to file
"""

import sys

LOG_PATH = "p6/m1_robustness/s4_log_print/"
FILENAME = LOG_PATH + "script.log"

with open(FILENAME, "a") as log:
    print("INFO: enter the script", file=log)
    print("Hello, user")
    print("INFO: exit the script", file=log)
