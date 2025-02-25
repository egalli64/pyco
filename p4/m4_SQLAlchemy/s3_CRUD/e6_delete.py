"""
Python Course - Part 4

https://github.com/egalli64/pyco

Module 4 - SQLAlchemy

CRUD: delete
"""

from sqlalchemy import create_engine, text

# 1. initialization
DB_PATH = "sqlite:///p4/m4_SQLAlchemy/countries.db"
engine = create_engine(DB_PATH)
conn = engine.connect()

# simulating the parameter passed in
id = 3

# 2. execute queries
query = text("DELETE from country WHERE region_id = :id")
result = conn.execute(query, {"id": id})
print("Delete: row count", result.rowcount)

query = text("SELECT * FROM country WHERE country_id = :id")
result = conn.execute(query, {"id": id})

# 3. verify result
print(result.fetchall())

# 4. closing - no commit, the delete will be lost!
conn.close()
