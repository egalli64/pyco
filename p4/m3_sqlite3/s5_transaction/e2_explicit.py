"""
Python Course - Part 4

https://github.com/egalli64/pyco

Module 3 - sqlite3

Transaction - explicit
"""

import sqlite3

COUNTRIES = "p4/m3_sqlite3/countries.db"
conn = sqlite3.connect(COUNTRIES)

if conn.isolation_level == "" or conn.isolation_level == "DEFERRED":
    print("Transactions are in the default mode")

cursor = conn.cursor()
# explicit start a transaction
try:
    cursor.execute("BEGIN TRANSACTION")
    cursor.execute("INSERT INTO region (name) values ('Antarctica')")
    if cursor.rowcount != 1:
        print(f"Unexpected! {cursor.rowcount} rows inserted")
    else:
        print(f"New row has PK", cursor.lastrowid, end=", ")
        cursor.execute("SELECT * FROM region WHERE region_id = ?", (cursor.lastrowid,))
        print("the full row is", cursor.fetchone())

    # commit must be explicit
    conn.commit()
except Exception as ex:
    print("Rollback on exception:", ex)
    # rollback must be explicit
    conn.rollback()

cursor.close()
conn.close()
