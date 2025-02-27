"""
Python Course - Part 6

https://github.com/egalli64/pyco

Module 4 - Web

requests - hello
The web server at the stated URL should be up
"""
import requests

try:
    response = requests.get("http://127.0.0.1:5000/")
    print(response.text)
except Exception as ex:
    print(ex)
