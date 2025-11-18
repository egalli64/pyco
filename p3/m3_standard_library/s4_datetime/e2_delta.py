"""
Python Course - Part 3

https://github.com/egalli64/pyco

Module 3 - Python Standard Library

datetime
"""

from datetime import datetime, date, time, timedelta


delta = timedelta(days=3, hours=2)
print(delta)
print(delta.days, delta.seconds, delta.microseconds)

dt = datetime(2025, 12, 31, 14, 30)
print(dt)
future_datetime = dt + delta
print(dt, future_datetime)
