"""
Python Course - Part 3

https://github.com/egalli64/pyco

Module 3 - Python Standard Library

datetime: datetime, date, time
"""

from datetime import datetime, date, time

d = date(2025, 12, 31)
print(d)

t = time(14, 30, 0)
print(t)

dt = datetime(2025, 12, 31, 14, 30)
print(dt)
print(dt.strftime("%Y %m %d, %H:%M"))

dt = datetime.strptime("2025-12-31", "%Y-%m-%d")
print(dt)
print(dt.date())
print(dt.time())

print(d.day, d.month, d.year)
print(t.hour, t.hour, t.min, t.second, t.microsecond)
