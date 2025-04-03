"""
Python Course - Part 4

https://github.com/egalli64/pyco

Module 2 - Serialization

CSV - DictWriter
"""

import csv

PATH = "p4/m2_serialization/s2_CSV/"
FILENAME = PATH + "friends.csv"
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
    # the constructor wants the field names
    writer = csv.DictWriter(file, fieldnames=HEADER)

    # uses the field names to generate the CSV header
    writer.writeheader()
    for friend in friends:
        # the dictionary keys should match the field names
        writer.writerow(friend)
