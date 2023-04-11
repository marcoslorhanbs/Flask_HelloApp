from flask import Flask
from markupsafe import escape

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello World!</p>"

@app.route("/InjectPrevent/<name>")
def hello(name):
    return f"Hello, {escape(name)}"

@app.route("/projects/")
def projects():
    return "The Project Page"

@app.route("/about")
def about():
    return "The About Page"