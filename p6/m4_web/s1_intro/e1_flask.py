"""
Python Course - Part 6

https://github.com/egalli64/pyco

Module 4 - Web

Flask - A minimal web server
Run it as normal Python script: python <script>.py
 or on Flask CLI: flask --app <script> run
"""

from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


if __name__ == "__main__":
    app.run(debug=True)
