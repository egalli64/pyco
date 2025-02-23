"""
Python Course - Part 4

https://github.com/egalli64/pyco

Module 3 - sqlite3

CRUD: delete
"""

import sqlite3

# 1. initialization
COUNTRIES = "p4/m3_sqlite3/countries.db"
conn = sqlite3.connect(COUNTRIES)
cursor = conn.cursor()

# simulating the parameter passed in
region_id = 3

# 2. execute queries
try:
    cursor.execute("DELETE from country WHERE region_id = ?", (region_id,))
    print("Delete: row count", cursor.rowcount)
    cursor.execute("SELECT * FROM country WHERE country_id = ?", (region_id,))

except sqlite3.OperationalError as ex:
    print("Operational Error:", ex)
except Exception as ex:
    print("Something went wrong:", ex)

# 3. verify result
print(cursor.fetchall())

# 4. closing
cursor.close()
conn.close()
