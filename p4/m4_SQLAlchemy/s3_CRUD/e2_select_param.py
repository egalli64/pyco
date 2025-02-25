"""
Python Course - Part 4

https://github.com/egalli64/pyco

Module 4 - SQLAlchemy

CRUD: read by parametrized select
"""

from sqlalchemy import create_engine, text

# 1. initialization
DB_PATH = "sqlite:///p4/m4_SQLAlchemy/countries.db"
engine = create_engine(DB_PATH)
conn = engine.connect()

for id in range(1, 5):
    print("Region", id, end=": ")
    # 2. execute query
    result = conn.execute(
        text("SELECT * FROM country WHERE region_id = :id"), {"id": id}
    )
    # 3. use the result
    for row in result.fetchall():
        print(row[1], end=" ")
    print()

# 4. closing
conn.close()
