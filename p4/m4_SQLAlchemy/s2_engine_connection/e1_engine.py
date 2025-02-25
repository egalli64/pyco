"""
Python Course - Part 4

https://github.com/egalli64/pyco

Module 4 - SQLAlchemy

Create an Engine
"""

from sqlalchemy import create_engine

# in-memory vs persistent SQLite database
# DB_PATH = "sqlite:///p4/m4_SQLAlchemy/countries.db"
DB_PATH = "sqlite://"

engine = create_engine(DB_PATH)

print("The engine dialect:", engine.dialect.name)
print("The engine driver used:", engine.driver)
print("The connection URL:", engine.url)
