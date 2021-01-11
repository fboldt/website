from flask import Flask, redirect
app = Flask(__name__)

@app.route('/')
def index():
    return redirect("/hello")

@app.route("/hello")
def hello_world():
    return 'Hello, Heroku!'
