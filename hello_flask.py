#! /usr/bin/env python

from flask import Flask
from flask import render_template
from flask.ext.script import Manager

app = Flask(__name__)
manager = Manager(app)

class Templates:
    index = "index.html"

@app.route("/")
@app.route("/index")
def index():
    return render_template(Templates.index)

@app.route("/user/<name>")
def user(name):
    user = {"nickname" : name}
    posts = [{
            "author": {"nickname": "John"},
            "body": "Pshooo! Flask is great!"},
            {"author": {"nickname": "Susan"},
            "body": "PShooPshoo!"}]
    return render_template(Templates.index,
            title="Home",
            user=user,
            posts=posts)


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
