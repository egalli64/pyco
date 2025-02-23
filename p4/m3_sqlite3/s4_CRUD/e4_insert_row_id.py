"""
Python Course - Part 4

https://github.com/egalli64/pyco

Module 3 - sqlite3

CRUD: create by insert (no autoincrement), lastrowid shows ROWID
"""

import sqlite3

# 1. initialization
COUNTRIES = "p4/m3_sqlite3/countries.db"
conn = sqlite3.connect(COUNTRIES)
cursor = conn.cursor()

# simulating parameters passed in
country_id = "XX"
country_name = "Unknown"
region_id = 1

# 2. execute queries
try:
    cursor.execute(
        "INSERT INTO country (country_id, name, region_id) values (?, ?, ?)",
        (country_id, country_name, region_id),
    )
    print(f"Insert: last row id {cursor.lastrowid}, row count {cursor.rowcount}")

    cursor.execute("SELECT * FROM country WHERE region_id = ?", (region_id,))

except sqlite3.OperationalError as ex:
    print("Operational Error:", ex)
except Exception as ex:
    print("Something went wrong:", ex)

# 3. verify result
print(cursor.fetchall())

# 4. closing
cursor.close()
conn.close()
