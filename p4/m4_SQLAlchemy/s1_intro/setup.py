"""
Python Course - Part 4

https://github.com/egalli64/pyco

Module 4 - SQLAlchemy

execute
"""

from sqlalchemy import create_engine, text

COUNTRIES = "sqlite:///p4/m4_SQLAlchemy/countries.db"
SCRIPT = "p4/m3_sqlite3/setup.sql"

engine = create_engine(COUNTRIES)

with open(SCRIPT, "r") as file:
    sql_script = file.read()

with engine.begin() as conn:
    for statement in sql_script.split(";"):
        if statement.strip():
            conn.execute(text(statement))

print("Database created successfully")
