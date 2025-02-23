"""
Python Course - Part 4

https://github.com/egalli64/pyco

Module 3 - sqlite3

context manager on connection is not meant to close it
"""

import sqlite3

with sqlite3.connect("p4/m3_sqlite3/countries.db") as conn:
    cursor = conn.cursor()
    # this should work fine
    conn.execute("SELECT 1")

# since exiting the context manager DO NOT CLOSE the connection, this should work fine
conn.execute("SELECT 2")

# EXPLICIT CLOSE of the connection is REQUIRED
conn.close()

try:
    # this call should throw an exception
    conn.execute("SELECT 3")
except sqlite3.ProgrammingError as ex:
    print("Now the connection is closed:", ex)
