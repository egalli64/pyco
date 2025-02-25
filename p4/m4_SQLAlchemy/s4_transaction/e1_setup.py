"""
Python Course - Part 4

https://github.com/egalli64/pyco

Module 4 - SQLAlchemy

Transaction - setup for examples, ensure no row has a PK > 4
"""

from sqlalchemy import create_engine, text

DB_PATH = "sqlite:///p4/m4_SQLAlchemy/countries.db"
engine = create_engine(DB_PATH)

with engine.begin() as conn:
    print(conn.execute(text("SELECT * FROM region")).fetchall())
    conn.execute(text("DELETE FROM region WHERE region_id > 4"))
    print(conn.execute(text("SELECT * FROM region")).fetchall())
