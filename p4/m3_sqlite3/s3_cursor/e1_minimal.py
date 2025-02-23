"""
Python Course - Part 4

https://github.com/egalli64/pyco

Module 3 - sqlite3

cursor - minimal approach, let Python to close connection and cursor at exit
"""

import sqlite3

COUNTRIES = "p4/m3_sqlite3/countries.db"

conn = sqlite3.connect(COUNTRIES)
cursor = conn.cursor()
print(f"Cursor opened on {COUNTRIES}")

cursor.execute("SELECT 1")

print("Done")
