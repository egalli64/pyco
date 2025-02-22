"""
Python Course - Part 4

https://github.com/egalli64/pyco

Module 3 - sqlite3

executescript
"""

import sqlite3

COUNTRIES = "p4/m3_sqlite3/countries.db"
SCRIPT = "p4/m3_sqlite3/setup.sql"

with sqlite3.connect(COUNTRIES) as conn:
    with open(SCRIPT, "r") as file:
        setup = file.read()
    conn.cursor().executescript(setup)

print("Database created successfully")
