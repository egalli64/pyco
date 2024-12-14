"""
Python Course - Part 4

https://github.com/egalli64/pyco

Module 2 - Structured File

CSV - DictReader
"""

import csv

FILENAME = "friends.csv"

# reading each line from the CSV file in a dictionary
with open(FILENAME) as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row)
