#! /usr/bin/env python

from flask import Flask
from flask.ext.script import Manager

app = Flask(__name__)
manager = Manager(app)

@app.route("/")
def index():
    return "<h1>Hello <b>World</b>!</h1>"

@app.route("/user/<name>")
def user(name):
    return "<h1>Hello <b>{0}</b></h1>".format(name)

@app.route("/user/id/<int:id>")
def user_id(id):
    return "<h1>ID = {0}</h1>".format(id)

@app.route("/user/balance/<float:balance>")
def user_balance(balance):
    return "<h1>balance = {0}</h1>".format(balance)

@app.route("/user/path/<path:path>/foo")
def user_path(path):
    return "{0}".format(path)

def main():
    manager.run()

if __name__ == "__main__":
    main()
