"""
Python Course - Part 4

https://github.com/egalli64/pyco

Module 1 - File

Open and close - x mode, managing exception
"""

FILENAME = "my_file.txt"

try:
    # raise an exception if the file already exists
    file = open(FILENAME, "x")
except FileExistsError as ex:
    print("Can't write-open", ex)
finally:
    # close file, but only if it has been defined
    if "file" in locals():
        file.close()
