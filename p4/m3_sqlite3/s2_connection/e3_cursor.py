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
    print("Open connection")
    conn = sqlite3.connect(COUNTRIES)
    print("Open cursor")
    cursor = conn.cursor()
    print("Cursor open on", COUNTRIES)
except sqlite3.Error as ex:
    print("SQLite Error:", ex)
except Exception as ex:
    print("Something went wrong:", ex)
finally:
    if cursor:
        print("Close cursor")
        cursor.close()
    if conn:
        print("Close connection")
        conn.close()

try:
    print("Using a closed cursor leads to trouble ...")
    cursor.execute("SELECT 1")
except sqlite3.ProgrammingError as ex:
    print(ex)
