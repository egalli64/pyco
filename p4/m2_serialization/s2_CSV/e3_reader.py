"""
Python Course - Part 4

https://github.com/egalli64/pyco

Module 2 - Serialization

CSV - reader
"""

import csv

PATH = "p4/m2_serialization/s2_CSV/"
FILENAME = PATH + "friends.csv"

# reading each line from the CSV file in a list of strings
print("Each row in the CSV file")
with open(FILENAME) as file:
    reader = csv.reader(file)
    for row in reader:
        # a row is seen as a list of strings
        print(row)
