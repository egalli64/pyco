"""
Python Course - Part 4

https://github.com/egalli64/pyco

Module 4 - SQLAlchemy

(Can't) get a Connection (safe)
"""

from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError

# good path, step 5 would fail (can't execute on a closed connection)
DB_PATH = "sqlite://"
# bad path, step 2 would file (can't find the database)
# DB_PATH = "sqlite:///p4/missing/countries.db"

# 1. create an engine
engine = create_engine(DB_PATH)

try:
    # 2. try get a connection in a context manager
    print("Try to connect ...")
    with engine.connect() as conn:
        # 3. use the connection
        print("Can execute:", conn.execute(text("SELECT 3")).fetchone()[0])

    # 4. the context manager closes the connection
    # 5. now the connection is closed
    conn.execute(text("SELECT 5"))

except SQLAlchemyError as ex:
    print(f"Can't connect to {DB_PATH}:", ex)
except Exception as ex:
    print(f"Unexpected error while connecting to {DB_PATH}:", ex)
