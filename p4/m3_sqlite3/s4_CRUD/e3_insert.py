"""
Python Course - Part 4

https://github.com/egalli64/pyco

Module 3 - sqlite3

CRUD: create by insert (autoincrement), lastrowid shows PK
"""

import sqlite3

# 1. initialization
COUNTRIES = "p4/m3_sqlite3/countries.db"
conn = sqlite3.connect(COUNTRIES)
cursor = conn.cursor()

# simulating a parameter passed in
region_name = "Antarctica"

# 2. execute queries
try:
    cursor.execute("INSERT INTO region (name) values (?)", (region_name,))
    print(f"Insert: last row id {cursor.lastrowid}, row count {cursor.rowcount}")
    cursor.execute("SELECT * FROM region")

except sqlite3.OperationalError as ex:
    print("Operational Error:", ex)
except Exception as ex:
    print("Something went wrong:", ex)

# 3. verify result
print(cursor.fetchall())

# 4. closing
cursor.close()
conn.close()
