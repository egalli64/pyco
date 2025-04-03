"""
Python Course - Part 4

https://github.com/egalli64/pyco

Module 2 - Serialization

CSV - DictReader
"""

import csv

PATH = "p4/m2_serialization/s2_CSV/"
FILENAME = PATH + "friends.csv"

# reading each line from the CSV file in a dictionary
with open(FILENAME) as f:
    # in this form the first row is used as header
    reader = csv.DictReader(f)
    for row in reader:
        # a row is seen as a dictionary with keys from the field names
        print(row)
