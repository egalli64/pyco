"""
Python Course - Part 4

https://github.com/egalli64/pyco

Module 3 - sqlite3

check exception on connect
"""

import sqlite3

for path in ["p4/missing/countries.db", "p4/m3_sqlite3/countries.db", 42]:
    conn = None
    try:
        print("Trying to connect to", path)
        conn = sqlite3.connect(path)
        print("Connected to", path)
    except sqlite3.Error as ex:
        print("SQLite Error:", ex)
    except Exception as ex:
        print("Something went wrong:", ex)
    finally:
        if conn:
            print("Closing connection to", path)
            conn.close()
