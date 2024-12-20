"""
Python Course - Part 5

https://github.com/egalli64/pyco

Module 2 - String

F-string formatting - datetime
"""

from datetime import datetime

dt = datetime.now()

print("Current datetime:", dt)

print(f"Today: {dt:%d %m %Y}")
print(f"Current time: {dt:%H %M %S}")
