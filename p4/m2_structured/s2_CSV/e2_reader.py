"""
Python Course - Part 4

https://github.com/egalli64/pyco

Module 2 - Structured File

CSV - reader
"""

import csv

FILENAME = "friends.csv"

# reading each line from the CSV file in a list of strings
print("Each row in the CSV file")
with open(FILENAME) as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
