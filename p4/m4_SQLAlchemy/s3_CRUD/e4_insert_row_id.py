"""
Python Course - Part 4

https://github.com/egalli64/pyco

Module 4 - SQLAlchemy

CRUD: create by insert (no autoincrement PK), lastrowid shows ROWID
"""

from sqlalchemy import create_engine, text

# 1. initialization
DB_PATH = "sqlite:///p4/m4_SQLAlchemy/countries.db"
engine = create_engine(DB_PATH)
conn = engine.connect()

# simulating parameters passed in
pk = "XX"
name = "Unknown"
fk = 1

# 2. execute queries
result = conn.execute(
    text("INSERT INTO country (country_id, name, region_id) values (:pk, :name, :fk)"),
    {"pk": pk, "name": name, "fk": fk},
)
print(f"Insert: last row id {result.lastrowid}, row count {result.rowcount}")

result = conn.execute(text("SELECT * FROM country WHERE region_id = :fk"), {"fk": fk})

# 3. verify result
print(result.fetchall())

# 4. closing - no commit, the insertion will be lost!
conn.close()
