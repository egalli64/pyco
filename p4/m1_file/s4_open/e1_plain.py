"""
Python Course - Part 4

https://github.com/egalli64/pyco

Module 1 - File

Open and close
"""

FILENAME = "my_file.txt"

# open a file in mode write(text) could recreate a file - previous data would be lost!
file = open(FILENAME, "w")
print(FILENAME, "has been created (again?)")
file.close()
