"""
Python Course - Part 3

https://github.com/egalli64/pyco

Module 3 - Python Standard Library

datetime: datetime, date, time
"""

from datetime import datetime, date, time

d = date(2025, 12, 31)
print("A date:", d)

t = time(14, 30, 0)
print("A time:", t)

dt = datetime(2025, 12, 31, 14, 30)
print("A datetime:", dt)
print("Formatting a datetime in a custom way:", dt.strftime("%Y %m %d, %H:%M"))

dt = datetime.strptime("2026-01-01", "%Y-%m-%d")
print("A datetime extracted from a string:", dt)
print("Extracting the date from a datetime:", dt.date())
print("Extracting the time from a datetime:", dt.time())

print("Extracting components from a date:", d.day, d.month, d.year)
print("... and from a time:", t.hour, t.minute, t.second, t.microsecond)
