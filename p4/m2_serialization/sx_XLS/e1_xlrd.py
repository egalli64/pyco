"""
Python Course - Part 4

https://github.com/egalli64/pyco

Module 2 - Serialization

Accessing XLS file by xlrd

https://xlrd.readthedocs.io/en/latest/

pip install xlrd
"""

import xlrd

SOURCE = "p4/m2_serialization/sx_XLS/friends.xls"

book = xlrd.open_workbook(SOURCE)
print(f"There are {book.nsheets} worksheets in this workbook")
print("Worksheet names are", book.sheet_names())

sheet = book.sheet_by_index(0)
print(f"Sheet {sheet.name} has {sheet.nrows} rows and {sheet.ncols} columns")

for i in range(sheet.nrows):
    print(sheet.row(i))

print("A cell value:", sheet.cell_value(rowx=1, colx=1))
