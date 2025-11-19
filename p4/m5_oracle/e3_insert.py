"""
Python Course - Part 4

https://github.com/egalli64/pyco

Module 5 - Oracle DB
"""

import oracledb
import db_config as db

connection = oracledb.connect(user=db.usr, password=db.pwd, dsn=db.dsn)
cursor = connection.cursor()

cursor.execute(
    "INSERT INTO test_py (name, salary) VALUES (:name, :salary)",
    {"name": "Alice", "salary": 50_000},
)
connection.commit()

cursor.close()
connection.close()
