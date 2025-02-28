"""
Python Course - Part 6

https://github.com/egalli64/pyco

Module 4 - Web

requests - post()
The web server for coders should be up
"""

import requests

coder = {"name": "Jim", "lang": "Java"}

try:
    response = requests.post("http://127.0.0.1:5000/coders", json=coder)
    print("Status code:", response.status_code)
    print("Coder:", response.json())
except Exception as ex:
    print(ex)
