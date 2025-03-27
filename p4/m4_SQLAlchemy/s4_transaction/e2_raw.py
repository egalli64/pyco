"""
Python Course - Part 4

https://github.com/egalli64/pyco

Module 4 - SQLAlchemy

Transaction in the explicit way
"""

from sqlalchemy import create_engine, text

DB_PATH = "sqlite:///p4/m4_SQLAlchemy/countries.db"
engine = create_engine(DB_PATH)

# implicit close the connection, explicit transaction management
with engine.connect() as conn:
    try:
        # start a transaction
        tx = conn.begin()

        # show the initial status
        print(conn.execute(text("SELECT * FROM region")).fetchall())

        # a change that requires a commit
        result = conn.execute(text("INSERT INTO region (name) values ('Antarctica')"))
        print(f"Inserted with PK {result.lastrowid}")

        # show the final status
        print(conn.execute(text("SELECT * FROM region")).fetchall())

        tx.commit()
    except:
        print(f"Insert of row with PK {result.lastrowid} rolled back!")
        tx.rollback()
