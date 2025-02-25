"""
Python Course - Part 4

https://github.com/egalli64/pyco

Module 4 - SQLAlchemy

Transaction: autocommit
"""

from sqlalchemy import create_engine, text

DB_PATH = "sqlite:///p4/m4_SQLAlchemy/countries.db"
engine = create_engine(DB_PATH)
conn = engine.connect()

try:
    conn.execution_options(isolation_level="AUTOCOMMIT")

    print(conn.execute(text("SELECT * FROM region")).fetchall())

    result = conn.execute(text("INSERT INTO region (name) values ('Antarctica')"))
    print(f"Inserted with PK {result.lastrowid}")

    print(conn.execute(text("SELECT * FROM region")).fetchall())
except:
    print("No rollback, each statement has been executed in its own transaction")

conn.close()
