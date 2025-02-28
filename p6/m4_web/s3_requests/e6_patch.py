"""
Python Course - Part 6

https://github.com/egalli64/pyco

Module 4 - Web

requests - patch()
The web server for coders should be up
"""

import requests

coder = {"lang": "Pascal"}

# 2 is expected to succeed, 42 is expected to fail
for id in [1, 42]:
    try:
        print("Patch coder with id", id)
        response = requests.patch(f"http://127.0.0.1:5000/coders/{id}", json=coder)
        print("Status code:", response.status_code)
        print("Coder:", response.json())
        print()
    except Exception as ex:
        print(ex)

# patching with an empty dictionary is expected to succeed
try:
    print("Patch coder without patching anything")
    response = requests.patch("http://127.0.0.1:5000/coders/2", json={})
    print("Status code:", response.status_code)
    print("Coder:", response.json())
    print()
except Exception as ex:
    print(ex)
