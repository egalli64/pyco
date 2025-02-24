"""
Python Course - Part 4

https://github.com/egalli64/pyco

Module 4 - SQLAlchemy

Get a Connection (raw)
"""

from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError

# 1. create an engine
engine = create_engine("sqlite://")

# 2. get a connection
conn = engine.connect()

# 3. use the connection
print("Can execute:", conn.execute(text("SELECT 3")).fetchone()[0])

# 4. close the connection
conn.close()

# 5. now the connection is closed
try:
    conn.execute(text("SELECT 5"))
except SQLAlchemyError as ex:
    print("Can't execute:", ex)
