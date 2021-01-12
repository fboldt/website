from flask import Flask, redirect, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return redirect("/hello")

@app.route("/disciplinas")
def disciplinas():
    return render_template("disciplinas.html")

@app.route("/hello")
def hello_world():
    return render_template("hello.html")
