#! /usr/bin/python

from flask import Flask, request, make_response, redirect
from flask.ext.script import Manager

app = Flask(__name__)
manager = Manager(app)

@app.route("/")
def index():
    user_agent = request.headers.get("User-Agent")
    response = make_response("<p>Your browser is {}</p>".format(user_agent))
    response.set_cookie("answer", "41+1")
    return response

@app.route("/togoogle")
def to_google():
    return redirect("http://www.google.com")

@app.route("/togoogle2")
def to_google_manual():
    return "", 302, {"Location": "http://www.google.com"}

def main():
    manager.run()

if __name__ == "__main__":
    main()
