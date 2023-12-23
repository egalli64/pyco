"""
Python Course - Part 1

https://github.com/egalli64/pyco

Module 8 - File

CSV
"""
import csv

FILENAME = "friends.csv"
HEADER = ['Name', 'Age', 'City']

friends = ["Tom", "Jenny", "Bob", "Kim", "Micky", "Lee"]
ages = [42, 37, 32, 41, 43, 38]
cities = ["Madrid", "Amsterdam", "Paris", "Stockholm", "Berlin", "London"]

# writing each line to the CSV file from a list of string convertible objects
with open(FILENAME, 'w', newline="") as f:
    writer = csv.writer(f)
    writer.writerow(HEADER)
    for i in range(len(friends)):
        writer.writerow([friends[i], ages[i], cities[i]])

# reading each line from the CSV file in a list of strings
print("Each row in the CSV file")
with open(FILENAME) as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

friend_info = []

# reading each line from the CSV file in a dictionary
with open(FILENAME) as f:
    reader = csv.DictReader(f)
    for row in reader:
        friend_info.append(row)

print("Friend info:", friend_info)

# writing each line to the CSV file from a list of dictionaries
with open(FILENAME, 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=['Name', 'Age', 'City'])

    writer.writeheader()
    for friend in friend_info:
        writer.writerow(friend)
