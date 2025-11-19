"""
Python Course - Part 4

https://github.com/egalli64/pyco

Module 5 - Oracle DB

requires pip install oracledb
"""

import os

usr = os.environ.get("ETL_USER")
if usr is None:
    usr = input("Enter user: ")

pwd = os.environ.get("ETL_PASSWORD")
if pwd is None:
    pwd = input("Enter password: ")

dsn = os.environ.get("ETL_DSN")
if dsn is None:
    dsn = input("Enter dsn: ")
