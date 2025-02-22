"""
Python Course - Part 4

https://github.com/egalli64/pyco

Module 3 - RDB

sqlite3 - exception on connect
"""

import sqlite3

for path in ["p4/missing/countries.db", 42]:
    try:
        print("Trying to connect to", path)
        # implicit close() on conn
        with sqlite3.connect(path) as conn:
            pass
    except sqlite3.Error as ex:
        print("SQLite Error:", ex)
    except Exception as ex:
        print("Something went wrong:", ex)
