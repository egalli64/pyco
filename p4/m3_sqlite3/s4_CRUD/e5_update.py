"""
Python Course - Part 4

https://github.com/egalli64/pyco

Module 3 - sqlite3

CRUD: update
"""

import sqlite3

# 1. initialization
COUNTRIES = "p4/m3_sqlite3/countries.db"
conn = sqlite3.connect(COUNTRIES)
cursor = conn.cursor()

# simulating parameters passed in
old_region_id = 4
new_region_id = 1

# 2. execute queries
try:
    cursor.execute(
        "UPDATE country SET region_id = ? WHERE region_id = ?",
        (new_region_id, old_region_id),
    )
    print("Update: row count", cursor.rowcount)
    cursor.execute("SELECT * FROM country WHERE region_id = ?", (new_region_id,))

except sqlite3.OperationalError as ex:
    print("Operational Error:", ex)
except Exception as ex:
    print("Something went wrong:", ex)

# 3. verify result
print(cursor.fetchall())

# 4. closing
cursor.close()
conn.close()
