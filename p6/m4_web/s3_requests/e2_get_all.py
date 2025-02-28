"""
Python Course - Part 6

https://github.com/egalli64/pyco

Module 4 - Web

requests - get() all the coders
The web server for coders should be up
"""

import requests

try:
    response = requests.get("http://127.0.0.1:5000/coders")
    print("All coders:", response.json())
except Exception as ex:
    print(ex)
