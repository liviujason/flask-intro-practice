from flask import Flask

app = Flask(__name__)


@app.route('/welcome')
def welcome():
    return "Welcome"


@app.route('/welcome/home')
def welcome():
    return "Welcome home"


@app.route('/welcome/back')
def welcome():
    return "Welcome back"
