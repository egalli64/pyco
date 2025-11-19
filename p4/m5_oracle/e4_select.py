"""
Python Course - Part 4

https://github.com/egalli64/pyco

Module 5 - Oracle DB
"""

import oracledb
import db_config as db

connection = oracledb.connect(user=db.usr, password=db.pwd, dsn=db.dsn)
cursor = connection.cursor()

cursor.execute("select * from test_py")

# rows = cursor.fetchall()
# for row in rows:
#     print(row)

for row in cursor:
    print(row)

cursor.close()
connection.close()
