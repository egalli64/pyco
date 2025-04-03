"""
Python Course - Part 4

https://github.com/egalli64/pyco

Module 2 - Serialization

Deserializing XLS file by xlrd

https://xlrd.readthedocs.io/en/latest/
"""

import xlrd

PATH = "p4/m2_serialization/s3_XLS/"
FILENAME = PATH + "friends.xls"

book = xlrd.open_workbook(FILENAME)
print(f"There are {book.nsheets} worksheets in this workbook")
print("Worksheet names are", book.sheet_names())

sheet = book.sheet_by_index(0)
print(f"Sheet {sheet.name} has {sheet.nrows} rows and {sheet.ncols} columns\n")

# looping on all the row/col indices
for i in range(sheet.nrows):
    for j in range(sheet.ncols):
        # accessing the cell value by cell indices
        print(sheet.cell_value(rowx=i, colx=j), end=" ")
    print()
print()

# iterating on each row to get each cell with its value
for i in range(sheet.nrows):
    for cell in sheet.row(i):
        print(cell.value, end=" ")
    print()
print()
