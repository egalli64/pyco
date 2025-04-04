"""
Python Course - Part 4

https://github.com/egalli64/pyco

Module 3 - sqlite3

CRUD: a SQL injection attack to a parametrized SELECT
"""

import sqlite3

COUNTRIES = "p4/m3_sqlite3/countries.db"
conn = sqlite3.connect(COUNTRIES)
cursor = conn.cursor()

# the expected usage
# name = "Italy"
# SQL injection
name = "' OR '1'='1"

query = "SELECT * FROM country WHERE name = ?"

try:
    # the passed variable is treated as a literal string
    cursor.execute(query, (name,))
except Exception as ex:
    print("Something went wrong:", type(ex), ex)
else:
    print(cursor.fetchall())

cursor.close()
conn.close()
