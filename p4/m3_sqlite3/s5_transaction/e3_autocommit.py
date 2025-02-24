"""
Python Course - Part 4

https://github.com/egalli64/pyco

Module 3 - sqlite3

Transaction - isolation level to autocommit
"""

import sqlite3

COUNTRIES = "p4/m3_sqlite3/countries.db"
conn = sqlite3.connect(COUNTRIES)
print("Isolation level by default is an empty string:", conn.isolation_level == "")

# enter in autocommit mode
conn.isolation_level = None
print("Isolation level for autocommit:", conn.isolation_level)

# work on the execution context
cursor = conn.cursor()
cursor.execute("INSERT INTO region (name) values ('Antarctica')")
if cursor.rowcount != 1:
    print(f"Unexpected! {cursor.rowcount} rows inserted!")
else:
    print(f"New row has PK", cursor.lastrowid, end=", ")
    cursor.execute("SELECT * FROM region WHERE region_id = ?", (cursor.lastrowid,))
    print("the full row is", cursor.fetchone())

# no need for commit, just close
cursor.close()
conn.close()
