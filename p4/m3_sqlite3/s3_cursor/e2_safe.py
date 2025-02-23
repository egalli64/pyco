"""
Python Course - Part 4

https://github.com/egalli64/pyco

Module 3 - sqlite3

cursor
"""

import sqlite3

COUNTRIES = "p4/m3_sqlite3/countries.db"

conn = None
cursor = None

try:
    conn = sqlite3.connect(COUNTRIES)
    print("Connection opened in", conn)
    cursor = conn.cursor()
    print(f"Cursor opened in {cursor} on {COUNTRIES}")

    # now we can operate on the cursor
    cursor.execute("SELECT 1")
except sqlite3.Error as ex:
    print("SQLite Error:", ex)
except Exception as ex:
    print("Something went wrong:", ex)
finally:
    if cursor:
        cursor.close()
        print(f"Now cursor {cursor} is closed")
    if conn:
        conn.close()
        print(f"Now connection {conn} is closed")

try:
    print("Using a closed cursor leads to trouble ...")
    cursor.execute("SELECT 2")
except sqlite3.ProgrammingError as ex:
    print(ex)
