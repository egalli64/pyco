"""
Python Course - Part 4

https://github.com/egalli64/pyco

Module 3 - RDB

sqlite3 - connect to an in-memory database
"""

import sqlite3

# lack of robustness and persistency
# in-memory database, not using "with" nor checking for exception
conn = sqlite3.connect(":memory:")
print("connected to in-memory database")

conn.close()
print("disconnected to in-memory database")
