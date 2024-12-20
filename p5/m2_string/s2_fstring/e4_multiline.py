"""
Python Course - Part 5

https://github.com/egalli64/pyco

Module 2 - String

F-string formatting - multiline
"""

from datetime import datetime

dt = datetime.now()

print(
    f"""
Current datetime: {dt}
Today: {dt:%d %m %Y}
Current time: {dt:%H %M %S}
"""
)
