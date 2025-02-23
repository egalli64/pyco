"""
Python Course - Part 4

https://github.com/egalli64/pyco

Module 3 - sqlite3

Transaction - setup for examples, ensure no row has a PK > 4
"""

import sqlite3

COUNTRIES = "p4/m3_sqlite3/countries.db"
conn = sqlite3.connect(COUNTRIES)

print(conn.execute("SELECT * FROM region").fetchall())
conn.execute("DELETE FROM region WHERE region_id > 4")
print(conn.execute("SELECT * FROM region").fetchall())

conn.commit()
conn.close()
