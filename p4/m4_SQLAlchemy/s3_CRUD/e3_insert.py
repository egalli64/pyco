"""
Python Course - Part 4

https://github.com/egalli64/pyco

Module 4 - SQLAlchemy

CRUD: create by insert (autoincrement PK), lastrowid shows PK
"""

from sqlalchemy import create_engine, text

# 1. initialization
DB_PATH = "sqlite:///p4/m4_SQLAlchemy/countries.db"
engine = create_engine(DB_PATH)
conn = engine.connect()

# simulating a parameter passed in
name = "Antarctica"

# 2. execute queries
result = conn.execute(text("INSERT INTO region (name) values (:name)"), {"name": name})
print(f"Insert: last row id {result.lastrowid}, row count {result.rowcount}")

result = conn.execute(text("SELECT * FROM region"))

# 3. verify result
print(result.fetchall())

# 4. closing - no commit, the insertion will be lost!
conn.close()
