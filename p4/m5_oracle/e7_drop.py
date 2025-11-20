"""
Python Course - Part 4

https://github.com/egalli64/pyco

Module 5 - Oracle DB
"""

import oracledb
import db_config as db

connection = oracledb.connect(user=db.usr, password=db.pwd, dsn=db.dsn)
cursor = connection.cursor()

cursor.execute("DROP TABLE test_py")

cursor.close()
connection.close()
