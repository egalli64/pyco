"""
Python Course - Part 4

https://github.com/egalli64/pyco

Module 3 - sqlite3

CRUD: read by select
"""

import sqlite3

# 1. initialization
COUNTRIES = "p4/m3_sqlite3/countries.db"
conn = sqlite3.connect(COUNTRIES)
cursor = conn.cursor()

# 2. execute query
try:
    cursor.execute("SELECT * FROM country")
except sqlite3.OperationalError as ex:
    print("Operational Error:", ex)
except Exception as ex:
    print("Something went wrong:", ex)

# 3. use result set
print(cursor.fetchone())
print(cursor.fetchmany(5))
print(cursor.fetchall())

# 4. closing
cursor.close()
conn.close()
