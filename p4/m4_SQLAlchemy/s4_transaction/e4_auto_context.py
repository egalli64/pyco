"""
Python Course - Part 4

https://github.com/egalli64/pyco

Module 4 - SQLAlchemy

Transaction: automatized by Engine.begin() + context manager
"""

from sqlalchemy import create_engine, text

DB_PATH = "sqlite:///p4/m4_SQLAlchemy/countries.db"
engine = create_engine(DB_PATH)

with engine.begin() as conn:
    # show the initial status
    print(conn.execute(text("SELECT * FROM region")).fetchall())

    # a change that requires a commit
    result = conn.execute(text("INSERT INTO region (name) values ('Antarctica')"))
    print(f"Insert: last row id {result.lastrowid}, row count {result.rowcount}")

    # show the final status
    print(conn.execute(text("SELECT * FROM region")).fetchall())

# no need to close, commit, rollback
