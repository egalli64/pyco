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
    "UPDATE test_py SET salary = :salary WHERE name = :name",
    {"name": "Alice", "salary": 60_000}
)
connection.commit()

cursor.close()
connection.close()
