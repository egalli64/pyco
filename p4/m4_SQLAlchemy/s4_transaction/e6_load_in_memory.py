"""
Python Course - Part 4

https://github.com/egalli64/pyco

Module 4 - SQLAlchemy

From source (persistent) to destination (in-memory)
"""

from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError

DB_SRC = "sqlite:///p4/m4_SQLAlchemy/countries.db"
DB_DEST = "sqlite://"
CREATE_TABLE_REGION = """
    create table region (
        region_id integer primary key,
        name varchar(25)
    )
    """

engine_src = create_engine(DB_SRC)
engine_dest = create_engine(DB_DEST)


def load_region():
    """Load the region table in-memory"""
    with engine_src.begin() as conn_src, engine_dest.begin() as conn_dest:
        # 1. extract from source
        result = conn_src.execute(text("select * from region")).fetchall()
        print("Read from source:", result)

        # 2. load in memory
        conn_dest.execute(text(CREATE_TABLE_REGION))
        for row in result:
            conn_dest.execute(
                text("INSERT INTO region (region_id, name) values (:id, :name)"),
                {"id": row[0], "name": row[1]},
            )
        result = conn_dest.execute(text("select * from region")).fetchall()
        print("Read from destination:", result)


if __name__ == "__main__":
    try:
        load_region()
    except SQLAlchemyError as e:
        print("Error loading data into memory database:", e)
    except Exception as e:
        print("An unexpected error occurred:", e)
