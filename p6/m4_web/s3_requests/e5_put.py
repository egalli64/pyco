"""
Python Course - Part 6

https://github.com/egalli64/pyco

Module 4 - Web

requests - put()
The web server for coders should be up
"""

import requests

coder = {"name": "Cho", "lang": "Clojure"}

# 2 is expected to succeed, 42 is expected to fail (I don't fallback to post in this example)
for id in [2, 42]:
    try:
        print("Put coder with id", id)
        response = requests.put(f"http://127.0.0.1:5000/coders/{id}", json=coder)
        print("Status code:", response.status_code)
        print("Coder:", response.json())
        print()
    except Exception as ex:
        print(ex)

# expected to fail, since name is missing
uncomplete = {"lang": "Zig"}
try:
    print("Put coder with missing name")
    response = requests.put("http://127.0.0.1:5000/coders/2", json=uncomplete)
    print("Status code:", response.status_code)
    print("Coder:", response.json())
    print()
except Exception as ex:
    print(ex)
