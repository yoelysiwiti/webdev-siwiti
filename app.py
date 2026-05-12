from flask import Flask

app = Flask(__name__)

print("Siwiti, this is app.py")

@app.route("/")

def message_add():
    return "This is mesage python"

def home():
    message_add()