"""
Python Course - Part 4

https://github.com/egalli64/pyco

Module 5 - Oracle DB
"""

import oracledb
import db_config as db

connection = oracledb.connect(user=db.usr, password=db.pwd, dsn=db.dsn)

print("DB name:", connection.db_name)
print("DB version:", connection.version)
print("Oracledb module version:", oracledb.__version__)

connection.close()
