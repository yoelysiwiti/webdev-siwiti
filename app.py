from flask import Flask

app = Flask(__name__)

@app.route("/")

def message_add():
    return "This is mesage python, removed print above"

def home():
    message_add()