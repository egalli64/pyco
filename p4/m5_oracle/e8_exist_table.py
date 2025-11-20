"""
Python Course - Part 4

https://github.com/egalli64/pyco

Module 5 - Oracle DB
"""

import oracledb
import db_config as db

connection = oracledb.connect(user=db.usr, password=db.pwd, dsn=db.dsn)
cursor = connection.cursor()

cursor.execute("SELECT table_name FROM user_tables WHERE table_name = :name", {"name": "TEST_PY"})
print(cursor.fetchone())

cursor.close()
connection.close()
