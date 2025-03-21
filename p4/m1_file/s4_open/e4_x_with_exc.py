"""
Python Course - Part 4

https://github.com/egalli64/pyco

Module 1 - File

Open and close - x mode, exception, context manager
"""

FILENAME = "my_file.txt"


# combine try-except and with
try:
    with open(FILENAME, "x") as f:
        print(FILENAME, "has been created")
except FileExistsError as ex:
    print("Can't write-open", ex)
