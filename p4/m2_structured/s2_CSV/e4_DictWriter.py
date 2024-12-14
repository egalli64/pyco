"""
Python Course - Part 4

https://github.com/egalli64/pyco

Module 2 - Structured File

CSV - DictWriter
"""

import csv

FILENAME = "friends.csv"
HEADER = ["Name", "Age", "City"]

friends = [
    {"Name": "Tom", "Age": 42, "City": "Madrid"},
    {"Name": "Jenny", "Age": 37, "City": "Amsterdam"},
    {"Name": "Bob", "Age": 32, "City": "Paris"},
    {"Name": "Kim", "Age": 41, "City": "Stockholm"},
    {"Name": "Micky", "Age": 43, "City": "Berlin"},
    {"Name": "Lee", "Age": 38, "City": "London"},
]

# writing each line to the CSV file from a list of dictionaries
with open(FILENAME, "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=HEADER)

    writer.writeheader()
    for friend in friends:
        writer.writerow(friend)
