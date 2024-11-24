from flask import Flask

app = Flask(__name__)

@app.route("/")
def welcome():
    return "Welcome to Flask"

@app.route("/fun2")
def home():
    return "Welcome to home page"

from Controller import *