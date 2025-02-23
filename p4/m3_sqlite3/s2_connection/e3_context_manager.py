"""
Python Course - Part 4

https://github.com/egalli64/pyco

Module 3 - sqlite3

context manager on connection is not meant to close it
"""

import sqlite3

# the connection is created in a context manager, but close() is still our responsibility!
with sqlite3.connect("p4/m3_sqlite3/countries.db") as conn:
    # this should work fine
    print("Check ...", conn.execute("SELECT 1").fetchone()[0])

# since exiting the context manager DO NOT CLOSE the connection, this should work fine
print("Check ...", conn.execute("SELECT 2").fetchone()[0])

# EXPLICIT CLOSE of the connection is REQUIRED
conn.close()

try:
    # this call should throw an exception
    print("Check ...", conn.execute("SELECT 3").fetchone()[0])
except sqlite3.ProgrammingError as ex:
    print("Now the connection is closed:", ex)
