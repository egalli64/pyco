"""
Python Course - Base

https://github.com/egalli64/pycoba

Module 7 - File

open() and close()
"""
FILENAME = "my_file.txt"

# open a file in mode write(text)
f = open(FILENAME, "w")
print(FILENAME, "has been created (again?)")
f.close()

# the "with" statement takes care of closing the file
with open(FILENAME, "w") as f:
    # recreate a file - previous data are lost!
    print(FILENAME, "has been created (again)")

try:
    # raise an exception if the file already exists
    f = open(FILENAME, "x")
    f.close()
except FileExistsError as ex:
    print("Can't write-open", ex)

# combine try-except and with
try:
    with open(FILENAME, "x") as f:
        print(FILENAME, "has been created")
except FileExistsError as ex:
    print("Can't write-open", ex)
