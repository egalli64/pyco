"""
Python Course - Part 4

https://github.com/egalli64/pyco

Module 1 - File

Open and close - with
"""

FILENAME = "my_file.txt"


# the "with" statement takes care of closing the file
# open "w" could recreate a file - previous data would be lost!
with open(FILENAME, "w") as f:
    print(FILENAME, "has been created (again)")
