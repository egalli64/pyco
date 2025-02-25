"""
Python Course - Part 4

https://github.com/egalli64/pyco

Module 4 - SQLAlchemy

CRUD: update
"""

from sqlalchemy import create_engine, text

# 1. initialization
DB_PATH = "sqlite:///p4/m4_SQLAlchemy/countries.db"
engine = create_engine(DB_PATH)
conn = engine.connect()

# simulating parameters passed in
prev = 4
new = 1

# 2. execute queries
query = text("UPDATE country SET region_id = :new WHERE region_id = :prev")
result = conn.execute(query, {"prev": prev, "new": new})
print("Update: row count", result.rowcount)

query = text("SELECT * FROM country WHERE region_id = :new")
result = conn.execute(query, {"new": new})

# 3. verify result
print(result.fetchall())

# 4. closing - no commit, the update will be lost!
conn.close()
