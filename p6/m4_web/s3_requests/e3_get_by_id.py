"""
Python Course - Part 6

https://github.com/egalli64/pyco

Module 4 - Web

requests - get() by id
The web server for coders should be up
"""

import requests

for id in [2, 42]:
    try:
        print("Requesting coder with id", id)
        response = requests.get(f"http://127.0.0.1:5000/coders/{id}")
        print("Status code:", response.status_code)
        print("Coder:", response.json())
        print()
    except Exception as ex:
        print(ex)
