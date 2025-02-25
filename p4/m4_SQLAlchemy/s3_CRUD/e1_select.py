"""
Python Course - Part 4

https://github.com/egalli64/pyco

Module 4 - SQLAlchemy

CRUD: read by select
"""

from sqlalchemy import create_engine, text

# 1. initialization
DB_PATH = "sqlite:///p4/m4_SQLAlchemy/countries.db"

engine = create_engine(DB_PATH)
conn = engine.connect()

# 2. execute query
result = conn.execute(text("SELECT * FROM country"))

# 3. use the result

print("Column names:", result.keys())

print("First row:", result.fetchone())
print("Next 5 rows:", result.fetchmany(5))
print("All the other rows:", result.fetchall())
print("Now the result has been exahusted:", result.fetchone())

# 2/2. execute another query
result = conn.execute(text("SELECT * FROM region"))

# 3/2. looping on the result
print("All regions in the table:")
for row in result:
    print(row)

# 4. closing
conn.close()
