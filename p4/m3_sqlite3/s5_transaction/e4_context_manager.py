"""
Python Course - Part 4

https://github.com/egalli64/pyco

Module 3 - sqlite3

Transaction - context manager
"""

import sqlite3

COUNTRIES = "p4/m3_sqlite3/countries.db"
conn = sqlite3.connect(COUNTRIES)
cursor = conn.cursor()

# the context manager on the connection ensure committing the transaction
with conn:
    try:
        cursor.execute("INSERT INTO region (name) values ('Antarctica')")
        if cursor.rowcount != 1:
            print(f"Unexpected! {cursor.rowcount} rows inserted!")
        else:
            print(f"New row has PK", cursor.lastrowid, end=", ")
            cursor.execute(
                "SELECT * FROM region WHERE region_id = ?", (cursor.lastrowid,)
            )
            print("the full row is", cursor.fetchone())

    except Exception as ex:
        # catching the exception gives the resposibility to rollback the transaction!
        print("Rollback caused by:", ex)
        conn.rollback()

cursor.close()
conn.close()
