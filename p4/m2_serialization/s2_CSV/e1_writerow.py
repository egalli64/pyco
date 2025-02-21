"""
Python Course - Part 4

https://github.com/egalli64/pyco

Module 2 - Serialization

CSV - writerow
"""

import csv

FILENAME = "friends.csv"
HEADER = ["Name", "Age", "City"]

friends = ["Tom", "Jenny", "Bob", "Kim", "Micky", "Lee"]
ages = [42, 37, 32, 41, 43, 38]
cities = ["Madrid", "Amsterdam", "Paris", "Stockholm", "Berlin", "London"]

# write as CSV the values passed, row by row
with open(FILENAME, "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(HEADER)
    for i in range(len(friends)):
        writer.writerow([friends[i], ages[i], cities[i]])
