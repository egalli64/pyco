"""
Python Course - Part 6

https://github.com/egalli64/pyco

Module 4 - Web

requests - get() text
The web server for coders should be up
"""

import requests

try:
    response = requests.get("http://127.0.0.1:5000/")
    print("Status code:", response.status_code)
    print("Headers:", response.headers)
    print("Text body is:", response.text)
except Exception as ex:
    print(ex)
