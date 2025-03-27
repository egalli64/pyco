"""
Python Course - Part 4

https://github.com/egalli64/pyco

Module 4 - SQLAlchemy

Transaction: catch AND automatic rollback by re-raise
"""

from sqlalchemy import create_engine, text

DB_PATH = "sqlite:///p4/m4_SQLAlchemy/countries.db"
engine = create_engine(DB_PATH)


def insert_region(name):
    """Insert a region with the passed name or throw an exception"""
    with engine.begin() as conn:
        try:
            sql = text("INSERT INTO region (name) values (:name)")
            result = conn.execute(sql, {"name": name})
            print(f"Inserted with id {result.lastrowid}")
            conn.execute(text("MISTAKE"))
        except Exception as ex:
            print(ex)
            raise


if __name__ == "__main__":
    try:
        insert_region("Antarctica")
    except:
        print("Can't insert the new region")

    print(engine.connect().execute(text("SELECT * FROM region")).fetchall())
