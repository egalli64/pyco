"""
Python Course - Part 4

https://github.com/egalli64/pyco

Module 1 - File

Open and close - x mode, managing exception
"""

FILENAME = "my_file.txt"

try:
    # raise an exception if the file already exists
    f = open(FILENAME, "x")
except FileExistsError as ex:
    print("Can't write-open", ex)
finally:
    # close f, but only if f has been defined
    if "f" in locals():
        f.close()
